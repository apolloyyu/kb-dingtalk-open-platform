---
title: "介绍"
source_url: "https://open.dingtalk.com/document/connection/connection-attendance-overview"
namespace: "connection"
slug: "connection-attendance-overview"
group: "连接平台"
tab: "连接器中心"
breadcrumb: "官方连接器 > 介绍"
doc_id: "blRnLZRqf5"
updated_at: "2026-08-03 09:15:59"
---

> Source: https://open.dingtalk.com/document/connection/connection-attendance-overview
> Path: 连接平台 / 连接器中心 / 官方连接器 > 介绍
> Updated: 2026-08-03 09:15:59

# 介绍

## **考勤**

钉钉考勤可随时随地了解团队状态，**出勤人员一目了然**；**智能统计考勤数据**，一键下载，无需人工核算；云端存储，**考勤数据永不丢失**。更多介绍请参见[钉钉使用手册-考勤](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/3KLw95QMzkb8gRGgMK6oJAjrymPeEN2q)。

钉钉考勤连接器覆盖3个触发事件和多个执行动作，支持对**员工打卡**、**排班变更**、**员工加班**事件的监听做针对性的业务处理。

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

### **触发事件**

考勤连接器支持监听以下 **3 类事件**，可实现自动化的业务处理：

| **事件类型** | **触发条件** |
| --- | --- |
| 员工打卡事件 | 监听员工打卡行为，触发后续业务流程，更多信息可查看[员工打卡事件](../../01-应用开发/04-LFcRvVD08N-事件订阅/0129-employee-clock-in-event.md)说明。 |
| 排班变更事件 | 监听排班调整，同步更新相关业务数据，更多信息可查看[班次变更](../../01-应用开发/04-LFcRvVD08N-事件订阅/0127-intelligent-personnel-shift-change.md)说明。 |
| 员工加班事件 | 监听加班申请与审批状态，自动化处理加班逻辑，更多信息可查看[员工加班事件](../../01-应用开发/04-LFcRvVD08N-事件订阅/0130-employee-overtime-events.md)说明。 |

### **执行动作**

| **模块** | **核心能力** |
| --- | --- |
| 考勤组管理 | 创建/更新/删除考勤组，批量管理参与人员，校验成员归属，更多信息查看[考勤组管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0170-attendance-group-write.md)相关接口介绍。  **[!NOTE]**  考勤组是一类具有相同的班次、考勤位置等考勤规则的人或部门的组合，企业可根据实际业务设置多个考勤组。 |
| 班次管理 | 创建/修改/删除班次，查询班次详情，按名称搜索班次，更多信息查看[班次管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0198-create-modify-shifts.md)相关接口介绍。  **[!NOTE]**  在钉钉考勤应用中，班次是一类具有相同的打卡时间、休息时间等规则的组合，企业可根据实际业务设置多个班次。 |
| 排班管理 | 排班制考勤组排班，查询排班打卡结果，查询企业排班详情，更多信息查看[排班管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0207-scheduling-system-attendance-group-scheduling.md)相关接口介绍。 |
| 打卡管理 | 上传打卡记录，获取打卡结果/详情（区分汇总与明细），更多信息查看[打卡管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0195-open-attendance-clock-in-data.md)相关接口介绍。 |
| 假期管理 | 假期规则，余额初始化/批量更新/查询，支持普通假期与调休假期，更多信息查看[假期管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0232-holiday-management-describe.md)相关接口介绍。 |
| 假期审批 | 补卡/审批通过/撤销通知（加班、请假、外出、出差），时长预计算与统计，更多信息查看[假期审批](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0225-api-calculateduration.md#undefined)相关接口介绍。 |
| 考勤统计 | 智能报表列定义/数据查询，用户考勤数据聚合（打卡流水、结果、审批列表），更多信息查看[考勤统计](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0216-obtain-the-attendance-update-data.md)相关接口介绍。 |
| 考勤机管理 | 查询员工智能考勤机列表，更多信息查看[查询员工智能考勤机列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0221-query-the-list-of-employee-intelligent-attendance-machines.md)相关接口介绍。 |

### **使用教程**

- [获取考勤调休余额](0009-obtain-attendance-balance.md)

## **宜搭**

宜搭平台集合了页面编排(表单门户等)、业务模型编排、业务流程编排、服务编排、数据展现及分析5大核心能力。宜搭构建的应用，天然具备云原生 (分布式计算、弹性扩容、异地容灾、CDN加速、企业级云安全) 和钉原生特性 (和钉钉的消息、通讯录 、待办打通，应用可以一键发布到钉钉群、工作台等)。更多介绍请参见[钉钉使用手册-宜搭](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/m0Xw6OYE4D7VLkB7vGP5WRq13rbjgPM5?spm=ding_open_doc.document.0.0.7289d3942KuNBd)。

在连接平台，你可以使用【宜搭】连接器来获取或操作宜搭表单、任务、流程等。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 流程管理 | 发起/更新/删除/终止审批流程，获取流程实例信息，批量查询流程实例，更多信息查看[流程管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0311-api-startinstance-v2.md)相关接口介绍。 |
| 表单管理 | 保存/更新/删除表单数据，查询表单实例，获取子表组件数据，获取表单组件定义，更多信息查看[表单管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0317-api-getformdatabyid-v2.md)相关接口介绍。 |
| 任务管理 | 转交任务，提交评论，获取审批记录，查询组织维度任务列表，查询抄送任务，更多信息查看[任务管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0341-transfer-tasks.md)相关接口介绍。 |

### **使用教程**

- [审批表单数据同步至宜搭](0010-approval-form-appropriate.md)

## **表格**

钉钉表格是阿里巴巴集团钉钉研发的企业协同办公套件的一部分。在日常使用中，无需下载文档即可通过电脑、手机或平板直接编辑和查看文档内容，文档内容实时自动保存。在钉钉中打开表格或 Excel 文件时，依据企业设置和文件内容，可能使用不同的应用打开表格。

### **参数说明**

- **目录项ID**

  目录项 id 唯一标识了一篇表格文档。可以在 url 中截取。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9308762371/p878199.png)
- **工作表名称**

  每个目录项中的工作表名称是唯一的。可以在文档底部栏获取，也可以对工作表名称进行编辑修改。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9308762371/p878200.png)
- **单元格区域**

  工作表中单元格区域格式为`区域内左上角单元格:区域内右下角单元格`

  例如： B2:C3 表示区域如下图所示。

  ![image.png](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9308762371/p878201.png)

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 工作表管理 | 在工作表指定位置插入/删除行或列，设置行/列的可见性，更多信息查看[工作表管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0591-create-a-worksheet.md)相关接口介绍。 |
| 区域管理 | 获取/更新/清除单元格指定区域内的数据，支持仅清除数据或同时清除格式，更多信息查看[区域管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0609-get-cell-properties.md)相关接口介绍。 |

## **日程**

钉钉日程管理与即时沟通深度结合，同事间共享日程，便捷发起日程会议，重要事情一目了然，团队协作更高效，给员工良好的使用体验。更多介绍请参见[钉钉使用手册-日程](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbOpyEdYLGLq2?dontjump=true%23%23)。

### **触发事件**

| **事件类型** | **触发条件** |
| --- | --- |
| 日程变更 | 当用户日程发生创建、更新、取消，或用户在本地删除日程时触发，更多信息可查看[日程变更](../../01-应用开发/04-LFcRvVD08N-事件订阅/0018-event-calendar-event-change.md)说明。 |

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 日程管理 | 创建/修改/删除日程（支持 userId 版本，相比 unionId 版本需额外传入 corpId），更多信息查看[日程管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0250-create-schedule.md)相关接口介绍。 |
| 日历查询 | 查询用户的日历本信息（userId 版本），更多信息查看[日历管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0261-query-a-calendar.md)相关接口介绍。 |
| 参与者管理 | 添加日程参与者（userId 版本），更多信息查看[参与者管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0256-add-schedule-participant.md)相关接口介绍。 |

### **使用教程**

- [新人入职自动发送培训日程](0011-new-recruits-automatically-send-training-schedule.md)

## **公告**

管理员可以通过公告发布公司或单位的规章制度、节假日信息等通知，快速通知到全体员工。更多功能详情可参考[钉钉使用手册-公告](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/mM3zoYAw1Rr8Dan5xEk6WnZ07y9NpXxD)。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 公告管理 | 创建/更新/删除企业公告，获取公告详情，更多信息查看[公告管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0279-create-an-enterprise-announcement.md)相关接口介绍。 |
| 公告查询 | 获取公告 ID 列表，获取公告分类列表，获取用户可查看的公告，更多信息查看[公告查询](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)相关接口介绍。 |
| 钉盘空间 | 获取公告钉盘空间信息，更多信息查看[获取公告钉盘空间信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0286-obtain-bulletin-nail-disk-space-information.md)相关接口介绍。 |

### **使用教程**

- [OA审批通过后发布公告](0012-announcement-approval.md)

## **签到**

员工可以在工作台或群中进行签到，快速上报当前位置。更多使用详情可参考[钉钉使用手册-签到介绍](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbEZDOqnQMXLq?dontjump=true)。

### **触发事件**

| **事件类型** | **触发条件** |
| --- | --- |
| 用户签到 | 当用户操作签到时，会触发用户签到事件，更多信息可查看[用户签到](../../01-应用开发/04-LFcRvVD08N-事件订阅/0014-event-check-in.md)说明。 |

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 获取部门用户签到记录 | 获取部门用户签到记录，更多信息查看[获取部门用户签到记录](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0291-get-check-in-data.md)相关接口介绍。 |
| 获取用户签到记录 | 查询多个用户一段时间范围内的签到记录，更多信息查看[获取用户签到记录](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0290-obtain-the-check-in-records-of-multiple-users.md)相关接口介绍。  **[!NOTE]**  只给企业调用，ISV无法调用。 |

## **日志**

方便管理者了解员工每日工作情况，可以帮助员工总结沉淀工作经验。更多介绍请参见[钉钉使用手册-日志](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbp6NA6NqzLq2?dontjump=true%23%23)。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 模板管理 | 获取模板详情，获取用户可见的日志模板，更多信息查看[模板管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0296-query-template-details.md)相关接口介绍。 |
| 日志查询 | 获取用户发出的日志列表，获取用户发送日志的概要信息，获取日志统计数据，更多信息查看[日志查询](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0297-query-logs-sent-by-an-employee.md)相关接口介绍。 |
| 互动管理 | 获取日志评论详情，获取日志相关人员列表（已读/评论/点赞人员），更多信息查看[日志评论](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0301-queries-log-comment-details.md)相关接口介绍。 |
| 接收范围 | 获取日志接收人员列表（含群成员），更多信息查看[获取日志接收人员列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0300-queries-log-sharing-personnel.md)接口介绍。 |
| 未读统计 | 获取用户日志未读数，更多信息查看[获取用户日志未读数](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0302-querying-the-employee-s-log-is-not-reading.md)接口介绍。 |

## **AI 能力**

AI接口是由阿里巴巴达摩院提供的功能服务，用于提升企业办公效率，主要有以下两个使用场景。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 文本翻译 | 输入一段文本，得到翻译指定语言后的译文，支持多种语言的互译，更多信息查看[钉钉文本翻译](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1009-dingtalk-translation.md)接口介绍。 |
| OCR文字识别 | 根据识别图片地址，进行OCR文字识别，更多信息查看[OCR文字识别](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1010-structured-image-recognition-api.md)接口介绍。 |

### **使用教程**

- [翻译文本内容](0013-translate-text-content.md)

## **AI 表格**

钉钉AI 表格集合了数据管理、流程协作、统计分析、自动化和数据可视化5大核心能力。AI 表格构建的数据应用，天然具备企业级特性（数据实时同步、权限精细管控、版本管理、数据追溯、多人协作）和钉原生特性（和钉钉的消息、通讯录、审批打通，数据可以一键分享到钉钉群、快捷发布到工作台等）。

在连接平台，你可以使用【AI 表格】连接器来获取或操作AI 表格数据表、记录等。

### **参数说明**

- **多维表ID**

  多维表id唯一标识了一篇文档。可以通过 url 获取，也可以通过文档信息面板获取。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864137.png)

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864142.png)
- **数据表ID**

  数据表 id 唯一标识了一篇AI表格文档。可以通过 url 获取，也可以通过文档信息面板获取。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864135.png)
- **记录ID**

  数据表中的每一行即是一个记录。一个数据表中通常有多个记录。

  记录 id 仅保证在文档中唯一，不保证全局唯一。可以通过`新增多行记录``获取多行记录`获取。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7102910371/p864129.png)

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 数据表管理 | 创建/更新/删除/获取数据表，获取所有数据表列表，更多信息查看[数据表管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0459-api-createsheet.md)相关接口介绍。 |
| 记录管理 | 新增/删除/更新/获取单行或多行记录，支持按用户维度查询记录，更多信息查看[记录管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0468-api-notable-insertrecords.md)相关接口介绍。 |

### **字段格式配置**

| **类型** | **设置值（新增/更新记录时使用的格式）** |
| --- | --- |
| 文本 | ``` "TextString" // 字符串 ``` |
| 数字 | ``` 123 // 支持整数/浮点数/字符串 ``` |
| 单选 | ``` "optionName1" // 单选选项名 ``` |
| 多选 | ``` ["optionName1", "optionName2"] // 多选选项名 ``` |
| 日期 | ``` "2023-12-20 03:00" // ISO 8601字符串 ``` |
| 人员 | ``` [   {     "unionId": "xxxxxxxxx"  // 可以通过获取多行记录等接口获取   } ] ```  ``` [   {     "staffId": "xxxxxxxxx"   } ] ``` |
| 部门 | ``` [   {     "deptId": "xxx"   } ] ``` |
| 附件 | 暂不支持 |
| 单向关联 | ``` {   "linkedRecordIds": [     "xxx",     "yyy"   ] } ``` |
| 双向关联 | ``` {   "linkedRecordIds": [     "xxx",     "yyy"   ] } ``` |
| 链接 | ``` {   "text": "Dingtalk",   "link": "https://dingtalk.com" } ``` |

### **条件查询配置**

| **字段类型** | **可用操作符** | **value** |
| --- | --- | --- |
| 文本 | equal | notEqual | contain | notContain | empty | notEmpty | 示例：`["abc"]`  operator 是 empty/notEmpty 时不需要传 |
| 数字 | equal | notEqual | greater | greaterEqual | less | lessEqual | empty | notEmpty | 示例：`["123"]`  operator 是 empty/notEmpty 时不需要传 |
| 单选 | equal | notEqual | contain | notContain | empty | notEmpty | 示例: `["option1", "optionId2"]`  operator 是 contain 时，包含 value 中的任何一个选项即满足条件  operator 是 notContain 时，不包含 value 中的所有选项即满足条件  operator 是 empty/notEmpty 时不需要传 |
| 多选 | 同「单选」 | 同「单选」 |
| 日期 | equal | greater | less | empty | notEmpty | 示例: `["2024-09-27" | timestamp]`  operator 是 empty/notEmpty 时不需要传  operator 是 equal 时，可以传相对日期，如下所示   ``` {   type: 'today' | 'tomorrow' | 'yesterday' | 'thisWeek' | 'lastWeek' | 'thisMonth' | 'lastMonth' | 'next7Days' | 'last7Days' | 'next30Days' | 'last30Days'; } ```   当 operator 是 greater/less 时，可以传相对日期，如下所示   ``` {   type: 'today' | 'tomorrow' | 'yesterday' | 'thisWeek' | 'lastWeek' | 'thisMonth' | 'lastMonth' | 'next7Days' | 'last7Days' | 'next30Days' | 'last30Days'; } ```   日期的筛选只精确到「日」。例如，{ operator: 'equal', value: ['2024-09-27 10:00']} 这一条件会匹配 '2024-09-27 12:00' 这条记录。 |
| 人员 | equal | notEqual | contain | notContain | empty | notEmpty | 示例: `[{"uid": "xxx"}, {"uid": "yyy"}]`  operator 是 contain 时，包含 value 中的任何一个选项即满足条件  operator 是 notContain 时，不包含 value 中的所有选项即满足条件  operator 是 empty/notEmpty 时不需要传 |

## **通讯录**

内部信息统一管理，清晰展示组织架构，快速找人，同时保障企业通讯数据安全。通讯录设置、管理、可见性管理等更多功能介绍请参考[钉钉使用手册-通讯录](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmbpxy30LLzLq2?dontjump=true#)。

### **触发事件**

| **事件类型** | **触发条件** |
| --- | --- |
| 企业相关 | 企业删除、企业信息变更，更多信息可查看[企业相关](../../01-应用开发/04-LFcRvVD08N-事件订阅/0058-the-organizational-relationship-enterprise-is-deleted.md)事件说明。 |
| 角色管理 | 创建角色、修改角色、删除角色，更多信息可查看[角色管理](../../01-应用开发/04-LFcRvVD08N-事件订阅/0059-businesses-increase-roles.md)相关事件说明。 |
| 部门管理 | 创建部门、修改部门、删除部门，更多信息可查看[部门管理](../../01-应用开发/04-LFcRvVD08N-事件订阅/0046-create-department-event.md)相关事件说明。 |
| 员工管理 | 企业员工激活、员工角色变更、员工部门变更、内部用户变更、通讯录用户增加、通讯录用户离职，更多信息可查看[用户管理](../../01-应用开发/04-LFcRvVD08N-事件订阅/0060-enterprise-role-change.md)相关事件说明。 |

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 用户管理 | 创建/更新/删除用户，查询用户详情，获取未登录钉钉的员工列表，userid/unionid 互转，更多信息查看[用户管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0055-user-information-creation.md)相关接口介绍。 |
| 角色管理 | 创建/更新/删除角色，获取角色详情/列表/组列表，批量增删员工角色，设定角色成员管理范围，更多信息查看[角色管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0086-address-book-add-role.md)相关接口介绍。 |
| 部门管理 | 更新/删除部门，获取部门详情/员工人数/子部门列表/人员列表/userid 列表，获取用户/部门的父部门列表，更多信息查看[部门管理](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0078-address-book-update-department.md)相关接口介绍。 |
| 外部联系人 | 添加/更新外部联系人，获取外部联系人列表/详情，更多信息查看[外部联系人](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0097-add-enterprise-external-contacts.md)相关接口介绍。 |
| 管理员与权限 | 获取管理员列表，获取管理员通讯录权限范围，更多信息查看[管理员与权限](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0068-query-the-administrator-list.md)相关接口介绍。 |

### **使用教程**

- [用户离职审批通过后删除用户](0014-delete-resignation-approval.md)

## **机器人**

在钉钉，机器人是独立存在的一个应用类型，可以开箱即用，也可以进行二次开发，无需和微应用或者群等场景进行强制绑定。

对于开发者，钉钉机器人是全局唯一的应用，即无论是在单聊场景中还是群聊场景中，都可以用来推送应用的通知和用来对用户进行对话式服务，机器人 ID 都可以是唯一的。这意味着开发者既可以选择仅创建一个机器人，而后将其放在各个应用场景下使用，也可以创建多个机器人，然后分别部署在不同场景下。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

#### **应用机器人**

| **模块** | **核心能力** |
| --- | --- |
| 文本消息 | 批量发送机器人单聊文本消息，更多信息查看[批量发送人与机器人会话中机器人消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口介绍。 |
| 图片消息 | 批量发送机器人单聊图片消息，更多信息查看[批量发送人与机器人会话中机器人消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口介绍。 |
| 链接消息 | 批量发送机器人单聊链接消息，更多信息查看[批量发送人与机器人会话中机器人消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口介绍。 |
| Markdown 消息 | 批量发送机器人单聊 Markdown 消息，更多信息查看[批量发送人与机器人会话中机器人消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口介绍。 |
| 按钮消息 | 批量发送单按钮/横向多按钮/竖向 2-5 个按钮消息，更多信息查看[批量发送人与机器人会话中机器人消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口介绍。 |

#### **自定义机器人**

| **模块** | **核心能力** |
| --- | --- |
| 文本消息 | 发送自定义机器人文本消息，更多信息查看[自定义机器人发送群消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0717-custom-robots-send-group-messages.md)接口介绍。 |
| 链接消息 | 发送自定义机器人链接消息，更多信息查看[自定义机器人发送群消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0717-custom-robots-send-group-messages.md)接口介绍。 |
| Markdown 消息 | 发送自定义机器人 Markdown 消息，更多信息查看[自定义机器人发送群消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0717-custom-robots-send-group-messages.md)接口介绍。 |
| ActionCard 消息 | 发送单按钮/横排多按钮/竖排多按钮 ActionCard 消息，更多信息查看[自定义机器人发送群消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0717-custom-robots-send-group-messages.md)接口介绍。 |
| FeedCard 消息 | 发送 FeedCard 消息（多图卡片），更多信息查看[自定义机器人发送群消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0717-custom-robots-send-group-messages.md)接口介绍。 |

### **使用教程**

- [机器人发送单聊文本消息](0015-robot-sends-message.md)
- [工作日定时发送机器人消息收集日报](0016-robot-weekdays-collect.md)

## **OA 审批**

审批中接入连接器，主要能解决以下：[表单加载外部数据源](0021-load-external-source.md)、[表单提交时校验](0022-verification-submission.md)、[表单数据同步到外部系统](0023-synchronize-form-system.md)以及[OA审批场景接入子流程](0024-oa-approval-integration.md)。

如果您有更多的定制化集成诉求，可以通过认证服务商一对一专属服务，解决您更多的定制化集成诉求，[点击提交需求](dingtalk://dingtalkclient/action/open_platform_link?pcLink=dingtalk%3A%2F%2Fdingtalkclient%2Fpage%2Flink%3Furl%3Dhttps%253A%252F%252Fh5.dingtalk.com%252Fdingtalk-da%252Findex.html%253FcorpId%253D%2526ddtab%253Dtrue%2526funnelsource%253Dopen_Connector%2523%252Fopportunity_submit)。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7726786761/p569689.png)

### **操作步骤**

1. [连接器配置](0019-connector-configuration.md)，配置需要使用到的连接器或子流程详情参见[创建连接器](../02-XdgyZifJkr-我的连接/0010-create-connector.md)和[创建连接流](../02-XdgyZifJkr-我的连接/0001-create-a-connection-flow-1.md)。
2. [审批配置](0020-approve-configuration.md)，配置在[表单中使用连接器](0020-approve-configuration.md)或配置在[流程节点中使用连接器](0020-approve-configuration.md)。

### **组件说明**

OA审批常用组件包含基础控件、增强控件和套件：

- OA审批表单设计基础控件部分，详情参见[基础控件](0018-basic-controls.md#db26118465in7)。
- OA审批表单设计增强控件部分，详情参见[基础控件](0018-basic-controls.md#3f1c95af93fo4)。
- OA审批表单设计套件部分，详情参见[套件](0017-oa-approval-kit.md)。

### **应用场景**

借助钉钉连接平台，企业可以打通钉钉审批与钉钉其他官方场景、SaaS应用以及企业内部应用，目前钉钉连接平台包含共40+官方场景和SaaS应用。

> **[!NOTE]**
>
> OA审批场景的接入目前仅支持钉钉专业版，详情请参考[钉钉专业版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fdd-pro-composite-order%2Fpc%2Findex.html%3Fpopup_wnd%3Dtrue%26dd_tab%3Dtrue%26width%3D900%26height%3D600%26title%3D%25E9%2592%2589%25E9%2592%2589%25E6%2595%25B0%25E5%25AD%2597%25E8%25B5%2584%25E4%25BA%25A7%26articleCode%3DDT_GOODS_dingtalkmemberplus%26channel%3Dopenpf_web_devdoc%26corpId%3D${corpId}%26accessoryProduct%3DpaasWithConnector%26tabKey%3DDT_GOODS_dingtalkmemberplus&popup_wnd=true&height=600&width=900)。

#### **场景一：表单加载外部数据源**

- **场景痛点**

  企业内部往往存在多个IT系统，如ERP、CRM等，当员工在钉钉提交表单时，往往需要从外部系统加载数据，如提交订单时从CRM加载客户列表、从ERP加载价目表等。在使用系统集成之前，员工往往需要在系统间手动拷贝数据，这不光降低了办公效率，同时带来了业务数据不一致的风险。
- **解决方案**

  企业可以在表单上配置表单组件的数据映射规则，表单在加载时可以基于集成器的规则进行数据自动填充，这样既提高了表单输入效率，也降低了由于误输入导致的业务数据不一致的风险。

  > **[!NOTE]**
  >
  > 如需了解更多，可查看[表单加载外部数据源](0021-load-external-source.md)操作手册介绍。

  ![表单自动填充](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1639771461/p380896.png)

### 场景二：表单提交时校验

- **场景痛点**

  当员工提交预算、订单类审批单时，往往需要在财务系统查询预算或者在供应链系统查询库存，在使用系统集成之前，管理员需要将第一个审批人设置成财务或者仓库管理员，这无疑给员工增加了负担，并降低了流程执行效率。
- **解决方案**

  企业可以配置表单提交时的数据校验规则，员工在提交表单时，集成器会连接外部系统进行预算、库存类校验，并可以定制化提示文案。

  > **[!NOTE]**
  >
  > 如需了解更多，可查看[表单提交时校验](0022-verification-submission.md)操作手册介绍。

  ![表单提交校验](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1639771461/p380897.png)

### 场景三：表单数据同步到外部系统

- **场景痛点**

  当员工在钉钉完成审批后，有时需要将审批单同步到外部系统，比如在出库审批单通过以后在ERP系统生成出库单。在使用系统集成之前，企业有两种方式实现数据同步：

  - 通过开放接口接收审批数据回调，通过自定义开发将审批单数据转换成ERP表单数据。
  - 手动同步。

  其中开放接口方案开发成本较高，且审批单数据变更以后，相关代码需要同步变更。手动同步的方式效率较低，且存在人为失误的风险。
- **解决方案**

  企业可以在审批流添加集成器节点，并通过配置化方式自定义需要同步到外部系统的数据，当审批流执行到该节点时，可以按照映射规则向外部系统同步数据。

  > **[!NOTE]**
  >
  > 如需了解更多，可查看[表单数据同步到外部系统](0023-synchronize-form-system.md)操作手册介绍。

  ![数据同步](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1639771461/p380899.png)

### **场景四：OA审批接入子流程**

- **场景痛点**

  OA审批场景下不支持编排和表达式，无法对官方和三方连接器的返回结果进行改造，使得返回结果不是所需要的内容。如获取智能人事员工花名册中岗位职级信息，返回结果是["P7"]。

  ![OA审批场景接入集成流痛点 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576616661/p506067.png)
- **解决方案**

  在连接平台通过子流程方式，对官方或三方连接器的执行动作出参进行改造，OA审批场景下直接引用发布后的子流程。如获取智能人事员工花名册中岗位职级信息，返回结果是P7。

  > **[!NOTE]**
  >
  > 如需了解更多，可查看[OA审批场景接入子流程](0024-oa-approval-integration.md)操作手册介绍。

  ![OA审批场景接入集成流解决方案 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0576616661/p506068.png)

### **使用教程**

- [OA审批附件同步到知识库](0025-oa-approval-attachment-is-synchronized-to-the-knowledge-base.md)

## **工作通知**

工作通知消息是以某个应用的名义推送到员工的工作通知消息，例如生日祝福、入职提醒等。可以发送文本、语音、链接等，消息类型和样例可参考消息类型与数据格式。

在连接平台，你可以使用【工作通知】官方连接器来给员工发送通知，可以是文本、语音、链接、卡片、图片等。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

#### **发送工作通知**

如果需要发送工作通知，可以通过【工作通知】下的执行动作来发送不同类型的通知：

可以通过以下执行动作发送任何类型的工作通知，包括文本、语音、链接、卡片、图片等。由于可以发送所有类型的通知，其参数设置会比较复杂，因此建议通过下面特定场景的工作通知发送。

| **模块** | **核心能力** |
| --- | --- |
| 文本消息 | 发送纯文本工作通知，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| 图片消息 | 发送图片工作通知，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| Markdown 消息 | 发送 Markdown 格式工作通知，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| OA 消息 | 发送 OA 样式工作通知（支持状态栏更新），更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| 链接消息 | 发送带链接的工作通知，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| 语音消息 | 发送语音工作通知，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| 文件消息 | 发送文件附件工作通知，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |
| 卡片消息 | 发送整体跳转/横排多按钮/竖排多按钮 ActionCard 消息，更多信息查看[发送工作通知](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0769-asynchronous-sending-of-enterprise-session-messages.md)接口介绍。 |

#### **操作已发送的工作通知**

工作通知发送后可能需要对工作通知的一些状态进行获取，可以使用【消息通知】连接器下的相应的执行动作：

| **模块** | **核心能力** |
| --- | --- |
| 获取发送进度 | 查看工作通知消息的发送进度，更多信息查看[获取工作通知消息的发送进度](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0772-obtain-the-sending-progress-of-asynchronous-sending-of-enterprise-session.md)接口介绍。  **[!NOTE]**  只能获取24小时内工作通知消息的发送进度。 |
| 更新状态栏 | 针对 OA 消息，更改 OA 消息状态栏，更多信息查看[更新工作通知状态栏](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0771-update-work-notification-status-bar.md)接口介绍。  **[!NOTE]**  只能更新24小时内发出的OA工作通知状态栏。 |
| 撤回消息 | 撤回已发送的工作通知消息，更多信息查看[撤回工作通知消息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0770-notification-of-work-withdrawal.md)接口介绍。  **[!NOTE]**  只能撤回24小时内发送的工作通知消息。 |
| 获取发送结果 | 获取哪些员工没有发送成功及失败原因，更多信息查看[获取工作通知消息的发送结果](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0773-gets-the-result-of-sending-messages-asynchronously-to-the-enterprise.md)接口介绍。  **[!NOTE]**  只能获取24小时内工作通知消息的发送结果。 |

### **使用教程**

- [发送工作通知文本消息](0026-send-notification-message.md)

## **消息通知**

消息通知是以企业的名义推送到企业内部群，例如生日祝福、入职提醒等。可以发送文本、语音、链接等。

在连接平台，你可以使用【消息通知】官方连接器来给员工发送通知，可以是文本、语音、链接、卡片、图片等。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 文本消息 | 发送纯文本消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| 图片消息 | 发送图片消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| Markdown 消息 | 发送 Markdown 格式消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| OA 消息 | 发送 OA 样式消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| 链接消息 | 发送带链接的消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| 语音消息 | 发送语音消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| 文件消息 | 发送文件附件消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |
| 卡片消息 | 发送卡片消息到企业群，更多信息查看[发送消息到企业群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1490-send-group-messages.md)接口介绍。 |

### **使用教程**

- [发送文本消息到企业群](0027-send-message-enterprise.md)

## **智能人事**

钉钉智能人事提供了强大、灵活、安全的人事解决方案，让企业迅速建立起来员工花名册，搭建员工入职、转正、调岗、离职流程，并给员工良好的使用体验。

在连接平台，你可以使用【智能人事】连接器完成组织内部人员花名册数据的查询和更新。

### **触发事件**

| **消息类型** | **触发条件** |
| --- | --- |
| 人事档案变动 | 当组织内部发生人事相关信息的变动时触发（如入职、转正、调岗、离职等），更多信息查看[人事档案变动](../../01-应用开发/04-LFcRvVD08N-事件订阅/0146-personnel-file-change.md)事件介绍。 |

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

#### **花名册数据管理**

智能人事花名册是组织在钉钉上记录的有关人力资源存档备查的档案，包括系统信息、基本信息、工作信息、个人信息、学历信息、银行卡信息、合同信息、紧急联系人信息、家庭信息、个人材料等。

| **模块** | **核心能力** |
| --- | --- |
| 获取花名册元数据 | 获取员工花名册的元数据定义（包括花名册分组、字段定义），更多信息查看[获取花名册元数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0937-intelligent-personnel-roster-metadata-query.md)接口介绍。 |
| 获取员工花名册字段信息 | 获取员工花名册字段信息，更多信息查看[获取员工花名册字段信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0939-api-getemployeerosterbyfield.md)接口介绍。 |
| 获取花名册字段组详情 | 提供给 ISV 查询花名册的员工档案信息中有权限的字段列表，更多信息查看[获取花名册字段组详情](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0938-get-roster-field-group-details.md)接口介绍。 |
| 更新员工花名册信息 | 更新员工花名册信息，更多信息查看[更新员工花名册信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0940-intelligent-personnel-update-employee-file-information.md)接口介绍。 |

#### **员工管理**

组织内部员工状态可以分为：待入职，在职，离职等：

- 对于待入职员工，可以添加待入职的信息。
- 对于在职员工，可以查询在职员工的列表信息
- 对于离职员工，可以查询离职员工的列表信息，离职员工的离职详情，修改员工的离职信息。

| **模块** | **核心能力** |
| --- | --- |
| 待入职员工 | 添加待入职员工信息，获取待入职员工列表，更多信息查看[添加待入职员工](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0945-add-employees-to-be-hired-supports-system-and-custom-fields.md)相关接口介绍。 |
| 在职员工 | 获取在职员工列表，更多信息查看[获取在职员工列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0946-intelligent-personnel-query-the-list-of-on-the-job-employees-of-the.md)接口介绍。 |
| 离职员工 | 获取离职员工列表，获取离职员工信息，修改员工最后一次离职信息，更多信息查看[获取离职员工列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0947-obtain-the-list-of-employees-who-have-left.md)相关接口介绍。 |

### **使用教程**

- [获取智能人事员工花名册信息并填充到OA表单](0028-obtain-roster-information.md)

## **待办事项**

待办是钉钉的一个协同办公产品，帮助企业员工更高效的进行事项（工作任务）管理。钉钉待办提供了强大的开放能力，各类业务系统或企业自建应用可低成本的接入。更多介绍请查看[钉钉产品使用手册-待办](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/Y7kmb7Dd340Y3GLq?dontjump=true%23%23)。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 新增待办任务 | 为用户创建一个钉钉待办任务，更多信息查看[创建钉钉待办任务](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0793-add-dingtalk-to-do-task.md)接口介绍。 |
| 更新待办任务 | 根据任务 ID，更新钉钉待办任务信息，更多信息查看[更新钉钉待办任务](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0796-updates-dingtalk-to-do-tasks.md)接口介绍。 |
| 删除待办任务 | 根据任务 ID，删除钉钉待办任务，更多信息查看[删除钉钉待办任务](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0795-delete-dingtalk-to-do-tasks.md)接口介绍。 |
| 获取待办详情 | 根据任务 ID 或 sourceId，获取钉钉待办任务详情信息，参数请查看下方参数说明介绍。 |
| 查询待办列表 | 获取该授权企业下某用户的待办列表，更多信息查看[查询企业下用户待办列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0798-query-the-to-do-list-of-enterprise-users.md)接口介绍。 |

### **参数说明**

- **获取钉钉待办任务详情**

  | 名称 | 类型 | 必填 | 描述 |
  | --- | --- | --- | --- |
  | userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
  | accessKey | String | 否 | 应用AccessKey：  - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
  | appType | String | 否 | 应用类型：  - ORG：组织 - ISV：三方 |
  | taskId | String | 是 | 待办ID。 |
- **根据sourceId获取钉钉待办任务详情**

  | 名称 | 类型 | 必填 | 描述 |
  | --- | --- | --- | --- |
  | userId | String | 是 | 当前访问资源所归属用户ID，和创建者ID保持一致。 |
  | accessKey | String | 否 | 应用AccessKey：  - 企业内部应用，填写应用的appKey - 第三方企业应用，填写应用suiteKey |
  | appType | String | 否 | 应用类型：  - ORG：组织 - ISV：三方 |
  | sourceId | String | 是 | 待办业务来源sourceId。  **[!NOTE]**  sourceId为创建待办时传入的sourceId。 |

## **应用管理**

应用管理是钉钉提供的开放能力之一，用于获取企业内部应用的基础信息、对企业内部应用-网页应用的管理，例如创建应用、删除应用、设置应用的可使用范围等。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 获取应用列表 | 获取企业所有应用的信息，包括应用名称、应用描述、应用图标、应用访问地址等，更多信息查看[获取应用列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0864-obtains-a-list-of-all-enterprise-applications.md)相关接口介绍。  **[!NOTE]**   - 如果是企业主管理员，在企业管理后台-应用管理列表页，可以查看到所有的应用信息。 - 如果是企业子管理员，必须同时拥有全部应用管理权限，在企业管理后台-应用管理列表页，可以查看所有应用的信息。 |
| 设置应用可见范围 | 设置指定应用的可见范围（支持企业内部应用-网页应用、小程序应用），更多信息查看[更新企业内部应用的可使用范围](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0871-update-the-visible-range-of-micro-applications.md)接口介绍。  **[!NOTE]**  企业内部应用-网页应用：   - 当前网页应用是开发版本，调用本接口可指定网页应用开发版本的可见范围。 - 当前网页应用是线上版本，调用本接口可指定网页应用线上版本的可见范围。   企业内部应用-小程序应用：   - 仅在小程序线上版本适用。 |
| 获取应用可见范围 | 根据应用 agentId 参数，获取应用的可见范围，更多信息查看[获取企业内部应用的可使用范围](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0872-obtains-the-application-visible-range.md)接口介绍。 |
| 获取员工可见应用列表 | 根据用户 ID，查询用户可见的应用列表，更多信息查看[获取用户可见的企业应用列表](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0866-obtains-the-list-of-enterprise-applications-visible-to-a-user.md)接口介绍。 |

## **数据目录**

数据开放目录是钉钉官方统一的归类入口，方便用户查询和申请数据服务，提高效率。目录中包含钉钉官方统计数据和行业化数据服务，例如直播、考勤、IM等数据服务。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

#### 办公协作数据

| **模块** | **核心能力** |
| --- | --- |
| 单聊统计 | 沟通互动率、聊天消息数、聊天用户数、单聊消息数、单聊用户数、人均发送消息数。更多信息查看[获取企业单聊统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1783-queries-the-statistics-on-one-time-enterprise-chats.md)接口介绍。 |
| 群聊统计 | 群聊用户数、群聊消息数、活跃群数、新增群数、内部群数量、部门群数量。更多信息查看[获取企业群聊统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1784-obtain-enterprise-group-chat-statistics.md)接口介绍。 |
| DING 发送统计 | 发送 DING 次数、发送应用/短信/电话 DING 次数及人数。更多信息查看[获取企业DING发送统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1801-obtain-sending-statistics-of-an-enterprise-ding.md)接口介绍。 |
| DING 接收及评论统计 | 接收 DING 次数、接收应用/短信/电话 DING 次数。更多信息查看[获取企业DING接收及评论统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1803-obtain-statistics-on-receiving-and-comments-of-enterprise-ding.md)接口介绍。 |

#### 会议与直播数据

| **模块** | **核心能力** |
| --- | --- |
| 电话会议统计 | 发起次数、成功发起次数、发起用户数、成功参与人数、会议时长（分钟）。  更多信息查看[获取企业电话会议统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1796-get-enterprise-teleconference-statistics.md)相关接口介绍。 |
| 视频会议统计 | 发起次数、发起用户数、成功发起次数、参与用户数、成功参与用户数、参与人次、会议时长（分钟）。更多信息查看[获取企业视频会议统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1797-get-enterprise-video-conference-statistics.md)接口介绍。 |
| 群直播统计 | 成功发起次数、观看次数、观看人数、直播时长（分钟）、看直播人数、回看次数、回看人数。更多信息查看[获取企业群直播统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1793-obtains-the-live-stream-statistics-for-an-enterprise-group.md)接口介绍。 |

#### 考勤与人事数据

| **模块** | **核心能力** |
| --- | --- |
| 考勤统计 | 应出勤人数、实际出勤人数、出勤率。更多信息查看[获取企业考勤统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1790-queries-enterprise-attendance-statistics.md)相关接口介绍。 |
| 签到统计 | 签到次数、签到用户数。更多信息查看[获取企业签到统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1788-queries-enterprise-check-in-statistics.md)接口介绍。 |
| 员工类型统计 | 全职人数、正式/试用/兼职/劳务外包/待离职/实习/劳务派遣/退休返聘/离职/试岗人数、资料不完整人数。更多信息查看[获取企业员工类型统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1800-obtains-statistics-on-employee-types.md)接口介绍。 |
| 用户激活状态统计 | 累计激活人数、激活率。更多信息查看[获取企业用户激活状态统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1802-obtains-statistics-on-user-activation-status.md)接口介绍。 |

#### 审批与待办数据

| **模块** | **核心能力** |
| --- | --- |
| 审批统计 | 累计审批模板数、累计自定义审批模板数、新建自定义模板数、提交审批单数、提交审批用户数、活跃审批模板数、操作审批次数和用户数。更多信息查看[获取企业审批统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1791-obtains-enterprise-approval-statistics.md)相关接口介绍。 |
| 待办统计 | 待办用户数。更多信息查看[获取企业待办统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1779-obtains-the-to-do-statistics-of-an-enterprise.md)接口介绍。 |

#### 内容与文档数据

| **模块** | **核心能力** |
| --- | --- |
| 文档统计 | 创建文档数、编辑文档数、分享文档数、阅读文档数。更多信息查看[获取企业文档统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1787-get-enterprise-document-statistics.md)相关接口介绍。 |
| 公告统计 | 公告已读人数、公告已接收人数、发布公告数。更多信息查看[获取企业公告统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1789-queries-corporate-announcement-statistics.md)接口介绍。 |
| 日志统计 | 发送日志数、发送日志用户数、评论日志用户数。更多信息查看[获取企业日志统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1785-obtain-enterprise-log-statistics.md)接口介绍。 |
| 钉盘统计 | 钉盘用户数、钉盘上传文件数、钉盘预览文件数。更多信息查看[获取企业钉盘统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1781-obtains-the-statistics-on-enterprise-dingtalk-trays.md)接口介绍。 |

#### 邮件与红包数据

| **模块** | **核心能力** |
| --- | --- |
| 邮箱统计 | 钉邮操作次数、发送/转发/回复操作次数及用户数。更多信息查看[获取企业邮箱统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1786-queries-enterprise-email-statistics.md)相关接口介绍。 |
| 发送红包统计 | 发送红包数、发送拼手气/专享红包数、发送红包用户数、发送拼手气/专享红包用户数。更多信息查看[获取企业发红包统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1792-obtains-the-statistics-on-red-packets-issued-by-enterprises.md)接口介绍。 |
| 接收红包统计 | 接收红包数、接收拼手气/专享红包数、接收红包用户数、接收拼手气/专享红包用户数。更多信息查看[获取企业接收红包统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1798-queries-the-red-envelope-receiving-statistics-of-an-enterprise.md)接口介绍。 |

#### 日程与组织数据

| **模块** | **核心能力** |
| --- | --- |
| 日程统计 | 日程用户数、发起日程用户数、接收日程用户数。更多信息查看[获取企业日程统计数据](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1780-queries-enterprise-schedule-statistics.md)相关接口介绍。 |
| 数字区县组织信息 | 通讯录录入手机人数、通讯录人数、激活人数、激活率、活跃人数、户数、一户一钉户数、一户至少激活一人率。更多信息查看[获取数字区县组织信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/1782-querydigitaldistrictorginfo-api-reference.md)接口介绍。 |

## **会话管理**

会话管理是钉钉通过开放多样的方式根据业务的需要创建、设置和管理群以及群内的成员，还可以为用户提供基于具体业务场景下的群内服务，将沟通和协同融合起来，让组织成员在群聊中通过丰富的群能力实现高效的、结构化的、明确的协作和沟通，提高协同办公效率。

### **执行动作**

> **[!NOTE]**
>
> 各模块下的具体接口参数、请求示例、返回结构等详细信息，请前往接口文档页面查阅。

| **模块** | **核心能力** |
| --- | --- |
| 创建场景群 | 根据业务场景创建专属群聊，更多信息查看[创建场景群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0746-create-a-scene-group.md)接口介绍。 |
| 更新场景群 | 更新场景群的基本信息（如群名称、群头像等），更多信息查看[更新场景群](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0747-api-updatescenegroup.md)接口介绍。 |
| 新增群成员 | 向场景群中添加成员，更多信息查看[添加群成员](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0749-api-addscenegroupmember.md)接口介绍。 |
| 删除群成员 | 从场景群中移除成员，更多信息查看[删除群成员](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0750-api-removescenegroupmember.md)接口介绍。 |
| 停用群模板 | 停用已启用的群模板，更多信息查看[停用群模板](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0760-disable-a-group-template.md)接口介绍。 |
| 获取场景群成员 | 查询场景群中的成员列表，更多信息查看[查询群成员](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0751-query-group-members.md)接口介绍。 |
| 查询场景群基本信息 | 获取场景群的基本信息（如群 ID、群名称、创建时间等），更多信息查看[查询群信息](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0755-queries-the-basic-information-of-a-scenario-group.md)接口介绍。 |

### **使用教程**

- [创建场景群](0029-create-scene-group.md)
