---
title: "批量移除Wi-Fi信息"
source_url: "https://open.dingtalk.com/document/development/batch-remove-wifi-under-attendance-group"
namespace: "development"
slug: "batch-remove-wifi-under-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 批量移除Wi-Fi信息"
doc_id: "RVdQPVLBYU"
updated_at: "2026-05-27 13:10:05"
---

> Source: https://open.dingtalk.com/document/development/batch-remove-wifi-under-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 批量移除Wi-Fi信息
> Updated: 2026-05-27 13:10:05

# 批量移除Wi-Fi信息

调用本接口，批量移除指定考勤组的Wi-Fi信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/wifis/remove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | CEDDFxxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |
| wifi\_key\_list | String | 是 | 0151Exxxx | Wi-Fi的key，可通过[批量查询Wi-Fi信息](0190-batch-query-wifi-under-attendance-group.md)接口获取，每次调用最多支持移除100个Wi-Fi信息。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/wifis/remove" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=deb9baxxxx32b89' \
-d 'group_key=0151E022xxxx917E876' \
-d 'op_userid=123456' \
-d 'wifi_key_list=0151E02xxxx917E876'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/wifis/remove");
OapiAttendanceGroupWifisRemoveRequest req = new OapiAttendanceGroupWifisRemoveRequest();
req.setOpUserid("user01");
req.setGroupKey("CEDDFxxxx");
req.setWifiKeyList("0151Exxxx");
OapiAttendanceGroupWifisRemoveResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupWifisRemoveRequest("https://oapi.dingtalk.com/topapi/attendance/group/wifis/remove")

req.op_userid="123456"
req.group_key="0151E02xxxx917E876"
req.wifi_key_list="0151E02xxxx7E876"
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
$req = new OapiAttendanceGroupWifisRemoveRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151E02xxxx17E876");
$req->setWifiKeyList("0151E02xxxx7E876");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/wifis/remove");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/wifis/remove");
OapiAttendanceGroupWifisRemoveRequest req = new OapiAttendanceGroupWifisRemoveRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E022xxxx7E876";
req.WifiKeyList = "0151E0xxxx17E876";
OapiAttendanceGroupWifisRemoveResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 删除成功的wifiId列表。 |
| error\_info\_list | ErrorInfo[] |  | 失败列表。 |
| failure\_list | String[] | 0151EEDDDF0xxxx | 错误列表。 |
| msg | String | business fault | 错误描述。 |
| code | String | 1000 | 错误码。 |
| success\_list | String[] | 0151EEDDDF0xxxx | 成功列表。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 7o76z7s5cett | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "success_list": [
      "0151Exxxx",
    ]
  },
  "success": true,
  "request_id": "7o76z7s5cett"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
