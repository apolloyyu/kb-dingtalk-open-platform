---
title: "跳转H5微应用"
source_url: "https://open.dingtalk.com/document/development/jump-to-h5-micro-application"
namespace: "development"
slug: "jump-to-h5-micro-application"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开应用 > 跳转H5微应用"
doc_id: "hCH8nG7D3w"
updated_at: "2025-09-17 20:57:30"
---

> Source: https://open.dingtalk.com/document/development/jump-to-h5-micro-application
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 打开应用 > 跳转H5微应用
> Updated: 2025-09-17 20:57:30

# 跳转H5微应用

调用**biz.navigation.navigateToPage**，跳转到另一个钉钉H5微应用。

## **使用说明**

| **客户端** | **Android** | **iOS** | **PC** | 是否需要鉴权 |
| --- | --- | --- | --- | --- |
| 支持说明 | 支持(钉钉版本≥6.5.45) | 支持(钉钉版本≥6.5.45) | 不支持 | 不需要 |

```
 dd.biz.navigation.navigateToPage({
      url: 'https://www.dingtalk.com',
      onSuccess: (res) => {
            console.log(JSON.stringify(res))
         },
       onFail:(err) =>{
             console.log(JSON.stringify(err))
         }
})
```

## **参数说明**

| 参数 | 类型 | 是否必传 | 说明 |
| --- | --- | --- | --- |
| url | String | 是 | 跳转的目标H5微应用页面地址，需要传http或https协议地址。 |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## **返回结果**

> **[!NOTE]**
>
> - 本接口调用成功后，无返回参数。
> - 调用本接口跳转页面失败后，暂无失败回调信息。当url参数页面打不开时，该接口不会触发onFail回调，需要检查url参数页面是否正常。
