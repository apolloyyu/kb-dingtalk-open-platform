---
title: "getBluetoothAdapterState"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-bluetooth-adapter-state"
namespace: "development"
slug: "jsapi-get-bluetooth-adapter-state"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > getBluetoothAdapterState"
doc_id: "NMubDhqOzk"
updated_at: "2025-08-27 18:07:55"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-bluetooth-adapter-state
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > getBluetoothAdapterState
> Updated: 2025-08-27 18:07:55

# getBluetoothAdapterState

调用getBluetoothAdapterState，获取本机蓝牙模块状态。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10175) |

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

- `available`（boolean，必填）：蓝牙模块是否可用。  
    
  > 需支持 BLE 并且蓝牙是打开状态。
- `discovering`（boolean，必填）：是否正在搜索设备。

## **示例****代码**

### 默认出入参

```
dd.getBluetoothAdapterState({
  success: (res) => {
    const { available, discovering } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "available": true, "discovering": true }
```
