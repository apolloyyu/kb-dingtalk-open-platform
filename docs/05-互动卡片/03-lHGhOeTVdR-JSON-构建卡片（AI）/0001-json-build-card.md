---
title: "JSON 构建卡片"
source_url: "https://open.dingtalk.com/document/development/json-build-card"
namespace: "development"
slug: "json-build-card"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "JSON 构建卡片"
doc_id: "rlaRPgt1hX"
updated_at: "2026-09-30 09:14:34"
---

> Source: https://open.dingtalk.com/document/development/json-build-card
> Path: 互动卡片 / JSON 构建卡片（AI） / JSON 构建卡片
> Updated: 2026-09-30 09:14:34

# JSON 构建卡片

## 概述

使用 JSON 消息直接描述卡片的组件树与数据模型，由钉钉客户端直接渲染。**不需要在卡片平台预先搭建、发布卡片模板**，卡片结构可以在运行时才确定。业务代码可以直接生成 JSON，不要求使用 Agent 或 Skill；也可以由 Agent 借助 Skill 生成。支持 iOS、Android、HarmonyOS、Windows、macOS 和 Web 六端渲染与交互。

钉钉 AI 卡片基于 A2UI 协议，并提供钉钉扩展能力。协议版本、消息格式与 Catalog 说明详见[协议版本与 Catalog](0002-message-structure-and-lifecycle.md#459797e8562di)。

## 效果展示

### **组件组合示例**

钉钉客户端中的组件组合示例，涵盖布局、图表、表单和媒体。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4780370971/p1104127.png)

### 执行过程与交互

- **执行进度**

  ![5eecdaf48460cde5de8d46ba12b898e7713eb49a14a94cbb75b8339e1c4c24831b75b38faadcd24bec177c308ebd530456073e3580196b123c9efba68a5fdf1045bc5bffafab2b24e631dd85026326a38a5ab0c638ee1d244fb4c8ed7016461c](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4780370971/p1104130.png)
- **展开详情**

  ![5eecdaf48460cde5de8d46ba12b898e7713eb49a14a94cbb75b8339e1c4c24831b75b38faadcd24bec177c308ebd53043a54532cead5f2fec056b0563877a4efab36cafe0abb8830e5486d54cb74493f4455f0887f4b64dc4fb4c8ed7016461c](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4780370971/p1104131.png)

## **核心概念**

| **概念** | **作用** | **对应消息** |
| --- | --- | --- |
| 组件树 | 决定显示什么、怎么排列。每个组件有唯一 `id`，通过 `children` / `child` 引用组成一棵树，`id` 为 `root` 的组件是根节点。 | `updateComponents` |
| 数据模型 | 保存业务值。静态内容可以直接填写；需要随数据变化的内容，可在字段支持时通过 `{"path": "/order/title"}` 这样的路径绑定读取。 | `updateDataModel` |
| 消息 | 用于创建画布、更新组件树或数据。同一张卡片的所有消息共用一个 `surfaceId`。 | `createSurface` / `updateComponents` / `updateDataModel` / `deleteSurface` |

结构与数据分离的设计，使后续更新仅需发送变化的数据，无需重发整棵组件树。完整规则参见[消息结构与生命周期](0002-message-structure-and-lifecycle.md)。

## 最小示例：创建与更新

以一张订单状态卡为例，演示最基本的流程：先创建卡片，再仅更新数据。

### **第一步：创建卡片**

创建由三条消息组成，按顺序执行：

1. `createSurface` 创建画布，并声明钉钉公开 Catalog 的 `catalogId`。
2. `updateDataModel` 写入数据。
3. `updateComponents` 声明组件树，两个 `Text` 分别绑定到 `/order/title` 和 `/order/detail`。

**创建卡片的完整消息（3 条）：**

- **card.a2ui.json**

  ```
  [
    {
      "version": "v1.0",
      "createSurface": {
        "surfaceId": "order-001",
        "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"
      }
    },
    {
      "version": "v1.0",
      "updateDataModel": {
        "surfaceId": "order-001",
        "path": "/",
        "value": {"order": {"title": "订单已创建", "detail": "订单号 A2024001，预计 3 天内发货"}}
      }
    },
    {
      "version": "v1.0",
      "updateComponents": {
        "surfaceId": "order-001",
        "components": [
          {"id": "root", "component": "Column", "children": ["title", "detail"], "gap": 8},
          {"id": "title", "component": "Text", "text": {"path": "/order/title"}},
          {
            "id": "detail",
            "component": "Text",
            "variant": "caption",
            "text": {"path": "/order/detail"}
          }
        ]
      }
    }
  ]
  ```
- **预期效果**：卡片显示标题"订单已创建"和一行说明"订单号 A2024001，预计 3 天内发货"。

### **第二步：仅更新数据**

订单发货后，仅需发送一条 `updateDataModel` 修改标题，无需重发组件树；同时将卡片状态推进至 `FINISH`。状态不在消息体中传递，而是通过发送命令的 `flowStatus` 参数指定，详见 [DWS 发送与更新](0017-json-card-dws-send-and-update.md)。

```
[
  {
    "version": "v1.0",
    "updateDataModel": {"surfaceId": "order-001", "path": "/order/title", "value": "订单已发货"}
  }
]
```

**预期效果**：标题变为"订单已发货"，说明文字不变，仅当投递更新同时设置 `flowStatus=FINISH` 时，卡片进入完成状态。

将消息保存为文件后，需先离线校验，再发送至会话：参见[Agent Skill 创建与校验](0015-json-card-agent-skill-create-and-validate.md)、[DWS 创建与校验](0014-json-card-dws-create-and-validate.md) 和 [DWS 发送与更新](0017-json-card-dws-send-and-update.md)。

## 延伸阅读

1. [消息结构与生命周期](0002-message-structure-and-lifecycle.md)：创建与更新的场景、消息顺序、组件 ID 与引用规则、数据绑定。
2. [使用示例](0013-json-card-usage-examples.md)：查找接近的现成结构进行修改，比从零编写更高效。
3. [组件](0003-json-card-component-overview.md)与[函数](0008-json-card-core-functions.md)手册：按需查阅，无需通读。
4. [Agent Skill 创建与校验](0015-json-card-agent-skill-create-and-validate.md)：编写完成后先离线校验，再发送给自己确认渲染效果。
5. [DWS 发送与更新](0017-json-card-dws-send-and-update.md)：发送至真实会话，并推进卡片状态。
6. 进阶：交互与回调：按钮和表单的写法参见[使用示例](0013-json-card-usage-examples.md)；事件如何返回业务侧及当前能力边界参见[监听交互事件](0016-json-card-listen-to-interaction-events.md)。
