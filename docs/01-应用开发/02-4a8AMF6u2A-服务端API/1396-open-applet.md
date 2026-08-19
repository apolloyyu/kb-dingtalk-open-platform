---
title: "打开小程序"
source_url: "https://open.dingtalk.com/document/development/open-applet"
namespace: "development"
slug: "open-applet"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开小程序"
doc_id: "xJ5Eye8mzH"
updated_at: "2026-07-21 09:26:21"
---

> Source: https://open.dingtalk.com/document/development/open-applet
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 打开小程序
> Updated: 2026-07-21 09:26:21

# 打开小程序

本文档介绍使用AppLink协议打开钉钉小程序的相关说明。

## **使用场景**

打开小程序或小程序中目标页面。

## **版本支持**

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥7.0.40 | ≥7.0.40 |

## **协议**

```
https://applink.dingtalk.com/action/open_mini_app
```

> **[!NOTE]**
>
> 如果要在PC端使用该协议打开钉钉小程序，在小程序发布时，必须选择**支持移动端与PC端**。否则PC端使用该协议打开的页面会是白屏。![iShot2023-01-04 16](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7640282761/p543041.png)

## **字段说明**

| **资源名+path定义** | **字段** | **必填** | **说明** |
| --- | --- | --- | --- |
| action/open\_mini\_app | miniAppId | 是 | 小程序miniAppId，可参考[基础概念-miniAppId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ebd9434a92c8s)。 |
| appId | 否 | 小程序appId。  **[!IMPORTANT]**  第三方企业小程序，该参数必传，可参考[基础概念-appId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#c0e465e9857uj)。 |
| type | 是 | 小程序类型。   - **1**：三方企业应用 - **2**：企业内部应用 - **4**：第三方个人应用 |
| page | 否 | 访问小程序应用的具体某个页面的路径，不设置则打开首页，需要encode处理。  例如：`%2Fpages%2Fmain%2Fmain`。 |
| target | 否 | 打开的容器类型：   - 移动端：    - **fullScreen**（默认）：全屏容器打开   - **panel**：沉浸式容器打开  **[!NOTE]**  什么是沉浸式容器，请参考[沉浸式容器](1427-immersive-container-1.md)。 - 桌面端：    - **slide**（默认），侧边栏打开   - **panel**：第四栏打开   - **popupWindow**：独立弹窗打开 |
| targetDesktop | 否 | 打开容器类型（桌面端）：   - **slide**（默认），侧边栏打开 - **panel**：第四栏打开 - **popupWindow**：独立弹窗打开   **[!NOTE]**   - targetDestop 参数仅针对桌面端有效， - 在链接中同时指定 targetDesktop 和 target 参数，桌面端会优先使用 targetDesktop 参数。 |
| mobileHeight | 否 | 沉浸式容器的高度。   - semi：百分之50屏幕高度。   **[!NOTE]**  该字段不填，则默认为百分之83的屏幕高度。 |
| corpId | 否 | 组织corpId。  **[!NOTE]**  如果是企业内部小程序，该字段必填。 |
| agentId | 否 | 小程序应用的agentId，可参考[基础概念-agentId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ef841f7f37kba)。  **[!NOTE]**  如果是企业内部小程序，该字段必填。 |
| pVersion | 否 | 企业内部小程序应用必填，固定值为1。 |
| packageType | 否 | 企业内部小程序应用必填，固定值为1。 |

## **使用示例**

- 使用**全屏容器**打开小程序

  ```
  https://applink.dingtalk.com/action/open_mini_app?type=2&miniAppId=xxxxx&corpId=xxxxx&agentId=xxxxx&pVersion=1&packageType=1
  ```
- 使用**沉浸式容器**打开小程序

  ```
  https://applink.dingtalk.com/action/open_mini_app?type=2&miniAppId=xxxxx&corpId=xxxxx&agentId=xxxxx&pVersion=1&packageType=1&target=panel
  ```
- 打开小程序中目标页面page/component/index

  ```
  https://applink.dingtalk.com/action/open_mini_app?type=2&miniAppId=xxxxx&corpId=xxxxx&agentId=xxxxx&pVersion=1&packageType=1&page=page%2Fcomponent%2Findex
  ```
