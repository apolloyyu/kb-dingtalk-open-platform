---
title: "获取用户授权"
source_url: "https://open.dingtalk.com/document/development/obtain-user-authorization"
namespace: "development"
slug: "obtain-user-authorization"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 授权 > 获取用户授权"
doc_id: "J5AqLmJkTG"
updated_at: "2026-09-02 18:14:15"
---

> Source: https://open.dingtalk.com/document/development/obtain-user-authorization
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 授权 > 获取用户授权
> Updated: 2026-09-02 18:14:15

# 获取用户授权

调用**biz.auth.requestAuthInfo**唤起授权弹窗，获取用户授权。

> **[!IMPORTANT]**
>
> - 如果未使用本接口，推荐使用[统一授权套件](../02-4a8AMF6u2A-服务端-API/0007-function-description.md)。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 使用说明

| **客户端** | Android | iOS | PC |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥5.1.32） | 支持（钉钉版本≥5.1.32） | 不支持 |

```
dd.biz.auth.requestAuthInfo({
    authorizeType: 1,
    ext:'{"dataType":1,"fieldScope":["mobile","mainOrgName"]}',
    onSuccess:(res) => {
         console.log(res)
      },
      onFail:(err) => {
         console.log(err)
    }
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| authorizeType | String | 是 | 固定传**1**。 |
| ext | String | 是 | 固定值：   ``` {     "dataType": 1,     "fieldScope": [         "mobile",         "mainOrgName"     ] } ``` |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| 2 | 参数错误。 |
| 3 | 未知错误。 |
| -1 | 用户取消。 |
| 其他 | 服务端接口返回的错误。 |
