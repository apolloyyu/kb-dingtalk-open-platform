---
title: "全局配置介绍"
source_url: "https://open.dingtalk.com/document/development/global-configuration-overview-1"
namespace: "development"
slug: "global-configuration-overview-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序全局配置 > 全局配置介绍"
doc_id: "MK5LY2B3cP"
updated_at: "2025-09-17 20:57:50"
---

> Source: https://open.dingtalk.com/document/development/global-configuration-overview-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序全局配置 > 全局配置介绍
> Updated: 2025-09-17 20:57:50

# 全局配置介绍

App代表顶层应用，管理所有页面和全局数据，以及提供生命周期方法。它也是一个构造方法，生成App实例。一个小程序就是一个App实例。

每个小程序的顶层一般包含三个文件。

| 文件 | 是否必须 | 说明 |
| --- | --- | --- |
| app.js | 是 | 小程序逻辑 |
| app.json | 是 | 小程序公共配置 |
| app.acss | 否 | 小程序公共样式表 |

小程序根目录下的 `app.json` 文件用来对钉钉小程序进行全局配置，决定页面文件的路径、窗口表现、设置网络超时时间、设置多 tab 等。文件内容为一个 JSON 对象。

下面是一个简单的 `app.json`示例。

```
{
   "pages":[
      "pages/index/index",
      "pages/logo/logo",
      "pages/B/B"
   ],
   "window":{
      "defaultTitle":"Demo",
      "allowsBounceVertical":"NO",
      "pullRefresh":false
   },
   "tabBar":{
      "textColor":"#dddddd",
      "selectedColor":"#49a9ee",
      "backgroundColor":"#ffffff",
      "items":[
         {
            "pagePath":"pages/index/index",
            "name":"首页"
         },
         {
            "pagePath":"pages/logo/logo",
            "name":"日志"
         }
      ]
   }
}
```

上面配置指定小程序包含两个页面，以及应用窗口的默认标题是 `Demo`。

`App` 提供四个事件，可以设置钩子方法。

1. onLaunch：小程序启动
2. onShow：小程序切换到前台
3. onHide：小程序切换到后台
4. onError: 小程序出错

一个简单的`app.js`代码如下。

```
App({
  onLaunch(options) {
    // 初始化
  },
  onShow(options) {
    // 显示
  },
  onHide() {
    // 隐藏
  },
  onError(msg) {
    console.log(msg)
  },
  globalData: {
    foo: true,
  }
})
```
