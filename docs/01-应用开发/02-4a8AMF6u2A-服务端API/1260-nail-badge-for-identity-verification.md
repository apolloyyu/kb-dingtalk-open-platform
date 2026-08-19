---
title: "钉工牌实现用户访客码创建"
source_url: "https://open.dingtalk.com/document/development/nail-badge-for-identity-verification"
namespace: "development"
slug: "nail-badge-for-identity-verification"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 使用教程 > 钉工牌实现用户访客码创建"
doc_id: "5tf0FdzBcK"
updated_at: "2026-07-20 09:21:56"
---

> Source: https://open.dingtalk.com/document/development/nail-badge-for-identity-verification
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 使用教程 > 钉工牌实现用户访客码创建
> Updated: 2026-07-20 09:21:56

# 钉工牌实现用户访客码创建

本文档介绍了如何调用钉工牌接口实现用户访客码创建的相关流程。首先创建一个企业内部应用，再使用钉工牌提供的API，实现配置企业钉工牌、创建钉工牌电子码、更新钉工牌电子码流程。

## 预期效果

![钉工牌访客码](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6150154871/p523471.png)

## 流程简介

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请钉工牌相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端钉工牌相关API。

1. 调用服务端API-[配置企业钉工牌](1261-save-dingtalk-enterprise-instance.md)接口，为企业开通钉工牌电子码。
2. 调用服务端API-[创建钉工牌电子码](1262-create-a-badge-user-instance.md)接口，进行用户访客码的创建，获取用户码codeId。
3. 根据用户码codeId，调用服务端API-[更新钉工牌电子码](1263-update-dingtalk-user-instance.md)接口，进行用户访客码的更新。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`Badge.Common.Write`和`Badge.Common.Read`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

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

## 步骤四：调用服务端钉工牌相关API

1. 调用服务端API-[配置企业钉工牌](1261-save-dingtalk-enterprise-instance.md)接口，为企业开通钉工牌访客码。

   > **[!NOTE]**
   >
   > [配置企业钉工牌](1261-save-dingtalk-enterprise-instance.md)中参数codeIdentity选择访客码标识**DT\_VISITOR**。

   ```
   public void badgeConfigure() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkbadge_1_0.Client client = new com.aliyun.dingtalkbadge_1_0.Client(config);
           SaveBadgeCodeCorpInstanceHeaders saveBadgeCodeCorpInstanceHeaders = new SaveBadgeCodeCorpInstanceHeaders();
           saveBadgeCodeCorpInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           Map<String,String> map = new HashMap<>();
           map.put("supportRelateAlipay","true");
           SaveBadgeCodeCorpInstanceRequest saveBadgeCodeCorpInstanceRequest = new SaveBadgeCodeCorpInstanceRequest()
                   .setCodeIdentity("DT_VISITOR")
                   .setCorpId("ding16b241fd05c8******5d8e4f7c288")
                   .setStatus("OPEN")
                   .setExtInfo(map);
           try {
               SaveBadgeCodeCorpInstanceResponse saveBadgeCodeCorpInstanceResponse = client.saveBadgeCodeCorpInstanceWithOptions(saveBadgeCodeCorpInstanceRequest, saveBadgeCodeCorpInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(saveBadgeCodeCorpInstanceResponse.getBody()));
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
2. 调用服务端API-[创建钉工牌电子码](1262-create-a-badge-user-instance.md)接口，进行用户访客码的创建，获取用户码codeId。

   > **[!NOTE]**
   >
   > [创建钉工牌电子码](1262-create-a-badge-user-instance.md)中参数codeIdentity选择访客码标识**DT\_VISITOR**。

   ```
   public void  createBadgeCode() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkbadge_1_0.Client client = new com.aliyun.dingtalkbadge_1_0.Client(config);
           CreateBadgeCodeUserInstanceHeaders createBadgeCodeUserInstanceHeaders = new CreateBadgeCodeUserInstanceHeaders();
           createBadgeCodeUserInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes availableTimes0 = new CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes()
                   .setGmtStart("2022-11-23 00:00:00")
                   .setGmtEnd("2022-11-24 00:00:00");

           Map<String,String> map = new HashMap<>();
           map.put("applicantName","小钉");
           map.put("applyTime","2022-11-23 00:00:00");
           map.put("visitorName","小七");
           map.put("visitorMobile","86-155****3240");
           CreateBadgeCodeUserInstanceRequest createBadgeCodeUserInstanceRequest = new CreateBadgeCodeUserInstanceRequest()
                   .setRequestId("202211231001")
                   .setCodeIdentity("DT_VISITOR")
                   .setCodeValue("badgeCode_11231001")
                   .setStatus("OPEN")
                   .setCorpId("ding16b241fd05c8******5d8e4f7c288")
                   .setUserCorpRelationType("INTERNAL_STAFF")
                   .setUserIdentity("manager7675")
                   .setGmtExpired("2022-11-24 00:00:00")
                   .setExtInfo(map)
                   .setAvailableTimes(java.util.Arrays.asList(
                           availableTimes0
                   ));
           try {
               CreateBadgeCodeUserInstanceResponse badgeCodeUserInstanceWithOptions = client.createBadgeCodeUserInstanceWithOptions(createBadgeCodeUserInstanceRequest, createBadgeCodeUserInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(badgeCodeUserInstanceWithOptions.getBody()));
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
3. 根据用户码codeId，调用服务端API-[更新钉工牌电子码](1263-update-dingtalk-user-instance.md)接口，进行用户访客码的更新。

   > **[!NOTE]**
   >
   > [更新钉工牌电子码](1263-update-dingtalk-user-instance.md)中参数codeIdentity选择访客码标识**DT\_VISITOR**。

   ```
   public void updateBadgeCode() throws Exception {
           Config config = new Config();
           config.protocol = "https";
           config.regionId = "central";
           com.aliyun.dingtalkbadge_1_0.Client client = new com.aliyun.dingtalkbadge_1_0.Client(config);
           com.aliyun.dingtalkbadge_1_0.models.UpdateBadgeCodeUserInstanceHeaders updateBadgeCodeUserInstanceHeaders = new com.aliyun.dingtalkbadge_1_0.models.UpdateBadgeCodeUserInstanceHeaders();
           updateBadgeCodeUserInstanceHeaders.xAcsDingtalkAccessToken = "accessToken";
           com.aliyun.dingtalkbadge_1_0.models.UpdateBadgeCodeUserInstanceRequest.UpdateBadgeCodeUserInstanceRequestAvailableTimes availableTimes0 = new com.aliyun.dingtalkbadge_1_0.models.UpdateBadgeCodeUserInstanceRequest.UpdateBadgeCodeUserInstanceRequestAvailableTimes()
                   .setGmtStart("2022-11-23 00:00:00")
                   .setGmtEnd("2022-11-25 00:00:00");

           Map<String,String> map = new HashMap<>();
           map.put("applicantName","小钉");
           map.put("applyTime","2022-11-23 00:00:00");
           map.put("visitorName","小七");
           map.put("visitorMobile","86-155****3240");

           com.aliyun.dingtalkbadge_1_0.models.UpdateBadgeCodeUserInstanceRequest updateBadgeCodeUserInstanceRequest = new com.aliyun.dingtalkbadge_1_0.models.UpdateBadgeCodeUserInstanceRequest()
                   .setCodeId("84a66edcf7065bc19a9169******888210a54611597e54e8_202211231001")
                   .setCodeIdentity("DT_VISITOR")
                   .setCodeValue("badgeCode_11231001")
                   .setStatus("OPEN")
                   .setCorpId("ding16b241fd05c8******5d8e4f7c288")
                   .setUserCorpRelationType("INTERNAL_STAFF")
                   .setUserIdentity("manager7675")
                   .setGmtExpired("2022-11-25 00:00:00")
                   .setExtInfo(map)
                   .setAvailableTimes(java.util.Arrays.asList(
                           availableTimes0
                   ));
           try {
               UpdateBadgeCodeUserInstanceResponse updateBadgeCodeUserInstanceResponse = client.updateBadgeCodeUserInstanceWithOptions(updateBadgeCodeUserInstanceRequest, updateBadgeCodeUserInstanceHeaders, new RuntimeOptions());
               System.out.println(JSON.toJSONString(updateBadgeCodeUserInstanceResponse.getBody()));
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
