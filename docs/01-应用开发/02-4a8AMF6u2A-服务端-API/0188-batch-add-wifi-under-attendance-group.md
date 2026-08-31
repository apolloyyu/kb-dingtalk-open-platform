---
title: "批量新增Wi-Fi信息"
source_url: "https://open.dingtalk.com/document/development/batch-add-wifi-under-attendance-group"
namespace: "development"
slug: "batch-add-wifi-under-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 批量新增Wi-Fi信息"
doc_id: "7U7Hd1UIt9"
updated_at: "2026-05-27 13:10:03"
---

> Source: https://open.dingtalk.com/document/development/batch-add-wifi-under-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 批量新增Wi-Fi信息
> Updated: 2026-05-27 13:10:03

# 批量新增Wi-Fi信息

调用本接口，为指定考勤组批量新增Wi-Fi信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/wifis/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 1eb68xxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人的userId。 |
| group\_key | String | 是 | 0151E0xxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |
| wifi\_list | Wifi[] | 是 |  | Wi-Fi列表，每次调用最多新增100个Wi-Fi信息。 |
| foreign\_id | String | 是 | alibaba-inc | 业务方wifiId。 |
| mac\_addr | String | 是 | 11:11:11:11:11:11 | MAC地址。 |
| ssid | String | 是 | alibaba-inc1 | 名称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/wifis/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b040xxxx34a60' \
-d 'group_key=0151E02xxxx17E876' \
-d 'op_userid=123456' \
-d 'wifi_list=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/wifis/add");
OapiAttendanceGroupWifisAddRequest req = new OapiAttendanceGroupWifisAddRequest();
req.setOpUserid("123456");
req.setGroupKey("0151Exxxx17E876");
List<Wifi> list2 = new ArrayList<Wifi>();
Wifi obj3 = new Wifi();
list2.add(obj3);
obj3.setForeignId("123456");
obj3.setMacAddr("11:11:11:11:11:11");
obj3.setSsid("alibaba-guest");
req.setWifiList(list2);
OapiAttendanceGroupWifisAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupWifisAddRequest("https://oapi.dingtalk.com/topapi/attendance/group/wifis/add")

req.op_userid="123456"
req.group_key="0151E022xxxx17E876"
req.wifi_list=""
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
$req = new OapiAttendanceGroupWifisAddRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151E0xxxx7E876");
$wifi_list = new Wifi;
$wifi_list->foreign_id="123456";
$wifi_list->mac_addr="11:11:11:11:11:11";
$wifi_list->ssid="alibaba-guest";
$req->setWifiList(array($wifi_list));
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/wifis/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/wifis/add");
OapiAttendanceGroupWifisAddRequest req = new OapiAttendanceGroupWifisAddRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E0xxxx17E876";
List<OapiAttendanceGroupWifisAddRequest.WifiDomain> list2 = new List<OapiAttendanceGroupWifisAddRequest.WifiDomain>();
OapiAttendanceGroupWifisAddRequest.WifiDomain obj3 = new OapiAttendanceGroupWifisAddRequest.WifiDomain();
list2.Add(obj3);
obj3.ForeignId = "123456";
obj3.MacAddr = "11:11:11:11:11:11";
obj3.Ssid = "alibaba-guest";
req.WifiList_ = list2;
OapiAttendanceGroupWifisAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DingOpenResult |  | 返回的信息。 |
| result | Result |  | 添加Wi-Fi结果。 |
| error\_info\_list | ErrorInfo[] |  | 添加失败的Wi-Fi列表。 |
| failure\_list | Wifi[] |  | 失败列表。 |
| foreign\_id | String | alibaba-guest | 业务方wifiId。 |
| mac\_addr | String | 02:10:18:11:11:11 | MAC地址。 |
| ssid | String | alibaba-guest1 | MAC名称。 |
| wifi\_key | String | 01xxxxE876 | 添加Wi-Fi失败的key。 |
| msg | String | business fault | 错误描述。 |
| code | String | 1000 | 错误码。 |
| success\_list | Wifi[] |  | 添加成功的Wi-Fi列表。 |
| foreign\_id | String | alibaba-inc | 业务方wifiId。 |
| mac\_addr | String | 11:11:11:11:11:11 | MAC地址。 |
| ssid | String | alibaba-inc1 | MAC名称。 |
| wifi\_key | String | 01xxxxE876 | 添加Wi-Fi成功的key。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | wicoxqraqt0g | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "errcode": 0,
    "errmsg":"ok",
    "result": {
      "error_info_list": [
        {
          "code": "1000",
          "failure_list": [
            {
              "foreign_id": "alibaba-guest",
              "mac_addr": "02:10:18:11:11:11",
              "ssid": "alibaba-guest1"
            }
          ],
          "msg": "business fault"
        }
      ],
      "success_list": [
        {
          "foreign_id": "alibaba-inc",
          "mac_addr": "11:11:11:11:11:11",
          "ssid": "alibaba-inc1"
        }
      ]
    },
    "success": true
  },
  "request_id": "10enywafok7h8"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
