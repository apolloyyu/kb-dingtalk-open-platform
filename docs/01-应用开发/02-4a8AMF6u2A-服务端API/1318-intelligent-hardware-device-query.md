---
title: "查询设备详情"
source_url: "https://open.dingtalk.com/document/development/intelligent-hardware-device-query"
namespace: "development"
slug: "intelligent-hardware-device-query"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 智能硬件 > 设备管理 > 查询设备详情"
doc_id: "vQwNsfXJoE"
updated_at: "2026-06-03 09:53:25"
---

> Source: https://open.dingtalk.com/document/development/intelligent-hardware-device-query
> Path: 应用开发 / 服务端API / 更多开放 > 智能硬件 > 设备管理 > 查询设备详情
> Updated: 2026-06-03 09:53:25

# 查询设备详情

调用本接口查询企业下的智能硬件设备详情。通过本接口可查询企业下已接入的智能硬件设备的详细信息，包括设备基础属性、归属企业及员工等元数据。

## **接口调用说明**

该接口适用于以下典型业务场景：

- 企业IT部门对已接入的智能考勤机、会议设备等进行设备详情查看与资产管理。
- 第三方IoT平台同步钉钉企业内设备的元数据（如设备名称、序列号、MAC地址）用于系统集成。
- 智能办公管理系统根据设备ID或名称查询具体设备信息，实现精细化运维支持。

> **[!IMPORTANT]**
>
> 调用本接口前请完成对接，请填写[表单](https://ding.aliwork.com/o/dingtalk_smartdevice_interface_apply)并详细描述智能硬件接口的应用场景，以确保正常调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/device/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_smart\_device\_base-智能设备访问权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| device\_query\_vo | DeviceQueryVo | 否 |  | 设备查询对象。 |
| pk | String | 是 | pk\_01 | 产品的唯一标识。 |
| device\_name | String | 否 | 产品智能 | 设备名称，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。  **[!NOTE]**  该参数不能和`device_id`同时为空。 |
| device\_id | String | 否 | QWR45GT | 设备id，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。  **[!NOTE]**  该参数不能和`device_name`同时为空。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/device/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=048401dxxxxc53ef0' \
-d 'device_query_vo=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/query");
OapiSmartdeviceDeviceQueryRequest req = new OapiSmartdeviceDeviceQueryRequest();
DeviceQueryVo deviceQueryVo = new DeviceQueryVo();
deviceQueryVo.setPk("pk_01");
deviceQueryVo.setDeviceName("产品智能");
deviceQueryVo.setDeviceId("QWR45GT");
req.setDeviceQueryVo(deviceQueryVo);
OapiSmartdeviceDeviceQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceDeviceQueryRequest("https://oapi.dingtalk.com/topapi/smartdevice/device/query")

req.device_query_vo=""
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
$req = new OapiSmartdeviceDeviceQueryRequest;
$device_query_vo = new DeviceQueryVo;
$device_query_vo->pk="yourproductkey";
$device_query_vo->device_name="yourdevicename";
$device_query_vo->device_id="yourdeviceid";
$req->setDeviceQueryVo($device_query_vo);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/device/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/query");
OapiSmartdeviceDeviceQueryRequest req = new OapiSmartdeviceDeviceQueryRequest();
OapiSmartdeviceDeviceQueryRequest.DeviceQueryVoDomain obj1 = new OapiSmartdeviceDeviceQueryRequest.DeviceQueryVoDomain();
obj1.Pk = "yourproductkey";
obj1.DeviceName = "yourdevicename";
obj1.DeviceId = "yourdeviceid";
req.DeviceQueryVo_ = obj1;
OapiSmartdeviceDeviceQueryResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DeviceDetailVO | result | 返回结果，包含设备详细信息对象。 |
| device\_mac | String | 11.11.11.11 | 设备的MAC地址。 |
| corp\_id | String | ding9f5xxxx | 企业id。 |
| nick | String | ding | 设备的昵称。 |
| device\_id | String | QWxxxxGT | 设备的id。 |
| device\_name | String | 产品智能 | 设备名称。 |
| pk | String | pk\_01 | 产品的唯一标识。 |
| userid | String | user01 | 员工的userid。 |
| ext | String | 智能产品 | 备注信息。 |
| sn | String | sdx12xxxx23asdf | 设备序列号。 |
| success | Boolean | true | 请求是否成功。   - **true**：请求成功 - **false**：请求失败，并配合errcode返回具体错误原因 |
| errcode | Number | 0 | 返回码，表示调用结果状态。 |
| errmsg | String | ok | 返回码描述信息。 |
| request\_id | String | exz1t52e9awo | 当前请求的唯一标识ID，用于问题排查和日志追踪。 |

### **响应体示例**

```
{
  "result":{
    "nick":"ding",
    "ext":"智能产品",
    "device_mac":"11.11.11.11",
    "device_name":"产品智能",
    "device_id":"QWxxxxGT",
    "pk":"pk_01",
    "sn":"sdx12xxxxasdf",
    "corp_id":"ding9f5xxxx",
    "userid":"user01"
  },
  "errcode":0,
  "success":true,
  "request_id": "exz1t52e9awo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
