---
title: "全局配置"
source_url: "https://open.dingtalk.com/document/development/app-js-registration-mini-program-1"
namespace: "development"
slug: "app-js-registration-mini-program-1"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序配置 > 全局配置"
doc_id: "pVuYFDGGNe"
updated_at: "2026-09-01 09:16:04"
---

> Source: https://open.dingtalk.com/document/development/app-js-registration-mini-program-1
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 小程序配置 > 全局配置
> Updated: 2026-09-01 09:16:04

# 全局配置

## **全局配置介绍**

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

## **app.js注册小程序**

> **[!IMPORTANT]**
>
> `App()`必须在`app.js`里调用，且不能调用多次。

### **Object属性说明**

| **属性** | 类型 | **说明** |
| --- | --- | --- |
| onLaunch | Function | 监听小程序初始化。  当小程序初始化完成时触发，全局只触发一次。 |
| onShow | Function | 监听小程序显示。  当小程序启动，或从后台进入前台显示时触发。 |
| onHide | Function | 监听小程序隐藏。  当小程序从前台进入后台时触发。 |
| onError | Function | 监听小程序错误。  当小程序发生 js 错误时触发。 |
| onPageNotFound | Function | 监听小程序启动时的页面不存在。  当小程序冷启动或热启动时触发。  不支持处理**导航栏相关API**失败场景，如以下API：   - [页面跳转（保留当前页）](0509-dd-navigateto.md) - [页面跳转（关闭当前页）](0510-dd-redirectto.md) - [页面跳转（关闭所有页面）](0511-dd-relaunch.md) - [返回上一级或多级页面](0512-dd-navigateback.md) - [设置导航栏](0508-dd-setnavigationbar.md) |
| 其他 | Any | 开发者可以添加任意数据或者函数到object对象中，可以通过getApp()方法获取。 |

> **[!NOTE]**
>
> - 用户点击左上角关闭，或者按了设备 Home 键离开钉钉时，小程序并不会直接销毁，而是进入了后台，当再次进入钉钉或再次打开小程序时，又会从后台进入前台。
> - 只有当小程序进入后台一定时间，或占用系统资源过高，才会被真正销毁。

### **代码示例**

```
App({
  onLaunch (options) {
    // 第一次打开时调用
    const { query, path } = options;
    const { corpId } = query;
  },
  onShow (options) {
    // 从后台被scheme重新打开时调用
    const { query, path } = options;
    const { corpId } = query;
  },
  onHide () {
    // 进入后台时调用
    console.log('App hide');
  },
  onError (error) {
    // 小程序执行出错时调用
    console.log(error);
  },
  onPageNotFound(err){
    dd.alert({
      title: 'onPageNotFound',
      content: JSON.stringify(err),
    });
    //小程序启动时，页面不存在可重定向到另一个页面。
    dd.redirectTo({
      url:'/pages/error/error',
    })
  },
  globalData: {
    foo: 'bar'
  }
});
```

### **onLaunch(options: Object)**

小程序初始化完成时触发，全局只触发一次。

`options`属性说明：

| **属性** | **类型** | 示例 | **描述** |
| --- | --- | --- | --- |
| query | Object | `{corpId: 'xxxxxx'}` | 启动小程序时scheme中的query参数。  **[!NOTE]**  非第三方个人应用类型（如企业内部应用、第三方企业应用）在启动时，会自动包含企业的corpId。 |
| path | String | `'x/y/z'` | 启动小程序的路径 (代码包路径)。  **[!NOTE]**  小程序启动scheme中path忽略时，默认为首页。 |

### **onShow(options: Object)**

小程序启动或者在后台时重新用scheme被打开显示时触发。参数与onLaunch一致。

### **onHide()**

当小程序从前台进入后台时触发。

### **onError()**

当小程序发生js错误时触发。

### **onPageNotFound()**

当小程序冷启动或热启动时触发。

## **app.json全局配置**

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

### **pages**

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

### **window**

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

### **tabBar**

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

## **getApp()方法**

小程序提供了全局的getApp()方法，可以获取到小程序实例，一般用在各个子页面之中获取顶层应用。

```
var app = getApp()
console.log(app.globalData) // 获取 globalData
```

> **[!IMPORTANT]**
>
> - `App()`必须在 `app.js` 里调用，且不能调用多次。
> - 不要在 `App()` 内定义的函数中调用 `getApp()`，使用 `this` 就可以拿到 `app` 实例。
> - 不要在 `onLaunch` 里调用[页面配置](0433-getcurrentpages-methods-1.md)，这个时候 `page` 还没有生成。
> - 通过 `getApp()` 获取实例之后，不要私自调用生命周期函数。
>
> 全局变量如果在一个页面中被改变，会在所有页面中都有效。

全局的数据可以在 App() 中设置，各个子页面通过全局函数 getApp() 可以获取全局的应用实例。

app.js示例代码：

```
// app.js
App({
  globalData: 1
})
```

a.js示例代码：

```
// a.js

// localValue 只在 a.js 有效
var localValue = 'a'
// 生成 app 实例
var app = getApp()
// 拿到全局数据，并改变它
app.globalData++
```

b.js示例代码：

```
// b.js

// localValue 只在 b.js 有效
var localValue = 'b'
// 如果 a.js 先运行，globalData 会返回 2
console.log(getApp().globalData)
```

上面代码中，`a.js`和`b.js`都声明了变量`localValue`，它们不会互相影响，因为各个脚本声明的变量和函数只在该文件中有效。

## **多语言配置**

钉钉小程序可以配置 native 渲染的 tabBar 和 titleBar 部分的多语言文案。多语言配置通过小程序全局配置文件和页面配置文件进行注入。

> **[!NOTE]**
>
> 目前支持 zh\_CN（简体中文）、zh\_TW（繁体中文台湾）、zh\_HK（繁体中文香港）、en\_US（美式英文）、ja\_JP（日文）五种语言。

**示例代码**：

```
// app.json 配置 tabBar 多语言文案
{
  "tabBar": {
    "items": [
      {
        "name": "首页",
        "name_locale": {
            "zh_CN": "首页",
          "en_US": "Home"
        }
      },
      {
        "name": "关于",
        "name_locale": {
            "zh_CN": "关于",
          "en_US": "About"
        }
      },
    ]
  }
}
```

```
// page.json 配置 titleBar 多语言文案
{
    "defaultTitle": "文件",
  "defaultTitle_locale": {
    "zh_CN": "文件",
    "en_US": "File",
    "ja_JP": "ファイル"
  }
}
```
