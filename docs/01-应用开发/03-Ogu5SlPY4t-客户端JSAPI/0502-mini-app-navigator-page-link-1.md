---
title: "navigator 页面链接"
source_url: "https://open.dingtalk.com/document/development/mini-app-navigator-page-link-1"
namespace: "development"
slug: "mini-app-navigator-page-link-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 导航 > navigator 页面链接"
doc_id: "2EKw7rFf2F"
updated_at: "2025-09-17 20:58:30"
---

> Source: https://open.dingtalk.com/document/development/mini-app-navigator-page-link-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 导航 > navigator 页面链接
> Updated: 2025-09-17 20:58:30

# navigator 页面链接

本文介绍页面链接组件的使用。

**扫码体验**

![1593332323-04](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6380462061/p170201.png)

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| hover-class | String | 点击时附加的类。  **默认值**：none。 |
| hover-start-time | Number | 按住多长时间后出现点击状态，单位毫秒。 |
| hover-stay-time | Number | 手指松开后点击状态保留时间，单位毫秒。 |
| url | String | 应用内的跳转链接。 |
| open-type | String | 跳转方式。  **默认值**：navigate。 |

open-type 有效值：

| **属性** | **描述** |
| --- | --- |
| navigate | 对应 dd.navigateTo 的功能。 |
| redirect | 对应 dd.redirectTo 的功能。 |
| switchTab | 对应 dd.switchTab 的功能。 |
| navigateBack | 对应 dd.navigateBack 的功能。 |

## 示例代码

.axm示例代码：

```
<!-- sample.axml -->
<view class="page">
  <view class="page-description">导航栏</view>
  <navigator open-type="navigate" url="./navigate" hover-class="navigator-hover">跳转到新页面</navigator>
  <navigator open-type="redirect" url="./redirect" hover-class="navigator-hover">在当前页打开</navigator>
  <navigator open-type="switchTab" url="/page/API/index/index" hover-class="navigator-hover">跳转到另外一个 Tab - "组件"</navigator>
  <navigator open-type="reLaunch" url="/page/component/index" hover-class="navigator-hover">reLaunch</navigator>
  <navigator open-type="navigateBack" hover-class="navigator-hover">navigateBack</navigator>
</view>
```

.acss示例代码：

```
navigator {
  background-color: lightcoral;
  color: #fff;
  margin-bottom: 10rpx;
  padding: 20rpx;
  text-align: center;
}

.navigator-hover {
  background-color: lightskyblue;
  color: #fff;
}
```
