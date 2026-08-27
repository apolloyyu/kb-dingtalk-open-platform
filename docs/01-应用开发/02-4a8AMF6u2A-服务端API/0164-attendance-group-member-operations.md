---
title: "新增、获取、更新及删除考勤人员"
source_url: "https://open.dingtalk.com/document/development/attendance-group-member-operations"
namespace: "development"
slug: "attendance-group-member-operations"
group: "应用开发"
tab: "服务端API"
breadcrumb: "考勤 > 使用教程 > 新增、获取、更新及删除考勤人员"
doc_id: "HpgAC8DZHF"
updated_at: "2026-07-02 10:36:07"
---

> Source: https://open.dingtalk.com/document/development/attendance-group-member-operations
> Path: 应用开发 / 服务端API / 考勤 > 使用教程 > 新增、获取、更新及删除考勤人员
> Updated: 2026-07-02 10:36:07

# 新增、获取、更新及删除考勤人员

本文介绍了创建一个企业内部应用，使用考勤人员管理提供的API，实现新增、获取、更新和删除考勤人员等。

## **预期效果**

考勤人员展示，如下图所示：

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5754745661/p501569.png)

## **接入流程简介**

前提条件：完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 调用服务端API-[批量新增参与考勤人员](0181-batch-add-employees-under-the-attendance-group.md)接口，实现新增考勤组参与考勤人员。
2. 调用服务端API-[获取用户考勤组](0180-queries-a-user-attendance-group.md)，获取用户所在考勤组信息。
3. 获取考勤组内参与考勤人员信息

   - 调用服务端API-[获取参与考勤人员的userid](0184-query-attendance-group-personnel-information-in-batches.md)接口，获取参与考勤人员的userId信息。
   - 调用服务端API-[获取参与考勤人员](0183-batch-query-of-attendance-group-members.md)接口，获取参与考勤人员信息。
   - 调用服务端API-[查询参与考勤人员列表](0186-batch-query-of-employees-in-the-attendance-group.md)，获取参与考勤人员列表信息。
4. 调用服务端API-[校验用户是否在当前考勤组](0187-query-members-by-id.md)接口，实现校验某个部门或者员工，是否在某考勤组内。
5. 调用服务端API-[更新参与考勤人员](0182-attendance-group-member-update.md)接口，实现更新考勤组参与考勤人员。
6. 调用服务端API-[批量删除参与考勤人员](0185-batch-delete-employees-under-the-attendance-group.md)接口，实现删除参与考勤人员。

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

> **[!NOTE]**
>
> 考勤组管理的操作流程，详情参见[创建、获取、更新及删除考勤组](0163-operation-related-to-attendance-group.md)。

1. 调用服务端API-[批量新增参与考勤人员](0181-batch-add-employees-under-the-attendance-group.md)接口，实现新增考勤组参与考勤人员。

   ```
   public void  addAttendanceMembers() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/add");
           OapiAttendanceGroupUsersAddRequest req = new OapiAttendanceGroupUsersAddRequest();
           req.setOpUserid("manager7675");
     			//groupKey获取：需要将groupId转化为groupKey，参见考勤组管理的操作流程
           req.setGroupKey("2A5**********24");
           req.setUserIdList("085218*********9877041");
           OapiAttendanceGroupUsersAddResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
2. 调用服务端API-[获取用户考勤组](0180-queries-a-user-attendance-group.md)，获取用户所在考勤组信息。

   ```
    public void attendanceUserGroup() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getusergroup");
           OapiAttendanceGetusergroupRequest req = new OapiAttendanceGetusergroupRequest();
           req.setUserid("0852**********72");
           OapiAttendanceGetusergroupResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
3. 获取考勤组内参与考勤人员信息

   > **[!NOTE]**
   >
   > 下列三个获取考勤组成员信息接口的区别，主要针对考勤组参与人员有部门的情况![考勤组成员](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4181657361/p351816.png)
   >
   > | 接口列表 | 张三userid | 测试部门ID | 测试部门员工userId |
   > | --- | --- | --- | --- |
   > | [获取参与考勤人员的userid](0184-query-attendance-group-personnel-information-in-batches.md) | ✅ | ❎ | ✅ |
   > | [获取参与考勤人员](0183-batch-query-of-attendance-group-members.md) | ✅ | ✅ | ❎ |
   > | [查询参与考勤人员列表](0186-batch-query-of-employees-in-the-attendance-group.md) | ✅ | ❎ | ❎ |
   >
   > **注：✅代表可以获取到 ❎代表获取不到**

   - 调用服务端API-[获取参与考勤人员的userid](0184-query-attendance-group-personnel-information-in-batches.md)接口，获取参与考勤人员的userId信息。

     ```
      public void attendanceGroupMemberUsers() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/memberusers/list");
             OapiAttendanceGroupMemberusersListRequest req = new OapiAttendanceGroupMemberusersListRequest();
             req.setCursor(0L);
             req.setOpUserId("ma********75");
             req.setGroupId(1001290520L);
             OapiAttendanceGroupMemberusersListResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```
   - 调用服务端API-[获取参与考勤人员](0183-batch-query-of-attendance-group-members.md)接口，获取参与考勤人员信息。

     ```
      public void groupMemberList() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/list");
             OapiAttendanceGroupMemberListRequest req = new OapiAttendanceGroupMemberListRequest();
             req.setCursor(0L);
             req.setOpUserId("ma*******5");
             req.setGroupId(1001290520L);
             OapiAttendanceGroupMemberListResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```
   - 调用服务端API-[查询参与考勤人员列表](0186-batch-query-of-employees-in-the-attendance-group.md)，获取参与考勤人员列表信息。

     ```
       public void groupUsersQuery() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/query");
             OapiAttendanceGroupUsersQueryRequest req = new OapiAttendanceGroupUsersQueryRequest();
             req.setSize(50L);
             req.setCursor("");
             req.setOpUserid("m*******75");
             req.setGroupKey("2A5B6**********EF24");
             OapiAttendanceGroupUsersQueryResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```
4. 调用服务端API-[校验用户是否在当前考勤组](0187-query-members-by-id.md)接口，实现校验某个部门或者员工，是否在某考勤组内。

   ```
   public void checkGroupMember() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/listbyids");
           OapiAttendanceGroupMemberListbyidsRequest req = new OapiAttendanceGroupMemberListbyidsRequest();
           req.setOpUserId("m*******75");
           req.setMemberIds("085**********272");
           req.setMemberType(0L);
           req.setGroupId(1001290520L);
           OapiAttendanceGroupMemberListbyidsResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
5. 调用服务端API-[更新参与考勤人员](0182-attendance-group-member-update.md)接口，实现更新考勤组参与考勤人员。

   ```
    public void updateGroupMember() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/member/update");
           OapiAttendanceGroupMemberUpdateRequest req = new OapiAttendanceGroupMemberUpdateRequest();
           req.setOpUserId("man*****75");
           req.setGroupId(1001290520L);
           req.setScheduleFlag(0L);
           OapiAttendanceGroupMemberUpdateRequest.TopGroupMemberUpdateParam updateParam = new OapiAttendanceGroupMemberUpdateRequest.TopGroupMemberUpdateParam();
   //        updateParam.setAddDepts(Arrays.asList("123"));
   //        updateParam.setRemoveDepts(Arrays.asList("456"));
           updateParam.setAddUsers(Arrays.asList("012**********197"));
   //        updateParam.setAddExtraUsers(Arrays.asList("user456"));
   //        updateParam.setRemoveExtraUsers(Arrays.asList("user789"));
   //        updateParam.setRemoveUsers(Arrays.asList("user121"));
           req.setUpdateParam(updateParam);
           OapiAttendanceGroupMemberUpdateResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
6. 调用服务端API-[批量删除参与考勤人员](0185-batch-delete-employees-under-the-attendance-group.md)接口，实现删除参与考勤人员。

   ```
    public void deleteGroupMember() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/users/remove");
           OapiAttendanceGroupUsersRemoveRequest req = new OapiAttendanceGroupUsersRemoveRequest();
           req.setOpUserid("ma******75");
           req.setGroupKey("2A5************F24");
           req.setUserIdList("012*********3197");
           OapiAttendanceGroupUsersRemoveResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
