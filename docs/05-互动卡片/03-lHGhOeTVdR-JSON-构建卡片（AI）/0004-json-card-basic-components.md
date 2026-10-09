---
title: "基础组件"
source_url: "https://open.dingtalk.com/document/development/json-card-basic-components"
namespace: "development"
slug: "json-card-basic-components"
group: "互动卡片"
tab: "JSON 构建卡片（AI）"
breadcrumb: "构建卡片结构 > 组件 > 基础组件"
doc_id: "aOjtrLc9jo"
updated_at: "2026-09-30 09:14:27"
---

> Source: https://open.dingtalk.com/document/development/json-card-basic-components
> Path: 互动卡片 / JSON 构建卡片（AI） / 构建卡片结构 > 组件 > 基础组件
> Updated: 2026-09-30 09:14:27

# 基础组件

本文档汇总钉钉互动卡片全部基础组件的属性说明与使用示例。每个组件包含属性表格和 JSON 构建代码，供开发者快速查阅。

## 文本（Text）

文本，支持字号、颜色与流式状态。`textEffect` 可添加扫光效果。

### **属性说明**

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `text` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 要显示的文本内容。   - 支持字面量、数据绑定和值函数。 - **不接受** `{content, i18n}` **这类对象形式**。 - 多语言文案需由服务端本地化后再发送。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`onLinkClick`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `variant` | caption \body | 否 | 文本样式预设，默认为body，字号与行高优先取设置的样式 Token。   - 取不到时，`body` 在桌面端回落为 14/21、移动端为 17/21（字号/行高），`caption` 在桌面端为 12/18、移动端为 12/16。 - 成功解析显式 `sizeToken` 优先级更高。 - 这些回落数值并非所有客户端的固定值。 |
| `sizeToken` | [SizeToken](0010-json-card-common-types.md#33c3267aafyn4) | 否 | DDesign 原生字号 Token ID，名称与用途见公共类型 `SizeToken`。   - 需填写完整的 `_fontsize` 键，优先级高于 `variant`。 - 行高会尝试使用对应的 `_lineheight` Token，解析不到时回落到 `variant` 预设。 - 不使用 `font-size/body` 这类设计标注名或不带后缀的样式名。 |
| `bold` | boolean | 否 | 文本是否加粗。 |
| `italic` | boolean | 否 | 文本是否斜体。 |
| `strikeThrough` | boolean | 否 | 是否添加删除线。 |
| `colorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即 `commonlevel1base_color` 这类 DDesign Token 名。   - 渲染器调用设计 Token 服务，钉钉按**当前客户端平台与主题**解析颜色，这是保持多端颜色一致的首选方式。 - 它的优先级最高：解析成功时忽略 `color`、`customLightColor` 和 `customDarkColor`。 - 未解析成功，按后续颜色来源依次取值。 |
| `customLightColor` | string | 否 | 浅色模式下的自定义文字颜色（十六进制）。 |
| `customDarkColor` | string | 否 | 深色模式下的自定义文字颜色（十六进制）。   - 渲染器按当前主题选择浅色或深色的值下发。 - 主题切换在卡片下一次刷新后生效。 |
| `maxLine` | integer | 否 | 超过该行数后截断，默认只显示3行，长文本会被静默截断。  **[!NOTE]**  要完整显示，请设置一个足够大的值。 |
| `icon` | object | 否 | 语义前置图标。   - `{"name":"icon library name"}` 与 `{"url":"light-theme URL","darkUrl":"dark-theme URL"}` 二者只能选一种。 - `darkUrl` 可选，缺省时使用 `url`。 - `name` **与** `url` **必须且只能提供一个**，两个都提供或都不提供均无效。 - `textEffect` 互斥：带 `textEffect` 的 `Text` 组件走另一条渲染路径，没有图标位。 - 两者同时下发时，保留图标、忽略效果。 |
| `textEffect` | shimmer | 否 | 文本呈现效果。   - `shimmer` 让高光反复扫过文字，适用于「思考中…」这类流式等待状态，省略时不加效果，用在 `CollapsiblePanel` 上时作用于面板标题。 - 该字段对所有客户端一致下发，目前仅 iOS 生效，不支持的客户端会静默忽略，按普通文本渲染，文字本身不受影响。 - 这些客户端后续支持时无需修改协议。 |
| `onLinkClick` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | - 取值必须是基础协议中的 `Action`：`event` 分支上报给 Agent，`functionCall` 分支在渲染器本地执行。 - 当前实现简化为「点击 `Text` 节点任意位置」：点击文本的任何部分都会触发该动作，且事件不会携带被点击的是哪个链接。 - 该字段适合「用户阅读了这段含链接的文本」这类粗粒度统计，无法区分用户点了哪个链接。 - 链接跳转本身不受影响：渲染器直接打开链接，不经过卡片事件系统。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### **注意事项**

- 优先使用已注册、以 `\\font\_size` 结尾的完整 `sizeToken` ID，其他字符串如何处理由设置的降级规则决定。
- 优先使用 `colorToken`，自定义主题色只用约定的 `customLightColor` / `customDarkColor`，不要添加 color。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Text",
  "text": "REPLACE_TEXT"
}
```

## **富文本（Markdown）**

Markdown，支持标题、列表、代码与引用。

### **属性说明**

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `content` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | Markdown 正文。   - 除标准 Markdown 外，钉钉还支持以下 @ 提及扩展：`<a atId="{openDingTalkId}">nickname</a>` 提及指定成员，`<a atId="all">everyone</a>` 提及所有人（`all` 是保留 ID）。 - 正文中出现的每个 `atId` 都必须列在创建卡片参数 `atIdList` 中，保留 ID `all` 不需要列出。 - 服务端会把每个 `openDingTalkId` 解析为对应用户，标签内只写显示名称，不要自己加 `@`。 - 渲染器渲染 at 节点时会自动在前面加 `@`，自己写的话会显示成 `@@` - 如果某个 `atId` 没有列出或无法解析，会降级为没有高亮和点击行为的纯文本，并且不报错。 - IM Markdown 消息使用的 `<@openDingTalkId>` 与 `<@all>` 占位写法在卡片链路中**不生效**，会按原文显示。 - 服务端解析 `openDingTalkId` 的能力尚未上线，因此目前提及不会生效，会按上文所述降级为纯文本，上线后正文语法和该字段的约定保持不变。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### **注意事项**

- 当前协议把 `<a atId>` 描述为纯文本降级，不保证可以点击提及，标签内只写显示名称。
- 不相关的主题拆到不同的 `Column` 或 `Card` 分组中，不要全部塞进一个 Markdown。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Markdown",
  "content": "REPLACE_TEXT"
}
```

## **图片（Image）**

图片展示，支持深色主题的替换图，省略 `variant` 时，钉钉当前实现渲染为整行宽、高 200 的图片，但是实际可用宽度仍受父级布局约束。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `url` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 浅色模式及默认的图片 URL。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `darkUrl` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 否 | 深色模式的图片 URL，未配置时渲染器继续使用该 URL。 |
| `fit` | contain | cover | fill | none | scaleDown | 否 | 图片在容器内的缩放方式。   - 不填写时，钉钉当前实现为裁剪填充，对应 `cover`，与官方 Basic Catalog 默认的 `fill` 不同。 - 请从本字段的取值中选择，控制包含、裁剪或拉伸。 |
| `variant` | icon | avatar | smallFeature | mediumFeature | largeFeature | header | 否 | 图片尺寸与样式提示，不填写时整行宽、高 200，非官方 Basic Catalog 默认的 `mediumFeature`。  钉钉当前尺寸为：   - `icon`：24×24 - `avatar`：40×40 - `smallFeature`：96×96 - `mediumFeature`：160×120 - `largeFeature`：320×200 - `header`：整行宽、高 200。   **[!NOTE]**  实际可用宽度受父级约束，客户端需接入对应实现。 |
| `cornerRadius` | number | 否 | 图片圆角，单位 px，默认为6px，0px为直角。   - `ImageList` 默认 4，`ImageCarousel` 默认 12。 - 圆角会裁剪图片的外层容器，请使用有限的非负数。 |
| `previewEnabled` | boolean | 否 | 是否允许点击图片打开大图预览，默认 true。   - 默认开启：未设置该字段时，只要 `url` 是渲染器能加载的地址，图片就可点击。 - 要作为纯展示图片，请显式设置 `false`。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### 注意事项

- 协议层没有 URL 协议白名单；非 HTTPS 地址能否使用取决于自己。
- `smallFeature` 最大 96×96；配文字时，标题控制在两行以内、摘要控制在三行以内，避免变形。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Image",
  "url": "https://example.com/REPLACE_WITH_RESOURCE"
}
```

## **图标（Icon）**

钉钉图标集，支持加载状态。当前图标尺寸为 14，行高 22。没有可解析的颜色配置时使用内置的浅色/深色颜色；有效的显式颜色优先。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `name` | [IconName](0010-json-card-common-types.md#bb5c0a95f7ith) | [DataBinding](0010-json-card-common-types.md#bba245c003o5j) | [FunctionCall](0010-json-card-common-types.md#3313ec177dzpl) | 是 | 只能使用下方 `IconName` 列表中的 24 个名称，区分大小写。   - 支持数据绑定和值函数，但结果也必须是列表中的名称。 - 不接受 SVG 对象、图片 URL 或自定义的语义别名。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `colorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即 `commonlevel1base_color` 这类 DDesign Token 名。   - 渲染器调用设计 Token 服务，钉钉按当前客户端平台与主题解析颜色，这是保持多端颜色一致的首选方式。 - 它的优先级最高：解析成功时忽略 `customLightColor` 和 `customDarkColor`。 - 不能解析时，按后续颜色来源依次取值。 |
| `customLightColor` | string | 否 | 浅色模式的自定义颜色（十六进制）。 |
| `customDarkColor` | string | 否 | 深色主题的自定义颜色，十六进制。渲染器按当前主题选择浅色或深色的值下发。主题切换在卡片下一次刷新后生效。 |
| `weight` | number | 否 | Flex 布局权重，用于按比例分配空间。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Icon",
  "name": "Search_L_outlined"
}
```

## **分割线（Divider）**

水平或垂直分割线。

### **属性说明**

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `axis` | horizontal | vertical | 否 | 分割线方向，默认 horizontal。   - `vertical` 用于同一行内元素之间的竖向分隔（例如底部操作栏里按钮之间的分隔），以固定线宽渲染，高度拉伸到父容器高度，因此**父容器必须是** `Row`**，且该行内元素高度一致**。 - 跨多行的通高竖条也用它，放在 `Row` 的第一个位置，线宽和颜色由 `borderWidth` / `borderColor` 控制。 |
| `borderWidth` | number | 否 | 线的粗细，单位 px，默认 0.5px，即设计规范中的细线值，取值必须是有限的非负数。   - 名称与取值含义和 `Row`、`Column`、`Card`、`Stack` 上的同名字段一致，对应 CSS 的 `border-width`。 - 无论方向如何，它始终表示线的粗细：`axis` 为 `horizontal` 时决定线高，`axis` 为 `vertical` 时决定线宽。 - 无效值会被静默丢弃并回落为 0.5px，不会导致卡片失败。 |
| `borderColor` | string | 否 | 线的颜色，格式为 `#AARRGGBB`，默认 `#1F111F2C`，约 12% 不透明度的中性灰。   - 对应 CSS 的 `border-color`。 - 只接受单个颜色值，不支持 `{light,dark}` 成对取值，因此颜色不随主题变化。 - 若需随主题变化，请使用下方的 `borderColorToken`。 |
| `borderColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即线条颜色的 DDesign Token 名。   - 优先级高于 `borderColor` ，也是让分割线跟随浅色与深色主题的唯一方式。 - 设计系统的线条色有两组：    - `commonlinelightcolor`：浅色模式 16%、深色模式 10%   - `common``linehardcolor`：浅色模式 24%、深色模式 18% - 旧的默认值 `#1F111F2C` 与两者都不同，要与设计系统保持一致，请显式指定 Token。 - 客户端解析不到时视为未填写，回落到 `borderColor`，不报错。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### **JSON 结构**

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Divider"
}
```

## **标签（Tag）**

语义标签，`theme` 统一决定文字颜色、背景色、边框颜色和边框宽度。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `text` | [DynamicString](0010-json-card-common-types.md#6b74f28968uj6) | 是 | 标签文字。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `theme` | black | gray | red | orange | green | blue | 否 | **语义主题：一个取值同时决定文字颜色、背景色、边框颜色和边框宽度**，默认为 gray。   - 这些搭配由设计系统固定，因此不接受任意十六进制颜色。 - **与** `Text` **和** `Icon` **上的** `color` **字段不同**，后者只指定单一前景色，这里是整套标签配色，所以命名为 `theme`，与 `CardHeader.theme` 保持一致。 - 未知取值回落为 `gray`，不报错。 |
| `variant` | filled | hollow | 否 | 标签样式，默认 `filled`。  **两种样式互斥**：   - `filled` 使用 `theme` 12% 不透明度的背景、无边框； - `hollow` 背景透明，使用 `theme` 48% 不透明度的 1px 边框。   **[!NOTE]**  两者文字颜色相同，**标签不能同时有填充背景和边框**，需要这种效果时请用 `Row` 组合实现。 |
| `maxWidth` | number | 否 | 标签最大宽度，单位 px，默认999px，是一个数值上限而不是不限宽，超出部分的文字会被截断。 |
| `weight` | number | 否 | Flex 布局权重。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### 注意事项

- 保持主题色与含义一致。
- 取值以本协议的枚举为准。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Tag",
  "text": "REPLACE_TEXT"
}
```

## **卡片容器（Card）**

单子组件的卡片容器，带内边距、背景和圆角。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `child` | [Child](0010-json-card-common-types.md#1fb1d1713fvjp) | 是 | 卡片内要渲染的唯一子组件的 ID。   - 要显示多个元素，必须先用布局组件（如 `Column` 或 `Row`）包起来，再把该容器的 ID 填在这里。 - 不要填多个 ID，也不要填不存在的 ID。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `backgroundColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即卡片底色的 DDesign Token 名，例如 `commonbgcolor`。   - 钉钉按当前客户端平台、主题和租户解析，这是保持底色在多端、多主题下一致的首选方式。 - 优先级高于 `backgroundColor`。 - 客户端解析不到时视为未填写，继续按 `backgroundColor` 取值，若该字段未填写时使用默认底色。 |
| `backgroundColor` | string | object | 否 | 卡片底色，支持两种形式：   - `#AARRGGBB` 格式的字符串是**单一取值**，不随浅色或深色主题变化。 - `{"light":"#…","dark":"#…"}` 提供**浅色和深色两个取值**，由渲染器按当前主题选择，**推荐使用**。   **[!NOTE]**  省略时使用默认底色：浅色模式为 `#FFFFFFFF`，深色模式为 `#FF1F1F1F`。 |
| `cornerRadius` | number | 否 | 卡片底面圆角，单位 px，默认 8px，必须是非负数。 |
| `borderWidth` | number | 否 | 边框宽度，单位 px，默认 0px，即无边框。  **[!NOTE]**  若要显示边框，需同时配置 `borderColor`。 |
| `borderColor` | string | 否 | 描边颜色，十六进制。   - 只有同时设置了 `borderWidth` 才可见。 - 设置颜色后会自动使用实线样式。 |
| `borderColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即边框颜色的 DDesign Token 名。   - 优先级高于 `borderColor` ，钉钉按当前客户端平台、主题和租户解析。 - 这是让边框跟随浅色与深色主题的唯一方式：`borderColor` 只接受单个取值，在深色模式下保持不变。 - 线条色有 `commonlinelightcolor` 和 `common``linehardcolor` 两组，实际色值与不透明度需自行解析。 - 客户端解析不到时视为未填写，继续按 `borderColor` 取值，不报错。 |
| `padding` | number | 否 | 四边统一的内边距，单位 px，默认 12px。  **[!NOTE]**  必须是不小于 0 的数字。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### **JSON 结构**

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Card",
  "child": "REPLACE_CHILD_ID"
}
```

## **行（Row）**

子节点从左到右排列。

### **属性说明**

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 定义子组件。   - 固定的一组子组件用字符串数组。 - 按数据列表生成子组件时用模板对象。 - 子组件不能内联定义，只能通过 ID 引用。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据。  动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `justify` | start | center | end | spaceBetween | spaceAround | spaceEvenly | stretch | 否 | 主轴布局，7 个取值与官方定义一致。   - `start`、`center`、`end` 控制子组件在主轴上的位置。 - `spaceBetween`、`spaceAround`、`spaceEvenly` 按与 CSS `justify-content` 完全相同的方式分配剩余空间（`gap` 仍只作用于相邻子组件之间，不会加在两端）。 - `spaceBetween` **且只有两个子组件时**：内容放得下时定位与 CSS 一致；最后一项过长时会在剩余宽度内换行，而不是溢出。 - 其他排列方式下，一旦行内出现带权重的子组件，后续子组件会按整行宽度测量，一行放不下的内容会溢出并被裁剪，长文本请给子组件设置 `weight`。 - 只要有子组件已设置 `weight`，就不再分配剩余空间，这与官方的 flex-grow 行为一致。 - 在 flex 行上，`stretch` 等同于 `start`，省略时为 `start`。 |
| `align` | start | center | end | stretch | 否 | 交叉轴对齐。   - `start`、`center`、`end` 控制子组件的垂直位置。 - 默认值 `stretch` 让子组件等高，与官方 `align-items: stretch` 的语义一致：容器类子组件（`Row`、`Column`、`Card` 和垂直方向的 `Divider`）拉伸到整行高度。 - `Text`、`Image`、`Button` 这类叶子组件和复合组件保持自身高度并顶部对齐，其 `weight`、间距和可见性不受影响。 - 等高生效时，被拉伸的子 `Column` 上的 `justify` 取值 `center`、`end`、`spaceBetween`、`spaceAround`、`spaceEvenly` 就能体现出效果。   **[!NOTE]**   - 组件 `id` 不能写成 `<Row id>__stretch.<n>` 的形式，这是布局保留的命名，冲突时整行会放弃等高。 - 在 `Column` 和 `List` 中，`stretch` 决定子组件是撑满可用宽度，还是按内容确定尺寸。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `backgroundColor` | string | 否 | 容器背景色，十六进制的 `#RRGGBB` 或 `#AARRGGBB` 格式，8 位形式中 Alpha 在前，默认是背景透明。   - 只接受单个颜色字符串，不支持 `{light,dark}` 对象，因此颜色不随主题变化。 - 深色主题要用不同颜色时，请发送更新后的组件定义。 |
| `cornerRadius` | number | 否 | 圆角，单位 px，不填写时不设置显式圆角，沿用容器的默认样式。   - 需要确定的外观时请设置一个非负数。 - 小数会被截断而不是四舍五入。 |
| `borderWidth` | number | 否 | 描边宽度，单位 px，必须是数字。   - 配置后自动使用实线样式，不能指定其他线型。 - 必须与 `borderColor` 成对配置才会绘制出可见的描边。 |
| `borderColor` | string | 否 | 描边颜色，取值格式与 `backgroundColor` 相同。   - 必须与 `borderWidth` 成对配置。 - 只提供颜色、不提供宽度时不会绘制线条。 |
| `borderColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即边框颜色的 DDesign Token 名。   - 优先级高于 `borderColor` ，钉钉按当前客户端平台、主题和租户解析。 - 让边框跟随浅色与深色主题的唯一方式：`borderColor` 只接受单个取值，在深色模式下保持不变。 - 线条色有 `commonlinelightcolor` 和 `common``linehardcolor` 两组，实际色值与不透明度自行解析。 - 客户端解析不到时视为未填写，继续按 `borderColor` 取值，不报错。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 让整个容器可点击。与 `Button.action` 的 `Action` 语义相同：`event`（上报给 Agent）和 `functionCall`（由渲染器本地执行）必须且只能出现一个。 |
| `padding` | number | 否 | 四边统一的内边距，单位 px，必须是不小于 0 的数字。   - 有背景色的容器通常需要设置，否则子内容会紧贴色块边缘。 - 只支持四边统一的取值，暂不支持单独设置某一边或 `paddingX`/`paddingY`。 - 未配置时不会下发该字段，与历史版本行为一致。 - 不填写不等同于显式设为 0：卡片根节点仍可能从卡片布局获得各平台的内衬，而嵌套容器省略该字段时不会增加内边距。 |
| `gap` | number | 否 | 子组件之间的间距，单位 px，必须是非负数。   - `Column` 作用于纵向，`Row` 作用于横向，第一个子组件不受影响。 - 不填写沿用按层级区分的默认值：卡片顶层区块之间为 8，嵌套的列内为 12，横向为 8，因此现有卡片的间距保持不变。 |
| `backgroundColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即容器背景的 DDesign Token 名，例如 `commonbgcolor`。   - 钉钉按当前客户端平台、主题和租户解析，它的优先级高于 `backgroundColor`。 - 这是该组件让背景跟随深色模式的唯一方式。 - `backgroundColor` 只接受单个颜色值，不随主题变化。 - 客户端解析不到时视为未填写，继续按 `backgroundColor` 取值，不报错。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### **注意事项**

- `align`\=stretch 会让行内子组件在交叉轴上拉伸，具体布局由目标客户端实现。
- 相邻条目较多时，按目标宽度换行或分组，组件数量不是协议层面的限制。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Row",
  "children": [
    "REPLACE_CHILD_ID"
  ]
}
```

## **列（Column）**

子节点从上到下堆叠。

- 作为卡片根节点、省略内边距且没有通栏 `CardHeader` 时，卡片布局会提供水平内衬（桌面端 16、移动端 12），上下内衬为 10。
- 移动端最后一个可见区块是 Markdown 时，下内衬变为 14。
- 嵌套的 Column 不会自动获得这些根节点内衬。

### 属性说明

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `children` | [ChildList](0010-json-card-common-types.md#1d4d9df91ezo0) | 是 | 定义子组件。   - 固定的一组子组件用字符串数组。 - 按数据列表生成子组件时用模板对象。 - 子组件不能内联定义，只能通过 ID 引用。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据，宿主动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `justify` | start | center | end | spaceBetween | spaceAround | spaceEvenly | stretch | 否 | 主轴布局。   - `Column` 通常按内容确定尺寸，没有剩余空间，因此 `spaceBetween`、`spaceAround`、`spaceEvenly` 和 `stretch` 在这里的表现与官方 flex 列完全相同，效果等同于 `start`（接受，不报错）。 - 唯一有剩余高度的情况是该列作为等高行的子组件被拉伸到行高（见 `Row` 的 `align`）：此时 `center` 和 `end` 正常生效，`spaceBetween`、`spaceAround`、`spaceEvenly` 按与 `Row` 相同的规则分配剩余高度（只要有子组件已设置 `weight` 就不分配）。   **[!NOTE]**   - 组件 `id` 不能写成 `<Column id>__justify.<n>` 的形式，这是布局保留的命名。 - 冲突时该列的 `justify` 失效，但整行的等高不受影响，省略时为 `start`。 |
| `align` | center | end | start | stretch | 否 | 定义子组件在交叉轴（水平方向）上的对齐方式，类似 CSS 的 align-items 属性。   - 省略时为 `stretch`。 - 子组件是否撑满可用宽度，还取决于它自身的固定尺寸和父级约束。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `backgroundColor` | string | 否 | 容器背景色，十六进制的 `#RRGGBB` 或 `#AARRGGBB` 格式，8 位形式中 Alpha 在前，默认是背景透明。   - 只接受单个颜色字符串，不支持 `{light,dark}` 对象，因此颜色不随主题变化。 - 深色主题要用不同颜色时，请发送更新后的组件定义。 |
| `cornerRadius` | number | 否 | 圆角，单位 px，省略时不设置显式圆角，沿用容器的默认样式。   - 需要确定的外观时请设置一个非负数。 - 请使用数字，小数会被截断而不是四舍五入。 |
| `borderWidth` | number | 否 | 描边宽度，单位 px，必须是数字。   - 配置后自动使用实线样式，不能指定其他线型。 - 必须与 `borderColor` 成对配置才会绘制出可见的描边。 |
| `borderColor` | string | 否 | 描边颜色，取值格式与 `backgroundColor` 相同。   - 必须与 `borderWidth` 成对配置。 - 只提供颜色、不提供宽度时不会绘制线条。 |
| `borderColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即边框颜色的 DDesign Token 名。   - 优先级高于 `borderColor` ，钉钉按当前客户端平台、主题和租户解析。 - 这是让边框跟随浅色与深色主题的唯一方式：`borderColor` 只接受单个取值，在深色模式下保持不变。 - 线条色有 `commonlinelightcolor` 和 `common``linehardcolor` 两组，实际色值与不透明度自行解析。 - 客户端解析不到时视为未填写，继续按 `borderColor` 取值，不报错。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 否 | 让整个容器可点击，与 `Button.action` 的 `Action` 语义相同：`event`（上报给 Agent）和 `functionCall`（由渲染器本地执行）必须且只能出现一个。 |
| `padding` | number | 否 | 四边统一的内边距，单位 px，必须是不小于 0 的数字。   - 有背景色的容器通常需要设置，否则子内容会紧贴色块边缘。 - 只支持四边统一的取值，暂不支持单独设置某一边或 `paddingX`/`paddingY`。 - 未填写不会下发该字段，与历史版本行为一致。 - 未填写不等同于显式设为 0：卡片根节点仍可能从卡片布局获得各平台的内衬，而嵌套容器省略该字段时不会增加内边距。 |
| `gap` | number | 否 | 子组件之间的间距，单位 px，必须是非负数。   - `Column` 作用于纵向，`Row` 作用于横向，第一个子组件不受影响。 - 省略时沿用按层级区分的默认值：卡片顶层区块之间为 8，嵌套的列内为 12，横向为 8，现有卡片的间距保持不变。 |
| `backgroundColorToken` | [ColorToken](0010-json-card-common-types.md#9e4a3330d5upi) | 否 | 只能使用公共 `ColorToken` 枚举中的 57 个 ID，即容器背景的 DDesign Token 名，例如 `commonbgcolor`。   - 钉钉按当前客户端平台、主题和租户解析，优先级高于 `backgroundColor`。 - 这是该组件让背景跟随深色模式的唯一方式。 - `backgroundColor` 只接受单个颜色值，不随主题变化。 - 客户端解析不到时视为未填写，继续按 `backgroundColor` 取值，不报错。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### **注意事项**

- `children` 纵向排列内容。空数组在结构上合法，只在有用时保留。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Column",
  "children": [
    "REPLACE_CHILD_ID"
  ]
}
```

## **按钮（Button）**

公开的 `Button` 组件。`disabled` 会让按钮置灰并移除点击动作。

![基础组件-按钮](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7680370971/p1104187.png)

### **属性说明**

| **属性** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| `id` | [ComponentId](0010-json-card-common-types.md#2cbbc8ceb036k) | 是 | 组件的唯一标识，在同一画布内既用于定义组件，也用于引用组件。 |
| `child` | [Child](0010-json-card-common-types.md#1fb1d1713fvjp) | 是 | 子组件的 ID。   - 带文字的按钮使用 `Text` 组件。 - 只有需求明确要求纯图标按钮时才使用 `Icon`。 |
| `action` | [Action](0010-json-card-common-types.md#3d860c6514irj) | 是 | 定义交互处理器，可以触发 Agent 侧事件，也可以执行渲染器本地函数。   - 钉钉实现：虽然契约要求必填，但缺失或无效时按钮不会消失。 - 按钮照常渲染文字和颜色，点击时提示「当前版本不支持该操作」。 - 无效的动作不影响渲染，渲染只要求 `child`。 |
| `catalogId` | string | 否 | 组件级 `catalogId`，覆盖画布的默认 Catalog。 |
| `accessibility` | [AccessibilityAttributes](0010-json-card-common-types.md#6c3fe27a7ff5d) | 否 | 为读屏软件等辅助技术提供名称和详细描述。  协议保留、当前不生效：字段本身合法，不会导致校验失败或组件降级，但读屏软件读不到这里配置的内容。 |
| `metadata` | any | 否 | 组件元数据，动作的执行结果可以回写到数据模型：在 `metadata.extensions.dt_actionBindingsV1.<槽位>.resultPath` 中声明路径（本组件的槽位：`action`），路径只能是 `/ui/` 下的对象键，见 [HostActionBinding](0010-json-card-common-types.md#0e16fb95edx0m)。 |
| `checks` | [CheckRule](0010-json-card-common-types.md#496ab27c64dc7)[] | 否 | 要执行的校验列表，每一项都是返回布尔值、表示是否通过的函数调用。   - 钉钉实现：点击时基于最新的数据模型执行校验，任一校验不通过会阻止点击并弹出 toast 提示。 - 这是挂载表单校验的标准位置：规则用 `path` 引用输入组件绑定的路径，就能一次校验整个表单。 |
| `variant` | default | primary | borderless | 否 | 按钮样式提示，不填写默认为 default。   - **primary**：标记主操作。 - **borderless**：去掉背景和边框。   **[!NOTE]**  当`disabled` 为 `true` 时，禁用色优先。 |
| `weight` | number | 否 | 该组件在 `Row` 或 `Column` 中的相对权重，类似 CSS 的 flex-grow 属性。  **[!NOTE]**  只有当组件是 `Row` 或 `Column` 的直接子组件时才能设置。 |
| `disabled` | boolean | 否 | 按钮是否禁用，不填写时默认false。  **[!NOTE]**  为 `true` 时，当前实现使用禁用色且不挂点击动作，按钮和文字仍然可见。 |
| `fallbackMarkdown` | string | 否 | 当前渲染器无法渲染该组件时，改为显示的 Markdown 内容。 |
| `visible` | [DynamicBoolean](0010-json-card-common-types.md#e82066479fgkv) | 否 | 可见性控制（布尔表达式或字面量）。 |

### 注意事项

- 按动作的主次选择 `variant`。校验器不限制主按钮的数量。
- 把 `bizId` 这类业务 ID 放进 `action.event.context`，便于回调时归属到对应卡片。
- `child` 引用一个 `Text` 组件的 ID，不要把按钮文字直接写在 `Button` 上。

### JSON 结构

下面是该组件的最小结构，只包含必填字段。

- `REPLACE_` 开头的值需要替换。
- 写好后可用 `dws aicard lint --file <文件> --fragment` 单独校验。

```
{
  "id": "REPLACE_ID",
  "component": "Button",
  "child": "REPLACE_CHILD_ID",
  "action": {
    "event": {
      "name": "REPLACE_TEXT"
    }
  }
}
```
