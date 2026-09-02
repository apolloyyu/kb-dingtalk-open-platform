---
title: "clearStorageSync"
source_url: "https://open.dingtalk.com/document/development/jsapi-clear-storage-sync"
namespace: "development"
slug: "jsapi-clear-storage-sync"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 缓存 > clearStorageSync"
doc_id: "KnCq7ZDqkj"
updated_at: "2025-08-27 18:07:06"
---

> Source: https://open.dingtalk.com/document/development/jsapi-clear-storage-sync
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 缓存 > clearStorageSync
> Updated: 2025-08-27 18:07:06

# clearStorageSync

调用clearStorageSync，同步清楚本地缓存数据。

> 小程序使用webview内嵌页面的缓存与小程序storage缓存信息是相互隔离的，即调用本接口只能清除本地 storage 下所有的缓存信息，无法清除webview内嵌页面的缓存。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10251) |

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

### 入参

（object）

## **错误码**

| **错误码** | **描述** |
| --- | --- |
| 3 | 系统异常 |

## **示例****代码**

### 默认出入参

```
dd.clearStorageSync();
```

`success`返回对象示例：

```
{}
```
