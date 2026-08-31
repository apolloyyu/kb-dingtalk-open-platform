---
title: "SelectorQuery.exec"
source_url: "https://open.dingtalk.com/document/development/jsapi-selector-query-exec"
namespace: "development"
slug: "jsapi-selector-query-exec"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 节点查询 > SelectorQuery.exec"
doc_id: "w7av8dZUlo"
updated_at: "2025-08-27 18:06:17"
---

> Source: https://open.dingtalk.com/document/development/jsapi-selector-query-exec
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 节点查询 > SelectorQuery.exec
> Updated: 2025-08-27 18:06:17

# SelectorQuery.exec

调用SelectorQuery.exec，将查询结果放入 callback 回调中。

> 查询结果为数组，每项为一次查询的结果，如果当前是节点列表，则单次查询结果也为数组。exec 必须放到 Page onReady 后调用。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10042) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 是 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.SelectorQuery.exec({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
