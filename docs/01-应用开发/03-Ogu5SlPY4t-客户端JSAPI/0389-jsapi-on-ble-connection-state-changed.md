---
title: "onBLEConnectionStateChanged"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-ble-connection-state-changed"
namespace: "development"
slug: "jsapi-on-ble-connection-state-changed"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 低功耗蓝牙 > onBLEConnectionStateChanged"
doc_id: "WcTLZdiQVz"
updated_at: "2025-08-27 18:07:50"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-ble-connection-state-changed
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 低功耗蓝牙 > onBLEConnectionStateChanged
> Updated: 2025-08-27 18:07:50

# onBLEConnectionStateChanged

调用onBLEConnectionStateChanged，监听低功耗蓝牙连接的错误事件，包括设备丢失，连接异常断开等。

> 为防止多次注册事件监听导致一次事件多次回调，建议每次调用on方法监听事件之前，先调用off方法，关闭之前的事件监听。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10171) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `deviceId`（string，必填）：蓝牙设备 ID。  
    
  > \* Android 上为设备 MAC 地址。  
  > \* iOS 上为设备 UUID。
- `connected`（boolean，必填）：连接目前的状态。

## **示例****代码**

### 默认出入参

```
dd.onBLEConnectionStateChanged((res) => {
  const { deviceId, connected } = res;
});
```

返回对象示例：

```
{ "deviceId": "0D9C82AD-1CC0-414D-9526-119E08D28124", "connected": true }
```
