---
title: "获取用户可查看的公告"
source_url: "https://open.dingtalk.com/document/development/list-the-user-s-announcement-list"
namespace: "development"
slug: "list-the-user-s-announcement-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 获取用户可查看的公告"
doc_id: "b8xRUSq3t7"
updated_at: "2026-05-29 09:13:34"
---

> Source: https://open.dingtalk.com/document/development/list-the-user-s-announcement-list
> Path: 应用开发 / 服务端API / 公告 > 获取用户可查看的公告
> Updated: 2026-05-29 09:13:34

# 获取用户可查看的公告

调用本接口，可获取指定人员的公告信息，在企业自定义工作首页进行公告轮播展示。列出用户当前有权限看到的10条公告。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/blackboard/listtopten |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_read-读取钉钉公告微应用数据的权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | manager01 | 员工的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/blackboard/listtopten" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8fc881xxxxeee24d' \
-d 'userid=manager01'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/listtopten");
OapiBlackboardListtoptenRequest req = new OapiBlackboardListtoptenRequest();
req.setUserid("manager01");
OapiBlackboardListtoptenResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiBlackboardListtoptenRequest("https://oapi.dingtalk.com/topapi/blackboard/listtopten")

req.userid="manager01"
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
$req = new OapiBlackboardListtoptenRequest;
$req->setUserid("manager01");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/blackboard/listtopten");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/listtopten");
OapiBlackboardListtoptenRequest req = new OapiBlackboardListtoptenRequest();
req.Userid = "manager01";
OapiBlackboardListtoptenResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 3y4bln1b7e7q | 请求ID。 |
| blackboard\_list | OapiBlackboardVo[] |  | 返回结果。 |
| gmt\_create | Date | 2020-09-08 14:42:12 | 创建时间。 |
| title | String | 放假通知。 | 公告标题。 |
| url | String | https://app.dingtalk.com/xxxx | 跳转URL。 |
| categoryId | String | 576920db | 公告分类ID。 |
| id | Sting | a3071449 | 公告ID。 |

### **响应体示例**

```
{
  "blackboard_list": [
    {
      "gmt_create": "2020-09-08 14:42:12",
      "title": "国庆节值班表",
      "url": "https://app.dingtalk.com/xxxx?dd_nav_bgcolor=FF5E97F6&showmenu=true&dd_share=true&bid=72b4f87d27e815f6fef989025xxxx",
      "categoryId":"576920db",
      "id":"a3071449"
    }
  ],
  "errcode": 0,
  "request_id": "3y4bln1b7e7q"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
