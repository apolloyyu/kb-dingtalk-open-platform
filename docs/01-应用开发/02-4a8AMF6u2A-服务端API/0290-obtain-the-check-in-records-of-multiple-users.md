---
title: "获取用户签到记录"
source_url: "https://open.dingtalk.com/document/development/obtain-the-check-in-records-of-multiple-users"
namespace: "development"
slug: "obtain-the-check-in-records-of-multiple-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "签到 > 获取用户签到记录"
doc_id: "zX1176HtzU"
updated_at: "2026-05-27 17:06:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-check-in-records-of-multiple-users
> Path: 应用开发 / 服务端API / 签到 > 获取用户签到记录
> Updated: 2026-05-27 17:06:33

# 获取用户签到记录

调用本接口，获取用户签到记录。

## **接口调用说明**

企业可以调用本接口获取指定人员的签到记录进行统计分析，也可以基于[高德地图](http://lbs.amap.com/)API接口开发人员分布图和热力图。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/checkin/record/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid\_list | String | 是 | manager4220 | 需要查询的用户列表，最大列表长度为10。 |
| start\_time | Number | 是 | 1605437194000 | 开始时间，Unix时间戳，单位毫秒。 |
| end\_time | Number | 是 | 1605786394000 | 截止时间，单位毫秒。   - 如果是取1个人的数据，时间范围最大10天。 - 如果是取多个人的数据，时间范围最大1天。 |
| cursor | Number | 是 | 0 | 分页查询的游标，最开始可以传0。 |
| size | Number | 是 | 100 | 分页查询的每页大小，最大100。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/checkin/record/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=4a492xxxxe6a92' \
-d 'cursor=0' \
-d 'end_time=1495126861000' \
-d 'size=100' \
-d 'start_time=1494126861000' \
-d 'userid_list=zhangsan%2Clisi'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/checkin/record/get");
OapiCheckinRecordGetRequest req = new OapiCheckinRecordGetRequest();
req.setUseridList("manager4220");
req.setStartTime(1605437194000L);
req.setEndTime(1605786394000L);
req.setCursor(0L);
req.setSize(100L);
OapiCheckinRecordGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCheckinRecordGetRequest("https://oapi.dingtalk.com/topapi/checkin/record/get")

req.userid_list="zhangsan,lisi"
req.start_time=1494126861000
req.end_time=1495126861000
req.cursor=0
req.size=100
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
$req = new OapiCheckinRecordGetRequest;
$req->setUseridList("zhangsan,lisi");
$req->setStartTime("1494126861000");
$req->setEndTime("1495126861000");
$req->setCursor("0");
$req->setSize("100");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/checkin/record/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/checkin/record/get");
OapiCheckinRecordGetRequest req = new OapiCheckinRecordGetRequest();
req.UseridList = "zhangsan,lisi";
req.StartTime = 1494126861000L;
req.EndTime = 1495126861000L;
req.Cursor = 0L;
req.Size = 100L;
OapiCheckinRecordGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | PageResult |  | 返回结果。 |
| next\_cursor | Number | 100 | 下次查询的游标，为null代表没有更多的数据。 |
| page\_list | CheckinRecordVo[] |  | 签到信息。 |
| checkin\_time | Number | 1494852872446 | 签到时间，单位毫秒。 |
| image\_list | String[] | ["https://static.dingtalk.com/media/xxxx"] | 签到照片URL列表。  **[!NOTE]**  如果签到没有上传图片，不返回该字段。 |
| detail\_place | String | 杭州市余杭区五常街道 | 签到详细地址。 |
| remark | String | 备注 | 签到备注。 |
| userid | String | 080517 | 签到用户userId。 |
| place | String | 绿城未来park | 签到地址。 |
| longitude | String | 120.017394 | 签到位置经度。 |
| latitude | String | 30.286046 | 签到位置维度。 |
| visit\_user | String | 刘先生 | 签到的拜访对象，可以为外部联系人的userId或者用户自己输入的名字。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | pod643x3uywf | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": {
    "page_list": [
      {
        "checkin_time": 1599544940000,
        "detail_place": "浙江省杭州市余杭区五常街道高教路961号绿城未来park",
        "image_list": [
          "https://static.dingtalk.com/media/xxxx"
        ],
        "place": "绿城未来park",
        "remark": "客户拜访",
        "userid": "manager4220",
      }
    ]
  },
  "request_id": "pod643x3uywf"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
