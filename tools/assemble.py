import shutil, collections
from pathlib import Path
rtm=Path('extract/vc6/VC98'); sp=Path('extract/sp6/cabs/vc98'); out=Path('msvc600sp6')
files={}
import json
REN=json.load(open('renames.json'))
def add(src,rel,origin):
    key=rel.replace('\\','/').lower()
    if origin=='rtm':
        if key in REN: key=key.rsplit('/',1)[0]+'/'+REN[key].lower()
        if key.startswith('mfc/src/platform/'): key='mfc/src/intel/'+key[len('mfc/src/platform/'):]
    prev=files.get(key)
    files[key]=(src,origin,prev[1] if prev else None)
for p in rtm.rglob('*'):
    if p.is_file(): add(p,str(p.relative_to(rtm)),'rtm')
for p in sp.rglob('*'):
    if p.is_file(): add(p,str(p.relative_to(sp)),'sp6')
msdev=Path('extract/vc6/COMMON/MSDEV98/BIN')
for n in ['MSPDB60.DLL','RC.EXE','RCDLL.DLL','MSDIS110.DLL']: add(msdev/n,'bin/'+n,'rtm-msdev98')
add(Path('extract/sp6/msvcep.dll'),'bin/c2.dll','sp6-msvcep')
for key,(src,origin,prev) in files.items():
    d=out/key; d.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(src,d)
print(collections.Counter((o,p) for _,o,p in files.values())); print(len(files))
