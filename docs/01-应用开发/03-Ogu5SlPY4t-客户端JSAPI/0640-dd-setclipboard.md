---
title: "设置剪切板数据"
source_url: "https://open.dingtalk.com/document/development/dd-setclipboard"
namespace: "development"
slug: "dd-setclipboard"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 设备 > 剪切板 > 设置剪切板数据"
doc_id: "L7Vg7hiEja"
updated_at: "2025-09-17 21:00:09"
---

> Source: https://open.dingtalk.com/document/development/dd-setclipboard
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 设备 > 剪切板 > 设置剪切板数据
> Updated: 2025-09-17 21:00:09

# 设置剪切板数据

调用**dd.setClipboard**设置剪切板数据。

## **示例代码**

```
Page({
  data: {
    text: '3.1415926',
    copy: '',
  },

  handleCopy() {
    dd.setClipboard({
      text: this.data.text,
    });
  },
});
```

## **入参**

| **参数** | **类型** | 是否必填 | **说明** |
| --- | --- | --- | --- |
| text | String | 是 | 剪切板数据。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
