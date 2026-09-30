---
title: "消息结构与生命周期"
source_url: "https://open.dingtalk.com/document/development/message-structure-and-lifecycle"
namespace: "development"
slug: "message-structure-and-lifecycle"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "消息结构与生命周期"
doc_id: "0hMNG9wRGN"
updated_at: "2026-09-30 09:14:33"
---

> Source: https://open.dingtalk.com/document/development/message-structure-and-lifecycle
> Path: 互动卡片 / JSON 构建卡片（AI） / 消息结构与生命周期
> Updated: 2026-09-30 09:14:33

# 消息结构与生命周期

四种公开消息的结构、Surface 创建方式与数据绑定规则。

## 消息集合

Agent 发送给客户端的消息共 4 种：

| **消息** | **用途** |
| --- | --- |
| `createSurface` | 创建新的 Surface，重复创建活动中的同名 Surface 将报错。 |
| `updateComponents` | 按组件 ID 新增或替换组件定义。 |
| `updateDataModel` | 按 JSON Pointer 路径更新 Surface 数据。 |
| `deleteSurface` | 移除 Surface、组件树、数据及本地状态。 |

消息包络必须包含 `version`（固定为 `"v1.0"`），且每条消息只能选择一种载荷类型。

## Surface 的创建方式

Surface 的创建方取决于卡片的来源，这是接入时容易混淆的关键点：

| **情形** | **首帧消息** | **说明** |
| --- | --- | --- |
| 发送新卡片 | `createSurface` | 消息数组中需包含 `createSurface`，其中 `catalogId` 必填。 |
| Surface 已由宿主预先创建 | `updateComponents` | 开发者仅需下发内容更新消息，无需发送 `createSurface`。 |

> **[!NOTE]**
>
> - 基础协议允许省略 `createSurface.catalogId`，但**钉钉当前协议要求显式填写**。
> - 普通`lint`不检查此项（因其也用于校验宿主创建的内容），新卡片使用`lint --preflight new-card`或`preview`，都会拦截遗漏。
> - 组件级 `catalogId` 可覆盖 Surface 的默认值。

无论哪种情形，同一张卡片的**所有消息必须使用同一个** `surfaceId`。

## 组件树规则

- **同一条消息内 ID 不可重复**：在同一条 `updateComponents` 中重复定义相同 ID，预检将判定为错误。

  > **[!NOTE]**
  >
  > 在后续消息中使用已有 ID，表示更新该组件。
- **引用必须可解析**：`children` / `child` 引用的 ID 必须在当前组件树中存在，可在本条消息中定义，也可来自之前的消息。

  > **[!NOTE]**
  >
  > 引用不存在的组件，预检将判定为错误。
- **绑定初始化**：首次使用绑定前，提供字段所需的、类型正确的初始数据。可以使用 `createSurface.dataModel`，也可以使用 `updateDataModel`。

  > **[!NOTE]**
  >
  > 本教程采用后者。
- **根组件 ID 为 root**：目标组件自身的 `id` 为 `"root"`，后续局部更新可只提交新增或变化的组件，无需每批重复提交根组件。
- **数组按字段契约填写**：数组是否可为空以各字段说明为准，例如 `Column.children` 可以为空，而 `ButtonGroup.buttons` 为空时组件将降级为占位符。

  > **[!NOTE]**
  >
  > 需要展示内容时应填入真实数据，不使用占位域名。

## 数据绑定的三种形式

只有字段契约声明支持动态值时，才能使用路径绑定或函数表达式。普通字符串字段通过 `updateComponents` 更新。以下以支持 `DynamicString` 的 `Text.text` 为例，表达式一栏仅展示结构，具体参数需按函数契约填写：

| **形式** | **写法** | **更新方式** |
| --- | --- | --- |
| 字面量 | `"text": "审批详情"` | 重新发送 `updateComponents`。 |
| 数据路径绑定 | `"text": {"path": "/order/title"}` | 发送 `updateDataModel`。 |
| 函数表达式 | `"text": {"call": "formatString", "args": {…}}` | 更新依赖路径所指向的数据，表达式自动重新计算。 |

只修改绑定数据时，使用 `updateDataModel`；组件结构或普通字段变化时，使用 `updateComponents`。更新时保持组件 ID 稳定，不重放无关的表单初值，避免覆盖用户已经输入的数据。

## 协议版本与 Catalog

钉钉 AI 卡片采用 A2UI 1.0 的部分能力，并扩展了组件、函数与宿主动作，不能直接替换为官方 A2UI 实现。接口参数中的 `a2uiMessages`、`a2uiAnnotations`、`protocolVersion` 均指该协议。

### 三个版本字段

三个版本字段含义不同，取值相互独立：

| **字段** | **取值** | **含义** |
| --- | --- | --- |
| `version` | `"v1.0"` | 消息包络版本，每条消息必填。 |
| `protocolVersion` | `"1.0"` | A2UI 协议版本，投递接口透传。 |
| `aicardVersion` | `"V0.8"` | 钉钉 AI 卡片的产品与能力集版本，当前公开 47 个组件。 |

> **[!NOTE]**
>
> 将消息包络的 `version` 误写为 `"V0.8"` 是高频错误，消息将被直接拒绝：`version` 描述的是消息格式，恒为 `"v1.0"`。

### Catalog 与 catalogId

组件与函数的可用集合及字段约束由 Catalog 声明。钉钉公开 Catalog 是钉钉自有的目录，内容为 A2UI 1.0 的子集加上钉钉扩展，**并非 A2UI 官方 Catalog**。`createSurface` 通过以下标识声明其引用：`https://dingtalk.com/card/a2ui/catalogs/public/catalog.json`。

- `catalogId` 是运行时标识，**不是下载地址**，客户端不会拉取该文件，而是按内置的组件实现进行渲染。
- Catalog 的作用是约定字段契约，供生成与校验使用。
- 调用钉钉端能力的写法参见[客户端动作](0011-json-card-client-actions.md)。

## createSurface

- **含义**：通知渲染器创建新画布并开始渲染。
- **说明**：

  - 创建画布会隐式实例化标准的 `Surface` 容器组件，其 `child` 为 `root`。
  - 在未先删除的情况下，使用已存在的 ID 创建画布将报错。
  - `surfaceId` 在渲染器的生命周期内必须全局唯一。
  - 发送此消息后，渲染器将等待同一 `surfaceId` 的 `updateComponents` 和/或 `updateDataModel` 消息来定义组件树。
- **属性说明：**

  | **属性** | **类型** | **必填** | **说明** |
  | --- | --- | --- | --- |
  | `surfaceId` | `string` | 是 | 要渲染的 UI 画布的唯一标识，在渲染器的生命周期内必须全局唯一。 |
  | `catalogId` | `string` | 否 | 钉钉当前新卡投递链路必须填写 `https://dingtalk.com/card/a2ui/catalogs/public/catalog.json`。未单独指定 `catalogId` 的组件和函数使用画布的默认 Catalog。  **[!NOTE]**  基础协议可选，钉钉新卡必填。 |
  | `sendDataModel` | `boolean` | 否 | 为 `true` 时，渲染器会在发给创建该画布的 Agent 的每条 A2A 消息的 `metadata` 中，携带该画布的完整数据模型。默认为 `false`。 |
  | `components` | `ComponentsList` | 否 | — |
  | `dataModel` | `object` | 否 | 画布初始的根数据模型对象。 |
  | `metadata` | `object` | 否 | 可选的画布级元数据。 |
- **示例**：

  ```
  {
    "version": "v1.0",
    "createSurface": {
      "surfaceId": "order-001",
      "catalogId": "https://dingtalk.com/card/a2ui/catalogs/public/catalog.json"
    }
  }
  ```

## updateComponents

- **含义**：按组件 ID 新增或替换组件定义。
- **说明**：

  - 完整组件树必须包含 `id: "root"` 的根组件。
  - 后续增量消息可以只提交变化的组件。
  - 目标 Surface 必须已经创建。
  - 宿主已创建时，不要重复发送 `createSurface`。
- **属性说明：**

  | **属性** | **类型** | **必填** | **说明** |
  | --- | --- | --- | --- |
  | `surfaceId` | `string` | 是 | 要更新的 UI 画布的唯一标识，在渲染器的生命周期内必须全局唯一。 |
  | `components` | `ComponentsList` | 是 | — |
- **示例**：

  ```
  {
    "version": "v1.0",
    "updateComponents": {
      "surfaceId": "order-001",
      "components": [
        {
          "id": "root",
          "component": "Text",
          "text": {
            "path": "/order/status"
          }
        }
      ]
    }
  }
  ```

## updateDataModel

- **含义**：更新已有画布的数据模型。
- **说明**：

  - 目标 Surface 必须已经创建。
  - 宿主已创建时，不要重复发送 `createSurface`。
- **属性说明：**

  | **属性** | **类型** | **必填** | **说明** |
  | --- | --- | --- | --- |
  | `surfaceId` | `string` | 是 | 本次数据模型更新所作用的 UI 画布的唯一标识，在渲染器生命周期内必须全局唯一。 |
  | `value` | `any` | 是 | 要写入数据模型的数据。基础协议中，把 `value` 显式设为 `null` 表示删除 `path` 处的键值；钉钉当前不执行这种删除。 |
  | `path` | `string` | 否 | 可选，指向数据模型中某个位置的路径（例如 `/user/name`）。省略或设为 `/` 时表示整个数据模型。 |
- **示例**：

  ```
  {
    "version": "v1.0",
    "updateDataModel": {
      "surfaceId": "order-001",
      "path": "/",
      "value": {
        "order": {
          "status": "订单已创建"
        }
      }
    }
  }
  ```

## deleteSurface

- **含义**：删除 `surfaceId` 所标识的已有画布。
- **说明**：

  - 目标 Surface 可以由应用或宿主创建，不要求应用重复发送 `createSurface`。
- **属性说明：**

  | **属性** | **类型** | **必填** | **说明** |
  | --- | --- | --- | --- |
  | `surfaceId` | `string` | 是 | 要删除的 UI 画布的唯一标识，在渲染器的生命周期内必须全局唯一。 |
- **示例**：

  ```
  {
    "version": "v1.0",
    "deleteSurface": {
      "surfaceId": "order-001"
    }
  }
  ```
