---
title: "安装与使用指南"
source_url: "https://open.dingtalk.com/document/development/dingtalk-dws-cli-install-guide"
namespace: "development"
slug: "dingtalk-dws-cli-install-guide"
group: "应用开发"
tab: "钉钉 CLI"
breadcrumb: "新手入门 > 安装与使用指南"
doc_id: "XYk3YaeWim"
updated_at: "2026-08-14 12:11:27"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-dws-cli-install-guide
> Path: 应用开发 / 钉钉 CLI / 新手入门 > 安装与使用指南
> Updated: 2026-08-14 12:11:27

# 安装与使用指南

## 什么是钉钉 dws CLI

### dws CLI解决什么问题

AI 大模型越来越聪明了，能理解需求、拆解任务、生成方案。但你有没有遇到这种情况：AI 给了你一个很好的答案，然后呢？你还是得自己动手——打开钉钉、找到群聊、发消息、建文档、创建日程。AI 再聪明，最终落地的那个动作还得你来。

钉钉 dws CLI（命令名 dws）要解决的就是这个问题，它是 Agent 使用钉钉能力的媒介。

它是钉钉官方开源的命令行工具，装上之后，AI 就能直接帮你操作钉钉。不是给你建议让你自己去做，而是真正替你动手——帮你发消息、查日程、写文档、管理多维表格、处理审批、收发邮件。

打个比方：以前 AI 就像一个很聪明的朋友，但他进不了你的办公室，只能隔着玻璃告诉你"你应该这样做"。装了 dws CLI 之后，相当于给他配了工牌和门禁卡，他可以直接进去帮你把活干了——当然，他能碰什么、不能碰什么，都由你和企业管理员说了算。

**你不需要学习命令行，也不需要懂编程。安装是一次性的事，装完之后你只需要用自然语言跟 AI 对话就行。**

### 谁适合使用

- **普通用户（使用千问办公、Claude Code、Cursor、Codex等 AI 工具的人）**

  职场打工人想提升办公效率，钉钉 dws CLI来帮你。你不需要懂编程，也不需要理解什么叫命令行。安装是一次性的事，装完之后你只需要跟 AI 对话就行。比如告诉它"帮我总结一下今天群里的聊天记录"、"帮我约下周的团队会议"，AI 会自动用 dws 去操作钉钉，你只管验收结果。
- **专业开发者和产品构建者**

  如果你正在开发需要与钉钉深度集成的 AI 产品——无论是 AI 员工、智能客服还是自动化工作流——dws CLI 提供了覆盖核心业务域的高频操作命令，支持用户身份与应用身份双模式认证，可以直接集成进你的 Agent 系统。
- **企业管理员**

  企业管理员想重塑企业工作流，让AI进入业务提效，可以让钉钉 dws CLI帮你完成。dws CLI 采用零信任架构：OAuth 设备流认证 + 域名白名单 + 最小权限作用域。每一次数据读写都经由钉钉开放平台 API，管理员可实时追溯完整调用日志，没有任何操作能绕过认证和审计。

## **快速安装**

### **安装方法**

#### **方式一：让 AI 帮你安装**

如果你已经在使用 AI 工具（如Cursor、Codex等AI工具），最简单的方式是把下面这句话发给 AI：

```
帮我安装钉钉 DWS : https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli
```

AI 会自动帮你完成安装和配置。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093788.png)

#### 方式二：手动安装

根据你的习惯和环境，选一种就行：

- **一键脚本（最快）**

  - Mac / Linux，打开终端粘贴

    ```
    curl -fsSL https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.sh | sh
    ```
  - Windows 打开 PowerShell

    ```
    irm https://raw.githubusercontent.com/DingTalk-Real-AI/dingtalk-workspace-cli/main/scripts/install.ps1 | iex
    ```
- **npm（需要电脑上有 Node.js）**

  ```
  npm install -g dingtalk-workspace-cli
  ```
- **Homebrew（Mac 用户熟悉的方式）**

  ```
  brew tap DingTalk-Real-AI/dingtalk-workspace-cli https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli.git
  brew install dingtalk-workspace-cli
  ```

你可以把代码仓库地址：`https://github.com/DingTalk-Real-AI/dingtalk-workspace-cli`发给Agent，让他建议你适合的安装方式。

### **登录授权**

安装完成后，执行以下命令完成登录：

```
dws auth login
```

选择你的企业组织并授权即可完成。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093789.png)

- **如果你的企业尚未开启 dws CLI 访问权限**：

  登录过程中选择企业后，点击"**立即申请**"通知管理员。管理员收到请求卡片后进行审批，审批通过后即可重新执行 `dws auth login`。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093790.png)
- **如果你是组织管理员，如何为组织成员开启dws CLI访问权限：**

  - **通过请求卡片快速开启**： 管理员可点击请求卡片中的"**开启本组织允许访问**"一键开启。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093791.png)
  - **通过开发者后台设置**： 进入[开发者后台](https://open-dev.dingtalk.com/fe/old?hash=%23%2FdeveloperSettings#/developerSettings)，依次点击**更多>基本信息**，选择**CLI设置**。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093795.png)

    在CLI设置页面，可点击"**允许成员通过CLI访问个人数据**"一键开启，也可点击"**编辑**"按钮设置可用人员和可用功能。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093797.png)

### **快速试用**

配置完成后，重启你的 AI 工具（如千问办公、Codex等），然后直接在对话框里用自然语言下达指令即可。比如：

> 帮我查看今天的日程安排

> 帮我给项目群发一条消息："周五下午 3 点开项目复盘会"

你不需要记住任何命令，AI 会自己选择合适的操作来完成你的请求。

## 核心能力

钉钉 dws CLI目前已经覆盖钉钉18 个产品模块，包含钉钉的核心业务能力：

| **产品模块** | **命令** | **核心能力** |
| --- | --- | --- |
| 通讯录 | contact | 用户查询、部门查询、花名册档案、离职员工、角色标签 |
| AI 搜问 | aisearch | 按姓名/部门/职位/职责/上级/下级/手机号/工号智能搜人 |
| 群聊与机器人 | chat | 消息发送（文本/Markdown/图片/文件）、群管理、机器人消息、Webhook、@提及、特别关注 |
| 日历 | calendar | 日程增删改查、参与者管理、会议室预定、闲忙查询、时间建议 |
| 钉钉文档 | doc | 文档搜索/浏览/读写、块级编辑、评论协作、权限管理、导出 |
| 钉钉云盘 | drive | 文件列表、上传下载、文件夹管理、元数据查询 |
| AI 表格 | aitable | 数据表/字段/记录/视图管理、图表仪表盘、批量导入导出、模板 |
| 在线电子表格 | sheet | 工作表读写、区域操作、CSV 批量写入、筛选视图、导出 xlsx |
| 邮箱 | mail | 邮箱地址查询、KQL 搜索、邮件收发、草稿、附件、模板 |
| AI 听记 | minutes | 听记列表、摘要、关键词、转写全文、待办、思维导图、发言人识别、热词 |
| OA 审批 | oa | 待处理审批、审批/拒绝/撤销、转交、评论、抄送查询 |
| 待办 | todo | 创建（支持优先级、截止时间、循环）、查询、修改、标记完成 |
| 日志 | report | 按模板创建日报/周报、收件箱/已发送查询、已读统计 |
| 考勤 | attendance | 打卡记录、考勤组、排班查询、汇总统计、假期余额 |
| DING 消息 | ding | 发送和撤回 DING 消息（应用内/短信/电话） |
| 知识库 | wiki | 知识库空间管理、成员管理、文档树浏览 |
| 开放平台文档 | devdoc | 搜索开发文档、诊断 API 调用错误 |
| 直播 | live | 查看直播列表 |

## **使用技巧**

钉钉 dws CLI 是一套命令行工具，让 AI Agent 能够直接操作钉钉的群聊、文档、日历、待办、AI 表格等产品能力。当你和 Agent 对话时，把需求说得越具体，Agent 执行得越精准。

**一个好用的结构：对象 + 动作 + 范围 + 输出格式 + 约束条件。**

举例来说，不要说"帮我整理一下群里的信息"，而是说"读取开发者反馈1群到7群最近30天的消息，按Bug/需求/咨询分类，最后写入AI表格"。前者 Agent 无法执行，后者可以一步到位。

如果你担心 Agent 直接改动数据，可以加一句"先给我看一下结果，确认后再写入"。

## 典型场景

### 场景一：会议纪要自动跟进

- **场景痛点**

  开会是每个职场人的高频场景，但无效会议还是困扰着每一个职场人。AI听记是钉钉会议场景最高频的产出物，但很多团队的AI听记生成之后就"沉默"了——没人去看，更没人跟进。想要让会议记录真正"活"起来，AI Agent来帮你。

  现在把一个听记链接扔给Agent，待办和通知自动总结，并向对应成员发送待办和群通知，彻底解决"会上说得热闹、会后没人跟进"的协作痛点。
- **用户指令示例**

  关键钉钉能力：AI听记、待办、通知

  ```
  请直接用 DWS 读取我今天/明天的日程、未完成待办和可用时间，
  不要只告诉我应该怎么查。以当前时区和今天的实际日期为准。
  按照时间冲突、截止时间和重要性，向我建议今天的工作重点和执行顺序。

  请标出：
  1. 固定时间的会议
  2. 今天必须完成的待办
  3. 可以安排深度工作的空档
  4. 已冲突、已过期或信息不完整的事项

  不要替我创建、修改或完成任何日程和待办，如需操作请先和我确认。
  先自动检查DWS、登录组织和所需能力，优先自动补齐；
  只有扫码登录、目标存在歧义或 DWS 明确要求确认时再找我。
  最终给我整理后的时间线，并说明数据来自哪些日历和待办列表。
  ```
- **效果演示**

  | **向会议成员发送待办** | **向会议群发送通知，并@责任人** |
  | --- | --- |
  | image | image |

  [](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260807/eshtgw/%E7%94%A8%E6%88%B7%E6%8C%87%E4%BB%A4%E7%A4%BA%E4%BE%8B%E8%A7%86%E9%A2%91%E6%BC%94%E7%A4%BA.mp4)

### 场景二：社群反馈自动沉淀

- **场景痛点**

  钉钉群是运营同学聚合用户的载体，群聊中通常沉淀了大量用户的真实反馈，但收集、分析社群中的用户反馈通常费时费力，通过开发自动化工具解决又是一大难点。

  通过AI Agent和钉钉 dws CLI，将原本需要运营同学花费2-3天手动翻阅数千条群消息、逐条分类录入表格的工作，压缩到一次对话指令内自动完成。数据不再是"感觉"，而是有结构、有趋势、可追踪的运营资产。
- **用户指令示例**

  关键钉钉能力：群、AI表格

  ```
  帮我分析"xxx群"和"xxx群"最近xx天的所有消息，把用户反馈提取出来
  按"反馈类型（Bug/需求/咨询/吐槽）、优先级（P0-P3）、涉及模块、原始消息摘要、反馈人、日期"这6个字段写入一张AI表格，表名叫《用户反馈汇总-7月》。
  ```
- **效果演示**

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8100706871/p1093806.png)

  [](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260807/ktetis/%E7%A4%BE%E7%BE%A4%E5%8F%8D%E9%A6%88%E8%87%AA%E5%8A%A8%E6%B2%89%E6%B7%80%E8%A7%86%E9%A2%91%E6%BC%94%E7%A4%BA.mp4)

### 场景三：工作优先级智能规划

- **场景痛点**

  忙碌的职场人经常被大量的会议和待办事项困扰，每天早上分别打开日历和待办，再人工判断会议冲突、截止时间和工作空档，面临大量的重复工作。

  而通过AI Agent 通过 dws CLI 同时读取当天日程、未完成待办和可用时间，再整理成一份当天工作的重点和建议执行顺序，让你一天的工作变得清晰而有条理。
- **用户指令示例**

  关键钉钉能力：日程、待办

  ```
  请直接用 DWS 读取我今天/明天的日程、未完成待办和可用时间，
  不要只告诉我应该怎么查。以当前时区和今天的实际日期为准。
  按照时间冲突、截止时间和重要性，向我建议今天的工作重点和执行顺序。

  请标出：
  1. 固定时间的会议
  2. 今天必须完成的待办
  3. 可以安排深度工作的空档
  4. 已冲突、已过期或信息不完整的事项

  不要替我创建、修改或完成任何日程和待办，如需操作请先和我确认。
  先自动检查DWS、登录组织和所需能力，优先自动补齐；
  只有扫码登录、目标存在歧义或 DWS 明确要求确认时再找我。
  最终给我整理后的时间线，并说明数据来自哪些日历和待办列表。
  ```
- **效果演示**

  [](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20260807/kduffn/%E5%B7%A5%E4%BD%9C%E4%BC%98%E5%85%88%E7%BA%A7%E6%99%BA%E8%83%BD%E8%A7%84%E5%88%92%E8%A7%86%E9%A2%91%E6%BC%94%E7%A4%BA.mp4)
