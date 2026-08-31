---
title: "DingTalk CLI — 让 AI 真正帮你在钉钉里干活"
source_url: "https://open.dingtalk.com/document/development/dingtalk-cli-performing-tasks-within"
namespace: "development"
slug: "dingtalk-cli-performing-tasks-within"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "新手入门 > DingTalk CLI — 让 AI 真正帮你在钉钉里干活"
doc_id: "vph4EMZ206"
updated_at: "2026-07-14 09:22:39"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-cli-performing-tasks-within
> Path: 应用开发 / 钉钉 CLI / 新手入门 > DingTalk CLI — 让 AI 真正帮你在钉钉里干活
> Updated: 2026-07-14 09:22:39

# DingTalk CLI — 让 AI 真正帮你在钉钉里干活

## **背景**

强大的 AI 推理能力若缺乏工具操作接口，将无法在钉钉内实现闭环。**DingTalk Workspace CLI (dws)** 作为连接 AI Agent 与钉钉生态的核心基础设施，旨在解决这一集成壁垒。

dws 将钉钉全链路产品能力（包括 AI 表格、日历、通讯录、群聊、审批等）封装为标准化命令行接口。在用户授权与预览确认机制的保障下，Agent 可安全访问并操作个人数据（如消息、日程、文档），实现跨应用的自动化工作流。

DingTalk CLI 现已开源，现在就让你的 AI 拥有行动力：👉 **获取代码**：[GitHub 开源仓库](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli)

### **CLI许愿墙**

你是否在终端敲完命令后，还得手动切换到钉钉发通知？是否希望自动化流程能直接联动钉钉——自动发消息、建待办、拉群聊？想让钉钉 CLI 支持什么新能力？在[钉钉CLI许愿墙](https://docs.dingtalk.com/notable/share/form/v01eLbnj1bw1ELb0laN_dv19yqvsgs3oebp3pcjys_1qX0QQ0?source=link)许个愿吧！

我们会定期整理大家的建议，评估并同步采纳与排期进展。

### **快速入群**

使用钉钉扫描下方二维码，加入dws开源沟通群：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7001696771/p1070740.png)

## 一键安装

> **[!NOTE]**
>
> 需要 Go 1.25+。使用 `make package` 可交叉编译全平台产物（macOS / Linux / Windows × amd64 / arm64）。

### **方式一：脚本安装（推荐）**

macOS / Linux：

```
curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.sh | sh
```

Windows（PowerShell）：

```
irm https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.ps1 | iex
```

### **方式二：通过 Agent 自动安装**

将以下指令直接发送给你的 AI 工具（如 Cursor、Claude Code、TRAE），让它帮你完成安装：

```
帮我安装钉钉 CLI：https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli
```

### **方式三：npm 安装**

```
npm install -g dingtalk-workspace-cli
```

### **方式四：从源码构建**

```
git clone https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli.git
cd dingtalk-workspace-cli
go build -o dws ./cmd       # build to current directory
cp dws ~/.local/bin/         # install to PATH
```

## 自升级

dws 内置自升级能力，更新直接从 [GitHub Releases](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/releases) 拉取，支持 SHA256 完整性校验和自动备份：

```
dws upgrade                    # 交互式升级到最新版本
dws upgrade --check            # 仅检查是否有新版本
dws upgrade --list             # 列出所有可用版本
dws upgrade --version v1.0.7   # 升级到指定版本
dws upgrade --rollback         # 回滚到上一个版本
dws upgrade -y                 # 跳过确认提示
```

升级采用**两阶段原子流程**确保一致性：先下载并校验全部文件（任何步骤失败即中止，不影响现有安装），再统一替换二进制文件和技能包。每次升级前自动创建备份，可随时回滚。

升级过程遵循两阶段原子流程，以确保一致性：

- **准备阶段**——将平台特定的二进制文件和技能包下载到临时目录，验证 SHA256 校验和，并提取/验证所有文件。如果任何步骤失败，升级将中止，而不会修改现有安装。
- **应用**——只有在所有准备工作都成功之后，二进制文件才会被替换，技能包才会被安装到所有检测到的代理目录（`~/.agents/skills/dws`，，，等）。`~/.claude/skills/dws``~/.cursor/skills/dws`

每次升级前都会自动创建当前版本的备份。`dws upgrade --rollback`如有需要，可使用该备份恢复到之前的版本。

| **命令** | **命令说明** |
| --- | --- |
| `--check` | 无需安装即可检查更新。 |
| `--list` | 列出所有可用版本及其更新日志。 |
| `--version` | 升级到特定版本（例如`v1.0.7`）。 |
| `--rollback` | 回滚到之前的备份版本。 |
| `--force` | 即使已是最新版本，也必须强制重新安装。 |
| `--skip-skills` | 跳过技能包更新。 |
| `-y` | 跳过确认提示。 |

## 使用CLI

### **用户启用 CLI**

AI 可以访问你的个人日历、消息和文档，并代替你执行操作。这需要一次性的用户授权——运行以下命令，浏览器会自动打开，选择组织并完成授权即可：

```
dws auth login
```

对于无图形界面环境（Docker、SSH、CI），使用设备码模式：

```
dws auth login --device
```

> **[!NOTE]**
>
> 如果你的组织尚未开启 CLI 访问权限，系统会提示你向管理员发送申请。管理员一键审批后，重新运行 `dws auth login` 即可。

### 管理员：为组织开启 CLI 访问

前往 [开发者平台](https://open-dev.dingtalk.com/)**→ 更多→ 基本信息→ CLI 访问管理 → 开启**。

![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7001696771/p1070738.png)

### 自定义应用模式（CI/CD、ISV 集成）

面向企业管控场景，创建企业内部应用：

1. 进入[开放平台](https://open-dev.dingtalk.com/fe/app#/corp/app)，在应用开发下面，点击**创建应用**，填写应用的基本信息后，点击**保存**完成应用的创建。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7001696771/p1070764.png)
2. 进入创建的应用详情页，在**安全设置**模块中，填写重定向URL：`http://127.0.0.1,https://login.dingtalk.com`

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7001696771/p1070765.png)
3. 进入**版本管理与发布**模块，点击**创建新版本**按钮后，填写版本信息完成应用的发布。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7001696771/p1070766.png)
4. 执行以下命令，完成登录：

   > **[!NOTE]**
   >
   > 首次登录后凭证安全持久化（Keychain），后续运行自动刷新 Token。

   ```
   dws auth login --client-id <your-app-key> --client-secret <your-app-secret>
   ```

## 使用场景

### 🗂️ 会议纪要—自动提取待办并执行

你在会议里随口说了一句"那个文档我稍后发给你"，散会就忘了。现在，AI 直接从钉钉听记中识别出这条待办，帮你发文档、排后续跟进。你只需要确认，剩下的它来处理。

说了要发文件？AI 帮你发。需要安排复盘会？AI 查日历、拟邀请，你审核通过就行。

**进阶玩法—语音触发**：你可以设置触发词（比如"钉钉钉钉"），在会议中说"钉钉钉钉，帮我把这个方案整理成文档发给老板"。会后 AI 自动从听记转录中识别你的指令，提取为高优待办并执行。你不需要记住自己说了什么，AI 替你记。

| 用户指令 | AI 执行 |
| --- | --- |
| 读一下这份听记，把里面的待办提取出来，直接帮我处理。执行前先给我看方案。 | AI 解析听记内容，识别出待办事项（发送文档、约复盘会、更新表格），逐一展示执行计划，获得确认后依次完成：通过机器人发送文档到群聊、查询参会人日历找空闲时段创建日程、在 AI 表格中更新项目状态。 |

### 📊 AI 表格—数据管理全自动化

AI 表格是钉钉 CLI 覆盖最深的产品域，提供 20 条命令，支持表格/数据表/字段/记录的完整 CRUD 操作。你可以让 AI 从 CSV 批量导入数据、按条件筛选记录、批量更新字段、甚至搭建自动化看板。

| 用户指令 | AI 执行 |
| --- | --- |
| 把这份 CSV 里的客户数据导入到 AI 表格，自动建表并设好字段类型。 | AI 读取 CSV 结构，创建 AI 表格和数据表，逐一添加字段（文本/数字/日期/选项），然后批量导入全部记录。完成后返回表格链接。 |
| 帮我查一下项目跟踪表里所有"逾期"状态的记录，汇总发到项目群。 | AI 查询 AI 表格中状态为"逾期"的记录，格式化为摘要列表，通过机器人发送到指定群聊。 |

### 📅 日历—智能排会议

约一个多人会议，通常意味着手动翻日历找共同空闲时间，来回沟通 20 分钟。如果团队分布在不同时区，手动算时差更是头疼。

现在，只需告诉 AI"帮我和这个群的人下周约个会"。AI 自动拉取群成员、查询每个人的日历空闲、考虑所有时区，推荐几个"所有人都在合理工作时间内"的选项。你选一个，会议就约好了。

| 用户指令 | AI 执行 |
| --- | --- |
| 帮我查一下项目组所有人的日历，找下周一个小时的空闲时间开讨论会。 | AI 查询群成员列表，批量查询每人的闲忙状态，推荐最优时间段，创建日程并添加参与者。如果需要会议室，自动查询可用会议室并预定。 |
| 帮我看看我这周的日程安排。 | AI 拉取本周日历事件，按天分组展示，标注会议类型和参与人数。 |

**进阶玩法—会议效率分析**：让 AI 拉取你过去两周的日历数据，自动给每个会议打标签（1:1 / 项目同步 / 团队例会 / 个人事务），写入 AI 表格并生成看板。饼图看占比、柱状图看趋势——一眼看出哪些会议该砍。

| 用户指令 | AI 执行 |
| --- | --- |
| 拉取我过去两周的日历，给每个事件分类打标签，写入 AI 表格，创建看板。我想看时间都花哪了。 | AI 读取日历事件，按类型分类，写入 AI 表格，汇总各类别时长占比。 |

### 🤖 群聊与机器人—消息自动化中枢

钉钉 CLI 提供 10 条群聊命令，覆盖群的全生命周期管理：搜索群、建群、群成员管理、改群名，以及机器人群发、单聊、消息撤回、Webhook 通知。

| 用户指令 | AI 执行 |
| --- | --- |
| 帮我建一个"Q2 冲刺"项目群，把产品、设计、研发的核心成员拉进来。 | AI 通过通讯录搜索相关同事，创建群聊，批量添加成员，设置群名称。 |
| 每天早上 9 点把昨天的考勤异常汇总发到 HR 群。 | AI 查询考勤记录，筛选异常数据，格式化为摘要，通过机器人定时发送到指定群。 |

### ✅ 待办—任务不再遗漏

你知道自己有一堆事要做，但散落在聊天记录、会议纪要、邮件里，根本理不清。现在让 AI 帮你统一管理：批量创建待办、设置优先级和截止时间、每日汇总未完成事项、扫描逾期任务。

| 用户指令 | AI 执行 |
| --- | --- |
| 帮我把这份任务清单批量创建为钉钉待办，设好优先级和截止时间。 | AI 解析任务列表，逐条创建待办，设置执行人、优先级（紧急/高/中/低）和截止日期。 |
| 帮我看看有哪些逾期的待办。 | AI 查询所有待办，筛选已逾期未完成的任务，按逾期天数排序展示。 |

### 📝 审批—流程自动化

请假、报销、出差申请——这些重复性流程现在可以让 AI 代劳。AI 能发起审批实例、查询审批进度、处理待审批任务。

| 用户指令 | AI 执行 |
| --- | --- |
| 帮我提交一个下周一到周三的年假申请。 | AI 查询年假审批模板，填充日期和理由，发起审批实例。 |
| 查一下我发起的报销审批到哪一步了。 | AI 查询你发起的审批实例列表，筛选报销类型，展示当前审批节点和状态。 |

### 📋 日志—日报周报一键提交

每周五下午写周报是不是最痛苦的事？现在让 AI 帮你：它可以查询你本周的日历事件、待办完成情况、群聊关键讨论，自动整理成周报模板并提交。

| 用户指令 | AI 执行 |
| --- | --- |
| 帮我根据本周的工作内容写一份周报并提交。 | AI 汇总本周日历事件和已完成待办，按照钉钉日志模板格式整理内容，创建并提交周报。 |
| 帮我看看今天收到了哪些日报。 | AI 查询今日收件箱中的日志，展示发送人、标题和关键内容摘要。 |

## 钉钉CLI能力覆盖

DingTalk CLI 覆盖 13 个产品共 159 条命令。

| **服务** | **命令** | **命令数** | **子命令示例** | **描述** |
| --- | --- | --- | --- | --- |
| 通讯录 | `contact` | 6 | `user` `dept` | 按姓名/手机号搜索、批量查询、部门树、当前用户信息 |
| 群聊 | `chat`（别名 `im`） | 23 | `message` `group` `bot` `conversation-info` `search` `search-common` `list-top-conversations` | 消息（发送 / 列表 / list-all / 按发送者 / @我 / 关注 / 未读 / 话题回复 / 搜索）、群增删改 + 成员管理（含 `add-bot`）、机器人身份消息（`send-by-bot` / `recall-by-bot` / `send-by-webhook`）、会话信息查询、共同群聊 |
| 日历 | `calendar` | 14 | `event` `room` `participant` `busy` | 日程 CRUD + 建议时间 + 附件、会议室预订、闲忙查询、参与者管理 |
| 待办 | `todo` | 6 | `task` | 创建、列表、修改、完成、详情、删除 |
| 审批 | `oa` | 9 | `approval` | 同意 / 拒绝 / 撤销、待我审批 / 我发起的、流程列表、操作记录 |
| 考勤 | `attendance` | 4 | `record` `shift` `summary` `rules` | 打卡记录、排班查询、考勤摘要、考勤组规则 |
| DING | `ding` | 2 | `message` | 发送 / 撤回 DING 消息 |
| 日志 | `report` | 7 | `create` `list` `detail` `template` `stats` `sent` | 创建日志、收发列表、模板、详情、统计 |
| AI 表格 | `aitable` | 41 | `base` `table` `record` `field` `view` `dashboard` `chart` `import` `export` `attachment` `template` | Base / 数据表 / 记录 / 字段 / 视图 全量 CRUD；图表 + 仪表盘（含分享配置）；数据导入导出；附件；模板 |
| 文档 | `doc` | 21 | `search` `list` `info` `read` `create` `update` `upload` `download` `copy` `move` `rename` `file` `folder` `block` `comment` | 搜索 / 读写文档、文件与文件夹创建、块级编辑、评论（list / create / reply / create-inline）、上传 / 下载 |
| 钉盘 | `drive` | 6 | `list` `info` `download` `mkdir` `upload-info` `commit` | 钉盘文件操作：列表、详情、下载、创建文件夹、两阶段上传 |
| AI 听记 | `minutes` | 19 | `list` `get` `update` `mind-graph` `speaker` `hot-word` `upload` | 听记列表（我创建 / 共享给我）、详情（info / summary / keywords / transcription / todos / batch）、标题/摘要更新、思维导图、发言人替换、热词、上传会话 |
| 开发者文档 | `devdoc` | 1 | `article` | 搜索钉钉开放平台文档 |

> 运行 `dws --help` 查看顶层命令树，或 `dws<service> --help` 查看子命令。

## 安全设计

`dws`将安全性视为架构中的首要考量，而非事后考虑。**凭证绝不写入磁盘，令牌绝不离开受信任域，权限绝不超出授权范围，操作绝不逃过审计**——每一次 API 调用都必须经过钉钉开放平台的认证和审计链，绝无例外。

### **面向开发者**

| **机制** | **细节** |
| --- | --- |
| **加密令牌存储** | **采用PBKDF2 + AES-256-GCM**加密，密钥由设备物理 MAC 地址生成；跨平台 Keychain/DPAPI 集成提供额外保护——令牌无法在其他设备上解密。 |
| **输入安全** | 路径遍历保护（符号链接解析 + 工作目录包含）、CRLF 注入阻止、Unicode 视觉欺骗过滤——防止 AI 代理被恶意指令欺骗 |
| **域名允许列表** | `DWS_TRUSTED_DOMAINS`默认情况下`*.dingtalk.com`；持有者令牌永远不会发送到非允许列表域。 |
| **强制使用HTTPS** | 所有请求都需要 TLS 加密；开发期间仅允许通过 HTTP 进行环回通信。 |
| **试运行预览** | `--dry-run`显示调用参数而不执行，防止意外修改。 |
| **零凭证持久性** | 客户端 ID/密钥仅保存在内存中，绝不会写入配置文件或日志。 |

### **面向企业管理员**

| **机制** | **细节** |
| --- | --- |
| **OAuth 设备流程认证** | 用户必须通过管理员授权的钉钉应用程序进行身份验证。 |
| **最小权限范围** | CLI 只能调用应用程序被授予的 API——无法提升权限 |
| **允许列表门控** | 共同创建阶段需要管理员确认；计划推出自助审批功能。 |
| **全链审计** | 所有数据读写操作都通过钉钉开放平台API进行——企业管理员可以实时追踪完整的通话记录；任何异常操作都无法隐藏。 |

### **对于独立软件开发商 (ISV)**

| **机制** | **细节** |
| --- | --- |
| **租户数据隔离** | 在已授权的应用身份下运行；无法跨租户访问 |
| **技能沙盒** | 代理技能是 Markdown 文档（`SKILL.md`）——仅包含提示描述，不包含任意代码执行。 |
| **零盲点** | ISV-dws技能编排过程中的每一次API调用都强制通过钉钉开放平台认证——完整的调用链可追溯，没有任何绕过路径。 |

## 常用命令速查

| 目标 | 命令 |
| --- | --- |
| 登录授权 | `dws auth login` |
| 设备码登录（无界面环境） | `dws auth login --device` |
| 查看当前登录状态 | `dws auth status` |
| 搜索同事 | `dws contact user search --keyword "关键词"` |
| 查看日历事件 | `dws calendar event list` |
| 创建待办 | `dws todo task create --title "标题" --executors "<user_id>"` |
| 预览操作（不执行） | `dws <command> --dry-run` |
| 查看所有可用命令 | `dws --help` |
| 查看子命令 | `dws <product> --help` |
| 查看 API Schema | `dws schema` |
| 升级到最新版本 | `dws upgrade` |

## 常见问题

- **安装后提示"command not found"？**

  确保 CLI 安装目录已添加到系统 PATH。使用脚本安装的用户，重新打开终端窗口即可。macOS 用户如遇"无法打开，因为 Apple 无法检查其是否包含恶意软件"，运行：`xattr -d com.apple.quarantine /path/to/dws`
- **组织未开启 CLI 访问怎么办？**

  登录时选择组织后，点击"立即申请"通知管理员。管理员收到申请卡片后一键审批，审批通过后重新运行 `dws auth login`。
- **企业管理员如何管控权限？**

  CLI 本质上是通过钉钉应用调用开放平台 API。应用管理仍遵循企业现有的安全和访问控制策略。管理员可在开发者后台的"CLI 访问管理"中开启或关闭。
- **如何在自动化任务或 AI 工作流中使用？**

  在本地完成一次配置和授权后，即可将 CLI 集成到你的脚本或 AI Agent 平台中复用。所有命令支持 `--yes` 跳过交互确认，`--format json` 输出结构化数据。
- **调用 API 时提示"权限不足"？**

  根据错误信息中提示的缺失权限，在开发者后台为应用授予对应权限。使用 `dws auth login --device` 重新授权以刷新权限范围。
