---
title: "scroll-view 可滚动视图区域"
source_url: "https://open.dingtalk.com/document/development/mini-app-scroll-view-the-scrollable-area"
namespace: "development"
slug: "mini-app-scroll-view-the-scrollable-area"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > scroll-view 可滚动视图区域"
doc_id: "QJDy9994rI"
updated_at: "2025-09-17 20:58:18"
---

> Source: https://open.dingtalk.com/document/development/mini-app-scroll-view-the-scrollable-area
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > scroll-view 可滚动视图区域
> Updated: 2025-09-17 20:58:18

# scroll-view 可滚动视图区域

本文介绍可滚动视图区域组件的使用。

> **[!IMPORTANT]**
>
> - scroll-into-view 的优先级高于 scroll-top。
> - 在滚动 scroll-view 时会阻止页面回弹，所以在 scroll-view 中滚动，是无法触发 onPullDownRefresh。

**扫码体验**

![1595559597625-03](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6153372061/p169755.png)

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| class | String | 外部样式名。 |
| style | String | 内联样式名。 |
| scroll-x | Boolean | 是否允许横向滚动。  **默认值**：false。 |
| scroll-y | Boolean | 是否允许纵向滚动。  **默认值**：false。 |
| upper-threshold | Number | 距顶部/左边多少距离时（px）触发。  **默认值**：50px。 |
| lower-threshold | Number | 距底部/右边多少距离时（px）触发。  **默认值**：50px。 |
| scroll-top | Number | 竖向滚动条位置。 |
| scroll-left | Number | 横向滚动条位置。 |
| scroll-into-view | String | 值为某个子元素的 id，滚动到该元素，元素顶部对齐滚动区域顶部。 |
| scroll-with-animation | Boolean | 是否在设置滚动条位置时使用动画过渡。  **默认值**：false。 |
| onScrollToUpper | EventHandle | 滚动到顶部/左边时触发。 |
| onScrollToLower | EventHandle | 滚动到底部/右边时触发。 |
| onScroll | EventHandle | 滚动时触发event.detail = {scrollLeft, scrollTop, scrollHeight, scrollWidth, deltaX, deltaY}。 |

> **[!IMPORTANT]**
>
> 使用竖向滚动时，需要给一个固定高度，通过 acss 设置 height。

## 示例代码

.axml示例代码：

```
<!-- page/component/scroll-view.axml -->
<view class="page">
  <view class="page-description">可滚动视图区域</view>
  <view class="page-section">
    <view class="page-section-title">vertical scroll</view>
    <view class="page-section-demo">
      <scroll-view scroll-y="{{true}}" style="height: 200px;" onScrollToUpper="upper" onScrollToLower="lower" onScroll="scroll" scroll-into-view="{{toView}}" scroll-top="{{scrollTop}}">
        <view id="blue" class="scroll-view-item bc_blue"></view>
        <view id="red"  class="scroll-view-item bc_red"></view>
        <view id="yellow" class="scroll-view-item bc_yellow"></view>
        <view id="green" class="scroll-view-item bc_green"></view>
      </scroll-view>
    </view>
    <view class="page-section-btns">
      <view onTap="tap">next</view>
      <view onTap="tapMove">move</view>
      <view onTap="scrollToTop">scrollToTop</view>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">horizontal scroll</view>
    <view class="page-section-demo">
      <scroll-view class="scroll-view_H" scroll-x="{{true}}" style="width: 100%" >
        <view id="blue2" class="scroll-view-item_H bc_blue"></view>
        <view id="red2"  class="scroll-view-item_H bc_red"></view>
        <view id="yellow2" class="scroll-view-item_H bc_yellow"></view>
        <view id="green2" class="scroll-view-item_H bc_green"></view>
      </scroll-view>
    </view>
  </view>
</view>
```

.js示例代码：

```
//page/component/scroll-view.js
const order = ['blue', 'red', 'green', 'yellow'];

Page({
  data: {
    toView: 'red',
    scrollTop: 100,
  },
  upper(e) {
    console.log(e);
  },
  lower(e) {
    console.log(e);
  },
  scroll(e) {
    this.setData({
      scrollTop: e.detail.scrollTop,
    });
  },
  scrollEnd() {

  },
  scrollToTop(e) {
    console.log(e);
    this.setData({
      scrollTop: 0,
    });
  },
  tap(e) {
    for (let i = 0; i < order.length; ++i) {
      if (order[i] === this.data.toView) {
        const next = (i + 1) % order.length;
        this.setData({
          toView: order[next],
          scrollTop: next * 200,
        });
        break;
      }
    }
  },
  tapMove() {
    this.setData({
      scrollTop: this.data.scrollTop + 10,
    });
  },
});
```

.json示例代码：

```
// page/component/scroll-view.json
{
  "defaultTitle": "Scroll View"
}
```

.acss示例代码：

```
/* page/component/swiper-view.acss */
.scroll-view_H {
  white-space: nowrap;
  display:flex;
}
.scroll-view-item {
  height: 200px;
}
.scroll-view-item_H {
  flex-shrink:0;
  flex-grow:0;
  width: 300px;
  height: 200px;
}
```
