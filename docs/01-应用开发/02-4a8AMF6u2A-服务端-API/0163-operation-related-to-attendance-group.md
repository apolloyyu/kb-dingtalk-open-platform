---
title: "创建、获取、更新及删除考勤组"
source_url: "https://open.dingtalk.com/document/development/operation-related-to-attendance-group"
namespace: "development"
slug: "operation-related-to-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 创建、获取、更新及删除考勤组"
doc_id: "9xgadQlBCR"
updated_at: "2026-07-02 10:36:05"
---

> Source: https://open.dingtalk.com/document/development/operation-related-to-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 创建、获取、更新及删除考勤组
> Updated: 2026-07-02 10:36:05

# 创建、获取、更新及删除考勤组

本文介绍了创建一个企业内部应用，使用考勤组管理提供的API，实现创建、获取、更新和删除考勤组等。

## **预期效果**

预期效果如下图所示，你可登录[钉钉管理后台](https://oa.dingtalk.com/)后，依次在**工作台 > 应用管理 > 考勤打卡 > 考勤组管理**中查看。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1110135661/p500946.png)

## **接入流程简介**

前提条件：完成[创建应用](https://open.dingtalk.com/document/orgapp/create-an-application)的流程

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 调用服务端API-[创建考勤组](0170-attendance-group-write.md)接口，获取考勤组`id`。

   > **[!NOTE]**
   >
   > 本文档示例采用固定班制考勤组信息。

   如果需要创建**固定班制考勤组**，调用创建考勤组接口前，需确保已设置了班次：

   - 如果无班次，调用服务端API-[创建班次](0198-create-modify-shifts.md)接口，获取班次ID。
   - 如果已有班次，调用服务端API-[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口，获取已有班次ID。
2. 获取考勤组信息。

   - 获取企业下所有的考勤组信息

     - 调用服务端API-[批量获取考勤组摘要](0178-batch-query-of-simple-information-of-the-attendance-group.md)，获取企业下所有的考勤组摘要信息。
     - 调用服务端API-[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)，获取企业下所有的考勤组详情。
   - 调用服务端API-[搜索考勤组摘要](0173-attendance-group-search.md)接口，根据考勤组名称模糊查询考勤组信息。
   - 获取单个考勤组信息

     - 根据考勤组`id`，调用服务端API-[获取考勤组详情](0174-query-a-single-attendance-group.md)，获取单个考勤组的考勤组详情信息。
     - 根据groupKey获取考勤组详情

       1. 根据考勤组`id`，调用服务端API-[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口，获取考勤组`groupKey`。
       2. 根据考勤组`groupKey`，调用服务端API-[根据groupKey查询考勤组信息](0175-queries-attendance-group-information-by-id.md)接口，获取考勤组信息。
3. 根据考勤组`id`，调用服务端API-[更新考勤组](0171-attendance-group-update-interface.md)，修改考勤组名称、考勤组班次等信息。
4. 根据考勤组`groupKey`，调用服务端API-[删除考勤组](0172-delete-attendance-group.md)接口，实现删除考勤组。

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

1. 调用服务端API-[创建考勤组](0170-attendance-group-write.md)接口，获取考勤组`id`。

   ```
   public void createGroup() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/add");
           OapiAttendanceGroupAddRequest req = new OapiAttendanceGroupAddRequest();
           req.setOpUserId("ma*****75");
           //考勤组相关信息
           OapiAttendanceGroupAddRequest.TopGroupVo topGroupVo = new OapiAttendanceGroupAddRequest.TopGroupVo();
           topGroupVo.setOwner("ma*****75");
           topGroupVo.setEnableEmpSelectClass(true);
           topGroupVo.setCorpId("ding***********288");
           topGroupVo.setSkipHolidays(true);
           topGroupVo.setEnableOutsideCameraCheck(true);
           List<OapiAttendanceGroupAddRequest.TopPositionVo> positionVos = new ArrayList<OapiAttendanceGroupAddRequest.TopPositionVo>();
           OapiAttendanceGroupAddRequest.TopPositionVo topPositionVo = new OapiAttendanceGroupAddRequest.TopPositionVo();
           positionVos.add(topPositionVo);
           topPositionVo.setAddress("生物科技产业园区经二路21号");
           topPositionVo.setCorpId("ding*******288");
           topPositionVo.setLatitude("36.687495");
           topPositionVo.setAccuracy("0");
           topPositionVo.setTitle("青藏高原自然博物馆");
           topPositionVo.setLongitude("101.750329");
           topGroupVo.setPositions(positionVos);
           topGroupVo.setModifyMember(true);
           topGroupVo.setType("FIXED");
           topGroupVo.setEnableFaceCheck(false);
           topGroupVo.setCheckNeedHealthyCode(true);
           topGroupVo.setEnableCameraCheck(false);
           List<OapiAttendanceGroupAddRequest.TopShiftVo> topShiftVos = new ArrayList<OapiAttendanceGroupAddRequest.TopShiftVo>();
           OapiAttendanceGroupAddRequest.TopShiftVo topShiftVo = new OapiAttendanceGroupAddRequest.TopShiftVo();
           topShiftVos.add(topShiftVo);
           topShiftVo.setId(1006170802L);
           topGroupVo.setShiftVoList(topShiftVos);
           topGroupVo.setEnableOutsideCheck(false);
           List<OapiAttendanceGroupAddRequest.TopMemberVo> memberVos = new ArrayList<OapiAttendanceGroupAddRequest.TopMemberVo>();
           OapiAttendanceGroupAddRequest.TopMemberVo topMemberVo = new OapiAttendanceGroupAddRequest.TopMemberVo();
           memberVos.add(topMemberVo);
           topMemberVo.setRole("Attendance");
           topMemberVo.setCorpId("ding********288");
           topMemberVo.setType("StaffMember");
           topMemberVo.setUserId("014***********041");
           topGroupVo.setMembers(memberVos);
           topGroupVo.setName("新考勤");
           topGroupVo.setEnableNextDay(false);
           topGroupVo.setManagerList(Arrays.asList("08*******272","ma*******75"));
           topGroupVo.setWorkdayClassList(Arrays.asList(0L,1006170802L,1006170802L,1006170802L,1006170802L,1006170802L,0L));
           topGroupVo.setDefaultClassId(1006170802L);
           topGroupVo.setOffset(300L);
           OapiAttendanceGroupAddRequest.TopGroupManageRolePermissionVo groupManageRolePermissionVo = new OapiAttendanceGroupAddRequest.TopGroupManageRolePermissionVo();
           groupManageRolePermissionVo.setSchedule("w");
           groupManageRolePermissionVo.setGroupMember("w");
           groupManageRolePermissionVo.setGroupType("r");
           groupManageRolePermissionVo.setCheckTime("w");
           groupManageRolePermissionVo.setCheckPositionType("r");
           groupManageRolePermissionVo.setOverTimeRule("r");
           groupManageRolePermissionVo.setCameraCheck("w");
           groupManageRolePermissionVo.setOutSideCheck("w");
           topGroupVo.setResourcePermissionMap(groupManageRolePermissionVo);
           //考勤wifi打卡相关配置信息
           //List<OapiAttendanceGroupAddRequest.TopWifiVo> topWifiVos = new ArrayList<OapiAttendanceGroupAddRequest.TopWifiVo>();
           //OapiAttendanceGroupAddRequest.TopWifiVo topWifiVo = new OapiAttendanceGroupAddRequest.TopWifiVo();
           // topWifiVos.add(topWifiVo);
           // topWifiVo.setMacAddr("C0:E0:D0:E0:C0:0F");
           //topWifiVo.setSsid("OFFICE-WiFi");
           //topWifiVo.setCorpId("dinge8xxxx");
           //topGroupVo.setWifis(topWifiVos);
           topGroupVo.setDisableCheckWithoutSchedule(true);
           topGroupVo.setFreecheckDayStartMinOffset(240L);
           topGroupVo.setDisableCheckWhenRest(true);
           req.setTopGroup(topGroupVo);
           OapiAttendanceGroupAddResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```

   > **[!NOTE]**
   >
   > 本文档示例采用固定班制考勤组信息。

   如果需要创建**固定班制考勤组**，调用创建考勤组接口前，需确保已设置了班次：

   - 如果无班次，调用服务端API-[创建班次](0198-create-modify-shifts.md)接口，获取班次ID。

     ```
     public void createShift() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/add");
             OapiAttendanceShiftAddRequest request = new OapiAttendanceShiftAddRequest();

             OapiAttendanceShiftAddRequest.TopAtClassVo topAtClassVo = new OapiAttendanceShiftAddRequest.TopAtClassVo();
             topAtClassVo.setOwner("ma******75");
             topAtClassVo.setClassGroupName("1009班次");
             topAtClassVo.setCorpId("ding******288");
             topAtClassVo.setName("新班次");

             List<OapiAttendanceShiftAddRequest.TopAtSectionVo> sectionVos = new ArrayList<>();
             OapiAttendanceShiftAddRequest.TopAtSectionVo sectionVo = new OapiAttendanceShiftAddRequest.TopAtSectionVo();
             List<OapiAttendanceShiftAddRequest.TopAtTimeVo> timeVos = new ArrayList<>();
             OapiAttendanceShiftAddRequest.TopAtTimeVo timeVo = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
             timeVo.setAcross(0L);
             timeVo.setBeginMin(60L);
             timeVo.setCheckTime(StringUtils.parseDateTime("2022-10-09 09:00:00"));
             timeVo.setCheckType("OnDuty");
             timeVo.setEndMin(30L);
             timeVo.setFreeCheck(false);
             OapiAttendanceShiftAddRequest.TopAtTimeVo timeVo1 = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
             timeVo1.setAcross(0L);
             timeVo1.setBeginMin(0L);
             timeVo1.setCheckTime(StringUtils.parseDateTime("2022-10-09 18:00:00"));
             timeVo1.setCheckType("OffDuty");
             timeVo1.setEndMin(-1L);
             timeVo1.setFreeCheck(false);
             timeVos.add(timeVo);
             timeVos.add(timeVo1);
             sectionVo.setTimes(timeVos);
             sectionVos.add(sectionVo);
             topAtClassVo.setSections(sectionVos);
             OapiAttendanceShiftAddRequest.TopAtClassSettingVo settingVo = new OapiAttendanceShiftAddRequest.TopAtClassSettingVo();
             topAtClassVo.setSetting(settingVo);
             OapiAttendanceShiftAddRequest.TopAtTimeVo restBeginTime = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
             settingVo.setRestBeginTime(restBeginTime);
             restBeginTime.setFreeCheck(false);
             restBeginTime.setAcross(0L);
             restBeginTime.setCheckType("OnDuty");
             restBeginTime.setFreeCheck(false);
             restBeginTime.setCheckTime(StringUtils.parseDateTime("2022-10-09 12:00:00"));
             OapiAttendanceShiftAddRequest.TopAtTimeVo restEndTime = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
             settingVo.setRestEndTime(restEndTime);
             restEndTime.setAcross(0L);
             restEndTime.setCheckType("OffDuty");
             restEndTime.setFreeCheck(false);
             restEndTime.setCheckTime(StringUtils.parseDateTime("2022-10-09 13:00:00"));
             settingVo.setCorpId("ding16*******c288");
             settingVo.setIsDeleted("N");
             settingVo.setAbsenteeismLateMinutes(60L);
             settingVo.setIsFlexible(false);
             settingVo.setSeriousLateMinutes(30L);
             request.setOpUserId("ma*****75");
             request.setShift(topAtClassVo);
             OapiAttendanceShiftAddResponse response = client.execute(request, "access_token");
             System.out.println(response.getBody());
         }
     ```
   - 如果已有班次，调用服务端API-[获取班次摘要信息](0203-enterprise-shift-query-in-batches.md)接口，获取已有班次ID。

     ```
     public void shiftList() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/list");
             OapiAttendanceShiftListRequest req = new OapiAttendanceShiftListRequest();
             req.setOpUserId("ma******75");
             req.setCursor(0L);
             OapiAttendanceShiftListResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```
2. 获取考勤组信息。

   - 获取企业下所有的考勤组信息

     - 调用服务端API-[批量获取考勤组摘要](0178-batch-query-of-simple-information-of-the-attendance-group.md)，获取企业下所有的考勤组摘要信息。

       ```
        public void groupMinimalismList() throws ApiException {
               DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/minimalism/list");
               OapiAttendanceGroupMinimalismListRequest req = new OapiAttendanceGroupMinimalismListRequest();
               req.setOpUserId("ma******75");
               req.setCursor(0L);
               OapiAttendanceGroupMinimalismListResponse rsp = client.execute(req, "access_token");
               System.out.println(rsp.getBody());
           }
       ```
     - 调用服务端API-[批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md)，获取企业下所有的考勤组详情。

       ```
       public void simpleGroups() throws ApiException {
               DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getsimplegroups");
               OapiAttendanceGetsimplegroupsRequest req = new OapiAttendanceGetsimplegroupsRequest();
               req.setOffset(0L);
               req.setSize(10L);
               OapiAttendanceGetsimplegroupsResponse rsp = client.execute(req, "access_token");
               System.out.println(rsp.getBody());
           }
       ```
   - 调用服务端API-[搜索考勤组摘要](0173-attendance-group-search.md)接口，根据考勤组名称模糊查询考勤组信息。

     ```
      public void groupSearch() throws ApiException {
             DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/search");
             OapiAttendanceGroupSearchRequest req = new OapiAttendanceGroupSearchRequest();
             req.setOpUserId("ma******75");
             req.setGroupName("新考勤");
             OapiAttendanceGroupSearchResponse rsp = client.execute(req, "access_token");
             System.out.println(rsp.getBody());
         }
     ```
   - 获取单个考勤组信息

     - 根据考勤组`id`，调用服务端API-[获取考勤组详情](0174-query-a-single-attendance-group.md)，获取单个考勤组的考勤组详情信息。

       ```
        public void groupQuery() throws ApiException {
               DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/query");
               OapiAttendanceGroupQueryRequest req = new OapiAttendanceGroupQueryRequest();
               req.setOpUserId("ma******75");
               req.setGroupId(1010195506L);
               OapiAttendanceGroupQueryResponse rsp = client.execute(req, "access_token");
               System.out.println(rsp.getBody());
           }
       ```
     - 根据groupKey获取考勤组详情

       1. 根据考勤组`id`，调用服务端API-[groupId转换为groupKey](0177-groupid-to-groupkey.md)接口，获取考勤组`groupKey`。

          ```
           public void groupsIdToKey() throws ApiException {
                  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/groups/idtokey");
                  OapiAttendanceGroupsIdtokeyRequest req = new OapiAttendanceGroupsIdtokeyRequest();
                  req.setOpUserId("ma******75");
                  req.setGroupId(1010195506L);
                  OapiAttendanceGroupsIdtokeyResponse rsp = client.execute(req, "access_token");
                  System.out.println(rsp.getBody());
              }
          ```
       2. 根据考勤组`groupKey`，调用服务端API-[根据groupKey查询考勤组信息](0175-queries-attendance-group-information-by-id.md)接口，获取考勤组信息。

          ```
           public void groupInfo() throws ApiException {
                  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/get");
                  OapiAttendanceGroupGetRequest req = new OapiAttendanceGroupGetRequest();
                  req.setOpUserid("ma******75");
                  req.setGroupKey("19F************2B2");
                  OapiAttendanceGroupGetResponse rsp = client.execute(req, "access_token");
                  System.out.println(rsp.getBody());
              }
          ```
3. 根据考勤组`id`，调用服务端API-[更新考勤组](0171-attendance-group-update-interface.md)，修改考勤组名称、考勤组班次等信息。

   ```
   public void  updateGroup() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/modify");
           OapiAttendanceGroupModifyRequest req = new OapiAttendanceGroupModifyRequest();
           req.setOpUserId("ma*****75");
           OapiAttendanceGroupModifyRequest.TopGroupVo topGroupVo = new OapiAttendanceGroupModifyRequest.TopGroupVo();
           topGroupVo.setOwner("ma*****75");
           topGroupVo.setEnableEmpSelectClass(false);
           topGroupVo.setSkipHolidays(true);
           List<OapiAttendanceGroupModifyRequest.TopPositionVo> positionVos = new ArrayList<OapiAttendanceGroupModifyRequest.TopPositionVo>();
           OapiAttendanceGroupModifyRequest.TopPositionVo topPositionVo = new OapiAttendanceGroupModifyRequest.TopPositionVo();
           positionVos.add(topPositionVo);
           topPositionVo.setAddress("生物科技产业园区经二路21号");
           topPositionVo.setCorpId("din***********88");
           topPositionVo.setLatitude("30.123");
           topPositionVo.setAccuracy("0");
           topPositionVo.setTitle("青藏高原自然博物馆");
           topPositionVo.setLongitude("120.123");
           topGroupVo.setPositions(positionVos);
           topGroupVo.setEnableFaceCheck(true);
           topGroupVo.setOpenCameraCheck(false);
           topGroupVo.setOpenFaceCheck(false);
           List<OapiAttendanceGroupModifyRequest.TopShiftVo> topShiftVos = new ArrayList<OapiAttendanceGroupModifyRequest.TopShiftVo>();
           OapiAttendanceGroupModifyRequest.TopShiftVo topShiftVo = new OapiAttendanceGroupModifyRequest.TopShiftVo();
           topShiftVos.add(topShiftVo);
     			// 班次ID
           topShiftVo.setId(1006170802L);
           topGroupVo.setShiftVoList(topShiftVos);
           topGroupVo.setEnableOutsideCheck(false);
           topGroupVo.setName("新考勤组1");
     			//考勤组ID
           topGroupVo.setId(1010195506L);
           topGroupVo.setManagerList(Arrays.asList("0147******041","0852*******72"));
           topGroupVo.setOffset(500L);
           topGroupVo.setDisableCheckWithoutSchedule(false);
     			//1006170802L：班次ID。
           topGroupVo.setWorkdayClassList(Arrays.asList(0L,1006170802L,1006170802L,1006170802L,1006170802L,1006170802L,0L));
           req.setTopGroup(topGroupVo);
           OapiAttendanceGroupModifyResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
4. 根据考勤组`groupKey`，调用服务端API-[删除考勤组](0172-delete-attendance-group.md)接口，实现删除考勤组。

   ```
    public void deleteGroup() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/delete");
           OapiAttendanceGroupDeleteRequest req = new OapiAttendanceGroupDeleteRequest();
           req.setOpUserid("ma********75");
           req.setGroupKey("19FB************22B2");
           OapiAttendanceGroupDeleteResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
