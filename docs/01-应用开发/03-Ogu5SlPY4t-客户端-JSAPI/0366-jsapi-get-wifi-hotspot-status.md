---
title: "getWifiHotspotStatus"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-wifi-hotspot-status"
namespace: "development"
slug: "jsapi-get-wifi-hotspot-status"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 网络状态 > getWifiHotspotStatus"
doc_id: "ZAGYMoCENJ"
updated_at: "2025-08-27 18:07:34"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-wifi-hotspot-status
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 网络状态 > getWifiHotspotStatus
> Updated: 2025-08-27 18:07:34

# getWifiHotspotStatus

调用getWifiHotspotStatus，获取热点接入信息。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11665) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11665) |

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

- `ssid`（string，必填）：热点ssid。
- `macIp`（string，必填）：热点mac地址。

## **示例****代码**

### 默认出入参

```
dd.getWifiHotspotStatus({
  success: (res) => {
    const { ssid, macIp } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "ssid": "alibaba-inc", "macIp": "3c:12:aa:09" }
```
