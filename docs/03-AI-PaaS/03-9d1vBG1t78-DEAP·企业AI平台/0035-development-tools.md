---
title: "DEAP智能体发送群聊消息"
source_url: "https://open.dingtalk.com/document/aipass/development-tools"
namespace: "aipass"
slug: "development-tools"
group: "AI PaaS"
tab: "DEAP·企业AI平台"
breadcrumb: "DEAP 开放API > 智能交互接口 > DEAP智能体发送群聊消息"
doc_id: "HxFtBCxWqo"
updated_at: "2026-11-05 15:14:46"
---

> Source: https://open.dingtalk.com/document/aipass/development-tools
> Path: AI PaaS / DEAP·企业AI平台 / DEAP 开放API > 智能交互接口 > DEAP智能体发送群聊消息
> Updated: 2026-11-05 15:14:46

# DEAP智能体发送群聊消息

以**已发布到钉钉渠道的 DEAP 智能体**身份，向指定钉钉群推送消息。群内全体成员可见，机器人作为发送者出现。

## **接口调用说明**

### **接口能力**

| **能力** | **是否支持** |
| --- | --- |
| 纯文本消息 | ✅ |
| Markdown 渲染(标题/列表/代码块/链接/图片/表格) | ✅ |
| 钉钉互动卡片(按钮/表单/状态翻转) | ✅ |
| 群内 @全员 | ✅ |
| 群内 @指定成员 | ✅ 单次 1~100 人，支持 userId / unionId |
| 普通群、内部群或外部群 | ✅ |
| openConversationId 两种形态自动识别(base64 + 纯数字) | ✅ |
| 消息撤回 / 更新 | ❌ V1 暂不支持 |
| 批量发送(同消息多群) | ❌ V1 暂不支持 |

### **前置条件**

调用本接口前,请确认以下 4 项资源都已就绪：

- 已经完成在DEAP 开放平台后台申请了 API Key，形如 `sk-xxxxxxxxxxxx`。
- 已经将智能体发布到钉钉渠道，并记录了智能体的`agentUuid`。
- 已经创建了一个钉钉群（≥2 人），并记录该群的 `openConversationId` 或纯数字 `conversationId`。

  > **[!NOTE]**
  >
  > - **获取 openConversationId 的方法**：在钉钉机器人消息回调 payload 里通常同时返回 `openConversationId` (base64 加密形态) 和 `conversationId` (纯数字形态)，任传其一即可。
  > - 调用接口的操作人可以不在群内，但发送消息的 AI 智能体必须已加入目标群。
- 已经在群设置中，将智能体加入到群内的操作。
- 如需使用`content_type=INTERACTIVE_CARD`，还需在钉钉互动卡片平台预先创建卡片模板，并记录模板 ID (`cardTemplateId`)和模板的 schema (字段定义，决定 `cardData` 的结构)。

  > **[!NOTE]**
  >
  > 创建完互动卡片后需要联系钉钉同学走卡片模板的审批，然后提供`cardTemplateId`和互动卡片模板编辑页链接。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api-deap.dingtalk.com/v1/assistant/messages/group |
| HTTP Method | POST |
| 权限要求 | DEAP智能体消息的写入权限 |

### **请求头**

| **名称** | **值** | **描述** |
| --- | --- | --- |
| Authorization | Bearer API KEY | 访问令牌，如何申请参照[调用授权](0017-configuration-memory-1.md)。  **[!NOTE]**  请勿在代码仓库、日志、群消息或工单中暴露完整 API Key。 |
| Content-Type | application/json | 请求体格式。 |

### **请求体**

| **名称** | **类型** | **是否必填** | **描述** |
| --- | --- | --- | --- |
| assistant\_id | string | 是 | 智能体 UUID,与发布到钉钉渠道时拿到的 agentUuid 一致。 |
| open\_conversation\_id | string | 是 | 钉钉群标识，base64 加密形态: `cidvFxxxxBfw==` |
| content\_type | string | 是 | 消息类型：   - **TEXT\_MESSAGE** - **INTERACTIVE\_CARD** |
| content | string | 否 | 支持纯文本和 Markdown，当`content_type=TEXT_MESSAGE` 时必填，详情可参见下方**Markdown支持范围**说明。 Markdown 语法中图片可引用钉钉 `mediaId`，例如：`![图片](mediaId)`。 |
| card\_template\_id | string | 否 | 钉钉互动卡片平台预创建的模板 ID，`content_type=INTERACTIVE_CARD` 时必填。 |
| card\_data | object | 否 | 卡片模板的填充数据,字段由模板 schema 决定，`content_type=INTERACTIVE_CARD` 时必填。 |
| corp\_id | string | 否 | 调用方企业 corpId。  **[!NOTE]**   - 建议省略，由服务端从 Access Key 的认证上下文获取； - 如显式传入，必须与认证企业一致，否则返回 HTTP 400。 - 该字段不能用于切换企业身份。 |
| target\_assistant\_id | string | 否 | ISV 分发场景目标智能体,**非 ISV 调用方留空。** |
| send\_to\_im | boolean | 否 | 是否实际推送到钉钉 IM，默认 `true`。  **[!NOTE]**  设为 `false` 时只落库不发卡片（调试用）。 |
| last\_message | string | 否 | 钉钉 IM 会话列表显示的“最后一条消息”摘要，缺省取 `agent 名称 + 发来一张卡片`。 |
| notification\_title | string | 否 | 卡片消息通知标题。 |
| notification\_description | string | 否 | 卡片消息通知描述。 |
| task\_id | string | 否 | 业务方任务 ID，可用于追踪。  **[!NOTE]**  不传时服务端用请求体 MD5 自动生成。 |
| at | object | 否 | 群成员提醒参数，不传时不 @任何人。 |
| at.all | boolean | 否 | 传入 `at` 时必填。   - **true**：表示 @全员，不能同时传入非空 `user_ids` 或 `union_ids`。 - **false**：表示 @指定成员，`user_ids` 和 `union_ids` 至少传入一种；两者原始入参数量总和必须为 1~100，且任何列表都不能包含 `null` 或空白字符串。    - @组织内成员（userId）：`{"all": false, "user_ids": ["userId-1", "userId-2"]}`   - @指定成员（unionId）：`{"all": false, "union_ids": ["unionId-1", "unionId-2"]}`   - 混合指定成员：`{"all": false, "user_ids": ["userId-1"], "union_ids": ["unionId-1"]}`   **[!NOTE]**   - `user_ids` 和 `union_ids` 分别按首次出现顺序去重，100 人上限按去重前的两个原始数组长度总和校验。两类标识最终解析到同一成员时只 @一次。 - `user_ids` 始终按 Access Key 的认证企业解析，任一 userId 无法解析时整次请求失败，不会只向其余成员部分发送。 |
| at.user\_ids | array<string> | 否 | `at.all=false` 时可传，表示组织内成员的钉钉 userId，可与 `at.union_ids` 混合使用。 |
| at.union\_ids | array<string> | 否 | `at.all=false` 时可传，表示群成员 unionId，可与 `at.user_ids` 混合使用。 |

### **请求示例**

- **TEXT\_MESSAGE （含 Markdown）**

  ```
  curl -i --location 'https://api-deap.dingtalk.com/v1/assistant/messages/group' \
  --header "Authorization: Bearer ${DEAP_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "assistant_id": "你的智能体UUID",
      "open_conversation_id": "你的钉钉群openConversationId",
      "content_type": "TEXT_MESSAGE",
      "content": "## 系统告警\n\n**[紧急]** 数据库连接池使用率超过阈值\n\n- 当前: `92%`\n- 阈值: `80%`\n- 时间: 2026-05-22 10:30:15\n\n请相关同学排查。",
      "send_to_im": true,
      "last_message": "数据库连接池告警",
      "notification_title": "数据库告警",
      "notification_description": "连接池使用率超阈值"
  }'
  ```
- **INTERACTIVE\_CARD （互动卡片）**

  ```
  curl -i --location 'https://api-deap.dingtalk.com/v1/assistant/messages/group' \
  --header "Authorization: Bearer ${DEAP_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "assistant_id": "你的智能体UUID",
      "open_conversation_id": "你的钉钉群openConversationId",
      "content_type": "INTERACTIVE_CARD",
      "card_template_id": "你的卡片模板ID.schema",
      "card_data": {
          "title": "请假申请待审批",
          "applicantName": "张三",
          "leaveType": "年假",
          "leaveDays": 3,
          "approveValue": "approve_123",
          "rejectValue": "reject_123"
      },
      "send_to_im": true,
      "last_message": "张三申请请假 3 天"
  }'
  ```
- **TEXT\_MESSAGE (@全员)**

  ```
  curl -i --location 'https://api-deap.dingtalk.com/v1/assistant/messages/group' \
  --header "Authorization: Bearer ${DEAP_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "assistant_id": "你的智能体UUID",
      "open_conversation_id": "你的钉钉群openConversationId",
      "content_type": "TEXT_MESSAGE",
      "content": "预发@全员测试",
      "send_to_im": true,
      "task_id": "group-at-all-001",
      "at": {
          "all": true
      }
  }'
  ```
- **TEXT\_MESSAGE（@认证企业内成员，使用 userId）**

  ```
  curl -i --location 'https://api-deap.dingtalk.com/v1/assistant/messages/group' \
  --header "Authorization: Bearer ${DEAP_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "assistant_id": "你的智能体UUID",
      "open_conversation_id": "你的钉钉群openConversationId",
      "content_type": "TEXT_MESSAGE",
      "content": "请指定成员关注本消息",
      "send_to_im": true,
      "task_id": "group-at-user-001",
      "at": {
          "all": false,
          "user_ids": ["userId-1", "userId-2"]
      }
  }'
  ```
- **INTERACTIVE\_CARD（@指定成员，使用 unionId）**

  ```
  curl -i --location 'https://api-deap.dingtalk.com/v1/assistant/messages/group' \
  --header "Authorization: Bearer ${DEAP_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "assistant_id": "你的智能体UUID",
      "open_conversation_id": "你的钉钉群openConversationId",
      "content_type": "INTERACTIVE_CARD",
      "card_template_id": "你的卡片模板ID.schema",
      "card_data": {
          "title": "待办事项",
          "content": "请指定成员处理"
      },
      "send_to_im": true,
      "task_id": "group-card-at-members-001",
      "at": {
          "all": false,
          "union_ids": ["unionId-1", "unionId-2"]
      }
  }'
  ```
- **TEXT\_MESSAGE（@指定成员，混合使用 userId 和 unionId）**

  ```
  curl -i --location 'https://api-deap.dingtalk.com/v1/assistant/messages/group' \
  --header "Authorization: Bearer ${DEAP_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "assistant_id": "你的智能体UUID",
      "open_conversation_id": "你的钉钉群openConversationId",
      "content_type": "TEXT_MESSAGE",
      "content": "请指定成员关注本消息",
      "send_to_im": true,
      "task_id": "group-at-mixed-001",
      "at": {
          "all": false,
          "user_ids": ["userId-1"],
          "union_ids": ["unionId-1"]
      }
  }'
  ```

## **响应**

### **响应体**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| session\_id | String | 内部 dialog ID，可用于在 DEAP H5 中回看群消息历史。 |
| message\_id | String | 本次消息的唯一 ID，用于追踪 / 后续操作(撤回/更新 V2 支持)。 |

### **响应体示例**

```
HTTP/2 200
Content-Type: application/json

{
  "session_id": "a8340e1xxxxec0c8f",
  "message_id": "c829caxxxxb963f040a5"
}
```

### 错误码示例

```
HTTP/2 4xx 或 5xx
Content-Type: application/json

{
  "error": {
    "code": "invalidParameter",
    "message": "open_conversation_id 不能为空,请传入钉钉群标识(接受 base64 cidm0xxx== 形式或纯数字 IM cid)"
  }
}
```

### **错误码**

| **HTTP状态码** | **错误码** | **典型 message** | **排查方向** |
| --- | --- | --- | --- |
| 400 | invalidParameter | xxx 不能为空，请传入... | 检查请求体字段是否齐全 |
| 400 | invalidParameter | content\_type 取值非法(实际=XXX) | 检查 `content_type` 拼写,只能是 `TEXT_MESSAGE` 或 `INTERACTIVE_CARD` |
| 400 | invalidParameter | at.all 不能为空 | 传入 `at` 时必须同时传入 `at.all` |
| 400 | invalidParameter | corp\_id must match the authenticated corporation | 删除 `corp_id`，或确保其与 Access Key 认证企业一致；不能用该字段切换企业身份 |
| 400 | invalidParameter | at.all=true 与 at.user\_ids 或 at.union\_ids 不能同时设置 | @全员时删除 `user_ids` 和 `union_ids` |
| 400 | invalidParameter | at.user\_ids 和 at.union\_ids 数量总和必须在1到100之间 | @指定成员时至少传入一种成员标识，且两个数组原始数量总和不超过 100 |
| 400 | invalidParameter | at.user\_ids 或 at.union\_ids 不能包含空值 | 删除 `null` 或空白字符串 |
| 400 | invalidParameter | 群消息请求参数不合法,请检查请求参数 | 可能是 userId/unionId 无法在认证企业身份域内解析；携带响应头 `eagleeye-traceid` 联系 DEAP 排查 |
| 401 | unauthorized | Authentication failed, invalid API key provided | 检查 token 是否正确,确认 Authorization Header 拼写为 `Bearer sk-xxx` |
| 403 | permissionDenied | Insufficient permissions to access this resource | token 没有访问该 assistant\_id 的权限,联系 DEAP 平台 |
| 5xx | systemError | 下游业务异常,请联系系统管理员 | 下游身份解析或消息发送失败；记录响应头 `eagleeye-traceid` 后联系 DEAP 排查 |
| 5xx | systemError | 群聊消息推送系统异常 | 服务端发生未预期异常；记录响应头 `eagleeye-traceid` 后联系 DEAP 排查 |

## 消息类型详解

- **TEXT\_MESSAGE（纯文本 / Markdown）**

  最常用的形式,直接传入文本字符串。支持完整 Markdown 渲染。

  ```
  {
    "assistant_id": "52e3c8xxxx74eed",
    "open_conversation_id": "cidvFFRxxxxfw==",
    "content_type": "TEXT_MESSAGE",
    "content": "## 订单状态更新\n\n您的订单 **#A1234567** 已完成发货。\n\n- 物流公司: 顺丰\n- 运单号: `SF1234567890`\n- 预计送达: 2026-05-25\n\n[查看详情](mediaId)",
    "send_to_im": true,
    "last_message": "订单 #A1234567 已发货"
  }
  ```
- **INTERACTIVE\_CARD（钉钉互动卡片）**

  适合需要按钮、表单、状态翻转的场景。**前置条件**: 已在钉钉互动卡片平台预创建模板。

  ```
  {
    "assistant_id": "52e3cxxxx85174eed",
    "open_conversation_id": "cidvFxxxxBfw==",
    "content_type": "INTERACTIVE_CARD",
    "card_template_id": "your-card-template-id.schema",
    "card_data": {
      "title": "请假申请待审批",
      "applicantName": "张三",
      "leaveType": "年假",
      "leaveDays": 3,
      "reason": "家庭旅行",
      "approveButton": {
        "text": "同意",
        "value": "approve"
      },
      "rejectButton": {
        "text": "拒绝",
        "value": "reject"
      }
    },
    "send_to_im": true,
    "last_message": "张三申请请假 3 天,请审批"
  }
  ```

  `card_data` 的字段完全由你的 `card_template_id` 对应的模板 schema 决定，需要参考你在钉钉互动卡片平台创建模板时填写的字段定义。
- **群成员提醒**

  `at` 同时适用于 `TEXT_MESSAGE` 和 `INTERACTIVE_CARD`。例如：

  ```
  {
    "at": {
      "all": true
    }
  }
  ```

  ```
  {
    "at": {
      "all": false,
      "user_ids": ["userId-1", "userId-2"]
    }
  }
  ```

  ```
  {
    "at": {
      "all": false,
      "union_ids": ["unionId-1", "unionId-2"]
    }
  }
  ```

  ```
  {
    "at": {
      "all": false,
      "user_ids": ["userId-1"],
      "union_ids": ["unionId-1"]
    }
  }
  ```

## 关键能力说明

### Markdown支持范围

`content_type = TEXT_MESSAGE` 的文本支持完整的标准 Markdown：

| **元素** | **语法** | **支持** |
| --- | --- | --- |
| 标题 (H1 ~ H6) | `#` ~ `######` | ✅ |
| 粗体 | `**文字**` | ✅ |
| 斜体 | `*文字*` | ✅ |
| 删除线 | `~~文字~~` | ✅ |
| 行内代码 | `代码` | ✅ |
| 多行代码块(含语法高亮) | ````` ````language` ````` | ✅ (支持 Java/Python/JS 等常见语言) |
| 链接 | `[文字](url)` | ✅ |
| 图片 | `![alt](url)` | ✅ (但需注意图片 URL 可达性) |
| 无序列表 | `-` 或 `*` | ✅ |
| 有序列表 | `1.` `2.` `3.` | ✅ |
| 嵌套列表 | 缩进 | ✅ |
| 任务列表 | `- [x]` `- [ ]` | ✅ |
| 引用 / 嵌套引用 | `>` `>>` `>>>` | ✅ |
| 表格 | `| col | col |` | ✅ |
| 分隔线 | `---` | ✅ |

### 图片渲染要求

图片 URL **必须钉钉客户端能直接访问**，否则显示成灰色占位框（不是渲染失败，而是图片拉取失败）。

| **推荐域名(经测试可达)** | **避免使用** |
| --- | --- |
| `*.alicdn.com` | GitHub 静态资源（`*.githubassets.com`，国内访问不稳定） |
| `*.dingtalk.com` | 需要 Referer 校验的防盗链图片 |
| 接入方自己的公网 OSS（带公开读权限） | 内网域名（钉钉客户端访问不到） |

### 群成员提醒适用范围

- @全员适用于内部群和外部群。
- @指定成员的目标必须实际在目标群内。认证企业内成员优先使用 `at.user_ids`；需要使用 unionId 的成员使用 `at.union_ids`。
- `at.user_ids` 接收 Access Key 认证企业内成员的钉钉 userId。服务端只在该认证企业中解析，不能通过 `corp_id` 指定其他企业；任一 userId 无法解析时整次请求失败。
- `at.union_ids` 与单聊接口 `POST /v1/assistant/messages` 的 `union_id` 使用同一类型的成员标识。该字段只接收 unionId，不能混传 userId、staffId、手机号、内部 uid 或 openDingTalkId。
- `user_ids`与`union_ids`可以同时传入。服务端先分别去重并解析为钉钉 IM 内部 UID，再对最终成员去重；任何一项无法解析时整次请求失败，不会部分发送。
- 当前 DEAP 开放 API 不提供“查询群内可 @成员”接口。如调用方无法获取外部组织成员的 unionId，请联系 DEAP 对接同学确认身份获取方案。

## 常见问题 FAQ

- **Q1：接口返回 200，但群里看不到消息**

  按以下顺序排查:

  1. **智能体在群里吗?** 在群设置 → 智能助理列表里确认目标智能体已加入；
  2. **token 对应的智能体权限正确吗?** 不同 token 可能授权不同的 assistant\_id 列表；
  3. **图片显示成灰色?** 见 图片渲染,这是图片 URL 拉取失败，不是接口问题；
  4. **以上都正常?** 把 `eagleeye-traceid` 响应头里的值给到 DEAP 平台运维同学查日志。
- **Q2：Markdown 里图片显示成灰色框**

  99% 情况是**图片 URL 钉钉客户端拉取失败**:

  - 404 (URL 不存在)
  - 网络不可达 (例如 GitHub 资源在国内访问慢/不通)
  - 防盗链 (要求 Referer)
  - 私有图片需要鉴权

  **推荐**：用 `*.alicdn.com` / `*.alipayobjects.com` 等阿里系 CDN，或自己 OSS 公开读资源。
- **Q3：错误响应里出现** `agentUuid`**、下游 IP 或内部错误详情，正常吗?**

  不正常。当前接口对外只返回稳定的错误码和安全文案，不应暴露内部字段、下游地址或异常详情。请保留响应头中的 `eagleeye-traceid` 并联系 DEAP 平台同学排查。
- **Q4：互动卡片的** `card_data`**字段应该填什么?**

  字段由你在钉钉互动卡片平台创建模板时定义的 schema 决定。**接口本身不做格式校验**，只把 `card_data` 整体透传给钉钉的卡片渲染引擎。

  举例：如果你的模板定义了 `{title, content, buttonText, buttonUrl}` 4 个字段，那 `card_data` 就应该传这 4 个 key。如果传错了 key，卡片会渲染异常(空白或错位)，但接口仍返回 200。
- **Q5：群消息能撤回 / 更新吗?**

  V1 接口暂不支持。已发出的消息无法撤回或修改内容。如需此能力请在产品需求中提出。
- **Q6：一次能发到多个群吗?**

  V1 接口不支持批量。如需发到 N 个群，调用方需自己循环 N 次调用（注意接口 QPS 限流）。
- **Q7：是否支持 @某个群成员?**

  支持。@全员传入 `"at": {"all": true}`；@指定成员可使用 `user_ids`、`union_ids`，也可以混合传入。纯文本和互动卡片均支持。
- **Q8：token 申请、智能体发布钉钉渠道、互动卡片模板创建等具体怎么做?**

  请查阅 DEAP 开放平台对应文档章节，或联系 DEAP 平台对接同学。
- **Q9：**`at.union_ids`**可以传 userId 吗?**

  不可以。`at.union_ids` 只接收 unionId。认证企业内成员的钉钉 userId 请放入 `at.user_ids`；staffId、手机号、内部 uid 和 openDingTalkId 均不支持。
- **Q10：外部群能否 @外部组织成员?**

  可以，但该成员必须在目标群内。`user_ids` 只能解析 Access Key 认证企业内的成员；外部组织成员通常需要传入当前调用方身份域内可解析的 unionId。如无法获取，请联系 DEAP 对接同学确认身份获取方案。
- **Q11：可以通过** `corp_id` **指定 userId 所属企业吗?**

  不可以。userId 始终在 Access Key 的认证企业中解析。建议省略 `corp_id`；如显式传入，其值必须与认证企业一致，否则请求会返回 HTTP 400 `invalidParameter`。
