---
title: "根据设备ID查询设备"
source_url: "https://open.dingtalk.com/document/development/the-smart-hardware-can-query-details-based-on-the-device"
namespace: "development"
slug: "the-smart-hardware-can-query-details-based-on-the-device"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 智能硬件 > 设备管理 > 根据设备ID查询设备"
doc_id: "MtJaARZ9Y9"
updated_at: "2026-06-03 09:53:27"
---

> Source: https://open.dingtalk.com/document/development/the-smart-hardware-can-query-details-based-on-the-device
> Path: 应用开发 / 服务端API / 更多开放 > 智能硬件 > 设备管理 > 根据设备ID查询设备
> Updated: 2026-06-03 09:53:27

# 根据设备ID查询设备

通过本接口，可根据设备ID查询企业下某个智能硬件设备的详细信息。

## **接口调用说明**

该接口适用于设备管理平台中根据唯一设备ID获取具体设备信息的业务场景，例如用于设备状态监控、资产管理、设备远程控制等。开发者可通过此接口实时获取设备的基本属性与配置信息，支撑企业内部智能化运维需求。

> **[!IMPORTANT]**
>
> 调用本接口前请完成对接，请填写[表单](https://ding.aliwork.com/o/dingtalk_smartdevice_interface_apply)并详细描述智能硬件接口的应用场景，以确保正常调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid |
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
| device\_query\_vo | DeviceQueryVo | 是 |  | 设备查询对象，包含查询条件。 |
| device\_id | String | 是 | QWR45GT | 设备主键ID，唯一标识一个设备，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=099161fxxxx5ac7d9' \
-d 'device_query_vo=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid");
OapiSmartdeviceDeviceQuerybyidRequest req = new OapiSmartdeviceDeviceQuerybyidRequest();
DeviceQueryVo deviceQueryVo = new DeviceQueryVo();
deviceQueryVo.setDeviceId("QWR45GT");
req.setDeviceQueryVo(deviceQueryVo);
OapiSmartdeviceDeviceQuerybyidResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceDeviceQuerybyidRequest("https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid")

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
$req = new OapiSmartdeviceDeviceQuerybyidRequest;
$device_query_vo = new DeviceQueryVo;
$device_query_vo->device_id="yourdeviceid";
$req->setDeviceQueryVo($device_query_vo);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/querybyid");
OapiSmartdeviceDeviceQuerybyidRequest req = new OapiSmartdeviceDeviceQuerybyidRequest();
OapiSmartdeviceDeviceQuerybyidRequest.DeviceQueryVoDomain obj1 = new OapiSmartdeviceDeviceQuerybyidRequest.DeviceQueryVoDomain();
obj1.DeviceId = "yourdeviceid";
req.DeviceQueryVo_ = obj1;
OapiSmartdeviceDeviceQuerybyidResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DeviceDetailVO | result | 返回结果，包含设备详细信息。 |
| device\_mac | String | 11:11:11:11:11 | 设备的MAC地址。 |
| corp\_id | String | ding9f5xxxx | 企业的Corp ID。 |
| nick | String | ding | 设备的昵称。 |
| device\_id | String | QWR45GT | 设备的ID。 |
| device\_name | String | 产品智能 | 设备名称。 |
| pk | String | pk\_01 | 产品的唯一标识。 |
| userid | String | user01 | 员工的userid。 |
| ext | String | 智能产品 | 备注信息。 |
| sn | String | sdx123d123asdf | 设备序列号。 |
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
    "device_mac":"11:11:11:11:11",
    "device_name":"产品智能",
    "device_id":"QWR45GT",
    "pk":"pk_01",
    "sn":"sdx123d123asdf",
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
