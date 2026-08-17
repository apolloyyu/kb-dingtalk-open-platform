---
title: "打开与某个用户的单聊会话"
source_url: "https://open.dingtalk.com/document/development/open-a-one-on-one-chat-session-with-a-user"
namespace: "development"
slug: "open-a-one-on-one-chat-session-with-a-user"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 会话 > 打开与某个用户的单聊会话"
doc_id: "aOaFJ239Rw"
updated_at: "2025-09-17 20:56:37"
---

> Source: https://open.dingtalk.com/document/development/open-a-one-on-one-chat-session-with-a-user
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 会话 > 打开与某个用户的单聊会话
> Updated: 2025-09-17 20:56:37

# 打开与某个用户的单聊会话

调用**biz.chat.openSingleChat**打开与某个用户的单聊会话。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.chat.openSingleChat)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.chat.openSingleChat({
    corpId: 'xxx', // 企业id,必须是用户所属的企业的corpid
    userId:'xxx', // 用户的uerid
    onSuccess : function() {},
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid，可在[开发者后台](https://open-dev.dingtalk.com/)首页查看。 |
| userId | String | 用户的userid。 |
