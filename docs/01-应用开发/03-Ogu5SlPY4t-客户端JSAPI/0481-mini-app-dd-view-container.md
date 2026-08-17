---
title: "view 视图容器"
source_url: "https://open.dingtalk.com/document/development/mini-app-dd-view-container"
namespace: "development"
slug: "mini-app-dd-view-container"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > view 视图容器"
doc_id: "zds657Dn0I"
updated_at: "2025-09-17 20:58:17"
---

> Source: https://open.dingtalk.com/document/development/mini-app-dd-view-container
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 视图容器 > view 视图容器
> Updated: 2025-09-17 20:58:17

# view 视图容器

本文介绍视图容器组件的使用。视图容器相当于 web 的 div 或者 react-native 的 View。

> **[!NOTE]**
>
> 对于明确指定了框架最低版本的属性，请通过 dd.canIUse 进行兼容性判断。
>
> 示例：[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)('view.onTransitionEnd')。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| disable-scroll | Boolean | 是否阻止区域内滚动页面。  **默认值**：false。 |
| hover-class | String | 点击时添加的样式类。 |
| hover-start-time | Number | 按住多久后出现点击状态，单位毫秒。 |
| hover-stay-time | Number | 松开后点击状态保留时间，单位毫秒。 |
| hidden | boolean | 是否隐藏。  **默认值**：false。 |
| class | String | 自定义样式名。 |
| style | String | 内联样式。 |
| animation | Object | 用于动画，详情请参考[创建动画实例](https://open.dingtalk.com/document/orgapp/dd-createanimation)。 |
| onTap | EventHandle | 点击。 |
| onTouchStart | EventHandle | 触摸动作开始。 |
| onTouchMove | EventHandle | 触摸后移动。 |
| onTouchEnd | EventHandle | 触摸动作结束。 |
| onTouchCancel | EventHandle | 触摸动作被打断，如来电提醒，弹窗。 |
| onLongTap | EventHandle | 长按 500ms 之后触发，触发了长按事件后进行移动将不会触发屏幕的滚动。 |
| onTransitionEnd | EventHandle | 过渡（Transition）结束时触发。  **版本**：1.21.2及以上。 |
| onAnimationIteration | EventHandle | 每开启一次新的动画过程时触发(第一不触发)。  **版本**：1.21.2及以上。 |
| onAnimationStart | EventHandle | 动画开始时触发。  **版本**：1.21.2及以上。 |
| onAnimationEnd | EventHandle | 动画结束时触发。  **版本**：1.21.2及以上。 |
| onAppear | EventHandle | 当前元素可见面积超过50%时触发。  **版本**：1.21.2及以上。 |
| onDisappear | EventHandle | 当前元素不可见面积超过50%时触发。  **版本**：1.21.2及以上。 |
| onFirstAppear | EventHandle | 当前元素不可见面积超过50%时触发。  **版本**：1.21.2及以上。 |

## 示例代码

```
<view class="post">
  <!-- hidden -->
  <view class="postUser" hidden>
    <view class="postUser__name">Jessie</view>
  </view>
  <!-- hover class -->
  <view class="postBody" hover-class="red">
    <view class="postBody__content">
      赞!
    </view>
    <view class="postBody__date">
      June 1
    </view>
  </view>
</view>
```

## 兼容性

对于明确指定了框架最低版本的属性，请通过 **dd.canIUse** 进行兼容性判断。
