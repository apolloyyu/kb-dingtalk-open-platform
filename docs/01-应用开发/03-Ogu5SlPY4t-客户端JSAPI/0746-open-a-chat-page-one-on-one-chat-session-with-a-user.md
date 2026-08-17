---
title: "打开与某个用户的聊天页面（单聊会话）"
source_url: "https://open.dingtalk.com/document/development/open-a-chat-page-one-on-one-chat-session-with-a-user"
namespace: "development"
slug: "open-a-chat-page-one-on-one-chat-session-with-a-user"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 会话 > 打开与某个用户的聊天页面（单聊会话）"
doc_id: "Jd5d6V4QF0"
updated_at: "2025-09-17 21:01:21"
---

> Source: https://open.dingtalk.com/document/development/open-a-chat-page-one-on-one-chat-session-with-a-user
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 会话 > 打开与某个用户的聊天页面（单聊会话）
> Updated: 2025-09-17 21:01:21

# 打开与某个用户的聊天页面（单聊会话）

调用**dd.openChatByUserId**打开与某个用户的聊天页面。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

## 示例代码

```
dd.openChatByUserId({
    userId:'xxx', // 用户的userid
    success: res => {

    },
    fail: err =>{
        dd.alert({
            content:JSON.stringify(err)
        })
    }
})
```

## **入参**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| userId | String | 用户的userid。 |
