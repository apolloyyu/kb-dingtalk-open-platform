---
title: "向蓝牙设备特征值中写入数据"
source_url: "https://open.dingtalk.com/document/development/dd-writeblecharacteristicvalue"
namespace: "development"
slug: "dd-writeblecharacteristicvalue"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 向蓝牙设备特征值中写入数据"
doc_id: "nIKpInRLgP"
updated_at: "2025-09-17 21:00:19"
---

> Source: https://open.dingtalk.com/document/development/dd-writeblecharacteristicvalue
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 向蓝牙设备特征值中写入数据
> Updated: 2025-09-17 21:00:19

# 向蓝牙设备特征值中写入数据

调用**dd.writeBLECharacteristicValue**向低功耗蓝牙设备特征值中写入数据。

> **[!IMPORTANT]**
>
> - 设备的特征值必须支持 write 才可以成功调用，具体参照 characteristic 的properties 属性。
> - 写入的二进制数据需要进行 hex 编码。

## **示例代码**

```
dd.writeBLECharacteristicValue({
  deviceId: deviceId,
  serviceId: serviceId,
  characteristicId: characteristicId,
  value: 'fffe',
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
| value | Hex String | 是 | 蓝牙设备特征值对应的值，16进制字符串，限制在20字节内。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
