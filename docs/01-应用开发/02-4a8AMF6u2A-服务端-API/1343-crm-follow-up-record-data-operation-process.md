---
title: "CRM跟进记录数据操作流程"
source_url: "https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process"
namespace: "development"
slug: "crm-follow-up-record-data-operation-process"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 使用教程 > CRM跟进记录数据操作流程"
doc_id: "d3t5nVXO1X"
updated_at: "2026-07-21 09:26:11"
---

> Source: https://open.dingtalk.com/document/development/crm-follow-up-record-data-operation-process
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 使用教程 > CRM跟进记录数据操作流程
> Updated: 2026-07-21 09:26:11

# CRM跟进记录数据操作流程

本文档介绍了CRM跟进记录数据操作流程。

## 流程简介

本文档介绍了如何调用客户管理接口查询CRM跟进记录数据等流程。首先创建一个企业内部应用，再使用客户管理提供的API，实现获取跟进记录对象的元数据、根据指定条件查询跟进记录数据、批量获取跟进记录数据流程。

步骤一：登录[开发者后台](https://open-dev.dingtalk.com/#/)，创建[企业内部应用](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。

步骤二：获取AppKey和AppSecret。

步骤三：[申请客户管理接口权限](0003-add-api-permission.md)。搜索“CRM”，申请相应的权限。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

步骤五：调用服务端跟进记录相关API。

1. 调用服务端API-[获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md)接口，获取客户管理跟进记录元数据信息。
2. 调用服务端API-[根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md)接口，查询符合指定条件的跟进记录数据。
3. 调用服务端API-[根据ID列表批量获取跟进记录数据](1372-dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you.md)接口，查询多个跟进记录数据。

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
public void  getAccessToken() throws ApiException {
        DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
        OapiGettokenRequest request = new OapiGettokenRequest();
        request.setAppkey("dingmp*****lxhgn");
        request.setAppsecret("9G_O44ATuwq9jrz3o********0t1JDf0Qq3neNDLmxamBkhgGIO");
        request.setHttpMethod("GET");
        OapiGettokenResponse response = client.execute(request);
        System.out.println(response.getBody());
    }
```

## 步骤五：调用服务端跟进记录相关API

1. 调用服务端API-[获取跟进记录对象的元数据](1367-obtains-the-metadata-description-of-the-crm-follow-up-record-object.md)接口，获取客户管理跟进记录元数据信息。

   ```
   public void customerFollowRecordObjectMeta() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/followrecord/describe");
           OapiCrmObjectmetaFollowrecordDescribeRequest req = new OapiCrmObjectmetaFollowrecordDescribeRequest();
           OapiCrmObjectmetaFollowrecordDescribeResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
2. 调用服务端API-[根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md)接口，查询符合指定条件的跟进记录数据。

   ```
   public void queryCustomerFollowRecord() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query");
           OapiCrmObjectdataFollowrecordQueryRequest req = new OapiCrmObjectdataFollowrecordQueryRequest();
           req.setCurrentOperatorUserid("user01");
           req.setCursor("0");
           req.setPageSize(100L);
           OapiCrmObjectdataFollowrecordQueryResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
3. 调用服务端API-[根据ID列表批量获取跟进记录数据](1372-dingtalk-the-primary-data-of-apsara-stack-agility-paas-allows-you.md)接口，查询多个跟进记录数据。

   ```
   public void getCustomerFollowRecordByInstanceIds() throws Exception {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/list");
           OapiCrmObjectdataFollowrecordListRequest req = new OapiCrmObjectdataFollowrecordListRequest();
           req.setCurrentOperatorUserid("user01");
           req.setDataIdList("INST_XX1,INST_XX2");
           OapiCrmObjectdataFollowrecordListResponse rsp = client.execute(req, access_token);
           System.out.println(rsp.getBody());
   }
   ```
