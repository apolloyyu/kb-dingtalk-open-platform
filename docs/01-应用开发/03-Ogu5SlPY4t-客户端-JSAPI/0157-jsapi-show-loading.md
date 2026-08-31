---
title: "showLoading"
source_url: "https://open.dingtalk.com/document/development/jsapi-show-loading"
namespace: "development"
slug: "jsapi-show-loading"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 交互反馈 > showLoading"
doc_id: "q8S2zZWj7W"
updated_at: "2025-08-27 18:06:07"
---

> Source: https://open.dingtalk.com/document/development/jsapi-show-loading
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 交互反馈 > showLoading
> Updated: 2025-08-27 18:06:07

# showLoading

调用dd.showLoading显示加载提示，可与dd.hideLoading配合使用。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 7.0.10 | 7.0.10 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10070) |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10070) |

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

- `content`（string，必填）：loading的文字内容。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.showLoading({
  content: '加载中...',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
