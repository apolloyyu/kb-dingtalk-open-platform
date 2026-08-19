---
title: "根据groupKey查询考勤组信息"
source_url: "https://open.dingtalk.com/document/development/queries-attendance-group-information-by-id"
namespace: "development"
slug: "queries-attendance-group-information-by-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 考勤组管理 > 根据groupKey查询考勤组信息"
doc_id: "52ZDjYcqKk"
updated_at: "2026-05-27 13:09:47"
---

> Source: https://open.dingtalk.com/document/development/queries-attendance-group-information-by-id
> Path: 应用开发 / 服务端API / 考勤 > 考勤组管理 > 根据groupKey查询考勤组信息
> Updated: 2026-05-27 13:09:47

# 根据groupKey查询考勤组信息

本接口根据考勤组groupKey查询考勤组如打卡范围、是否允许外勤打卡、外勤打卡是否需要审批等信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/attendance/group/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 4c9ebd2b1534xxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| op\_userid | String | 否 | user123 | 操作人userId。 |
| group\_key | String | 是 | 02B1Exxxx | 考勤组groupKey。  **[!NOTE]**  如果你使用的考勤组标识是group\_id，可以调用[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口将group\_id转换为group\_key。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/attendance/group/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9d319xxxx6e5f0' \
-d 'group_key=0151E0xxxx2A1A917' \
-d 'op_userid=123456'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/get");
OapiAttendanceGroupGetRequest req = new OapiAttendanceGroupGetRequest();
req.setOpUserid("123456");
req.setGroupKey("0151E022xxxxx1A917");
OapiAttendanceGroupGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAttendanceGroupGetRequest("https://oapi.dingtalk.com/topapi/attendance/group/get")

req.op_userid="123456"
req.group_key="0151E02xxxxA1A917"
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
$req = new OapiAttendanceGroupGetRequest;
$req->setOpUserid("123456");
$req->setGroupKey("0151Exxxx1A917");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/attendance/group/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/get");
OapiAttendanceGroupGetRequest req = new OapiAttendanceGroupGetRequest();
req.OpUserid = "123456";
req.GroupKey = "0151E0xxxxA1A917";
OapiAttendanceGroupGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Object |  | 考勤组信息结果。 |
| name | String | 测试考勤组1 | 考勤组名称。 |
| ext | String |  | 扩展字段，JSON格式。 |
| location\_offset | Number | 100 | 打卡范围，单位为米。  **[!NOTE]**  该字段已废弃，请以[批量查询地点](0193-batch-query-position-under-attendance-group.md)接口返回的offset为准。 |
| group\_key | String | 0151E0223B1EDDDF00DD6B7F72A1A917 | 考勤组groupKey。 |
| enable\_face\_check | Boolean | false | 是否开启笑脸打卡。   - **true**：开启 - **false**（默认）：关闭 |
| enable\_face\_beauty | Boolean | false | 是否开启美颜。   - **true**：开启 - **false**（默认）：关闭 |
| enable\_camera\_check | Boolean | false | 是否开启拍照打卡。   - **true**：开启 - **false**（默认）：关闭 |
| enable\_outside\_check | Boolean | false | 是否允许外勤打卡。   - **true**：允许 - **false**（默认）：不允许 |
| enable\_outside\_apply | Boolean | false | 外勤打卡是否需要审批。   - **true**：需要 - **false**（默认）：不需要 |
| outside\_check\_approve\_mode | Number | 0 | 外勤打卡审批模式。   - **-1**（默认）：关闭 - **0**：先审批，再打卡 - **1**：先打卡，再审批 |
| enable\_outside\_remark | Boolean | false | 外勤打卡是否需要填写备注。   - **true**：需要 - **false**（默认）：不需要 |
| enable\_outside\_camera\_check | Boolean | false | 外勤打卡是否需要拍照备注。   - **true**：需要 - **false**（默认）：不需要 |
| forbid\_hide\_outside\_address | Boolean | true | 是否禁止员工隐藏详细地址。   - **true**（默认）：禁止 - **false**：不禁止 |
| enable\_outside\_update\_normal\_check | Boolean | false | 是否允许外勤卡更新内勤卡。   - **true**：允许 - **false**（默认）：不允许 |
| enable\_trim\_distance | Boolean | false | 是否允许地点微调距离。   - **true**：允许 - **false**（默认）：不允许 |
| trim\_distance | Number | 50 | 地点微调范围，单位为米。 |
| errmsg | String | ok | 返回的错误信息描述。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 错误码。 |

### **响应体示例**

```
{
  "result":{
    "ext":"",
    "enable_camera_check":false,
    "enable_face_beauty":false,
    "outside_check_approve_mode":0,
    "forbid_hide_outside_address":true,
    "enable_face_check":false,
    "enable_outside_apply":false,
    "enable_outside_camera_check":false,
    "enable_outside_update_normal_check":false,
    "trim_distance":50,
    "enable_outside_check":false,
    "location_offset":100,
    "enable_outside_remark":false,
    "name":"测试考勤组1",
    "group_key":"0151E0223B1EDDDF00DD6B7F72A1A917",
    "enable_trim_distance":false
  },
  "errcode":0,
  "success":true,
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
