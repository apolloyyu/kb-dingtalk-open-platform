---
title: "组件概述"
source_url: "https://open.dingtalk.com/document/development/json-card-component-overview"
namespace: "development"
slug: "json-card-component-overview"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 组件概述"
doc_id: "J5gaTQIvsc"
updated_at: "2026-09-30 10:43:22"
---

> Source: https://open.dingtalk.com/document/development/json-card-component-overview
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 组件概述
> Updated: 2026-09-30 10:43:22

# 组件概述

## **组件总览**

JSON 构建链路共提供 **47** 个组件，按用途分为基础、布局与组合、输入、展示四类。每个组件的属性与类型均由协议 Schema 定义。

## **基础组件**

| **组件** | **必填属性** |
| --- | --- |
| [文本（Text）](0004-json-card-basic-components.md#13ef02b2022od) | `id`、`text` |
| [富文本（Markdown）](0004-json-card-basic-components.md#1ce0ed5542mr8) | `id`、`content` |
| [图片（Image）](0004-json-card-basic-components.md#1533f9ee21az2) | `id`、`url` |
| [图标（Icon）](0004-json-card-basic-components.md#aa50686b032kd) | `id`、`name` |
| [分割线（Divider）](0004-json-card-basic-components.md#0b259d3bbcyiy) | `id` |
| [标签（Tag）](0004-json-card-basic-components.md#1abfa54b108o6) | `id`、`text` |
| [卡片容器（Card）](0004-json-card-basic-components.md#fe45ab0e05k5z) | `id`、`child` |
| [行（Row）](0004-json-card-basic-components.md#da352de5abcqd) | `id`、`children` |
| [行（Row）](0004-json-card-basic-components.md#da352de5abcqd) | `id`、`children` |
| [按钮（Button）](0004-json-card-basic-components.md#0672f0c8ce2ua) | `id`、`action`、`child` |

## 布局与组合组件

| **组件** | **必填属性** |
| --- | --- |
| [链接（Link）](0007-json-card-layout-and-composite-components.md#6fc7d6dd7fu3g) | `id` `text` |
| [卡片标题（CardHeader）](0007-json-card-layout-and-composite-components.md#22dc1b3c9fh0j) | `id` `title` |
| [网格布局（GridLayout）](0007-json-card-layout-and-composite-components.md#2e8867674ah11) | `id` `children` |
| [循环容器（Loop）](0007-json-card-layout-and-composite-components.md#c4d6191cf3osm) | `id` `children` |
| [层叠容器（Stack）](0007-json-card-layout-and-composite-components.md#e05adba98214e) | `id` `child` |
| [滚动容器（ScrollView）](0007-json-card-layout-and-composite-components.md#baa7978caevuk) | `id` |
| [标签页（Tabs）](0007-json-card-layout-and-composite-components.md#0e5c0574c7dpn) | `id` `tabs` |
| [列表（List）](0007-json-card-layout-and-composite-components.md#6cbb44b6del7s) | `id` `children` |
| [折叠面板（CollapsiblePanel）](0007-json-card-layout-and-composite-components.md#4b89ff4313rzs) | `id` `children` `title` |
| [分栏布局（ColumnLayout）](0007-json-card-layout-and-composite-components.md#e6899901f5kv4) | `id` `children` |
| [按钮组（ButtonGroup）](0007-json-card-layout-and-composite-components.md#b5e7269ee7luj) | `id` `buttons` |

## 输入组件

| **组件** | **必填属性** |
| --- | --- |
| [输入框（TextField）](0005-json-card-input-components.md#c8296fd29e5ch) | `id` `label` |
| [选择器（ChoicePicker）](0005-json-card-input-components.md#5dab134788dfy) | `id` `options` `value` |
| [复选框（CheckBox）](0005-json-card-input-components.md#07e4bee514w5w) | `id` `label` `value` |
| [开关（Switch）](0005-json-card-input-components.md#59784e8d932ow) | `id` |
| [日期时间（DateTimeInput）](0005-json-card-input-components.md#ce2f0937dcrgd) | `id` `value` |
| [数字输入（NumberInput）](0005-json-card-input-components.md#fb7df3ede4lxa) | `id` `value` |
| [评分（Rating）](0005-json-card-input-components.md#f4c073ea020d6) | `id` `value` |
| [滑块（Slider）](0005-json-card-input-components.md#8ffa16f477jfv) | `id` `max` `value` |
| [输入列表（InputList）](0005-json-card-input-components.md#cc7fdca66ajsl) | `id` `value` |
| [多选列表（CheckboxListMulti）](0005-json-card-input-components.md#9c4cb6646b5ko) | `id` `children` |
| [可选图片列表（CheckableImageList）](0005-json-card-input-components.md#08d00feb2065l) | `id` `images` `value` |
| [人员选择器（UserPicker）](0005-json-card-input-components.md#4bd0e4a04dtnl) | `id` `value` |
| [会话选择器（ConversationPicker）](0005-json-card-input-components.md#e8cedd2cc6b6a) | `id` `value` |
| [图片上传（ImageUpload）](0005-json-card-input-components.md#f8a9710700rs2) | `id` `value` |

## 展示组件

| **组件** | **必填属性** |
| --- | --- |
| [图片列表（ImageList）](0006-json-card-display-components.md#6f83338315h88) | `id` `images` |
| [头像（Avatar）](0006-json-card-display-components.md#ae9570575945m) | `id` |
| [头像组（AvatarGroup）](0006-json-card-display-components.md#8632318569zzf) | `id` `items` |
| [表格（Table）](0006-json-card-display-components.md#efd654cc9eeh5) | `id` `data` |
| [图表（Chart）](0006-json-card-display-components.md#feb28dcd0b6fl) | `id` `data` |
| [进度条（ProgressBar）](0006-json-card-display-components.md#b08e77c80a2tq) | `id` `value` |
| [计时（ElapsedTime）](0006-json-card-display-components.md#b2a92429814o4) | `id` |
| [倒计时（Countdown）](0006-json-card-display-components.md#2037d5ac1bes1) | `id` `endTime` |
| [视频（Video）](0006-json-card-display-components.md#7f2edf3f48qrs) | `id` `url` |
| [音频播放器（AudioPlayer）](0006-json-card-display-components.md#d88aeed1dal4t) | `id` `url` |
| [文件（File）](0006-json-card-display-components.md#bad99da332tyx) | `id` `fileName` `url` |
| [图片轮播（ImageCarousel）](0006-json-card-display-components.md#5de9582e0es4t) | `id` `items` |
