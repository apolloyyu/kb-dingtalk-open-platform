---
title: "getStorage"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-storage"
namespace: "development"
slug: "jsapi-get-storage"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 缓存 > getStorage"
doc_id: "zn56GKN5sl"
updated_at: "2025-08-27 18:07:06"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-storage
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 缓存 > getStorage
> Updated: 2025-08-27 18:07:06

# getStorage

调用getStorage，获取缓存数据，可以获取指定key的单条缓存数据。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10246) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.5.60 | 6.5.60 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10246) |

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
dd.getStorage({
  key: 'key1',
  success: (res) => {
    const {} = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{}
```
