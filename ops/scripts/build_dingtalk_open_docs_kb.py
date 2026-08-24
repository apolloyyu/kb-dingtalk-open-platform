#!/usr/bin/env python3
"""
Build an agent-friendly Markdown knowledge base from DingTalk Open Platform docs.

Data sources used by the current DingTalk document center:
- /api/docCenter/getDocPageGroupList
- /api/docCenter/getDocInfoList?tabCode=...
- https://icms-document.oss-cn-beijing.aliyuncs.com/zh-CN/dingtalk/{namespace}/topics/{slug}.html
"""

from __future__ import annotations

import concurrent.futures
import datetime as dt
import hashlib
import html
import json
import os
import posixpath
import re
import shutil
import sys
import time
import traceback
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md


BASE_URL = "https://open.dingtalk.com"
GROUPS_API = f"{BASE_URL}/api/docCenter/getDocPageGroupList"
TREE_API = f"{BASE_URL}/api/docCenter/getDocInfoList"
OSS_BASE = "https://icms-document.oss-cn-beijing.aliyuncs.com/zh-CN/dingtalk"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
)


@dataclass
class TabRef:
    group_code: str
    group_name: str
    group_sort: int
    tab_code: str
    tab_name: str
    tab_sort: int


@dataclass
class DocRef:
    doc_id: str
    doc_name: str
    doc_url: str
    namespace: str
    slug: str
    group_code: str
    group_name: str
    group_sort: int
    tab_code: str
    tab_name: str
    tab_sort: int
    breadcrumb: list[str]
    sort_path: list[int]
    local_md: Path | None = None
    raw_html: Path | None = None
    updated_at: str = ""
    title: str = ""
    headings: list[str] = field(default_factory=list)
    snippet: str = ""
    content_chars: int = 0
    html_sha256: str = ""


def request_bytes(url: str, *, timeout: int = 45, retries: int = 3) -> bytes:
    last_error: Exception | None = None
    for attempt in range(retries):
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/json,text/html,application/xhtml+xml,text/plain,*/*",
                "Accept-Encoding": "identity",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as exc:  # noqa: BLE001 - report exact failure later
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(0.5 * (2**attempt))
    assert last_error is not None
    raise last_error


def get_json(url: str, params: dict[str, str] | None = None) -> dict[str, Any]:
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    data = request_bytes(url)
    return json.loads(data.decode("utf-8"))


def safe_segment(value: str, fallback: str = "untitled", max_len: int = 90) -> str:
    value = html.unescape(value or "").strip()
    value = re.sub(r"[\\/:*?\"<>|#%{}$!@`~^+=\[\];,，。？、\s]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._")
    if not value:
        value = fallback
    if len(value) > max_len:
        value = value[:max_len].rstrip("-._")
    return value


def parse_doc_url(url: str) -> tuple[str, str]:
    parsed = urllib.parse.urlparse(url)
    match = re.match(r"/document/([^/?#]+)/([^/?#]+)", parsed.path)
    if not match:
        raise ValueError(f"Unsupported doc URL: {url}")
    return match.group(1), match.group(2)


def normalized_doc_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc in {"developers.dingtalk.com", "pre-open.dingtalk.com"}:
        parsed = parsed._replace(netloc="open.dingtalk.com", scheme="https")
    if not parsed.scheme:
        parsed = parsed._replace(scheme="https", netloc="open.dingtalk.com")
    return urllib.parse.urlunparse(parsed._replace(query="", fragment=""))


def oss_url(namespace: str, slug: str) -> str:
    return f"{OSS_BASE}/{namespace}/topics/{slug}.html"


def flatten_tree(
    nodes: list[dict[str, Any]],
    tab: TabRef,
    *,
    breadcrumb: list[str] | None = None,
    sort_path: list[int] | None = None,
) -> list[DocRef]:
    breadcrumb = breadcrumb or []
    sort_path = sort_path or []
    docs: list[DocRef] = []
    for node in sorted(nodes or [], key=lambda item: item.get("sort") or 0):
        name = node.get("docName") or node.get("name") or "未命名"
        next_breadcrumb = [*breadcrumb, name]
        next_sort_path = [*sort_path, int(node.get("sort") or 0)]
        doc_url = node.get("docUrl")
        if doc_url:
            url = normalized_doc_url(doc_url)
            namespace, slug = parse_doc_url(url)
            docs.append(
                DocRef(
                    doc_id=str(node.get("docId") or ""),
                    doc_name=name,
                    doc_url=url,
                    namespace=namespace,
                    slug=slug,
                    group_code=tab.group_code,
                    group_name=tab.group_name,
                    group_sort=tab.group_sort,
                    tab_code=tab.tab_code,
                    tab_name=tab.tab_name,
                    tab_sort=tab.tab_sort,
                    breadcrumb=next_breadcrumb,
                    sort_path=next_sort_path,
                )
            )
        docs.extend(
            flatten_tree(
                node.get("children") or [],
                tab,
                breadcrumb=next_breadcrumb,
                sort_path=next_sort_path,
            )
        )
    return docs


def make_output_paths(root: Path, docs: list[DocRef]) -> None:
    counters: dict[tuple[str, str], int] = {}
    seen_paths: set[Path] = set()
    for doc in docs:
        key = (doc.group_code, doc.tab_code)
        counters[key] = counters.get(key, 0) + 1
        group_dir = f"{doc.group_sort:02d}-{safe_segment(doc.group_name)}"
        tab_dir = safe_segment(doc.tab_name)
        filename = f"{counters[key]:04d}-{safe_segment(doc.slug, max_len=120)}.md"
        path = root / "docs" / group_dir / f"{doc.tab_sort:02d}-{safe_segment(doc.tab_code, max_len=16)}-{tab_dir}" / filename
        if path in seen_paths:
            suffix = hashlib.sha1(doc.doc_url.encode("utf-8")).hexdigest()[:8]
            path = path.with_name(f"{path.stem}-{suffix}.md")
        seen_paths.add(path)
        doc.local_md = path
        doc.raw_html = root / "raw_html" / doc.namespace / f"{safe_segment(doc.slug, max_len=160)}.html"


def collect_tabs(groups: list[dict[str, Any]]) -> list[TabRef]:
    tabs: list[TabRef] = []
    for group in sorted(groups, key=lambda item: item.get("sort") or 0):
        for tab in sorted(group.get("tabs") or [], key=lambda item: item.get("sort") or 0):
            tabs.append(
                TabRef(
                    group_code=str(group.get("groupCode") or ""),
                    group_name=str(group.get("groupName") or ""),
                    group_sort=int(group.get("sort") or 0),
                    tab_code=str(tab.get("tabCode") or ""),
                    tab_name=str(tab.get("tabName") or ""),
                    tab_sort=int(tab.get("sort") or 0),
                )
            )
    return tabs


def table_first_row_to_header(soup: BeautifulSoup) -> None:
    for table in soup.find_all("table"):
        if table.find("th"):
            continue
        first_tr = table.find("tr")
        if not first_tr:
            continue
        for td in first_tr.find_all("td", recursive=False):
            td.name = "th"


def render_json_schema_components(soup: BeautifulSoup) -> int:
    """展开官方文档的字段说明组件(JsonSchemaEditor)。

    2025 年起官方把事件/接口的字段表做成前端组件,数据以 URL 编码 JSON 存放在
    <div data-type="JsonSchemaEditor" value="%7B..."> 属性里;html_to_md 只保留
    正文文本,组件会整体丢失(实测 579/3664 篇受影响,含 type/result 等关键枚举)。
    此处解码 schema,按 index 顺序展开为「字段说明」标题 + 列表。返回替换个数。
    """
    count = 0
    for div in soup.find_all("div", attrs={"data-type": "JsonSchemaEditor"}):
        raw = div.get("value") or ""
        try:
            schema = json.loads(urllib.parse.unquote(raw))
        except Exception:
            continue
        items: list[tuple[str, dict[str, Any], bool]] = []

        def walk(node: dict[str, Any], path: str) -> None:
            props = node.get("properties") or {}
            required = set(node.get("required") or [])
            ordered = sorted(
                (kv for kv in props.items() if isinstance(kv[1], dict)),
                key=lambda kv: kv[1].get("index", 0),
            )
            for name, sub in ordered:
                dotted = f"{path}.{name}" if path else name
                items.append((dotted, sub, name in required))
                walk(sub, dotted)
                if isinstance(sub.get("items"), dict):
                    walk(sub["items"], f"{dotted}[]")

        walk(schema if isinstance(schema, dict) else {}, "")
        if not isinstance(schema, dict):
            continue
        title = str(schema.get("title") or "").strip() or "字段说明"
        container = soup.new_tag("div")
        heading = soup.new_tag("h3")
        heading.string = title
        container.append(heading)
        if not items:
            # 标量 schema(常见于 JSAPI 出参):无 properties,只有类型/描述/示例
            desc = str(schema.get("description") or "").strip()
            if not desc and not schema.get("type"):
                continue
            p = soup.new_tag("p")
            bits = [b for b in (str(schema.get("type") or ""),) if b]
            if bits:
                p.append(f"（{bits[0]}）")
            if desc:
                p.append(desc)
            sample = schema.get("sample")
            if sample not in (None, "") and not schema.get("hiddenSample"):
                p.append(" 示例：")
                code = soup.new_tag("code")
                code.string = str(sample)
                p.append(code)
            container.append(p)
            div.replace_with(container)
            count += 1
            continue
        ul = soup.new_tag("ul")
        for dotted, sub, req in items:
            li = soup.new_tag("li")
            code = soup.new_tag("code")
            code.string = dotted
            li.append(code)
            bits = [b for b in (str(sub.get("type") or ""), "必填" if req else "") if b]
            if bits:
                li.append(f"（{'，'.join(bits)}）")
            desc = str(sub.get("description") or "").strip()
            if desc:
                li.append("：")
                for i, line in enumerate(desc.splitlines()):
                    if i:
                        li.append(soup.new_tag("br"))
                    li.append(line)
            ul.append(li)
        container.append(ul)
        div.replace_with(container)
        count += 1
    return count


def rewrite_notes(soup: BeautifulSoup) -> None:
    note_type_map = {
        "note-important": "IMPORTANT",
        "note-warning": "WARNING",
        "note-notice": "IMPORTANT",
        "note-note": "NOTE",
        "note-tip": "TIP",
        "note-caution": "CAUTION",
    }
    for note in soup.select("div.note"):
        classes = set(note.get("class") or [])
        note_type = "NOTE"
        for cls, label in note_type_map.items():
            if cls in classes:
                note_type = label
                break
        content = note.select_one(".noteContentSpan") or note
        for icon in content.select(".note-icon-wrapper, i.icon-note"):
            icon.decompose()
        blockquote = soup.new_tag("blockquote")
        p = soup.new_tag("p")
        strong = soup.new_tag("strong")
        strong.string = f"[!{note_type}]"
        p.append(strong)
        blockquote.append(p)
        for child in list(content.children):
            if getattr(child, "name", None) == "strong":
                text = child.get_text(" ", strip=True)
                if text in {"重要", "说明", "注意", "警告"}:
                    child.extract()
                    continue
            blockquote.append(child.extract() if hasattr(child, "extract") else child)
        note.replace_with(blockquote)


def rewrite_links(soup: BeautifulSoup, current_doc: DocRef, local_map: dict[str, Path]) -> None:
    assert current_doc.local_md is not None
    for tag in soup.find_all(["a", "img"]):
        attr = "href" if tag.name == "a" else "src"
        raw = tag.get(attr)
        if not raw:
            continue
        raw = raw.strip()
        if raw.startswith(("data:", "mailto:", "tel:", "javascript:")):
            continue
        if raw.startswith("//"):
            tag[attr] = "https:" + raw
            continue
        parsed = urllib.parse.urlparse(raw)
        if tag.name == "a":
            if raw.startswith("#"):
                continue
            abs_url = raw
            if parsed.scheme == "":
                if raw.startswith("/"):
                    abs_url = urllib.parse.urljoin(BASE_URL, raw)
                else:
                    abs_url = urllib.parse.urljoin(current_doc.doc_url, raw)
            normalized = normalized_doc_url(abs_url)
            hash_part = urllib.parse.urlparse(abs_url).fragment
            if normalized in local_map:
                target = local_map[normalized]
                rel = posixpath.relpath(target.as_posix(), current_doc.local_md.parent.as_posix())
                if hash_part:
                    rel = f"{rel}#{hash_part}"
                tag[attr] = rel
            elif re.search(r"/document/", normalized):
                tag[attr] = normalized + (f"#{hash_part}" if hash_part else "")
            elif parsed.scheme == "":
                tag[attr] = urllib.parse.urljoin(BASE_URL, raw)
        elif tag.name == "img":
            if parsed.scheme == "":
                tag[attr] = urllib.parse.urljoin(oss_url(current_doc.namespace, current_doc.slug), raw)


def clean_html_to_markdown(doc: DocRef, html_text: str, local_map: dict[str, Path]) -> tuple[str, dict[str, Any]]:
    html_text = (
        html_text.replace("static-aliyun-doc.oss-accelerate.aliyuncs.com", "help-static-aliyun-doc.aliyuncs.com")
        .replace("static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com", "help-static-aliyun-doc.aliyuncs.com")
    )
    soup = BeautifulSoup(html_text, "lxml")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    table_first_row_to_header(soup)
    render_json_schema_components(soup)
    rewrite_notes(soup)
    rewrite_links(soup, doc, local_map)

    title = ""
    if soup.find("h1"):
        title = soup.find("h1").get_text(" ", strip=True)
    elif soup.find("title"):
        title = soup.find("title").get_text(" ", strip=True)
    title = title or doc.doc_name

    # 页面可能带多个 gmtModify meta(历史版本+最近修改),取最大值才是真实更新时间
    updated_at = ""
    dates = [
        str(m["content"]).strip()
        for m in soup.find_all("meta", attrs={"name": "gmtModify"})
        if m.get("content")
    ]
    if dates:
        updated_at = max(dates)

    main = soup.find("main") or soup.find("body") or soup
    headings = [
        h.get_text(" ", strip=True)
        for h in main.find_all(["h1", "h2", "h3", "h4"])
        if h.get_text(" ", strip=True)
    ]
    plain_text = re.sub(r"\s+", " ", main.get_text(" ", strip=True)).strip()
    snippet = plain_text[:700]

    body_md = html_to_md(str(main), heading_style="ATX", bullets="-").strip()
    body_md = re.sub(r"\n{3,}", "\n\n", body_md)

    frontmatter = {
        "title": title,
        "source_url": doc.doc_url,
        "namespace": doc.namespace,
        "slug": doc.slug,
        "group": doc.group_name,
        "tab": doc.tab_name,
        "breadcrumb": " > ".join(doc.breadcrumb),
        "doc_id": doc.doc_id,
        "updated_at": updated_at,
    }
    fm_lines = ["---"]
    for key, value in frontmatter.items():
        escaped = str(value).replace('"', '\\"')
        fm_lines.append(f'{key}: "{escaped}"')
    fm_lines.append("---")

    meta_block = [
        "",
        f"> Source: {doc.doc_url}",
        f"> Path: {doc.group_name} / {doc.tab_name} / {' > '.join(doc.breadcrumb)}",
    ]
    if updated_at:
        meta_block.append(f"> Updated: {updated_at}")

    markdown = "\n".join(fm_lines + meta_block + ["", body_md, ""]).strip() + "\n"
    return markdown, {
        "title": title,
        "updated_at": updated_at,
        "headings": headings,
        "snippet": snippet,
        "content_chars": len(plain_text),
    }


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def fetch_and_write_doc(doc: DocRef, local_map: dict[str, Path]) -> tuple[DocRef, dict[str, Any] | None]:
    try:
        assert doc.local_md is not None
        assert doc.raw_html is not None
        url = oss_url(doc.namespace, doc.slug)
        raw = request_bytes(url)
        html_text = raw.decode("utf-8", errors="replace")
        if "<html" not in html_text.lower() and "<body" not in html_text.lower():
            raise ValueError("OSS response does not look like HTML")
        doc.html_sha256 = hashlib.sha256(raw).hexdigest()
        doc.raw_html.parent.mkdir(parents=True, exist_ok=True)
        doc.raw_html.write_bytes(raw)
        markdown, info = clean_html_to_markdown(doc, html_text, local_map)
        doc.local_md.parent.mkdir(parents=True, exist_ok=True)
        doc.local_md.write_text(markdown, encoding="utf-8")
        doc.title = info["title"]
        doc.updated_at = info["updated_at"]
        doc.headings = info["headings"]
        doc.snippet = info["snippet"]
        doc.content_chars = info["content_chars"]
        return doc, None
    except Exception as exc:  # noqa: BLE001 - keep failures in audit file
        return doc, {
            "doc_name": doc.doc_name,
            "source_url": doc.doc_url,
            "oss_url": oss_url(doc.namespace, doc.slug),
            "namespace": doc.namespace,
            "slug": doc.slug,
            "group": doc.group_name,
            "tab": doc.tab_name,
            "breadcrumb": doc.breadcrumb,
            "error": repr(exc),
            "traceback": traceback.format_exc(limit=5),
        }


def doc_record(doc: DocRef, root: Path) -> dict[str, Any]:
    assert doc.local_md is not None
    assert doc.raw_html is not None
    return {
        "title": doc.title or doc.doc_name,
        "doc_name": doc.doc_name,
        "source_url": doc.doc_url,
        "namespace": doc.namespace,
        "slug": doc.slug,
        "group_code": doc.group_code,
        "group": doc.group_name,
        "tab_code": doc.tab_code,
        "tab": doc.tab_name,
        "breadcrumb": doc.breadcrumb,
        "doc_id": doc.doc_id,
        "updated_at": doc.updated_at,
        "local_path": str(doc.local_md.relative_to(root)),
        "raw_html_path": str(doc.raw_html.relative_to(root)),
        "headings": doc.headings,
        "snippet": doc.snippet,
        "content_chars": doc.content_chars,
        "html_sha256": doc.html_sha256,
    }


def build_index(root: Path, groups: list[dict[str, Any]], docs: list[DocRef], failures: list[dict[str, Any]]) -> None:
    crawl_time = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(timespec="seconds")
    records = [doc_record(doc, root) for doc in docs if doc.local_md and doc.local_md.exists()]
    write_json(root / "metadata" / "groups.json", groups)
    write_json(root / "metadata" / "documents.json", records)
    write_jsonl(root / "metadata" / "documents.jsonl", records)
    write_json(root / "metadata" / "failures.json", failures)

    counts_by_group: dict[str, int] = {}
    counts_by_tab: dict[str, int] = {}
    for record in records:
        counts_by_group[record["group"]] = counts_by_group.get(record["group"], 0) + 1
        key = f'{record["group"]} / {record["tab"]}'
        counts_by_tab[key] = counts_by_tab.get(key, 0) + 1

    manifest = {
        "name": "钉钉开放平台文档中心知识库",
        "source_entry": "https://open.dingtalk.com/document/dingstart/basic-concepts-beta",
        "crawl_time": crawl_time,
        "source_apis": [GROUPS_API, TREE_API, OSS_BASE],
        "groups": len(groups),
        "tabs": sum(len(g.get("tabs") or []) for g in groups),
        "documents_discovered": len(docs),
        "documents_written": len(records),
        "failures": len(failures),
        "counts_by_group": counts_by_group,
        "counts_by_tab": counts_by_tab,
    }
    write_json(root / "MANIFEST.json", manifest)

    lines = [
        "# 钉钉开放平台文档中心知识库",
        "",
        f"- 抓取时间：{crawl_time}",
        f"- 入口：{manifest['source_entry']}",
        f"- 覆盖：{manifest['groups']} 个大类，{manifest['tabs']} 个 tab，{manifest['documents_written']} 篇 Markdown",
        f"- 失败：{manifest['failures']} 篇，详见 `metadata/failures.json`",
        "",
        "## Agent 使用方式",
        "",
        "1. 先读 `MANIFEST.json` 和 `INDEX.md` 确认覆盖范围。",
        "2. 用 `rg \"关键词\" docs metadata/documents.jsonl` 检索正文和元数据。",
        "3. 每篇 Markdown 开头都有 `source_url`、`namespace`、`slug`、`group`、`tab`、`breadcrumb`、`updated_at`。",
        "4. 优先引用 Markdown 内的 `Source` 原始链接；遇到内容冲突，以 `updated_at` 更新的页面为准。",
        "5. `raw_html/` 保存了原始正文 HTML，适合检查表格、图片或 Markdown 转换边界。",
        "",
        "## 目录",
        "",
        "- `docs/`：按大类/tab 分组的 Markdown 正文。",
        "- `raw_html/`：OSS 原始 HTML。",
        "- `metadata/documents.jsonl`：逐篇文档索引，适合 agent 读取或导入向量库。",
        "- `metadata/failures.json`：失败清单和异常信息。",
        "",
        "## 覆盖统计",
        "",
    ]
    for group, count in sorted(counts_by_group.items(), key=lambda item: item[0]):
        lines.append(f"- {group}: {count}")
    (root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    index_lines = ["# INDEX", ""]
    by_group_tab: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in records:
        by_group_tab.setdefault((record["group"], record["tab"]), []).append(record)
    for (group, tab), items in sorted(by_group_tab.items(), key=lambda item: (item[0][0], item[0][1])):
        index_lines.append(f"## {group} / {tab}")
        index_lines.append("")
        for item in items:
            rel = item["local_path"].replace(" ", "%20")
            breadcrumb = " > ".join(item["breadcrumb"])
            updated = f" `{item['updated_at']}`" if item.get("updated_at") else ""
            index_lines.append(f"- [{item['title']}]({rel}){updated} - `{item['namespace']}/{item['slug']}` - {breadcrumb}")
        index_lines.append("")
    (root / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    guide = [
        "# AGENT_GUIDE",
        "",
        "这份知识库适合代码 agent、研究 agent、Claude Code/Codex 等直接检索使用。",
        "",
        "## 推荐检索",
        "",
        "```bash",
        "rg \"access_token|事件订阅|机器人|JSAPI|智能硬件\" docs metadata/documents.jsonl",
        "jq -r 'select(.group==\"应用开发\" and .tab==\"服务端API\") | [.title,.source_url,.local_path] | @tsv' metadata/documents.jsonl",
        "```",
        "",
        "## 字段含义",
        "",
        "- `group`：文档中心左侧一级分类，例如应用开发、连接平台、硬件开发。",
        "- `tab`：同一分类下的顶部/二级 tab，例如服务端API、客户端JSAPI。",
        "- `breadcrumb`：文档树路径，能定位文档所属功能域。",
        "- `namespace/slug`：钉钉文档 URL 的稳定路径片段。",
        "- `updated_at`：原页面 `<meta name=\"gmtModify\">` 时间。",
        "",
        "## 注意",
        "",
        "- 本知识库是静态快照；实时变更请重新运行 `work/build_dingtalk_open_docs_kb.py`。",
        "- Markdown 中的站内链接会尽量改写为本地相对链接；未在本次目录树内的链接保留为开放平台 URL。",
        "- 图片保留远程 URL，不下载到本地。",
    ]
    (root / "AGENT_GUIDE.md").write_text("\n".join(guide) + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build_dingtalk_open_docs_kb.py <output-dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).expanduser().resolve()
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)

    print(f"Output: {root}")
    groups_payload = get_json(GROUPS_API)
    if not groups_payload.get("success"):
        raise RuntimeError(f"Failed to fetch groups: {groups_payload}")
    groups = groups_payload.get("result") or []
    tabs = collect_tabs(groups)
    print(f"Groups: {len(groups)}, tabs: {len(tabs)}")

    raw_tree_dir = root / "raw_api" / "trees"
    raw_tree_dir.mkdir(parents=True, exist_ok=True)
    all_docs: list[DocRef] = []
    for idx, tab in enumerate(tabs, start=1):
        payload = get_json(TREE_API, {"tabCode": tab.tab_code})
        write_json(raw_tree_dir / f"{tab.tab_code}.json", payload)
        if not payload.get("success"):
            print(f"Warning: failed tree for {tab.tab_name}: {payload}", file=sys.stderr)
            continue
        docs = flatten_tree(payload.get("result") or [], tab)
        all_docs.extend(docs)
        print(f"[{idx:02d}/{len(tabs)}] {tab.group_name}/{tab.tab_name}: {len(docs)} docs")
        time.sleep(0.05)

    # Keep stable ordering and fail fast on duplicate URLs.
    seen: set[str] = set()
    deduped: list[DocRef] = []
    for doc in all_docs:
        if doc.doc_url in seen:
            continue
        seen.add(doc.doc_url)
        deduped.append(doc)
    all_docs = deduped
    make_output_paths(root, all_docs)
    local_map = {doc.doc_url: doc.local_md for doc in all_docs if doc.local_md is not None}

    print(f"Documents to fetch: {len(all_docs)}")
    failures: list[dict[str, Any]] = []
    completed = 0
    max_workers = min(10, max(4, (os.cpu_count() or 4)))
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_and_write_doc, doc, local_map) for doc in all_docs]
        for future in concurrent.futures.as_completed(futures):
            doc, failure = future.result()
            if failure:
                failures.append(failure)
            completed += 1
            if completed % 100 == 0 or completed == len(all_docs):
                print(f"Fetched {completed}/{len(all_docs)}; failures={len(failures)}")

    build_index(root, groups, all_docs, failures)
    print(f"Done. Wrote {len(all_docs) - len(failures)} docs, failures={len(failures)}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
