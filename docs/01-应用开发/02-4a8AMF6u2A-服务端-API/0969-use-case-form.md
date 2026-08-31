---
title: "获取用户的填表数据详情"
source_url: "https://open.dingtalk.com/document/development/use-case-form"
namespace: "development"
slug: "use-case-form"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能填表 > 使用教程 > 获取用户的填表数据详情"
doc_id: "d3frJHZcvO"
updated_at: "2026-07-14 09:22:34"
---

> Source: https://open.dingtalk.com/document/development/use-case-form
> Path: 应用开发 / 服务端 API / 智能填表 > 使用教程 > 获取用户的填表数据详情
> Updated: 2026-07-14 09:22:34

# 获取用户的填表数据详情

本文档介绍了如何使用智能填表相关的接口，实现获取用户的填表数据详情。

## 接入流程简介

本文档展示了，创建一个企业内部应用，使用智能填表API，实现获取用户创建的模板、获取某个模板下提交的数据、获取某条数据详情流程：

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请智能填表相关接口权限。

步骤三：调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用智能填表相关API：

1. 调用服务端API-[获取用户创建的填表模板列表](0970-new-obtains-the-template-that-a-user-creates.md)接口，获取智能填表模板`formCode`。
2. 根据智能填表模板`formCode`，调用服务端API-[获取填表实例列表](0971-obtain-the-table-filling-instance-list-data.md)接口，获取填表模板下的填表数据实例列表`list`。
3. 根据实例列表`list`下具体的实例。调用服务端API-[获取单条填表实例详情](0972-obtains-the-instance-details-of-a-single-fill-table.md)接口，获取填表数据详情。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

单击**开发配置** > **权限管理**，在权限搜索框中输入`qyapi_swapp_collection_read`，并申请权限。

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

## 步骤四：调用智能填表相关API

1. 调用服务端API-[获取用户创建的填表模板列表](0970-new-obtains-the-template-that-a-user-creates.md)接口，获取智能填表模板`formCode`。

   ```
    public static com.aliyun.dingtalkswform_1_0.Client createClient() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           return new com.aliyun.dingtalkswform_1_0.Client(config);
       }
    public void getFormList() throws Exception {
           com.aliyun.dingtalkswform_1_0.Client client = Sample.createClient();
           ListFormSchemasByCreatorHeaders listFormSchemasByCreatorHeaders = new ListFormSchemasByCreatorHeaders();
           listFormSchemasByCreatorHeaders.xAcsDingtalkAccessToken = "accessToken";
           ListFormSchemasByCreatorRequest listFormSchemasByCreatorRequest = new ListFormSchemasByCreatorRequest()
                   .setMaxResults(10)
                   .setBizType(0)
                   .setCreator("userId")
                   .setNextToken(0L);
           try {
               ListFormSchemasByCreatorResponse listFormSchemasByCreatorResponse = client.listFormSchemasByCreatorWithOptions(listFormSchemasByCreatorRequest, listFormSchemasByCreatorHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(listFormSchemasByCreatorResponse));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(JSON.toJSONString(err));
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(JSON.toJSONString(err));
               }

           }
       }
   ```
2. 根据智能填表模板`formCode`，调用服务端API-[获取填表实例列表](0971-obtain-the-table-filling-instance-list-data.md)接口，获取填表模板下的填表数据实例列表`list`。

   ```
      public static com.aliyun.dingtalkswform_1_0.Client createClient() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           return new com.aliyun.dingtalkswform_1_0.Client(config);
       }
      
       public void ListInstances() throws Exception {
           com.aliyun.dingtalkswform_1_0.Client client = Sample.createClient();
           ListFormInstancesHeaders listFormInstancesHeaders = new ListFormInstancesHeaders();
           listFormInstancesHeaders.xAcsDingtalkAccessToken = "accessToken";
           ListFormInstancesRequest listFormInstancesRequest = new ListFormInstancesRequest()
                   .setBizType(0)
                   .setActionDate("2022-01-01")
                   .setNextToken(0)
                   .setMaxResults(10);
           try {
               ListFormInstancesResponse listFormInstancesResponse = client.listFormInstancesWithOptions("PROC-8DBC8FEB-18B8xxxxx", listFormInstancesRequest, listFormInstancesHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(listFormInstancesResponse));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(JSON.toJSONString(err));
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(JSON.toJSONString(err));
               }

           }
       }
   ```
3. 根据实例列表`list`下具体的实例。调用服务端API-[获取单条填表实例详情](0972-obtains-the-instance-details-of-a-single-fill-table.md)接口，获取填表数据详情。

   ```
       public static com.aliyun.dingtalkswform_1_0.Client createClient() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           return new com.aliyun.dingtalkswform_1_0.Client(config);
       }
       
       public void getInstance(){
           com.aliyun.dingtalkswform_1_0.Client client = Sample.createClient();
           GetFormInstanceHeaders getFormInstanceHeaders = new GetFormInstanceHeaders();
           getFormInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           GetFormInstanceRequest getFormInstanceRequest = new GetFormInstanceRequest()
                   .setBizType(0);
           try {
               GetFormInstanceResponse formInstanceWithOptions = client.getFormInstanceWithOptions("11125769-fxxxx", getFormInstanceRequest, getFormInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(formInstanceWithOptions));
           } catch (TeaException err) {
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(JSON.toJSONString(err));
               }

           } catch (Exception _err) {
               TeaException err = new TeaException(_err.getMessage(), _err);
               if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                   // err 中含有 code 和 message 属性，可帮助开发定位问题
                   System.out.println(JSON.toJSONString(err));
               }

           }
       }
   ```
