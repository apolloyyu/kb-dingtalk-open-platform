---
title: "企业账号概述"
source_url: "https://open.dingtalk.com/document/development/dedicated-account-overview"
namespace: "development"
slug: "dedicated-account-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 企业账号概述"
doc_id: "mqXKgJOl0A"
updated_at: "2025-09-10 19:27:25"
---

> Source: https://open.dingtalk.com/document/development/dedicated-account-overview
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 企业账号概述
> Updated: 2025-09-10 19:27:25

# 企业账号概述

本文介绍了什么是企业账号，企业账号开放的接口能力等。

## 什么是企业账号

企业账号是组织/企业可管理的账号，包括创建、修改、停用、启用等对账号整个生命周期的操作都可由组织进行管理。更多企业账号详情可参考[钉钉使用手册-企业账号介绍](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbEj6djBVjXLq?dontjump=true%23%23)。

目前有以下两种类型：

- SSO账号：使用组织内部已有的账号体系登录钉钉，账号管理在钉钉外。
- 钉钉企业账号：在钉钉创建并进行管理的企业账号。

## 如何开通企业账号

该功能目前仍在灰度测试中，如果您所在组织尚未开通，请先[填写试用申请](https://yida.alibaba-inc.com/o/dingtalk-jjfa?spm=a213l2.15044028.1543252304.1.6a2e5632YehstI&acm=lb-zebra-694702-8604571.1003.4.8185952&scm=1003.4.lb-zebra-694702-8604571.OTHER_15916559412151_8185952#/?channel=%E4%B8%93%E5%B1%9E%E9%92%89%E9%92%89-%E5%92%A8%E8%AF%A2%E4%B8%93%E5%AE%B6-PC)。

## 企业账号开放的接口能力

企业账号提供了丰富的接口开放能力，开发者通过API接口可以实现企业账号和企业业务系统打通。

| API | 说明 | 新版规范（新版服务端API） | 旧版规范（服务端API） |
| --- | --- | --- | --- |
| 创建企业账号用户 | 创建企业账号新用户。 | - | [创建企业账号用户](https://open.dingtalk.com/document/orgapp/create-dedicated-accounts)  **[!NOTE]**  文档已迁移至历史文档目录下。   - 如果未使用本接口，推荐根据账号类型选择使用[创建SSO企业账号](0104-create-an-sso-account.md)或者[创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md)或者[邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md)接口。 - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。 |
| 创建SSO企业账号 | 创建SSO企业账号新用户。 | - | [创建SSO企业账号](0104-create-an-sso-account.md) |
| 创建钉钉自建企业账号 | 创建钉钉自建企业账号新用户。 | - | [创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md) |
| 邀请其他组织企业账号加入 | 邀请其他组织企业账号加入。 | - | [邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md) |
| 更新企业账号用户信息 | 更新指定的企业账号用户信息。 | - | [更新企业账号用户信息](0107-update-dedicated-accounts-information.md) |
| 查询企业账号用户详情 | 获取指定企业账号用户的详细信息。 | - | [查询企业账号用户详情](0108-queries-the-details-of-a-dedicated-account.md) |
| 获取部门企业账号用户详情 | 获取指定部门中的用户详细信息。 | - | [获取部门企业账号用户详情](0116-queries-account-details.md) |
| 根据手机号查询企业账号用户 | 根据手机号获取企业账号用户的userId。 | - | [根据手机号查询企业账号用户](0117-obtain-the-userid-of-your-mobile-phone-number.md) |
| 启用企业账号 | 启用指定企业账号。 | [启用企业这账号](0109-enable-a-dedicated-account.md) | - |
| 停用企业账号 | 停用指定的企业账号。 | [停用企业账号](0110-disable-an-exclusive-account.md) | - |
| 强制登出企业账号 | 强制登出指定的企业账号。 | [强制登出企业账号](0111-force-logout-from-dedicated-account.md) | - |
| 查询企业账号状态 | 查询某企业账号的启用状态。 | [查询企业账号状态](0112-query-dedicated-account-status-1.md) | - |
| 授权企业账号可加入多组织 | 授权企业账号可以加入多个组织。 | [授权企业账号可加入多组织](0114-authorize-a-dedicated-account-to-join-multiple-organizations.md) | - |
| 查询企业账号拥有的组织 | 查询企业账号在哪些企业下拥有创建者身份，并获取这些企业信息。 | [查询企业账号拥有的组织](0113-you-can-call-this-operation-to-query-the-organization-that.md) | - |
| 企业账号转交主管理员（创建者） | 将本组织内某企业账号有所有权的组织，转交给另一企业账号，如果接收的账号不在该组织内则自动加入。 | [企业账号转交主管理员（创建者）](0118-transfer-exclusive-account-to-main-administrator-creator.md) | - |
| 根据迁移后的dingId查询原dingId | 根据迁移后的dingId查询原dingId。 | [根据迁移后的dingId查询原dingId](0119-query-the-original-dingid-based-on-the-dingid-after-migration.md) | - |
| 根据迁移后的unionId查询原unionId | 根据迁移后的unionId查询原unionId。 | [根据迁移后的unionId查询原unionId](https://open.dingtalk.com/document/orgapp/query-the-original-union-id-based-on-the-union-id)[根据迁移后的unionId查询原unionId](0120-query-the-original-union-id-based-on-the-union-id.md) | - |
| 根据原dingId查询迁移后的dingId | 根据原dingId查询迁移后的dingId。 | [根据原dingId查询迁移后的dingId](0121-query-the-new-dingid-based-on-the-original-dingid.md) | - |
| 根据原unionId查询迁移后的unionId | 根据原unionId查询迁移后的unionId。 | [根据原unionId查询迁移后的unionId](0122-the-union-id-that-you-want-to-query-you-can.md) | - |

## 名词解释

### 组织代码

由于企业账号归属于组织，在登录时需要通过输入**组织代码**告诉钉钉希望前往登录的组织。组织代码是使用企业账号组织的唯一标识。

当组织开通企业账号功能后，钉钉会默认分配一个8位随机的组织代码，您可以联系账号管理员在[钉钉管理后台](https://oa.dingtalk.com/) > **设置** > **组织代码**查看。同时组织管理员也可以申请更加个性化的代码，方便组织成员记忆和使用。![iShot_2023-09-07_10.36.36.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0300704961/p716435.png)
