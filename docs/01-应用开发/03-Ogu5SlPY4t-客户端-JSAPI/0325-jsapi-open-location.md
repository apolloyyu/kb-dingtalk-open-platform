---
title: "openLocation"
source_url: "https://open.dingtalk.com/document/development/jsapi-open-location"
namespace: "development"
slug: "jsapi-open-location"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "位置服务 > openLocation"
doc_id: "bzhJe7uxkT"
updated_at: "2025-08-27 18:07:15"
---

> Source: https://open.dingtalk.com/document/development/jsapi-open-location
> Path: 应用开发 / 客户端 JSAPI / 位置服务 > openLocation
> Updated: 2025-08-27 18:07:15

# openLocation

调用openLocation，使用内置地图查看位置。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10257) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10257) |

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

- `address`（string，必填）：位置描述。
- `latitude`（string，必填）：纬度，范围为 -90~90，负数表示南纬。
- `longitude`（string，必填）：经度，范围为 -180~180，负数表示西经。
- `title`（string，必填）：在地图锚点气泡显示的文案。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.openLocation({
  title: '北京国家广告产业园',
  address: '学院路77号',
  latitude: '120.126293',
  longitude: '30.274653',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
