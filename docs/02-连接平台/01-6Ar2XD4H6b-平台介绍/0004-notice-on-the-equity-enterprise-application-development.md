---
title: "关于企业应用开发和自动化在钉钉PaaS 底座中的权益调整的通告"
source_url: "https://open.dingtalk.com/document/connection/notice-on-the-equity-enterprise-application-development"
namespace: "connection"
slug: "notice-on-the-equity-enterprise-application-development"
group: "连接平台"
tab: "平台介绍"
breadcrumb: "平台公告 > 关于企业应用开发和自动化在钉钉PaaS 底座中的权益调整的通告"
doc_id: "QJcfTgu9j0"
updated_at: "2026-01-22 21:25:56"
---

> Source: https://open.dingtalk.com/document/connection/notice-on-the-equity-enterprise-application-development
> Path: 连接平台 / 平台介绍 / 平台公告 > 关于企业应用开发和自动化在钉钉PaaS 底座中的权益调整的通告
> Updated: 2026-01-22 21:25:56

# 关于企业应用开发和自动化在钉钉PaaS 底座中的权益调整的通告

尊敬的钉钉用户：

您好！钉钉将于 **2025年10月31日起** 推出数字资产长期保存计划，并调整部分版本权益。此举旨在助力企业有效存储数字资产，实现数据集中沉淀、资源灵活配置，并为未来的智能化做好准备。

调整包含：

- **数据统一存储至企业空间**，实现数字资产**集中沉淀、长期可用、权限可控**
- **钉钉部分版本权益调整**，促进企业资源灵活配置

## **（一）钉钉底座的 PaaS 权益变更说明**

为响应企业关于资源灵活调配诉求，以便更好积累、沉淀与管理数字资产，自2025年11月19日起，钉钉将对各版本部分权益进行如下调整：

#### **一、企业应用开发付费 API 、Webhook&Stream 和连接流节点执行量的每个月的权益额度调整**

| **权益项** | | **钉钉标准版**  **未年检认证** | **钉钉标准版**  **已年检认证** | **钉钉专业版**  **9800元/年/套** |
| --- | --- | --- | --- | --- |
| 企业存储 | | 30GB | 100GB | 1TB |
| 音视频 | 会议资源 | 3 个  40分钟100人标清会议室 | 3 个  60分钟100人标清会议室 | 3 个  60分钟100人标清会议室  + 2 个  24小时100人高清会议室 |
| 直播资源 | 1 个  40分钟300人标清直播间 | 1 个  60分钟300人标清直播间 | 1 个  60分钟300人标清直播间  + 1 个  24小时500人高清直播间 |
| **应用开发** | **付费 API 调用量** | **5000 次/自然月** | **5000 次/自然月** | **20 万次/自然月** |
| **Webhook & Stream** | **3000 次/自然月** | **3000 次/自然月** | **5 万次/自然月** |
| **连接流节点执行量** | **500 次/自然月** | **500 次/自然月** | **1 万次/自然月** |

- 已购买钉钉专业版/钉钉专属版且合同处于有效期内的客户，仍享有原合同权益，不受本次调整影响。
- 附：[企业数字资产存储及版本权益调整公告](https://alidocs.dingtalk.com/i/p/WVJqzqJw73dDXYEKJqzqJxpRNn9QKXYE?dontjump=true)

#### **二、以下部分企业付费增值的 OpenAPI 权益调整**

原部分增值 OpenAPI，需要企业升级钉钉专业版、钉钉专属版或者购买企业应用开发增购包后才能申请使用的 OpenAPI， 本次调整后将下调门槛，所有钉钉底座均可以直接使用。

| **OpenAPI名称** | **OpenAPI详情** |
| --- | --- |
| [添加待入职员工](../../01-应用开发/02-4a8AMF6u2A-服务端API/0945-add-employees-to-be-hired-supports-system-and-custom-fields.md) | 在企业自有通讯录系统内，添加待入职员工时，调用本接口在钉钉智能人事应用内同步添加待入职员工 |
| [配置考勤排班附加信息](../../01-应用开发/02-4a8AMF6u2A-服务端API/0211-synchronization-scheduling-information.md) | 企业考勤排班信息较多，手动配置排班的打卡位置、打卡WiFi信息比较繁琐，可调用本接口，更新排班的附加信息 |
| [查询指定用户的封账规则](../../01-应用开发/02-4a8AMF6u2A-服务端API/0242-encapsulate-account-sealing-and-unsealing-rules.md) | 开启封账后，封账范围内的考勤结果将封存不允许修改。包含以下操作：请假，外出，出差，加班，补卡申请；员工排班，修改考勤结果等，调用本接口根据企业员工userId列表，获取员工的封账规则信息 |
| [发送DING消息](../../01-应用开发/02-4a8AMF6u2A-服务端API/0712-robot-sends-nail-message.md) | 企业在紧急场景下，可调用本接口给指定员工发起应用内DING消息、短信DING消息和电话DING消息提醒 |
| [撤回已经发送的DING消息](../../01-应用开发/02-4a8AMF6u2A-服务端API/0713-robot-withdraws-pin-message.md) | 已发送的DING消息，支持调用本接口进行撤回 |
| [上传打卡记录](../../01-应用开发/02-4a8AMF6u2A-服务端API/0197-upload-punch-records.md) | 企业使用三方打卡设备或门禁系统刷卡，调用本接口，可将三方打卡或刷卡记录上传到钉钉考勤，作为员工的考勤打卡信息 |

## **（二）扩容方式调整**

为满足企业级客户对应用开发资源的需求，现对现有资源进行了提升，具体方案可通过以下两种模式实现弹性扩展。

**方式一**：当客户每购入**1套专业版**，您可在以下权益中**任选5项组合扩容**，根据企业需求灵活定制，实现资源精准配置：

| **权益项** | | **若5项资源都需要**  示例配置A | **若需要应用开发、连接流**  示例配置B |
| --- | --- | --- | --- |
| 企业存储 | | 1TB | 不选 |
| 音视频 | 会议资源 | 3 个60分钟标清会议室  + 2 个24小时高清会议室  （同时开5个会议） | 不选 |
| 直播资源 | 1 个60分钟标清直播间  + 1个24小时高清直播间  （同时进行2场直播） | 不选 |
| 应用开发 | 付费 API 调用量  Webhook & Stream用量 | 20 万次/自然月  5 万次/自然月 | 60 万次/自然月  15 万次/自然月  （3个权益） |
| 连接流节点执行量 | 1 万次/自然月 | 2万次/自然月  （2个权益） |

- 已购买钉钉专业版/钉钉专属版且合同处于有效期内的客户，仍享有原合同权益，不受本次调整影响。
- 附：[钉钉专业版（新）权益说明](https://alidocs.dingtalk.com/i/p/WVJqzqJw73dDXYEKJqzqJxEjkKyJqXYE?dontjump=true)

**方式二**：

- 支持购买[企业开发增购包](../../01-应用开发/02-4a8AMF6u2A-服务端API/1431-dingtalk-application-development-platform-billing-model.md)，开发者可登录[开发者后台-资源管理](https://open-dev.dingtalk.com/?hash=%23%2F#/)查看企业所有的用量权益。如您已经收到用量预警，或调用额度无法满足使用，您可以购买[应用开发增购包（独立购）](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)提升当月调用总额度。

  |  | **企业应用开发增购包** | **价格** |
  | --- | --- | --- |
  | **API接口调用量** | **500万次/自然月（可叠加）** | **19800元/年** |
  | **Webhook&Stream调用量** | **50万次/自然月（可叠加）** |
  | **QPS频次限制** | **60qps（****上限60QPS****）** |
  | **连接流节点执行量** | **10万次/自然月（可叠加）** |
- 支持[连接流增购包](0003-connection-platform-billing-model-1.md)独立购，开发者可登录[开发者后台-资源管理](https://open-dev.dingtalk.com/?hash=%23%2F#/)查看企业所有的用量权益。如您已经收到用量预警，或调用额度无法满足使用，您可以购买[连接流增购包](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)提升当月调用总额度。

**钉钉开放平台团队**

**2025年10月31日**
