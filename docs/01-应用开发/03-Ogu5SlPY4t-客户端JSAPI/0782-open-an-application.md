---
title: "打开应用"
source_url: "https://open.dingtalk.com/document/development/open-an-application"
namespace: "development"
slug: "open-an-application"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 业务 > 打开应用"
doc_id: "WOpkMHJCDt"
updated_at: "2025-09-17 20:56:21"
---

> Source: https://open.dingtalk.com/document/development/open-an-application
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 业务 > 打开应用
> Updated: 2025-09-17 20:56:21

# 打开应用

调用**biz.microApp.openApp**打开应用。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.microApp.openApp)在线调试该接口。

## 使用说明

调用本接口前，请先引入钉钉js，参考[准备工作](https://open.dingtalk.com/document/orgapp/read-before-development)。

在微应用中跳转到钉钉原生微应用（如审批、日志等）或已上架的第三方微应用，可使用该JSAPI打开应用。

| **客户端** | **是否需要鉴权** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- | --- |
| 支持说明 | 不需要 | 支持 | 支持 | 不支持 |

```
dd.biz.microApp.openApp({
    agentId: '123',
    appId: '234',
    corpId: 'dingxxxxxxxxx',
    onSuccess : function(result) {},
    onFail : function(err) {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| agentId | String | 要打开应用的agentId，获取方式请参考[基础概念-AgentId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |
| appId | String | 要打开应用的appId，可以在[开发者后台](https://open-dev.dingtalk.com/fe/app#/isv/app)应用详情页获取。 |
| corpId | String | 要打开的应用所属的corpId，获取方式请参考[基础概念-CorpId](https://open.dingtalk.com/document/orgapp/basic-concepts)。 |

开发者有两种方式来打开应用：

- 通过agentId打开应用。
- 通过appId和corpId打开应用。

> **[!NOTE]**
>
> - 如果提供了正确的agentId，系统将直接根据agentId打开应用，不会再使用appId和corpId参数。
> - 如果使用agentId无法打开应用，系统将根据appId和corpId来打开应用，否则返回错误。
