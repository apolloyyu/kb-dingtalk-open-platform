---
title: "按天获取员工考勤报表信息"
source_url: "https://open.dingtalk.com/document/development/obtain-the-employee-attendance-report-information"
namespace: "development"
slug: "obtain-the-employee-attendance-report-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 按天获取员工考勤报表信息"
doc_id: "0nxu85pR9m"
updated_at: "2026-07-02 10:36:11"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-employee-attendance-report-information
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 按天获取员工考勤报表信息
> Updated: 2026-07-02 10:36:11

# 按天获取员工考勤报表信息

本文档介绍实现按天获取员工考勤报表信息。

> **[!NOTE]**
>
> 本文档以企业内部应用实现为例，第三方企业应用实现流程与本文档流程一致。

## **预期效果**

考勤统计的能力是为了通过接口获取每一天的某些项指标的值。**再经过开发者自行汇总每一天的值**，可以实最终结果与[钉钉管理后台](https://oa.dingtalk.com/)-考勤打卡中的报表信息保持一致。

![月度汇总](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6259295361/p347319.png)

## **接入流程简介**

本文介绍了按天获取员工考勤报表信息实现获取员工考勤统计中每天的值。按天获取员工考勤报表信息的流程。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：无需申请接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 调用服务端API-[查询是否启用智能统计报表](0215-determine-whether-to-enable-attendance-intelligent-report.md)接口，确认是否已经开启智能统计。

   > 目前考勤打卡应用已经开启智能统计能力，由于存在旧版 UI 可能未开启智能统计，调用接口确认是否已经开启。
2. 调用服务端API-[获取考勤报表列定义](0218-queries-the-enterprise-attendance-report-column.md)接口，获取考勤报表列`ID`。
3. 根据考勤报表列`ID`，调用服务端API-[获取考勤报表列值](0219-queries-the-column-value-of-the-attendance-report.md)接口，实现获取列定义对应的值的信息。

> **[!IMPORTANT]**
>
> 本流程并不是直接获取考勤月度汇总表的信息，当前开放接口实现的效果是获取每一天的某些项指标的值，最终统计结果需要开发者进行汇总。
>
> 比如需求是获取小明在12月份的**应出勤天数**统计信息，本流程获取的结果是小明在12月份每一天的**应出勤天数**值获取的结果如下
>
> ```
> {
> "column_vals":[{
>    "column_vals":[
>       {"date":"2021-12-01 00:00:00","value":"1.0"},
>       {"date":"2021-12-02 00:00:00","value":"1.0"},
>       {"date":"2021-12-03 00:00:00","value":"0.0"},
>       ...
>       {"date":"2021-12-31 00:00:00","value":"1.0"},
>       ...
>       ],"column_vo":{"id":7331XXX}}]}
> ```

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## **步骤二：添加接口权限**

无需申请接口权限。

## 步骤三：获取应用访问凭证accessToken

> **[!IMPORTANT]**
>
> 服务端API差异详情参见[新版API VS 旧版API](0002-download-the-server-side-sdk.md#section-8lr-id4-rbz)。以下接口均使用服务端API接口，SDK下载详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)。

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。

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

## 步骤四：调用考勤相关API

1. 调用服务端API-[获取考勤报表列定义](0218-queries-the-enterprise-attendance-report-column.md)接口，获取考勤报表列`ID`。

   ```
    public void attendanceColumns() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getattcolumns");
           OapiAttendanceGetattcolumnsRequest req = new OapiAttendanceGetattcolumnsRequest();
           OapiAttendanceGetattcolumnsResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```

   > **[!NOTE]**
   >
   > 获取列定义不包含请假信息，如需获取报表内的请假统计信息，调用[获取报表假期数据](0217-obtains-the-holiday-data-from-the-smart-attendance-report.md)接口即可。
2. 根据考勤报表列`ID`，调用服务端API-[获取考勤报表列值](0219-queries-the-column-value-of-the-attendance-report.md)接口，实现获取列定义对应的值的信息。

   ```
    public void attendanceColumnsValue() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getcolumnval");
           OapiAttendanceGetcolumnvalRequest req = new OapiAttendanceGetcolumnvalRequest();
           req.setUserid("01472825524039877041");
           req.setColumnIdList("184678999,184727001");
           req.setFromDate(StringUtils.parseDateTime("2022-10-24 00:00:00"));
           req.setToDate(StringUtils.parseDateTime("2022-10-25 00:00:00"));
           OapiAttendanceGetcolumnvalResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
