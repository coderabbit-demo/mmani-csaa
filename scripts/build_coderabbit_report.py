import argparse, json, html, re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description='Build a dated CodeRabbit assessment HTML snapshot.')
parser.add_argument('--report-dir',type=Path,default=root/'reports'/'2026-10-21')
args=parser.parse_args()
report_dir=args.report_dir
report=json.loads((report_dir/'coderabbit-assessment.json').read_text())
pi=report.get('pathInstructions')
lines=(root/'runbook.md').read_text().splitlines()
sources=report['sources']
def esc(s): return html.escape(str(s),quote=True)
def fmt(s):
    t=esc(s)
    t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    return t.replace('\n','<br>')
def refs(ids):
    return ' '.join('<a href="'+esc(sources[i][1])+'">['+i+']</a>' for i in dict.fromkeys(ids))
def p(s,cls=''): return '<p'+(' class="'+cls+'"' if cls else '')+'>'+fmt(s)+'</p>'
def pi_cell(key):
    item=pi['candidates'][key]
    if not item['prompt']: return p(item['limit'])
    return p('Suggested paths: '+', '.join(item['paths']))+p('Prompt: '+item['prompt'])+p('Limit: '+item['limit'])
def table(headers,rows,widths=None,row_ids=None):
    if pi and row_ids is not None:
        headers=[*headers,'Potential PI prompt (proposed)']
        rows=[[*row,pi_cell(key)] for row,key in zip(rows,row_ids,strict=True)]
        widths=[6,9.5,22,17,21.5,24]
    out='<table border="1" cellspacing="0" cellpadding="5" width="100%">'
    if widths: out+='<colgroup>'+''.join('<col width="'+str(w)+'%">' for w in widths)+'</colgroup>'
    out+='<thead><tr>'+''.join('<th>'+h+'</th>' for h in headers)+'</tr></thead><tbody>'
    for row in rows: out+='<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>'
    return out+'</tbody></table>'
def label(value):
    return '<p><strong>'+esc(value)+'</strong></p>'
def exact(row):
    c=row['cells']; key=row['id']
    x='<p><strong>'+fmt(c[1])+'</strong></p>'
    if key.startswith('G'):
        x+=p('How to test: '+c[2])+p('Stop / concern: '+c[3])
        if key=='G3':
            x+=p('Detailed prohibited actions (verbatim):')
            x+='<ul>'+''.join('<li>'+fmt(t[2:])+'</li>' for t in lines[347:355] if t.startswith('- '))+'</ul>'
    elif key.startswith('P'):
        x+=p('Setup: '+c[2])+p('Expected good signal: '+c[3])+p('Bad signal: '+c[4])
        if key=='P6':
            x+=p('Origin definitions (§7.3):')
            for ln in lines[465:469]:
                q=[v.strip() for v in ln.strip('|').split('|')]
                if len(q)==2: x+=p(q[0]+': '+q[1])
    else:
        x+=p(('Rule content: ' if key.startswith('R') else 'Expected signal: ')+c[2])
        if key.startswith('S'): x+=p('Status: '+c[3])
    return x+p('Source: runbook.md, line '+str(row['line'])+'.','source')
def prod_section(key,title,note):
    out='<h1>'+esc(title)+'</h1>'+p(note)
    rs=[]
    for q in report['requirements'][key]:
        if q['id'] not in report['productRows']: continue
        a=report['productRows'][q['id']]
        rs.append([label(q['id']),label(a['status']),exact(q),p(a['evidence'])+p('POC evidence: not supplied.'),p(a['mitigation'])+'<p>'+refs(a['refs'])+'</p>'])
    return out+table(['ID','Met','Exact requirement wording','Evidence and remaining gap','Available mitigation and closure proof'],rs,[6.5,10,30,23.5,30],row_ids=[q['id'] for q in report['requirements'][key] if q['id'] in report['productRows']])
out='<!doctype html><html><head><meta charset="utf-8"><title>'+esc(report['title'])+'</title><style>@page{size:letter landscape;margin:0.5in;}body{font-size:11pt;line-height:1.15;max-width:10in;margin:0 auto;}p{margin:0 0 6pt;}h1{font-size:18pt;margin:18pt 0 8pt;}h2{font-size:16pt;margin:14pt 0 8pt;}h1.title{font-size:22pt;}table{border-collapse:collapse;margin:6pt 0 14pt;}th,td{border:1px solid #aab4c1;padding:5pt;vertical-align:top;}th{background:#e8eef5;text-align:left;}code,pre{font-family:monospace;}pre{white-space:pre-wrap;font-size:10pt;border:1px solid #c8cfd8;padding:8pt;}p.source{color:#475467;font-size:10pt;}li{margin-bottom:4pt;}</style></head><body>'
out+='<h1 class="title">'+esc(report['title'])+'</h1>'+p(report['date'])
out+=p('The framework is a credible basis for a controlled POC. The supplied package is a draft specification with no executed gate/probe evidence. Many gaps can be mitigated through supported CodeRabbit configuration, context controls or an evidence adapter; proposed mitigation is not proof that a criterion has been met.')
out+=p(report.get('extension',{}).get('intro','This revision expands the exact evaluated wording, separates supported product capability from actual POC evidence, and evaluates a mitigation for every previous hard No. It does not apply any CodeRabbit settings or change the source package.'))
if pi: out+=p(report['extension']['usage'])
out+=p('Local authority: '+report['packageVersion']+'. Product implementation reference: ')+ '<p><a href="https://github.com/coderabbitai/mono/tree/'+esc(report['monoRef'])+'">coderabbitai/mono @ '+esc(report['monoRef'])+'</a>. Targeted source inspection establishes implementation evidence; it does not establish the deployed SaaS revision or your enabled plan.</p>'
out+='<h1>How to read the assessment</h1>'
out+=p('Met describes current documentation/source support: Yes = a supported route satisfies the literal capability; Partial = support exists with conditions or an export/enforcement gap; Maybe = a plausible unverified route; Unknown = insufficient evidence; No = an identified current gap. Every live gate and behavioral probe remains unexecuted in this package. These labels are not the framework’s 0–3 scores or Green/Yellow/Red probe ratings.')
out+=p('The exact-wording column reproduces the applicable runbook cells. The framework-gap table quotes the relevant clauses or explicitly labels a proposed additional safeguard. It does not present a new safeguard as an already written requirement.')
out+=p('Context/setup controls can be allowed in the native manifest, subject to the existing scope policy. New house rules, semantic path instructions, custom checks, profile tuning or remediation require a declared manifest/version and separate reporting. Output-format-only prompting needs an explicit predeclared DPT decision; normalization must not invent evidence. Original frozen results retain their role under runbook §19.')
out+='<h2>Important corrections to the earlier shorthand</h2>'
out+='<ul>'+''.join('<li>'+fmt(t)+'</li>' for t in [
'G7 accepts API, JSON, SARIF, webhook, Code Insights OR a structured report. CLI JSON satisfies the stated availability criterion; Bitbucket-specific field completeness is a separate export/P10 validation.',
'G3’s detailed list prohibits code pushes without explicit human action. Human-triggered fixes are not an automatic failure; automatic approval and the wider effect boundary still need controls.',
'G4 asks whether files beyond the diff are available. P2 separately tests whether context was used to find the issue.',
'P2 should not fail solely because an inline finding is anchored on a changed line. Evaluate the evidence it used.',
'No locked cases or evidence is a package-readiness gap. It is not a demonstrated CodeRabbit detection failure.',
'A statement in path instructions is a behavior aid; it is not a provider-enforced permission boundary.'
])+'</ul>'
out+='<h1>Mitigation mechanisms</h1>'+p('C1–C10 below distinguish product settings from evaluator-owned work. They are reusable references in the requirement tables.')
out+=table(['Code / mechanism','What is available and where it applies','Evidence'],[[p(c[0]+' — '+c[1])+p(c[2]),p(c[3]),refs(c[4]) or p('Evaluation process; local runbook authority.')] for c in report['catalog']],[24,61,15])
sections=[
('G','Mandatory gates G1–G8','Literal pass/fail gate wording from runbook §6. A supported capability is not a recorded gate pass. See the G3 row for the detailed qualified prohibited-action list.'),
('P','Required probes P1–P13','Exact setup, expected-good-signal and bad-signal cells from §7.2 are retained. No cases have been executed. Score against locked keys, preserve decoys/controls, and keep any configured/remediation result separate.'),
('A','Agentic probes A1–A5','Applicability follows §8.1: A4 is required core on every platform; A1–A3 and A5 are required on TPS and NA elsewhere until agentic coding is in use. G8 tests a product capability on every platform.'),
('D','Payment probes D1–D9','Per §8.1: required on TPS, and on Payment Central / Informatica where the reviewed code/data is on a payment path. Product customization makes the business rule available; it does not demonstrate detection.'),
('C','Contract/API probes C1–C8','Per §8.1: required on TPS; conditionally required for Payment Central APIs/events and Informatica reviewable file/feed/external contracts.'),
('S','AWS/serverless probes S1–S10','S1, S5, S8 and S10 are core on TPS. Other S-probes are optional and must be preselected. NA on platforms without AWS. Keep the existing Snyk-overlap policy and record per-tool provenance.'),
('R','Configured organizational rules R1–R6','Per §8.7, these test a locked tool-independent profile in a separately frozen configured round. Until a platform profile is locked the R-set is NA; once an applicable locked rule exists, inability to accept/apply it is Red rather than NA.'),
('E','Separate-spec and external-context probes E1/E2','Only E1 and E2 are assessed here. E2 was promoted to required core; §7 makes it NA for a change without a linked ticket. Required-context retrieval failure is not automatically true non-applicability.')
]
for args in sections:out+=prod_section(*args)
out+='<h1>Platform-specific coverage</h1>'
out+=table(['ID','Met','Exact evaluated clause','Evidence and remaining gap','Mitigation and closure proof'],[[label(x['id']),label(x['status']),p(x['name'])+p(x['exact'])+p(x['local'],'source'),p(x['evidence']),p(x['mitigation'])+'<p>'+refs(x['refs'])+'</p>'] for x in report['platforms']],[6.5,10,30,23.5,30],row_ids=[x['id'] for x in report['platforms']])
out+=p('E3–E10 and AS1–AS8 remain optional/aspirational unless explicitly elevated by the evaluation owner. Their absence is not assigned a hard No or treated as a Day 1 adoption blocker in this report.')
out+='<h1>Framework gaps and mitigation of every hard No</h1>'
out+=p('Current Met below concerns the package’s coverage or artifacts, not product capability. A supported mitigation does not change No to Yes until the package is updated and closure evidence exists. Proposed additional coverage is labeled explicitly.')
out+=table(['ID','Met','Exact clause or explicitly proposed requirement','Assessment','Product mitigation, owner work and residual proof'],[
[label(g['id']),label(g['met']),p(g['name']+' — '+g['priority'])+p(g['exact'])+p(g['local'],'source'),p(g['assessment']),'<p><strong>'+esc(g['mitigationSupport'])+'</strong></p>'+p(g['mitigation'])+'<p>'+refs(g['refs'])+'</p>'] for g in report['gaps']],[6.5,10,30,23.5,30],row_ids=[g['id'] for g in report['gaps']])
out+='<h1>Illustrative configuration fragments</h1>'
out+=p('These are supported-format examples based on the inspected schema, not an applied or fully validated tenant configuration. Validate against the deployed schema/YAML validator and export @coderabbitai configuration before freezing. Do not copy the mono repository’s own dogfooding configuration wholesale.')
out+='<h2>Advisory controls</h2><pre>'+esc(report['examples']['advisory'])+'</pre>'
out+=p('Also omit Bitbucket write:repository:bitbucket, constrain the account’s repository roles, keep required human reviewers, and turn off merge/coding automations outside this fragment. Required PR-write scope still permits provider approval, so the runtime configuration guard and protected configuration are material controls. inheritance:false does not cancel final organization/workspace global overrides; inspect the effective result. [D1, D9, M1, M2]')
out+=p('For a strict native round, separately declare whether code_guidelines must be disabled and which linked-repository/MCP/web sources are supplied. Do not disable a source required by A4/E2 and then grade missing context as a successful test. learnings.scope:local reduces cross-repository learning but does not freeze this repository’s or source PR’s evolving state.')
out+='<h2>Configured review semantics</h2><pre>'+esc(report['examples']['configured'])+'</pre>'
out+=p('Replace placeholder paths with real repository paths and supply the locked external specification via linked-repository/MCP configuration as applicable. The payment/format instructions are general rules, not probe-specific answer hints. Path instructions can shape inline review behavior; the warning-mode custom check produces a separate summary verdict. Neither changes access permissions or guarantees correct reasoning. [M1, M13, M14]')
out+='<h1>Decision and calibration clauses retained</h1>'
out+=p('The support labels in this report do not replace these existing outcome rules. Local source: runbook §19.')
def readtable(a,b):
    out=[]
    for n in range(a,b+1):
        line=lines[n-1]
        if line.startswith('|') and not re.match(r'^\|[- :|]+$',line):
            out.append([v.strip() for v in line.strip('|').split('|')])
    return out
dec=readtable(913,918)
out+=table([fmt(s) for s in dec[0]],[[fmt(s) for s in r] for r in dec[1:]],[22,78])
out+=p('“NA cells count neither for nor against an outcome; the outcome lists which cells were NA. Any exception to these rules is approved by the Week 1 decision owner, recorded with its reason, and reported to ARC.” (line 920). F08 proposes a separate execution-status field so this applicability rule cannot silently exempt missing required evidence.')
out+=p('Calibration bands are aids rather than industry standards. Local source: runbook §16.')
cal=readtable(819,826)
out+=table([fmt(s) for s in cal[0]],[[fmt(s) for s in r] for r in cal[1:]],[22,26,26,26])
out+='<h1>Closure sequence</h1><ol>'+''.join('<li>'+fmt(t)+'</li>' for t in [
'Resolve the disposable/live-PR policy, applicability versus execution status, and non-author scoring assignments; approve the evaluation wave.',
'Create frozen code/spec snapshots, independent locked answer keys, meaningful controls and an evidence capture plan. Do not expose the answer-key repository to the reviewer.',
'Freeze the deployed CodeRabbit version/CLI, provider/plan entitlements, effective settings, tool inventory, credential scopes and supplied sources. Prove the advisory boundary with actual denied-action checks.',
'Run native probes with completed/non-reused comparisons; capture raw findings and provenance. Preserve failures and misses.',
'Apply named general configuration/customization remedies as separate manifest versions. Re-run the same locked assets and report original and remediated results separately; include the additional setup effort.',
'Make the platform recommendation from recorded gates and required probe evidence. Product configuration availability alone is not a Ready to pilot outcome.'
])+'</ol>'
out+='<h1>Sources and traceability</h1>'
out+=p('Reviewed on October 21, 2026. Public documentation was checked for the available mitigation mechanisms. Mono links are pinned to the inspected revision and require the reader’s existing repository permission.')
for i,(title,url) in sources.items():out+='<p><a href="'+esc(url)+'">['+i+'] '+esc(title)+'</a></p>'
out+=p('Local package: framework.md owns principles; runbook.md owns mechanics. All exact requirements above are copied from the supplied package, with line references. The package contains 14 Markdown files and 19 placeholder .gitkeep files; no populated evidence/baseline records or locked executable probe case was supplied.')
for name in ['runbook.md','framework.md','probe-pack/README.md']:
    out+=p(name+' SHA-256: '+report['hashes'][name],'source')
out+=p('No local source-package file or CodeRabbit setting was changed by this review. The requested Google Doc is a report, not execution evidence.')
out+='</body></html>'
(report_dir/'coderabbit-assessment.html').write_text(out,encoding='utf-8')
plain=re.sub(r'<[^>]+>',' ',out)
print(json.dumps({'html_bytes':len(out.encode()),'approx_words':len(plain.split()),'product_rows':len(report['productRows'])+len(report['platforms']),'framework_gaps':len(report['gaps']),'tables':out.count('<table '),'path':str(report_dir/'coderabbit-assessment.html')}))
