---
title: "获取部门列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-industry-departments"
namespace: "development"
slug: "obtains-a-list-of-industry-departments"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 行业通讯录 > 获取部门列表"
doc_id: "rcKzSW9wpT"
updated_at: "2026-05-27 13:09:36"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-industry-departments
> Path: 应用开发 / 服务端 API / 通讯录管理 > 行业通讯录 > 获取部门列表
> Updated: 2026-05-27 13:09:36

# 获取部门列表

调用本接口根据部门ID获取行业通讯录部门列表，例如，教育行业组织内有家校通讯录，属于行业通讯录类型之一，调用本接口如果参数部门ID传1，代表获取的是家校通讯录下的一级部门列表，可以获取到XX二中和XX高中对应的部门ID。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/industry/department/list |
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
| dept\_id | Number | 是 | 1 | 父部门ID，行业根部门传1。 |
| cursor | Number | 否 | 1 | 分页查询的游标。 |
| size | Number | 是 | 10 | 分页查询的大小，最大值1000。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/industry/department/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=50edxxxxc8f0' \
-d 'cursor=1' \
-d 'dept_id=2345' \
-d 'size=30'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/department/list");
OapiIndustryDepartmentListRequest req = new OapiIndustryDepartmentListRequest();
req.setDeptId(1L);
req.setSize(10L);
req.setCursor(1L);
OapiIndustryDepartmentListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiIndustryDepartmentListRequest("https://oapi.dingtalk.com/topapi/industry/department/list")

req.dept_id=2345
req.cursor=1
req.size=30
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
$req = new OapiIndustryDepartmentListRequest;
$req->setDeptId("2345");
$req->setCursor("1");
$req->setSize("30");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/industry/department/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/industry/department/list");
OapiIndustryDepartmentListRequest req = new OapiIndustryDepartmentListRequest();
req.DeptId = 2345L;
req.Cursor = 1L;
req.Size = 30L;
OapiIndustryDepartmentListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ResultWrapper |  | 部门列表信息。 |
| details | OpenIndustryDeptInfo[] |  | 部门详情列表。 |
| feature | String | {\"manager\_user\_id\":\"hhhj\",\"home\_tel\":\"13336082716\",\"destitute\":\"是\"} | 部门的其他业务属性。可JSON反序列化。例如：   - 针对家校    - **period\_type**：学段类型（幼儿园，小学等）   - **name\_mode**：学段对应的名称类型（一年级，一年级1班等）   - **grade\_level**：年纪级数（一年级值为1）   - **start\_year**：入学年份   - **class\_level**：年级下班级级数 - 针对农村    - **manager\_user\_id**：组长userID   - **home\_tel**：家庭电话   - **destitute**：是否贫困户 |
| contact\_type | String | Origin | 通讯录类型 行业相关。例如：   - 针对学校    - **classic**：传统经典校区、学段、年级、班级4层结构。   - **custom**：自定义结构 - 针对农村    - **Origin**：传统农村类型   - **Community**：社区类型   - **custom**：自定义结构 |
| dept\_type | String | VillageGroup | 部门类型。行业相关。例如：   - 针对学校    - **campus**：校区   - **period**：学段   - **grade**：年级   - **class**：班级 - 针对农村    - **VillageGroup**：组   - **Residence**：户   - **LeaseholderDept**：租客   - **SecretaryDept**：村委 |
| name | String | 21组 | 部门名称 |
| dept\_id | Number | 4240018 | 部门ID |
| next\_cursor | Number | 1525 | 分页查询的游标。 |
| has\_more | Boolean | false | 是否还有更多数据。 |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 7afehfo9w76t | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "details": [
      {
        "dept_id": 4240018,
        "feature": "{\"manager_user_id\":\"hhhj\",\"home_tel\":\"13336082716\",\"destitute\":\"是\"}",
        "name": "21组",
        "contact_type": "Origin",
        "dept_type": "VillageGroup"
      },
      {
        "dept_id": 4240019,
        "feature": "{}",
        "name": "21户",
        "contact_type": "Origin",
        "dept_type": "Residence"
      }
    ],
    "has_more": false,
    "next_cursor": 1525
  },
  "errmsg": "ok",
  "errcode": 0,
  "request_id": "7afehfo9w76t"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 40069 | 无效的size | 请检查size是否合法 |
| 40009 | 无效的部门id | 请检查dept\_id是否合法 |
| 400001 | 系统错误 | 请稍后重试 |
