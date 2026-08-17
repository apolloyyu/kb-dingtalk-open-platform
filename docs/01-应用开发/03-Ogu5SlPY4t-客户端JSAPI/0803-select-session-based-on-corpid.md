---
title: "根据corpid选择会话"
source_url: "https://open.dingtalk.com/document/development/select-session-based-on-corpid"
namespace: "development"
slug: "select-session-based-on-corpid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 会话 > 根据corpid选择会话"
doc_id: "FUSQFk6Y4f"
updated_at: "2025-09-17 20:56:35"
---

> Source: https://open.dingtalk.com/document/development/select-session-based-on-corpid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 会话 > 根据corpid选择会话
> Updated: 2025-09-17 20:56:35

# 根据corpid选择会话

调用**biz.chat.chooseConversationByCorpId**根据corpid选择会话。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.chat.chooseConversationByCorpId)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 支持 |

```
dd.biz.chat.chooseConversationByCorpId({
    corpId: 'xxx', //企业id,必须是用户所属的企业的corpid
    isAllowCreateGroup:false,
    filterNotOwnerGroup:false,
    onSuccess : function() {
        /*{
            chatId: 'xxxx',
            title:'xxx'
        }*/
},
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid，可在[开发者后台](https://open-dev.dingtalk.com/)首页查看。 |
| isAllowCreateGroup | Boolean | 是否允许创建会话：   - **true**：允许 - **false**：不允许 |
| filterNotOwnerGroup | Boolean | 是否限制为自己创建的会话。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| chatId | 会话id。  **[!IMPORTANT]**  后续版本中chatid将不再使用，请将openConversationId作为群会话唯一标识。 |
| openConversationId | 会话id。 |
| title | 会话标题。 |
