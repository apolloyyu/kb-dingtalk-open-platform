---
title: "removeTabBarItem"
source_url: "https://open.dingtalk.com/document/development/jsapi-remove-tab-bar-item"
namespace: "development"
slug: "jsapi-remove-tab-bar-item"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 界面 > TabBar > removeTabBarItem"
doc_id: "FgmvH7HaGI"
updated_at: "2025-08-27 18:05:04"
---

> Source: https://open.dingtalk.com/document/development/jsapi-remove-tab-bar-item
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 界面 > TabBar > removeTabBarItem
> Updated: 2025-08-27 18:05:04

# removeTabBarItem

调用removeTabBarItem，移除tabBar页面。

使用该接口请注意：

- removeTabBarItem 不可在非 tabBar 页面调用。
- removeTabBarItem 不可移除自身。
- removeTabBarItem 不可移除主 tab 页。

## 支持说明

| 应用能力 | Android | iOS | Harmony | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 7.0.0 | 6.0.0 | 6.0.0 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=11534) |

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

- `index`（number，必填）：要删除的 item 对应的位置，从 0 开始。

## **返回结果**

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性为空

## **示例****代码**

### 默认出入参

```
dd.removeTabBarItem({
  index: 0,
  success: () => {},
  fail: () => {},
  complete: () => {},
});
```
