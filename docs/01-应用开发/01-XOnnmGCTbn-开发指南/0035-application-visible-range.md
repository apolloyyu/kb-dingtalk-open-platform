---
title: "体验网页应用"
source_url: "https://open.dingtalk.com/document/dingstart/application-visible-range"
namespace: "dingstart"
slug: "application-visible-range"
group: "应用开发"
tab: "开发指南"
breadcrumb: "开发网页应用 > 体验网页应用"
doc_id: "AuC6XHUrR5"
updated_at: "2026-06-30 09:00:37"
---

> Source: https://open.dingtalk.com/document/dingstart/application-visible-range
> Path: 应用开发 / 开发指南 / 开发网页应用 > 体验网页应用
> Updated: 2026-06-30 09:00:37

# 体验网页应用

本文可以帮助你了解什么是应用的可使用范围、可使用范围的设置类型、如何设置可使用范围，以及如何在工作台添加并使用应用。

## **本文适用范围**

- 企业管理员：希望了解什么是应用的可使用范围、如何修改应用的可使用范围，以及如何在工作台添加并使用应用。
- 新手开发者：希望了解什么是应用的可使用范围、如何修改应用的可使用范围，以及如何在工作台添加并使用应用。
- 正在开发应用的开发者：希望了解如何设置应用的可使用范围，以及如何在工作台添加并使用应用。

## **可使用范围**

### **什么是可使用范围**

应用的可使用范围，指企业下哪些员工可以使用该应用，不在可使用范围内的员工无法使用。本文后续简称为可使用范围。

> **[!NOTE]**
>
> 每个应用都有可使用范围，不同的应用可以被设置不同的可使用范围。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p508225.png)

应用的可使用范围设置有三种类型。

| 可使用范围设置类型 | 说明 |
| --- | --- |
| 全部员工 | 企业下所有员工都可以使用该应用。 |
| 部分员工 | 企业下部分员工可以使用该应用，可以同时添加部门、员工。  例如，部分员工添加小钉和财务部门，小钉和财务部门下的员工可以使该应用，其他员工无法使用。 |
| 仅限管理员 | 企业的管理员，包括主管理员和管理组成员都可以使用该应用。  例如，小钉是企业的主管理员，小张在“财务管理”管理组，小钉和小张可以使用该应用，其他普通员工无法使用。 |

### **如何设置可使用范围**

应用的类型不同，设置可使用范围的平台不同。目前将应用分为基础应用、第三方应用、自建应用。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p508229.png)

- 基础应用

  一般为钉钉提供的官方应用，非企业自主开发的应用，在[钉钉管理后台 > 应用管理](https://oa.dingtalk.com/index.htm#/microApp/microAppList)页面，选中应用后，单击**设置**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p508246.png)

  在设置页面，修改可见范围，进行设置可使用范围。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p508248.png)
- 第三方应用

  一般为开通的产品服务商或钉钉提供的第三方企业应用，非企业自主开发的应用，在[钉钉管理后台 > 应用管理](https://oa.dingtalk.com/index.htm#/microApp/microAppList)页面，选中应用后，单击**设置**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p508250.png)

  在设置页面，修改可见范围，进行设置可使用范围。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p508284.png)
- 自建应用

  自建应用是企业自主开发的企业内部应用，在[钉钉开发者后台](https://open-dev.dingtalk.com/)设置可使用范围。

  > **[!NOTE]**
  >
  > 本文以创建企业内部应用为例介绍如何设置可使用范围。

### **需要设置应用可使用范围场景**

开发者或企业管理员在以下场景可能需要设置应用的可使用范围。

**场景一**：企业开发人员创建应用后，系统默认可使用范围类型是部分员工，且只有当前开发人员，即只有应用的创建人员可以使用该应用。如果希望企业其他的员工使用该应用，需要重新设置修改可使用范围。

**场景二**：应用已有可使用范围，需要修改已设置的可使用范围，比如需要新增或减少可使用员工等。

### **哪些人员可以设置应用的可使用范围**

在企业，同时具有以下权限的人员可以设置应用的可使用范围。

- 有权限登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。如无法登录，请查看[获取开发者权限](0006-get-developer-permissions.md)申请权限。
- 有对应应用的管理权限。

  - 对于企业内部应用，应用的创建者，默认有该应用的管理权限。
  - 如果不是应用的创建者，则需要通过[钉钉管理后台](https://oa.dingtalk.com/index.htm#/welcome) **> 安全与权限 > 权限管理**页面，单击**添加管理组**。添加如下图中公告的管理权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p508294.png)

## **流程说明**

本文以企业自主开发的企业内部应用为例介绍。

**步骤一**：登录[钉钉开发者后台](https://open-dev.dingtalk.com/)，单击[应用创建与配置](0007-create-application.md)所创建的企业内部应用。

**步骤二**：设置企业内部应用的可使用范围，可以任选以下一种设置类型。

- 方式一：设置部分人员可使用应用。
- 方式二：设置仅限管理员。
- 方式三：设置企业全部成员可使用应用。

**步骤三**：在工作台添加并使用应用。

## **准备工作**

在开始设置应用的可使用范围前，确保你已经完成[获取开发者权限](0006-get-developer-permissions.md)。

## 步骤一：打开应用

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。

   > **[!NOTE]**
   >
   > 只有管理员和管理组成员可登录开发者后台，详情请参考[获取开发者权限](0006-get-developer-permissions.md)。
2. 单击**应用开发 > 企业内部开发 > 钉钉应用**，找到需要设置可使用范围的应用。例如创建的应用为**测试H5微应用**。

   > **[!NOTE]**
   >
   > 如何创建企业内部应用**测试H5微应用**，请参考文档[应用创建与配置](0007-create-application.md)。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p508297.png)
3. 单击**版本管理与发布 > 创建新版本**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p508298.png)

## 步骤二：设置应用的可使用范围。

分别介绍3种设置方式，可以任选以下一种方式。

- **方式一**：设置部分员工。
- **方式二**：设置仅限管理员。
- **方式三**：设置全部员工。

### 方式一：设置部分员工

在版本管理与发布页面，选择**部分员工**，同时设置员工或者部门，单击**保存**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p508891.png)

### 方式二：设置仅限管理员

在版本管理与发布页面，选择**仅限管理员**，并单击**保存**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p508897.png)

### 方式三：设置全部员工

在版本管理与发布页面，选择**全部员工**，并单击**保存**。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p508898.png)

## 步骤三：添加应用到工作台

企业员工在工作台找到应用并使用，已创建的企业内部应用需要手动添加到工作台，才可以在工作台展示，员工才能在工作台使用该应用。如果应用已同时设置了移动端首页地址、PC端首页地址，可以通过移动端或者PC端任一端工作台添加。钉钉官方提供的工作台，有我的、全员应用列表。

> **[!NOTE]**
>
> 本文以应用同时设置了移动端首页地址、PC端首页地址为例介绍。如何设置首页地址请查看[应用创建与配置](0007-create-application.md)。

### 添加应用到工作台-我的

员工可以通过**工作台-我的**管理自己常用的应用列表。

> **[!NOTE]**
>
> - 哪些成员可以管理应用：只有自己能管理“我的”应用列表。
> - 哪些成员可以看到应用：每个成员只能看到自己管理的“我的”应用列表。

通过移动端添加：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p509178.png)

通过PC端添加：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p509185.png)

### 添加应用到工作台-全员

用于管理企业员工可以看到的应用列表。

> **[!NOTE]**
>
> - 哪些成员可以管理应用：[钉钉管理后台](https://oa.dingtalk.com/) **> 安全与权限 > 权限管理**，具有工作台管理权限的成员，可以管理在“全员”列表的应用。如无可以联系企业主管理员申请。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p509199.png)
> - 哪些成员可以看到应用：成员有应用的可使用范围，在“全员”列表可以看到对应的应用。

通过移动端添加：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7321872871/p509250.png)

通过PC端添加：![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4373927661/p509252.png)
