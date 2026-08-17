---
title: "异步获取当前storage的相关信息"
source_url: "https://open.dingtalk.com/document/development/get-current-cached-data-asynchronously"
namespace: "development"
slug: "get-current-cached-data-asynchronously"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 缓存 > 异步获取当前storage的相关信息"
doc_id: "wvn2UdH3j1"
updated_at: "2025-09-17 21:00:03"
---

> Source: https://open.dingtalk.com/document/development/get-current-cached-data-asynchronously
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 缓存 > 异步获取当前storage的相关信息
> Updated: 2025-09-17 21:00:03

# 异步获取当前storage的相关信息

调用**dd.getStorageInfo**异步获取当前storage下所有缓存信息的key、已占用空间大小和限制最大的缓存空间大小信息。

## 扫码体验

![扫码体验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0101855461/p407734.png)

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

> **[!NOTE]**
>
> - 小程序缓存具有钉钉账号和小程序两级隔离，即当切换钉钉账号或小程序时，无法获取原账号下某小程序设置的缓存信息。
>
>   例如当前钉钉账号用户A，使用了“小程序1”、“小程序2”等应用。
>
>   - 在用户A使用小程序1调用本接口时，可以获取用户A使用“小程序1”设置的缓存信息。使用小程序2时，只能获取到“小程序2”设置的缓存信息。
>   - 切换钉钉账号用户B时，无法获取到用户A在使用小程序时设置的缓存信息。
> - 小程序使用webview内嵌页面的缓存与小程序storage缓存信息是相互隔离的，即调用本接口无法获取webview内嵌页面的缓存，只能获取通过存储缓存API设置的小程序storage缓存信息，如[将数据存储在本地缓存](https://open.dingtalk.com/document/orgapp/dd-setstorage)或[同步将数据存储](https://open.dingtalk.com/document/orgapp/dd-setstoragesync)等。
> - 卸载钉钉客户端重新安装，当前 storage下所有小程序缓存会失效；直接升级钉钉客户端版本，当前 storage下缓存不会失效。
> - 钉钉客户端设置中心清除缓存不会导致小程序缓存失效。操作路径：钉钉客户端-我的-设置-通用-一键清理。
> - iOS 手机备份时，缓存信息会同时备份。

## 示例代码

```
// .js
dd.getStorageInfo({
  success: function(res) {
    console.log(res.keys)
    console.log(res.currentSize)
    console.log(res.limitSize)
  }
})
```

## 入参

Object类型，属性如下：

| 属性 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

### success回调函数

| 属性 | 类型 | 描述 |
| --- | --- | --- |
| keys | String[] | 当前 storage 中所有的 key。 |
| currentSize | Number | 当前占用的空间大小, 单位为 KB。 |
| limitSize | Number | 限制的空间大小，单位为 KB。 |
