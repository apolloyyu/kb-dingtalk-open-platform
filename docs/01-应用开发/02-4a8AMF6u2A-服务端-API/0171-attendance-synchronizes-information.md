---
title: "假勤审批集成：假勤数据自动同步至钉钉考勤"
source_url: "https://open.dingtalk.com/document/development/attendance-synchronizes-information"
namespace: "development"
slug: "attendance-synchronizes-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 假勤审批集成：假勤数据自动同步至钉钉考勤"
doc_id: "ANOoKtLNB2"
updated_at: "2026-09-23 12:04:32"
---

> Source: https://open.dingtalk.com/document/development/attendance-synchronizes-information
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 假勤审批集成：假勤数据自动同步至钉钉考勤
> Updated: 2026-09-23 12:04:32

# 假勤审批集成：假勤数据自动同步至钉钉考勤

本文档介绍企业使用自有考勤系统或第三方考勤设备如何同步打卡记录到钉钉考勤模块，支持将门禁刷卡、指纹机、人脸识别等设备的打卡数据自动汇聚至钉钉，实现统一考勤管理。

## 概述

本方案提供一套完整的考勤打卡数据同步解决方案，通过钉钉开放平台的考勤打卡API，实现将企业自有系统中的员工打卡记录自动同步至钉钉考勤应用。

### **方案背景**

企业在日常运营管理中，已部署自研考勤系统或第三方考勤设备（如门禁刷卡、指纹机、人脸识别机等）用于记录员工上下班打卡。然而，这些系统与钉钉考勤模块之间缺乏标准的数据接口，导致：

- **手工补卡效率低**：员工在自有系统打卡后，需在钉钉中手动补卡，操作繁琐且易遗漏。
- **数据不同步**：自有考勤系统与钉钉考勤数据分散，HR需要跨系统核对考勤记录。
- **实时性差**：员工期望打卡后能立即在钉钉中看到考勤状态，而非等待次日批量同步。

### 核心价值

本方案提供一套完整的考勤打卡数据同步解决方案，通过钉钉开放平台的考勤打卡API，实现将企业自有系统中的员工打卡记录自动同步至钉钉考勤应用。

- **打卡数据自动同步**：自有系统打卡后自动上传至钉钉，零人工干预。
- **统一管理入口**：所有考勤数据汇聚至钉钉，HR可在一个平台完成考勤统计与分析。
- **低成本快速接入**：仅需调用2个核心API即可完成对接，开发成本低。

### 适用场景

本方案适用于以下典型业务场景：

- **自有考勤系统集成**：将企业自研的考勤系统或第三方考勤设备（门禁刷卡、指纹机、人脸识别机等）与钉钉考勤模块打通，实现打卡数据自动同步。
- **多设备数据统一汇聚**：企业部署多种考勤设备分布在不同办公地点，需将所有设备的打卡记录统一汇聚至钉钉进行集中管理。
- **实时考勤状态展示**：员工期望打卡后立即在钉钉中看到考勤状态，而非等待次日批量同步。
- **HR跨系统核对消除**：避免HR在自有考勤系统和钉钉之间手动核对数据，提升考勤统计效率。

## 典型业务场景

### 场景一：自有考勤系统打卡数据同步

#### 痛点分析

传统模式下，员工在企业自有考勤系统（如门禁刷卡、指纹打卡）完成打卡后，如需在钉钉中体现考勤状态，必须手动在钉钉中进行补卡操作。对于日均打卡数千次的企业，HR每天需处理大量补卡申请，耗时耗力且容易出错。

#### 价值验证

- **自动化流程**

  ![自有考勤系统打卡数据同步流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5301699871/p1103147.png)
- **关键优势**

  - **消除重复操作**：员工在自有考勤系统完成打卡后，数据通过API自动同步至钉钉考勤模块，无需手动补卡或二次录入，彻底消除重复操作。
  - **减少人工审核**：打卡记录实时同步，HR无需逐条核对补卡申请，大幅减少人工审核工作量，节省时间成本。
  - **提升数据准确性**：系统自动同步避免了人为干预和手工录入误差，确保考勤数据真实、准确、可追溯。
  - **改善用户体验**：员工打卡状态实时可见，无需担心漏打卡或忘记补卡，考勤体验更高效便捷。

### 场景二：多考勤设备数据统一汇聚

#### 痛点分析

大型企业通常部署多种考勤设备（指纹机、人脸识别、GPS定位等），分布在不同办公地点。各设备产生的打卡数据分散存储，HR需要登录多个系统导出Excel再手动合并，效率极低且容易遗漏数据。

#### 价值验证

- **自动化流程**

  ![多考勤设备数据统一汇聚流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5301699871/p1103148.png)
- **关键优势**

  - **多源数据统一**：整合指纹机、人脸识别、GPS定位等多种考勤设备的打卡数据，统一标准格式并集中汇聚至钉钉，消除数据孤岛。
  - **一站式管理**：HR可在钉钉平台实时查看所有员工的考勤记录，无需登录多个系统导出Excel再手动合并，管理更便捷高效。
  - **提升统计效率**：系统自动完成数据汇聚与报表生成，大幅缩短考勤统计周期，节省宝贵时间。
  - **减少人工操作**：自动化流程替代手动导出、清洗、合并等重复劳动，降低人工成本，同时减少人为错误风险。

## 实施指南

### 技术架构

本方案基于钉钉开放平台的考勤相关OpenAPI构建，核心技术组件包括：

- **身份鉴权层**：通过 `Client ID` / `Client Secret` 获取 `access_token`，确保接口调用安全性。
- **权限管理层**：申请通讯录和考勤相关接口权限。
- **用户标识获取层**：调用通讯录服务端API获取部门用户详情，获取企业员工在钉钉组织架构中的userId值信息。
- **打卡数据上传层**：调用考勤服务端API上传打卡记录，将自有系统的打卡日期、时间等信息上传到钉钉考勤应用。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限，并申请以下接口权限：

  - `qyapi_get_department_member`（通讯录部门成员读权限）
  - `Pro.AttendanceRecord.Write`（考勤打卡记录写权限）
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：[添加接口调用权限](0003-add-api-permission.md)。查找“通讯录”、“考勤”，申请对应接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用通讯录、考勤相关API：

1. 调用通讯录服务端API-[获取部门用户详情](0061-queries-the-complete-information-of-a-department-user.md)接口，获取企业员工在钉钉组织架构中的userId值信息。
2. 调用考勤服务端API-[上传打卡记录](0199-upload-punch-records.md)接口，将企业自有系统的员工考勤打卡日期、时间等信息上传到钉钉考勤应用。实现同步考勤。

## **实施步骤**

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

   - `qyapi_get_department_member`（通讯录部门成员读权限）— 用于获取部门用户详情，获取userId。
   - `Pro.AttendanceRecord.Write`（考勤打卡记录写权限）— 用于上传打卡记录到钉钉考勤应用。

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

### 步骤四：核心API调用

1. **获取部门用户详情**：调用通讯录服务端API-[获取部门用户详情](0061-queries-the-complete-information-of-a-department-user.md)接口，获取企业员工在钉钉组织架构中的userId值信息。

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
       OapiV2UserListResponse rsp = client.execute(req, "access_token");
       System.out.println(rsp.getBody());
   }
   ```
2. **上传打卡记录**：调用考勤服务端API-[上传打卡记录](0199-upload-punch-records.md)接口，将企业自有系统的员工考勤打卡日期、时间等信息上传到钉钉考勤应用。实现同步考勤。

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

**实施完成检查清单**：

- 应用凭证获取成功（Client ID / Client Secret）。
- 通讯录和考勤权限申请成功。
- access\_token获取成功。
- 获取部门用户详情接口调用成功，返回正确的userId列表。
- 上传打卡记录接口调用成功，钉钉考勤应用显示同步的打卡数据。

## 常见问题（FAQ）

- **Q1：上传打卡记录时必填哪些参数？**

  A：必填参数包括：

  - `userid`：员工在钉钉组织架构中的userId
  - `userCheckTime`：打卡时间（Unix时间戳，毫秒级）
  - `deviceId`：考勤设备ID
  - `deviceName`：考勤设备名称

    可选参数包括 `photoUrl`（打卡备注图片地址，必须是公网可访问的地址）。
- **Q2：打卡数据同步失败的常见原因有哪些？**

  A：常见原因包括：

  - userId不正确（必须是钉钉组织架构中存在的员工ID）
  - userCheckTime格式错误或为未来时间
  - access\_token无效或已过期
  - 应用未申请考勤相关权限
  - 网络请求超时或服务器异常
- **Q3：多员工打卡数据批量上传的最佳实践是什么？**

  A：当前接口支持单次上传一条打卡记录。如需批量上传，建议在业务层循环调用该接口，注意控制调用频率避免触发限流。也可联系钉钉技术支持咨询批量上传方案。
