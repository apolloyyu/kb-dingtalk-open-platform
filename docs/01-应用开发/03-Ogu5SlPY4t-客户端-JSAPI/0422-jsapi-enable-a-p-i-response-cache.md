---
title: "enableAPIResponseCache"
source_url: "https://open.dingtalk.com/document/development/jsapi-enable-a-p-i-response-cache"
namespace: "development"
slug: "jsapi-enable-a-p-i-response-cache"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 内存不足处理 > enableAPIResponseCache"
doc_id: "fMONr2mW0V"
updated_at: "2025-10-16 15:45:36"
---

> Source: https://open.dingtalk.com/document/development/jsapi-enable-a-p-i-response-cache
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 内存不足处理 > enableAPIResponseCache
> Updated: 2025-10-16 15:45:36

# enableAPIResponseCache

开启JSAPI返回值缓存

开启 JSAPI 返回值缓存，在调用耗内存的 JSAPI 前调用。
开启后，使用 getCachedAPIResponse 获取调用后缓存的 JSAPI 返回值。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11928) |
| 小程序 | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11928) |

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

- `enable`（boolean，必填）：true 开启，false 关闭

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认Demo标题

```
dd.enableAPIResponseCache({
  enable: true,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
