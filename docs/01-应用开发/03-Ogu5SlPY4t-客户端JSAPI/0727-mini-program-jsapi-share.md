---
title: "分享"
source_url: "https://open.dingtalk.com/document/development/mini-program-jsapi-share"
namespace: "development"
slug: "mini-program-jsapi-share"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 分享"
doc_id: "KMrWiYT1bR"
updated_at: "2025-09-17 21:01:07"
---

> Source: https://open.dingtalk.com/document/development/mini-program-jsapi-share
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 分享
> Updated: 2025-09-17 21:01:07

# 分享

在Page中定义**onShareAppMessage**函数，用来自定义该页面的分享内容。

如果在Page中定义了onShareAppMessage函数，此时该页面右上角菜单中会显示**分享**按钮，反之不显示。

> **[!IMPORTANT]**
>
> - 用户点击分享按钮时才会调用此事件。
> - 此事件需要return一个Object，用于自定义分享内容。

## 扫码体验

![image.png ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3654199951/p163583.png)

## 分享卡片规范

![定制化文案和图片](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8162814361/p338530.png)

## **示例****代码**

```
Page({
  onShareAppMessage() {
    return {
      title: '小程序示例',
      desc: '小程序官方示例Demo，展示已支持的接口能力及组件。',
      path: 'page/component/component-pages/view/view?param=123'
    };
  },
});
```

## 入参

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| title | String | 是 | 自定义分享标题。 |
| desc | String | 否 | 自定义分享描述。 |
| path | String | 是 | 自定义分享页面的路径，path中的自定义参数可在小程序生命周期的onLoad方法中获取（参数传递遵循http get的传参规则）。 |
| imageUrl | String | 否 | 自定义分享图片(只支持网络图片路径)。 |
| fallbackUrl | String | 否 | 可降级 H5 URL，仅适用于企业应用。当前钉钉桌面客户端不支持打开企业类小程序，配置此设置后，在桌面端访问此企业应用时，会打开fallbackUrl配置的H5 URL。 |
| desktopContainerType | String | 否 | 当前只支持 "side\_panel" ，表示在 桌面端使用 side\_panel 钉钉容器打开 fallbackUrl 。需要和 fallbackUrl 配合使用。 |
