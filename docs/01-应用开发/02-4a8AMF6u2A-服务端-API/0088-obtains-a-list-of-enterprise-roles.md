---
title: "获取角色列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-enterprise-roles"
namespace: "development"
slug: "obtains-a-list-of-enterprise-roles"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 获取角色列表"
doc_id: "rtTxtM7fQC"
updated_at: "2026-05-27 13:09:27"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-enterprise-roles
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 获取角色列表
> Updated: 2026-05-27 13:09:27

# 获取角色列表

调用本接口，获取角色列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_list-通讯录部门信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6ed1bxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| size | Number | 否 | 20 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小**，**默认值20**，**最大值200。 |
| offset | Number | 否 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a0a639xxxx2998' \
-d 'offset=0' \
-d 'size=20'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/list");
OapiRoleListRequest req = new OapiRoleListRequest();
req.setSize(20L);
req.setOffset(0L);
OapiRoleListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleListRequest("https://oapi.dingtalk.com/topapi/role/list")

req.size=20
req.offset=0
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
$req = new OapiRoleListRequest;
$req->setSize("20");
$req->setOffset("0");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/list");
OapiRoleListRequest req = new OapiRoleListRequest();
req.Size = 20L;
req.Offset = 0L;
OapiRoleListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | ii8a42qgzu7e | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageVo |  | 结果列表。 |
| hasMore | Boolean | false | 是否还有更多数据。 |
| list | OpenRoleGroup[] |  | 角色组列表。 |
| name | String | 默认 | 角色组名称。 |
| groupId | Number | 1507113577 | 角色组ID。 |
| roles | OpenRole[] |  | 角色列表。 |
| name | String | 管理员 | 角色名称。 |
| id | Number | 1507113578 | 角色ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "hasMore": true,
    "list": [
      {
        "groupId": 1507113577,
        "name": "默认",
        "roles": [
          {
            "id": 1507113580,
            "name": "负责人"
          },
          {
            "id": 1507113581,
            "name": "主管"
          },
          {
            "id": 1507113578,
            "name": "主管理员"
          },
          {
            "id": 1507113579,
            "name": "子管理员"
          }
        ]
      }
    ]
  },
  "request_id": "ii8a42qgzu7e"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400043 | 非法的orgId | 请检查access\_token是否正确 |
| 40069 | 非法的size | 请调整分页的大小 |
| 40068 | 无效的偏移量 | 请调整偏移量的大小 |
| 400001 | 系统错误 | 请稍后再试 |
