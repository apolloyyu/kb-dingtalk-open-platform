---
title: "接入群聊酷应用"
source_url: "https://open.dingtalk.com/document/dingstart/configuration-group-chat-quick-entry"
namespace: "dingstart"
slug: "configuration-group-chat-quick-entry"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发群聊酷应用 > 群聊酷应用 > 接入群聊酷应用"
doc_id: "MIeD8Ouh51"
updated_at: "2025-09-03 15:56:17"
---

> Source: https://open.dingtalk.com/document/dingstart/configuration-group-chat-quick-entry
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发群聊酷应用 > 群聊酷应用 > 接入群聊酷应用
> Updated: 2025-09-03 15:56:17

# 接入群聊酷应用

如果你需要接入群聊酷应用，可依据本文档操作步骤进行接入。

## **前提条件**

需要完成[创建酷应用](https://open.dingtalk.com/document/dingstart/create-coolapp)流程。

## **操作步骤**

1. 在**基础信息**页面，配置**群聊酷应用信息**。

   | **配置项** | **必填** | **说明** |
   | --- | --- | --- |
   | 图标 | 是 | 酷应用图标，尺寸：240\*240px，格式：PNG。默认使用主应用图标。 |
   | 名称 | 是 | 酷应用名称信息。 |
   | 描述 | 是 | 简要描述酷应用功能。 |
2. 单击**功能设计**，配置**群聊酷应用组件**内容。

   1. 单击**基础组件** > **群快捷入口**，配置快捷入口信息。

      | **配置项** | **必填** | **说明** |
      | --- | --- | --- |
      | 图标 | 是 | 快捷入口图标设置，尺寸：48\*48px，格式：PNG。默认为应用图标。 |
      | 名称 | 是 | 群聊酷应用入口的名称，第三方企业应用填写时不能超过6个字符。 |
      | 桌面端访问地址 | 是 | - 企业内部应用：PC 客户端单击快捷入口，打开的桌面端访问地址。  **[!NOTE]**  钉钉 PC 端固定为侧边栏打开。 - 第三方企业应用：需要输入`https://`或`dingtalk://`协议地址，如`https://open.dingtalk.com/developer`。  **[!NOTE]**  dingtalk 协议参考[群相关跳转协议](0057-group-jump-protocol.md)，服务商也可以在 url 获取群 id 信息。 |
      | 移动端访问地址 | 是 | 移动客户端单击快捷入口，打开的移动端访问地址。  **[!NOTE]**  钉钉移动端固定为半浮层打开。 |

      检查各配置项是否正确，检查完成后，单击右上角**保存**按钮。

      > **[!NOTE]**
      >
      > 企业内部应用配置链接时支持通过配置特定的**地址动参**来实现打开链接时通过参数获取群openConversationId等参数，详情参考：[设置快捷入口（群插件）URL](../02-4a8AMF6u2A-服务端-API/0732-create-a-swarm-plug-in-1.md)
3. 企业内部在**预览发布**页面，单击**预览效果，**测试体验群聊酷应用**。**

   > **[!NOTE]**
   >
   > 第三方企业应用需要在**创建群应用**页面，检查各配置项是否正确，检查完成后，单击右上角**提交审核**。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9980127661/p510103.png)
4. 企业内部应用体验酷应用完成后，单击发布群聊酷应用。

## **后续步骤**

- **企业内部应用**

  群聊酷应用发布完成后，需要进行[发布应用](0017-publish-dingtalk-application.md)。

  > **[!NOTE]**
  >
  > 如果你需要接入群聊酷应用其他功能，可根据下方进行选择：
  >
  > - [接入机器人能力](0045-group-chat-coolapp-access-robot-app.md)
  > - [管理酷应用](0048-manage-group-chat-coolapp.md)
  > - [互动卡片](0055-group-chat-coolapp-interactive-card.md)
  > - [吊顶卡片](0056-permanent-type-suspended-ceiling.md)
  > - [感知群变化（事件订阅）](0058-group-chat-coolapp-event.md)
- **第三方企业应用**

  群聊酷应用提交审核后，如果你需要上架群聊酷应用到酷应用市场，请参考[上架群聊酷应用（ISV应用）](0047-grounding-group-chat-coolapp.md)。

  > **[!NOTE]**
  >
  > 如果你需要接入群聊酷应用其他功能，可根据下方进行选择：
  >
  > - [接入机器人能力](0045-group-chat-coolapp-access-robot-app.md)
  > - [开发互动卡片](0046-develop-group-chat-coolapp-interactive-card.md)
