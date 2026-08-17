---
title: "app.json全局配置"
source_url: "https://open.dingtalk.com/document/development/app-json-global-configuration-1"
namespace: "development"
slug: "app-json-global-configuration-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序全局配置 > app.json全局配置"
doc_id: "5EX8zbflra"
updated_at: "2025-09-17 20:57:51"
---

> Source: https://open.dingtalk.com/document/development/app-json-global-configuration-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序全局配置 > app.json全局配置
> Updated: 2025-09-17 20:57:51

# app.json全局配置

app.json用于全局配置，决定页面文件的路径、窗口表现、设置多 tab 等。

以下是一个包含了部分配置选项的简单配置`app.json`示例：

```
{
  "pages": [
    "pages/index/index",
    "pages/logs/index"
  ],
  "window": {
    "defaultTitle": "Demo"
  }
}
```

`app.json`配置项如下:

| 属性 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| pages | String Array | 是 | 设置页面路径。 |
| window | Object | 否 | 设置默认页面的窗口表现。 |
| tabBar | Object | 否 | 设置底部 tab 的表现。 |

## **pages**

`app.json`中的`pages`属性是一个数组，数组中每一项都是字符串，用于指定小程序的页面。每一项代表对应页面的路径信息，数组的第一项代表小程序的首页。 页面路径不需要写 `js` 后缀，框架会自动去加载同名的`.json`、`.js`、`.axml`、`.acss`文件。

> **[!IMPORTANT]**
>
> 小程序中新增/减少页面，都需要对 `pages`数组进行修改。

如果开发目录为：

```
├── pages
│   ├──index
│   │    ├── index.json
│   │    ├── index.js
│   │    ├── index.axml
│   │    └── index.acss
│   ├──logs
│   │    ├── logs.json
│   │    ├── logs.js
│   │    └── logs.axml
├── app.json
├── app.js
└── app.acss
```

则需要在app.json中写：

```
{
  "pages":[
    "pages/index/index",
    "pages/logs/logs"
  ]
}
```

## **window**

`window`属性用于设置通用的的状态栏、导航条、标题、窗口背景色。子属性如下表所示：

| **属性** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| titleBarColor | HexColor | 否 | 导航栏背景色，HexColor示例：#F5F5F。 |
| defaultTitle | String | 否 | 页面标题。 |
| defaultTitle\_locale | Dict<Language, String> | 否 | 页面标题的多语言配置。 |
| pullRefresh | Boolean | 否 | 是否允许下拉刷新，默认为**false**。 |
| allowsBounceVertical | String | 否 | 页面是否支持纵向拽拉超出实际内容，默认为**YES**。 |
| supportColorScheme | Array | 否 | 支持的显示模式，模式有 light和dark 两种。默认为**light**。 |

> **[!IMPORTANT]**
>
> - HexColor（十六进制颜色值），如"#ff00ff"。
> - 如果要开启下拉刷新事件，需要将pullRefresh设置为 true 。

示例代码：

```
{
  "window":{
    "titleBarColor":"#F5F5F",
    "defaultTitle": "钉钉接口功能演示",
    "pullRefresh":false,
    "allowsBounceVertical":"YES",
    "supportColorScheme":["light"]
  }
}
```

## **tabBar**

如果你的小程序是一个多 tab 应用（客户端窗口的底部栏可以切换页面），那么可以通过`tabBar`配置项指定 tab 栏的表现，以及 tab 切换时显示的对应页面。

> **[!IMPORTANT]**
>
> 通过页面跳转（`dd.navigateTo`）或者页面重定向（`dd.redirectTo`）所到达的页面，即使它是定义在 tabBar 配置中的页面，也不会显示底部的 tab 栏。另外，tabBar的第一个页面必须是首页。

| **属性** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| textColor | HexColor | 否 | 文字颜色。 |
| selectedColor | HexColor | 否 | 选中文字颜色。 |
| backgroundColor | HexColor | 否 | 背景色。 |
| items | Array | 是 | 每个 tab 配置。 |
| colorSchemes | Dict<Scheme, Config> | 否 | 显示模式对应的 tabBar 配置。 |

每个item的属性配置如下表所示:

| **属性** | **类型** | **必填** | **描述** |
| --- | --- | --- | --- |
| pagePath | String | 是 | 设置页面路径。 |
| name | String | 是 | 名称。 |
| name\_locale | Dict<Language, String> | 否 | item名称的多语言配置。 |
| icon | String | 否 | 平常图标路径。 |
| activeIcon | String | 否 | 高亮图标路径。 |
| colorSchemes | Dict<Scheme, Config> | 否 | 显示模式对应的 tabBar Item 配置。 |

> **[!NOTE]**
>
> icon 推荐大小为 60\*60px 大小，系统会对任意传入的图片非等比拉伸/缩放。

示例代码：

```
{
  "tabBar": {
    "textColor": "#dddddd",
    "selectedColor": "#49a9ee",
    "backgroundColor": "#ffffff",
    "items": [
      {
        "pagePath": "pages/index/index",
        "name": "首页"
      },
      {
        "pagePath": "pages/logs/logs",
        "name": "日志"
      }
    ]
  }
}
```

## 相关文档

- [多语言配置](https://open.dingtalk.com/document/dingstart/multi-language-configuration-1)
