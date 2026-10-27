---
title: "创建部门"
source_url: "https://open.dingtalk.com/document/development/address-book-creation-department-established-department"
namespace: "development"
slug: "address-book-creation-department-established-department"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 部门管理 > 创建部门"
doc_id: "AQsj8RcyMr"
updated_at: "2026-05-27 13:09:10"
---

> Source: https://open.dingtalk.com/document/development/address-book-creation-department-established-department
> Path: 应用开发 / 服务端 API / 通讯录管理 > 部门管理 > 创建部门
> Updated: 2026-05-27 13:09:10

# 创建部门

调用本接口，创建新部门。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-通讯录数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | 开发部门 | 部门名称。  长度限制为1~64个字符，不允许包含字符"-"","以及","。 |
| parent\_id | Number | 是 | 10 | 父部门ID，根部门ID为1。 |
| hide\_dept | Boolean | 否 | true | 是否隐藏本部门：   - **true**：隐藏部门，隐藏后本部门将不会显示在公司通讯录中 - **false（默认值）**：显示部门 |
| dept\_permits | String | 否 | "123,456" | 指定可以查看本部门的其他部门列表，总数不能超过50。  当**hide\_dept**为**true**时，则此值生效。 |
| user\_permits | String | 否 | "user123,manager222" | 指定可以查看本部门的人员userId列表，总数不能超过50。  当**hide\_dept**为**true**时，则此值生效。 |
| outer\_dept | Boolean | 否 | true | 是否限制本部门成员查看通讯录：   - **true**：开启限制。开启后本部门成员只能看到限定范围内的通讯录 - **false（默认值）**：不限制 |
| outer\_dept\_only\_self | Boolean | 否 | false | 本部门成员是否只能看到所在部门及下级部门通讯录：   - **true**：只能看到所在部门及下级部门通讯录 - **false**：不能查看所有通讯录，在通讯录中仅能看到自己   当**outer\_dept**为**true**时，此参数生效。 |
| outer\_permit\_users | String | 否 | "manager123,user123" | 指定本部门成员可查看的通讯录用户userId列表，总数不能超过50。  当**outer\_dept**为**true**时，此参数生效。 |
| outer\_permit\_depts | String | 否 | "456,123" | 指定本部门成员可查看的通讯录部门ID列表，总数不能超过50。  当**outer\_dept**为**true**时，此参数生效。 |
| create\_dept\_group | Boolean | 否 | true | 是否创建一个关联此部门的企业群，默认为**false**即不创建。 |
| auto\_approve\_apply | Boolean | 否 | false | 是否默认同意加入该部门的申请：   - **true：**表示加入该部门的申请将默认同意 - **false：**表示加入该部门的申请需要有权限的管理员同意 |
| order | Number | 否 | 10 | 在父部门中的排序值，order值小的排序靠前。 |
| source\_identifier | String | 否 | HR部门 | 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d5ca5xxxxa8' \
-d 'parent_id=10' \
-d 'outer_dept=true' \
-d 'hide_dept=true' \
-d 'create_dept_group=true' \
-d 'order=10' \
-d 'name=HR' \
-d 'source_identifier=HR%E9%83%A8%E9%97%A8' \
-d 'dept_permits=3%2C4%2C5' \
-d 'user_permits=100%2C200' \
-d 'outer_permit_users=500%2C600' \
-d 'outer_permit_depts=6%2C7%2C8' \
-d 'outer_dept_only_self=true'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/create");
OapiV2DepartmentCreateRequest req = new OapiV2DepartmentCreateRequest();
req.setParentId(10L);
req.setOuterDept(true);
req.setHideDept(true);
req.setCreateDeptGroup(true);
req.setOrder(10L);
req.setName("HR");
req.setSourceIdentifier("HR部门");
req.setDeptPermits("3,4,5");
req.setUserPermits("100,200");
req.setOuterPermitUsers("500,600");
req.setOuterPermitDepts("6,7,8");
req.setOuterDeptOnlySelf(true);
OapiV2DepartmentCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
# -*- coding: utf-8 -*-
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentCreateRequest("https://oapi.dingtalk.com/topapi/v2/department/create")

req.parent_id=10
req.outer_dept=true
req.hide_dept=true
req.create_dept_group=true
req.order=10
req.name="HR"
req.source_identifier="HR部门"
req.dept_permits="3,4,5"
req.user_permits="100,200"
req.outer_permit_users="500,600"
req.outer_permit_depts="6,7,8"
req.outer_dept_only_self=true
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
$req = new OapiV2DepartmentCreateRequest;
$req->setName("HR");
$req->setParentId("10");
$req->setHideDept("true");
$req->setDeptPermits("3,4,5");
$req->setUserPermits("100,200");
$req->setOuterPermitUsers("500,600");
$req->setOuterPermitDepts("6,7,8");
$req->setOuterDeptOnlySelf("true");
$req->setOuterDept("true");
$req->setCreateDeptGroup("true");
$req->setOrder("10");
$req->setSourceIdentifier("HR部门");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/v2/department/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/create");
OapiV2DepartmentCreateRequest req = new OapiV2DepartmentCreateRequest();
req.ParentId = 10L;
req.OuterDept = true;
req.HideDept = true;
req.CreateDeptGroup = true;
req.Order = 10L;
req.Name = "HR";
req.SourceIdentifier = "HR部门";
req.DeptPermits = "3,4,5";
req.UserPermits = "100,200";
req.OuterPermitUsers = "500,600";
req.OuterPermitDepts = "6,7,8";
req.OuterDeptOnlySelf = true;
OapiV2DepartmentCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | 6iq4zcul5zjp | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | DeptCreateResponse |  | 调用结果。 |
| dept\_id | Number | 100 | 部门ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "dept_id": 41xxxx76
  },
  "request_id": "6iq4zcul5zjp"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40035 | 参数非法 | 请确认参数按照上述文档要求填写 |
| 43007 | 需要授权 | 请确认access\_token有权限进行此操作 |
| 60004 | 父部门不存在 | 请检查parent\_id是否正确 |
| 600109 | 不合法的可见id列表 | 请确认可见列表是否符合要求 |
| -1 | 系统繁忙 | 请稍后再试 |
