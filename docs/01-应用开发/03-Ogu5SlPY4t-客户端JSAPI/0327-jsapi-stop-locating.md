---
title: "stopLocating"
source_url: "https://open.dingtalk.com/document/development/jsapi-stop-locating"
namespace: "development"
slug: "jsapi-stop-locating"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "位置服务 > stopLocating"
doc_id: "EvgOTARmkb"
updated_at: "2025-08-27 18:07:16"
---

> Source: https://open.dingtalk.com/document/development/jsapi-stop-locating
> Path: 应用开发 / 客户端JSAPI / 位置服务 > stopLocating
> Updated: 2025-08-27 18:07:16

# stopLocating

调用stopLocating，停止连续定位。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11677) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11677) |

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

- `sceneId`（string，必填）：停止的定位场景id。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

- `sceneId`（string，必填）：停止的定位场景id，或者null。

## **示例****代码**

### 默认出入参

```
dd.stopLocating({
  sceneId: '停止的定位场景id',
  success: (res) => {
    const { sceneId } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "sceneId": "******" }
```
