---
title: "监听发现新设备事件"
source_url: "https://open.dingtalk.com/document/development/dd-onbluetoothdevicefound"
namespace: "development"
slug: "dd-onbluetoothdevicefound"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 监听发现新设备事件"
doc_id: "XPkMceTAjO"
updated_at: "2025-09-17 21:00:26"
---

> Source: https://open.dingtalk.com/document/development/dd-onbluetoothdevicefound
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 监听发现新设备事件
> Updated: 2025-09-17 21:00:26

# 监听发现新设备事件

调用**dd.onBluetoothDeviceFound**搜索到新的蓝牙设备时触发此事件。

> **[!IMPORTANT]**
>
> - 模拟器可能无法获取 advertisData 及 RSSI ，请使用真机调试。
> - 开发者工具和 Android 上获取到的deviceId为设备 MAC 地址，iOS 上则为设备 uuid。因此deviceId不能硬编码到代码中，需要分平台处理，iOS可根据设备属性（localName/advertisData/manufacturerData等）进行动态匹配。
> - 若在 `dd.onBluetoothDeviceFound` 回调中包含了某个蓝牙设备，则此设备会添加到 `dd.getBluetoothDevices`接口获取到的数组中。

## **示例代码**

```
Page({
  onLoad() {
    this.callback = this.callback.bind(this);
    dd.onBluetoothDeviceFound(this.callback);
  },
  onUnload() {
    dd.offBluetoothDeviceFound(this.callback);
  },
  callback(res) {
    console.log(res);
  },
})
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 事件发生时回调。 |

**callback返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| devices | Array | 新搜索到的设备列表。 |

**device对象**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| name | String | 蓝牙设备名称，某些设备可能没有。 |
| deviceName(兼容旧版本) | String | 值与 name 一致。 |
| localName | String | 广播设备名称。 |
| deviceId | String | 设备 Id。 |
| RSSI | Number | 设备信号强度。 |
| advertisData | Hex String | 设备的广播内容。 |
