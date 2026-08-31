---
title: "发送工作通知"
source_url: "https://open.dingtalk.com/document/development/asynchronous-sending-of-enterprise-session-messages"
namespace: "development"
slug: "asynchronous-sending-of-enterprise-session-messages"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 发送工作通知"
doc_id: "qjsm3ypsHu"
updated_at: "2026-05-29 09:13:40"
---

> Source: https://open.dingtalk.com/document/development/asynchronous-sending-of-enterprise-session-messages
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 工作通知 > 发送工作通知
> Updated: 2026-05-29 09:13:40

# 发送工作通知

调用本接口发送工作通知消息。

## **接口调用说明**

工作通知消息是以某个应用的名义推送到员工的工作通知消息，例如生日祝福、入职提醒等。可以发送文本、语音、链接等，消息类型和样例可参考[消息通知类型](0775-message-types-and-data-format.md)。

> **[!NOTE]**
>
> 如果接口发送成功，接收人没有收到信息，可调用[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)查询结果，并对比文档中的返回错误码。

![工作通知](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5476921161/p230053.png)

### **使用场景**

> **[!IMPORTANT]**
>
> 2020年11月27日以后创建的第三方企业应用，请调用[使用模板发送工作通知消息](0774-work-notification-templating-send-notification-interface.md)接口发送工作通知。

- 适用场景：适用于发送通知类的消息，不包含审批任务等。
- 不适用场景：需要发送一条任务类的通知提醒给员工，比如审批任务等，调用此接口无法实现。这种场景可以使用[创建待办](0793-add-dingtalk-to-do-task.md)接口。

### **频率限制**

**超出以下限制次数后，接口返回成功，但用户无法接收到。**

> **[!NOTE]**
>
> 详细的限制说明，请参考[调用频率限制](0012-call-frequency-limit.md)。

- 企业内部应用发送消息单次最多只能给5000人发送，第三方企业应用发送消息单次最多能给1000人发送。
- 给同一员工一天只能发送一条内容相同的消息通知。
- 企业内部应用每天给每个员工最多可发送500条消息通知，第三方企业应用最多可发送100条。
- 企业内部应用或第三方企业应用发送消息时，每分钟最多有5000人可以接收到消息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend\_v2 |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agent\_id | Long | 是 | 123L | 发送消息时使用的微应用的AgentID。   - 企业内部应用可在[开发者后台](https://open-dev.dingtalk.com/#/appMgr/inner/h5/836390886/1)的应用详情页面查看。 - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| userid\_list | String | 否 | user123,user456 | 接收者的userid列表，最大用户列表长度100。 |
| dept\_id\_list | String | 否 | 123,345 | 接收者的部门id列表，最大列表长度20。  接收者是部门ID时，包括子部门下的所有用户。 |
| to\_all\_user | Boolean | 否 | false | 是否发送给企业全部用户。  **[!NOTE]**  当设置为false时必须指定userid\_list或dept\_id\_list其中一个参数的值。 |
| msg | JSON Object | 是 | {  "msgtype": "text",  "text": {  "content": "请提交日报。"  }  } | 消息内容，最长不超过2048个字节，支持以下[消息通知类型](0775-message-types-and-data-format.md)，msgtype 包括：  **[!IMPORTANT]**  发送消息时，不支持同时发送多种消息类型。   - text：文本消息 - image：图片消息 - voice：语音消息 - file：文件消息 - link：链接消息 - oa：OA消息  **[!NOTE]**  OA消息支持通过`status_bar`参数设置消息状态文案和颜色，发送后可通过[更新工作通知状态栏](0771-update-work-notification-status-bar.md)接口更新消息状态和颜色。 - markdown：Markdown消息 - action\_card：卡片消息 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7e0a4xxxx31351' \
-d 'agent_id=123' \
-d 'dept_id_list=123%2C456' \
-d 'msg=%7B+++++%5C%22msgtype%5C%22%3A+%5C%22text%5C%22%2C+++++%5C%22text%5C%22%3A+%7B+++++++++%5C%22content%5C%22%3A+%5C%22%E5%BC%A0%E4%B8%89%E7%9A%84%E8%AF%B7%E5%81%87%E7%94%B3%E8%AF%B7%5C%22+++++%7D+%7D' \
-d 'to_all_user=false' \
-d 'userid_list=123%2C456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2");
OapiMessageCorpconversationAsyncsendV2Request request = new OapiMessageCorpconversationAsyncsendV2Request();
request.setAgentId(2839445214L);
request.setUseridList("0147282552401293909,manager4974");
request.setToAllUser(false);
OapiMessageCorpconversationAsyncsendV2Request.Msg msg = new OapiMessageCorpconversationAsyncsendV2Request.Msg();
msg.setMsgtype("text");
OapiMessageCorpconversationAsyncsendV2Request.Text text = new OapiMessageCorpconversationAsyncsendV2Request.Text();
text.setContent("test123");
msg.setText(text);
request.setMsg(msg);
OapiMessageCorpconversationAsyncsendV2Response rsp = client.execute(request, accessToken);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageCorpconversationAsyncsendV2Request("https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2")

req.agent_id=123
req.userid_list="123,456"
req.dept_id_list="123,456"
req.to_all_user=false
req.msg="{\"msgtype\":\"text\",\"text\": {\"content\": \"张三的请假申请\"}}"
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
$req = new OapiMessageCorpconversationAsyncsendV2Request;
$req->setAgentId("123");
$req->setUseridList("123,456");
$req->setDeptIdList("123,456");
$req->setToAllUser("false");
$msg = new Msg;
$msg->msgtype="text";
$text = new Text;
$text->content="123";
$msg->text = $text;
$req->setMsg($msg);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/asyncsend_v2");
OapiMessageCorpconversationAsyncsendV2Request req = new OapiMessageCorpconversationAsyncsendV2Request();
req.AgentId = 123L;
req.UseridList = "123,456";
req.DeptIdList = "123,456";
req.ToAllUser = false;
OapiMessageCorpconversationAsyncsendV2Request.MsgDomain obj1 = new OapiMessageCorpconversationAsyncsendV2Request.MsgDomain();
obj1.Msgtype = "text";
OapiMessageCorpconversationAsyncsendV2Request.TextDomain obj2 = new OapiMessageCorpconversationAsyncsendV2Request.TextDomain();
obj2.Content = "123";
obj1.Text= obj2;
req.Msg_ = obj1;
OapiMessageCorpconversationAsyncsendV2Response rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 4jzllmte0wau | 请求ID。 |
| errmsg | String | ok | 返回码描述。  **[!IMPORTANT]**  如果接口发送成功，接收人没有收到信息，可调用[获取工作通知消息的发送结果](0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)查询结果，并对比文档中的返回错误码。 |
| errcode | Number | 0 | 返回码。 |
| task\_id | Number | 256271667526 | 创建的异步发送任务ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "task_id":256271667526,
  "request_id":"4jzllmte0wau"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
