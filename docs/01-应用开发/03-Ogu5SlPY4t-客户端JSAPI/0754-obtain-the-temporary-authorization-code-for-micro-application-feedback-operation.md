---
title: "获取微应用反馈式操作的临时授权码"
source_url: "https://open.dingtalk.com/document/development/obtain-the-temporary-authorization-code-for-micro-application-feedback-operation"
namespace: "development"
slug: "obtain-the-temporary-authorization-code-for-micro-application-feedback-operation"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 免登 > 获取微应用反馈式操作的临时授权码"
doc_id: "JebjLh5ER0"
updated_at: "2025-09-17 20:56:02"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-temporary-authorization-code-for-micro-application-feedback-operation
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 免登 > 获取微应用反馈式操作的临时授权码
> Updated: 2025-09-17 20:56:02

# 获取微应用反馈式操作的临时授权码

调用**runtime.permission.requestOperateAuthCode**获取微应用反馈式操作的临时授权码。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 需要 | 支持 | 支持 | 支持 |

```
dd.runtime.permission.requestOperateAuthCode({
    corpId: "corpid",
    agentId:"agentId",
    onSuccess: function(result) {
    /*{
        code: 'hYLK98jkf0m' //string authCode
    }*/
    },
    onFail : function(err) {}
 
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 说明 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业的corpId。  **[!NOTE]**  第三方企业应用可以在微应用的首页URL中使用**$CORPID$**做为参数占位符，钉钉容器会将**$CORPID$**替换为当前访问用户的企业corpId。 |
| agentId | String | 是 | 微应用agentId，   - 企业内部应用，可以从应用信息中获取，参考[基础概念-AgentId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 - 第三方企业应用，可以从授权信息中获取到，调用[获取企业授权信息](https://open.dingtalk.com/document/isvapp/obtains-the-basic-information-of-an-enterprise)接口获取，必须与dd.config的agentId一致。 |

## 返回结果

| **参数** | **说明** |
| --- | --- |
| code | 授权码，有效期5分钟，且只能使用一次。 |
