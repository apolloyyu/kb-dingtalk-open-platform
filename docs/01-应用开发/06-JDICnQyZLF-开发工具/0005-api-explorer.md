---
title: "服务端API调试工具"
source_url: "https://open.dingtalk.com/document/download/api-explorer"
namespace: "download"
slug: "api-explorer"
group: "应用开发"
tab: "开发工具"
breadcrumb: "开发者工具 > 服务端API开发工具 > 服务端API调试工具"
doc_id: "mpXM6nbtST"
updated_at: "2026-01-16 18:20:12"
---

> Source: https://open.dingtalk.com/document/download/api-explorer
> Path: 应用开发 / 开发工具 / 开发者工具 > 服务端API开发工具 > 服务端API调试工具
> Updated: 2026-01-16 18:20:12

# 服务端API调试工具

## **介绍**

API 调试台是钉钉平台提供的可视化API在线调试工具，支持企业内部应用及第三方企业应用接口的在线调试服务。其核心功能包括API总览、快速检索、开发文档查阅、可视化调试界面，以及调试过程中同步生成可执行的SDK示例代码，以模块化设计实现高效开发支持，兼具功能全面性与操作便捷性。

## **功能说明**

为方便开发者能快速调试，钉钉开放平台提供了两种调试方式，开发者可根据实际情况自行选择：

### **方式一：文档左侧打开调试台**

通过接口文档右侧的“展开调试”功能，打开调试工具：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022900.png)

点击右侧“**展开调试**”功能，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022903.png)

- **文档区域（图示中①）**：用于展示每一篇文档内容及相关接口信息。
- **接口调试区域（图示中②）**：接口调试区域，可参照接口文档快速调试相关接口。

在调试区域内，我们提供了三种快捷方式，相比老版本的调试工具更快捷、更简单：

#### **功能一：API调试台**

API 调试台主要用于接口的调试，在该区域内，具有获取凭证、设置接口请求体、查看接口调试结果的功能。接口调试成功后，也可以通过复制功能复制调试结果。

> **[!NOTE]**
>
> 在接口正式调试前，需要申请相关权限。

#### **功能二：权限配置**

在旧版中，调用接口都需要申请应用的权限后才可进行调试。改版后，当调用某接口时，若没有接口的调用权限，则会提示申请权限的相关提示，在界面中可直接进行申请且已经申请权限后，二次调试无需申请。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022919.png)

#### **功能三：示例代码**

接口调用成功后，调试台的参数会自动生成示例代码，开发者可以直接复制不同语言的示例到自己的项目工程内，目前官方提供了多种类型代码，开发者可自行选择。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8555322671/p1022928.png)

### **方式二：API 调试台调试接口**

通过访问API 调试台，进入调试台主界面：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022931.png)

调试台主界面左侧菜单栏包含了钉钉所有开放API类目，并集成了API总览、快速检索的功能，开发者能够根据接口文档的名称， 通过搜索（如：搜索/user/get、获取用户详情 等）快速定位接口位置；中间是接口的调试区域，右侧也为开发者提供了三个功能：

#### **功能一：示例代码**

接口调用成功后，可同步动态生成对应的SDK示例代码，开发者可以直接复制不同语言的示例到自己的项目工程内直接运行，目前官方提供了多种不同类型代码，开发者可自行选择。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8555322671/p1022936.png)

#### **功能二：调试结果**

用于查看接口的返回结果。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022940.png)

#### **功能三：查看文档**

该功能用于开发者快速定位当前接口的源文档内容，在接口调试过程中，方便开发者进行比对参数及参数说明。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022942.png)

## **使用教程**

本文以上述方式一为例，使用API调试工具通过企业内部应用并调用[查询用户详情](../02-4a8AMF6u2A-服务端-API/0056-query-user-details.md)接口获取用户详情：

> **[!IMPORTANT]**
>
> 发起API调用将对当前登录企业的企业数据发起线上调用，请认真确认后操作。

1. 访问钉钉官网并打开[查询用户详情](../02-4a8AMF6u2A-服务端-API/0056-query-user-details.md)接口文档。
2. 点击接口文档右侧“**打开调试**”功能，展开调试工作台。

   > **[!NOTE]**
   >
   > 正式开始前，请提前登录开发者后台。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022958.png)
3. 通过应用切换功能，切换至目标应用。若当前没有应用，我们提供了快速创建的功能，在切换应用界面点击右下角**创建应用**功能，即可快速创建一个新的应用。

   > **[!IMPORTANT]**
   >
   > 企业内部应用列表按照角色权限查询：
   >
   > - **普通成员**：仅可查看自己创建或参与协作的应用（应用成员管理里当前成员为拥有者/管理者/开发者）。
   > - **子管理员或拥有全局应用管理权限的主管理员**：查看当前组织的所有应用。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7246992671/p1025883.png)
4. 查看接口是否具有权限，如果没有权限，在权限配置后会做红色**!**提示，并提示当前应用未开通调用该接口的必要权限。

   > **[!NOTE]**
   >
   > 若提示接口没有权限，可点击接口后的**申请权限**功能进行申请，申请成功后即可调用该接口。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8555322671/p1022990.png)
5. 点击**获取Token**按钮获取最新的Token，并在**请求体Body**中填写相关参数，最后单击**发起调试**。

   > **[!NOTE]**
   >
   > - 应用每次获取Token后有效期为2小时，超时后可通过**刷新Token**重新获取。
   > - 接口调试时避免频繁点击发起调试，否则会触发限流机制，影响接口调用稳定性。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8555322671/p1022974.png)

   第三方企业应用会根据接口区分Token是应用身份获取访问凭证Token，或用户身份获取访问凭证Token，如果是用户身份访问则代表当前接口不支持在线调试。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7246992671/p1025946.png)
6. 在调试结果中，查看接口的返回数据。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7555322671/p1022981.png)
