---
title: "监听文档是否保存"
source_url: "https://open.dingtalk.com/document/development/whether-the-saved"
namespace: "development"
slug: "whether-the-saved"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "酷应用 > 文档酷应用 > 监听文档状态 > 监听文档是否保存"
doc_id: "9d5re3R0eV"
updated_at: "2025-08-27 18:09:28"
---

> Source: https://open.dingtalk.com/document/development/whether-the-saved
> Path: 应用开发 / 客户端 JSAPI / 酷应用 > 文档酷应用 > 监听文档状态 > 监听文档是否保存
> Updated: 2025-08-27 18:09:28

# 监听文档是否保存

本文通过调用**Dingdocs.workbook.event.onSaveStateChanged**监听当前文档是否已保存。

## **准备工作**

初始化脚本服务JSAPI需依赖[dingtalk-docs-cool-app](https://www.npmjs.com/package/dingtalk-docs-cool-app)，请先升级到最新版本。

```
npm install dingtalk-docs-cool-app --save
```

## **API使用说明**

> **[!NOTE]**
>
> 建议钉钉版本使用最新版本。

| **客户端** | **Android** | **IOS** | **PC** |
| --- | --- | --- | --- |
| 支持说明 | 不支持 | 不支持 | 支持 |

调用**Dingdocs.workbook.event.onSaveStateChanged**监听当前文档是否已保存。

```
offSaveStateChanged = Dingdocs.workbook.event.onSaveStateChanged(({ isSaved }) => {
  console.log('SaveStateChanged', isSaved);
})
// 注销监听
offSaveStateChanged();
```

## **参数说明**

| **参数** | **类型** | **是否必填** | **说明** |
| --- | --- | --- | --- |
| handler | Function | 是 | 监听文文档保存状态后的回调：   - isSaved：当前文档是否已保存。 |
