---
title: "radio-group 单项项目组"
source_url: "https://open.dingtalk.com/document/development/mini-app-radio-group-individual-project-group-1"
namespace: "development"
slug: "mini-app-radio-group-individual-project-group-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > radio-group 单项项目组"
doc_id: "adOUyz2L8S"
updated_at: "2025-09-17 20:58:26"
---

> Source: https://open.dingtalk.com/document/development/mini-app-radio-group-individual-project-group-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > radio-group 单项项目组
> Updated: 2025-09-17 20:58:26

# radio-group 单项项目组

本文介绍单项选择器组组件的使用。

单项选择器组内部由多个 radio 组成。

## 在线体验

## **属性**

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| onChange | EventHandle | 选中项发生变化时触发，`event.detail = {value: 选中项 radio 的 value}`。 |
| name | String | 组件名字，用于表单提交获取数据。 |

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
