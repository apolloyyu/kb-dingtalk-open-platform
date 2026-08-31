---
title: "getStorageInfo"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-storage-info"
namespace: "development"
slug: "jsapi-get-storage-info"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 缓存 > getStorageInfo"
doc_id: "Vy3tgdejoz"
updated_at: "2025-08-27 18:07:07"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-storage-info
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 缓存 > getStorageInfo
> Updated: 2025-08-27 18:07:07

# getStorageInfo

调用getStorageInfo，异步获取当前storage的相关信息。

> 小程序缓存具有钉钉账号和小程序两级隔离，即当切换钉钉账号或小程序时，无法获取原账号下某小程序设置的缓存信息。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10252) |

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

- `keys`（array，必填）：当前 storage 中所有的 key。
- `limitSize`（number，必填）：限制的空间大小，单位为 KB。
- `currentSize`（number，必填）：当前占用的空间大小, 单位为 KB。

## **示例****代码**

### 默认出入参

```
dd.getStorageInfo();
```

`success`返回对象示例：

```
{ "keys": [`keys示例值1`, `keys示例值2`], "limitSize": 45, "currentSize": 85 }
```
