---
title: "使用内置地图查看位置"
source_url: "https://open.dingtalk.com/document/development/dd-openlocation"
namespace: "development"
slug: "dd-openlocation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 位置 > 使用内置地图查看位置"
doc_id: "haiFU01FHO"
updated_at: "2025-09-17 20:59:57"
---

> Source: https://open.dingtalk.com/document/development/dd-openlocation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 位置 > 使用内置地图查看位置
> Updated: 2025-09-17 20:59:57

# 使用内置地图查看位置

调用**dd.openLocation**使用内置地图查看位置。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3454199951/p163567.png)

## **示例****代码**

```
dd.openLocation({
  longitude: '120.126293',
  latitude: '30.274653',
  name: '黄龙万科中心',
  address: '学院路77号',
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| longitude | String | 是 | 经度。 |
| latitude | String | 是 | 纬度。 |
| address | String | 是 | 地址的详细说明。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
