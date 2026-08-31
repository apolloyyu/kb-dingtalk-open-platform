---
title: "审批附件的操作流程"
source_url: "https://open.dingtalk.com/document/development/new-version-of-attachment-approval-process"
namespace: "development"
slug: "new-version-of-attachment-approval-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 使用教程 > 官方OA 审批 > 审批附件的操作流程"
doc_id: "gCYVw2ivlo"
updated_at: "2026-07-10 10:11:34"
---

> Source: https://open.dingtalk.com/document/development/new-version-of-attachment-approval-process
> Path: 应用开发 / 服务端 API / OA 审批 > 使用教程 > 官方OA 审批 > 审批附件的操作流程
> Updated: 2026-07-10 10:11:34

# 审批附件的操作流程

教程介绍了如何通过官方OA审批API实现发起带附件的审批流，及下载附件。

> **[!NOTE]**
>
> - 本文档以企业内部应用为例，第三方企业应用实现流程类似。
> - 仅调用服务端API无法实现审批附件的操作流程，必须与客户端JSAPI结合使用。

## 预期效果

发起附件审批，如下图：

![0818发起带附件评审](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2133980661/p478664.png)

## 接入流程简介

本文档展示了，创建一个企业内部应用，实现使用**官方**OA审批发起带附件的审批、下载审批附件等流程：

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：进入应用详情页，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请“OA审批”相应权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用OA审批相关API和客户端JSAPI：

1. 调用服务端API-[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，获取审批钉盘空间`spaceId`。
2. 调用客户端JSAPI-[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息。
3. 获取模板的唯一编码`processCode`。

   - 通过[钉钉管理后台](https://oa.dingtalk.com/index.htm#/microApp/microAppListNew)-OA审批-打开对应审批模板获取。
   - 调用服务端API-[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口，创建审批模板获取`processCode`。
4. 调用服务端API-[发起审批实例](0497-create-an-approval-instance.md)接口发起审批，获取审批实例`instanceId`。
5. 根据审批实例`instanceId`，调用服务端API-[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取审批实例详情中的`fileId`。
6. 审批附件操作：

   1. 下载审批附件

      1. 调用服务端API-[授权下载审批钉盘文件](0504-download-the-approval-nail-file.md)接口，进行审批钉盘文件的授权操作。
      2. 调用服务端API-[下载审批附件](0505-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。目前不支持第三方企业应用调用。
   2. 预览审批附件：

      1. 调用服务端API-[授权预览审批附件](0503-official-authorized-preview-approval-attachment.md)接口，实现钉盘文件的预览操作。
      2. 调用客户端JSAPI-[预览钉盘文件](../03-Ogu5SlPY4t-客户端-JSAPI/0330-jsapi-preview-file-in-ding-talk.md)接口，实现预览钉盘文件。

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

## 步骤四：调用OA审批API

1. 调用服务端API-[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，获取审批钉盘空间`spaceId`。

   ```
   public void ProcessSpaceInfo() throws Exception {
           com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders getAttachmentSpaceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceHeaders();
           getAttachmentSpaceHeaders.xAcsDingtalkAccessToken ="accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest getAttachmentSpaceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetAttachmentSpaceRequest()
                   .setUserId("manager7675")
                   .setAgentId(11******75L);
           try {
               GetAttachmentSpaceResponse attachmentSpaceWithOptions = client.getAttachmentSpaceWithOptions(getAttachmentSpaceRequest, getAttachmentSpaceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(attachmentSpaceWithOptions.getBody()));
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
2. 调用客户端JSAPI-[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)接口，获取文件基本信息，本流程示例使用[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10318)实现。

   > **[!IMPORTANT]**
   >
   > 调用该方法前，需要调用[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)进行授权操作。
3. 获取模板的唯一编码`processCode`。有2种方式可以获取processCode，可以选择以下任一种：

   - 方式一：通过[钉钉管理后台](https://aflow.dingtalk.com/dingtalk/web/query/dashboard?dinghash=aflowSetting#/aflowSetting)-OA审批-打开对应审批模板获取。

     > **[!NOTE]**
     >
     > 钉钉管理后台版本不同，获取processCode的方式不同。登录钉钉管理后台，在首页查看版本。如下图所示，页面展示**回到旧版**和**新版反馈**，说明当前是新版。![审批获取processCode ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6144871461/p381720.png)

     **新版钉钉管理后台**：在审批模板编辑页-基础设置-**页面底部**查看。![OA审批-使用案例-审批附件-新增获取processcode新旧版方式 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9849463871/p443734.png)**旧版钉钉管理后台**：在审批模板编辑页的URL中查看。![processCode](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9849463871/p344894.png)
   - 调用服务端API-[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口，创建审批模板获取`processCode`。

     ```
      public void createProcessTemplate() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
             FormCreateHeaders formCreateHeaders = new FormCreateHeaders();
             formCreateHeaders.xAcsDingtalkAccessToken = "accessToken"；

             // 1. 单行输入控件
             FormComponentProps formComponentProps = new FormComponentProps()
                     .setComponentId("DDAttachment-sys1001")
                     .setLabel("附件");
             FormComponent formComponent = new FormComponent()
                     .setComponentType("DDAttachment")
                     .setProps(formComponentProps);

             FormCreateRequest formCreateRequest = new FormCreateRequest()
                     .setName("审批附件表单")
                     .setDescription("测试审批附件组件")
                     //有参数processCode时为更新模板，无参数processCode时，为创建模板，该示例为创建模板
                     //.setProcessCode("PROC-42928B7C-****-****-****-B52B4E1702FC")
                     .setFormComponents(java.util.Arrays.asList(
                             formComponent
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
4. 调用服务端API-[发起审批实例](0497-create-an-approval-instance.md)接口发起审批，获取审批实例`instanceId`。

   ```
   public void ProcessInstances() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           StartProcessInstanceHeaders startProcessInstanceHeaders = new StartProcessInstanceHeaders();
           startProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";

           //1.附件
           JSONObject json  = new JSONObject();
           json.put("spaceId","479****886");
           json.put("fileName","IMG_2895(1).PNG");
           json.put("fileSize","2****4");
           json.put("fileType","png");
           json.put("fileId","68********11");
           StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues = new StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                   .setName("附件")
                   .setValue(JSON.toJSONString(Arrays.asList(json)));

           //设置审批人
           //会签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers0 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("AND")
                   .setUserIds(java.util.Arrays.asList(
                           "014******877041", "085******4272"
                   ));
           //或签审批
           StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers1 = new StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                   .setActionType("OR")
                   .setUserIds(java.util.Arrays.asList(
                           "014******877041", "085******4272"
                   ));
           StartProcessInstanceRequest startProcessInstanceRequest = new StartProcessInstanceRequest()
                   .setOriginatorUserId("审批发起人userId")
                   .setProcessCode("PROC-42928B7C-****-****-****-B52B4E1702FC")
                   .setDeptId(1L)
                   .setMicroappAgentId(11******5L)
                   .setApprovers(java.util.Arrays.asList(
                           approvers0, approvers1
                   ))
                   .setCcList(java.util.Arrays.asList(
                           "抄送人userId"
                   ))
                   .setCcPosition("FINISH")
                   .setFormComponentValues(java.util.Arrays.asList(
                           formComponentValues
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
5. 根据审批实例`instanceId`，调用服务端API-[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取审批实例详情中的`fileId`。

   ```
    public void processInstancesInfo() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders getProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceHeaders();
           getProcessInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest getProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetProcessInstanceRequest()
                   .setProcessInstanceId("Ay9***************199");
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
6. 审批附件操作：

   1. 下载审批附件：

      1. 调用服务端API-[授权下载审批钉盘文件](0504-download-the-approval-nail-file.md)接口，进行审批钉盘文件的授权操作。

         ```
          public void spaceAuthDownload() throws Exception {
                 com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
                 config.protocol = "https";
                 config.regionId = "central";
                 com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
                 com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthHeaders addApproveDentryAuthHeaders = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthHeaders();
                 addApproveDentryAuthHeaders.xAcsDingtalkAccessToken = "accessToken";
                 com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos fileInfos0 = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos()
                         .setFileId("49*****61")
                         .setSpaceId(47*****86L);
                 com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest addApproveDentryAuthRequest = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest()
                         .setUserId("manager7675")
                         .setFileInfos(java.util.Arrays.asList(
                                 fileInfos0
                         ));
                 try {
                     AddApproveDentryAuthResponse addApproveDentryAuthResponse = client.addApproveDentryAuthWithOptions(addApproveDentryAuthRequest, addApproveDentryAuthHeaders, new RuntimeOptions());
                     System.out.println(JSON.toJSONString(addApproveDentryAuthResponse.getBody()));
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
      2. 调用服务端API-[下载审批附件](0505-download-an-approval-attachment.md)接口，获取文件的链接`downloadUri`实现下载。目前不支持第三方企业应用调用。

         ```
         public void processFileDownload() throws Exception {
                 com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
                 config.protocol = "https";
                 config.regionId = "central";
                 com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
                 com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileHeaders grantProcessInstanceForDownloadFileHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileHeaders();
                 grantProcessInstanceForDownloadFileHeaders.xAcsDingtalkAccessToken = "accessToken";
                 com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileRequest grantProcessInstanceForDownloadFileRequest = new com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileRequest()
                         .setProcessInstanceId("Ay9***************199")
                         .setFileId("68********11");
                 try {
                     GrantProcessInstanceForDownloadFileResponse grantProcessInstanceForDownloadFileResponse = client.grantProcessInstanceForDownloadFileWithOptions(grantProcessInstanceForDownloadFileRequest, grantProcessInstanceForDownloadFileHeaders, new RuntimeOptions());
                     System.out.println(JSON.toJSONString(grantProcessInstanceForDownloadFileResponse.getBody()));
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
   2. 预览审批附件：

      1. 调用服务端API-[授权预览审批附件](0503-official-authorized-preview-approval-attachment.md)接口，实现钉盘文件的预览操作。

         ```
          public void authPreview() throws Exception {
                 com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
                 config.protocol = "https";
                 config.regionId = "central";
                 com.aliyun.dingtalkworkflow_1_0.Client client = new com.aliyun.dingtalkworkflow_1_0.Client(config);
                 com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthHeaders getSpaceWithDownloadAuthHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthHeaders();
                 getSpaceWithDownloadAuthHeaders.xAcsDingtalkAccessToken = "accessToken";
                 com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthRequest getSpaceWithDownloadAuthRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetSpaceWithDownloadAuthRequest()
                         .setUserId("ma*****75")
                         .setAgentId(118****5L)
                         .setProcessInstanceId("yIYiVlR3R***********4433")
                         .setFileId("495******61");
                 try {
                     GetSpaceWithDownloadAuthResponse spaceWithDownloadAuthWithOptions = client.getSpaceWithDownloadAuthWithOptions(getSpaceWithDownloadAuthRequest, getSpaceWithDownloadAuthHeaders, new RuntimeOptions());
                     System.out.println(JSON.toJSONString(spaceWithDownloadAuthWithOptions.getBody()));
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
      2. 调用客户端JSAPI-[预览钉盘文件](../03-Ogu5SlPY4t-客户端-JSAPI/0330-jsapi-preview-file-in-ding-talk.md)接口，实现预览钉盘文件。可通过访问[JSAPI Explorer](https://open.dingtalk.com/tools/explorer/jsapi?id=10317)在线调试该接口。

         > **[!NOTE]**
         >
         > 每一次预览审批附件前，都需要调用[授权预览审批附件](0503-official-authorized-preview-approval-attachment.md)接口实现授权操作。
