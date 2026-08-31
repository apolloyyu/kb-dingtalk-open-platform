---
title: "修改设备昵称"
source_url: "https://open.dingtalk.com/document/development/intelligent-hardware-device-nickname-modification"
namespace: "development"
slug: "intelligent-hardware-device-nickname-modification"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 智能硬件 > 设备管理 > 修改设备昵称"
doc_id: "de3pL4cOaZ"
updated_at: "2026-06-03 09:53:22"
---

> Source: https://open.dingtalk.com/document/development/intelligent-hardware-device-nickname-modification
> Path: 应用开发 / 服务端 API / 更多开放 > 智能硬件 > 设备管理 > 修改设备昵称
> Updated: 2026-06-03 09:53:22

# 修改设备昵称

通过此接口修改指定智能设备的显示名称（昵称）。

## **接口调用说明**

本接口适用于智能硬件设备管理系统中用户自定义设备显示名称的业务场景。例如，企业内部应用可通过该接口对已绑定的智能办公设备（如智能门禁、会议签到机等）进行个性化命名，便于管理员识别和管理。支持根据设备ID或设备名称定位目标设备，并更新其对外展示的昵称。

> **[!IMPORTANT]**
>
> 调用本接口前请完成对接，请填写[表单](https://ding.aliwork.com/o/dingtalk_smartdevice_interface_apply)并详细描述智能硬件接口的应用场景，以确保正常调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick |
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
| device\_nick\_modify\_vo | DeviceNickModifyVo | 否 |  | 昵称修改参数对象。 |
| pk | String | 是 | pk\_01 | 产品的唯一标识。该参数需要线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。 |
| device\_name | String | 否 | 产品智能 | 设备名称，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。  **[!NOTE]**  该参数不能和`device_id`同时为空。 |
| device\_id | String | 否 | QWxxxxGT | 设备id，可通过[查询设备列表](1317-intelligent-hardware-list-query.md)接口获取。  **[!NOTE]**  该参数不能和`device_name`同时为空。 |
| nick | String | 是 | newding | 新的设备昵称。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3d1f3b8xxxxf32c2210' \
-d 'device_nick_modify_vo=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick");
OapiSmartdeviceDeviceUpdatenickRequest req = new OapiSmartdeviceDeviceUpdatenickRequest();
DeviceNickModifyVo deviceNickModifyVo = new DeviceNickModifyVo();
deviceNickModifyVo.setPk("yourproductkey");
deviceNickModifyVo.setDeviceName("产品智能");
deviceNickModifyVo.setDeviceId("QWxxxxGT");
deviceNickModifyVo.setNick("newding");
req.setDeviceNickModifyVo(deviceNickModifyVo);
OapiSmartdeviceDeviceUpdatenickResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceDeviceUpdatenickRequest("https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick")

req.device_nick_modify_vo=""
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
$req = new OapiSmartdeviceDeviceUpdatenickRequest;
$device_nick_modify_vo = new DeviceNickModifyVo;
$device_nick_modify_vo->pk="yourproductkey";
$device_nick_modify_vo->device_name="yourdevicename";
$device_nick_modify_vo->device_id="yourdeviceid";
$device_nick_modify_vo->nick="newnick";
$req->setDeviceNickModifyVo($device_nick_modify_vo);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/device/updatenick");
OapiSmartdeviceDeviceUpdatenickRequest req = new OapiSmartdeviceDeviceUpdatenickRequest();
OapiSmartdeviceDeviceUpdatenickRequest.DeviceNickModifyVoDomain obj1 = new OapiSmartdeviceDeviceUpdatenickRequest.DeviceNickModifyVoDomain();
obj1.Pk = "yourproductkey";
obj1.DeviceName = "yourdevicename";
obj1.DeviceId = "yourdeviceid";
obj1.Nick = "newnick";
req.DeviceNickModifyVo_ = obj1;
OapiSmartdeviceDeviceUpdatenickResponse rsp = client.Execute(req, access_token);
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
