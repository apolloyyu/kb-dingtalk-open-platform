---
title: "企业自有假勤审批同步到钉钉"
source_url: "https://open.dingtalk.com/document/development/enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays"
namespace: "development"
slug: "enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 使用教程 > 企业自有假勤审批同步到钉钉"
doc_id: "qieVTeeppo"
updated_at: "2026-07-02 10:36:13"
---

> Source: https://open.dingtalk.com/document/development/enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays
> Path: 应用开发 / 服务端API / 考勤 > 使用教程 > 企业自有假勤审批同步到钉钉
> Updated: 2026-07-02 10:36:13

# 企业自有假勤审批同步到钉钉

本文档介绍企业使用自有OA审批系统如何同步到钉钉的OA审批。

> **[!NOTE]**
>
> 本文档以企业内部应用实现为例，第三方企业应用实现流程与本文档流程一致。

## **接入流程简介**

本文介绍了创建一个企业内部应用，使用**假勤审批**提供的API，实现企业将自有假勤系统的审批单，同步到钉钉。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

> **[!NOTE]**
>
> 该功能支持企业自研系统的加班、出差和请假信息与钉钉同步。

1. 调用服务端API-[预计算时长](1544-calculate-duration-based-on-attendance-scheduling.md)接口，实现根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。
2. 在企业自有审批系统提交了假勤申请，审批通过后通过该接口通知钉钉考勤，调用服务端API-[通知审批通过](1545-notice-of-approval.md)接口，实现钉钉考勤同步通过。保存自定义审批单ID`approve_id`。
3. 在企业自有审批系统提交了撤销假勤申请，根据自定义审批单ID`approve_id`，调用服务端API-[通知审批撤销](0227-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，实现钉钉考勤同步撤销。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中输入`qyapi_attendance_group_manage`和`qyapi_attendance_group_read`，并申请权限。

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

## **步骤四：调用考勤相关API**

1. 调用服务端API-[预计算时长](1544-calculate-duration-based-on-attendance-scheduling.md)接口，实现根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。

   > **[!NOTE]**
   >
   > 该步骤不可跳过，自有系统内的审批单信息同步到钉钉。
   >
   > 例如，小明在10月15日的排班是8小时，10月16日的排班是4小时，如果正常上班，小明在10月15日、16日这2天的工作时间是12小时。
   >
   > 小明在企业自有系统内提交请假审批单时，以下各情况，可提交的请假时长不同：
   >
   > - 情况一，选择请假开始时间是10月15日，结束时间是10月15日；调用[预计算时长](1544-calculate-duration-based-on-attendance-scheduling.md)接口，获取的可提交请假时长最大是8小时。
   > - 情况二，选择请假开始时间是10月15日，结束时间是10月16日，调用[预计算时长](1544-calculate-duration-based-on-attendance-scheduling.md)接口，获取的可提交请假时长最大是12小时。

   ```
   public void durationCalculate() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/duration/calculate");
           OapiAttendanceApproveDurationCalculateRequest req = new OapiAttendanceApproveDurationCalculateRequest();
           req.setUserid("01472825524039877041");
           req.setBizType(2L);
           req.setFromTime("2022-10-13 09:00");
           req.setToTime("2022-10-13 18:00");
           req.setDurationUnit("hour");
           req.setCalculateModel(1L);
           OapiAttendanceApproveDurationCalculateResponse rsp = client.execute(req,"access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 在企业自有审批系统提交了假勤申请，审批通过后通过该接口通知钉钉考勤，调用服务端API-[通知审批通过](1545-notice-of-approval.md)接口，实现钉钉考勤同步通过，保存自定义审批单ID`approve_id`。

   > **[!NOTE]**
   >
   > 本步骤不会在钉钉中产生OA审批单。

   ```
    public void approveFinish() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/finish");
           OapiAttendanceApproveFinishRequest req = new OapiAttendanceApproveFinishRequest();
           req.setUserid("01472825524039877041");
      			//本示例使用外出
           req.setBizType(2L);
           req.setFromTime("2022-10-13 09:00");
           req.setToTime("2022-10-13 19:00");
           req.setDurationUnit("hour");
           req.setCalculateModel(1L);
           req.setTagName("外出");
           req.setApproveId("dingTalk");
           req.setJumpUrl("https://xxx.xxx");
           OapiAttendanceApproveFinishResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
3. 在企业自有审批系统提交了撤销假勤申请，根据自定义审批单ID`approve_id`，调用服务端API-[通知审批撤销](0227-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，实现钉钉考勤同步撤销。

   ```
   public void approveCancel() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/cancel");
           OapiAttendanceApproveCancelRequest req = new OapiAttendanceApproveCancelRequest();
           req.setUserid("01472825524039877041");
           req.setApproveId("dingTalk");
           OapiAttendanceApproveCancelResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
