---
title: "使用长振动"
source_url: "https://open.dingtalk.com/document/development/dd-vibratelong"
namespace: "development"
slug: "dd-vibratelong"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 振动 > 使用长振动"
doc_id: "KNXdH6nzRo"
updated_at: "2025-09-17 21:00:11"
---

> Source: https://open.dingtalk.com/document/development/dd-vibratelong
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 振动 > 使用长振动
> Updated: 2025-09-17 21:00:11

# 使用长振动

调用dd.vibrateLong使用长振动功能。

## 扫码体验

![震动](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6380605061/p180600.png)

## 代码示例

```
Page({
  vibrateShort() {
    dd.vibrateLong({
      success: () => {
        dd.alert({ title: '长振动'});
      }
    });
  },
})
```

## 兼容性

请使用 dd.canIUse('vibrateLong') 进行可用性判断。
