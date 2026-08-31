---
title: "概述"
source_url: "https://open.dingtalk.com/document/development/attendance-overview"
namespace: "development"
slug: "attendance-overview"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 概述"
doc_id: "LEAUqHYt7C"
updated_at: "2026-07-02 10:36:00"
---

> Source: https://open.dingtalk.com/document/development/attendance-overview
> Path: 应用开发 / 服务端 API / 考勤 > 概述
> Updated: 2026-07-02 10:36:00

# 概述

本文介绍了考勤打卡开放接口的能力以及如何接入考勤相关接口。

## 什么是考勤

考勤打卡是钉钉的官方应用，致力于为企业提供软硬一体的员工考勤管理的解决方案，随时随地了解团队状态，**出勤人员一目了然**；**智能统计考勤数据，**一键下载，无需人工核算，更多介绍请参见[钉钉使用手册-考勤](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbEJAykaY3XLq?dontjump=true%23%23)。

具备以下特点：

- **打卡方式丰富，覆盖多种考勤场景**：支持GPS定位，WiFi定位，蓝牙定位，考勤机打卡等软硬一体的打卡方式。
- **内外勤统一管理，数据统计更便捷**：支持外勤打卡，对于临时外出，外地出差的员工考勤也能有效管理。
- **假勤审批关联，算工资一张表搞定**：请假，加班，外出，出差审批自动汇总计算，避免多张报表反复校验。

## 如何开通考勤

考勤是钉钉默认安装的官方应用。员工可以在钉钉工作台打开应用并使用。

- 手机端：钉钉手机客户端-工作台

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0679592871/p1084731.png)
- 电脑端：钉钉电脑客户端-工作台

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0679592871/p512230.png)

## 开放概览

### **开放接口列表**

考勤提供了丰富的接口开放能力，开发者通过API接口可以实现考勤和企业业务系统打通。

#### **考勤组管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建考勤组](0170-attendance-group-write.md) | 调用本接口创建考勤组。 | 旧版 |
| [更新考勤组](0171-attendance-group-update-interface.md) | 调用本接口根据考勤组id更新考勤组信息。 | 旧版 |
| [删除考勤组](0172-delete-attendance-group.md) | 调用本接口批量删除考勤组。 | 旧版 |
| [搜索考勤组摘要](0173-attendance-group-search.md) | 调用本接口按考勤组名称模糊搜索，获取考勤组摘要信息。 | 旧版 |
| [获取考勤组详情](0174-query-a-single-attendance-group.md) | 调用本接口根据考勤组ID获取考勤组详情。 | 旧版 |
| [根据groupKey查询考勤组信息](0175-queries-attendance-group-information-by-id.md) | 调用本接口根据考勤组id查询考勤组信息。 | 旧版 |
| [groupKey转换为groupId](0176-convert-groupkey-to-groupid.md) | 调用本接口将考勤组的groupKey转换为groupId。 | 旧版 |
| [groupId转换为groupKey](0177-groupid-to-groupkey.md) | 调用本接口将考勤组的groupId转换为groupKey。 | 旧版 |
| [批量获取考勤组摘要](0178-batch-query-of-simple-information-of-the-attendance-group.md) | 调用本接口分页获取企业内所有考勤组摘要信息。 | 旧版 |
| [批量获取考勤组详情](0179-batch-obtain-attendance-group-details.md) | 调用本接口查询所有的考勤组详情信息。 | 旧版 |
| [获取用户考勤组](0180-queries-a-user-attendance-group.md) | 调用本接口获取员工的考勤组信息。 | 旧版 |
| [批量新增参与考勤人员](0181-batch-add-employees-under-the-attendance-group.md) | 调用本接口在指定的考勤组下批量新增考勤组成员。 | 旧版 |
| [更新参与考勤人员](0182-attendance-group-member-update.md) | 调用本接口更新考勤组成员，支持新增或删除人员、部门、无需考勤人员。 | 旧版 |
| [获取参与考勤人员](0183-batch-query-of-attendance-group-members.md) | 调用本接口通过操作人的userid和考勤组id获取当前考勤组下的成员信息。 | 旧版 |
| [获取参与考勤人员的userid](0184-query-attendance-group-personnel-information-in-batches.md) | 调用本接口分页获取某个考勤组下的所有员工的userId。 | 旧版 |
| [批量删除参与考勤人员](0185-batch-delete-employees-under-the-attendance-group.md) | 调用本接口批量删除指定考勤组下的考勤组成员。 | 旧版 |
| [查询参与考勤人员列表](0186-batch-query-of-employees-in-the-attendance-group.md) | 调用本接口查询指定考勤组下的员工列表。 | 旧版 |
| [校验用户是否在当前考勤组](0187-query-members-by-id.md) | 调用本接口校验某个部门或者员工是否属于某个考勤组，返回值为属于这个考勤组的部门ID或者员工ID。 | 旧版 |
| [批量新增Wi-Fi信息](0188-batch-add-wifi-under-attendance-group.md) | 调用本接口为指定考勤组批量新增wifi信息。 | 旧版 |
| [批量查询Wi-Fi信息](0190-batch-query-wifi-under-attendance-group.md) | 调用本接口批量查询指定考勤组下的wifi列表信息。 | 旧版 |
| [批量移除Wi-Fi信息](0189-batch-remove-wifi-under-attendance-group.md) | 调用本接口批量移除指定考勤组的wifi信息。 | 旧版 |
| [批量新增地点](0191-atch-add-position-under-attendance-group.md) | 调用本接口在指定考勤组下批量新增position。 | 旧版 |
| [批量查询地点](0193-batch-query-position-under-attendance-group.md) | 调用本接口批量查询指定考勤组下的position列表信息。 | 旧版 |
| [批量删除地点](0192-delete-position-in-batches-under-the-attendance-group.md) | 调用本接口在指定考勤组下批量删除position。 | 旧版 |
| [查询考勤写操作权限](0194-attendance-writing-operation-is-brand-new-query.md) | 用于查询企业员工在考勤组内的操作权限。 | 新版 |

#### **考勤打卡**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [获取打卡结果](0195-open-attendance-clock-in-data.md) | 调用本接口返回企业内员工的实际打卡结果。 | 旧版 |
| [获取打卡详情](0196-attendance-clock-in-record-is-open.md) | 调用本接口返回企业内员工的实际打卡详情。 | 旧版 |
| [上传打卡记录](0197-upload-punch-records.md) | 调用本接口将三方考勤系统的刷卡或刷脸记录上传到钉钉考勤，做为钉钉打卡流水。 | 新版 |

#### **考勤班次**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [创建班次](0198-create-modify-shifts.md) | 调用本接口创建钉钉考勤班次。 | 旧版 |
| [删除班次](0199-delete-shift.md) | 调用本接口根据班次ID删除考勤班次。 | 旧版 |
| [按名称搜索班次](0202-search-shifts-by-rank.md) | 调用本接口根据名称模糊搜索班次，返回班次名称和ID信息。 | 旧版 |
| [获取班次摘要信息](0203-enterprise-shift-query-in-batches.md) | 调用本接口查询所有的班次信息。 | 旧版 |
| [获取班次详情](0204-shift-query.md) | 调用本接口根据班次ID查询班次的详细信息。 | 旧版 |
| [查询历史班次](0201-query-history-shifts.md) | 调用本接口根据班次ID和version查询历史班次信息。 | 旧版 |
| [修改打卡时段设置](0200-modify-card-settings.md) | 调用本接口修改考勤班次卡点的设置信息。 | 旧版 |

#### **考勤排班**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询成员排班信息](0205-query-scheduling-for-a-day.md) | 调用本接口查询某人在某工作日的排班信息。 | 旧版 |
| [批量查询人员排班信息](0206-query-batch-scheduling-information.md) | 调用本接口批量查询员工在工作日内的排班信息。 | 旧版 |
| [排班制考勤组排班](0207-scheduling-system-attendance-group-scheduling.md) | 调用此接口给排班制考勤组成员进行排班。 | 旧版 |
| [查询排班打卡结果](0208-query-the-results-of-a-batch-of-tasks.md) | 调用本接口查询排班的打卡结果，打卡结果包含打卡时间、迟到、早退、内勤及外勤等信息。 | 旧版 |
| [查询企业考勤排班详情](0209-interface-for-daily-full-query-of-attendance-scheduling-information.md) | 调用本接口查询某天的考勤排班信息。 | 旧版 |
| [批量查询成员排班概要信息](0210-query-scheduling-summary-information.md) | 调用本接口查询用户在某个时间段内的排班概要信息。 | 旧版 |

#### **考勤规则**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [分页获取加班规则列表](0212-retrieve-a-list-of-overtime-rules-by-page.md) | 调用本接口分页获取考勤打卡中设置的加班规则列表。 | 新版 |
| [分页获取补卡规则列表](0213-retrieve-a-list-of-replenishment-rules-by-page.md) | 调用本接口分页获取考勤打卡中设置的补卡规则列表。 | 新版 |
| [批量获取加班规则设置](0214-batch-retrieve-overtime-rules.md) | 调用本接口用于根据多个加班规则ID，批量获取加班规则设置详情。 | 新版 |

#### **考勤统计**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询是否启用智能统计报表](0215-determine-whether-to-enable-attendance-intelligent-report.md) | 调用本接口判断企业是否开启了考勤智能报表，如果企业未启用智能报表，无法调用统计报表其他的接口。 | 旧版 |
| [获取用户考勤数据](0216-obtain-the-attendance-update-data.md) | 调用本接口获取指定用户当天的考勤数据，包括打卡流水记录、打卡结果和审批列表等。 | 旧版 |
| [获取报表假期数据](0217-obtains-the-holiday-data-from-the-smart-attendance-report.md) | 调用本接口根据假期名称和用户ID获取钉钉智能考勤报表的假期数据。 | 旧版 |
| [获取考勤报表列定义](0218-queries-the-enterprise-attendance-report-column.md) | 调用本接口获取企业智能考勤报表中的列信息。 | 旧版 |
| [获取考勤报表列值](0219-queries-the-column-value-of-the-attendance-report.md) | 调用本接口用于获取钉钉智能考勤报表的列值数据。 | 旧版 |
| [查询用户某段时间内是否处于封账状态](0220-checks-whether-a-user-has-blocked-accounts-within-a-specified.md) | 调用本接口查询员工一段时间内是否处于封账状态，如果处于封账状态，不能发起审批、排班、换班等操作。 | 新版 |

#### **考勤机管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询员工智能考勤机列表](0221-query-the-list-of-employee-intelligent-attendance-machines.md) | 调用本接口查询员工智能考勤机列表。 | 旧版 |
| [根据设备ID获取员工信息](0222-obtain-information-about-employees-based-on-device-ids.md) | 调用本接口根据考勤机设备ID查询这台考勤机设备上的员工信息。 | 新版 |
| [查询考勤机信息](0223-query-attendance-machine-information.md) | 调用本接口根据考勤机设备ID查询这台考勤机的相关信息。 | 新版 |
| [变更智能考勤机员工](0224-change-intelligent-attendance-machine-staff.md) | 调用本接口变更智能考勤机员工。 | 新版 |

#### **假期审批**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [通知审批通过](0226-api-processapprovefinish.md) | 调用本接口通知审批通过，支持加班、请假、外出和出差类型。 | 旧版 |
| [通知审批撤销](0227-notify-the-attendance-to-modify-the-punch-result-when-the.md) | 调用本接口通知审批撤销，支持加班、请假、外出、出差和补卡类型。 | 旧版 |
| [通知补卡通过](0228-make-up-the-card-after-approval.md) | 调用本接口通知考勤补卡通过。 | 旧版 |
| [通知换班通过](0229-shift-change-operation-after-approval.md) | 通过本接口换班审批通过后，通知考勤执行换班动作，可以和自己换班，也可以和别人换班。 | 旧版 |
| [预计算时长](0225-api-calculateduration.md) | 调用本接口根据考勤系统的排班情况，预计算员工加班、出差及请假的时长信息。 | 旧版 |
| [计算请假时长](0230-calculate-leave-duration.md) | 调用本接口获取自动根据排班规则统计出每个员工的请假时长。 | 旧版 |
| [查询请假状态](0231-query-status.md) | 调用本接口查询指定企业下指定用户在指定时间段内的请假状态。 | 旧版 |

#### **假期管理**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [添加假期规则](0233-add-holiday-rules.md) | 调用本接口新建一个假期规则。 | 新版 |
| [更新假期规则](0234-update-holiday-rules.md) | 调用本接口更新指定假期的相关规则。 | 新版 |
| [删除假期规则](0235-api-for-deleting-holiday-types.md) | 调用本接口删除指定的假期规则。 | 旧版 |
| [查询假期规则列表](0238-holiday-type-query.md) | 调用本接口查询企业内的假期规则列表。 | 旧版 |
| [初始化假期余额](0236-initialize-holiday-balance.md) | 调用本接口批量初始化假期余额。 | 旧版 |
| [查询假期余额](0239-query-holiday-balance.md) | 调用本接口根据企业或员工分页获取假期余额信息，每次返回50条数据。 | 旧版 |
| [批量更新假期余额](0237-bulk-update-holiday-balance.md) | 调用本接口批量更新假期余额信息。 | 旧版 |
| [批量查询员工假期余额变更记录](0240-batch-query-employee-leave-balance-change-record.md) | 调用本接口根据员工分页获取假期余额记录信息。 | 旧版 |
| [查询用户考勤节假日信息](0241-obtain-user-attendance-and-holiday-information.md) | 调用本接口查询员工一段时间内的节假日信息。 | 新版 |

#### **封账规则**

| **API** | **API说明** | **API版本** |
| --- | --- | --- |
| [查询指定用户的封账规则](0242-encapsulate-account-sealing-and-unsealing-rules.md) | 调用本接口查询指定用户的封账和解封规则。 | 新版 |

### **回调事件列表**

考勤支持班次变更、考勤组变更、员工打卡事件及员工加班事件等多种回调事件，更多事件参考[事件订阅总览](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)。

## 使用教程

钉钉提供了考勤组管理、假勤审批及考勤补卡等常用场景的使用流程示例。

- [通过考勤接口与事件获取员工到岗情况](0166-the-enterprise-big-screen-displays-the-attendance-of-employees.md)
- [同步与更新企业自有考勤补卡信息](0165-the-replenishment-card-of-enterprise-self-developed-attendance-system-is-synchronized.md)
- [创建、获取、更新及删除考勤组](0163-operation-related-to-attendance-group.md)
- [新增、获取、更新及删除考勤人员](0164-attendance-group-member-operations.md)
- [按天获取员工考勤报表信息](0167-obtain-the-employee-attendance-report-information.md)
- [企业自有假勤审批同步到钉钉](0168-enterprise-s-own-oa-approval-system-synchronized-to-dingtalk-during-holidays.md)
- [企业自有系统考勤打卡信息同步到钉钉](0169-attendance-synchronizes-information.md)

## 名词解释

### 考勤组

考勤组是企业管理员为员工设置的考勤规则组，可以满足根据企业不同工种设置不同类型的考勤组。

> **[!NOTE]**
>
> 由于新旧接口规范等原因，考勤组的的唯一标识为group\_id或groupKey。groupKey值可以调用[groupKey转换为groupId](0176-convert-groupkey-to-groupid.md)接口转换为对应的group\_id。

考勤组类型分为三类：

- **固定班制考勤组**：适用于上班时间、休息时间固定的人员。例如每天朝九晚六、固定双休。
- **排班制考勤组**：适用于早晚班或每日班次不太一样、休息需要排休的人员。
- **自由工时考勤组**：适用于上班时间灵活的人员。

登录[钉钉管理后台](https://oa.dingtalk.com/)，在**工作台 > 应用管理 > 考勤打卡 > 考勤组管理**中新增考勤组。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0679592871/p512244.png)

### 假期规则（leave\_code）

假期规则的唯一标识是leave\_code。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0679592871/p512246.png)

### 班次

创建考勤组时需要绑定班次，班次确定的是考勤组内员工打卡的时间点和上班时长等，企业可以根据自身需求个性化设置员工的考勤班次，支持设置弹性打卡、晚到晚走、早到早走、迟到、旷工等。

登录[钉钉管理后台](https://oa.dingtalk.com/)，在**应用管理 > 考勤打卡 > 班次管理**中新增班次。![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0679592871/p512247.png)
