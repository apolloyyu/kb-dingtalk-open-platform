---
title: "企业自研考勤系统补卡同步"
source_url: "https://open.dingtalk.com/document/development/the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized"
namespace: "development"
slug: "the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 企业自研考勤系统补卡同步"
doc_id: "nTMMOfrMW3"
updated_at: "2026-09-20 09:32:30"
---

> Source: https://open.dingtalk.com/document/development/the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 企业自研考勤系统补卡同步
> Updated: 2026-09-20 09:32:30

# 企业自研考勤系统补卡同步

通过API实现自有OA/假勤系统与钉钉考勤的补卡信息自动同步，审批通过后实时更新钉钉考勤状态为"补卡通过"，撤销后自动恢复原始打卡状态，消除双系统并行带来的数据不一致与人工重复操作。

## 概述

本方案提供一套完整的企业自研考勤系统补卡同步解决方案，通过钉钉开放平台的考勤补卡API，实现自有OA/假勤系统与钉钉考勤应用的无缝集成。

### 方案背景

企业在日常考勤管理中，员工因外出、忘打卡等原因需要补卡时，通常在企业自有OA或假勤系统中发起补卡申请。然而，钉钉考勤系统中的缺卡记录不会自动同步这些外部审批结果，导致员工需要在两个系统中重复操作：先在自有系统提交补卡审批，再手动在钉钉中修改考勤状态。这种双系统并行不仅增加员工负担，还容易造成数据不一致，影响考勤统计的准确性。

### 核心价值

企业通过本方案可以实现自有考勤系统与钉钉考勤的补卡信息自动同步，将原本依赖人工操作的跨系统数据同步流程转化为API驱动的标准化作业，显著提升考勤管理效率与数据一致性。

- **跨系统自动同步**：自有假勤系统审批通过后，自动调用钉钉API同步补卡信息，无需员工二次操作。
- **状态精准映射**：根据审批结果（通过/撤销）自动更新钉钉考勤状态为"补卡通过"或恢复原打卡状态。
- **排班智能匹配**：同步前自动查询员工对应日期的排班打卡时间点，确保补卡信息准确关联。
- **审批流解耦**：补卡同步不产生钉钉补卡审批单，避免重复审批，保持自有系统审批流程独立性。

### 适用场景

本方案适用于以下典型业务场景：

- **自有OA系统补卡同步**：员工在自有OA系统提交补卡申请并审批通过后，自动同步到钉钉考勤。
- **第三方假勤平台对接**：使用第三方假勤管理系统时，审批结果实时同步至钉钉考勤应用。
- **批量补卡处理**：HR批量导入历史补卡记录时，自动同步到钉钉考勤系统。
- **补卡撤销同步**：员工撤销自有系统补卡申请后，自动恢复钉钉考勤原始打卡状态。

## 典型业务场景

### 场景一：自有OA系统补卡审批通过后同步钉钉

#### 痛点分析

传统模式下，员工在自有OA系统提交补卡申请并通过审批后，仍需登录钉钉APP手动修改当天考勤状态为"补卡"，或在钉钉中重新提交补卡审批。对于每月有数十次补卡需求的企业，员工需重复操作多次，且容易遗漏或选错日期，导致考勤数据不准确。

#### 价值验证

- **自动化流程**

图：自有OA系统补卡审批通过后同步钉钉流程

- **关键优势**

  - **全自动触发**：自有OA系统审批通过后自动调用钉钉API同步补卡信息，员工零感知。
  - **精准匹配**：同步前自动查询员工对应日期排班打卡时间点，确保补卡信息准确关联。
  - **实时生效**：补卡信息同步后立即生效，钉钉考勤状态从"缺卡"变更为"补卡通过"。
  - **审批流解耦**：补卡同步不产生钉钉补卡审批单，避免重复审批，保持自有系统审批独立性。

### 场景二：补卡申请撤销后恢复原始打卡状态

#### 痛点分析

当员工在自有OA系统撤销补卡申请后，钉钉考勤系统中的补卡状态不会自动恢复，仍显示为"补卡通过"。HR需手动登录钉钉后台逐一修正，耗时耗力且容易遗漏，导致考勤统计数据失真。

#### 价值验证

图：补卡申请撤销后恢复原始打卡状态流程

- **自动化流程**
- **关键优势**

  - **状态自动回滚**：自有系统撤销补卡申请后，自动调用钉钉API恢复原始打卡状态。
  - **数据一致性保障**：确保钉钉考勤状态与自有OA系统审批结果始终保持一致。
  - **审计留痕**：每次同步/撤销操作记录操作人、时间戳、审批单ID，满足合规要求。
  - **异常可追溯**：同步失败时记录详细错误日志，便于问题排查与修复。

## 实施指南

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

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 员工在自有考勤系统提交补卡申请时，根据员工选择的补卡日期调用服务端API-[查询成员排班信息](0207-query-scheduling-for-a-day.md)接口，获取对应日期该员工的排班打卡时间点。
2. 员工使用自有假勤系统发起补卡审批单，审批结果不同，触发的操作不同。

   - 如果审批通过，调用服务端API-[通知补卡通过](0230-make-up-the-card-after-approval.md)接口，提交的补卡信息会同步到钉钉考勤应用，考勤状态从缺卡修改为补卡通过。

     > **[!NOTE]**
     >
     > 本步骤不会在钉钉中产生补卡审批单。
   - 如果员工撤销了补卡申请，可以调用服务端API-[通知审批撤销](0229-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，撤销已同步到钉钉的补卡审申请，考勤状态恢复到修改之前的打卡状态。

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

   - `qyapi_attendance_group_manage`（考勤组管理权限）— 用于同步补卡信息、撤销补卡。
   - `qyapi_attendance_group_read`（考勤组查询权限）— 用于查询员工排班信息。

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

### **步骤四：核心API调用**

1. **查询成员排班信息**：员工在自有考勤系统提交补卡申请时，根据员工选择的补卡日期调用服务端API-[查询成员排班信息](0207-query-scheduling-for-a-day.md)接口，获取对应日期该员工的排班打卡时间点。

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
2. **通知补卡通过**：员工使用自有假勤系统发起补卡审批单，如果审批通过，调用服务端API-[通知补卡通过](0230-make-up-the-card-after-approval.md)接口，提交的补卡信息会同步到钉钉考勤应用，考勤状态从缺卡修改为补卡通过。

   > **[!NOTE]**
   >
   > 本步骤不会在钉钉中产生补卡审批单，仅同步补卡结果到考勤记录。

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

   **参数说明：**

   | **参数** | **类型** | **必填** | **说明** |
   | --- | --- | --- | --- |
   | userid | String | 是 | 员工userId。 |
   | workDate | String | 是 | 补卡工作日期。 |
   | punchId | Long | 是 | 要补的排班ID，从查询排班接口获取。 |
   | punchCheckTime | String | 是 | 排班的打卡时间。 |
   | userCheckTime | String | 是 | 用户打卡时间。 |
   | approveId | String | 是 | 审批单ID，自定义值。 |
   | jumpUrl | String | 否 | 审批单跳转地址。 |
   | tagName | String | 否 | 审批单名称。 |
3. **通知审批撤销**：如果员工撤销了补卡申请，可以调用服务端API-[通知审批撤销](0229-notify-the-attendance-to-modify-the-punch-result-when-the.md)接口，撤销已同步到钉钉的补卡审申请，考勤状态恢复到修改之前的打卡状态。

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

**实施完成检查清单**：

- ✅ 所有API调用均返回成功状态码（errcode=0）。
- ✅ 补卡同步后调用查询排班接口验证打卡时间点正确。
- ✅ 撤销操作后验证考勤状态已恢复为原始状态。
- ✅ 错误日志记录完整，包含审批单ID、员工userId、操作时间。
- ✅ 自有OA系统与钉钉考勤补卡数据定期比对一致。

## **常见问题（FAQ）**

- **Q1：补卡同步和钉钉原生补卡审批有什么区别？**

  A：两者定位完全不同：

  - 钉钉原生补卡审批：员工在钉钉APP中发起补卡申请→主管审批→自动更新考勤状态。适用于无自有OA系统的企业。
  - 本方案补卡同步：员工在自有OA/假勤系统发起补卡→OA审批通过→API同步到钉钉。适用于已有成熟OA审批流的企业，避免员工在两个系统中重复操作。

  **核心差异**：本方案不产生钉钉补卡审批单，仅将OA审批结果同步到钉钉考勤记录，保持自有系统审批流程的独立性。
- **Q2：批量补卡同步时，部分员工失败如何处理？**

  A：批量补卡同步建议采用"逐条处理+失败重试"策略：

  1. **分批处理**：每次批量不超过50人，避免单次请求超时。
  2. **失败隔离**：解析返回结果，提取失败员工的userId及错误原因（errcode/errmsg）。
  3. **分类处理**：

     - `用户不在考勤组`：检查员工是否已加入对应考勤组。
     - `日期超出范围`：确认补卡日期是否在允许补卡的时间窗口内。
     - `网络超时`：自动重试3次，间隔递增（1s/2s/4s）。
  4. **日志记录**：所有失败案例记录审批单ID、员工userId、错误原因、重试次数，便于后续人工介入。
- **Q3：如何验证补卡同步后的数据一致性？**

  A：建议建立三层校验机制：

  1. **实时校验**：补卡同步成功后，立即确认该员工当天的考勤状态已从"缺卡"变更为"补卡通过"。
  2. **定时比对**：每日凌晨运行全量比对任务，拉取自有OA系统当日补卡审批记录与钉钉考勤补卡记录，按审批单ID+员工userId匹配，发现不一致时生成告警工单。
  3. **异常监控**：对连续3次同步失败的员工触发告警，通知HR管理员手动核查（可能原因：员工离职未移除考勤组、排班未配置等）。
- **Q4：撤销补卡后，如果员工当天有正常打卡记录会怎样？**

  A：撤销操作会将钉钉考勤状态恢复为补卡前的**原始打卡状态**，具体行为如下：

  - 若补卡前为"缺卡"（未打卡）→ 撤销后恢复为"缺卡"。
  - 若补卡前为"正常打卡" → 撤销后恢复为"正常打卡"，补卡记录被清除。
  - 若补卡前为"迟到/早退" → 撤销后恢复为"迟到/早退"，补卡记录被清除。

  **重要提示**：撤销操作不可逆，一旦执行无法再次恢复补卡状态。建议在自有OA系统中增加"二次确认"环节，避免误撤销。
