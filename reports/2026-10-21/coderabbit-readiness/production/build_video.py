import sys, json, subprocess, textwrap, hashlib, re, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import pyte

ROOT=Path(__file__).resolve().parent
BUILD=ROOT/'build'
OUT=ROOT.parent/'deliverables'
W,H=2560,1440
BG='#131318'; BAND='#1c1b22'; ORANGE='#ff7846'; WHITE='#f6f2ed'; MUTED='#b9b5be'
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
MONO='/System/Library/Fonts/Menlo.ttc'
def f(size,bold=False):return ImageFont.truetype(BOLD if bold else FONT,size)
def lines(draw,text,font,maxwidth):
    result=[]; line=''
    for word in text.split():
        candidate=(line+' '+word).strip()
        if draw.textlength(candidate,font=font)>maxwidth and line:result.append(line);line=word
        else:line=candidate
    if line:result.append(line)
    return result
def chrome(im,label,kind='BITBUCKET CLOUD + CLI'):
    d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,87),fill=BG)
    d.text((56,23),'CodeRabbit Readiness',font=f(35,True),fill=WHITE)
    right=f'{kind}  |  SILENT WALKTHROUGH'
    d.text((W-56-d.textlength(right,font=f(23)),31),right,font=f(23),fill=MUTED)
    d.rectangle((0,1120,W,H),fill=BAND)
    d.rectangle((0,1120,W,1125),fill=ORANGE)
    step,body=label.split('|',1) if '|' in label else ('READINESS',label)
    d.text((60,1154),'STEP '+step.strip() if step.strip().isdigit() else step.strip(),font=f(27,True),fill=ORANGE)
    y=1210
    for line in lines(d,body.strip(),f(40),W-120):
        d.text((60,y),line,font=f(40),fill=WHITE); y+=53
    d.text((60,1398),'Action descriptions are permanently burned into the picture. No audio or subtitle track.',font=f(22),fill=MUTED)
    return im
def probe(path):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type,width,height','-of','json',str(path)]))
def ff(cmd):
    p=subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error']+cmd)
    if p.returncode:raise RuntimeError('ffmpeg failed')
def card(name,kicker,title,subtitle,bullets,note):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    d.rectangle((100,130,110,1260),fill=ORANGE)
    d.text((165,150),kicker,font=f(31,True),fill=ORANGE)
    d.text((160,245),title,font=f(92,True),fill=WHITE)
    d.text((165,375),subtitle,font=f(42),fill=MUTED)
    y=520
    for item in bullets:
        d.ellipse((170,y+14,184,y+28),fill=ORANGE)
        for line in lines(d,item,f(39),2110):
            d.text((215,y),line,font=f(39),fill=WHITE);y+=58
        y+=35
    d.rectangle((155,1120,2410,1305),fill=BAND)
    y=1152
    for line in lines(d,note,f(30),2150):d.text((185,y),line,font=f(30),fill=MUTED);y+=43
    path=BUILD/(name+'.png');im.save(path);return path
def encode_card(path,seconds,output):
    ff(['-loop','1','-i',str(path),'-t',str(seconds),'-an','-r','30','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p',str(output)])

def make_assets():
    BUILD.mkdir(exist_ok=True);OUT.mkdir(exist_ok=True)
    intro=card('intro','CUSTOMER SETUP GUIDE','CodeRabbit Readiness','Bitbucket Cloud installation, connections, scopes and CLI',[
        'Follow the actual configured demo tenant, with visible clicks and typed input.',
        'Use the provider permissions and repository scope approved for your customer.',
        'Finish with an observed PR review and a fresh CLI installation.'
    ],'Existing cloud setup is demonstrated. New account creation, OAuth consent, secret issuance and final installation saves are explained, not repeated. The CLI installation is recorded live.')
    terminal=card('terminal-intro','LOCAL DEVELOPER SETUP','Install CodeRabbit CLI','A real timed shell session, rendered from its recorded output',[
        'The official installer downloads and verifies a fresh CLI binary.',
        'Commands retain their original character-by-character timing.',
        'Authentication is checked separately from the hosted Bitbucket installation.'
    ],'This recording uses an isolated installation directory and defers browser login. The machine has an existing GitHub sign-in; a customer must choose the correct Bitbucket identity and organization.')
    close=card('closing','CUSTOMER HANDOFF','Verify readiness','Repeat these checks in the customer Bitbucket Cloud instance',[
        'Review identity + scoped token, repository installation + working webhook.',
        'Native Jira connection + approved repository scope + project exclusions.',
        'Repository-root YAML + intended automatic or manual review triggers.',
        'Eligible test PR + observed review + expected Jira and change-scope checks.',
        'CLI version + matching sign-in identity, organization and plan access.'
    ],'Replace all demo workspace, repository and CDC/CDB identifiers. Keep tokens and installation secrets private. Preserve required human approvals. Setup evidence is separate from formal evaluation success.')
    return intro,terminal,close

def browser_video():
    duration=float(probe(ROOT/'raw/browser-window.mp4')['format']['duration'])
    events=[json.loads(l) for l in (ROOT/'events.jsonl').read_text().splitlines()]
    events=[e for e in events if e['time']<duration]
    events[0]['time']=0
    concat=BUILD/'browser-labels.ffconcat'
    with concat.open('w') as out:
        out.write('ffconcat version 1.0\n')
        for i,event in enumerate(events):
            path=BUILD/f'label-{i:02}.png'
            label_image=chrome(Image.new('RGBA',(W,H),(0,0,0,0)),event['label'])
            ImageDraw.Draw(label_image).text((2080,1093),'FULL WINDOW CONTEXT',font=f(17,True),fill=WHITE)
            label_image.save(path)
            end=events[i+1]['time'] if i+1<len(events) else duration
            out.write(f"file '{path}'\nduration {end-event['time']:.6f}\n")
        out.write(f"file '{path}'\n")
    print('Encoding browser walkthrough with permanent action labels...',flush=True)
    views=[(54,1.65,800,120),(73,1.75,850,0),(88,1.9,1200,50),
           (106,1.8,1000,0),(118,1.8,1000,500),(144,1.95,1615,60),
           (164,2.0,1100,80),(176,1.8,850,0),(191,1.8,1000,0),
           (210,1.8,1000,500),(245,1.8,200,130),(270,1.8,200,500),
           (299,1.4,300,0),(9999,1.6,300,300)]
    def choose(column):
        expr=str(views[-1][column])
        for v in reversed(views[:-1]):expr=f'if(lt(on,{v[0]*30}),{v[column]},{expr})'
        return expr
    filters=("[0:v]fps=30,crop=3316:1340:124:100,split=2[wide][detail];"
       f"[detail]zoompan=z='{choose(1)}':x='{choose(2)}':y='{choose(3)}':d=1:s=2560x1034:fps=30,"
       "pad=2560:1440:0:87:color=0x131318[base];"
       "[wide]scale=464:188:flags=lanczos,pad=468:216:2:2:color=0x3f3a46[pip];"
       "[base][pip]overlay=2070:895[context];[context][1:v]overlay=0:0:shortest=1:format=auto[v]")
    ff(['-i',str(ROOT/'raw/browser-window.mp4'),'-f','concat','-safe','0','-i',str(concat),'-filter_complex',filters,
        '-map','[v]','-t',str(duration),'-an','-r','30','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',str(BUILD/'browser-final.mp4')])
    return duration

ANSI={'black':'#15151b','red':'#ed7a7d','green':'#83d6a3','brown':'#edc47c','blue':'#80aef5','magenta':'#c7a0eb','cyan':'#78d9db','white':'#e7e6eb',
      'brightblack':'#8e8999','brightred':'#ff8c90','brightgreen':'#a5ecc0','brightbrown':'#f5dc9e','brightblue':'#a5c7ff','brightmagenta':'#e0bbff','brightcyan':'#a7f1f3','brightwhite':'#ffffff','default':'#e7e6eb'}
def term_frame(screen,label):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    px,py,pw,ph=275,106,2010,996
    d.rounded_rectangle((px,py,px+pw,py+ph),radius=16,fill='#101117',outline='#494451',width=2)
    d.rounded_rectangle((px,py,px+pw,py+45),radius=16,fill='#302e38')
    for i,color in enumerate(['#ff6057','#febc2e','#28c840']):d.ellipse((px+20+i*28,py+15,px+34+i*28,py+29),fill=color)
    d.text((px+155,py+11),'Recorded shell session (PTY)  |  zsh  |  account email hidden',font=f(20),fill=WHITE)
    font=ImageFont.truetype(MONO,25); cw=d.textlength('M',font=font); lh=24.5
    sx,sy=px+25,py+56
    for y in range(screen.lines):
        line=screen.buffer[y]
        for x in range(screen.columns):
            char=line[x]
            if not char.data or char.data==' ':continue
            fg=ANSI.get(char.fg,'#'+char.fg if re.fullmatch('[0-9a-fA-F]{6}',char.fg) else WHITE)
            d.text((sx+x*cw,sy+y*lh),char.data,font=font,fill=fg)
    if not screen.cursor.hidden:
        x,y=screen.cursor.x,screen.cursor.y
        d.rectangle((sx+x*cw,sy+y*lh+3,sx+(x+1)*cw-1,sy+y*lh+24),outline=ORANGE,width=2)
    return chrome(im,label,'REAL TERMINAL SESSION')

def terminal_video():
    cast=[json.loads(l) for l in (ROOT/'raw/terminal.cast').read_text().splitlines()]
    entries=cast[1:]
    labels=[json.loads(l) for l in (ROOT/'terminal-events.jsonl').read_text().splitlines() if 'END |' not in l]
    labels[0]['time']=0
    screen=pyte.Screen(cast[0]['width'],cast[0]['height']); stream=pyte.Stream(screen)
    alltimes=sorted(set([0.0]+[float(e[0]) for e in entries]+[float(e['time']) for e in labels]))
    frames=BUILD/'terminal-frames';frames.mkdir(exist_ok=True)
    pos=0;lp=0;sequence=[];last_digest=None;last_path=None
    for i,t in enumerate(alltimes):
        while pos<len(entries) and entries[pos][0]<=t:
            text=entries[pos][2]
            stream.feed(text);pos+=1
        while lp+1<len(labels) and labels[lp+1]['time']<=t:lp+=1
        im=term_frame(screen,labels[lp]['label'])
        digest=hashlib.sha256(im.tobytes()).hexdigest()
        if digest==last_digest:continue
        path=frames/f'{len(sequence):04}.png';im.save(path,optimize=False)
        sequence.append((t,path));last_digest=digest;last_path=path
    duration=entries[-1][0]+1
    concat=BUILD/'terminal.ffconcat'
    with concat.open('w') as out:
        out.write('ffconcat version 1.0\n')
        for i,(t,path) in enumerate(sequence):
            end=sequence[i+1][0] if i+1<len(sequence) else duration
            out.write(f"file '{path}'\nduration {end-t:.6f}\n")
        out.write(f"file '{last_path}'\n")
    print(f'Encoding real terminal recording: {len(sequence)} observed screen changes...',flush=True)
    ff(['-f','concat','-safe','0','-i',str(concat),'-t',str(duration),'-an','-r','30','-c:v','libx264','-preset','fast','-crf','18','-pix_fmt','yuv420p',str(BUILD/'terminal-final.mp4')])
    return duration

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'all'
    if mode in ['assets','all']:
        a,b,c=make_assets()
        encode_card(a,16,BUILD/'intro.mp4');encode_card(b,12,BUILD/'terminal-intro.mp4');encode_card(c,22,BUILD/'closing.mp4')
    if mode in ['browser','all']:browser_video()
    if mode in ['terminal','all']:terminal_video()
    if mode in ['join','all']:
        files=['intro.mp4','browser-final.mp4','terminal-intro.mp4','terminal-final.mp4','closing.mp4']
        concat=BUILD/'final.ffconcat'
        concat.write_text('ffconcat version 1.0\n'+''.join(f"file '{BUILD/name}'\n" for name in files))
        final=OUT/'CodeRabbit-Readiness-Bitbucket-Cloud.mp4'
        ff(['-f','concat','-safe','0','-i',str(concat),'-map','0:v:0','-c','copy','-an','-movflags','+faststart',str(final)])
        print(json.dumps({'final':str(final),'probe':probe(final)},indent=2),flush=True)
