---
title: "读取蓝牙设备特征值数据"
source_url: "https://open.dingtalk.com/document/development/dd-readblecharacteristicvalue"
namespace: "development"
slug: "dd-readblecharacteristicvalue"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 读取蓝牙设备特征值数据"
doc_id: "BgANdIVgvy"
updated_at: "2025-09-17 21:00:19"
---

> Source: https://open.dingtalk.com/document/development/dd-readblecharacteristicvalue
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 读取蓝牙设备特征值数据
> Updated: 2025-09-17 21:00:19

# 读取蓝牙设备特征值数据

调用**dd.readBLECharacteristicValue**读取低功耗蓝牙设备特征值中的数据。调用后在 `dd.onBLECharacteristicValueChange()` 事件中接收数据返回。

> **[!IMPORTANT]**
>
> - 设备的特征值必须支持read才可以成功调用，具体参照 characteristic 的 properties 属性。
> - 并行多次调用读写接口存在读写失败的可能性。
> - 如果读取超时，错误码 10015，`dd.onBLECharacteristicValueChange`接口之后可能返回数据，需要接入方酌情处理。

## **示例代码**

```
dd.readBLECharacteristicValue({
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
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| characteristic | Object | 设备特征值信息。 |

**characteristic对象**

蓝牙设备characteristic(特征值)信息。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| characteristicId | String | 蓝牙设备特征值的 uuid。 |
| serviceId | String | 蓝牙设备特征值对应服务的 uuid。 |
| value | Hex String | 蓝牙设备特征值的value。 |
