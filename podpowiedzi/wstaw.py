#!/usr/bin/env python3
"""Wstawia podpowiedzi z podpowiedzi.tsv do gry.

Użycie:  python3 podpowiedzi/wstaw.py index.html
Plik TSV: kolumny rozdzielone tabulatorem: klucz, gdzie, PL, EN, DE.
  klucz  el.<id>   – podpowiedź po najechaniu na element o tym id (przyciski z lewej, kafelki u góry …)
         tool.<typ> – opis narzędzia/budynku (pokazuje się po najechaniu i w pasku podpowiedzi)
  PL     tekst po polsku (to widzi gra)
  EN/DE  tłumaczenia; puste pole = zostaje tekst polski
Nie zmieniaj kolumny „klucz”. Wiersze można usuwać – wtedy gra użyje tekstu wbudowanego.
"""
import json,re,sys,os
here=os.path.dirname(os.path.abspath(__file__))
game=sys.argv[1] if len(sys.argv)>1 else os.path.join(here,'..','index.html')
tips={}
with open(os.path.join(here,'podpowiedzi.tsv'),encoding='utf-8') as f:
    head=f.readline()
    for n,line in enumerate(f,2):
        line=line.rstrip('\r\n')
        if not line.strip() or line.startswith('#'):continue
        c=line.split('\t')
        if len(c)<3 or not c[0].strip() or not c[2].strip():
            print(f'pomijam wiersz {n}: brak klucza albo tekstu PL');continue
        c+=['']*(5-len(c))
        tips[c[0].strip()]=[c[2].strip(),c[3].strip(),c[4].strip()]
js=json.dumps(tips,ensure_ascii=False).replace('</','<\\/')
block=f'<script id="lt-tips">/* podpowiedzi z podpowiedzi/podpowiedzi.tsv – nie edytuj tutaj, uruchom podpowiedzi/wstaw.py */\nconst LT_TIPS={js};\n</script>'
s=open(game,encoding='utf-8').read()
pat=re.compile(r'<script id="lt-tips">.*?</script>',re.S)
if not pat.search(s):sys.exit('w grze brak bloku <script id="lt-tips"> (potrzebna wersja 8.0.2 lub nowsza)')
s=pat.sub(lambda m:block,s,count=1)
open(game,'w',encoding='utf-8').write(s)
print(f'wstawiono podpowiedzi: {len(tips)}')
