---
title: "上传打卡记录"
source_url: "https://open.dingtalk.com/document/development/upload-punch-records"
namespace: "development"
slug: "upload-punch-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤打卡 > 上传打卡记录"
doc_id: "R9Zrzl0rDO"
updated_at: "2026-05-27 18:39:33"
---

> Source: https://open.dingtalk.com/document/development/upload-punch-records
> Path: 应用开发 / 服务端API / 考勤 > 考勤打卡 > 上传打卡记录
> Updated: 2026-05-27 18:39:33

# 上传打卡记录

调用本接口将三方考勤系统的刷卡或刷脸记录上传到钉钉考勤，做为钉钉打卡流水。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/record/upload |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Pro.AttendanceRecord.Write-考勤打卡记录写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | af21axxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user123 | 需要上传打卡记录的员工userId。 |
| device\_name | String | 是 | 东门考勤机 | 考勤机名称，该参数值是自定义的，比如123456。 |
| device\_id | String | 是 | abc123456 | 考勤机ID，该参数值是自定义的，比如abcde。 |
| photo\_url | String | 否 | https://xxx.com/xxx.png | 打卡备注图片地址，必须是公网可访问的地址。 |
| user\_check\_time | Number | 是 | 1587020403000 | 员工打卡的时间，单位毫秒。  **[!NOTE]**   - 该参数单位必须是毫秒。 - 需要传 180 天以内的日期。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/record/upload" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0927xxxx3e28ea' \
-d 'device_id=abc123456' \
-d 'device_name=%E4%B8%9C%E9%97%A8%E8%80%83%E5%8B%A4%E6%9C%BA' \
-d 'photo_url=https%3A%2F%2Fxxx.com%2Fxxx.png' \
-d 'user_check_time=1587020403000' \
-d 'userid=dd_dd'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/record/upload");
OapiAttendanceRecordUploadRequest req = new OapiAttendanceRecordUploadRequest();
req.setUserid("dd_dd");
req.setDeviceName("东门考勤机");
req.setDeviceId("abc123456");
req.setPhotoUrl("https://xxx.com/xxx.png");
req.setUserCheckTime(1587020403000L);
OapiAttendanceRecordUploadResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceRecordUploadRequest("https://oapi.dingtalk.com/topapi/attendance/record/upload")

req.userid="dd_dd"
req.device_name="东门考勤机"
req.device_id="abc123456"
req.photo_url="https://xxx.com/xxx.png"
req.user_check_time=1587020403000
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
$req = new OapiAttendanceRecordUploadRequest;
$req->setUserid("dd_dd");
$req->setDeviceName("东门考勤机");
$req->setDeviceId("abc123456");
$req->setPhotoUrl("https://xxx.com/xxx.png");
$req->setUserCheckTime("1587020403000");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/record/upload");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/record/upload");
OapiAttendanceRecordUploadRequest req = new OapiAttendanceRecordUploadRequest();
req.Userid = "dd_dd";
req.DeviceName = "东门考勤机";
req.DeviceId = "abc123456";
req.PhotoUrl = "https://xxx.com/xxx.png";
req.UserCheckTime = 1587020403000L;
OapiAttendanceRecordUploadResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | ktoftehkz2bt | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "success":true,
  "request_id" : "3ynh2gp5ndke"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
