import sys,json,re,time
from pathlib import Path
r=Path(__file__).resolve().parent
progress=r/'progress.txt'
s=progress.read_text() if progress.exists() else ''
a=re.findall(r'out_time_us=(\d+)',s)
t=int(a[-1])/1e6 if a else 0
e={'time':t,'wall':time.time(),'label':sys.argv[1]}
with (r/'events.jsonl').open('a') as f:f.write(json.dumps(e)+'\n')
print(json.dumps(e))
