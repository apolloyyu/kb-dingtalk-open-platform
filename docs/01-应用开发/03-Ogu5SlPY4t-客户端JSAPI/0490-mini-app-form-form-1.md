---
title: "form 表单"
source_url: "https://open.dingtalk.com/document/development/mini-app-form-form-1"
namespace: "development"
slug: "mini-app-form-form-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > form 表单"
doc_id: "2OSYBJ9kJ2"
updated_at: "2025-09-17 20:58:23"
---

> Source: https://open.dingtalk.com/document/development/mini-app-form-form-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > form 表单
> Updated: 2025-09-17 20:58:23

# form 表单

本文介绍表单组件的使用。

表单用于将组件内的用户输入的 `<textarea>`、 `<switch/>`、 `<input/>` 、`<checkbox-group/>`、`<slider/>`、`<radio-group/>`、`<picker/>` 等组件提交。

当点击 `form` 表单中 `formType` 为 `submit` 的 `button` 组件时，会将表单组件中的 `value` 值进行提交，需要在表单组件中加上 `name` 来作为 `key`。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| onSubmit | EventHandle | 携带 form 中的数据触发 submit 事件event.detail = {value : {'name': 'value'}}。 |
| onReset | EventHandle | 表单重置时会触发 reset 事件。 |
| class | String | 外部样式名。 |
| style | String | 内联样式。 |

## 示例代码

.axml示例代码：

```
<!-- page/component/form/form.axml -->
<view class="page">
  <view class="page-description">表单</view>
  <form onSubmit="onSubmit" onReset="onReset">
    <view class="page-section">
      <view class="page-section-title">Slider</view>
      <view class="page-section-demo">
        <slider value="80" name="slider" show-value />
      </view>
    </view>
    <view class="page-section">
      <view class="form-row">
        <view class="form-row-label">Switch</view>
        <view class="form-row-content" style="text-align: right">
          <switch name="switch" />
        </view>
      </view>
      <view class="form-line" />
      <view class="form-row">
        <view class="form-row-label">Input</view>
        <view class="form-row-content">
          <input name="input" class="input" placeholder="input something" />
        </view>
      </view>
    </view>
    <view class="page-section">
      <view class="page-section-title">Radio</view>
      <view class="page-section-demo">
        <radio-group name="radio-group">
          <label><radio value="radio1" />radio1</label>
          <label><radio value="radio2" />radio2</label>
        </radio-group>
      </view>
    </view>
    <view class="page-section">
      <view class="page-section-title">Checkbox</view>
      <view class="page-section-demo">
        <checkbox-group name="checkbox">
          <label><checkbox value="checkbox1" />checkbox1</label>
          <label><checkbox value="checkbox2" />checkbox2</label>
        </checkbox-group>
      </view>
      <view class="page-section-btns">
        <view><button type="ghost" size="mini" formType="reset">Reset</button></view>
        <view><button type="primary" size="mini" data-id="121" formType="submit">Submit</button></view>
      </view>
    </view>
  </form>
</view>
```

.js示例代码：

```
//page/component/form/form.js
Page({
  formSubmit: function(e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
  },
  formReset: function() {
    console.log('form发生了reset事件')
  }
})
```

.acss示例代码：

```
/*page/component/form/form.acss */
button + button {
  margin-top: 32rpx;
}
```
