---
title: "获取指定角色的员工列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-list-of-employees-of-a-role"
namespace: "development"
slug: "obtain-the-list-of-employees-of-a-role"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 角色管理 > 获取指定角色的员工列表"
doc_id: "BTSzqDJMWg"
updated_at: "2026-05-27 13:09:29"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-list-of-employees-of-a-role
> Path: 应用开发 / 服务端 API / 通讯录管理 > 角色管理 > 获取指定角色的员工列表
> Updated: 2026-05-27 13:09:29

# 获取指定角色的员工列表

调用本接口，获取指定角色的员工列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/simplelist |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_member-通讯录部门成员读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| role\_id | Number | 是 | 1203141 | 角色roleId，可通过调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取id参数值。 |
| size | Number | 否 | 20 | 分页大小。  **[!NOTE]**  与offset参数同时设置时才生效，此参数代表分页大小，默认值20，最大100。 |
| offset | Number | 否 | 0 | 分页偏移量。  **[!NOTE]**  与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/simplelist" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d1812xxxxc53245' \
-d 'offset=0' \
-d 'role_id=1203141' \
-d 'size=20'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/simplelist");
OapiRoleSimplelistRequest req = new OapiRoleSimplelistRequest();
req.setRoleId(1203141L);
req.setSize(20L);
req.setOffset(0L);
OapiRoleSimplelistResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleSimplelistRequest("https://oapi.dingtalk.com/topapi/role/simplelist")

req.role_id=1203141
req.offset=0
req.size=20
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
$req = new OapiRoleSimplelistRequest;
$req->setRoleId("1203141");
$req->setOffset("0");
$req->setSize("20");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/simplelist");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/simplelist");
OapiRoleSimplelistRequest req = new OapiRoleSimplelistRequest();
req.RoleId = 1203141L;
req.Offset = 0L;
req.Size = 20L;
OapiRoleSimplelistResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | f6249uw1kuus | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | PageVo |  | 查询结果。 |
| hasMore | Boolean | true | 是否还有更多数据。 |
| list | OpenEmpSimple[] |  | 角色下的员工列表。 |
| userid | String | manager4220 | 员工的userid。 |
| name | String | 小钉 | 员工姓名。 |
| manageScopes | OrgDeptVo[] |  | 管理范围。 |
| dept\_id | Number | 11 | 部门ID。 |
| name | String | 纪检部 | 部门名称。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "hasMore": false,
    "list": [
      {
        "name": "小钉",
        "userid": "manager4220",
        "manageScopes":[
          {
            "dept_id":11,
            "name":"纪检部"
          }
        ]
      }
    ]
  },
  "request_id": "f6249uw1kuus"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errorcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33011 | 无效的roleId | 请检查roleId是否正确 |
| 40069 | 无效的size | 请调整分页大小 |
| 40068 | 无效的偏移量 | 请调整偏移量 |
| 400001 | 系统错误 | 请稍后重试 |
