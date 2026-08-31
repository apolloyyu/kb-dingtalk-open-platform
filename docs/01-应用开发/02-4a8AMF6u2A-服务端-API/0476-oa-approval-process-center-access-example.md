---
title: "OA审批流程中心操作流程"
source_url: "https://open.dingtalk.com/document/development/oa-approval-process-center-access-example"
namespace: "development"
slug: "oa-approval-process-center-access-example"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 自由OA 审批 > OA审批流程中心操作流程"
doc_id: "AWK1bjUyDl"
updated_at: "2026-07-10 10:11:14"
---

> Source: https://open.dingtalk.com/document/development/oa-approval-process-center-access-example
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 自由OA 审批 > OA审批流程中心操作流程
> Updated: 2026-07-10 10:11:14

# OA审批流程中心操作流程

本文介绍了如何调用OA审批流程中心操作流程。

## 预期效果

### 发起审批

**通过流程中心方式接入的三方审批，详情页样式跟官方界面是一致的，用户可以复用官方OA审批的评论、建群讨论等官方能力，同时可以支持三方自定义某些按钮功能。比如「同意」、「拒绝」按钮可以直接跳转到三方系统中去。**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193809661/p521789.png)

### 审批实例

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193809661/p521790.png)

### **待处理任务**

**通过流程中心接入后，创建待处理任务后，审批单详情页中会出现同意/拒绝操作按钮，同时流程中心会把该审批任务同步生成为钉钉待办任务，这样三方就可以复用到钉钉统一待办提醒功能。**

- **审批单详情页：**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7193809661/p517423.png)
- **钉钉待办中心：**![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6193809661/p517424.png)

## 接入流程简介

本文档展示了，创建一个企业内部应用，使用OA审批流程中心提供的API，实现创建/更新/删除三方审批模板、创建/更新审批实例、创建/更新/查询审批待办任务、清理OA审批数据等流程：

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API：

1. 调用新版服务端API-[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，获取模板的唯一编码`processCode`。
2. 如果没有保存`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。
3. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看三方自有审批单模板、查看/搜索模板数据、导出/删除模板数据等。
4. 根据模板编码`processCode`，调用新版服务端API-[创建实例](0513-create-a-ticket-approval-instance.md)接口发起审批实例，获取审批实例`processInstanceId`。
5. 创建审批实例成功后，用户也可以进入钉钉OA审批中心，查看审批四大列表（待处理、已处理、已发起、我收到的）、搜索审批实例数据、执行审批等操作。
6. 根据审批实例`processInstanceId`和待办事项列表tasks，调用[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。
7. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。
8. 根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。
9. 根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0514-update-instance-status.md)或 [批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。
10. 最后，若需要对审批模板数据进行清理，可以调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`Workflow.Form.Write`、`Workflow.Instance.Write`、`Workflow.Instance.Read`和`qyapi_aflow`，并申请权限。

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

1. 调用新版服务端API-[创建或更新审批模板](0510-create-orupdate-the-approval-template-new.md)接口，获取模板的唯一编码`processCode`。

   > **[!NOTE]**
   >
   > 若没有保存接口返回的模板编码`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。

   ```
     public void  saveProcess() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           SaveProcessHeaders saveProcessHeaders = new SaveProcessHeaders();
           saveProcessHeaders.xAcsDingtalkAccessToken = "accessToken";

           // 1. 单行输入控件
           FormComponentProps formComponentProps1 = new FormComponentProps()
                   .setComponentId("TextField-abcd")
                   .setPlaceholder("请输入")
                   .setLabel("单行输入")
                   .setRequired(true);
           FormComponent formComponent1 = new FormComponent()
                   .setComponentType("TextField")
                   .setProps(formComponentProps1);
           // 2. 多行输入控件
           FormComponentProps formComponentProps2 = new FormComponentProps()
                   .setComponentId("TextareaField-abcd")
                   .setPlaceholder("请输入")
                   .setLabel("多行输入")
                   .setRequired(true);
           FormComponent formComponent2 = new FormComponent()
                   .setComponentType("TextareaField")
                   .setProps(formComponentProps2);
           // 3. 数字输入控件
           FormComponentProps formComponentProps3 = new FormComponentProps()
                   .setComponentId("NumberField-abcd")
                   .setPlaceholder("请输入")
                   .setLabel("数字输入")
                   .setUnit("元")
                   .setRequired(true);
           FormComponent formComponent3 = new FormComponent()
                   .setComponentType("NumberField")
                   .setProps(formComponentProps3);
           // 4. 单选控件
           SelectOption option1 = new SelectOption();
           option1.setKey("option1");
           option1.setValue("选项1");
           SelectOption option2 = new SelectOption();
           option2.setKey("option2");
           option2.setValue("选项2");
           FormComponentProps formComponentProps4 = new FormComponentProps()
                   .setComponentId("DDSelectField-abcd")
                   .setPlaceholder("请选择")
                   .setLabel("单选")
                   .setBizAlias("staff_type")
                   .setOptions(java.util.Arrays.asList(option1, option2))
                   .setRequired(true);
           FormComponent formComponent4 = new FormComponent()
                   .setComponentType("DDSelectField")
                   .setProps(formComponentProps4);

           // 5. 多选控件
           SelectOption option3 = new SelectOption();
           option3.setKey("option1");
           option3.setValue("选项1");
           SelectOption option4 = new SelectOption();
           option4.setKey("option2");
           option4.setValue("选项2");
           FormComponentProps formComponentProps5 = new FormComponentProps()
                   .setComponentId("DDMultiSelectField-abcd")
                   .setPlaceholder("请选择")
                   .setLabel("多选")
                   .setOptions(java.util.Arrays.asList(option3, option4))
                   .setRequired(true);
           FormComponent formComponent5 = new FormComponent()
                   .setComponentType("DDMultiSelectField")
                   .setProps(formComponentProps5);

           // 6. 日期控件
           FormComponentProps formComponentProps6 = new FormComponentProps()
                   .setComponentId("DDDateField-abcd")
                   .setPlaceholder("请选择")
                   .setLabel("日期")
                   .setUnit("小时")
                   .setFormat("yyyy-MM-dd HH:mm")
                   .setRequired(true);
           FormComponent formComponent6 = new FormComponent()
                   .setComponentType("DDDateField")
                   .setProps(formComponentProps6);

           // 7. 时间区间控件
           FormComponentProps formComponentProps7 = new FormComponentProps()
                   .setComponentId("DDDateRangeField-abcd")
                   .setPlaceholder("请选择")
                   .setLabel("[\"开始时间\",\"结束时间\"]")
                   .setUnit("小时")
                   .setFormat("yyyy-MM-dd HH:mm")
                   .setRequired(true);
           FormComponent formComponent7 = new FormComponent()
                   .setComponentType("DDDateRangeField")
                   .setProps(formComponentProps7);

           // 8. 文字说明控件
           FormComponentProps formComponentProps8 = new FormComponentProps()
                   .setComponentId("TextNote-abcd")
                   .setLabel("说明")
                   .setContent("详细说明内容")
                   .setLink("https://www.dingtalk.com/")
                   .setPrint("0")
                   .setRequired(false);
           FormComponent formComponent8 = new FormComponent()
                   .setComponentType("TextNote")
                   .setProps(formComponentProps8);

           // 10. 图片控件
           FormComponentProps formComponentProps10 = new FormComponentProps()
                   .setComponentId("DDPhotoField-abcd")
                   .setLabel("图片");
           FormComponent formComponent10 = new FormComponent()
                   .setComponentType("DDPhotoField")
                   .setProps(formComponentProps10);

           // 11. 金额控件
           FormComponentProps formComponentProps11 = new FormComponentProps()
                   .setComponentId("MoneyField-abcd")
                   .setUpper("0")
                   .setPlaceholder("请输入金额")
                   .setLabel("奖金（元）");
           FormComponent formComponent11 = new FormComponent()
                   .setComponentType("MoneyField")
                   .setProps(formComponentProps11);

           // 13. 附件控件
           FormComponentProps formComponentProps13 = new FormComponentProps()
                   .setComponentId("DDAttachment-abcd")
                   .setLabel("附件");
           FormComponent formComponent13 = new FormComponent()
                   .setComponentType("DDAttachment")
                   .setProps(formComponentProps13);

           // 14. 联系人控件
           FormComponentProps formComponentProps14 = new FormComponentProps()
                   .setComponentId("InnerContactField-abcd")
                   .setLabel("联系人")
                   .setChoice("1");
           FormComponent formComponent14 = new FormComponent()
                   .setComponentType("InnerContactField")
                   .setProps(formComponentProps14);

           // 15. 部门控件
           FormComponentProps formComponentProps15 = new FormComponentProps()
                   .setComponentId("DepartmentField-abcd")
                   .setLabel("部门")
                   .setMultiple(false);
           FormComponent formComponent15 = new FormComponent()
                   .setComponentType("DepartmentField")
                   .setProps(formComponentProps15);

           // 16. 关联审批单控件
           AvaliableTemplate template = new AvaliableTemplate();
           template.setName("出差申请单");
           template.setProcessCode("出差申请单的ProcessCode");
           FormComponentProps formComponentProps16 = new FormComponentProps()
                   .setComponentId("RelateField-abcd")
                   .setLabel("关联审批单")
                   .setAvailableTemplates(java.util.Arrays.asList(template));
           FormComponent formComponent16 = new FormComponent()
                   .setComponentType("RelateField")
                   .setProps(formComponentProps16);

           // 17. 省市区控件
           FormComponentProps formComponentProps17 = new FormComponentProps()
                   .setComponentId("AddressField-abcd")
                   .setLabel("省市区")
                   .setPlaceholder("请选择")
                   .setAddressModel("city");
           FormComponent formComponent17 = new FormComponent()
                   .setComponentType("AddressField")
                   .setProps(formComponentProps17);

           // 18. 评分控件
           FormComponentProps formComponentProps18 = new FormComponentProps()
                   .setComponentId("StarRatingField-abcd")
                   .setLabel("请输入")
                   .setLimit(5);
           FormComponent formComponent18 = new FormComponent()
                   .setComponentType("StarRatingField")
                   .setProps(formComponentProps18);        
                         
           SaveProcessRequestProcessFeatureConfigFeatures features1 = new SaveProcessRequestProcessFeatureConfigFeatures()
               .setName("TASK_EXECUTE")
               .setRunType("REDIRECT")
               .setPcUrl("https://www.dingtalk.com")
               .setMobileUrl("https://www.dingtalk.com");

         	SaveProcessRequestProcessFeatureConfig processFeatureConfig = new SaveProcessRequestProcessFeatureConfig()
           		.setFeatures(java.util.Arrays.asList(features1));
           
           SaveProcessRequest saveProcessRequest = new SaveProcessRequest()
                   .setName("出差报销审批")
                   .setDescription("用于员工差旅费用报销使用")
                   .setFormComponents(java.util.Arrays.asList(
                           formComponent1, formComponent2, formComponent3, formComponent4, formComponent5,
                           formComponent6, formComponent7, formComponent8, formComponent10,
                           formComponent11, formComponent13, formComponent14, formComponent15,
                           formComponent16, formComponent17, formComponentProps18
                   ))
                   .setProcessFeatureConfig(processFeatureConfig);
           try {
               SaveProcessResponse saveProcessResponse = client.saveProcessWithOptions(saveProcessRequest, saveProcessHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(saveProcessResponse.getBody()));
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
2. 如果没有保存`processCode`，可以通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取`processCode`。

   ```
   public void getProcessCodeByName() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameHeaders getProcessCodeByNameHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameHeaders();
           getProcessCodeByNameHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameRequest getProcessCodeByNameRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessCodeByNameRequest()
                   .setName("名称");
           try {
               GetProcessCodeByNameResponse getProcessCodeByNameResponse = client.getProcessCodeByNameWithOptions(getProcessCodeByNameRequest, getProcessCodeByNameHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(getProcessCodeByNameResponse.getBody()));
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
3. 创建审批模板成功后，用户可以在钉钉OA审批管理后台，查看自有审批单模板。

   ![未标题-1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7193809661/p517459.gif)
4. 根据模板编码`processCode`，调用新版服务端API-[创建实例](0513-create-a-ticket-approval-instance.md)接口发起审批实例，获取审批实例`processInstanceId`。

   ```
   public void saveIntegratedInstance() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           SaveIntegratedInstanceHeaders saveIntegratedInstanceHeaders = new SaveIntegratedInstanceHeaders();
           saveIntegratedInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
     
           //1.单行输入框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues1 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户名称")
                   .setValue("小钉");

           //2.多行输入框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues2 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户描述")
                   .setValue("潜在优质客户");
     
           //3.数字输入框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues3 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("数量")
                   .setValue("100");
     
           //4.单选框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues4 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户类型")
                   .setValue("大客户");
     
           //5.多选框组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues5;
           formComponentValues5 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户标签")
                   .setValue("[\"重要\",\"一般\"]")
                   .setComponentType("DDMultiSelectField");

           //6.日期组件，日期时间格式需要与创建OA审批模板中的日期控件格式一致
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues6 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("日期")
                   .setValue("2022-08-14 15:00");
     
           //7.日期区间组件，日期时间格式需要与创建OA审批模板中的时间区间控件格式一致
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues7 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("[\"客户达成意向开始时间\",\"客户达成意向结束时间\"]")
                   .setValue("[\"2022-08-14 15:00\",\"2022-08-15 15:00\"]");

           //8.文字说明组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues8 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("文字说明")
                   .setValue("详细说明内容");
       
           //10.图片组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues10 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("图片")
                   .setValue("[\"http://url1\",\"http://url2\",\"http://url3\"]");
           
     			//11.金额组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues11 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("金额（元）")
                   .setValue("100");

     			/*
           		附件控件的 value 是一个 json 数组转义为字符串形式。数组中的每个 json 对象是一个附件文件，
             	每个文件都必须包含 spaceId、fileName、fileSize、fileType 和 fileId 字段，这些字段
             	都可以通过调用钉盘的上传附件接口获取。
           */
       		//13.附件组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues13 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("附件")
                   .setValue("[{\"spaceId\": \"163xxxx658\", \"fileName\": \"2644.JPG\", \"fileSize\": \"333\", \"fileType\": \"jpg\", \"fileId\": " +
       "\"643xxxx140\"}]");    
     
     
     			//14.联系人组件，注意联系人控件需要指定extValue值，具体格式参考下面示例，其中emplId和itemId为用户userId
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues14 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("联系人")
                   .setValue(JSON.toJSONString(Arrays.asList("联系人名称")))
                   .setExtValue("[{\"name\":\"小钉\",\"emplId\":\"userid123\",\"itemId\":\"userid123\"}]");

           //15.部门组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues15 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("联系人部门")
                   .setValue("部门ID");
                               
           //16.关联审批单组件，注意关联审批单控件需要指定extValue值，具体格式参考下面示例，其中procInstId为需要关联的审批实例id
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues16 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("关联审批单")
                   .setValue(JSON.toJSONString(Arrays.asList("xxx提交的出差报销审批")))
             			.setExtValue("{\"list\":[{\"procInstId\":\"zUUgcEmeSQG-xxx\"}]}");
                               
           //17.省市区组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues17 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("客户地址")
                   .setValue(JSON.toJSONString(Arrays.asList("北京,北京市,朝阳区,东湖街道,xxxxxxxA座")));
                               
           //18.评分组件
           SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValues18 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                   .setName("评分")
                   .setValue("5");

     			//设置抄送人
          SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers notifiers0 = new SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers()
                   .setUserid("manager001")
                   .setPosition("start");
      		
     		SaveIntegratedInstanceRequest saveIntegratedInstanceRequest = new SaveIntegratedInstanceRequest()
                   .setProcessCode("proc")
                   .setOriginatorUserId("manager1234")
                   .setFormComponentValueList(java.util.Arrays.asList(
                      formComponentValues1, formComponentValues2, formComponentValues3, formComponentValues4,
                      formComponentValues5, formComponentValues6, formComponentValues7, formComponentValues8,
                      formComponentValues10, formComponentValues11,
                      formComponentValues13,formComponentValues14,formComponentValues15, formComponentValues16, 
                      formComponentValues17, formComponentValues18
                   ))
                   .setTitle("xxx的审批")
                   .setUrl("https://www.dingtalk.com/")
                   .setNotifiers(java.util.Arrays.asList(
                       notifiers0
                   ));
           try {
               SaveIntegratedInstanceResponse saveIntegratedInstanceResponse = client.saveIntegratedInstanceWithOptions(saveIntegratedInstanceRequest, saveIntegratedInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(saveIntegratedInstanceResponse.getBody()));
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
5. 根据审批实例`processInstanceId`和待办事项列表tasks，调用[创建流程中心待处理任务](0516-create-pending-tasks-in-process-center.md)接口，可以将三方系统内的审批节点信息同步到钉钉OA审批，获取待办事项的taskId并生成对应的钉钉待办任务。创建待处理任务后，审批单详情页中会出现同意/拒绝操作按钮，同时流程中心会把该审批任务同步生成为钉钉待办任务，这样三方就可以复用到钉钉统一待办提醒功能。

```
public void createIntegratedTask() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
  			CreateIntegratedTaskHeaders createIntegratedTaskHeaders = new CreateIntegratedTaskHeaders();
        createIntegratedTaskHeaders.xAcsDingtalkAccessToken = "accessToken";
        CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks tasks0 = new CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks()
                .setUserId("manager001")
                .setUrl("https://www.dingtalk.com");
        CreateIntegratedTaskRequest createIntegratedTaskRequest = new CreateIntegratedTaskRequest()
                .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                .setActivityId("act_xxxxx")
                .setTasks(java.util.Arrays.asList(
                    tasks0
                ));
        try {
            CreateIntegratedTaskResponse createIntegratedTaskResponse = client.createIntegratedTaskWithOptions(createIntegratedTaskRequest, createIntegratedTaskHeaders, new RuntimeOptions());
            System.out.println(JSON.toJSONString(createIntegratedTaskResponse.getBody()));
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

7. 创建待处理任务成功后，调用[查询通过流程中心集成的OA审批任务](0517-query-oa-approval-tasks-integrated-through-process-center.md)接口，可以查询到用户运行中的审批任务。

```
public void  queryIntegratedTodoTask() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
        QueryIntegratedTodoTaskHeaders queryIntegratedTodoTaskHeaders = new QueryIntegratedTodoTaskHeaders();
        queryIntegratedTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryIntegratedTodoTaskRequest queryIntegratedTodoTaskRequest = new QueryIntegratedTodoTaskRequest()
                .setUserId("manager001")
                .setPageSize(10)
                .setPageNumber(1)
                .setCreateBefore(1660036833411L);
        try {
            QueryIntegratedTodoTaskResponse queryIntegratedTodoTaskResponse = client.queryIntegratedTodoTaskWithOptions(queryIntegratedTodoTaskRequest, queryIntegratedTodoTaskHeaders, new RuntimeOptions());
            System.out.println(JSON.toJSONString(queryIntegratedTodoTaskResponse.getBody()));
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

8. 根据审批实例`processInstanceId`和审批待办任务taskId，可以调用[更新流程中心任务状态](0518-update-process-center-task-status.md)接口，同步完成自有审批待办状态的更新。在或签等场景，可以调用[批量取消流程中心待处理任务](0519-cancel-multiple-oa-approval-tasks.md)接口，批量将审批实例下正在运行中的待办事项设置为CANCELED。

   - **更新流程中心任务状态**

     ```
     public void  updateIntegratedTask() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       			UpdateIntegratedTaskHeaders updateIntegratedTaskHeaders = new UpdateIntegratedTaskHeaders();
             updateIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
             UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks tasks0 = new UpdateIntegratedTaskRequest.UpdateIntegratedTaskRequestTasks()
                     .setTaskId(1234567L)
                     .setStatus("COMPLETED")
                     .setResult("AGREE");
             UpdateIntegratedTaskRequest updateIntegratedTaskRequest = new UpdateIntegratedTaskRequest()
                     .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                     .setTasks(java.util.Arrays.asList(
                         tasks0
                     ));
             try {
                 UpdateIntegratedTaskResponse updateIntegratedTaskResponse = client.updateIntegratedTaskWithOptions(updateIntegratedTaskRequest, updateIntegratedTaskHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateIntegratedTaskResponse.getBody()));
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
   - **批量取消OA审批任务**

     ```
     public void  cancelIntegratedTask() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
       			CancelIntegratedTaskHeaders cancelIntegratedTaskHeaders = new CancelIntegratedTaskHeaders();
             cancelIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
             CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new CancelIntegratedTaskRequest()
                     .setProcessInstanceId("tPr_FB_mT_xxxxxxxxx2hQ05201655306463")
                     .setActivityId("act_xxxx")
                     .setActivityIds(java.util.Arrays.asList(
                         "act_xxxx"
                     ));
             CancelIntegratedTaskRequest cancelIntegratedTaskRequest = new UpdateIntegratedTaskRequest()
                     .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                     .setTasks(java.util.Arrays.asList(
                         tasks0
                     ));
             try {
                 CancelIntegratedTaskResponse cancelIntegratedTaskResponse = client.cancelIntegratedTaskWithOptions(cancelIntegratedTaskRequest, cancelIntegratedTaskHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(cancelIntegratedTaskResponse.getBody()));
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
9. 根据审批实例`processInstanceId`和实例状态status、实例结果result等，可以调用[更新实例状态](0514-update-instance-status.md)或 [批量更新实例状态](0515-self-owned-batch-update-of-instance-status.md)接口，更新实例状态。

   ```
   public void  updateProcessInstance() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     			com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceHeaders updateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceHeaders();
           updateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
           com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest.UpdateProcessInstanceRequestNotifiers()
                   .setUserId("001");
           com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest updateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.UpdateProcessInstanceRequest()
                   .setProcessInstanceId("proc")
                   .setStatus("COMPLETED")
                   .setResult("agree")
                   .setNotifiers(java.util.Arrays.asList(
                       notifiers0
                   ));
           try {
               UpdateProcessInstanceResponse updateProcessInstanceResponse = client.updateProcessInstanceWithOptions(updateProcessInstanceRequest, updateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
               System.out.println(JSON.toJSONString(updateProcessInstanceResponse.getBody()));
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

   ```
   public void  batchUpdateProcessInstances() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
     			com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceHeaders batchUpdateProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceHeaders();
           batchUpdateProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
           com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers updateProcessInstanceRequests0Notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequestsNotifiers()
                   .setUserId("001");
           com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests updateProcessInstanceRequests0 = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest.BatchUpdateProcessInstanceRequestUpdateProcessInstanceRequests()
                   .setProcessInstanceId("EF6YJL35")
                   .setStatus("COMPLETED")
                   .setResult("agree")
                   .setNotifiers(java.util.Arrays.asList(
                       updateProcessInstanceRequests0Notifiers0
                   ));
           com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest batchUpdateProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.BatchUpdateProcessInstanceRequest()
                   .setUpdateProcessInstanceRequests(java.util.Arrays.asList(
                       updateProcessInstanceRequests0
                   ));
           try {
               BatchUpdateProcessInstanceResponse batchUpdateProcessInstanceResponse = client.batchUpdateProcessInstanceWithOptions(batchUpdateProcessInstanceRequest, batchUpdateProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
               System.out.println(JSON.toJSONString(batchUpdateProcessInstanceResponse.getBody()));
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
10. 最后，若需要对审批模板数据进行清理，可以调用[删除模板](0512-self-owned-approval-deletion-template.md)接口，删除为企业创建的审批模板，同时删除该模板下创建的实例和待办任务。

    ```
    public void  deleteProcess() throws Exception {
            Config config = new Config();
            config.protocol = "https";
            config.regionId = "central";
            com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
      			DeleteProcessHeaders deleteProcessHeaders = new DeleteProcessHeaders();
            deleteProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
            DeleteProcessRequest deleteProcessRequest = new DeleteProcessRequest()
                    .setProcessCode("proc-abc")
                    .setCleanRunningTask(false);
            try {
                DeleteProcessResponse deleteProcessResponse = client.deleteProcessWithOptions(deleteProcessRequest, deleteProcessHeaders, new RuntimeOptions());
                System.out.println(JSON.toJSONString(deleteProcessResponse.getBody()));
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
