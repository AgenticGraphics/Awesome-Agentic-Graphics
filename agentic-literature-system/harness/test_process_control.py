import os
from pathlib import Path
import shlex
import sys
import time
from process_control import run_command


def running(pid):
    path=Path('/proc')/str(pid)/'stat'
    return path.exists() and path.read_text().split()[2]!='Z'


def test_timeout_reaps_child_even_when_it_ignores_term(tmp_path):
    code='import os,signal,time,pathlib;signal.signal(signal.SIGTERM,signal.SIG_IGN);pathlib.Path("child.pid").write_text(str(os.getpid()));time.sleep(30)'
    cmd=shlex.quote(sys.executable)+' -c '+shlex.quote(code)+' & wait'
    started=time.monotonic()
    result=run_command(cmd,tmp_path,os.environ.copy(),.5)
    pid=int((tmp_path/'child.pid').read_text())
    for _ in range(20):
        if not running(pid):break
        time.sleep(.01)
    assert result['exit_code']==124 and result['timed_out']
    assert time.monotonic()-started<3
    assert not running(pid)


def test_nonzero_exit_and_output_are_preserved(tmp_path):
    result=run_command('echo diagnostic >&2; exit 7',tmp_path,os.environ.copy(),2)
    assert result['exit_code']==7 and not result['timed_out']
    assert result['stderr'].strip()=='diagnostic'


def test_logged_runner_preserves_output_and_times_out(tmp_path):
    from process_control import run_logged
    path=tmp_path/'output.log'
    code='import time;print("persisted",flush=True);time.sleep(30)'
    with path.open('w') as out:
        result=run_logged([sys.executable,'-c',code],cwd=tmp_path,env=os.environ.copy(),timeout=.3,stdout=out,stderr=out)
    assert result=={'exit_code':124,'timed_out':True}
    assert path.read_text().strip()=='persisted'


def test_logged_runner_accepts_prompt_without_shell_interpretation(tmp_path):
    from process_control import run_logged
    path=tmp_path/'output.log';prompt='Literal $(do-not-run) `nor-this`\nSecond line.'
    with path.open('w') as out:
        result=run_logged([sys.executable,'-c','import sys;print(sys.stdin.read(),end="")'],cwd=tmp_path,env=os.environ.copy(),timeout=2,stdout=out,stderr=out,input_text=prompt)
    assert result=={'exit_code':0,'timed_out':False} and path.read_text()==prompt


def test_oversized_stdout_and_stderr_are_explicit_and_fully_recoverable(tmp_path):
    code='import sys;sys.stdout.write("候选"*20000);sys.stderr.write("warning"*1000)'
    cmd=shlex.quote(sys.executable)+' -c '+shlex.quote(code)
    result=run_command(cmd,tmp_path,os.environ.copy(),5,output_dir=tmp_path/'captures')
    assert result['exit_code']==0 and result['stdout_truncated'] and result['stderr_truncated']
    assert len(result['stdout'])==24000 and len(result['stderr'])==4000
    assert Path(result['stdout_path']).read_text()=='候选'*20000
    assert Path(result['stderr_path']).read_text()=='warning'*1000
    assert result['stdout_total_bytes']==len(('候选'*20000).encode())


def test_short_output_has_no_false_truncation_or_retained_empty_files(tmp_path):
    result=run_command('printf small',tmp_path,os.environ.copy(),2,output_dir=tmp_path/'captures')
    assert result['stdout']=='small' and not result['stdout_truncated'] and not result['stderr_truncated']
    assert not list((tmp_path/'captures').iterdir())


def test_async_chunk_preview_preserves_its_full_text(tmp_path):
    from process_control import preview_text
    result=preview_text('x'*30000,24000,tmp_path)
    assert result['stdout_truncated'] and result['stdout_total_chars']==30000
    assert Path(result['stdout_path']).read_text()=='x'*30000


def test_synchronous_command_cannot_consume_harness_stdin(tmp_path):
    code='import sys;print(len(sys.stdin.read()))'
    result=run_command(shlex.quote(sys.executable)+' -c '+shlex.quote(code),tmp_path,os.environ.copy(),2)
    assert result['exit_code']==0 and result['stdout'].strip()=='0'
