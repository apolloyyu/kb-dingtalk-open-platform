---
title: "使用短振动"
source_url: "https://open.dingtalk.com/document/development/dd-vibrateshort"
namespace: "development"
slug: "dd-vibrateshort"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 振动 > 使用短振动"
doc_id: "pao4FE6e8a"
updated_at: "2025-09-17 21:00:11"
---

> Source: https://open.dingtalk.com/document/development/dd-vibrateshort
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 振动 > 使用短振动
> Updated: 2025-09-17 21:00:11

# 使用短振动

调用**dd.vibrateShort**使用短振动功能。

## 扫码体验

![扫码短震动](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3300805061/p180598.png)

## 使用限制

仅在 iPhone 7 / 7 Plus 以上及 Android 机型生效。

## **示例代码**

```
Page({
  vibrateShort() {
    dd.vibrateShort({
      success: () => {
        dd.alert({ title: '短振动'});
      }
    });
  },
})
```

## 兼容性

请使用 dd.canIUse('vibrateShort') 进行可用性判断
