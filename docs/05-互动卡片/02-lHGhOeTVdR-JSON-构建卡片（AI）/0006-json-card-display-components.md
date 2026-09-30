---
title: "展示组件"
source_url: "https://open.dingtalk.com/document/development/json-card-display-components"
namespace: "development"
slug: "json-card-display-components"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 组件 > 展示组件"
doc_id: "gOpVHhFTzr"
updated_at: "2026-09-30 09:14:18"
---

> Source: https://open.dingtalk.com/document/development/json-card-display-components
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 组件 > 展示组件
> Updated: 2026-09-30 09:14:18

# 展示组件

本文档汇总钉钉互动卡片全部展示组件的属性说明与使用示例。每个组件包含属性表格和 JSON 构建代码，供开发者快速查阅。

## **图片列表（ImageList）**

多张图片缩略图，并汇总显示数量。当前图片区高度为 200，宽度受父级布局约束。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `images` | string[] | 是 | 图片 URL 数组，至少一项。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `previewEnabled` | boolean | 否 | 点击是否可以预览，省略时为 `true`。  **[!NOTE]**  只有组内包含可加载的图片 URL 时才会开启预览。 |
| `fit` | contain | cover | fill | none | scaleDown | 否 | 图片缩放方式，采用 CSS `object-fit` 的取值。   - 省略时为完整包含，对应 `contain`，这与 `Image` 省略时裁剪填充的行为不同。 - `contain`/`scaleDown`/`none` 对应完整包含，`cover` 对应裁剪，`fill` 对应拉伸。 - 不要下发渲染器内部的缩放名称。 |
| `cornerRadius` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 图片组的圆角，省略时为 4，与 `Image` 默认的 6 不同。 |
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
  "component": "ImageList",
  "images": [
    "REPLACE_TEXT"
  ]
}
```

## **头像（Avatar）**

头像图片。未配置尺寸时为 48×48，外圆角为实际尺寸的四分之一。`sizeType` 选择使用预设还是 `customSize`。

### 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `imageUrl` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 头像图片 URL。 |
| `sizeType` | Standard | Custom | 否 | 尺寸类型：   - **Standard**：使用 size 预设 - **Custom 或省略**：使用 `customSize`，`customSize` 也省略时运行时默认48px。   **[!NOTE]**  其他取值不符合公开 Schema。 |
| `size` | extraSmall | small | middle | 否 | 尺寸预设，仅在 `sizeType` 为 `Standard` 时生效：`extraSmall` = 20px、`small` = 30px、`middle` = 48px。  **[!NOTE]**  省略时使用 middle，其他取值不符合公开 Schema。 |
| `customSize` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 自定义尺寸。  **[!NOTE]**  `sizeType` 不是 Standard 时使用，不填写默认 48px。 |
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
  "component": "Avatar"
}
```

## **头像组（AvatarGroup）**

头像叠放，并显示超出的数量。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `items` | object[] | 是 | 用户对象列表。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `maxVisible` | integer | 否 | 最多显示的头像数（超出时显示 +N），不填写默认为 5。 |
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
  "component": "AvatarGroup",
  "items": [
    {}
  ]
}
```

## **表格（Table）**

表格，支持表头、斑马纹和分页数据。

### 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `data` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | object | 是 | 表格数据，包含 `meta`（列）和 `data`（行）。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `cellPadding` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 单元格内边距，不填写默认左右各 12、上下各 8，显式的数字会统一应用到四边。 |
| `imageSize` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 表格内图片的尺寸，不填写默认为 30。 |
| `pageSize` | integer | 否 | 每页行数，默认 10，仅在 `pagination` 为 `true` 时生效。  **[!NOTE]**  小于 1 的取值无效，删除该字段即恢复默认。 |
| `maxLine` | integer | 否 | **文本类数据单元格**（`STRING`、`OBJECT` 和 `MICROAPP`）的最大显示行数，超出部分截断，默认且最多 3行，表头不受影响。   - 因渲染器的按钮不使用行数设置，所以`BUTTON` 单元格不受影响。 - 0 及以下的取值会被规整为 1，并将 0 下发给渲染器不显示行，导致该列文字消失。 |
| `zebra` | boolean | 否 | 是否开启斑马纹（隔行变色），省略时为 `false`，不隔行变色。 |
| `pagination` | boolean | 否 | 是否开启分页，默认 `false`。   - 分页完全在本地进行：全部数据一次下发，翻页只更新视图，不会向服务端读取数据。 - 若读取的数据少于一页的数据量，不渲染分页控件。 |
| `pageIndex` | integer | 否 | 初始页码（从 0 开始），删除该字段时默认渲染第 0 页   - 只决定首帧停在哪一页，之后的翻页由用户控制。 - 超过总页数时停在最后一页，负数视为无效。 |
| `scrollAreaWidth` | number | 否 | 横向滚动区域的宽度（px），默认 600px且必须是正数。  **[!NOTE]**  若表格列数超出表格宽度，表格会在当前设置宽度内横向滚动。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### **注意事项**

- `data` 是包含 `meta` 和 `data` 的结构化对象。
- 因为分页是在本地进行，所以需要一次提供全部行数据。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Table",
  "data": {
    "data": [
      {}
    ],
    "meta": [
      {
        "colKey": "REPLACE_TEXT",
        "colName": "REPLACE_TEXT",
        "type": "BUTTON"
      }
    ]
  }
}
```

## **图表（Chart）**

统一的公开图表，支持标准数据、模板渲染和响应式尺寸，**图表始终可以点击查看详情**，不需要也无法配置：卡片里的图表数值很难看清，点击查看大图是该组件的基本能力。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `data` | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | object | 是 | 图表数据的绑定，或真实的图表数据对象。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `aspectRatio` | 1:1 | 2:1 | 4:3 | 16:9 | 否 | 响应式宽高比，未配置 `height` 时生效。   - `height` 与 `aspectRatio` 都不填写默认 `2:1`。 - 若已经配置了固定高度，请勿配置该字段。 |
| `height` | number | 否 | 固定高度，配置该字段即启用固定高度。  **[!NOTE]**  若配置了该字段，请勿再配置 `aspectRatio`。 |
| `weight` | number | 否 | Flex 布局权重。仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### **注意事项**

- `data.type` 选择图表类型。
- `data.data` 是 {x,y} 数据点数组，不是组件 ID。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Chart",
  "data": {
    "data": [
      {
        "x": "REPLACE_TEXT",
        "y": 0
      }
    ],
    "type": "REPLACE_TEXT"
  }
}
```

## **进度条（ProgressBar）**

公开的进度组件，`variant` 把连续进度条和紧凑的块状进度统一在同一套取值、颜色和浅色/深色主题模型下。若没有可解析的颜色配置时，填充使用品牌色，取不到时回落为内置的浅色/深色颜色。

### 属性说明

| 属性 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `value` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | 进度值，语义范围为 0 到 100，字面量超出范围时校验失败，数据绑定的值由渲染器限制在有效范围内。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `variant` | bar | block | 否 | 渲染器显示连续或块状进度，默认 bar。   - **bar**：连续进度条 - **block**：紧凑的块状进度。 |
| `showLabel` | boolean | 否 | 仅在 bar 模式下生效，是否显示百分比文字，默认为 true。 |
| `labelPosition` | start | inside | end | 否 | 百分比文字相对轨道的位置，默认end，仅在 bar 模式下生效。   - **start**：放在左侧。 - **inside**：叠放在已填充段内，不占用额外的水平空间。 - **end：**轨道右侧，间距 12px。 |
| `colorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即进度条填充的 DDesign Token 名，**颜色解析优先级最高**。   - 解析成功时忽略 `customLightColor`、`customDarkColor` 和 `color` - 按当前客户端平台与主题解析，机制与 `Text.colorToken` 相同 - 解析不到时，按后续颜色来源依次取值。 |
| `customLightColor` | string | 否 | 两种模式共用的浅色主题颜色，支持 `#RRGGBB` 和 `#AARRGGBB`。 |
| `customDarkColor` | string | 否 | 两种模式共用的深色主题颜色，必须同时提供 `customLightColor`。   - 渲染器按当前主题选择浅色或深色的值下发。 - 主题切换在卡片下一次刷新后生效。 |
| `rounded` | boolean | 否 | 是否使用胶囊圆角，默认为true，仅在 bar 模式下生效。 |
| `size` | medium | small | 否 | 仅在 `bar` 模式下生效，且默认为medium。   - `medium`：6px 轨道。 - `small`：4px 轨道。   **[!NOTE]**   - 当`rounded` 为 true 时，圆角为轨道高度的一半。 - 当`variant`为 block 时，固定为 32×32。 |
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
  "component": "ProgressBar",
  "value": 0
}
```

## **计时（ElapsedTime）**

正向计时。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `startTime` | number | 否 | 开始时间戳，单位毫秒，默认为 0。  **[!NOTE]**  若需确定开始时间，请设置时间戳。 |
| `prefix` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 左侧文字，不填写不显示前缀文字。 |
| `suffix` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 右侧文字，不填写不显示后缀文字。 |
| `gravity` | left | center | right | 否 | 对齐方式，默认为 left。 |
| `textStyleType` | string | 否 | 文字样式类别。  **[!NOTE]**  当前实现始终使用 `Standard`，设置该字段不会切换为自定义样式。 |
| `textStyle` | string | 否 | 文字样式预设。  **[!NOTE]**  无论该字段如何设置，当前实现始终使用 `paragraph`。 |
| `weight` | number | 否 | Flex 布局权重，仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ElapsedTime"
}
```

## **倒计时（Countdown）**

倒计时，支持结束事件。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `endTime` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 是 | 倒计时目标时刻的 Unix 毫秒时间戳。   - 字面量、数据绑定的求值结果和函数调用的返回值都必须是 JSON 数字。 - 不接受数字字符串或 ISO 8601 日期时间字符串。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`onComplete`、`onTap`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `prefix` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 倒计时左侧的文字，不填写不显示前缀文字。 |
| `suffix` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 倒计时右侧的文字，不填写不显示后缀文字。 |
| `gravity` | left | center | right | 否 | 对齐方式，默认为 left。 |
| `textStyleType` | string | 否 | 文字样式类别。  **[!NOTE]**  当前实现始终使用 `Standard`，设置该字段不会切换为自定义样式。 |
| `textStyle` | string | 否 | 文字样式预设。  **[!NOTE]**  无论该字段如何设置，钉钉当前实现始终使用 `paragraph`。 |
| `onComplete` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 倒计时归零时触发的动作。 |
| `onTap` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 点击组件时执行的动作，只有组件声明了可点击能力时才生效。 |
| `weight` | number | 否 | Flex 布局权重，仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Countdown",
  "endTime": 0
}
```

## **视频（Video）**

视频，支持封面、内嵌播放和控制栏。当前实现关闭自动播放和循环播放，开启内嵌播放和控制栏，并配置 16:9、圆角 6 的封面区域，这些设置由渲染器实现决定。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `url` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 要播放的视频 URL。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `posterUrl` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 视频播放前显示的封面图 URL。  **[!NOTE]**  默认不提供自定义封面 URL，封面显示由播放器处理。 |
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
  "component": "Video",
  "url": "https://example.com/REPLACE_WITH_RESOURCE"
}
```

## **音频播放器（AudioPlayer）**

音频，支持封面、标题和播放进度。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `url` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 要播放的音频 URL。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `coverUrl` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 封面图 URL，桌面端和移动端都会渲染，默认播放器不显示封面。  **[!NOTE]**  桌面端显示在播放器左侧，移动端由富文本中的音频节点渲染。 |
| `description` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 音频的描述，例如标题或摘要，默认不提供自定义标题。 |
| `artist` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 作者 / 来源署名，显示在标题一侧。与 `description` 一起构成播放器的文字区，若未配置则不显示。 |
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
  "component": "AudioPlayer",
  "url": "https://example.com/REPLACE_WITH_RESOURCE"
}
```

## **文件（File）**

文件产物，图标根据文件类型确定。点击该行打开文件，行尾另有一个打开按钮。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `fileName` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 带后缀的显示文件名，也是渲染器自动识别文件图标和类型的唯一依据。 |
| `url` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 文件下载 URL。  **[!NOTE]**  可以是需鉴权的绝对 URL，也可以是当前应用能解析的相对 URL。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容 |
| `metadata` | any | 否 | 组件元数据。动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`onPreview`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `mimeType` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 可选的 MIME 类型，只用于补充信息和打开方式，不影响文件图标的选择。 |
| `size` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 可选的文件大小，单位字节，由渲染器格式化为 KB、MB 或 GB，默认不显示文件大小。 |
| `description` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 可选的补充信息，例如文件来源、生成状态或版本。  **[!NOTE]**  不填写时，则根据文件大小和类型生成辅助文字，没有大小时只显示类型。 |
| `previewUrl` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 在线预览页的 URL，若不为空则点击该行打开这个 URL，否则使用 `url`属性配置的URL。   - 当前属性与表示文件本身的 `url` 含义不同。 - 行尾的下载按钮始终使用 `url`，不受该字段影响。 |
| `onPreview` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 点击该行时触发，默认该行没有点击动作。   - **采用先打开、成功后再上报**的两步流程：渲染器先打开 `previewUrl`（`previewUrl` 若为空则打开 `url`），打开成功后才把事件发给 Agent。 - 文件无法打开时不上报事件，因此不需要等待 Agent 返回 `openLink`，所以跳转是即时的。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "File",
  "fileName": "REPLACE_TEXT",
  "url": "https://example.com/REPLACE_WITH_RESOURCE"
}
```

## **图片轮播（ImageCarousel）**

钉钉图片轮播组件。

![图片轮播（ImageCarousel）](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8580370971/p1104316.png)

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件唯一标识，同一画布内不可重复。 |
| `items` | object[] | 是 | 轮播项，`url`必填，`linkUrl`、标题和描述可选。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `cornerRadius` | [DynamicNumber](0010-json-card-common-types.md#a61dabef73gpz) | 否 | 圆角，单位 px，默认值 12px。  **[!NOTE]**   - 请使用有限的非负数，0px为直角。 - 桌面端作用于轮播图片，移动端用外层容器裁剪图片组。 |
| `autoplayIntervalMs` | integer | 否 | 自动滚动间隔，单位 ms，默认为 0（关闭），不自动滚动。 |
| `previewEnabled` | boolean | 否 | 点击是否可以预览，默认为 true。  **[!NOTE]**  只有存在可加载的图片 URL 时才开启预览。 |
| `fit` | contain | cover | fill | none | scaleDown | 否 | 图片缩放方式，取值与 CSS `object-fit` 一致：   - `contain`/`scaleDown`/`none`：完整显示 - `cover`：裁剪填充 - `fill`：拉伸填充   **[!NOTE]**  **只在显式提供时下发**，取值之外的值（包括 `fitCenter`/`fitXY`/`centerCrop` 这类内部名称）会被静默恢复为默认值。 |
| `weight` | number | 否 | Flex 布局权重，仅作为 Row/Column 直接子组件时生效。 |
| `fallbackMarkdown` | string | 否 | 渲染器不支持时的 Markdown 降级内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "ImageCarousel",
  "items": [
    {
      "url": "REPLACE_TEXT"
    }
  ]
}
```
