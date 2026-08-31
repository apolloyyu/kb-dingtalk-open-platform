---
title: "获取员工签到信息"
source_url: "https://open.dingtalk.com/document/development/obtain-check-in-information"
namespace: "development"
slug: "obtain-check-in-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "签到 > 使用教程 > 获取员工签到信息"
doc_id: "ApvXyICPxJ"
updated_at: "2026-07-02 10:36:29"
---

> Source: https://open.dingtalk.com/document/development/obtain-check-in-information
> Path: 应用开发 / 服务端 API / 签到 > 使用教程 > 获取员工签到信息
> Updated: 2026-07-02 10:36:29

# 获取员工签到信息

本文档介绍了如何调用签到相关接口实现实时显示签到信息的相关流程。首先创建一个企业内部应用，再使用签到提供的API，实现获取员工的签到信息流程。

## 流程简介

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请签到相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端签到相关API。

1. 参会人员使用钉钉-签到应用进行签到。
2. 调用服务端API-[获取用户签到记录](0290-obtain-the-check-in-records-of-multiple-users.md)接口，获取员工的签到详情信息。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

默认开通，无需申请。

## 步骤三：获取应用访问凭证accessToken。

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)。

```
public void getAccessToken() throws ApiException {
        DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/gettoken");
        OapiGettokenRequest req = new OapiGettokenRequest();
        req.setAppkey("dingxxxxxxxxxhgn");
        req.setAppsecret("9G_xxxxxxxxxxxxxxx1JDf0Qq3nexxxxxxxxGIO");
        req.setHttpMethod("GET");
        OapiGettokenResponse rsp = client.execute(req);
        System.out.println(rsp.getBody());
    }
```

## 步骤四：调用服务端签到相关API。

1. 参与人员，可以使用钉钉签到进行签到。操作路径：打开钉钉客户端端 > 打开工作台 > 点击并打开签到。

   ![iShot2022-02-23 18](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9879592871/p408438.png)
2. 根据员工的userId，调用服务端API-[获取用户签到记录](0290-obtain-the-check-in-records-of-multiple-users.md)接口，获取员工签到的详情信息。

   ```
   public void checkinRecord() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/checkin/record/get");
           OapiCheckinRecordGetRequest req = new OapiCheckinRecordGetRequest();
           req.setUseridList("manager7675");
           req.setStartTime(1646064000000L);
           req.setEndTime(1646668800000L);
           req.setCursor(0L);
           req.setSize(100L);
           OapiCheckinRecordGetResponse rsp = client.execute(req, "accessToken");
           System.out.println(rsp.getBody());
       }
   ```
