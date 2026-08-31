---
title: "setStorage"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-storage"
namespace: "development"
slug: "jsapi-set-storage"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 缓存 > setStorage"
doc_id: "hrDV4ygOPl"
updated_at: "2025-08-27 18:07:10"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-storage
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 缓存 > setStorage
> Updated: 2025-08-27 18:07:10

# setStorage

调用setStorage，将数据存储在本地缓存中指定的 key 中，会覆盖掉原来该 key 对应的数据。

> 单条数据转换成字符串后，字符串长度最大200\*1024。同一个钉钉用户，同一个小程序缓存总上限为10MB。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10244) |
| 小程序 | 7.0.0 | 7.0.0 | 7.0.0 | 7.0.0 | 7.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10244) |

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
dd.setStorage({
  key: 'currentCity',
  data: '杭州',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
