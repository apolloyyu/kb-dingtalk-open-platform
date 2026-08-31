---
title: "UpdateManager.applyUpdate"
source_url: "https://open.dingtalk.com/document/development/jsapi-update-manager-apply-update"
namespace: "development"
slug: "jsapi-update-manager-apply-update"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 更新管理 > UpdateManager.applyUpdate"
doc_id: "XMr9zLPWHG"
updated_at: "2025-08-27 18:08:15"
---

> Source: https://open.dingtalk.com/document/development/jsapi-update-manager-apply-update
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 更新管理 > UpdateManager.applyUpdate
> Updated: 2025-08-27 18:08:15

# UpdateManager.applyUpdate

强制小程序重启并使用新版本

当小程序新版本下载完成后（即收到 onUpdateReady 回调），强制小程序重启并使用新版本。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10023) |

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
const updateManager = dd.getUpdateManager();

updateManager.applyUpdate({});
```
