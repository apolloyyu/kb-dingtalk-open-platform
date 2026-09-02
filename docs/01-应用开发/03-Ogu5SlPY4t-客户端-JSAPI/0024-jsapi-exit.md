---
title: "exit"
source_url: "https://open.dingtalk.com/document/development/jsapi-exit"
namespace: "development"
slug: "jsapi-exit"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 基础 > exit"
doc_id: "P9pny0F7Qa"
updated_at: "2025-08-27 18:04:55"
---

> Source: https://open.dingtalk.com/document/development/jsapi-exit
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 基础 > exit
> Updated: 2025-08-27 18:04:55

# exit

关闭钉钉小程序。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11552) |

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
dd.exit({
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
