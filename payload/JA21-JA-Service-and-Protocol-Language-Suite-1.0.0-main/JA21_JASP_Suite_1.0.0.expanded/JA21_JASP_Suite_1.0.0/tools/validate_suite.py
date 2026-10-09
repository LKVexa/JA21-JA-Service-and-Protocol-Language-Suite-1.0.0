#!/usr/bin/env python3
from pathlib import Path
import gzip,json,csv,hashlib,collections,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.')
errors=[]
corpus=root/'corpus/technical/JA21_JASP_TECHNICAL_CORPUS_10000.jsonl.gz'
records=[]
with gzip.open(corpus,'rt',encoding='utf-8') as f:
 for line in f:
  o=json.loads(line)
  if 'record_id' in o: records.append(o)
if len(records)!=10000: errors.append(f'expected 10000 records, found {len(records)}')
if len({r['record_id'] for r in records})!=len(records): errors.append('duplicate record ids')
for r in records:
 if hashlib.sha256(r['source'].encode()).hexdigest()!=r['source_sha256']:
  errors.append('source hash mismatch '+r['record_id']);break
scripts=list((root/'examples/scripts_1000').rglob('*.jasp'))
if len(scripts)!=1000: errors.append(f'expected 1000 scripts, found {len(scripts)}')
with (root/'catalogs/SCRIPT_CATALOG.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
if len(rows)!=1000: errors.append('catalog row count')
if len(set(r['feature'] for r in rows))!=32: errors.append('feature coverage')
if collections.Counter(r['level'] for r in rows)!={x:100 for x in ['beginner','intermediate','advanced','expert','compiler','runtime','optimization','validation','certification','deployment']}:errors.append('level distribution')
book=(root/'textbook/JA21_JA_SERVICE_PROTOCOL_LANGUAGE_TEXTBOOK.md').read_text(encoding='utf-8')
if len(re.findall(r'^# Chapter \d+:',book,flags=re.M))!=22: errors.append('chapter count')
print('PASS' if not errors else 'FAIL')
for e in errors: print('-',e)
sys.exit(1 if errors else 0)
