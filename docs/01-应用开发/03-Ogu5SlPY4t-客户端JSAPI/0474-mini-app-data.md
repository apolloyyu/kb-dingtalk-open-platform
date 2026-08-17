---
title: "data"
source_url: "https://open.dingtalk.com/document/development/mini-app-data"
namespace: "development"
slug: "mini-app-data"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > data"
doc_id: "g7WrWFp9QR"
updated_at: "2025-09-17 20:58:09"
---

> Source: https://open.dingtalk.com/document/development/mini-app-data
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > data
> Updated: 2025-09-17 20:58:09

# data

data 为组件的局部状态，和页面一样，可以通过this.setData更改，会触发组件的重新渲染；也可以通过this.$spliceData做数据的更改。

详情请参考[注册小程序页面](https://open.dingtalk.com/document/dingstart/register-a-mini-program-page-1)。

**示例代码**

```
// /components/counter/index.js
Component({
  data: { counter: 0 }
});
```

```
<!-- /components/counter/index.axml -->
<view>{{counter}}</view>
```

```
// /components/counter/index.json
{
  "component": true,
}
```

以上代码分别实现了自定义组件的三个要素：js、axml、json。然后我们在页面上就可以使用了。 首先需要在页面的 json 文件中声明依赖的组件，和组件的声明依赖方式相同。

```
// /pages/index/index.json
{
  "usingComponents": {
    "my-component": "/components/counter/index"
  }
}
```

然后在页面的 axml 中就可以使用了。

```
<!-- /pages/index/index.axml -->
<my-component />
```

页面输出：

```
0
```
