---
title: "onBluetoothAdapterStateChange"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-bluetooth-adapter-state-change"
namespace: "development"
slug: "jsapi-on-bluetooth-adapter-state-change"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > onBluetoothAdapterStateChange"
doc_id: "JwzgDX1wFy"
updated_at: "2025-08-27 18:07:58"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-bluetooth-adapter-state-change
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > onBluetoothAdapterStateChange
> Updated: 2025-08-27 18:07:58

# onBluetoothAdapterStateChange

调用onBluetoothAdapterStateChange，监听本机蓝牙状态变化的事件。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10182) |

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
- `discovering`（boolean，必填）：蓝牙模块是否处于搜索状态。

## **示例****代码**

### 默认出入参

```
dd.onBluetoothAdapterStateChange((res) => {
  const { available, discovering } = res;
});
```

返回对象示例：

```
{ "available": true, "discovering": true }
```
