---
title: "课堂数据介绍"
source_url: "https://open.dingtalk.com/document/development/teaching-data-overview"
namespace: "development"
slug: "teaching-data-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 在线课堂 > 课堂数据介绍"
doc_id: "0wt8AB0OGU"
updated_at: "2026-07-20 09:21:44"
---

> Source: https://open.dingtalk.com/document/development/teaching-data-overview
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 在线课堂 > 课堂数据介绍
> Updated: 2026-07-20 09:21:44

# 课堂数据介绍

## **数据读取**

授课的数据读取需要依托前置定义的数据类别及因子，当前已支持的授课数据类别如下：

### **数据类别**

| 名称 | **编码category\_code** | 包含因子 | 说明 |
| --- | --- | --- | --- |
| 课堂基础数据 | BASIC\_INFO | - 课堂开始时间 - 课堂结束时间 - 课堂参与人数 - 课堂消息数 - 进入课堂时间 - 退出课堂时间 | 授课课堂的基础类别数据 |
| 课堂举手数据 | RAISE\_HAND | - 开始举手时间 - 取消举手时间 | 授课课堂的举手类别数据 |
| 课堂连麦数据 | CONVERSE | - 邀请连麦时间 - 同意连麦时间 - 结束连麦时间 - 踢出连麦时间 | 授课课堂的连麦类别数据 |
| 课堂点名签到数据 | SIGN\_IN | - 点名轮次id - 点名开始时间 - 点名结束时间 - 点名参与总人数 - 实际签到人数 - 点名发起时间 - 是否签到 - 签到具体时间 | 授课课堂的点名签到数据 |

### **数据因子**

| 名称 | 编码 | 类别 | 说明 |
| --- | --- | --- | --- |
| 课堂开始时间 | classroomStartTime | 概要数据 | 授课课堂的开始时间 |
| 课堂结束时间 | classroomEndTime | 概要数据 | 授课课堂的结束时间 |
| 课堂参与人数 | classroomMemberCount | 概要数据 | 授课课堂的参与人数，多少人听课 |
| 课堂消息数 | classroomMessageCount | 概要数据 | 授课课堂的整体消息数 |
| 进入课堂时间 | joinClassroomTime | 明细数据 | 授课课堂参与方进入课堂时间 |
| 退出课堂时间 | leaveClassroomTime | 明细数据 | 授课课堂参与方退出课堂时间 |
| 开始举手时间 | raiseTime | 明细数据 | 授课课堂学生举手时间 |
| 取消举手时间 | raiseCancelTime | 明细数据 | 授课课堂学生取消举手时间 |
| 邀请连麦时间 | inviteConverseTime | 明细数据 | 授课课堂老师邀请学生连麦时间 |
| 同意连麦时间 | acceptConverseTime | 明细数据 | 授课课堂学生同意连麦时间 |
| 结束连麦时间 | leaveConverseTime | 明细数据 | 授课课堂学生主动结束连麦时间 |
| 踢出连麦时间 | kickConverseTime | 明细数据 | 授课课堂老师踢出学生连麦时间 |
| 点名轮次id | signInId | 概要数据 | 本点名轮次id |
| 点名开始时间 | signInStartTime | 概要数据 | 本点名轮次开始时间 |
| 点名结束时间 | signInEndTime | 概要数据 | 本点名轮次结束时间 |
| 点名参与总人数 | signInTotalCount | 概要数据 | 本点名轮次实际参与总数 |
| 实际签到人数 | signedInCount | 概要数据 | 本点名轮次实际签到人数 |
| 点名发起时间 | signInCreateTime | 明细数据 | 授课课堂老师发起点名时间 |
| 是否签到 | isSignedIn | 明细数据 | 授课课堂学生是否签到 |
| 签到具体时间 | signedInTime | 明细数据 | 授课课堂学生签到具体时间 |

## **数据推送**

第三方应用服务商在线课堂数据事件的数据推送格式。

### **RDS数据推送**

| 数据类型 | 数据类别 | 数据因子 |
| --- | --- | --- |
| 课堂概要数据 | 课堂基础数据（BASIC\_INFO） | 进入课堂时间（joinClassroomTime） |
| 退出课堂时间（leaveClassroomTime） |

在使用前，需要先申请“排课授课接口权限”，然后在开发管理中，推送回调事件勾选“教育课程数据”选项。

![回调事件](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0944173061/p176632.png)当 biz\_type = 62，对应的数据为课堂数据。

| 字段 | 说明 |
| --- | --- |
| subscribe\_id | 套件suiteid加下划线0。 |
| corp\_id | 套件所属企业的corpid。 |
| biz\_id | 业务ID。 |
| biz\_data | 推送的业务数据，格式为JSON。 |
| └ type | 数据类型：   - **1**：表示课堂的概要数据 - **2**：表示课堂明细数据 |
| └ data | 推送的具体数据。 |

- type=1时，biz\_data数据格式如下。

  | type | Number | 1 | 数据类型。  1表示课堂的概要数据。 |
  | --- | --- | --- | --- |
  | data | Json |  | 数据。 |
  | └ category\_code | String | BASIC\_INFO | 数据类别编码。 |
  | └ category\_biz\_key | String | 1\_6d20b8ae-edd3-4ac8-b8d0-70be7837b4b4 | 数据类别业务唯一键。 |
  | └ data | Json | {"classroomMemberCount":2,"classroomEndTime":1600696867000,"classroomStartTime":1600696128000,"classroomMessageCount":2} | 数据：  - **key**：数据因子编码 - **value**： 对应的数据 |
  | └ course\_code | String | GJKI49001 | 课堂编码。 |

  数据示例：

  ```
  {
    "data":"{
      "categoryBizKey":"1_6d20b8ae-edd3-4ac8-b8d0-70be7837b4b4",
      "categoryCode":"BASIC_INFO,
      "courseCode":"GJKI49001",
      "data":{
          "classroomMemberCount":2,
          "classroomEndTime":1600696867000,
          "classroomStartTime":1600696128000,
          "classroomMessageCount":2
        }
    }",
    "type":1
  }
  ```
- type=2时，biz\_data数据格式如下。

  | type | Number | 2 | 数据类型。  2表示课堂明细数据。 |
  | --- | --- | --- | --- |
  | data | Json |  | 数据。 |
  | └ user\_cropid | String | ding4220d8e5128d0edd | 用户组织ID。 |
  | └ userid | String | user01 | 用户的userid。 |
  | └ category\_code | String | BASIC\_INFO | 数据类别编码。 |
  | └ category\_biz\_key | String | b3540b13-60bf-4xxx | 数据业务唯一键，例如标识具体哪一次进入教室。 |
  | └ value | String | 1600741723451 | 数据值，例如进入教室的时间戳。 |
  | └ course\_code | String | GJKI49001 | 课堂编码。 |
  | └ factor\_code | String | joinClassroomTime | 数据因子编码。 |

  数据示例：

  ```
  {
    "data":"{
      "categoryBizKey":"b3540b13-60bf-4375-bfe5-633bbe5adef3_JOIN_1600741723451",
      "categoryCode""BASIC_INFO",
      "courseCode":"GJKI49001",
      "factorCode":"joinClassroomTime",
      "userCropId":"ding4220d8e5128d0edd",
      "userId":"user01",
      "value":"1600741723451"
    }",
    "type":2
  }
  ```
