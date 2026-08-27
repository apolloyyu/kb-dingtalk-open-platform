---
title: "connectSocket"
source_url: "https://open.dingtalk.com/document/development/jsapi-connect-socket"
namespace: "development"
slug: "jsapi-connect-socket"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 网络 > WebSocket > connectSocket"
doc_id: "Uw8xlhVpfw"
updated_at: "2025-08-27 18:07:21"
---

> Source: https://open.dingtalk.com/document/development/jsapi-connect-socket
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 网络 > WebSocket > connectSocket
> Updated: 2025-08-27 18:07:21

# connectSocket

调用connectSocket，创建一个 WebSocket 的连接。

一个钉钉小程序同时只能保留一个 WebSocket 连接，如果当前已存在 WebSocket 连接，会自动关闭该连接，并重新创建一个新的 WebSocket 连接。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 7.0.15 | 7.0.15 | 7.0.0 | 7.0.15 | 7.0.15 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10283) |

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
- `data`（object）：请求的参数。
- `header`（object）：请求的头部。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 1 | 当前端不支持此API |
| 2 | 参数无效 |
| 3 | 系统异常 |
| 4 | 在开发者后台将上传URL设置为http安全域名。 |
| 5 | corpId 获取不到 |
| 6 | 创建会话失败 |
| 7 | 服务器返回的https证书无效。 |
| 8 | 服务端返回协议头无效。 |
| 9 | WebSocket请求没有指定Sec-WebSocket-Protocol请求头。 |
| 10 | 网络连接没有打开，无法发送消息。 |
| 11 | 在开发者后台将此域名添加到安全域名列表中。 |
| 12 | 由网络原因导致的错误，如网络不通等。 |

## **示例****代码**

### 默认出入参

```
dd.connectSocket({
  url: 'wss://aa.bb.com',
  data: {},
  header: {},
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
