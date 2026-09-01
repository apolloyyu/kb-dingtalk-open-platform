# kb-dingtalk-open-platform — 钉钉开放平台文档知识库

钉钉开放平台文档中心的完整本地知识库——**拿到文件夹即可离线技术答疑**，无需联网、向量库或任何第三方依赖。

| | |
|---|---|
| 内容 | 官方文档中心全量快照：8 大类 / 26 子类 / **3781 篇** Markdown |
| 快照日期 | 2026-09-01（权威值见 [meta/source_manifest.json](meta/source_manifest.json) 的 crawl_time） |
| 检索设施 | 三级索引（107 文件）· 关系图谱（5 张边表，8124 条互链）· `dkdoc` 查询 CLI |
| 维护方式 | 重爬 → 按 `doc_id` 对账 → 全量重建派生层 → lint（[ops/INGEST.md](ops/INGEST.md)） |
| 使用定位 | **外挂文件夹**：不作为 Agent 工作区（cwd），挂给任意 Agent 使用 |

## 快速开始

把下面这句话交给任意 Agent：

> 钉钉开放平台知识库在 `<本目录绝对路径>`，先读其中 AGENTS.md，再回答我的问题。

Agent 读完 [AGENTS.md](AGENTS.md) 即掌握全部用法。人类直接查也行：

```bash
python3 <路径>/bin/dkdoc ctx 免登               # ★一次打包:实体命中+正文+相邻篇+审计行
python3 <路径>/bin/dkdoc find 免登 小程序       # 找文档
python3 <路径>/bin/dkdoc api 创建群             # 查接口
python3 <路径>/bin/dkdoc err invalidDept        # 查错误码（未命中自动全文兜底）
python3 <路径>/bin/dkdoc cat <路径|slug>        # 读正文
```

## 目录结构

```
AGENTS.md                   Agent 操作手册：定位/最佳实践/找不到怎么办/ingest/维护  ← 入口
bin/dkdoc                   查询 CLI：ctx/find/api/err/event/jsapi/perm/links/cat/grep（python3 标准库）
index/
  INDEX.md                  L1 总索引：26 子类 + 一句话路由提示
  <大类>/<子类>.md           L2 子类清单；>200 篇的大类目再按功能域拆 L3
  TOPICS.md                 高频主题 → 权威文档直达（唯一人工维护的索引页）
graph/
  GRAPH.md                  图谱说明 + jq 查询配方
  links.jsonl               文档互链 8124 条边；hubs.md 被引用 Top100 枢纽榜
  api/event/errcode/permission.jsonl   接口/事件/错误码/权限点 四张实体表
docs/                       3781 篇正文快照（每篇头部带 source_url/breadcrumb/updated_at）
meta/                       documents.jsonl（逐篇元数据+sha256）· kb_manifest.jsonl（T0-T2/DROP 分层）
                            tombstones.jsonl（下线留档）· source_manifest.json · UNAVAILABLE.md
ops/
  INGEST.md                 变更维护协议（原则/流程/决策表/验收清单）
  changes/                  每次快照对账报告（变更日志）
  scripts/                  爬虫 + 4 个生成器 + diff_snapshot + lint（全部幂等、cwd 无关）
```

## 设计：三层架构

沿用 LLM Wiki 范式（原始层不可改 / 编译层脚本维护 / 认知层 LLM 策展），针对"上游可全量重爬"做了简化：

| 层 | 位置 | 谁维护 | 纪律 |
|---|---|---|---|
| 原始层（上游镜像） | `docs/` `meta/` | 爬虫，快照整体换入 | 只读；`doc_id` 为稳定身份，删除写 tombstone |
| 结构层（派生索引） | `index/`* `graph/`* | 脚本全量重建，从不增量修补 | 生成物勿手改，lint 会报漂移 |
| 认知层（人工策展） | `index/TOPICS.md` 及各入口文件 | 人 / LLM | 只收会饱和的高频主题；快照更新后复核 |

<sub>* `index/TOPICS.md` 与 `graph/GRAPH.md` 属认知层，生成器不触碰。</sub>

检索采用**渐进式披露**：高频主题（TOPICS）→ 精确实体（graph 四表）→ 领域浏览（L1→L2→L3）→ 全文兜底（grep），多数问题在前两层解决。

## 维护

```bash
python3 ops/scripts/build_dingtalk_open_docs_kb.py <新快照目录>   # 1. 重爬
python3 ops/scripts/diff_snapshot.py <新快照目录>                 # 2. 对账预览（增/删/改/移四张清单）
python3 ops/scripts/diff_snapshot.py <新快照目录> --apply         # 3. 换层 + 全量重建 + lint
#  4. 按报告复核 index/TOPICS.md（唯一需要 LLM 的步骤）
#  5. git commit —— diff 天然暴露本次快照的全部增删改
```

完整协议（五条原则、变更决策表、新鲜度验收清单）见 [ops/INGEST.md](ops/INGEST.md)；日常体检 `python3 ops/scripts/lint.py`（7 项只读检查）。

## 边界

- 静态快照，时效止于 2026-09-01；时效敏感问题（计费/灰度/上线时间）以线上为准。
- 源站 90MB 原始 HTML（`raw_html/`）未收编，需要时回源 dump 查转换边界。
- 已知抓取盲区见 [meta/UNAVAILABLE.md](meta/UNAVAILABLE.md) 与 `meta/failures.json`（1 篇失败）。
- 文档内容版权归钉钉官方；本仓库提供快照的组织方式、索引与工具。

## dws 域(已迁移)

dws CLI 整理版知识库已独立为 [kb-dws-wiki](https://github.com/apolloyyu/kb-dws-wiki) 仓库(知识库组按「一库一仓」组织,权限与生命周期独立)。

## 更新机制与协作规则

本仓库是**知识库组**的一员,遵循 KB Spec v1(布局与元数据见 `meta/MANIFEST.json`)。

- **正规更新通道**:自动流水线(每日爬取官方文档站→doc_id 对账→索引/图谱重建→lint 门禁→直推),无变化不产生提交
- **可以手改的**:认知/策展层(如 TOPICS、README、AGENTS)欢迎直接 PR;
- **不要手改的**:docs/(上游镜像,下次 ingest 覆盖)与 index/graph/meta 派生层(脚本全量重建);文档勘误写入 index/TOPICS.md 对应主题并注明与官方原文的分歧
- 勘误与建议:提 Issue,或联系维护人(MANIFEST 的 contact)。
