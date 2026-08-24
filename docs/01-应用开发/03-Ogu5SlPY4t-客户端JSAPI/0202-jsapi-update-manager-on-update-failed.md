---
title: "UpdateManager.onUpdateFailed"
source_url: "https://open.dingtalk.com/document/development/jsapi-update-manager-on-update-failed"
namespace: "development"
slug: "jsapi-update-manager-on-update-failed"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 更新管理 > UpdateManager.onUpdateFailed"
doc_id: "Nir5akRR4t"
updated_at: "2025-08-27 18:08:16"
---

> Source: https://open.dingtalk.com/document/development/jsapi-update-manager-on-update-failed
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 更新管理 > UpdateManager.onUpdateFailed
> Updated: 2025-08-27 18:08:16

# UpdateManager.onUpdateFailed

监听小程序更新失败事件

小程序有新版本，客户端主动触发下载（无需开发者触发），下载失败（可能是网络原因等）后回调。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 6.0.0 | 6.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10026) |

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

继承[通用输出对象](https://open.dingtalk.com/document/direction/jsapi-standard-input-output-object)，扩展属性描述：

### 出参

（object）

## **示例****代码**

### 默认出入参

```
const updateManager = dd.getUpdateManager();

updateManager.onUpdateFailed((res) => {
  const {} = res;
});
```

返回对象示例：

```
{}
```
