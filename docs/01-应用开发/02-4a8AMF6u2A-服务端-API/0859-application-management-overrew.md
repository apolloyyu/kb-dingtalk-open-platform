---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/application-management-overrew"
namespace: "development"
slug: "application-management-overrew"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 概述"
doc_id: "JpJhDg3nOv"
updated_at: "2026-07-24 09:16:39"
---

> Source: https://open.dingtalk.com/document/development/application-management-overrew
> Path: 应用开发 / 服务端 API / 钉钉应用 > 概述
> Updated: 2026-07-24 09:16:39

# 概述

本文档介绍了什么是应用管理，应用管理开放了哪些接口能力，以及如何接入应用管理接口能力等。

## 什么是应用管理

应用管理是钉钉提供的开放能力之一，用于获取企业内部应用的基础信息、对企业内部应用-H5微应用的管理，例如创建应用、删除应用、设置应用的可使用范围等。

## 开放概览

### 开放接口列表

应用管理提供了丰富的接口开放能力，开发者通过API接口可以实现应用管理和企业业务系统打通。

#### **应用管理**

| **API** | **说明** | **API版本** |
| --- | --- | --- |
| [创建企业内部应用](0861-create-an-h5-application-for-your-enterprise.md) | 创建企业内部应用信息。 | 新版 |
| [更新企业内部应用](0862-update-internal-h5-applications.md) | 更新企业内部应用信息。 | 新版 |
| [删除企业内部应用](0863-delete-an-internal-h5-application.md) | 删除H5微应用。 | 新版 |
| [获取企业所有应用列表](0864-obtains-a-list-of-all-enterprise-applications.md) | 获取企业所有的应用列表。 | 新版 |
| [获取企业内部所有应用列表](0865-get-a-list-of-all-applications-inside-the-enterprise.md) | 获取企业内部所有应用列表 | 新版 |
| [获取用户可见的企业应用列表](0866-obtains-the-list-of-enterprise-applications-visible-to-a-user.md) | 获取用户可使用的企业应用列表及应用信息。 | 新版 |

#### **版本管理**

| **API** | **说明** | **API版本** |
| --- | --- | --- |
| [发布企业内部小程序版本](0867-release-internal-applet-version.md) | 可以对企业内部小程序进行线上和体验版的发布。 | 新版 |
| [回滚企业内部小程序版本](0868-rollback-of-enterprise-internal-applet-version.md) | 回滚企业内部小程序版本。 | 新版 |
| [获取企业内部小程序的版本列表](0869-get-the-version-list-of-the-enterprise-internal-applet.md) | 获取企业内部小程序的版本列表 | 新版 |
| [获取企业内部小程序历史版本列表](0870-obtain-the-list-of-historical-versions-of-enterprise-internal-applets.md) | 获取企业内部小程序历史版本列表 | 新版 |

#### **使用范围**

| **API** | **说明** | **API版本** |
| --- | --- | --- |
| [更新企业内部应用的可使用范围](0871-update-the-visible-range-of-micro-applications.md) | 更新企业内部应用的可使用范围。 | 新版 |
| [获取企业内部应用的可使用范围](0872-obtains-the-application-visible-range.md) | 获取企业内部应用的可使用范围信息。 | 新版 |

#### **智能体**

| **API** | **说明** | **API版本** |
| --- | --- | --- |
| [创建企业智能体应用](0873-api-createagent.md) | 创建企业智能体应用。 | 新版 |
| [提交创建企业自建Agent](0874-api-submitcreateenterpriseagent.md) | 提交创建企业自建 Agent 任务。 | 新版 |
| [查询创建企业自建Agent任务进度](0875-api-querycreateenterpriseagent.md) | 根据任务ID获取任务进度信息。 | 新版 |

### **回调事件列表**

应用管理提供了小程序版本发布事件、小程序版本回滚事件、企业内部应用发布、企业内部应用状态变更等多个事件，更多信息可参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## 使用教程

钉钉提供了应用管理接口接入流程示例，请参见[应用的全生命周期管理](0860-application-management-workflow.md)。
