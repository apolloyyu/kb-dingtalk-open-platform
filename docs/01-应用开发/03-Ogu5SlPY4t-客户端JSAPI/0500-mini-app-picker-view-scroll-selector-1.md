---
title: "picker view 滚动选择器"
source_url: "https://open.dingtalk.com/document/development/mini-app-picker-view-scroll-selector-1"
namespace: "development"
slug: "mini-app-picker-view-scroll-selector-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > picker view 滚动选择器"
doc_id: "BzTPcTsJIQ"
updated_at: "2025-09-17 20:58:29"
---

> Source: https://open.dingtalk.com/document/development/mini-app-picker-view-scroll-selector-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > picker view 滚动选择器
> Updated: 2025-09-17 20:58:29

# picker view 滚动选择器

本文介绍滚动选择器（嵌入页面内）的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| value | Number Array | 数字表示 picker-view-column 中对应的 index （从 0 开始）。 |
| indicatorStyle | String | 选中框样式。 |
| onChange | EventHandle | 滚动选择 value 改变时触发，event.detail = {value: value}；value为数组，表示 picker-view 内的 picker-view-column index 索引，从 0 开始。 |

> **[!IMPORTANT]**
>
> 其中只可放置组件，其他节点不会显示。该组件请勿放入 hidden 或 display none 的节点内部，需要隐藏请用 a:if 切换。

不推荐：

```
<view hidden><picker-view/></view>
```

推荐：

```
<view a:if="{{xx}}"><picker-view/></view>
```

## 示例代码

.axml示例代码：

```
<view class="pv-container">
  <view class="pv-left">
    <picker-view value="{{value}}" onChange="onChange">
      <picker-view-column>
        <view>2013</view>
        <view>2014</view>
      </picker-view-column>
      <picker-view-column>
        <view>春</view>
        <view>夏</view>
      </picker-view-column>
    </picker-view>
  </view>
  <view class="pv-right">
    {{value}}
  </view>
</view>
```

.js示例代码：

```
Page({
  data: {},
  onChange(e) {
    console.log(e.detail.value);
    this.setData({
      value: e.detail.value,
    });
  },
});
```
