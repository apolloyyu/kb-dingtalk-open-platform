---
title: "app.js注册小程序"
source_url: "https://open.dingtalk.com/document/development/app-js-registration-mini-program-1"
namespace: "development"
slug: "app-js-registration-mini-program-1"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 小程序全局配置 > app.js注册小程序"
doc_id: "pVuYFDGGNe"
updated_at: "2025-09-17 20:57:50"
---

> Source: https://open.dingtalk.com/document/development/app-js-registration-mini-program-1
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 小程序全局配置 > app.js注册小程序
> Updated: 2025-09-17 20:57:50

# app.js注册小程序

App()接受一个Object作为参数，用来配置小程序的生命周期回调等。

> **[!IMPORTANT]**
>
> `App()`必须在`app.js`里调用，且不能调用多次。

## Object属性说明

| **属性** | 类型 | **说明** |
| --- | --- | --- |
| onLaunch | Function | 监听小程序初始化。  当小程序初始化完成时触发，全局只触发一次。 |
| onShow | Function | 监听小程序显示。  当小程序启动，或从后台进入前台显示时触发。 |
| onHide | Function | 监听小程序隐藏。  当小程序从前台进入后台时触发。 |
| onError | Function | 监听小程序错误。  当小程序发生 js 错误时触发。 |
| onPageNotFound | Function | 监听小程序启动时的页面不存在。  当小程序冷启动或热启动时触发。  不支持处理**导航栏相关API**失败场景，如以下API：   - [页面跳转（保留当前页）](https://open.dingtalk.com/document/orgapp/dd-navigateto) - [页面跳转（关闭当前页）](https://open.dingtalk.com/document/orgapp/dd-redirectto) - [页面跳转（关闭所有页面）](https://open.dingtalk.com/document/orgapp/dd-relaunch) - [返回上一级或多级页面](https://open.dingtalk.com/document/orgapp/dd-navigateback) - [设置导航栏](https://open.dingtalk.com/document/orgapp/dd-setnavigationbar) |
| 其他 | Any | 开发者可以添加任意数据或者函数到object对象中，可以通过getApp()方法获取。 |

> **[!NOTE]**
>
> - 用户点击左上角关闭，或者按了设备 Home 键离开钉钉时，小程序并不会直接销毁，而是进入了后台，当再次进入钉钉或再次打开小程序时，又会从后台进入前台。
> - 只有当小程序进入后台一定时间，或占用系统资源过高，才会被真正销毁。

## 代码示例

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

## onLaunch(options: Object)

小程序初始化完成时触发，全局只触发一次。

`options`属性说明：

| **属性** | **类型** | 示例 | **描述** |
| --- | --- | --- | --- |
| query | Object | `{corpId: 'xxxxxx'}` | 启动小程序时scheme中的query参数。  **[!NOTE]**  非第三方个人应用类型（如企业内部应用、第三方企业应用）在启动时，会自动包含企业的corpId。 |
| path | String | `'x/y/z'` | 启动小程序的路径 (代码包路径)。  **[!NOTE]**  小程序启动scheme中path忽略时，默认为首页。 |

## **onShow(options: Object)**

小程序启动或者在后台时重新用scheme被打开显示时触发。参数与onLaunch一致。

## onHide()

当小程序从前台进入后台时触发。

## onError()

当小程序发生js错误时触发。

## onPageNotFound()

当小程序冷启动或热启动时触发。

## 相关文档

- [getApp()方法](https://open.dingtalk.com/document/dingstart/getapp-method-1)
