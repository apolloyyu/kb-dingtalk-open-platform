---
title: "检查某企业的办公电话开通状态"
source_url: "https://open.dingtalk.com/document/development/check-the-status-of-office-telephones-of-an-enterprise-h5"
namespace: "development"
slug: "check-the-status-of-office-telephones-of-an-enterprise-h5"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 检查某企业的办公电话开通状态"
doc_id: "KPBv2sfq7n"
updated_at: "2025-09-17 20:56:39"
---

> Source: https://open.dingtalk.com/document/development/check-the-status-of-office-telephones-of-an-enterprise-h5
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 电话 > 检查某企业的办公电话开通状态
> Updated: 2025-09-17 20:56:39

# 检查某企业的办公电话开通状态

调用**biz.telephone.checkBizCall**检查某企业的办公电话开通状态。

## 调试

访问[JSAPI Explorer](https://open-dev.dingtalk.com/apiExplorer#/jsapi?api=biz.telephone.checkBizCall)在线调试该接口。

## 使用说明

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持 | 支持 | 不支持 |

```
dd.biz.telephone.checkBizCall({
    corpId: '', //企业id
    onSuccess: function(result) {
        /*{
            isSupport: 1 // 是否开通
        }*/
    },
    onFail : function(err) 
})
```

## 参数说明

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业的corpId。 |

## 返回结果

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| isSupport | Boolean | 是否已开通。 |
