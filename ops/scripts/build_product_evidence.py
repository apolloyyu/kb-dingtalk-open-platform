#!/usr/bin/env python3
"""Versioned product-guide mirror; original bodies, no generated answers/rules."""
import hashlib,json,pathlib,re,sys

def build(repo, source, commit):
    repo,source=pathlib.Path(repo),pathlib.Path(source)
    if not re.fullmatch('[0-9a-f]{40}',commit):raise ValueError('fixed full source commit required')
    directory=source/'skills/mono/references/products'
    roots={p.stem:p for p in directory.glob('*.md')}
    def title(path):
        return next((line[2:].strip() for line in path.read_text().splitlines() if line.startswith('# ')),path.stem)
    rows=[]
    for path in sorted(directory.rglob('*.md')):
        parts=path.relative_to(directory).parts
        product=parts[0] if len(parts)>1 else path.stem
        parents=[name for name in roots if product.startswith(name+'-')]
        if parents:product=min(parents,key=len)
        root=roots.get(product)
        body=path.read_text();rel=str(path.relative_to(source))
        rows.append({'product':product,'product_title':title(root) if root else product,
            'title':title(path),'source_url':'https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/blob/'+commit+'/'+rel,
            'source_file':rel,'source_commit':commit,'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'body':body})
    target=repo/'graph/peer-products.json';target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps({'source_commit':commit,'source_kind':'upstream product guides; fixed snapshot','documents':rows},ensure_ascii=False,indent=2)+'\n')
    return {'documents':len(rows),'bytes':target.stat().st_size,'source_commit':commit}

if __name__=='__main__':print(json.dumps(build(*sys.argv[1:4])))
