---
title: "getAuthCode"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-auth-code"
namespace: "development"
slug: "jsapi-get-auth-code"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "获取凭证 > getAuthCode"
doc_id: "g8rSsXuydW"
updated_at: "2025-08-27 18:08:50"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-auth-code
> Path: 应用开发 / 客户端JSAPI / 获取凭证 > getAuthCode
> Updated: 2025-08-27 18:08:50

# getAuthCode

调用 dd.getAuthCode，获取应用免登授权码。

> - 免登是指用户进入应用后，无需输入钉钉用户名和密码，应用程序可自动获取当前用户登录系统的流程。
> - 在免登流程中需要向钉钉获取免登授权码，即是通过调用该api获取。获取的免登授权码有效期5分钟，且只能使用一次。

具体免登流程如下：

1. 调用本接口获取免登授权码。
2. 调用[获取应用的 Access Token](https://open.dingtalk.com/document/orgapp/api-gettoken)接口，获取应用访问凭证。
3. 调用[通过免登码获取用户信息](https://open.dingtalk.com/document/orgapp/obtain-the-userid-of-a-user-by-using-the-log-free)接口，获取用户userid。
4. 调用[查询用户详情](https://open.dingtalk.com/document/orgapp/query-user-details)接口，获取用户信息。

> 小程序免登具体操作内容，可参考[小程序应用免登](https://open.dingtalk.com/document/orgapp/small-program-application-free-of-registration)，包含Demo 示例。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10295) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `corpId`（string，必填）：企业 CorpID。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `authCode`（string，必填）：授权码。有效期5分钟，且只能使用一次，使用后会失效。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.getAuthCode({
  corpId: 'ding12345xxx',
  success: (res) => {
    const { authCode } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "authCode": "hYLK98jkf0m" }
```
