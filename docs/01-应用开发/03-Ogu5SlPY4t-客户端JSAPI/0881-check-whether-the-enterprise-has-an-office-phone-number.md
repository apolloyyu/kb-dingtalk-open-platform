---
title: "查询企业是否已开办公电话"
source_url: "https://open.dingtalk.com/document/development/check-whether-the-enterprise-has-an-office-phone-number"
namespace: "development"
slug: "check-whether-the-enterprise-has-an-office-phone-number"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > JSAPI参考 > 办公电话 > 查询企业是否已开办公电话"
doc_id: "ooQx1ZBXeK"
updated_at: "2025-09-17 20:57:34"
---

> Source: https://open.dingtalk.com/document/development/check-whether-the-enterprise-has-an-office-phone-number
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > H5微应用 > JSAPI参考 > 办公电话 > 查询企业是否已开办公电话
> Updated: 2025-09-17 20:57:34

# 查询企业是否已开办公电话

调用**biz.conference.getCloudCallInfo**查询企业是否已开办公电话。

## 使用说明

查询企业是否开通了办公电话，并返回开通的电话号码列表。

| **客户端** | **Android** | **iOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 支持（钉钉版本≥6.0.0） | 支持（钉钉版本≥6.0.0） | 支持（钉钉版本≥6.0.9） |

```
dd.biz.conference.getCloudCallInfo ({
  "corpId":"xxx",
   onSuccess : function() {},
   onFail : function() {}
})
```

## 参数说明

| 参数 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 企业corpId。 |

## 返回结果

**成功**

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| code | Number | 返回码。  **200**：正常 |
| cause | String | 异常描述。 |
| hasOpen | Boolean | 是否开户。 |
| bizNumberList | Array<String> | 返回开通的号码列表。 |

**失败**

| error | 描述 |
| --- | --- |
| 1001 | 参数无效。 |
| 3003 | 没有权限。 |
