---
title: "setNavigationBar"
source_url: "https://open.dingtalk.com/document/development/jsapi-set-navigation-bar"
namespace: "development"
slug: "jsapi-set-navigation-bar"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > 导航栏 > setNavigationBar"
doc_id: "HBLMyHLR7C"
updated_at: "2025-08-27 18:05:01"
---

> Source: https://open.dingtalk.com/document/development/jsapi-set-navigation-bar
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > 导航栏 > setNavigationBar
> Updated: 2025-08-27 18:05:01

# setNavigationBar

调用setNavigationBar，设置导航栏。

> 设置小程序导航栏样式及标题等。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10048) |

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

- `title`（string，必填）：导航栏标题。
- `backgroundColor`（string，必填）：导航栏背景色，支持十六进制颜色值。
- `reset`（boolean，必填）：是否重置导航栏为钉钉默认配色。 默认值： false。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.setNavigationBar({
  reset: false,
  title: '你好',
  backgroundColor: '#108ee9',
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
