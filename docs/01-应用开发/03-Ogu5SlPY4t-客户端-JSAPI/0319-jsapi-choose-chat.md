---
title: "chooseChat"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-chat"
namespace: "development"
slug: "jsapi-choose-chat"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "会话管理 > chooseChat"
doc_id: "GuMMnPK9lu"
updated_at: "2025-08-27 18:08:53"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-chat
> Path: 应用开发 / 客户端 JSAPI / 会话管理 > chooseChat
> Updated: 2025-08-27 18:08:53

# chooseChat

调用chooseChat，选择会话。

对于群聊会话，该 JSAPI 存在如下限制条件：

1. 仅支持选择企业内部群，其他群类型不支持选择；
2. 只会列出用户当前在群内的群聊。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10303) |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10303) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `isAllowCreateGroup`（boolean）：是否允许创建会话。
- `filterNotOwnerGroup`（boolean）：是否限制为自己创建的会话。
- `corpId`（string）：企业corpId。  
    
  > 在H5应用中必填。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 字段说明

- `chatId`（string，必填）：会话id。  
  > 后续版本中 chatId 将不再使用，请将 openConversationId 作为群会话唯一标识。
- `openConversationId`（string，必填）：会话id。
- `title`（string，必填）：会话标题。

## **示例****代码**

### 默认出入参

```
dd.chooseChat({
  corpId: `corpId示例值`,
  isAllowCreateGroup: true,
  filterNotOwnerGroup: true,
  success: (res) => {
    const { title, chatId, openConversationId } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "title": "全员群", "chatId": "4555", "openConversationId": "cid*****" }
```
