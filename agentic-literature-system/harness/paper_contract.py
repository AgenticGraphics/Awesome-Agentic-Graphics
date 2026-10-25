"""Machine-readable paper contract; does not supply or infer paper decisions."""
def build_paper_schema(codebook):
    string={'type':'string'}
    evidence={'type':'object','properties':{
        'primary_url':string,'locator':string,'evidence':string,
        'level':{'type':'string','enum':['reported','derived']},
        'reasoning':{'type':'string','description':'Required when level is derived.'}},
        'required':['primary_url','locator','evidence','level'],'additionalProperties':True}
    fields=codebook['fields']
    properties={
        'canonical_title':string,
        'canonical_urls':{'type':'array','items':string,'minItems':1},
        'identifiers':{'type':'object','properties':{'arxiv':string,'doi':string,'openreview':string},'additionalProperties':True},
        'authors':{'type':'array','items':string},
        'abstract':string,
        'events':{'type':'array','items':{'type':'object','additionalProperties':True}},
        'source_records':{'type':'array','items':{'type':'object','additionalProperties':True}},
        'screening_status':{'type':'string','enum':['core','enabling_or_adjacent','scope_dependent','excluded','unresolved']},
        'screening_reason':string,
        'screening_evidence':{'type':'array','items':{'anyOf':[string,{'type':'object','additionalProperties':True}]}},
        'application_families':{'type':'array','items':{'type':'string','enum':codebook['application_families']},'minItems':1,'uniqueItems':True},
        'operations':{'type':'array','items':{'type':'string','enum':codebook['operations']},'minItems':1,'uniqueItems':True},
        'taxonomy_cells':{'type':'object','properties':{
            key:{'type':'array','items':{'type':'string','enum':values+codebook['sentinels']},'minItems':1,'uniqueItems':True,
                 'description':'Use exact labels. A sentinel must appear alone, never mixed with concrete labels.'}
            for key,values in fields.items()},'required':list(fields),'additionalProperties':False},
        'field_evidence':{'type':'object','properties':{key:evidence for key in fields},'additionalProperties':False},
        'contribution':string,
        'limitations':{'type':'string','description':'A prose string, NOT an array of bullet strings.'},
        'taxonomy_delta':{'type':'array','items':{'anyOf':[string,{'type':'object','additionalProperties':True}]}},
        'confidence':{'type':'string','enum':['High','Medium','Low']},
    }
    required=list(properties)
    properties['analysis_target']={'type':'string','minLength':1,
        'description':'For retained papers, name the principal agentic subsystem and phase classified by these 18 fields. Distinguish task-time execution, data generation, training, and enabling components.'}
    properties['agent_graphics_relation']={'type':'object','properties':{
        key:{'type':'string','minLength':1} for key in
        ('controller','action_or_decision','graphics_target','primary_url','locator','evidence')},
        'required':['controller','action_or_decision','graphics_target','primary_url','locator','evidence','evidence_status'],
        'additionalProperties':True,
        'description':'Required for retained papers under graphics-action-borderline-v1. Describe the evidenced controller/action/graphics relation; state missing evidence explicitly for borderline work.'}
    properties['agent_graphics_relation']['properties']['evidence_status']={
        'type':'string','enum':['demonstrated','explicit_enabling','uncertain'],
        'description':'core requires demonstrated; enabling_or_adjacent requires explicit_enabling; scope_dependent requires uncertain. This is an evidence claim to review, not automatic truth certification.'}
    properties['full_text_reading']={'type':'object','properties':{
        'sha256':{'type':'string','pattern':'^[a-f0-9]{64}$'},
        'sections_reviewed':{'type':'array','items':string,'minItems':1}},
        'required':['sha256','sections_reviewed'],'additionalProperties':True,
        'description':'Required for core, enabling_or_adjacent, and scope_dependent papers; must match this run\'s PDF receipts.'}
    return {'type':'object','properties':properties,'required':required,'additionalProperties':True}

def contract_errors(paper,codebook):
    from jsonschema import Draft202012Validator
    validator=Draft202012Validator(build_paper_schema(codebook))
    return [('/'.join(map(str,error.absolute_path)) or 'paper')+': '+error.message
            for error in sorted(validator.iter_errors(paper),key=lambda e:str(list(e.absolute_path)))][:12]
