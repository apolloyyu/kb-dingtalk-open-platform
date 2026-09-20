---
title: "绑定设备"
source_url: "https://open.dingtalk.com/document/development/establishing-a-binding-relationship-between-intelligent-hardware-and-cloud"
namespace: "development"
slug: "establishing-a-binding-relationship-between-intelligent-hardware-and-cloud"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 智能硬件 > 设备管理 > 绑定设备"
doc_id: "Uiacv6ncSZ"
updated_at: "2026-06-03 09:53:18"
---

> Source: https://open.dingtalk.com/document/development/establishing-a-binding-relationship-between-intelligent-hardware-and-cloud
> Path: 应用开发 / 服务端 API / 更多开放 > 智能硬件 > 设备管理 > 绑定设备
> Updated: 2026-06-03 09:53:18

# 绑定设备

本接口用于与组织建立设备绑定关系。

## **接口调用说明**

调用本接口前请完成对接，请填写[表单](https://ding.aliwork.com/o/dingtalk_smartdevice_interface_apply)并详细描述智能硬件接口的应用场景，以确保正常调用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartdevice/external/bind |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_smart\_device\_bind\_write-智能设备绑定信息写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| device\_bind\_req\_vo | DeviceBindReqVo | 是 |  | 设备请求信息对象，包含设备绑定所需的所有参数。 |
| nick | String | 否 | ding | 设备昵称，可用于用户界面展示。 |
| sn | String | 是 | sdx123d123asdf | 设备序列号（SN），唯一标识一台物理设备。 |
| mac | String | 否 | 11:11:11:11:11 | MAC地址，用于网络设备识别。 |
| outid | String | 否 | 123456 | 外部设备ID  **[!NOTE]**  开发者可以自定义此字段，如123456。 |
| ext | String | 否 | ext | 扩展信息。 |
| dn | String | 是 | 产品智能 | 设备名称。 |
| pk | String | 是 | pk\_01 | 产品的唯一标识。该参数需线下提供，请发送邮件至`yuze.yl@alibaba-inc.com`，并说明调用智能硬件接口的场景描述。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartdevice/external/bind" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=caa6d0xxxxc30667' \
-d 'device_bind_req_vo=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/external/bind");
OapiSmartdeviceExternalBindRequest req = new OapiSmartdeviceExternalBindRequest();
DeviceBindReqVo bindReqVo = new DeviceBindReqVo();
bindReqVo.setNick("ding");
bindReqVo.setSn("sdx123d123asdf");
bindReqVo.setMac("11:11:11:11:11");
bindReqVo.setOutid("123456");
bindReqVo.setExt("智能产品");
bindReqVo.setDn("产品智能");
bindReqVo.setPk("pk_01");
req.setDeviceBindReqVo(bindReqVo);
OapiSmartdeviceExternalBindResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartdeviceExternalBindRequest("https://oapi.dingtalk.com/topapi/smartdevice/external/bind")

req.device_bind_req_vo=""
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
$req = new OapiSmartdeviceExternalBindRequest;
$device_bind_req_vo = new DeviceBindReqVo;
$device_bind_req_vo->nick="ding";
$device_bind_req_vo->sn="sdx123d123asdf";
$device_bind_req_vo->mac="xxx.xxx.xx.xx";
$device_bind_req_vo->outid="123456";
$device_bind_req_vo->ext="ext";
$device_bind_req_vo->dn="devicename";
$device_bind_req_vo->pk="productkey";
$req->setDeviceBindReqVo($device_bind_req_vo);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartdevice/external/bind");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartdevice/external/bind");
OapiSmartdeviceExternalBindRequest req = new OapiSmartdeviceExternalBindRequest();
OapiSmartdeviceExternalBindRequest.DeviceBindReqVoDomain obj1 = new OapiSmartdeviceExternalBindRequest.DeviceBindReqVoDomain();
obj1.Nick = "ding";
obj1.Sn = "sdx123d123asdf";
obj1.Mac = "xxx.xxx.xx.xx";
obj1.Outid = "123456";
obj1.Ext = "ext";
obj1.Dn = "devicename";
obj1.Pk = "productkey";
req.DeviceBindReqVo_ = obj1;
OapiSmartdeviceExternalBindResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DeviceBindRespVo | result | 接口调用成功后的返回结果对象 |
| device\_id | String | QWR45GT | 设备ID。 |
| success | Boolean | true | 请求是否成功。   - **true**：请求成功 - **false**：请求失败，并配合errcode返回具体错误原因 |
| errcode | Number | 0 | 返回码，表示调用结果状态。 |
| errmsg | String | ok | 返回码描述信息。 |
| request\_id | String | exz1t52e9awo | 当前请求的唯一标识ID，用于问题排查和日志追踪。 |

### **响应体示例**

```
{
  "result":{
    "device_id":"QWR45GT"
  },
  "errcode":0,
  "success":true,
  "request_id": "exz1t52e9awo"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
