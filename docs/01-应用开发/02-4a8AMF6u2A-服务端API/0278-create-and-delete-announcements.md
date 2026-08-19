---
title: "创建、获取、更新及删除公告"
source_url: "https://open.dingtalk.com/document/development/create-and-delete-announcements"
namespace: "development"
slug: "create-and-delete-announcements"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 使用教程 > 创建、获取、更新及删除公告"
doc_id: "DXnHG9nq6w"
updated_at: "2026-07-02 10:36:26"
---

> Source: https://open.dingtalk.com/document/development/create-and-delete-announcements
> Path: 应用开发 / 服务端API / 公告 > 使用教程 > 创建、获取、更新及删除公告
> Updated: 2026-07-02 10:36:26

# 创建、获取、更新及删除公告

本文档介绍了如何调用公告接口创建公告等流程。首先创建一个企业内部应用，再使用公告提供的API，实现创建公告、获取公告ID列表、获取公告详情、更新公告和删除公告流程。

## **预期效果**

公告展示效果如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6879592871/p499292.png)

## 流程简介

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请公告相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端公告相关API。

1. 调用服务端API-[创建公告](0279-create-an-enterprise-announcement.md)接口，进行公告创建。
2. 调用服务端API-[获取公告ID列表](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口，获取公告`blackboardId`。
3. 根据公告blackboardId进行公告管理。

   - 根据公告`blackboardId`，调用服务端API-[获取公告详情](1550-obtains-the-details-of-a-bulletin-that-is-not-deleted.md)接口，实现获取公告详情信息。
   - 根据公告`blackboardId`，调用服务端API-[更新公告](0281-modify-the-announcement-according-to-the-announcement-id.md)接口，实现更新公告内容。
   - 根据公告`blackboardId`，调用服务端API-[删除公告](0280-delete-announcements-based-on-the-announcement-id.md)接口，实现删除公告。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中分别输入`qyapi_blackboard_manage`和`qyapi_blackboard_read`，并申请权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。

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

## 步骤四：调用服务端公告相关API

1. 调用服务端API-[创建公告](0279-create-an-enterprise-announcement.md)接口，进行公告创建。

   ```
    public void createNotice() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/create");
           OapiBlackboardCreateRequest req = new OapiBlackboardCreateRequest();
           OapiBlackboardCreateRequest.OapiCreateBlackboardVo boardVoObj = new OapiBlackboardCreateRequest.OapiCreateBlackboardVo();
           boardVoObj.setOperationUserid("ma*******75");
           boardVoObj.setAuthor("小钉");
           boardVoObj.setPrivateLevel(0L);
           boardVoObj.setDing(true);
           OapiBlackboardCreateRequest.BlackboardReceiverOpenVo receiverOpenVoObj = new OapiBlackboardCreateRequest.BlackboardReceiverOpenVo();
           receiverOpenVoObj.setUseridList(Arrays.asList("0147**********41"));
           boardVoObj.setBlackboardReceiver(receiverOpenVoObj);
           boardVoObj.setTitle("入职须知");
           boardVoObj.setPushTop(true);
           boardVoObj.setContent("欢迎加入我们的大家庭");
           boardVoObj.setCoverpicMediaid("@lADPDeC2ufXOeRzMqM0BLA");
           req.setCreateRequest(boardVoObj);
           OapiBlackboardCreateResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 调用服务端API-[获取公告ID列表](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)接口，获取公告`blackboardId`。

   ```
   public void getListIds() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/listids");
           OapiBlackboardListidsRequest req = new OapiBlackboardListidsRequest();
           OapiBlackboardListidsRequest.OapiBlackboardQueryVo queryVoObj= new OapiBlackboardListidsRequest.OapiBlackboardQueryVo();
           queryVoObj.setOperationUserid("ma*******75");
           queryVoObj.setPageSize(10L);
           queryVoObj.setStartTime(StringUtils.parseDateTime("2022-10-08 00:00:00"));
           queryVoObj.setEndTime(StringUtils.parseDateTime("2022-10-09 00:00:00"));
           queryVoObj.setPage(1L);
           req.setQueryRequest(queryVoObj);
           OapiBlackboardListidsResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
3. 根据公告blackboardId进行公告管理。

   - 根据公告`blackboardId`，调用服务端API-[获取公告详情](1550-obtains-the-details-of-a-bulletin-that-is-not-deleted.md)接口，实现获取公告详情信息。

     ```
     public void getInfo() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/get");
             OapiBlackboardGetRequest req = new OapiBlackboardGetRequest();
             req.setBlackboardId("23c8**********152");
             req.setOperationUserid("ma******75");
             OapiBlackboardGetResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```

     > **[!NOTE]**
     >
     > 公告的保密级别和查看权限要求如下：
     >
     > - 非保密公告，可查看人员：
     >
     >   - 全公司员工
     > - 保密公告，可查看人员：
     >
     >   - 公告管理员
     >   - 公告的接收人
   - 根据公告`blackboardId`，调用服务端API-[更新公告](0281-modify-the-announcement-according-to-the-announcement-id.md)接口，实现更新公告内容。

     ```
     public void updateNotice() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/update");
             OapiBlackboardUpdateRequest req = new OapiBlackboardUpdateRequest();
             OapiBlackboardUpdateRequest.OapiUpdateBlackboardVo boardVoObj = new OapiBlackboardUpdateRequest.OapiUpdateBlackboardVo();
             boardVoObj.setAuthor("小钉");
             boardVoObj.setDing(true);
             boardVoObj.setBlackboardId("206**********ae9");
             boardVoObj.setTitle("入职须知2");
             boardVoObj.setContent("欢迎加入我们的大家庭2");
             boardVoObj.setNotify(true);
             boardVoObj.setOperationUserid("ma*******5");
             boardVoObj.setCoverpicMediaid("@lADPDeC2ufXOeRzMqM0BLA");
             req.setUpdateRequest(boardVoObj);
             OapiBlackboardUpdateResponse rsp = client.execute(req, getAccessToken());
             System.out.println(rsp.getBody());
         }
     ```

     > **[!NOTE]**
     >
     > 只有以下权限的人员可更新公告：
     >
     > - 主管理员。
     > - 公告子管理员并且是待修改公告的创建者。
   - 根据公告`blackboardId`，调用服务端API-[删除公告](0280-delete-announcements-based-on-the-announcement-id.md)接口，实现删除公告。

     ```
     public void deleteNotice() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/delete");
             OapiBlackboardDeleteRequest req = new OapiBlackboardDeleteRequest();
             req.setBlackboardId("206**********ae9");
             req.setOperationUserid("001");
             OapiBlackboardDeleteResponse rsp = client.execute(req, getAccessToken());
             System.out.println(rsp.getBody());
         }
     ```

     > **[!NOTE]**
     >
     > 只有以下身份可以删除：
     >
     > - 主管理员
     > - 公告子管理员并且是待删除公告创建者
