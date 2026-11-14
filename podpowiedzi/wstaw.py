#!/usr/bin/env python3
"""Wstawia podpowiedzi z podpowiedzi.xlsx do gry (nie potrzeba żadnych dodatkowych bibliotek).

Użycie:  python3 podpowiedzi/wstaw.py index.html
Arkusz „Podpowiedzi”: kolumny klucz, gdzie, PL, EN, DE (pierwszy wiersz to nagłówki).
  klucz  el.<id>    – podpowiedź po najechaniu na element o tym id (lewy pasek, górny pasek …)
         tool.<typ> – opis narzędzia/budynku (po najechaniu i w pasku podpowiedzi)
  PL     tekst po polsku; EN/DE tłumaczenia (puste = zostaje tekst polski)
"""
import json,re,sys,os,zipfile,xml.etree.ElementTree as ET
here=os.path.dirname(os.path.abspath(__file__))
game=sys.argv[1] if len(sys.argv)>1 else os.path.join(here,'..','index.html')
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def col(ref):
    n=0
    for ch in re.match(r'[A-Z]+',ref).group(0):n=n*26+ord(ch)-64
    return n-1
def read_xlsx(path):
    z=zipfile.ZipFile(path)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',NS):
            ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%NS['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml'));rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    target=None
    for sh in wb.find('m:sheets',NS):
        if sh.get('name')=='Podpowiedzi' or target is None:
            rid=sh.get('{%s}id'%NS['r'])
            for r in rels:
                if r.get('Id')==rid:t=r.get('Target');t=t.lstrip('/');target=t if t.startswith('xl/') else 'xl/'+t
            if sh.get('name')=='Podpowiedzi':break
    rows=[]
    for row in ET.fromstring(z.read(target)).iter('{%s}row'%NS['m']):
        vals={}
        for c in row.findall('m:c',NS):
            t=c.get('t');v=c.find('m:v',NS)
            if t=='s' and v is not None:val=ss[int(v.text)]
            elif t=='inlineStr':val=''.join(x.text or '' for x in c.iter('{%s}t'%NS['m']))
            else:val=v.text if v is not None else ''
            vals[col(c.get('r'))]=val or ''
        rows.append([vals.get(k,'') for k in range(5)])
    return rows
src=os.path.join(here,'podpowiedzi.xlsx')
rows=read_xlsx(src)[1:]
tips={}
for n,c in enumerate(rows,2):
    k=(c[0] or '').strip();pl=(c[2] or '').strip()
    if not k:continue
    if not pl:print(f'pomijam wiersz {n} ({k}): pusty tekst PL');continue
    tips[k]=[pl,(c[3] or '').strip(),(c[4] or '').strip()]
js=json.dumps(tips,ensure_ascii=False).replace('</','<\\/')
block=f'<script id="lt-tips">/* podpowiedzi z podpowiedzi/podpowiedzi.xlsx – nie edytuj tutaj, uruchom podpowiedzi/wstaw.py */\nconst LT_TIPS={js};\n</script>'
s=open(game,encoding='utf-8').read()
pat=re.compile(r'<script id="lt-tips">.*?</script>',re.S)
if not pat.search(s):sys.exit('w grze brak bloku <script id="lt-tips"> (potrzebna wersja 8.0.2 lub nowsza)')
s=pat.sub(lambda m:block,s,count=1)
open(game,'w',encoding='utf-8').write(s)
print(f'wstawiono podpowiedzi: {len(tips)}')
