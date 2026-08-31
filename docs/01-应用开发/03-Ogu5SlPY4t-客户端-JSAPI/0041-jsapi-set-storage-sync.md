---
title: "setStorageSync"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-storage-sync"
namespace: "development"
slug: "jsapi-set-storage-sync"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 缓存 > setStorageSync"
doc_id: "wa0LJJCXPG"
updated_at: "2025-08-27 18:07:10"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-storage-sync
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 缓存 > setStorageSync
> Updated: 2025-08-27 18:07:10

# setStorageSync

调用dd.setStorageSync同步将数据存储在本地缓存中指定的 key 中。

同步数据IO操作可能会影响小程序流畅度，建议使用异步接口，或谨慎处理调用异常。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10245) |

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

- `key`（string，必填）：缓存数据的key。
- `data`（string，必填）：要缓存的数据。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.setStorageSync({
  key: 'city',
  data: '杭州',
});
```
