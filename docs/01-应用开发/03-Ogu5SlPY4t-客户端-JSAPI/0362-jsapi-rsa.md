---
title: "rsa"
source_url: "https://open.dingtalk.com/document/development/jsapi-rsa"
namespace: "development"
slug: "jsapi-rsa"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 系统信息 > rsa"
doc_id: "JD62CdTRgB"
updated_at: "2025-08-27 18:07:32"
---

> Source: https://open.dingtalk.com/document/development/jsapi-rsa
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 系统信息 > rsa
> Updated: 2025-08-27 18:07:32

# rsa

调用rsa，实现rsa加解密。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.0 | 7.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11619) |
| 小程序 | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11619) |

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

- `key`（string，必填）：RSA 密钥。PKCS8 格式。 加密使用公钥，解密使用私钥。
- `text`（string，必填）：算法输入。加密时传入明文，解密时传入密文（base64 编码）。RSA key 为 1024 位时，最多支持 117 个字节。
- `action`（string，必填）：使用 RSA 加密还是 RSA 解密。可选值：encrypt / decrypt

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `text`（string，必填）：算法输出。加密时得到密文（base64 编码），解密时得到明文。

## **示例****代码**

### 默认出入参

```
dd.rsa({
  key: 'key示例值',
  text: 'text示例值',
  action: 'action示例值',
  success: (res) => {
    const { text } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "text": "result示例值" }
```
