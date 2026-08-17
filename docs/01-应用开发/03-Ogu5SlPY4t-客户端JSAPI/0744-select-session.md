---
title: "选择会话"
source_url: "https://open.dingtalk.com/document/development/select-session"
namespace: "development"
slug: "select-session"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 会话 > 选择会话"
doc_id: "qdmZAjV1aj"
updated_at: "2025-09-17 21:01:19"
---

> Source: https://open.dingtalk.com/document/development/select-session
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 会话 > 选择会话
> Updated: 2025-09-17 21:01:19

# 选择会话

调用**dd.chooseChat**选择会话。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

## 示例代码

```
dd.chooseChat({
        isAllowCreateGroup:false,//是否允许创建会话
    filterNotOwnerGroup:false,//是否限制为自己创建的会话
    success: res => {
        /*{
            chatId: 'xxxx',
            title:'xxx'
        }*/
    },
    fail: err =>{
        dd.alert({
            content:JSON.stringify(err)
        })
    }
})
```

## 返回结果

| **参数** | **说明** |
| --- | --- |
| chatId | 会话id（该会话cid永久有效）。 |
| title | 会话标题。 |
