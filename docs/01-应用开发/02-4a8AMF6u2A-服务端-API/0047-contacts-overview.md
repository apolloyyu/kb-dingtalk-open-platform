---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/contacts-overview"
namespace: "development"
slug: "contacts-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 概述"
doc_id: "21IqXiWBhF"
updated_at: "2026-07-02 10:35:39"
---

> Source: https://open.dingtalk.com/document/development/contacts-overview
> Path: 应用开发 / 服务端 API / 通讯录管理 > 概述
> Updated: 2026-07-02 10:35:39

# 概述

本文档旨在帮助读者全面了解钉钉通讯录，通过阅读本文档，企业管理者、IT 负责人和开发者可以快速掌握通讯录的能力边界，为后续的系统集成和业务创新奠定基础。

## **什么是钉钉通讯录**

钉钉通讯录是企业内部信息统一管理的核心基础设施，它以数字化方式呈现企业的组织架构和人员信息，为企业成员提供快速找人、高效协作的基础能力。

更多功能介绍请参考[钉钉使用手册-企业通讯录](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbpxy30LLzLq2?dontjump=true#)。

| **维度** | **说明** |
| --- | --- |
| 本质 | 企业组织结构的数字化表达载体 |
| 形态 | 树形部门结构 + 人员信息数据库 |
| 作用 | 连接企业人、事、物的枢纽，支撑审批流、消息路由、权限控制等场景 |

## 如何查看通讯录

### 企业管理员视角

企业管理员可通过以下方式管理和查看通讯录：

- 钉钉管理后台：登录登录[钉钉管理后台](https://oa.dingtalk.com/)，进入**内部通讯录**模块，可进行通讯录的完整管理和配置
- 通讯录设置：配置通讯录的可见性规则、自定义字段、高管模式等高级功能

![iShot2022-01-10 17](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3305512461/p381941.png)

### 普通成员

普通组织成员可通过以下终端查看通讯录：

- **PC 端钉钉**：在钉钉 PC 客户端中点击「通讯录」标签，可查看企业组织架构和联系详情
- **手机端钉钉**：在钉钉移动 App 中进入「通讯录」页面，支持按部门浏览和关键词搜索
- **Web 端钉钉**：通过钉钉网页版访问通讯录功能

## 开放概览

### 开放接口列表

通讯录提供了丰富的接口开放能力，开发者通过API接口可以实现通讯录和企业业务系统打通。

#### **用户通讯录**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [获取用户通讯录个人信息](0054-dingtalk-retrieve-user-information.md) | 获取企业用户通讯录中的个人信息。 | 新版 |

#### **通讯录权限**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [获取通讯录权限范围](0053-obtain-corpsecret-authorization-scope.md) | 获取通讯录权限范围。 | 旧版 |

#### **用户管理**

| API | API说明 | API 版本 |
| --- | --- | --- |
| [创建用户](0055-user-information-creation.md) | 创建新用户。 | 旧版 |
| [更新用户信息](0057-user-information-update.md) | 更新指定的用户信息。 | 旧版 |
| [删除用户](0058-delete-a-user.md) | 根据用户的userid删除指定用户。 | 旧版 |
| [查询用户详情](0056-query-user-details.md) | 获取指定用户的详细信息。 | 旧版 |
| [获取部门用户基础信息](0066-queries-the-simple-information-of-a-department-user.md) | 获取指定部门的用户基础信息。 | 旧版 |
| [获取部门用户userid列表](0065-query-the-list-of-department-userids.md) | 获取指定部门的userid列表。 | 旧版 |
| [获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md) | 获取指定部门中的用户详细信息。 | 旧版 |
| [获取员工人数](0059-user-management-acquires-number-employees.md) | 获取员工人数。 | 旧版 |
| [获取未登录钉钉的员工列表](0067-queries-the-inactive-users-or-active-users-under-an-enterprise.md) | 查询指定日期内未登录钉钉的企业员工列表。 | 旧版 |
| [根据手机号查询用户](0063-query-users-by-phone-number.md) | 根据手机号获取用户的userId。 | 旧版 |
| [根据unionid获取用户userid](0064-query-a-user-by-the-union-id.md) | 根据unionid获取用户的userid。 | 旧版 |
| [获取管理员列表](0068-query-the-administrator-list.md) | 查询管理员列表。 | 旧版 |
| [获取管理员通讯录权限范围](0070-query-permissions-of-the-administrator-address-book.md) | 获取管理员通讯录权限范围。 | 旧版 |
| [获取管理员的应用管理权限](0069-obtains-the-administrator-s-microapplication-management-permission.md) | 获取管理员的应用管理权限。 | 旧版 |
| [查询离职记录列表](0073-query-the-details-of-employees-who-have-left-office.md) | 查询企业离职记录列表。 | 新版 |
| [设置高管模式](0071-update-executive-settings.md) | 设置员工的高管模式。 | 新版 |
| [获取用户高管模式设置](0072-get-user-executive-mode-settings.md) | 获取用户高管模式的设置详情。 | 新版 |
| [删除用户属性可见性设置](0076-delete-enterprise-employee-attribute-field-visibility-settings.md) | 删除企业员工属性字段可见性设置。 | 新版 |
| [获取用户属性可见性设置](0075-pull-hidden-property-field-for-enterprise-employees.md) | 获取企业员工属性字段隐藏设置。 | 新版 |
| [设置用户属性可见性](0074-add-or-update-the-hidden-settings-of-the-employee-property.md) | 新增或更新企业员工属性字段隐藏设置。 | 新版 |
| [搜索用户userId](0060-address-book-search-user-id.md) | 根据用户名称搜索用户userId。 | 新版 |
| [通讯录userId排序](0061-address-book-userid-sorting.md) | 根据用户姓名拼音进行userId排序。 | 新版 |

#### **部门管理**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [创建部门](0077-address-book-creation-department-established-department.md) | 创建新部门。 | 旧版 |
| [更新部门](0078-address-book-update-department.md) | 更新部门信息。 | 旧版 |
| [删除部门](0079-address-book-deletion-department.md) | 根据部门ID删除指定部门。 | 旧版 |
| [搜索部门ID](0080-address-book-search-department-id.md) | 搜索部门ID。 | 新版 |
| [获取部门详情](0081-query-department-details0-v2.md) | 根据部门ID获取指定部门详情。 | 旧版 |
| [获取部门列表](0082-user-management-acquires-the-list-departments.md) | 获取下一级部门基础信息。 | 旧版 |
| [获取子部门ID列表](0083-obtain-the-list-of-sub-department-ids.md) | 获取企业部门下的所有直属子部门列表。 | 旧版 |
| [获取指定部门的所有父部门列表](0084-query-the-list-of-all-parent-departments-of-a-department.md) | 获取指定部门的所有父部门ID列表。 | 旧版 |
| [获取指定用户的所有父部门列表](0085-queries-the-list-of-all-parent-departments-of-a-user.md) | 查询指定用户所属的所有父级部门。 | 旧版 |

#### **角色管理**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [创建角色](0086-address-book-add-role.md) | 创建新角色。 | 旧版 |
| [创建角色组](0091-add-a-role-group.md) | 创建角色组。 | 旧版 |
| [更新角色名称](0088-update-the-character-name.md) | 更新角色名称。 | 旧版 |
| [批量增加员工角色](0093-add-role-information-to-employees-in-batches.md) | 批量增加员工角色。 | 旧版 |
| [删除角色](0087-delete-role-information.md) | 根据角色ID删除指定的角色。 | 旧版 |
| [批量删除员工角色](0094-delete-the-color-information-of-employee-corners-in-batches.md) | 批量删除员工的角色。 | 旧版 |
| [设定角色成员管理范围](0095-update-role-member-management-department-scope.md) | 设定角色成员管理范围。 | 旧版 |
| [获取角色组列表](0092-obtains-the-role-group-information.md) | 获取角色组信息。 | 旧版 |
| [获取角色列表](0089-obtains-a-list-of-enterprise-roles.md) | 获取角色列表。 | 旧版 |
| [获取角色详情](0090-queries-role-details.md) | 根据角色ID获取指定角色详情。 | 旧版 |
| [获取指定角色的员工列表](0096-obtain-the-list-of-employees-of-a-role.md) | 获取指定角色的员工列表。 | 旧版 |

#### **外部联系人**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [添加外部联系人](0097-add-enterprise-external-contacts.md) | 添加企业外部联系人。 | 旧版 |
| [删除外部联系人](0098-delete-external-contact.md) | 删除企业外部联系人。 | 旧版 |
| [更新外部联系人](0099-update-enterprise-external-contacts.md) | 更新企业外部联系人。 | 旧版 |
| [获取外部联系人列表](0100-obtain-the-external-contact-list.md) | 获取企业外部联系人列表。 | 旧版 |
| [获取外部联系人标签列表](0101-obtains-a-list-of-external-contact-tags.md) | 获取企业外部联系人的标签。 | 旧版 |
| [获取外部联系人详情](0102-obtains-the-external-contact-details-of-an-enterprise.md) | 获取企业外部联系人的详细信息。 | 旧版 |

#### **企业账号**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [创建SSO企业账号](0104-create-an-sso-account.md) | 创建SSO企业账号新用户。 | 旧版 |
| [企业账号修改钉钉号](0105-api-changedingtalkid.md) | 修改企业账号钉钉号。 | 新版 |
| [创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md) | 创建钉钉自建企业账号新用户。 | 旧版 |
| [更新企业账号用户信息](0107-update-dedicated-accounts-information.md) | 更新指定的企业账号用户信息。 | 旧版 |
| [查询企业账号用户详情](0108-queries-the-details-of-a-dedicated-account.md) | 获取指定企业账号用户的详细信息。 | 旧版 |
| [启用企业账号](0109-enable-a-dedicated-account.md) | 启用指定企业账号。 | 新版 |
| [停用企业账号](0110-disable-an-exclusive-account.md) | 停用指定的企业账号。 | 新版 |
| [强制登出企业账号](0111-force-logout-from-dedicated-account.md) | 强制登出指定的企业账号。 | 新版 |
| [查询企业账号状态](0112-query-dedicated-account-status-1.md) | 查询某企业账号的启用状态。 | 新版 |
| [查询企业账号拥有的组织](0113-you-can-call-this-operation-to-query-the-organization-that.md) | 查询企业账号在哪些企业下拥有创建者身份，并获取这些企业信息。 | 新版 |
| [授权企业账号可加入多组织](0114-authorize-a-dedicated-account-to-join-multiple-organizations.md) | 授权企业账号可以加入多个组织。 | 新版 |
| [邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md) | 加入其他组织企业账号进入本组织。 | 旧版 |
| [获取部门企业账号用户详情](0116-queries-account-details.md) | 获取指定部门中的用户详细信息。 | 旧版 |
| [根据手机号查询企业账号用户](0117-obtain-the-userid-of-your-mobile-phone-number.md) | 根据手机号获取企业账号用户的userId。 | 旧版 |
| [企业账号转交主管理员（创建者）](0118-transfer-exclusive-account-to-main-administrator-creator.md) | 将本组织内某企业账号有所有权的组织，转交给另一企业账号。 | 新版 |
| [根据迁移后的dingId查询原dingId](0119-query-the-original-dingid-based-on-the-dingid-after-migration.md) | 根据迁移后的dingId查询原dingId。 | 新版 |
| [根据迁移后的unionId查询原unionId](0120-query-the-original-union-id-based-on-the-union-id.md) | 根据迁移后的unionId查询原unionId。 | 新版 |
| [根据原dingId查询迁移后的dingId](0121-query-the-new-dingid-based-on-the-original-dingid.md) | 根据原dingId查询迁移后的dingId。 | 新版 |
| [根据原unionId查询迁移后的unionId](0122-the-union-id-that-you-want-to-query-you-can.md) | 根据原unionId查询迁移后的unionId。 | 新版 |
| [授权其他组织查看本组织的企业账号信息](0123-api-orgaccountmobilevisibleinotherorg.md) | 其他组织查看本组织的企业账号信息的具体字段。 | 新版 |

#### **企业管理**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [获取企业认证信息](0124-obtain-enterprise-authentication-information.md) | 获取企业认证信息。 | 新版 |
| [获取企业邀请信息](0125-obtain-invitation-information.md) | 获取企业的邀请信息。 | 新版 |
| [获取企业最新钉钉指数信息](0126-queries-the-latest-dingtalk-index-information.md) | 获取企业最新钉钉指数信息。 | 新版 |
| [查询管理员是否有应用管理权限](0127-check-whether-the-administrator-has-application-management-permissions.md) | 查询企业管理员是否有应用的管理权限。 | 新版 |

#### **行业通讯录**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [获取部门详情](0129-industry-address-book-api-for-obtaining-department-information.md) | 根据部门ID获取部门详情。 | 旧版 |
| [获取部门下人员列表](0130-obtains-the-list-of-people-under-a-department.md) | 获取部门下的人员列表信息。 | 旧版 |
| [获取部门列表](0128-obtains-a-list-of-industry-departments.md) | 根据部门ID获取行业通讯录部门列表。 | 旧版 |
| [获取部门用户详情](0131-queries-department-user-details.md) | 获取部门用户详情。 | 旧版 |
| [获取企业信息](0132-obtain-enterprise-information.md) | 获取行业通讯录的企业信息。 | 旧版 |

#### **通讯录ID转译**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [异步转译通讯录ID](0133-asynchronous-address-book-file-content-translation.md) | 起异步通讯录ID内容转译，替换产品方案商通讯录权限范围内的用户ID和部门ID。 | 新版 |
| [获取异步转译任务结果](0134-obtains-the-results-of-an-asynchronous-translation-task.md) | 获取查询已经提交过的转译任务结果。 | 新版 |

#### **通讯录可见性管理**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [获取通讯录隐藏设置](0136-obtains-the-hide-settings-of-the-address-book.md) | 批量获取通讯录隐藏的设置列表。 | 新版 |
| [删除通讯录隐藏设置](0137-delete-hide-settings.md) | 删除通讯录隐藏设置。 | 新版 |
| [新增或更新通讯录隐藏设置](0139-update-address-book-hide-settings.md) | 新增或更新通讯录隐藏设置。 | 新版 |
| [设置部门可见性优先级](0138-set-address-book-visibility-sub-department-settings-to-take-precedence.md) | 设置通讯录部门可见性优先级。 | 新版 |
| [新增或修改限制查看通讯录设置](0140-add-or-modify-visibility-settings-for-address-book-restrictions.md) | 新增或修改限制查看通讯录设置。 | 新版 |
| [获取限制查看通讯录设置列表](0141-gets-a-list-of-address-book-limit-visibility-settings.md) | 获取限制查看通讯录的设置列表。 | 新版 |
| [删除限制查看通讯录设置](0142-delete-visible-restrictions.md) | 删除限制查看通讯录设置 | 新版 |

#### **上下游组织**

| API | 说明 | API 版本 |
| --- | --- | --- |
| [创建上下游组织](0144-create-a-cooperation-space.md) | 创建上下游组织。 | 新版 |
| [解除关联组织](0145-disassociate-upstream-and-downstream-organizations.md) | 解除关联组织关系。 | 新版 |
| [获取上下游组织的邀请信息](0146-obtain-the-invitation-information-of-a-cooperation-space.md) | 获取上下游组织的邀请链接。 | 新版 |
| [批量通过伙伴组织的加入申请](0147-apply-for-batch-addition-through-upstream-and-downstream-organizations.md) | 批量通过伙伴组织加入上下游组织申请。 | 新版 |
| [更新伙伴组织在上下游组织内的属性信息](0148-update-properties-of-branches-in-alibaba-group-1.md) | 更新伙伴组织在上下游组织内内的属性信息。 | 新版 |
| [设置伙伴组织在上下游组织内的可见范围](0149-set-the-visible-range-of-the-branch-in-the-group-1.md) | 设置伙伴组织在上下游组织内的可见范围。 | 新版 |
| [获取企业已经加入的或申请加入中的上下游组织的信息](0150-obtains-information-about-the-workspaces-that-the-enterprise-has-joined.md) | 获取企业已经加入的上下游组织信息或获取企业已经加入的上下游组织信息。 | 新版 |
| [获取已加入或正在申请加入上下游组织的组织和个人信息](0151-obtains-the-information-about-how-to-join-or-apply-to.md) | 通过上下游组织组织ID获取加入或申请加入上下游组织的组织和个人信息。 | 新版 |

#### 上下级组织

| API | 说明 | API 版本 |
| --- | --- | --- |
| [解除关联组织](0153-disassociate-an-organization.md) | 解除关联组织关系。 | 新版 |
| [获取主干组织列表](0154-obtain-backbone-organization-list.md) | 获取主干组织列表。 | 新版 |
| [获取分支组织列表](0155-obtains-the-branch-organization-list.md) | 获取分支组织列表。 | 新版 |
| [批量通过伙伴组织的加入申请](0156-batch-through-the-application-of-partner-organizations-to-join-contact.md) | 批量通过分支组织加入主干组织申请。 | 新版 |
| [获取上下级组织分支授权的数据](0157-data-authorized-by-a-branch-of-an-associated-organization.md) | 获取上下级组织分支授权的数据。 | 新版 |
| [设置分支组织在主干组织内的可见范围](0158-sets-the-visible-range-of-branch-organizations-within-the-group.md) | 设置分支组织在主干组织内的可见范围。 | 新版 |
| [更新分支组织在主干组织内的属性信息](0159-updates-the-property-information-of-a-branch-organization-in-a.md) | 更新分支组织在主干组织内的属性信息。 | 新版 |

### 回调事件列表

通讯录支持用户变更、部门变更、角色变更和企业信息变更等回调事件，更多事件可参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## 使用教程

钉钉提供了通讯录接口接入流程示例。

- [创建、获取、更新和删除企业员工](0048-address-book-employee-operations.md)
- [创建、获取、更新和删除企业部门](0049-operations-related-to-address-book-departments.md)
- [企业OA系统与钉钉通讯录实现同步](0050-synchronization-between-enterprise-oa-system-and-dingtalk-address-book.md)
- [第三方个人小程序获取登录用户信息](0051-third-party-personal-applet-to-obtain-login-user-information-tutorial.md)

## 名词解释

### 工号

工号对应的字段编码是job\_number，企业内员工的工号可以不唯一，所以不能作为员工在企业内的唯一标识。

企业管理员登录[钉钉管理后台](https://oa.dingtalk.com/)，在通讯录页面单击**员工姓名**可查看员工工号，工号字段是非必填字段。![通讯录概述1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0538514561/p440185.png)

### unionId

用户在当前钉钉开放平台账号范围内的唯一标识，同一个钉钉开放平台账号可以包含多个开放应用，同时也包含ISV的套件应用及企业应用。

unionId可通过调用[查询用户详情](0056-query-user-details.md)接口获取。

### 角色组和角色

企业内定义的角色组和角色，方便对员工身份信息进行管理，员工同时可拥有多个角色身份。

企业管理员登录[钉钉管理后台](https://oa.dingtalk.com/)，在**通讯录 > 内部通讯录管理**页面，单击**角色**可查看角色组和角色。![通讯录概述2](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0538514561/p440187.png)

### 通讯录扩展字段

通讯录可以添加扩展字段。

企业管理员登录[钉钉管理后台](https://oa.dingtalk.com/)，在**内部通讯录设置 > 通讯录信息** > **添加自定义字段**页面，新增自定义字段。![通讯录概述3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0538514561/p440179.png)
