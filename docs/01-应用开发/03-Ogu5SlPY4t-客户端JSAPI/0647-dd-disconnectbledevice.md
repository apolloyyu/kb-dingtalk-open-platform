---
title: "断开蓝牙链接"
source_url: "https://open.dingtalk.com/document/development/dd-disconnectbledevice"
namespace: "development"
slug: "dd-disconnectbledevice"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 断开蓝牙链接"
doc_id: "SSJxuFSFaI"
updated_at: "2025-09-17 21:00:15"
---

> Source: https://open.dingtalk.com/document/development/dd-disconnectbledevice
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 断开蓝牙链接
> Updated: 2025-09-17 21:00:15

# **断开蓝牙链接**

调用**dd.disconnectBLEDevice**断开与低功耗蓝牙设备的连接。

> **[!IMPORTANT]**
>
> - 蓝牙连接随时可能断开，建议监听 `dd.onBLEConnectionStateChanged` 回调事件，当蓝牙设备断开时按需执行重连操作。
> - 若对未连接的设备或已断开连接的设备调用数据读写操作的接口，会返回10006错误，详见错误码，建议进行重连操作。

## **示例代码**

```
dd.disconnectBLEDevice({
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
| deviceId | String | 是 | 蓝牙设备ID。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行。 |
