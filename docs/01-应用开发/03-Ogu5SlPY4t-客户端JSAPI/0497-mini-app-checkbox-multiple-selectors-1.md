---
title: "checkbox 多项选择器"
source_url: "https://open.dingtalk.com/document/development/mini-app-checkbox-multiple-selectors-1"
namespace: "development"
slug: "mini-app-checkbox-multiple-selectors-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > checkbox 多项选择器"
doc_id: "E79B2CCYXu"
updated_at: "2025-09-17 20:58:27"
---

> Source: https://open.dingtalk.com/document/development/mini-app-checkbox-multiple-selectors-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > checkbox 多项选择器
> Updated: 2025-09-17 20:58:27

# checkbox 多项选择器

本文介绍多项选择器组件的使用。

## 在线体验

## 属性

多选项目。

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| value | String | 组件值，选中时 change 事件会携带的 value。 |
| checked | Boolean | 当前是否选中，可用来设置默认选中。  **默认****值**：false。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |
| onChange | EventHandle | 组件发生改变时触发，detail = {value: 该 checkbox 是否 checked}。 |

## **示例****代码**

.axml示例代码：

```
<!-- page/component/checkbox/checkbox.js -->
<view class="page">
  <view class="page-description">多项选择器</view>
  <form onSubmit="onSubmit" onReset="onReset">
    <view class="page-section">
      <view class="page-section-title">选择你用过的框架：</view>
      <view class="page-section-demo">
        <checkbox-group onChange="onChange" name="libs">
          <label class="checkbox" a:for="{{items}}" key="label-{{index}}">
            <checkbox value="{{item.name}}" checked="{{item.checked}}" disabled="{{item.disabled}}" />
            <text class="checkbox-text">{{item.value}}</text>
          </label>
        </checkbox-group>
      </view>
      <view class="page-section-btns">
        <view><button type="ghost" size="mini" formType="reset">reset</button></view>
        <view><button type="primary" size="mini" formType="submit">submit</button></view>
      </view>
    </view>
  </form>
</view>
```

.js示例代码：

```
//  page/component/checkbox/checkbox.js
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
    console.log('onSubmit', e);
    my.alert({
      content: `你选择的框架是 ${e.detail.value.libs.join(', ')}`,
    });
  },
  onReset(e) {
    console.log('onReset', e);
  },
  onChange(e) {
    console.log(e);
  },
});
```

.acss示例代码：

```
/*page/component/checkbox/checkbox.acss */
.checkbox {
  display: block;
  margin-bottom: 20rpx;
}

button + button {
  margin-top: 32rpx;
}

.checkbox-text {
  font-size:34rpx;
  line-height: 1.2;
}
```
