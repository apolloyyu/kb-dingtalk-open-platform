---
title: "应用使用敏感权限"
source_url: "https://open.dingtalk.com/document/development/use-sensitive-permissions"
namespace: "development"
slug: "use-sensitive-permissions"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "API 调用指南 > 申请 API 权限 > 应用使用敏感权限"
doc_id: "pROxoPXvvK"
updated_at: "2026-08-07 14:50:52"
---

> Source: https://open.dingtalk.com/document/development/use-sensitive-permissions
> Path: 应用开发 / 服务端 API / API 调用指南 > 申请 API 权限 > 应用使用敏感权限
> Updated: 2026-08-07 14:50:52

# 应用使用敏感权限

如果你的应用需要调用涉及组织核心数据的敏感接口（如通讯录写操作、多维表读写等），必须经过严格的权限授权流程。本文将系统介绍敏感权限的概念、开发者接入流程、管理员授权体验及常见问题处理，帮助你顺利完成敏感权限的管理。

## **概念介绍**

### **什么是敏感权限**

在钉钉开放平台中，部分权限因涉及企业核心数据或高风险操作，被定义为“敏感权限”。应用需单独申请并获得组织管理员明确授权后，方可调用相关 OpenAPI。

当前开放的主要敏感权限包括：

> **[!NOTE]**
>
> 只有具备指定角色的用户才能对敏感权限进行授权或解除授权操作。例如，“全组织通讯录管理员”是唯一可授权 `qyapi_manage_addresslist` 权限的角色。

| **权限点code** | **权限点介绍** | **可操作权限点角色** |
| --- | --- | --- |
| qyapi\_manage\_addresslist | 通讯录数据管理权限 | 全组织通讯录管理员 |
| Notable.Base.Write | 钉钉多维表写权限  **[!IMPORTANT]**  多维表权限点扩容中，暂不支持新增申请，特殊需求请联系产品团队。 | 钉钉文档（知识库）管理员 |
| Notable.Base.Read | 钉钉多维表读权限  **[!IMPORTANT]**  多维表权限点扩容中，暂不支持新增申请，特殊需求请联系产品团队。 | 钉钉文档（知识库）管理员 |

### **什么是全组织通讯录管理员**

`qyapi_manage_addresslist` 是用于调用通讯录写类接口的敏感权限点，其授权操作仅限于“全组织通讯录管理员”。

该角色需同时满足两个条件：

- 拥有通讯录基础管理权限
- 管理范围必须是全组织

【全组织通讯录管理员】查看路径：进入[OA后台](https://oa.dingtalk.com)，点击权限管理。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5884425171/p797095.png)

### 统一授权套件与 authCode 说明

- **统一授权套件**：是钉钉提供的标准化组织级授权解决方案，适用于第三方应用向客户组织请求敏感权限的场景。通过接入该套件，开发者可引导授权组织完成授权流程，并获取临时授权码（authCode）。
- **authCode**：即临时授权码，由钉钉在用户确认授权后返回，具有较短生命周期。开发者需使用此 code 调用 接口换取 `access_token`，进而调用受保护的 OpenAPI。

## **开发者体验**

### **应用开发态关联权限点**

> 本文以敏感权限点`qyapi_manage_addresslist`为例。

你首先需要在开发者后台，把敏感权限点`qyapi_manage_addresslist`关联到应用上，这样应用才可以调用敏感权限下的 OpenAPI —— 设定角色成员管理范围。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p797100.png)

如果你在开发者后台没有敏感权限点`qyapi_manage_addresslist`，你需要联系[技术支持](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)，说明你的业务需求，评估通过后，平台会为你的开发者组织开放敏感权限。

> 权限申请后，开发者需要再接入[钉钉统一授权套件](0007-function-description.md)，触达授权组织管理员，让授权组织管理员进行授权。否则调用接口将会显示 403。

### **应用调用 OpenAPI**

使用 `access_token` 调用目标 OpenAPI（如创建部门、更新成员等），返回 HTTP 200 表示调用成功。这里的开发者体验和使用普通权限点是一致的。

## **组织管理员体验**

### **应用开通授权**

- 普通权限在应用开通时就会由管理员授予应用；
- 敏感权限不会随应用开通而生效，必须由具备相应角色的管理员进入工作台手动完成授权。

### 工作台授权

#### **在钉钉客户端授权**

以移动端为例：

1. 点击工作台右上角的【齿轮】进入企业管理。然后点击【应用&模板】进入应用管理。找到想要管理的应用，点击【设置】，进入该应用的管理页。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p797114.png)
2. 管理员可以看到授权管理中有待授权的红点，点击进入。你可以看到待授权的敏感权限清单，和应用开通时已经授予的基础权限清单。你可以在外层直接点击授权，也可以进入敏感权限清单，进行单个权限授权。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5884425171/p797115.png)
3. 授权相关操作：

   - 单击**授权** > **允许**，即可完成授权操作。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p798588.png)

     如果你不是全组织通讯录管理员，下方窗口会让你选择处理人，点击联系管理员，就会发单聊消息卡片给到全组织通讯录管理员。

     | **用户向全组织通讯录管理员发送授权申请** | **全组织通讯录管理员看到的授权消息卡片** |
     | --- | --- |
     | image | image |
   - 如果你需要解除授权，你可以单击解除授权并确定，即可解除成功。

     ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p798590.png)

     > 目前只支持敏感权限的解除授权。

#### **在钉钉管理后台授权**

1. 组织或通讯录管理员角色登录[钉钉管理后台](https://open.dingtalk.com/document/development/www.oa.dingtalk.com)，在【工作台】的【应用管理】下搜索需要授权的应用名称，找到对应需要授权的应用，点击【设置】进入应用的管理页面。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5884425171/p797150.png)
2. 在【应用权限】下有【查看】和【更新授权】等授权管理相关的操作。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p797152.png)

### 在OA后台查看审计日志

你可以在组织的OA后台查看组织对敏感权限的操作，包括“同意应用获取权限”和“撤回同意应用获取的权限”。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p798591.png)

## **常见问题**

- **应用调用 OpenAPI，返回了403，应该如何解决？**

  可能原因及解决方案如下：

  确认开发者后台是否已正确申请所需接口权限。

  - 首先确认开发者后台是否申请接口权限。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4079592871/p797100.png)
  - 检查是否已完成组织侧授权:

    - 引导授权组织管理员前往工作台完成手动授权；
    - 或接入[统一授权套件 SDK](0010-unified-licensing-suite-sdk.md)，实现自动化授权流程。

  调用 OpenAPI 返回 403 时，说明应用的授权组织没有授予权限给应用或者组织解除了原来授予给应用的权限。
- **授权组件的接入需要开发时间，如果开发者来不及接入授权组件怎么办？有没有解决403问题的什么临时方案？**

  答：三方应用开发者可以引导**授权组织管理员**到工作台完成手动授权。
