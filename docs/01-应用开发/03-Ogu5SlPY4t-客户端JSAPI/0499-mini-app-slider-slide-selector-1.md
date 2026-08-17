---
title: "slider 滑动选择器"
source_url: "https://open.dingtalk.com/document/development/mini-app-slider-slide-selector-1"
namespace: "development"
slug: "mini-app-slider-slide-selector-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > slider 滑动选择器"
doc_id: "6PtRrkNA72"
updated_at: "2025-09-17 20:58:28"
---

> Source: https://open.dingtalk.com/document/development/mini-app-slider-slide-selector-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > slider 滑动选择器
> Updated: 2025-09-17 20:58:28

# slider 滑动选择器

本文介绍滑动选择器组件的使用。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| name | String | 组件名字，用于表单提交获取数据。 |
| min | Number | 最小值。  **默认值**：0。 |
| max | Number | 最大值。  **默认值**：100。 |
| step | Number | 步长，值必须大于 0，并可被(max - min)整除。  **默认值**：1。 |
| disabled | Boolean | 是否禁用。  **默认值**：false。 |
| value | Number | 当前取值。  **默认值**：0。 |
| show-value | Boolean | 是否显示当前 value。  **默认值**：false。 |
| activeColor | String | 已选择的颜色。  **默认值**：#108ee9。 |
| backgroundColor | String | 背景条的颜色。  **默认值**：#ddd。 |
| trackSize | Number | 轨道线条高度。  **默认值**：4。 |
| handleSize | Number | 滑块大小。  **默认值**：22。 |
| handleColor | String | 滑块填充色。  **默认值**：#fff。 |
| onChange | EventHandle | 完成一次拖动后触发，event.detail = {value: value}。 |

## 示例代码

.axml示例代码：

```
<view class="page">
  <view class="page-description">滑块</view>
  <view class="page-section">
    <view class="page-section-title">设置step</view>
    <view class="page-section-demo">
      <slider value="5" onChange="slider2change" step="5"/>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">设置最小/最大值范围</view>
    <view class="page-section-demo">
      <slider value="33" onChange="slider4change" min="25" max="50" show-value/>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">自定义样式</view>
    <view class="page-section-demo">
      <slider value="33" onChange="slider4change" min="25" max="50" show-value
      backgroundColor="#FFAA00" activeColor="#00aaee" trackSize="2" handleSize="6" handleColor="blue" />
    </view>
  </view>
</view>
```

.js示例代码：

```
const pageData = {};

for (let i = 1; i < 5; ++i) {
  (function (index) {
    pageData['slider' + index + 'change'] = function (e) {
      console.log('slider' + index + '发生 change 事件，携带值为', e.detail.value);
    };
  })(i);
}
Page(pageData);
```
