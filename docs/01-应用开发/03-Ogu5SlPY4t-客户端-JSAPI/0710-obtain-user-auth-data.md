---
title: "获取用户授权"
source_url: "https://open.dingtalk.com/document/development/obtain-user-auth-data"
namespace: "development"
slug: "obtain-user-auth-data"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 授权 > 获取用户授权"
doc_id: "2o38pdI1W9"
updated_at: "2026-09-02 18:13:49"
---

> Source: https://open.dingtalk.com/document/development/obtain-user-auth-data
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 授权 > 获取用户授权
> Updated: 2026-09-02 18:13:49

# 获取用户授权

调用**dd.requestAuthInfo**唤起授权弹窗，获取用户授权。

> **[!IMPORTANT]**
>
> - 如果未使用本接口，推荐使用[统一授权套件](../02-4a8AMF6u2A-服务端-API/0007-function-description.md)。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 示例代码

> **[!NOTE]**
>
> 在调用本接口前，你可以先使用[dd.canIUse](0477-dd-caniuse.md)判断是否支持authorizeType的参数。例如`dd.canIUse('requestAuthInfo.object.authorizeType.1')`，表示判断客户端版本是否支持authorizeType 为 1。

```
dd.requestAuthInfo({
  authorizeType:1,
  ext:'{"dataType":1,"fieldScope":["mobile","mainOrgName"]}',
  success: (res) => {
    console.log(res)
  },
  fail: (err) => {
    console.error(err)
  }
})
```

## 入参

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| authorizeType | String | 是 | 固定传**1**。 |
| ext | String | 是 | 固定值：   ``` {     "dataType": 1,     "fieldScope": [         "mobile",         "mainOrgName"     ] } ``` |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |

## 错误码

| 参数 | 说明 |
| --- | --- |
| 2 | 参数错误。 |
| 3 | 未知错误。 |
| -1 | 用户取消。 |
| 其他 | 服务端接口返回的错误。 |
