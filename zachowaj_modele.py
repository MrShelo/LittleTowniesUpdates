#!/usr/bin/env python3
"""Kopiuje nową wersję gry do index.html, zachowując modele wysłane z edytora (blok /*LT-MODELS*/).
Użycie (po git pull): python3 zachowaj_modele.py nowa.html
Wersja nowej gry musi być wyższa niż ta na GitHubie (edytor sam podbija wersję przy wysyłce)."""
import json,re,sys
new=open(sys.argv[1],encoding='utf-8').read()
try:old=open('index.html',encoding='utf-8').read()
except FileNotFoundError:old=''
rx=re.compile(r'/\*LT-MODELS\*/([\s\S]*?)/\*LT-MODELS-END\*/')
mo=rx.search(old);models=json.loads(mo.group(1)) if mo else {}
mn=rx.search(new)
if not mn:sys.exit('nowa wersja nie ma bloku LT-MODELS')
cur=json.loads(mn.group(1));cur.update(models)
new=new[:mn.start()]+'/*LT-MODELS*/'+json.dumps(cur,ensure_ascii=False,separators=(',',':'))+'/*LT-MODELS-END*/'+new[mn.end():]
v=lambda s:tuple(int(x) for x in re.search(r"LT_VERSION='([\d.]+)'",s).group(1).split('.')) if re.search(r"LT_VERSION='([\d.]+)'",s) else (0,0,0)
if old and v(new)<=v(old):sys.exit(f'wersja {v(new)} nie jest wyższa niż na GitHubie {v(old)}')
open('index.html','w',encoding='utf-8').write(new)
print('zachowano modeli:',len(models),'· wersja',v(new))
