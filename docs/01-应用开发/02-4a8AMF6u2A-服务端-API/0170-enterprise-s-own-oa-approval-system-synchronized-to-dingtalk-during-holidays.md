---
title: "打卡数据同步：硬件打卡记录自动上传至钉钉"
source_url: "https://open.dingtalk.com/document/development/enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays"
namespace: "development"
slug: "enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 打卡数据同步：硬件打卡记录自动上传至钉钉"
doc_id: "qieVTeeppo"
updated_at: "2026-09-23 12:04:31"
---

> Source: https://open.dingtalk.com/document/development/enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 打卡数据同步：硬件打卡记录自动上传至钉钉
> Updated: 2026-09-23 12:04:31

# 打卡数据同步：硬件打卡记录自动上传至钉钉

本文档介绍企业使用自有OA审批系统如何同步到钉钉的OA审批，支持企业自研系统的加班、出差和请假信息与钉钉考勤模块打通。

## 概述

本方案提供一套完整的假勤审批数据同步解决方案，通过钉钉开放平台的假勤审批API，实现将企业自有系统中的假勤审批数据自动同步至钉钉。

### 方案背景

企业在日常运营管理中，已部署自研的假勤管理系统用于处理员工的加班、出差和请假申请。然而，这些系统与钉钉考勤模块之间缺乏标准的数据接口，导致：

- **数据孤岛严重**：员工在自有系统提交请假申请并审批通过后，仍需手动在钉钉打卡或补卡，造成重复操作和数据不一致。
- **时长计算复杂**：不同日期的排班时长不同（如工作日8小时、周末4小时），人工计算可请假时长容易出错，且无法动态适配排班调整。
- **状态不同步**：自有系统审批通过后，钉钉考勤无法自动感知，HR需手动核对两个系统的数据，耗时且易遗漏。

### 核心价值

本方案提供一套完整的企业自有假勤审批系统与钉钉考勤集成的解决方案，通过标准化接口调用流程与最佳实践，帮助企业高效实现审批数据的自动化同步与统一管理。

- **轻量级接入**：无需改造业务系统前端，仅需调用3个核心API即可完成集成，开发成本低。
- **排班智能计算**：根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息，避免人工计算错误。
- **状态实时同步**：审批通过后自动通知钉钉考勤同步，审批撤销时自动同步撤销，确保数据一致性。
- **灵活的场景适配**：支持跨天请假、多日期排班等复杂场景，自动累加各天排班时长，提升用户体验。

### 适用场景

本方案适用于以下典型业务场景：

- **自有假勤系统集成**：将企业自研的加班、出差、请假审批系统与钉钉考勤模块打通，实现审批结果自动同步。
- **排班时长预计算**：根据员工排班情况，智能计算可提交的请假时长上限，避免超期申请或资源浪费。
- **审批结果同步**：自有系统审批通过后，自动同步至钉钉考勤，避免HR手动核对两个系统的数据。
- **跨天请假管理**：员工请假跨越多个工作日且每日排班时长不同时，自动累加各天排班时长，简化操作流程。

## 典型业务场景

### 场景一：自有假勤审批与钉钉考勤同步

#### 痛点分析

企业已部署自研的假勤管理系统，但该系统与钉钉考勤数据独立，导致员工在自有系统提交请假申请后，仍需手动在钉钉打卡或补卡。当企业规模扩大至千人以上时，手工操作几乎不可行，且容易因人为疏忽导致数据不一致。

同时，不同日期的排班时长不同（如工作日8小时、周末4小时），HR需人工计算每个员工的可请假时长，耗时且容易出错。审批通过后，钉钉考勤无法自动感知，需人工干预同步，进一步增加了管理成本。

#### 价值验证

- **自动化流程**

  ![自有假勤审批与钉钉考勤同步流程图_20260918_171736](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5597689871/p1103052.png)
- **关键优势**

  - **智能时长预计算**：根据排班自动计算最大可请假时长，避免超期申请，减少HR审核工作量。
  - **审批自动同步**：审批通过后自动通知钉钉考勤，无需二次操作，节省HR 80%的核对时间。
  - **撤销实时生效**：审批撤销后自动同步至钉钉，确保数据一致性，避免考勤统计错误。
  - **低成本接入**：仅需调用3个核心API，开发周期缩短70%，快速上线。

### 场景二：跨天请假时长智能计算

#### 痛点分析

员工请假跨越多个工作日，且每日排班时长不同（如小明10月15日排班8小时，10月16日排班4小时）。传统方式需人工累加各天排班时长，容易出错且效率低。当员工请假时间跨度较大（如一周）时，HR需逐一查询每天的排班规则，耗时且容易遗漏。

此外，若员工在请假期间遇到调休或临时排班调整，人工计算的时长可能不准确，导致请假申请被驳回或考勤数据异常。

#### 价值验证

- **自动化流程**

  ![跨天请假时长智能计算流程图_20260918_171923](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5597689871/p1103053.png)
- **关键优势**

  - **自动累加排班**：调用预计算接口，自动返回跨天请假的最大可提交时长，消除人工计算错误。
  - **精准控制**：根据实际排班动态调整可请假时长上限，避免资源浪费或超期申请。
  - **用户体验提升**：员工提交请假时无需手动计算，系统自动提示可请假时长，降低操作门槛。
  - **动态适配调整**：若排班发生变更，重新调用预计算接口即可获取最新时长，确保数据准确性。

## 实施指南

### **技术架构**

本方案基于钉钉开放平台的考勤相关OpenAPI构建，核心技术组件包括：

- **身份鉴权层**：通过 `Client ID` / `Client Secret` 获取 `access_token`，确保接口调用安全性。
- **权限管理层**：申请考勤相关接口权限（`qyapi_attendance_group_manage` 和 `qyapi_attendance_group_read`）。
- **时长预计算引擎**：调用服务端API-预计算时长接口，根据考勤系统排班情况预计算员工加班、出差及请假的时长信息。
- **审批同步层**：审批通过后调用通知审批通过接口，实现钉钉考勤同步；审批撤销时调用通知审批撤销接口，实现同步撤销。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，申请考勤相关接口权限。

  - `qyapi_attendance_group_manage`（考勤组管理权限）
  - `qyapi_attendance_group_read`（考勤组查询权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请考勤相关接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

> **[!NOTE]**
>
> 该功能支持企业自研系统的加班、出差和请假信息与钉钉同步。

1. 调用服务端API-[预计算时长](0227-api-calculateduration.md)接口，实现根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。
2. 在企业自有审批系统提交了假勤申请，审批通过后通过该接口通知钉钉考勤，调用服务端API-[通知审批通过](0228-api-processapprovefinish.md)接口，实现钉钉考勤同步通过。保存自定义审批单ID`approve_id`。
3. 在企业自有审批系统提交了撤销假勤申请，根据自定义审批单ID`approve_id`，调用服务端API-[通知审批撤销](0229-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，实现钉钉考勤同步撤销。

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

   - `qyapi_attendance_group_manage`（考勤组管理权限）
   - `qyapi_attendance_group_read`（考勤组查询权限）

> **[!NOTE]**
>
> 不同业务场景可能需要不同的权限组合，请根据实际需求申请。例如批量导入场景还需申请批量操作用户的相关权限。

### 步骤三：获取访问凭证（access\_token）

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

**最佳实践**：

- **缓存策略**：`access_token`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤四：**核心API调用

1. **预计算时长**：调用服务端API-[预计算时长](0227-api-calculateduration.md)接口，实现根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。

   > **[!NOTE]**
   >
   > 该步骤不可跳过，自有系统内的审批单信息同步到钉钉。例如，小明在10月15日的排班是8小时，10月16日的排班是4小时，如果正常上班，小明在10月15日、16日这2天的工作时间是12小时。小明在企业自有系统内提交请假审批单时，以下各情况，可提交的请假时长不同：
   >
   > - 情况一，选择请假开始时间是10月15日，结束时间是10月15日；调用[预计算时长](1545-calculate-duration-based-on-attendance-scheduling.md)接口，获取的可提交请假时长最大是8小时。
   > - 情况二，选择请假开始时间是10月15日，结束时间是10月16日，调用[预计算时长](1545-calculate-duration-based-on-attendance-scheduling.md)接口，获取的可提交请假时长最大是12小时。

   ```
   public CalculateDurationResponseBody durationCalculate(){
     com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
     config.protocol = "https";
     config.regionId = "central";
     try {
       com.aliyun.dingtalkattendance_1_0.Client client = new  com.aliyun.dingtalkattendance_1_0.Client(config);
       CalculateDurationHeaders calculateDurationHeaders = new CalculateDurationHeaders();
       calculateDurationHeaders.xAcsDingtalkAccessToken = "<your access token>";
       CalculateDurationRequest calculateDurationRequest = new CalculateDurationRequest()
         .setUserId("01472825524039877041")
         .setBizType(3L)
         .setFromTime("2022-10-13 09:00")
         .setToTime("2022-10-13 18:00")
         .setDurationUnit("day")
         .setCalculateModel(1L)
         .setLeaveCode("e2dsad-34dfa-2vas23da");
       CalculateDurationResponse calculateDurationResponse = client.calculateDurationWithOptions(calculateDurationRequest, calculateDurationHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(calculateDurationResponse.getBody());
       return calculateDurationResponse.getBody();
     } catch (Exception e) {
       throw new RuntimeException(e);
     }
   }
   ```
2. **通知审批通过**：在企业自有审批系统提交了假勤申请，审批通过后通过该接口通知钉钉考勤，调用服务端API-[通知审批通过](0228-api-processapprovefinish.md)接口，实现钉钉考勤同步通过。

   > **[!NOTE]**
   >
   > - 本步骤不会在钉钉中产生OA审批单。
   > - 保存自定义审批单ID `approve_id`，后续如需撤销审批时需使用该ID。

   ```
   public ProcessApproveFinishResponseBody approveFinish(){
     com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
     config.protocol = "https";
     config.regionId = "central";
     try {
       com.aliyun.dingtalkattendance_1_0.Client client = new  com.aliyun.dingtalkattendance_1_0.Client(config);
       ProcessApproveFinishHeaders processApproveFinishHeaders = new ProcessApproveFinishHeaders();
       processApproveFinishHeaders.xAcsDingtalkAccessToken = "<your access token>";
       ProcessApproveFinishRequest.ProcessApproveFinishRequestTopCalculateApproveDurationParam topCalculateApproveDurationParam = new ProcessApproveFinishRequest.ProcessApproveFinishRequestTopCalculateApproveDurationParam()
         .setBizType(2L)
         .setFromTime("2022-10-13 09:00")
         .setToTime("2022-10-13 19:00")
         .setDurationUnit("hour")
         .setCalculateModel(1L);
       com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishRequest processApproveFinishRequest = new com.aliyun.dingtalkattendance_1_0.models.ProcessApproveFinishRequest()
         .setUserId("manager123")
         .setTopCalculateApproveDurationParam(topCalculateApproveDurationParam)
         .setTagName("外出")
         .setApproveId("dingTalk")
         .setJumpUrl("https://open.dingtalk.com/");
       ProcessApproveFinishResponse processApproveFinishResponse = client.processApproveFinishWithOptions(processApproveFinishRequest, processApproveFinishHeaders, new com.aliyun.teautil.models.RuntimeOptions());
       System.out.println(processApproveFinishResponse.getBody());
       return processApproveFinishResponse.getBody();
     } catch (Exception e) {
       throw new RuntimeException(e);
     }
   }
   ```
3. **通知审批撤销**：在企业自有审批系统提交了撤销假勤申请，根据自定义审批单ID `approve_id`，调用服务端API-[通知审批撤销](0229-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，实现钉钉考勤同步撤销。

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

**实施完成检查清单**：

- 应用凭证获取成功（Client ID / Client Secret）。
- 考勤相关权限申请成功（qyapi\_attendance\_group\_manage / qyapi\_attendance\_group\_read）。
- access\_token获取成功。
- 预计算时长接口调用成功，返回正确的可请假时长。
- 审批通过后调用通知审批通过接口，钉钉考勤同步成功。
- 审批撤销时调用通知审批撤销接口，钉钉考勤同步撤销成功。

## **常见问题（FAQ）**

- **Q1：为什么需要先调用预计算时长接口？**

  A：预计算时长接口会根据员工的排班情况，智能计算可提交的请假时长上限。例如，员工在某天排班4小时，则当天最多只能请假4小时。跳过此步骤可能导致请假时长与实际排班不匹配，影响考勤数据统计准确性。
- **Q2：approve\_id的作用是什么？**

  A：`approve_id` 是自定义审批单的唯一标识，由业务系统生成并保存。当需要撤销审批时，必须通过该ID调用通知审批撤销接口，钉钉才能准确定位并撤销对应的考勤记录。
- **Q3：本方案会在钉钉中产生OA审批单吗？**

  A：不会。本方案仅实现自有系统审批结果与钉钉考勤的数据同步，不会在钉钉OA审批中心创建审批实例。审批流程仍在自有系统中完成，钉钉仅作为考勤数据的接收方。
- **Q4：如果员工跨天请假，预计算时长接口如何工作？**

  A：接口会自动累加请假期间所有工作日的排班时长。例如，小明10月15日排班8小时，10月16日排班4小时，若请假时间为10月15日至10月16日，接口返回的最大可请假时长为12小时（8+4）。
- **Q5：权限申请失败怎么办？**

  A：请确认以下几点：

  - 应用类型是否为"企业内部应用"
  - 账号是否具有企业管理员或子管理员权限
  - 权限标识是否输入正确（`qyapi_attendance_group_manage` 和 `qyapi_attendance_group_read`）
  - 如仍失败，联系钉钉技术支持提供应用ID和错误日志
