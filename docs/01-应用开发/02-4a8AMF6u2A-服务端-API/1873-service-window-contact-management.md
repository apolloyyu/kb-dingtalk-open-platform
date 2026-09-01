---
title: "服务窗联系人管理"
source_url: "https://open.dingtalk.com/document/development/service-window-contact-management"
namespace: "development"
slug: "service-window-contact-management"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 服务窗联系人管理"
doc_id: "CRThzPVYKi"
updated_at: "2026-08-28 10:27:08"
---

> Source: https://open.dingtalk.com/document/development/service-window-contact-management
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 服务窗联系人管理
> Updated: 2026-08-28 10:27:08

# 服务窗联系人管理

本文介绍了如何通过接口获取服务窗联系人信息。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，客户管理的服务窗接口已升级。客户管理-服务窗API文档已于2022年11月30日移动至历史文档（不推荐）目录。新用户请关注和调用[服务窗](1277-customer-service-overview.md)接口。

## 获取服务窗联系人信息

服务窗联系人信息分为以下两类：

- 免登之后，无需用户授权即可获取的，例如联系人昵称和联系人userid。
- 属于联系人敏感信息，包括联系人手机号和所在企业名称，这些信息在获取时需要先获得用户授权才可以调用接口获取。

### 获取联系人基础信息

自建服务窗应用免登之后，可以通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取用户详情。免登可参考[网页应用（H5微应用）免登](0018-enterprise-internal-application-logon-free.md)。

### 获取联系人手机号、企业名称等信息

联系人手机号和所在企业名称属于用户敏感信息，获取时需要先获得用户授权。可通过以下步骤获取授权数据：

1. 获取联系人授权

   服务窗用户授权通过调用前端jsapi实现，详情请参考[获取用户授权](../03-Ogu5SlPY4t-客户端-JSAPI/0711-obtain-user-auth-data.md)接口。
2. 调用接口获取授权数据

   可调用调用[获取服务窗联系人信息](1874-obtains-the-contact-information-of-the-service-window.md)接口获取授权之后的手机号和企业名称等数据。

## 获取全量已关注服务窗的联系人信息

自建服务窗应用首次启用时，可以使用[批量获取服务窗联系人数据](1875-obtain-contact-data-from-the-service-window.md)接口全量同步历史联系人数据。

增量联系人数据请通过监听关注、取消关注事件回调获取，而不是频繁调用该接口来进行同步，事件回调请参考[服务窗关注与取消回调](1876-callback-event-for-service-window-following-and-cancellation.md)。
