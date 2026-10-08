---
title: "签到数据自动采集：从钉钉签到到业务系统实时同步"
source_url: "https://open.dingtalk.com/document/development/obtain-check-in-information"
namespace: "development"
slug: "obtain-check-in-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "签到 > 使用教程 > 签到数据自动采集：从钉钉签到到业务系统实时同步"
doc_id: "ApvXyICPxJ"
updated_at: "2026-09-23 12:04:38"
---

> Source: https://open.dingtalk.com/document/development/obtain-check-in-information
> Path: 应用开发 / 服务端 API / 签到 > 使用教程 > 签到数据自动采集：从钉钉签到到业务系统实时同步
> Updated: 2026-09-23 12:04:38

# 签到数据自动采集：从钉钉签到到业务系统实时同步

本文档介绍企业使用自有系统或第三方应用如何通过钉钉开放平台API实现员工签到信息的自动获取，支持将钉钉签到数据实时同步至业务系统进行考勤统计、人员分布分析等场景。

## 概述

本方案提供一套完整的钉钉签到数据采集解决方案，通过调用钉钉开放平台的签到相关API，实现对企业员工签到记录的批量查询及分页获取，支持基于高德地图API进行人员分布图和热力图的可视化展示。

### 方案背景

企业在日常运营中常面临以下痛点：

- **签到数据分散**：员工通过钉钉签到产生的位置、时间、照片等数据无法自动同步至业务系统，需人工导出整理。
- **统计分析困难**：缺乏统一的签到数据视图，难以按部门、时间段、地点等多维度进行统计分析。
- **实时监控缺失**：外勤人员签到情况无法实时掌握，管理者难以及时了解团队工作动态。
- **数据孤岛阻碍决策**：签到数据未与企业通讯录、考勤系统等模块打通，无法基于组织架构自动关联相关人员。

### 核心价值

本方案提供钉钉签到数据采集解决方案，通过调用钉钉开放平台的签到相关API，实现对企业员工签到记录的批量查询、分页获取。

- **签到数据自动采集**：业务系统定时调用API自动获取签到记录，无需人工导出整理，大幅提升数据处理效率。
- **多维度统计分析**：支持按用户、时间段、地点等多维度查询签到数据，形成完整的签到分析视图。
- **实时位置可视化**：结合高德地图API实现人员分布图和热力图展示，直观呈现外勤人员工作轨迹。
- **组织架构联动**：基于钉钉通讯录自动匹配签到人员所属部门，支持按组织架构层级进行数据统计。

### 适用场景

本方案适用于以下典型业务场景：

- **外勤人员签到监控**：销售、巡检等外勤人员的签到数据自动同步至CRM或工单系统，实时掌握工作动态。
- **考勤数据统计分析**：HR系统定期获取员工签到记录进行考勤统计，自动生成月度考勤报表。
- **活动签到管理**：会议、培训等活动的签到数据自动采集并生成参与人员名单及签到率统计。
- **人员分布热力图**：基于签到位置数据生成热力图，辅助管理层优化人员配置和业务布局。

## 典型业务场景

### 场景一：外勤销售签到数据自动同步至CRM系统

#### 痛点分析

销售团队外出拜访客户时使用钉钉签到，但签到数据仅存在于钉钉系统中：

- CRM系统无法自动获取销售人员的拜访记录，需手动录入客户拜访信息
- 管理者无法实时查看团队成员的工作轨迹和拜访进度
- 签到照片、地址等关键信息无法与客户档案关联，难以验证拜访真实性
- 缺乏统一的签到数据看板，难以评估外勤工作效率

#### 价值验证

- **自动化流程**

  ![外勤销售签到同步流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8726310971/p1103407.png)
- **关键优势**

  - **签到数据自动回写**：销售人员完成签到后1分钟内自动同步至CRM系统，无需手动录入拜访记录。
  - **拜访轨迹实时可视**：基于签到位置和照片生成外勤工作轨迹图，管理者实时掌握团队动态。
  - **客户档案自动关联**：签到地址与客户档案智能匹配，自动更新客户拜访历史和跟进状态。

### 场景二：HR系统月度考勤统计自动化

#### 痛点分析

人力资源部门每月需手工统计员工考勤数据：

- 需从钉钉后台逐个导出签到记录，耗时且易遗漏
- 签到时间与考勤规则比对困难，异常考勤识别效率低
- 跨部门考勤统计需多次筛选汇总，工作量巨大
- 缺乏历史签到数据趋势分析，难以发现考勤异常模式

#### 价值验证

- **自动化流程**

  ![HR考勤统计自动化流程图](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8726310971/p1103409.png)
- **关键优势**

  - **考勤数据自动采集**：HR系统每日凌晨自动拉取前一日签到记录，无需人工导出整理。
  - **异常考勤智能识别**：基于签到时间和地点自动标记迟到、早退、缺勤等异常情况。
  - **月度报表一键生成**：自动汇总全月签到数据生成考勤报表，支持按部门、个人多维度查看。

## 实施指南

### 技术架构

- **接口调用层**：调用签到服务端API实现签到记录的查询与获取操作。
- **用户标识获取层**：调用通讯录服务端API获取部门用户详情，获取企业员工在钉钉组织架构中的userId值信息。
- **签到数据同步层**：调用签到服务端API批量获取员工签到记录并同步至业务系统。
- **数据分析层**：对签到数据进行多维度统计分析，支持按时间、地点、人员等维度聚合。
- **可视化展示层**：结合高德地图API实现签到位置的热力图和分布图展示。
- **错误处理层**：完善的错误码体系，便于快速定位和解决问题。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：默认开通，无需额外申请权限。
- **开发环境**：已安装Java开发环境（JDK1.6及以上）及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：申请接口权限，申请签到相关接口的权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：调用服务端签到相关API。

1. 参会人员使用钉钉-签到应用进行签到。
2. 调用服务端API-[获取用户签到记录](0292-obtain-the-check-in-records-of-multiple-users.md)接口，获取员工的签到详情信息。

## 实施步骤

### **步骤一：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### 步骤二：获取访问凭证（accessToken）

根据步骤一中 的 Client ID 和 Client Secret，获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。

```
public String getAccessToken() {
    com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
    config.protocol = "https";
    config.regionId = "central";
    try {
        com.aliyun.dingtalkoauth2_1_0.Client client = new com.aliyun.dingtalkoauth2_1_0.Client(config);
        GetAccessTokenRequest getAccessTokenRequest = new GetAccessTokenRequest()
                .setAppKey("dingeqqpkv3xxxxxx")
                .setAppSecret("GT-lsu-taDAxxxsTsxxxx");
        GetAccessTokenResponse response = client.getAccessToken(getAccessTokenRequest);
        System.out.println(response.getBody());
        return response.getBody().getAccessToken();
    } catch (Exception e) {
        throw new RuntimeException(e);
    }
}
```

**最佳实践**：

- **缓存策略**：`accessToken`有效期为2小时，建议在内存或Redis中缓存，过期前5分钟主动刷新。
- **并发控制**：避免多个线程同时刷新token导致冲突，可使用分布式锁机制。
- **异常重试**：网络波动时自动重试，最多3次，间隔递增（1s → 2s → 4s）。

### **步骤三：核心API调用**

参与人员，可以使用钉钉签到进行签到。操作路径：打开钉钉客户端端 > 打开工作台 > 点击并打开签到。

![iShot2022-02-23 18](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9879592871/p408438.png)

#### **场景一：获取用户签到记录**

根据员工的userId，调用服务端API-[获取用户签到记录](0292-obtain-the-check-in-records-of-multiple-users.md)接口，获取员工签到的详情信息。企业可以调用本接口获取指定人员的签到记录进行统计分析。

```
public void checkinRecord() throws ApiException {
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/checkin/record/get");
  OapiCheckinRecordGetRequest req = new OapiCheckinRecordGetRequest();
  req.setUseridList("manager7675");
  req.setStartTime(1646064000000L);
  req.setEndTime(1646668800000L);
  req.setCursor(0L);
  req.setSize(100L);
  OapiCheckinRecordGetResponse rsp = client.execute(req, "accessToken");
  System.out.println(rsp.getBody());
}
```

**参数说明**：

- `userid_list`：**重点参数**，需要查询的用户列表，最大列表长度为10。
- `start_time`：**重点参数**，开始时间，Unix时间戳，单位毫秒。
- `end_time`：**重点参数**，截止时间，Unix时间戳，单位毫秒。

  **注意**：如果是取1个人的数据，时间范围最大10天，如果是取多个人的数据，时间范围最大1天
- `cursor`：分页查询的游标，最开始可以传0。
- `size`：分页查询的每页大小，最大100。

**响应字段说明**：

- `next_cursor`：下次查询的游标，为null代表没有更多的数据。
- `page_list`：签到信息列表，包含以下字段：

  - `checkin_time`：签到时间，单位毫秒。
  - `image_list`：签到照片URL列表（如果签到没有上传图片，不返回该字段）。
  - `detail_place`：签到详细地址。
  - `remark`：签到备注。
  - `userid`：签到用户userId。
  - `place`：签到地址。
  - `longitude`：签到位置经度。
  - `latitude`：签到位置纬度。
  - `visit_user`：签到的拜访对象，可以为外部联系人的userId或者用户自己输入的名字。

#### **场景二：获取部门用户签到记录**

根据部门的department\_id，调用服务端API-[获取部门用户签到记录](0293-get-check-in-data.md)接口，获取部门员工签到的详情信息。企业可以调用本接口获取指定部门的签到记录进行统计分析，也可以基于高德地图API接口开发人员分布图和热力图。

```
public void checkinRecord() throws ApiException {
  DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/checkin/record");
  OapiCheckinRecordRequest req = new OapiCheckinRecordRequest();
  req.setDepartmentId("1");
  req.setEndTime(1520956800000L);
  req.setStartTime(1520956800000L);
  req.setOffset(0L);
  req.setSize(100L);
  req.setOrder("asc");
  req.setHttpMethod("GET");
  OapiCheckinRecordResponse rsp = client.execute(req, access_token);
  System.out.println(rsp.getBody());
}
```

**参数说明**：

- `department_id`：**重点参数**，需要查询的部门ID，1表示根部门。
- `start_time`：**重点参数**，开始时间，Unix时间戳，单位毫秒。
- `end_time`：**重点参数**，截止时间，Unix时间戳，单位毫秒。

  **注意**：如果是取1个人的数据，时间范围最大10天，如果是取多个人的数据，时间范围最大1天
- `offset`：支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，从0开始。
- `cursor`：分页查询的游标，最开始可以传0。
- `size`：分页查询的每页大小，最大100。

**响应字段说明**：

- `data`：签到信息列表，包含以下字段：

  - `name`：员工姓名。
  - `userid`：员工userId，不可修改。
  - `avatar`：头像URL。
  - `timestamp`：签到时间，不可修改。
  - `place`：签到地址。
  - `detailPlace`：签到详细地址。
  - `remark`：签到备注。
  - `imageList`：签到照片URL列表（如果签到没有上传图片，不返回该字段）。
  - `latitude`：签到位置纬度。
  - `longitude`：签到位置经度。

**实施完成检查清单**：

- ✅ 应用凭证获取成功（Client ID / Client Secret）。
- ✅ access\_token获取成功。
- ✅ 获取用户签到记录接口调用成功，返回正确的签到详情。
- ✅ 分页查询正常工作，能获取全部签到数据。
- ✅ 签到数据已成功同步至业务系统。

## 常见问题（FAQ）

- **Q1：调用签到相关API是否需要申请特定权限？**

  A：默认开通，无需额外申请权限。只要完成企业内部应用的创建与配置即可调用。
- **Q2：record/get接口各参数的含义和使用说明？**

  A：主要参数包括：

  - `userid_list`：需要查询的用户列表，最多10个用户ID。
  - `start_time` / `end_time`：查询的时间范围（Unix时间戳，毫秒）。单人查询最多10天，多人查询最多1天。
  - `cursor` / `size`：分页参数，cursor初始值为0，size最大为100。
- **Q3：查询签到记录的最佳实践是什么？**

  A：建议采用以下策略：

  - **分页查询**：使用cursor和size参数进行分页，避免一次性加载大量数据。
  - **时间范围控制**：单人查询控制在10天内，多人查询控制在1天内，超出范围会报错。
  - **性能优化**：批量查询时尽量缩小时间范围，减少单次请求的数据量。
  - **定时任务**：设置定时任务每日凌晨拉取前一日数据，避免频繁调用接口。
  - **错误重试**：对于网络超时等临时错误，实现指数退避重试机制。
