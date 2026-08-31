---
title: "应用的全生命周期管理"
source_url: "https://open.dingtalk.com/document/development/application-management-workflow"
namespace: "development"
slug: "application-management-workflow"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 使用教程 > 应用的全生命周期管理"
doc_id: "izYdSmy8KD"
updated_at: "2026-07-14 09:22:19"
---

> Source: https://open.dingtalk.com/document/development/application-management-workflow
> Path: 应用开发 / 服务端 API / 钉钉应用 > 使用教程 > 应用的全生命周期管理
> Updated: 2026-07-14 09:22:19

# 应用的全生命周期管理

本文档介绍了如何调用钉钉开放平台的应用管理相关接口，完成企业内部应用的创建、配置、查询与删除等全生命周期管理。适用于具备管理员权限的企业开发者，通过API实现自动化应用管理。

## 流程简介

前提条件：

- 已完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。
- 操作者为企业管理员，具备在开发者后台进行配置的权限。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请应用管理相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)，通过accessToken鉴权调用者身份。

步骤四：调用服务端应用管理相关API。

1. 应用查询操作流程：

   1. 调用服务端API-[获取企业所有应用列表](0864-obtains-a-list-of-all-enterprise-applications.md)接口，获取企业应用信息。
   2. 调用服务端API-[获取用户可见的企业应用列表](0866-obtains-the-list-of-enterprise-applications-visible-to-a-user.md)接口，获取当前用户可使用的应用信息。
2. 应用管理操作流程：

   1. 调用服务端API-[创建企业内部应用](0861-create-an-h5-application-for-your-enterprise.md)接口，创建一个企业内部应用-H5微应用，获取应用的agentid。
   2. 根据应用agentid，调用服务端API-[更新企业内部应用](0862-update-internal-h5-applications.md)接口，更新企业内部应用-H5微应用信息。
   3. 根据应用agentid，调用服务端API-[获取企业内部应用的可使用范围](0872-obtains-the-application-visible-range.md)接口，获取当前应用的可使用范围。
   4. 根据应用agentid，调用服务端API-[更新企业内部应用的可使用范围](0871-update-the-visible-range-of-micro-applications.md)接口，更新当前应用的可使用范围。
   5. 根据应用agentid，调用服务端API-[删除企业内部应用](0863-delete-an-internal-h5-application.md)接口，删除对应的企业内部应用。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`qyapi_get_microapp_list`和`qyapi_microapp_manage`，并申请权限。

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

## 步骤四：调用服务端应用管理相关API

1. 应用查询操作流程：

   1. 调用服务端API-[获取企业所有应用列表](0864-obtains-a-list-of-all-enterprise-applications.md)接口，获取企业应用信息。

      ```
       public void allApps() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              ListAllAppHeaders listAllAppHeaders = new ListAllAppHeaders();
              listAllAppHeaders.xAcsDingtalkAccessToken = "accessToken";
              try {
                  ListAllAppResponse listAllAppResponse = client.listAllAppWithOptions(listAllAppHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(listAllAppResponse.getBody()));
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
   2. 调用服务端API-[获取用户可见的企业应用列表](0866-obtains-the-list-of-enterprise-applications-visible-to-a-user.md)接口，获取当前用户可使用的应用信息。

      ```
      public void usersApps() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              ListUserVilebleAppHeaders listUserVilebleAppHeaders = new ListUserVilebleAppHeaders();
              listUserVilebleAppHeaders.xAcsDingtalkAccessToken = "accessToken";
              try {
                  ListUserVilebleAppResponse userAppsList = client.listUserVilebleAppWithOptions("manager7675", listUserVilebleAppHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(userAppsList.getBody()));
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
2. 应用管理操作流程：

   1. 调用服务端API-[创建企业内部应用](0861-create-an-h5-application-for-your-enterprise.md)接口，创建一个企业内部应用，获取应用的agentid。

      ```
       public void appsCreate() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              CreateInnerAppHeaders createInnerAppHeaders = new CreateInnerAppHeaders();
              createInnerAppHeaders.xAcsDingtalkAccessToken = "accessToken";
              CreateInnerAppRequest createInnerAppRequest = new CreateInnerAppRequest()
                      .setOpUnionId("E9CS6Xu5*****N7QiEiE")
                      .setName("20221104应用")
                      .setDesc("20221104应用")
                      .setIcon("@lADOd*****0CbA")
                      .setHomepageLink("https://www.dingtalk.com")
                      .setPcHomepageLink("https://www.dingtalk.com")
                      .setOmpLink("https://www.dingtalk.com")
                      .setIpWhiteList(java.util.Arrays.asList(
                              "1.1.1.1","127.0.0.1"
                      ))
                      .setScopeType("BASE");
              try {
                  CreateInnerAppResponse innerAppWithOptions = client.createInnerAppWithOptions(createInnerAppRequest, createInnerAppHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(innerAppWithOptions.getBody()));
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
   2. 根据应用agentid，调用服务端API-[更新企业内部应用](0862-update-internal-h5-applications.md)接口，更新企业内部应用信息。

      ```
      public void appsUpdate() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              UpdateInnerAppHeaders updateInnerAppHeaders = new UpdateInnerAppHeaders();
              updateInnerAppHeaders.xAcsDingtalkAccessToken = "accessToken";
              UpdateInnerAppRequest updateInnerAppRequest = new UpdateInnerAppRequest()
                      .setOpUnionId("E9CS6Xu5*****N7QiEiE")
                      .setName("20221104应用测试")
                      .setDesc("20221104应用测试")
                      .setIcon("@lADOd*****bM0CbA")
                      .setHomepageLink("https://www.dingtalk.com")
                      .setPcHomepageLink("https://www.dingtalk.com")
                      .setOmpLink("https://www.dingtalk.com")
                      .setIpWhiteList(java.util.Arrays.asList(
                             "1.1.1.1","127.0.0.1"
                      ));
              try {
                  UpdateInnerAppResponse updateInnerAppResponse = client.updateInnerAppWithOptions("2021****82", updateInnerAppRequest, updateInnerAppHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(updateInnerAppResponse.getBody()));
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
   3. 根据应用agentid，调用服务端API-[获取企业内部应用的可使用范围](0872-obtains-the-application-visible-range.md)接口，获取当前应用的可使用范围。

      ```
      public void  appsScopes() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              GetMicroAppScopeHeaders getMicroAppScopeHeaders = new GetMicroAppScopeHeaders();
              getMicroAppScopeHeaders.xAcsDingtalkAccessToken = "accessToken";
              try {
                  GetMicroAppScopeResponse microAppScopeWithOptions = client.getMicroAppScopeWithOptions("2021****82", getMicroAppScopeHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(microAppScopeWithOptions.getBody()));
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
   4. 根据应用agentid，调用服务端API-[更新企业内部应用的可使用范围](0871-update-the-visible-range-of-micro-applications.md)接口，更新当前应用的可使用范围。

      ```
       public void appsScopesUpdate() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              SetMicroAppScopeHeaders setMicroAppScopeHeaders = new SetMicroAppScopeHeaders();
              setMicroAppScopeHeaders.xAcsDingtalkAccessToken = "accessToken";
              SetMicroAppScopeRequest setMicroAppScopeRequest = new SetMicroAppScopeRequest()
                      .setAddUserIds(java.util.Arrays.asList(
                              "01296106445126923197"
                      ))
                      .setOnlyAdminVisible(false);
              try {
                  SetMicroAppScopeResponse setMicroAppScopeResponse = client.setMicroAppScopeWithOptions("2021****82", setMicroAppScopeRequest, setMicroAppScopeHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(setMicroAppScopeResponse.getBody()));
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
   5. 根据应用agentid，调用服务端API-[删除企业内部应用](0863-delete-an-internal-h5-application.md)接口，删除对应的企业内部应用。

      ```
       public void appsDelete() throws Exception {
              Config config = new Config();
              config.protocol = "https";
              config.regionId = "central";
              com.aliyun.dingtalkmicro_app_1_0.Client client = new com.aliyun.dingtalkmicro_app_1_0.Client(config);
              DeleteInnerAppHeaders deleteInnerAppHeaders = new DeleteInnerAppHeaders();
              deleteInnerAppHeaders.xAcsDingtalkAccessToken = "accessToken";
              DeleteInnerAppRequest deleteInnerAppRequest = new DeleteInnerAppRequest()
                      .setOpUnionId("E9CS6Xu5*****N7QiEiE");
              try {
                  DeleteInnerAppResponse deleteInnerAppResponse = client.deleteInnerAppWithOptions("2021****82", deleteInnerAppRequest, deleteInnerAppHeaders, new RuntimeOptions());
                  System.out.println(JSON.toJSONString(deleteInnerAppResponse.getBody()));
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
