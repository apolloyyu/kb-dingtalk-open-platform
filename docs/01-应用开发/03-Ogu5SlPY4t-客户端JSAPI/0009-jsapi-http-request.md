---
title: "httpRequest"
source_url: "https://open.dingtalk.com/document/development/jsapi-http-request"
namespace: "development"
slug: "jsapi-http-request"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 网络 > 发网络请求 > httpRequest"
doc_id: "zptTnxvzKn"
updated_at: "2025-08-27 18:07:18"
---

> Source: https://open.dingtalk.com/document/development/jsapi-http-request
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 网络 > 发网络请求 > httpRequest
> Updated: 2025-08-27 18:07:18

# httpRequest

调用dd.httpRequest向指定服务器发起一个跨域 http(s) 请求。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10280) |

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

- `url`（string，必填）：目标服务器url。
- `data`（object）：请求参数。
- `timeout`（number）：超时时间，单位ms，默认30000。
- `dataType`（string）：期望返回的数据格式，默认json，支持json、text、base64。
- `headers`（object）：设置请求的 HTTP 头，默认 {'Content-Type': 'application/x-www-form-urlencoded'}。
- `method`（string）：默认GET，目前支持GET和POST。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `data`（string，必填）：响应数据，格式取决于请求时的 dataType 参数。
- `status`（number，必填）：响应码。
- `headers`（object，必填）：响应头。

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 4 | 在开发者后台将上传URL设置为http安全域名。 |
| 11 | 在开发者后台将此域名添加到安全域名列表中。 |
| 12 | 由网络原因导致的错误，如网络不通等。 |
| 13 | http请求超时出现此类错误。 |
| 14 | httpRequest会根据dataType设置的类型自动对返回内容解码，解码失败时会出现此类错误。出现此类错误时，需要确定http请求返回的内容格式是否与dataType设置的类型一致。比如，当dataType类型为json时，httpRequest会将返回内容认定为json字符串，自动对内容做JSON.parse类操作，其他dataType类型类似。如果开发过程中不确定http返回内容是否OK，可以手动设置dataType为text，来查看http返回的内容。 |
| 19 | 异常http状态码错误。如500等接口异常。 |

## **示例****代码**

### 默认出入参

```
dd.httpRequest({
  url: 'http://httpbin.org/post',
  data: {},
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  timeout: 30000,
  dataType: 'json',
  success: (res) => {
    const { data, status, headers } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{
  "data": "{}",
  "status": 200,
  "headers": { "Content-Type": "application/x-www-form-urlencoded" }
}
```
