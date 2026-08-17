---
title: "拨打钉钉电话"
source_url: "https://open.dingtalk.com/document/development/call-dingtalk"
namespace: "development"
slug: "call-dingtalk"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 开放接口 > 电话 > 拨打钉钉电话"
doc_id: "Top8V7CapV"
updated_at: "2025-09-17 21:01:14"
---

> Source: https://open.dingtalk.com/document/development/call-dingtalk
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 开放接口 > 电话 > 拨打钉钉电话
> Updated: 2025-09-17 21:01:14

# 拨打钉钉电话

调用**dd.callUsers**拨打钉钉电话。

## 示例代码

```
dd.callUsers({
    users: ['101'], //用户列表，工号
    success:function(res){   
    },
    fail:function(err){
    }
})
```

## 入参

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| users | String[] | 用户列表，工号。 |
