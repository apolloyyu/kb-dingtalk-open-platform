---
title: "navigateBack"
source_url: "https://open.dingtalk.com/document/development/jsapi-navigate-back"
namespace: "development"
slug: "jsapi-navigate-back"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 界面 > 路由 > navigateBack"
doc_id: "wfBKzEDpZ8"
updated_at: "2025-08-27 18:05:08"
---

> Source: https://open.dingtalk.com/document/development/jsapi-navigate-back
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 界面 > 路由 > navigateBack
> Updated: 2025-08-27 18:05:08

# navigateBack

调用dd.navigateBack关闭当前页面，返回上一级或多级页面。

可通过 getCurrentPages 获取当前的页面栈信息，决定需要返回几层。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10034) |

## 支持应用类型

| 应用类型 | 是否支持调用 |
| --- | --- |
| 企业内部应用 | 是 |
| 第三方企业应用 | 是 |
| 第三方个人应用 | 否 |

## 鉴权规则

无需鉴权即可直接调用

## **参数说明**

继承[通用输入对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 入参

- `delta`（number）：返回的页面数，如果 delta 大于现有打开的页面数，则返回到当前页面栈最顶部的页。 默认值：1。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.navigateBack({
  delta: 1,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
