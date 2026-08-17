---
title: "获取蓝牙设备所有服务"
source_url: "https://open.dingtalk.com/document/development/dd-getbledeviceservices"
namespace: "development"
slug: "dd-getbledeviceservices"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取蓝牙设备所有服务"
doc_id: "mRxVUYIbod"
updated_at: "2025-09-17 21:00:16"
---

> Source: https://open.dingtalk.com/document/development/dd-getbledeviceservices
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取蓝牙设备所有服务
> Updated: 2025-09-17 21:00:16

# 获取蓝牙设备所有服务

调用**dd.getBLEDeviceServices**获取蓝牙设备所有服务（service）。

> **[!IMPORTANT]**
>
> 建立连接后先执行`dd.getBLEDeviceServices`与`dd.getBLEDeviceCharacteristics`
>
> 后再进行与蓝牙设备的数据交互。

## **示例代码**

```
dd.getBLEDeviceServices({
  deviceId: deviceId,
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
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| services | Array | 设备service 对象列表，详见下表特征值信息。 |

**service对象**

蓝牙设备service(服务)信息。

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| serviceId | String | 蓝牙设备服务的 uuid。 |
| isPrimary | Boolean | 该服务是否为主服务。 |
