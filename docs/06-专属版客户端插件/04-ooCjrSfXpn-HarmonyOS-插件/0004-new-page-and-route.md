---
title: "新建页面和路由"
source_url: "https://open.dingtalk.com/document/development/new-page-and-route"
namespace: "development"
slug: "new-page-and-route"
group: "专属版客户端插件"
tab: "HarmonyOS 插件"
breadcrumb: "HarmonyOS 插件 > 新建页面和路由"
doc_id: "6Wi2TuwLfx"
updated_at: "2025-10-15 17:02:14"
---

> Source: https://open.dingtalk.com/document/development/new-page-and-route
> Path: 专属版客户端插件 / HarmonyOS 插件 / HarmonyOS 插件 > 新建页面和路由
> Updated: 2025-10-15 17:02:14

# 新建页面和路由

重点讲述了如何自定义插件的页面，以及如何路由打开页面。

## **新建页面**

> **[!NOTE]**
>
> 鸿蒙端基于 Navigation 实现页面栈的管理，钉钉内部框架存在自定义的NavDestination。插件为了能够定义钉钉样式的页面以及在钉钉栈中路由，需要实现两部分：
>
> - 创建页面配置描述类（DTOpenPage），声明页面的titlebar模型以及页面内容组件的 WrappedBuilder。
> - 页面内容组件类，可从页面的参数中获取路由参数信息，并构建页面View。

1. 创建页面描述类（DTOpenPage）

   关键接口如下描述：

   | **接口** | **说明** |
   | --- | --- |
   | getPageBuilder(): WrappedBuilder<[DTOpenPageParams]> | 获取页面内容 Component 的 WrappedBuilder，DTOpenPageParams 为页面的路由参数等信息。 |
   | getPageConfig(): DTOpenPageConfig | 获取页面的配置信息，当前支持如下字段：  - title：页面标题 - hideTitleBar：是否隐藏页面标题栏（默认 false） - hideBackButton：是否隐藏页面回退按钮（默认 false） - menus：页面右上角按钮菜单，当前仅支持 Text 样式菜单 |

   示例代码：

   ```
   export class TCSettingPage extends DTOpenPage {

     getPageBuilder(): WrappedBuilder<[DTOpenPageParams]> {
       // settingBuilder 的定义请参考后续文档中创建
       return wrapBuilder(settingBuilder)
     }

     getPageConfig(): DTOpenPageConfig {
       return { title: '测试用例' }
     }
   }
   ```
2. 创建页面组件类

   同常规的 Navigation 路由页面定义方式不同的是，此处根组件无需使用 NavDestination 作为根节点。示例代码：

   ```
   @Builder
   function settingBuilder(params: DTOpenPageParam) {
     SettingPageContent({ params: params })
   }

   @ComponentV2
   struct SettingPageContent {
     @Require
     @Param
     params: DTOpenPageParam  // 路由中携带的参数

     build() {
       Column() {
         Text("Hello, Dingtalk")
       }
     }
   }
   ```
3. dingtalk-bundle.json5 中添加页面配置

   首先请在 Index.ets 文件中导出 TCSettingPage，然后添加页面声明配置。

   ```
   "pages": [
       {
         "class": "TCSettingPage",
         "routePath": "tc_settings" // 路由时需要使用的页面path
       }
   ],
   ```

## **路由页面**

1. 路由打开自定义页面

   为了能在其他地方路由并打开页面，需要使用的 Bundle.ets 中定义的全局对象 myBundle。

   ```
   myBundle.routePage({
     component: context.component as CustomComponent,
     path: 'tc_settings',
   })
   ```
2. 路由传递参数

   当前仅支持 Map<string, string> 类型的参数，不支持对象参数。

   ```
   const param = new Map<string, string>()
   param.set("key1", "value1")
   param.set("key2", "value2")

   myBundle.routePage({
     component: context.component as CustomComponent,
     path: 'tc_settings',
     params: param
   })
   ```

   页面使用时可以从 DTOpenPageParam 对象中获取。

   > **[!NOTE]**
   >
   > 假如页面是通过统一路由URI的方式打开，URI中附带的参数将会被自动转成map传递到页面中。
3. 页面关闭回调

   当期望在页面关闭后回调并执行业务逻辑，可使用 onPop 回调函数。

   ```
   myBundle.routePage({
     component: context.component as CustomComponent,
     path: 'tc_settings',
     onPop: () => {
       console.info('页面close')
     }
   })
   ```

> **[!NOTE]**
>
> 假如期望通过 uri 的方式打开，可以使用如下两种的任何一种规范生成自定义页面的统一路由URI。
>
> **规范一：**
>
> `https://applink.dingtalk.com/action/exclusive_open_sdk?bizType=<自定义页面path>`
>
> **规范二：**
>
> `dingtalk://dingtalkclient/action/exclusive_open_sdk?bizType=<自定义页面path>`
>
> 其中，“自定义页面 path” 请替换成插件页面在dingtalk-bundle.json5中配置的path字段值。
