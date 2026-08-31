---
title: "创建日志"
source_url: "https://open.dingtalk.com/document/development/create-a-log"
namespace: "development"
slug: "create-a-log"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 创建日志"
doc_id: "DvP1O1C2FE"
updated_at: "2026-05-27 13:10:11"
---

> Source: https://open.dingtalk.com/document/development/create-a-log
> Path: 应用开发 / 服务端 API / 日志 > 创建日志
> Updated: 2026-05-27 13:10:11

# 创建日志

调用本接口创建日志，对应日志模板中的每个组件只允许是文本类型，其他类型组件暂不支持接口调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_report\_manage-员工日志数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| create\_report\_param | OapiCreateReportParam | 是 |  | 创建日志的参数对象。 |
| contents | OapiReportContentVo[] | 是 |  | 日志内容数组，根据该日志模板中每一项信息传参。 |
| sort | Number | 是 | 0 | 写日志对应的模板某个字段的唯一序列ID，可调用[获取模板详情](0296-query-template-details.md)接口获取sort参数值。 |
| type | Number | 是 | 1 | 写日志对应的模板某个字段的类型，可调用[获取模板详情](0296-query-template-details.md)接口获取type参数值。  **[!NOTE]**  只支持文本类型日志组件，即type参数固定值为1，其他类型不支持。 |
| content\_type | String | 是 | markdown | 日志内容的类型。  **[!NOTE]**   - 目前支持markdown类型。 - 支持[获取模板详情](0296-query-template-details.md)接口中，日志组件是**文本**的类型。 |
| content | String | 是 | ### 序号1 | 日志内容。  **[!NOTE]**   - 只支持 Markdown 语法。 - 内容不能超过 1000 字符，超出的内容会被截断。 |
| key | String | 是 | 今日完成工作 | 写日志对应的模板某个字段的标题，可调用[获取模板详情](0296-query-template-details.md)接口获取field\_name参数值。 |
| template\_id | String | 是 | 12345abcde | 模板ID，可调用[获取模板详情](0296-query-template-details.md)接口获取id参数值。 |
| to\_userids | String[] | 否 | ["123","456"] | 日志发送到的员工userId。 |
| to\_chat | Boolean | 是 | true | 发送日志到员工时是否发送单聊消息。   - **true**：发送日志消息给指定用户 - **false**：不单独发送消息 |
| to\_cids | String[] | 否 | 123 | 日志要发送到的群ID。配置接收群后，可调用[获取模板详情](0296-query-template-details.md)接口获取**conversation\_id**参数值，即为发送到的群ID。  **[!IMPORTANT]**   - 该群是在日志模板中预先已经配置好的接收群。如果没有配置，则无法发送到指定的群。 - 进入**钉钉工作台**，然后选择**日志 > 模板管理 > 权限设置 > 默认发送范围**，设置该日志模板的默认接收群。image |
| dd\_from | String | 是 | report | 日志来源，每个组织可以自己起一个唯一的来源标识，自定义的值。 |
| userid | String | 是 | 12345 | 创建日志的员工userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/create?access_token=YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "create_report_param": {
      "contents": [
        {
          "sort": 0,
          "type": 1,
          "content_type": "markdown",
          "content": "### 今日完成工作\n1. 完成项目需求分析\n2. 编写技术方案文档",
          "key": "今日完成工作"
        },
        {
          "sort": 1,
          "type": 1,
          "content_type": "markdown",
          "content": "### 明日计划\n1. 开始编码实现\n2. 进行单元测试",
          "key": "明日计划"
        }
      ],
      "template_id": "12345abcde",
      "to_userids": ["user123", "user456"],
      "to_chat": true,
      "to_cids": ["cid123"],
      "dd_from": "report",
      "userid": "user123"
    }
  }'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/create");
OapiReportCreateRequest req = new OapiReportCreateRequest();
OapiCreateReportParam obj1 = new OapiCreateReportParam();
List<OapiReportContentVo> list3 = new ArrayList<OapiReportContentVo>();
OapiReportContentVo obj4 = new OapiReportContentVo();
list3.add(obj4);
obj4.setSort(0L);
obj4.setType(1L);
obj4.setContentType("markdown");
obj4.setContent("### 序号1");
obj4.setKey("字段1");
obj1.setContents(list3);
obj1.setToUserids(""123","456"");
obj1.setTemplateId("12345abcde");
obj1.setToChat(true);
obj1.setDdFrom("report");
obj1.setUserid("12345");
obj1.setToCids(""123","456"");
req.setCreateReportParam(obj1);
OapiReportCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiReportCreateRequest("https://oapi.dingtalk.com/topapi/report/create")

req.create_report_param=""
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
$req = new OapiReportCreateRequest;
$create_report_param = new OapiCreateReportParam;
$contents = new OapiReportContentVo;
$contents->sort="0";
$contents->type="1";
$contents->content_type="markdown";
$contents->content="### 序号1";
$contents->key="字段1";
$create_report_param->contents = array($contents);
$create_report_param->to_userids="[\"123\",\"456\"]";
$create_report_param->template_id="12345abcde";
$create_report_param->to_chat="true";
$create_report_param->dd_from="report";
$create_report_param->userid="12345";
$create_report_param->to_cids="[\"123\",\"456\"]";
$req->setCreateReportParam($create_report_param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/create");
OapiReportCreateRequest req = new OapiReportCreateRequest();
OapiReportCreateRequest.OapiCreateReportParamDomain obj1 = new OapiReportCreateRequest.OapiCreateReportParamDomain();
List<OapiReportCreateRequest.OapiReportContentVoDomain> list3 = new List<OapiReportCreateRequest.OapiReportContentVoDomain>();
OapiReportCreateRequest.OapiReportContentVoDomain obj4 = new OapiReportCreateRequest.OapiReportContentVoDomain();
list3.Add(obj4);
obj4.Sort = 0L;
obj4.Type = 1L;
obj4.ContentType = "markdown";
obj4.Content = "### 序号1";
obj4.Key = "字段1";
obj1.Contents= list3;
obj1.ToUserids = ""123","456"";
obj1.TemplateId = "12345abcde";
obj1.ToChat = true;
obj1.DdFrom = "report";
obj1.Userid = "12345";
obj1.ToCids = ""123","456"";
req.CreateReportParam_ = obj1;
OapiReportCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| result | String | 175abec4de6bd | 调用结果。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": "1734xxxxxxe08500e",
  "request_id": "5kaikoe9uc8i"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
