import os, pty, fcntl, termios, struct, time, select, json, threading
from pathlib import Path

root = Path(__file__).resolve().parent
recording = root / 'raw/terminal.cast'
events = root / 'terminal-events.jsonl'
start = time.monotonic()
lock = threading.Lock()
buffer = ''
finished = False
log = recording.open('w')
log.write(json.dumps({'version': 2, 'width': 112, 'height': 38, 'timestamp': int(time.time()), 'env': {'TERM':'xterm-256color'}, 'title':'CodeRabbit Readiness — real terminal session'})+'\n')
log.flush()
pid, fd = pty.fork()
if pid == 0:
    os.chdir(root)
    env = dict(os.environ, TERM='xterm-256color', PROMPT='readiness-demo %% ', RPROMPT='', ZDOTDIR=str(root/'shell-config'))
    os.execvpe('/bin/zsh', ['/bin/zsh','-f'], env)
fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack('HHHH',38,112,0,0))

def reader():
    global buffer, finished
    while not finished:
        ready,_,_ = select.select([fd],[],[],0.1)
        if not ready: continue
        try: data=os.read(fd,65536)
        except OSError: break
        if not data: break
        text=data.decode('utf-8','replace')
        with lock:
            buffer += text
            log.write(json.dumps([round(time.monotonic()-start,4),'o',text])+'\n')
            log.flush()

thread = threading.Thread(target=reader,daemon=True)
thread.start()

def mark(label):
    row={'time':round(time.monotonic()-start,4),'label':label}
    with events.open('a') as out: out.write(json.dumps(row)+'\n')
    print(label,flush=True)

def run(command,label,hold=2):
    mark(label)
    with lock: offset=len(buffer)
    for character in command:
        os.write(fd,character.encode())
        time.sleep(0.065)
    os.write(fd,b'\r')
    deadline=time.monotonic()+180
    while time.monotonic()<deadline:
        with lock: output=buffer[offset:]
        if 'readiness-demo % ' in output: break
        time.sleep(0.1)
    else: raise RuntimeError('Command did not return to prompt: '+command)
    time.sleep(hold)

try:
    time.sleep(1)
    run('export CODERABBIT_INSTALL_DIR="$PWD/cli-bin"', '13 | Fresh CLI installation: choose an isolated demonstration directory. A normal install uses ~/.local/bin.')
    run('export PATH="$CODERABBIT_INSTALL_DIR:$PATH"', '13 | Add the installation directory to this shell PATH so coderabbit and cr resolve correctly.')
    run('curl -fsSL https://cli.coderabbit.ai/install.sh | CR_CLI_SKIP_LOGIN=1 sh', '14 | Download and run the official installer. Browser login is deferred so no authentication tokens appear in the recording.', 6)
    run('coderabbit --version', '15 | Verify the installed CodeRabbit CLI version. The cr command is its short alias.', 4)
    run('cr auth login --help', '16 | New users run cr auth login (or --region eu) and complete browser sign-in with the intended account.', 8)
    run('cr auth status', '17 | Verify sign-in identity and organization. This existing machine is GitHub-authenticated; Bitbucket users must sign in to the matching account and organization.', 8)
    run('cr auth org --help', '18 | Select the organization with the Bitbucket connection and CLI entitlement. A hosted PR installation does not establish CLI access.', 6)
    mark('END | Terminal installation and authentication guidance captured. No code review was started.')
    os.write(fd,b'exit\r')
    os.waitpid(pid,0)
finally:
    finished=True
    thread.join(timeout=2)
    log.close()
print('Saved timed terminal recording: '+str(recording),flush=True)
