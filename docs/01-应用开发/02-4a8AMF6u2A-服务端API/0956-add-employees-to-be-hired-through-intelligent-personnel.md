---
title: "添加企业待入职员工"
source_url: "https://open.dingtalk.com/document/development/add-employees-to-be-hired-through-intelligent-personnel"
namespace: "development"
slug: "add-employees-to-be-hired-through-intelligent-personnel"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工关系 > 添加企业待入职员工"
doc_id: "blLz1gQGVQ"
updated_at: "2026-06-01 09:15:24"
---

> Source: https://open.dingtalk.com/document/development/add-employees-to-be-hired-through-intelligent-personnel
> Path: 应用开发 / 服务端API / 智能人事 > 员工关系 > 添加企业待入职员工
> Updated: 2026-06-01 09:15:24

# 添加企业待入职员工

调用本接口，添加企业待入职员工。

## **接口调用说明**

- 本接口不同步员工详细档案信息。
- 本接口只能添加非本企业员工（手机号为准），否则会提示系统繁忙。
- 本接口添加的待入职员工的来源信息为开放平台。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_manager-智能人事数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| param | PreEntryEmployeeAddParam | 是 |  | 添加待入职人员。 |
| pre\_entry\_time | Date | 否 | 2020-09-09 00:00:00 | 预期入职时间。 |
| name | String | 是 | 张三 | 待入职员工姓名。 |
| extend\_info | String | 否 | "{\"depts\":\"1\",\"employeeType\":10003,\"mainDeptId\":379661095,\"mainDeptName\":\"市场部\",\"position\":\"市场经理\",\"workPlace\":\"杭州\"}" | 扩展信息，json串格式，按要求传入有效信息，无效信息不会保存。  有效信息有：   - **depts**：部门ID列表，多个部门用"|"分隔 - **mainDeptId**：主部门ID - **mainDeptName**：主部门名称 - **position**：职位 - **workPlace**：工作地点 - **jobNumber**：工号 - **employeeType**：员工类型枚举值：    - **0**：无类型   - **1**：全职   - **2**：兼职   - **3**：实习   - **4**：劳务派遣   - **5**：退休返聘   - **6**：劳务外包 |
| op\_userid | String | 否 | manager123 | 操作人userid。 |
| mobile | String | 是 | 1370000000 | 待入职员工手机号。  **[!NOTE]**  本接口只能添加非本企业员工（手机号为准），否则报错系统繁忙。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=72d385cxxxx0abe1' \
-d 'param=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry");
OapiSmartworkHrmEmployeeAddpreentryRequest req = new OapiSmartworkHrmEmployeeAddpreentryRequest();
PreEntryEmployeeAddParam obj1 = new PreEntryEmployeeAddParam();
obj1.setPreEntryTime(StringUtils.parseDateTime("2018-08-08 00:00:00"));
obj1.setName("张三");
obj1.setExtendInfo("{\"depts\":\"1\",\"employeeType\":10003,\"mainDeptId\":379661095,\"mainDeptName\":\"市场部\",\"position\":\"市场经理\",\"workPlace\":\"杭州\"}");
obj1.setOpUserid("manager123");
obj1.setMobile("13712345678");
req.setParam(obj1);
OapiSmartworkHrmEmployeeAddpreentryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartworkHrmEmployeeAddpreentryRequest("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry")

req.param=""
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
$req = new OapiSmartworkHrmEmployeeAddpreentryRequest;
$param = new PreEntryEmployeeAddParam;
$param->pre_entry_time="2018-08-08 00:00:00";
$param->name="张三";
$param->extend_info="{\"depts\": \"123|345|899\",   \"employeeType\": 1,   \"mainDeptId\": 123,   \"mainDeptName\": \"研发部\",   \"position\": \"高级工程师\",   \"workPlace\": \"杭州\" }";
$param->op_userid="manager123";
$param->mobile="13712345678";
$req->setParam($param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/addpreentry");
OapiSmartworkHrmEmployeeAddpreentryRequest req = new OapiSmartworkHrmEmployeeAddpreentryRequest();
OapiSmartworkHrmEmployeeAddpreentryRequest.PreEntryEmployeeAddParamDomain obj1 = new OapiSmartworkHrmEmployeeAddpreentryRequest.PreEntryEmployeeAddParamDomain();
obj1.PreEntryTime = DateTime.Parse(2018-08-08 00:00:00");
obj1.Name = "张三";
obj1.ExtendInfo = "{\"depts\": \"123|345|899\",   \"employeeType\": 1,   \"mainDeptId\": 123,   \"mainDeptName\": \"研发部\",   \"position\": \"高级工程师\",   \"workPlace\": \"杭州\" }";
obj1.OpUserid = "manager123";
obj1.Mobile = "13712345678";
req.Param_ = obj1;
OapiSmartworkHrmEmployeeAddpreentryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| userid | String | 15994884216176833 | 员工ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | false | 是否调用成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | pl29537rx3lo | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success": true,
  "userid": "15994884216176833",
  "request_id": "pl29537rx3lo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
