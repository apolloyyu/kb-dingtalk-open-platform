---
title: "考勤组成员管理自动化"
source_url: "https://open.dingtalk.com/document/development/attendance-group-member-operations"
namespace: "development"
slug: "attendance-group-member-operations"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 考勤组成员管理自动化"
doc_id: "HpgAC8DZHF"
updated_at: "2026-09-17 09:36:38"
---

> Source: https://open.dingtalk.com/document/development/attendance-group-member-operations
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 考勤组成员管理自动化
> Updated: 2026-09-17 09:36:38

# 考勤组成员管理自动化

通过钉钉开放平台考勤组成员管理API，实现HR/OA系统与钉钉考勤成员体系的无缝集成，解决传统人工维护考勤组成员效率低、易出错、无法批量操作等核心痛点。

## 概述

### 方案背景

企业日常运营中，员工入职、离职、调岗、部门调整等组织变动频繁发生。每次变动都需要HR或管理员手动在钉钉后台逐一调整考勤组成员名单：新增员工加入考勤组、离职员工移除、调岗员工切换考勤组。对于千人级企业，每月可能有数十至上百人次的组织变动，手工操作不仅耗时耗力，还容易出现遗漏或错误，导致员工打卡异常、考勤数据不准确等问题。

### 核心价值

企业通过本方案可以实现考勤组成员的自动化全生命周期管理，将原本依赖人工操作的批量新增、查询、更新、删除等流程转化为API驱动的标准化作业，显著提升HR系统运维效率与数据一致性。

- **成员批量自动化管理**：新增、查询、更新、删除等操作通过API自动完成，零人工干预。
- **多接口精准适配**：针对个人/部门/混合成员场景，智能选择最优查询接口，确保数据获取完整准确。
- **实时校验反馈**：支持校验用户是否在指定考勤组内，更新后立即验证，保障数据一致性。
- **跨系统数据统一**：HR系统、OA系统与钉钉考勤组成员数据实时同步，消除信息孤岛。

### 适用场景

本方案适用于以下典型业务场景：

- **新员工入职**：HR系统录入新员工后，自动将其加入对应部门的考勤组。
- **员工离职处理**：OA离职审批通过后，自动从所有考勤组中移除该员工。
- **岗位调动同步**：员工调岗时，自动从原考勤组移除并加入新部门考勤组。
- **批量人员调整**：组织架构调整后，批量更新多个考勤组的成员名单。

## 典型业务场景

### 场景一：新员工入职自动加入考勤组

#### 痛点分析

传统模式下，HR在新员工入职当天需手动登录钉钉后台，查找对应部门的考勤组，逐个添加新员工到考勤组。若企业每日有5-10人入职，HR需重复操作多次，且容易遗漏或选错考勤组，导致新员工无法正常打卡。

#### 价值验证

- **自动化流程**

  ![新员工入职自动加入考勤组流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8998069871/p1102590.png)
- **关键优势**

  - **全自动触发**：HR系统录入新员工后自动调用API加入考勤组，无需人工发起。
  - **精准匹配**：根据员工所属部门自动匹配对应考勤组，避免人工选错。
  - **实时生效**：加入后立即校验确认，确保新员工当日即可正常打卡。
  - **审计留痕**：每次操作记录操作人、时间戳、考勤组ID，满足合规要求。

### 场景二：员工离职自动移除考勤组

#### 痛点分析

员工离职时，HR需手动从所有相关考勤组中移除该员工。若员工同时属于多个考勤组（如主部门+项目组），人工逐一查找并移除极易遗漏，导致离职员工仍可打卡、考勤数据异常，甚至引发薪资计算错误。

#### 价值验证

- **自动化流程**

  ![员工离职自动移除考勤组流程](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8998069871/p1102591.png)
- **关键优势**

  - **全自动触发**：OA离职审批通过后自动执行移除操作，无需人工介入。
  - **全面覆盖**：一次性查询并移除该员工在所有考勤组中的记录，避免遗漏。
  - **即时生效**：移除后立即校验确认，确保离职员工无法继续打卡。
  - **审计日志完整**：每次移除操作均记录详细信息，满足合规审计与追溯要求。

## 实施指南

### 技术架构

本方案基于钉钉开放平台的服务端API构建，核心技术组件包括：

- **身份鉴权层**：通过 `Client ID` / `Client Secret` 获取 `access_token`，确保接口调用安全性。
- **成员管理层**：提供批量新增、查询、更新、删除考勤组成员的完整API能力。
- **智能路由层**：根据成员类型（个人/部门/混合）自动选择最优查询接口，确保数据获取完整。
- **错误处理层**：完善的错误码体系与重试机制，便于快速定位和解决问题。

**API版本说明**：服务端API存在新版与旧版差异，建议优先使用新版API以获得更好的性能和功能支持。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_attendance_group_manage`（考勤组管理权限）
  - `qyapi_attendance_group_read`（考勤组读取权限）
- **开发环境**：已安装Java开发环境(JDK1.6及以上)及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请 `qyapi_attendance_group_manage` 和 `qyapi_attendance_group_read` 权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1443-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用考勤相关API：

1. 调用服务端API-[批量新增参与考勤人员](0180-batch-add-employees-under-the-attendance-group.md)接口，实现新增考勤组参与考勤人员。
2. 调用服务端API-[获取用户考勤组](0179-queries-a-user-attendance-group.md)，获取用户所在考勤组信息。
3. 获取考勤组内参与考勤人员信息

   - 调用服务端API-[获取参与考勤人员的userid](0183-query-attendance-group-personnel-information-in-batches.md)接口，获取参与考勤人员的userId信息。
   - 调用服务端API-[获取参与考勤人员](0182-batch-query-of-attendance-group-members.md#undefined)接口，获取参与考勤人员信息。
   - 调用服务端API-[查询参与考勤人员列表](0185-batch-query-of-employees-in-the-attendance-group.md)，获取参与考勤人员列表信息。
4. 调用服务端API-[校验用户是否在当前考勤组](0186-query-members-by-id.md)接口，实现校验某个部门或者员工，是否在某考勤组内。
5. 调用服务端API-[更新参与考勤人员](0181-attendance-group-member-update.md)接口，实现更新考勤组参与考勤人员。
6. 调用服务端API-[批量删除参与考勤人员](0184-batch-delete-employees-under-the-attendance-group.md)接口，实现删除参与考勤人员。

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

> **[!NOTE]**
>
> 考勤组管理的操作流程，详情参见[考勤组管理自动化](0162-operation-related-to-attendance-group.md)。

1. **批量新增参与考勤人员**：调用服务端API-[批量新增参与考勤人员](0180-batch-add-employees-under-the-attendance-group.md)接口，实现新增考勤组参与考勤人员。

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
2. **获取用户所在考勤组**：调用服务端API-[获取用户考勤组](0179-queries-a-user-attendance-group.md)，获取用户所在考勤组信息。

   ```
    public void attendanceUserGroup() throws ApiException {
           DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/getusergroup");
           OapiAttendanceGetusergroupRequest req = new OapiAttendanceGetusergroupRequest();
           req.setUserid("0852**********72");
           OapiAttendanceGetusergroupResponse rsp = client.execute(req, "access_token");
           System.out.println(rsp.getBody());
       }
   ```
3. **获取考勤组内参与考勤人员信息**

   下列三个获取考勤组成员信息接口的区别，主要针对考勤组参与人员有部门的情况。![考勤组成员](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4181657361/p351816.png)

   | 接口列表 | 张三userid | 测试部门ID | 测试部门员工userId |
   | --- | --- | --- | --- |
   | [获取参与考勤人员的userid](0183-query-attendance-group-personnel-information-in-batches.md) | ✅ | ❎ | ✅ |
   | [获取参与考勤人员](0182-batch-query-of-attendance-group-members.md) | ✅ | ✅ | ❎ |
   | [查询参与考勤人员列表](0185-batch-query-of-employees-in-the-attendance-group.md) | ✅ | ❎ | ❎ |

   **注**：✅代表可以获取到 ❎代表获取不到

   - **获取参与考勤人员的userId**：调用服务端API-[获取参与考勤人员的userid](0183-query-attendance-group-personnel-information-in-batches.md)接口，获取参与考勤人员的userId信息。

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
   - **获取参与考勤人员信息**：调用服务端API-[获取参与考勤人员](0182-batch-query-of-attendance-group-members.md)接口，获取参与考勤人员信息。

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
   - **查询参与考勤人员列表（支持分页）：**调用服务端API-[查询参与考勤人员列表](0185-batch-query-of-employees-in-the-attendance-group.md)，获取参与考勤人员列表信息。

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
4. **校验用户是否在当前考勤组**：调用服务端API-[校验用户是否在当前考勤组](0186-query-members-by-id.md)接口，确认某员工是否属于指定考勤组。

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
5. **更新参与考勤人员**：调用服务端API-[更新参与考勤人员](0181-attendance-group-member-update.md)接口，调整考勤组成员名单（添加/移除员工或部门）。

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
6. **批量删除参与考勤人员**：调用服务端API-[批量删除参与考勤人员](0184-batch-delete-employees-under-the-attendance-group.md)接口，从考勤组中移除离职或调岗员工。

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

**实施完成检查清单**：

- ✅ 所有API调用均返回成功状态码（errcode=0）。
- ✅ 新增/删除操作后调用校验接口确认结果。
- ✅ 错误日志记录完整，便于问题追溯。
- ✅ HR系统与钉钉考勤组成员数据定期比对一致。

## **常见问题（FAQ）**

- **Q1：三个查询成员接口的区别是什么？**

  A：三个接口针对不同成员类型场景：

  - [获取参与考勤人员的userid](0183-query-attendance-group-personnel-information-in-batches.md)：仅返回userId列表，适合只需判断成员是否存在于考勤组的场景。
  - [获取参与考勤人员](0182-batch-query-of-attendance-group-members.md)：返回成员详细信息（姓名、部门等），适合需要展示成员详情的场景。
  - [查询参与考勤人员列表](0185-batch-query-of-employees-in-the-attendance-group.md)：支持分页查询，适合考勤组成员数量较多时的分批获取场景。

  当考勤组包含部门成员时，需注意：若查询个人userId，可获取该员工信息；若查询部门ID，则无法直接获取部门下员工详情，需额外调用部门成员查询接口。
- **Q2：批量新增成员时，部分成员失败如何处理？**

  A：批量新增接口采用"尽力而为"策略，成功与失败的成员会分别返回。建议：

  1. 解析返回结果，提取失败成员的userId及错误原因。
  2. 记录失败日志，分析失败原因（如用户不存在、已在考勤组中等）。
  3. 对可修复的错误（如用户刚创建尚未同步）进行重试。
  4. 对不可修复的错误（如用户已离职）跳过并记录。
- **Q3：如何确保离职员工被完全移除？**

  A：建议采用以下步骤确保彻底移除：

  1. OA离职审批通过后，调用[获取用户考勤组](0179-queries-a-user-attendance-group.md)接口，获取该员工所在的所有考勤组ID。
  2. 遍历所有考勤组，调用[批量删除参与考勤人员](0184-batch-delete-employees-under-the-attendance-group.md)接口移除该员工。
  3. 调用[校验用户是否在当前考勤组](0186-query-members-by-id.md)接口，确认该员工已从所有考勤组中移除。
  4. 记录操作日志，包含考勤组ID列表、操作时间、操作人等信息。
