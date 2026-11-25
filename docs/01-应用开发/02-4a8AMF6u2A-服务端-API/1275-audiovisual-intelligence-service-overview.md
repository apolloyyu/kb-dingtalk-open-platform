---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/audiovisual-intelligence-service-overview"
namespace: "development"
slug: "audiovisual-intelligence-service-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > 概述"
doc_id: "kK63kCLgqH"
updated_at: "2026-11-25 18:45:49"
---

> Source: https://open.dingtalk.com/document/development/audiovisual-intelligence-service-overview
> Path: 应用开发 / 服务端 API / 视听智能服务 > 概述
> Updated: 2026-11-25 18:45:49

# 概述

## **什么是视听智能服务**

钉钉视听智能服务平台（PaaS）是钉钉面向企业开发者提供的音视频 AI 能力开放平台。平台将钉钉在语音识别、音频处理等领域沉淀的核心原子能力，以标准化 API 接口的形式对外开放，帮助企业将先进的 AI 技术快速集成到自有业务系统中。

通过本平台，企业无需自建复杂的 AI 模型或部署昂贵的基础设施，只需完成商务签约、购买资源包并创建应用获取调用凭证，即可按实际用量灵活调用钉钉视听智能服务，大幅降低 AI 能力接入的技术门槛和成本投入。

## **功能介绍**

### **服务管理**

- **查看服务**：访问[视听智能服务平台](https://open-dev.dingtalk.com/fe/dvi?hash=%23%2Fmonitor#/monitor)，在服务管理模块查看已上线的服务信息。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6983920871/p1075810.png)
- **查看当前已支持功能**：**离线 ASR 语音识别**
- **能力特点**：高精度离线语音转写解决方案，确保数据隐私安全。
- **计费单位**：最小颗粒度为秒。

### **资源包管理**

- **查看资产清单**：访问[视听智能服务平台](https://open-dev.dingtalk.com/fe/dvi?hash=%23%2Fmonitor#/monitor)，在资源包管理模块查看所有权益资产清单。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6983920871/p1075811.png)
- **核心关注字段**：

  - **资源总量**：购买时该包赋予的总计费额度（如 3600/小时）。
  - **当前剩余量**：实时更新的尚未用完的可用额度。
  - **失效日期**：资源包过期时间，过期则当前资源包无法使用。
- **资源包状态解析：**

  资源包将显示两种状态：

  - **生效中**：资源包在有效期内，且额度未用完，API 调用正常扣费。
  - **已失效**：资源包已过失效日期，或额度已被彻底扣光。
- **扣费优先级规则：**仅从**生效中**的资源包中扣除，**优先消耗有效期较近的资源包。**
- **追踪使用明细**：资源包列表 → 找到目标资源包所在行 → 操作列点击**【使用明细】，**你可以清晰看到该资源包的每笔出账流水：

  - 消耗来自哪个**抵扣应用名称**。
  - 具体的**抵扣时间（**抵扣时间：每次 API 调用**结束**的时间戳**）**
  - **抵扣量**与抵扣前后的额度走势。如果发现某个应用的抵扣量异常激增，可针对性展开排查。

    > **[!NOTE]**
    >
    > **资源包核销的最小颗粒度为秒**

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6983920871/p1075812.png)

### **监控统计**

提供数据看板可视化展现当下的业务调用规模与未来隐患。

- **查看监控统计**：访问[视听智能服务平台](https://open-dev.dingtalk.com/fe/dvi?hash=%23%2Fmonitor#/monitor)，在监控统计模块查看所有权益资产清单。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6983920871/p1075813.png)
- **汇总卡片**：

  - **应用总数**：当前账号下已登记的应用实体总和。
  - **资源包总数**：名下持有的权益包总计，点击"管理"快捷跳转**【资源包管理】**。
- **业务用量折线趋势分析：**在数据卡片下方，支持查询过往用量统计情况。

  - **灵活检索**：支持搜索指定的"应用名称/服务名称"，或选定某一日期段。
  - **图表展示切换**：支持在可视化折线图表与精确数据表格之间切换。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6983920871/p1075814.png)
  - **数据下载**：支持一键导出下载走势表作存档分析。

    ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6983920871/p1075815.png)

## **开放概览**

### **开放接口列表**

#### **通用接口**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询设备属性](1276-api-querydevicestatus.md) | 通过本接口，批量获取指定的智能语音设备（A1或B1）的状态。 | 新版 |
| [批量获取设备详情](1277-api-querydevicedetail.md) | 通过本接口，批量获取指定SN的智能音频设备（A1或B1）详情。 | 新版 |
| [获取音频文件信息](1278-api-getaudiofileinfo.md) | 通过本接口，获取智能音频设备（A1或B1）产生的音频文件信息。 | 新版 |
| [分页查询指定设备的音频文件列表](1279-api-queryaudiofile.md) | 通过本接口，分页查询智能设备（A1或B1）产生的音频文件。 | 新版 |

#### **DingTalk B1**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取客户信息](1281-api-getcustomerinfo.md) | 通过本接口，获取AI销售管理中的单条客户数据。 | 新版 |
| [查询团队列表](1280-api-listteam.md) | 调用本接口，获取AI销售管理中的团队列表信息。 | 新版 |
| [查询单条服务记录](1284-api-getservicerecord.md) | 通过本接口，使用服务记录ID获取AI销售管理中的指定服务记录。 | 新版 |
| [获取服务待办信息](1288-api-listservicetodo.md) | 调用本接口，通过服务记录ID，获取AI销售管理中的服务记录待列表。 | 新版 |
| [获取服务会话总结](1283-api-getservicechatsummary.md) | 调用本接口，通过服务记录ID，获取AI销售管理中的服务会话总结。 | 新版 |
| [获取服务表现数据](1282-api-getservicequalityinspection.md) | 通过本接口，根据服务记录ID，获取AI销售管理中的服务表现数据。 | 新版 |
| [分页查询客户列表](1287-api-listcustomer.md) | 通过本接口，分页获取AI销售管理中的客户数据。 | 新版 |
| [分页查询设备列表](1285-api-listdevice.md) | 调用本接口，分页查询AI销售管理中的设备列表。 | 新版 |
| [更新设备绑定关系](1286-api-updatedevicebinding.md) | 通过本接口，更新AI销售管理中硬件设备与使用人之间的绑定关系。 | 新版 |
| [获取服务对话章节摘要](1289-api-getservicechaptersummary.md) | 通过本接口，获取AI销售管理中的服务记录对话章节摘要。 | 新版 |
| [获取AI销售管理客户洞察信息](1290-api-getcustomerinsight.md) | 通过本接口，获取AI销售管理中的客户洞察信息。 | 新版 |
| [分页获取企业下的服务记录信息](1291-api-listservicerecord.md) | 调用本接口，分页获取企业下的服务记录信息。 | 新版 |

#### **BV 看鉴**

- **看鉴记录**

  | **API** | **API说明** | **API版本** |
  | --- | --- | --- |
  | [查询看鉴记录详情](1292-api-getkanjianrecord.md) | 调用本接口，按记录 ID 查询看鉴 BV 记录详情。 | 新版 |
  | [分页查询看鉴记录列表](1293-api-listkanjianrecords.md) | 调用本接口，分页查询企业下的看鉴 BV 设备录制记录。 | 新版 |
  | [看鉴记录首次绑定主任务](1294-api-bindkanjianrecordtask.md) | 调用本接口，给看鉴 BV 记录首次绑定主任务。 | 新版 |
  | [分页拉取看鉴记录的关键识别结果](1295-api-pagekanjianrecordanalysis.md) | 调用本接口，分页拉取看鉴 BV 记录的关键识别结果。 | 新版 |
  | [分页拉取看鉴记录的过程记录结果](1296-api-pagekanjianrecordprocess.md) | 调用本接口，分页拉取看鉴 BV 记录的过程记录。 | 新版 |
- **看鉴任务**

  | **API** | **API说明** | **API版本** |
  | --- | --- | --- |
  | [创建看鉴任务](1297-api-createkanjiantask.md) | 调用本接口，创建看鉴主任务及子任务。 | 新版 |
  | [删除看鉴任务](1298-api-deletekanjiantask.md) | 调用本接口，删除指定的看鉴主任务，并同时删除其下全部子任务。 | 新版 |
  | [更新看鉴主任务](1299-api-updatekanjiantask.md) | 调用本接口，更新看鉴主任务，只修改传入的非空字段。 | 新版 |
  | [分页查询看鉴任务列表](1300-api-listkanjiantasks.md) | 调用本接口，分页查询企业看鉴主任务列表。 | 新版 |
  | [查询看鉴主任务详情及子任务列表](1301-api-getkanjiantask.md) | 调用本接口，按任务 ID 查询看鉴主任务详情及其子任务列表。 | 新版 |
- **看鉴设备**

  | **API** | **API说明** | **API版本** |
  | --- | --- | --- |
  | [BV 设备开始录制](1302-api-startkanjianrecording.md) | 调用本接口，让企业看鉴 BV 设备开始录制。 | 新版 |
  | [BV 设备结束录制](1303-api-stopkanjianrecording.md) | 调用本接口，按会话 ID 停止看鉴 BV 设备录制。 | 新版 |
  | [分页查询看鉴 BV 设备列表](1304-api-listkanjiandevices.md) | 调用本接口，分页查询企业下的看鉴 BV 设备。 | 新版 |
  | [查询企业看鉴 BV 设备详情](1305-api-getkanjiandevice.md) | 调用本接口，按设备序列号查询企业看鉴 BV 设备详情。 | 新版 |

#### **音频转写服务**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询ASR转写结果](1306-api-getasrtranscription.md) | 调用本接口查询[创建ASR离线转写任务]的转写结果。 | 新版 |
| [创建ASR离线转写任务](1307-api-createasrtranscription.md) | 调用本接口，创建音频离线转写任务。 | 新版 |

### 回调事件列表

视听智能服务支持BV看鉴设备上下线事件、记录状态变更等回调事件：

- [BV看鉴设备上下线事件](../04-LFcRvVD08N-事件订阅/0127-events-kanjian-device-online-changed.md)
- [BV看鉴录制状态变更事件](../04-LFcRvVD08N-事件订阅/0129-events-kanjian-recording-status-changed.md)
- [BV看鉴记录状态变更事件](../04-LFcRvVD08N-事件订阅/0128-events-kanjian-record-status-changed.md)
- [DingTalkB1设备状态变更事件](../04-LFcRvVD08N-事件订阅/0130-events-badge-device-status-change.md)
- [AI销售管理设备使用人变更事件](../04-LFcRvVD08N-事件订阅/0131-events-dvi-device-owner-change.md)
- [智能工牌自定义AI分析项完成事件](../04-LFcRvVD08N-事件订阅/0132-events-dvi-custom-ai-analysis-completed.md)

## **使用教程**

### **前提条件**

- 已与钉钉商务签约并完成资源包付款（当前不支持线上购买）。
- 拥有钉钉企业管理员或开发者权限，可参考[获取开发者权限](../01-XOnnmGCTbn-开发指南/0006-get-developer-permissions.md)。
- 提前获取[企业 CorpId](../01-XOnnmGCTbn-开发指南/0001-basic-concepts-beta.md#91c2ae57b23p9)（在钉钉开发者平台右侧面板可查看）。
- 已经完成[应用创建与配置](../01-XOnnmGCTbn-开发指南/0007-create-application.md)的流程。

### **流程简介**

步骤一：购买资源包。

> **[!NOTE]**
>
> **现不支持平台线上购买，请对接商务进行购买。**

步骤二：获取应用凭证信息，获取应用 Client ID 和 Client Secret。

步骤三：申请接口权限，申请视听智能服务`Dvi.Audio.Analysis.Read`权限点，如何申请请参考[添加接口调用权限](0003-add-api-permission.md)。

步骤四：获取应用访问凭证[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)。调用接口时，通过accessToken鉴权调用者身份。

步骤五：调用离线 ASR 识别服务，消耗对应的资源包额度，进入**【开放能力】-【视听智能服务】**进行查看与管理。

## **名词解释**

### **服务 (Service)**

平台提供的能力

- 一个独立的API接口称为一个服务如：离线 ASR 识别；
- 一个服务可根据实际情况调整具体的技术参数设置，如ASR的通道等、热词表；
- 同一个服务不同技术参数下是否要拆分为多个单独的服务，需要看是否有独立的商业价值。

### **应用 (Application)**

调用服务时的身份入口和容器

- 多个服务封装成一个应用，一个应用有唯一的AK/SK；
- 同一个服务可以封装到不用的应用中；
- 一个应用可以设置调用层面的参数，比如，限流、IP白名单等。

### **资源包 (Resource)**

购买的使用额度

- 服务的权益封装包包含数量和时间信息；
- 服务的权益封装包，一个服务可以有多个资源包；
- 一个资源包仅封装一个服务。

> **[!NOTE]**
>
> 三者流转关系**：购买资源包 → 创建应用 → 用应用凭证调用服务 → 消耗资源包额度**
