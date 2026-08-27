---
title: "查询家庭孩子信息"
source_url: "https://open.dingtalk.com/document/development/query-family-child-information"
namespace: "development"
slug: "query-family-child-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家庭 > 查询家庭孩子信息"
doc_id: "LkBhtT587G"
updated_at: "2026-06-08 09:47:57"
---

> Source: https://open.dingtalk.com/document/development/query-family-child-information
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家庭 > 查询家庭孩子信息
> Updated: 2026-06-08 09:47:57

# 查询家庭孩子信息

调用本接口，根据孩子的userId查询家庭孩子信息，包括孩子的昵称、学校的corpId、班级ID等信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/family/child/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-edu\_family\_group\_read-钉钉教育家庭组织读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| child\_userid | String | 是 | user01 | 孩子的userId。 |
| op\_userid | String | 是 | 2384082340 | 操作人的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/family/child/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d2aacb36-ac9c-48a7-985c-45cf96e2b430' \
-d 'child_userid=1123' \
-d 'op_userid=1234L'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/family/child/get");
OapiEduFamilyChildGetRequest req = new OapiEduFamilyChildGetRequest();
req.setChildUserid("user01");
req.setOpUserid("2384082340");
OapiEduFamilyChildGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduFamilyChildGetRequest("https://oapi.dingtalk.com/topapi/edu/family/child/get")

req.child_userid="1123"
req.op_userid="1234L"
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
$req = new OapiEduFamilyChildGetRequest;
$req->setChildUserid("1123");
$req->setOpUserid("1234L");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/family/child/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/family/child/get");
OapiEduFamilyChildGetRequest req = new OapiEduFamilyChildGetRequest();
req.ChildUserid = "1123";
req.OpUserid = "1234L";
OapiEduFamilyChildGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ChildDto |  | 查询结果。 |
| userid | String | user03 | 孩子在家庭组织里面的userId。 |
| nick | String | 班长 | 孩子的昵称。 |
| bind\_students | BindStudent[] |  | 孩子信息。 |
| corp\_id | String | ding9f50b1xxxx | 学校的corpId。 |
| class\_id | String | 677995086 | 班级ID。 |
| period\_code | String | primary\_school | 学段编码。 |
| userid | String | user02 | 孩子在学校的userId。 |
| avatar | String | RSDFS | 头像图片id。 |
| open\_id | String | gliiW0piiii02zBUjUxxxx | 孩子对应的openId。  **[!NOTE]**  该字段已废弃。 |
| unionId | String | gliiW0piiii02zBUjUxxxx | 孩子对应的唯一标识。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6bzhf2vn89pv | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "userid": "user03",
    "nick": "班长",
    "bind_students": [
      {
        "corp_id": "ding9f50b1xxxx",
        "class_id": "677995086 ",
        "period_code": "primary_school",
        "userid": "user02",
        "avatar": "RSDFS",
        "unionId": "gliiW0piiii02zBUjUxxxx"
      }
    ]
  },
  "success": true,
  "request_id": "6bzhf2vn89pv"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
