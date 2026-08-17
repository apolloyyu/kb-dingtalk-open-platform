---
title: "movable-area 可移动视图区域"
source_url: "https://open.dingtalk.com/document/development/mini-app-movable-area-movable-view-area"
namespace: "development"
slug: "mini-app-movable-area-movable-view-area"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > movable-area 可移动视图区域"
doc_id: "lRj3XKG6CB"
updated_at: "2025-09-17 20:58:19"
---

> Source: https://open.dingtalk.com/document/development/mini-app-movable-area-movable-view-area
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > movable-area 可移动视图区域
> Updated: 2025-09-17 20:58:19

# movable-area 可移动视图区域

本文介绍可移动区域组件的使用。movable-area 必须设置 width 和 height 属性，不设置默认为 10px。

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| scale-area | Boolean | movable-view 设置为支持双指缩放时，设置此值可将缩放手势生效区域修改为整个 movable-area。  **默认值**：false。  **版本**：1.12.0及以上。 |

## 示例代码

.axml示例代码：

```
<!-- page/component/movable-view.axml -->
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
// page/component/movable-view.json
{
  "allowsBounceVertical": "NO"
}
```

.acss 示例代码：

```
/* page/component/movable-view.acss */
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
