---
title: "showTabBarRedDot"
source_url: "https://open.dingtalk.com/document/development/jsapi-show-tab-bar-red-dot"
namespace: "development"
slug: "jsapi-show-tab-bar-red-dot"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > TabBar > showTabBarRedDot"
doc_id: "thLaGoumok"
updated_at: "2025-08-27 18:05:06"
---

> Source: https://open.dingtalk.com/document/development/jsapi-show-tab-bar-red-dot
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > TabBar > showTabBarRedDot
> Updated: 2025-08-27 18:05:06

# showTabBarRedDot

调用showTabBarRedDot，显示tabBar红点。

> 显示tabBar某一项的右上角的红点。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10061) |

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

- `index`（number，必填）：tabBar 的哪一项，从左边算起。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.showTabBarRedDot({
  index: 1,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
