---
title: "显示加载提示"
source_url: "https://open.dingtalk.com/document/development/dd-showloading"
namespace: "development"
slug: "dd-showloading"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示加载提示"
doc_id: "SpIE7l2RuH"
updated_at: "2025-09-17 20:59:15"
---

> Source: https://open.dingtalk.com/document/development/dd-showloading
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 交互反馈 > 显示加载提示
> Updated: 2025-09-17 20:59:15

# 显示加载提示

调用**dd.showLoading**显示加载提示，可与dd.hideLoading配合使用。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6354199951/p163559.png)

## **示例****代码**

```
dd.showLoading({
  content: '加载中...',
});
// 设置加载时间
setTimeout(() => {
     dd.hideLoading();
}, 5000)
```

## 入参

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| content | String | 否 | loading的文字内容。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
