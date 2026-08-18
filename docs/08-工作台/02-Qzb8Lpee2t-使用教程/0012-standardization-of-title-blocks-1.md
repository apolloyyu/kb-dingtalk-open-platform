---
title: "标题栏的标准化"
source_url: "https://open.dingtalk.com/document/dingstart/standardization-of-title-blocks-1"
namespace: "dingstart"
slug: "standardization-of-title-blocks-1"
group: "工作台"
tab: "使用教程"
breadcrumb: "组件教程 > 全码组件 > 场景示例"
doc_id: "LuDZwLxoS7"
updated_at: "2025-09-03 15:57:08"
---

> Source: https://open.dingtalk.com/document/dingstart/standardization-of-title-blocks-1
> Path: 工作台 / 使用教程 / 组件教程 > 全码组件 > 场景示例
> Updated: 2025-09-03 15:57:08

# 标题栏的标准化

钉钉将组件的标题区整体做了接管，开发者只需要提供内容，钉钉会统一在营销态和运行态支持标题、图标、管理的展示。

> **[!NOTE]**
>
> - 如后期设计规范升级，工作台会统一修改组件外框等样式，为减少组件未来的维护成本，请使用 **config.json** 中 **quickSetting** 的标准设置。
> - 如使用了旧的配置，请同步删除。

![标题栏的标准化](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7551987261/p300383.png)

使用标准标题栏及卡片样式，只需要增加 **config.json** 中的 **quickSetting** 配置即可，配置如下：

```
{
    "pluginComponentName": "project-select-view",
    "name": "对应下图中的title",
    "icon": "对应下图中的icon",
    "previewUrl": "https://img.alicdn.com/tfs/TB1KcAWdrj1gK0jSZFOXXc7GpXa-750-100.jpg",
    "previewHeight": 200,        
  // 工作台组件的快速设置选项   
    "quickSetting": {
        "useStandardHead": true,     // 使用工作台组件标准标题栏，请所有组件升级到此设置
        "useStandardContainer": true,   // 使用工作台组件标准样式，请所有组件升级到此设置
        "containerType": "standard",    // 组件是标准高度的组件值设置为standard，2倍高度的组件值为doubleHeight
    },
    "props": {

    }
}
```

设置 **quickSetting** 后，只需开发组件内容区，如下图所示：

![quickSetting](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3580858261/p300389.png)

- **icon**：组件的 config.json 里的 icon（图示中①）。
- **name**：组件的 config.json 里的 name（图示中②）。
- **link**：点击标题跳转链接，组件上架时提交给验收人员（图示中③）。
- **manage**：右侧管理，自动注入，开发者无需提供（图示中④）。
