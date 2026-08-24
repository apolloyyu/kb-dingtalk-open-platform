---
title: "openBluetoothAdapter"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-bluetooth-adapter"
namespace: "development"
slug: "jsapi-open-bluetooth-adapter"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > openBluetoothAdapter"
doc_id: "BsCHwKEMax"
updated_at: "2025-08-27 18:07:58"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-bluetooth-adapter
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > openBluetoothAdapter
> Updated: 2025-08-27 18:07:58

# openBluetoothAdapter

调用openBluetoothAdapter，初始化小程序蓝牙模块，生效周期为调用openBluetoothAdapter 至调用closeBluetoothAdapter，或小程序被销毁为止。

在小程序蓝牙适配器模块生效期间，开发者可以正常调用蓝牙模块API，并会收到蓝牙模块相关的on事件回调。
小程序蓝牙模块初始化完成后，可以通过调用onBluetoothAdapterStateChange监听手机蓝牙状态的改变。

> - 在调用openBluetoothAdapterAPI之前，调用小程序其它蓝牙模块相关API，API会返回错误，参见下方错误码。
> - 在用户蓝牙未开启或者手机不支持蓝牙功能的情况下，调用openBluetoothAdapter会返回错误，参见下方错误码。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10173) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `autoClose`（boolean）：是否自动断开，默认是true。  
    
  > 表示是否在离开当前页面时自动断开蓝牙(仅对android有效)。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.openBluetoothAdapter({
  autoClose: true,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
