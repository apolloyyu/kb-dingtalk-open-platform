---
title: "获取当前网络状态"
source_url: "https://open.dingtalk.com/document/development/dd-getnetworktype"
namespace: "development"
slug: "dd-getnetworktype"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 网络状态 > 获取当前网络状态"
doc_id: "qvo4HFXtAl"
updated_at: "2025-09-17 21:00:07"
---

> Source: https://open.dingtalk.com/document/development/dd-getnetworktype
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 网络状态 > 获取当前网络状态
> Updated: 2025-09-17 21:00:07

# 获取当前网络状态

调用**dd.getNetworkType**获取当前网络状态。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6454199951/p163570.png)

## **示例****代码**

```
dd.getNetworkType({
    success: (res) => {
        this.setData({
          networkType: res.networkType
        });
    }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| key | String | 是 | 缓存数据的key。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| networkAvailable | Boolean | 网络是否可用。 |
| networkType | String | 网络类型值 UNKNOWN / NOTREACHABLE / WIFI / 3G / 2G / 4G / WWAN |
