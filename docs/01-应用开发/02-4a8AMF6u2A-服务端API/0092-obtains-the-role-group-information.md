---
title: "获取角色组列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-role-group-information"
namespace: "development"
slug: "obtains-the-role-group-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 角色管理 > 获取角色组列表"
doc_id: "8sVOvfK98o"
updated_at: "2026-05-27 13:09:26"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-role-group-information
> Path: 应用开发 / 服务端API / 通讯录管理 > 角色管理 > 获取角色组列表
> Updated: 2026-05-27 13:09:26

# 获取角色组列表

调用本接口，获取角色组信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/role/getrolegroup |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_department\_list-通讯录部门信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| group\_id | Number | 是 | 1507113580 | 角色组的ID。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/role/getrolegroup" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ab02axxxx7d770' \
-d 'group_id=1'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/getrolegroup");
OapiRoleGetrolegroupRequest req = new OapiRoleGetrolegroupRequest();
req.setGroupId(1507113580L);
OapiRoleGetrolegroupResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiRoleGetrolegroupRequest("https://oapi.dingtalk.com/topapi/role/getrolegroup")

req.group_id=1
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
$req = new OapiRoleGetrolegroupRequest;
$req->setGroupId("1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/role/getrolegroup");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/role/getrolegroup");
OapiRoleGetrolegroupRequest req = new OapiRoleGetrolegroupRequest();
req.GroupId = 1L;
OapiRoleGetrolegroupResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| role\_group | OpenRoleGroup |  | 角色组信息。 |
| roles | OpenRole[] |  | 角色列表信息。 |
| role\_id | Number | 1507113580 | 角色ID。 |
| role\_name | String | 主管 | 角色名。 |
| group\_name | String | 默认 | 角色组名。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 8lgzequlri0o | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "role_group": {
    "group_name": "默认",
    "roles": [
      {
        "role_name": "负责人",
        "role_id": 1507113580
      },
      {
        "role_name": "主管",
        "role_id": 1507113581
      },
      {
        "role_name": "主管理员",
        "role_id": 1507113578
      },
      {
        "role_name": "子管理员",
        "role_id": 1507113579
      }
    ]
  },
  "request_id": "8lgzequlri0o"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 400002 | 无效的参数 | 请检验groupId是否合法 |
| -1 | 系统繁忙 | 请稍后再试 |
