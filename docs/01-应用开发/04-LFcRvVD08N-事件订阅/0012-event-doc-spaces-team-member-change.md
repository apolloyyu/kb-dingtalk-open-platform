---
title: "文档知识库中小组成员变更"
source_url: "https://open.dingtalk.com/document/development/event-doc-spaces-team-member-change"
namespace: "development"
slug: "event-doc-spaces-team-member-change"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "协同 > 文档 > 文档知识库中小组成员变更"
doc_id: "TMbs7Kq4T2"
updated_at: "2025-08-27 16:10:52"
---

> Source: https://open.dingtalk.com/document/development/event-doc-spaces-team-member-change
> Path: 应用开发 / 事件订阅 / 协同 > 文档 > 文档知识库中小组成员变更
> Updated: 2025-08-27 16:10:52

# 文档知识库中小组成员变更

## 事件信息

| 名称 | 值 |
| --- | --- |
| 中文名称 | 文档知识库中小组成员变更 |
| 英文名称 | doc\_spaces\_team\_member\_change |

## 功能描述

文档知识库中小组成员变更事件数据说明。

## 支持应用类型

| 应用类型 | Stream模式推送 | HTTP推送 | SyncHTTP/RDS推送 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 支持 | 不支持 |

## 事件体描述

Stream模式推送

### 字段说明

- `eventUnifiedAppId`（String，必填）：统一应用身份Id。
- `eventCorpId`（String）：事件所属的corpId。
- `eventType`（String）：事件类型。
- `eventId`（String）：事件的唯一Id。
- `eventBornTime`（Long）：事件生成时间。
- `data`（object）：事件体data。
- `data.unionId`（string）：事件操作人unionId。
- `data.teamId`（string）：小组id。
- `data.roleCode`（string）：当前成员的角色：  
  - 1：只读成员  
  - 2：只读成员（可下载）  
  - 3：成员  
  - 4：管理员  
  - 5：所有者
- `data.member`（object）：变更的成员信息，具体字段见下文变更成员字段说明。
- `data.member.memberName`（string）：成员名称。
- `data.member.memberType`（string）：变更的成员类型：  
  - USER：用户  
  - CONVERSATION：群  
  - ORG：组织  
  - DEPT：部门
- `data.member.memberId`（string）：变更的成员id。  
  > 类型是USER，memberId是用户的 unionId。
- `data.type`（string）：类型：  
  - TEAM\_MODIFY\_MEMBER：修改成员  
  - TEAM\_ADD\_MEMBER：添加成员  
  - TEAM\_REMOVE\_MEMBER：移除成员

### **事件体示例**

```
{
  "eventUnifiedAppId": "bbb381b6-f01xxxxx58daac",
  "eventCorpId": "ding9f50b15bxxxx16741",
  "eventType": "doc_spaces_team_member_change",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "eventBornTime": 1683533823336,
  "data": {
    "unionId": "h3ZErk0**giEiE",
    "teamId": "YRB****4Jm",
    "roleCode": "3",
    "member": {
      "memberName": "小钉",
      "memberType": "USER",
      "memberId": "KPfmZAt****giEiE"
    },
    "type": "TEAM_ADD_MEMBER"
  }
}
```

HTTP推送

### 字段说明

- `EventType`（String）：事件英文名称。
- `EventTime`（Long）：事件发生的时间。
- `CorpId`（String）：企业corpId。
- `BizId`（String）：无业务意义，幂等。
- `eventId`（String）：事件的唯一Id。
- `unionId`（string）：事件操作人unionId。
- `teamId`（string）：小组id。
- `roleCode`（string）：当前成员的角色：  
  - 1：只读成员  
  - 2：只读成员（可下载）  
  - 3：成员  
  - 4：管理员  
  - 5：所有者
- `member`（object）：变更的成员信息，具体字段见下文变更成员字段说明。
- `member.memberName`（string）：成员名称。
- `member.memberType`（string）：变更的成员类型：  
  - USER：用户  
  - CONVERSATION：群  
  - ORG：组织  
  - DEPT：部门
- `member.memberId`（string）：变更的成员id。  
  > 类型是USER，memberId是用户的 unionId。
- `type`（string）：类型：  
  - TEAM\_MODIFY\_MEMBER：修改成员  
  - TEAM\_ADD\_MEMBER：添加成员  
  - TEAM\_REMOVE\_MEMBER：移除成员

### **事件体示例**

```
{
  "EventType": "doc_spaces_team_member_change",
  "EventTime": 1663143335567,
  "CorpId": "ding9f50b15bxxxx16741",
  "BizId": "1663**35567",
  "eventId": "c7c7120f2c07419**ebdba0318c8",
  "unionId": "h3ZErk0**giEiE",
  "teamId": "YRB****4Jm",
  "roleCode": "3",
  "member": {
    "memberName": "小钉",
    "memberType": "USER",
    "memberId": "KPfmZAt****giEiE"
  },
  "type": "TEAM_ADD_MEMBER"
}
```
