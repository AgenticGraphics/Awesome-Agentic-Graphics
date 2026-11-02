"""Opt-in BVB transport retaining returned Responses items and assistant phases.

No reference answers or Codex instructions are supplied. Opaque reasoning items
are replayed only when encrypted content is actually returned by the provider.
"""
import hashlib,json,os,sys,uuid
from pathlib import Path
import httpx
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
import litellm
from runtime_config import api_base, api_key
for parent in Path(__file__).resolve().parents:
    vendor=parent/'third_party'
    if vendor.is_dir():sys.path.insert(0,str(vendor));break
from bvb_sandbox.models import Model,_manual_cost


def normalize_output(output):
    """Retain messages/reasoning; disclose only observed empty failed image markers.

    Some proxies insert a failed image-generation marker without any payload.
    It is not a tool request or a result. Never dispatch or replay it, and never
    silently accept a real native call, a payload, or an unfinished call.
    """
    retained=[];omitted=[]
    for item in output:
        if item.get('type') in ('message','reasoning'):
            retained.append(item)
        elif (item.get('type')=='image_generation_call' and item.get('status')=='failed'
              and isinstance(item.get('id'),str) and item['id']
              and set(item)=={'id','type','status'}):
            omitted.append(item)
        else:
            raise ValueError('Unexpected native tool output: '+str(item.get('type'))+
                             '; this adapter uses the BVB fenced-tool dispatcher')
    return retained,omitted


def usage_cost(model,usage):
    it=int(usage.get('input_tokens') or 0);ot=int(usage.get('output_tokens') or 0)
    normalized={'model':model,'usage':{'prompt_tokens':it,'completion_tokens':ot,
        'total_tokens':usage.get('total_tokens',it+ot),
        'prompt_tokens_details':usage.get('input_tokens_details',{}),
        'completion_tokens_details':usage.get('output_tokens_details',{})},
        'choices':[{'index':0,'message':{'role':'assistant','content':''},'finish_reason':'stop'}]}
    uncached=_manual_cost(model,it,ot)
    if os.environ.get('INPUT_COST_PER_MILLION') or os.environ.get('OUTPUT_COST_PER_MILLION'):
        return uncached,'configured_uncached_rates',uncached
    try:cost=float(litellm.completion_cost(completion_response=normalized) or 0)
    except Exception:cost=0
    if cost==0 and (it or ot):return uncached,'manual_uncached_fallback',uncached
    return cost,'litellm_cache_aware_usage',uncached


def digest(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()


class ResponsesModel(Model):
    def __init__(self,*args,state_path=None,**kwargs):
        super().__init__(*args,**kwargs)
        state_path=state_path or os.environ.get('BVB_RESPONSES_STATE')
        self.state_path=Path(state_path) if state_path else None
        self.state=json.loads(self.state_path.read_text()) if self.state_path and self.state_path.exists() else {'version':4,'model':self.model,'reasoning':self.reasoning,'responses':{}}
        if self.state.get('version')!=4 or self.state.get('model')!=self.model or self.state.get('reasoning')!=self.reasoning:
            raise ValueError('Responses state belongs to different model, reasoning, or adapter version')

    def persist(self):
        if not self.state_path:return
        self.state_path.parent.mkdir(parents=True,exist_ok=True)
        temporary=self.state_path.with_name(self.state_path.name+'.'+uuid.uuid4().hex+'.tmp')
        descriptor=os.open(temporary,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(descriptor,'w') as stream:
            json.dump(self.state,stream,ensure_ascii=False);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary,self.state_path)

    def archive_response(self,data):
        """Preserve provider anomalies and usage before validation, without secrets."""
        if not self.state_path:return None
        directory=self.state_path.parent/'provider-responses';directory.mkdir(parents=True,exist_ok=True)
        path=directory/(uuid.uuid4().hex+'.json')
        descriptor=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
        with os.fdopen(descriptor,'w') as stream:
            json.dump(data,stream,ensure_ascii=False);stream.flush();os.fsync(stream.fileno())
        return str(path)

    @staticmethod
    def content(parts):
        if all(p['kind']=='text' for p in parts):return '\n'.join(p['text'] for p in parts)
        result=[]
        for p in parts:
            if p['kind']=='text':result.append({'type':'input_text','text':p['text']})
            elif p['kind']=='image':result.append({'type':'input_image','image_url':f"data:{p['media_type']};base64,{p['data']}"})
            else:raise ValueError('Unsupported BVB message part: '+str(p['kind']))
        return result

    def complete(self,system,messages):
        system_hash=digest(system)
        if self.state.get('system_sha256') not in (None,system_hash):raise ValueError('Cannot reuse Responses state with changed system instructions')
        signature=digest({'system':system,'messages':messages})
        cached=self.state.get('unconsumed_response',{})
        if cached.get('request_sha256')==signature:
            return cached['reply'],{**cached['info'],'reused_unconsumed_response':True}
        items=[{'role':'system','content':system}]
        for index,message in enumerate(messages):
            content=self.content(message['parts'])
            saved=self.state['responses'].get(str(index))
            if message['role']=='assistant' and saved:
                if saved['reply_sha256']!=digest(content):raise ValueError('Assistant history changed; refusing mismatched reasoning replay')
                items.extend(saved['output_items'])
            else:items.append({'role':message['role'],'content':content})
        # Keep the original fenced-tool protocol rather than native tool dispatch.
        body={'model':self.model,'input':items,'store':False,'stream':False,
              'include':['reasoning.encrypted_content']}
        if self.reasoning:body['reasoning']={'effort':self.reasoning}
        with httpx.Client(timeout=self.timeout) as client:
            response=client.post(api_base()+'/responses',json=body,
                                 headers={'Authorization':'Bearer '+api_key()})
        response.raise_for_status();data=response.json()
        raw_path=self.archive_response(data)
        if data.get('error'):raise RuntimeError('Responses provider error: '+str(data['error'].get('code','unspecified')))
        if data.get('status') not in (None,'completed'):raise RuntimeError('Responses output not completed: '+str(data.get('status')))
        output,omitted_markers=normalize_output(data.get('output',[]))
        text='\n'.join(part.get('text','') for item in output if item.get('type')=='message'
                       for part in item.get('content',[]) if part.get('type')=='output_text')
        if not text:raise RuntimeError('Responses provider returned no assistant text')
        replay=[item for item in output if item.get('type')=='message' or item.get('encrypted_content')]
        encrypted=sum(item.get('type')=='reasoning' and bool(item.get('encrypted_content')) for item in output)
        omitted=sum(item.get('type')=='reasoning' and not item.get('encrypted_content') for item in output)
        usage=data.get('usage') or {};it=int(usage.get('input_tokens') or 0);ot=int(usage.get('output_tokens') or 0)
        cost,cost_basis,uncached=usage_cost(self.model,usage)
        info={'cost':cost,'cost_estimate_basis':cost_basis,'uncached_cost_estimate_usd':uncached,'input_tokens':it,'output_tokens':ot,
              'transport':'responses-items-v4','response_id':data.get('id'),'raw_usage':usage,
              'provider_response_path':raw_path,'native_calls_dispatched_by_adapter':False,
              'omitted_empty_failed_image_markers':omitted_markers,
              'encrypted_reasoning_items':encrypted,'reasoning_items_without_replayable_content':omitted,
              'assistant_phases':[item.get('phase') for item in output if item.get('type')=='message']}
        self.state['responses'][str(len(messages))]={'reply_sha256':digest(text),'output_items':replay}
        self.state['system_sha256']=system_hash
        self.state['unconsumed_response']={'request_sha256':signature,'reply':text,'info':info}
        self.persist()
        return text,info
