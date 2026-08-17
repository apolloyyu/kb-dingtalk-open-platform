---
title: "根据openConversationId跳转到对应会话"
source_url: "https://open.dingtalk.com/document/development/redirects-to-the-specified-session-based-on-the-openconversationid"
namespace: "development"
slug: "redirects-to-the-specified-session-based-on-the-openconversationid"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 会话 > 根据openConversationId跳转到对应会话"
doc_id: "pqUBz0Q6Yb"
updated_at: "2025-09-17 20:56:36"
---

> Source: https://open.dingtalk.com/document/development/redirects-to-the-specified-session-based-on-the-openconversationid
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 会话 > 根据openConversationId跳转到对应会话
> Updated: 2025-09-17 20:56:36

# 根据openConversationId跳转到对应会话

调用**biz.chat.toConversationByOpenConversationId**，根据openConversationId跳转到对应会话。

## **效果示例**

![iShot2022-11-07 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8248787661/p514145.png)

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持(钉钉版本≥5.1.30) | 支持(钉钉版本≥5.1.30) | 支持(钉钉版本≥5.1.33) |

```
dd.biz.chat.toConversationByOpenConversationId({
      openConversationId:"cidG+fFwaNKTxxxxx",
      onSuccess:function (result) {
          console.log(JSON.stringify(result))
        },
       onFail : function(err) {
          console.log(JSON.stringify(err))
         }
 })
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| openConversationId | String | 会话的openConversationId。   - 企业内部应用，可调用[创建群会话](https://open.dingtalk.com/document/orgapp/create-group-session)接口获取openConversationId参数值。 - 第三方企业应用，可调用[创建群](https://open.dingtalk.com/document/orgapp/create-a-scene-group-v2)接口获取open\_conversation\_id参数值。 |
| onSuccess | Fuction | 调用成功的回调函数。 |
| onFail | Fuction | 调用失败的回调函数。 |

## **返回结果**

### **成功**

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| success | String | 调用本接口成功跳转到对应会话。  **[!NOTE]**  如果是Android端调用成功，返回值为空字符串。 |

### **失败**

如果页面出现强提示“会话不存在”，说明当前操作人不是目标会话中的成员。

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| invalid openConversationId | String | openConversationId参数不正确。 |

## **错误码**

| **参数** | **说明** |
| --- | --- |
| 3 | openConversationId参数不正确。  **[!NOTE]**  iOS端错误码。 |
| 9 | openConversationId参数不正确。  **[!NOTE]**  Android、PC端错误码。 |
