---
title: "存量群升级为场景群"
source_url: "https://open.dingtalk.com/document/development/step-3-create-a-scene-group"
namespace: "development"
slug: "step-3-create-a-scene-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 存量群升级为场景群"
doc_id: "Y6UtvNnjBw"
updated_at: "2026-07-14 09:21:58"
---

> Source: https://open.dingtalk.com/document/development/step-3-create-a-scene-group
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 存量群升级为场景群
> Updated: 2026-07-14 09:21:58

# 存量群升级为场景群

如果你需要将存量群升级为场景群，可以参考本文档操作步骤。

## **前提条件**

完成[创建群聊会话（场景群）](0734-create-a-group-chat-session.md)的流程。

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)，单击顶部导航栏**开放能力** > **场景群。**选择侧边导航栏**群模板。**
2. 选择目标群模板，单击目标群模板右下角**灰度，**填写[企业CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)。
3. 存量群升级场景群：

   - 调用[启用群模板](0759-enable-a-group-template.md)接口，你可以将存量群升级为场景群。
   - 你可以登录钉钉客户端：

     1. 找到目标群会话，单击右上角群设置标识。
     2. 单击**群管理** > **快捷栏管理** > **管理酷应用**，进入酷应用页面。
     3. 单击最下方**群模板设置**，选择上述目标群模板开启即可。

        ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1820719071/p771006.png)

> 如果你需要通过接口直接创建场景群，请参考[创建场景群](0746-create-a-scene-group.md)接口。
