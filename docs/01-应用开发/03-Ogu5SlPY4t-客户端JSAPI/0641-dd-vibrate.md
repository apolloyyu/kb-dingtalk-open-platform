---
title: "使用振动功能"
source_url: "https://open.dingtalk.com/document/development/dd-vibrate"
namespace: "development"
slug: "dd-vibrate"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 振动 > 使用振动功能"
doc_id: "xa7f0jJuTO"
updated_at: "2025-09-17 21:00:10"
---

> Source: https://open.dingtalk.com/document/development/dd-vibrate
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 振动 > 使用振动功能
> Updated: 2025-09-17 21:00:10

# 使用振动功能

调用**dd.vibrate**使用振动功能。

## 扫码体验

![1595554033574-1 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9974382061/p172328.png)

## **示例代码**

```
Page({
  vibrate() {
    dd.vibrate({
      success: () => {
        dd.alert({ title: '振动起来了'});
      }
    });
  },
})
```
