---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/im-session-overview"
namespace: "development"
slug: "im-session-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 概述"
doc_id: "8s8KVFzInb"
updated_at: "2026-05-15 18:20:35"
---

> Source: https://open.dingtalk.com/document/development/im-session-overview
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 概述
> Updated: 2026-05-15 18:20:35

# 概述

本文介绍了会话管理的相关内容介绍。

## **什么是会话管理**

会话管理是钉钉通过开放多样的方式根据业务的需要创建、设置和管理群以及群内的成员，还可以为用户提供基于具体业务场景下的群内服务，将沟通和协同融合起来，让组织成员在群聊中通过丰富的群能力实现高效的、结构化的、明确的协作和沟通，提高协同办公效率。

![会话管理能力 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5486523761/p548650.gif)

## **版本说明**

钉钉会话管理分为「群管理」和「场景群」两代版本，两个版本均可以实现群聊会话的基本管理功能，但是场景群对群聊会话在组织协同方面做了更多功能扩充：

| **功能说明** | **群管理** | **场景群** |
| --- | --- | --- |
| 群聊会话及成员的基本管理 | ✅ | ✅ |
| 实现群聊会话中高级功能的预置（如群吊顶、群快捷入口、群机器人等） | ❌ | ✅ |
| 根据群模板实现API批量管理群聊会话的功能 | ❌ | ✅ |
| 根据群模板自定义组织内的群类型及其功能 | ❌ | ✅ |

存量群升级为场景群

## **开放概览**

### **开放接口列表**

会话管理提供了丰富的接口开放能力，开发者通过API接口可以实现群和企业业务系统打通。

#### **群管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建群会话](0738-create-common-group-new-version-v2.md) | 创建内部群跟普通群会话。 | 新版 |
| [更新群会话](0739-api-updategroup.md) | 通过群chatid更新指定群会话的基本信息及成员。 | 新版 |
| [查询群信息](0740-obtain-a-group-session.md) | 获取群设置和成员信息。 | 旧版 |
| [更新群成员的群昵称](0741-set-a-group-nickname.md) | 更新群成员在群中的昵称。 | 旧版 |
| [批量设置企业群管理员](0742-batch-setup-group-administrator.md) | 批量设置企业群内用户为管理员身份或批量取消企业群内用户的管理员身份。 | 新版 |
| [设置禁止群成员私聊](0743-set-private-chat.md) | 设置群成员之间是否可以添加好友和私聊。 | 旧版 |
| [获取入群二维码链接](0744-obtain-a-qr-code-link.md) | 获取群入群二维码邀请链接。 | 旧版 |
| [获取群会话的OpenConversationId](0745-obtain-group-openconversationid.md) | 通过chatId查询OpenConversationId。 | 新版 |

#### **场景群**

##### **群管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建场景群](0746-create-a-scene-group.md) | 根据群模板ID创建群。 | 新版 |
| [更新场景群](0747-api-updatescenegroup.md) | 根据群ID更新群信息。 | 新版 |
| [添加群成员](0749-api-addscenegroupmember.md) | 向群内新增群成员（群成员人数上限1000）。 | 新版 |
| [删除群成员](0750-api-removescenegroupmember.md) | 根据群ID和群成员ID删除群成员。 | 新版 |
| [查询群信息](0755-queries-the-basic-information-of-a-scenario-group.md) | 根据群ID获取群名称、群图标、群主id、入群链接、群设置项等信息。 | 旧版 |
| [设置群成员禁言状态](0756-set-group-members-access-control.md) | 设置场景群内的群成员禁言状态。 | 新版 |
| [查询群禁言状态](0753-query-group-silence-status.md) | 查询群和群内成员的禁言状态。 | 新版 |
| [更新群成员的群昵称](0757-update-group-nicknames.md) | 根据群ID和群成员ID，更新群成员的群昵称。 | 新版 |
| [更新群管理员](0752-update-group-administrators.md) | 更新群的群管理员。 | 新版 |
| [查询群简要信息](0754-query-group-information.md) | 根据群ID查询群名称、群图标、群主id等基本信息。 | 新版 |
| [查询群成员](0751-query-group-members.md) | 查询群成员信息。 | 新版 |
| [解散群聊](0748-api-dsbandopenscenegroup.md) | 根据群ID解散指定群。 | 新版 |
| [查询群内群模板机器人](0758-search-group-scene-template-robot.md) | 查询群内群模板机器人信息。 | 新版 |

##### **群模板**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [启用群模板](0759-enable-a-group-template.md) | 根据群模板ID启用群模板。 | 旧版 |
| [停用群模板](0760-disable-a-group-template.md) | 根据群模板ID停用群模板。 | 旧版 |

##### **群吊顶**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建并开启互动卡片吊顶](0761-send-group-helper-message.md) | 创建并开启会话中的互动卡片吊顶。 | 新版 |
| [关闭互动卡片吊顶](0762-close-interactive-card-ceiling.md) | 关闭会话中的互动卡片吊顶。 | 新版 |

##### **群助手**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [发送群助手消息](0763-group-template-robot-message.md) | 通过群模板定义的机器人向群内发送消息。 | 旧版 |

### **回调事件列表**

会话管理支持群会话解散、群会话添加人员、删除人员、更换群主等等回调事件，更多事件可参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## **使用教程**

钉钉提供了会话管理接口接入流程示例。

- [创建群聊会话（场景群）](0734-create-a-group-chat-session.md)
- [创建快捷入口（群插件）](0735-create-a-group-plug-in.md)
- [群助手发送消息](0733-group-assistant-sends-a-message.md)
- [创建、查询、修改及管理群会话](0737-group-session-operation-process.md)
- [实现置顶卡片纯拉模式](0736-pure-pull-mode-process-guide.md)

## **名词解释**

### **会话**

钉钉开放的会话类型主要包括**人与人单聊会话**、**群聊会话**2种。

### **群成员**

指群聊会话中所有的组成成员。

### **群管理身份**

指群聊会话中具备不同群管理权限的身份类型，包括**群主、群管理员、群普通成员**，它们具备的群管理权限范围为群主>群管理员>群普通成员。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8235423761/p547987.png)

### **群角色**

指群成员在群中被群主或群管理员赋予的角色，例如「产品经理」、「HR」等。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8235423761/p547988.png)

### **群模板**

通过预设群模板，并使用群模板创建群聊会话、或将普通内部群转为套用群模板的群，你可以将集群设置项、群内机器人、群内快捷入口等于一身的多样功能一次性安装到群内，你还可以通过群模板实现对群聊会话的批量化管理；同时，群模板支持设置可见范围并在+号建群入口中展示，让组织内用户直接在钉钉端内一键创建自定义类型的群聊会话。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4925092761/p543335.png)

### **吊顶**

群聊会话支持通过API将指定的内容填入指定群的吊顶中，展示通知、公告等信息，提高信息触达。

### **快捷入口**

原群插件。通过群内的快捷栏快速打开常用的应用，无需跳转到工作台或应用广场，在群内实现业务高效流转

群聊会话支持通过群模板和酷应用自定义指定群的快捷入口，包括具体的入口链接、顺序等；单聊机器人会话中的快捷入口也可通过API根据组织维度进行设定。

如何创建快捷入口，可参考[创建快捷入口（群插件）](0735-create-a-group-plug-in.md)。

### **互动卡片**

互动卡片在会话中是动态消息的一种类型，具有动态性、可交互性、多端统一等特点，能够更丰富的去展示信息，并且促进用户即刻沟通互动。

### **chatId**

chatId用于唯一标识**群聊会话**，通过[创建群](1483-session-management-creates-groups.md)接口返回值获取。

> **[!IMPORTANT]**
>
> 后续版本中**chatid**将不再使用，请将**openConversationId**作为群会话唯一标识。

### **openConversationId**

openConversationId用于唯一识别**群聊会话**，通过[创建群](1486-create-a-scene-group-v2.md)接口返回值获取。

### **templateId**

群模板的唯一识别ID，[开发者后台-开放能力-场景群-群模板](https://open-dev.dingtalk.com/fe/im#/group/list)的详情页面中可获取。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4925092761/p543332.png)
