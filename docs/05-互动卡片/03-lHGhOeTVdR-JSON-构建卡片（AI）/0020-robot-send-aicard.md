---
title: "机器人发送卡片"
source_url: "https://open.dingtalk.com/document/development/robot-send-aicard"
namespace: "development"
slug: "robot-send-aicard"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "发送与互动 > 机器人发送卡片"
doc_id: "F1XK1ZkWnP"
updated_at: "2026-10-29 11:52:27"
---

> Source: https://open.dingtalk.com/document/development/robot-send-aicard
> Path: 互动卡片 / JSON 构建卡片（AI） / 发送与互动 > 机器人发送卡片
> Updated: 2026-10-29 11:52:27

# 机器人发送卡片

本文以机器人群聊发卡为例，示例包含转发、摘要和 @ 成员，可按需取舍。

## **说明**

用企业内部应用的机器人，通过调用[创建并投放 AI 卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0793-api-createanddeliveraicard.md)接口把卡片发到群聊。卡片发出后要更新内容或状态，详见[机器人更新卡片](0021-robot-update-aicard.md)。

## 前置条件

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../../01-应用开发/01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并参考[添加接口调用权限](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0003-add-api-permission.md)说明，申请以下接口权限：

  - `AICard.Instance.Write`（视频会议信息管理写权限）

    > **[!NOTE]**
    >
    > 若未添加权限点，接口会返回 `403 Forbidden.AccessDenied.AccessTokenPermissionDenied`，`requiredScopes`为 `["AICard.Instance.Write"]`。的错误提示。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。
- **创建内部群**：创建一个钉钉内部群，并获取**群的** `openConversationId`，例如 `cidXXXX==`。
- **机器人入群**：参考[配置企业机器人](../../01-应用开发/01-XOnnmGCTbn-开发指南/0078-configure-the-robot-application.md)完成机器人创建，并[添加机器人入群](../../01-应用开发/01-XOnnmGCTbn-开发指南/0079-add-robot-to-group.md)。
- **获取应用AccessToken**：获取应用[Client ID](../../01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（原appKey）和[Client Secret](../../01-应用开发/01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#7d9825efaadw7)（原appSecret）参数，并执行以下命令获取应用AccessToken：

  ```
  curl -s -X POST https://api.dingtalk.com/v1.0/oauth2/accessToken \
    -H 'Content-Type: application/json' \
    -d '{"appKey":"<AppKey>","appSecret":"<AppSecret>"}'
  ```

## 准备消息内容

沿用[最小示例：创建与更新](0001-json-build-card.md#739b42ba58lku)中的订单卡片，并在正文里 @ 跟进人：

**card.a2ui.json：**

```
[
  {"version": "v1.0", "createSurface": {"surfaceId": "order-001", "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"}},
  {"version": "v1.0", "updateDataModel": {"surfaceId": "order-001", "path": "/", "value": {"order": {"title": "订单已创建", "detail": "订单号 A2024001，预计 3 天内发货"}}}},
  {"version": "v1.0", "updateComponents": {"surfaceId": "order-001", "components": [
    {"id": "root", "component": "Column", "children": ["title", "owner", "detail"], "gap": 8},
    {"id": "title", "component": "Text", "text": {"path": "/order/title"}},
    {"id": "owner", "component": "Markdown", "content": "<a atId=\"<staffId>\">张三</a> 请跟进这笔订单"},
    {"id": "detail", "component": "Text", "variant": "caption", "text": {"path": "/order/detail"}}
  ]}}
]
```

请求体里的 `a2uiMessages` 是**字符串数组**：把上面每条消息各自序列化成 JSON 字符串，再组成数组。直接传对象数组会被拒绝。

## 发送卡片

> **[!NOTE]**
>
> 本示例包括转发 + 摘要 + @。

```
POST /v1.0/card/ai/instances/createAndDeliver

{
  "outTrackId": "order-001-20261027",
  "openSpaceId": "dtv1.card//im_group.<openConversationId>",
  "protocolVersion": "1.0",
  "flowStatus": "PROCESSING",
  "a2uiMessages": ["<消息 1 的 JSON 字符串>", "<消息 2 的 JSON 字符串>", "<消息 3 的 JSON 字符串>"],
  "a2uiAnnotations": [
    {"surfaceId": "order-001", "componentId": "title", "type": "artifact"},
    {"surfaceId": "order-001", "componentId": "detail", "type": "artifact"}
  ],
  "imGroupOpenSpaceModel": {
    "supportForward": true,
    "lastMessageI18n": {"ZH_CN": "[订单] A2024001 已创建", "EN_US": "[Order] A2024001 created"},
    "notification": {"alertContent": "订单 A2024001 已创建，请跟进", "notificationOff": false}
  },
  "imGroupOpenDeliverModel": {
    "robotCode": "<robotCode>",
    "atUserIds": {"<staffId>": "张三"}
  },
  "summary": "订单 A2024001 已创建",
  "userIdType": 1,
  "cardAtUserIds": ["<staffId>"]
}
```

返回示例：

```
{"success": true, "result": {"outTrackId": "order-001-20261027",
  "deliverResults": [{"spaceType": "IM_GROUP", "spaceId": "cidXXXX==", "success": true, "carrierId": "..."}]}}
```

逐项检查 `deliverResults` 中每一项的 `success`：顶层 `success=true` 不代表每个目标都投递成功。**保存** `outTrackId`，之后用它更新这张卡片的内容和状态，见[机器人更新卡片](0021-robot-update-aicard.md)。

## 转发、摘要与 @成员

### 转发

需要转发时，把 `imGroupOpenSpaceModel.supportForward`（单聊为 `imRobotOpenSpaceModel.supportForward`）显式设为 `true`。本页示例传了 true。

### 摘要

> **[!NOTE]**
>
> 以下四个字段各管一处。

| **字段** | **显示位置** | **建议** |
| --- | --- | --- |
| `a2uiAnnotations`（`type: "artifact"`） | 卡片完成后在**会话中显示的文本**，由被标注组件的内容生成。 | **建议必传**；创建时标注标题、正文等主要内容组件即可，之后一直保留，更新时不必重复传。 |
| `imGroupOpenSpaceModel.lastMessageI18n` | **会话列表**里的最后一条消息摘要。 | 按语言给值，如 `{"ZH_CN": "...", "EN_US": "..."}`。 |
| `imGroupOpenSpaceModel.notification` | **推送通知**：`alertContent` 为文案。 | `notificationOff: true` 可关闭通知。 |
| `summary` | 卡片**降级摘要**（编码为 `fallbackText.summary`）。 | 纯文本，建议不超过 2048 字节。 |

### @ 成员

消息级 @ 和卡片正文里的 @ 是两件事，按需要组合：

| **目标** | **写法** |
| --- | --- |
| 让对方**收到 @ 提醒** | `imGroupOpenDeliverModel.atUserIds`：`{"<staffId>": "展示名"}`。 |
| 卡片**正文里显示 @某人** | Markdown 写 `<a atId="<staffId>">展示名</a>`，同时把该 ID 放进 `cardAtUserIds`，并传 `userIdType: 1`。 |
| 卡片**正文里显示 @所有人** | Markdown 写 `<a atId="all">所有人</a>`，同时传 `atAll: true`，两者缺一不可。 |

## 快速接入

本文以Python 标准库为示例，参考下方代码并替换 `AppKey`、`AppSecret`、`robotCode`、群 ID、成员 staffId 和展示名后运行：发送订单卡片，3 秒后更新为「订单已发货」并完成。

```
import json, time, urllib.error, urllib.request

APP_KEY, APP_SECRET = "<AppKey>", "<AppSecret>"
ROBOT_CODE = "<robotCode>"                 # 从应用的机器人配置页获取
CID = "<openConversationId>"                # 机器人所在的群
AT_STAFF_ID, AT_NAME = "<staffId>", "张三"   # 要 @ 的成员
API = "https://api.dingtalk.com"

def call(method, path, body, token=None):
  headers = {"Content-Type": "application/json"}
  if token:
    headers["x-acs-dingtalk-access-token"] = token
  req = urllib.request.Request(API + path, json.dumps(body, ensure_ascii=False).encode(), headers, method=method)
  try:
    with urllib.request.urlopen(req, timeout=30) as resp:
      return json.load(resp)
  except urllib.error.HTTPError as e:  # 打印钉钉返回的错误码和说明，例如缺少的权限
    raise SystemExit(f"{method} {path} -> HTTP {e.code}: {e.read().decode()}")

def wire(messages):  # a2uiMessages 是字符串数组
  return [json.dumps(m, ensure_ascii=False) for m in messages]

token = call("POST", "/v1.0/oauth2/accessToken", {"appKey": APP_KEY, "appSecret": APP_SECRET})["accessToken"]
sid = "order-001"
card = [
  {"version": "v1.0", "createSurface": {"surfaceId": sid, "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"}},
  {"version": "v1.0", "updateDataModel": {"surfaceId": sid, "path": "/", "value": {"order": {"title": "订单已创建", "detail": "订单号 A2024001，预计 3 天内发货"}}}},
  {"version": "v1.0", "updateComponents": {"surfaceId": sid, "components": [
    {"id": "root", "component": "Column", "children": ["title", "owner", "detail"], "gap": 8},
    {"id": "title", "component": "Text", "text": {"path": "/order/title"}},
    {"id": "owner", "component": "Markdown", "content": f'<a atId="{AT_STAFF_ID}">{AT_NAME}</a> 请跟进这笔订单'},
    {"id": "detail", "component": "Text", "variant": "caption", "text": {"path": "/order/detail"}},
  ]}},
]
artifacts = [{"surfaceId": sid, "componentId": c, "type": "artifact"} for c in ("title", "detail")]
out_track_id = f"order-001-{int(time.time())}"

created = call("POST", "/v1.0/card/ai/instances/createAndDeliver", {
  "outTrackId": out_track_id,
  "openSpaceId": f"dtv1.card//im_group.{CID}",
  "protocolVersion": "1.0",
  "flowStatus": "PROCESSING",
  "a2uiMessages": wire(card),
  "a2uiAnnotations": artifacts,
  "imGroupOpenSpaceModel": {
    "supportForward": True,
    "lastMessageI18n": {"ZH_CN": "[订单] A2024001 已创建", "EN_US": "[Order] A2024001 created"},
    "notification": {"alertContent": "订单 A2024001 已创建，请跟进", "notificationOff": False},
  },
  "imGroupOpenDeliverModel": {"robotCode": ROBOT_CODE, "atUserIds": {AT_STAFF_ID: AT_NAME}},
  "summary": "订单 A2024001 已创建",
  "userIdType": 1,
  "cardAtUserIds": [AT_STAFF_ID],
}, token)
assert all(r.get("success") is True for r in created["result"]["deliverResults"]), created

time.sleep(3)
print(call("PUT", "/v1.0/card/ai/instances/update", {
  "outTrackId": out_track_id,
  "outUpdateId": f"{out_track_id}-shipped",
  "flowStatus": "FINISH",
  "a2uiMessages": wire([{"version": "v1.0", "updateDataModel": {"surfaceId": sid, "path": "/order/title", "value": "订单已发货"}}]),
    "a2uiAnnotations": artifacts,
}, token))
```

## 完整示例

本示例是一张「线上问题登记单」带输入框的表单卡片为例，包含单行和多行输入框、单选、多选、数字、评分、开关和日期，提交按钮带必填校验。发送时请求体和上文相同，其中：

- `a2uiAnnotations` 的 `surfaceId` 改为 `incident-form`，`componentId` 改为 `title` 和 `intro`；
- 接收「提交」事件还需配置回调接收端。

  - 创建时用 callbackType 指定方式：`STREAM` 不传 `callbackRouteKey`；
  - HTTP 需传已注册的 `callbackRouteKey`，参数参见[创建并投放 AI 卡片](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0793-api-createanddeliveraicard.md)接口文档说明。

**incident-form.a2ui.json**

```
[
  {"version": "v1.0", "createSurface": {"surfaceId": "incident-form", "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"}},
  {"version": "v1.0", "updateDataModel": {"surfaceId": "incident-form", "path": "/", "value": {
    "status": "填写后点击「提交」",
    "form": {"title": "", "detail": "", "priority": ["P1"], "platforms": [], "affected": 0, "severity": 3, "urgent": false, "dueDate": "", "owner": ""}}}},
  {"version": "v1.0", "updateComponents": {"surfaceId": "incident-form", "components": [
    {"id": "root", "component": "Column", "children": ["title", "intro", "f-title", "f-detail", "priority-title", "f-priority", "platform-title", "f-platforms", "f-affected", "severity-title", "f-severity", "urgent-row", "due-title", "f-due", "f-owner", "actions", "status"]},
    {"id": "title", "component": "Text", "text": "线上问题登记单", "bold": true},
    {"id": "intro", "component": "Markdown", "content": "<a atId=\"<staffId>\">张三</a> 请登记这个线上问题，**标题**和**影响端**为必填。"},
    {"id": "f-title", "component": "TextField", "label": "问题标题", "placeholder": "一句话描述问题", "variant": "shortText", "value": {"path": "/form/title"}},
    {"id": "f-detail", "component": "TextField", "label": "现象与复现步骤", "placeholder": "1. 打开… 2. 点击… 3. 出现…", "variant": "longText", "value": {"path": "/form/detail"}},
    {"id": "priority-title", "component": "Text", "text": "优先级", "variant": "caption"},
    {"id": "f-priority", "component": "ChoicePicker", "variant": "mutuallyExclusive", "displayStyle": "chips", "options": [{"label": "P0 阻塞", "value": "P0"}, {"label": "P1 严重", "value": "P1"}, {"label": "P2 一般", "value": "P2"}], "value": {"path": "/form/priority"}},
    {"id": "platform-title", "component": "Text", "text": "影响端（可多选）", "variant": "caption"},
    {"id": "f-platforms", "component": "ChoicePicker", "variant": "multipleSelection", "displayStyle": "checkbox", "options": [{"label": "iOS", "value": "ios"}, {"label": "Android", "value": "android"}, {"label": "Mac", "value": "mac"}, {"label": "Windows", "value": "windows"}, {"label": "鸿蒙", "value": "ohos"}], "value": {"path": "/form/platforms"}},
    {"id": "f-affected", "component": "NumberInput", "label": "预估影响人数", "placeholder": "输入人数", "min": 0, "value": {"path": "/form/affected"}},
    {"id": "severity-title", "component": "Text", "text": "严重程度", "variant": "caption"},
    {"id": "f-severity", "component": "Rating", "value": {"path": "/form/severity"}},
    {"id": "urgent-row", "component": "Row", "align": "center", "children": ["urgent-label", "f-urgent"]},
    {"id": "urgent-label", "component": "Text", "text": "需要立即电话通知值班", "weight": 1},
    {"id": "f-urgent", "component": "Switch", "value": {"path": "/form/urgent"}},
    {"id": "due-title", "component": "Text", "text": "期望修复日期", "variant": "caption"},
    {"id": "f-due", "component": "DateTimeInput", "label": "选择日期", "enableDate": true, "value": {"path": "/form/dueDate"}},
    {"id": "f-owner", "component": "TextField", "label": "建议负责人", "placeholder": "花名", "variant": "shortText", "value": {"path": "/form/owner"}},
    {"id": "actions", "component": "Row", "justify": "end", "children": ["btn-submit"]},
    {"id": "btn-submit", "component": "Button", "variant": "primary", "child": "btn-submit-label",
      "checks": [
        {"condition": {"call": "required", "args": {"value": {"path": "/form/title"}}}, "message": "请填写问题标题"},
        {"condition": {"call": "required", "args": {"value": {"path": "/form/platforms"}}}, "message": "请至少选择一个影响端"}],
      "action": {"event": {"name": "submit_incident", "context": {"form": {"path": "/form"}}}}},
    {"id": "btn-submit-label", "component": "Text", "text": "提交"},
    {"id": "status", "component": "Text", "text": {"path": "/status"}, "variant": "caption"}
  ]}}
]
```

- 每个输入组件都要用 `value: {"path": ...}` 绑定，并在 `updateDataModel` 里给出类型正确的初始值，不绑定就收不到用户输入。
- `ChoicePicker` 单选时值也是字符串数组。
- 必填校验写在提交按钮的 `checks` 上，不写在输入框上。
- 更新时不要重发表单的初始数据，否则会覆盖用户已输入的内容。
- 表单 JSON 只定义输入与提交事件，业务处理和结果回写需由接收端实现。
- 「监听交互事件」介绍的是 DWS 发卡链路，不作为本机器人示例的接入步骤。

## 常见错误

- **调用接口提示：**`403 AccessTokenPermissionDenied`**，**`requiredScopes` **为** `AICard.Instance.Write`**？**

  提示该错误代表应用未开通权限，在应用所属组织的开发者后台开通后重试。
- **群里只显示「暂无可展示的最终产物」**

  没传 `a2uiAnnotations`，或标注的组件文本由函数生成，创建时用 `type: "artifact"` 标注字面文本或路径绑定的主要内容组件。
- **提示**`400 param.userIdNotExist`

  `cardAtUserIds` 或 `userId` 与 `userIdType` 不匹配，或用户不存在。

  - 核对 `userIdType` 对应的 ID 类型及用户是否有效；
  - 本文 `staffId` 示例使用 `userIdType`: 1。
- **正文里显示了「@某人」，但不高亮、不能点击**

  正文 `<a atId>` 里的 ID 没有放进 `cardAtUserIds`，或两边 ID 不一致**。**

  - 本文 `staffId` 示例使用 `userIdType`: 1，并将正文成员 `atId` 列入 `cardAtUserIds`；
  - 保留 ID all 单独使用 atAll。.
- **收到 @ 提醒，但正文里没有 @**

  只传了 `atUserIds` 或 `cardAtUserIds`**。**在 Markdown 正文里写 `<a atId="...">名字</a>`。
- **提示**`400 param.invalid`

  参数或 A2UI 消息不合法**，**看返回的 `errorMsg`；确认 `a2uiMessages` 是非空的字符串数组、消息 `version` 为 `"v1.0"` **。**
- **提示**`500 system.resultUnknown` **/** `system.operationInProgress`

  结果未知或仍在处理**。**先回读目标会话核实是否已投递，再决定是否重新发送**。**
- `deliverResults` **中某项** `success` **为** `false`

  该目标投递失败。看该项的 `errorMsg`；检查机器人是否在群里、`openSpaceId` 是否正确。
