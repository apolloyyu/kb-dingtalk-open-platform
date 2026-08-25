---
title: "智能人事事件"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-events"
namespace: "development"
slug: "intelligent-personnel-events"
group: "应用开发"
tab: "事件订阅"
breadcrumb: "历史文档（不推荐） > RDS推送/SyncHTTP推送 > 智能人事事件"
doc_id: "Z8tRQMnBKK"
updated_at: "2025-10-16 15:06:32"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-events
> Path: 应用开发 / 事件订阅 / 历史文档（不推荐） > RDS推送/SyncHTTP推送 > 智能人事事件
> Updated: 2025-10-16 15:06:32

# 智能人事事件

本文介绍了智能人事事件回调的RDS和SyncHTTP推送的数据格式。

## 配置事件回调

第三方企业应用配置事件订阅流程，请参见[第三方企业应用事件与回调流程](https://open.dingtalk.com/document/isvapp/third-party-enterprise-application-address-book-change-event-subscription-process)。

## 数据表

| **主键（id）** | **订阅者ID（**subscribe\_id**）** | **企业ID（**corp\_id**）** | **业务ID（**biz\_id**）** | **业务类型（**biz\_type**）** | 说明 |
| --- | --- | --- | --- | --- | --- |
| 137 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=137的数据格式解释。 | 137 | 人事平台员工异动V2事件。 |
| 165 | xxxxx\_0 | corpxxxx | 无业务意义，幂等。  详见下方biz\_type=165的数据格式解释 | 165 | 人事平台员工档案变动事件相关数据的回调事件。 |
| 175 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=175的数据格式解释。 | 175 | 人事解决方案变更事件。 |
| 224 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=224的数据格式解释。 | 224 | 人事商业化方案事件。 |
| 238 | xxxxx\_0 | corpxxxx | 详见下方biz\_type=238的数据格式解释。 | 238 | 培训学习记录同步事件。 |

## biz\_type=137

当biz\_type=137时，数据为人事平台员工异动V2相关数据。

该数据为人事平台员工异动V2相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值137，表示人事平台员工异动V2相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "hrm_mdm_user_change",
    "changeType": 4,
    "staffId": "01142240209xxxxx",
    "bizTime": 1559836800000,
    "syncSeq": "335BF2BEE1351DC0241DDE"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| changeType | Number | 人事平台员工异动类型：   - **1**：入职 - **2**：转正 - **3**：调岗 - **4**：离职 - **8**：晋升 |
| staffId | String | 用户userId。 |
| bizTime | Long | 业务时间。 |
| syncSeq | String | 无业务意义。 |

## biz\_type=165

当biz\_type=165时，数据为人事平台员工档案变动事件相关数据。

该数据为人事平台员工档案变动事件相关数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值165，表示人事平台员工档案变动事件相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
    "syncAction": "hrm_mdm_user_info_change",
    "staffId": "xxx6129461xxxxxx"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| staffId | String | 档案发生变动的员工userId。 |

## biz\_type=175

当biz\_type=175时，数据为人事解决方案变更事件的相关数据。

该数据为人事解决方案变更事件相关的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值175，表示人事解决方案变更相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "corpId" : "ding57935b18bfd13e9735cxxxxxxxxxx",
  "staffIds" : [ "157087xxxxxxxx" ],
  "syncAction" : "hrm_solution_manage",
  "solutionType" : "onboarding",
  "solutionStatus" : "start"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| corpId | String | 企业corpId。 |
| staffIds | Array of String | 用户userId。 |
| syncAction | String | 事件类型。 |
| solutionType | String | 人事解决方案类型：   - **onboarding**：新人流程 |
| solutionStatus | String | 人事解决方案状态：   - **init**：初始化解决方案 - **start**：发起解决方案 |

## biz\_type=224

当biz\_type=224时，数据为人事商业化方案相关数据。

该数据为人事商业化方案的数据变更时的数据推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值224，表示人事商业化方案变更的相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  "syncAction" : "commercial_solution",
  "solutionId" : "HRM_COMMERCIAL_SOLUTION_ON_BOARDING_TRAIN",
  "solutionStatus" : "ENABLE"
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| solutionId | String | 解决方案ID。 |
| solutionStatus | String | 解决方案状态：   - **ENABLE**：启用 - **DISABLE**：停用 |

## biz\_type=238

当biz\_type=238时，数据为培训学习记录同步相关数据。

该数据为培训学习记录同步相关的数据变更时推送，插入表open\_sync\_biz\_data\_medium中。

| **字段** | **说明** |
| --- | --- |
| corp\_id | 企业corpId。 |
| biz\_id | 无业务意义，幂等。 |
| biz\_type | 固定值238，表示培训学习记录同步相关数据。 |
| biz\_data | 数据为Json格式。 |

biz\_data数据如下：

```
{
  	"syncAction":"train_course_user_info",
    "courseId":"xxx",    // 课程id
    "learnContent":[
      {
        "userId":"xxx",     // 员工id
        "learnTime":100,   // 学习时长，ms
        "uuid":"xxxx"      //记录的唯一标识，去重用
      }
    ]
}
```

字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| syncAction | String | 事件类型。 |
| courseId | String | 课程id。 |
| learnContent | Array of Object | 学习内容，具体字段见下文学习内容字段说明。 |

学习内容**learnContent**字段说明：

| 参数 | 数据类型 | 说明 |
| --- | --- | --- |
| userId | String | 员工userId。 |
| learnTime | Long | 学习时长，单位毫秒。 |
| uuid | String | 记录的唯一标识，去重。 |
