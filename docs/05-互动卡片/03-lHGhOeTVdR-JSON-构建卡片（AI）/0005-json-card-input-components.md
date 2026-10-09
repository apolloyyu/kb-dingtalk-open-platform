---
title: "输入组件"
source_url: "https://open.dingtalk.com/document/development/json-card-input-components"
namespace: "development"
slug: "json-card-input-components"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 组件 > 输入组件"
doc_id: "FlWKzZ1xUu"
updated_at: "2026-09-30 09:14:22"
---

> Source: https://open.dingtalk.com/document/development/json-card-input-components
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 组件 > 输入组件
> Updated: 2026-09-30 09:14:22

# 输入组件

本文档汇总钉钉互动卡片全部输入组件的属性说明与使用示例。每个组件包含属性表格和 JSON 构建代码，供开发者快速查阅。

## **输入框（TextField）**

公开的 `TextField` 组件，`variant` 统一了单行和多行文本输入，点击后打开输入面板，结果在本地回显，可以禁用。不支持 `checks` 字段：请把输入校验挂在提交按钮的 `Button.checks` 上，并用 `path` 引用值绑定。

![输入框（TextField）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104208.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 输入框的文字标签。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `value` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 输入框的值，省略时初始文本为空。要提交用户输入，请配置数据绑定，省略 `value` 不会产生回写路径 |
| `placeholder` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 输入框的占位文字，省略时为空，`label` 不会自动用作占位文字。 |
| `variant` | shortText | longText | 否 | 输入类型，默认 `shortText`，`longText` 打开多行输入面板。  基础协议的 `number` 和 `obscured` 两种类型在钉钉没有对应的运行时输入方式，因此本枚举只开放这两个取值。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `disabled` | boolean | 否 | 是否禁用，默认 `false`。设为 `true` 时，不会触发输入事件（点击不再打开输入面板），文字置灰（有值时使用禁用色，无值时本来就是占位灰）。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "TextField",
  "label": "REPLACE_TEXT"
}
```

## 选择器（ChoicePicker）

公开的 `ChoicePicker` 组件，`variant` 统一了单选和多选，`displayStyle` 选择行、标签或下拉的展示方式，`disabled` 让整组置灰。

![选择器（ChoicePicker）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104213.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `options` | object[] | 是 | 可供选择的选项列表。 |
| `value` | [DynamicStringList](0010-json-card-common-types.md#afd2f8465fmyy) | 是 | 当前选中的值列表，应绑定到数据模型中的字符串数组。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `checks` | [CheckRule](0010-json-card-common-types.md#496ab27c64dc7)[] | 否 | 只在配置了 `action` 时才会执行。   - 本地状态可能已经更新或回显，校验不通过会阻止后续 `Action` 并弹出 toast 提示，但不保证能阻止或回滚本地的选择。 - 表单校验请挂在提交按钮上。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 这组选项的标签。 |
| `variant` | multipleSelection | mutuallyExclusive | 否 | 选择器的展示和行为提示。省略时为 `mutuallyExclusive`（单选），多选请显式使用 `multipleSelection` |
| `displayStyle` | checkbox | chips | dropdown | 否 | 展示样式   - `checkbox` 显示为纵向排列的可点击行，`chips` 显示为一行标签。 - `dropdown` 显示为一个紧凑的行，点击后打开客户端原生选择器，**省略时使用** `dropdown`。 - 枚举之外的取值也回落为 `dropdown`，不会变成占位。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | **仅对** `displayStyle: dropdown`**（省略时的默认值）生效**。   - 用户在原生面板中确认选择后，渲染器先把新值写入 `value` 绑定的路径，再把事件发给 Agent。 - 取消面板不会触发该动作。 - 内联样式（`checkbox` 和 `chips`）没有确认步骤，**不会触发** `action`，它们的选中值通过 `value` 绑定写入本地状态，由提交按钮的 `context` 经父路径收集。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `disabled` | boolean | 否 | 是否禁用，默认 `false`。设为 `true` 时，不会触发点击事件（不再打开选择面板，也不能切换选项），**文字、选中标记和选中底色都切换为禁用态**。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### 注意事项

- `options[]`是内联数组，单选和多选的值绑定都是字符串数组。
- 由 `variant` 选择模式。

  - 只有默认的下拉样式在确认时触发 `action`。
  - checkbox 和 chips 样式只更新本地状态。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ChoicePicker",
  "options": [
    {
      "label": "REPLACE_TEXT",
      "value": "REPLACE_TEXT"
    }
  ],
  "value": [
    "REPLACE_TEXT"
  ]
}
```

## **复选框（CheckBox）**

布尔选择，必填的 `value` 决定初始是否勾选，`label` 显示在复选框旁。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 显示在复选框旁的文字。 |
| `value` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 是 | 复选框的当前状态：   - `true` ：勾选 - `false` ：未勾选 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。 |
| `checks` | [CheckRule](0010-json-card-common-types.md#496ab27c64dc7)[] | 否 | 只在配置了 `action` 时才会执行。   - 本地状态可能已经更新或回显，校验不通过会阻止后续 `Action` 并弹出 toast 提示，但不保证能阻止或回滚本地的选择。 - 表单校验请挂在提交按钮上 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj)仅 event | 否 | **只接受** `action.event`**，不能写** `functionCall`**，**勾选状态变化后上报。   - 渲染器先在本地切换取值并写入 `value` 绑定的路径，再把事件发给 Agent。 - 只支持 `event` 分支，`functionCall` 分支会被忽略，等同于没有设置 `action`。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "CheckBox",
  "label": "REPLACE_TEXT",
  "value": false
}
```

## **开关（Switch）**

开关，支持状态与尺寸。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。 |
| `value` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 开关是否打开，省略时为 `false`，初始关闭。 |
| `disabled` | boolean | 否 | 开关是否禁用，默认 `false`。为 `true` 时，渲染器下发 `enabled=0`，客户端原生开关无法切换，并按系统样式置灰 |
| `size` | small | normal | large | 否 | 尺寸预设，默认 `normal`。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) 仅 event | 否 | **只接受** `action.event`**，不能写** `functionCall`，开关状态变化后上报。   - 渲染器先在本地切换取值，并写入 `value` 绑定的路径，再把事件发给 Agent。 - 只支持 `event` 分支，`functionCall` 分支会被忽略，等同于没有设置 `action` |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Switch"
}
```

## **日期时间（DateTimeInput）**

日期与时间选择入口。

![日期时间（DateTimeInput）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104216.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 选中的日期和/或时间，ISO 8601 格式。尚未设置时用空字符串初始化。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `checks` | [CheckRule](0010-json-card-common-types.md#496ab27c64dc7)[] | 否 | 只在配置了 `action` 时才会执行。   - 本地状态可能已经更新或回显，校验不通过会阻止后续 `Action` 并弹出 toast 提示，但不保证能阻止或回滚本地的选择。 - 表单校验请挂在提交按钮上。 |
| `enableDate` | boolean | 否 | 为 `true` 时允许选择日期，省略时为 `true`。 |
| `enableTime` | boolean | 否 | 为 `true` 时允许选择时间。   - 省略时为 `false`，因此两个开关都省略时只选日期。 - `enableDate` 和 `enableTime` 不能同时为 `false`。 |
| `min` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 允许的最早日期/时间，ISO 8601 格式。 |
| `max` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 允许的最晚日期/时间，ISO 8601 格式。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 输入框的文字标签。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 用户在日期/时间面板中确认取值后上报。   - 渲染器先把新值写入 `value` 绑定的路径，再把事件发给 Agent。 - 取消选择器不会上报事件。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "DateTimeInput",
  "value": "REPLACE_TEXT"
}
```

## **数字输入（NumberInput）**

数字输入入口，点击后打开输入面板并显示结果。目前不是带加减按钮的步进器。必填的 `value` 提供初始数值。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | 当前值。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 输入标签，用作数字输入面板的标题。   - `placeholder` 省略或为空字符串时，它同时用作占位文字。 - `TextField` 不会自动用 `label` 代替 `placeholder`。 |
| `min` | number | 否 | 最小值，省略时不向输入面板提供明确的下限。 |
| `max` | number | 否 | 最大值，省略时不向输入面板提供明确的上限。 |
| `precision` | integer | 否 | 小数精度，省略时为 0。 |
| `placeholder` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 占位文字。 |
| `disabled` | boolean | 否 | 是否禁用，默认 `false`。   - 为 `true` 时，**不会触发输入事件**（点击不再打开数字输入面板），**文字置灰**。 - 与 `TextField` 使用同一种表单行实现。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj)仅 event | 否 | **只接受** `action.event`**，不能写** `functionCall`，用户在输入面板中完成编辑后上报。   - 渲染器先把新值写入 `value` 绑定路径，再把事件发给 Agent。 - 只支持 `event` 分支，`functionCall` 分支会被忽略，等于没有设置 `action`。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "NumberInput",
  "value": 0
}
```

## **评分（Rating）**

星级评分。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | 评分值（0-5）。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。 |
| `onTap` | [Action](0010-json-card-common-types.md#3d860c6514irj) 仅 event | 否 | 只接受 `action.event`，不能写 `functionCall`。   - 渲染器**先把新评分写入** `value` **绑定的路径，再把事件发给 Agent**。 - 只支持 `event` 分支，`functionCall` 分支会被忽略，等同于没有设置 `onTap`，因为客户端函数会占用星级控件的点击位，导致本地评分无法变化。 - 用户修改评分后上报、只有配置了该处理器，评分才可交互，否则为只读。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Rating",
  "value": 0
}
```

## **滑块（Slider）**

数值滑块，钉钉渲染为**只读进度条**，比例按 `value`、`min`、`max` 计算，不能拖动。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `max` | number | 是 | 滑块的最大值。 |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | 滑块的当前值。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据，客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `checks` | [CheckRule](0010-json-card-common-types.md#496ab27c64dc7)[] | 否 | 只在配置了 `action` 时，于点击后执行。   - 校验不通过会阻止后续 `Action` 并弹出 toast 提示，没有 `action` 时不执行任何校验。 - 表单校验请挂在提交按钮上。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 滑块的标签。 |
| `min` | number | 否 | 滑块的最小值。省略时为 0。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 点击进度条时上报给 Agent。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Slider",
  "max": 0,
  "value": 0
}
```

## **输入列表（InputList）**

可增删行的输入列表。

![输入列表（InputList）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104221.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DynamicStringList](0010-json-card-common-types.md#afd2f8465fmyy) | 是 | 可增删的字符串数组，应绑定到数据模型。   - 服务端下发的数组决定初始行数和各行取值。 - 本地增加、删除或编辑后，同一张卡片上提交按钮的 `context` 通过该路径读取**当前完整的本地数组**，包括本地新增的行。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。 |
| `label` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 输入列表的标题。 |
| `placeholder` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 新增输入项的占位提示。 |
| `addLabel` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 添加按钮的文字，省略时由运行时提供内置文字，需要特定措辞或语言时请显式设置。 |
| `variant` | shortText | longText | 否 | 每一行的输入类型，默认 `shortText`。   - `longText` 渲染为多行文本框，其他取值都按 `shortText` 处理。 - `inline` 和 `dialog` 两个取值会被静默按 `shortText` 渲染。 |
| `disabled` | boolean | 否 | 列表是否禁用，默认 `false`。   - 为 `true` 时，**不挂输入事件，不渲染添加入口和每行的删除按钮，文字和标签置灰**。 - 行数固定为服务端最初下发的数量。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) 仅 event | 否 | **只接受** `action.event`**，不能写** `functionCall`。   - 删除行和编辑单行不会上报事件，只更新本地状态，提交时通过 `value` 绑定的路径合并到数据模型。 - 只支持 `event` 分支，`functionCall` 分支会被忽略，等于没有设置 `action`。 - 点击添加时上报、渲染器先本地新增一行，再把事件发给 Agent。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "InputList",
  "value": [
    "REPLACE_TEXT"
  ]
}
```

## **多选列表（CheckboxListMulti）**

多选列表，支持本地状态。

![多选列表（CheckboxListMulti）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104222.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 动态 `ChildList`，用于声明可绑定的多选列表。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。 |
| `selectedIndexes` | integer[] | 否 | 初始选中的行下标，从 0 开始，单向下发，用户的修改不会更新该字段本身。   - 要获取选择结果，请配置 `value`。 - 省略时初始不选中任何行。 |
| `size` | small | middle | large | 否 | 选项行的尺寸，默认 `middle`。 |
| `disabled` | boolean | 否 | 控件是否禁用，默认 `false`。为 `true` 时。   - 若无点击事件，处理器仍会响应点击但状态不变。 - **是否置灰由渲染器的复选框决定**。 |
| `contentCheckable` | boolean | 否 | 点击整行是否切换该行的选中状态，默认 `true`。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) 仅 event | 否 | **只接受** `action.event`**，不能写** `functionCall`**，**任意一行的勾选状态切换后上报。   - 渲染器先改本地状态，再把事件发给 Agent。 - 只支持 `event` 分支，写 `functionCall` 不会生效，视为未配置 `action`。 |
| `value` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | 否 | 选择结果的回写路径。   - 回写的值是选中行下标的数组，含义与 `selectedIndexes` 相同。 - 省略时不回写，提交按钮也无法引用这次选择。 - `disabled` 为 `true` 时不回写。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "CheckboxListMulti",
  "children": {
    "componentId": "REPLACE_CHILD_ID",
    "path": "REPLACE_TEXT"
  }
}
```

## **可选图片列表（CheckableImageList）**

可选择的 1 到 9 张图片布局，按 4:3 裁剪，行列间距 12。

列数跟随卡片宽度，取不到宽度时为 2 列，支持布局期重排的桌面端会按组件实际宽度重新计算 1–5 列，其他使用按宽度计算的列数。

![可选图片列表（CheckableImageList）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104224.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `images` | string | object[] | 是 | 1 到 9 张图片。对象形式必须包含 `url`，可选字符串 `title`。   - 只要有一项带标题，就为每一项预留标题区。 - 选中下标对应图片在数组中的原始位置。 |
| `value` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | 是 | 存放选中图片下标的数据绑定。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。 |
| `previewEnabled` | boolean | 否 | 点击图片是否可以预览能加载的 URL ，省略时为 `true`。设为 `false` 只关闭图片预览，不影响选择。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### 注意事项

- `images` 接受字符串或 {`url`} 对象；`value` 是选中图片下标的数组。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "CheckableImageList",
  "images": [
    "REPLACE_TEXT"
  ],
  "value": {
    "path": "/REPLACE_PATH"
  }
}
```

## **人员选择器（UserPicker）**

打开钉钉通讯录选人面板，选择用户。

![人员选择器（UserPicker）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104227.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | 是 | 选中用户的数据绑定。   - 钉钉目前保留客户端选择器的原始结果形式：单选成功回写用户对象，多选成功回写用户对象数组。 - 清空多选回写空数组。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `placeholder` | string | 否 | 占位文字。   - 未选择时，提示文字优先使用 `title`，其次 `placeholder`。 - 两者都省略时使用运行时的内置提示。 |
| `title` | string | 否 | 选择面板的标题。 |
| `maxSelections` | number | 否 | 最多可选的用户数（默认 10），设为 1 表示单选，大于 1 表示多选。 |
| `disabled` | boolean | 否 | 是否禁用，默认 `false`。为 `true` 时，**不会触发点击事件**（不再打开选择面板），右侧的加号图标置灰。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 定义交互处理器，可以触发 Agent 侧事件，也可以执行渲染器本地函数。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "UserPicker",
  "value": {
    "path": "/REPLACE_PATH"
  }
}
```

## **会话选择器（ConversationPicker）**

调用钉钉会话选择器。

![会话选择器（ConversationPicker](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104229.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | 是 | 选中会话的数据绑定。   - 钉钉目前保留客户端选择器的原始结果形式：单选成功可能回写会话对象，也可能回写只含一个元素的对象数组。 - 多选成功回写会话对象数组，确认空选择时回写空数组。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。  客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `placeholder` | string | 否 | 占位文字。   - 未选择时，提示文字优先使用 `title`，其次 `placeholder`。 - 两者都省略时使用运行时的内置提示。 |
| `title` | string | 否 | 选择面板的标题。 |
| `multiple` | boolean | 否 | 是否允许多选，`multiple` 和 `maxSelections` 都省略时为单选。   - 显式设置 `multiple`=`true`，或 `maxSelections` 大于 1，都会开启多选。 - 单选结果可能是对象，也可能是只含一个元素的数组，取决于客户端，多选结果是数组。 |
| `maxSelections` | number | 否 | 最多可选数量。未开启多选时省略即为 1，取值大于 1 同样会开启多选。   - 显式设置 `multiple`=`true` 而不设置 `maxSelections` 时，上限由客户端决定。 - 需要固定上限时请显式设置。 |
| `disabled` | boolean | 否 | 选择器是否禁用，默认 `false`。为 `true` 时，如无点击事件，不再打开会话选择器，右侧的加号图标置灰。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 定义交互处理器，可以触发 Agent 侧事件，也可以执行渲染器本地函数。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ConversationPicker",
  "value": {
    "path": "/REPLACE_PATH"
  }
}
```

## **图片上传（ImageUpload）**

调用钉钉图片上传，把上传结果回填到 `value` 绑定的路径，并在按钮下方逐行列出已上传的文件（可删除）。

![图片上传（ImageUpload](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2680370971/p1104231.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `value` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | 是 | 上传结果的数据绑定，是图片 URL 数组。   - 服务端下发的初始值会渲染为已上传的文件行。 - 上传或删除后，最新的 URL 数组保留在客户端本地状态中。 - **提交时**通过该路径合并到数据模型，使同一张卡片上提交按钮的 `context` 能读到用户实际上传的图片。 - 该字段只接受数据绑定，写成字面量数组会被校验拒绝。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `label` | string | 否 | 上传按钮的文字。   - 省略时由运行时提供内置文字。 - 不能是空字符串，需要特定措辞或语言时请显式设置。 |
| `disabled` | boolean | 否 | 是否禁止上传，默认 `false`。为 `true` 时，渲染器使用禁用样式，不响应上传操作，已上传的文件行也不显示删除按钮。 |
| `requiresAuth` | boolean | 否 | 是否使用鉴权上传，默认 `true`。为 `true` 时回写的是需鉴权的媒体 URL，为 `false` 时回写普通 URL。 |
| `maxFiles` | number | 否 | 一次最多可选的图片数，默认 9，必须是正整数。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 上传成功后上报。   - 渲染器先把新返回的 URL 追加到 `value` 绑定的路径，再把事件发给 Agent。 - 上传失败和取消选图都不会上报事件。 - 失败行重试成功后，与首次上传一样上报。 - 只支持 `event` 分支，`functionCall` 分支会被忽略，等同于没有设置 `action`。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### 注意事项

- `value` 绑定图片 URL 数组；上传和删除会更新本地状态，提交时的 `context` 可以读取。
- `action` 只在上传成功后触发，上传失败或取消都不会触发，并且只支持 `event` 分支。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ImageUpload",
  "value": {
    "path": "/REPLACE_PATH"
  }
}
```
