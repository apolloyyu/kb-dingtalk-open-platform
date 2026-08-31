---
title: "CRM自定义对象数据操作流程"
source_url: "https://open.dingtalk.com/document/development/crm-custom-object-data-operation-process"
namespace: "development"
slug: "crm-custom-object-data-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > CRM自定义对象数据操作流程"
doc_id: "CtYgKI5kQ2"
updated_at: "2026-07-21 09:26:13"
---

> Source: https://open.dingtalk.com/document/development/crm-custom-object-data-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 使用教程 > CRM自定义对象数据操作流程
> Updated: 2026-07-21 09:26:13

# CRM自定义对象数据操作流程

本文档介绍了CRM自定义对象数据操作流程。

## 流程简介

本文档介绍了如何调用客户管理接口创建CRM自定义对象数据等流程。首先创建一个企业内部应用，再使用客户管理提供的API，实现获取自定义对象对象的元数据、创建CRM自定义对象数据、更新CRM自定义对象数据、删除CRM自定义对象数据、批量获取自定义对象数据、根据指定条件查询自定义对象数据流程。

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](https://open.dingtalk.com/document/orgapp/apply-for-crm-api-permission)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五：调用服务端自定义对象相关API。

1. 调用服务端API-[获取自定义对象的元数据](1376-get-metadata-description-of-crm-custom-object.md)接口，获取客户管理自定义对象的元数据信息。
2. 调用服务端API-[创建CRM自定义对象数据](1373-dingtalk-paas-master-create-custom-crm-object-data.md)接口，进行自定义对象数据的创建，获取自定义对象数据`instanceId`。
3. 根据自定义对象数据`instanceId`进行自定义对象数据管理操作。

   - 根据自定义对象数据`instanceId`，调用服务端API-[更新自定义对象数据](1375-crm-master-data-opens-interface-for-updating-custom-object-data.md)接口，进行更新自定义对象数据。
   - 根据自定义对象数据`instanceId`，调用服务端API-[删除CRM自定义对象数据](1374-delete-crm-custom-object-data.md)接口，进行删除自定义对象数据。
   - 根据自定义对象数据`instanceId`，调用服务端API-[按照ID列表批量获取CRM自定义表单数据](1378-retrieves-custom-crm-forms-from-the-id-list.md)接口，进行批量获取自定义对象数据信息。
4. 调用服务端API-[根据指定条件查询自定义对象数据](1377-api-getobjectdata.md)接口，查询符合指定条件的自定义对象数据。

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

## 步骤五：调用服务端自定义对象相关API

1. 调用服务端API-[获取自定义对象的元数据](1376-get-metadata-description-of-crm-custom-object.md)接口，获取客户管理自定义对象的元数据信息。

   ```
   public void getCustomizedObjectMeta() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/describe");
           OapiCrmObjectmetaDescribeRequest req = new OapiCrmObjectmetaDescribeRequest();
           req.setName("PROC-EF1xxxx");
           OapiCrmObjectmetaDescribeResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
2. 调用服务端API-[创建CRM自定义对象数据](1373-dingtalk-paas-master-create-custom-crm-object-data.md)接口，进行自定义对象数据的创建，获取自定义对象数据`instanceId`。

   ```
   public void createCustomizedData() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create");
           OapiCrmObjectdataCustomobjectCreateRequest req = new OapiCrmObjectdataCustomobjectCreateRequest();
           ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
           objectDataInstanceVo.setCreatorUserid("user01");
           objectDataInstanceVo.setData("{\"TextField-xxxxxx\":\"李xx\"}");
           objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
           DataPermissionVo dataPermissionVo = new DataPermissionVo();
           dataPermissionVo.setParticipantUserids(Arrays.asList("user01", "user02"));
           objectDataInstanceVo.setPermission(dataPermissionVo);
           objectDataInstanceVo.setFormCode("PROC-A1xxxx");
           req.setInstance(objectDataInstanceVo);
           OapiCrmObjectdataCustomobjectCreateResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
3. 根据自定义对象数据`instanceId`进行自定义对象数据管理操作。

   - 根据自定义对象数据instanceId，调用服务端API-[更新自定义对象数据](1375-crm-master-data-opens-interface-for-updating-custom-object-data.md)接口，进行更新自定义对象数据。

     ```
      public void updateCustomizedData() throws Exception {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update");
             OapiCrmObjectdataCustomobjectUpdateRequest req = new OapiCrmObjectdataCustomobjectUpdateRequest();
             ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
             DataPermissionVo dataPermissionVo = new DataPermissionVo();
             dataPermissionVo.setParticipantUserids(Arrays.asList("user01", "user02"));
             objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
             objectDataInstanceVo.setPermission(dataPermissionVo);
             objectDataInstanceVo.setInstanceId("INST_XX");
             objectDataInstanceVo.setFormCode("PROC-EFxxxx");
             objectDataInstanceVo.setModifierUserid("user01");
             objectDataInstanceVo.setModifierNick("张xx");
             req.setInstance(objectDataInstanceVo);
             OapiCrmObjectdataCustomobjectUpdateResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
     }
     ```
   - 根据自定义对象数据`instanceId`，调用服务端API-[删除CRM自定义对象数据](1374-delete-crm-custom-object-data.md)接口，进行删除自定义对象数据。

     ```
      public void deleteCustomizedData() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataHeaders deleteCrmCustomObjectDataHeaders = new com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataHeaders();
             deleteCrmCustomObjectDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
             com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataRequest deleteCrmCustomObjectDataRequest = new com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataRequest()
                     .setFormCode("PROC-EFxxxx");
             try {
                 DeleteCrmCustomObjectDataResponse deleteCrmCustomObjectDataResponse = client.deleteCrmCustomObjectDataWithOptions("INST_XX", deleteCrmCustomObjectDataRequest, deleteCrmCustomObjectDataHeaders, new RuntimeOptions());
                 System.out.println(JSON.toJSONString(deleteCrmCustomObjectDataResponse.getBody()));
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
   - 根据自定义对象数据`instanceId`，调用服务端API-[按照ID列表批量获取CRM自定义表单数据](1378-retrieves-custom-crm-forms-from-the-id-list.md)接口，进行批量获取自定义对象数据信息。

     ```
      public void getCustomizedDatasByInstanceIds() throws Exception {
             Config config = new Config();
             config.protocol = "https";
             config.regionId = "central";
             com.aliyun.dingtalkcrm_1_0.Client client = new com.aliyun.dingtalkcrm_1_0.Client(config);
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/list");
             OapiCrmObjectdataListRequest req = new OapiCrmObjectdataListRequest();
             req.setCurrentOperatorUserid("user01");
             req.setDataIdList("INST_XX1,INST_XX2");
             req.setName("PROC-EFxxxx");
             OapiCrmObjectdataListResponse rsp = client.execute(req, access_token);
             System.out.println(rsp.getBody());
      }
     ```
4. 调用服务端API-[根据指定条件查询自定义对象数据](1377-api-getobjectdata.md)接口，查询符合指定条件的自定义对象数据。

   ```
    public void queryCustomizedDatas() throws Exception {
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
