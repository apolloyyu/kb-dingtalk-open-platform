---
title: "更新部门"
source_url: "https://open.dingtalk.com/document/development/address-book-update-department"
namespace: "development"
slug: "address-book-update-department"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 部门管理 > 更新部门"
doc_id: "X1yBTxFqGW"
updated_at: "2026-06-08 09:23:10"
---

> Source: https://open.dingtalk.com/document/development/address-book-update-department
> Path: 应用开发 / 服务端API / 通讯录管理 > 部门管理 > 更新部门
> Updated: 2026-06-08 09:23:10

# 更新部门

调用本接口，更新部门信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/v2/department/update |
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
| dept\_id | Number | 是 | 100 | 部门ID，可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |
| parent\_id | Number | 否 | 2 | 父部门ID，根部ID为1。可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取parent\_id参数值。 |
| hide\_dept | Boolean | 否 | true | 是否隐藏本部门：   - **true**：隐藏部门  隐藏后本部门将不会显示在公司通讯录中。 - **false**：显示部门   不传值，则保持不变。 |
| dept\_permits | String | 否 | 123,456 | 指定可以查看本部门的其他部门列表。  当**hide\_dept**为**true**时，则此值生效。  **[!NOTE]**  该参数列表总数和user\_permits列表总数之和不能超过50。 |
| user\_permits | String | 否 | user123,manager222 | 指定可以查看本部门的用户userid列表。  当**hide\_dept**为**true**时，则此值生效。  **[!NOTE]**  该参数列表总数和dept\_permits列表总数之和不能超过50。 |
| create\_dept\_group | Boolean | 否 | true | 是否创建一个关联此部门的企业群，默认为false即不创建。  不传值，则保持不变。 |
| order | Number | 否 | 10 | 在父部门中的排序值，order值小的排序靠前。 |
| name | String | 否 | HR | 部门名称，长度限制为1~64个字符，不允许包含字符‘-’‘，’以及‘,’。 |
| source\_identifier | String | 否 | HR部门 | 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。  **[!NOTE]**  该字段在企业管理后台部门信息中不可见。 |
| outer\_dept | Boolean | 否 | true | 是否限制本部门成员查看通讯录：   - **true**：开启限制。开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制   不传值，则保持不变。 |
| outer\_permit\_users | String | 否 | user123,manager123 | 指定本部门成员可查看的通讯录用户userid列表。  当**outer\_dept**为**true**时，此参数生效。  **[!NOTE]**  该参数列表总数和outer\_permit\_depts列表总数之和不能超过50。 |
| outer\_permit\_depts | String | 否 | 123,456 | 指定本部门成员可查看的通讯录部门ID列表。  当**outer\_dept**为**true**时，此参数生效。  **[!NOTE]**  该参数列表总数和outer\_permit\_users列表总数之和不能超过50。 |
| outer\_dept\_only\_self | Boolean | 否 | true | 本部门成员是否只能看到所在部门及下级部门通讯录：   - **true**：只能看到所在部门及下级部门通讯录 - **false**：不能查看所有通讯录，在通讯录中仅能看到自己   当**outer\_dept**为**true**时，此参数生效。  不传值，则保持不变。 |
| language | String | 否 | zh\_CN | 通讯录语言：   - **zh\_CN**：中文 - **en\_US**：英文 |
| auto\_add\_user | Boolean | 否 | false | 当部门群已经创建后，有新人加入部门时是否会自动加入该群：   - **true**：自动加入群 - **false**：不会自动加入群   不传值，则保持不变。 |
| auto\_approve\_apply | Boolean | 否 | false | 是否默认同意加入该部门的申请：   - **true：**表示加入该部门的申请将默认同意 - **false：**表示加入该部门的申请需要有权限的管理员同意 |
| dept\_manager\_userid\_list | String | 否 | manager220 | 部门的主管userId列表，多个userid之间使用英文逗号分隔。  **[!NOTE]**  部门主管必须在当前部门内，否则接口会报错**不存在的userId**。 |
| group\_contain\_sub\_dept | Boolean | 否 | true | 部门群是否包含子部门：   - **true**：包含 - **false**：不包含   不传值，则保持不变。 |
| group\_contain\_outer\_dept | Boolean | 否 | true | 部门群是否包含外包部门：   - **true**：包含 - **false**：不包含   不传值，则保持不变。  **[!NOTE]**  外包部门是仅可见自己的部门，不能看到其他部门和其他人。 |
| group\_contain\_hidden\_dept | Boolean | 否 | true | 部门群是否包含隐藏部门：   - **true**：包含 - **false**：不包含   不传值，则保持不变。 |
| org\_dept\_owner | String | 否 | 100 | 企业群群主的userId。  **[!NOTE]**  群主必须在当前部门内 |
| force\_update\_fields | String | 否 | dept\_manager\_userid\_list | 强制更新的字段，支持清空指定的字段，多个字段之间使用英文逗号分隔。目前支持字段: `dept_manager_userid_list`。 |
| code | String | 否 | 10000 | 部门编码，最多30个字符。  **[!NOTE]**  该字段只能通过本接口进行设置。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/v2/department/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=c6391xxxxb574' \
-d 'dept_id=100' \
-d 'parent_id=2' \
-d 'hide_dept=true' \
-d 'user_permits=100%2C200'
-d 'dept_permits=3%2C4%2C5' \
-d 'language=zh_CN' \
-d 'code=10000'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/update");
OapiV2DepartmentUpdateRequest req = new OapiV2DepartmentUpdateRequest();
req.setDeptId(100L);
req.setParentId(2L);
req.setOuterDept(true);
req.setHideDept(true);
req.setCreateDeptGroup(true);
req.setOrder(10L);
req.setName("HR");
req.setSourceIdentifier("HR部门");
req.setDeptPermits("123,456");
req.setUserPermits("user123,manager222");
req.setOuterPermitUsers("user100,user200");
req.setOuterPermitDepts("123,456");
req.setOuterDeptOnlySelf(true);
req.setLanguage("zh_CN");
req.setAutoAddUser(false);
req.setDeptManagerUseridList("manager200");
req.setGroupContainSubDept(true);
req.setGroupContainOuterDept(true);
req.setGroupContainHiddenDept(true);
req.setOrgDeptOwner("100");
OapiV2DepartmentUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiV2DepartmentUpdateRequest("https://oapi.dingtalk.com/topapi/v2/department/update")

req.dept_id=100
req.parent_id=2
req.hide_dept=true
req.user_permits="100,200"
req.dept_permits="3,4,5"
req.language="zh_CN"
req.code="10000"
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
$req = new OapiV2DepartmentUpdateRequest;
$req->setDeptId("100");
$req->setParentId("2");
$req->setHideDept("true");
$req->setDeptPermits("3,4,5");
$req->setUserPermits("100,200");
$req->setLanguage("zh_CN");
$req->setCode("10000");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/department/update");
OapiV2DepartmentUpdateRequest req = new OapiV2DepartmentUpdateRequest();
req.DeptId = 100L;
req.ParentId = 2L;
req.HideDept = true;
req.DeptPermits = "3,4,5";
req.UserPermits = "100,200";
req.Language = "zh_CN";
req.Code = "10000";
OapiV2DepartmentUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6iq4zcul5zjp | 请求ID。 |

### **响应体示例**

```
{
 "errcode":0,
 "errmsg":"ok",
 "request_id": "6iq4zcul5zjp"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 43007 | 权限不足 | 请确认access\_token是否有操作权限 |
| 40009 | 无效的部门id | 请确认dept\_id是否正确 |
| 60018 | 根部门不能被更新 | 请更换dept\_id |
| 60003 | 未找到该部门 | 请确认dept\_id是否正确 |
| 60001 | 无效的部门名称 | 请确认部门名称是否正确 |
| 40011 | 无效的顺序 | 请确认order是否合法 |
| 60004 | 父部门不存在 | 请确认parent\_id是否正确 |
| 60010 | 部门id存在循环 | 请重新设置部门id |
| 60109 | 非法的可查看id列表 | 请校验可查看列表是否合法 |
| 40031 | 无效的userId列表 | 请确认userId是否正确 |
| 40093 | 无效的企业群群主 | 请确认企业群群主的userid是否正确 |
| 60510 | 设置部门权限失败 | 请检验参数是否合法 |
| -1 | 系统繁忙 | 请稍后再试 |
