---
title: "布局与组合组件"
source_url: "https://open.dingtalk.com/document/development/json-card-layout-and-composite-components"
namespace: "development"
slug: "json-card-layout-and-composite-components"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 组件 > 布局与组合组件"
doc_id: "Ju6SHabOQQ"
updated_at: "2026-09-30 09:14:15"
---

> Source: https://open.dingtalk.com/document/development/json-card-layout-and-composite-components
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 组件 > 布局与组合组件
> Updated: 2026-09-30 09:14:15

# 布局与组合组件

本文档汇总钉钉互动卡片全部布局与容器组件的属性说明与使用示例。每个组件包含属性表格和 JSON 构建代码，供开发者快速查阅。

## 链接（Link）

可点击的链接文字与跳转。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `text` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 链接显示的文字。支持字面量、数据绑定和值函数。  **[!NOTE]**  多语言文案由服务端本地化后再发送。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `maxLine` | integer | 否 | 最大显示行数，不填写是默认为 2。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 点击组件时执行的动作，只有组件声明了可点击能力时才生效。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Link",
  "text": "REPLACE_TEXT"
}
```

## **卡片标题（CardHeader）**

统一的卡片标题栏，支持主题色、动态标题、深色主题图标和尾部内容。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `title` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 卡片标题，支持字面量、数据绑定和函数返回值。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `theme` | blue | red | orange | green | pink | purple | yellow | water | olive | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 否 | 语义主题，默认 blue、未知取值回落为 `blue`，不报错。   - **一个取值同时决定四种浅色/深色颜色**：浅色和深色下的标题颜色，以及浅色和深色下的标题栏背景色。 - 搭配由设计系统固定，不接受任意十六进制颜色，也不拆成多个字段。采用枚举而非 `colorToken`，因为后者一个 Token 仅对应一种颜色，无法表达一对多关系。 - 背景使用主色 12%–16% 的不透明度，由渲染器按当前主题选择浅色或深色，标题颜色的选择方式相同。 - 为兼容旧卡片，也可以直接传主色的十六进制值（`#0066FF`、`#00B853`、`#F2510C`、`#FF9200`）。 |
| `icon` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 标题栏 LOGO 图片 URL，显示在标题左侧，16×16 px，与标题间距 6px，未配置时不渲染图标位。 |
| `darkIcon` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 深色主题下的 Logo 图片 URL，不填写时使用`icon`。  **[!NOTE]**  浅色和深色的 URL 一起下发，由渲染器按当前主题选择，主题切换时立即更新。 |
| `trailing` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 否 | 标题右侧的插槽，取值是同一画布内某个组件的 `id`：单个字符串，不是数组，不填写时不渲染尾部内容。   - 插槽内容右对齐，与标题间距 6px，标题占据剩余宽度，过长时换行，常用于来源标签、状态标签和时间。 - 要放多个元素，请在插槽里放一个 `Row`，用它的 `gap` 和 `align` 显式控制间距与对齐 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "CardHeader",
  "title": "REPLACE_TEXT"
}
```

## **网格布局（GridLayout）**

网格布局，支持静态子组件和数据模板，省略 `columns` 时按卡片内容宽度自适应列数，设置 `columns` 时固定列数，省略行高和列间距时的行为见对应字段。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 子组件 ID 列表或动态子组件模板。动态形式下：  **componentId**：指向单元格模板。  **path**：指向数据模型中的数组。  **[!NOTE]**  两种形式的渲染结果相同，单元格按 `columns` 逐行排列。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `columns` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 每行列数，**未填写时按卡片宽度自适应**：最小列宽 234，最多 3 列，取不到宽度时为 2 列。  **[!NOTE]**  指定时严格按该值排列，不再自适应。 |
| `columnGap` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 列间距，可以是数字或卡片协议的 `DynamicNumber`。  **[!NOTE]**  设置 `columns` 时默认 8，省略 `columns`、处于自适应模式时默认 12。 |
| `rowGap` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 行间距，默认 8，可以是数字或卡片协议的 `DynamicNumber`。 |
| `itemHeight` | number | 否 | 固定的单元格高度，不填写或设为 0 时，不向渲染器提供固定高度，最终高度由布局决定。  **[!NOTE]**  需要固定高度时请设置正数。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "GridLayout",
  "children": [
    "REPLACE_CHILD_ID"
  ]
}
```

## **循环容器（Loop）**

数据驱动的重复渲染容器。重复项纵向排列，尺寸跟随模板内容和父级布局。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 模板与数据路径的结构和动态 `ChildList` 相同。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### **注意事项**

- `children` 使用 {`componentId`, `path`} 模板形式。相对路径绑定只在该模板上下文内有效。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Loop",
  "children": {
    "componentId": "REPLACE_CHILD_ID",
    "path": "REPLACE_TEXT"
  }
}
```

## **层叠容器（Stack）**

Z 轴层叠容器：由一个**底层**决定尺寸，在其上叠放 0~N 个**叠加层**。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `child` | [Child](0010-json-card-common-types.md#1fb1d1713fvjp) | 是 | **底层**的组件 ID，只能一个。   - 它铺满整个 `Stack` 并**决定容器尺寸**，叠加层相对它定位。 - 要放多个元素，请先用 `Row` / `Column` 包起来再填在这里。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `overlays` | object[] | 否 | **叠加层**列表，按数组顺序从下到上叠放在底层之上。   - 每一项是一个对象，只接受 `child` 和 `position` 两个键，且都必填。 - 不填写时只显示底层，不创建叠加层。 |
| `backgroundColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即容器背景的 DDesign Token 名。   - **优先级高于** `backgroundColor` 。 - 取值与行为和 `Row`、`Column` 上的同名字段一致。 |
| `backgroundColor` | string | 否 | 容器背景色，十六进制 `#RRGGBB` 或 `#AARRGGBB`，为设置时透明。  **[!NOTE]**  在图片上叠一层半透明遮罩，是层叠容器的典型用法。 |
| `cornerRadius` | number | 否 | 圆角，单位 px，必须是数字。  **[!NOTE]**  不填写时不设置显式圆角，沿用客户端容器的默认样式。 |
| `borderWidth` | number | 否 | 边框宽度，单位 px，必须是数字。  **[!NOTE]**  要显示边框，还需要同时配置 `borderColor` |
| `borderColor` | string | 否 | 描边颜色，取值格式与 `backgroundColor` 相同。 |
| `borderColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即边框颜色的 DDesign Token 名，**优先级高于** `borderColor` 。   - 由客户端按**当前客户端平台、主题和租户解析**，这是让边框跟随浅色与深色主题的唯一方式：`borderColor` 只接受单个取值，在深色模式下保持不变。 - 线条色有 `common_line_light_color` 和 `common_line_hard_color` 两组，实际色值与不透明度由客户端解析。 - 客户端解析不到时视为未填写，继续按 `borderColor` 取值，不报错。 |
| `padding` | number | 否 | 四边统一的内边距，单位 px，用于让叠加层与容器边缘保持距离。  **[!NOTE]**  不填写时该字段不增加内边距，卡片根节点仍可能从卡片布局获得内衬。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 让整个容器可点击，`Action` 语义与 `Row` / `Column` 上的 `action` 字段相同。 |
| `weight` | number | 否 | Flex 布局权重。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### **注意事项**

- 底层由 `child` 指定，叠加层的引用在 `overlays`[].child 中。两处引用都必须能解析到组件。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Stack",
  "child": "REPLACE_CHILD_ID"
}
```

## **滚动容器（ScrollView）**

水平或垂直滚动容器。

### 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  客户端动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `direction` | horizontal | vertical | 否 | 滚动方向，不填写时默认为 `vertical`。  **[!NOTE]**  垂直滚动需设置`maxHeight` 来限定可视区域，水平滚动受可用宽度约束。 |
| `autoScrollOnUpdate` | boolean | 否 | 内容更新后自动滚动到末端：水平方向滚到最右，垂直方向滚到底部，默认 `false`。   - 流式输出期间，桌面端还会屏蔽用户滚动，避免跟随滚动被打断。 - 仅对**可滚动**的配置生效：`direction: "horizontal"`，或带 `maxHeight` 的 `direction: "vertical"`。 - 不限高的垂直列表不会滚动，该字段在那里没有效果。 |
| `maxHeight` | number | 否 | 可视区域的高度上限，不填写或设为 0 时不限高，垂直内容全部展开，不在内部滚动。   - 正数会同时限制水平和垂直模式的可视高度。 - 垂直模式会开启内部滚动，水平滚动取决于内容是否超出可用宽度。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 否 | 子组件 ID 列表，所有引用都必须存在于当前画布中。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 定义交互处理器，可以触发 Agent 侧事件，也可以执行渲染器本地函数。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ScrollView"
}
```

## **标签页（Tabs）**

标签页，包含页签栏和内容面板。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `tabs` | object[] | 是 | 对象数组，每个对象定义一个页签的标题和子组件，数组第一项初始选中。   - 之后的选中状态在本地维护，没有公开的初始页签选择字段。 - **其中** `tabs`**[]**`.action` **只接受** `action.event`。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### **注意事项**

- 子组件的引用写在 `tabs`[].child 中，而不是顶层 `children`；每个 `child` 都必须对应一个已存在的组件。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Tabs",
  "tabs": [
    {
      "child": "REPLACE_CHILD_ID",
      "title": "REPLACE_TEXT"
    }
  ]
}
```

## **列表（List）**

公开的 `List` 组件，`direction` 统一了水平列表、垂直列表和数据驱动列表。

### 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 定义子组件。固定的一组子组件用字符串数组，按数据列表生成子组件时用模板对象。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `direction` | vertical | horizontal | 否 | 列表项的排列方向，不填写时默认为 `vertical`。 |
| `align` | start | center | end | stretch | 否 | 定义子组件在交叉轴上的对齐方式。不填写时默认为 `stretch`。 |
| `wrap` | boolean | 否 | 放不下时子组件是否换行，默认 `false`。   - **仅在** `direction: horizontal` **时生效**。 - 垂直容器在卡片中高度不受限，永远不会换行，垂直 `List` 上的 `wrap: true` 会被忽略，组件仍正常渲染。   **[!NOTE]**   - **与子组件的** `weight` **不兼容**：带权重的子组件会占满整行，导致无法换行。 - 需要换行时不要给子组件设置 `weight`**。** |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "List",
  "children": [
    "REPLACE_CHILD_ID"
  ]
}
```

## **折叠面板（CollapsiblePanel）**

统一的折叠面板，默认收起，`variant` 控制展开内容的样式：`indented` 在左侧显示缩进竖线，`reasoning` 使用平铺的 Agent 推理布局，`defaultExpanded` 可让首帧展开，`maxHeight` 在超过高度上限后开启内部滚动，`textEffect` 可给标题加扫光效果。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `title` | string | 是 | 折叠面板标题。当前接入要求非空文本。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 子组件 ID 列表，或数据驱动的模板。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `textEffect` | shimmer | 否 | 文本呈现效果。`shimmer` 让高光反复扫过文字，适用于「思考中…」这类流式等待状态，如果不填写则不加效果。   - 用在 `CollapsiblePanel` 上时作用于面板标题。 - 该字段对所有客户端一致下发，目前仅 iOS 生效，不支持的客户端会静默忽略，按普通文本渲染，文字本身不受影响。 - 这些客户端后续支持时无需修改协议。 |
| `icon` | string | 否 | 浅色模式下的标题图标地址。 |
| `darkIcon` | string | 否 | 深色模式下的标题图标 URL，未提供时使用 `icon`。 |
| `variant` | indented | reasoning | 否 | 展开内容的样式，默认indented。   - **indented**：在左侧画一条细竖线并缩进内容，表示这些是隶属于标题的细节，适合步骤详情和工具调用列表。 - **reasoning**：不画竖线，内容与标题对齐，把面板标记为 Agent 执行或推理的容器，适合标题只起开关作用、内容本身才是主要信息的场景。   **[!NOTE]**  该字段只影响展开内容的外观和这层语义标记：两种样式下的折叠行为、`defaultExpanded` 和 `maxHeight` 滚动完全相同。 |
| `defaultExpanded` | boolean | 否 | 首帧是否展开，默认 `false`（收起）。   - 折叠面板的语义是「先收起，想看再点开」，所以默认收起，确实需要一开始就展开的面板，请显式设为 `true`。 - 用户点击标题后的展开/收起状态由渲染器在本地维护，不受该字段影响。 |
| `maxHeight` | number | 否 | 展开内容区的最大高度，单位 px，默认 300px。超出部分在面板内滚动，不撑高整张卡片。   - 内容较短时只占实际高度，不会留白。 - 设为 0 表示不限高。 |
| `colorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即 DDesign Token 名，**颜色解析优先级最高**。   - 解析成功时忽略 `customLightColor` 和 `customDarkColor`。 - 解析机制与 `Text.colorToken` 相同。 |
| `customLightColor` | string | 否 | 浅色模式下的标题颜色，十六进制。仅在 `colorToken` 未命中时生效。 |
| `customDarkColor` | string | 否 | 深色模式下的标题颜色，十六进制。仅在 `colorToken` 未命中时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "CollapsiblePanel",
  "title": "REPLACE_TEXT",
  "children": [
    "REPLACE_CHILD_ID"
  ]
}
```

## **分栏布局（ColumnLayout）**

响应式分栏，支持 1 到 6 列。

### 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 子组件 ID 列表，或数据驱动的模板。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `columns` | integer | 否 | 常规宽度下的列数提示，1 到 6，内部默认 2。   - 当前的水平布局按子组件及其权重分配宽度，并不按该字段分组或换行。 - 要两栏布局，请提供两个子栏。 |
| `gap` | number | 否 | 列间距，不填写时默认为 8，响应式堆叠后用作纵向间距。 |
| `columnWidths` | number | "auto"[] | 否 | 各子栏的权重或 auto，按顺序对应 `children`。   - 仅在水平布局中用于分配宽度，子组件自身显式设置的权重优先。 - 不填写时，没有自身权重的子组件平分宽度。 - 响应式堆叠为纵向单列后，该字段不再分配宽度。 |
| `contentAlignment` | topStart | topCenter | topEnd | centerStart | center | centerEnd | bottomStart | bottomCenter | bottomEnd | 否 | 二维内容对齐，取值与 `Stack.overlays[].position`相同的九宫格。  各栏本身平分权重，因此它实际控制的是**每一栏在交叉轴（垂直方向）上的对齐**：栏高不同时，决定较矮的栏顶部、居中还是底部对齐。 |
| `responsive` | boolean | 否 | **窄卡片上的响应式堆叠**，默认 `false`。   - 开启且 `responsiveColumns` 不填写或设为 1 时，子栏在窄卡片上纵向堆叠，`gap` 变为纵向间距。 - 较宽的卡片上，实际的子组件及其权重仍保持水平布局。 - 详见响应式行为说明。 |
| `responsiveColumns` | integer | 否 | 窄屏下的目标列数，默认 `1`，只有与 `responsive: true` 一起配置时才生效。  **[!NOTE]**  目前只能取 `1` ，设置其他值不会减少列数，窄屏下保持原布局。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ColumnLayout",
  "children": [
    "REPLACE_CHILD_ID"
  ]
}
```

## **按钮组（ButtonGroup）**

并排排列的一组按钮，每个按钮有自己的文字和动作，按钮样式与独立的 `Button` 完全相同（同一套胶囊样式），唯一区别是用数组一次声明多个按钮，并统一控制间距和换行。

![按钮组（ButtonGroup）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5580370971/p1104328.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `buttons` | [HostActionOwner](0010-json-card-common-types.md#6b75537bc69u5)[] | 是 | 按钮定义列表不能是空数组。空数组会导致整个组件降级为占位。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  按钮的客户端动作结果回写各自写在 `buttons`[]`.metadata.extensions.dt_actionBindingsV1.action.resultPath` 中，不写在按钮组本身；路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `responsive` | boolean | 否 | **宽窄屏自适应换行**，默认 `false`。详见下文「响应式行为」。 |
| `gap` | number | 否 | 相邻按钮之间的水平间距，单位 px，默认 `8`。第一个按钮前不加间距。 |
| `weight` | number | 否 | 作为 `Row` 或 `Column` 的直接子组件时的相对 flex 系数。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### **注意事项**

- `buttons`[] 是内联对象数组；每一项的宿主回写写在它自己的 `metadata` 中，而不是父组件上。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ButtonGroup",
  "buttons": [
    {
      "label": "REPLACE_TEXT"
    }
  ]
}
```
