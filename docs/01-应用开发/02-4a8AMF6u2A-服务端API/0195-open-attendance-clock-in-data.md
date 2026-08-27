---
title: "获取打卡结果"
source_url: "https://open.dingtalk.com/document/development/open-attendance-clock-in-data"
namespace: "development"
slug: "open-attendance-clock-in-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤打卡 > 获取打卡结果"
doc_id: "Ai0FqxfGGB"
updated_at: "2026-05-27 17:05:51"
---

> Source: https://open.dingtalk.com/document/development/open-attendance-clock-in-data
> Path: 应用开发 / 服务端API / 考勤 > 考勤打卡 > 获取打卡结果
> Updated: 2026-05-27 17:05:51

# 获取打卡结果

调用本接口，获取企业内员工的实际打卡结果。

## **接口调用说明**

- 本接口不支持查询半年以前的数据。
- 如果需要获取打卡详细数据，例如打卡位置，可以使用[获取打卡详情](0196-attendance-clock-in-record-is-open.md)接口。
- 考勤信息同步可能会出现延迟，可稍后再试。
- **如果当天用户有排班，但是没有打卡操作，本接口会返回当天排班的卡点信息，不会返回空**。

例如，企业给一个员工设定的排班是上午9点和下午6点各打一次卡，即使员工在这期间打了多次，本接口也只会返回两条记录，包括上午的打卡结果和下午的打卡结果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7685238471/p961023.png)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/attendance/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_isv\_query\_result-企业考勤数据读权限permission-qyapi\_get\_attendance\_data-考勤数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| workDateFrom | String | 是 | 2020-11-07 08:00:00 | 查询考勤打卡记录的起始工作日。格式为yyyy-MM-dd HH:mm:ss，HH:mm:ss可以使用00:00:00，将返回此日期从0点到24点的结果。  例如，参数传"2021-12-01 10:00"，获取的是12月1日一整天的考勤结果。  **[!IMPORTANT]**  workDateFrom和workDateTo参数  相隔最多7天（包含7天）。 |
| workDateTo | String | 是 | 2020-11-11 08:00:00 | 查询考勤打卡记录的结束工作日。格式为“yyyy-MM-dd HH:mm:ss”，HH:mm:ss可以使用00:00:00，将返回此日期从0点到24点的结果。  例如，参数传"2021-12-01 19:00"，获取的是12月1日一整天的考勤结果。  **[!IMPORTANT]**  workDateFrom和workDateTo参数  相隔最多7天（包含7天）。 |
| userIdList | String[] | 是 | ["manager4220"] | 员工在企业内的userId列表，最大值50。  **[!IMPORTANT]**  务必确保userId参数的正确性，否则本接口获取信息为空。 |
| offset | Number | 是 | 0 | 表示获取考勤数据的起始点。第一次传0，如果还有多余数据，下次获取传的offset值为之前的offset+limit，0、1、2...依次递增。 |
| limit | Number | 是 | 50 | 表示获取考勤数据的条数，最大值50。 |
| isI18n | Boolean | 否 | true | 是否为海外企业使用：   - **true**：海外平台使用 - **false**（默认）：国内平台使用 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/attendance/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=713b06xxxxd4cbdf4' \
-d 'isI18n=true' \
-d 'limit=100' \
-d 'offset=0' \
-d 'userIdList=1' \
-d 'workDateFrom=yyyy-MM-dd+hh%3Amm%3Ass' \
-d 'workDateTo=yyyy-MM-dd+hh%3Amm%3Ass'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/attendance/list");
OapiAttendanceListRequest req = new OapiAttendanceListRequest();
req.setWorkDateFrom("2020-11-07 08:00:00");
req.setWorkDateTo("2020-11-11 08:00:00");
req.setUserIdList(Arrays.asList("manager"));
req.setOffset(0L);
req.setLimit(10L);
req.setIsI18n(true);
OapiAttendanceListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceListRequest("https://oapi.dingtalk.com/attendance/list")

req.workDateFrom="yyyy-MM-dd hh:mm:ss"
req.workDateTo="yyyy-MM-dd hh:mm:ss"
req.userIdList="1"
req.offset=0
req.limit=100
req.isI18n=true
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
$req = new OapiAttendanceListRequest;
$req->setWorkDateFrom("yyyy-MM-dd hh:mm:ss");
$req->setWorkDateTo("yyyy-MM-dd hh:mm:ss");
$req->setUserIdList("1");
$req->setOffset("0");
$req->setLimit("100");
$req->setIsI18n("true");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/attendance/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/attendance/list");
OapiAttendanceListRequest req = new OapiAttendanceListRequest();
req.WorkDateFrom = "yyyy-MM-dd hh:mm:ss";
req.WorkDateTo = "yyyy-MM-dd hh:mm:ss";
req.UserIdList = "1";
req.Offset = 0L;
req.Limit = 100L;
req.IsI18n = true;
OapiAttendanceListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| recordresult | Recordresult[] |  | 打卡记录。 |
| sourceType | String | USER | 数据来源：   - **ATM**：考勤机打卡（指纹/人脸打卡） - **BEACON**：IBeacon - **DING\_ATM**：钉钉考勤机（考勤机蓝牙打卡） - **USER**：用户打卡 - **BOSS**：老板改签 - **APPROVE**：审批系统 - **SYSTEM**：考勤系统 - **AUTO\_CHECK**：自动打卡 |
| baseCheckTime | Date | 1599378660000 | 计算迟到和早退，基准时间。 |
| userCheckTime | Date | 1599378681000 | 实际打卡时间, 用户打卡时间的毫秒数。 |
| procInstId | String | 59f77e82-6625-4a31-b434 | 关联的审批实例ID，当该字段非空时，表示打卡记录与请假、加班等审批有关。 |
| approveId | Number | 2376620852 | 关联的审批ID，当该字段非空时，表示打卡记录与请假、加班等审批有关。 |
| locationResult | String | Normal | 位置结果：   - **Normal**：范围内 - **Outside**：范围外 - **NotSigned**：未打卡 |
| timeResult | String | Normal | 打卡结果：   - **Normal**：正常 - **Early**：早退 - **Late**：迟到 - **SeriousLate**：严重迟到 - **Absenteeism**：旷工迟到 - **NotSigned**：未打卡 |
| checkType | String | OnDuty | 考勤类型：   - **OnDuty**：上班 - **OffDuty**：下班 |
| userId | String | manager4220 | 打卡人的userId。 |
| workDate | Date | 1599321600000 | 工作日。 |
| recordId | Number | 43002777448 | 打卡记录ID。 |
| planId | Number | 145342017988 | 排班ID。 |
| groupId | Number | 685935028 | 考勤组ID。 |
| id | Number | 101135139831 | 唯一标识ID。 |
| hasMore | Boolean | false | 分页返回参数，表示是否还有更多数据。   - **true**：有 - **false**：没有 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode": 0,
  "recordresult": [
    {
      "checkType": "OnDuty",
      "locationResult": "Normal",
      "baseCheckTime": 1599372300000,
      "groupId": 685935028,
      "timeResult": "Normal",
      "userId": "manager4220",
      "recordId": 42833709096,
      "workDate": 1599321600000,
      "sourceType": "APPROVE",
      "userCheckTime": 1599372300000,
      "planId": 145583519353,
      "id": 100068640553
    },
    {
      "checkType": "OffDuty",   
      "locationResult": "Normal",
      "baseCheckTime": 1599373560000,
      "groupId": 685935028,
      "timeResult": "Normal",
      "userId": "manager4220",
      "recordId": 43003136655,
      "workDate": 1599321600000,
      "sourceType": "USER",
      "userCheckTime": 1599373608000,
      "planId": 144623724178,
      "id": 100375228689
    }
  ],
  "hasMore": false,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
