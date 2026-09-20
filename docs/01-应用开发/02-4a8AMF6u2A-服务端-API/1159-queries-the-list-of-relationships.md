---
title: "获取班级内学生的关系列表"
source_url: "https://open.dingtalk.com/document/development/queries-the-list-of-relationships"
namespace: "development"
slug: "queries-the-list-of-relationships"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取班级内学生的关系列表"
doc_id: "yVd6G2j5WY"
updated_at: "2026-06-08 09:48:07"
---

> Source: https://open.dingtalk.com/document/development/queries-the-list-of-relationships
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取班级内学生的关系列表
> Updated: 2026-06-08 09:48:07

# 获取班级内学生的关系列表

调用本接口，查看班级下的所有学生的关系列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/user/relation/list |
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
| page\_no | Number | 是 | 1 | 页码，从1开始。 |
| page\_size | Number | 是 | 30 | 每页大小，取值1~30。 |
| class\_id | Number | 是 | 4240006 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/user/relation/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7dad1a09-ffcb-4263-bdb1-d3b7dd55f749' \
-d 'class_id=4240006' \
-d 'page_no=1' \
-d 'page_size=30'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/relation/list");
OapiEduUserRelationListRequest req = new OapiEduUserRelationListRequest();
req.setPageNo(1L);
req.setPageSize(30L);
req.setClassId(4240006L);
OapiEduUserRelationListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduUserRelationListRequest("https://oapi.dingtalk.com/topapi/edu/user/relation/list")

req.page_no=1
req.page_size=30
req.class_id=4240006
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
$req = new OapiEduUserRelationListRequest;
$req->setPageNo("1");
$req->setPageSize("30");
$req->setClassId("4240006");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/user/relation/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/relation/list");
OapiEduUserRelationListRequest req = new OapiEduUserRelationListRequest();
req.PageNo = 1L;
req.PageSize = 30L;
req.ClassId = 4240006L;
OapiEduUserRelationListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| has\_more | Boolean | false | 是否还存在数据。   - **true**：有 - **false**：没有 |
| relations | OpenEduUserRelationDetail[] |  | 关系列表。 |
| class\_id | Number | 4240006 | 班级ID。 |
| relation\_name | String | 爸爸 | 关系名。 |
| relation\_code | String | F | 关系code。   - **F**：爸爸 - **M**：妈妈 - **GF**：爷爷 - **GM**：奶奶 - **GFA**：外公 - **GMA**：外婆 - **U**：叔叔 - **A**：阿姨 - **B**：哥哥 - **S**：姐姐 - **O**：家长 |
| from\_userid | String | manager9707 | 监护人userId。 |
| to\_userid | String | 10203029011219896 | 学生userId。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 用户不存在 | 返回码描述。 |
| request\_id | String | 4ue6aposozud | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "has_more": false,
    "relations": [
      {
        "class_id": 4240006,
        "from_userid": "16039409358101367795256",
        "relation_code": "M",
        "relation_name": "妈妈",
        "to_userid": "16039409358232571410"
      },
      {
        "class_id": 4240006,
        "from_userid": "manager9707",
        "relation_code": "F",
        "relation_name": "爸爸",
        "to_userid": "10203029011219896"
      }
    ]
  },
  "success": true,
  "errcode": 0,
  "request_id":"4ue6aposozud"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
