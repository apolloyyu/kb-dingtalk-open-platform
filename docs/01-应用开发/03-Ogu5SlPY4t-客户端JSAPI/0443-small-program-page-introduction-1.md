---
title: "小程序页面介绍"
source_url: "https://open.dingtalk.com/document/development/small-program-page-introduction-1"
namespace: "development"
slug: "small-program-page-introduction-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序页面配置 > 小程序页面介绍"
doc_id: "1zMEXYJciN"
updated_at: "2025-09-17 20:57:53"
---

> Source: https://open.dingtalk.com/document/development/small-program-page-introduction-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序页面配置 > 小程序页面介绍
> Updated: 2025-09-17 20:57:53

# 小程序页面介绍

Page代表应用的一个页面，负责页面展示和交互。每个页面对应一个子目录，一般有多少个页面，就有多少个子目录。它也是一个构造函数，用来生成页面实例。

每个小程序页面一般包含四个文件，如下表所示。

| **文件类型** | **是否必填** | **作用** |
| --- | --- | --- |
| js | 是 | 页面逻辑，比如数据获取、验证等。 |
| axml | 是 | 页面结构，由一系列标签堆叠而成。 |
| acss | 否 | 页面样式，比如页面纵横布局等。 |
| json | 否 | 页面配置，比如页面标题等。 |

## 示例

示例1：

`/pages/index/index.js`注册页面并在初始化时提供数据。

```
Page({
  data: {
    title: 'Dingtalk',
    array: [{user: 'li'}, {user: 'zhao'}]
  }
})
```

`pages/index/index.axml`根据以上提供的数据渲染页面内容。

```
<view>{{title}}</view>
<view>{{array[0].user}}</view>
```

示例2：

`pages/index/index.axml`中定义交互行为时，需要指定在页面脚本里面定义的响应函数。

```
<view onTap="handleTap">click me</view>
```

`/pages/index/index.js`中定义`handleTap`方法。

```
Page({
  handleTap() {
    console.log('yo! view tap!')
  }
})
```

示例3：

`pages/index/index.axml`中页面内容若要重新渲染，需在页面脚本里面调用`this.setData`方法。

```
<view>{{text}}</view>
<button onTap="changeText"> Change normal data </button>
```

`/pages/index/index.js`中定义`changeText`方法。

```
Page({
  data: {
    text: 'init data',
  },
  changeText() {
    this.setData({
      text: 'changed data'
    })
  },
})
```

上面代码中，`changeText`方法里面调用`this.setData`方法，会将页面进行重新渲染。
