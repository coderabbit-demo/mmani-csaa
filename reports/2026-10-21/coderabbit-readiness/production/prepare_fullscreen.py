from pathlib import Path
root=Path(__file__).resolve().parent
s=(root/'build_video.py').read_text()
s=s.replace("BUILD=ROOT/'build'", "BUILD=ROOT/'build-fullscreen'\nBUILD.mkdir(exist_ok=True)")
s=s.replace('W,H=2560,1440', 'W,H=3440,1640')
a=s.index('def chrome('); b=s.index('def probe(', a)
s=s[:a]+'''def chrome(im,label,kind='BITBUCKET CLOUD + CLI'):
    d=ImageDraw.Draw(im)
    d.rectangle((0,1440,W,H),fill=BAND)
    d.rectangle((0,1440,W,1444),fill=ORANGE)
    step,body=label.split('|',1) if '|' in label else ('READINESS',label)
    d.text((44,1464),'STEP '+step.strip() if step.strip().isdigit() else step.strip(),font=f(27,True),fill=ORANGE)
    y=1460
    for line in lines(d,body.strip(),f(36),W-265):
        d.text((210,y),line,font=f(36),fill=WHITE); y+=49
    d.text((44,1600),'CodeRabbit Readiness  |  '+kind+'  |  SILENT',font=f(21),fill=MUTED)
    return im
''' + s[b:]
a=s.index('def card('); b=s.index('def encode_card(', a)
s=s[:a]+'''def card(name,kicker,title,subtitle,bullets,note):
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    d.rectangle((120,160,130,1485),fill=ORANGE)
    d.text((195,165),kicker,font=f(34,True),fill=ORANGE)
    d.text((190,275),title,font=f(112,True),fill=WHITE)
    d.text((195,435),subtitle,font=f(48),fill=MUTED)
    y=630
    for item in bullets:
        d.ellipse((200,y+18,216,y+34),fill=ORANGE)
        for line in lines(d,item,f(44),W-510):
            d.text((250,y),line,font=f(44),fill=WHITE);y+=65
        y+=37
    d.rectangle((185,1330,W-185,1535),fill=BAND)
    y=1363
    for line in lines(d,note,f(34),W-450):
        d.text((220,y),line,font=f(34),fill=MUTED);y+=47
    path=BUILD/(name+'.png');im.save(path);return path
''' + s[b:]
s=s.replace("            ImageDraw.Draw(label_image).text((2080,1093),'FULL WINDOW CONTEXT',font=f(17,True),fill=WHITE)\n",'')
a=s.index('    views=['); b=s.index('    ff([', a)
s=s[:a]+'''    filters=(f"[0:v]fps=30,pad={W}:{H}:0:0:color=0x131318[base];"
             "[base][1:v]overlay=0:0:shortest=1:format=auto[v]")
''' + s[b:]
s=s.replace('px,py,pw,ph=275,106,2010,996', 'px,py,pw,ph=320,25,2800,1390')
s=s.replace("font=ImageFont.truetype(MONO,25); cw=d.textlength('M',font=font); lh=24.5", "font=ImageFont.truetype(MONO,34); cw=d.textlength('M',font=font); lh=33.5")
s=s.replace('sy+y*lh+24)', 'sy+y*lh+33)')
s=s.replace("'-crf','18'", "'-crf','16'")
s=s.replace("'-preset','fast'", "'-preset','veryfast'")
s=s.replace("final=OUT/'CodeRabbit-Readiness-Bitbucket-Cloud.mp4'", "final=OUT/'CodeRabbit-Readiness-Bitbucket-Cloud-Fullscreen.mp4'")
(root/'build_fullscreen.py').write_text(s)
