---
title: "初始化家校架构"
source_url: "https://open.dingtalk.com/document/development/initialize-the-home-school-architecture"
namespace: "development"
slug: "initialize-the-home-school-architecture"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 初始化家校架构"
doc_id: "uGf8BGUv3m"
updated_at: "2026-06-08 09:48:09"
---

> Source: https://open.dingtalk.com/document/development/initialize-the-home-school-architecture
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 初始化家校架构
> Updated: 2026-06-08 09:48:09

# 初始化家校架构

调用本接口，初始化家校结构。

## **接口调用说明**

本接口只支持在没有校区的情况下初始化一次校区，不支持创建多校区的情况。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/school/init |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-钉钉教育家校通讯录写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| campus | OpenCampus | 是 |  | 校区信息。 |
| name | String | 是 | 实验学校 | 校区名称。 |
| periods | OpenPeriod[] | 是 |  | 学段列表。 |
| step | String | 是 | 小学 | 学段名称：   - 幼儿园 - 小学 - 初中 - 高中 |
| grades | OpenGrade[] | 是 |  | 年级列表，最大列表长度为999。 |
| grade | String | 是 | 2 | 年级级数，一年级为1，二年级为2。 |
| name | String | 是 | 二年级2019级 | 年级名称，需要与grade和start\_year对应。 |
| start\_year | String | 是 | 2019 | 入学年份。  **[!NOTE]**  请注意start\_year、name、grade三者之间的关联关系。 |
| classes | Number | 是 | 0 | 每个年级下班级级数，1班为1，2班为2。0表示无限。  **[!NOTE]**  尽量不要超过100个，否则页面性能有问题。 |
| period\_code | String | 是 | primary\_school | 学段编码。   - **kindergarten** ：幼儿园 - **primary\_school**：小学 - **middle\_school**： 初中 - **high\_school**： 高中 |
| name\_mode | String | 是 | number | 学段名称类型。   - **text**：文本型，如初中为七年级，八年级，九年级。 - **number**：数字型，如初中一年级1班，二年级1班等。 |
| operator | String | 是 | user01 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |

### **请求示例**

curl

```
curl -i 'https://oapi.dingtalk.com/topapi/edu/school/init' \
  -X 'POST' \
  -H 'Content-Type: application/json' \
  -H 'x-acs-dingtalk-access-token: 74c17e625cd83b628847837c7b6ac144' \
  -d 'operator:12344' \
  -d 'campus:null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/school/init");
OapiEduSchoolInitRequest req = new OapiEduSchoolInitRequest();
OpenCampus campus = new OpenCampus();
campus.setName("实验学校");
List<OapiEduSchoolInitRequest.OpenPeriod> VoPeriods = new ArrayList<OapiEduSchoolInitRequest.OpenPeriod>();
OpenPeriod periods = new OpenPeriod();
periods.setStep("小学");
OpenGrade openGrade =new OpenGrade();
openGrade.setGrade("2");
openGrade.setName("二年级2019级");
openGrade.setStartYear("2019");
openGrade.setClasses(0L);
VoPeriods.add(periods);
campus.setPeriods(VoPeriods);
req.setOperator("user01");
req.setCampus(campus);
OapiEduSchoolInitResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduSchoolInitRequest("https://oapi.dingtalk.com/topapi/edu/school/init")

req.campus="数据结构示例JSON格式"
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
$req = new OapiEduSchoolInitRequest;
$campus = new OpenCampus;
$campus->name="余杭校区";
$periods = new OpenPeriod;
$campus->periods = array($periods);
$req->setCampus($campus);
$req->setOperator("12344");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/school/init");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/school/init");
OapiEduSchoolInitRequest req = new OapiEduSchoolInitRequest();
OpenCampus campus = new OpenCampus();
campus.Name = "实验学校";
List<OpenPeriod> periodsList = new List<OpenPeriod>();
OpenPeriod period = new OpenPeriod();
period.Step = "小学";
OpenGrade grade = new OpenGrade();
grade.Grade = "2";
grade.Name = "二年级2019级";
grade.StartYear = "2019";
grade.Classes = 0L;
period.Periods = new List<OpenGrade> { grade };
periodsList.Add(period);
campus.Periods = periodsList;
req.Operator = "user01";
req.Campus = campus;
OapiEduSchoolInitResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenEduSchoolInitResponse |  | 初始化结果。 |
| campus\_list | Number[] | [100, 35  ] | 校区列表。 |
| effected | String | 1 | - **0**：已经有校区，不会进行初始化校区。 - **1**：执行了初始化校区。 |
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
    "campus_list": [
      100,
      35
    ],
    "effected": "1"
  },
  "success": true,
  "request_id": "5bsof0hsgtds"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
