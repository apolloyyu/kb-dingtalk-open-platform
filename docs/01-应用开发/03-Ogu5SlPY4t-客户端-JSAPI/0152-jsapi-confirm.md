---
title: "confirm"
source_url: "https://open.dingtalk.com/document/development/jsapi-confirm"
namespace: "development"
slug: "jsapi-confirm"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 交互反馈 > confirm"
doc_id: "FQJpDCcQGX"
updated_at: "2025-08-27 18:06:04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-confirm
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 交互反馈 > confirm
> Updated: 2025-08-27 18:06:04

# confirm

调用dd.confirm显示确认框，可以配置确认框的标题、内容、确认或取消按钮的文字等。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10066) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.5.60 | 6.5.60 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10066) |

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

- `title`（string，必填）：confirm框的标题。
- `content`（string，必填）：confirm框的内容。
- `confirmButtonText`（string）：确认按钮文字。
- `cancelButtonText`（string）：取消按钮文字。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `confirm`（boolean）：返回操作button的结果，确定按钮返回true，取消按钮返回false。

## **示例****代码**

### 默认出入参

```
dd.confirm({
  title: '提交确认',
  content: '提交后没法修改，确定提交吗？',
  cancelButtonText: '我再想想',
  confirmButtonText: '提交',
  success: (res) => {
    const { confirm } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "confirm": true }
```
