---
title: "OA审批场景接入子流程"
source_url: "https://open.dingtalk.com/document/connection/oa-approval-integration"
namespace: "connection"
slug: "oa-approval-integration"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 使用教程 > OA审批 > 操作手册 > OA审批场景接入子流程"
doc_id: "ZO4W74CNCL"
updated_at: "2026-01-22 21:27:45"
---

> Source: https://open.dingtalk.com/document/connection/oa-approval-integration
> Path: 连接平台 / 连接器中心 / 官方连接器 > 使用教程 > OA审批 > 操作手册 > OA审批场景接入子流程
> Updated: 2026-01-22 21:27:45

# OA审批场景接入子流程

本教程主要介绍在OA审批场景下如何接入连接平台子流程。

## **教程说明**

本教程通过在OA审批场景下接入，实现OA审批表单中选择员工姓名后，自动填充需要的员工职级信息。

> **[!NOTE]**
>
> 本教程接入的子流程中配置的执行动作为官方连接器下的执行动作，如子流程需配置自建连接器下的执行动作，详情请参考[创建连接器](../02-XdgyZifJkr-我的连接/0010-create-connector.md)、[添加触发事件](../02-XdgyZifJkr-我的连接/0011-add-trigger-event-1.md)、[添加执行动作](../02-XdgyZifJkr-我的连接/0012-add-execution-action-1.md)和[创建连接流](../02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)。

**OA审批接入子流程的作用**：

- 当前OA审批场景下不支持对执行动作出参进行重新定义，可以在连接平台侧通过子流程的方式对执行动作出参进行重新定义，OA审批场景下直接引用子流程即可。
- 多个执行动作聚合后的能力更加易用，例如先查询OA审批表单详情，再更新，两个动作合并后，通过子流程的方式被业务流集成，更简单。

## **前提条件**

在开始本教程前，确保你已经完成了以下准备工作：

- 已经完成了钉钉开发者的注册与激活并拥有了子管理员和开发者权限。若尚未完成，请参考[成为钉钉开发者](https://open.dingtalk.com/document/dingstart/dingtalk-developer)。
- 已开通钉钉专业版（OA审批中使用连接器必备）。若尚未完成，请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。
- 创建一个企业H5微应用并获取应用的AgentId，如何创建可参考[创建企业内部应用](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0861-create-an-h5-application-for-your-enterprise.md)。

## **审批场景**

### **场景痛点**

OA审批场景下不支持编排和表达式，无法对官方或三方连接器的返回结果进行改造，使得返回结果含职级以外的符号[" "]，不是所需要的职级内容信息。

例如：获取智能人事员工花名册中岗位职级信息，返回结果是["P7"]。

![OA审批接入集成流-痛点场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0720019661/p522693.png)

### **解决方案**

在连接平台通过子流程方式，对官方或三方连接器的执行动作出参进行改造，OA审批场景下直接引用发布后的子流程，解决智能人事中获取花名册单字段返回值含[" "] 问题，使得显示结果仅展示所需职级内容信息。

例如：获取智能人事员工花名册中岗位职级信息，返回结果是P7。

![OA审批接入集成流-解决方案场景图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0720019661/p522696.png)

## **子流程实例**

### **创建子流程**

> **[!NOTE]**
>
> 子流程如何创建及调试，详情请参考[创建连接流](../02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)。

### **配置子流程入参**

设置子流程入参，添加查询花名册信息所需要的**agentId**和**userId**参数。

![OA审批接入集成流-配置集成流入参](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506146.png)

### **配置子流程执行动作**

1. 在右侧依次选择**官方 > 智能人事 > 获取员工花名册字段信息**，并单击**设置**按钮。

   ![OA审批接入集成流-选择智能人事连接器](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506147.png)
2. 在入参映射设置界面中，将**上文节点出参**参数映射给**本节点入参**参数，单击**确定**并**保存**。

   ![OA审批接入集成流-入参映射设置](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506148.png)

   - **需要获取的花名册字段信息**：选择**固定值**，并设置为**sys01-positionLevel**，更多字段信息，请参考[花名册自定义字段业务code](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0943-roster-custom-field-business-code.md)。

### **配置子流程出参**

1. 设置子流程出参，添加**level**出参参数**。**

   > **[!NOTE]**
   >
   > 官方智能人事连接器，字段值列表格式为Array<Object>，具体字段取值为String，因此字段值展示为["XXX"]，此处对出参参数进行改造，设置为String类型。

   ![OA审批接入集成流-配置集成流出参参数](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506149.png)
2. 在出参映射设置界面**本节点入参**下，选择**表达式**。

   ![OA审批接入集成流-选择表达式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506151.png)
3. 在**公式编辑**界面，根据需求自定义表达式内容。

   > **[!NOTE]**
   >
   > 获取数组第一个元素，表达式如何使用，请参考[表达式](../02-XdgyZifJkr-我的连接/0008-expression-overview.md)。

   ![OA审批接入集成流-编辑表达式](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506152.png)

## **OA审批实例**

### **创建OA审批表单**

1. 登录[钉钉管理后台](https://oa.dingtalk.com/#/welcome)，依次选择**工作台 > 应用管理** ，然后单击**OA审批**。

   ![OA审批接入集成流-选择OA审批](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506153.png)
2. 单击**创建新表单**，然后选择**流程表单**。

   ![OA审批接入集成流-选择流程表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506155.png)
3. 在**基础设置**界面，填写基本信息包括表单名称和所在分组。

   ![OA审批接入集成流-填写表单名称](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506156.png)

### **设置触发事件**

1. 在**表单设计**界面，设计并添加OA审批表单控件后，依次选择**连接器 > 配置连接器**。

   ![OA审批接入集成流-设置触发事件-选择连接器](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506158.png)

   - **员工姓名**：选择**联系人**增强控件。
   - **员工职级**：选择**单行输入框**基础控件。
2. 在**配置连接器**模块的**设置触发条件**下，选择**控件值发生变化时**，绑定触发事件的控件并**确定**，单击**下一步**。

   ![OA审批接入集成流-设置触发事件-选择控件发生变化时](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506160.png)

   - **新建表单加载时**：当打开表单时触发，可以通过接口自动给某些表单控件赋值。
   - **控件值发生变化时**：当表单中某些控件值发生变化后调用接口，自动给其他表单控件赋值。
   - **表单提交（含发起人重新提交）时验证**：当单击提交按钮时，通过接口对数据进行校验，如不通过则阻断用户发起审批。

### **绑定连接器**

1. 在**配置连接器**模块的**选择连接器**下，依次选择**子流程（原集成流） > 查询员工花名册信息**，然后单击**下一步**。

   > **[!NOTE]**
   >
   > 此处的**查询员工花名册信息**为自定义集成流名称，创建的集成流都统一归到**集成流**分组中。

   ![OA审批接入集成流-绑定连接器-选择集成流](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506161.png)

### **配置执行动作**

1. 设置**员工id**，选择下拉菜单，绑定**员工姓名ID**。

   ![OA审批接入集成流-配置执行动作-绑定员工姓名ID](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506164.png)
2. 设置**微应用在企业的agentId**，依次选择**设置 > 自定义**，填写获取的H5微应用AgentId值。

   > **[!NOTE]**
   >
   > AgentId如何获取，详情请参考[创建企业内部应用](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0861-create-an-h5-application-for-your-enterprise.md)。

   ![OA审批接入集成流-配置执行动作-自定义企业agentId](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506165.png)
3. 设置**获取的数据填充到以下控件**，选择**添加**，将**字段取值**填充到**员工职级**，并单击**保存**。

   ![OA审批接入集成流-配置执行动作-填充岗位职级](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506166.png)
4. 单击**发布**按钮，发布成功，如下图所示：

   ![OA审批接入集成流-发布](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506167.png)

## **实例效果**

1. 进入钉钉**工作台**，然后进入**OA审批**，找到**创建OA审批表单实例**中已创建的审批表单。

   ![OA审批接入集成流-实例效果-找到创建的表单](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506169.png)
2. 在发起审批界面，选择**员工姓名**后，会自动填充**员工职级**信息，如下图所示：

   > **[!NOTE]**
   >
   > 如果选择员工姓名后无法自动获取员工职级字段值或字段为“null”，请确认以下内容：
   >
   > - 进入[**钉钉管理后台**](https://oa.dingtalk.com/#/welcome)，依次选择**通讯录 > 智能人事** > **花名册**，然后确认查询员工的岗位职级信息是否有值。
   > - 确认在**OA审批实例**的**配置执行动作**下，**填写以下控件的值获取数据**和**获取的数据值填充到以下控件**的配置是否正确。

   ![OA审批接入集成流-实例效果-效果图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9531716661/p506172.png)
