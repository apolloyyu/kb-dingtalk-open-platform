---
title: "icon 图标"
source_url: "https://open.dingtalk.com/document/development/mini-app-icon-1"
namespace: "development"
slug: "mini-app-icon-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > icon 图标"
doc_id: "KyZlUq7SRZ"
updated_at: "2025-09-17 20:58:21"
---

> Source: https://open.dingtalk.com/document/development/mini-app-icon-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > icon 图标
> Updated: 2025-09-17 20:58:21

# icon 图标

本文介绍图标组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| type | String | icon 类型，有效值： info、warn、waiting、cancel、download、search、clear、success、success\_no\_circle。 |
| size | Number | icon 大小，单位px。  **默认值**：23。 |
| color | Color | icon 颜色，同 css 的 color。 |

## 示例代码

.axml示例代码：

```
<!--page/component/icon.axml-->
<view class="page">
  <view class="page-description">图标</view>
  <view class="page-section">
    <view class="page-section-title">Type</view>
    <view class="page-section-demo icon-list">
      <block a:for="{{iconType}}">
        <view class="item">
          <icon type="{{item}}" size="45"/>
          <text>{{item}}</text>
        </view>
      </block>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">Size</view>
    <view class="page-section-demo icon-list">
      <block a:for="{{iconSize}}">
        <view class="item">
          <icon type="success" size="{{item}}"/>
          <text>{{item}}</text>
        </view>
      </block>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">Color</view>
    <view class="page-section-demo icon-list">
      <block a:for="{{iconColor}}">
        <view class="item">
          <icon type="success" size="45" color="{{item}}"/>
          <text style="color:{{item}}">{{item}}</text>
        </view>
      </block>
    </view>
  </view>
</view>>
</block>
```

.js示例代码：

```
//page/component/icon.js
Page({
  data: {
    iconSize: [20, 30, 40, 50, 60],
    iconColor: [
      'red', 'yellow', 'blue', 'green',
    ],
    iconType: [
      'success',
      'info',
      'warn',
      'waiting',
      'clear',
      'success_no_circle',
      'download',
      'cancel',
      'search',
    ],
  },
});
```

.acss示例代码：

```
/*page/component/icon.acss*/
.icon-list {
  display: -webkit-flex;
  display: flex;
  -webkit-flex-wrap: wrap;
  flex-wrap: wrap;
}

.item {
  display: -webkit-flex;
  display: flex;
  flex-direction: column;
  -webkit-flex-direction: column;
  margin-bottom: 10px;
  margin-right: 10px;
  align-items: center;
  -webkit-align-items: center;
}
```
