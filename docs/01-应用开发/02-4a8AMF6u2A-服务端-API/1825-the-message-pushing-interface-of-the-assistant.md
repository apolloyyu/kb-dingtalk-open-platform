---
title: "使用服务助手推送消息"
source_url: "https://open.dingtalk.com/document/development/the-message-pushing-interface-of-the-assistant"
namespace: "development"
slug: "the-message-pushing-interface-of-the-assistant"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 员工服务台 > 使用服务助手推送消息"
doc_id: "IYcbGPvGJD"
updated_at: "2026-08-27 14:20:53"
---

> Source: https://open.dingtalk.com/document/development/the-message-pushing-interface-of-the-assistant
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 生态开放 > 员工服务台 > 使用服务助手推送消息
> Updated: 2026-08-27 14:20:53

# 使用服务助手推送消息

调用本接口通过服务助手机器人给企业员工发送消息。

> **[!IMPORTANT]**
>
> 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## 权限

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartbot/msg/push`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msg | Msg | 是 | { "msgtype": "text", "text": { "content": "请提交日报。" } } | 消息内容，最长不超过2048个字节。消息类型和样例参考[消息类型与数据格式](1826-service-desk-message-types-and-data-formats.md)。 |
| msgtype | String | 是 |  | 消息类型，支持如下消息类型。   - **text**：文本消息。 - **markdown**：Markdown消息。 - **action\_card**：卡片消息。 |
| text | Text | 否 |  | 文本消息。 |
| content | String | 否 | 请提交日报。 | 文本消息内容，建议500字符以内。 |
| markdown | Markdown | 否 |  | markdown消息。 |
| text | String | 否 | # 这是支持markdown的文本 | markdown格式的消息，建议500字符以内。 |
| title | String | 否 | 测试标题 | 首屏会话透出的展示内容。 |
| action\_card | ActionCard | 否 |  | 卡片消息。 |
| btn\_json\_list | BtnJson[] | 否 |  | 使用独立跳转**ActionCard**样式时的按钮列表，必须与**btn\_orientation**同时设置，且长度不超过1000字符。  **[!NOTE]**  如果是独立跳转的**ActionCard**样式，则**btn\_json\_list**和**btn\_orientation**必须设置。 |
| action\_url | String | 否 | https://www.tmall.com/ | 使用独立跳转**ActionCard**样式时的跳转链接，最长500个字符。 |
| title | String | 否 | 这是一个按钮 | 使用独立跳转**ActionCard**样式时的按钮的标题，最长20个字符。 |
| btn\_orientation | String | 否 | 0 | 使用独立跳转**ActionCard**样式时的按钮排列方式。   - **0**：竖直排列 - **1**：横向排列   必须与**btn\_json\_list**同时设置。 |
| single\_url | String | 否 | https://open.dingtalk.com | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。  消息链接跳转，请参考[消息链接说明](1827-message-description-service-desk.md)。 |
| single\_title | String | 否 | 查看详情 | 使用整体跳转ActionCard样式时的标题。必须与single\_url同时设置，最长20个字符。  **[!NOTE]**  如果是整体跳转的ActionCard样式，则**single\_title**和**single\_url**必须设置。 |
| markdown | String | 否 | # 这是支持markdown的文本 | 消息内容，支持markdown，语法参考标准markdown语法。建议1000个字符以内。 |
| title | String | 否 |  | 透出到会话列表和通知的文案，最长64个字符 |
| user\_id\_list | String | 否 | user123,user456 | 接收者的userid列表，最大用户列表长度100。 |
| chat\_id\_list | String | 否 | 123,345 | 接收者的会话chatid列表，最大会话列表长度10。 |
| to\_all\_user | Boolean | 否 | false | 是否发送给企业全部用户。  **[!NOTE]**  当设置为**false**时必须指定**userid\_list**或**chat\_id\_list**其中一个参数的值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| task\_id | String | 6809f986xxxx | 创建的异步发送任务id |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 4jzllmte0wau | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartbot/msg/push?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "msg": {
    "msgtype": "text",
    "text": {
      "content": "请提交日报。"
    }
  },
  "user_id_list": "user456"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartbot/msg/push");
OapiSmartbotMsgPushRequest req = new OapiSmartbotMsgPushRequest();
Text text = new Text();
text.setContent("请提交日报。");
Msg msg = new Msg();
msg.setText(text);
msg.setMsgtype("text");
req.setUserIdList("user456");
req.setMsg(msg);
OapiSmartbotMsgPushResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "task_id": "6809f986xxxx",
  "request_id": "5o3k8aamtrva"
}
```
