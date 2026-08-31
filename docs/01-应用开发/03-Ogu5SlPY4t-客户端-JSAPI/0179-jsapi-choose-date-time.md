---
title: "chooseDateTime"
source_url: "https://open.dingtalk.com/document/development/jsapi-choose-date-time"
namespace: "development"
slug: "jsapi-choose-date-time"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 选择日期 > chooseDateTime"
doc_id: "YBZwFKTiyC"
updated_at: "2025-08-27 18:06:21"
---

> Source: https://open.dingtalk.com/document/development/jsapi-choose-date-time
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 选择日期 > chooseDateTime
> Updated: 2025-08-27 18:06:21

# chooseDateTime

调用chooseDateTime，选择日期和时间。

> 选择的时间精确到分钟。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11712) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11712) |

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

- `default`（number，必填）：时间戳，默认选中日期时间，单位为毫秒。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 字段说明

- `chosen`（number，必填）：时间戳，用户选择的日期时间，单位为毫秒。
- `timezone`（number，必填）：整型，用户当前所在时区，例如8为第八时区。

## **示例****代码**

### 默认出入参

```
dd.chooseDateTime({
  default: 1494415396228,
  success: (res) => {
    const { chosen, timezone } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "chosen": 1580796000000, "timezone": 8 }
```
