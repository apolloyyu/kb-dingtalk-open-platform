---
title: "不纳入调用量限制的接口清单"
source_url: "https://open.dingtalk.com/document/development/basic-interfaces-such-as-log-off-and-address-book"
namespace: "development"
slug: "basic-interfaces-such-as-log-off-and-address-book"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "平台公告与计费 > 资源与计费 > API调用量配额 > 不纳入调用量限制的接口清单"
doc_id: "GnKegSScKl"
updated_at: "2026-07-22 16:24:53"
---

> Source: https://open.dingtalk.com/document/development/basic-interfaces-such-as-log-off-and-address-book
> Path: 应用开发 / 服务端 API / 平台公告与计费 > 资源与计费 > API调用量配额 > 不纳入调用量限制的接口清单
> Updated: 2026-07-22 16:24:53

# 不纳入调用量限制的接口清单

本文介绍了不纳入每月调用量限制的接口清单，包括基础接口（获取访问凭证、身份验证（免登）和通讯录）和生态接口的清单。

## **基础清单**

### **获取访问凭证**

| **API** | **接口说明** |
| --- | --- |
| [获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md) | 调用本接口获取access\_token，调用服务端API获取应用资源时，需要通过access\_token来鉴权调用者身份进行授权。 |
| [获取第三方个人应用的access\_token](0034-obtain-personal-application.md) | 调用本接口获取第三方个人应用的access\_token。 |
| [获取用户token](0031-obtain-user-token.md) | 调用本接口获取用户token。 |
| [获取jsapiTicket](0038-create-a-jsapi-ticket.md) | 当开发H5微应用时，需要先通过本接口获取jsapi\_ticket，然后再生成鉴权签名，最后调用dd.config完成鉴权。 |
| [获取微应用后台免登的accessToken](0024-obtain-the-access-token-of-the-micro-application-background-without-log-on.md) | 调用本接口获取微应用后台免登的access\_token。获取的access\_token即ssotoken只在应用管理后台免登场景中使用。 |
| [查询个人授权记录](0039-query-personal-authorization-records.md) | 当需要查询用户的授权记录信息时，可以调用本接口查询用户的个人授权记录。 |

### **身份验证（免登）**

| **API** | **接口说明** |
| --- | --- |
| [通过免登码获取用户信息](0023-obtain-the-userid-of-a-user-by-using-the-log-free.md) | 在第三方企业应用免登和企业内部应用免登场景中，开发者需要使用本接口通过access\_token和免登接口中获取的code来获取用户userid。 |
| [获取应用管理后台免登的用户信息](0025-obtains-the-identity-of-an-application-administrator.md) | 在应用管理后台免登场景中，需要本接口通过获取到的免登授权码code和获取到的应用后台免登的access\_token来换取应用管理员的身份信息。 |
| [获取应用管理后台免登的用户信息](0025-obtains-the-identity-of-an-application-administrator.md) | 在应用管理后台免登场景中，需要本接口通过获取到的免登授权码code和获取到的应用后台免登的access\_token来换取应用管理员的身份信息。 |

### **通讯录管理**

#### **用户管理**

| **API** | **接口说明** |
| --- | --- |
| [创建用户](0054-user-information-creation.md) | 调用本接口创建新用户。 |
| [更新用户信息](0056-user-information-update.md) | 调用本接口更新指定的用户信息。 |
| [查询用户详情](0055-query-user-details.md) | 调用本接口获取指定用户的详细信息。 |
| [删除用户](0057-delete-a-user.md) | 调用本接口根据用户的userid删除指定用户。 |
| [获取部门用户基础信息](0065-queries-the-simple-information-of-a-department-user.md) | 调用本接口获取指定部门的用户基础信息。 |
| [获取部门用户详情](0061-queries-the-complete-information-of-a-department-user.md) | 调用本接口获取指定部门中的用户详细信息。 |
| [获取部门用户userid列表](0064-query-the-list-of-department-userids.md) | 调用本接口获取指定部门的userid列表。 |
| [获取员工人数](0058-user-management-acquires-number-employees.md) | 调用本接口获取员工人数。 |
| [获取未登录钉钉的员工列表](0066-queries-the-inactive-users-or-active-users-under-an-enterprise.md) | 调用本接口查询指定日期内未登录钉钉的企业员工列表。 |
| [根据手机号查询用户](0062-query-users-by-phone-number.md) | 调用本接口根据手机号获取专属账号用户的userId。 |
| [根据unionid获取用户userid](0063-query-a-user-by-the-union-id.md) | 调用本接口根据unionid获取用户的userid。 |
| [获取管理员列表](0067-query-the-administrator-list.md) | 调用本接口查询管理员列表。 |
| [获取管理员通讯录权限范围](0069-query-permissions-of-the-administrator-address-book.md) | 调用本接口获取管理员通讯录权限范围。 |
| [查询离职记录列表](0072-query-the-details-of-employees-who-have-left-office.md) | 调用本接口查询企业离职记录列表，包含离职员工的离职日期、手机号码和退出企业方式等信息。 |
| [设置高管模式](0070-update-executive-settings.md) | 调用本接口设置员工的高管模式。 |
| [获取用户高管模式设置](0071-get-user-executive-mode-settings.md) | 调用本接口获取用户高管模式设置。 |
| [删除用户属性可见性设置](0075-delete-enterprise-employee-attribute-field-visibility-settings.md) | 调用本接口删除企业员工属性字段可见性设置。 |
| [获取用户属性可见性设置](0074-pull-hidden-property-field-for-enterprise-employees.md) | 调用本接口获取用户属性可见性设置。 |
| [设置用户属性可见性](0073-add-or-update-the-hidden-settings-of-the-employee-property.md) | 调用本接口设置用户属性可见性。 |
| [获取用户通讯录个人信息](0053-dingtalk-retrieve-user-information.md) | 调用本接口获取企业用户通讯录中的个人信息。 |

#### **部门管理**

| **API** | **接口说明** |
| --- | --- |
| [创建部门](0076-address-book-creation-department-established-department.md) | 调用本接口创建新部门。 |
| [更新部门](0077-address-book-update-department.md) | 调用本接口更新部门信息。 |
| [删除部门](0078-address-book-deletion-department.md) | 调用本接口根据部门ID删除指定部门。 |
| [获取部门详情](0080-query-department-details0-v2.md) | 调用本接口根据部门ID获取指定部门详情。 |
| [获取部门列表](0081-user-management-acquires-the-list-departments.md) | 调用本接口获取下一级部门基础信息。 |
| [获取子部门ID列表](0082-obtain-the-list-of-sub-department-ids.md) | 调用本接口获取企业部门下的所有直属子部门列表。 |
| [获取指定部门的所有父部门列表](0083-query-the-list-of-all-parent-departments-of-a-department.md) | 调用本接口获取指定部门的所有父部门ID列表。 |
| [获取指定用户的所有父部门列表](0084-queries-the-list-of-all-parent-departments-of-a-user.md) | 调用本接口查询指定用户所属的所有父级部门。 |

#### **角色管理**

| **API** | **接口说明** |
| --- | --- |
| [创建角色](0085-address-book-add-role.md) | 调用本接口创建新角色。 |
| [创建角色组](0090-add-a-role-group.md) | 调用本接口创建角色组。 |
| [更新角色名称](0087-update-the-character-name.md) | 调用本接口更新角色名称。 |
| [批量增加员工角色](0092-add-role-information-to-employees-in-batches.md) | 调用本接口批量增加员工角色。 |
| [删除角色](0086-delete-role-information.md) | 调用本接口根据角色ID删除指定的角色。 |
| [批量删除员工角色](0093-delete-the-color-information-of-employee-corners-in-batches.md) | 调用本接口批量删除员工的角色。 |
| [设定角色成员管理范围](0094-update-role-member-management-department-scope.md) | 调用本接口设定角色成员管理范围。 |
| [获取角色组列表](0091-obtains-the-role-group-information.md) | 调用本接口获取角色组信息。 |
| [获取角色列表](0088-obtains-a-list-of-enterprise-roles.md) | 调用本接口获取角色列表。 |
| [获取角色详情](0089-queries-role-details.md) | 调用本接口根据角色ID获取指定角色详情。 |
| [获取指定角色的员工列表](0095-obtain-the-list-of-employees-of-a-role.md) | 调用本接口获取指定角色的员工列表。 |

#### **外部联系人**

| **API** | **接口说明** |
| --- | --- |
| [添加外部联系人](0096-add-enterprise-external-contacts.md) | 调用本接口添加企业外部联系人。 |
| [删除外部联系人](0097-delete-external-contact.md) | 调用本接口删除企业外部联系人。 |
| [更新外部联系人](0098-update-enterprise-external-contacts.md) | 调用本接口更新企业外部联系人。 |
| [获取外部联系人列表](0099-obtain-the-external-contact-list.md) | 调用本接口获取企业外部联系人列表。 |
| [获取外部联系人标签列表](0100-obtains-a-list-of-external-contact-tags.md) | 调用本接口获取企业外部联系人的标签。 |
| [获取外部联系人详情](0101-obtains-the-external-contact-details-of-an-enterprise.md) | 调用本接口获取企业外部联系人的详细信息。 |

#### **企业管理**

| **API** | **接口说明** |
| --- | --- |
| [获取企业邀请信息](0124-obtain-invitation-information.md) | 调用本接口获取企业的邀请信息。 |
| [获取企业最新钉钉指数信息](0125-queries-the-latest-dingtalk-index-information.md) | 调用本接口获取企业最新钉钉指数信息。 |
| [获取企业认证信息](0123-obtain-enterprise-authentication-information.md) | 调用本接口获取企业认证信息。 |

#### **通讯录可见性管理**

| **API** | **接口说明** |
| --- | --- |
| [获取通讯录隐藏设置](0135-obtains-the-hide-settings-of-the-address-book.md) | 调用本接口批量获取通讯录隐藏的设置列表。 |
| [删除通讯录隐藏设置](0136-delete-hide-settings.md) | 调用本接口删除通讯录隐藏设置。 |
| [新增或更新通讯录隐藏设置](0138-update-address-book-hide-settings.md) | 调用本接口更新通讯录隐藏设置。 |
| [设置部门可见性优先级](0137-set-address-book-visibility-sub-department-settings-to-take-precedence.md) | 调用本接口设置通讯录部门可见性优先级。 |

## **智能人事清单**

| **API** | **接口说明** |
| --- | --- |
| [添加企业待入职员工](0955-add-employees-to-be-hired-through-intelligent-personnel.md) | 添加企业待入职员工。 |
| [获取待入职员工列表](0943-intelligent-personnel-query-the-list-of-employees-to-be-hired.md) | 查询企业待入职员工userid列表。 |
| [获取在职员工列表](0945-intelligent-personnel-query-the-list-of-on-the-job-employees-of-the.md) | 查询企业在职员工userid列表。 |
| [更新员工花名册信息](0939-intelligent-personnel-update-employee-file-information.md) | 更新员工档案信息，支持明细分组。 |
| [获取员工花名册字段信息](0938-api-getemployeerosterbyfield.md) | 查询员工花名册指定字段的信息，支持明细分组字段。 |
| [获取花名册元数据](0936-intelligent-personnel-roster-metadata-query.md) | 获取员工花名册的元数据，包括花名册分组、字段等。 |
| [批量获取员工离职信息](0948-obtain-resignation-information-of-employees-new-version.md) | 批量查询员工的离职信息，如离职人员的部门ID、离职主动原因和被动原因等。 |
| [智能人事员工调岗](0953-intelligent-personnel-staff-transfer.md) | 给智能人事员工调岗，支持以下内容调整，如员工部门列表、主部门、职务、职位和职级。 |
| [获取离职员工列表](0946-obtain-the-list-of-employees-who-have-left.md) | 查询企业离职员工userId列表。 |

## **钉钉客联清单**

| **API** | **接口说明** |
| --- | --- |
| [创建钉钉客联钉外账号](1844-create-bc-account-association.md) | 创建钉外用户账号，并建立与钉内用户的账号关联关系。 |
| [创建互通群](1843-create-an-intercommunication-group.md) | 创建钉钉客联互通群，群类型为普通群或跨钉两人群。 |
| [创建钉外两人群](1842-create-two-people-outside-the-nail.md) | 创建钉外两人群。 |
| [创建店铺群](1841-create-a-store-group.md) | 创建店铺群。 |
| [获取钉钉客联H5页面地址](1847-get-the-dingtalk-guest-group-session-address.md) | 获取钉钉客联群会话地址，钉外用户可通过该地址进入对应群内。 |
| [添加钉钉客联互通群成员](1850-add-a-group-member-1.md) | 向互通群内添加群成员。 |
| [查询钉钉客联互通群成员列表](1855-queries-the-group-member-list.md) | 查询互通群成员列表，包括普通群、跨钉两人群、钉外两人群和店铺群。 |
| [移除钉钉客联互通群成员](1851-remove-group-members.md) | 移除互通群成员。 |
| [修改钉钉客联互通群头像](1852-modify-the-avatar-of-a-communication-group.md) | 修改互通群头像，包括普通群、跨钉两人群、钉外两人群和商铺群。 |
| [修改钉钉客联互通群名称](1853-modify-the-group-name.md) | 修改群名称，包括普通群、跨钉两人群、钉外两人群和店铺群。 |
| [更换钉钉客联互通群群主](1854-change-group-owner.md) | 更换互通群的群主。 |
| [在钉钉客联互通群中使用钉外账号发送消息](1858-send-c2b-messages.md) | 实现钉外用户向钉内用户或互通群发送消息。 |
| [在钉钉客联互通群中使用钉内账号发送消息](1859-send-b2c-messages.md) | 实现钉内用户给钉外用户或者互通群发送消息。 |
| [在钉钉客联互通群中使用机器人发送消息](1857-group-robots-send-messages.md) | 通过互通群内机器人向群内发送消息。 |
| [查询钉钉客联钉外账号未读消息数](1849-querying-the-number-of-unread-messages-of-the-user.md) | 查询钉外用户未读消息的数量。 |
| [批量查询跨钉两人互通群列表](1848-queries-the-session-information-of-two-population-groups.md) | 根据群成员批量查询跨钉两人群列表。 |
| [解散钉钉客联互通群](1856-disband-bc-interconnection-group.md) | 解散互通群，包括普通群、跨钉两人群、钉外两人群和店铺群。 |

## 生态**清单**

### **阿里商旅**

| **API** | **接口说明** |
| --- | --- |
| [机票城市搜索](1011-air-ticket-city-search.md) | 搜索火车票城市。 |
| [火车票城市搜索](1012-train-ticket-city-search.md) | 搜索机票城市。 |
| [新建成本中心](1013-new-cost-center.md) | 新建成本中心。 |
| [修改成本中心](1014-modify-basic-cost-center-information.md) | 修改成本中心基本信息。 |
| [删除成本中心](1015-delete-cost-center.md) | 删除成本中心。 |
| [查询成本中心](1016-query-cost-center.md) | 查询成本中心信息。 |
| [设置成本中心人员信息](1017-set-up-cost-center-personnel-information.md) | 设置成本中心人员信息。 |
| [删除成本中心人员信息](1018-delete-the-personnel-information-of-the-cost-center.md) | 删除成本中心人员信息。 |
| [商旅成本中心转换为外部成本中心](1019-business-travel-cost-center-converted-to-external-cost-center.md) | 商旅成本中心转换为外部成本中心。 |
| [添加项目](1020-add-a-project.md) | 添加商旅项目。 |
| [修改项目](1021-project-change.md) | 修改项目信息。 |
| [删除项目](1022-delete-a-project.md) | 删除项目。 |
| [新建审批单](1023-user-new-approval-form.md) | 新建审批单。 |
| [获取申请单列表](1024-search-enterprise-approval-form-data.md) | 查询企业审批单数据。 |
| [获取申请单详情](1025-obtains-the-detailed-data-of-a-single-request.md) | 获取单个申请单的详细信息。 |
| [修改申请单](1026-user-modify-approval-form.md) | 修改出差申请单。 |
| [更新申请单状态](1027-update-approval-form.md) | 更新审批单状态。 |
| [搜索第三方酒店超标审批单](1028-dingtalk-oapi-alitrip-btrip-exceedapply-hotel-get.md) | 搜索第三方酒店超标审批单。 |
| [搜索第三方火车票超标审批单](1029-dingtalk-oapi-alitrip-btrip-exceedapply-train-get.md) | 搜索第三方火车票超标审批单。 |
| [回传第三方超标审批结果](1030-dingtalk-oapi-alitrip-btrip-exceedapply-sync.md) | 回传第三方超标审批结果。 |
| [搜索第三方机票超标审批单](1031-dingtalk-oapi-alitrip-btrip-exceedapply-flight.md) | 搜索第三方机票的超标审批单。 |
| [获取企业机票订单数据](1032-obtains-enterprise-ticket-order-data.md) | 获取企业机票订单数据 |
| [获取企业商旅酒店订单数据](1033-enterprises-obtain-order-data-for-business-hotels.md) | 获取商旅酒店订单数据。 |
| [获取企业火车票订单数据](1034-obtains-the-enterprise-train-ticket-order-data.md) | 获取企业火车票订单数据。 |
| [获取用车订单数据](1035-vehicle-order-query-interface.md) | 获取企业用车订单数据。 |
| [关联单号查询相关订单信息列表](1036-related-order-information.md) | 申请单中关联单号获取订单信息。 |
| [获取商旅访问地址](1037-obtain-business-travel-access-addresses.md) | 获取各个场景预订访问地址，以及我的订单地址。 |
| [新增发票配置](1038-new-invoice-configuration.md) | 新增发票配置。 |
| [配置发票适用人群](1039-configure-invoice-users.md) | 配置发票适用人群。 |
| [查询可用发票列表](1040-query-available-invoices.md) | 查询可用发票列表。 |
| [修改发票配置](1041-modify-invoice-configuration.md) | 修改发票配置。 |
| [删除发票信息](1042-delete-invoice-information.md) | 删除发票信息。 |
| [同步市内用车申请单](1043-synchronize-third-party-city-vehicle-approval-form.md) | 同步市内用车申请单。 |
| [审批市内用车申请单](1044-approval-of-third-party-city-car-application-form.md) | 审批市内用车申请单。 |
| [查询市内用车申请单](1045-query-the-application-form-for-third-party-vehicles-in-the-city.md) | 查询市内用车申请单。 |
| [查询用车结算记账记录](1046-query-interface-for-vehicle-settlement-and-bookkeeping.md) | 查询商旅用车的结算记账数据。 |
| [查询商旅火车票结算记账数据](1047-business-travel-train-ticket-settlement-bookkeeping-query-interface.md) | 查询商旅火车票结算记账数据。 |
| [查询酒店结算记账数据](1048-hotel-settlement-bookkeeping-query-interface.md) | 查询商旅酒店结算记账数据。 |
| [查询机票结算记账数据](1049-ticket-settlement-bookkeeping-query-interface.md) | 查询机票结算记账数据。 |
| [获取月对账结算数据](1050-obtain-monthly-reconciliation-settlement-data.md) | 获取月对账结算数据下载地址。 |
| [查询预估价](1051-query-estimated-price.md) | 查询预估价。 |

### **小蜜客服**

| **API** | **接口说明** |
| --- | --- |
| [智能问答](1825-alimebot-intelligent-q-a-interface.md) | 使用小蜜客服机器人的能力进行智能问答。 |
| [推送小蜜机器人单聊O2O消息](1827-push-xiaomi-customer-service-robot-single-chat-message.md) | 通过小蜜客服机器人发送O2O（即Online To Offline）线上线下消息。 |
| [小蜜客服机器人消息回复](1828-xiaomi-customer-service-robot-message-reply.md) | 根据小蜜客服机器人sessionId进行异步消息回复。 |
| [查询机器人基础指标数据](1829-query-robot-data-indicators.md) | 根据机器人ID查询某时间段机器人的基础指标数据。 |
| [获取用户登录凭证](1826-obtains-the-user-login-credential-of-the-third-party-system-of.md) | 获取用户的登录凭证。 |

### **智能客服**

| **API** | **接口说明** |
| --- | --- |
| [创建自助单](1002-create-a-self-service-ticket.md) | 创建用户自定义的自助单。 |
| [执行工单活动](1003-intelligent-customer-service-execute-work-order-activities.md) | 执行工单活动。 |
| [查询动作记录](1004-intelligent-customer-service-query-action-records.md) | 查询动作记录。 |
| [分页查询工单](1005-intelligent-customer-service-paging-query-work-order.md) | 分页查询工单。 |

### **员工服务台**

| **API** | **接口说明** |
| --- | --- |
| [使用服务助手推送消息](1822-the-message-pushing-interface-of-the-assistant.md) | 通过服务助手机器人给企业员工发送消息。 |

### **制造业**

| **API** | **接口说明** |
| --- | --- |
| [计件报工](1105-riqing-monthly-settlement-piece-rate-reporting-interface.md) | 用于MES系统上报计件数据到平台。 |
| [查询计件报工数据](1106-riqing-monthly-settlement-query-interface-for-piece-rate-reporting.md) | 查询计件报工的数据。 |

### **e签宝**

| **API** | **接口说明** |
| --- | --- |
| [e签宝数据初始化](1068-isv-service-provider-data-initialization.md) | 帮助钉钉企业进行e签宝开放平台的数据初始化。 |
| [获取授权的页面地址](1069-obtain-the-address-of-the-authorized-page.md) | 获取企业授权的页面地址。 |
| [取消企业授权](1070-cancel-enterprise-authorization.md) | 取消授权过企业的授权状态。 |
| [套餐转售—分润模式](1071-package-resale-1-distribution-mode.md) | 为使用电子合同的用户创建转售订单。 |
| [套餐转售—底价结算模式](1072-package-resale-2-reserve-price-settlement-mode.md) | 直接转售e签宝订单给最终真正使用电子合同的用户。 |
| [查询套餐余量](1073-query-package-balance.md) | 查询当前企业的套餐余量。 |
| [获取企业的e签宝微应用状态](1074-obtain-the-current-status-of-the-company-s-e-sign-micro-application.md) | 获取企业的e签宝微应用状态。 |
| [查询企业是否实名认证](1075-query-enterprise-information.md) | 查询企业是否已在e签宝完成实名认证。 |
| [获取企业控制台地址](1076-get-enterprise-console-address.md) | 获取的企业在e签宝的控制台地址。 |
| [查询个人是否实名认证](1077-query-personal-information.md) | 查询当前用户是否已在e签宝完成实名认证。 |
| [获取个人实名的地址](1078-obtain-the-address-that-is-redirected-to-the-user-s-real.md) | 通过个人信息接口查询到个人未实名时，可调用本接口获取个人实名认证地址。 |
| [获取跳转到企业实名的地址](1079-obtain-the-address-that-is-redirected-to-the-enterprise-s-real.md) | 通过企业信息接口查询到企业未实名时，可调用本接口获取实名地址，在应用内展示给企业。 |
| [获取文件上传地址](1082-obtain-the-upload-url-of-a-file-1.md) | 获取到文件上传地址。 |
| [获取文件详情](1081-gets-the-file-details.md) | 查询文件详情。 |
| [获取发起签署任务的地址](1086-obtain-the-address-used-to-initiate-a-signed-task.md) | 获取发起签署任务的地址。 |
| [创建签署流程](1083-use-the-api-to-initiate-a-signature-process.md) | 当ISV侧企业有文件需签署时，可调用本接口获取发起签署地址。 |
| [获取签署人签署地址](1084-get-signatory-address.md) | 获取签署人签署地址。 |
| [获取流程的签署详情](1085-get-the-details-of-process-signing.md) | 根据taskId获取流程签署相关的详细信息。 |
| [获取流程任务用印审批列表](1087-obtains-the-print-approval-list-for-process-tasks.md) | 获取流程任务用印审批列表。 |
| [获取流程详细信息及操作记录](1088-obtains-the-task-details.md) | 获取流程详细信息及操作记录。 |
| [获取流程任务的所有合同列表](1089-get-a-list-of-all-contracts-for-the-process-task.md) | 获取流程任务的所有合同列表，收到签署完成消息后查询。 |

### 金智CRM

| **API** | **接口说明** |
| --- | --- |
| [客户资料](1054-add-or-edit-customer-profile.md) | 新增或编辑客户资料。 |
| [客户公共池](1055-add-or-edit-customer-public-pools.md) | 新增或编辑客户公共池。 |
| [联系人](1056-add-or-edit-contacts.md) | 新增或编辑联系人。 |
| [合同订单](1057-add-or-edit-contract-orders.md) | 新增或编辑合同订单。 |
| [发货单](1058-add-or-edit-invoices.md) | 新增或编辑发货单。 |
| [销售换货单](1059-add-or-edit-a-sales-order.md) | 新增或编辑销售换货单。 |
| [销售机会](https://open.dingtalk.com/document/development/add-or-edit-opportunities) | 新增或编辑销售机会。 |
| [报价记录](https://open.dingtalk.com/document/development/add-or-edit-quotation-records) | 新增或编辑报价记录。 |
| [采购单](1060-edit-purchase-order.md) | 新增或编辑采购单。 |
| [生产单](1061-add-or-edit-a-production-order.md) | 新增或编辑生产单。 |
| [产品信息](1062-add-or-edit-product-information.md) | 新增或编辑产品信息。 |
| [入库单](1063-add-or-edit-a-shipment-record.md) | 新增或编辑入库单。 |
| [出库单](1064-add-or-edit-an-issue-ticket.md) | 新增或编辑出库单。 |
| [获取数据列表](1066-obtain-the-data-list.md) | 获取各种单据的列表数据。 |
| [获取数据详情](1065-queries-data-details.md) | 获取各种单据的详情数据。 |

### 氚云

| **API** | **接口说明** |
| --- | --- |
| [获取应用列表](1802-queries-applications.md) | 查询氚云的应用信息。 |
| [获取应用功能节点](1803-queries-the-application-feature-nodes.md) | 获取应用的功能节点信息。 |
| [获取组织数据](1804-queries-organization-data.md) | 获取组织部门数据信息。 |
| [获取用户数据](1805-obtain-user-data.md) | 获取用户基础数据信息。 |
| [获取角色数据](1806-obtain-role-data.md) | 获取角色组、角色数据等信息。 |
| [获取角色用户数据](1807-historical-acquisition-of-role-user-data.md) | 获取指定角色包含的用户。 |
| [获取表单对象结构](1808-gets-the-form-object-structure.md) | 获取表单对象结构信息。 |
| [创建表单业务数据](1809-create-form-business-data.md) | 创建单条表单、流程表单的业务数据对象。 |
| [查询表单业务数据列表](1810-querying-form-business-data.md) | 查询表单业务数据实例集合。 |
| [修改表单业务对象数据](1811-modify-form-business-object-data.md) | 修改表单的单条业务实例数据。 |
| [批量新增表单业务数据](1812-batch-add-form-business-data.md) | 批量新增表单的业务实例数据。 |
| [删除业务对象](1813-delete-a-business-object.md) | 批量新增表单的业务实例数据。 |
| [获取业务实例信息](1814-queries-business-instance-information.md) | 获取表单的单条业务实例数据。 |
| [创建流程实例](1815-create-a-process-instance.md) | 创建流程表单的流程实例数据。 |
| [删除流程实例数据](1816-delete-process-instance-data.md) | 流程表单的单条流程实例数据。 |
| [取消流程实例](1817-cancel-a-process-instance.md) | 取消流程实例，取消后的流程实例状态为已取消。 |
| [查询流程实例](1818-query-flow-instances.md) | 查询流程表单的流程实例数据。 |
| [查询流程实例节点工作项](1819-query-flow-instance-node-work-items.md) | 获取流程实例节点工作项的相关信息。 |
| [获取附件临时免登地址](1820-obtain-the-temporary-attachment-free-address.md) | 获取附件临时免登的访问地址。 |
| [获取文件上传地址](1821-obtain-the-upload-url-of-a-file-2.md) | 返回表单中指定图片、附件等控件的文件上传地址。 |
