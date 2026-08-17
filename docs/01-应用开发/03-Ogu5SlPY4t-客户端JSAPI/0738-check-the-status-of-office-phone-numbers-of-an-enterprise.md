---
title: "检查某企业办公电话开通状态"
source_url: "https://open.dingtalk.com/document/development/check-the-status-of-office-phone-numbers-of-an-enterprise"
namespace: "development"
slug: "check-the-status-of-office-phone-numbers-of-an-enterprise"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 电话 > 检查某企业办公电话开通状态"
doc_id: "FAeSsUWOeV"
updated_at: "2025-09-17 21:01:15"
---

> Source: https://open.dingtalk.com/document/development/check-the-status-of-office-phone-numbers-of-an-enterprise
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 电话 > 检查某企业办公电话开通状态
> Updated: 2025-09-17 21:01:15

# 检查某企业办公电话开通状态

调用**dd.checkBizCall**检查某企业办公电话开通状态。

## 示例代码

```
dd.checkBizCall({
    corpId:'', 
    success:function(res){
        //{"isSupport":false}
    },
    fail:function(err){
    }
})
```

## **入参**

| **参数** | 说明 |
| --- | --- |
| corpId | 被检测企业的corpId。 |

## 返回结果

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| isSupport | boolean | 是否已开通。 |
