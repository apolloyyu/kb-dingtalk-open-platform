---
title: "progress 进度条"
source_url: "https://open.dingtalk.com/document/development/mini-app-progress-progress-bar-1"
namespace: "development"
slug: "mini-app-progress-progress-bar-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > progress 进度条"
doc_id: "3ybBNxLB11"
updated_at: "2025-09-17 20:58:21"
---

> Source: https://open.dingtalk.com/document/development/mini-app-progress-progress-bar-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 基础内容 > progress 进度条
> Updated: 2025-09-17 20:58:21

# progress 进度条

本文介绍进度条组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| percent | Float | 百分比(0~100)。 |
| show-info | Boolean | 在右侧显示百分比值。  **默认值**：false。 |
| stroke-width | Number | 线的粗细，单位 px。  **默认值**：6px。 |
| activeColor | Color | 已选择的进度条颜色。  **默认****值**：#09BB07。 |
| backgroundColor | Color | 未选择的进度条颜色。 |
| active | Boolean | 从左往右是否进行加载动画。  **默认值**：false。 |

## 示例代码

.axml示例代码：

```
<!--page/component/progress.axml -->
<view class="page">
  <view class="page-description">进度条</view>
  <view class="page-section">
    <view class="page-section-demo">
      <progress percent="20" show-info/>
      <progress percent="40" active/>
      <progress percent="60" stroke-width="10"/>
      <progress percent="80" active-Color="#6abf47" backgroundColor="#f4333c" />
    </view>
  </view>
</view>
```

.acss示例代码：

```
/*page/component/progress.acss*/
progress{
  margin-bottom: 60rpx;
}
```
