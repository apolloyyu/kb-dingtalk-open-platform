---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/dedicated-dingtalk-overview"
namespace: "development"
slug: "dedicated-dingtalk-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 概述"
doc_id: "chN58Xrk2p"
updated_at: "2026-07-14 09:09:58"
---

> Source: https://open.dingtalk.com/document/development/dedicated-dingtalk-overview
> Path: 应用开发 / 服务端API / 专属钉钉 > 概述
> Updated: 2026-07-14 09:09:58

# 概述

本文档介绍了什么是专属钉钉，如何申请开通专属钉钉，专属钉钉接口能力，以及如何接入专属钉钉接口能力等。

## 什么是专属钉钉

专属钉钉助力企业打造专属、安全、开放的数字化办公运营平台，定义企业自己的数字化工作学习方式。更多介绍请参见[钉钉使用手册-专属钉钉](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/4Pko7gla1mAWRxPPgRaEJBxz5qZY9Q6j)。

**平台支撑**

提供标准的数字化应用平台、统一的企业应用入口、丰富的SaaS应用、持续的更新迭代。

**降本增效**

基于专属钉钉平台，用户可根据业务场景快速搭建客制化应用，为业务发展提供数字化运营支撑。

**文化共振**

以用户为中心重构用户体验，围绕企业文化品牌形象打造一款属于企业自己的App、实现企业文化建设和生态运营。

**决策支撑**

提供专属开放接口，连通组织数据和业务数据，帮助企业构造运营分析数据，为经营决策提供数据支撑。

**运营优化**

通过五个在线，实现生态互联、员工赋能、重构商业模式，助力企业优化运营。

**安全托管**

支持混合云部署、数据私有化存储；提供存储、网络、安全策略等保障方案，为客户打造企业级安全托管服务。

## 如何申请开通专属钉钉

步骤一：打开钉钉移动端，单击**我的**。

步骤二：在我的页面，单击**发现**。

步骤三：在发现页面，单击**钉钉专属版**。

步骤四：在专属钉钉体验中心页面，单击**申请样板间**。

步骤五：在申请样板间页面，填写申请信息。

- **选择您的组织**：选择申请开通专属钉钉的组织。
- **所属行业**：选择组织所属行业。
- **申请用途**：填写申请用途。

步骤六：填写完申请信息后，单击**提交申请**。![图片排版-手机展示-4张图1备份 4](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8931993871/p449400.png)

## 开放概览

### 开放接口列表

专属钉钉提供了丰富的接口开放能力，开发者通过API接口可以实现专属钉钉和企业业务系统打通。

#### **审计**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取审计协议签署人员信息](0804-obtains-the-information-about-the-persons-who-sign-the-audit-1.md) | 获取审计应用内已签署和未签署人员的信息 | 新版 |

#### **可信设备**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新增可信设备信息](0805-add-information-about-a-trusted-device.md) | 新增一个可信设备。 | 新版 |
| [批量新增可信设备](0806-create-multiple-trusted-devices.md) | 给某个用户批量新增可信设备。 | 新版 |
| [删除可信设备](0807-delete-trusted-devices.md) | 通过mac地址删除可信设备。 | 新版 |
| [查询可信设备详细信息](0808-query-trusted-device-details.md) | 查询组织内员工的可信设备详细信息。 | 新版 |
| [查询公共设备](0809-query-public-equipment.md) | 调用本接口查询公共设备。 | 新版 |

#### **互动服务窗**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [新增服务号](0810-added-service-number.md) | 新增一个服务号。 | 旧版 |
| [更新服务号](0811-service-number-update-1.md) | 更新指定服务号的相关信息。 | 旧版 |
| [查询服务号列表](0812-query-service-number-list.md) | 查询当前组织的服务号列表。 | 旧版 |
| [查询服务号详情](0813-inquire-about-service-number-details.md) | 根据服务号的unionid查询服务号详情。 | 旧版 |
| [新增文章](0814-new-article-1.md) | 新增一篇文章。 | 旧版 |
| [删除文章](0815-delete-article-1.md) | 删除一篇指定的文章。 | 旧版 |
| [更新文章](0816-save-article-details-1.md) | 更新指定文章。 | 旧版 |
| [查询文章列表](0817-query-the-article-list.md) | 查询文章列表。 | 旧版 |
| [获取文章详情](0818-get-article.md) | 查询一篇文章的详细信息。 | 旧版 |
| [发布文章](0819-article-publishing-interface-1.md) | 发布文章。 | 旧版 |
| [新增图文卡片](0820-new-message-card-1.md) | 新增消息卡片。 | 旧版 |
| [删除图文卡片](0821-delete-message-card.md) | 删除指定的消息卡片素材。 | 旧版 |
| [获取图文卡片详情](0822-get-message-card-details.md) | 获取消息卡片详情。 | 旧版 |
| [更新图文卡片](0823-message-card-material-update-interface.md) | 更新消息卡片。 | 旧版 |
| [查询图文卡片列表](0824-query-message-card-list.md) | 查询消息卡片列表。 | 旧版 |
| [消息撤回](0825-service-number-message-withdrawal.md) | 根据消息发送的任务id撤回消息。 | 旧版 |
| [消息群发](0826-api-sendmessage.md) | 群发消息。 | 新版 |
| [查询群发消息列表](0827-service-account-query-msgsend-records.md) | 查询指定服务号群发消息列表。 | 新版 |
| [查询群发消息详情](0828-service-account-msg-record-detail.md) | 查询指定推送号群发消息详情。 | 新版 |
| [服务号菜单更新](0829-service-number-menu-update.md) | 更新服务号的会话菜单。 | 旧版 |
| [查询服务号菜单](0830-query-service-number-menu-1.md) | 查询指定服务号的会话菜单。 | 旧版 |

#### **产业互联**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取可打标部门列表](0832-obtains-a-list-of-departments-that-can-be-marked.md) | 获取可打标部门的信息 | 新版 |
| [获取子标签列表](0833-obtain-child-tags-from-a-parent-tag.md) | 使用父标签ID获取子标签列表 | 新版 |
| [设置部门伙伴类型和伙伴编码](0834-set-department-partner-type-and-partner-code.md) | 通过部门ID设置部门伙伴类型和伙伴编码。 | 新版 |
| [修改伙伴类型可见性](0835-modify-partner-type-visibility.md) | 修改伙伴标签类型可见性。 | 新版 |
| [查询伙伴角色列表](0836-query-the-list-of-partners.md) | 根据父标签ID获取角色列表。 | 新版 |
| [修改角色可见性](0837-modify-role-visibility.md) | 修改角色标签可见性。 | 新版 |
| [发送邀请函](0838-send-invitations.md) | 向下游企业发送加入合作伙伴邀请函。 | 新版 |
| [根据userId查询人员的标签信息](0839-you-can-call-this-operation-to-retrieve-the-user-tag.md) | 查询上下游组织内人员的标签信息。 | 新版 |

#### **DING**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [DING服务](0840-send-in-application-ding.md) | 通过专属DING服务中设置的互动服务窗来发送应用内DING。 | 新版 |

#### **文件**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [发送文件更改的评论](0842-send-comments-on-file-changes.md) | 发送文件更改的评论。 | 新版 |
| [获取文件操作记录](0841-obtain-file-operation-records.md) | 获取专属钉钉内成员所有所在组织的操作文件或文档的记录。 | 新版 |
| [获取专属存储文件路径](0843-api-getprivatestorefilepath.md) | 根据 spaceId 和 dentryId 获取专属存储文件路径。 | 新版 |

#### **企业内部群**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询企业内部群信息](0844-obtain-group-info.md) | 查询企业内部群信息。 | 新版 |
| [企业内部群禁言或解除禁言](0845-exclusive-dingtalk-group-ban.md) | 设置企业内部群禁言或者解除企业内部群禁言。 | 新版 |
| [获取群活跃明细列表](0846-obtains-the-group-activity-details-list.md) | 获取自己企业下群组的相关信息列表。 | 新版 |

#### **其他**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取防截屏操作记录](0849-obtain-anti-screen-capture-operation-records.md) | 获取企业员工防截屏操作记录。 | 新版 |
| [同步存储数据](0847-api-datasync.md) | 为应用同步数据到专属存储。 | 新版 |
| [专属小红点推送](0848-push-a-red-dot-to-the-micro-application.md) | 给企业自建或第三方企业应用推送在快捷栏上显示的小红点信息。 | 新版 |
| [查询实人认证状态](0850-queries-the-id-verification-status.md) | 查询实人认证状态。 | 新版 |
| [查询人脸录入状态](0851-query-face-entry-status.md) | 查询人脸录入状态。 | 新版 |
| [获取实人认证接口调用记录](0852-obtains-the-call-record-of-the-id-authentication-api.md) | 获取实人认证接口调用记录。 | 新版 |
| [获取人脸对比接口调用记录](0853-you-can-call-this-operation-to-query-the-call-records.md) | 获取人脸对比接口调用记录。 | 新版 |
| [根据会议逻辑ID查询会议基本信息](0854-query-basic-meeting-information-using-a-logical-id.md) | 根据会议逻辑ID查询会议基本信息，包括会议标题、创建者昵称、开始时间等。 | 新版 |
| [获取企业专属钉钉权益列表](0855-api-queryexclusivebenefits.md) | 获取企业专属钉钉的权益列表。 | 新版 |
| [更新发送文件的检测状态](0856-update-the-detection-status-of-a-sent-file.md) | 更改发送文件的检测状态。 | 新版 |
| [企业员工专属安全管控功能命中查询](0857-api-checkcontrolhitstatus.md) | 查询企业员工专属安全管控功能命中情况。 | 新版 |
| [获取视频会议详情](0858-get-video-meeting-details.md) | 获取视频会议详情，包含参会人员列表和各个参会人员的参会时长。 | 新版 |

### 回调事件列表

专属钉钉支持企业员工发送文件的检测事件和服务号收到用户消息回调事件。

- [服务号接收单聊消息](../04-LFcRvVD08N-事件订阅/0206-service-number-receiving-single-chat-message.md)
- [企业员工发送文件的检测事件](../04-LFcRvVD08N-事件订阅/0208-detection-event-of-enterprise-employee-sending-file.md)
- [专属群扩容审批](../04-LFcRvVD08N-事件订阅/0204-exclusive-group-expansion-approval.md)
- [专属钉钉数据迁移](../04-LFcRvVD08N-事件订阅/0205-dedicated-dingtalk-data-migration.md)
