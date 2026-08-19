---
title: "批量查询地点"
source_url: "https://open.dingtalk.com/document/development/batch-query-position-under-attendance-group"
namespace: "development"
slug: "batch-query-position-under-attendance-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 批量查询地点"
doc_id: "uvogf2gtN9"
updated_at: "2026-05-27 17:05:50"
---

> Source: https://open.dingtalk.com/document/development/batch-query-position-under-attendance-group
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 批量查询地点
> Updated: 2026-05-27 17:05:50

# 批量查询地点

调用本接口，批量查询指定考勤组下的地点列表信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/positions/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b15xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| cursor | String | 否 | 0151Exxxx | 首次为空，后续 has\_more 为 true 时，cursor 值等于上次请求结果中最后一个 position\_key 的值。 |
| size | Number | 是 | 50 | 分页大小。 |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | CEDDFxxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/positions/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=80645xxxx3164b3' \
-d 'cursor=0151E02xxxx7E876' \
-d 'group_key=0151ExxxxA1A917E876' \
-d 'op_userid=123456' \
-d 'size=50'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/positions/query");
OapiAttendanceGroupPositionsQueryRequest req = new OapiAttendanceGroupPositionsQueryRequest();
req.setCursor("0151Exxxx");
req.setSize(50L);
req.setOpUserid("user01");
req.setGroupKey("CEDDFxxxx");
OapiAttendanceGroupPositionsQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupPositionsQueryRequest("https://oapi.dingtalk.com/topapi/attendance/group/positions/query")

req.cursor="0151E0xxxx917E876"
req.size=50
req.op_userid="123456"
req.group_key="0151E0xxxxA917E876"
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
$req = new OapiAttendanceGroupPositionsQueryRequest;
$req->setCursor("0151E0xxxx17E876");
$req->setSize("50");
$req->setOpUserid("123456");
$req->setGroupKey("0151E0xxxx917E876");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/positions/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/positions/query");
OapiAttendanceGroupPositionsQueryRequest req = new OapiAttendanceGroupPositionsQueryRequest();
req.Cursor = "0151E0xxxx917E876";
req.Size = 50L;
req.OpUserid = "123456";
req.GroupKey = "0151E02xxxx917E876";
OapiAttendanceGroupPositionsQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DingOpenResult |  | 返回结果。 |
| result | Result |  | 查询结果。 |
| position\_list | Position[] |  | position列表。 |
| offset | Number | 100 | 打卡位置允许偏移量。 |
| address | String | 阿里巴巴西溪园区 | 地址描述。 |
| latitude | String | 30.123 | 纬度(支持6位小数)。 |
| longitude | String | 120.123 | 经度(支持6位小数)。 |
| position\_key | String | 9E459Fxxxx | position的唯一标识。 |
| has\_more | Boolean | false | 是否还有更多。   - **true**：有 - **false**：没有 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | rss38gia1egs | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "errcode": 0,
    "errmsg":"ok",
    "result": {
      "has_more": false,
      "position_list": [
        {
          "offset":100,
          "address": "阿里巴巴西溪园区",
          "latitude": "30.280232",
          "longitude": "120.171377",
          "position_key": "9E459Fxxxx"
        }            ]
    },
    "success": true
  },
  "request_id": "rss38gia1egs"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
