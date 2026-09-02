---
title: "removeCachedAPIResponse"
source_url: "https://open.dingtalk.com/document/development/jsapi-remove-cached-a-p-i-response"
namespace: "development"
slug: "jsapi-remove-cached-a-p-i-response"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "设备能力 > 内存不足处理 > removeCachedAPIResponse"
doc_id: "702lcs0vJg"
updated_at: "2025-10-16 15:45:34"
---

> Source: https://open.dingtalk.com/document/development/jsapi-remove-cached-a-p-i-response
> Path: 应用开发 / 客户端 JSAPI / 设备能力 > 内存不足处理 > removeCachedAPIResponse
> Updated: 2025-10-16 15:45:34

# removeCachedAPIResponse

删除已缓存的JSAPI返回值

清除当前页面上已缓存的 JSAPI 返回值，例如页面表单提交成功后，就可以清空之前的 JSAPI 缓存。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11930) |
| 小程序 | 不支持 | 8.0.15 | 不支持 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11930) |

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

- `jsapiName`（string，必填）：需要清除的 JSAPI 名称
- `removeAll`（boolean，必填）：是否清除所有 JSAPI 的返回值缓存，默认 false

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认Demo标题

```
dd.removeCachedAPIResponse({
  jsapiName: 'biz.util.chooseImage',
  removeAll: false,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
