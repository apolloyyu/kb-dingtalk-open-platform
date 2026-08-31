---
title: "timePicker"
source_url: "https://open.dingtalk.com/document/development/jsapi-time-picker"
namespace: "development"
slug: "jsapi-time-picker"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 选择日期 > timePicker"
doc_id: "AxIO4Dw9dS"
updated_at: "2025-08-27 18:06:24"
---

> Source: https://open.dingtalk.com/document/development/jsapi-time-picker
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 选择日期 > timePicker
> Updated: 2025-08-27 18:06:24

# timePicker

调用timePicker，时间选择器。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11708) |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11708) |

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

- `format`（string，必填）：时间格式，固定为HH:mm，例如07:40。
- `value`（string）：默认选中的时间。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 字段说明

- `value`（string，必填）：返回选择的时间。

## **示例****代码**

### 默认出入参

```
dd.timePicker({
  value: '07:40',
  format: 'HH:mm',
  success: (res) => {
    const { value } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "value": "07:40" }
```
