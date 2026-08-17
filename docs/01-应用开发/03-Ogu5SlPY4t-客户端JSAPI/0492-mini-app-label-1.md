---
title: "label 标签"
source_url: "https://open.dingtalk.com/document/development/mini-app-label-1"
namespace: "development"
slug: "mini-app-label-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > 表单 > label 标签"
doc_id: "QMtohl9Nnl"
updated_at: "2025-09-17 20:58:24"
---

> Source: https://open.dingtalk.com/document/development/mini-app-label-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > 表单 > label 标签
> Updated: 2025-09-17 20:58:24

# label 标签

本文介绍标签组件的使用。

`label`可以用来改进表单组件的可用性，使用 `for` 属性找到对应组件的 `id`，或者将组件放在该标签下，当点击时，就会聚焦对应的组件。

`for` 优先级高于内部组件，内部有多个组件的时候默认触发第一个组件。

目前可以绑定的控件有：`<checkbox/>`，`<radio/>`，`<input/>`，`<textarea/>`。

## 在线体验

## 属性

| **属性** | **类型** | **描述** |
| --- | --- | --- |
| for | String | 绑定组件的 id。 |
| class | String | 外部样式。 |
| style | String | 内联样式。 |

## 示例代码

.axml示例代码：

```
<!--page/component/label/label.axml -->
<view class="page">
  <view class="page-section">
    <view class="page-section-title">Checkbox</view>
    <view class="page-section-demo">
      <checkbox-group>
        <view>
          <label>
            <checkbox value="AngularJS" />
            <text> AngularJS</text>
          </label>
        </view>
        <view>
          <label>
            <checkbox value="React" />
            <text> React</text>
          </label>
        </view>
      </checkbox-group>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">Radio</view>
    <view class="page-section-demo">
      <radio-group>
        <view>
          <radio id="AngularJS" value="AngularJS" />
          <label for="AngularJS">AngularJS</label>
        </view>
        <view>
          <radio id="React" value="React" />
          <label for="React">React</label>
        </view>
      </radio-group>
    </view>
  </view>

  <view class="page-section">
    <view class="page-section-title">多个 Checkbox只选中一个</view>
    <view class="page-section-demo">
      <label>
        <checkbox>选中我</checkbox>
        <checkbox>选不中</checkbox>
        <checkbox>选不中</checkbox>
        <checkbox>选不中</checkbox>
        <view>
          <text>Click Me</text>
        </view>
      </label>
    </view>
  </view>
</view>
```

.acss示例代码

```
/*page/component/label/label.acss */
checkbox-group > view,
radio-group > view {
  margin-bottom: 12rpx;
}
```
