---
title: "钉钉账号绑定阿里云账号"
source_url: "https://open.dingtalk.com/document/dingstart/bind-a-dingtalk-account-to-an-alibaba-cloud-account"
namespace: "dingstart"
slug: "bind-a-dingtalk-account-to-an-alibaba-cloud-account"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发指南 > 三方应用部署 > 钉钉账号绑定阿里云账号"
doc_id: "cFoBe1kqQf"
updated_at: "2026-01-22 20:01:27"
---

> Source: https://open.dingtalk.com/document/dingstart/bind-a-dingtalk-account-to-an-alibaba-cloud-account
> Path: 应用开发 / 开发指南 / 开发指南 > 三方应用部署 > 钉钉账号绑定阿里云账号
> Updated: 2026-01-22 20:01:27

# 钉钉账号绑定阿里云账号

本文档指导企业组织管理员如何将钉钉账号与阿里云账号进行关联，实现统一身份管理与应用部署权限的集成。本功能适用于需要在钉钉开放平台开发第三方企业应用，并通过阿里云资源进行部署和运维的场景。

## 适用对象

- 本功能主要面向**第三方企业应用**的开发者及组织管理员。
- 操作者必须具备**组织管理员**权限，方可执行绑定操作。

## 前置条件

在开始绑定前，请确保满足以下条件：

1. 当前登录账号为该钉钉组织的**组织管理员**；
2. 所属企业已完成**企业实名认证**；
3. 已在阿里云官网注册账号，并可使用钉钉扫码方式完成第三方账号绑定；

## **操作步骤**

1. 登录[开发者后台](https://open-dev.dingtalk.com/)，单击**更多** > **阿里云** > **关联阿里云账号**。
2. 根据是否已关联阿里云账号，执行对应操作：

   - **如果已关联阿里云账号，**你可以直接选择检测到的阿里云账号并单击**确认**。

     ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9569473071/p752235.png)
   - **如果未关联阿里云账号**，显示“***请先用该钉钉账号，去阿里云官网，并通过钉钉扫码进行绑定。绑定成功后，刷新此页以继续选择。***”，你需要：![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9569473071/p752228.png)

     1. 登录[阿里云账号](https://account.console.aliyun.com/v2/#/home/person)实现三方账号的绑定操作。

        ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9569473071/p752229.png)
     2. 绑定成功后，再次单击**关联阿里云账号**会显示检测到的阿里云账号，再单击**确认**，即可完成关联。

        ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9569473071/p752231.png)

## 使用说明

### 管理员绑定限制

- 仅支持组织管理员进行绑定操作。
- 一个钉钉组织下的管理员角色账号只能绑定一个阿里云主账号，可以设置不同的管理员角色账号绑定不同的阿里云账号。

### 主账号用途

被绑定的阿里云主账号将作为该组织的默认**应用部署账号**，用于后续发布和管理基于阿里云资源的应用服务。

### 子账号支持

在主账号绑定完成后，支持进一步配置RAM子账号，用于精细化的应用部署和权限管理。

### 常见问题

- **Q：非管理员能否绑定阿里云账号？**

  A：不可以。仅组织管理员具备此项操作权限。
- **Q：绑定失败怎么办？**

  A：请确认钉钉账号已在阿里云完成三方绑定，并尝试刷新页面。若仍无法检测到账号，请检查网络或联系技术支持。
- **Q：是否支持多主账号绑定？**

  A：不支持。一个组织仅允许绑定一个主账号，但可通过RAM子账号实现多用户协同管理。
