---
title: "会议事件"
source_url: "https://open.dingtalk.com/document/development/video-conference-events"
namespace: "development"
slug: "video-conference-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 会议事件"
doc_id: "BtjBc3j4jo"
updated_at: "2025-10-16 15:06:33"
---

> Source: https://open.dingtalk.com/document/development/video-conference-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 会议事件
> Updated: 2025-10-16 15:06:33

# 会议事件

本文介绍了会议事件回调的RDS和SyncHTTP推送的数据格式。

## 准备工作

钉钉会向第三方企业应用推送订阅的回调事件，详情参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 225 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=225的数据格式解释。 | 225 | 会议状态变化事件。 |
| 226 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=226的数据格式解释。 | 226 | 成员状态变化事件。 |

## biz\_type=225

当biz\_type=225时，数据为会议状态变化相关数据。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值225，表示会议状态变化的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "meeting_status_change",
  "changeScene" : "conference_created",
  "statusSeqNum" : 1,
  "openConfModel" :  {
      	"conferenceId" : "6321*******9b6ed40",
        "title" : "开放会议",
        "roomCode" : "422 615 97832",
        "externalLinkUrl" : "https://example.com/app?roomCode=4226***832&token=1_20da226e-****-****-****-15af0fa1f41e",
        "status" : 1,
        "startTime" : 1663143334000,
        "endTime" : :1663143344000,
        "confDuration" : 10000,
        "invitedNum" : 0,
        "activeNum" : 0,
        "attendNum" : 0,
        "creatorId" :  "2iPO*********wiEiE",
        "creatorNick" : "开放会议创建者"
  }
}
```

字段说明：

| 参数 | 说明 |
| --- | --- |
| syncAction | 事件类型。 |
| changeScene | 会议状态变化细分类型：   - conference\_created : 会议创建事件 - conference\_closed : 会议关闭事件 |
| statusSeqNum | 会议、成员信息总体序列号, 用于区分消息顺序。 |
| openConfModel | 会议信息：   - conferenceId：会议id - title：会议标题 - roomCode：会议码 - externalLinkUrl：会议web链接 - status：会议状态 - startTime：会议开始时间 - endTime：会议结束时间 - confDuration：会议时长 - invitedNum：会议邀请人数 - activeNum：会中成员人数 - attendNum：累积在会人数（包含已离会） - creatorId：会议创建人unionId - creatorNick：会议创建人昵称 |

## biz\_type=226

当biz\_type=226时，数据为成员状态变化相关数据。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值226，表示成员状态变化的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction": "meeting_member_status_change",
  "changeScene" : "user_join",
  "statusSeqNum" : 2,
  "openMemberModels" :  [{
      	"userId" : "2iPO*********wiEiE",
        "conferenceId" : "6321*******9b6ed40",
        "userNick" : "开放会议参会者",
        "joinTime" : 1663143334000,
        "leaveTime" : :1663143344000,
        "duration" : 10000,
        "attendStatus" : 3,
        "host" : true,
        "coHost" : false,
        "outerOrgMember" :  false,
        "pstnJoin" : false
  }]
}
```

字段说明：

| 参数 | 说明 |
| --- | --- |
| syncAction | 事件类型。 |
| changeScene | 成员状态变化细分类型：   - user\_join：成员入会事件 - user\_leave：成员离会事件 - user\_invited：成员被邀请事件 - user\_kicked：成员被踢事件 |
| statusSeqNum | 会议、成员信息总体序列号, 用于区分消息顺序。 |
| openMemberModels | 变更的成员信息列表：   - userId：用户unionId（外部企业成员为空） - conferenceId：会议id - userNick：用户昵称 - joinTime：入会时间 - leaveTime：离会时间 - duration：在会时长 - attendStatus：成员状态 - host：是否为主持人 - coHost：是否为联席主持人 - outerOrgMember：是否外部企业成员 - pstnJoin：是否为pstn入会 |
