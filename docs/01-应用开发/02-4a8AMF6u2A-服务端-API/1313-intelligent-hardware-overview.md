---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/intelligent-hardware-overview"
namespace: "development"
slug: "intelligent-hardware-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 智能硬件 > 概述"
doc_id: "9ZkRKNS5XF"
updated_at: "2026-07-20 09:25:45"
---

> Source: https://open.dingtalk.com/document/development/intelligent-hardware-overview
> Path: 应用开发 / 服务端 API / 更多开放 > 智能硬件 > 概述
> Updated: 2026-07-20 09:25:45

# 概述

本文介绍了什么是智能硬件，智能硬件接口能力等。

## 什么是智能硬件

智能硬件是钉钉旗下智能办公硬件品牌，打造了智能考勤、智能前台、智能门禁、智能网络中心、智能会议室等，满足不同工作或学习场景需求，助你轻松实现智能移动办公。更多使用详情可参考[钉钉使用手册-智能硬件](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Mk5evdR04jBV5PvqAnbyWQL3x2OlParn)。

## 开放概览

智能硬件提供了丰富的接口开放能力，开发者通过API接口可以实现智能硬件和企业业务系统打通。

### **开放接口列表**

#### **设备管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [绑定设备](1314-establishing-a-binding-relationship-between-intelligent-hardware-and-cloud.md) | 用于和组织建立绑定关系。 | 新版 |
| [解绑设备](1315-unbind-a-smart-hardware-device.md) | 解除智能硬件设备和企业之前的绑定关系。 | 新版 |
| [修改设备昵称](1316-intelligent-hardware-device-nickname-modification.md) | 修改设备昵称。 | 新版 |
| [查询设备列表](1317-intelligent-hardware-list-query.md) | 分页查询企业下的智能设备列表。 | 新版 |
| [查询设备详情](1318-intelligent-hardware-device-query.md) | 查询企业下的智能硬件设备详情。 | 新版 |
| [根据设备ID查询设备](1319-the-smart-hardware-can-query-details-based-on-the-device.md) | 根据设备ID查询企业下某个智能硬件设备。 | 新版 |

#### AIoT 平台

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询指定设备的详情](1320-api-getdevicedetail.md) | 查询指定设备的详情。 | 新版 |
| [设置指定设备的属性](1321-api-setdeviceproperties.md) | 更新指定设备的属性。 | 新版 |
| [查询设备服务调用结果](1322-api-getserviceinvocation.md) | 查询设备服务调用结果。 | 新版 |
| [确认执行设备固件升级](1323-api-confirmfirmwareupgrade.md) | 确认执行设备固件升级。 | 新版 |
| [检查指定设备的固件升级](1324-api-checkdeviceupdate.md) | 检查指定设备的固件升级。 | 新版 |
| [读取指定设备的属性快照](1325-api-getdeviceproperties.md) | 读取指定设备的属性快照。 | 新版 |
| [调用指定设备的物模型服务](1326-api-invokedeviceservice.md) | 调用指定设备的物模型服务。 | 新版 |

#### DingTalk A1

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询DingTalkA1小助理分析](1327-api-querysmartdeviceaisummary.md) | 查询DingTalkA1小助理分析结果。 | 新版 |
| [创建DingTalkA1小助理分析](1328-api-createsmartdeviceaisummary.md) | 创建DingTalkA1小助理分析。 | 新版 |

### **回调事件列表**

智能硬件支持小助理总结完成、小助理状态变更和AIoT设备上行等回调事件，更多事件可参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

- [DingTalkA1小助理总结完成事件](../04-LFcRvVD08N-事件订阅/0119-events-aone-assistant-summary-change.md)
- [DingTalkA1小助理状态变更](../04-LFcRvVD08N-事件订阅/0120-events-aone-assistant-status-change-1.md)
- [AIoT设备上行事件](../04-LFcRvVD08N-事件订阅/0118-events-aiot-device-uplink-event.md)
