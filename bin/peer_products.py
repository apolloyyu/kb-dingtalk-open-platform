"""Read peer product sources for a product question, without network or a model."""
import json,pathlib,re
import evidence_sections
from urllib.parse import urlsplit

_GENERIC={'钉钉','命令','参考','管理','文档','使用','指南','功能','产品','平台','操作'}
def excerpt(root,query,budget=3600):
    path=pathlib.Path(root)/'graph/peer-products.json'
    if not path.is_file():return ''
    # Explicit entry-point questions retain their own source domain. This is
    # source scope selection, never an API support conclusion.
    urls = re.findall(r'https?://[^\s<>]+', query, re.I)
    words_only = re.sub(r'https?://[^\s<>]+', ' ', query, flags=re.I)
    direct_api_url = any(urlsplit(url).hostname in ('api.dingtalk.com', 'oapi.dingtalk.com') for url in urls)
    if direct_api_url or re.search(r'(?<![a-z0-9_])(?:api|http|sdk|jsapi|dws)(?![a-z0-9_])|接口', words_only, re.I):return ''
    payload=json.loads(path.read_text());rows=payload['documents'];families={}
    for row in rows:
        name=re.sub(r'命令参考|命令|参考|管理|文档|指南','',row['product_title'])
        words={word for part in re.findall('[一-鿿]+',name) for size in (2,3,4)
               for word in [part[i:i+size] for i in range(len(part)-size+1)] if word not in _GENERIC}
        score=sum(len(word) for word in words if word in words_only)
        if re.search(r'(?<![\w-])'+re.escape(row['product'])+r'(?![\w-])',words_only,re.I):score+=10
        if score:families[row['product']]=score
    if not families:return ''
    maximum=max(families.values());selected={p for p,s in families.items() if s==maximum}
    ranked=sorted((row for row in rows if row['product'] in selected),key=lambda r:(
        -3*evidence_sections.relevance(r['title'],words_only)-evidence_sections.relevance(r['body'],words_only),r['source_file']))
    output=[];used=0
    for row in ranked:
        if len(output)>=2:break
        cap=min(1700,budget-used-260)
        if cap<400:break
        body,coverage=evidence_sections.select(row['body'],words_only,cap)
        text=('== 产品原文（独立产品与调用入口） ==\nproduct: '+row['product_title']+'\nsource_url: '+row['source_url']
              +'\nsource_commit: '+row['source_commit']+'\ncoverage: '+coverage['coverage']+'\n'+body)
        if used+len(text)>budget:continue
        output.append(text);used+=len(text)
    return '\n\n'.join(output)
