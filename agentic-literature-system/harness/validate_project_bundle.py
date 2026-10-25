"""Validate the bundled skill under its declared portable installation name.

The harness calls its bundle directory 'skill'; the upstream validator expects
the installation directory to match frontmatter. Platform metadata is rejected
in production before checking an otherwise exact content copy in a temp folder.
"""
import json,pathlib,re,shutil,subprocess,sys,tempfile


def validate(skill):
    skill=pathlib.Path(skill).resolve()
    metadata=[str(p.relative_to(skill)) for p in skill.rglob('*') if p.is_file() and (p.name.startswith('._') or p.name=='.DS_Store')]
    if metadata:return {'passed':False,'platform_metadata_files':metadata,'error':'Archive OS metadata before validating the production bundle'}
    name=re.search(r'^name:\s*([a-z0-9-]+)\s*$',(skill/'SKILL.md').read_text(),re.M)
    if not name:return {'passed':False,'error':'Missing valid portable skill name'}
    with tempfile.TemporaryDirectory(prefix='agentic-bundle-validation-') as tmp:
        dest=pathlib.Path(tmp)/name.group(1)
        shutil.copytree(skill,dest,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        result=subprocess.run([sys.executable,str(dest/'scripts/validate_portable_skill.py'),'--skill-dir',str(dest)],capture_output=True,text=True)
        try:report=json.loads(result.stdout)
        except ValueError:return {'passed':False,'error':'Bundle validator did not return JSON','stderr':result.stderr[-2000:]}
        report.update(source_bundle=str(skill),installation_name=name.group(1),exit_code=result.returncode)
        report['passed']=result.returncode==0 and report.get('passed') is True
        return report


if __name__=='__main__':
    result=validate(pathlib.Path(__file__).resolve().parent.parent/'skill')
    print(json.dumps(result,indent=2,ensure_ascii=False))
    raise SystemExit(0 if result['passed'] else 1)
