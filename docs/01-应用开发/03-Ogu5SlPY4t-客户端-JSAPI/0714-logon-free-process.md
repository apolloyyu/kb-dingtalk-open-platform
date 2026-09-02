---
title: "免登流程"
source_url: "https://open.dingtalk.com/document/development/logon-free-process"
namespace: "development"
slug: "logon-free-process"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "历史文档（不推荐） > H5微应用 > 免登流程"
doc_id: "15Ieace2tc"
updated_at: "2026-09-02 18:13:59"
---

> Source: https://open.dingtalk.com/document/development/logon-free-process
> Path: 应用开发 / 客户端 JSAPI / 历史文档（不推荐） > H5微应用 > 免登流程
> Updated: 2026-09-02 18:13:59

# 免登流程

“**免登**”是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户身份，进而登录系统的流程。

## 获取微应用免登授权码

使用以下代码获取免登授权码（调用此api不需要进行鉴权，即不需要进行dd.config）。获取的免登授权码有效期5分钟，且只能使用一次。接口说明，请参考[获取微应用免登授权码](0716-obtain-the-micro-application-exemption-authorization-code.md)。

> **[!NOTE]**
>
> 第三方企业应用可以在微应用的首页URL中使用**$CORPID$**做为参数占位符，钉钉容器会将**$CORPID$**替换为当前访问用户的企业corpId。
>
> 例如，微应用首页地址为https://www.dingtalk.com，需要获取当前访问用户的企业corpId值，微应用首页地址可改为https://www.dingtalk.com?corpId=$CORPID$。在进入该首页地址页面时，使用js方法获取当前页面URL，即可获取corpId值。

```
dd.ready(function() {
    dd.runtime.permission.requestAuthCode({
        corpId: "ding12345xxx", // 企业id
        onSuccess: function (info) {
                  code = info.code // 通过该免登授权码可以获取用户身份
        }});
});
```

## 通过免登授权码换取用户身份

可以通过免登授权码和access\_token获取用户的userid，然后通过userid获取用户的详细信息，详情请参考[网页应用（H5微应用）免登](../02-4a8AMF6u2A-服务端-API/0018-enterprise-internal-application-logon-free.md)。
