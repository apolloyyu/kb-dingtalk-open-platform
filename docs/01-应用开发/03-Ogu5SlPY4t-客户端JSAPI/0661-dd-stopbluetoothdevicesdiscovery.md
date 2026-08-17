---
title: "停止搜寻附近的蓝牙设备"
source_url: "https://open.dingtalk.com/document/development/dd-stopbluetoothdevicesdiscovery"
namespace: "development"
slug: "dd-stopbluetoothdevicesdiscovery"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 停止搜寻附近的蓝牙设备"
doc_id: "bBf7UrpFuH"
updated_at: "2025-09-17 21:00:22"
---

> Source: https://open.dingtalk.com/document/development/dd-stopbluetoothdevicesdiscovery
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 停止搜寻附近的蓝牙设备
> Updated: 2025-09-17 21:00:22

# 停止搜寻附近的蓝牙设备

调用**dd.stopBluetoothDevicesDiscovery**停止搜寻附近的蓝牙外围设备。

## **示例代码**

```
dd.stopBluetoothDevicesDiscovery({
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
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
