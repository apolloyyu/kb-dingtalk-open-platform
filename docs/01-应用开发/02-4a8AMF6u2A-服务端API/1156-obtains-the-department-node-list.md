---
title: "获取部门列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-department-node-list"
namespace: "development"
slug: "obtains-the-department-node-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取部门列表"
doc_id: "cTgeghLflS"
updated_at: "2026-06-08 09:48:03"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-department-node-list
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取部门列表
> Updated: 2026-06-08 09:48:03

# 获取部门列表

调用本接口，查看某个部门下的所有子部门列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/dept/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_addresslist\_edu\_read-【敏感】钉钉教育家校通讯录读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| page\_size | Number | 是 | 30 | 每页大小，最大30。 |
| page\_no | Number | 是 | 1 | 页码，从1开始。 |
| super\_id | Number | 否 | 4240017 | 父部门节点ID，如果不填，则默认获取第一层级的部门节点。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/dept/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=39107120-97d2-483c-8051-1cd2df99b228' \
-d 'page_no=1' \
-d 'page_size=30' \
-d 'super_id=1234'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/dept/list");
OapiEduDeptListRequest req = new OapiEduDeptListRequest();
req.setPageSize(30L);
req.setPageNo(1L);
req.setSuperId(4240017L);
OapiEduDeptListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduDeptListRequest("https://oapi.dingtalk.com/topapi/edu/dept/list")

req.page_size=30
req.page_no=1
req.super_id=1234
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
$req = new OapiEduDeptListRequest;
$req->setPageSize("30");
$req->setPageNo("1");
$req->setSuperId("1234");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/dept/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/dept/list");
OapiEduDeptListRequest req = new OapiEduDeptListRequest();
req.PageSize = 30L;
req.PageNo = 1L;
req.SuperId = 1234L;
OapiEduDeptListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenEduDeptListResponse |  | 返回结果。 |
| details | OpenEduDeptDetails[] |  | 部门节点列表。 |
| nick | String | 希望小学 | 节点别名。 |
| chain | String | [4240016, 4240017] | 节点链。从顶层节点到当前节点的中间节点，其内容不包含当前节点。 |
| feature | String | {\"class\_level\":\"0\",\"grade\_level\":\"0\"} | 节点的其他业务属性。可JSON反序列化。 |
| name | String | 自定义下的班级 | 节点名称。 |
| contact\_type | String | classic | 通讯录类型。   - **classic**：传统经典4层结构。校区/学段/年级/班级 - **custom**：自定义结构 |
| dept\_type | String | class | 节点类型。   - **campus**：校区 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：普通节点，没有业务含义，主用存在于自定义通讯录中 |
| dept\_id | Number | 4240018 | 节点ID。 |
| has\_more | Boolean | false | 是否有更多数据。   - **true**：有 - **false**：没有 |
| super\_id | Number | 4240017 | 父部门ID。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码说明。 |
| request\_id | String | u7bcdo0f1o0r | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "details": [
      {
        "chain": "[4240016, 4240017]",
        "contact_type": "classic",
        "dept_id": 132691544,
        "dept_type": "grade",
        "feature":"{\"grade_level\":3,\"start_year\":\"2018\"}",
        "name": "未来PARK小学",
        "nick": ""
      },
      {
        "chain": "[4240016, 4240017]",
        "contact_type": "classic",
        "dept_id": 401272125,
        "dept_type": "grade",
        "feature":"{\"grade_level\":2,\"start_year\":\"2019\"}",
        "name": "希望小学",
        "nick": ""
      },
    ],
    "has_more": false,
    "super_id":4240017
  },
  "success": true,
  "request_id": "u7bcdo0f1o0r"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
