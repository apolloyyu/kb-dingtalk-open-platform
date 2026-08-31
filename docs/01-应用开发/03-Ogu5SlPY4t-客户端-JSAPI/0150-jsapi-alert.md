---
title: "alert"
source_url: "https://open.dingtalk.com/document/development/jsapi-alert"
namespace: "development"
slug: "jsapi-alert"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 交互反馈 > alert"
doc_id: "dV5eC19S18"
updated_at: "2025-08-27 18:06:03"
---

> Source: https://open.dingtalk.com/document/development/jsapi-alert
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 交互反馈 > alert
> Updated: 2025-08-27 18:06:03

# alert

调用dd.alert显示警告框，可以设置警告框的标题、内容、按钮文字等。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10065) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10065) |

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

- `title`（string，必填）：alert框的标题。
- `content`（string，必填）：alert框的内容。
- `buttonText`（string）：按钮文字。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.alert({
  title: '消息提示',
  content: '请求发布成功',
  buttonText: '我知道了',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
