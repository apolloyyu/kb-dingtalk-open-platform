---
title: "保存日志内容"
source_url: "https://open.dingtalk.com/document/development/save-custom-log-content"
namespace: "development"
slug: "save-custom-log-content"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 保存日志内容"
doc_id: "2PKQTOVTxh"
updated_at: "2026-05-26 09:01:04"
---

> Source: https://open.dingtalk.com/document/development/save-custom-log-content
> Path: 应用开发 / 服务端 API / 日志 > 保存日志内容
> Updated: 2026-05-26 09:01:04

# 保存日志内容

调用本接口，保存自定义的日志内容，后续进入钉钉日志可在写日志页面再拉取此内容。以便将第三方系统的日志集成至钉钉日志中。

## **接口调用说明**

调用本接口，请配合[三方系统发起和查看日志信息](0293-log-api-use-cases.md)案例使用，相当于把需要发送的日志内容打包，在需要发送日志的时候拉取该内容显示到日志模板中。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/savecontent |
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
| create\_report\_param | OapiCreateReportParam | 是 |  | 保存日志的参数对象。 |
| contents | OapiReportContentVo[] | 是 |  | 日志内容数组。 |
| sort | Number | 是 | 0 | 写日志对应的模板某个字段的唯一序列ID，可调用[获取模板详情](0296-query-template-details.md)接口获取sort参数值。 |
| type | Number | 是 | 1 | 写日志对应的模板某个字段的类型，可调用[获取模板详情](0296-query-template-details.md)接口获取type参数值。  **[!NOTE]**  只支持文本类型日志组件，即type参数固定值为1，其他类型不支持。 |
| content\_type | String | 是 | markdown | 日志内容的类型。  **[!NOTE]**   - 目前支持markdown类型。 - 支持[获取模板详情](0296-query-template-details.md)接口中，日志组件是**文本**的类型。 |
| content | String | 是 | ### 序号1 | 日志内容。  **[!NOTE]**  只支持Markdown语法。 |
| key | String | 是 | 字段1 | 写日志对应的模板某个字段的标题，可调用[获取模板详情](0296-query-template-details.md)接口获取field\_name参数值。 |
| template\_id | String | 是 | 12345abcde | 模板ID，可调用[获取模板详情](0296-query-template-details.md)接口获取id参数值。 |
| dd\_from | String | 是 | report | 日志来源，每个组织可以自己起一个唯一的来源标识。 |
| userid | String | 是 | 12345 | 创建日志的员工的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/savecontent?access_token=YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "create_report_param": {
      "contents": [
        {
          "sort": 0,
          "type": 1,
          "content_type": "markdown",
          "content": "这里是今天已经完成的工作。",
          "key": "今日完成工作"
        },
        {
          "sort": 1,
          "type": 1,
          "content_type": "markdown",
          "content": "这是待处理的任务。",
          "key": "未完成工作"
        }
      ],
      "template_id": "1734bff776fcc65ce6944f749e08500e",
      "to_userids": ["user123", "user456"],
      "to_chat": true,
      "to_cids": ["cid123"],
      "dd_from": "report",
      "userid": "user456"
    }
  }'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/savecontent");
OapiReportSavecontentRequest req = new OapiReportSavecontentRequest();
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
obj1.setTemplateId("12345abcde");
obj1.setDdFrom("report");
obj1.setUserid("12345");
req.setCreateReportParam(obj1);
OapiReportSavecontentResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportSavecontentRequest("https://oapi.dingtalk.com/topapi/report/savecontent")

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
$req = new OapiReportSavecontentRequest;
$create_report_param = new OapiCreateReportParam;
$contents = new OapiReportContentVo;
$contents->sort="0";
$contents->type="1";
$contents->content_type="markdown";
$contents->content="### 序号1";
$contents->key="字段1";
$create_report_param->contents = array($contents);
$create_report_param->template_id="12345abcde";
$create_report_param->dd_from="report";
$create_report_param->userid="12345";
$req->setCreateReportParam($create_report_param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/savecontent");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/savecontent");
OapiReportSavecontentRequest req = new OapiReportSavecontentRequest();
OapiReportSavecontentRequest.OapiCreateReportParamDomain obj1 = new OapiReportSavecontentRequest.OapiCreateReportParamDomain();
List<OapiReportSavecontentRequest.OapiReportContentVoDomain> list3 = new List<OapiReportSavecontentRequest.OapiReportContentVoDomain>();
OapiReportSavecontentRequest.OapiReportContentVoDomain obj4 = new OapiReportSavecontentRequest.OapiReportContentVoDomain();
list3.Add(obj4);
obj4.Sort = 0L;
obj4.Type = 1L;
obj4.ContentType = "markdown";
obj4.Content = "### 序号1";
obj4.Key = "字段1";
obj1.Contents= list3;
obj1.TemplateId = "12345abcde";
obj1.DdFrom = "report";
obj1.Userid = "12345";
req.CreateReportParam_ = obj1;
OapiReportSavecontentResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | 12345 | 调用结果。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": "175da298c2d6eb61373bb314725ae15d",
  "request_id": "14g3ttfdbjfpv"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
