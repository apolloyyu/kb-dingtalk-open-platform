---
title: "closeBluetoothAdapter"
source_url: "https://open.dingtalk.com/document/development/jsapi-close-bluetooth-adapter"
namespace: "development"
slug: "jsapi-close-bluetooth-adapter"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "设备能力 > 蓝牙 > 传统蓝牙 > closeBluetoothAdapter"
doc_id: "nvfh2AR8dQ"
updated_at: "2025-08-27 18:07:54"
---

> Source: https://open.dingtalk.com/document/development/jsapi-close-bluetooth-adapter
> Path: 应用开发 / 客户端JSAPI / 设备能力 > 蓝牙 > 传统蓝牙 > closeBluetoothAdapter
> Updated: 2025-08-27 18:07:54

# closeBluetoothAdapter

调用closeBluetoothAdapter，关闭本机蓝牙模块。

> - 调用该方法将断开所有已建立的蓝牙连接并释放系统资源。
> - 建议在结束小程序蓝牙流程时调用，与openBluetoothAdapter成对调用。
> - 调用closeBluetoothAdapter释放资源为异步操作，不建议使用closeBluetoothAdapter和openBluetoothAdapter作为异常处理流程（相当于先关闭再开启，重新初始化，效率低，易发生线程同步问题）。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10174) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.closeBluetoothAdapter({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
