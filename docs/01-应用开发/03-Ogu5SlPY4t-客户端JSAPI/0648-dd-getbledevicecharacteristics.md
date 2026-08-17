---
title: "获取蓝牙设备所有特征值"
source_url: "https://open.dingtalk.com/document/development/dd-getbledevicecharacteristics"
namespace: "development"
slug: "dd-getbledevicecharacteristics"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取蓝牙设备所有特征值"
doc_id: "WZFs7XuIKi"
updated_at: "2025-09-17 21:00:15"
---

> Source: https://open.dingtalk.com/document/development/dd-getbledevicecharacteristics
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取蓝牙设备所有特征值
> Updated: 2025-09-17 21:00:15

# 获取蓝牙设备所有特征值

调用**dd.getBLEDeviceCharacteristics**获取蓝牙设备所有特征值（characteristic）。

> **[!IMPORTANT]**
>
> 建立连接后先执行`dd.getBLEDeviceServices`与`dd.getBLEDeviceCharacteristics`
>
> 后再进行与蓝牙设备的数据交互。

## **示例代码**

```
dd.getBLEDeviceCharacteristics({
  deviceId: deviceId,
  serviceId: serviceId,
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
| deviceId | String | 是 | 蓝牙设备ID，参考 device 对象。 |
| serviceId | String | 是 | 蓝牙特征值对应 service 的 uuid。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| characteristics | Array | 设备特征值列。 |

**characteristic对象**

蓝牙设备 characteristic （特征值）信息。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| characteristicId | String | 蓝牙设备特征值的 uuid。 |
| serviceId | String | 蓝牙设备特征值对应服务的 uuid。 |
| value | Hex String | 蓝牙设备特征值对应的16进制值。 |
| properties | Object | 该特征值支持的操作类型。 |

**properties 对象**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| read | boolean | 该特征值是否支持 read 操作。 |
| write | boolean | 该特征值是否支持 write 操作。 |
| notify | boolean | 该特征值是否支持 notify 操作。 |
| indicate | boolean | 该特征值是否支持 indicate 操作。 |
