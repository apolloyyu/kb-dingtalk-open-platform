---
title: "组件生命周期"
source_url: "https://open.dingtalk.com/document/development/mini-app-component-lifecycle"
namespace: "development"
slug: "mini-app-component-lifecycle"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件生命周期"
doc_id: "DREk6NTqFq"
updated_at: "2025-09-17 20:58:10"
---

> Source: https://open.dingtalk.com/document/development/mini-app-component-lifecycle
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 自定义组件 > 开发自定义组件 > 组件生命周期
> Updated: 2025-09-17 20:58:10

# 组件生命周期

通过传递 props 属性实现了自定义组件与外部调用者的交流。但有时自定义组件依赖外部数据。

例如希望在自定义组件中向服务端发送请求获取数据。或者希望在确保组件已经渲染到页面上之后，再做某些操作。为此自定义组件提供了三个生命周期函数: didMount 、didUpdate 、didUnmount 。

## didMount

didMount为渲染后回调，此时页面已经渲染，通常在这里请求服务端数据比较合适。

```
Component({
  data: {},
  didMount() {
    let that = this;
    dd.httpRequest({
      url: 'http://httpbin.org/post',
      success: function(res) {
        that.setData({name: 'xiaoming'})                
      }
    });
  },
});
```

## didUpdate

didUpdate 为更新后回调，每次组件数据变更的时候都会调用。

> **[!IMPORTANT]**
>
> - 组件内部调用 this.setData 会触发 didUpdate
> - 外部调用者调用 this.setData 也会触发 didUpdate

```
Component({
  data: {},
  didUpdate(prevProps,prevData) {
    console.log(prevProps, this.props, prevData, this.data)
  },
});
```

## didUnmount

didUnmount 为删除后回调，每当组件示例从页面删除的时候会触发此回调。

```
Component({
  data: {},
  didUnmount() {
    console.log(this)
  },
});
```
