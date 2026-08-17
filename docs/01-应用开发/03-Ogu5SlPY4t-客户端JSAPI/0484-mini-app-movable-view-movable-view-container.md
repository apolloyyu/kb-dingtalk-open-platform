---
title: "movable-view 可移动视图容器"
source_url: "https://open.dingtalk.com/document/development/mini-app-movable-view-movable-view-container"
namespace: "development"
slug: "mini-app-movable-view-movable-view-container"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > movable-view 可移动视图容器"
doc_id: "KPVKCCEBZ6"
updated_at: "2025-09-17 20:58:19"
---

> Source: https://open.dingtalk.com/document/development/mini-app-movable-view-movable-view-container
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > movable-view 可移动视图容器
> Updated: 2025-09-17 20:58:19

# movable-view 可移动视图容器

本文介绍可移动视图容器组件的使用。

**movable-view** 可移动的视图容器，在页面中可以拖拽滑动。movable-view 必须在[movable-area 可移动视图区域](https://open.dingtalk.com/document/orgapp/movable-area-movable-view-area) 组件中，并且必须是直接子节点，否则不能移动。

> **[!IMPORTANT]**
>
> - movable-view 必须设置 width 和 height 属性，不设置默认为 10px。
> - movable-view 默认为绝对定位(请不要修改)，top 和 left 属性为 0px。
> - 当 movable-view 小于 movable-area 时，movable-view 的移动范围是在 movable-area 内；当 movable-view 大于 movable-area 时，movable-view 的移动范围必须包含 movable-area （x 轴方向和 y 轴方向分开考虑）。

**扫码体验**

![可移动视图的预览地址](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5147091161/p236677.png)

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| direction | String | movable-view 的移动方向，属性值有 all、vertical、horizontal、none。  **默认值**：none。 |
| inertia | Boolean | movable-view 是否带有惯性。  **默认值**：false。  **版本**：1.20.0及以上。 |
| out-of-bounds | Boolean | 超过可移动区域后，movable-view 是否还可以移动。  **默认值**：false。  **版本**：1.20.0及以上。 |
| x | Number | 定义 x 轴方向的偏移，会换算为 left 属性，如果 x 的值不在可移动范围内，会自动移动到可移动范围。  **默认值**：0。 |
| y | Number | 定义 y 轴方向的偏移，会换算为 top 属性，如果 y 的值不在可移动范围内，会自动移动到可移动范围。  **默认值**：0。 |
| damping | Number | 阻尼系数，用于控制x或y改变时的动画和过界回弹的动画，值越大移动越快。  **默认值**：20。  **版本**：1.20.0及以上。 |
| friction | Number | 摩擦系数，用于控制惯性滑动的动画，值越大摩擦力越大，滑动越快停止；必须大于 0，否则会被设置成默认值。  **默认值**：2。  **版本**：1.20.0及以上。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |
| scale | Boolean | 是否支持双指缩放，默认缩放手势生效区域是在 movable-view 内。  **默认值**：false。  **版本**：1.20.0及以上。 |
| scale-min | Number | 定义缩放倍数最小值。  **默认值**：0.5。  **版本**：1.20.0及以上。 |
| scale-max | Number | 定义缩放倍数最大值。  **默认值**：10。  **版本**：1.20.0及以上。 |
| scale-value | Number | 定义缩放倍数，取值范围为 0.5 - 10。  **默认值**：1。  **版本**：1.20.0及以上。 |
| animation | Boolean | 是否使用动画。  **默认值**：false。  **版本**：1.20.0及以上。 |
| onTouchStart | EventHandle | 触摸动作开始，事件会向父节点传递。 |
| catchTouchStart | EventHandle | 触摸动作开始，事件仅作用于组件，不向父节点传递。 |
| onTouchMove | EventHandle | 触摸移动事件，事件会向父节点传递。 |
| catchTouchMove | EventHandle | 触摸移动事件，事件仅作用于组件，不向父节点传递。 |
| onTouchEnd | EventHandle | 触摸动作结束，事件会向父节点传递。 |
| catchTouchEnd | EventHandle | 触摸动作结束，事件仅作用于组件，不向父节点传递。 |
| onTouchCancel | EventHandle | 触摸动作被打断，如来电提醒、弹窗。 |
| onChange | EventHandle | 拖动过程中触发的事件，`event.detail = {x: x, y: y, source: source}`，其中 source 表示产生移动的原因，值可为 touch（拖动）。 |
| onChangeEnd | EventHandle | 拖动结束触发的事件`event.detail= {x: x, y: y}`。 |
| onScale | EventHandle | 缩放过程中触发的事件`event.detail = {x, y, scale`}。  **版本**：1.20.0及以上。 |

**onChange返回值detail.source**

source字段表示产生移动的原因：

| **返回值** | **说明** |
| --- | --- |
| touch | 拖动。 |
| touch-out-of-bounds | 超出移动范围。 |
| out-of-bounds | 超出移动范围后的回弹。 |
| friction | 惯性。 |
| 空字符串 | setData。 |

## 示例代码

.axml示例代码：

```
<！--page/component/movable-view.axml-->
<view class="page">
  <view class="page-description">可移动视图</view>
  <view class="page-section">
    <view class="page-section-title">movable-view区域小于movable-area</view>
    <view class="page-section-demo">
      <movable-area>
        <movable-view x="{{x}}" y="{{y}}" direction="all">movable-view</movable-view>
      </movable-area>
    </view>
    <button style="margin-left: 10px; mrigin-right: 10px;" type="primary" onTap="onButtonTap">点击移动到 (30px, 30px)</button>
  </view>
  <view class="page-section">
    <view class="page-section-title">movable-view区域大于movable-area</view>
    <view class="page-section-demo">
      <movable-area>
        <movable-view class="max" direction="all">movable-view</movable-view>
      </movable-area>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">只可以横向移动</view>
    <view class="page-section-demo">
     <movable-area>
        <movable-view direction="horizontal">
          movable-view
        </movable-view>
      </movable-area>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">只可以纵向移动</view>
    <view class="page-section-demo">
     <movable-area>
        <movable-view direction="vertical">
          movable-view
        </movable-view>
      </movable-area>
    </view>
  </view>
</view>
```

.js示例代码：

```
// page/component/movable-view.js
Page({
  data: {
    x: 0,
    y: 0,
  },
  onButtonTap() {
    const { x, y } = this.data;
    if (x === 30) {
      this.setData({
        x: x + 1,
        y: y + 1,
      });
    } else {
      this.setData({
        x: 30,
        y: 30
      });
    }
  },
});
```

.json示例代码：

```
// API-DEMO page/component/movable-view.json
{
  "allowsBounceVertical": "NO"
}
```

.acss代码示例：

```
/*page/component/movable-view.acss */
movable-area {
  height: 400rpx;
  width: 400rpx;
  margin: 50rpx 0rpx 0 50rpx;
  background-color: #ccc;
  overflow: hidden;
}

movable-view {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 200rpx;
  width: 200rpx;
  background: #108ee9;
  color: #fff;
}

.max {
  width: 600rpx;
  height: 600rpx;
}
```
