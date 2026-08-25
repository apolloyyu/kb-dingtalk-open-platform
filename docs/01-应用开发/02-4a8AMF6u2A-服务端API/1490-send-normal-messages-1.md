---
title: "发送普通消息"
source_url: "https://open.dingtalk.com/document/development/send-normal-messages-1"
namespace: "development"
slug: "send-normal-messages-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 即时通信 > 消息通知 > 普通消息 > 发送普通消息"
doc_id: "c3wFqfxHQD"
updated_at: "2026-08-25 09:37:21"
---

> Source: https://open.dingtalk.com/document/development/send-normal-messages-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 即时通信 > 消息通知 > 普通消息 > 发送普通消息
> Updated: 2026-08-25 09:37:21

# 发送普通消息

调用本接口发送普通消息。

> **[!IMPORTANT]**
>
> - 为提升接口的使用体验，当前接口计划升级，重新开放时间请[开放概览](0764-message-corpconversation-overview.md#section-rtj-q87-8ea)。
> - 不再支持新应用接入，已接入用户不受影响。

发送普通消息是指员工个人在使用应用时，可以通过界面操作的方式向群或其他人的会话中推送消息，例如发送日志的场景。

发送普通消息，需要在前端页面调用JSAPI唤起联系人会话选择页面，选中后会返回会话cid，然后再调用服务端接口向会话里发送一条消息，如下图所示：

> **[!IMPORTANT]**
>
> 发送普通消息需要注意以下事项：
>
> - 不在当前接口调用所使用的企业的接收者（单聊接收者或者群聊会话里的接收者）不能收到消息。
> - 获取到的会话cid只能使用一次，且有效期为24小时。
> - 消息类型和样例，可参考[消息通知类型](0775-message-types-and-data-format.md)。

![群消息示例 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9534199951/p157712.png)

## 权限

该接口权限默认已添加，无需申请。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/message/send_to_conversation`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用，可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，可通[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| sender | String | 是 | user123 | 消息发送者的userid。 |
| cid | String | 是 | 123 | 群会话或者个人会话的id，通过JSAPI接口唤起联系人界面选择会话获取会话cid。 |
| msg | JSON Object | 是 | {"msgtype":"text","text":{"content":"请提交日报。"} | 消息内容，可参考[消息通知类型](0775-message-types-and-data-format.md)，最长不超过2048个字节。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| receiver | String | UserID1|UserID2 | 有效接收消息的员工的userid。   - 接收者可以是单聊接收者或者群聊会话里的接收者，如果接收者是当前接口调用所使用的企业的员工，则是有效接收者。 - 接口返回所有有效接收者的userid。 - 非有效接收者是收不到消息的。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/message/send_to_conversation?access_token=ACCESS_TOKEN
```

请求正文

```
{
   "sender":"user123",
   "cid":"9f540d572b71cf97a556d95929f335",
   "msg":{
      "msgtype":"text",
      "text":{
         "content":"9月运动会通知"
      }
   }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/message/send_to_conversation");

OapiMessageSendToConversationRequest req = new OapiMessageSendToConversationRequest();
req.setSender("01376814877479");
req.setCid("14ac70d94e79377b88aa5fc75759fe84");
OapiMessageSendToConversationRequest.Msg msg = new OapiMessageSendToConversationRequest.Msg();

// 文本消息
OapiMessageSendToConversationRequest.Text text = new OapiMessageSendToConversationRequest.Text();
text.setContent("测试测试");
msg.setText(text);
msg.setMsgtype("text");
req.setMsg(msg);

// 图片
OapiMessageSendToConversationRequest.Image image = new OapiMessageSendToConversationRequest.Image();
image.setMediaId("@lADOdvRYes0CbM0CbA");
msg.setImage(image);
msg.setMsgtype("image");
req.setMsg(msg);

// 文件
OapiMessageSendToConversationRequest.File file = new OapiMessageSendToConversationRequest.File();
file.setMediaId("@lADOdvRYes0CbM0CbA");
msg.setFile(file);
msg.setMsgtype("file");
req.setMsg(msg);

OapiMessageSendToConversationRequest.Markdown markdown = new OapiMessageSendToConversationRequest.Markdown();
markdown.setText("# 这是支持markdown的文本 \\n## 标题2  \\n* 列表1 \\n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)");
markdown.setTitle("首屏会话透出的展示内容");
msg.setMarkdown(markdown);
msg.setMsgtype("markdown");
req.setMsg(msg);

OapiMessageSendToConversationRequest.ActionCard actionCard = new OapiMessageSendToConversationRequest.ActionCard();
actionCard.setTitle("是透出到会话列表和通知的文案");
actionCard.setMarkdown("持markdown格式的正文内");
actionCard.setSingleTitle("查看详情");
actionCard.setSingleUrl("https://open.dingtalk.com");
msg.setActionCard(actionCard);
msg.setMsgtype("action_card");
req.setMsg(msg);

// link消息
OapiMessageSendToConversationRequest.Link link = new OapiMessageSendToConversationRequest.Link();
link.setMessageUrl("https://www.baidu.com/");
link.setPicUrl("@lADOdvRYes0CbM0CbA");
link.setText("测试");
link.setTitle("oapi");
msg.setLink(link);
msg.setMsgtype("link");
req.setMsg(msg);

OapiMessageSendToConversationResponse response = client.execute(req, accessToken);
System.out.println(response.getBody());
```

**返回示例**

```
{
        "errcode":"0",
        "receiver":"UserID1|UserID2",
        "errmsg":"ok"
}
```
