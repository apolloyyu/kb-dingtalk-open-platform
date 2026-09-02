---
title: "自定义机器人发送群消息"
source_url: "https://open.dingtalk.com/document/development/custom-robots-send-group-messages"
namespace: "development"
slug: "custom-robots-send-group-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 机器人 > 发送普通消息 > 自定义机器人发送群消息"
doc_id: "uHJmwtLsII"
updated_at: "2026-07-14 09:21:57"
---

> Source: https://open.dingtalk.com/document/development/custom-robots-send-group-messages
> Path: 应用开发 / 服务端 API / 即时通信 > 机器人 > 发送普通消息 > 自定义机器人发送群消息
> Updated: 2026-07-14 09:21:57

# 自定义机器人发送群消息

调用本接口，使用自定义机器人发送群消息。

## **接口调用说明**

- 本接口支持自定义机器人在企业内部群和普通群中发送消息，调用本接口前需要创建自定义机器人，可参见[开发机器人应用](0698-development-robot-overview.md)。
- 如果你有大量发消息的场景（譬如系统监控报警）可以将这些信息进行整合，通过markdown消息以摘要的形式发送到群里。
- 如果自定义机器人的安全设置使用的是[自定义机器人安全设置](../01-XOnnmGCTbn-开发指南/0084-customize-robot-security-settings.md)，调用本接口发送消息时，需要拼接timestamp和sign参数，示例为：

  ```
  https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
  ```
- **每个机器人每分钟最多发送20条消息到群里，如果超过20条，会限流10分钟。**

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/robot/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API基础权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | BE3xxxx | 自定义机器人调用接口的凭证。  自定义机器人安装后webhook地址中的access\_token值。详情参考[获取自定义机器人 Webhook 地址](../01-XOnnmGCTbn-开发指南/0085-obtain-the-webhook-address-of-a-custom-robot.md)。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| msgtype | String | 是 | text | 消息类型，自定义机器人可发送的消息类型参见[消息发送与接收类型](0699-robot-message-type.md)。 |
| msgUuid | String | 否 | 123 | 消息幂等key，可用于控制消息幂等。  **[!NOTE]**  典型的使用场景：发消息时接口调用超时或未知错误等报错，开发者可使用同一个msgUuid重试，避免重复发出消息。 |
| text | Object | 否 |  | 文本类型消息。 |
| content | String | 否 | 钉钉，让进步发生 | 文本消息的内容。 |
| at | Object | 否 |  | 被@的群成员信息。 |
| isAtAll | Boolean | 否 | false | 是否@所有人。   - true：是 - false：否 |
| atMobiles | String[] | 否 | ["15xxx,18xxx"] | 被@的群成员手机号。 |
| atUserIds | String[] | 否 | ["user001","user002"] | 被@的群成员userId。  **[!NOTE]**  在@群成员时，最多只能@50个。 |
| link | Object | 否 |  | 链接类型消息。 |
| messageUrl | String | 否 | https://www.dingtalk.com | 点击消息跳转的URL。 |
| title | String | 否 | 这是标题 | 链接消息标题。 |
| picUrl | String | 否 | @aubHxxxxx | 链接消息内的图片地址，建议使用[上传媒体文件](0646-upload-media-files.md)接口获取。 |
| text | String | 否 | 链接消息的内容 | 链接消息的内容。 |
| markdown | Object | 否 |  | markdown类型消息。 |
| text | String | 否 | markdown消息内容 | markdown类型消息的文本内容。 |
| title | String | 否 | 会话列表展示的标题 | 消息会话列表中展示的标题，非消息体的标题。 |
| actionCard | Object | 否 |  | actionCard类型消息。 |
| hideAvatar | String | 否 | 1 | 是否显示消息发送者头像。   - 0：正常发消息者头像 - 1：隐藏发消息者头像 |
| btnOrientation | String | 否 | 1 | 消息内按钮排列方式。   - 0：按钮竖直排列 - 1：按钮横向排列 |
| singleURL | String | 否 | https://www.dingtalk.com | 点击singleTitle按钮触发的URL。  **[!NOTE]**  消息内只有一个按钮时，该参数必填。 |
| singleTitle | String | 否 | 这是一个按钮 | 单个按钮的方案。(设置此项和singleURL后btns无效。)  **[!NOTE]**  消息内只有一个按钮时，该参数必填。 |
| text | String | 否 | 消息内容 | actionCard类型消息的正文内容，支持markdown语法。 |
| title | String | 否 | 显示到会话列表中的标题 | 消息会话列表中展示的标题，非消息体的标题。 |
| btns | Object[] | 否 |  | 按钮的信息列表。  **[!NOTE]**  消息内不止一个按钮时，该参数必填。 |
| actionURL | String | 否 | https://www.dingtalk.com | 按钮跳转的URL。 |
| title | String | 否 | 这是一个按钮 | 按钮上显示的文本。 |
| feedCard | Object | 否 |  | feedCard类型消息。 |
| links | Object[] | 否 |  | feedCard消息的内容列表。 |
| picURL | String | 否 | @aubHxxxxx | feedCard消息内每条内容的图片URL，建议使用[上传媒体文件](0646-upload-media-files.md)接口获取。 |
| messageURL | String | 否 | https://www.dingtalk.com | feedCard消息内每条内容上午跳转链接。 |
| title | String | 否 | 消息标题 | feedCard消息内每条内容的标题。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/robot/send" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c370586xxxxd65d506' \
-d 'actionCard=null' \
-d 'at=null' \
-d 'feedCard=null' \
-d 'link=null' \
-d 'markdown=null' \
-d 'msgtype=text' \
-d 'text=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/robot/send");
OapiRobotSendRequest req = new OapiRobotSendRequest();
req.setMsgtype("text");
Text obj1 = new Text();
obj1.setContent("123");
req.setText(obj1);
At obj2 = new At();
obj2.setIsAtAll(false);
obj2.setAtMobiles("");
obj2.setAtUserIds("");
req.setAt(obj2);
Link obj3 = new Link();
obj3.setMessageUrl("1");
obj3.setTitle("1");
obj3.setPicUrl("1");
obj3.setText("1");
req.setLink(obj3);
Markdown obj4 = new Markdown();
obj4.setText("1");
obj4.setTitle("1");
req.setMarkdown(obj4);
Actioncard obj5 = new Actioncard();
obj5.setHideAvatar("1");
obj5.setBtnOrientation("1");
obj5.setSingleURL("1");
obj5.setSingleTitle("1");
obj5.setText("1");
obj5.setTitle("1");
List<Btns> list7 = new ArrayList<Btns>();
Btns obj8 = new Btns();
list7.add(obj8);
obj8.setActionURL("1");
obj8.setTitle("1");
obj5.setBtns(list7);
req.setActionCard(obj5);
Feedcard obj9 = new Feedcard();
List<Links> list11 = new ArrayList<Links>();
Links obj12 = new Links();
list11.add(obj12);
obj12.setPicURL("1");
obj12.setMessageURL("1");
obj12.setTitle("1");
obj9.setLinks(list11);
req.setFeedCard(obj9);
OapiRobotSendResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiRobotSendRequest("https://oapi.dingtalk.com/robot/send")

req.msgtype="text"
req.text=""
req.at=""
req.link=""
req.markdown=""
req.actionCard=""
req.feedCard=""
try:
	resp= req.getResponse(access_token)
	print(resp)
except Exception,e:
	print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiRobotSendRequest;
$req->setMsgtype("text");
$text = new Text;
$text->content="123";
$req->setText($text);
$at = new At;
$at->isAtAll="false";
$at->atMobiles="[]";
$at->atUserIds="[]";
$req->setAt($at);
$link = new Link;
$link->messageUrl="1";
$link->title="1";
$link->picUrl="1";
$link->text="1";
$req->setLink($link);
$markdown = new Markdown;
$markdown->text="1";
$markdown->title="1";
$req->setMarkdown($markdown);
$actionCard = new Actioncard;
$actionCard->hideAvatar="1";
$actionCard->btnOrientation="1";
$actionCard->singleURL="1";
$actionCard->singleTitle="1";
$actionCard->text="1";
$actionCard->title="1";
$btns = new Btns;
$btns->actionURL="1";
$btns->title="1";
$actionCard->btns = array($btns);
$req->setActionCard($actionCard);
$feedCard = new Feedcard;
$links = new Links;
$links->picURL="1";
$links->messageURL="1";
$links->title="1";
$feedCard->links = array($links);
$req->setFeedCard($feedCard);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/robot/send");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/robot/send");
OapiRobotSendRequest req = new OapiRobotSendRequest();
req.Msgtype = "text";
OapiRobotSendRequest.TextDomain obj1 = new OapiRobotSendRequest.TextDomain();
obj1.Content = "123";
req.Text_ = obj1;
OapiRobotSendRequest.AtDomain obj2 = new OapiRobotSendRequest.AtDomain();
obj2.IsAtAll = false;
obj2.AtMobiles = "";
obj2.AtUserIds = "";
req.At_ = obj2;
OapiRobotSendRequest.LinkDomain obj3 = new OapiRobotSendRequest.LinkDomain();
obj3.MessageUrl = "1";
obj3.Title = "1";
obj3.PicUrl = "1";
obj3.Text = "1";
req.Link_ = obj3;
OapiRobotSendRequest.MarkdownDomain obj4 = new OapiRobotSendRequest.MarkdownDomain();
obj4.Text = "1";
obj4.Title = "1";
req.Markdown_ = obj4;
OapiRobotSendRequest.ActioncardDomain obj5 = new OapiRobotSendRequest.ActioncardDomain();
obj5.HideAvatar = "1";
obj5.BtnOrientation = "1";
obj5.SingleURL = "1";
obj5.SingleTitle = "1";
obj5.Text = "1";
obj5.Title = "1";
List<OapiRobotSendRequest.BtnsDomain> list7 = new List<OapiRobotSendRequest.BtnsDomain>();
OapiRobotSendRequest.BtnsDomain obj8 = new OapiRobotSendRequest.BtnsDomain();
list7.Add(obj8);
obj8.ActionURL = "1";
obj8.Title = "1";
obj5.Btns= list7;
req.ActionCard_ = obj5;
OapiRobotSendRequest.FeedcardDomain obj9 = new OapiRobotSendRequest.FeedcardDomain();
List<OapiRobotSendRequest.LinksDomain> list11 = new List<OapiRobotSendRequest.LinksDomain>();
OapiRobotSendRequest.LinksDomain obj12 = new OapiRobotSendRequest.LinksDomain();
list11.Add(obj12);
obj12.PicURL = "1";
obj12.MessageURL = "1";
obj12.Title = "1";
obj9.Links= list11;
req.FeedCard_ = obj9;
OapiRobotSendResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 错误码描述。 |
| errcode | Number | 0 | 错误码。 |

### **响应体示例**

```
{
  "errcode":"0",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| -1 | 系统繁忙 | 请稍后重试 |
| 40035 | 缺少参数 json | 请补充消息json |
| 43004 | 无效的HTTP HEADER Content-Type | 请设置具体的消息参数 |
| 400013 | 群已被解散 | 请向其他群发消息 |
| 400101 | access\_token不存在 | 请确认access\_token拼写是否正确 |
| 400102 | 机器人已停用 | 请联系管理员启用机器人 |
| 400105 | 不支持的消息类型 | 请使用文档中支持的消息类型 |
| 400106 | 机器人不存在 | 请确认机器人是否在群中 |
| 410100 | 发送速度太快而限流 | 请降低发送速度 |
| 430101 | 含有不安全的外链 | 请确认发送的内容合法 |
| 430102 | 含有不合适的文本 | 请确认发送的内容合法 |
| 430103 | 含有不合适的图片 | 请确认发送的内容合法 |
| 430104 | 含有不合适的内容 | 请确认发送的内容合法 |

当出现以下错误时，表示消息校验未通过，请查看机器人的安全设置。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 310000 | - keywords not in content - invalid timestamp - sign not match - ip X.X.X.X not in whitelist | - 消息内容中不包含任何关键词 - timestamp 无效 - 签名不匹配 - IP地址不在白名单 |
