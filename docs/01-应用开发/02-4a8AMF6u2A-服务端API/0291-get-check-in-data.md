---
title: "获取部门用户签到记录"
source_url: "https://open.dingtalk.com/document/development/get-check-in-data"
namespace: "development"
slug: "get-check-in-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "签到 > 获取部门用户签到记录"
doc_id: "mYtLzfrL2y"
updated_at: "2026-05-27 17:06:34"
---

> Source: https://open.dingtalk.com/document/development/get-check-in-data
> Path: 应用开发 / 服务端API / 签到 > 获取部门用户签到记录
> Updated: 2026-05-27 17:06:34

# 获取部门用户签到记录

调用本接口，以部门维度获取员工签到记录。

## **接口调用说明**

企业可以调用本接口获取部门人员的签到记录进行统计分析，也可以基于[高德地图](http://lbs.amap.com/)API接口开发人员分布图和热力图。

> **[!NOTE]**
>
> 目前最多获取1000人以内的签到数据，如果所传部门ID及其子部门下的user超过1000，会报错。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/checkin/record |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_checkin\_read-签到数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |
| department\_id | String | 是 | 1 | 部门ID，1表示根部门，可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取dept\_id参数值。 |
| end\_time | Number | 是 | 1520956800000 | 结束时间，Unix时间戳，单位毫秒。 |
| start\_time | Number | 是 | 1520956800000 | 开始时间，开始时间，Unix时间戳，单位毫秒。  **[!NOTE]**  开始时间和结束时间的间隔不能大于45天。 |
| offset | Number | 否 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，从0开始。 |
| size | Number | 否 | 100 | 支持分页查询，与offset 参数同时设置时才生效，此参数代表分页大小，最大100。 |
| order | String | 否 | asc | 排序。   - **asc**：正序 - **desc**：倒序 |

### **请求示例**

curl

```
curl -X GET "https://oapi.dingtalk.com/checkin/record" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f044ec63-6ec6-4f51-bf22-38b76596f40a' \
-d 'department_id=1' \
-d 'end_time=1520956800000' \
-d 'offset=0' \
-d 'order=asc' \
-d 'size=100' \
-d 'start_time=1520956800000'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/checkin/record");
OapiCheckinRecordRequest req = new OapiCheckinRecordRequest();
req.setDepartmentId("1");
req.setEndTime(1520956800000L);
req.setStartTime(1520956800000L);
req.setOffset(0L);
req.setSize(100L);
req.setOrder("asc");
req.setHttpMethod("GET");
OapiCheckinRecordResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCheckinRecordRequest("https://oapi.dingtalk.com/checkin/record")

req.department_id="1"
req.end_time=1520956800000
req.start_time=1520956800000
req.offset=0
req.size=100
req.order="asc"
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

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_GET , DingTalkConstant::$FORMAT_JSON);
$req = new OapiCheckinRecordRequest;
$req->setDepartmentId("1");
$req->setEndTime("1520956800000");
$req->setStartTime("1520956800000");
$req->setOffset("0");
$req->setSize("100");
$req->setOrder("asc");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/checkin/record");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/checkin/record");
OapiCheckinRecordRequest req = new OapiCheckinRecordRequest();
req.DepartmentId = "1";
req.EndTime = 1520956800000L;
req.StartTime = 1520956800000L;
req.Offset = 0L;
req.Size = 100L;
req.Order = "asc";
req.SetHttpMethod("GET");
OapiCheckinRecordResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| data | Data[] |  | 返回结果。 |
| name | String | 杨xx | 员工姓名。 |
| userId | String | manager4220 | 员工userId，不可修改。 |
| avatar | String | https://static.dingtalk.com/media/xxxx | 头像URL。  **[!NOTE]**  如果用户没有设置头像，不返回该字段。 |
| timestamp | Number | 1599544940000 | 签到时间，不可修改。 |
| place | String | 绿城未来park | 签到地址。 |
| detailPlace | String | 杭州市五常街道 | 签到详细地址。 |
| remark | String | 拜访客户 | 签到备注。 |
| imageList | String[] | ["https://static.dingtalk.com/media/xxxx"] | 签到照片URL列表。  **[!NOTE]**  签到时上传图片，返回该字段。 |
| latitude | String | 30.286053 | 纬度。 |
| longitude | String | 120.017394 | 经度。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode": 0,
  "data": [
    {
      "detailPlace": "浙江省杭州市余杭区五常街道",
      "latitude": 30.286053,
      "name": "杨xx",
      "remark": "客户拜访",
      "place": "绿城未来park",
      "userId": "manager4220",
      "imageList": [
        "https://static.dingtalk.com/media/lADPD2eDNX5H2ljNBQDNAlA_592_1280.jpg"
      ],
      "timestamp": 1599544940000,
      "longitude": 120.017394
    }
  ],
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
