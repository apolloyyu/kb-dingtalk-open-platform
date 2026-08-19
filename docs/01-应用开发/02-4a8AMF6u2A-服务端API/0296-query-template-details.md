---
title: "获取模板详情"
source_url: "https://open.dingtalk.com/document/development/query-template-details"
namespace: "development"
slug: "query-template-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "日志 > 获取模板详情"
doc_id: "rjUekkv7Wb"
updated_at: "2026-05-27 13:10:14"
---

> Source: https://open.dingtalk.com/document/development/query-template-details
> Path: 应用开发 / 服务端API / 日志 > 获取模板详情
> Updated: 2026-05-27 13:10:14

# 获取模板详情

调用本接口，根据日志模板名称获取模板详情，包含日志模板内的字段信息、默认接收群、日志模板ID等信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/template/getbyname |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_report\_statistics-钉钉日志统计数据读权限permission-qyapi\_report\_query-企业员工日志读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | 12345 | 操作该接口的员工userId。 |
| template\_name | String | 是 | 日报 | 模板名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/template/getbyname" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9e5ffxxxx8018b' \
-d 'template_name=日报' \
-d 'userid=12345'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/template/getbyname");
OapiReportTemplateGetbynameRequest req = new OapiReportTemplateGetbynameRequest();
req.setUserid("12345");
req.setTemplateName("日报");
OapiReportTemplateGetbynameResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportTemplateGetbynameRequest("https://oapi.dingtalk.com/topapi/report/template/getbyname")

req.userid="12345"
req.template_name="日报"
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
$req = new OapiReportTemplateGetbynameRequest;
$req->setUserid("12345");
$req->setTemplateName("日报");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/template/getbyname");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/template/getbyname");
OapiReportTemplateGetbynameRequest req = new OapiReportTemplateGetbynameRequest();
req.Userid = "12345";
req.TemplateName = "日报";
OapiReportTemplateGetbynameResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ReportTemplateResponseVo |  | 返回结果。 |
| default\_receivers | DefaultReceivers[] |  | 模板默认接收人。 |
| user\_name | String | 用户1 | 默认接收人名称。 |
| userid | String | 111 | 默认接收人员工的userId。 |
| name | String | 周报 | 模板名称。 |
| id | String | 12345abcde | 模板ID。 |
| fields | Fields[] |  | 日志模板内各字段的信息。 |
| field\_name | String | 字段1 | 模板字段名称。 |
| type | Number | 1 | 字段类型。 |
| sort | Number | 0 | 模板字段在当前模板内排序。 |
| user\_name | String | 小明 | 操作该接口的员工姓名。 |
| userid | String | 12345 | 操作该接口的员工userId。 |
| default\_received\_convs | BaseConversationVo[] |  | 默认接收群。  **[!NOTE]**  模板中如果没有设置默认接收群，该字段不会返回。 |
| conversation\_id | String | 1223445 | 该日志模板的默认接收群ID。  **[!NOTE]**  进入**钉钉工作台**，然后选择**日志 > 模板管理 > 权限设置 > 默认发送范围**，设置该日志模板的默认接收群。image |
| title | String | 群名称 | 群名称。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "default_received_convs": [
      {
        "conversation_id": "$DD_KExxxx1YA==",
        "title": "开放平台"
      }
    ],
    "default_receivers": [
      {
        "user_name": "测试主管",
        "userid": "user123"
      }
    ],
    "fields": [
      {
        "field_name": "今日完成工作",
        "sort": 0,
        "type": 1
      },
      {
        "field_name": "未完成工作",
        "sort": 1,
        "type": 1
      }
    ],
    "id": "173xxxxxx08500e",
    "name": "日报",
    "user_name": "测试用户",
    "userid": "user456"
  },
  "request_id": "y5yrfbh3n40u"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
