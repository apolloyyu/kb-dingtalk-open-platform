---
title: "关闭蓝牙适配器"
source_url: "https://open.dingtalk.com/document/development/dd-closebluetoothadapter"
namespace: "development"
slug: "dd-closebluetoothadapter"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 关闭蓝牙适配器"
doc_id: "xMVlazI1Nj"
updated_at: "2025-09-17 21:00:21"
---

> Source: https://open.dingtalk.com/document/development/dd-closebluetoothadapter
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 蓝牙 > 关闭蓝牙适配器
> Updated: 2025-09-17 21:00:21

# 关闭蓝牙适配器

调用**dd.closeBluetoothAdapter**关闭本机蓝牙模块。

> **[!IMPORTANT]**
>
> - 调用该方法将断开所有已建立的蓝牙连接并释放系统资源。
> - 建议在结束小程序蓝牙流程时调用，与`dd.openBluetoothAdapter`成对调用。
> - 调用`dd.closeBluetoothAdapter`释放资源为异步操作，不建议使用`dd.closeBluetoothAdapter`和`dd.openBluetoothAdapter`作为异常处理流程（相当于先关闭再开启，重新初始化，效率低，易发生线程同步问题）。

## **示例代码**

```
dd.closeBluetoothAdapter({
  success: (res) => {
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
