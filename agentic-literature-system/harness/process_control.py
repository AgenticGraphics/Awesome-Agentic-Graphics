"""Bounded subprocess groups: timeouts must not leave owned descendants running."""
import os
import signal
import subprocess
import time


def stop_group(process, grace=0.3):
    # Timeout handling and final cleanup may both call this function. On macOS,
    # signaling a reaped group again may report EPERM rather than ESRCH.
    if getattr(process, '_research_group_stopped', False):return
    try:os.killpg(process.pid,signal.SIGTERM)
    except ProcessLookupError:
        process._research_group_stopped=True
        return
    try:process.wait(timeout=grace)
    except subprocess.TimeoutExpired:pass
    # The shell can exit before a descendant that ignores TERM; kill the group too.
    try:os.killpg(process.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    try:process.wait(timeout=1)
    except subprocess.TimeoutExpired:pass
    process._research_group_stopped=True


def preview_text(text, limit, output_dir, label='stdout'):
    """Preserve an oversized asynchronous chunk and disclose its preview boundary."""
    from pathlib import Path
    import uuid
    truncated=len(text)>limit
    result={label:text[:limit],label+'_truncated':truncated,label+'_total_chars':len(text)}
    if truncated:
        directory=Path(output_dir);directory.mkdir(parents=True,exist_ok=True)
        path=directory/(label+'-'+uuid.uuid4().hex+'.txt');path.write_text(text)
        result[label+'_path']=str(path)
        result['output_notice']='Preview truncated; complete captured output is in the returned path. Inspect or page it before claiming full coverage.'
    return result


def run_command(cmd,cwd,env,timeout,output_dir=None):
    from contextlib import ExitStack
    from pathlib import Path
    import tempfile
    if output_dir is not None:
        output_dir=Path(output_dir);output_dir.mkdir(parents=True,exist_ok=True)
    with ExitStack() as stack:
        streams={label:stack.enter_context(tempfile.NamedTemporaryFile(mode='w+',encoding='utf-8',errors='replace',prefix='command-',suffix='-'+label+'.log',dir=output_dir,delete=output_dir is None)) for label in ('stdout','stderr')}
        process=subprocess.Popen(cmd,shell=True,executable='/bin/bash',cwd=cwd,env=env,
                                 stdin=subprocess.DEVNULL,stdout=streams['stdout'],stderr=streams['stderr'],text=True,start_new_session=True)
        timed_out=False
        try:
            process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out=True;stop_group(process)
        finally:
            stop_group(process)
        result={'exit_code':124 if timed_out else process.returncode,'timed_out':timed_out}
        for label,limit in (('stdout',24000),('stderr',4000)):
            stream=streams[label];stream.seek(0);preview=stream.read(limit+1)
            truncated=len(preview)>limit
            result.update({label:preview[:limit],label+'_truncated':truncated,label+'_total_bytes':os.fstat(stream.fileno()).st_size})
            if output_dir is not None:
                if truncated:result[label+'_path']=stream.name
                else:Path(stream.name).unlink()
        if result['stdout_truncated'] or result['stderr_truncated']:
            result['output_notice']='Preview truncated; complete output is in the returned paths when a capture directory is configured. Inspect or page it before claiming full coverage.'
        return result


def run_logged(cmd, *, cwd, env, timeout, stdout, stderr, input_text=None):
    """Bound an experimental runner while preserving streaming diagnostic files."""
    process = subprocess.Popen(cmd, cwd=cwd, env=env, stdout=stdout, stderr=stderr,
                               stdin=subprocess.PIPE if input_text is not None else subprocess.DEVNULL,
                               text=True, start_new_session=True)
    try:
        process.communicate(input=input_text, timeout=timeout)
        return {'exit_code': process.returncode, 'timed_out': False}
    except subprocess.TimeoutExpired:
        stop_group(process)
        return {'exit_code': 124, 'timed_out': True}
    finally:
        stop_group(process)
