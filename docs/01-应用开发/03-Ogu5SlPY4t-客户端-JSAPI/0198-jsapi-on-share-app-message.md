---
title: "onShareAppMessage"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-share-app-message"
namespace: "development"
slug: "jsapi-on-share-app-message"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 分享 > onShareAppMessage"
doc_id: "RJXuSrJiv7"
updated_at: "2025-08-27 18:08:12"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-share-app-message
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 分享 > onShareAppMessage
> Updated: 2025-08-27 18:08:12

# onShareAppMessage

在Page中定义onShareAppMessage函数，用来自定义该页面的分享内容。此时该页面右上角菜单中会显示分享按钮，反之不显示。

用户点击分享按钮时才会调用此事件。
此事件需要return一个Object，用于自定义分享内容。

扫码体验
![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3654199951/p163583.png)
分享卡片规范
![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8162814361/p338530.png)

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| H5 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10021) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `desc`（string）：自定义分享描述。
- `path`（string，必填）：自定义分享页面的路径，path中的自定义参数可在小程序生命周期的onLoad方法中获取（参数传递遵循http get的传参规则）。
- `imageUrl`（string）：自定义分享图片(只支持网络图片路径)。
- `fallbackUrl`（string）：可降级 H5 URL，仅适用于企业应用。当前钉钉桌面客户端不支持打开企业类小程序，配置此设置后，在桌面端访问此企业应用时，会打开fallbackUrl配置的H5 URL。
- `desktopContainerType`（string）：当前只支持 "side\_panel" ，表示在 桌面端使用 side\_panel 钉钉容器打开 fallbackUrl 。需要和 fallbackUrl 配合使用。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
Page({
  onShareAppMessage() {
    return {
      title: '小程序示例',
      desc: '小程序官方示例Demo，展示已支持的接口能力及组件。',
      path: 'page/component/component-pages/view/view?param=123',
    };
  },
});
```
