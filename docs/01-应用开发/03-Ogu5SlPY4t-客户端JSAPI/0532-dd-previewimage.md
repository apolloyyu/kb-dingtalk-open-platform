---
title: "预览图片"
source_url: "https://open.dingtalk.com/document/development/dd-previewimage"
namespace: "development"
slug: "dd-previewimage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 预览图片"
doc_id: "wsDVV9WSa0"
updated_at: "2025-09-17 20:58:57"
---

> Source: https://open.dingtalk.com/document/development/dd-previewimage
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 多媒体 > 图片 > 预览图片
> Updated: 2025-09-17 20:58:57

# 预览图片

调用**dd.previewImage**预览图片。

## 扫码体验

![]()![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7254199951/p163545.png)

## **示例代码**

```
dd.previewImage({
  current: 2,
  urls: [
    'https://img.alicdn.com/tps/TB1sXGYIFXXXXc5XpXXXXXXXXXX.jpg',
    'https://img.alicdn.com/tps/TB1pfG4IFXXXXc6XXXXXXXXXXXX.jpg',
    'https://img.alicdn.com/tps/TB1h9xxIFXXXXbKXXXXXXXXXXXX.jpg'
  ],
});
```

## **入参**

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| urls | String[] | 是 | 要预览的图片链接列表。 |
| current | Number | 否 | 当前显示图片索引。  **默认值****：**0。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数。 |
