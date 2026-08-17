---
title: "通用电话拨打"
source_url: "https://open.dingtalk.com/document/development/universal-phone-call-h5"
namespace: "development"
slug: "universal-phone-call-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 通用电话拨打"
doc_id: "42Y4PQt2R6"
updated_at: "2025-09-17 20:56:39"
---

> Source: https://open.dingtalk.com/document/development/universal-phone-call-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 通用电话拨打
> Updated: 2025-09-17 20:56:39

# 通用电话拨打

调用**biz.telephone.showCallMenu**通用电话拨打。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.telephone.showCallMenu)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.telephone.showCallMenu({
    phoneNumber: '1xxxxxxxxxx', // 期望拨打的电话号码
    code: '+86', // 国家代号，中国是+86
    showDingCall: true, // 是否显示钉钉电话
    onSuccess : function() {},
    onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| phoneNumber | String | 期望拨打的电话号码。 |
| code | String | 国家代号，中国是+86。 |
| showDingCall | Boolean | 是否显示钉钉电话。 |
