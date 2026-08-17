---
title: "web-view"
source_url: "https://open.dingtalk.com/document/development/mini-app-web-view"
namespace: "development"
slug: "mini-app-web-view"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础组件 > web-view"
doc_id: "i9ncAdMGvj"
updated_at: "2025-09-17 20:58:34"
---

> Source: https://open.dingtalk.com/document/development/mini-app-web-view
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础组件 > web-view
> Updated: 2025-09-17 20:58:34

# web-view

本文介绍web-view组件的使用。

**<web-view />** 组件是一个可以用来承载H5网页的组件，自动铺满整个小程序页面。需要开发者到开发者后台配置渲染H5网页的安全域名。

> **[!IMPORTANT]**
>
> 每个页面只能有一个`<web-view />`，该组件会自动铺满整个页面，并覆盖其它组件。暂时不支持钉钉微应用相关JSAPI使用，后续迭代支持。

## 属性

| **属性** | **类型** | **说明** |
| --- | --- | --- |
| src | String | web-view 要渲染的H5网页URL。H5网页URL需要登录[开发者后台](https://open-dev.dingtalk.com/#/suite)，进行H5域名白名单配置。 |
| onMessage | EventHandler | 网页向小程序 postMessage 消息，e.detail = { data }。 |

**示例代码**

```
<web-view id="web-view-1" src="https://open.dingtalk.com/mobile" onMessage="test"></web-view>
```

## web-view组件控制

### dd.createWebViewContext

`<web-view />`要渲染的H5页面可以使用手动引入`https://appx/web-view.min.js` （此链接仅支持在钉钉客户端内访问），组件提供了相关与小程序交互的接口。

> **[!NOTE]**
>
> 该示例代码的双向通信能力的流程是 H5 先发消息给小程序，小程序接收到消息后再发消息给 H5。

| **接口名** | **接口类别** | **说明** |
| --- | --- | --- |
| dd.postMessage | 向小程序发送消息 | 向小程序发送消息，自定义一组或多组key、value数据，格式为JSON，如：dd.postMessage({name:"测试web-view"})。 |
| dd.onMessage | 监听小程序发过来的消息 | 监听小程序发过来的消息。 |

**示例代码**

`<web-view />`H5页面内：

```
<!-- html -->
<script type="text/javascript" src="https://appx/web-view.min.js"></script>
// 如该H5页面需要同时在非钉钉客户端内使用，为避免该请求404，可参考以下写法
// 请尽量在html头部执行以下脚本
<script>
  if (navigator.userAgent.toLowerCase().indexOf('dingtalk') > -1) {
    document.writeln('<script src="https://appx/web-view.min.js"' + '>' + '<' + '/' + 'script>');
  }

// javascript
dd.navigateTo({url: '/Pages/home/index'});

// 网页向小程序 postMessage 消息
dd.postMessage({name:"测试web-view"});

// 接收来自小程序的消息。
dd.onMessage = function(e) {
  console.log(e); //{'sendToWebView': '1'}
}

</script>
```

`dd.postMessage`信息发送后，小程序页面接收信息时，会执行`onMessage`配置的方法：

```
// 小程序页面对应的page.js声明test方法，
// 由于page.axml里的web-view组件设置了onMessage="test",
// 当网页里执行完dd.postMessage后，test方法会被执行
// "web-view-1"为视图中<web-view />组件的id，必须设置

Page({
  onLoad(e){
    this.webViewContext = dd.createWebViewContext('web-view-1');    
  },
  test(e){
    dd.alert({
      content:JSON.stringify(e.detail),
    });  
    this.webViewContext.postMessage({'sendToWebView': '1'});
  },
});
```

## 通过桥接方式调用 dd 上的方法

下面介绍一种通过桥接的方式在 H5 中调用 **dd.alert** 的方法，通过该方式也可以调用其他 dd 上挂载的 api。

承载 `<web-view />` 组件的小程序页面内的 `index.axml`：

```
<web-view id="web-view-1" src="https://open.dingtalk.com/mobile" onMessage="onmessage"></web-view>
```

承载 `<web-view />` 组件的小程序页面内的 `index.js`：

```
Page({
  onLoad(){
    this.webViewContext = dd.createWebViewContext('web-view-1');    
  },
  onmessage: function(e) {
    const { d_m, params } = e.detail;
    const callbackId = params.callbackId;
    params.success = () => {
      this.webViewContext.postMessage({
        callbackId: callbackId,
        issuccess: true
      })
    }
    params.fail = () => {
      this.webViewContext.postMessage({
        callbackId: callbackId,
        issuccess: false
      })
    }
    delete params.callbackId
    dd[d_m](params);
  }
});
```

`<web-view />`H5页面内：

```
let uniqId = 1;

function getUniqId() {
  return uniqId++;
}

const callBackMap = {};

// 通过该方法就可以在 H5 中调用 dd.alert
window.native_alert = function() {
  const callbackId = getUniqId();
  callBackMap[callbackId] = {
    success: function() {
      console.log('成功');
    },
    fail: function() {
      console.log('失败');
    }
  }
  dd.postMessage({
    d_m: 'alert',
    params: {
      title: '亲',
      content: '您本月的账单已出',
      buttonText: '我知道了',
      callbackId
    }
  });
}

dd.onMessage = function(e) {
  const { callbackId, issuccess } = e;
  const { success, fail } = callBackMap[callbackId];
  delete callBackMap[callbackId];
  issuccess ? success() : fail();
}
```
