---
title: "UpdateManager.onCheckForUpdate"
source_url: "https://open.dingtalk.com/document/development/jsapi-update-manager-on-check-for-update"
namespace: "development"
slug: "jsapi-update-manager-on-check-for-update"
group: "应用开发"
tab: "客户端JSAPI"
breadcrumb: "基础交互 > 更新管理 > UpdateManager.onCheckForUpdate"
doc_id: "osYpV6mnWZ"
updated_at: "2025-08-27 18:08:17"
---

> Source: https://open.dingtalk.com/document/development/jsapi-update-manager-on-check-for-update
> Path: 应用开发 / 客户端JSAPI / 基础交互 > 更新管理 > UpdateManager.onCheckForUpdate
> Updated: 2025-08-27 18:08:17

# UpdateManager.onCheckForUpdate

监听向钉钉后台请求检查更新结果事件

钉钉在小程序冷启动时自动检查更新，不需由开发者主动触发。

## 支持说明

| 应用能力 | Android | iOS | Mac | Windows | 预览效果 |
| --- | --- | --- | --- | --- | --- |
| 网页应用（原H5微应用） | 不支持 | 不支持 | 不支持 | 不支持 | - |
| 小程序 | 5.0.0 | 5.0.0 | 不支持 | 不支持 | [去预览](https://open.dingtalk.com/tools/explorer/jsapi?id=10024) |

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

- `hasUpdate`（boolean，必填）：是否有更新

## **示例****代码**

### 默认出入参

```
const updateManager = dd.getUpdateManager();

updateManager.onCheckForUpdate({
  success: (res) => {
    const { hasUpdate } = res;
  },
  fail: () => {},
  complete: () => {},
});
```

`success`返回对象示例：

```
{ "hasUpdate": true }
```
