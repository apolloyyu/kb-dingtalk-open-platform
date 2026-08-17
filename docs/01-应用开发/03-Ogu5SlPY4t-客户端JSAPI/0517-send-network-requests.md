---
title: "发网络请求"
source_url: "https://open.dingtalk.com/document/development/send-network-requests"
namespace: "development"
slug: "send-network-requests"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "历史文档（不推荐） > 小程序 > 网络 > 发网络请求"
doc_id: "C0NZsYkG0S"
updated_at: "2025-09-17 20:58:47"
---

> Source: https://open.dingtalk.com/document/development/send-network-requests
> Path: 应用开发 / 客户端JSAPI / 历史文档（不推荐） > 小程序 > 网络 > 发网络请求
> Updated: 2025-09-17 20:58:47

# 发网络请求

调用dd.httpRequest向指定服务器发起一个跨域 http(s) 请求。

确保在发起网络请求前，已在[开发者后台](http://open-dev.dingtalk.com/)设置应用**安全域名**。

![iShot2022-10-18 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0673606661/p505244.png)

## 扫码体验

![扫码发送网络请求](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9696800161/p211121.png)

## **示例代码**

```
// Content-Type为application/x-www-form-urlencoded即默认的接口请求方式
dd.httpRequest({
  url: 'http://httpbin.org/post',
  method: 'POST',
  data: {
    from: '钉钉',
    production: 'DingTalk',
  },
  dataType: 'json',
  success: function(res) {
    dd.alert({content: 'success'});
  },
  fail: function(res) {
    dd.alert({content: 'fail'});
  },
  complete: function(res) {
    dd.alert({content: 'complete'});
  }
});

// Content-Type为application/json时，data参数只支持json字符串，用户需要手动调用JSON.stringify进行序列化
dd.httpRequest({
  headers: {
    "Content-Type": "application/json"
  },
  url: 'http://httpbin.org/post',
  method: 'POST',
  // 需要手动调用JSON.stringify将数据进行序列化
  data: JSON.stringify({
    from: '钉钉',
    production: 'DingTalk',
  }),
  dataType: 'json',
  success: function(res) {
    dd.alert({content: 'success'});
  },
  fail: function(res) {
    dd.alert({content: 'fail'});
  },
  complete: function(res) {
    dd.alert({content: 'complete'});
  }
});
```

## **入参**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| url | String | 是 | 目标服务器url。 |
| headers | Object | 否 | 设置请求的 HTTP 头，默认 {'Content-Type': 'application/x-www-form-urlencoded'}。 |
| method | String | 否 | 默认GET，目前支持GET和POST。 |
| data | Object | 否 | 请求参数。 |
| timeout | Number | 否 | 超时时间，单位ms，默认30000。 |
| dataType | String | 否 | 期望返回的数据格式，默认json，支持json、text、base64。 |
| success | Function | 否 | 调用成功的回调函数。 |
| fail | Function | 否 | 调用失败的回调函数。 |
| complete | Function | 否 | 调用结束的回调函数（调用成功、失败都会执行）。 |

**success 返回值**

| **名称** | **类型** | **描述** |
| --- | --- | --- |
| data | String | 响应数据，格式取决于请求时的 dataType 参数。 |
| status | Number | 响应码。 |
| headers | Object | 响应头。 |

## **错误码**

| **错误码** | **描述** | 解决方案 |
| --- | --- | --- |
| 4 | 设置错误。 | 在开发者后台将上传URL设置为HTTP安全域名。 |
| 11 | 无权跨域。 | 在开发者后台将此域名添加到安全域名列表中。 |
| 12 | 网络出错。 | 由网络原因导致的错误，如网络不通等。 |
| 13 | 超时。 | http请求超时出现此类错误。 |
| 14 | 解码失败。 | httpRequest会根据dataType设置的类型自动对返回内容解码，解码失败时会出现此类错误。出现此类错误时，需要确定http请求返回的内容格式是否与dataType设置的类型一致。比如，当dataType类型为json时，httpRequest会将返回内容认定为json字符串，自动对内容做JSON.parse类操作，其他dataType类型类似。如果开发过程中不确定http返回内容是否OK，可以手动设置dataType为text，来查看http返回的内容。 |
| 19 | HTTP错误 | 异常http状态码错误。如500等接口异常。 |
