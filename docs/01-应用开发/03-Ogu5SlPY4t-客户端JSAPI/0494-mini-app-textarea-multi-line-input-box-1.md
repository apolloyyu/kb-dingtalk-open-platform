---
title: "textarea 多行输入框"
source_url: "https://open.dingtalk.com/document/development/mini-app-textarea-multi-line-input-box-1"
namespace: "development"
slug: "mini-app-textarea-multi-line-input-box-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > textarea 多行输入框"
doc_id: "0pvfA0qisu"
updated_at: "2025-09-17 20:58:25"
---

> Source: https://open.dingtalk.com/document/development/mini-app-textarea-multi-line-input-box-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > textarea 多行输入框
> Updated: 2025-09-17 20:58:25

# textarea 多行输入框

本文介绍多行输入框组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| name | String | 组件名字，用于表单提交获取数据。 |
| value | String | 初始内容。 |
| placeholder | String | 占位符。 |
| class | String | 样式名。 |
| style | String | 内联样式。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |
| maxlength | Number | 最大长度，当设置为-1时不限制最大长度。  **默认值**：140。 |
| focus | Boolean | 获取焦点。  **默认值**：false。 |
| auto-height | Boolean | 是否自动增高。  **默认值**：false。 |
| onInput | EventHandle | 键盘输入时触发，event.detail = {value: value}。 |
| onFocus | EventHandle | 输入框聚焦时触发 event.detail = {value: value}。 |
| onBlur | EventHandle | 输入框失去焦点时触发，event.detail = {value: value}。 |
| onConfirm | EventHandle | 点击完成时触发，event.detail = {value: value}。 |

## 示例代码

.axml示例代码：

```
<!--page/component/textarea/textarea.axml -->
<view class="page">
  <view class="page-description">文本框</view>
  <view class="page-section">
    <view class="page-section-title">受控聚焦</view>
    <view class="page-section-demo">
      <textarea focus="{{focus}}" onFocus="onFocus" onBlur="onBlur" placeholder="Please input something" />
    </view>
    <view class="page-section-btns">
      <button type="default" size="mini" onTap="bindButtonTap">聚焦</button>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">自适应高度</view>
    <view class="page-section-demo">
      <textarea onBlur="bindTextAreaBlur" auto-height placeholder="Please input something" />
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">结合表单</view>
    <form onSubmit="bindFormSubmit">
      <view class="page-section-demo">
        <textarea name="textarea" placeholder="Please input something"  />
      </view>
      <view class="page-section-btns">
        <button form-type="submit" size="mini" type="primary">提交</button>
      </view>  
    </form>
  </view>
</view>
```

.js示例代码：

```
//page/component/textarea/textarea.js
Page({
  data: {
    height: 20,
    focus: false,
  },
  bindButtonTap() {
    this.onFocus();
  },
  onFocus() {
    this.setData({
      focus: true,
    });
  },
  onBlur() {
    this.setData({
      focus: false,
    });
  },

  bindTextAreaBlur(e) {
    console.log(e.detail.value);
  },
  bindFormSubmit(e) {
    my.alert({
      content: e.detail.value.textarea,
    });
  },
}
);
```
