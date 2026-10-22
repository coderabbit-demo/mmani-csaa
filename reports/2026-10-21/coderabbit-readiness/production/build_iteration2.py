import json, math, hashlib, subprocess, shutil, importlib.util, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
BUILD=ROOT/'build-iteration2'; BUILD.mkdir(exist_ok=True)
spec=importlib.util.spec_from_file_location('video_base',ROOT/'build_fullscreen.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.BUILD=BUILD
OUT=m.OUT
FPS=30
SPEED=0.85
HELP_READY_FRAME=math.ceil(34.8317*FPS)
TERMINAL_END_FRAME=HELP_READY_FRAME+4*FPS
BROWSER_STEPS=[(1,0),(2,13),(3,30),(4,55),(5,65),(6,83),(7,109),(8,156),(9,200),(10,261),(11,315)]
CLI_STEPS=[(12,0),(13,math.ceil(11.1612*FPS)/FPS),(14,math.ceil(27.7837*FPS)/FPS),(15,math.ceil(33.3426*FPS)/FPS)]
TRANSITIONS={
2:('Create a scoped API token','Give the review identity the permissions CodeRabbit needs.'),
3:('Connect the Bitbucket workspace','Authorize CodeRabbit to reach the intended Bitbucket Cloud workspace.'),
4:('Install on selected repositories','Choose which repositories receive CodeRabbit PR reviews.'),
5:('Configure the review identity','Attach the account credentials CodeRabbit uses for review activity.'),
6:('Verify the webhook','Ensure pull-request events can reach CodeRabbit.'),
7:('Connect Jira','Provide native issue context for review and linked-issue checks.'),
8:('Scope the connection','Limit connection access to the intended repositories.'),
9:('Configure the review policy','Set repository context, checks and automatic or manual review triggers.'),
10:('Verify a real PR review','Confirm the review and context checks appear on a real pull request.'),
11:('Request a manual review','Use the explicit command when automatic reviews are disabled.'),
12:('Prepare the CLI environment','Set the installation directory and PATH for local CLI use.'),
13:('Install CodeRabbit CLI','Download and verify the official CodeRabbit command-line tool.'),
14:('Verify the CLI version','Confirm the installation resolves and reports its version.'),
15:('Explore CLI login options','See authentication options before signing in with the intended account.'),
}

def ff(cmd): m.ff(cmd)
def framecount(path):
    data=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=nb_frames,duration','-of','json',str(path)]))['streams'][0]
    return int(data['nb_frames'])
def frame_time(frame): return f'{frame/FPS:.9f}'
def encode_segmented(input_args,filters,total_frames,boundaries,pattern):
    cuts=[frame_time(x) for x in boundaries]
    cmd=input_args+['-vf',filters,'-frames:v',str(total_frames),'-an','-r',str(FPS),'-c:v','libx264','-preset','veryfast','-crf','16','-pix_fmt','yuv420p','-force_key_frames',','.join(cuts),'-flags','+cgop','-f','segment','-segment_times',','.join(cuts),'-segment_time_delta',str(1/(2*FPS)),'-reset_timestamps','1',str(pattern)]
    ff(cmd)

def assets():
    intro,_,_=m.make_assets()
    m.encode_card(intro,7,BUILD/'intro.mp4')
    shutil.copy2(ROOT/'build-fullscreen/closing.mp4',BUILD/'closing.mp4')
    for step,(title,purpose) in TRANSITIONS.items():
        im=m.Image.new('RGB',(m.W,m.H),m.BG);d=m.ImageDraw.Draw(im)
        d.rectangle((160,290,171,1330),fill=m.ORANGE)
        d.text((245,315),f'UP NEXT  |  STEP {step:02d}',font=m.f(40,True),fill=m.ORANGE)
        y=510
        for line in m.lines(d,title,m.f(100,True),m.W-500):
            d.text((240,y),line,font=m.f(100,True),fill=m.WHITE);y+=125
        d.text((245,830),'PURPOSE',font=m.f(32,True),fill=m.ORANGE)
        y=900
        for line in m.lines(d,purpose,m.f(54),m.W-560):
            d.text((245,y),line,font=m.f(54),fill=m.WHITE);y+=76
        d.text((245,1240),'CodeRabbit Readiness  |  Bitbucket Cloud + CLI',font=m.f(27),fill=m.MUTED)
        png=BUILD/f'transition-{step:02}.png';im.save(png)
        m.encode_card(png,4,BUILD/f'transition-{step:02}.mp4')
    print('Opening: 7 seconds. Transition cards: 14 x 4 seconds.',flush=True)

def browser():
    source=ROOT/'build-fullscreen/browser-final.mp4'
    total=math.ceil(framecount(source)/SPEED)
    boundaries=[math.ceil(t/SPEED*FPS) for _,t in BROWSER_STEPS[1:]]
    print('Rendering full-frame browser at 85% speed...',flush=True)
    encode_segmented(['-i',str(source)],f'setpts=(PTS-STARTPTS)/{SPEED},fps={FPS},tpad=stop_mode=clone:stop_duration=0.1',total,boundaries,BUILD/'browser-%02d.mp4')
    print('Browser segments complete.',flush=True)

def terminal():
    cast=[json.loads(l) for l in (ROOT/'raw/terminal.cast').read_text().splitlines()]
    entries=[e for e in cast[1:] if e[0]<=HELP_READY_FRAME/FPS]
    labels=[json.loads(l) for l in (ROOT/'terminal-events.jsonl').read_text().splitlines() if json.loads(l)['time']<=HELP_READY_FRAME/FPS]
    labels[0]['time']=0
    for label in labels:
        step,body=label['label'].split('|',1)
        label['label']=f'{int(step)-1:02} |{body}'
    indices=sorted(set([0]+[math.ceil(e[0]*FPS) for e in entries]+[math.ceil(e['time']*FPS) for e in labels]))
    screen=m.pyte.Screen(cast[0]['width'],cast[0]['height']);stream=m.pyte.Stream(screen)
    frames=BUILD/'terminal-frames';frames.mkdir(exist_ok=True)
    sequence=[];pos=lp=0;last_digest=None
    for frame in indices:
        t=frame/FPS
        while pos<len(entries) and entries[pos][0]<=t+1e-8:
            stream.feed(entries[pos][2]);pos+=1
        while lp+1<len(labels) and labels[lp+1]['time']<=t+1e-8:lp+=1
        im=m.term_frame(screen,labels[lp]['label'])
        digest=hashlib.sha256(im.tobytes()).hexdigest()
        if digest==last_digest:continue
        p=frames/f'{len(sequence):04}.png';im.save(p)
        sequence.append((frame,p));last_digest=digest
    # Last complete help screen remains visible for exactly 120 video frames.
    assert sequence[-1][0]==HELP_READY_FRAME,(sequence[-1][0],HELP_READY_FRAME)
    concat=BUILD/'terminal.ffconcat'
    with concat.open('w') as out:
        out.write('ffconcat version 1.0\n')
        for i,(frame,p) in enumerate(sequence):
            end=sequence[i+1][0] if i+1<len(sequence) else TERMINAL_END_FRAME
            out.write(f"file '{p}'\noption framerate 30\nduration {(end-frame)/FPS:.9f}\n")
        out.write(f"file '{sequence[-1][1]}'\noption framerate 30\n")
    print(f'Encoding terminal through login help; final screen held for 4 seconds ({len(sequence)} changes).',flush=True)
    encode_segmented(['-f','concat','-safe','0','-i',str(concat)],'fps=30',TERMINAL_END_FRAME,[round(t*FPS) for _,t in CLI_STEPS[1:]],BUILD/'terminal-%02d.mp4')

def join():
    sequence=[('intro',BUILD/'intro.mp4')]
    for i,(step,_) in enumerate(BROWSER_STEPS):
        if i:sequence.append((f'transition-{step:02}',BUILD/f'transition-{step:02}.mp4'))
        sequence.append((f'step-{step:02}',BUILD/f'browser-{i:02}.mp4'))
    for i,(step,_) in enumerate(CLI_STEPS):
        sequence.append((f'transition-{step:02}',BUILD/f'transition-{step:02}.mp4'))
        sequence.append((f'step-{step:02}',BUILD/f'terminal-{i:02}.mp4'))
    sequence.append(('closing',BUILD/'closing.mp4'))
    timeline=[];at=0
    for name,p in sequence:
        count=framecount(p)
        timeline.append({'name':name,'start_frame':at,'duration_frames':count,'start_seconds':at/FPS,'duration_seconds':count/FPS,'file':str(p)})
        at+=count
    concat=BUILD/'final.ffconcat'
    concat.write_text('ffconcat version 1.0\n'+''.join(f"file '{p}'\n" for _,p in sequence))
    final=OUT/'CodeRabbit-Readiness-Bitbucket-Cloud-v2.mp4'
    ff(['-f','concat','-safe','0','-i',str(concat),'-map','0:v:0','-c','copy','-an','-movflags','+faststart',str(final)])
    data={'file':str(final),'fps':FPS,'duration_frames':at,'duration_seconds':at/FPS,'browser_speed':SPEED,'help_ready_source_seconds':HELP_READY_FRAME/FPS,'help_hold_seconds':4,'timeline':timeline}
    (BUILD/'timeline.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='timeline'},indent=2),flush=True)

if __name__=='__main__':
    {'assets':assets,'browser':browser,'terminal':terminal,'join':join}[sys.argv[1]]()
