---
title: "客户端Tab切换"
source_url: "https://open.dingtalk.com/document/development/client-tab-switching"
namespace: "development"
slug: "client-tab-switching"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > AppLink协议 > 已支持的协议 > 客户端Tab切换"
doc_id: "Frsn2chn7v"
updated_at: "2026-01-22 20:17:47"
---

> Source: https://open.dingtalk.com/document/development/client-tab-switching
> Path: 应用开发 / 服务端API / 更多开放 > AppLink协议 > 已支持的协议 > 客户端Tab切换
> Updated: 2026-01-22 20:17:47

# 客户端Tab切换

本文档介绍如何通过 AppLink 协议实现钉钉客户端Tab 页面的切换，适用于移动端应用集成场景。该功能可用于引导用户快速跳转至指定功能模块（如消息、Ding、工作台），提升用户体验和操作效率。

## **使用场景**

通过 AppLink 链接，可在外部 H5 页面、小程序或其他集成环境中，一键唤起钉钉客户端并自动切换到指定 Tab，常见场景包括：

- 用户点击通知后直接进入“Ding”消息列表；
- 从企业门户跳转至钉钉“工作台”，加载该企业的专属应用；
- 在引导流程中控制客户端界面导航，提升交互连贯性。

快速体验请查看以下链接：

<https://applink.dingtalk.com/action/switchtab?index=1&name=Ding>。

## 版本支持

| **钉钉客户端** | **Android** | **iOS** | **macOS** | **Windows** |
| --- | --- | --- | --- | --- |
| 版本 | ≥6.5.45 | ≥6.5.45 | ≥6.5.50 | ≥6.5.50 |

## **协议**

该 URL 使用钉钉标准 AppLink 协议格式，通过 Query 参数传递指令，由客户端解析并执行 Tab 切换动作。

```
https://applink.dingtalk.com/action/switchtab
```

## **字段说明**

| **资源名+path定义** | **参数** | **必填** | **说明** |
| --- | --- | --- | --- |
| action/switchtab | index | 是 | 目标 Tab 的索引值：   - **0**：消息 - **1**：Ding - **2**：工作台 |
| name | 是 | 目标 Tab 的名称标识：   - **im**：消息 - **ding**：Ding - **work**：工作台 |
| corpid |  | 当切换到工作台Tab时，需要展示企业的corpId。  **[!NOTE]**  仅在移动端生效。 |
| reload |  | 是否重新刷新。   - **true**：刷新 - **false**：不刷新   **[!NOTE]**  如果为true并且工作tab上为H5页面，则重新reload当前页面。 |

## **使用示例**

- 打开钉钉客户端的消息 Tab，并强制刷新页面：

  ```
  https://applink.dingtalk.com/action/switchtab?index=0&name=im&reload=true
  ```
- 打开钉钉客户端的 Ding 消息 Tab，并强制刷新页面：

  ```
  https://applink.dingtalk.com/action/switchtab?index=1&name=ding&reload=true
  ```
- 打开钉钉客户端的 工作台 Tab，并加载指定企业（corpid=abc123）的内容，不刷新页面：

  ```
  https://applink.dingtalk.com/action/switchtab?index=2&name=工作台&corpid=abc123&reload=false
  ```

**注意事项**

- **参数一致性**：建议`index`与`name`成对设置，避免因版本差异导致映射错乱。
- **corpid 为空时的行为**：若未传入`corpid`且目标为“工作台”，客户端将默认展示当前登录用户的主企业工作台。

## **常见问题**

- **Q：为什么设置了**`corpid`**但没有生效？**

  A：请确认当前设备为移动端（Android/iOS），且用户已在对应企业内。桌面端目前不支持该参数。
- **Q：**`reload=true`**为什么没有刷新页面？**

  A：该参数仅对 H5 页面生效。如果目标是原生功能页（如消息、Ding），客户端不会执行刷新操作。
- **Q：能否通过该协议打开自定义 Tab？**

  A：不可以。AppLink 只支持切换钉钉客户端标准 Tab（消息、Ding、工作台），不支持跳转至企业自定义 Tab 或其他插件页面。
- **Q：如何调试 AppLink 链接是否生效？**

  A：可在手机浏览器中直接访问构造好的链接，观察是否成功唤起钉钉并完成跳转。
