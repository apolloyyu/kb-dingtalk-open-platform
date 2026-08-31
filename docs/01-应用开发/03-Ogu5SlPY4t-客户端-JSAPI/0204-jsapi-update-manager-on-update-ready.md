---
title: "UpdateManager.onUpdateReady"
source_url: "https://open.dingtalk.com/document/development/jsapi-update-manager-on-update-ready"
namespace: "development"
slug: "jsapi-update-manager-on-update-ready"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "基础交互 > 更新管理 > UpdateManager.onUpdateReady"
doc_id: "uyTVoKXxQK"
updated_at: "2025-08-27 18:08:17"
---

> Source: https://open.dingtalk.com/document/development/jsapi-update-manager-on-update-ready
> Path: 应用开发 / 客户端 JSAPI / 基础交互 > 更新管理 > UpdateManager.onUpdateReady
> Updated: 2025-08-27 18:08:17

# UpdateManager.onUpdateReady

监听小程序有版本更新事件

客户端主动触发下载（无需开发者触发），下载成功后回调。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 不支持 | 不支持 | 不支持 | 不支持 | - |

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

- `version`（string，必填）：版本号

## **示例****代码**

### 默认出入参

```
const updateManager = dd.getUpdateManager();

updateManager.onUpdateReady((res) => {
  const { version } = res;
});
```

返回对象示例：

```
{ "version": "1.0.0" }
```
