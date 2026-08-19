---
title: "创建学段"
source_url: "https://open.dingtalk.com/document/development/create-a-learning-segment"
namespace: "development"
slug: "create-a-learning-segment"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建学段"
doc_id: "OpkayGkV72"
updated_at: "2026-07-20 09:21:49"
---

> Source: https://open.dingtalk.com/document/development/create-a-learning-segment
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建学段
> Updated: 2026-07-20 09:21:49

# 创建学段

调用本接口，在指定校区下创建学段。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/period/create |
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
| super\_id | Number | 是 | 4240018 | 校区ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为campus时的dept\_id参数值。 |
| operator | String | 是 | user01 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |
| open\_period | OpenPeriod | 是 |  | 学段信息。 |
| step | String | 是 | 小学 | 学段名称。   - 幼儿园 - 小学 - 初中 - 高中 |
| grades | Grades[] | 是 |  | 年级列表，最大列表长度为999。 |
| grade | String | 是 | 2 | 年级级数，一年级为1，二年级为2。 |
| classes | Number | 是 | 0 | 每个年级下班级级数，1班为1，2班为2。0表示无限。  **[!NOTE]**  尽量不要超过100个，否则页面性能有问题。 |
| name | String | 是 | 二年级2019级 | 年级名称，需要与grade和start\_year对应。 |
| start\_year | String | 是 | 2019 | 入学年份。  **[!NOTE]**  请注意start\_year、name、grade三者之间的关联关系。 |
| period\_code | String | 是 | primary\_school | 学段编码。   - **kindergarten** ：幼儿园 - **primary\_school**：小学 - **middle\_school**： 初中 - **high\_school**： 高中 |
| name\_mode | String | 是 | number | 学段名称类型。   - **text**：文本型，如初中为七年级，八年级，九年级。 - **number**：数字型，如初中一年级1班，二年级1班等。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/period/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=66c8b742-eef5-47dc-aa3f-db35b8b0119a' \
-d 'open_period=null' \
-d 'operator=12334' \
-d 'super_id=1233'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/period/create");
OapiEduPeriodCreateRequest req = new OapiEduPeriodCreateRequest();
OapiEduPeriodCreateRequest.OpenPeriod periods = new OapiEduPeriodCreateRequest.OpenPeriod();
periods.setStep("小学");
List<OapiEduPeriodCreateRequest.Grades> VoGrades = new ArrayList<OapiEduPeriodCreateRequest.Grades>();
Grades grades = new Grades();
grades.setGrade("2");
grades.setClasses(0L);
grades.setName("二年级2019级");
grades.setStartYear("2019");
VoGrades.add(grades);
periods.setGrades(VoGrades);
periods.setPeriodCode("primary_school");
periods.setNameMode("number");
req.setSuperId(4240018L);
req.setOpenPeriod("user01");
req.setOpenPeriod(periods);
OapiEduPeriodCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduPeriodCreateRequest("https://oapi.dingtalk.com/topapi/edu/period/create")

req.super_id=1233
req.operator="12334"
req.open_period=""
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
$req = new OapiEduPeriodCreateRequest;
$req->setSuperId("1233");
$req->setOperator("12334");
$open_period = new OpenPeriod;
$open_period->step="小学";
$grades = new Grades;
$grades->grade="2";
$grades->classes="0";
$grades->name="二年级2019级";
$grades->start_year="2019";
$open_period->grades = array($grades);
$open_period->period_code="high_school";
$open_period->name_mode="number";
$req->setOpenPeriod($open_period);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/period/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/period/create");
OapiEduPeriodCreateRequest req = new OapiEduPeriodCreateRequest();
req.SuperId = 1233L;
req.Operator = "12334";
OapiEduPeriodCreateRequest.OpenPeriodDomain obj1 = new OapiEduPeriodCreateRequest.OpenPeriodDomain();
obj1.Step = "小学";
List<OapiEduPeriodCreateRequest.GradesDomain> list3 = new List<OapiEduPeriodCreateRequest.GradesDomain>();
OapiEduPeriodCreateRequest.GradesDomain obj4 = new OapiEduPeriodCreateRequest.GradesDomain();
list3.Add(obj4);
obj4.Grade = "2";
obj4.Classes = 0L;
obj4.Name = "二年级2019级";
obj4.StartYear = "2019";
obj1.Grades= list3;
obj1.PeriodCode = "high_school";
obj1.NameMode = "number";
req.OpenPeriod_ = obj1;
OapiEduPeriodCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenPeriodCreateResponse |  | 调用结果。 |
| deptId | Number | 3 | 学段ID。 |
| grades | EduGradeDo[] |  | 年级列表。 |
| campus\_id | Number | 122 | 校区ID。 |
| dept\_id | Number | 4240018 | 年级ID。 |
| grade | Number | 2 | 年级级数，一年级为1，二年级为2。 |
| name | String | 二年级2019级 | 年级名。 |
| super\_id | Number | 4240018 | 学段ID。 |
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
    "deptId": "",
    "grades": [
      {
        "campus_id": 122,
        "dept_id": 4240018,
        "grade": 2,
        "name": "二年级2019级",
        "super_id": 4240018
      }
    ]
  },
  "success": true,
  "request_id": "5bsof0hsgtds"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
