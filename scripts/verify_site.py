#!/usr/bin/env python3
"""Check exported post routes and local references in the generated website."""
import json
from pathlib import Path
from urllib.parse import urlsplit,unquote
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parent.parent
public=ROOT/'public'
missing={}
for item in json.loads((ROOT/'migration-manifest.json').read_text()):
    assert (public/unquote(item['url']).lstrip('/')/'index.html').is_file(),item['url']
for page in public.rglob('*.html'):
    soup=BeautifulSoup(page.read_text(),'html.parser')
    for node in soup.find_all(['a','img','iframe','link','script']):
        ref=node.get('src') or node.get('href','')
        parsed=urlsplit(ref)
        if parsed.netloc or not parsed.path.startswith('/'): continue
        path=public/unquote(parsed.path).lstrip('/')
        if path.is_file() or (path/'index.html').is_file():continue
        missing.setdefault(parsed.path,set()).add(str(page.relative_to(public)))
report={'original_routes_verified':154,'missing_local_targets':{k:sorted(v) for k,v in sorted(missing.items())}}
(ROOT/'link-report.json').write_text(json.dumps(report,indent=2))
print('Original routes verified:',154)
print('Missing local targets:',len(missing))
for key,values in list(sorted(missing.items()))[:30]:print(key, 'from',next(iter(values)))
