---
title: "批量查询Wi-Fi信息"
source_url: "https://open.dingtalk.com/document/development/batch-query-wifi-under-attendance-group"
namespace: "development"
slug: "batch-query-wifi-under-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤组管理 > 批量查询Wi-Fi信息"
doc_id: "NHbXJxmyYh"
updated_at: "2026-05-27 13:10:07"
---

> Source: https://open.dingtalk.com/document/development/batch-query-wifi-under-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 考勤组管理 > 批量查询Wi-Fi信息
> Updated: 2026-05-27 13:10:07

# 批量查询Wi-Fi信息

调用本接口，批量查询指定考勤组下的Wi-Fi列表信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/wifis/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b1534xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cursor | String | 否 | 0151E022xxxx | 上一批次最后一个Id，默认为空。 |
| size | Number | 是 | 50 | 分页大小。 |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | 015xxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/wifis/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=698cxxxx9b13' \
-d 'cursor=0151E0xxxx17E876' \
-d 'group_key=0151Exxxx17E876' \
-d 'op_userid=123456' \
-d 'size=50'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/wifis/query");
OapiAttendanceGroupWifisQueryRequest req = new OapiAttendanceGroupWifisQueryRequest();
req.setCursor("0151E022xxxx");
req.setSize(50L);
req.setOpUserid("user01");
req.setGroupKey("015xxxx");
OapiAttendanceGroupWifisQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupWifisQueryRequest("https://oapi.dingtalk.com/topapi/attendance/group/wifis/query")

req.cursor="0151E0xxxx917E876"
req.size=50
req.op_userid="123456"
req.group_key="0151E0xxxx917E876"
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
$req = new OapiAttendanceGroupWifisQueryRequest;
$req->setCursor("0151E0xxxxE876");
$req->setSize("50");
$req->setOpUserid("123456");
$req->setGroupKey("0151E02xxxx7E876");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/wifis/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/wifis/query");
OapiAttendanceGroupWifisQueryRequest req = new OapiAttendanceGroupWifisQueryRequest();
req.Cursor = "0151E022xxxx7E876";
req.Size = 50L;
req.OpUserid = "123456";
req.GroupKey = "0151E02xxxxA917E876";
OapiAttendanceGroupWifisQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DingOpenResult |  | 返回结果。 |
| result | Result |  | 查询Wi-Fi列表结果。 |
| wifi\_list | Wifi[] |  | Wi-Fi列表。 |
| mac\_addr | String | 54:8D:xx:xx:xx:73 | mac地址。 |
| ssid | String | alibaba-inc | Wi-Fi名称。 |
| wifi\_key | String | E4CB0xxxx | Wi-Fi的key。 |
| has\_more | Boolean | true | 是否还有更多。   - **true**：有 - **false**：没有 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | 155qyie8nxoqu | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "errcode": 0,
    "errmsg":"ok",
    "result": {
      "has_more": false,
      "wifi_list": [
        {
          "mac_addr": "54:8D:xx:xx:xx:73",
          "ssid": "alibaba-inc",
          "wifi_key": "E4CB0xxxx"
        }
      ]
    },
    "success": true
  },
  "request_id": "155qyie8nxoqu"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
