---
title: "ACSS样式语法参考"
source_url: "https://open.dingtalk.com/document/development/mini-app-acss-style-syntax-reference"
namespace: "development"
slug: "mini-app-acss-style-syntax-reference"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > ACSS样式语法参考"
doc_id: "ZPXSwWS2Bc"
updated_at: "2025-09-17 20:58:04"
---

> Source: https://open.dingtalk.com/document/development/mini-app-acss-style-syntax-reference
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > ACSS样式语法参考
> Updated: 2025-09-17 20:58:04

# ACSS样式语法参考

ACSS用于描述页面的样式。它是一套样式语言，用于描述 axml 的组件样式，决定 axml 的组件应该怎么显示。

为了适应广大的前端开发者，我们的 acss 具有 css 大部分特性。同时为了更适合开发小程序，我们对 css 进行了扩充。

## **rpx**

rpx（responsive pixel）可以根据屏幕宽度进行自适应。规定屏幕宽为750rpx。如在 iPhone6 上，屏幕宽度为375px，共有750个物理像素，则750rpx = 375px = 750物理像素，1rpx = 0.5px = 1物理像素。

| **设备** | **rpx换****算px (屏****幕宽度/750)** | **px换算rpx (750/屏幕宽****度)** |
| --- | --- | --- |
| iPhone5 | 1rpx = 0.42px | 1px = 2.34rpx |
| iPhone6 | 1rpx = 0.5px | 1px = 2rpx |
| iPhone6 Plus | 1rpx = 0.552px | 1px = 1.81rpx |

## **样式导入**

使用`@import`语句可以导入外联样式表，`@import`后需要加上外联样式表的相对路径，用`;`表示结束。

button.acss样式如下：

```
/** button.acss **/
.sm-button {
  padding:5px;
}
```

app.acss样式：

```
/** app.acss **/
@import "./button.acss";
.md-button {
  padding:15px;
}
```

导入路径支持从 node\_modules 目录载入第三方模块，例如 page.acss:

```
@import "./button.acss"; /*相对路径*/
@import "/button.acss"; /*项目绝对路径*/
@import "third-party/button.acss"; /*第三方 npm 包路径*/
```

## **内联样式**

组件上支持使用`style`、`class`属性来控制样式。

- `style`属性：静态的样式统一写到`class`中。`style`接收动态的样式，样式在运行时会进行解析。

  > **[!IMPORTANT]**
  >
  > 请尽量避免将静态的样式写进`style`中，以免影响渲染速度。

  ```
  <view style="color:{{color}};" />
  ```
- `class`属性：用于指定样式规则，属性值是样式规则中类选择器名(样式类名)的集合，样式类名不需要带上`.`，之间用空格分隔。

  ```
  <view class="my-awesome-view" />
  ```

## **选择器**

同 css3 保持一致，请注意：

- `.a-`, `.am-` 开头的类选择器为系统组件占用，请不要使用。
- 不支持属性选择器。

## **全局样式与局部样式**

定义在`app.acss`中的样式为全局样式，作用于每一个页面。在 Page 的`acss`文件中定义的样式为局部样式，只作用在对应的页面，并会覆盖`app.acss`中相同的选择器。

## **页面容器样式**

可以通过 page 元素选择器来设置页面容器的样式，比如页面背景色:

```
page {
  background-color: red;
}
```

## 暗黑模式

必须正确配置 app.json 文件，小程序才能在系统显示模式切换时自动切换显示模式，获得较好的样式效果。

全局配置 app.json：

```
{
  "window": {
    "supportColorScheme": ["light", "dark"]
  },
  "tabBar": {
    "textColor": "#333", // 兼容不支持 colorSchemes 的旧版本客户端
    "backgroundColor": "#ddd",
    "selectedColor": "#38f",
    "colorSchemes": { // 不同显示模式下的配置
      "light": { // 正常模式下配置，如有将覆盖外部配置
        "textColor": "#333",
        "backgroundColor": "#ddd",
        "selectedColor": "#38f"
      },
      "dark": { // 暗黑模式下配置
        "textColor": "#ddd",
        "backgroundColor": "#333",
        "selectedColor": "#999"
      }
    },
    "items": [{
      "pagePath": "tab_page_path",
      "icon": "path_or_url", // 兼容不支持 colorSchemes 配置的老版本客户端
      "activeIcon": "path_or_url",
      "colorSchemes": { // 不同显示模式下的配置
        "light": {
          "icon": "path_or_url",
          "activeIcon": "path_or_url"
        },
        "dark": {
          "icon": "path_or_url",
          "activeIcon": "path_or_url"
        }
      }
    }]
  }
}
```

页面样式适配：

- 手动适配：手动优化对应页面的 `page.acss`

  ```
  .lightmode .custom_class {
    color: #333;
  }

  .darkmode .custom_class {
    color: #ddd;
  }
  ```
- 使用 css 变量：小程序支持css变量，设置变量并使用可以快速适配显示模式

  ```
  /* app.acss（全局生效） pagePath/index.acss (只对某页面生效) */

  /* 注册 css 变量 */
  .lightmode page {
    --custom-color: #333;
  }

  .darkmode page {
    --custom-color: #ddd;
  }

  /* 在相应的样式文件中使用 css 变量 */
  .example {
    color: #333; /* 兼容 iOS 9.3及以下不支持 css 变量的版本 */
    color: var(--custom-color);
  }
  ```
- 高级用法：小程序新增了关于显示模式的JSAPI和事件。详情请参考[显示模式](https://open.dingtalk.com/document/orgapp/display-mode)。

## 常见问题

**Q：一个 axml 引用多个自定义组件或 template 模板、include 等，造成样式之间相互影响、样式污染怎么办？**

A：请开发者自行通过名空间处理样式隔离。

**Q：给页面设高度100%为什么没用**？

A：添加一个绝对定位就可以了，不添加的话，会根据您的页面的内容去自适应的。
