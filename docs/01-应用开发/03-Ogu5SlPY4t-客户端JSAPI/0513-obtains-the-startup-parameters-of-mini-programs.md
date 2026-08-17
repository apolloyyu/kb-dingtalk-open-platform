---
title: "获取小程序启动时的参数"
source_url: "https://open.dingtalk.com/document/development/obtains-the-startup-parameters-of-mini-programs"
namespace: "development"
slug: "obtains-the-startup-parameters-of-mini-programs"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > 获取小程序启动时的参数"
doc_id: "5Q1YdXSFc5"
updated_at: "2025-09-17 20:58:43"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-startup-parameters-of-mini-programs
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > 获取小程序启动时的参数
> Updated: 2025-09-17 20:58:43

# 获取小程序启动时的参数

调用**dd.getLaunchOptionsSync**获取小程序启动时的参数。

## 扫码体验

![获取小程序启动时的参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4835575461/p406836.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 开发者可以通过[dd.canIUse](https://open.dingtalk.com/document/orgapp/dd-caniuse)函数判断端上是否支持此能力。
> - 第三方个人小程序获取的启动参数只有path。
> - 本接口获取的信息与小程序启动方法[App.onLaunch](https://open.dingtalk.com/document/orgapp/app-js-registration-mini-program#section-kym-z05-hv9)内携带的参数信息是一致的。
>
> ```
> App({
>   onLaunch(options) {
>     console.log(options);
>     }
> })
> ```

## 示例代码

### .js示例代码

```
Page({
  onLoad(query) {
    let param = dd.getLaunchOptionsSync();
    console.log(JSON.stringify(param));
}
})
```

## 返回值说明

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| query | Object | 当前小程序的 query，从启动参数的 query 字段解析而来。 |
| scene | String | 该字段暂无使用场景，可忽略。  **[!NOTE]**  IDE模拟器可获取该字段值为"0000"，真机不支持获取该字段。 |
| path | String | 当前小程序启动时进入的页面路径地址。 |
