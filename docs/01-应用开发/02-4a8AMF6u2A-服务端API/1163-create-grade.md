---
title: "创建年级"
source_url: "https://open.dingtalk.com/document/development/create-grade"
namespace: "development"
slug: "create-grade"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建年级"
doc_id: "IX4TkTcjLZ"
updated_at: "2026-06-08 09:48:12"
---

> Source: https://open.dingtalk.com/document/development/create-grade
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建年级
> Updated: 2026-06-08 09:48:12

# 创建年级

调用本接口，创建年级。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/grade/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-钉钉教育家校通讯录写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| open\_grade | OpenGrade | 是 |  | 年级信息。 |
| grade | String | 是 | 2 | 年级级数，一年级为1，二年级为2。 |
| classes | Number | 是 | 1 | 每个年级下班级级数，1班为1，2班为2。0表示无限。  **[!NOTE]**  尽量不要超过100个，否则页面性能有问题。 |
| name | String | 是 | 二年级2019级 | 年级名称，需要与grade和start\_year对应。 |
| start\_year | String | 是 | 2019 | 入学年份。  **[!NOTE]**  请注意start\_year、name、grade三者之间的关联关系。 |
| super\_id | Number | 是 | 4240018 | 学段ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为period时的dept\_id参数值。 |
| operator | String | 是 | user01 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/grade/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3935b93c-4f70-4911-a769-012e1c76b8ff' \
-d 'open_grade=null' \
-d 'operator=12344' \
-d 'super_id=2333'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/grade/create");
OapiEduGradeCreateRequest req = new OapiEduGradeCreateRequest();
OpenGrade openGrade = new OpenGrade();
openGrade.setName("二年级2019级");
openGrade.setClasses(1L);
openGrade.setGrade("2");
openGrade.setStartYear("2019");
req.setSuperId(4240018L);
req.setOperator("user01");
req.setOpenGrade(openGrade);
OapiEduGradeCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduGradeCreateRequest("https://oapi.dingtalk.com/topapi/edu/grade/create")

req.open_grade=""
req.super_id=2333
req.operator="12344"
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
$req = new OapiEduGradeCreateRequest;
$open_grade = new OpenGrade;
$open_grade->grade="2";
$open_grade->classes="0";
$open_grade->name="二年级2019级";
$open_grade->start_year="2019";
$req->setOpenGrade($open_grade);
$req->setSuperId("2333");
$req->setOperator("12344");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/grade/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/grade/create");
OapiEduGradeCreateRequest req = new OapiEduGradeCreateRequest();
OapiEduGradeCreateRequest.OpenGradeDomain obj1 = new OapiEduGradeCreateRequest.OpenGradeDomain();
obj1.Grade = "2";
obj1.Classes = 0L;
obj1.Name = "二年级2019级";
obj1.StartYear = "2019";
req.OpenGrade_ = obj1;
req.SuperId = 2333L;
req.Operator = "12344";
OapiEduGradeCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenGradeCreateResponse |  | 调用结果。 |
| dept\_id | Number | 4240018 | 年级ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 5bsof0hsgtds | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "dept_id": 4240018
  },
  "success": true,
  "request_id": "5bsof0hsgtds"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
