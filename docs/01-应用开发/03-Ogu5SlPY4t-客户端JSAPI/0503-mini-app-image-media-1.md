---
title: "Image 图片"
source_url: "https://open.dingtalk.com/document/development/mini-app-image-media-1"
namespace: "development"
slug: "mini-app-image-media-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 媒体 > Image 图片"
doc_id: "wPL00dza9u"
updated_at: "2025-09-17 20:58:31"
---

> Source: https://open.dingtalk.com/document/development/mini-app-image-media-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 媒体 > Image 图片
> Updated: 2025-09-17 20:58:31

# Image 图片

本文介绍图片组件的介绍。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| src | String | 图片地址。 |
| mode | String | 图片模式。mode 有 13 种模式，其中 4 种是缩放模式，9 种是裁剪模式。  **默认值**：scaleToFill。 |
| class | String | **默认值**：外部样式。 |
| style | String | **默认值**：内联样式。 |
| onError | HandleEvent | 当图片加载错误时触发，事件对象event.detail = {errMsg: 'something wrong'}。 |
| onLoad | HandleEvent | 图片载入完毕时触发，事件对象event.detail = {height:'图片高度px', width:'图片宽度px'}。 |

> **[!IMPORTANT]**
>
> `image` 组件默认宽度 300px、高度 225px。

## 缩放模式

| **属性** | **描述** |
| --- | --- |
| scaleToFill | 不保持纵横比缩放，使图片的宽高完全拉伸至填满 image 元素。 |
| aspectFit | 保持纵横比缩放，使图片的长边能完全显示出来。也就是说，可以完整地将图片显示出来。 |
| aspectFill | 保持纵横比缩放，只保证图片的短边能完全显示出来。也就是说，图片通常只在水平或垂直方向是完整的，另一个方向将会发生截取。 |
| widthFix | 宽度不变，高度自动变化，保持原图宽高比不变。 |

## 裁剪模式

| **属性** | **描述** |
| --- | --- |
| top | 不缩放图片，只显示顶部区域。 |
| bottom | 不缩放图片，只显示底部区域。 |
| center | 不缩放图片，只显示中间区域。 |
| left | 不缩放图片，只显示左边区域。 |
| right | 不缩放图片，只显示右边区域。 |
| top left | 不缩放图片，只显示左上边区域。 |
| top right | 不缩放图片，只显示右上边区域。 |
| bottom left | 不缩放图片，只显示左下边区域。 |
| bottom right | 不缩放图片，只显示右下边区域。 |

> **[!IMPORTANT]**
>
> 图片高度不能设置为 auto，如果需要图片高度为 auto，直接设置 mode 为 widthFix。

## 示例代码

.axml示例代码：

```
<view class="page">
  <view class="page-description">图片</view>
  <view class="page-section" a:for="{{array}}" a:for-item="item">
    <view class="page-section-title">{{item.text}}</view>
    <view class="page-section-demo" onTap="onTap">
      <image class="image"
        data-name="{{item.mode}}"
        onTap="onTap"
        mode="{{item.mode}}" src="{{src}}" onError="imageError" onLoad="imageLoad" />
    </view>
  </view>
</view>
```

.js示例代码：

```
Page({
  data: {
    array: [{
      mode: 'scaleToFill',
      text: 'scaleToFill：不保持纵横比缩放图片，使图片完全适应',
    }, {
      mode: 'aspectFit',
      text: 'aspectFit：保持纵横比缩放图片，使图片的长边能完全显示出来',
    }, {
      mode: 'aspectFill',
      text: 'aspectFill：保持纵横比缩放图片，只保证图片的短边能完全显示出来',
    }, {
      mode: 'widthFix',
      text: 'widthFix：宽度不变，高度自动变化，保持原图宽高比不变',
    }, {
      mode: 'top',
      text: 'top：不缩放图片，只显示图片的顶部区域',
    }, {
      mode: 'bottom',
      text: 'bottom：不缩放图片，只显示图片的底部区域',
    }, {
      mode: 'center',
      text: 'center：不缩放图片，只显示图片的中间区域',
    }, {
      mode: 'left',
      text: 'left：不缩放图片，只显示图片的左边区域',
    }, {
      mode: 'right',
      text: 'right：不缩放图片，只显示图片的右边边区域',
    }, {
      mode: 'top left',
      text: 'top left：不缩放图片，只显示图片的左上边区域',
    }, {
      mode: 'top right',
      text: 'top right：不缩放图片，只显示图片的右上边区域',
    }, {
      mode: 'bottom left',
      text: 'bottom left：不缩放图片，只显示图片的左下边区域',
    }, {
      mode: 'bottom right',
      text: 'bottom right：不缩放图片，只显示图片的右下边区域',
    }],
     src: './2.png',
  },
  imageError(e) {
    console.log('image 发生 error 事件，携带值为', e.detail.errMsg);
  },
  onTap(e) {
    console.log('image 发生 tap 事件', e);
  },
  imageLoad(e) {
    console.log('image 加载成功', e);
  },
});
```

.acss示例代码：

```
.page-section-demo {
  display: flex;
  justify-content: space-around;
}
.image {
  background-color: red;
  width: 100px;
  height: 100px;
}
```
