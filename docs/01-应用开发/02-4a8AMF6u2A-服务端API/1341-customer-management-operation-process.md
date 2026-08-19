---
title: "CRM客户数据操作流程"
source_url: "https://open.dingtalk.com/document/development/customer-management-operation-process"
namespace: "development"
slug: "customer-management-operation-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > CRM客户数据操作流程"
doc_id: "nKJO0CMQxq"
updated_at: "2026-07-21 09:26:06"
---

> Source: https://open.dingtalk.com/document/development/customer-management-operation-process
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 使用教程 > CRM客户数据操作流程
> Updated: 2026-07-21 09:26:06

# CRM客户数据操作流程

本文档介绍了CRM客户数据操作流程。

> **[!NOTE]**
>
> 本文档以企业内部应用实现为例，第三方企业应用实现流程与本文档流程一致。

## 流程简介

本文档介绍了如何调用客户管理接口创建CRM客户数据等流程。首先创建一个企业内部应用，再使用客户管理提供的API，实现获取客户对象的元数据、创建CRM客户数据、更新CRM客户数据、删除CRM客户数据、批量获取客户数据流程。

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](0003-add-api-permission.md)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五：调用服务端客户管理相关API。

1. 调用服务端API-[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取客户管理客户元数据信息。
2. 客户管理创建客户数据：

   - 调用服务端API-[创建个人或企业客户数据](1348-add-crm-personal-customers.md)接口，进行客户数据的创建，获取客户数据`instanceId`。
   - 调用服务端API-[批量新增个人或企业客户数据](1351-add-multiple-relationship-data-in-batches.md)接口，进行客户数据的批量创建，获取多个客户数据`instanceId`。
3. 根据客户数据`instanceId`进行客户数据管理操作：

   - 根据客户数据`instanceId`，调用服务端API-[更新个人或企业客户数据](1349-update-crm-personal-customers.md)接口，进行更新客户数据。
   - 根据客户数据`instanceId`，调用服务端API-[批量更新个人或企业客户数据](1352-update-multiple-relational-data-tables-at-a-time.md)接口，进行更新客户数据。
   - 根据客户数据`instanceId`，调用服务端API-[删除个人或企业客户数据](1350-delete-crm-personal-customer.md)接口，进行删除客户数据。
   - 根据客户数据`instanceId`，调用服务端API-[批量获取个人或企业客户数据](1353-acquire-crm-individual-customers-in-batches.md)接口，进行批量获取客户数据信息。
4. 客户管理数据查询操作：

   - 调用服务端API-[获取全量个人或企业客户数据](1354-crm-obtains-all-private-sea-customer-data.md)接口，获取全部客户数据。
   - 调用服务端API-[根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口，查询符合指定条件的客户数据。
   - 调用服务端API-[获取个人或企业客户查重字段](1356-obtain-duplicate-check-fields.md)接口，获取查重字段数据。

## 步骤一：创建企业内部应用

> **[!NOTE]**
>
> 如果已有企业内部应用，可直接使用已有应用，可忽略此步骤。

1. 登录[开发者后台](https://open-dev.dingtalk.com/#/)， 创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

   ![1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1799054871/p527245.png)
2. 填写应用的基本信息，然后单击**确定创建**。
3. 创建成功后，添加**网页应用**，如何添加可参考[添加应用能力](../01-XOnnmGCTbn-开发指南/0007-create-application.md#e052f533e1kd3)。

## 步骤二：获取AppKey和AppSecret

在**凭证与基础信息**中，获取AppKey和AppSecret（用于后续换取access\_token，此凭证需严格保密，切勿泄露至前端或客户端代码中）。

![3](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4940154871/p527248.png)

## 步骤三：添加接口权限

[申请客户管理接口权限](0003-add-api-permission.md)。搜索“CRM”，申请相应的权限。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6617954871/p499403.png)

## 步骤四：获取应用访问凭证accessToken

根据步骤二中的AppKey和AppSecret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

> **[!NOTE]**
>
> 以下接口均使用新版服务端API接口，服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。

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

## 步骤五：调用服务端客户管理相关API

1. 调用服务端API-[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取个人或企业客户的元数据信息。

   ```
   public void getCustomerObjectMeta() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           DescribeCrmPersonalCustomerObjectMetaHeaders describeCrmPersonalCustomerObjectMetaHeaders = new DescribeCrmPersonalCustomerObjectMetaHeaders();
           describeCrmPersonalCustomerObjectMetaHeaders.xAcsDingtalkAccessToken = "accessToken";
           DescribeCrmPersonalCustomerObjectMetaRequest describeCrmPersonalCustomerObjectMetaRequest = new DescribeCrmPersonalCustomerObjectMetaRequest()
                   .setRelationType("crm_customer");
           try {
               DescribeCrmPersonalCustomerObjectMetaResponse describeCrmPersonalCustomerObjectMetaResponse = client.describeCrmPersonalCustomerObjectMetaWithOptions(describeCrmPersonalCustomerObjectMetaRequest, describeCrmPersonalCustomerObjectMetaHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(describeCrmPersonalCustomerObjectMetaResponse.getBody()));
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
2. 客户管理创建客户数据：

   - 调用服务端API-[创建个人或企业客户数据](https://open.dingtalk.com/document/orgapp/add-crm-personal-customers)接口，进行客户数据的创建，获取客户数据`instanceId`。

     ```
      public void createCustomers() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             AddCrmPersonalCustomerHeaders addCrmPersonalCustomerHeaders = new AddCrmPersonalCustomerHeaders();
             addCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "accessToken";
             AddCrmPersonalCustomerRequest.AddCrmPersonalCustomerRequestPermission permission = new AddCrmPersonalCustomerRequest.AddCrmPersonalCustomerRequestPermission()
                     .setOwnerStaffIds(java.util.Arrays.asList(
                             "ma*******75"

                     ))
                     .setParticipantStaffIds(java.util.Arrays.asList(
                             "0147*********041"
                     ));
             Map<String,String> data = new HashMap<>();
             //客户名称字段必须填写
             data.put("customer_name","小钉");
             data.put("customer_follow_up_status","新获取");
             data.put("address","浙江省,杭州市,西湖区");
             data.put("TextField-714256","三墩镇,XX路XX号XX大厦XX室");
             data.put("MultiTagField-1437d010","客户");
             data.put("MultiTagField-e63401a9","重要");
             data.put("MultiTagField-5c48fb1d","洽谈");
             AddCrmPersonalCustomerRequest addCrmPersonalCustomerRequest = new AddCrmPersonalCustomerRequest()
                     .setCreatorUserId("ma*******75")
                     .setCreatorNick("小七")
                     .setData(data)
                     .setPermission(permission)
                     .setRelationType("crm_customer")
                     .setSkipDuplicateCheck(false);
     //                .setAction("publicDraw");
             try {
                 AddCrmPersonalCustomerResponse addCrmPersonalCustomerResponse = client.addCrmPersonalCustomerWithOptions(addCrmPersonalCustomerRequest, addCrmPersonalCustomerHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(addCrmPersonalCustomerResponse.getBody()));
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
   - 调用服务端API-[批量新增个人或企业客户数据](https://open.dingtalk.com/document/orgapp/add-multiple-relationship-data-in-batches)接口，进行客户数据的批量创建，获取多个客户数据`instanceId`。

     ```
     public void batchAddCustomers() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             BatchAddRelationDatasHeaders batchAddRelationDatasHeaders = new BatchAddRelationDatasHeaders();
             batchAddRelationDatasHeaders.xAcsDingtalkAccessToken = "<your access token>";
             BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListRelationPermissionDTO relationList0RelationPermissionDTO = new BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListRelationPermissionDTO()
                     .setPrincipalUserIds(java.util.Arrays.asList(
                             "manager0123"
                     ))
                     .setParticipantUserIds(java.util.Arrays.asList(
                             "manager0123"
                     ));
             java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                     new TeaPair("key", "1")
             );
             BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListBizDataList relationList0BizDataList0 = new BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationListBizDataList()
                     .setKey("customer_name")
                     .setValue("XX有限公司");
             BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationList relationList0 = new BatchAddRelationDatasRequest.BatchAddRelationDatasRequestRelationList()
                     .setBizDataList(java.util.Arrays.asList(
                             relationList0BizDataList0
                     ))
                     .setBizExtMap(relationList0BizExtMap)
                     .setRelationPermissionDTO(relationList0RelationPermissionDTO);
             BatchAddRelationDatasRequest batchAddRelationDatasRequest = new BatchAddRelationDatasRequest()
                     .setRelationType("crm_customer")
                     .setOperatorUserId("manager021a")
                     .setSkipDuplicateCheck(false)
                     .setRelationList(java.util.Arrays.asList(
                             relationList0
                     ));
             try {
                 BatchAddRelationDatasResponse batchAddRelationDatasResponse = client.batchAddRelationDatasWithOptions(batchAddRelationDatasRequest, batchAddRelationDatasHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(batchAddRelationDatasResponse.getBody()));
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
3. 根据客户数据instanceId进行客户数据管理操作：

   - 根据客户数据`instanceId`，调用服务端API-[更新个人或企业客户数据](1349-update-crm-personal-customers.md)接口，进行更新单个客户数据。

     ```
       public void updateCustomer() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             UpdateCrmPersonalCustomerHeaders updateCrmPersonalCustomerHeaders = new UpdateCrmPersonalCustomerHeaders();
             updateCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "accessToken";
             UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission permission = new UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission()
                     .setOwnerStaffIds(java.util.Arrays.asList(
                             "ma*******75"
                     ))
                     .setParticipantStaffIds(java.util.Arrays.asList(
                             "014****************41"
                     ));
             Map<String,String> data = new HashMap<>();
             data.put("customer_name","小钉");
             data.put("customer_follow_up_status","新获取");
             data.put("address","北京市,朝阳区,望京东");
             data.put("TextField-714256","阿******座");
             data.put("MultiTagField-1437d010","客户");
             data.put("MultiTagField-e63401a9","重要");
             data.put("MultiTagField-5c48fb1d","洽谈");
             UpdateCrmPersonalCustomerRequest updateCrmPersonalCustomerRequest = new UpdateCrmPersonalCustomerRequest()
                     .setInstanceId("22GX******************2641")
                     .setModifierUserId("ma******75")
                     .setData(data)
                     .setModifierNick("小七")
                     .setPermission(permission)
                     .setRelationType("crm_customer")
                     .setSkipDuplicateCheck(false);
     //                .setAction("publicDraw");
             try {
                 UpdateCrmPersonalCustomerResponse updateCrmPersonalCustomerResponse = client.updateCrmPersonalCustomerWithOptions(updateCrmPersonalCustomerRequest, updateCrmPersonalCustomerHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(updateCrmPersonalCustomerResponse.getBody()));
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
   - 根据客户数据`instanceId`，调用服务端API-[批量更新个人或企业客户数据](1352-update-multiple-relational-data-tables-at-a-time.md)接口，进行批量更新多个客户数据。

     ```
       public void batchUpdateCustomers() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             BatchUpdateRelationDatasHeaders batchUpdateRelationDatasHeaders = new BatchUpdateRelationDatasHeaders();
             batchUpdateRelationDatasHeaders.xAcsDingtalkAccessToken = "<your access token>";
             java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                     new TeaPair("key", "1")
             );
             BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationListBizDataList relationList0BizDataList0 = new BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationListBizDataList()
                     .setKey("customer_name")
                     .setValue("XX有限公司");
             BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList relationList0 = new BatchUpdateRelationDatasRequest.BatchUpdateRelationDatasRequestRelationList()
                     .setBizDataList(java.util.Arrays.asList(
                             relationList0BizDataList0
                     ))
                     .setBizExtMap(relationList0BizExtMap)
                     .setRelationId("fasdg8i814-0afsd");
             BatchUpdateRelationDatasRequest batchUpdateRelationDatasRequest = new BatchUpdateRelationDatasRequest()
                     .setRelationType("crm_customer")
                     .setOperatorUserId("manager021a")
                     .setSkipDuplicateCheck(false)
                     .setRelationList(java.util.Arrays.asList(
                             relationList0
                     ));
             try {
                 BatchUpdateRelationDatasResponse batchUpdateRelationDatasResponse = client.batchUpdateRelationDatasWithOptions(batchUpdateRelationDatasRequest, batchUpdateRelationDatasHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(batchUpdateRelationDatasResponse.getBody()));
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
   - 根据客户数据`instanceId`，调用服务端API-[删除个人或企业客户数据](1350-delete-crm-personal-customer.md)接口，进行删除客户数据。

     ```
      public void deleteCustomerData() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             DeleteCrmPersonalCustomerHeaders deleteCrmPersonalCustomerHeaders = new DeleteCrmPersonalCustomerHeaders();
             deleteCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "accessToken";
             DeleteCrmPersonalCustomerRequest deleteCrmPersonalCustomerRequest = new DeleteCrmPersonalCustomerRequest()
                     .setRelationType("crm_customer")
                     .setCurrentOperatorUserId("m********5");
             try {
                 DeleteCrmPersonalCustomerResponse deleteCrmPersonalCustomerResponse = client.deleteCrmPersonalCustomerWithOptions("22GXvbkITYCMkIKBDo9YJA08811665212641", deleteCrmPersonalCustomerRequest, deleteCrmPersonalCustomerHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(deleteCrmPersonalCustomerResponse.getBody()));
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
     ```
   - 根据客户数据`instanceId`，调用服务端API-[批量获取个人或企业客户数据](1353-acquire-crm-individual-customers-in-batches.md)接口，进行批量获取客户数据信息。

     ```
     public void  getCustomersByInstanceIds() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             ListCrmPersonalCustomersHeaders listCrmPersonalCustomersHeaders = new ListCrmPersonalCustomersHeaders();
             listCrmPersonalCustomersHeaders.xAcsDingtalkAccessToken = "accessToken";
             ListCrmPersonalCustomersRequest listCrmPersonalCustomersRequest = new ListCrmPersonalCustomersRequest()
                     .setCurrentOperatorUserId("m*******5")
                     .setBody(java.util.Arrays.asList(
                             "FPG*****************4161"
                     ));
             try {
                 ListCrmPersonalCustomersResponse listCrmPersonalCustomersResponse = client.listCrmPersonalCustomersWithOptions(listCrmPersonalCustomersRequest, listCrmPersonalCustomersHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(listCrmPersonalCustomersResponse.getBody()));
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
4. 客户管理数据查询操作：

   - 调用服务端API-[获取全量个人或企业客户数据](1354-crm-obtains-all-private-sea-customer-data.md)接口，获取全部客户数据。

     ```
      public void queryAllCustomers() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             QueryAllCustomerHeaders queryAllCustomerHeaders = new QueryAllCustomerHeaders();
             queryAllCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
             QueryAllCustomerRequest queryAllCustomerRequest = new QueryAllCustomerRequest()
                     .setOperatorUserId("ding_userid")
                     .setMaxResults(100L)
                     .setNextToken("")
                     .setObjectType("crm_customer");
             try {
                 QueryAllCustomerResponse queryAllCustomerResponse = client.queryAllCustomerWithOptions(queryAllCustomerRequest, queryAllCustomerHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(queryAllCustomerResponse.getBody()));
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
   - 调用服务端API-[根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口，查询符合指定条件的客户数据。

     ```
     public void queryCustomers() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             QueryCrmPersonalCustomerHeaders queryCrmPersonalCustomerHeaders = new QueryCrmPersonalCustomerHeaders();
             queryCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
             QueryCrmPersonalCustomerRequest queryCrmPersonalCustomerRequest = new QueryCrmPersonalCustomerRequest()
                     .setCurrentOperatorUserId("2665246xxx")
                     .setRelationType("crm_customer_personal")
                     .setNextToken("0")
                     .setMaxResults(10)
                     .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}");
             try {
                 QueryCrmPersonalCustomerResponse queryCrmPersonalCustomerResponse = client.queryCrmPersonalCustomerWithOptions(queryCrmPersonalCustomerRequest, queryCrmPersonalCustomerHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(queryCrmPersonalCustomerResponse.getBody()));
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
   - 调用服务端API-[获取个人或企业客户查重字段](1356-obtain-duplicate-check-fields.md)接口，获取查重字段数据。

     ```
     public void getRelationUkSetting() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             GetRelationUkSettingHeaders getRelationUkSettingHeaders = new GetRelationUkSettingHeaders();
             getRelationUkSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
             GetRelationUkSettingRequest getRelationUkSettingRequest = new GetRelationUkSettingRequest()
                     .setRelationType("crm_customer");
             try {
                 GetRelationUkSettingResponse relationUkSettingWithOptions = client.getRelationUkSettingWithOptions(getRelationUkSettingRequest, getRelationUkSettingHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(relationUkSettingWithOptions.getBody()));
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
