---
title: "获取打卡详情"
source_url: "https://open.dingtalk.com/document/development/attendance-clock-in-record-is-open"
namespace: "development"
slug: "attendance-clock-in-record-is-open"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤打卡 > 获取打卡详情"
doc_id: "iVGmyqQjSb"
updated_at: "2026-05-27 17:05:52"
---

> Source: https://open.dingtalk.com/document/development/attendance-clock-in-record-is-open
> Path: 应用开发 / 服务端API / 考勤 > 考勤打卡 > 获取打卡详情
> Updated: 2026-05-27 17:05:52

# 获取打卡详情

调用本接口，获取企业内员工的实际打卡详情。

## **接口调用说明**

- 本接口不支持查询180天之前的数据。
- 如果只需要获取打卡结果数据，不需要详情数据，可使用[获取打卡结果](0195-open-attendance-clock-in-data.md)接口。
- 考勤信息同步可能会出现延迟，可稍后再试。
- **如果当天用户有排班，但是没有打卡操作，本接口返回的信息为空**。
- 本接口可以获取所有的打卡明细，员工迟到和作弊打卡等需要二次确认场景的打卡数据，这类属于无效打卡，获取之后要根据实际业务场景进行过滤，请关注出参`invalidRecordType`、`isLegal`和`invalidRecordMsg`。

例如，企业给一个员工设定的排班是上午9点和下午6点各打一次卡，但是员工在这期间打了多次，本接口会把所有的打卡记录都返回。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8685238471/p961028.png)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/attendance/listRecord |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_get\_attendance\_data-考勤数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userIds | List | 是 | ["user456","user123"] | 企业内的员工ID列表，最大值50。  **[!IMPORTANT]**  务必确保userId参数的正确性，否则本接口获取信息为空。 |
| checkDateFrom | String | 是 | 2020-09-07 00:00:00 | 查询考勤打卡记录的起始工作日。格式为：yyyy-MM-dd hh:mm:ss。  例如，参数传"2021-12-01 10:00:00"，员工在09:00的打卡信息获取不到。  **[!IMPORTANT]**  workDateFrom和workDateTo参数  相隔最多7天（包含7天） |
| checkDateTo | String | 是 | 2020-09-08 00:00:00 | 查询考勤打卡记录的结束工作日。格式为：yyyy-MM-dd hh:mm:ss。  例如，参数传"2021-12-01 18:00:00"，员工在19:00的打卡信息获取不到。  **[!IMPORTANT]**  workDateFrom和workDateTo参数  相隔最多7天（包含7天） |
| isI18n | Boolean | 否 | true | 是否为海外企业使用：   - **true**：海外平台使用 - **false**（默认）：国内平台使用 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/attendance/listRecord" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7258e1c9-af43-411c-b3f4-bcb069bfbb93' \
-d 'checkDateFrom=2018-01-01' \
-d 'checkDateTo=2018-01-01' \
-d 'isI18n=true' \
-d 'userIds=%221%22%2C%222%22'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/attendance/listRecord");
OapiAttendanceListRecordRequest req = new OapiAttendanceListRecordRequest();
req.setUserIds(Arrays.asList("user123","user456"));
req.setCheckDateFrom("2020-11-07 08:00:00");
req.setCheckDateTo("2020-11-12 08:00:00");
req.setIsI18n(false);
OapiAttendanceListRecordResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceListRecordRequest("https://oapi.dingtalk.com/attendance/listRecord")

req.userIds="[\"1\",\"2\"]"
req.checkDateFrom="2018-01-01"
req.checkDateTo="2018-01-01"
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
$req = new OapiAttendanceListRecordRequest;
$req->setUserIds("[\"1\",\"2\"]");
$req->setCheckDateFrom("2018-01-01");
$req->setCheckDateTo("2018-01-01");
$req->setIsI18n("true");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/attendance/listRecord");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/attendance/listRecord");
OapiAttendanceListRecordRequest req = new OapiAttendanceListRecordRequest();
req.UserIds = "[\"1\",\"2\"]";
req.CheckDateFrom = "2018-01-01";
req.CheckDateTo = "2018-01-01";
req.IsI18n = true;
OapiAttendanceListRecordResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | String | 0 | 返回码。 |
| recordresult | Array of Object |  | 打卡详情。 |
| userAccuracy | String | 65 | 用户打卡定位精度。 |
| classId | Long | 677995086 | 班次ID。 |
| userLatitude | String | 30.285622 | 用户打卡纬度。  **[!NOTE]**  打卡数据来源为ATM或DING\_ATM，不返回该字段。 |
| userLongitude | String | 120.017019 | 用户打卡经度。  **[!NOTE]**  打卡数据来源为ATM或DING\_ATM，不返回该字段。 |
| userAddress | String | 浙江省杭州市 | 用户打卡地址。  **[!NOTE]**  如果是考勤机打卡 userAddress，返回的是考勤机名称。 |
| deviceId | String | 67da0fxxxx | 打卡设备ID。  **[!NOTE]**  使用手机钉钉客户端打卡返回该字段。 |
| locationMethod | String | MAP | 定位方法。 |
| isLegal | String | N | 是否合法。   - **Y**：合法  **[!NOTE]**  当timeResult和locationResult都为Normal时，为该值。 - **N**：不合法 |
| userCheckTime | String | 1599450909000 | 实际打卡时间。 |
| procInstId | String | 59f77e82-xxxx | 关联的审批实例ID，当该字段非空时，表示打卡记录与请假、加班等审批有关。 |
| baseCheckTime | String | 1599442200000 | 计算迟到和早退，基准时间；也可作为排班打卡时间。 |
| approveId | String | 2376620852 | 关联的审批ID，当该字段非空时，表示打卡记录与请假、加班等审批有关。 |
| timeResult | String | Normal | 打卡结果：   - **Normal**：正常 - **Early**：早退 - **Late**：迟到 - **SeriousLate**：严重迟到 - **Absenteeism**：旷工迟到 - **NotSigned**：未打卡 |
| locationResult | String | Normal | 位置结果：   - **Normal**：范围内 - **Outside**：范围外 - **NotSigned**：未打卡 |
| checkType | String | OnDuty | 考勤类型：   - **OnDuty**：上班 - **OffDuty**：下班 |
| sourceType | String | USER | 数据来源：   - **ATM**：考勤机打卡（指纹/人脸打卡） - **BEACON**：IBeacon - **DING\_ATM**：钉钉考勤机（考勤机蓝牙打卡） - **USER**：用户打卡 - **BOSS**：老板改签 - **APPROVE**：审批系统 - **SYSTEM**：考勤系统 - **AUTO\_CHECK**：自动打卡 |
| userId | String | manager4220 | 打卡人的userId。 |
| workDate | String | 1599321600000 | 工作日。 |
| corpId | String | dinge8axxxx5384 | 企业ID。 |
| planId | String | 145342017988 | 排班ID。 |
| groupId | String | 685935028 | 考勤组ID。 |
| id | String | 101135139831 | 考勤ID。 |
| invalidRecordType | String | Other | 异常信息类型：   - **Security**：安全相关原因 - **Other**：其他原因 |
| userSsid | String | xxxx | 用户打卡wifi SSID。 |
| userMacAddr | String | 192.168.xx.xx | 用户打卡wifi Mac地址。 |
| planCheckTime | String | 1492568497000 | 排班打卡时间。 |
| baseAddress | String | 杭州 | 基准地址。 |
| baseLongitude | String | 12.109 | 基准经度。  **[!NOTE]**  打卡数据来源为ATM或**DING\_ATM**，不返回该字段 |
| baseLatitude | String | 0.123 | 基准纬度。  **[!NOTE]**  打卡数据来源为ATM或**DING\_ATM**，不返回该字段 |
| baseAccuracy | String | hazdgwrxxxx | 基准定位精度。 |
| baseSsid | String | 423dsddfxxxx | 基准wifi ssid。 |
| baseMacAddr | String | 00:27:19:48:58:4c | 基准Mac地址。 |
| gmtCreate | String | 1599441505000 | 打卡记录创建时间。 |
| invalidRecordMsg | String | 需要二次确认 | 对应的**invalidRecordType**异常信息的具体描述。 |
| gmtModified | String | 1599441505001 | 打卡记录修改时间。 |
| outsideRemark | String | 拜访客户 | 打卡备注。 |
| deviceSN | String | gd53354xxxx | 打卡设备序列号。 |
| bizId | String | E171DCCExxxx | 关联的业务ID。 |
| photoUrl | String | https://static.dingtalk.com/media/lQDPM369C6xxxxK6PiY | 拍照图片 URL。  **[!NOTE]**   - 如需使用该参数，请使用HTTP的方式调用该接口，SDK不返回该参数。 - 若打卡详情中有拍照的图片信息，会返回 photoUrl，否则该字段不返回。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "recordresult": [
    {
      "gmtModified": 1599454972000,
      "baseCheckTime": 1599442200000,
      "groupId": 685935028,
      "timeResult": "Normal",
      "deviceId": "67da0fxxxx",
      "approveId": 2376620852,
      "userAccuracy": 65,
      "classId": 677995086,
      "workDate": 1599408000000,
      "bizId": "E171DCCExxxx",
      "planId": 144872188720,
      "id": 43047156750,
      "checkType": "OnDuty",
      "planCheckTime": 1599442200000,
      "corpId": "dinge8axxxx5384",
      "locationResult": "Outside",
      "userLongitude": 120.017139,
      "isLegal": "N",
      "procInstId": "59f77e82-xxxx",
      "gmtCreate": 1599441505000,
      "userId": "manager4220",
      "outsideRemark": "拜访客户",
      "userAddress": "浙江省杭州市",
      "userLatitude": 30.285413,
      "sourceType": "USER",
      "userCheckTime": 1599441505000,
      "locationMethod": "MAP"
    },
    {
      "gmtModified": 1599450909000,
      "deviceId": "67da0fxxxx",
      "userAccuracy": 65,
      "workDate": 1599408000000,
      "bizId": "E171DCCExxxx",
      "id": 43055377426,
      "invalidRecordType": "Other",
      "corpId": "dinge8axxxx5384",
      "userLongitude": 120.017019,
      "gmtCreate": 1599450909000,
      "invalidRecordMsg": "需要二次确认",
      "userId": "manager4220",
      "userAddress": "浙江省杭州市",
      "userLatitude": 30.285622,
      "sourceType": "USER",
      "userCheckTime": 1599450909000,
      "locationMethod": "MAP"
    }
  ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
