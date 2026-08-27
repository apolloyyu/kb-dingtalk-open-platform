---
title: "批量新增地点"
source_url: "https://open.dingtalk.com/document/development/atch-add-position-under-attendance-group"
namespace: "development"
slug: "atch-add-position-under-attendance-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 批量新增地点"
doc_id: "zq96ahcncm"
updated_at: "2026-05-27 13:10:08"
---

> Source: https://open.dingtalk.com/document/development/atch-add-position-under-attendance-group
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 批量新增地点
> Updated: 2026-05-27 13:10:08

# 批量新增地点

调用本接口，在指定考勤组下批量新增地点。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/positions/add |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_manage-考勤组管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b1534xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user01 | 操作人userId。 |
| group\_key | String | 是 | 03B1Exxxx | 考勤组ID。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |
| position\_list | Object[] | 是 |  | postion列表，每次新增最多支持新增100个地点信息。 |
| address | String | 是 | 阿里巴巴西溪北苑 | 地址描述。 |
| foreign\_id | String | 是 | 0151E23B1 | 业务方positionId。 |
| longitude | String | 是 | 120.123 | 经度(支持6位小数)。 |
| latitude | String | 是 | 30.123 | 纬度(支持6位小数)。 |
| offset | Number | 否 | 100 | 打卡位置允许的偏移量，单位米。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/positions/add" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=23adcxxxx46c5226' \
-d 'group_key=0151E02xxxx917E876' \
-d 'op_userid=123456' \
-d 'position_list=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/positions/add");
OapiAttendanceGroupPositionsAddRequest req = new OapiAttendanceGroupPositionsAddRequest();
req.setOpUserid("user01");
req.setGroupKey("03B1Exxxx");
List<Position> list = new ArrayList<Position>();
Position position = new Position();
list.add(position);
position.setAddress("阿里巴巴西溪北苑");
position.setForeignId("0151E23B1");
position.setLongitude("120.123");
position.setLatitude("30.123");
position.setOffset(100);
req.setPositionList(list);
OapiAttendanceGroupPositionsAddResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupPositionsAddRequest("https://oapi.dingtalk.com/topapi/attendance/group/positions/add")

req.op_userid="123456"
req.group_key="0151E02xxxx1A917E876"
req.position_list=""
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
$req = new OapiAttendanceGroupPositionsAddRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151E02xxxx7E876");
$position_list = new Position;
$position_list->address="阿里巴巴西溪北苑";
$position_list->foreign_id="0151E022xxxx917E876";
$position_list->longitude="120.123";
$position_list->latitude="30.123";
$position_list->offset="100";
$req->setPositionList(array($position_list));
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/positions/add");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/positions/add");
OapiAttendanceGroupPositionsAddRequest req = new OapiAttendanceGroupPositionsAddRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E02xxxx17E876";
List<OapiAttendanceGroupPositionsAddRequest.PositionDomain> list2 = new List<OapiAttendanceGroupPositionsAddRequest.PositionDomain>();
OapiAttendanceGroupPositionsAddRequest.PositionDomain obj3 = new OapiAttendanceGroupPositionsAddRequest.PositionDomain();
list2.Add(obj3);
obj3.Address = "阿里巴巴西溪北苑";
obj3.ForeignId = "0151E0xxxx917E876";
obj3.Longitude = "120.123";
obj3.Latitude = "30.123";
obj3.Offset = 100L;
req.PositionList_ = list2;
OapiAttendanceGroupPositionsAddResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DingOpenResult |  | 返回结果。 |
| result | Result |  | 查询结果。 |
| error\_info\_list | ErrorInfo[] |  | 错误列表。 |
| failure\_list | Position[] |  | 失败列表。 |
| foreign\_id | String | 0151E23B1xxxx | 业务方positionId。 |
| address | String | 阿里巴巴西溪北苑 | 地址描述。 |
| latitude | String | 120.123 | 经度(支持6位小数)。 |
| longitude | String | 30.123 | 纬度(支持6位小数)。 |
| position\_key | String |  | 位置key，失败时为空。 |
| msg | String | business fault | 错误信息。 |
| code | String | 1000 | 错误码。 |
| success\_list | Position[] |  | 成功列表。 |
| foreign\_id | String | 0151E23B1 | 业务方positionId。 |
| address | String | 阿里巴巴西溪北苑 | 地址描述。 |
| latitude | String | 120.123 | 经度(支持6位小数)。 |
| longitude | String | 30.123 | 纬度(支持6位小数)。 |
| position\_key | String | 9E459D1xxxx | position的唯一标识。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | rndx5wfzebph | 请求ID。 |

### **响应体示例**

```
{
  "result": {
    "errcode": 0,
    "errmsg" "ok",
    "result": {
      "success_list": [
        {
          "address": "阿里巴巴西溪北苑",
          "foreign_id": "0151E23B1",
          "latitude": "30.123",
          "longitude": "120.123",
          "position_key": "9E459D1xxxx"
        }
      ]
    },
    "success": true
  },
  "request_id": "rndx5wfzebph"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
