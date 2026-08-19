---
title: "CRM联系人数据操作流程"
source_url: "https://open.dingtalk.com/document/development/crm-contact-data-operation-process"
namespace: "development"
slug: "crm-contact-data-operation-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > CRM联系人数据操作流程"
doc_id: "qd944mJZCf"
updated_at: "2026-07-21 09:26:10"
---

> Source: https://open.dingtalk.com/document/development/crm-contact-data-operation-process
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 使用教程 > CRM联系人数据操作流程
> Updated: 2026-07-21 09:26:10

# CRM联系人数据操作流程

本文档介绍了CRM联系人数据操作流程。

## 流程简介

本文档介绍了如何调用客户管理接口创建CRM联系人数据等流程。首先创建一个企业内部应用，再使用客户管理提供的API，实现获取联系人对象的元数据、创建CRM联系人数据、更新CRM联系人数据、删除CRM联系人数据、批量获取联系人数据流程。

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](0003-add-api-permission.md)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五：调用服务端联系人相关API。

1. 调用服务端API-[获取联系人的元数据](1364-gets-the-metadata-description-of-a-crm-contact-object.md)接口，获取客户管理联系人元数据信息。
2. 调用服务端API-[批量新增联系人数据](1361-add-contact-data-in-batches.md)接口，进行联系人数据的创建，获取联系人数据`instanceId`（部分接口可能定义为relationId或data\_id，含义相同）。
3. 根据联系人数据`instanceId`进行联系人数据管理操作。

   - 根据联系人数据`instanceId`，调用服务端API-[批量修改联系人数据](1363-modify-contact-data-in-batches.md)接口，进行更新联系人数据。
   - 根据联系人数据`instanceId`，调用服务端API-[删除联系人数据](1362-delete-crm-contact.md)接口，进行删除联系人数据。
   - 根据联系人数据`instanceId`，调用服务端API-[按照ID列表批量获取联系人数据](1366-retrieves-contact-data-in-batches-based-on-the-id-list.md)接口，进行批量获取联系人数据信息。
4. 调用服务端API-[根据指定条件查询联系人数据](1365-api-getcontacts.md)接口，查询符合指定条件的联系人数据。

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

[申请客户管理接口权限](0003-add-api-permission.md)。搜索“CRM”，申请相应的权限。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6617954871/p499403.png)

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

## 步骤五：调用服务端联系人相关API

1. 调用服务端API-[获取联系人的元数据](1364-gets-the-metadata-description-of-a-crm-contact-object.md)接口，获取客户管理联系人元数据信息。

   ```
   public void getContactObjectMeta() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/contact/describe");
           OapiCrmObjectmetaContactDescribeRequest req = new OapiCrmObjectmetaContactDescribeRequest();
           OapiCrmObjectmetaContactDescribeResponse rsp = client.execute(req, accessToken);
           System.out.println(rsp.getBody());
   }
   ```
2. 调用服务端API-[批量新增联系人数据](1361-add-contact-data-in-batches.md)接口，进行联系人数据的创建，获取联系人数据`instanceId`（部分接口可能定义为relationId或data\_id，含义相同）。

   ```
   public void batchAddContacts() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
           BatchAddContactsHeaders batchAddContactsHeaders = new BatchAddContactsHeaders();
           batchAddContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
           java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                   new TeaPair("key", "{}")
           );
           BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList0 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                   .setKey("contact_name")
                   .setValue("XX有限公司");
           BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList1 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                   .setKey("contact_related_customer")
                   .setValue("[\"XX公司\"]")
                   .setExtendValue("{\"list\":[{\"instanceId\":\"customerInstanceId\"}]}");
           BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList relationList0BizDataList2 = new BatchAddContactsRequest.BatchAddContactsRequestRelationListBizDataList()
                   .setKey("contact_phone")
                   .setValue("185xxxxxxxx");
           BatchAddContactsRequest.BatchAddContactsRequestRelationList relationList0 = new BatchAddContactsRequest.BatchAddContactsRequestRelationList()
                   .setBizDataList(java.util.Arrays.asList(
                           relationList0BizDataList0,
                           relationList0BizDataList1,
                           relationList0BizDataList2
                   ))
                   .setBizExtMap(relationList0BizExtMap);
           BatchAddContactsRequest batchAddContactsRequest = new BatchAddContactsRequest()
                   .setOperatorUserId("manager021a")
                   .setRelationList(java.util.Arrays.asList(
                           relationList0
                   ));
           try {
               BatchAddContactsResponse batchAddContactsResponse = client.batchAddContactsWithOptions(batchAddContactsRequest, batchAddContactsHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(batchAddContactsResponse.getBody()));
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
3. 根据联系人数据`instanceId`进行联系人数据管理操作。

   - 根据联系人数据instanceId，调用服务端API-[批量修改联系人数据](1363-modify-contact-data-in-batches.md)接口，进行更新联系人数据。

     ```
      public void  batchUpdateContacts() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             BatchUpdateContactsHeaders batchUpdateContactsHeaders = new BatchUpdateContactsHeaders();
             batchUpdateContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
             java.util.Map<String, String> relationList0BizExtMap = TeaConverter.buildMap(
                     new TeaPair("key", "{}")
             );
             BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationListBizDataList relationList0BizDataList0 = new BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationListBizDataList()
                     .setKey("TextField_71U51A")
                     .setValue("XX有限公司")
                     .setExtendValue("{}");
             BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationList relationList0 = new BatchUpdateContactsRequest.BatchUpdateContactsRequestRelationList()
                     .setBizDataList(java.util.Arrays.asList(
                             relationList0BizDataList0
                     ))
                     .setBizExtMap(relationList0BizExtMap)
                     .setRelationId("fasdg8i814-0afsd");
             BatchUpdateContactsRequest batchUpdateContactsRequest = new BatchUpdateContactsRequest()
                     .setOperatorUserId("manager021a")
                     .setRelationList(java.util.Arrays.asList(
                             relationList0
                     ));
             try {
                 BatchUpdateContactsResponse batchUpdateContactsResponse = client.batchUpdateContactsWithOptions(batchUpdateContactsRequest, batchUpdateContactsHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(batchUpdateContactsResponse.getBody()));
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
   - 根据联系人数据`instanceId`，调用服务端API-[删除联系人数据](1362-delete-crm-contact.md)接口，进行删除联系人数据。

     ```
      public void deleteContact() throws Exception {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/delete");
             OapiCrmObjectdataContactDeleteRequest req = new OapiCrmObjectdataContactDeleteRequest();
             req.setOperatorUserid("user01");
             req.setDataId("INST_XX");
             OapiCrmObjectdataContactDeleteResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
      }
     ```
   - 根据联系人数据`instanceId`，调用服务端API-[按照ID列表批量获取联系人数据](1366-retrieves-contact-data-in-batches-based-on-the-id-list.md)接口，进行批量获取联系人数据信息。

     ```
      public void getContactsByInstanceIds() throws Exception {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list");
             OapiCrmObjectdataContactListRequest req = new OapiCrmObjectdataContactListRequest();
             req.setCurrentOperatorUserid("manager1");
             req.setDataIdList("nst_Id1, inst_Id2");
             OapiCrmObjectdataContactListResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
      }
     ```
4. 调用服务端API-[根据指定条件查询联系人数据](1365-api-getcontacts.md)接口，查询符合指定条件的联系人数据。

   ```
   public void queryContacts() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/query");
           OapiCrmObjectdataContactQueryRequest req = new OapiCrmObjectdataContactQueryRequest();
           req.setCurrentOperatorUserid("user01");
           req.setCursor("0");
           req.setPageSize(100L);
           req.setProviderCorpid("dingxxx");
           req.setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"filterType\":\"EQ\",\"value\":\"18000****000\"},{\"fieldId\":\"contact_related_customer\",\"filterType\":\"EQ\",\"value\":\"INST-XXX\"}]}]}");
           OapiCrmObjectdataContactQueryResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
