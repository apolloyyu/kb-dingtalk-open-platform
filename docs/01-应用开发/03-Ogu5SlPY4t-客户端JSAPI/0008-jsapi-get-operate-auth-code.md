---
title: "getOperateAuthCode"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-operate-auth-code"
namespace: "development"
slug: "jsapi-get-operate-auth-code"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "获取凭证 > getOperateAuthCode"
doc_id: "W74JUsfTgo"
updated_at: "2025-08-27 18:08:51"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-operate-auth-code
> Path: 应用开发 / 客户端JSAPI / 获取凭证 > getOperateAuthCode
> Updated: 2025-08-27 18:08:51

# getOperateAuthCode

调用getOperateAuthCode，获取微应用反馈式操作的临时授权码。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11658) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11658) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

在H5应用中，调用[dd.config](https://open.dingtalk.com/document/orgapp/jsapi-authentication)完成鉴权后使用

在小程序应用中，无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `corpId`（string，必填）：企业的corpid。  
    
  > 第三方企业应用可以在微应用的首页URL中使用$CORPID$做为参数占位符，钉钉容器会将$CORPID$替换为当前访问用户的企业corpId。
- `agentId`（string，必填）：企业内部微应用ID，可以从授权信息中获取到。必须与dd.config的agentId一致。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `code`（string，必填）：微应用反馈式操作的临时授权码，有效期5分钟，且只能使用一次，使用后会失效。

## **示例****代码**

### 默认出入参

```
dd.getOperateAuthCode({
  corpId: 'ding1234xxxx',
  agentId: '2179124000',
  success: (res) => {
    const { code } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "code": "hYLK98jkf0m" }
```
