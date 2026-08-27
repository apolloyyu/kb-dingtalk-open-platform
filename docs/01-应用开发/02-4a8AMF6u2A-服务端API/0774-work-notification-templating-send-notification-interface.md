---
title: "使用模板发送工作通知消息"
source_url: "https://open.dingtalk.com/document/development/work-notification-templating-send-notification-interface"
namespace: "development"
slug: "work-notification-templating-send-notification-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 使用模板发送工作通知消息"
doc_id: "vXJurUZi0m"
updated_at: "2026-07-13 09:45:40"
---

> Source: https://open.dingtalk.com/document/development/work-notification-templating-send-notification-interface
> Path: 应用开发 / 服务端API / 即时通信 > 消息通知 > 工作通知 > 使用模板发送工作通知消息
> Updated: 2026-07-13 09:45:40

# 使用模板发送工作通知消息

调用本接口，使用消息模板发送工作通知。

## **接口调用说明**

> **[!IMPORTANT]**
>
> 在调用本接口前，确保已经在开发者后台配置并启用了消息模板。详情请参考[创建和配置消息模板](0765-manage-message-templates.md)。

第三方企业应用调用本接口，发送工作通知消息需要注意以下事项：

- 单次发送人数最大1000。
- 每分钟接收人数最大5000。
- 给同一员工，每天只能发送一条内容相同的消息。
- 每天给每个员工最多可发送100条。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agent\_id | Number | 是 | 948060598 | 应用的agentid，可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| template\_id | String | 是 | e27a9eed42b34a14a2xxxx | 消息模板ID。  在[开发者后台](https://open-dev.dingtalk.com/#/isveapp)应用的**开发管理**页面查看。 |
| userid\_list | String | 否 | "123,456" | 接收者的用户userId列表。最大列表长度为5000。 |
| dept\_id\_list | String | 否 | 421897262 | 接收者的部门id列表。最大列表长度为500。  **[!IMPORTANT]**  **dept\_id\_list**和**userid\_list**不能同时为空。 |
| data | String | 否 | {\"name\":\"淘宝6\",\"name2\":\"[https://www.taobao.com\](http://www.taobao.com\)"} | 消息模板动态参数赋值数据。  **[!NOTE]**  key和value均为字符串格式。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=bdefeb04-96ad-40d9-bb92-a62a99d2e8d3' \
-d 'agent_id=123' \
-d 'data=%7B%5C%22%E5%90%8D%E5%AD%97%5C%22%3A%5C%22%E5%BC%A0%E4%B8%89%5C%22%7D' \
-d 'dept_id_list=%5C%22123%2C456%5C%22' \
-d 'template_id=xxxx' \
-d 'userid_list=%5C%22123%2C456%5C%22'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate");
OapiMessageCorpconversationSendbytemplateRequest req = new OapiMessageCorpconversationSendbytemplateRequest();
req.setAgentId(948060598L);
req.setDeptIdList("421897262");
req.setUseridList("123,456");
req.setTemplateId("e27a9eed42b34a14a2xxxx");
req.setData("{\"name\":\"淘宝6\",\"name2\":\"http://www.taobao.com\"}");
OapiMessageCorpconversationSendbytemplateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageCorpconversationSendbytemplateRequest("https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate")

req.agent_id=123
req.userid_list=""123,456""
req.dept_id_list=""123,456""
req.template_id="xxxx"
req.data="{\"名字\":\"张三\"}"
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
$req = new OapiMessageCorpconversationSendbytemplateRequest;
$req->setAgentId("123");
$req->setUseridList("\"123,456\"");
$req->setDeptIdList("\"123,456\"");
$req->setTemplateId("xxxx");
$req->setData("{\"名字\":\"张三\"}");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/sendbytemplate");
OapiMessageCorpconversationSendbytemplateRequest req = new OapiMessageCorpconversationSendbytemplateRequest();
req.AgentId = 123L;
req.UseridList = "\"123,456\"";
req.DeptIdList = "\"123,456\"";
req.TemplateId = "xxxx";
req.Data = "{\"名字\":\"张三\"}";
OapiMessageCorpconversationSendbytemplateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| task\_id | Number | 282632271040 | 创建的异步发送任务ID。 |
| request\_id | String | 52izpwz1p0iw | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "task_id": 282632271040,
  "request_id": "52izpwz1p0iw"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误信息描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 885001 | 消息模板不存在 | 确认消息模板是否正确 |
| 885006 | 消息模板不可用 | 消息模板需要先审批通过 |
| 400002 | agentId不合法 | 确认agentId是否正确 |
| 500 | 系统异常 | 出现未知的系统异常 |
