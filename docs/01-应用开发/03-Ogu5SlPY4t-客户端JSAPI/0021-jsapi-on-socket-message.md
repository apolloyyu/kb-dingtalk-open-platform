---
title: "onSocketMessage"
source_url: "https://open.dingtalk.com/document/development/jsapi-on-socket-message"
namespace: "development"
slug: "jsapi-on-socket-message"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 网络 > WebSocket > onSocketMessage"
doc_id: "RxGFE2YaXy"
updated_at: "2025-08-27 18:07:25"
---

> Source: https://open.dingtalk.com/document/development/jsapi-on-socket-message
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 网络 > WebSocket > onSocketMessage
> Updated: 2025-08-27 18:07:25

# onSocketMessage

调用onSocketMessage，监听WebSocket接收到服务器的消息事件。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 7.0.10 | 7.0.10 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10289) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `data`（string，必填）：服务器返回的消息。   
    
  > 普通的文本String或者经base64编码后的String。
- `isBuffer`（boolean，必填）：\* true：data字段表示接收到的经过了base64编码后的String，  
  \* false：data字段表示接收到的普通String文本。

## **示例****代码**

### 默认出入参

```
dd.onSocketMessage((res) => {
  const { data, isBuffer } = res;
});
```

返回对象示例：

```
{ "data": "abc", "isBuffer": false }
```
