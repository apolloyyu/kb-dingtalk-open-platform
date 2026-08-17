---
title: "input 输入框"
source_url: "https://open.dingtalk.com/document/development/mini-app-basic-components-input-box-1"
namespace: "development"
slug: "mini-app-basic-components-input-box-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > input 输入框"
doc_id: "rStT1ZMttY"
updated_at: "2025-09-17 20:58:25"
---

> Source: https://open.dingtalk.com/document/development/mini-app-basic-components-input-box-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > input 输入框
> Updated: 2025-09-17 20:58:25

# input 输入框

本文介绍输入框组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| value | String | 初始内容。 |
| name | String | 组件名字，用于表单提交获取数据。 |
| class | String | 外部样式名。 |
| style | String | 内联样式。 |
| type | String | input 的类型，有效值：text、search。  **默认值**：text。 |
| password | Boolean | 是否是密码类型。  **默认值**：false。 |
| placeholder | String | 占位符。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |
| maxlength | Number | 最大长度。  **默认值**：140。 |
| onInput | EventHandle | 键盘输入时触发input事件，event.detail = {value: value}。 |
| onConfirm | EventHandle | 点击键盘完成（Enter）时触发，event.detail = {value: value}。 |
| onFocus | EventHandle | 聚焦时触发，event.detail = {value: value}。 |
| onBlur | EventHandle | 失去焦点时触发，event.detail = {value: value}。 |

## 示例代码

.axml示例代码：

```
<!--page/component/input/input.axml-->
<view class="page">
  <view class="page-description">输入框</view>
  <view class="page-section">
    <view class="form-row">
      <view class="form-row-label">受控聚焦</view>
      <view class="form-row-content">
        <input class="input" focus="{{focus}}" onFocus="onFocus" onBlur="onBlur" placeholder="input something" />
      </view>
    </view>
    <view class="page-section-btns">
      <button size="mini" onTap="bindButtonTap">聚焦</button>
    </view>
  </view>
  <view class="page-section">
    <view class="form-row">
      <view class="form-row-label"><label for="controlled">显示输入</label></view>
      <view class="form-row-content">
        <input class="input" id="controlled" onInput="bindKeyInput" placeholder="show input content" />
      </view>
    </view>
    <view class="extra-info">你输入的是：{{inputValue}}</view>
  </view>
  <view class="page-section">
    <view class="form-row">
      <view class="form-row-label">最大长度</view>
      <view class="form-row-content">
        <input class="input" maxlength="10" placeholder="maxlength 10" />
      </view>
    </view>
    <view class="form-line" />
    <view class="form-row">
      <view class="form-row-label">收起键盘</view>
      <view class="form-row-content">
        <input class="input" onInput="bindHideKeyboard" placeholder="输入 123 自动收起键盘" />
      </view>
    </view>
    <view class="form-line" />
    <view class="form-row">
      <view class="form-row-label">输入密码</view>
      <view class="form-row-content">
        <input class="input" password type="text" placeholder="密码输入框" />
      </view>
    </view>
    <view class="form-line" />
    <view class="form-row">
      <view class="form-row-label">输入数字</view>
      <view class="form-row-content">
        <input class="input" type="number" placeholder="数字输入框" />
      </view>
    </view>
    <view class="form-line" />
    <view class="form-row">
      <view class="form-row-label">小数点键盘</view>
      <view class="form-row-content">
        <input class="input" type="digit" placeholder="带小数点的数字键盘" />
      </view>
    </view>
    <view class="form-line" />
    <view class="form-row">
      <view class="form-row-label">身份证键盘</view>
      <view class="form-row-content">
        <input class="input" type="idcard" placeholder="身份证输入键盘" />
      </view>
    </view>
  </view>
  <view class="page-section">
    <view class="page-section-title">搜索框</view>
    <view class="page-section-demo">
      <view class="search-outer">
        <input
          class="search-input"
          placeholder="搜索"
          value="{{search}}"
          onConfirm="doneSearch"
          onInput="handleSearch"
        />
        <text class="search-cancel" onTap="clearSearch">取消</text>
      </view>
    </view>
  </view>
</view>
```

.js示例代码：

```
//page/component/input/input.js
Page({
  data: {
    focus: false,
    inputValue: '',
  },
  bindButtonTap() {
    // blur 事件和这个冲突
    setTimeout(() => {
      this.onFocus();
    }, 100);
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
  bindKeyInput(e) {
    this.setData({
      inputValue: e.detail.value,
    });
  },
  bindHideKeyboard(e) {
    if (e.detail.value === '123') {
      // 收起键盘
      my.hideKeyboard();
    }
  },
  handleSearch(e) {
    console.log('search', e.detail.value);
    this.setData({
      search: e.detail.value,
    });
  },
  doneSearch() {
    console.log('doneSearch', this.data.search);
    my.hideKeyboard();
  },
  clearSearch() {
    console.log('clear search', this.data.search);
    this.setData({
      search: '',
    });
  },
});
```

.acss示例代码：

```
/*page/component/input/input.acss */
.extra-info {
  border-top: 1px solid #ddd;
  margin-left: 30rpx;
  padding: 20rpx 0;
  overflow: auto;
}
.search-outer {
  box-sizing: border-box;
  display:flex;
  height:40px;
  overflow:hidden;
  padding: 8px;
  border-bottom: 1px solid #ddd;
  background-color: #efeff4;
}
.search-outer * {
  box-sizing: border-box;
}
.search-input {
  flex:1;
  text-align: left;
  display: block;
  color: #000;
  height: 24px;
  font-size: 15px;
  background-color: #fff;
  border-color: transparent;
}
.search-input:focus + .search-cancel {
  margin-right:0;
  opacity: 1;
}
.search-cancel {
  margin-right:-40px;
  display: inline-block;
  opacity: 0;
  padding-left: 8px;
  height: 24px;
  line-height: 24px;
  font-size: 16px;
  color: #108ee9;
  text-align: right;
  transition: margin-right .3s,opacity .3s;
  transition-delay: .1s;
}
```
