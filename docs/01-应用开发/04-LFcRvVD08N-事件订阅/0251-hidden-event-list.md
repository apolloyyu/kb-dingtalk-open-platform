---
title: "事件列表"
source_url: "https://open.dingtalk.com/document/development/hidden-event-list"
namespace: "development"
slug: "hidden-event-list"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > HTTP回调 > 事件列表"
doc_id: "e7wPI1mDam"
updated_at: "2025-10-16 14:31:49"
---

> Source: https://open.dingtalk.com/document/development/hidden-event-list
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > HTTP回调 > 事件列表
> Updated: 2025-10-16 14:31:49

# 事件列表

| 分类 | 回调事件 | 说明 | 支持的应用类型 |
| --- | --- | --- | --- |
| 通讯录事件 | user\_add\_org | 通讯录用户增加。 | 企业内部应用  第三方企业应用 |
| user\_modify\_org | 通讯录用户更改。 |
| user\_leave\_org | 通讯录用户离职。 |
| user\_active\_org | 加入企业后用户激活。 |
| org\_admin\_add | 通讯录用户被设为管理员。 |
| org\_admin\_remove | 通讯录用户被取消设置管理员。 |
| org\_dept\_create | 通讯录企业部门创建。 |
| org\_dept\_modify | 通讯录企业部门修改。 |
| org\_dept\_remove | 通讯录企业部门删除。 |
| org\_remove | 企业被解散。 |
| org\_change | 企业信息发生变更。 |
| label\_user\_change | 员工角色信息发生变更。 |
| label\_conf\_add | 增加角色或者角色组。 |
| label\_conf\_del | 删除角色或者角色组。 |
| label\_conf\_modify | 修改角色或者角色组。 |
| 家校通讯录事件 | edu\_user\_insert | 人员身份新增。 | 企业内部应用 |
| edu\_user\_update | 人员身份更新。 |
| edu\_user\_delete | 人员身份删除。 |
| edu\_user\_relation\_insert | 人员关系新增。 |
| edu\_user\_relation\_update | 人员关系更新。 |
| edu\_user\_relation\_delete | 人员关系删除。 |
| edu\_dept\_insert | 部门节点新增。 |
| edu\_dept\_update | 部门节点更新。 |
| edu\_dept\_delete | 部门节点删除。 |
| 审批事件 | bpms\_task\_change | 审批任务开始，结束，转交。 | 企业内部应用  第三方企业应用 |
| bpms\_instance\_change | 审批实例开始，结束。 |
| 群会话事件 | chat\_add\_member | 群会话添加人员。 | 企业内部应用 |
| chat\_remove\_member | 群会话删除人员。 |
| chat\_quit | 群会话用户主动退群。 |
| chat\_update\_owner | 群会话更换群主。 |
| chat\_update\_title | 群会话更换群名称。 |
| chat\_disband | 群会话解散群。 |
| 签到事件 | check\_in | 用户签到事件。 | 企业内部应用 |
| 考勤事件 | attendance\_check\_record | 员工打卡事件。 | 企业内部应用 |
| attendance\_schedule\_change | 员工排班变更事件。 |
| attendance\_overtime\_duration | 员工加班事件。 |
| 会议室事件 | meetingroom\_book | 会议室预定等事件，预定成功、取消等。 | 企业内部应用 |
| meetingroom\_room\_info | 会议室创建、更新、删除等。 | 企业内部应用 |
