---
title: "同意或拒绝审批流程"
source_url: "https://open.dingtalk.com/document/development/approve-or-reject-the-new-version"
namespace: "development"
slug: "approve-or-reject-the-new-version"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 官方OA 审批 > 同意或拒绝审批流程"
doc_id: "cuimEOJGTR"
updated_at: "2026-07-10 10:11:32"
---

> Source: https://open.dingtalk.com/document/development/approve-or-reject-the-new-version
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 官方OA 审批 > 同意或拒绝审批流程
> Updated: 2026-07-10 10:11:32

# 同意或拒绝审批流程

本文介绍了官方OA审批如何发起及操作审批流程。

## 预期效果

- 同意审批节点

  ![0817同意审批](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5047070661/p478193.png)
- 拒绝审批节点

  ![0817拒绝审批节点](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5047070661/p478197.png)

## 接入流程简介

本文档展示了，创建一个企业内部应用，使用**官方OA审批**实现发起审批、操作审批等流程：

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。
2. 根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0497-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。

   > **[!NOTE]**
   >
   > 若无保存审批实例`instanceId`，可通过调用新版服务端API-[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取发起实例时间段的审批实例`instanceId`。
3. 根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情，获取审批任务各个任务节点信息`taskId`。
4. 根据审批实例`instanceId`和相应的任务节点`taskId`信息，调用新版服务端API-[同意或拒绝审批任务](0506-approve-or-reject-the-approval-task.md)，实现审批任务的操作，所有审批节点同意后，则该审批单通过。该步骤不支持第三方企业应用。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`Workflow.Form.Write`、`Workflow.Instance.Write`和`Workflow.Instance.Read`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

```
 public void getAccessToken() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest accessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("din*********hgn")
                .setAppSecret("9G_O************mBkhgGIO");
        GetAccessTokenResponse accessToken = client.getAccessToken(accessTokenRequest);
        System.out.println(JSON.toJSONString(accessToken.getBody()));
    }
```

## 步骤四：调用服务端OA相关API

1. 调用新版服务端API-[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > 若没有保存接口返回的模板编码`processCode`，钉钉管理后台版本不同，获取processCode的方式不同。登录钉钉管理后台，在首页查看版本。如下图所示，页面展示**回到旧版**和**新版反馈**，说明当前是新版。![审批获取processCode ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6144871461/p381720.png)

   **新版钉钉管理后台**：在审批模板编辑页-基础设置-**页面底部**查看。![OA审批-使用案例-审批附件-新增获取processcode新旧版方式 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9849463871/p443734.png)**旧版钉钉管理后台**：在审批模板编辑页的URL中查看。![processCode](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9849463871/p344894.png)

   ```
     public void createProcessTemplate() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           FormCreateHeaders formCreateHeaders = new FormCreateHeaders();
           formCreateHeaders.xAcsDingtalkAccessToken = "accessToken";

           // 1. 单行输入控件
           FormComponentProps formComponentProps1 = new FormComponentProps()
                   .setComponentId("TextField-sys1001")
                   .setPlaceholder("请输入")
                   .setLabel("客户名称")
                   .setRequired(false);
           FormComponent formComponent1 = new FormComponent()
                   .setComponentType("TextField")
                   .setProps(formComponentProps1);
           // 2. 多行输入控件
           FormComponentProps formComponentProps2 = new FormComponentProps()
                   .setComponentId("TextareaField-sys1002")
                   .setPlaceholder("请输入")
                   .setLabel("客户描述")
                   .setRequired(false);
           FormComponent formComponent2 = new FormComponent()
                   .setComponentType("TextareaField")
                   .setProps(formComponentProps2);

           //3.多选控件
           SelectOption option3 = new SelectOption();
           option3.setKey("option1");
           option3.setValue("重要");
           SelectOption option4 = new SelectOption();
           option4.setKey("option2");
           option4.setValue("一般");
           FormComponentProps formComponentProps3 = new FormComponentProps()
                   .setComponentId("DDMultiSelectField-sys1003")
                   .setLabel("客户标签")
                   .setOptions(java.util.Arrays.asList(option3, option4));
           FormComponent formComponent3 = new FormComponent()
                   .setComponentType("DDMultiSelectField")
                   .setProps(formComponentProps3);

           //4. 时间区间控件
           FormComponentProps formComponentProps4 = new FormComponentProps()
                   .setComponentId("DDDateRangeField-sys1004")
                   .setLabel("[\"客户达成意向开始时间\",\"客户达成意向结束时间\"]")
                   .setUnit("小时")
                   .setPlaceholder("请选择对应时间")
                   .setFormat("yyyy-MM-dd HH:mm");
           FormComponent formComponent4 = new FormComponent()
                   .setComponentType("DDDateRangeField")
                   .setProps(formComponentProps4);

           //5.明细控件
           //明细子控件统计
           FormComponentProps.FormComponentPropsStatField formComponentPropsStatField2 = new FormComponentProps.FormComponentPropsStatField()
                   .setComponentId("NumberField-sysC1005")
                   .setLabel("数字输入");

           FormComponentProps.FormComponentPropsStatField formComponentPropsStatField1 = new FormComponentProps.FormComponentPropsStatField()
                   .setComponentId("CalculateField-sysC1005")
                   .setLabel("金额（元）");

           //明细子控件
           //5.1明细单行输入框
           FormComponentProps childProp1 = new FormComponentProps()
                   .setComponentId("TextField-sysC1005")
                   .setLabel("名称");
           FormComponent child1 = new FormComponent()
                   .setComponentType("TextField")
                   .setProps(childProp1);

           //5.2明细金额输入框
           FormComponentProps childProp2 = new FormComponentProps()
                   .setComponentId("MoneyField-sysC1005")
                   .setLabel("单价（元）");
           FormComponent child2 = new FormComponent()
                   .setComponentType("MoneyField")
                   .setProps(childProp2);

           //5.3明细数字输入框
           FormComponentProps childProp3 = new FormComponentProps()
                   .setComponentId("NumberField-sysC1005")
                   .setLabel("个数");
           FormComponent child3 = new FormComponent()
                   .setComponentType("NumberField")
                   .setProps(childProp3);
           //5.4计算公式组件
           JSONObject jsonObject1 = new JSONObject();
           jsonObject1.put("id", "NumberField-sysC1005");
           String s = "*";
           JSONObject jsonObject2 = new JSONObject();
           jsonObject2.put("id", "MoneyField-sysC1005");
           Object objects[] = new Object[]{jsonObject1, s, jsonObject2};
           FormComponentProps childProp4 = new FormComponentProps()
                   .setComponentId("CalculateField-sysC1005")
                   .setLabel("总计")
                   .setPlaceholder("自动计算数值")
                   .setRequired(false)
                   .setFormula(JSON.toJSONString(objects));
           FormComponent child4 = new FormComponent()
                   .setComponentType("CalculateField")
                   .setProps(childProp4);

           FormComponentProps formComponentProps5 = new FormComponentProps()
                   .setComponentId("TableField-sys1005")
                   .setTableViewMode("table")
                   .setLabel("明细")
                   .setVerticalPrint(true)
                   .setStatField(Arrays.asList(formComponentPropsStatField1, formComponentPropsStatField2));
           FormComponent formComponent5 = new FormComponent()
                   .setComponentType("TableField")
                   .setChildren(Arrays.asList(child1, child2, child3, child4))
                   .setProps(formComponentProps5);

           // 6. 联系人控件
           FormComponentProps formComponentProps6 = new FormComponentProps()
                   .setComponentId("InnerContactField-sys1006")
                   .setLabel("联系人")
                   .setPlaceholder("请选择联系人")
                   .setChoice("1");
           FormComponent formComponent6 = new FormComponent()
                   .setComponentType("InnerContactField")
                   .setProps(formComponentProps6);

           // 7. 部门控件
           FormComponentProps formComponentProps7 = new FormComponentProps()
                   .setComponentId("DepartmentField-sys1007")
                   .setLabel("联系人部门")
                   .setPlaceholder("请选择部门")
                   .setMultiple(false);
           FormComponent formComponent7 = new FormComponent()
                   .setComponentType("DepartmentField")
                   .setProps(formComponentProps7);

           // 8. 省市区控件
           FormComponentProps formComponentProps8 = new FormComponentProps()
                   .setComponentId("AddressField-sys1008")
                   .setLabel("客户地址")
                   .setPlaceholder("请选择")
                   .setAddressModel("city");
           FormComponent formComponent8 = new FormComponent()
                   .setComponentType("AddressField")
                   .setProps(formComponentProps8);

           //9.单选控件
           SelectOption selectOption1 = new SelectOption();
           selectOption1.setKey("option1");
           selectOption1.setValue("紧急");
           SelectOption selectOption2 = new SelectOption();
           selectOption2.setKey("option2");
           selectOption2.setValue("普通");
           FormComponentProps formComponentProps9 = new FormComponentProps()
                   .setComponentId("DDSelectField-sys1009")
                   .setLabel("审批需求状态")
                   .setOptions(Arrays.asList(selectOption1, selectOption2));
           FormComponent formComponent9 = new FormComponent()
                   .setComponentType("DDSelectField")
                   .setProps(formComponentProps9);

           FormCreateRequest formCreateRequest = new FormCreateRequest()
                   .setName("客户表单")
                   .setDescription("客户表单")
                   //有参数processCode时为更新模板，无参数processCode时，为创建模板，该示例为创建模板
                   //.setProcessCode("PROC-ECED8693-****-****-****-A5EE2F7E9F46")
                   .setFormComponents(java.util.Arrays.asList(
                           formComponent1, formComponent2, formComponent3, formComponent4,
                           formComponent5, formComponent6, formComponent7, formComponent8,
                           formComponent9
                   ));
           try {
               FormCreateResponse formCreateResponse = client.formCreateWithOptions(formCreateRequest, formCreateHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(formCreateResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
2. 根据模板编码`processCode`，调用新版服务端API-[发起审批实例](0497-create-an-approval-instance.md)接口发起审批实例，获取审批实例`instanceId`。

   > **[!NOTE]**
   >
   > 若无保存审批实例`instanceId`，可通过调用新版服务端API-[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取发起实例时间段的审批实例`instanceId`。
   >
   > ```
   > public void instanceIdsQuery() throws Exception {
   >         Config config = new Config();
   >         config.protocol = "https";
   >         config.regionId = "central";
   >         com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
   >         com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsHeaders listProcessInstanceIdsHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsHeaders();
   >         listProcessInstanceIdsHeaders.xAcsDingtalkAccessToken = "accessToken";
   >         com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsRequest listProcessInstanceIdsRequest = new com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsRequest()
   >                 .setProcessCode("PROC-ECED8693-****-****-****-A5EE2F7E9F46")
   >                 .setStartTime(1663*****000L)
   >                 .setEndTime(1663******00L)
   >                 .setNextToken(0L)
   >                 .setMaxResults(10L)
   >                 .setUserIds(java.util.Arrays.asList(
   >                         "审批发起人userId"
   >                 ));
   >         try {
   >             ListProcessInstanceIdsResponse listProcessInstanceIdsResponse = client.listProcessInstanceIdsWithOptions(listProcessInstanceIdsRequest, listProcessInstanceIdsHeaders, new RuntimeOptions());
   >             System.out.println(JSON.toJSONString(listProcessInstanceIdsResponse.getBody()));
   >         } catch (TeaException err) {
   >             if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
   >                 // err 中含有 code 和 message 属性，可帮助开发定位问题
   >                 System.out.println(err.code);
   >                 System.out.println(err.message);
   >             }
   >         } catch (Exception _err) {
   >             TeaException err = new TeaException(_err.getMessage(), _err);
   >             if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
   >                 // err 中含有 code 和 message 属性，可帮助开发定位问题
   >                 System.out.println(err.code);
   >                 System.out.println(err.message);
   >             }
   >         }
   >     }
   > ```

   ```
   public void ProcessInstances() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           StartProcessInstanceHeaders startProcessInstanceHeaders = new StartProcessInstanceHeaders();
           startProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

           //1.单行输入框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues1 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户名称")
                   .setValue("小钉");

           //2.多行输入框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues2 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户描述")
                   .setValue("潜在优质客户");

           //3.多选框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues3;
           formComponentValues3 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户标签")
                   .setValue("[\"重要\",\"一般\"]")
                   .setComponentType("DDMultiSelectField");

           //4.日期区间组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues4 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("[\"客户达成意向开始时间\",\"客户达成意向结束时间\"]")
                   .setValue("[\"2022-08-14 15:00\",\"2022-08-15 15:00\"]");

           //5.明细表格组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details1 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("名称")
                   .setValue("钉钉F2 智能视频会议一体机");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details2 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("单价（元）")
                   .setValue("29999");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details3 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("个数")
                   .setValue("1");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details4 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("名称")
                   .setValue("钉钉F1 智能视频会议一体机");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details5 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("单价（元）")
                   .setValue("4999");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details6 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                   .setName("个数")
                   .setValue("5");

           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues5 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("明细")
                   .setValue(JSON.toJSONString(Arrays.asList(Arrays.asList(formComponentValues0Details1, formComponentValues0Details2, formComponentValues0Details3), Arrays.asList(formComponentValues0Details4, formComponentValues0Details5, formComponentValues0Details6))))
                   .setDetails(Arrays.asList(formComponentValues0Details1, formComponentValues0Details2, formComponentValues0Details3, formComponentValues0Details4, formComponentValues0Details5, formComponentValues0Details6));

           //6.联系人组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues6 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("联系人")
                   .setValue(JSON.toJSONString(Arrays.asList("联系人userId")));

           //7.部门组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues7 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("联系人部门")
                   .setValue("部门ID");

           //8.省市区组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues8 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("客户地址")
                   .setValue(JSON.toJSONString(Arrays.asList("北京,北京市,朝阳区,东湖街道,xxxxxxxA座")));

           //9.单选框组件
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues9 = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("审批需求状态")
                   .setValue("紧急");

           //设置审批人
           //会签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers0 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("AND")
                   .setUserIds(java.util.Arrays.asList(
                           "014******77041", "0852*******284272"
                   ));
           //或签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers1 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("OR")
                   .setUserIds(java.util.Arrays.asList(
                           "014******77041", "0852*******284272"
                   ));
           StartProcessInstanceRequest startProcessInstanceRequest = new StartProcessInstanceRequest()
                   .setOriginatorUserId("发起人userId")
                   .setProcessCode("PROC-ECED8693-****-****-****-A5EE2F7E9F46")
                   .setDeptId(1L)
                   .setMicroappAgentId(118*****5L)
                   .setApprovers(java.util.Arrays.asList(
                           approvers0, approvers1
                   ))
             			//抄送人
                   .setCcList(java.util.Arrays.asList(
                           "抄送人userId"
                   ))
                   .setCcPosition("FINISH")
                   .setFormComponentValues(java.util.Arrays.asList(
                           formComponentValues1, formComponentValues2, formComponentValues3, formComponentValues4,
                           formComponentValues5, formComponentValues6, formComponentValues7, formComponentValues8,
                           formComponentValues9
                   ));
           try {
               StartProcessInstanceResponse startProcessInstanceResponse = client.startProcessInstanceWithOptions(startProcessInstanceRequest, startProcessInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(startProcessInstanceResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
3. 根据审批实例`instanceId`，调用新版服务端API-[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情，获取审批任务各个任务节点信息`taskId`。

   ```
   public void processInstancesInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders getProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders();
           getProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest getProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest()
                   .setProcessInstanceId("zRfPT*********************159");
           try {
               GetProcessInstanceResponse processInstanceWithOptions = client.getProcessInstanceWithOptions(getProcessInstanceRequest, getProcessInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(processInstanceWithOptions.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
4. 根据审批实例`instanceId`和相应的任务节点`taskId`信息，调用新版服务端API-[同意或拒绝审批任务](0506-approve-or-reject-the-approval-task.md)接口，实现审批任务的操作，所有审批节点同意后，则该审批单通过。该步骤不支持第三方企业应用。

   > **[!NOTE]**
   >
   > 需按照审批节点顺序的`taskId`执行。以本流程为例：发起审批时设置先设置了会签，然后设置了或签两个审批节点，必须先执行会签中的`taskId`任务节点，否则接口将无法调用成功。

   ```
     public void processInstancesExecute() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceHeaders executeProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceHeaders();
           executeProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFileAttachments fileAttachments0 = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFileAttachments()
                   .setSpaceId("86****763")
                   .setFileSize("10***45")
                   .setFileId("673*****24")
                   .setFileName("***.jpg")
                   .setFileType("file");
           com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile file = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile()
                   .setPhotos(java.util.Arrays.asList(
                           "https://*********"
                   ))
                   .setAttachments(java.util.Arrays.asList(
                           fileAttachments0
                   ));
           com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest executeProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest()
                   .setProcessInstanceId("********")
                   .setRemark("同意")
                   .setResult("agree")
                   .setActionerUserId("审批节点人userId")
                   .setTaskId(76*****56L)
                   .setFile(file);
           try {
               ExecuteProcessInstanceResponse executeProcessInstanceResponse = client.executeProcessInstanceWithOptions(executeProcessInstanceRequest, executeProcessInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(executeProcessInstanceResponse.getBody()));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(err.code);
                   System.out.println(err.message);
               }
           }
       }
   ```
