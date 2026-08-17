---
title: "拨打钉钉电话"
source_url: "https://open.dingtalk.com/document/development/call-dingtalk-h5"
namespace: "development"
slug: "call-dingtalk-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 拨打钉钉电话"
doc_id: "FwZjV5Tt07"
updated_at: "2025-09-17 20:56:40"
---

> Source: https://open.dingtalk.com/document/development/call-dingtalk-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 拨打钉钉电话
> Updated: 2025-09-17 20:56:40

# 拨打钉钉电话

调用**biz.telephone.call**拨打钉钉电话。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.telephone.call)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.telephone.call({
    users: ['101'], //用户列表，工号
    corpId: '', //企业id
    onSuccess : function() {},
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpid，可在[开发者后台](https://open-dev.dingtalk.com/)首页查看。 |
| userId | String | 用户的userid。 |
