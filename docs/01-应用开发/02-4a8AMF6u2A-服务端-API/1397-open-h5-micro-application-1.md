---
title: "打开H5微应用"
source_url: "https://open.dingtalk.com/document/development/open-h5-micro-application-1"
namespace: "development"
slug: "open-h5-micro-application-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 打开H5微应用"
doc_id: "UG8jBu5dd7"
updated_at: "2026-07-21 09:26:22"
---

> Source: https://open.dingtalk.com/document/development/open-h5-micro-application-1
> Path: 应用开发 / 服务端 API / 更多开放 > AppLink协议 > 已支持的协议 > 打开H5微应用
> Updated: 2026-07-21 09:26:22

# 打开H5微应用

本文档介绍通过 AppLink 协议在钉钉客户端中打开 H5 微应用的相关说明，包括支持的参数、使用场景及注意事项。

## **使用场景**

通过 AppLink 协议，可在钉钉内安全、定向地打开指定企业的 H5 微应用或其内部具体页面。典型使用场景包括：

- 从外部系统跳转至钉钉内的业务微应用；
- 在群机器人消息卡片中点击按钮打开对应功能页；
- 第三方服务通知推送后，点击进入处理页面；
- 多端统一入口唤起 H5 应用，并根据设备类型适配不同容器展示方式。

> **[!NOTE]**
>
> 需确保目标用户已在该 H5 微应用的可见范围内，否则将无法正常打开。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥7.0.5 | ≥7.0.5 | ≥7.0.40 | ≥7.0.40 |

## **协议**

```
https://applink.dingtalk.com/page/h5_app_open
```

此为标准 AppLink 协议地址，所有参数以 Query String 形式附加于其后。

## **字段说明**

| **资源名+path定义** | **字段** | **必填** | **说明** |
| --- | --- | --- | --- |
| page/h5\_app\_open | appId | 是 | H5应用标识。   - 如果是企业内部H5微应用，该参数传agentId，参考[基础概念-agentId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#ef841f7f37kba)。 - 如果是第三方企业H5微应用，该参数传appId，参考[基础概念-appId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#c0e465e9857uj)。 |
| appType | 是 | 应用类型：   - **1**：第三方企业应用 - **2**：企业内部应用 |
| corpId | 是 | 应用所在组织的corpId。 |
| path | 否 | 访问H5微应用的具体某个页面时，该字段的参数将替换H5应用URL的path部分，需要encode处理。 |
| pathAndroid | 否 | 同path参数，Android端会优先使用该参数替换H5微应用URL的path部分，需要encode处理。如果该参数不存在，则会使用path参数。 |
| pathIos | 否 | 同path参数，iOS端会优先使用该参数替换H5微应用URL的path部分，需要encode处理。如果该参数不存在，则会使用path参数。 |
| pathPc | 否 | 同path参数，桌面端会优先使用该参数替换H5微应用URL的path部分，需要encode处理。如果该参数不存在，则会使用path参数。 |
| target | 否 | 打开的容器类型：   - 移动端：    - **fullScreen**（默认**）**：全屏容器打开   - **panel**：[沉浸式容器](1427-immersive-container-1.md)打开 - 桌面端：    - **workbench（默认）**：桌面端工作台打开   - **popupWindow**：独立窗口打开   - **panel**：第四栏打开   - **slide**：侧边栏打开 |
| targetDesktop | 否 | 打开的容器类型（桌面端）：   - **workbench（默认）**：桌面端工作台打开 - **popupWindow**：独立窗口打开 - **panel**：第四栏打开 - **slide**：侧边栏打开   **[!NOTE]**   - targetDestop参数仅针对桌面端有效。 - 在链接中同时指定 targetDesktop 和 target 参数，桌面端会优先使用 targetDesktop 参数。 |
| fallbackLink | 否 | 端上能识别appLink协议的情况下，如果触发异常（包括：appId为空、获取页面url失败、appType类型错误的情况），需要跳转的路径。 |

## 使用示例

- 使用**全屏容器**打开 H5 微应用

  ```
  https://applink.dingtalk.com/page/h5_app_open?appId=1234&corpId=ding16b241fd****4f7c288&appType=2
  ```
- 使用**沉浸式容器**打开 H5 微应用

  ```
  https://applink.dingtalk.com/page/h5_app_open?appId=1234&corpId=ding16b241fd****4f7c288&appType=2&target=panel
  ```
- 打开 H5 微应用，并将 path 替换为`/a/index`

  > 路径参数需进行 URL 编码，例如 `/a/index` 应编码为 `%2Fa%2Findex`。

  ```
  https://applink.dingtalk.com/page/h5_app_open?appId=1234&corpId=ding16b241fd****4f7c288&appType=2&path=%2Fa%2Findex
  ```
