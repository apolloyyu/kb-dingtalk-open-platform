---
title: "同步与更新企业自有考勤补卡信息"
source_url: "https://open.dingtalk.com/document/development/the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized"
namespace: "development"
slug: "the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 使用教程 > 同步与更新企业自有考勤补卡信息"
doc_id: "nTMMOfrMW3"
updated_at: "2026-07-02 10:36:08"
---

> Source: https://open.dingtalk.com/document/development/the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized
> Path: 应用开发 / 服务端API / 考勤 > 使用教程 > 同步与更新企业自有考勤补卡信息
> Updated: 2026-07-02 10:36:08

# 同步与更新企业自有考勤补卡信息

本文介绍了创建一个企业内部应用，使用提供的假勤审批中考勤补卡等API，实现把企业自有考勤系统提交的补卡信息同步到钉钉考勤中，修改钉钉考勤的缺卡为补卡。

> **[!NOTE]**
>
> 本文档以企业内部应用实现为例，第三方企业应用实现流程与本文档流程一致。

## **预期效果**

预期结果如下图所示：

![补卡同步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6914757361/p355383.png)

## **接入流程简介**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 员工在自有考勤系统提交补卡申请时，根据员工选择的补卡日期调用服务端API-[查询成员排班信息](0205-query-scheduling-for-a-day.md)接口，获取对应日期该员工的排班打卡时间点。
2. 员工使用自有假勤系统发起补卡审批单，审批结果不同，触发的操作不同。

   （1）如果审批通过，调用服务端API-[通知补卡通过](0228-make-up-the-card-after-approval.md)接口，提交的补卡信息会同步到钉钉考勤应用，考勤状态从缺卡修改为补卡通过。

   > **[!NOTE]**
   >
   > 本步骤不会在钉钉中产生补卡审批单。

   （2）如果员工撤销了补卡申请，可以调用服务端API-[通知审批撤销](0227-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，撤销已同步到钉钉的补卡审申请，考勤状态恢复到修改之前的打卡状态。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中输入`qyapi_attendance_group_manage`和`qyapi_attendance_group_read`，并申请权限。

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

## **步骤四：调用服务端考勤相关API**

1. 员工在自有考勤系统提交补卡申请时，根据员工选择的补卡日期调用服务端API-[查询成员排班信息](0205-query-scheduling-for-a-day.md)接口，获取对应日期该员工的排班打卡时间点。

   ```
    public void scheduleInfo() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/schedule/listbyday");
           OapiAttendanceScheduleListbydayRequest req = new OapiAttendanceScheduleListbydayRequest();
           req.setOpUserId("ma******75");
           req.setUserId("014*********041");
           req.setDateTime(166*******00L);
           OapiAttendanceScheduleListbydayResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 员工使用自有假勤系统发起补卡审批单，审批结果不同，触发的操作不同。

   （1）如果审批通过，调用服务端API-[通知补卡通过](0228-make-up-the-card-after-approval.md)接口，提交的补卡信息会同步到钉钉考勤应用，考勤状态从缺卡修改为补卡通过。

   ```
    public void approveCheck() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/check");
           OapiAttendanceApproveCheckRequest req = new OapiAttendanceApproveCheckRequest();
           req.setUserid("ma****75");
           req.setWorkDate("2022-10-10 09:00:00");
           req.setPunchId(1006170802L);
           req.setPunchCheckTime("2022-10-10 09:00:00");
           req.setUserCheckTime("2022-10-10 08:00:00");
           req.setApproveId("dingTalk10001");
           req.setJumpUrl("https://www.dingtalk.com");
           req.setTagName("补卡");
           OapiAttendanceApproveCheckResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```

   > **[!NOTE]**
   >
   > 本步骤不会在钉钉中产生补卡审批单。

   （2）如果员工撤销了补卡申请，可以调用服务端API-[通知审批撤销](0227-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，撤销已同步到钉钉的补卡审申请，考勤状态恢复到修改之前的打卡状态。

   ```
   public void approveCancel() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/approve/cancel");
           OapiAttendanceApproveCancelRequest req = new OapiAttendanceApproveCancelRequest();
           req.setUserid("ma****75");
           req.setApproveId("dingTalk10001");
           OapiAttendanceApproveCancelResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
