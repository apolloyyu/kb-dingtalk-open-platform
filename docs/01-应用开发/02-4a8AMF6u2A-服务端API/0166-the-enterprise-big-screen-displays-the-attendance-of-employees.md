---
title: "通过考勤接口与事件获取员工到岗情况"
source_url: "https://open.dingtalk.com/document/development/the-enterprise-big-screen-displays-the-attendance-of-employees"
namespace: "development"
slug: "the-enterprise-big-screen-displays-the-attendance-of-employees"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 使用教程 > 通过考勤接口与事件获取员工到岗情况"
doc_id: "KyPWUiGk6g"
updated_at: "2026-07-02 10:36:10"
---

> Source: https://open.dingtalk.com/document/development/the-enterprise-big-screen-displays-the-attendance-of-employees
> Path: 应用开发 / 服务端API / 考勤 > 使用教程 > 通过考勤接口与事件获取员工到岗情况
> Updated: 2026-07-02 10:36:10

# 通过考勤接口与事件获取员工到岗情况

本文介绍了创建一个企业内部应用，使用**考勤事件**和**考勤组管理**提供的API，实现获取员工到勤情况等。

## **接入流程简介**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：本示例无需申请接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1443-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：相关调用流程：

1. 调用考勤服务端API-[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)接口，获取企业考勤组内的排班上下班时间。
2. 获取员工考勤打卡情况，需要注册企业考勤事件回调，参考文档[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)，并订阅[考勤事件](../04-LFcRvVD08N-事件订阅/0125-employee-clock-in-event.md)。
3. 成功注册企业考勤事件回调后，企业内员工上班执行打卡即可实时产生回调。
4. 根据实时推送的打卡信息userId、groupId、checkTime值跟获取的考勤组内排班打卡时间对比即可得到该员工打卡是正常打卡还是迟到打卡。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

本示例无需申请接口权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1443-obtain-orgapp-token.md)。

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

## **步骤四：**相关调用流程

1. 调用考勤服务端API-[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)接口，获取企业考勤组内的排班上下班时间。

   ```
   public void batchAttendanceGroupInfo() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getsimplegroups");
           OapiAttendanceGetsimplegroupsRequest req = new OapiAttendanceGetsimplegroupsRequest();
           req.setOffset(0L);
           req.setSize(10L);
           OapiAttendanceGetsimplegroupsResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 获取员工考勤打卡情况，需要注册企业考勤事件回调，参考文档[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)，并订阅[考勤事件](../04-LFcRvVD08N-事件订阅/0125-employee-clock-in-event.md)。
3. 成功注册企业考勤事件回调后，企业内员工上班执行打卡即可实时产生回调，接收到的回调信息如下。

   ```
         {
               "DataList":[
               {
                       //打卡员工的userId值
                       "userId":"0126xxxx",
                       //员工执行打卡时间，单位毫秒
                       "checkTime":1570791880000,
                       //执行打卡时的地址
                       "address":"中国科学院工程热物理研究所（浙江海外高层次人才创新园7幢东）",
                       //企业corpId
                       "corpId":"dingxxxx",
                       //该员工所在的考勤组ID
                       "groupId":"4C63xxxx",
                       //打卡地址对应的纬度
                       "latitude":30.285230848524307,
                       //打卡地址对应的经度
                       "longitude":120.01713514539931,
                       //打卡业务ID
                       "bizId":"FF62xxxx",
                       //定位方法
                       "locationMethod":"MAP",
               }
       ],
               "EventType":"attendance_check_record"
           }
   ```
4. 根据实时推送的打卡信息userId、groupId、checkTime值跟获取的考勤组内排班打卡时间对比即可得到该员工打卡是正常打卡还是迟到打卡。
