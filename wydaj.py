#!/usr/bin/env python3
"""Przygotowuje wydanie: czyta LT_VERSION z index.html i zapisuje version.json oraz update.js.
Użycie: python3 wydaj.py "co nowego"   potem: git add -A && git commit -m "v<wersja>" && git tag v<wersja> && git push --tags origin main"""
import json,re,sys
html=open('index.html',encoding='utf-8').read()
v=re.search(r"LT_VERSION='([\d.]+)'",html).group(1)
notes=sys.argv[1] if len(sys.argv)>1 else ''
json.dump({'v':v,'notes':notes},open('version.json','w',encoding='utf-8'),ensure_ascii=False)
open('update.js','w',encoding='utf-8').write('window.__ltUpdate('+json.dumps({'v':v,'notes':notes,'html':html},ensure_ascii=False)+');\n')
print('wersja',v)
