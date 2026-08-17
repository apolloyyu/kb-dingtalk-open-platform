---
title: "搜寻附近蓝牙设备"
source_url: "https://open.dingtalk.com/document/development/dd-startbluetoothdevicesdiscovery"
namespace: "development"
slug: "dd-startbluetoothdevicesdiscovery"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 搜寻附近蓝牙设备"
doc_id: "h3OyQQnxIw"
updated_at: "2025-09-17 21:00:22"
---

> Source: https://open.dingtalk.com/document/development/dd-startbluetoothdevicesdiscovery
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 搜寻附近蓝牙设备
> Updated: 2025-09-17 21:00:22

# 搜寻附近蓝牙设备

调用**dd.startBluetoothDevicesDiscovery**开始搜寻附近的蓝牙外围设备。搜索结果将在 dd.onBluetoothDeviceFound事件中返回。

> **[!IMPORTANT]**
>
> 该操作比较耗费系统资源，请在搜索并连接到设备后调用stop方法停止搜索。

## **示例代码**

```
dd.startBluetoothDevicesDiscovery({
  services: ['fff0'],
  success: (res) => {
    console.log(res)
  },
  fail:(res) => {
  },
  complete: (res)=>{
  }
});
```

## 入参

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| services | Array | 否 | 蓝牙设备主 service 的 uuid 列表。 |
| allowDuplicatesKey | Boolean | 否 | 是否允许重复上报同一设备， 如果允许重复上报，则onBluetoothDeviceFound 方法会多次上报同一设备，但是 RSSI 值会有不同。 |
| interval | Integer | 否 | 上报设备的间隔，默认为0，意思是找到新设备立即上报，否则根据传入的间隔上报。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
