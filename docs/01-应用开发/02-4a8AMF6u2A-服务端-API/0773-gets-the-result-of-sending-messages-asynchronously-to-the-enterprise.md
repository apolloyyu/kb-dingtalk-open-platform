---
title: "获取工作通知消息的发送结果"
source_url: "https://open.dingtalk.com/document/development/gets-the-result-of-sending-messages-asynchronously-to-the-enterprise"
namespace: "development"
slug: "gets-the-result-of-sending-messages-asynchronously-to-the-enterprise"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 消息通知 > 工作通知 > 获取工作通知消息的发送结果"
doc_id: "uUgjebUmeZ"
updated_at: "2026-07-13 09:45:39"
---

> Source: https://open.dingtalk.com/document/development/gets-the-result-of-sending-messages-asynchronously-to-the-enterprise
> Path: 应用开发 / 服务端 API / 即时通信 > 消息通知 > 工作通知 > 获取工作通知消息的发送结果
> Updated: 2026-07-13 09:45:39

# 获取工作通知消息的发送结果

调用本接口，查询工作通知消息的发送结果。

## **接口调用说明**

本接口适用于需要确认工作通知消息是否成功送达特定人员的场景，如企业 HR 部门发送重要通知后需要确认员工接收情况。

> **[!NOTE]**
>
> - 调用本接口，只能获取24小时内工作通知消息的发送结果。
> - 当接收人列表超过100人时，不支持调用本接口，否则系统会返回**调用超时**。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult |
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
| agent\_id | Number | 是 | 836390886 | 发送消息时使用的微应用的AgentID。   - 企业内部应用，可在[开发者后台](https://open-dev.dingtalk.com/#/appMgr/inner/h5/836390886/1)的应用详情页面查看。image - 第三方企业应用可调用[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取。 |
| task\_id | Number | 是 | 256271667526 | 发送消息时钉钉返回的任务ID，调用[发送工作通知](0769-asynchronous-sending-of-enterprise-session-messages.md)接口获取task\_id参数值。  **[!NOTE]**  仅支持查询24小时内的任务。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=cfe36xxxxd8dbce' \
-d 'agent_id=123' \
-d 'task_id=456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult");
OapiMessageCorpconversationGetsendresultRequest req = new OapiMessageCorpconversationGetsendresultRequest();
req.setAgentId(123L);
req.setTaskId(456L);
OapiMessageCorpconversationGetsendresultResponse rsp = client.execute(req, accessToken);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiMessageCorpconversationGetsendresultRequest("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult")

req.agent_id=123
req.task_id=456
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
$req = new OapiMessageCorpconversationGetsendresultRequest;
$req->setAgentId("123");
$req->setTaskId("456");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/message/corpconversation/getsendresult");
OapiMessageCorpconversationGetsendresultRequest req = new OapiMessageCorpconversationGetsendresultRequest();
req.AgentId = 123L;
req.TaskId = 456L;
OapiMessageCorpconversationGetsendresultResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| send\_result | AsyncSendResult |  | 返回结果。 |
| invalid\_user\_id\_list | String[] | ["manager4220",user123"] | 无效的userId。 |
| forbidden\_user\_id\_list | String[] | ["manager4220",user123"] | 因发送消息过于频繁或超量而被流控过滤后实际未发送的userId。  未被限流的接收者仍会被成功发送。  限流规则包括：   - 给同一用户发相同内容消息一天仅允许一次。 - 同一个应用给同一个用户发送消息：    - 如果是第三方企业接入方式，给同一用户发消息一天不得超过100次。   - 如果是企业接入方式，此上限为500。 |
| failed\_user\_id\_list | String[] | ["manager4220",user123"] | 发送失败的userId。 |
| read\_user\_id\_list | String[] | ["manager4220",user123"] | 已读消息的userId。 |
| unread\_user\_id\_list | String[] | ["manager4220",user123"] | 未读消息的userId。 |
| invalid\_dept\_id\_list | Number[] | [1,2,3] | 无效的部门ID。 |
| forbidden\_list | SendForbiddenModel[] |  | 推送被禁止的具体原因。 |
| code | String | 143105 | 流控code。   - 143105表示企业自建应用每日推送给用户的消息超过上限。 - 143106表示企业自建应用推送给用户的消息重复。 |
| count | Number | 1 | 流控阈值。 |
| userid | String | user123 | 被流控员工的userId。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6pcvwp6jcows | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "send_result": {
    "failed_user_id_list": [],
    "forbidden_list": [],
    "invalid_dept_id_list": [],
    "invalid_user_id_list": [],
    "read_user_id_list": [
      "manager4220"
    ],
    "unread_user_id_list": []
  },
  "request_id": "6pcvwp6jcows"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码 | 描述 | 解决方案 |
| --- | --- | --- |
| 143103 | 企业单应用消息发送人次QPM超限 | 接口调用太快，稍后重试。 |
| 143104 | 企业每分钟发送人次QPM超限 | 接口调用太快，稍后重试。 |
| 143105 | 单应用给单人每日推送量超限 | 企业每天给每个员工最多可发送500条消息通知，ISV最多可发送50条。 |
| 143106 | 单应用给单人推送重复消息超限 | 给同一员工一天只能发送一条内容相同的消息通知。 |
| 143203 | ISV单应用发送给单企业人次QPM超限 | 接口调用太快，稍后重试。 |
| 143204 | ISV单应用发送给所有企业人次QPM超限 | 接口调用太快，稍后重试。 |
| 143205 | 单应用给单人每日推送量超限 | 企业每天给每个员工最多可发送500条消息通知，ISV最多可发送50条。 |
| 143206 | 单应用给单人推送重复消息超限 | 给同一员工一天只能发送一条内容相同的消息通知。 |
| 1430000 | 接收者为空 | 接收者不能为空，请检查消息接收者是否为空。 |
| 1430001 | 未识别的grantType | 无。 |
| 1430002 | 包含违禁内容 | 检查消息文本中是否有黄色、反动等词语。 |
| 1430003 | 触发OAPI系统保护 | 无。 |
| 1430004 | 超级高管保护 | 关闭高管保护。 |
