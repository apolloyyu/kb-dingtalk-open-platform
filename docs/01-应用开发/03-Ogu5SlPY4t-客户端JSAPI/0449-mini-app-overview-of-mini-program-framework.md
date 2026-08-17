---
title: "小程序框架概述"
source_url: "https://open.dingtalk.com/document/development/mini-app-overview-of-mini-program-framework"
namespace: "development"
slug: "mini-app-overview-of-mini-program-framework"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 框架 > 小程序框架概述"
doc_id: "RamB0G2ptc"
updated_at: "2025-09-17 20:57:48"
---

> Source: https://open.dingtalk.com/document/development/mini-app-overview-of-mini-program-framework
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 框架 > 小程序框架概述
> Updated: 2025-09-17 20:57:48

# 小程序框架概述

小程序提供了一套简单高效的开发框架，让开发者可以在钉钉中开发具有原生 APP 体验的服务。

整个小程序框架系统分为逻辑层（App Service）和 视图层（View）。小程序提供了自己的视图层描述语言 AXML 和 ACSS，以及基于 JavaScript 的逻辑层框架，并在视图层与逻辑层间提供了数据传输和事件系统，让开发者能够专注于数据与逻辑。

![小程序框架](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4597272061/p171372.png)

## 数据绑定

小程序的核心是一个响应式的数据绑定系统，逻辑上分为视图层和逻辑层。这两层始终保持同步，只要在逻辑层修改数据，视图层就会相应的更新。

示例：

```
<!-- 视图层 -->
<view> Hello {{name}}! </view>
<button onTap="changeName"> Click me! </button>
```

```
// 逻辑层
var initialData = {
  name: 'alibaba'
};

Page({
  data: initialData,
  changeName(e) {
    this.setData({
      name: 'dingtalk'
    })
  }
});
```

上述示例代码中，框架自动将逻辑层数据中的`name`与视图层的`name`进行了绑定，所以在页面一打开的时候会显示`Hello alibaba!`。

用户点击按钮的时候，视图层会发送`changeName`的事件给逻辑层，逻辑层找到对应的事件处理函数。逻辑层执行了`setData`的操作，将`name`从`alibaba`变为`dingtalk`，因为该数据和视图层已经绑定了，从而视图层会自动改变为`Hello dingtalk!`。

> **[!IMPORTANT]**
>
> 由于框架并非运行在浏览器中，所以 JavaScript 在 web 中的一些能力都无法使用，如 `document`、`window`等对象。

逻辑层 js 可以用 es2015 模块化语法组织代码：

```
import util from './util'; // 载入相对路径
import absolute from '/absolute'; // 载入项目根路径文件
```

## 第三方NPM模块

小程序支持引入第三方模块，需先在小程序根目录下执行如下命令安装该模块:

```
npm install lodash
```

引入后即可在逻辑层中直接使用：

```
import lodash from 'lodash'; // 载入第三方 npm 模块
```

> **[!IMPORTANT]**
>
> 由于 node\_modules 里第三方模块代码不会经过转换器，为了确保各个终端兼容，node\_modules 下的代码需要转成 es5 格式再引用，模块格式推荐使用 es2015 的 import/export。浏览器相关web能力同样无法使用。
