---
title: "解绑设备"
source_url: "https://open.dingtalk.com/document/development/unbind-a-smart-hardware-device"
namespace: "development"
slug: "unbind-a-smart-hardware-device"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 智能硬件 > 设备管理 > 解绑设备"
doc_id: "i3UdLcAf9a"
updated_at: "2026-06-03 09:53:20"
---

> Source: https://open.dingtalk.com/document/development/unbind-a-smart-hardware-device
> Path: 应用开发 / 服务端 API / 更多开放 > 智能硬件 > 设备管理 > 解绑设备
> Updated: 2026-06-03 09:53:20

# 解绑设备

调用本接口可解除智能硬件设备与企业的绑定关系。同时，解除绑定的数据可通过RDS回调开放给业务方。

## **接口调用说明**

在企业不再需要管理某台智能硬件设备时（如设备退场、更换厂商或终止合作），可通过本接口解除该设备与企业的绑定关系。解绑后，设备将无法再通过钉钉通道接收指令或上报数据，相关权限和访问控制也将同步失效。

建议在调用前确认：

- 设备当前状态是否允许解绑
- 是否已通知相关业务系统进行数据清理或归档
- RDS回调机制已配置，以便捕获解绑事件并做后续处理

> **[!IMPORTANT]**
>
> 调用本接口前请完成对接，请填写[表单](https://ding.aliwork.com/o/dingtalk_smartdevice_interface_apply)并详细描述智能硬件接口的应用场景，以确保正常调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/device/unbind |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_smart\_device\_base-智能设备访问权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| device\_unbind\_vo | DeviceUnbindVo | 否 |  | 解绑参数。 |
| pk | String | 是 | pk\_01 | 产品的唯一标识。该参数需要线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。 |
| device\_name | String | 否 | 产品智能 | 设备名称，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。  **[!NOTE]**  该参数不能和`device_id`同时为空。 |
| device\_id | String | 否 | QWR45GT | 设备id，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。  **[!NOTE]**  该参数不能和`device_name`同时为空。 |
| userid | String | 否 | user01 | 操作者userid。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/device/unbind" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0595ebxxxxa366755' \
-d 'device_unbind_vo=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/unbind");
OapiSmartdeviceDeviceUnbindRequest req = new OapiSmartdeviceDeviceUnbindRequest();
DeviceUnbindVo deviceUnbindVo = new DeviceUnbindVo();
deviceUnbindVo.setPk("pk_01");
deviceUnbindVo.setDeviceName("产品智能");
deviceUnbindVo.setDeviceId("QWR45GT");
deviceUnbindVo.setUserid("user01");
req.setDeviceUnbindVo(deviceUnbindVo);
OapiSmartdeviceDeviceUnbindResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceDeviceUnbindRequest("https://oapi.dingtalk.com/topapi/smartdevice/device/unbind")

req.device_unbind_vo=""
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
$req = new OapiSmartdeviceDeviceUnbindRequest;
$device_unbind_vo = new DeviceUnbindVo;
$device_unbind_vo->pk="yourproductkey";
$device_unbind_vo->device_name="yourdevicename";
$device_unbind_vo->device_id="yourdeviceid";
$device_unbind_vo->userid="123456";
$req->setDeviceUnbindVo($device_unbind_vo);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/device/unbind");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/unbind");
OapiSmartdeviceDeviceUnbindRequest req = new OapiSmartdeviceDeviceUnbindRequest();
OapiSmartdeviceDeviceUnbindRequest.DeviceUnbindVoDomain obj1 = new OapiSmartdeviceDeviceUnbindRequest.DeviceUnbindVoDomain();
obj1.Pk = "yourproductkey";
obj1.DeviceName = "yourdevicename";
obj1.DeviceId = "yourdeviceid";
obj1.Userid = "123456";
req.DeviceUnbindVo_ = obj1;
OapiSmartdeviceDeviceUnbindResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 请求是否成功。   - **true**：请求成功 - **false**：请求失败，并配合errcode返回具体错误原因 |
| errcode | Number | 0 | 返回码，表示调用结果状态。 |
| errmsg | String | ok | 返回码描述信息。 |
| request\_id | String | exz1t52e9awo | 当前请求的唯一标识ID，用于问题排查和日志追踪。 |

### **响应体示例**

```
{
  "errcode":0,
  "success":true,
  "request_id": "exz1t52e9awo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
