---
title: "数据资产接口调整说明"
source_url: "https://open.dingtalk.com/document/dataopen/data-asset-interface-adjustment-description-1"
namespace: "dataopen"
slug: "data-asset-interface-adjustment-description-1"
group: "数据资产"
tab: "平台介绍"
breadcrumb: "平台计费 > 数据资产接口调整说明"
doc_id: "PZRkVA5P5Y"
updated_at: "2025-09-23 19:20:35"
---

> Source: https://open.dingtalk.com/document/dataopen/data-asset-interface-adjustment-description-1
> Path: 数据资产 / 平台介绍 / 平台计费 > 数据资产接口调整说明
> Updated: 2025-09-23 19:20:35

# 数据资产接口调整说明

本文介绍了数据资产 API 调整内容。

## **数据目录**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取企业待办统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1779-obtains-the-to-do-statistics-of-an-enterprise.md) | 调用本接口获取企业待办相关的统计数据 | 新版服务端 |
| [获取企业日程统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1780-queries-enterprise-schedule-statistics.md) | 调用本接口获取企业日程相关的统计数据 | 新版服务端 |
| [获取企业钉盘统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1781-obtains-the-statistics-on-enterprise-dingtalk-trays.md) | 调用本接口获取企业钉盘的统计数据 | 新版服务端 |
| [获取数字区县组织信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1782-querydigitaldistrictorginfo-api-reference.md) | 调用本接口获取数字区县组织信息 | 新版服务端 |
| [获取企业单聊统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1783-queries-the-statistics-on-one-time-enterprise-chats.md) | 调用本接口获取企业即时沟通中单聊的统计数据 | 新版服务端 |
| [获取企业群聊统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1784-obtain-enterprise-group-chat-statistics.md) | 调用本接口获取企业即时沟通中群聊的统计数据 | 新版服务端 |
| [获取企业日志统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1785-obtain-enterprise-log-statistics.md) | 调用本接口获取企业日志的统计数据 | 新版服务端 |
| [获取企业邮箱统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1786-queries-enterprise-email-statistics.md) | 调用本接口获取企业邮箱的统计数据 | 新版服务端 |
| [获取企业文档统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1787-get-enterprise-document-statistics.md) | 获取本接口获取企业文档的统计数据 | 新版服务端 |
| [获取企业签到统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1788-queries-enterprise-check-in-statistics.md) | 调用本接口获取企业签到的统计数据 | 新版服务端 |
| [获取企业公告统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1789-queries-corporate-announcement-statistics.md) | 调用本接口获取企业公告的统计数据 | 新版服务端 |
| [获取企业考勤统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1790-queries-enterprise-attendance-statistics.md) | 调用本接口获取企业考勤的统计数据 | 新版服务端 |
| [获取企业审批统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1791-obtains-enterprise-approval-statistics.md) | 调用本接口获取企业OA审批的统计数据 | 新版服务端 |
| [获取企业发红包统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1792-obtains-the-statistics-on-red-packets-issued-by-enterprises.md) | 调用本接口获取企业发红包的统计数据 | 新版服务端 |
| [获取企业群直播统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1793-obtains-the-live-stream-statistics-for-an-enterprise-group.md) | 调用本接口获取企业群直播的统计数据 | 新版服务端 |
| [获取企业全员圈统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1794-obtains-the-statistical-data-of-all-employees-of-an-enterprise.md) | 调用本接口获取企业全员圈评论、点赞和动态统计数据 | 新版服务端 |
| [获取企业用户在线统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1795-retrieve-online-statistics-of-enterprise-users.md) | 调用本接口获取企业用户在线情况的统计数据 | 新版服务端 |
| [获取企业电话会议统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1796-get-enterprise-teleconference-statistics.md) | 调用本接口获取企业电话会议发起和参与情况的统计数据 | 新版服务端 |
| [获取企业视频会议统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1797-get-enterprise-video-conference-statistics.md) | 调用本接口获取企业视频会议发起和参与情况的统计数据 | 新版服务端 |
| [获取企业接收红包统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1798-queries-the-red-envelope-receiving-statistics-of-an-enterprise.md) | 调用本接口获取企业接收红包（抢红包）的统计数据 | 新版服务端 |
| [获取企业钉钉运动统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1799-queries-dingtalk-movement-statistics.md) | 调用本接口获取企业员工钉钉运动的统计数据 | 新版服务端 |
| [获取企业员工类型统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1800-obtains-statistics-on-employee-types.md) | 调用本接口获取企业花名册不同类型员工的统计数据 | 新版服务端 |
| [获取企业DING发送统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1801-obtain-sending-statistics-of-an-enterprise-ding.md) | 调用本接口获取企业DING发送的统计数据 | 新版服务端 |
| [获取企业用户激活状态统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1802-obtains-statistics-on-user-activation-status.md) | 调用接口获取企业用户激活状态的统计数据 | 新版服务端 |
| [获取企业DING接收及评论统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1803-obtain-statistics-on-receiving-and-comments-of-enterprise-ding.md) | 调用本接口获取企业接收和评论DING的统计数据 | 新版服务端 |

## **专属开放**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取视频直播明细列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1747-queries-the-details-list-of-apsaravideo-live.md) | 调用本接口获取视频直播明细列表 | 旧版服务端 |
| [获取视频直播观看人员列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1748-query-users-of-apsaravideo-live.md) | 调用本接口获取观看视频直播的人员列表 | 旧版服务端 |
| [获取企业视频直播统计列表（部门维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1749-live-broadcast-summary-statistics-of-key-account-departments.md) | 调用本接口按部门直播视频统计列表数据 | 旧版服务端 |
| [获取企业视频直播统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1750-query-live-streaming-statistics.md) | 调用本接口获取企业视频直播统计数据 | 旧版服务端 |
| [获取企业某天的视频会议统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1751-video-conferencing-statistics-query-v2-for-key-accounts.md) | 调用本接口获取企业在某一天的视频会议统计数据 | 旧版服务端 |
| [获取企业某天的所有部门视频会议统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1752-video-conferencing-statistics-list-for-key-accounts-and-departments.md) | 调用本接口查询企业在某天各部门视频会议统计列表 | 旧版服务端 |
| [获取企业视频会议明细列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1753-video-conference-details-for-key-accounts.md) | 调用本接口获取企业视频会议明细列表 | 旧版服务端 |
| [获取视频会议详情](https://open.dingtalk.com/document/development/get-video-meeting-details-1) | 调用本接口获取视频会议详情，包含参会人员列表和各个参会人员的参会时长 | 新版服务端 |
| [获取企业某天的所有部门电话会议统计列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1755-major-customer-department-dimension-teleconference-statistics.md) | 调用本接口查询企业在某天各部门电话会议汇总统计列表 | 旧版服务端 |
| [获取企业电话会议明细列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1756-major-account-conference-call-details-list.md) | 调用本接口查询企业在某天发起的电话会议列表及详情 | 旧版服务端 |
| [获取企业某天的电话会议数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1757-major-customer-teleconference-statistics-interface.md) | 调用本接口获取企业某天的电话会议数据 | 旧版服务端 |
| [获取企业各类群组创建情况](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1758-api-for-obtaining-the-creation-status-of-various-groups.md) | 调用本接口查询企业各类群组创建情况 | 旧版服务端 |
| [获取企业聊天数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1759-chat-data-statistics-query-for-key-accounts.md) | 调用本接口查询当前企业每天的聊天汇总数据，包含用户数及群数等 | 旧版服务端 |
| [获取企业部门聊天数据（部门维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1760-dingtalk-chat-information-in-key-accounts.md) | 调用本接口查询企业各部门聊天数据 | 旧版服务端 |
| [获取企业应用访问情况](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1761-queries-the-daily-usage-summary-of-microapplications-in-an-enterprise.md) | 调用本接口查询当前企业每天的微应用使用汇总数据 | 旧版服务端 |
| [统计企业活跃用户](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1762-query-for-dau-statistics.md) | 调用本接口查询企业的DAU（日活跃用户数量）汇总数据 | 旧版服务端 |
| [企业活跃用户统计列表（部门维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1763-query-the-statistics-of-active-users-in-a-department-of.md) | 调用本接口查询部门维度的活跃用户统计数据列表 | 旧版服务端 |
| [查询企业通讯录未激活用户列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1764-queries-the-list-of-inactive-accounts-in-the-key-account.md) | 调用本接口查询当前企业当前通讯录未激活用户明细列表 | 旧版服务端 |
| [获取企业DING使用数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1765-enterprise-ding-quantity-statistics.md) | 调用本接口查询企业各类DING的使用情况 | 旧版服务端 |
| [获取企业DING使用数据（部门维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1766-query-the-departmental-transmission-status-of-key-clients.md) | 调用本接口查询企业各部门各类DING的使用情况 | 旧版服务端 |
| [获得组织维度日程相关信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1767-queries-the-number-of-people-who-have-created-an-event.md) | 调用本接口获得组织维度日程相关信息 | 新版服务端 |
| [获得企业创建日志相关信息（部门维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1768-obtains-information-about-a-created-enterprise-log-from-the-department.md) | 调用本接口按部门维度获取企业创建日志相关信息 | 新版服务端 |
| [获得企业创建日志相关信息（组织维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1769-obtains-information-about-a-created-enterprise-log-from-the-organization.md) | 获取企业组织维度创建日志相关数据 | 新版服务端 |
| [获得用户创建文档数和创建文档人数（部门维度）](https://open.dingtalk.com/document/development/queries-the-number-dingtalk-documents-created-per-day-in-a) | 调用本接口按部门维度获取用户创建文档数和创建文档人数 | 新版服务端 |
| [获取用户创建文档数和创建文档人数（组织维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1771-queries-the-number-dingtalk-documents-created-per-day-in-an.md) | 调用本接口按组织维度获取用户创建文档数和创建文档人数 | 新版服务端 |
| [获取发布智能填表数量和使用智能填表人数（部门维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1772-obtains-the-number-of-tables-published-by-the-enterprise-from.md) | 调用本接口按部门维度获取发布智能填表数量和使用智能填表人数 | 新版服务端 |
| [获取企业发布智能填表数（组织维度）](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1773-queries-the-number-of-tables-published-in-an-organization.md) | 调用本接口按组织维度获取企业发布智能填表数 | 新版服务端 |
| [获取互动服务窗相关数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1774-queries-the-data-about-the-interactive-service-window.md) | 调用本接口获取互动服务窗应用分析相关数据 | 新版服务端 |
| [获取年报数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1775-obtain-annual-report-data.md) | 调用本接口获取企业年报数据，涵盖当年参与音视频会议的次数和时长等。在一个自然年按照组织、部门和员工三个维度生产数据 | 旧版服务端 |
| [获取用户月活跃数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1776-retrieves-the-user-s-monthly-active-data.md) | 调用本接口获取组织维度用户月活跃数据 | 新版服务端 |
| [获取未活跃用户登录明细](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1777-obtains-the-logon-details-of-inactive-users.md) | 调用本接口未活跃用户登录明细统计信息 | 新版服务端 |
| [获取用户版本分布情况](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1778-queries-the-distribution-of-user-versions.md) | 调用本接口获取用户版本分布情况 | 新版服务端 |

## **其他**

| **API** | **接口说明** | **接口版本** |
| --- | --- | --- |
| [获取日志统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1550-query-log-statistics.md) | 调用本接口，获取日志的已读人数、评论条数、评论人数、点赞人数 | 旧版服务端 |
| [查询直播的观看数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1494-queries-the-playback-data-of-a-live-stream.md) | 调用本接口，查询直播的观看数据 | 新版服务端 |
| [批量获取钉钉运动数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1745-queries-the-number-of-dingtalk-movement-steps-of-multiple-users.md) | 调用本接口，批量获取钉钉运动数据 | 旧版服务端 |
| [获取个人或部门钉钉运动数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1746-queries-individual-or-department-dingtalk-exercise-steps.md) | 调用本接口，查询用户个人或企业部门每天的钉钉运动步数，最多可以查询31天的数据 | 旧版服务端 |
