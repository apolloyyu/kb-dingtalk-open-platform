---
title: "接入单聊酷应用"
source_url: "https://open.dingtalk.com/document/dingstart/configuration-private-chat-quick-entry"
namespace: "dingstart"
slug: "configuration-private-chat-quick-entry"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发酷应用 > 开发单聊酷应用 > 接入单聊酷应用"
doc_id: "oBsF6IJ2SU"
updated_at: "2026-01-29 14:52:02"
---

> Source: https://open.dingtalk.com/document/dingstart/configuration-private-chat-quick-entry
> Path: 应用开发 / 开发指南 / 开发酷应用 > 开发单聊酷应用 > 接入单聊酷应用
> Updated: 2026-01-29 14:52:02

# 接入单聊酷应用

如果你需要在钉钉中使用单聊酷应用，可通过本文档完成从配置到发布的完整接入流程。

## **前提条件**

- 企业已完成认证。
- 已完成[创建酷应用](https://open.dingtalk.com/document/dingstart/create-coolapp)流程。
- 确保已获取有效的`AppKey`和`AppSecret`，用于后续接口调用鉴权。

## **操作步骤**

1. 在**基础信息**页面，配置**单聊酷应用信息**。

   | **配置项** | **是否必填** | **说明** |
   | --- | --- | --- |
   | 图标 | 是 | 酷应用图标，尺寸：240\*240px，格式：PNG。默认使用主应用图标。 |
   | 名称 | 是 | 酷应用名称信息。 |
   | 描述 | 是 | 简要描述酷应用功能。 |
2. 配置**单聊酷应用入口**。

   | **配置项** | **是否必填** | **说明** |
   | --- | --- | --- |
   | 名称 | 是 | 单聊应用入口的名称。名称长度不超过6个字。 |
   | 桌面端访问地址 | 是 | 桌面端访问地址：  - 填写说明：请输入https://或dingtalk://协议地址。 - 填写示例：如`https://open.dingtalk.com/developer`。 **[!NOTE]**  dingtalk协议参见[单聊相关跳转协议](0064-private-chat-related-jump-protocol.md)。 |
   | 移动端访问地址 | 是 | 移动端访问地址：  - 填写说明：请输入https://或dingtalk://协议地址。 - 填写示例：如`https://open.dingtalk.com/developer`。 **[!NOTE]**  dingtalk协议参见[单聊相关跳转协议](0064-private-chat-related-jump-protocol.md)。 |

   > **[!NOTE]**
   >
   > 配置链接时支持通过配置特定的**地址动参**来实现打开链接时通过参数获取群openConversationId等参数，详情参考：[设置快捷入口（群插件）URL](../02-4a8AMF6u2A-服务端API/0732-create-a-swarm-plug-in-1.md)
3. 完成所有配置项后，请仔细核对内容准确性。
4. 单击页面左下角的 **保存** 按钮，保存当前配置。
5. 保存成功后，在单聊应用信息页面右上角点击 **提交发布**，完成发布操作。

## **后续步骤**

单聊酷应用发布完成后，还需执行[发布应用](0017-publish-dingtalk-application.md)操作，将应用推送到目标组织范围内，确保用户可见可用。

**相关功能扩展**：

如需进一步增强单聊酷应用能力，可参考以下文档继续开发：

- [接入机器人能力](0045-group-chat-coolapp-access-robot-app.md)：为应用添加消息收发、自动回复等机器人功能。
- [开发互动卡片](0063-private-chat-coolapp-develop-interactive-cards.md)：提升交互体验，支持按钮点击、表单提交等富交互操作。
- [批量安装酷应用到单聊会话](../03-Ogu5SlPY4t-客户端JSAPI/0277-batch-chat-session.md)：实现自动化部署，快速覆盖多个会话场景。
