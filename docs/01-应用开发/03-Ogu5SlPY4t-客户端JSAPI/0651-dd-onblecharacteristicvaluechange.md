---
title: "监听特征值变化事件"
source_url: "https://open.dingtalk.com/document/development/dd-onblecharacteristicvaluechange"
namespace: "development"
slug: "dd-onblecharacteristicvaluechange"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 监听特征值变化事件"
doc_id: "UQPg8USVj9"
updated_at: "2025-09-17 21:00:17"
---

> Source: https://open.dingtalk.com/document/development/dd-onblecharacteristicvaluechange
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 监听特征值变化事件
> Updated: 2025-09-17 21:00:17

# 监听特征值变化事件

调用**dd.onBLECharacteristicValueChange**监听低功耗蓝牙设备的特征值变化的事件。

## **示例代码**

```
Page({
  onLoad() {
    this.callback = this.callback.bind(this);
    dd.onBLECharacteristicValueChange(this.callback);
  },
  onUnload() {
    dd.offBLECharacteristicValueChange(this.callback);
  },
  callback(res) {
    console.log(res);
  },
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| callback | Function | 是 | 事件回调函数。 |

**callback 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| deviceId | String | 蓝牙设备 id，参考 device 对象。 |
| serviceId | String | 蓝牙特征值对应 service 的 uuid。 |
| characteristicId | String | 蓝牙特征值的 uuid。 |
| value | Hex String | 特征值最新的16进制值。 |
