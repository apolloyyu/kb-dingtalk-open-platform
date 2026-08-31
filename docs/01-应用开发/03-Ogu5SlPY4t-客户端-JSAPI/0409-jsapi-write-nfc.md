---
title: "writeNFC"
source_url: "https://open.dingtalk.com/document/development/jsapi-write-nfc"
namespace: "development"
slug: "jsapi-write-nfc"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > NFC > writeNFC"
doc_id: "IypLcGswyM"
updated_at: "2025-08-27 18:08:03"
---

> Source: https://open.dingtalk.com/document/development/jsapi-write-nfc
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > NFC > writeNFC
> Updated: 2025-08-27 18:08:03

# writeNFC

调用writeNFC，实现NFC数据写入。

首先调用此JSAPI，再把芯片放上去，即可读取。调用一次jsapi读取一次信息，支持NDEF的数据交换格式。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 不支持 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11699) |
| 小程序 | 6.0.0 | 不支持 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11699) |

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

- `content`（string，必填）：NFC芯片的内容。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.writeNFC({
  content: 'aaa',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
