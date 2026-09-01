---
title: "免登授权码"
source_url: "https://open.dingtalk.com/document/development/mini-program-free-login"
namespace: "development"
slug: "mini-program-free-login"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 基础 API > 免登授权码"
doc_id: "kcTFGpit02"
updated_at: "2026-09-01 09:16:31"
---

> Source: https://open.dingtalk.com/document/development/mini-program-free-login
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > 小程序 > 基础 API > 免登授权码
> Updated: 2026-09-01 09:16:31

# 免登授权码

调用dd.getAuthCode接口获取小程序免登授权码。

免登是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户身份登录系统的流程。企业应用和个人应用的免登授权码均可通过该JSAPI获取。

```
dd.getAuthCode({
    success:function(res){
        /*{
            authCode: 'hYLK98jkf0m' //string authCode
        }*/
    },
    fail:function(err){
    }
});
```

**返回说明：**

| **参数** | **说明** |
| --- | --- |
| authCode | 授权码。有效期5分钟，且只能使用一次，使用后会失效。 |

## 通过免登授权码换取用户身份

- [网页应用（H5微应用）免登](../02-4a8AMF6u2A-服务端-API/0018-enterprise-internal-application-logon-free.md)
