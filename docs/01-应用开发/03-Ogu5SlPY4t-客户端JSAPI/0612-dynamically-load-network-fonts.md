---
title: "动态加载网络字体"
source_url: "https://open.dingtalk.com/document/development/dynamically-load-network-fonts"
namespace: "development"
slug: "dynamically-load-network-fonts"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 界面 > 动态加载网络字体"
doc_id: "nQS6slidzF"
updated_at: "2025-09-17 20:59:48"
---

> Source: https://open.dingtalk.com/document/development/dynamically-load-network-fonts
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 界面 > 动态加载网络字体
> Updated: 2025-09-17 20:59:48

# 动态加载网络字体

调用**dd.loadFontFace**动态的加载网络字体。

## 扫码体验

![动态加载网络字体](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2211855461/p407562.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - iOS 仅支持 HTTPS 格式文件地址。
> - 钉钉小程序目前只支持 woff，otf，ttf，sfnt 字体。
> - 钉钉小程序不支持woff2字体，原因是：
>
>   - 相对其他格式字体，对内存占用较高。
>   - 此字体支持对于内核so size有较大负担，目前钉钉使用的u4内核3.0将woff2格式支持给裁剪了，导致无法正常显示，建议使用其他格式。

## 示例代码

### .axml 示例代码

```
<!-- .axml -->
<view class="page">
  <view class="page-description">动态加载网络字体</view>
  <view class="page-section">
    <view class="page-section-title">loadFontFace</view>
    <view class="page-section-demo">
      <button size="default" type="primary" onTap="loadFontFace">
        loadFontFace
      </button>
    </view>
  </view>
</view>
```

### .js示例代码

```
// .js
Page({
  data: {},
  onLoad() { },
  loadFontFace() {
    dd.loadFontFace({
      family: 'Bitstream Vera Serif Bold',
      source: 'url("https://sungd.github.io/Pacifico.ttf")',
      success() {
        dd.alert({
          title: 'loadfontface 成功!!!',
        })
      },
      fail: (err) => {
        dd.alert({
          content: JSON.stringify(err),
        })
      },
    })
  },
})
```

### .acss示例代码

```
.page{
  font-family: Bitstream Vera Serif Bold;
}
```

## 入参说明

| 属性 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| family | String | 是 | 字体名称。 |
| source | String | 是 | 字体资源地址。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |
