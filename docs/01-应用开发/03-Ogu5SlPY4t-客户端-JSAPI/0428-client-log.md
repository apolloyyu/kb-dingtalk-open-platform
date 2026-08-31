---
title: "更新日志"
source_url: "https://open.dingtalk.com/document/development/client-log"
namespace: "development"
slug: "client-log"
group: "应用开发"
tab: "客户端 JSAPI"
breadcrumb: "更新日志"
doc_id: "tiW4sWdL7b"
updated_at: "2026-08-14 17:07:56"
---

> Source: https://open.dingtalk.com/document/development/client-log
> Path: 应用开发 / 客户端 JSAPI / 更新日志
> Updated: 2026-08-14 17:07:56

# 更新日志

钉钉开放平台客户端 API 更新日志，记录了新增开放的客户端 API、API 升级、目录结构调整及名称变更等内容。本文档旨在帮助开发者全面了解钉钉 JSAPI 的演进历程，提升开发效率与集成体验。

> **[!NOTE]**
>
> **2023年8月**起，客户端 JSAPI 统一升级为一段式调用。新版兼容旧版，小程序与 H5 微应用均使用同一套接口，无需适配差异，如需迁移请参见[版本对比与迁移](0004-comparison-client-apis.md)文档介绍。

## **2026年01月**

| **类目** | **说明** | **应用类型** |
| --- | --- | --- |
| **DingTalk A1** | **新增开放**：   - 新增[getDingerDeviceStatus](0427-jsapi-get-dinger-device-status.md)JSAPI，查询 DingTalk A1 设备状态。 | - 企业内部应用 - 第三方企业应用 - 第三方个人应用 |

## **2026年01月**

| **类目** | **说明** | **应用类型** |
| --- | --- | --- |
| **DingTalk A1** | **新增开放**：   - 新增[startDingerRecord](0425-jsapi-start-dinger-record.md)JSAPI，DingTalk A1 发起录音。 - 新增[stopDingerRecord](0426-jsapi-stop-dinger-record.md)JSAPI，DingTalk A1 发起录音。 | - 企业内部应用 - 第三方企业应用 - 第三方个人应用 |

## **2025年10月**

| **类目** | **说明** | **应用类型** |
| --- | --- | --- |
| **多媒体** | **新增开放**：   - 新增[chooseMedia](0213-jsapi-choose-media.md)JSAPI，拍摄或从手机相册中选择图片或视频。 | - 企业内部应用 - 第三方企业应用 - 第三方个人应用 |
| **设备** | **新增开放**：   - 新增[removeCachedAPIResponse](0419-jsapi-remove-cached-a-p-i-response.md)JSAPI，清除当前页面上已缓存的 JSAPI 返回值。 - 新增[getCachedAPIResponse](0420-jsapi-get-cached-a-p-i-response.md)JSAPI，获取已缓存的JSAPI返回值。 - 新增[enableAPIResponseCache](0421-jsapi-enable-a-p-i-response-cache.md)JSAPI，开启JSAPI返回值缓存。 - 新增[getPageTerminateInfo](0422-jsapi-get-page-terminate-info.md)JSAPI，获取WebView崩溃信息。 | - 企业内部应用 - 第三方企业应用 - 第三方个人应用 |
