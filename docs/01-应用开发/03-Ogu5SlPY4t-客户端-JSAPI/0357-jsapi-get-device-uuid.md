---
title: "getDeviceUUID"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-device-uuid"
namespace: "development"
slug: "jsapi-get-device-uuid"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > UUID > getDeviceUUID"
doc_id: "Yfkeghlero"
updated_at: "2025-08-27 18:07:28"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-device-uuid
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > UUID > getDeviceUUID
> Updated: 2025-08-27 18:07:28

# getDeviceUUID

调用getDeviceUUID，获取uuid。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11672) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11672) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `uuid`（string，必填）：设备uuid。

## **示例****代码**

### 默认出入参

```
dd.getDeviceUUID((res) => {
  const { uuid } = res;
});
```

`callback`返回对象示例：

```
{ "uuid": "3udbhg98ddlljokkkl" }
```
