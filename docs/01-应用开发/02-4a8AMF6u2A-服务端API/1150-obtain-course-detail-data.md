---
title: "获取课堂明细数据"
source_url: "https://open.dingtalk.com/document/development/obtain-course-detail-data"
namespace: "development"
slug: "obtain-course-detail-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课堂明细数据"
doc_id: "arUGSwFaQD"
updated_at: "2026-07-20 09:21:46"
---

> Source: https://open.dingtalk.com/document/development/obtain-course-detail-data
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 获取课堂明细数据
> Updated: 2026-07-20 09:21:46

# 获取课堂明细数据

调用本接口，可获取课堂明细数据，包括数据类别编码、课堂数据、课堂编码等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/course/detaildata/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_course\_read-钉钉教育在线课堂数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cursor | Number | 是 | 0 | 分页游标，从0开始。 |
| size | Number | 是 | 10 | 分页大小，取值0~100。 |
| factor\_codes | String[] | 否 | [\"joinClassroomTime\",\"leaveClassroomTime\"] | 数据因子编码数组。  不填则自动填充类别下全部的明细因子。  **[!NOTE]**  一次最多可传入100个数据因子。 |
| course\_code | String | 是 | GJKI49001 | 课程唯一编码，调用[创建课程](1137-create-course.md)接口获取course\_code参数值。 |
| category\_code | String | 是 | BASIC\_INFO | 数据类别编码，可参考[数据类别](1136-teaching-data-overview.md#section-2mx-hrp-6et)介绍。 |
| op\_userid | String | 是 | manager | 当前操作人的userId。 |
| user\_ids | String[] | 否 | [\"user01\"] | 需要获取的用户userId。  **[!NOTE]**  一次最多可传入100个userId。 |
| user\_cropid | String | 否 | ding4220d8e5128d0edd | 需要获取的用户的组织cropId。  **[!NOTE]**  必须和user\_ids同时传值或同时为空。  CorpId |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/course/detaildata/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=1bbb375d-e416-4f17-934f-d178d20d7f9b' \
-d 'category_code=BASIC_INFO' \
-d 'course_code=GJKI49001' \
-d 'cursor=0' \
-d 'factor_codes=joinClassroomTime%2CleaveClassroomTime' \
-d 'op_userid=manager' \
-d 'size=10' \
-d 'user_cropid=ding4220d8e5128d0edd' \
-d 'user_ids=user01%2Cuser02'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/detaildata/list");
OapiEduCourseDetaildataListRequest req = new OapiEduCourseDetaildataListRequest();
req.setCursor(0L);
req.setSize(10L);
req.setFactorCodes("[\"joinClassroomTime\",\"leaveClassroomTime\"]");
req.setCourseCode("GJKI49001");
req.setCategoryCode("BASIC_INFO");
req.setOpUserid("manager");
req.setUserIds("[\"user01\"]");
req.setUserCropid("ding4220d8e5128d0edd");
OapiEduCourseDetaildataListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCourseDetaildataListRequest("https://oapi.dingtalk.com/topapi/edu/course/detaildata/list")

req.cursor=0
req.size=10
req.factor_codes="joinClassroomTime,leaveClassroomTime"
req.course_code="GJKI49001"
req.category_code="BASIC_INFO"
req.op_userid="manager"
req.user_ids="user01,user02"
req.user_cropid="ding4220d8e5128d0edd"
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
$req = new OapiEduCourseDetaildataListRequest;
$req->setCursor("0");
$req->setSize("10");
$req->setFactorCodes("joinClassroomTime,leaveClassroomTime");
$req->setCourseCode("GJKI49001");
$req->setCategoryCode("BASIC_INFO");
$req->setOpUserid("manager");
$req->setUserIds("user01,user02");
$req->setUserCropid("ding4220d8e5128d0edd");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/course/detaildata/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/course/detaildata/list");
OapiEduCourseDetaildataListRequest req = new OapiEduCourseDetaildataListRequest();
req.Cursor = 0L;
req.Size = 10L;
req.FactorCodes = "joinClassroomTime,leaveClassroomTime";
req.CourseCode = "GJKI49001";
req.CategoryCode = "BASIC_INFO";
req.OpUserid = "manager";
req.UserIds = "user01,user02";
req.UserCropid = "ding4220d8e5128d0edd";
OapiEduCourseDetaildataListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageQueryResponse |  | 返回结果。 |
| next\_cursor | Number | 0 | 表示下一次分页的游标。  如果next\_corsor为null或者has\_more为false，表示没有更多的分页数据。 |
| has\_more | Boolean | true | 表示是否还有更多的数据。   - **true**：有 - **false**：没有 |
| list | CourseDetailDataDTO[] |  | 课堂明细数据。 |
| user\_cropid | String | ding4220d8e5128d0edd | 用户组织的corpId。 |
| userid | String | user01 | 用户的userId。 |
| category\_code | String | BASIC\_INFO | 数据类别编码，可参考[数据类别](1136-teaching-data-overview.md#section-2mx-hrp-6et)介绍。 |
| category\_biz\_key | String | b3540b13-60bf-4375-bfe5-633bbe5adef3\_JOIN\_1600741723451 | 数据业务唯一键，例如标识具体哪一次进入教室。 |
| value | String | 1600741723451 | 数据值，例如进入教室的时间戳。 |
| course\_code | String | GJKI49001 | 课堂编码。 |
| factor\_code | String | joinClassroomTime | 数据因子编码，可参考[数据因子](1136-teaching-data-overview.md#section-qcu-tp4-r03)介绍。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 2zw2h7s74d1 | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "next_cursor": 0,
    "has_more": true,
    "list": [
      {
        "category_biz_key": "b3540b13-60bf-4375-bfe5-633bbe5adef3_JOIN_1600741723451",
        "course_code": "GJKI49001",
        "category_code": "BASIC_INFO",
        "factor_code": "joinClassroomTime",
        "user_cropid": "ding4220d8e5128d0edd",
        "userid": "user01",
        "value": "1600741723451"
      }
    ]
  },
  "errcode": 0,
  "success": true,
  "errmsg": "ok",
  "request_id": "2zw2h7s074d1"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
