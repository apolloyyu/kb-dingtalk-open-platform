---
title: "radio 单选按钮"
source_url: "https://open.dingtalk.com/document/development/mini-app-radio-button-1"
namespace: "development"
slug: "mini-app-radio-button-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > radio 单选按钮"
doc_id: "i6GaEfNidC"
updated_at: "2025-09-17 20:58:26"
---

> Source: https://open.dingtalk.com/document/development/mini-app-radio-button-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > radio 单选按钮
> Updated: 2025-09-17 20:58:26

# radio 单选按钮

本文介绍单选按钮组件的使用。

## 在线体验

## **属性**

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| value | String | 组件值，选中时 change 事件会携带的 value。 |
| checked | Boolean | 当前是否选中。  **默认值**：false。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |

## **示例****代码**

.axml示例代码：

```
<!--page/component/radio/radio.axml -->
<view class="page">
  <view class="page-description">单选框</view>
  <view class="page-section">
    <view class="section section_gap">
      <form onSubmit="onSubmit" onReset="onReset">
        <view class="page-section-demo">
          <radio-group class="radio-group" onChange="radioChange" name="lib">
            <label class="radio" a:for="{{items}}" key="label-{{index}}">
              <radio value="{{item.name}}" checked="{{item.checked}}" disabled="{{item.disabled}}" />
              <text class="radio-text">{{item.value}}</text>
            </label>
          </radio-group>
        </view>
        <view class="page-section-btns">
          <view><button size="mini" type="ghost" formType="reset">reset</button></view>
          <view><button size="mini" type="primary" formType="submit">submit</button></view>
        </view>
      </form>
    </view>
  </view>
</view>
```

.js示例代码：

```
// page/component/radio/radio.js
Page({
  data: {
    items: [
      { name: 'angular', value: 'AngularJS' },
      { name: 'react', value: 'React', checked: true },
      { name: 'polymer', value: 'Polymer' },
      { name: 'vue', value: 'Vue.js' },
      { name: 'ember', value: 'Ember.js' },
      { name: 'backbone', value: 'Backbone.js', disabled: true },
    ],
  },
  onSubmit(e) {
    my.alert({
      content: e.detail.value.lib,
    });
    console.log('onSubmit', e.detail);
  },
  onReset(e) {
    console.log('onReset', e);
  },
  radioChange(e) {
    console.log('你选择的框架是：', e.detail.value);
  },
});
```

.acss示例代码：

```
/*page/component/radio/radio.acss */
.radio {
  display: block;
  margin-bottom: 20rpx;
}
.radio-text {
  line-height: 1.8;
}
```
