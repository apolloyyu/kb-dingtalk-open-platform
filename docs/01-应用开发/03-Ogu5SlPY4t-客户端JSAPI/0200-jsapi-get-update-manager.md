---
title: "getUpdateManager"
source_url: "https://open.dingtalk.com/document/development/jsapi-get-update-manager"
namespace: "development"
slug: "jsapi-get-update-manager"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 更新管理 > getUpdateManager"
doc_id: "rSg6OywsBo"
updated_at: "2025-08-27 18:08:15"
---

> Source: https://open.dingtalk.com/document/development/jsapi-get-update-manager
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 更新管理 > getUpdateManager
> Updated: 2025-08-27 18:08:15

# getUpdateManager

使用UpdateManager对象，用来管理小程序更新。

### 创建UpdateManager对象

调用dd.getUpdateManager创建一个UpdateManager对象，获取全局唯一的版本更新管理器，用于管理小程序更新。

### 方法

|  | 方法 | 说明 |
| --- | --- | --- |
| 强制小程序重启并使用新版本 | UpdateManager.applyUpdate() | 当小程序新版本下载完成后（即收到 onUpdateReady 回调），强制小程序重启并使用新版本。 |
| 监听向钉钉后台请求检查更新结果事件 | UpdateManager.onCheckForUpdate(function callback) | 监听向钉钉后台请求检查更新结果事件。钉钉在小程序冷启动时自动检查更新，不需由开发者主动触发。 |
| 监听小程序有版本更新事件 | UpdateManager.onUpdateReady(function callback) | 监听小程序有版本更新事件。客户端主动触发下载（无需开发者触发），下载成功后回调。 |
| 监听小程序更新失败事件 | UpdateManager.onUpdateFailed(function callback) | 小程序有新版本，客户端主动触发下载（无需开发者触发），下载失败（可能是网络原因等）后回调。 |

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10022) |

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
dd.getUpdateManager();
```
