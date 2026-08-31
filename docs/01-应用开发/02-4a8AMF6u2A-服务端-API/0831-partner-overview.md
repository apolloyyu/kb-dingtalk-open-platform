---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/partner-overview"
namespace: "development"
slug: "partner-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 产业互联 > 概述"
doc_id: "km8jN8m209"
updated_at: "2026-05-15 18:21:27"
---

> Source: https://open.dingtalk.com/document/development/partner-overview
> Path: 应用开发 / 服务端 API / 专属钉钉 > 产业互联 > 概述
> Updated: 2026-05-15 18:21:27

# 概述

本文介绍了什么是产业互联，如何开通产业互联以及产业互联接口能力。

## 什么是产业互联

产业互联，为大型企业提供对合作伙伴的邀请、维护、沟通、运营、业务协作等管理能力和业务协同能力，帮助大型企业管理和运营企业的产业生态。![合作伙伴概述图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3171856561/p462034.png)

## 如何开通产业互联

### 开通上下游组织

企业先需要开通上下游组织功能，才能开通产业互联。

> **[!IMPORTANT]**
>
> - 只有创建该组织的主管理员有创建上下游组织的权限。
> - 开通上下游组织只能在钉钉移动端操作。

步骤一：打开钉钉移动端，单击**通讯录**，选择需要开通上下游组织的企业，单击**管理**。

步骤二：在企业管理页面，单击**上下游组织**。

步骤三：在上下游组织页面，单击**创建上下游组织**。

步骤四：在创建上下游组织页面，按照下列要求填写基本信息后，单击**确认并继续**。

- 上下游组织：请输入上下游组织名称。
- 所属行业：请选择上下游组织所属行业。
- LOGO：请上传上下游组织LOGO图片。
- 选择部门和成员：请添加本企业的部门和成员到上下游组织。

步骤五：上下游组织创建成功后，可分享链接或保存图片上的二维码邀请其他组织加入该上下游组织。

![iShot2022-06-30 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4171856561/p461922.png)

### 开通产业互联

专属钉钉企业开通上下游组织后，登录[企业管理后台](https://oa.dingtalk.com)会自动出现合作伙伴目录，如下图所示。

> **[!NOTE]**
>
> 产业互联目前仅支持专属钉钉企业开通，如何申请开通专属钉钉，请参考[专属钉钉开通流程](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/YQBnd5ExVEwmZPaeUdZL5D9N8yeZqMmz?spm=ding_open_doc.document.0.0.2db6d3945o8kBl)。

![iShot2022-06-30 14](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4171856561/p461959.png)

## 开放概览

产业互联提供了丰富的接口开放能力，开发者通过API接口可以实现批量进行产业互联相关功能的设置。

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
