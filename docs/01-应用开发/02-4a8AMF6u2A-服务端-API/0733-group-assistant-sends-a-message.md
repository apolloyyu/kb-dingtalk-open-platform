---
title: "群助手发送消息"
source_url: "https://open.dingtalk.com/document/development/group-assistant-sends-a-message"
namespace: "development"
slug: "group-assistant-sends-a-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 使用教程 > 群助手发送消息"
doc_id: "ItyRrLUMsj"
updated_at: "2026-07-14 09:21:59"
---

> Source: https://open.dingtalk.com/document/development/group-assistant-sends-a-message
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 使用教程 > 群助手发送消息
> Updated: 2026-07-14 09:21:59

# 群助手发送消息

本示例介绍了如何发送群助手消息。

![群助手消息](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9922390461/p377888.png)

本文档展示了，创建一个企业内部应用，使用**场景群**提供的API，实现群助手发送消息流程：

1. 选择目标应用，进入应用详情页，单击基础信息 > 凭证与基础信息。
2. 获取应用 Client ID 和 Client Secret。
3. 申请发送群助手消息接口权限。
4. 获取应用访问凭证，[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。
5. 在开发者后台-场景群页面，申请[机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)，审核通过后获取机器人id参数**robotCode**。
6. 在开发者后台-场景群页面，创建[群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，获取群模板id参数**template\_id**。
7. 绑定[场景群-机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)到[场景群-群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，保存编辑，返回群场景列表。
8. 进入对应群模板，提交审核，点击发布。
9. 依据**template\_id**调用[创建场景群](0746-create-a-scene-group.md)接口，获取`open_conversation_id`。
10. 调用[发送群助手消息](0763-group-template-robot-message.md)接口，实现机器人群消息的发送。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **操作步骤**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。
3. 单击**开发配置** > **权限管理**，在权限搜索框中输入`qyapi_chat_manage`，并申请权限。
4. 获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。
5. 在开发者后台-场景群页面，申请[机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p1086792.png)
6. 获取机器人ID参数，即**robotCode**。

   > **[!NOTE]**
   >
   > 申请机器人需要审核，审批通过后可以查看ID，如下图所示。

   ![创建机器人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p355281.png)
7. 在开发者后台-场景群页面，创建[群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，获取群模板id参数**template\_id**。

   ![创建群模板1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p355273.png)
8. 绑定[场景群-机器人](https://open-dev.dingtalk.com/fe/im#/robot/list)到[场景群-群模板](https://open-dev.dingtalk.com/fe/im#/group/list)，保存编辑，返回群场景列表。

   ![保存群模板](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9112993871/p379280.png)
9. 进入对应群模板，进行提交审核，点击发布。

   > **[!NOTE]**
   >
   > 审核自动通过，无需审批。

   ![发布流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2473821461/p379282.png)
10. 通过**template\_id**调用[创建场景群](0746-create-a-scene-group.md)接口，获取`open_conversation_id`。
11. 调用[发送群助手消息](0763-group-template-robot-message.md)接口，实现机器人群消息的发送。
