---
title: "事件订阅总览"
source_url: "https://open.dingtalk.com/document/development/org-event-overview"
namespace: "development"
slug: "org-event-overview"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "事件订阅总览"
doc_id: "XfFwKhqxhk"
updated_at: "2026-09-01 09:16:14"
---

> Source: https://open.dingtalk.com/document/development/org-event-overview
> Path: 应用开发 / 事件订阅 / 事件订阅总览
> Updated: 2026-09-01 09:16:14

# 事件订阅总览

## **身份与免登**

| **名称** | **描述** |
| --- | --- |
| [套件票据](0006-event-suite-ticket.md) | 数据为第三方企业应用票据最新suiteTicket，定时每5个小时推送一次。 |
| [套件授权](0007-event-org-suite-auth.md) | 数据为企业授权应用的最新状态，套件授权事件表示企业授权第三方企业应用。 |
| [企业授权变更事件](0008-event-org-suite-relieve.md) | 数据为企业授权应用的最新状态，企业授权变更事件表示企业变更第三方企业应用的授权范围。 |
| [企业解除套件授权](0009-enterprise-release-kit-authorization.md) | 企业解除套件授权事件，解除第三方企业应用授权时推送。 |

## **协同**

### **文档**

| **名称** | **描述** |
| --- | --- |
| [文档知识库中创建小组](0010-event-doc-spaces-create-team.md) | 文档知识库中创建小组的推送数据。 |
| [文档知识库中小组变更](0011-event-doc-spaces-team-change.md) | 文档知识库中变更小组的推送数据。 |
| [文档知识库中小组成员变更](0012-event-doc-spaces-team-member-change.md) | 文档知识库中小组成员变更的推送数据。 |
| [文档导出任务完成事件](0013-events-doc-export-completed.md) | 当文档导出任务状态发生变更的推送数据。 |

### **签到**

| **名称** | **描述** |
| --- | --- |
| [用户签到](0014-event-check-in.md) | 用户签到的推送数据。 |

### **存储**

| **名称** | **描述** |
| --- | --- |
| [文件更新](0015-event-storage-dentry-update.md) | 文件或文件夹更新事件数据。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。 |
| [文件或文件夹删除](0016-event-storage-dentry-delete.md) | 文件或文件夹删除事件。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。 |
| [文件或文件夹添加](0017-event-storage-dentry-create.md) | 文件或文件夹添加事件数据。如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与接口配合使用，接口详情参见[订阅文件变更事件](https://open.dingtalk.com/document/orgapp/subscribe-to-file-change-events)。 |

### **日程**

| **名称** | **描述** |
| --- | --- |
| [日程变更](0018-event-calendar-event-change.md) | 用户日程发生变更的推送数据。 |

### **公告**

| **名称** | **描述** |
| --- | --- |
| [公告发送](0019-events-blackboard-sent.md) | 发送公告的事件数据。 |

### **项目管理**

| **名称** | **描述** |
| --- | --- |
| [Teambiton工时变更事件](0020-event-project-worktime-updated.md) | 当Teambiton项目中工时属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中工时属性内容的变更推送给开发者，用于监听项目中工时属性更新的信息。 |
| [Teambiton项目变更事件](0021-teambiton-project-change-event.md) | 当Teambiton项目本身发生变更时，钉钉通过事件订阅的方式将对应的项目本身的变更内容推送给开发者，用于监听项目变更信息。 |
| [Teambition项目更新事件](0026-teamposition-project-update-event.md) | 当Teambiton项目属性发生更新操作时，钉钉通过事件订阅的方式将对应的项目属性的更新推送给开发者，用于监听项目属性更新信息。 |
| [Teambition应用变更事件](0023-teamposition-application-change-event.md) | 当Teambiton项目应用发生变更时，钉钉通过事件订阅的方式将项目应用变更内容推送给开发者，用于监听Teambiton项目应用变更信息。 |
| [Teambition成员变更事件](0022-teamposition-member-change-event.md) | 当Teambiton项目成员发生变更时，钉钉通过事件订阅的方式将项目成员变更内容推送给开发者，用于监听Teambiton项目成员变更信息。 |
| [Teambition任务更新事件](0025-teamposition-task-update-event.md) | 当Teambiton项目中任务属性内容发生更新时，钉钉通过事件订阅的方式将对应的项目中任务属性内容的变更推送给开发者，用于监听项目中任务属性更新的信息。 |
| [Teambition项目任务变更事件](0024-teamposition-project-task-change-event.md) | 当Teambiton项目中任务本身发生变更时，钉钉通过事件订阅的方式将对应的项目中任务本身发生的变更内容推送给开发者，用于监听项目中任务变更信息。 |

## **办公**

### **待办**

| **名称** | **描述** |
| --- | --- |
| [待办任务新增](0027-event-todo-task-create.md) | 当用户发起一个钉钉待办任务时，会触发待办任务新增事件。 |
| [待办任务更新](0028-event-todo-task-update.md) | 当用户更新待办任务状态，变更执行者和参与者以及参与者的执行状态变更时，触发待办任务更新事件。 |
| [待办任务删除](0029-event-todo-task-delete.md) | 删除钉钉待办任务信息时，会触发待办任务删除事件。 |

### **钉工牌**

| **名称** | **描述** |
| --- | --- |
| [钉工牌核验事件](0030-event-ding-badge-verify.md) | 钉工牌扫码核验事件。 |
| [批量支付消息通知](0031-event-open-batch-trade-callback.md) | 批量支付完成事件回调。 |
| [企业金融用户协议回调事件](0032-event-open-user-agreement-callback.md) | 用户代扣签解约事件回调。 |

### **OA审批**

| **名称** | **描述** |
| --- | --- |
| [审批实例状态变更](0033-event-workflow-instance-change-broadcast.md) | 针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。 |
| [审批任务状态变更](0034-event-workflow-task-change-broadcast.md) | 针对已授权的审批模板，触发该审批单相应实例、任务状态变更后，会给已授权的ISV推送回调。 |
| [审批实例状态变更](0035-event-workflow-instance-change-directed.md) | 用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。 |
| [审批任务状态变更](0036-event-workflow-task-change-directed.md) | 用户在钉钉侧或三方通过API触发相应实例、任务状态变更后，会给对应归属的ISV应用定向推送回调。 |
| [OA限时审批事件变更](0037-events-oa-timeout-plugin-task-msg.md) | OA限时审批事件，在OA限时审批插件通知相应人员的时候，同时推送给客户业务系统，用于客户业务系统处理内部业务逻辑。 |
| [审批模板状态变更](0040-events-workflow-form-change.md) | OA审批表单模板变更事件，用户在OA审批管理后台操作模板变更后，同时推送给客户业务系统，用于客户业务系统处理内部业务逻辑。 |
| [审批实例开始、结束、终止、删除](0039-event-bpms-instance-change.md) | 审批实例开始、结束的推送数据。 |
| [审批任务开始，结束，转交](0038-event-bpms-task-change.md) | 审批任务开始、结束、转交的推送数据 |

## **通讯录**

### **用户管理**

| **名称** | **描述** |
| --- | --- |
| [用户激活信息](0041-user-activation-information.md) | 企业内部用户变更事件。 |
| [通讯录用户更改](0042-address-book-user-change.md) | 通讯录用户更改的推送数据。 |
| [通讯录用户离职](0043-address-book-user-resignation.md) | 通讯录用户离职的推送数据。 |
| [通讯录用户被设为管理员](0044-user-is-set-as-administrator.md) | 通讯录用户被设为管理员的推送数据。 |
| [通讯录用户被取消设置管理员](0045-address-book-user-canceled-setting-administrator.md) | 通讯录用户被取消设置管理员的推送数据。 |

### **部门管理**

| **名称** | **描述** |
| --- | --- |
| [通讯录企业部门创建](0046-create-department-event.md) | 通讯录企业部门创建的推送数据。 |
| [通讯录企业部门修改](0047-address-book-enterprise-department-modification.md) | 通讯录企业部门修改的推送数据。 |
| [通讯录企业部门删除](0048-address-book-enterprise-department-delete.md) | 通讯录企业部门删除的推送数据。 |

### **角色管理**

| **名称** | **描述** |
| --- | --- |
| [员工角色信息发生变更](0052-employee-role-information-changes.md) | 企业员工角色信息发生变更的推送数据。 |
| [增加角色或者角色组](0049-add-a-role-or-role-group.md) | 增加角色或者角色组的推送数据。 |
| [修改角色或者角色组](0050-modify-a-role-or-role-group.md) | 修改角色或者角色组的推送数据。 |
| [删除角色或者角色组](0051-delete-a-role-or-role-group.md) | 删除角色或者角色组的推送数据。 |
| [员工角色管理范围变更事件](0053-events-emp-label-scope-change.md) | 员工角色管理范围发生变更时，发送这个事件。 |

### **外部联系人**

| **名称** | **描述** |
| --- | --- |
| [外部联系人修改](0054-external-contact-modification.md) | 在授权的第三方企业应用中，企业修改外部联系人的推送信息。 |
| [企业增加外部联系人](0055-enterprise-adds-external-contacts.md) | 在授权的第三方企业应用中，企业增加外部联系人的推送信息。 |
| [企业删除外部联系人](0056-enterprise-delete-external-contacts.md) | 在授权的第三方企业应用中，企业外部联系人删除的推送信息。 |

### **企业管理**

| **名称** | **描述** |
| --- | --- |
| [企业变更](0057-event-subscription-for-enterprise-changes.md) | 在授权的第三方企业应用中，企业信息发生变更的时刻推送。 |
| [企业删除](0058-the-organizational-relationship-enterprise-is-deleted.md) | 企业被解散的推送数据。 |
| [企业增加角色](0059-businesses-increase-roles.md) | 在授权的第三方企业应用中，发生角色的增加的时刻推送。 |
| [企业删除角色](0061-enterprise-deletes-the-role.md) | 在授权的第三方企业应用中，发生角色的删除的时刻推送。 |
| [企业删除员工](0062-enterprise-delete-employee.md) | 企业删除员工推送信息。 |
| [企业角色变更](0060-enterprise-role-change.md) | 在授权的第三方企业应用中，发生角色的修改的时刻推送。 |
| [企业信息发生变更](0065-enterprise-information-changes.md) | 企业信息发生变更的推送数据。 |
| [企业增加员工事件](0063-enterprise-increases-employee-events.md) | 通讯录用户增加的推送数据。 |
| [企业修改员工事件](0064-enterprise-modify-employee-event.md) | 企业内部用户变更事件。 |
| [企业修改员工部门后员工信息事件](0067-employee-information-event-after-enterprise-modifies-employee-department.md) | 在授权的第三方企业应用中，用户所在部门变更的推送信息。 |
| [企业修改员工所在角色后员工信息事件](0068-employee-information-event-after-the-enterprise-modifies-the-employee-s-role.md) | 企业修改员工所在角色(包括管理员变更)事件之后的员工信息。 |
| [加入企业后用户激活](0066-user-activation-after-joining-the-enterprise.md) | 通讯录用户加入企业后用户激活的推送数据。 |

### **通讯录ID转译**

| **名称** | **描述** |
| --- | --- |
| [异步转译通讯录id任务完成通知](0069-asynchronous-translation-address-book-id-task-completion-notification.md) | 企业异步转译通讯录id任务完成，发送的异步转译通讯录事件数据。 |

## **音视频**

### **直播**

| **名称** | **描述** |
| --- | --- |
| [直播状态变更](0074-event-live-status-change-event.md) | 直播状态变更的推送数据。 |
| [直播信息修改](0075-event-live-update-event.md) | 直播信息进行修改的推送数据。 |
| [直播回放观看数据推送](0076-event-live-watch-playback-event.md) | 直播回放观看信息的推送数据。 |
| [直播结束数据处理完成事件](0077-event-live-statistic-done-event.md) | 直播结束数据处理完成的数据推送。 |

### **智能会议室**

| **名称** | **描述** |
| --- | --- |
| [会议室事件](0078-nqrbp8.md) | - 会议室预定成功、取消事件。 - 会议室创建、更新、删除事件。 |
| [设备中控事件](0079-events-open-meeting-room-central-control.md) | 当使用设备中控功能时，钉钉推送的设备状态变化事件。 |

### **视频/音频会议**

| **名称** | **描述** |
| --- | --- |
| [设备属性变更](0080-event-open-meeting-room-device-property-change.md) | 当钉钉视频会议设备属性变更时，钉钉推送的设备属性变更事件内容。 |
| [设备告警事件](0081-event-open-meeting-room-device-alarm.md) | 钉钉视频会议设备发生告警时，钉钉推送的设备告警事件内容。 |
| [钉钉投屏事件](0082-event-dingtalk-projection.md) | 钉钉投屏端发起投屏的推送数据。 |
| [视频会议状态变更](0083-event-meeting-status-change.md) | 视频会议状态变更的推送数据。 |
| [设备绑定会议室变更](0084-event-open-meeting-room-device-bind-change.md) | 当钉钉视频会议设备绑定、解绑钉钉会议室时，钉钉推送的设备绑定会议室变更事件内容。 |
| [视频会议成员状态变更](0085-event-meeting-member-status-change.md) | 视频会议成员状态变更的推送数据。 |
| [视频会议状态变更App定向推送](0086-events-meeting-status-change-target-push.md) | 视频会议状态变更定向推送。 |
| [视频会议成员状态变更App定向推送](0087-events-meeting-member-status-change-target-push.md) | 视频会议成员状态变更定向推送。 |
| [视频会议ASR转写结果开放事件](0088-events-meeting-asr-result-event.md) | 会议中的闪记ASR转写识别结果事件。 |
| [视频会议ASR转写结果开放事件定向推送](0089-asr-transcription-conferences-targeted-event-push.md) | 视频会议云录制、闪记ASR转写识别结果事件，指定App推送。 |
| [闪记状态变更开放事件](0090-flash-memory-status-change-open-event.md) | 音视频会议闪记的开放接口状态同步事件：   - 当摘要已生成后，会发送状态同步事件。 - 当视频转码或合并完成后，发送状态同步事件。 |
| [闪记状态变更定向开放事件](0091-events-flash-minutes-open-event-directed.md) | 音视频会议闪记的开放接口状态同步事件：   - 当摘要已生成后，发送状态同步事件。 - 当视频转码或合并完成后，发送状态同步事件。 |

## **服务窗**

| **名称** | **描述** |
| --- | --- |
| [服务窗关注事件](0070-service-window-event.md) | 用户关注服务窗的推送数据。 |
| [服务窗取关事件](0071-service-window-close-event.md) | 用户取消关注服务窗的推送数据。 |
| [用户信息授权结果](0072-user-information-authorization-result.md) | 用户授权同意或者拒绝的推送数据。 |
| [服务号接收用户交互](0073-service-number-receive-user-interaction.md) | 服务号收到用户的交互事件, 目前只有菜单点击事件。 |

## **服务群**

| **名称** | **描述** |
| --- | --- |
| [服务群群信息变更](0092-event-servicegroup-group-info-change.md) | 服务群群信息变更的推送数据。 |
| [服务群联系人关联客户](0093-event-servicegroup-contact-relate-customer.md) | 服务群联系人关联客户的推送数据。 |
| [服务群入群表单保存](0094-event-servicegroup-contact-join-group-form.md) | 服务群入群表单保存的推送数据。 |
| [服务群自定义表单删除实例](0095-service-group-custom-form-delete-instance.md) | 服务群自定义表单删除实例的推送数据。 |
| [服务群自定义表单更新实例](0096-service-group-custom-form-update-instance.md) | 服务群自定义表单更新实例的推送数据。 |
| [服务群自定义表单创建实例](0097-service-group-custom-form-creation-instance.md) | 服务群自定义表单创建实例的推送数据。 |
| [服务群工单处理反馈](0098-service-group-work-order-processing-feedback.md) | 服务群工单处理反馈的推送数据。 |
| [服务群工单添加备注](0099-service-group-work-order-add-comment.md) | 服务群工单添加备注的推送数据。 |
| [弹内服务群话题变更事件](0100-internal-cloud-service-group-topic-change-event.md) | 服务群话题变更的推送数据。 |
| [服务群工单已读](0101-service-group-work-order-read.md) | 服务群工单已读的推送数据。 |
| [服务群工单创建](0102-service-group-work-order-creation.md) | 服务群工单创建的推送数据。 |
| [服务群工单申领](0103-service-group-work-order-application.md) | 服务群工单申领的推送数据。 |
| [服务群工单催办](0104-service-group-work-order-reminder.md) | 服务群工单催办的推送数据。 |

## **即时通讯**

### **会话管理**

| **名称** | **描述** |
| --- | --- |
| [群会话解散群](0105-group-session-disband-group.md) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。群会话解散事件推送数据说明。 |
| [群会话添加人员](0106-group-session-add-persons.md) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话添加人员事件字段说明。 |
| [群会话删除人员](0107-group-session-delete-persons.md) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话删除人员事件推送数据说明。 |
| [群会话更换群主](0108-group-session-change-group-master.md) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。该文档为群会话更换群主事件字段说明。 |
| [群会话更换群名称](0109-group-session-change-group-name.md) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话更换群名称事件数据说明。 |
| [群会话用户主动退群](0110-group-session-users-actively-withdraw-from-the-group.md) | 开发者监听群回调事件可以更及时地响应群的变化，与业务集成。为群会话删除人员事件推送数据说明。 |
| [群模板被启用或停用](0111-group-templates-are-enabled-or-disabled.md) | 群模板被启用或停用的推送数据。 |

### **机器人**

| **名称** | **描述** |
| --- | --- |
| [机器人消息已读事件](0113-bot-message-read-event.md) | 开发者操作机器人发消息时，机器人消息被读的推送数据。 |
| [机器人消息撤回事件](0112-bot-message-withdrawal-event.md) | 开发者操作机器人发消息时，机器人消息撤回的推送数据。 |

### **酷应用**

| **名称** | **描述** |
| --- | --- |
| [单聊安装酷应用](0114-single-chat-install-cool-app.md) | 单聊安装酷应用的推送数据。 |
| [单聊卸载酷应用](0115-single-chat-uninstall-cool-application.md) | 单聊卸载酷应用的推送数据。 |
| [群内安装酷应用事件](0116-install-cool-application-events-in-the-group.md) | 群内安装酷应用的推送数据。 |
| [群内卸载酷应用事件](0117-uninstall-cool-app-event-in-group.md) | 群内卸载酷应用的推送数据。 |

## **智能硬件**

### **硬件**

| **名称** | **描述** |
| --- | --- |
| [AIoT设备上行事件](0118-events-aiot-device-uplink-event.md) | 设备上行事件。 |

### **DingTalk A1**

| **名称** | **描述** |
| --- | --- |
| [DingTalkA1小助理总结完成事件](0120-events-aone-assistant-summary-change.md) | DingTalkA1小助理执行分析结果事件。 |
| [DingTalkA1小助理状态变更](0119-events-aone-assistant-status-change-1.md) | DingTalkA1小助理状态变更事件。 |
| [A1设备信息变更事件](0121-events-aone-device-info-changed.md) | 当企业内A1设备的设备信息发生变化时，推送该事件。 |
| [A1设备绑定状态变更事件](0122-events-aone-device-bind-changed.md) | 当企业内A1设备的绑定状态发生变化时，推送该事件。 |
| [A1行业版设备绑定状态变更事件](0123-events-aone-industry-device-bind-changed.md) | 当行业版A1设备的绑定状态发生变化时，向三方组织推送该变更事件。 |

## **视听智能服务**

| **名称** | **描述** |
| --- | --- |
| [AI销售管理设备使用人变更事件](0124-events-dvi-device-owner-change.md) | AI销售管理中的设备使用人发生变更时产生的事件。 |
| [智能工牌自定义AI分析项完成事件](0125-events-dvi-custom-ai-analysis-completed.md) | 智能工牌应用中客户自定义的AI分析项分析完成的通知事件。 |
| [DingTalkB1设备状态变更事件](0126-events-badge-device-status-change.md) | DingTalkB1设备状态发生变更事件。 |

## **智能人事**

### **考勤**

| **名称** | **描述** |
| --- | --- |
| [班次变更](0127-intelligent-personnel-shift-change.md) | 考勤班次变更的推送数据。 |
| [考勤组变更](0128-attendance-group-change.md) | 考勤组变更的推送数据。 |
| [员工打卡事件](0129-employee-clock-in-event.md) | 当考勤数据发生员工打卡时，钉钉推送的员工打卡事件数据。 |
| [员工加班事件](0130-employee-overtime-events.md) | 企业内部应用通过考勤接口写入加班，触发加班转调休时，推送的员工加班事件数据。 |
| [水印打卡签到](0131-watermark-punch-in.md) | 水印打卡签到的推送数据。 |
| [考勤结果变更](0132-change-of-attendance-results.md) | 当钉钉管理员修改考勤结果变更时，钉钉通过事件订阅的方式将考勤结果变更内容推送给开发者。 |
| [假期数据同步](0133-holiday-data-synchronization.md) | 企业发生假期相关的数据变更时推送。 |
| [假期消费记录变更](0134-holiday-consumption-record-change.md) | 在授权微应用的企业中，发生假期消费记录(请假数据)增加、修改的时刻推送。 |
| [假期规则变更事件](0135-vacation-rule-change-event.md) | 当假期规则变更时，钉钉通过事件订阅的方式将规则变更内容推送给开发者，规则变更包括：增、删、改。 |
| [手动修改假期余额](0136-manually-modify-the-holiday-balance.md) | 当管理员手动修改假期余额时，钉钉通过事件订阅的方式将规则变更内容推送给开发者。 |
| [考勤日统计变更事件](0137-attendance-day-statistics-change-event.md) | 考勤日统计数据发生变更时，钉钉通过事件订阅的方式将变更内容推送给开发者。 |
| [考勤报表字段变更事件](0138-attendance-report-field-change-event.md) | 当考勤报表字段发生变更（如新增、删除或修改）时，钉钉推送发生变更的字段的信息。 |
| [请假、加班、出差、外出状态变更事件](0139-leave-overtime-business-trip-out-of-office-status-change-events.md) | 当钉钉审批单状态变更时，钉钉通过事件订阅的方式将审批单变更内容推送给开发者，状态变更包括：发起、审批完成、撤销、删除。 |

### **智能招聘**

| **名称** | **描述** |
| --- | --- |
| [招聘业务平台配置变更](0144-event-ats-config-change.md) | 招聘业务平台配置变更事件的相关推送的数据说明。 |
| [招聘渠道消息推送开关](0140-recruitment-channel-message-push-switch.md) | 该事件用于通知与钉钉智能招聘打通的招聘渠道平台，用户在智能招聘侧设置渠道候选人投递简历的通知消息是否通过IM进行推送。 |
| [招聘业务平台权益变更](0141-change-of-rights-and-interests-of-recruitment-business-platform.md) | 招聘高级版权益变更时会发出事件。 |
| [智能招聘人才直通车任务](0142-intelligent-recruitment-talent-through-train-task.md) | 创建人才直通车，仅招聘需求可申请。 |
| [招聘平台职位投递变更事件](0143-recruitment-platform-position-delivery-change-event.md) | 数据为招聘平台职位投递变更事件。 |

### **智能人事**

| **名称** | **描述** |
| --- | --- |
| [人事档案变动](0146-personnel-file-change.md) | 人事档案变动的推送数据。 |
| [人事解决方案变更事件](0147-personnel-solution-change-event.md) | 人事解决方案变更的推送数据。 |
| [人事平台员工异动事件v2](0148-personnel-platform-employee-change-event-v2.md) | 人事平台员工异动的推送数据，异动有入职、转正、调岗、离职和晋升。 |
| [人事商业化方案事件](0149-personnel-commercialization-program-event.md) | 人事商业化方案事件，为人事商业化方案的数据变更时的数据的推送数据。 |
| [培训学习记录同步事件](0150-training-learning-record-sync-events.md) | 培训学习记录同步事件数据。 |
| [智能人事一体化应用授权](0151-intelligent-personnel-integration-application-authorization.md) | 企业将三方应用数据授权给人事主数据平台后的事件通知。 |

## **智能财务**

| **名称** | **描述** |
| --- | --- |
| [智能财务企业信息变更](0152-intelligent-financial-enterprise-information-change.md) | 数据为智能财务企业信息变更相关数据。 |
| [智能财务审批模板变更事件](0153-smart-financial-approval-template-change-event.md) | 当智能财务相关审批模板发生变更时，钉钉会通过事件订阅的方式将审批模板变更的信息推送给开发者，用于监听审批模板变更信息。 |
| [开票申请单关联发票数据变更](0154-invoice-data-associated-with-invoicing-requisition-change.md) | 该事件用于给ISV推送在智能财务侧完成的开票申请单的发票数据，用户ISV配合钉钉侧完成后续业务逻辑。 |
| [智能财务企业多主体信息变更](0155-intelligent-financial-enterprise-multi-subject-information-change.md) | 智能财务的企业主体变更时，会通过该事件通知业务方。 |
| [钉钉智能财务客户信息变更事件](0156-dingtalk-intelligent-financial-customer-information-change-event.md) | 该文档为智能财务的客户变更相关数据。 |
| [钉钉智能财务商品信息变更事件](0157-dingtalk-intelligent-financial-commodity-information-change-event.md) | 当智能财务商品辅助字段发生增删改时，钉钉会通过事件订阅的方式将商品变更的信息推送给开发者，用于监听商品变更信息。 |
| [钉钉智能财务角色成员变更事件](0158-dingtalk-smart-finance-role-member-change-event.md) | 数据为智能财务的角色成员变更事件相关数据。 |
| [钉钉智能财务项目信息变更事件](0159-dingtalk-intelligent-financial-project-information-change-event.md) | 数据为智能财务的项目变更相关数据。 |
| [钉钉智能财务供应商信息变更事件](0160-dingtalk-intelligent-financial-supplier-information-change-event.md) | 数据为智能财务的供应商变更相关数据。 |
| [钉钉智能财务收支类别信息变更事件](0161-dingtalk-intelligent-financial-revenue-and-expenditure-category-information-change-event.md) | 数据为智能财务的收支类别变更相关数据。 |
| [钉钉智能财务自定义档案信息变更事件](0162-dingtalk-intelligent-financial-custom-profile-information-change-event.md) | 数据为智能财务的自定义档案类别信息变更相关数据。 |
| [钉钉智能财务自定义档案数据信息变更事件](0163-dingtalk-intelligent-financial-custom-file-data-information-change-event.md) | 数据为智能财务的自定义档案具体数据信息变更相关数据。 |

## **客户管理**

| **名称** | **描述** |
| --- | --- |
| [主数据实例新增事件](0166-events-ding-paas-object-data-create.md) | 主数据实例新增的推送数据。 |
| [主数据实例删除事件](0167-event-ding-paas-object-data-delete.md) | 主数据实例删除的推送数据。 |
| [主数据实例更新事件](0168-event-ding-paas-object-data-update.md) | 主数据实例更新的推送数据。 |
| [CRM元数据](0164-event-ding-crm-object-meta.md) | 客户管理元数据回调事件，当用户进入客户管理后台编辑并发布客户、联系人、跟进记录表单时会触发推送。 |
| [CRM客户动态](0165-crm-customer-dynamics.md) | CRM客户动态相关信息发生变更时，钉钉通过事件订阅的方式将CRM客户动态相关变更内容推送给开发者。 |

## **Agoal**

| **名称** | **描述** |
| --- | --- |
| [Agoal新增指标事件](0169-events-agoal-indicator-add.md) | 当Agoal管理员在Agoal中新增指标时，会发送事件通知订阅方新增指标的信息。 |
| [Agoal修改指标事件](0170-events-agoal-indicator-modify.md) | 当Agoal管理员在Agoal中修改指标内容时，会发送事件通知订阅方被修改指标的信息。 |
| [Agoal复制指标事件](0171-events-agoal-indicator-copy.md) | 当Agoal管理员在Agoal中复制指标时，会发送事件通知订阅方被复制指标及复制生成的指标信息。 |
| [Agoal删除指标事件](0172-events-agoal-indicator-remove.md) | 当Agoal管理员在Agoal中删除指标时，会发送事件通知订阅方被删除指标的信息。 |
| [Agoal新增目标进展事件](0173-events-agoal-objectiveprogress-add.md) | 当用户在Agoal中新增目标进展时，会发送事件通知订阅方目标进展的信息。 |
| [Agoal修改目标进展事件](0174-events-agoal-objectiveprogress-modify.md) | 当用户在Agoal中修改目标进展时，会发送事件通知订阅方目标进展的信息。 |
| [Agoal删除目标进展事件](0175-events-agoal-objectiveprogress-remove.md) | 当用户在Agoal中删除目标进展时，会发送事件通知订阅方目标进展的信息。 |
| [Agoal新增目标规则事件](0176-events-agoal-objectiverule-add.md) | 当用户在Agoal中新增目标规则时，会发送事件通知订阅方目标规则的信息。 |
| [Agoal修改目标规则事件](0177-events-agoal-objectiverule-modify.md) | 当用户在Agoal中修改目标规则时，会发送事件通知订阅方目标规则的信息。 |
| [Agoal删除目标规则事件](0178-events-agoal-objectiverule-remove.md) | 当用户在Agoal中删除目标规则时，会发送事件通知订阅方目标规则的信息。 |
| [Agoal个人目标删除事件](0179-agoal-personal-goal-deletion-event.md) | 当用户在Agoal中删除个人目标时，会发送事件通知订阅方个人目标的信息。 |
| [Agoal个人目标更新事件](0180-agoal-personal-goal-update-event.md) | 当用户在Agoal中修改个人目标内容或更新进展时，会发送事件通知订阅方个人目标的信息。 |
| [Agoal个人目标新增事件](0181-agoal-personal-goals-have-added-new-events.md) | 当用户在Agoal的员工目标下录入目标时，会发送事件通知订阅方个人目标的信息。 |

## **组织大脑**

| **名称** | **描述** |
| --- | --- |
| [组织大脑人才池新增](0182-events-hrbrain-talent-pool-add.md) | 当组织大脑人才池新增时，会通知订阅方。 |
| [组织大脑人才池编辑](0183-events-hrbrain-talent-pool-edit.md) | 当组织大脑人才池修改时，会通知订阅方。 |
| [组织大脑人才池删除](0184-events-hrbrain-talent-pool-delete.md) | 当组织大脑人才池删除时，会通知订阅方。 |
| [组织大脑人才池人员新增](0185-events-hrbrain-talent-pool-staff-add.md) | 当人才池人员入池时，会通知订阅方。 |
| [组织大脑人才池人员删除](0186-events-hrbrain-talent-pool-staff-delete.md) | 当人才池人员出池时，会通知订阅方。 |

## **企业文化**

| **名称** | **描述** |
| --- | --- |
| [荣誉授予](0187-honor-confer.md) | 授予企业成员荣誉勋章时，推送的荣誉授予事件内容。 |
| [荣誉审核结果](0188-honor-review-results.md) | 荣誉审核结果事件数据。 |

## **应用市场**

| **名称** | **描述** |
| --- | --- |
| [商品操作](0189-commodity-operation.md) | 组织/个人在应用开通后，钉钉后台新增了应用开通记录的回调信息。 |
| [应用市场下单](0190-application-market-order.md) | 数据为企业在钉钉服务市场购买开通应用产生订单时刻，推送的订单信息事件内容。 |
| [市场订单标识](0191-market-order-identification.md) | 市场订单标识事件。 |
| [轻量级商机通知](0192-lightweight-opportunity-notification.md) | 客户触发的进服务群、提交业务需求等轻量级商机触发事件 |
| [应用订单退款事件](0193-apply-order-refund-event.md) | 应用商品订单退款事件。 |
| [钉钉交易订购开启](0194-dingtalk-transaction-ordering-on.md) | 业在应用市场购买商品对应的权益服务开通事件数据。 |
| [钉钉交易订购关闭](0195-dingtalk-transaction-ordering-closed.md) | 服务关闭事件数据。 |
| [一体化应用安装事件](0196-all-in-one-application-installation-events.md) | 一体化应用安装事件。 |
| [市场AI助理下单](0197-events-market-ai-agent-order.md) | 数据为企业在钉钉市场购买开通AI助理产生订单时刻，推送的订单信息事件内容。 |

## **应用管理**

| **名称** | **描述** |
| --- | --- |
| [企业逻辑启用微应用](0198-enterprise-logic-enabled-microapps.md) | 数据为第三方企业应用的最新状态，该事件为当第三方企业应用启用。 |
| [企业逻辑停用微应用](0199-enterprise-logic-deactivates-microapps.md) | 该事件为企业停用第三方企业应用停用的时刻推送的数据。 |
| [企业物理删除微应用](0200-enterprise-physical-deletion-of-micro-applications.md) | 该事件为第三方企业应用第三方企业应用删除。 |
| [企业微应用可见范围变更](0201-enterprise-micro-application-visible-range-change.md) | 该事件为第三方企业应用可见范围变更推送的数据。 |
| [小程序版本发布事件](https://open.dingtalk.com/document/orgapp/event-inner-app-version-publish) | 当开发者在开发者后台操作或者调用开放平台接口对企业内部小程序的开发版本进行体验发布和线上发布，推送的小程序版本发布事件数据。 |
| [小程序版本回滚事件](https://open.dingtalk.com/document/orgapp/event-inner-app-version-rollback) | 开发者在开发者后台操作或者调用开放平台接口对企业内部小程序的历史线上版本进行回滚时，推送的小程序版本回滚事件数据。 |
| [企业内部应用发布](0204-enterprise-self-built-application-release.md) | 当开发者对企业内部应用进行发布时，推送事件相关数据。 |
| [企业内部应用状态变更](0205-enterprise-self-built-application-status-change.md) | 当开发者对企业内部应用进行启用/停用/删除时，推送事件相关数据。 |
| [企业内部应用可使用范围变更](0206-enterprise-self-built-applications-can-be-used-to-change-the-scope.md) | 当开发者对企业内部应用进行可使用范围变更时，推送事件相关数据。 |

## **专属开放**

| **名称** | **描述** |
| --- | --- |
| [服务号接收单聊消息](0209-service-number-receiving-single-chat-message.md) | 服务号收到用户单聊消息的事件,钉钉服务器给开发者推送的事件内容，开发者根据收到的用户消息，结合发消息的接口，实现个性化的自动回复功能。 |
| [企业员工发送文件的检测事件](0211-detection-event-of-enterprise-employee-sending-file.md) | 企业员工发送文件的检测的推送数据。 |
| [专属群扩容审批](0207-exclusive-group-expansion-approval.md) | 群规模扩容审批的推送数据。 |
| [专属钉钉数据迁移](0208-dedicated-dingtalk-data-migration.md) | 专属钉钉数据迁移的推送数据。 |
| [专属可信设备删除推送事件](0210-events-exclusive-delete-trusted-device.md) | 删除专属可信设备时触发该事件。 |

## **行业开放**

### **医疗**

| **名称** | **描述** |
| --- | --- |
| [医疗行业用户属性变动](0213-user-attribute-change-in-medical-industry.md) | 医疗通讯录发生医疗行业用户属性变动时，触发的医疗行业用户属性变动事件推送数据说明。 |
| [医疗行业用户所在科室医疗组变动](0216-changes-in-the-medical-group-of-the-department-where-the.md) | 医疗通讯录发生医疗行业用户所在科室医疗组变动时，医疗行业用户所在科室医疗组变动的数据推送说明。 |
| [医疗行业科室医疗组变动](0214-changes-in-medical-departments-and-medical-groups-in-the-medical.md) | 医疗通讯录发生医疗行业科室医疗组变动时，推送的医疗行业科室医疗组变动事件数据。 |
| [医疗行业科室医疗组属性变动](0215-change-of-attribute-of-medical-group-of-medical-department-in.md) | 医疗通讯录发生医疗行业科室医疗组变动时，推送的医疗行业科室医疗组变动事件数据。 |
| [医疗通讯录全量同步](0212-full-synchronization-of-medical-address-book.md) | 医疗通讯录发生医疗通讯录全量同步时，推送的医疗通讯录全量同步事件数据说明。 |

### **教育**

| **名称** | **描述** |
| --- | --- |
| [教育部门新增](0217-new-education-sector.md) | 家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,edu\_dept\_insert表示部门节点新增事件数据。 |
| [教育部门更新](0218-education-sector-update.md) | 家校通讯录2.0部门信息变更，家校通讯录架构中各个部门发生变更时的信息,edu\_dept\_update为部门节点更新事件数据。 |
| [教育部门删除](0219-education-department-delete.md) | 家校通讯录2.0，部门信息变更。主要包括家校通讯录架构中各个部门发生变更时的信息,该事件为部门节点删除事件数据。 |
| [新教育人员新增](0220-new-education-staff-added.md) | 家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。教育人员新增事件表示在某个班级中人员相关身份新增触发的事件推送的数据。 |
| [新教育人员更新](0221-new-education-staff-update.md) | 家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。教育人员更新事件表示在某个班级中人员相关身份更新触发的事件推送的数据。 |
| [新教育人员删除](0222-new-education-staff-deleted.md) | 家校通讯录2.0，家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系（目前关系只有监护人与学生的关系)。该事件表示在某个班级中人员相关身份删除事件数据。 |
| [新教育人员关系新增](0223-new-education-staff-relations-added.md) | 家校通讯录2.0，人员变更推送。家校通讯录人员变更，主要包括两部分：人员在家校业务场景下的身份以及用户关系。（目前关系只有监护人与学生的关系)。 该事件表示在某个班级中人员关系新增。此事件中各个字段的理解，可以总结为如下一句表达式：在班级${classId}中，${fromUserid}与${toUserid}的关系是 ${relationName}。在家校场景下，fromUserid为监护人，toUserid为学生。此回调事件推送的是最简单的数据。 |
| [新教育人员关系更新](0224-new-education-staff-relationship-update.md) |
| [新教育人员关系删除](0225-new-education-staff-relation-delete.md) |
| [打卡任务更新](0226-events-edu-card-update.md) | 新教育2.0，对已创建且未结束、未删除的打卡任务进行信息更新时，触发此事件的推送。 |
| [打卡任务结束](0227-events-edu-card-end.md) | 新教育2.0，当打卡任务被提前结束时，触发此事件的推送。 |
| [打卡任务删除](0228-events-edu-card-delete.md) | 新教育2.0，组织打卡任务删除事件。当已创建且未结束的打卡任务被删除时，触发此事件的推送。 |
| [支付状态同步](0229-payment-status-synchronization.md) | 为了方便开发者感知用户状态变化，统一支付平台提供了事件推送能力，当前仅支持支付状态同步事件，即当用户订单的支付状态发生变化时，钉钉会通过事件订阅的方式将用户订单的支付状态的变更内容推送给开发者。 |

### **行业通用**

| **名称** | **描述** |
| --- | --- |
| [门店通节点变更事件](0230-store-pass-node-change-event.md) | 门店架构节点变更时的数据推送。 |
| [门店通门店分组事件](0231-stores-through-stores-grouping-events.md) | 门店通门店分组变更的数据推送。 |
| [门店通业务角色变更事件](0232-store-general-business-role-change-event.md) | 业务角色的添加、更新、删除，以及角色对应的人员变更。 |
| [门店通用户权益变更事件](0233-store-general-account-equity-change-event.md) | 门店通用户权益变更事件的推送数据。 |
