---
title: "获取用户可见的日志模板"
source_url: "https://open.dingtalk.com/document/development/obtains-the-list-of-visible-log-templates-based-on-the"
namespace: "development"
slug: "obtains-the-list-of-visible-log-templates-based-on-the"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "日志 > 获取用户可见的日志模板"
doc_id: "pIc7uznyap"
updated_at: "2026-05-27 13:10:23"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-list-of-visible-log-templates-based-on-the
> Path: 应用开发 / 服务端 API / 日志 > 获取用户可见的日志模板
> Updated: 2026-05-27 13:10:23

# 获取用户可见的日志模板

调用本接口，根据用户userId获取用户可见的日志模板，包括模板名称、模板图标URL等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/report/template/listbyuserid |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_report\_statistics-钉钉日志统计数据读权限permission-qyapi\_report\_query-企业员工日志读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 否 | manager7078 | 员工的userId。  **[!NOTE]**  不传递表示获取所有日志模板。 |
| offset | Number | 否 | 0 | 分页游标，从0开始。根据返回结果里的next\_cursor是否为空来判断是否还有下一页，且再次调用时offset设置成next\_cursor的值。 |
| size | Number | 否 | 100 | 分页大小，最大可设置成100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/report/template/listbyuserid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8389xxxx83c34a' \
-d 'offset=0' \
-d 'size=100' \
-d 'userid=manager7078'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/template/listbyuserid");
OapiReportTemplateListbyuseridRequest req = new OapiReportTemplateListbyuseridRequest();
req.setUserid("manager7078");
req.setOffset(0L);
req.setSize(100L);
OapiReportTemplateListbyuseridResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiReportTemplateListbyuseridRequest("https://oapi.dingtalk.com/topapi/report/template/listbyuserid")

req.userid="manager7078"
req.offset=0
req.size=100
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
$req = new OapiReportTemplateListbyuseridRequest;
$req->setUserid("manager7078");
$req->setOffset("0");
$req->setSize("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/report/template/listbyuserid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/report/template/listbyuserid");
OapiReportTemplateListbyuseridRequest req = new OapiReportTemplateListbyuseridRequest();
req.Userid = "manager7078";
req.Offset = 0L;
req.Size = 100L;
OapiReportTemplateListbyuseridResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | kszb71rpxu7u | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 错误信息 |
| result | HomePageReportTemplateVo |  | 返回结果。 |
| template\_list | ReportTemplateTopVo[] |  | 模板列表。 |
| name | String | 日报 | 日志模板名称。 |
| icon\_url | String | https://landray.dingtalkapps.com/alid/app/report/images/ico-png/0.png | 模板图标URL。 |
| report\_code | String | 14e882e7fd7e774e40ce9d144ddaa84d | 模板Code。 |
| url | String | https://landray.dingtalkapps.com/alid/app/report/createReport\_new.html?skip=0&corpid=${corpid}&id=${report\_code} | 模板URL。 |
| next\_cursor | Number | 100 | 下一次分页调用的offset值，当返回结果里没nextCursor时，表示分页结束。 |

### **响应体示例**

```
{
    "errcode": 0,
    "errmsg":"ok",
    "result": {
        "template_list": [
            {
                "icon_url": "https://landray.dingtalkapps.com/alid/app/report/images/ico-png/16.png",
                "name": "拜访记录",
                "report_code": "1734bff7730ae106bb7621645e78a92b",
                "url": "https://landray.dingtalkapps.com/alid/app/report/createReport_new.html?skip=0&corpid=dinge8a56572f80b02a8ffe93478753d9884&id=1734bff7730ae106bb7621645e78a92b"
            },
            {
                "icon_url": "https://landray.dingtalkapps.com/alid/app/report/images/ico-png/25.png",
                "name": "业绩日报",
                "report_code": "1734bff7743cba0744180ff4c5f9f0d9",
                "url": "https://landray.dingtalkapps.com/alid/app/report/createReport_new.html?skip=0&corpid=dinge8a56572f80b02a8ffe93478753d9884&id=1734bff7743cba0744180ff4c5f9f0d9"
            },
            {
                "icon_url": "https://landray.dingtalkapps.com/alid/app/report/images/ico-png/21.png",
                "name": "月报",
                "report_code": "1734bff775442f054b10629476caef48",
                "url": "https://landray.dingtalkapps.com/alid/app/report/createReport_new.html?skip=0&corpid=dinge8a56572f80b02a8ffe93478753d9884&id=1734bff775442f054b10629476caef48"
            },
            {
                "icon_url": "https://landray.dingtalkapps.com/alid/app/report/images/ico-png/22.png",
                "name": "周报",
                "report_code": "1734bff7761372057f96c7047f6b58c2",
                "url": "https://landray.dingtalkapps.com/alid/app/report/createReport_new.html?skip=0&corpid=dinge8a56572f80b02a8ffe93478753d9884&id=1734bff7761372057f96c7047f6b58c2"
            },
            {
                "icon_url": "https://landray.dingtalkapps.com/alid/app/report/images/ico-png/20.png",
                "name": "日报",
                "report_code": "1734bff776fcc65ce6944f749e08500e",
                "url": "https://landray.dingtalkapps.com/alid/app/report/createReport_new.html?skip=0&corpid=dinge8a56572f80b02a8ffe93478753d9884&id=1734bff776fcc65ce6944f749e08500e"
            },
            {
                "icon_url": "https://landray.dingtalkapps.com/alid/app/report/images/ico-png/0.png",
                "name": "空白日志",
                "report_code": "1746962ed1196d7ac8bc7044ce79b86a",
                "url": "https://landray.dingtalkapps.com/alid/app/report/createReport_new.html?skip=0&corpid=dinge8a56572f80b02a8ffe93478753d9884&id=1746962ed1196d7ac8bc7044ce79b86a"
            }
        ]
    },
    "request_id": "kszb71rpxu7u"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
