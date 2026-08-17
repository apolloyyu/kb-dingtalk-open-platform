---
title: "其他组件实例属性"
source_url: "https://open.dingtalk.com/document/development/mini-app-other-component-instance-properties"
namespace: "development"
slug: "mini-app-other-component-instance-properties"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 其他组件实例属性"
doc_id: "arbMCaygE8"
updated_at: "2025-09-17 20:58:11"
---

> Source: https://open.dingtalk.com/document/development/mini-app-other-component-instance-properties
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 其他组件实例属性
> Updated: 2025-09-17 20:58:11

# 其他组件实例属性

除了 data、setData、props等属性外，组件实例上还有如下属性：

- `is`: 组件路径
- `$page`: 组件所属页面实例
- `$id`: 组件 id，在 axml 中也可直接渲染

  > **[!NOTE]**
  >
  > 在组件中可以使用 dd 调用 api。

```
// /components/xx/index.js
Component({
  didMount(){
    console.log(this.is);
    console.log(this.$page);
    console.log(this.$id);
  }
});
```

```
<!-- /components/xx/index.axml 组件id可直接在组件axml中渲染 -->
<view>{{$id}}</view>
```

```
// /pages/index/index.json
{
  "usingComponents": {
    "xx": "/components/xx/index"
  }
}
```

```
<!-- /pages/index/index.axml -->
<xx />
```

当组件在页面上渲染后，执行 didMount 回调，控制台输出大概是这样的：

```
/components/xx/index
{$viewId: 51, route: "pages/index/index"}
1
```
