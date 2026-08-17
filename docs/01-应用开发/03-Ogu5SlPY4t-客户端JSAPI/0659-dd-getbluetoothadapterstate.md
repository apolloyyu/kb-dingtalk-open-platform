---
title: "获取本机蓝牙模块状态"
source_url: "https://open.dingtalk.com/document/development/dd-getbluetoothadapterstate"
namespace: "development"
slug: "dd-getbluetoothadapterstate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取本机蓝牙模块状态"
doc_id: "14sax1wqNc"
updated_at: "2025-09-17 21:00:21"
---

> Source: https://open.dingtalk.com/document/development/dd-getbluetoothadapterstate
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 获取本机蓝牙模块状态
> Updated: 2025-09-17 21:00:21

# 获取本机蓝牙模块状态

调用**dd.getBluetoothAdapterState**获取本机蓝牙模块状态。

## **示例代码​**

```
dd.getBluetoothAdapterState({
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

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success** **返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| discovering | Boolean | 是否正在搜索设备。 |
| available | Boolean | 蓝牙模块是否可用(需支持 BLE 并且蓝牙是打开状态)。 |
