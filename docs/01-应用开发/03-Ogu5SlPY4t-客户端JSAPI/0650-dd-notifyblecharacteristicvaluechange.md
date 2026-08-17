---
title: "设置读特征通知模式"
source_url: "https://open.dingtalk.com/document/development/dd-notifyblecharacteristicvaluechange"
namespace: "development"
slug: "dd-notifyblecharacteristicvaluechange"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 设置读特征通知模式"
doc_id: "vKZWSJJBTG"
updated_at: "2025-09-17 21:00:16"
---

> Source: https://open.dingtalk.com/document/development/dd-notifyblecharacteristicvaluechange
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 设置读特征通知模式
> Updated: 2025-09-17 21:00:16

# 设置读特征通知模式

调用**dd.notifyBLECharacteristicValueChange**启用低功耗蓝牙设备特征值变化时的notify功能。

> **[!IMPORTANT]**
>
> - 订阅操作成功后需要设备主动更新特征值的 value，才会触发`dd.onBLECharacteristicValueChange`。
> - 订阅方式效率比较高，推荐使用订阅代替 read 方式。
> - 设备的特征值必须支持 notify/indicate 才可以成功调用，具体参照 haracteristic 的 properties 属性。
> - 必须先启用 notify 才能监听到设备 characteristicValueChange 事件。

## **示例代码**

```
dd.notifyBLECharacteristicValueChange({
  deviceId: deviceId,
  serviceId: serviceId,
  characteristicId: characteristicId,
  success: (res) => {
    console.log(res)
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | String | 是 | 蓝牙设备 id，参考 device 对象。 |
| serviceId | String | 是 | 蓝牙特征值对应 service 的 uuid。 |
| characteristicId | String | 是 | 蓝牙特征值的 uuid。 |
| descriptorId | String | 否 | notify 的 descriptor 的 uuid （只有android 会用到，非必填，默认值00002902-0000-10008000-00805f9b34fb）。 |
| state | Boolean | 否 | 是否启用notify或indicate。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
