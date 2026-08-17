---
title: "获取钉钉客户端是否为专属钉钉"
source_url: "https://open.dingtalk.com/document/development/retrieve-user-information-info"
namespace: "development"
slug: "retrieve-user-information-info"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 专属钉钉 > 获取钉钉客户端是否为专属钉钉"
doc_id: "kvRRXLulT7"
updated_at: "2025-09-17 20:57:38"
---

> Source: https://open.dingtalk.com/document/development/retrieve-user-information-info
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 专属钉钉 > 获取钉钉客户端是否为专属钉钉
> Updated: 2025-09-17 20:57:38

# 获取钉钉客户端是否为专属钉钉

调用**biz.realm.getUserExclusiveInfo**获取钉钉客户端是否为专属钉钉。

## 使用说明

| **客户端** | Android | iOS | PC |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥6.0.15） | 支持（钉钉版本≥6.0.15） | 支持（钉钉版本≥6.0.17） |

```
dd.biz.realm.getUserExclusiveInfo({

    onSuccess: function() {},
    onFail: function() {}
});
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| onSuccess | Function | 否 | 调用成功的回调函数。 |
| onFail | Function | 否 | 调用失败的回调函数。 |

## 返回结果

| 参数 | 说明 |
| --- | --- |
| isExclusiveApp | - **0**：标准钉钉。 - **1**：专属钉钉。 |
