---
title: "获取学生监护人详情"
source_url: "https://open.dingtalk.com/document/development/obtain-the-relationship-between-home-and-school-personnel"
namespace: "development"
slug: "obtain-the-relationship-between-home-and-school-personnel"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取学生监护人详情"
doc_id: "xeUV98U2Tx"
updated_at: "2026-06-08 09:48:08"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-relationship-between-home-and-school-personnel
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取学生监护人详情
> Updated: 2026-06-08 09:48:08

# 获取学生监护人详情

调用本接口，查看班级下某个监护人的详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/user/relation/get |
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
| from\_userid | String | 是 | manager9707 | 监护人userId。 |
| class\_id | Number | 是 | 4240006 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/user/relation/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=76c22564-cc79-4152-b5e8-4952231d249b' \
-d 'class_id=4240006' \
-d 'from_userid=manager9707'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/relation/get");
OapiEduUserRelationGetRequest req = new OapiEduUserRelationGetRequest();
req.setFromUserid("manager9707");
req.setClassId(4240006L);
OapiEduUserRelationGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduUserRelationGetRequest("https://oapi.dingtalk.com/topapi/edu/user/relation/get")

req.from_userid="manager9707"
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
$req = new OapiEduUserRelationGetRequest;
$req->setFromUserid("manager9707");
$req->setClassId("4240006");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/user/relation/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/user/relation/get");
OapiEduUserRelationGetRequest req = new OapiEduUserRelationGetRequest();
req.FromUserid = "manager9707";
req.ClassId = 4240006L;
OapiEduUserRelationGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| relations | OpenEduUserRelationDetail[] |  | 关系详情列表。 |
| class\_id | Number | 4240006 | 班级ID。 |
| relation\_name | String | 爸爸 | 关系名。 |
| relation\_code | String | F | 关系code。   - **F**：爸爸 - **M**：妈妈 - **GF**：爷爷 - **GM**：奶奶 - **GFA**：外公 - **GMA**：外婆 - **U**：叔叔 - **A**：阿姨 - **B**：哥哥 - **S**：姐姐 - **O**：家长 |
| from\_userid | String | manager9707 | 监护人userId。 |
| to\_userid | String | 16039409358232571410 | 学生userId。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | 用户不存在 | 返回码描述。 |
| request\_id | String | sgx0d7yb2lal | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "relations": [
      {
        "class_id": 4240006,
        "from_userid": "15919287602721543266165",
        "relation_code": "F",
        "relation_name": "爸爸",
        "to_userid": "16039409358232571410"
      }
    ]
  },
  "success": true,
  "errcode": 0,
  "request_id":"sgx0d7yb2lal"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
