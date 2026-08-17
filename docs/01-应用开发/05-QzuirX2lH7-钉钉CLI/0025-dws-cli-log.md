---
title: "更新日志"
source_url: "https://open.dingtalk.com/document/development/dws-cli-log"
namespace: "development"
slug: "dws-cli-log"
group: "应用开发"
tab: "钉钉CLI"
breadcrumb: "更新日志"
doc_id: "JqaPUpyWXl"
updated_at: "2026-08-10 16:30:16"
---

> Source: https://open.dingtalk.com/document/development/dws-cli-log
> Path: 应用开发 / 钉钉CLI / 更新日志
> Updated: 2026-08-10 16:30:16

# 更新日志

## **钉钉 CLI 开源**

### **版本安装/升级**

使用过程中，执行下方命令即可将 dws 升级至最新稳定版，解锁更多钉钉能力。

```
# 升级到最新稳定版
dws upgrade

# 或安装最新 beta
dws upgrade --beta

# 查看完整版本历史
dws upgrade --list
```

### **了解更多**

- 您可前往 [GitHub 仓库](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli)查看并下载最新代码。
- 如有宝贵建议或想法，欢迎提交至[许愿墙](https://docs.dingtalk.com/notable/share/form/v01eLbnj1bw1ELb0laN_dv19yqvsgs3oebp3pcjys_1qX0QQ0?source=link)，我们将尽快安排专员与您联系沟通。
- 钉钉 CLI 每周发布更新，开发者可扫描下方二维码加入"**dwa 开源沟通群**"获取最新动态。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6160536871/p1094200.png)

## **2026-08-07**

### **更新说明**

本周CLI 聚焦 **钉钉文档与知识库、日历邮件与 AI 听记、IM 与 OA 协作、Agent 与 Schema 体验** 四大方向，共发布 [v1.0.56](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/releases/tag/v1.0.56) / [v1.0.57](https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli/releases/tag/v1.0.57) 两个稳定版及多个 beta 版本。

### **新增功能**

#### 钉钉文档与知识库

- **钉钉文档快捷操作** ：支持安全下载、内容历史查看、审阅、媒体处理、样式调整和访问共享等工作流。

  > **[!NOTE]**
  >
  > 涉及修改或授权时仍需先确认。

  - 相关命令：`dws doc +fetch`、`dws doc +export`、`dws doc +history-list`、`dws doc +review`、`dws doc +media-download`、`dws doc +background-update`、`dws doc +access-grant`
- **文档内嵌白板工作流** ：支持插入、读取和更新白板内容，可上传 Vector/SVG 资源。

  > **[!NOTE]**
  >
  > 插入和更新写入前需确认。

  - 相关命令：`dws doc whiteboard insert`、`dws whiteboard query`、`dws whiteboard update`、`dws doc media upload`
- **知识库动态查询** ：按游标分页查询文档更新、上传与评论动态，可排除指定文件。

  - 相关命令：`dws wiki feed list`
- **AI 表格工作流编辑参考** ：获取服务端工作流编辑说明与 `workflow-dsl/v1` 示例。

  - 相关命令：`dws aitable workflow edit-example`

#### **日历、邮件与听记**

- **循环日程实例查询** ：按事件 ID、时间范围和游标查询具体实例。

  - 相关命令：`dws calendar event instances`
- **企业邮箱日历与邮件工作流** ：查询邮箱日历及日程、导出邮件为本地文件、分享邮件到单聊。

  - 相关命令：`dws mail calendar list`、`dws mail calendar-event list`、`dws mail message export`、`dws mail message share-to-chat`
- **AI 听记补齐能力** ：删除个人热词、为用户申请指定级别听记权限、按时间或游标查询语音备忘列表。

  - 相关命令：`dws minutes hot-word delete`、`dws minutes permission apply`、`dws minutes audio-memo list`

#### **云盘能力**

- **支持筛选最近修改文件及 Markdown 版本对比** ：比较远端版本或本地文件的差异。

  - 相关命令：`dws drive list --latest 5`、`dws markdown diff --node <nodeId> --version 3 --version2 5`
- **大文件下载支持分片与断点续传** ：并行下载、校验文件指纹、401/403 后刷新凭据、`Ctrl+C`中断时保留检查点。

  - 相关命令：`dws drive download`、`dws drive download-version`
  - 新增参数：`--part-size`、`--parallel`、`--no-resume`

#### **IM 与 OA 协作**

- **IM Agent 工作流覆盖更完整** ：统一发送、流式卡片、消息搜索、话题回复与资源下载等 Shortcut 可被稳定发现，群与稳定 ID 解析、分页及 JSON 导出链路补齐。

  - 相关命令：`dws chat +messages-send`、`dws chat +messages-send-card`、`dws chat +search-msg`、`dws chat +thread-replies`、`dws chat +messages-resource-download`
- **聊天回复支持 @成员和 @所有人** ：可直接传入成员 `openDingTalkId`列表或群聊@所有人。

  - 新增参数：`--at-open-dingtalk-ids`、`--at-all`
  - 相关命令：`dws chat message reply`
- **新增联系人个人状态更新** ：更新个人状态文本，用于同步办公地点或当前状态等信息。

  > **[!NOTE]**
  >
  > 写入前需确认。

  - 相关命令：`dws contact user update-ownness`
- **新增 OA 审批发起前置工作流** ：查询表单 Schema、预测审批路径，确认后创建审批实例。

  > **[!NOTE]**
  >
  > 既可使用简单参数，也可提交完整请求体。

  - 相关命令：`dws oa approval form-schema`、`dws oa approval forecast-process`、`dws oa approval create-instance`

### **体验优化**

#### **Agent Skill 与 Schema**

- **命令契约统一** ：原生命令与 Shortcut 统一声明参数、约束、确认规则、Help 和 Runtime Schema，Agent 看到的契约与实际执行一致。

  - 相关命令：`dws schema --compact`
- **Schema 上下文更可控** ：compact 结果聚焦可执行契约，避免加载不必要元数据。

  - 示例：`dws schema --cli-path "chat message reply" --compact`
- **Chat Skill 上下文减负** ：常见激活路径的上下文占用下降约 35%，能力覆盖保持不变。

  - 相关命令：`dws schema --cli-path "chat message send" --compact`
- **多 Skill 路由更清晰** ：长尾能力归入`dingtalk-misc`，共享能力由`dingtalk-shared`提供，减少 Agent 在相近 Skill 之间的选择歧义。

  > **[!NOTE]**
  >
  > **建议** ：Skill 集成按新包名引用共享与长尾能力。

#### **Agent 身份与参数**

- **Agent Product 与 Host 身份分离** ：新集成使用`DWS_AGENT_PRODUCT`表示产品、`DWS_AGENT_HOST=cloud|desktop`表示运行形态。

  > **[!NOTE]**
  >
  > 仅用于可观测性和消息展示，不改变 PAT、认证或路由。
- **参数别名更安全** ：CLI请求前拒绝含糊、被拦截或冲突的别名，正确处理`--dry-run false`显式布尔值。
- **必选组合判断更准确** ：空字符串不再满足 `at_least_one` / `exactly_one` 约束，调用方至少为一个成员传入非空值。

#### 兼容性说明（ **行为变更** ）

- **Recovery 工作流退役** ：`dws recovery plan/execute/finalize`不再支持，改用`dws doctor`、`dws schema`和业务命令排查重试。
- **动态发现缓存退役** ：`dws cache refresh/status/clean` 仅保留历史参数兼容入口，不刷新端点，通过`dws upgrade`获取最新静态端点、用`dws schema` 检查当前命令契约。
- **旧 Chat 命令进入迁移模式** ：`dws chat send/history`及`dws im`别名给出迁移提示，新调用使用`dws chat message send/list`。
- **Agent Host 历史组合值兼容** ：`qwenwork_cloud`等标签仍可使用，新集成请分别设置`DWS_AGENT_PRODUCT`与`DWS_AGENT_HOST`。

### **问题优化**

- **Chat 媒体下载 JSON 恢复可解析** ：返回干净的`success`、`downloadUrl`和`output`字段，不再被进度信息污染。

  - 相关命令：`dws chat message download-media --format json`
- **IM 消息与资源处理更可靠** ：精确解析接收人，保留富文本和嵌套资源，同名下载不再相互覆盖，非交互读取不静默返回空结果。

  - 相关命令：`dws chat +chat-messages`、`dws chat +messages-send`
- **个人事件订阅避免无界重试** ：确定性失败遵循退避策略、`Retry-After`与终止状态，不再形成持续回调风暴。

  - 相关命令：`dws event consume`
- **共享文件系统事件消费恢复稳定** ：当`~/.dws`位于NFS/CSI/FUSE文件系统时，事件总线会使用经过权限校验的用户私有运行目录，避免 `bind: errno 524`。

  > **[!NOTE]**
  >
  > **建议** ：多用户部署提供私有`XDG_RUNTIME_DIR`。

  - 相关命令：`dws event consume`
- **Shortcut 确认结果更明确** ：在stdin关闭、用户拒绝或取消时返回明确的非零错误，不再表现为"成功但未执行"。

  > **[!NOTE]**
  >
  > **建议** ：自动化调用先完成用户确认，预览使用`--dry-run`。
- **邮件分享到聊天的确认门禁补齐** ：首次远程写入前必须显示确认，确认后的自动重试仍可继续，降低误分享风险。

  - 相关命令：`dws mail message share-to-chat`

## **2026-07-31**

### **更新说明**

本周发布 v1.0.55 稳定版：

- 人事大脑（HR Brain）产品上线；
- 约 30 个云盘/文档/在线表格/群聊命令补齐；
- 全部 210 个内置快捷命令以完整 Agent 契约发布；
- 旧版 `chat media upload` 正式退役；
- 个人事件订阅再扩 8 类事件。

```
# 人员搜索
dws hrbrain search employees --keyword "张"

# 发送本地文件到群聊（推荐路径）
dws chat message send --group <openConversationId> --title 文件 --msg-type file --file-path ./report.pdf
```

### **新增功能**

#### **人事大脑（HR Brain）产品上线** {#h4-HR-Brain}

- **人才与组织洞察命令族** ：人才库浏览（列表/详情/成员）、员工画像（元数据/查询/标签/履历/绩效）、基础与规则化人员搜索，共 11 个命令。

  - 相关命令：`dws hrbrain talent-pool list/detail/employees`、`dws hrbrain profile metadata/query/labels/career/performance`、`dws hrbrain search employees/employees-structured/fields`

#### **工作空间命令面扩充** {#h5-}

- **约 30 个命令补齐** ：钉钉云盘版本与权限操作、钉钉文档样式、在线表格评论/版本/公式校验、群聊文本表情就地更新等，命令统一携带安全与确认元数据。
- **云盘覆盖上传** ：`dws drive upload --node <fileId>` 可替换已有文件（与 `--folder` 互斥，支持 dry-run）。

  > **[!NOTE]**
  >
  > 写入前需确认。
- **文档分片读取与群提及** ：`dws doc read --content-format jsonml` 支持按大纲/范围/区块/自定义标签读取片段；文档评论创建、回复、更新支持通过 `--mentioned-open-conversation-id` @ 群。
- **群昵称清除与跨组织待办** ：`dws chat group update-nick` 省略 `--nick` 即清除群昵称；`dws todo task list --query-all` 跨组织查询待办。

#### **快捷命令与事件订阅扩展**

- **210 个快捷命令完整契约发布** ：全部内置 `+快捷命令`（含 88 个群聊快捷命令）以审阅过的 Runtime Schema 叶子工具发布，含可执行路径、参数约束、选择指引与 dry-run 能力；`dws shortcut list` 仍是轻量批量发现入口。
- **个人事件订阅扩容** ：新增 8 类 IM 事件键；一次 `dws event consume` 可订阅消费多个事件键；停止订阅时精准关闭对应本地消费者，其他消费者不受影响。
- **MCP 地址解析** ：`dws mcp url get <mcpId>` 将 MCP 市场 ID 解析为当前用户与组织维度的 Streamable HTTP 地址。

#### **Agent 集成身份**

- **Agent 身份标签** ：新增 `DWS_AGENT_HOST`（运行形态）与 `DWS_AGENT_PRODUCT`（产品归属）环境变量，用于日志与统计归因；仅声明性用途，不参与认证与路由。

### **体验优化**

#### **其他体验优化**

- **多账号安全规则强化** ：组织内多账号且无唯一默认账号时，Agent 必须显式询问，不得猜测或使用最近登录账号。
- **Skill 指引渐进化** ：内置产品指引重组为渐进式发现结构，降低上下文占用。
- **旧版登录态平滑迁移** ：v1.0.53 之前的全局/组织级登录状态自动迁入身份化令牌存储，外部联系人等无目录身份也能正常登录，不跨账号借用令牌。

#### **兼容性说明（行为变更）**

- `chat media upload` **退役** ：基于 AppKey/AppSecret 的旧版媒体上传命令已从命令目录、帮助与 Skill 中移除，历史调用会收到明确的迁移提示；本地文件请改用 `dws chat message send --msg-type file --file-path <路径>`，已持有 mediaId 的调用方可继续用 `--msg-type image --media-id`。

### **问题优化**

- **快捷命令不再"静默返回空"** ：通讯录、审批、知识库、云盘、AI 听记、日历、考勤、群聊、日志等读类快捷命令修复了后端有数据却被投影为空结果的问题。
- **消息读取渲染增强** ：消息列表快捷命令可正确渲染卡片与自动回复富文本、展开合并转发记录、将不可解密的加密消息标记为 `[加密消息]`；`dws chat message download-media` 新增 `--msg-id` / `--open-message-id` 别名。
- **命令契约边界修复** ：审批撤回与文档版本回滚在确认/预检前先遵守 `--dry-run`；云盘重命名避免扩展名重复、文档重命名保留原显示名；云盘详情恢复 `fileSize` 等专属字段；待办提醒规则非法 JSON 会被拒绝。
- **外部联系人兼容** ：仅暴露 openDingTalkId 的外部/跨组织联系人可被正常解析与保留。

## **2026-07-24**

### **更新说明**

本周是能力与渠道双爆发， **企业创建与员工邀请命令上线、366 个** `+快捷命令` **落地、同一组织多账号登录、个人 IM 事件订阅扩展到已读回执/撤回/表情回应，并上线官方多平台 Homebrew 渠道** 。

> **[!NOTE]**
>
> 建议通过 `dws upgrade` 或 Homebrew 升级，并关注事件输出相关的兼容性说明。

```
# 或通过 Homebrew 安装
brew install dingtalk-workspace-cli

# 体验快捷命令
dws sheet import create --file ./data.xlsx
```

### **新增功能**

#### **企业开通与办公命令覆盖**

- **企业创建与成员邀请** ：新增创建钉钉企业、按手机号邀请员工、开通企业登录账号命令。

  - 相关命令：`dws contact org create`, `dws contact user invite`, `dws contact account create`
- **366 个声明式快捷命令** ：覆盖 16 个服务的 `dws <服务> +<命令>` 快捷入口，含单命令封装与多步智能工作流，具备命名参数、校验与确认元数据、写操作 dry-run 保护。

  - 示例：`dws aitable +import-upload`
- **在线表格导入** ：本地 xlsx/xls 一键转换为在线表格并轮询导入进度。

  - 相关命令：`dws sheet import`, `dws sheet import create`, `dws sheet import get`
- **AI 表格工作流写入** ：支持应用校验过的 workflow-dsl 定义。

  - 相关命令：`dws aitable workflow create/update`

#### **同一组织多账号**

- **一个组织内登录多个账号** ：profile 按"组织：用户"区分，`--profile` 可用组织名/ID + 用户名/ID 精确选择；`dws auth logout --profile` 支持登出单个账号或整个组织的所有账号，互不覆盖凭证。

#### **个人 IM 事件订阅扩展**

- **更多事件类型** ：新增单聊与群聊的消息已读回执、撤回、表情回应事件；支持按 staffId 或 openDingTalkId 订阅指定发送人的消息。

#### **官方 Homebrew 渠道**

- **多平台 Homebrew 安装** ：官方提供 stable 与 beta 两个 Formula，覆盖 macOS/Linux 的 Intel 与 Apple Silicon/ARM64；beta 为 keg-only，不会覆盖 stable。

  - 示例：`brew install dingtalk-workspace-cli`

### **体验优化**

#### **其他体验优化**

- **认证与凭证可靠性增强** ：组织策略拒绝会在任何变更前立即终止；长时间运行的客户端一致地重载与刷新访问令牌；并发凭证写入原子化。
- **命令本地校验** ：无效的在线表格/任务目标在本地即失败；AI 表格导入上传强制携带有效文件大小。

#### **兼容性说明（行为变更）**

- `event consume` **输出默认保持传输信封** ：`ndjson` / `json` / `pretty` 输出默认保留 `type/event_type/data/headers` 信封结构（`compact` 处理器维持原状）；Agent 工作流如需直接读取事件专属顶层字段，请使用 `--flatten`（与 `-f raw`, `--debug-raw-events` 互斥），`dws event schema --flatten` 可查看对应结构。
- **Windows 便携凭证包不再假装支持** ：`dws auth export` / `dws auth import` 在 Windows DPAPI 注册表凭证场景会提前明确报错，不再读写凭证与文件。

### **问题优化**

- **Schema 路径兼容性修复** ：面向用户的 Schema 查询重新支持空格、点号、斜杠分隔的 CLI 路径写法。
- **插件命令树注册恢复** ：已安装插件重新注册其 manifest 声明的命令树（HTTP 与 stdio），插件可替换隐藏的兼容回退命令（如 `conference`）而不再被当作分发冲突跳过。
- **IM 快捷命令对齐** ：IM 发送快捷命令默认携带与 `chat message send` 一致的 AI 发送标记（可用 `--ai-tag=false` 关闭），并保留搜索、会话 ID、分页大小等兼容别名。
- **发布渠道版本校验修复** ：npm，Homebrew 与打包二进制的版本标记校验不再因相邻字节粘连而误拒正确的稳定版二进制。

## **2026-07-17**

### **更新说明**

本周发布 v1.0.52 稳定版，带来三大能力：

- **个人事件订阅** （实时监听 @ 我与指定会话消息）、 **本地操作审计日志** 、 **22个产品和564个工具的稳定 Agent 命令目录** ；
- 同时补齐在线表格、群聊、云盘、文档多项命令。

```
# 监听个人事件
dws event consume

# 查看近期操作审计
dws audit tail
```

### **新增功能**

#### **个人事件订阅**

- **实时监听个人 IM 事件** ：新增 `dws event` 命令族，可订阅"@ 我的消息"、指定单聊与指定群聊的消息事件；多个本地消费者共享一条事件总线、输出互不干扰。

  - 相关命令：`dws event list`, `dws event schema`, `dws event consume`, `dws event status`, `dws event stop`
  - 示例：`dws event consume`

#### **本地操作审计**

- **用户操作审计日志** ：通过 `dws` 执行的操作会生成脱敏的每日 JSONL 记录（操作者、命令、结果类别、耗时等），并以哈希链防篡改；支持查看、导出与校验。

  - 相关命令：`dws audit tail`, `dws audit export`, `dws audit verify`

#### **命令能力补齐**

- **在线表格** ：新增数据表、透视表、网格线相关命令。
- **群聊** ：新增消息收藏能力。
- **钉钉云盘** ：新增容量统计与快捷方式命令。
- **钉钉文档** ：评论支持更新与删除（`dws doc comment update/delete`）

#### **Agent 命令目录**

- **稳定命令目录上线** ：`dws schema` 提供确定性的 22 产品 / 564 工具目录，构建期嵌入、无需运行时发现，支持按产品/命令组/叶子命令渐进查询，含完整参数契约与安全确认元数据。

  - 示例：`dws schema chat`

#### **macOS 凭证迁移**

- **钥匙串到文件加密的安全迁移** ：`dws auth migrate-keychain --to file-dek` 支持沙箱与普通进程共享登录态，迁移前逐项预检、支持 `--dry-run` 预览、需显式 `--yes` 确认。

### **体验优化**

- `event consume` **更适配自动化编排** ：输出固定的就绪行与退出摘要，支持 stdin EOF 优雅退出，`--profile` 正确传递，订阅按归属清理，编排方无需 sleep 或担心订阅泄漏。
- **IM 阅读体验对齐** ：`chat message list` 保留引用、合并转发与图片上下文；消息搜索权限受限时展示服务端友好提示；`ding message list` 同时展示 DING 内容与状态。
- **macOS 发布包签名升级** ：官方 macOS 压缩包现要求 Apple Developer ID 签名 + 时间戳 + 强化运行时，签名校验不通过即拒绝发布。

### **问题优化**

- **智能分类建群修复** ：`dws chat category create-smart` 的分类名、群名关键词、成员 ID 正确映射到服务端契约，空值本地拦截，网络连接失败给出可操作的诊断信息。
- **桥接守护重启稳定性** ：修复重启竞态与进程组管理，不再出现重启循环或残留进程。
- **复杂消息与附件完整送达** ：富文本图片按序保留、排队回合附件不丢失、未知消息类型透传原始 JSON；嵌套聊天记录中的图片/音频/视频/文件可恢复下载。
- **macOS 钥匙串模式变更兼容** ：凭证读取不再误创建密钥，密钥不匹配会明确报告而非当作未登录。

## **2026-07-10**

### **更新说明**

本周亮点：

- 目标管理（Agoal）产品上线；
- 机器人桥接（dev connect）获得完整的守护与健康监控能力；
- 运行时切换为静态端点、不再依赖动态服务发现（命令面保持兼容）；
- 全局 `--jq` / `--fields` 过滤在产品命令上全面生效。

> **[!NOTE]**
>
> 建议通过 `dws upgrade` 升级，并关注兼容性说明。

```
# 查看所有机器人桥接连接状态
dws dev connect list

# 产品命令使用 jq 过滤
dws contact user search --query 张 --jq '.result'
```

### **新增功能**

#### **目标管理（Agoal）产品上线**

- **Agoal 命令族落地** ：覆盖战略、合约、记分卡、用户目标、报告与目标模板六大命令组，并附带配套 Skill。

  - 相关命令：`dws agoal ...`

#### **机器人桥接守护与监控**

- **连接监控四件套** ：`dws dev connect list`（状态总览表）、`dws dev connect status`（心跳/会话详情，支持 `--json` 对接外部监控）、`dws dev connect restart`, `dws dev connect stop`。
- **自动拉起与通知** ：`--alwayson` 崩溃自动重启；`--notify-staff-id` 在启动/停止/崩溃时向指定成员发送钉钉通知。
- **凭证免落盘** ：`--unified-app-id` 启动时自动获取 clientId/clientSecret，密钥不再出现在命令行与状态文件中。
- **API 发送的文件可下载** ：通过 `dws chat message send --msg-type file` 发送的文件，机器人侧现在也能下载到本地，文件问答场景全链路打通。

#### **命令能力补齐**

- **群聊能力补齐** ：新增群公告 `chat group notice create/edit/get/list`、群分享邀请、文本翻译、智能分类建组、消息表情回复列表。
- **钉钉文档导入** ：`dws doc import` 发起导入，`dws doc import get` 查询导入任务。
- **邮箱能力补齐** ：邮箱资料、批量获取邮件、撤回与撤回详情、自动回复设置、黑白名单管理。
- **在线表格行列分组** ：`dws sheet group-dimension` / `ungroup-dimension` 支持整行/整列分组与取消分组。
- **机器人消息 @ 指定成员** ：`dws chat message send-by-bot` 新增 `--at-open-dingtalk-ids`，可按 openDingTalkId @ 机器人或跨组织用户。
- **钥匙串健康诊断** ：`dws doctor` 新增钥匙串检查；`dws auth status` 可区分"未登录"与钥匙串不可用/密钥缺失，并给出修复提示。

### **体验优化**

#### **其他体验优化**

- 全局输出过滤全面生效：`--jq` / `--fields` 此前在产品命令上被忽略，现在所有产品命令与 `dws api` 行为一致。

  - 示例：`dws minutes list mine --jq '.[0].title'`
- `dws skill setup --dry-run` 纯预览：只打印将要写入的内容，不再触碰 Skill 目录与配置。
- 批量样式更新可追踪：`dws sheet range batch-set-style` 在 JSON 模式下逐行报告结果（`{index, sheetId, range, ok, error}`），配合 `--continue-on-error` 可精确定位部分失败。

#### **兼容性说明（行为变更）**

- 运行时不再依赖动态服务发现：开源版切换为静态端点运行时，启动更快更稳定；既有命令与兼容别名保持不变。此前"命令目录缓存"类问题的影响面进一步收窄。
- `dws pat chmod` 默认授予长期权限：不带 `--grant-type` 时默认申请 `permanent` 授权（原为会话级）；会话级授权请显式传 `--grant-type session --session-id <id>`。
- `chat file upload` 入口下线：该隐藏入口现返回明确的下线提示；上传文件请改用 `dws chat message send --msg-type file --file-path <路径>`。
- 通讯录标签（label）为正式能力：`dws contact label list/get/list-members` 恢复为真实能力；`contact role` 保留为别名。

### **问题优化**

- **机器人互 @ 端到端修复** ：机器人 @ 另一个机器人的发送与接收链路修复，@ 标记在所有场景正确渲染。
- **真机 QA 批量修复** ：AI 表格图表/仪表盘分享开关（`--enabled false` 可关闭）、会话信息查询别名、通讯录 `--dept` 参数拼写、知识库节点类型枚举修正、DING 消息列表默认类型等十余处命令行为修正。
- **日历 dry-run 不再真实调用** ：`dws calendar event list --dry-run` 现在只打印预览。
- **凭证读取无副作用** ：钥匙串读取路径不再生成或替换密钥，缺密钥/钥匙串不可用会以明确诊断错误呈现。
- **桥接回合调度非阻塞** ：回合进行中收到的新消息合并为一条待处理跟进，不同会话可并行推进；Gemini 通道改走官方 generateContent API，无需本地可执行文件。

## **2026-07-03**

### **更新说明**

本周重磅：

- **多组织登录上线** ，一台设备可同时登录多个钉钉组织并随时切换，命令支持 `--profile` 一次性指定目标组织；
- **在线表格与日志** （report）的结构化输入能力对齐；
- **AI 发送徽标** 默认开启。

```
# 登录第二个组织
dws auth login

# 查看与切换组织
dws profile list
dws profile switch <corpId>
```

### **新增功能**

#### **多组织登录与 Profile 管理**

- **同时登录多个钉钉组织** ：对新组织执行 `dws auth login` 即新增一个 profile；凭证按组织隔离存储在系统钥匙串。
- **组织切换与查询** ：`dws profile list` 查看已登录组织（含主组织/当前标记与有效性），`dws profile switch <名称|corpId|->` 持久切换（`-` 切回上一个，无参数时打开交互选择器）

  - 示例：`dws profile switch corpA`
- **单条命令指定组织** ：全局参数 `--profile <名称|corpId>` 让单条命令在指定组织上执行，不改变默认组织。

  - 示例：`dws contact user search --query 张 --profile corpB`
- **新旧版本双向兼容** ：旧版单组织令牌自动迁移并在需要时镜像回原存储位，旧版二进制与嵌入式宿主不受影响。

#### **结构化输入增强**

- **日志提交支持文件输入** ：`dws report entry submit` 原生支持 `--contents-file <path>` 与 `--contents -`（stdin），长内容不再受 shell 引号困扰。
- **JSON 类参数支持** `@file` **/** `@-`：`--values`, `--criteria`, `--sort-keys` 等结构化 JSON 参数可直接从文件或管道读取。

  - 示例：`dws sheet range update --values @cells.json`
- **在线表格超链接写入** ：`dws sheet range update` 新增 `--hyperlinks` 参数，按二维网格为单元格写入超链接。

### **体验优化**

#### **其他体验优化**

- **在线表格读写格式更宽容** ：`range update` 接受标量单元格（字符串/数字/布尔自动包装）与 `null` 清空单元格；`range read` 在富 `cells` 结构外同时输出扁平 `values` 二维数组，便于脚本处理。
- **帮助只展示可调用命令** ：后端未部署的"幻影"命令不再出现在 `--help` 中，空命令组自动折叠。
- **日志 Skill 对齐新命令** ：Skill 文档统一引导使用 `entry submit` / `inbox list` / `outbox list` 资源.动词式命令；旧别名仍可执行，会提示已废弃。
- **多组织 Skill 支持** ：新增多组织使用规则与决策树说明，读/搜索类场景可跨组织编排。

#### **兼容性说明（行为变更）**

- `--ai-tag` **默认开启** ：通过 `dws chat message send` / `reply` 发送的消息默认携带钉钉「通过AI发送」徽标；如需以纯用户身份发送，请显式传 `--ai-tag=false`。
- **不会静默跨组织取令牌** ：当前组织凭证读取失败时不再回退到其他组织的令牌，而是明确报错，避免误操作到错误组织。

### **问题优化**

- **PAT 授权 agentCode 传递修复** ：显式声明的 `DINGTALK_DWS_AGENTCODE` 现在原样传递到授权与后续命令检查，授权与实际调用不再分裂到不同 Agent 身份；`dws pat chmod --agentCode` 仍是最高优先级。
- **多组织凭证并发安全** ：`profiles.json` 读写加锁并原子写入，损坏时自动隔离重建；钥匙串瞬时读取失败不再误清已有登录状态。

## **2026-06-26**

### **更新说明**

本周是命令能力与安装体验双升级：

- **通讯与结构化办公两大域命令树全面扩充** （日历、AI 听记、邮箱、群聊文件、待办附件、AI 表格高级能力等）；
- **国内安装镜像开箱即用** （Gitee 自动回退）；
- **机器人桥接本地 AI** 支持任意命令行工具接入。

```
# 查询主日历
dws calendar book get --id primary

# 上传文件到群聊
dws chat file upload --group <openConversationId> --file ./slides.pdf
```

### **新增功能**

#### **日历、AI 听记、邮箱命令扩充**

- **日历查询与权限** ：新增日历查询（支持 `--id primary` 主日历）、按名称模糊搜索日历、日历访问控制列表查询；新增 `attendee list/add/delete` 参与人管理；事件/参与人/会议室/附件命令支持 `--calendar-id` 指定非主日历。

  - 相关命令：`dws calendar book get/search`, `dws calendar acl list`, `dws calendar attendee list/add/delete`
- **AI 听记标签管理** ：新增标签列表与按标签查询听记；听记列表命令统一为 `dws minutes list mine/shared/all`。

  - 相关命令：`dws minutes tag list`, `dws minutes tag query --tag-id xxx`
- **邮箱管理能力补齐** ：新增文件夹创建/更新/删除、邮件模板 CRUD、邮件联系人 CRUD 与批量删除、按文件夹列出邮件。

  - 相关命令：`dws mail folder create/update/delete`, `dws mail template create/list/get/update/delete`, `dws mail contact create/list/update/batch-delete`, `dws mail message list`

#### **群聊文件、待办附件与 AI 表格高级能力**

- **群聊文件上传** ：`dws chat file upload` 支持上传本地文件或远程 URL 到会话文件空间。
- **待办添加附件** ：`dws todo task add-attachment` 为待办附加本地文件。
- **AI 表格能力扩展** ：高级权限与角色、视图子命令（锁定/复制/冻结列/行高/填色规则/卡片/时间条）、分组节点管理、工作流开关、记录 upsert / 分享链接 / 历史记录、字段搜索选项等。

  - 相关命令：`dws aitable record upsert`, `dws aitable record share-url`, `dws aitable record history-list` 等

#### **安装与分发**

- **国内安装开箱即用** ：安装脚本自动探测 GitHub 可达性，不可达时自动切换到 Gitee 镜像下载全部资源，国内环境直接 `curl ... | sh` 即可；也可通过 npmmirror 的 npm 渠道安装。
- **Skill 内置于二进制** ：`dws skill setup` 默认使用内置 Skill 副本，离线也能安装/刷新 Skill。

#### **机器人桥接本地 AI**

- **任意 AI CLI 工具可接入** ：`dws devapp robot connect` 新增通用 `custom` 通道，通过 `--agent-cmd "<命令>"` 桥接任何"接收问题、输出答案"的无头 AI 命令行工具，自建 Agent 无需改代码即可接入钉钉机器人。

  - 示例：`dws devapp robot connect --agent-cmd "my-agent ask"`

### **体验优化**

- **会话命令语义明确** ：机器人桥接中 `/new` 开启新会话且保留旧会话（可恢复），`/clear` 真正销毁当前会话，二者不再混同。
- **输出契约统一** ：成功结果统一携带 `success: true`，缺少必填参数的提示统一为 `missing required flag(s): --x`，dry-run 输出格式对齐。
- **参数解析增强** ：显式布尔值（如 `--flag false`）正确生效；考勤班次打卡时间支持 `HH:mm` 格式自动转换。
- **输入本地校验** ：日历重复规则、考勤排班/班次/考勤组输入在本地先行校验，错误更早暴露。

### **问题优化**

- **长对话不再被 30 秒截断** ：机器人桥接 opencode 时，长耗时回合（如数分钟的研究报告）不再因 HTTP 客户端超时被中断，回合预算由 `DWS_AGENT_TIMEOUT_MS`（默认 300 秒）控制。

## **2026-06-19**

### **更新说明**

本周重点：

- **"AI 发送"标识改为可选** ，以用户身份发送的消息默认不再带 AI 徽标，需要时通过 `--ai-tag` 显式开启；
- 同时修复在线表格导出挂起、`dws upgrade --dry-run` 误执行真实升级等问题。

```
# 发送带 AI 标识的消息（可选）
dws chat message send --group <openConversationId> --title "通知" --text "已部署" --ai-tag
```

### **新增功能**

- `ai-tag` **可选 AI 发送标识** ：`dws chat message send` / `dws chat message reply` 新增 `--ai-tag` 参数，显式传入时消息会展示"通过 AI 发送"徽标；不传则消息与人工发送一致。覆盖文本/Markdown、富媒体与单聊发送路径；机器人与 webhook 消息不受影响。

  - 示例：`dws chat message send --group xxx --title 通知 --text "已部署" --ai-tag`
- **Agent 来源识别（统计用途）** ：请求中携带 Agent 宿主类型（如 claudecode / codex / qoder / cursor 等）与实例标识，仅用于用量统计与可观测性，不参与认证与鉴权。

### **体验优化**

#### **其他体验优化**

- **文档写入自动清理非法字符** ：`dws doc create` / `dws doc update` 会自动剔除服务端拒绝的控制字符、零宽字符等（常见于复制粘贴或 AI 生成内容），不再因此写入失败；Tab 与换行保留。

#### **兼容性说明（行为变更）**

- **"AI 发送"徽标默认关闭** ：此前以用户身份发送/回复的每条消息都会带 AI 徽标；现在默认不带，需要展示时请显式使用 `--ai-tag`。依赖该徽标做来源判断的集成方请知悉。

### **问题优化**

- **在线表格导出不再挂起** ：`dws sheet export` 因状态值大小写不匹配而轮询至超时的问题已修复，导出恢复正常返回。
- `dws upgrade --dry-run` **真正只预览** ：此前该参数会执行真实升级；现在仅打印将要执行的步骤，不做任何下载与替换。
- `no-browser` **登录参数生效** ：`dws auth login --no-browser` 不再自动拉起浏览器，适用于无图形界面/远程 SSH 环境。
- **回复消息标识修正** ：开源版 `dws chat message reply` 不再错误携带内部定制版品牌的 AI 徽标。

## **2026-06-12**

### **更新说明**

本周亮点：

- 开放平台文档 RAG 搜索与错误诊断命令上线（`dws devdoc`）；
- 群聊 @ 提及渲染问题修复；并带来四层防御彻底终结"命令目录缓存中毒导致 CLI 无法启动"的问题。

> **[!NOTE]**
>
> 若你通过 npm 安装了 v1.0.36，请升级到 v1.0.37（npm 渠道对齐版本）建议通过 `dws upgrade` 升级。

```
# 诊断开放平台错误码
dws devdoc error diagnose --error-code 40078

# 读取单聊消息
dws chat message list-direct --user <userId>
```

### **新增功能**

#### **开放平台文档智能检索**

- **文档搜索升级为 RAG 检索** ：`dws devdoc article search` 接入 RAG 检索能力，返回结构化的参考结果。
- **新增错误诊断命令** ：`dws devdoc error diagnose`（别名 `troubleshoot`）用于诊断钉钉开放平台 API 错误，支持按 requestId、错误码、错误信息、API 名称等维度检索。

  - 示例：`dws devdoc error diagnose --error-code 40078`

### **体验优化**

#### **其他体验优化**

- **缓存中毒自愈机制** ：命令目录构建异常时自动隔离受损缓存并重新拉取重建，无需手动删缓存；`dws upgrade` 在替换二进制后会自动清理命令目录缓存，升级到本版本即可彻底摆脱该类故障。
- **异常降级保底** ：即使命令目录构建失败，`auth` / `cache` / `doctor` / `upgrade` 等内置命令始终可用，可自行修复。
- **PAT 批量授权更严谨** ：批量授权现在正确携带 agentCode（`--agentCode` 或 `DINGTALK_DWS_AGENTCODE`），且批量授权必须显式 `--yes` 确认后才执行，防止多 scope 授权被误触发。

#### **兼容性说明（行为变更）**

- **旧版本被缓存"锁死"的自救方法** ：v1.0.35 及更早版本若因缓存中毒无法启动，可用 `DWS_CACHE_DIR=$(mktemp -d) dws upgrade` 绕过缓存升级，或手动删除 `~/.dws/cache/<分区>/tools/` 目录，或重新执行安装脚本；

  > **[!NOTE]**
  >
  > 升级到 v1.0.36+ 后不再需要此类操作。

### **问题优化**

- **群聊 @ 提及恢复渲染** ：`dws chat message send` 发送群消息或单聊消息时，`@某人` / `@所有人` 此前因内容被 HTML 转义而显示为纯文本（接口仍返回成功）；现已保留原始 `<@...>` 标记，@ 提及可正常点击。
- **单聊消息读取命令文档对齐** ：`dws chat message list` 仅支持群聊，单聊消息读取请使用专用命令 `dws chat message list-direct`；相关文档与脚本已同步（旧用法 `list --user` 会报 unknown flag）
- **PAT 授权链接不再被转义** ：PAT 错误信息中的授权 URL 不再把 `&` 转义为 `&amp;`，复制链接直接可用。
- **文档创建不再重复标题** ：`dws doc create` 会自动去掉正文中与文档标题完全重复的一级标题，避免出现两个相同标题。

## **2026-06-05**

### **更新说明**

本周是能力大幅扩充的一周：

- **钉钉文档全命令族、知识库、AI 表格表单与导入导出** 集中落地，邮箱/待办/日志命令树完成重构对齐；
- 同时上线 **登录凭证迁移工具** （`dws auth export/import`）与 **PAT 批量授权** 。
- **请注意** ：AI 应用（aiapp）产品本周下线，PAT 授权输出格式有行为变更。

```
# 创建一篇钉钉文档
dws doc create --name "会议纪要" --content "# 结论"

# 导出登录凭证用于环境迁移
dws auth export -o dws-auth.tar.gz
```

### **新增功能**

#### **钉钉文档全命令族**

- **文档能力全面开放** ：检索（search/list/info/read）、创作（create/update）、上传下载、复制/移动/重命名，以及文件、文件夹、块级编辑与评论（list/create/reply/create-inline）；

  > **[!NOTE]**
  >
  > 创作内容支持 **DocxXML** 与 **JSONML** 两种格式并带 Schema 校验。

  - 示例：`dws doc create --name "周报" --content "# 本周进展"`

#### **知识库与 AI 表格扩展**

- **知识库管理** ：知识库空间的创建、查询、列表、搜索与成员管理。

  - 相关命令：`dws wiki space create/get/list/search`, `dws wiki member add/list/update`
- **AI 表格表单与导入导出** ：数据表表单管理；记录全量导入/导出

  > **[!NOTE]**
  >
  > 大数据量走异步任务。

  - 相关命令：`dws aitable form ...`, `dws aitable export ...`, `dws aitable import ...`

#### **凭证迁移与批量授权**

- **登录凭证便携迁移** ：`dws auth export` / `dws auth import` 打包加密凭证与配置（tar.gz，支持 `--base64` 复制粘贴），用于 Linux 沙箱等环境间迁移；`dws auth status` 表格输出新增刷新令牌有效期展示。

  - 示例：`dws auth export -o bundle.tar.gz`
- **PAT 批量授权** ：`dws pat chmod` 支持一次会话为多个产品批量授权，服务端不支持时自动回退单个授权流程。

#### **命令树重构对齐**

- **邮箱、待办、日志、群聊、通讯录命令树重构** ：对齐统一基线，日志（report）新增人类可读渲染输出。

### **体验优化**

#### **其他体验优化**

- **命令目录生成的命令原生支持别名** ：命令目录声明的别名直接注册为 CLI 别名。
- **长任务与翻页基础设施** ：异步任务与游标/分页遍历的公共能力落地，支撑导入导出、文档导出等长耗时操作。

#### **兼容性说明（行为变更）**

- `dws pat chmod` **默认输出改为摘要** ：默认打印紧凑的授权摘要（授权状态、agentCode, scope 数量、下一步提示）；解析原始 JSON 的脚本请改用 `--format json` 或 `--verbose`。
- **AI 应用（aiapp）产品下线** ：`dws aiapp create/query/modify` 已从 CLI 移除，产品数由 19 个调整为 18 个；相关脚本请移除对 aiapp 的调用。

### **问题优化**

本周无。

## **2026-05-29**

### **更新说明**

本周发布 v1.0.32 稳定版，修复两个影响面较大的问题：

- **钉钉云盘上传全面恢复** （此前几乎所有真实文件都会报 403 签名错误）与 **Apple Silicon 自升级恢复** （此前在"解压并验证"步骤被系统终止）；
- 同时 AI 表格附件一步上传命令改为公开可见。

```
# 云盘上传（已恢复正常）
dws drive upload --file ./demo.pdf

# AI 表格附件一步上传
dws aitable attachment upload-file --file ./img.png
```

### **新增功能**

- **AI 表格附件一步上传命令公开** ：`dws aitable attachment upload-file`（准备凭证 + 上传 + 提交一步完成，直接返回 fileToken）从隐藏转为公开，在 `dws aitable attachment --help` 中可见；推荐 AI Agent 默认使用该命令，而非仅完成第一步的 `attachment upload`。

  - 示例：`dws aitable attachment upload-file --base-id xxx --field-id yyy --file ./img.png`

### **体验优化**

- **根帮助附升级提示** ：`dws --help` 底部现在会提示"遇到能力缺失或命令报错。

  > **[!NOTE]**
  >
  > 请先 `dws upgrade` 升级到最新版本再试"，减少因版本过旧导致的问题排查成本。

### **问题优化**

- **钉钉云盘上传 403 修复** ：`dws drive upload` 因 Content-Type 与预签名不一致导致所有文件返回 403；现已信任服务端请求头，上传恢复正常。
- **Apple Silicon 自升级修复** ：`dws upgrade` 在 Apple Silicon Mac 上因未签名被终止的问题已修复；发布包统一附加 ad-hoc 签名,客户端可自动补签自愈。
- **附件上传文档澄清** ：`dws aitable attachment upload`（仅准备凭证）的帮助文案明确其为三步流程的第一步，并指引使用 `upload-file` 一步完成。

## **2026-05-22**

### **更新说明**

本周亮点：

- **三大新产品上线** ：AI 应用（aiapp）、钉钉直播（live）、企业人才搜索（aisearch）；
- 群聊新增消息回复命令，中文 @ 提及不再被误判为文件引用；钉钉云盘上传实现一条命令直达。新产品通过命令目录下发，执行一次 `dws cache refresh` 即可使用。

```
# 刷新命令目录（加载 aiapp/live/aisearch 等新产品）
dws cache refresh

# 一步上传文件到钉钉云盘
dws drive upload --file ./demo.pdf
```

### **新增功能**

#### **三大新产品上线**

- **AI 应用（aiapp）** ：支持按提示词创建 AI 应用、查询任务进度、基于会话继续修改。

  - 相关命令：`dws aiapp create`, `dws aiapp query`, `dws aiapp modify`
- **钉钉直播（live）** ：查询我的直播列表。

  - 相关命令：`dws live stream list`
- **企业人才搜索（aisearch）** ：按关键词 + 多维过滤搜索企业人员，维度支持姓名、部门、职位、主管、下属、手机号、工号等，可逗号分隔多选。

  - 示例：`dws aisearch person --keyword "张" --dimension name,department`

> **[!NOTE]**
>
> 以上产品需执行一次 `dws cache refresh` 加载。

#### **群聊消息回复**

- **新增** `dws chat message reply`：回复指定聊天消息，与 `send` / `send-by-bot` / `recall-by-bot` / `send-by-webhook` 并列。

#### **钉钉云盘上传一步到位**

- `dws drive upload` **一步上传** ：本地文件一条命令直达钉钉云盘，内部自动完成"获取上传凭证 → PUT 上传 → 提交入库"三步，支持 `--dry-run` 预览。

  - 示例：`dws drive upload --file ./report.pdf --folder <dentryUuid>`
- **新增云盘空间列表与文件删除** ：`dws drive list-spaces` 查看可见空间，`dws drive delete` 删除文件（需 `dws cache refresh`）
- **钉盘 URL 直接作为** `--node` **输入** ：`alidocs.dingtalk.com/document/edit?dentryKey=...` 形式的链接可整体传给 `dws doc info` / `dws doc read` 的 `--node`，无需手动拆解。

### **体验优化**

#### **其他体验优化**

- **群聊命令结构对齐服务发现** ：`chat search`, `chat group rename`、群成员管理、`chat bot search` 等命令改由命令目录动态生成，命令面与参数保持不变，后续更新下发更快。
- **多步任务失败快速返回** ：Pipeline 执行中上游返回错误码时立即报错，不再空转轮询直到超时。
- **机器人命令树完整保留** ：共享同一服务端的多个机器人命令根（消息/群组等）不再被去重合并丢失。

#### **兼容性说明（行为变更）**

- **多版本凭证隔离（安全）** ：多版本运行时凭证按版本分区存放(`app-<edition>.json`)，防止串用，开源版保持原`app.json`路径。混用多版本产生的遗留`~/.dws/app.json`可手动清理。

### **问题优化**

- **中文 @ 提及不再报错** ：机器人 webhook 消息中的 `@所有人`, `@张三` 等中文提及此前被误判为 `@文件` 语法而报"file not found"；现在仅当 `@` 后接 ASCII 路径字符时才按文件注入处理。
- `dws chat` **不再嵌套为** `dws chat chat`：多个命令目录条目贡献同一顶层命令时正确合并为单层子树。
- **尾部多余参数不再报错** ：AI Agent 在叶子命令后附带多余词语时不再报 unknown command，静默忽略，提升容错。
- **多服务端同名工具路由纠正** ：工具归属端点按实际拥有者优先，避免同名工具被路由到错误服务。

## **2026-05-15**

### **更新说明**

本周亮点：

- 新增 `ndjson` / `csv` 两种全局输出格式，在线电子表格（sheet，34 个命令）与知识库（wiki）命令参考正式上线.
- 钉钉文档支持从文件/管道写入长 Markdown。
- 多个文档命令修复需要执行一次 `dws cache refresh`，详见下文。

```
# 刷新本地命令目录缓存（本周多个修复需要）
dws cache refresh

# CSV 格式输出
dws todo task list --format csv
```

### **新增功能**

#### **输出格式扩展**

- **新增** `-f ndjson` **与** `-f csv` **全局输出格式** ：`ndjson` 每行一条紧凑 JSON，可直接接入 `jq -c` / 日志管道；`csv` 符合 RFC-4180（引号、换行、中文均正确处理），与 `-f table` 列解析对齐。通讯录、群聊、文档、邮箱、待办等命令的列表输出均能正确展开为行数据。

  - 示例：`dws contact user search --query 张 --format csv`

#### **在线电子表格与知识库参考上线**

- **在线电子表格（sheet）34 个命令参考落地** ：覆盖工作表管理、区域读写与追加、行列增删移动、单元格合并、查找替换、筛选视图、图片写入、异步导出（`submit_export_job` + `query_export_job` 两段式）

  - 示例：`dws sheet range read ...`, `dws sheet find --find "关键词"`
- **知识库（wiki）7 个命令参考落地** ：覆盖知识库空间的创建、查询、列表、搜索与成员管理。

  - 相关命令：`dws wiki space create/get/list/search`, `dws wiki member add/list/update`

#### **文档长内容写入**

- `dws doc update` **支持从文件读取 Markdown** ：新增 `--content-file <path>` 参数（与 `--content` 二选一），长文、表格密集的 Markdown 不再受 shell 转义困扰；`--content-file -` 支持从管道读入。

  > **[!NOTE]**
  >
  > 需先执行一次 `dws cache refresh` 生效。

  - 示例：`cat long.md | dws doc update --doc-id xxx --content-file -`

### 体验优化

#### **其他体验优化**

- **命令别名机制** ：信封 Schema 支持为命令注册别名（如 `range read` 也接受 `range get`）；`dws sheet find --query` 作为 `--find` 的隐藏别名可用，跨文档复制命令不再报 unknown flag（需 `dws cache refresh`）
- **参数纠错更智能** ：粘连参数拆分（如 `--limit100`）现在按参数类型校验，拼错的参数不再被静默改写，而是明确报 unknown flag。
- **未知参数错误附带可用参数列表** ：`-f json` 的 unknown-flag 错误体新增 `available_flags` 字段，Agent 无需解析 `--help` 即可自我恢复。
- **多步任务编排能力** ：信封 Schema 支持 Pipeline 声明"提交任务 → 轮询状态 → 下载结果"类多步流程，为导出等异步场景提供统一入口。

#### **兼容性说明（行为变更）**

- **嵌入式发行版禁止自升级** ：以嵌入方式分发的 CLI 执行 `dws upgrade` 会提前退出并给出明确提示，避免覆盖宿主管理的二进制。
- **群聊发消息必填** `--title`：`dws chat message send --group` 缺少 `--title` 时在本地直接报错（退出码 2），不再落到服务端返回误导性的"发群服务窗会话消息失败"；单聊同样必填。

### 问题优化

- **文档评论命令修复** ：`dws doc comment list/create/create-inline/reply` 报"未找到指定工具"的问题已通过市场元数据修正；请执行一次 `dws cache refresh` 使修复生效。
- **单聊发消息缺标题前置校验** ：单聊缺 `--title` 时本地直接提示，不再返回误导性错误。
- **Windows 授权链接不再被截断** ：PAT 授权 URL 中的 `&userCode=` 段此前被 `cmd start` 截断导致打开 0 权限页面；现改用完整的 URL 打开方式，并在输出中单独打印 `PAT_AUTHORIZATION_URL=` 便于宿主捕获。
- **在线表格文件下载前置拦截** ：`dws doc download` 对在线电子表格（axls）节点先做类型检查并本地拒绝，引导改用 sheet 区域工具，不再触发不必要的下载授权。
- **macOS 沙箱环境钥匙串回退** ：新增可选环境变量 `DWS_DISABLE_KEYCHAIN=1`，沙箱宿主（Keychain 被拦截）可切换为文件加密存储；默认行为不变，文件方案信任级别较低，请知悉后再启用。
- **插件正常退出不再刷 WARN** ：stdio 插件正常关闭时不再输出 `failed to stop stdio client` 噪音日志。

## **2026-05-08**

### **更新说明**

本周为稳定性修复周：

- 重点解决钉钉云盘命令错误路由、考勤统计命令不可用、HTTP 代理被忽略、登录复用过期凭证等问题，无新增命令。

```
# 考勤统计（月度）
dws attendance summary --stats-type month
```

### **新增功能**

本周无。

### **体验优化**

- **考勤统计补上关键参数** ：`dws attendance summary` 新增必填参数 `--stats-type`（`week` / `month`），命令从"不可用"恢复为可用。

  - 示例：`dws attendance summary --stats-type month`
- **帮助文案更准确** ：`dws chat message list` 明确 `nextCursor` 为不透明游标、需原样回传 `--cursor`；`dws chat message send-by-bot`, `dws report create` 的必填参数标注 `(必填)`；通讯录搜索示例统一为 `--query`。

### **问题优化**

- **钉钉云盘命令路由修复** ：`dws drive mkdir` / `dws drive download` 此前可能被错误路由到钉钉文档服务，出现"返回成功但实际未生效"的问题；现按产品维度优先解析端点，彻底消除同名工具冲突。
- **HTTP 代理生效** ：`HTTP_PROXY` / `HTTPS_PROXY` 环境变量此前被所有内置 HTTP 通道静默忽略，沙箱或内网代理环境无法使用；现已在 MCP，OpenAPI、注册表三个通道全部启用环境变量代理。
- **登录不再复用过期凭证** ：`dws login` 每次重新获取 MCP 描述信息，避免缓存的旧 clientId 导致持续认证失败。
- Hermes Skill 目录补齐：安装脚本现在会为已安装 Hermes 的用户自动填充 `~/.hermes/skills/dws/`，未安装用户无影响。

## **2026-05-01**

### **更新说明**

本周亮点：

- **邮箱（Mail）产品线上线** ，邮件搜索/收发命令落地；
- `dws api` **原始 OpenAPI 通道开放** ，无需封装即可直调钉钉开放平台接口；
- PAT 授权进入宿主托管模式。
- 命令总数达到 163 个、覆盖 14 个产品。

> **[!NOTE]**
>
> 建议通过 `dws upgrade` 升级，并关注兼容性说明中的退出码变更。

```
# 搜索邮件
dws mail message search --query "subject:周报"

# 直调钉钉开放平台接口
dws api GET /v1.0/contact/users/me
```

### **新增功能**

#### **邮箱产品上线**

- **钉钉邮箱命令落地** ：支持列出邮箱地址、KQL语法搜索邮件(按文件夹/发件人/日期等)、获取邮件全文与附件、发送邮件。

  - 相关命令：`dws mail mailbox list`, `dws mail message search`, `dws mail message get`, `dws mail message send`
  - 示例：`dws mail message search --query "from:someone@example.com"`

#### **原始 OpenAPI 通道** `dws api`

- **直调钉钉开放平台接口** ：无需编写 MCP 封装即可调用 `api.dingtalk.com` 与 `oapi.dingtalk.com` 接口，支持 GET/POST/PUT/PATCH/DELETE，JSON 参数、stdin 输入、dry-run 预览、`--jq` 过滤、自动翻页（`--page-all`）。

  - 示例：`dws api GET /v1.0/contact/users/me`
- **应用级令牌自动管理** ：自建应用凭证自动获取、缓存并在到期前刷新应用访问令牌，新旧两种 OpenAPI 形态通用。

#### **PAT 授权宿主托管**

- **宿主托管授权流程** ：Agent宿主设置`DINGTALK_DWS_AGENTCODE`后接管授权界面，权限拦截返回stderr JSON，宿主渲染UI后调用`dws pat chmod`授权并重放命令。

  - 相关命令：`dws pat chmod`, `dws pat browser-policy`
- **浏览器打开策略可控** ：`dws pat browser-policy --enabled <true|false>` 独立控制 CLI 是否可拉起浏览器。

### **体验优化**

#### **其他体验优化**

- **插件命令即时可见** ：stdio插件声明overlay时同步构建命令树，无需等待子进程握手；慢启动或失败插件不再导致命令"消失"。
- **插件产品不再被白名单隐藏** ：版本白名单与动态注册产品取并集，插件产品在`dws --help`中正常展示。
- **发消息必填** `--title` **说明明确** ：`dws chat message send` 的帮助文案与文档明确 `--title` 为必填项。
- **多版本缓存隔离** ：不同 edition 使用独立缓存分区，避免共享 `~/.dws` 缓存相互污染。

#### **兼容性说明（行为变更）**

- **PAT 退出码契约调整** ：PAT授权拦截统一使用退出码`4`；Discovery/缓存/协议协商失败统一使用退出码`6`。下游脚本需更新判断逻辑。
- `dws chat message send` **的 @ 参数仅限群聊** ：`--at-users`/`--at-all`/`--at-mobiles`在单聊模式下被显式拒绝，避免@意图被静默丢弃。

### **问题优化**

- **群聊 @ 提及恢复** ：`dws chat message send --group ...` 重新支持并正确转发 `--at-users`, `--at-all`, `--at-mobiles`。
- **群成员列表命令恢复** ：`dws chat group members list --id <openConversationId>` 恢复可达。
- **待办详情查询修复** ：`dws todo task get` 修复调用错误工具导致返回空结果的问题，恢复待办详情查询。
- **插件缓存防污染** ：插件发现返回空工具列表时不再覆盖已有缓存，避免偶发失败导致下次启动信息退化。
- **授权链接完整性** ：PAT授权链接原样保留query/hash内容；轮询兼容设备流旧格式。
- `dws pat chmod` **空结果处理** ：授权结果为空时返回明确错误，不再误判为成功。

## **2026-04-24**

### **更新说明**

本周聚焦 **群聊与 IM 消息能力全面扩展** ：

- 用户身份发消息、消息阅读与搜索、话题回复、@ 提及等能力一次性落地；
- 同时钉钉文档、AI 听记命令参考正式上线，并进行了大规模的参数命名标准化（请注意兼容性说明）。

```
# 以用户身份给群发消息
dws chat message send --group <openConversationId> --text "Hello"

# 查看我的 AI 听记
dws minutes list mine
```

### **新增功能**

#### **群聊与 IM 消息能力大扩展**

- **以用户身份发送消息** ：`dws chat message send` 支持以当前用户身份向群或单聊发送 Markdown 消息，支持 @ 所有人 / @ 指定成员、图片消息。

  - 示例：`dws chat message send --group xxx --text "已发布" --at-all`
- **消息阅读与检索全面开放** ：拉取会话消息、按时间范围拉取全部会话、话题回复、按发送人过滤、@ 我的消息、特别关注消息、未读会话、关键词搜索、会话信息、置顶会话。

  - 相关命令：`dws chat message list/list-all/list-topic-replies/list-by-sender/list-mentions/list-focused/list-unread-conversations/search/info`, `dws chat list-top-conversations`
- **个人消息发送** ：`dws chat message send-personal` 支持个人通道消息发送（敏感操作，执行前需确认）
- **组织级建群与找群** ：`dws chat group create-org` 创建组织全员群；`dws chat search-common` 按昵称搜索共同群聊，支持 AND/OR 匹配与游标分页。
- **机器人生命周期管理** ：`dws chat bot create` 创建企业机器人，`dws chat bot search-groups` 查询机器人所在群。
- **新增** `dws im` **别名** ：`dws im` 等价于 `dws chat`，意图更直观。

#### **钉钉文档与 AI 听记命令上线**

- **钉钉文档 16 个命令参考落地** ：覆盖文档检索（`search`/`list`/`info`/`read`）、创作（`create`/`update`/`folder create`）、文件上传下载、块级编辑（`block query/insert/update/delete`）与评论（`comment list/create/reply`）

  - 示例：`dws doc read --doc-id xxx`
- **AI 听记命令参考落地** ：覆盖听记列表（我的/共享/全部）、基本信息、AI 摘要、关键词、转写文本、提取待办、批量详情、标题修改，以及录音控制（开始/暂停/恢复/停止）

  - 示例：`dws minutes list mine`
- **AI 表格能力增强** ：新增仪表盘/图表工作流与两段式数据导出（`export data`）指引，`field create` 支持单字段模式。

#### **登录与授权体验**

- **PAT 授权错误可视化与自动重试** ：权限不足时输出可读的错误类型、提示与授权命令，完成授权后自动重试；也支持 `--format json` 输出。
- **终端登录被拒的引导优化** ：登录被拒绝时给出更清晰的提示与重试入口。

### **体验优化**

#### **其他体验优化**

- **插件启动提速** ：插件工具列表改从磁盘缓存读取，发现过程并行化，HTTP 冷启动预算从 4 秒压缩至数百毫秒。
- **插件管理更干净** ：移除插件时同步清除其配置项；第三方插件一律通过 `dws plugin install` 平等安装。
- **命令目录合并优化** ：多个服务条目可合并到同一命令子树，`dws chat --help` 不再出现重复条目。
- **发布全量命令索引** ：新增 `docs/command-index.md`，统一列出全部 159 个命令及适用场景说明。
- **Schema v3 扩展** ：支持位置参数、示例展示、默认值、互斥/必选参数组等更丰富的命令契约。

#### **兼容性说明（行为变更）**

- **大范围参数命名标准化** ：群聊、日历、钉钉云盘、AI 听记、通讯录、开放平台文档命令的参数名统一，请按新名称调整脚本：

  - 搜索类统一为 `--query`（原 `--keyword`）：`dws contact user search`, `dws contact dept search`, `dws devdoc article search`
  - 群聊会话参数统一为 `--group`（原 `--id`）、`--open-dingtalk-id`（原 `--open-id`）
  - `dws chat message list-by-sender` 改用 `--sender-user-id` / `--sender-open-dingtalk-id`
  - `dws drive list` 改用 `--max` / `--thumbnail`
  - `dws calendar event suggest` 改用 `--users` / `--duration` / `--timezone`
  - `dws minutes list mine/shared` 改用 `--max`，新增 `--query` / `--start` / `--end`
- **新增常用参数** ：`dws calendar event create/update` 新增 `--attendees`, `--open-dingtalk-ids`, `--timezone`；`dws chat message send` 新增文件消息参数；`dws todo task create` 新增 `--recurrence` 重复规则。

### **问题优化**

- `dws --help` **卡顿修复** ：插件端点不可达时的启动等待从约 10 秒限制到约 4 秒内。
- **插件子进程不再残留** ：退出与卸载插件时正确终止 stdio 子进程。
- **错误 JSON 输出到 stderr** ：`-f json` 模式下错误信息改从 stderr 输出，stdout 保持纯净，便于 CI 断言。
- **中文帮助完整本地化** ：插件与帮助命令的 `--help` 文案完成中文本地化。
- **设备流登录防御性重置** ：`--device` 登录前清理旧凭证状态并重新获取 clientID，修复此前 OAuth 登录后设备流异常要求 clientSecret 的问题。
- **单聊发送链路打通** ：`dws chat message send` 按 `--group` / `--user` / `--open-dingtalk-id` 自动路由，单聊发送端到端可用。

## **2026-04-17**

### **更新说明**

本周发布 v1.0.9 稳定版，是 v1.0.0 以来最大的一次更新：

- 插件系统正式上线，第三方 MCP 服务可作为一等命令接入；
- 同时新增 `dws doctor` 一站式诊断与 `dws config list` 配置总览，命令执行管线扩展为五阶段。

```
# 安装一个插件
dws plugin install <插件名或地址>

# 环境体检
dws doctor
```

### **新增功能**

#### **插件系统上线**

- **第三方 MCP 服务一键接入** ：`dws plugin install` 可将第三方 MCP 服务器注册为 CLI 命令，stdio 服务的工具自动成为 CLI 子命令，Streamable-HTTP 服务自动发现工具。

  - 相关命令：`dws plugin install`, `dws plugin list`, `dws plugin info`, `dws plugin enable`, `dws plugin disable`, `dws plugin remove`
- **插件开发脚手架** ：`dws plugin create` 一键生成插件模板（plugin.json，SKILL.md, hooks.json），`dws plugin dev` 支持源码目录直接注册调试。

  - 示例：`dws plugin create my-plugin`
- **插件独立凭证管理** ：第三方 MCP 服务可在 plugin.json 中声明独立的 HTTP 认证头，与钉钉 OAuth 互不干扰。
- **插件配置持久化** ：`dws plugin config set/get/list/unset` 持久化配置并自动注入环境变量，`${KEY}` 占位符自动解析，无需手动 export。
- **插件 Skill 同步** ：插件携带的 Skill 会在启动时自动同步到 Agent 目录。

#### **诊断与配置工具**

- **新增** `dws doctor`：一站式检查环境、登录与网络连通性，快速定位常见问题。

  - 示例：`dws doctor`
- **新增** `dws config list`：集中查看分散的各项配置。
- **恢复 Skill 市场检索** ：`dws skill find` / `dws skill get` 恢复可用。

### **体验优化**

- **命令执行管线升级为五阶段** ：Register → PreParse → PostParse → PreRequest → PostResponse，插件钩子可介入各阶段。
- **Schema 降级错误结构化** ：命令目录不可用时不再静默返回空结果，而是返回明确原因（未登录 / 市场不可达 / 运行时全部失败），并前置登录检查减少无效连接。
- **多服务并行发现提速** ：启动时的服务发现由串行改为并行，最长等待从多个 10 秒叠加降为单个 10 秒上限。
- **插件安装更灵活** ：plugin.json 的 `cli` 字段支持指向独立文件路径；MCP 工具列表不可用时可回退静态描述。

### **问题优化**

- **插件安全边界加固** ：插件安装仅允许 https/ssh 协议的 git 地址；ZIP 解压拒绝符号链接条目（防路径穿越）；构建产物必须位于插件目录内；阻止插件配置注入 `PATH`, `LD_PRELOAD` 等危险环境变量。
- **插件工具发现修复** ：修复 schema 标志参数与 HTTP 工具发现的问题；开发模式跳过最低版本检查。

## **2026-04-10**

### **更新说明**

本周发布 v1.0.8 稳定版：

- AI 表格命令族全面落地为 20 个静态命令，安装方式对齐 npm 规范并新增 npm 安装渠道。
- 同时强化命令执行超时处理。

> **[!NOTE]**
>
> 建议通过 `dws upgrade` 升级（需 v1.0.7 及以上版本支持自升级）。

```
# 或通过 npm 安装
npm install -g dingtalk-workspace-cli
```

### **新增功能**

#### **AI 表格命令族扩展**

- **AI 表格 20 个静态命令上线** ：覆盖 AI 表格（Base）、数据表、字段、记录、模板、附件的常用操作，替代此前的动态路由方式，命令提示与参数校验更明确。

  - 相关命令：`dws aitable base list/search/get/create/update`, `dws aitable table get/create/update`, `dws aitable field get/create/update`, `dws aitable record query/create/update`, `dws aitable template search`, `dws aitable attachment upload`
  - 示例：`dws aitable record query --base-id xxx --sheet-id yyy`

#### **安装渠道扩展**

- **新增 npm 安装方式** ：可通过 npm 安装 CLI，Skill 安装目录同步对齐 npm 规范，并新增 OpenClaw 智能体支持。

### **体验优化**

- **命令超时处理优化** ：优化命令执行超时、埋点与诊断逻辑，长耗时调用更稳定。
- **AI** **表格记录标签渲染优化** ：记录查询结果的标签字段展示更准确。

### **问题优化**

本周无。

## **2026-04-03**

### **更新说明**

钉钉工作空间 CLI（dws）本周正式发布：

- v1.0.0 首个公开版上线，带来 11 大产品线命令与一键安装；
- 随后一周内快速迭代至 v1.0.7，陆续补齐输出过滤、待办命令族、凭证自动持久化与 `dws upgrade` 自升级能力。

建议通过安装脚本获取最新版。

```
# macOS / Linux 一键安装
curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/install.sh | bash

# 登录
dws auth login

# 自升级到最新版
dws upgrade
```

### **新增功能**

#### **首个公开版发布：11 大产品线一站式命令**

- **钉钉工作空间 CLI 正式发布** ：一条命令行即可操作钉钉核心产品能力，覆盖 AI 表格、OA 审批、考勤、日历、群聊与机器人消息、通讯录、开放平台文档、DING 消息、日志、待办、工作台。

  - 示例：`dws calendar event list`, `dws chat message send-by-bot`, `dws todo create`
- **OAuth 设备流登录** ：`dws auth login` 完成授权，令牌采用加密存储。
- **结构化输出** ：支持 `json` / `table` / `raw` 三种输出格式，以及 `--verbose`, `--debug`, `--dry-run`, `--yes`, `--timeout` 等全局参数。
- **一键安装与 Agent Skill** ：macOS / Linux / Windows 一行脚本安装，内置 Agent Skill 参考文档与 Bash/Zsh/Fish 命令补全。

  - 示例：`curl -fsSL .../install.sh | bash`

#### **登录与安全存储增强**

- **登录状态支持 JSON 输出** ：`dws auth login` 与 `dws auth status` 支持 `--format json`，便于脚本化处理。
- **系统钥匙串安全存储** ：凭证由跨平台钥匙串保管，配合原子写入避免配置损坏。

#### **输出过滤与输入容错**

- **新增** `--fields` **/** `--jq` **全局过滤** ：按需裁剪输出字段，支持 jq 表达式。

  - 示例：`dws contact user get --user xxx --jq '.name'`
- `--fields` **支持点路径与数组下标** ：如 `--fields response.content`, `response.items[0]`。
- `@file` **/** `@-` **输入语法** ：字符串类参数可直接从文件或标准输入读取，群聊消息内容支持从文件读入。
- **命令输入自动纠错** ：自动规范化参数大小写（`--userId` → `--user-id`）、拆分粘连参数（`--limit100` → `--limit 100`）、纠正近似拼写（`--limt` → `--limit`）

#### **待办命令族与 Schema 查询**

- **新增** `todo` **待办命令族** ：支持创建、更新、完成、查询、删除待办，支持 ISO-8601 截止时间与优先级。

  - 相关命令：`dws todo create`, `dws todo update`, `dws todo done`, `dws todo get`, `dws todo delete`
- `schema` **命令公开并支持表格输出** ：可查看命令契约与端点信息。

#### **凭证可靠性与自升级**

- **客户端凭证自动持久化** ：`--client-id` / `--client-secret` 自动保存，令牌过期后自动刷新。
- **错误诊断增强** ：错误信息中展示 trace\_id 与服务端错误码，支持 Normal / Verbose / Debug 三档详细度，便于定位问题。
- **危险命令交互确认** ：删除类操作执行前会请求确认，可用 `--yes` 跳过。
- **新增** `dws upgrade` **自升级** ：从 GitHub Releases 拉取新版本并原子替换，支持 macOS / Linux / Windows。

  - 示例：`dws upgrade`
- **新增** `dws version` **详情输出** ：支持 JSON 格式查看版本、架构、构建信息。

### **体验优化**

#### **其他体验优化**

- **日志（report）日期解析更灵活** ：日志相关命令提供更友好的日期解析与默认值。
- **首次使用引导简化** ：快速开始文档内联登录命令，上手路径更短。
- **OAuth 授权页面视觉升级** ：登录授权页面 UI 重新设计。

#### **兼容性说明（行为变更）**

- **默认输出格式改为 JSON** ：默认输出格式由 `table` 调整为 `json`；需要表格展示请使用 `-f table`。

### **问题优化**

- **登录安全检查收紧** ：CLI 登录开关检测由"失败放行"改为"失败拦截"，网络异常时引导用户检查网络或申请权限，避免误判为已授权。
- **子命令日志级别继承修复** ：`--verbose` / `--debug` 现在可正确被子命令继承，业务错误（HTTP 200 但失败）也会写入本地日志便于离线排查。
- **OAuth 回调竞态修复** ：授权回调先写响应再回传授权码，避免偶发登录失败。
