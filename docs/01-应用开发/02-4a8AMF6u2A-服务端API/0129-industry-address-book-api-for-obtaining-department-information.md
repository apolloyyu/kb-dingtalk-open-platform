---
title: "获取部门详情"
source_url: "https://open.dingtalk.com/document/development/industry-address-book-api-for-obtaining-department-information"
namespace: "development"
slug: "industry-address-book-api-for-obtaining-department-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 行业通讯录 > 获取部门详情"
doc_id: "2SU3stHNc8"
updated_at: "2026-05-27 13:09:37"
---

> Source: https://open.dingtalk.com/document/development/industry-address-book-api-for-obtaining-department-information
> Path: 应用开发 / 服务端API / 通讯录管理 > 行业通讯录 > 获取部门详情
> Updated: 2026-05-27 13:09:37

# 获取部门详情

调用本接口，根据部门ID获取行业通讯录下部门详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/industry/department/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_industry\_info\_read-行业通讯录信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 1 | 部门ID，可调用[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/industry/department/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=81462exxxx365499' \
-d 'dept_id=123444'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/department/get");
OapiIndustryDepartmentGetRequest req = new OapiIndustryDepartmentGetRequest();
req.setDeptId(1L);
OapiIndustryDepartmentGetResponse rsp = client.execute(req,access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiIndustryDepartmentGetRequest("https://oapi.dingtalk.com/topapi/industry/department/get")

req.dept_id=123444
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
$req = new OapiIndustryDepartmentGetRequest;
$req->setDeptId("123444");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/industry/department/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/department/get");
OapiIndustryDepartmentGetRequest req = new OapiIndustryDepartmentGetRequest();
req.DeptId = 123444L;
OapiIndustryDepartmentGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenIndustryDeptInfo |  | 部门信息。 |
| feature | String | {\"manager\_user\_id\":\"hhhj\",\"home\_tel\":\"1333608\*\*\*\*\",\"destitute\":\"是\"} | 部门的其他业务属性。可JSON反序列化。例如：   - 针对家校    - **period\_type**：学段类型（幼儿园，小学等）   - **name\_mode**：学段对应的名称类型（一年级，一年级1班等）   - **grade\_level**：年纪级数（一年级值为1）   - **start\_year**：入学年份   - **class\_level**：年级下班级级数 - 针对农村    - **manager\_user\_id**：组长userID   - **home\_tel**：家庭电话   - **destitute**：是否贫困户 |
| contact\_type | String | Origin | 通讯录类型行业相关。例如：   - 针对学校    - **classic**：传统经典校区、学段、年级、班级4层结构。   - **custom**：自定义结构 - 针对农村    - **Origin**：传统农村类型   - **Community**：社区类型   - **custom**：自定义结构 |
| dept\_type | String | Residence | 部门类型。行业相关。例如：   - 针对学校    - **campus**：校区   - **period**：学段   - **grade**：年级   - **class**：班级 - 针对农村    - **VillageGroup**：组   - **Residence**：户   - **LeaseholderDept**：租客   - **SecretaryDept**：村委 |
| super\_id | Number | 50 | 父部门ID。 |
| name | String | HR | 部门名称。 |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 7afehfo9w76t | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "feature": "{\"manager_user_id\":\"hhhj\",\"home_tel\":\"133360*****\",\"destitute\":\"是\"}",
    "contact_type": "Origin",
    "dept_type": "Residence",
    "super_id": 4240018,
    "name": "21户"
  },
  "request_id": "7afehfo9w76t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40009 | 无效的部门id | 请检查dept\_id是否正确 |
| 60003 | 未找到此部门 | 请确认部门在对应的企业中 |
| 400001 | 系统错误 | 请稍后重试 |
