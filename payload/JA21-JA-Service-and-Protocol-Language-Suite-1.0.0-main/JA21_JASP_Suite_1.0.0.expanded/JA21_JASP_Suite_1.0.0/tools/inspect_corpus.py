#!/usr/bin/env python3
import gzip,json,collections,sys
p=sys.argv[1] if len(sys.argv)>1 else 'corpus/technical/JA21_JASP_TECHNICAL_CORPUS_10000.jsonl.gz'
counts=collections.Counter();features=collections.Counter();levels=collections.Counter();n=0
with gzip.open(p,'rt',encoding='utf-8') as f:
 for line in f:
  o=json.loads(line)
  if 'record_id' not in o: continue
  n+=1; counts[o['validation_class']]+=1; features[o['feature']]+=1; levels[o['level']]+=1
print('records',n);print('classes',dict(counts));print('levels',dict(levels));print('features',len(features))
