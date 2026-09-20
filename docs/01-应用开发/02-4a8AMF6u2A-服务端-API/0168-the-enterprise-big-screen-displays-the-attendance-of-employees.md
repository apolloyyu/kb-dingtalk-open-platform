---
title: "企业大屏展示员工考勤"
source_url: "https://open.dingtalk.com/document/development/the-enterprise-big-screen-displays-the-attendance-of-employees"
namespace: "development"
slug: "the-enterprise-big-screen-displays-the-attendance-of-employees"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 使用教程 > 企业大屏展示员工考勤"
doc_id: "KyPWUiGk6g"
updated_at: "2026-09-20 09:32:32"
---

> Source: https://open.dingtalk.com/document/development/the-enterprise-big-screen-displays-the-attendance-of-employees
> Path: 应用开发 / 服务端 API / 考勤 > 使用教程 > 企业大屏展示员工考勤
> Updated: 2026-09-20 09:32:32

# 企业大屏展示员工考勤

通过钉钉Stream推送机制与考勤API，实现员工打卡数据实时采集与智能分析，为企业大屏、BI系统提供标准化数据接口，解决传统人工导出滞后、系统集成困难、状态判定复杂等核心痛点。

## 概述

本方案提供一套完整的企业大屏展示员工考勤解决方案，通过钉钉开放平台的Stream推送机制与考勤API，实现实时数据采集、智能状态判定与标准化输出。

### 方案背景

企业在日常运营中，需要实时掌握员工的到岗情况，尤其是对于制造车间、客服中心、零售门店等场景，管理层需要通过大屏直观展示当前在岗人数、迟到人员、缺勤情况等关键指标。然而，钉钉原生考勤数据分散在后台管理系统中，无法直接对接企业自建的大屏可视化系统，导致：

- **数据获取滞后**：HR需手动导出考勤报表，无法实现秒级实时更新。
- **系统集成困难**：缺乏标准化的API接口，难以将考勤数据嵌入企业自有BI或大屏系统。
- **状态判断复杂**：仅凭打卡时间无法自动判定"正常/迟到/缺勤"，需人工比对排班规则。
- **监控盲区**：无法对异常打卡（如异地打卡、代打卡）进行实时告警。

### 核心价值

企业通过本方案可以实现考勤数据的实时采集与智能分析，将原本依赖人工导出的离线数据转化为API驱动的实时流，显著提升管理决策效率与数据透明度。

- **实时数据采集**：通过Stream推送机制，员工打卡后毫秒级回调至企业服务器，实现零延迟数据同步。
- **智能状态判定**：自动比对打卡时间与排班规则，精准识别"正常/迟到/早退/缺勤"等状态。
- **标准化API输出**：提供统一的RESTful接口，便于与企业大屏、BI系统、OA看板无缝集成。
- **全量历史追溯**：支持批量查询历史考勤记录，满足月度统计、趋势分析等深度需求。

### 适用场景

本方案适用于以下典型业务场景：

- **制造车间大屏**：实时显示各产线在岗人数、缺勤率、迟到预警，辅助生产调度。
- **客服中心监控**：监控坐席到岗情况，确保服务人力充足，及时调配资源。
- **零售门店管理**：多门店统一监控员工打卡状态，优化排班与客流匹配。
- **总部指挥中心**：集团级考勤数据汇总，支持跨区域对比与异常告警。

## 典型业务场景

### 场景一：制造车间实时在岗监控

#### 痛点分析

传统模式下，车间主任需每2小时人工统计一次各产线在岗人数，耗时30分钟且数据滞后。当发生突发缺勤时，无法及时调整生产计划，导致产能损失。

#### 价值验证

- **自动化流程**

  ![制造车间实时在岗监控流程_20260918_092529](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2597689871/p1102974.png)
- **关键优势**

  - **秒级更新**：员工打卡后1秒内大屏数据刷新，管理层实时掌握人力分布。
  - **自动告警**：缺勤率超过阈值（如10%）时自动触发短信/钉钉通知，快速响应。
  - **历史对比**：支持同比/环比分析，识别季节性缺勤规律，优化排班策略。
  - **多维度筛选**：按产线、班组、工种灵活筛选，精准定位问题区域。

### 场景二：客服中心人力调度优化

#### 痛点分析

客服主管无法实时了解各时段实际到岗人数，常出现高峰期人手不足、低峰期人力冗余的情况，影响客户满意度与运营成本。

#### 价值验证

- **自动化流程**

  ![客服中心人力调度优化流程_20260918_092638](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2597689871/p1102975.png)
- **关键优势**

  - **热力图展示**：以时间轴+坐席数为维度，直观呈现人力分布热点。
  - **预测性调度**：基于历史数据预测未来2小时人力需求，提前调整排班。
  - **异常检测**：自动识别连续迟到、频繁早退等异常行为，生成重点关注名单。
  - **绩效关联**：将考勤数据与接通率、满意度等KPI关联，量化人力投入产出比。

## 实施指南

### 技术架构

本方案基于钉钉开放平台的服务端API与Stream推送机制构建，核心技术组件包括：

- **身份鉴权层**：通过 `Client ID` / `Client Secret` 获取 `access_token`，确保接口调用安全性。
- **实时数据接入层**：配置Stream推送订阅考勤打卡事件，实现毫秒级回调至企业服务器。
- **智能判定引擎**：本地算法比对打卡时间与排班规则，自动识别"正常/迟到/严重迟到/缺勤"状态。
- **数据存储与缓存**：考勤组排班规则每小时全量同步，打卡记录实时写入数据库并缓存。
- **标准化API输出层**：提供RESTful接口供企业大屏、BI系统调用，支持多维度筛选与聚合查询。

数据流向说明：员工在钉钉APP打卡 → Stream推送实时回调 → 企业服务器接收并判定状态 → 写入数据库并缓存 → 大屏API接口返回数据。

### 前置条件

在实施方案前，需满足以下条件：

- **应用准备**：完成企业内部应用的创建与配置，参考[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)。
- **权限要求**：拥有钉钉企业管理员或子管理员权限。
- **开发环境**：已安装Java开发环境(JDK1.6及以上)及Maven构建工具。
- **SDK准备**：下载钉钉服务端SDK，详情参见[服务端SDK下载](0002-download-the-server-side-sdk.md)，支持Java/Python/Go等多语言。
- **服务器要求**：企业拥有可公网访问的服务器，用于接收Stream推送回调。
- **大屏系统**：大屏展示系统支持HTTP API数据接入（如ECharts、DataV、Tableau等）。

### 代码实现

步骤一：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤二：本示例无需申请接口权限。

步骤三：获取应用访问凭证[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤四：相关调用流程：

1. 调用考勤服务端API-[批量获取考勤组详情](0181-batch-obtain-attendance-group-details.md)接口，获取企业考勤组内的排班上下班时间。
2. 获取员工考勤打卡情况，需要注册企业考勤事件回调，参考文档[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)，并订阅[考勤事件](../04-LFcRvVD08N-事件订阅/0129-employee-clock-in-event.md)。
3. 实现智能状态判定逻辑：根据实时推送的打卡信息（userId、groupId、checkTime）与缓存的考勤组排班时间对比，判定打卡状态（Normal/Late/SeriousLate/Absent）。
4. 提供标准化API接口供大屏系统调用，支持按部门、考勤组、时间段等维度查询实时在岗数据。

## 实施步骤

### **步骤一：****获取应用凭证**

1. 登录[钉钉开发者后台](https://open-dev.dingtalk.com/)。
2. 选择目标应用，进入应用详情页。
3. 单击**基础信息** > **凭证与基础信息**。
4. 记录应用的`Client ID`和`Client Secret`。

   > **[!NOTE]**
   >
   > 请妥善保管 `Client Secret`，不要泄露给第三方。建议将其存储在环境变量或密钥管理系统中，避免硬编码在代码里。

### **步骤二**：获取访问凭证（access\_token）

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

### **步骤三：核心API调用**

1. **批量获取考勤组详情**：调用考勤服务端API-[批量获取考勤组详情](0181-batch-obtain-attendance-group-details.md)接口，获取企业考勤组内的排班上下班时间。

   ```
   public void batchGetAttendanceGroups() throws ApiException {
       DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/attendance/group/detail/batchquery");
       OapiAttendanceGroupDetailBatchqueryRequest req = new OapiAttendanceGroupDetailBatchqueryRequest();
       // 设置请求参数
       OapiAttendanceGroupDetailBatchqueryResponse rsp = client.execute(req, "access_token");
       System.out.println(rsp.getBody());
   }
   ```
2. **配置Stream推送并订阅考勤事件**：参考[配置 Stream 推送（推荐）](../04-LFcRvVD08N-事件订阅/0003-configure-stream-push.md#151be9e66238j)文档，注册企业考勤事件回调，并订阅[考勤事件](../04-LFcRvVD08N-事件订阅/0129-employee-clock-in-event.md)。

   **回调数据结构**：

   ```
   {
     "DataList":[
       {
         //打卡员工的userId值
         "userId":"0126xxxx",
         //员工执行打卡时间，单位毫秒
         "checkTime":1570791880000,
         //执行打卡时的地址
         "address":"中国科学院工程热物理研究所（浙江海外高层次人才创新园7幢东）",
         //企业corpId
         "corpId":"dingxxxx",
         //该员工所在的考勤组ID
         "groupId":"4C63xxxx",
         //打卡地址对应的纬度
         "latitude":30.285230848524307,
         //打卡地址对应的经度
         "longitude":120.01713514539931,
         //打卡业务ID
         "bizId":"FF62xxxx",
         //定位方法
         "locationMethod":"MAP",
       }
     ],
     "EventType":"attendance_check_record"
   }
   ```
3. **智能状态判定逻辑**：

   **核心算法**：根据实时推送的打卡信息（userId、groupId、checkTime）与缓存的考勤组排班时间对比，判定打卡状态。

   ```
   public String determineAttendanceStatus(String userId, String groupId, String checkTime) {
       // 1. 从缓存中获取该考勤组的排班规则
       ScheduleRule rule = cache.getScheduleRule(groupId);
       
       // 2. 解析打卡时间
       LocalDateTime punchTime = LocalDateTime.parse(checkTime, formatter);
       
       // 3. 对比排班时间
       if (punchTime.isBefore(rule.getStartTime().plusMinutes(rule.getLateThreshold()))) {
           return "Normal";  // 正常打卡
       } else if (punchTime.isBefore(rule.getStartTime().plusMinutes(rule.getSeriousLateThreshold()))) {
           return "Late";    // 迟到
       } else {
           return "SeriousLate";  // 严重迟到
       }
   }
   ```

   **状态映射表**：

   | **判定条件** | **返回状态** | **大屏显示颜色** |
   | --- | --- | --- |
   | 打卡时间 ≤ 上班时间点 + 迟到阈值 | Normal（正常） | 🟢 绿色 |
   | 上班时间点 + 迟到阈值 < 打卡时间 ≤ 严重迟到阈值 | Late（迟到） | 🟡 黄色 |
   | 打卡时间 > 严重迟到阈值 | SeriousLate（严重迟到） | 🔴 红色 |

**实施完成检查清单**：

- ✅ Stream推送配置成功，能接收到打卡回调。
- ✅ 考勤组排班规则缓存正常，每小时自动刷新。
- ✅ 状态判定逻辑测试通过，准确率100%。
- ✅ 大屏API接口响应时间<200ms。
- ✅ 异常打卡（如异地打卡）能正确标记并告警。

## **常见问题（FAQ）**

- **Q1：Stream推送和轮询拉取有什么区别？**

  A：两者数据获取方式完全不同：

  - **轮询拉取**：企业服务器定时调用API查询打卡记录，存在延迟（通常5-15分钟），且频繁调用易触发限流。
  - **Stream推送**：钉钉在员工打卡后主动推送至企业指定URL，延迟<1秒，无需主动查询，适合实时大屏场景。

  **核心差异**：Stream推送是事件驱动模式，按需推送；轮询是定时查询模式，无论有无新数据都需调用。推荐优先使用Stream推送。
- **Q2：如何判定员工是"迟到"还是"缺勤"？**

  A：判定逻辑如下：

  - **迟到**：员工有打卡记录，但打卡时间晚于排班规定的上班时间+迟到阈值（通常10-30分钟，可在考勤组配置中设置）。
  - **缺勤**：截至当前时间（如下午3点），员工当日无任何打卡记录，且排班规则要求该员工今日应出勤。

  **注意**：需结合排班规则判断，若员工今日排休，则即使无打卡也不算缺勤。
- **Q3：如何处理异地打卡或代打卡异常？**

  A：钉钉考勤事件回调中包含 `LocationResult` 字段，标识打卡地点是否正常：

  - `Normal`：打卡地点在考勤组允许的范围内。
  - `Outside`：打卡地点超出允许范围，疑似异地打卡。

  **处理策略**：

  - 大屏中标记 `LocationResult=Abnormal` 的记录为橙色警告。
  - 生成异常打卡日报，发送至HR管理员审核。
  - 结合人脸识别、WiFi指纹等多因子验证，降低代打卡风险。
- **Q4：大屏数据刷新频率多少合适？**

  A：取决于业务场景：

  - **制造车间/客服中心**：建议1-5秒刷新一次，确保实时性。
  - **零售门店**：建议30秒-1分钟刷新一次，平衡性能与实时性。
  - **总部指挥中心**：建议5-10分钟刷新一次，侧重趋势分析而非秒级监控。

  **性能优化**：采用增量更新策略，仅推送变化的数据（如新打卡记录），而非全量刷新，可降低90%以上的网络开销。
