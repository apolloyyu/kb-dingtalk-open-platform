---
title: "常见问题"
source_url: "https://open.dingtalk.com/document/development/development-mlogon-faq"
namespace: "development"
slug: "development-mlogon-faq"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "认证与授权 > 身份验证（免登） > 常见问题"
doc_id: "8dX4XuC2KS"
updated_at: "2026-08-03 09:18:07"
---

> Source: https://open.dingtalk.com/document/development/development-mlogon-faq
> Path: 应用开发 / 服务端 API / 认证与授权 > 身份验证（免登） > 常见问题
> Updated: 2026-08-03 09:18:07

# 常见问题

本文介绍钉钉免登功能的常见问题及解决方案，帮助开发者快速定位和处理授权过程中的异常情况。

## 适用对象说明

文档适用于以下类型的应用：

- H5微应用
- 小程序应用（含组织小程序）

不同应用类型的免登实现方式略有差异，请根据实际应用场景选择正确的授权码获取方式。

如需了解如何创建对应类型的应用，请参考：[应用类型与能力说明](../01-XOnnmGCTbn-开发指南/0002-application-type-introduction.md)。

## 免登流程概述

身份验证“**免登**”是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户身份并完成登录的流程。

该流程基于临时授权码机制实现：前端通过 JSAPI 获取一次性临时授权码`tmp_auth_code`，服务端使用该码调用钉钉开放平台接口换取用户的`userId`等身份信息。

**关键术语说明**：`tmp_auth_code` 是通过前端 JSAPI（如`dd.getAuthCode`或`dd.runtime.permission.requestAuthCode`）获取的一次性临时授权码，有效期为 5 分钟，仅能使用一次。服务端需将其传递给钉钉 API（如`/user/get`），以换取用户身份标识。

## **可运行示例**

### **前端代码（H5 微应用）**

```
// 使用 dd SDK 获取临时授权码
dd.ready(function() {
  dd.runtime.permission.requestAuthCode({
    corpId: "your_corp_id", // 替换为企业 ID
    onSuccess: function(result) {
      const code = result.code; // 获取 tmp_auth_code
      // 发送到你的服务端
      fetch('/api/login', {
        method: 'POST',
        body: JSON.stringify({ tmp_auth_code: code }),
        headers: { 'Content-Type': 'application/json' }
      });
    },
    onFail: function(err) {
      console.error('获取授权码失败:', err);
    }
  });
});
```

### **服务端代码（Node.js 示例）**

```
const axios = require('axios');

async function getUserId(tmpAuthCode, accessToken) {
  try {
    const response = await axios.post(
      'https://oapi.dingtalk.com/topapi/v2/user/getuserinfo',
      null,
      {
        params: {
          access_token: accessToken,
          code: tmpAuthCode
        }
      }
    );
    if (response.data.errcode === 0) {
      return response.data.result.userid;
    } else {
      throw new Error(`获取用户信息失败: ${response.data.errmsg}`);
    }
  } catch (error) {
    console.error('接口调用异常:', error.message);
  }
}
```

## 常见错误码解析

在各类免登场景中，可能遇见的错误及原因如下。

- **errcode=40078, errmsg=不存在的临时授权码**

  可能原因如下：

  - **未正确获取免登授权码**

    - 小程序应用请通过[getAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0006-jsapi-get-auth-code.md)获取；
    - H5微应用请通过 [requestAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0008-jsapi-request-auth-code.md)或[getOperateAuthCode](../03-Ogu5SlPY4t-客户端-JSAPI/0009-jsapi-get-operate-auth-code.md)获取。
  - **授权码已过期**

    - 免登授权码生成后，有效期为 **5分钟**，超过时间则失效。
  - **授权码已被使用**

    - 免登授权码为一次性凭证，一旦使用即失效，不可重复调用。
  - **授权码类型混用**

    - 例如：使用管理后台的免登授权码传入企业内部应用接口获取用户 `userId`，会导致此错误。
- **errcode=41007, errmsg=无效的ssocode**

  可能原因如下：

  - **ssoCode 不存在或拼写错误**

    - 检查前端传递的 `ssoCode` 参数值是否完整、无截断。
  - **ssoCode 已过期**

    - ssoCode 通常具有较短的有效期（约5分钟），请确保及时使用。
  - **ssoCode 已被消费**

    - 该码为一次性使用，若已在其他请求中使用，则后续调用将失败。
- **errcode=41026, errmsg=缺少tmp\_auth\_code**

  可能原因如下：

  - 请求参数中未包含 `tmp_auth_code` 字段；
  - 参数名拼写错误（如写成 `temp_auth_code` 或 `authCode`）；
  - 参数未通过 QueryString 正确传递（应为 `?tmp_auth_code=xxx` 形式）；
  - 前端未成功返回授权码，导致服务端无法构造完整请求。
  > 解决方案：检查前端是否正确回调并传递 `code` 值，服务端需明确接收 `tmp_auth_code` 参数。
- **errcode=40079, errmsg=不存在的授权信息**

  可能原因如下：

  - 应用尚未完成授权流程，用户未完成登录确认；
  - 用户非应用可见范围内的成员（如不在通讯录中或未被授权访问）；
  - 应用权限未正确配置，未开启“免登”相关能力；
  - 调用时机过早，在用户上下文未准备好时尝试获取授权码。
  > 建议：在调用前增加判断逻辑，确保用户已进入应用且客户端环境就绪。
- **errcode=40087, errmsg=创建永久授权码失败**

  可能原因如下：

  - 当前应用类型不支持创建永久授权码；
  - 缺少必要的权限配置（如“持久授权”权限未开启）；
  - 调用接口频率过高，触发限流机制；
  - 应用状态异常（如被禁用或审核中）。
- **errcode=40091, errmsg=缺少tmp\_auth\_code**

  可能原因如下：

  - 创建持久授权码时未提供有效的临时授权码（`tmp_auth_code`）；
  - 用户未完成授权动作，导致临时码为空；
  - 参数未正确传递至创建接口。
  > 解决方案：引导用户重新授权，从前端重新获取 `authCode` 并提交至服务端用于创建持久授权码。
