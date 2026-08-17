---
title: "根据chatId跳转到对应会话"
source_url: "https://open.dingtalk.com/document/development/redirects-to-a-specific-session-based-on-the-chatid"
namespace: "development"
slug: "redirects-to-a-specific-session-based-on-the-chatid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 会话 > 根据chatId跳转到对应会话"
doc_id: "ryYgBAkrnu"
updated_at: "2025-09-17 21:01:20"
---

> Source: https://open.dingtalk.com/document/development/redirects-to-a-specific-session-based-on-the-chatid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 会话 > 根据chatId跳转到对应会话
> Updated: 2025-09-17 21:01:20

# 根据chatId跳转到对应会话

调用**dd.openChatByChatId**打开对应会话。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

## 示例代码

```
dd.openChatByChatId({
    chatId:'xxx',//会话Id
    success: res => {

    },
    fail: err =>{
        dd.alert({
            content:JSON.stringify(err)
        })
    }
})
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| chatId | String | 会话ID。 |
