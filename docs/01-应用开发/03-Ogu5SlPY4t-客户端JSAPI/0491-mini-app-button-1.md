---
title: "button 按钮"
source_url: "https://open.dingtalk.com/document/development/mini-app-button-1"
namespace: "development"
slug: "mini-app-button-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > button 按钮"
doc_id: "7ISpKGThjh"
updated_at: "2025-09-17 20:58:24"
---

> Source: https://open.dingtalk.com/document/development/mini-app-button-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > button 按钮
> Updated: 2025-09-17 20:58:24

# button 按钮

本文介绍按钮组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| size | String | 有效值 default、mini。  **默认值**：default。 |
| open-type | String | 开放能力。 |
| type | String | 按钮的样式类型，有效值 primary、default、warn。  **默认值**：default。 |
| plain | Boolean | 是否镂空。  **默认值**：false。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |
| loading | Boolean | 按钮文字前是否带 loading 图标。  **默认值**：false。 |
| onTap | EventHandle | 点击。 |
| form-type | String | 有效值：submit、reset，用于表单组件，点击分别会触发 submit/reset 事件。 |
| hover-class | String | 按钮按下去的样式类。hover-class="none" 时表示没有点击态效果。  **默认值**：button-hover。 |
| hover-start-time | Number | 按住后多少时间后出现点击状态，单位毫秒。  **默认值**：20。 |
| hover-stay-time | Number | 手指松开后点击状态保留时间，单位毫秒。  **默认值**：70。 |

> **[!IMPORTANT]**
>
> `button-hover` 默认为 `{background-color: rgba(0, 0, 0, 0.1); opacity: 0.7;}`。

open-type 有效值:

| **值** | **说明** |
| --- | --- |
| share | 触发自定义分享，可使用[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)判断。 |

## 示例代码

.axml示例代码：

```
<!--pages/component/button .axml-->
<view class="page">
  <view class="page-description">按钮</view>
  <view class="page-section">
    <view class="page-section-title">type-primary/ghost</view>
    <view class="page-section-demo">
      <button type="primary">主要操作 Normal</button>
      <button type="primary" loading>操作</button>
      <button type="primary" disabled>主要操作 Disable</button>
      <button type="ghost">ghost操作</button>
      <button type="ghost" loading>ghost操作</button>
      <button type="ghost" disabled>ghost操作 Disable</button>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">type-default</view>
    <view class="page-section-demo">
      <button data-aspm-click="xxx">辅助操作 Normal</button>
      <button disabled>辅助操作 Disable</button>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">type-warn</view>
    <view class="page-section-demo">
      <button type="warn">警告类操作 Normal</button>
      <button type="warn" disabled>警告类操作 Disable</button>
      <button type="warn" hover-class="red">hover-red</button>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">Size</view>
    <view class="page-section-demo">
      <button size="mini" loading>提交</button>
      <button style="margin-left: 10px;" type="primary" size="mini">选项</button>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">open</view>
    <view class="page-section-demo">
      <button open-type="share">share</button>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">Form</view>
    <view class="page-section-demo">
      <form onSubmit="onSubmit" onReset="onReset">
        <button form-type="submit" type="primary">submit</button>
        <button form-type="reset">reset</button>
      </form>
    </view>
  </view>
</view>
```

.js示例代码：

```
//pages/component/button.js
Page({
  data: {},
  onSubmit() {
    my.alert({ title: 'You click submit' });
  },
  onReset() {
    my.alert({ title: 'You click reset' });
  },
});
```

.acss示例代码：

```
/*pages/component/button .acss*/
.red {
  background-color: red;
  border-color: red;
  color: #fff;
}

button + button {
  margin-top: 32rpx;
}
```
