---
title: "考勤组管理自动化"
source_url: "https://open.dingtalk.com/document/development/operation-related-to-attendance-group"
namespace: "development"
slug: "operation-related-to-attendance-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 考勤组管理自动化方案"
doc_id: "9xgadQlBCR"
updated_at: "2026-09-17 09:36:36"
---

> Source: https://open.dingtalk.com/document/development/operation-related-to-attendance-group
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 考勤组管理自动化方案
> Updated: 2026-09-17 09:36:36

# 考勤组管理自动化

通过钉钉开放平台考勤组管理API，实现HR/OA系统与钉钉考勤体系的无缝集成，解决传统人工维护考勤组效率低、易出错、无法批量操作等核心痛点。

## **概述**

本方案提供一套完整的考勤组管理自动化解决方案，通过钉钉开放平台的考勤组管理API，实现HR系统、OA系统等业务平台与钉钉考勤体系的无缝集成。

### 方案背景

企业在考勤管理中，面临以下挑战：

- **考勤规则复杂**：固定班制、排班制、自由工时等多种考勤模式并存，手动配置耗时且易出错。
- **人员变动频繁**：入职、离职、调岗等场景下，需手动调整考勤组成员，千人级企业每周耗费数小时。
- **跨系统不同步**：HR系统中的组织架构变更未能及时同步到钉钉考勤组，导致打卡数据异常。
- **批量操作缺失**：无法一次性创建或更新多个考勤组，逐一操作效率极低。

### 核心价值

通过本方案，企业可以实现：

- **考勤组自动化管理**：创建、查询、更新、删除等操作通过API自动完成，零人工干预。
- **班次智能关联**：自动创建或关联已有班次，确保考勤规则准确无误。
- **批量高效执行**：支持批量获取、搜索、更新考勤组，大幅提升运维效率。
- **跨系统数据统一**：HR系统、OA系统与钉钉考勤数据实时同步，消除信息孤岛。

### 适用场景

本方案适用于以下典型业务场景：

- **HR系统集成**：将人力资源管理系统中的考勤规则自动同步至钉钉考勤组。
- **企业并购重组**：快速批量创建新收购公司的考勤组和班次配置。
- **OA流程联动**：审批流程结束后，自动创建或调整对应考勤组。
- **权限动态调整**：根据部门变更自动更新考勤组成员和管理员权限。

## 典型业务场景

### 场景一：HR系统考勤组同步（批量创建与管理）

#### 痛点分析

传统模式下，HR在系统中规划好新的考勤规则后，需手动登录钉钉后台逐个创建考勤组、设置班次、添加成员。千人级企业通常有20-50个考勤组，手工操作耗时数小时且容易出现班次错误或人员遗漏。

#### 价值验证

- **自动化流程**

  ![attendance_scenario1](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6998069871/p1102603.png)
- **核心优势**

  - **全自动触发**：HR系统录入新员工后自动执行API调用,无需人工登录钉钉后台或手动发起操作,真正实现"录入即同步"。
  - **精准匹配**：根据员工所属部门ID自动查询并匹配对应考勤组的groupKey,避免人工查找选错考勤组导致打卡异常。
  - **实时生效**：调用batch-add-employees接口批量新增后立即调用query-members-by-id接口校验确认,员工加入考勤组后即时生效可打卡。
  - **审计留痕**：每次API调用均记录操作人、时间戳、考勤组ID、员工userId等详细信息,满足企业合规审计与追溯要求。

### **场景二：组织架构调整后的考勤组自动同步**

#### 痛点分析

企业发生部门合并、拆分或人员调动时，HR需手动逐一修改相关考勤组的成员列表和排班规则。大型组织调整涉及数十个考勤组，手动操作不仅耗时，还容易遗漏部分考勤组，导致员工打卡异常。

#### 价值验证

- **自动化流程**

  ![组织架构调整考勤组自动化流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6998069871/p1102573.png)
- **核心优势**

  - **自动触发**：OA审批流结束后系统自动捕获变更事件并执行，无需人工发起或监控，真正实现"审批即同步"。
  - **批量精准处理**：一次性识别并更新所有受影响的考勤组，避免人工逐一查找遗漏，确保组织调整100%覆盖。
  - **实时校验反馈**：更新完成后立即调用查询接口验证数据一致性，异常自动告警，保障考勤规则准确生效。
  - **审计日志完整**：每次API调用均记录操作人、时间戳、变更内容，满足企业合规审计与追溯要求。

## **实施指南**

### 技术架构

本方案基于钉钉开放平台的服务端API构建，核心技术组件包括：

- **身份鉴权层**：通过 `Client ID` / `Client Secret` 获取 `access_token`，确保接口调用安全性。
- **考勤组管理层**：提供考勤组创建、查询、更新、删除等完整API能力，支持固定班制与排班制考勤组。
- **班次管理层**：提供班次创建、查询等API能力，作为考勤组的前置依赖资源。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

**API版本说明**：服务端API存在新版与旧版差异，建议优先使用新版API以获得更好的性能和功能支持。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_attendance_group_manage`（考勤组管理权限）
  - `qyapi_attendance_group_read`（考勤组查询权限）
- **开发环境**：已安装Java开发环境(JDK1.6及以上)及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1443-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 调用服务端API-[创建考勤组](0169-attendance-group-write.md)接口，获取考勤组`id`。

   > **[!NOTE]**
   >
   > 本文档示例采用固定班制考勤组信息。

   如果需要创建**固定班制考勤组**，调用创建考勤组接口前，需确保已设置了班次：

   - 如果无班次，调用服务端API-[创建班次](0197-create-modify-shifts.md)接口，获取班次ID。
   - 如果已有班次，调用服务端API-[获取班次摘要信息](0202-enterprise-shift-query-in-batches.md)接口，获取已有班次ID。
2. 获取考勤组信息。

   - 获取企业下所有的考勤组信息

     - 调用服务端API-[批量获取考勤组摘要](0177-batch-query-of-simple-information-of-the-attendance-group.md)，获取企业下所有的考勤组摘要信息。
     - 调用服务端API-[批量获取考勤组详情](0178-batch-obtain-attendance-group-details.md)，获取企业下所有的考勤组详情。
   - 调用服务端API-[搜索考勤组摘要](0172-attendance-group-search.md)接口，根据考勤组名称模糊查询考勤组信息。
   - 获取单个考勤组信息

     - 根据考勤组`id`，调用服务端API-[获取考勤组详情](0173-query-a-single-attendance-group.md)，获取单个考勤组的考勤组详情信息。
     - 根据groupKey获取考勤组详情

       1. 根据考勤组`id`，调用服务端API-[groupId转换为groupKey](0176-groupid-to-groupkey.md)接口，获取考勤组`groupKey`。
       2. 根据考勤组`groupKey`，调用服务端API-[根据groupKey查询考勤组信息](0174-queries-attendance-group-information-by-id.md)接口，获取考勤组信息。
3. 根据考勤组`id`，调用服务端API-[更新考勤组](0170-attendance-group-update-interface.md)，修改考勤组名称、考勤组班次等信息。
4. 根据考勤组`groupKey`，调用服务端API-[删除考勤组](0171-delete-attendance-group.md)接口，实现删除考勤组。

## 实施步骤

### **步骤一：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤二：添加接口权限**

1. 在应用详情页，单击**权限管理**。
2. 在权限搜索框中输入以下权限标识并申请：

   - `qyapi_attendance_group_manage`（考勤组管理权限）— 用于创建、更新、删除考勤组。
   - `qyapi_attendance_group_read`（考勤组查询权限）— 用于查询考勤组摘要和详情。

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（access\_token）

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

**最佳实践**：

- **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：**核心API调用

#### 创建考勤组

> **[!NOTE]**
>
> 本文档示例采用固定班制考勤组信息。

如果需要创建固定班制考勤组，调用创建考勤组接口前，需确保已设置了班次：

- 如果无班次，调用服务端API-[创建班次](0197-create-modify-shifts.md)接口，获取班次ID。

  ```
  public void createShift() throws ApiException {
      DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/shift/add");
      OapiAttendanceShiftAddRequest request = new OapiAttendanceShiftAddRequest();
      request.setOpUserId("ma*****75");

      // 班次基本信息
      OapiAttendanceShiftAddRequest.TopAtClassVo topAtClassVo = new OapiAttendanceShiftAddRequest.TopAtClassVo();
      topAtClassVo.setOwner("ma******75");
      topAtClassVo.setClassGroupName("1009班次");
      topAtClassVo.setCorpId("ding******288");
      topAtClassVo.setName("新班次");

      // 班次时间段配置（上班 & 下班）
      List<OapiAttendanceShiftAddRequest.TopAtSectionVo> sectionVos = new ArrayList<>();
      OapiAttendanceShiftAddRequest.TopAtSectionVo sectionVo = new OapiAttendanceShiftAddRequest.TopAtSectionVo();

      List<OapiAttendanceShiftAddRequest.TopAtTimeVo> timeVos = new ArrayList<>();

      // 上班时间
      OapiAttendanceShiftAddRequest.TopAtTimeVo timeVo = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
      timeVo.setAcross(0L);
      timeVo.setBeginMin(60L);
      timeVo.setCheckTime(StringUtils.parseDateTime("2022-10-09 09:00:00"));
      timeVo.setCheckType("OnDuty");
      timeVo.setEndMin(30L);
      timeVo.setFreeCheck(false);
      timeVos.add(timeVo);

      // 下班时间
      OapiAttendanceShiftAddRequest.TopAtTimeVo timeVo1 = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
      timeVo1.setAcross(0L);
      timeVo1.setBeginMin(0L);
      timeVo1.setCheckTime(StringUtils.parseDateTime("2022-10-09 18:00:00"));
      timeVo1.setCheckType("OffDuty");
      timeVo1.setEndMin(-1L);
      timeVo1.setFreeCheck(false);
      timeVos.add(timeVo1);

      sectionVo.setTimes(timeVos);
      sectionVos.add(sectionVo);
      topAtClassVo.setSections(sectionVos);

      // 班次设置
      OapiAttendanceShiftAddRequest.TopAtClassSettingVo settingVo = new OapiAttendanceShiftAddRequest.TopAtClassSettingVo();
      settingVo.setCorpId("ding16*******c288");
      settingVo.setIsDeleted("N");
      settingVo.setAbsenteeismLateMinutes(60L);
      settingVo.setIsFlexible(false);
      settingVo.setSeriousLateMinutes(30L);

      // 休息开始时间
      OapiAttendanceShiftAddRequest.TopAtTimeVo restBeginTime = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
      restBeginTime.setFreeCheck(false);
      restBeginTime.setAcross(0L);
      restBeginTime.setCheckType("OnDuty");
      restBeginTime.setCheckTime(StringUtils.parseDateTime("2022-10-09 12:00:00"));
      settingVo.setRestBeginTime(restBeginTime);

      // 休息结束时间
      OapiAttendanceShiftAddRequest.TopAtTimeVo restEndTime = new OapiAttendanceShiftAddRequest.TopAtTimeVo();
      restEndTime.setAcross(0L);
      restEndTime.setCheckType("OffDuty");
      restEndTime.setFreeCheck(false);
      restEndTime.setCheckTime(StringUtils.parseDateTime("2022-10-09 13:00:00"));
      settingVo.setRestEndTime(restEndTime);

      topAtClassVo.setSetting(settingVo);

      request.setShift(topAtClassVo);

      OapiAttendanceShiftAddResponse response = client.execute(request, "access_token");
      System.out.println(response.getBody());
  }
  ```
- 如果已有班次，调用服务端API-[获取班次摘要信息](0202-enterprise-shift-query-in-batches.md)接口，获取已有班次ID。

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

接口说明：调用服务端API-[创建考勤组](0169-attendance-group-write.md)接口，获取考勤组`id`。

```
public void createGroup() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/add");
    OapiAttendanceGroupAddRequest req = new OapiAttendanceGroupAddRequest();
    req.setOpUserId("ma*****75");

    // 考勤组相关信息
    OapiAttendanceGroupAddRequest.TopGroupVo topGroupVo = new OapiAttendanceGroupAddRequest.TopGroupVo();
    topGroupVo.setOwner("ma*****75");
    topGroupVo.setEnableEmpSelectClass(true);
    topGroupVo.setCorpId("ding***********288");
    topGroupVo.setSkipHolidays(true);
    topGroupVo.setEnableOutsideCameraCheck(true);

    // 打卡位置配置
    List<OapiAttendanceGroupAddRequest.TopPositionVo> positionVos = new ArrayList<>();
    OapiAttendanceGroupAddRequest.TopPositionVo topPositionVo = new OapiAttendanceGroupAddRequest.TopPositionVo();
    topPositionVo.setAddress("生物科技产业园区经二路21号");
    topPositionVo.setCorpId("ding*******288");
    topPositionVo.setLatitude("36.687495");
    topPositionVo.setAccuracy("0");
    topPositionVo.setTitle("青藏高原自然博物馆");
    topPositionVo.setLongitude("101.750329");
    positionVos.add(topPositionVo);
    topGroupVo.setPositions(positionVos);

    topGroupVo.setModifyMember(true);
    topGroupVo.setType("FIXED");
    topGroupVo.setEnableFaceCheck(false);
    topGroupVo.setCheckNeedHealthyCode(true);
    topGroupVo.setEnableCameraCheck(false);

    // 班次配置
    List<OapiAttendanceGroupAddRequest.TopShiftVo> topShiftVos = new ArrayList<>();
    OapiAttendanceGroupAddRequest.TopShiftVo topShiftVo = new OapiAttendanceGroupAddRequest.TopShiftVo();
    topShiftVo.setId(1006170802L);
    topShiftVos.add(topShiftVo);
    topGroupVo.setShiftVoList(topShiftVos);

    topGroupVo.setEnableOutsideCheck(false);

    // 成员配置
    List<OapiAttendanceGroupAddRequest.TopMemberVo> memberVos = new ArrayList<>();
    OapiAttendanceGroupAddRequest.TopMemberVo topMemberVo = new OapiAttendanceGroupAddRequest.TopMemberVo();
    topMemberVo.setRole("Attendance");
    topMemberVo.setCorpId("ding********288");
    topMemberVo.setType("StaffMember");
    topMemberVo.setUserId("014***********041");
    memberVos.add(topMemberVo);
    topGroupVo.setMembers(memberVos);

    topGroupVo.setName("新考勤");
    topGroupVo.setEnableNextDay(false);
    topGroupVo.setManagerList(Arrays.asList("08*******272", "ma*******75"));
    topGroupVo.setWorkdayClassList(Arrays.asList(0L, 1006170802L, 1006170802L, 1006170802L, 1006170802L, 1006170802L, 0L));
    topGroupVo.setDefaultClassId(1006170802L);
    topGroupVo.setOffset(300L);

    // 管理角色权限配置
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

    // 考勤WiFi打卡相关配置信息（已注释）
    // List<OapiAttendanceGroupAddRequest.TopWifiVo> topWifiVos = new ArrayList<>();
    // OapiAttendanceGroupAddRequest.TopWifiVo topWifiVo = new OapiAttendanceGroupAddRequest.TopWifiVo();
    // topWifiVos.add(topWifiVo);
    // topWifiVo.setMacAddr("C0:E0:D0:E0:C0:0F");
    // topWifiVo.setSsid("OFFICE-WiFi");
    // topWifiVo.setCorpId("dinge8xxxx");
    // topGroupVo.setWifis(topWifiVos);

    topGroupVo.setDisableCheckWithoutSchedule(true);
    topGroupVo.setFreecheckDayStartMinOffset(240L);
    topGroupVo.setDisableCheckWhenRest(true);

    req.setTopGroup(topGroupVo);

    OapiAttendanceGroupAddResponse rsp = client.execute(req, "access_token");
    System.out.println(rsp.getBody());
}
```

#### 获取考勤组信息

- **获取企业下所有的考勤组信息**

  1. **批量获取考勤组摘要**：调用服务端API-[批量获取考勤组摘要](0177-batch-query-of-simple-information-of-the-attendance-group.md)，获取企业下所有的考勤组摘要信息。

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
  2. **批量获取考勤组详情**：调用服务端API-[批量获取考勤组详情](0178-batch-obtain-attendance-group-details.md)，获取企业下所有的考勤组详情。

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
  3. **搜索考勤组摘要**：调用服务端API-[搜索考勤组摘要](0172-attendance-group-search.md)接口，根据考勤组名称模糊查询考勤组信息。

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
- **获取单个考勤组信息**

  1. **获取单个考勤组详情**：根据考勤组`id`，调用服务端API-[获取考勤组详情](0173-query-a-single-attendance-group.md)，获取单个考勤组的考勤组详情信息。

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
  2. **groupId转换为groupKey**：根据考勤组`id`，调用服务端API-[groupId转换为groupKey](0176-groupid-to-groupkey.md)接口，获取考勤组`groupKey`。

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
  3. **根据groupKey查询考勤组信息**：根据考勤组`groupKey`，调用服务端API-[根据groupKey查询考勤组信息](0174-queries-attendance-group-information-by-id.md)接口，获取考勤组信息。

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

#### 更新考勤组

根据考勤组`id`，调用服务端API-[更新考勤组](0170-attendance-group-update-interface.md)，修改考勤组名称、考勤组班次等信息。

```
public void updateGroup() throws ApiException {
    DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/modify");

    OapiAttendanceGroupModifyRequest req = new OapiAttendanceGroupModifyRequest();
    req.setOpUserId("ma*****75");

    // 考勤组基本信息
    OapiAttendanceGroupModifyRequest.TopGroupVo topGroupVo = new OapiAttendanceGroupModifyRequest.TopGroupVo();
    topGroupVo.setId(1010195506L); // 考勤组ID
    topGroupVo.setName("新考勤组1");
    topGroupVo.setOwner("ma*****75");
    topGroupVo.setEnableEmpSelectClass(false);
    topGroupVo.setSkipHolidays(true);
    topGroupVo.setEnableFaceCheck(true);
    topGroupVo.setOpenCameraCheck(false);
    topGroupVo.setOpenFaceCheck(false);
    topGroupVo.setEnableOutsideCheck(false);
    topGroupVo.setDisableCheckWithoutSchedule(false);
    topGroupVo.setOffset(500L);
    topGroupVo.setManagerList(Arrays.asList("0147******041", "0852*******72"));

    // 打卡位置配置
    List<OapiAttendanceGroupModifyRequest.TopPositionVo> positionVos = new ArrayList<>();
    OapiAttendanceGroupModifyRequest.TopPositionVo topPositionVo = new OapiAttendanceGroupModifyRequest.TopPositionVo();
    topPositionVo.setAddress("生物科技产业园区经二路21号");
    topPositionVo.setCorpId("din***********88");
    topPositionVo.setLatitude("30.123");
    topPositionVo.setLongitude("120.123");
    topPositionVo.setAccuracy("0");
    topPositionVo.setTitle("青藏高原自然博物馆");
    positionVos.add(topPositionVo);
    topGroupVo.setPositions(positionVos);

    // 班次配置
    List<OapiAttendanceGroupModifyRequest.TopShiftVo> topShiftVos = new ArrayList<>();
    OapiAttendanceGroupModifyRequest.TopShiftVo topShiftVo = new OapiAttendanceGroupModifyRequest.TopShiftVo();
    topShiftVo.setId(1006170802L); // 班次ID
    topShiftVos.add(topShiftVo);
    topGroupVo.setShiftVoList(topShiftVos);

    // 工作日班次列表（1006170802L：班次ID）
    topGroupVo.setWorkdayClassList(Arrays.asList(0L, 1006170802L, 1006170802L, 1006170802L, 1006170802L, 1006170802L, 0L));

    req.setTopGroup(topGroupVo);

    OapiAttendanceGroupModifyResponse rsp = client.execute(req, "access_token");
    System.out.println(rsp.getBody());
}
```

#### 删除考勤组

根据考勤组`groupKey`，调用服务端API-[删除考勤组](0171-delete-attendance-group.md)接口，实现删除考勤组。

> **[!NOTE]**
>
> - 确认该考勤组下无在职员工（先调用获取考勤组详情接口检查）。
> - 将该考勤组关联的待办事项、审批单等转移给其他考勤组。
> - 备份该考勤组的历史数据（如有必要）。
> - 通知相关部门（IT、HR、行政等）进行后续清理工作。

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

## **常见问题（FAQ）**

- **Q1：创建考勤组时提示"班次不存在"怎么办？**

  A：固定班制考勤组需要先创建班次。请先调用[创建班次](0197-create-modify-shifts.md)接口，或调用[获取班次摘要信息](0202-enterprise-shift-query-in-batches.md)接口获取已有班次ID，再创建考勤组。
- **Q2：如何批量获取所有考勤组信息？**

  A：分两步操作：先调用[批量获取考勤组摘要](0177-batch-query-of-simple-information-of-the-attendance-group.md)获取所有考勤组的简要信息（含id），再根据需要调用[批量获取考勤组详情](0178-batch-obtain-attendance-group-details.md)获取完整详情。
- **Q3：考勤组id和groupKey有什么区别？**

  A：`id`是考勤组的数字标识，`groupKey`是字符串标识。部分接口（如删除考勤组）需要使用`groupKey`。可通过[groupId转换为groupKey](0176-groupid-to-groupkey.md)接口进行转换。
- **Q4：更新考勤组时是否需要传入所有字段？**

  A：不需要。只需传入要修改的字段和考勤组`id`即可，未传入的字段保持原值不变。
