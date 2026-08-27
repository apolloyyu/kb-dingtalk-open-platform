---
title: "企业自有系统考勤打卡信息同步到钉钉"
source_url: "https://open.dingtalk.com/document/development/attendance-synchronizes-information"
namespace: "development"
slug: "attendance-synchronizes-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 使用教程 > 企业自有系统考勤打卡信息同步到钉钉"
doc_id: "ANOoKtLNB2"
updated_at: "2026-07-02 10:36:14"
---

> Source: https://open.dingtalk.com/document/development/attendance-synchronizes-information
> Path: 应用开发 / 服务端API / 考勤 > 使用教程 > 企业自有系统考勤打卡信息同步到钉钉
> Updated: 2026-07-02 10:36:14

# 企业自有系统考勤打卡信息同步到钉钉

本文介绍企业自有考勤系统的打卡信息同步到钉钉考勤打卡。

## **预期效果**

同步打卡信息界面，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2714555661/p503035.png)

## **接入流程简介**

本文介绍了创建一个企业内部应用，使用**考勤打卡和通讯录**提供的API，实现将企业自有系统的考勤打卡信息同步到钉钉考勤应用，使用钉钉考勤管理打卡数据。

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：[添加接口调用权限](0003-add-api-permission.md)。查找“通讯录”、“考勤”，申请对应接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用通讯录、考勤相关API：

1. 调用通讯录服务端API-[获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md)接口，获取企业员工在钉钉组织架构中的userId值信息。
2. 调用考勤服务端API-[上传打卡记录](0197-upload-punch-records.md)接口，将企业自有系统的员工考勤打卡日期、时间等信息上传到钉钉考勤应用。实现同步考勤。

## **前提条件**

完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

## **步骤一：获取应用凭证**

1. 选择目标应用，进入应用详情页，单击**基础信息** > **凭证与基础信息**。
2. 获取应用 Client ID 和 Client Secret。

## 步骤二：添加接口权限

单击**开发配置** > **权限管理**，在权限搜索框中查找“通讯录”、“考勤”，并申请权限。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7450699661/p528872.png)

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0368499661/p528870.png)

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

## **步骤四：调用相关API**

1. 调用通讯录服务端API-[获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md)接口，获取企业员工在钉钉组织架构中的userId值信息。

   ```
   public void deptInfo() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/v2/user/list");
           OapiV2UserListRequest req = new OapiV2UserListRequest();
           req.setDeptId(1L);
           req.setCursor(0L);
           req.setSize(10L);
           req.setOrderField("entry_asc");
           req.setContainAccessLimit(false);
           req.setLanguage("zh_CN");
           OapiV2UserListResponse rsp = client.execute(req, "access_token"）;
           System.out.println(rsp.getBody());
       }
   ```
2. 调用考勤服务端API-[上传打卡记录](0197-upload-punch-records.md)接口，将企业自有系统的员工考勤打卡日期、时间等信息上传到钉钉考勤应用。实现同步考勤。

   ```
   public void attendanceRecordUpload() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/record/upload");
           OapiAttendanceRecordUploadRequest req = new OapiAttendanceRecordUploadRequest();
           req.setUserid("01472825524039877041");
           req.setDeviceName("东门考勤机");
           req.setDeviceId("dingTalk_one");
           req.setPhotoUrl("https://xxx.com/xxx.png");
           req.setUserCheckTime(1665363600000L);
           OapiAttendanceRecordUploadResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
