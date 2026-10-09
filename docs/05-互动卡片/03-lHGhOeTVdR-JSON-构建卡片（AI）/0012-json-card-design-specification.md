---
title: "设计规范"
source_url: "https://open.dingtalk.com/document/development/json-card-design-specification"
namespace: "development"
slug: "json-card-design-specification"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 设计规范"
doc_id: "aq9qSttIYR"
updated_at: "2026-09-30 09:14:06"
---

> Source: https://open.dingtalk.com/document/development/json-card-design-specification
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 设计规范
> Updated: 2026-09-30 09:14:06

# 设计规范

## 设计原则

- **默认用客户端背景**

  - 除非内容需要，不要给最外层卡片设背景。
  - 局部区域可用背景建立层次。
- **生成中要有状态**

  - Agent 生成或执行时，Markdown 的 content 可前置 `[AIGenerating]`。
  - 完成、失败或取消后移除该标记并更新文案
- **执行细节收起来**

  - 用 `CollapsiblePanel` 配 `variant: "reasoning"` 承载推理或执行过程。

## 适用范围

本文只覆盖 JSON 构建这条链路的组件级设计约定。 卡片在 IM、吊顶、工作台等场域下的尺寸与视觉规范与构建方式无关， 两条链路共用，见开放平台的[卡片规范](https://open.dingtalk.com/document/development/card-specification-1)。

> **[!NOTE]**
>
> - 校验通过不代表视觉正确。
> - 信息完整性、层次与密度不是 lint 能检查的， 需要人工评审，并在目标客户端上确认最终效果。

## 内容区块规划

- 先想清楚用户最需要知道或做什么，再安排结论、依据、细节与操作。
- 报表可以结论先行， 执行卡可以进度先行。
- **内容短就不需要额外区块**，下表是可选的组合参考，不是固定顺序。

| **角色** | **用途** | **常用组件** |
| --- | --- | --- |
| header | 标题、来源与状态 | Row + Text + Tag |
| hero | 关键封面或人物图 | Image |
| facts | 标签—数值型事实 | Column + Row + Text |
| summary | 结论先行的说明文字 | Markdown |
| metrics | 少量关键指标 | Row + Column + Text |
| data | 对比、趋势或构成 | Table / Chart |
| list | 重复条目 | Column + Card + Text |
| timeline | 按时间或阶段排列的进展 | Column + Row + Text + Tag |
| attachments | 文件结果 | Divider + Text + File |
| form | 文本与选择输入 | TextField + ChoicePicker |
| actions | 主操作与次操作 | Divider + Row + Button + Text |
| details | 不常看的补充信息 | CollapsiblePanel + Markdown + Link |
| progress | 生成或执行阶段 | CollapsiblePanel + Markdown |
| terminal-status | 完成、失败或取消的稳定态 | Tag + Text + Link |

## 字号规范

- 用于 `Text.sizeToken`。
- 优先选带 `__font_size` 后缀的完整 ID。
- 实际字号由当前客户端解析，**不保证跨平台字号与行高一致**，也不会自动套用同名字体样式。

| **Token** | **用途** |
| --- | --- |
| common\_largetitle\_text\_style\_\_font\_size | 大标题，用作页面或主要内容区的标题。 |
| common\_supertitle\_text\_style\_\_font\_size | 特大标题，用作页面或模块的主标题。 |
| common\_h1\_text\_style\_\_font\_size | 一级标题，用于卡片或内容区的标题。 |
| common\_h2\_text\_style\_\_font\_size | 二级标题，用于内容分组的标题。 |
| common\_h3\_text\_style\_\_font\_size | 三级标题，用于更小层级的内容标题。 |
| common\_h4\_text\_style\_\_font\_size | 四级标题，用于副标题或标题下的补充信息。 |
| common\_body\_text\_style\_\_font\_size | 正文，用于主要内容。 |
| common\_action\_text\_style\_\_font\_size | 操作文字，用于按钮、链接等操作类文案。 |
| common\_description\_text\_style\_\_font\_size | 辅助说明，用于次要信息和补充说明。 |
| common\_footnote\_text\_style\_\_font\_size | 脚注，用于来源、备注、图片说明或状态标签。 |
| common\_tiny\_text\_style\_\_font\_size | 小号提示文字，用于空间受限场景中的轻提示。 |
| common\_subhead\_text\_style\_\_font\_size | 副标题，用于标题下方的补充信息。 |

## 色彩体系

- 只允许使用下列 Token ID，**区分大小写**。
- 实际色值与透明度由客户端按当前平台与主题解析， 协议不固定色值。
- 同一张卡片内，一个 Token 只表达一种含义。

### 语义色

| **Token** | **用途** |
| --- | --- |
| extended\_yellow0\_color | 黄色背景色，用于该色系区域的背景填充。 |
| extended\_yellow1\_color | 黄色边框色，用于该色系区域的描边。 |
| extended\_yellow6\_color | 黄色文字色，用于该色系的文字强调。 |
| extended\_orange0\_color | 橙色背景色，用于该色系区域的背景填充。 |
| extended\_orange1\_color | 橙色边框色，用于该色系区域的描边。 |
| extended\_orange6\_color | 橙色文字色，用于该色系的文字强调。 |
| common\_orange1\_color | 警示状态色，用于需要用户注意的提示。 |
| extended\_red0\_color | 红色背景色，用于该色系区域的背景填充。 |
| extended\_red1\_color | 红色边框色，用于该色系区域的描边。 |
| extended\_red6\_color | 红色文字色，用于该色系的文字强调。 |
| common\_red1\_color | 危险状态色，用于传达危险或错误的语义。 |
| extended\_magenta0\_color | 品红背景色，用于该色系区域的背景填充。 |
| extended\_magenta1\_color | 品红边框色，用于该色系区域的描边。 |
| extended\_magenta6\_color | 品红文字色，用于该色系的文字强调。 |
| extended\_purple0\_color | 紫色背景色，用于该色系区域的背景填充。 |
| extended\_purple1\_color | 紫色边框色，用于该色系区域的描边。 |
| extended\_purple6\_color | 紫色文字色，用于该色系的文字强调。 |
| extended\_deeppurple0\_color | 深紫背景色，用于该色系区域的背景填充。 |
| extended\_deeppurple1\_color | 深紫边框色，用于该色系区域的描边。 |
| extended\_deeppurple6\_color | 深紫文字色，用于该色系的文字强调。 |
| extended\_blue0\_color | 蓝色背景色，用于该色系区域的背景填充。 |
| extended\_blue1\_color | 蓝色边框色，用于该色系区域的描边。 |
| extended\_blue6\_color | 蓝色文字色，用于该色系的文字强调。 |
| extended\_darkgreen0\_color | 深绿背景色，用于该色系区域的背景填充。 |
| extended\_darkgreen1\_color | 深绿边框色，用于该色系区域的描边。 |
| extended\_darkgreen6\_color | 深绿文字色，用于该色系的文字强调。 |
| extended\_green0\_color | 绿色背景色，用于该色系区域的背景填充。 |
| extended\_green1\_color | 绿色边框色，用于该色系区域的描边。 |
| extended\_green6\_color | 绿色文字色，用于该色系的文字强调。 |
| common\_green1\_color | 成功状态色，用于成功或完成的反馈。 |

### 层级与功能

| **Token** | **用途** |
| --- | --- |
| common\_level1\_base\_color | 一级文字与图标，用于标题、正文等主要信息。 |
| common\_level2\_base\_color | 二级文字与图标，用于次要信息和辅助图标。 |
| common\_level3\_base\_color | 三级文字与图标，用于更弱的补充信息。 |
| common\_level4\_base\_color | 禁用状态的文字与图标颜色；只表达视觉状态。 |
| common\_stamp\_color | 水印色，用于低干扰的水印内容。 |
| common\_link\_color | 超链接文字与高亮边框颜色。 |
| common\_bg\_color | 区域背景色，用于页面或内容区的背景。 |
| common\_fg\_z1\_color | 前景区域背景色，用于叠在基础背景之上的内容区。 |
| common\_line\_light\_color | 弱分割线，用于较轻的内容分隔。 |
| common\_line\_hard\_color | 强分割线，用于需要更清晰边界的内容分隔。 |

### 中性色

| **Token** | **用途** |
| --- | --- |
| common\_white1\_color | 白色蒙层，用于白色叠加，实际透明度由客户端主题资源决定。 |
| common\_white2\_color | 白色蒙层（设计为 40% 档），用于白色叠加，实际透明度由客户端主题资源决定。 |
| common\_white3\_color | 白色蒙层（设计为 30% 档），用于白色叠加，实际透明度由客户端主题资源决定。 |
| common\_white4\_color | 白色蒙层（设计为 20% 档），用于白色叠加，实际透明度由客户端主题资源决定。 |
| common\_white5\_color | 白色蒙层（设计为 10% 档），用于白色叠加，实际透明度由客户端主题资源决定。 |
| common\_white6\_color | 白色蒙层（设计为 5% 档），用于白色叠加，实际透明度由客户端主题资源决定。 |
| common\_black1\_color | 黑色蒙层，用于黑色叠加，实际透明度由客户端主题资源决定。 |
| common\_black2\_color | 黑色蒙层（设计为 40% 档），用于黑色叠加，实际透明度由客户端主题资源决定。 |
| common\_black3\_color | 黑色蒙层（设计为 30% 档），用于黑色叠加，实际透明度由客户端主题资源决定。 |
| common\_black4\_color | 黑色蒙层（设计为 20% 档），用于黑色叠加，实际透明度由客户端主题资源决定。 |
| common\_black5\_color | 黑色蒙层（设计为 10% 档），用于黑色叠加，实际透明度由客户端主题资源决定。 |
| common\_black6\_color | 黑色蒙层（设计为 5% 档），用于黑色叠加，实际透明度由客户端主题资源决定。 |

### 主题色

| **Token** | **用途** |
| --- | --- |
| theme\_primary3\_color | 主题背景色，用于承载主题样式的区域背景。 |
| theme\_primary2\_color | 浅主题色，用于较浅的主题色高亮和辅助装饰。 |
| theme\_primary\_hover\_color | 主题悬停色，用于指针悬停时主题色的视觉反馈。 |
| theme\_primary1\_color | 主题主色，用于主要的主题强调。 |
| theme\_primary\_press\_color | 主题按下色，用于按下时主题色的视觉反馈。 |

## 图标库

- 用于 `Icon.name`，区分大小写。
- **不要臆造图标名**，找不到合适的就用素材或文字表达。

| **图标名** | **含义与用法** |
| --- | --- |
| Search\_L\_outlined | 搜索。用于搜索、搜索内容、搜索文件、搜索图片。 |
| Language\_L\_outlined | 语言切换图标，常用于联网搜索。 |
| CodeProgram\_L\_outlined | 代码。用于在终端中运行命令。 |
| Picture\_L\_outlined | 图片。用于生成图片。 |
| Folder\_L\_outlined | 文件夹。用于读取文件。 |
| Edit\_L\_outlined | 编辑或笔图标。用于写入和创建文件。 |
| ListView\_L\_outlined | 列表视图 1。用于列出文件。 |
| ManagementBackground\_L\_outlined | 管理后台图标，常用于浏览器访问。 |
| Tool\_L\_outlined | 工具。用于调用工具、Workspace 工具集、MCP 工具集、DWS 工具集、MCP 调用，以及通用兜底。 |
| Delete\_L\_outlined | 删除。用于删除文件。 |
| SpinLoading\_L\_outlined | 加载中图标。用于 Skill 加载等加载状态；图标名本身不会开启旋转动画。 |
| UploadOne\_L\_outlined | 上传。用于上传文件。 |
| DownloadAndSave\_L\_outlined | 下载并保存。用于下载文件。 |
| Check\_L\_outlined | 对勾。用于表示完成或成功。 |
| Copy\_L\_outlined | 复制。用于复制文字、内容或结果。 |
| Close\_L\_outlined | 关闭、叉号。用于关闭弹窗、面板或页面。 |
| More\_L\_outlined | 更多、省略号、三个点。用于打开更多操作菜单。 |
| Error\_L\_outlined | 警告、错误提醒、带感叹号的圆圈。用于表示操作失败或异常状态。 |
| InformationThere\_L\_outlined | 信息提示，圆形字母 i。用于显示说明或附加信息。 |
| Setting\_L\_outlined | 设置、齿轮。用于打开设置或调整配置。 |
| ExpandThere\_L\_outlined | 展开。用于放大内容区或展开面板。 |
| Collapse\_L\_outlined | 收起。用于缩小内容区或收起面板。 |
| Link\_L\_outlined | 链接、链条。用于插入链接或打开相关地址。 |
| Share\_L\_outlined | 分享、转发。用于分享内容、会话或结果。 |
