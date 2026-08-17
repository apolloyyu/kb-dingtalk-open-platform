---
title: "picker底部弹起的滚动选择器"
source_url: "https://open.dingtalk.com/document/development/mini-app-scroll-picker-that-pops-up-on-the-bottom-of-the-1"
namespace: "development"
slug: "mini-app-scroll-picker-that-pops-up-on-the-bottom-of-the-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > picker底部弹起的滚动选择器"
doc_id: "4b4xKi35Fb"
updated_at: "2025-10-13 11:59:05"
---

> Source: https://open.dingtalk.com/document/development/mini-app-scroll-picker-that-pops-up-on-the-bottom-of-the-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > picker底部弹起的滚动选择器
> Updated: 2025-10-13 11:59:05

# picker底部弹起的滚动选择器

本文介绍滚动选择器（从底部弹起）组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| range | String[] / Object[] | String[] 时表示可选择的字符串列表 Object[] 时需指定 range-key 表示可选择的字段。  **默认值**：[]。 |
| range-key | String | 当 range 是一个 Object[] 时，通过 range-key 来指定 Object 中 key 的值作为选择器显示内容。 |
| value | Number | 表示选择了 range 中的第几个（下标从 0 开始）。 |
| onChange | EventHandle | value 改变时触发，event.detail = {value: value}。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |

## 示例代码

.axml示例代码：

```
<!--page/component/picker/picker.axml -->
<view class="page">
  <view class="page-description">选择器</view>
  <view class="page-section">
    <picker onChange="bindPickerChange" value="{{index}}" range="{{array}}">
      <view class="row">
        <view class="row-title">地区选择器</view>
        <view class="row-extra">当前选择：{{array[index]}}</view>
        <image class="row-arrow" src="/image/arrowright.png" mode="aspectFill" />
      </view>
    </picker>
  </view>

  <view class="page-section">
    <picker onChange="bindObjPickerChange" value="{{arrIndex}}" range="{{objectArray}}" range-key="name">
      <view class="row">
        <view class="row-title">ObjectArray</view>
        <view class="row-extra">当前选择：{{objectArray[arrIndex].name}}</view>
        <image class="row-arrow" src="/image/arrowright.png" mode="aspectFill" />
      </view>
    </picker>
  </view>
</view>
```

.js示例代码：

```
//page/component/picker/picker.js
Page({
  data: {
    array: ['中国', '美国', '巴西', '日本'],
    objectArray: [
      {
        id: 0,
        name: '美国',
      },
      {
        id: 1,
        name: '中国',
      },
      {
        id: 2,
        name: '巴西',
      },
      {
        id: 3,
        name: '日本',
      },
    ],
    arrIndex: 0,
    index: 0
  },
  bindPickerChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value);
    this.setData({
      index: e.detail.value,
    });
  },
  bindObjPickerChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value);
    this.setData({
      arrIndex: e.detail.value,
    });
  },
});
```

.acss示例代码：

```
/* page/component/picker/picker.acss */
.date-radio {
  padding: 26rpx;
}

.date-radio label + label {
  margin-left: 20rpx;
}

.row {
  display: flex;
  align-items: center;
  padding: 0 30rpx;
}

.row-title {
  flex: 1;
  padding-top: 28rpx;
  padding-bottom: 28rpx;
  font-size: 34rpx;
  color: #000;
}

.row-extra {
  flex-basis: initial;
  font-size: 32rpx;
  color: #888;
}

.row-arrow {
  width: 32rpx;
  height: 32rpx;
  margin-left: 16rpx;
}
```
