---
title: "switch 单选开关"
source_url: "https://open.dingtalk.com/document/development/mini-app-switch-radio-switch-1"
namespace: "development"
slug: "mini-app-switch-radio-switch-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > switch 单选开关"
doc_id: "iu4CLigXzy"
updated_at: "2025-09-17 20:58:27"
---

> Source: https://open.dingtalk.com/document/development/mini-app-switch-radio-switch-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > switch 单选开关
> Updated: 2025-09-17 20:58:27

# switch 单选开关

本文介绍单选开关组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| name | String | 组件名字，用于表单提交获取数据。 |
| checked | Boolean | 是否选中。 |
| disabled | Boolean | 是否禁用。 |
| color | String | 组件颜色。 |
| onChange | EventHandle | checked 改变时触发，event.detail={value:checked}。 |

## 示例代码

.axml示例代码：

```
<!--page/component/switch/switch.axml -->
<view class="page">
  <view class="page-description">开关</view>
  <view class="page-section">
    <view class="page-section-demo switch-list">
      <view class="switch-item">
        <switch checked onChange="switch1Change" aria-label="{{switch1 ? 'switch opened' : 'switch closed'}}" />
      </view>
      <view class="switch-item">
        <switch onChange="switch2Change"/>
      </view>
      <view class="switch-item">
        <switch color="red" checked />
      </view>
    </view>
  </view>
</view>
```

.js示例代码：

```
//  page/component/switch/switch.js
Page({
  data: {
    switch1: true,
  },
  switch1Change(e) {
    console.log('switch1 发生 change 事件，携带值为', e.detail.value);
    this.setData({
      switch1: e.detail.value,
    });
  },
  switch2Change(e){
    console.log('switch2 发生 change 事件，携带值为', e.detail.value);
  },
});
```

.acss示例代码：

```
/* page/component/switch/switch.acss */
.switch-item + .switch-item {
  margin-top: 20rpx;
}
```
