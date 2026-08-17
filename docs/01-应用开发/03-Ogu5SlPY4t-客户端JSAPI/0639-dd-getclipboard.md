---
title: "获取系统剪贴板的内容"
source_url: "https://open.dingtalk.com/document/development/dd-getclipboard"
namespace: "development"
slug: "dd-getclipboard"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 剪切板 > 获取系统剪贴板的内容"
doc_id: "yYAYHUqZLK"
updated_at: "2025-09-17 21:00:09"
---

> Source: https://open.dingtalk.com/document/development/dd-getclipboard
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 剪切板 > 获取系统剪贴板的内容
> Updated: 2025-09-17 21:00:09

# 获取系统剪贴板的内容

调用**dd.getClipboard**获取系统剪贴板的内容。

## 扫码体验

![剪切板扫码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0899705061/p180594.png)

## **示例****代码**

```
Page({
  data: {
    text: '3.1415926',
    copy: '',
  },
  
  handlePaste() {
    dd.getClipboard({
      success: ({ text }) => {
        this.setData({ copy: text });
      },
    });
  },
});
```

## **入参**

| **参数** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success返回值**

| **名称** | 类型 | 描述 |
| --- | --- | --- |
| text | String | 剪切板数据。 |
