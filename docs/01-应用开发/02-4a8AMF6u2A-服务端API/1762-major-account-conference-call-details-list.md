---
title: "获取企业电话会议明细列表"
source_url: "https://open.dingtalk.com/document/development/major-account-conference-call-details-list"
namespace: "development"
slug: "major-account-conference-call-details-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 电话会议统计 > 获取企业电话会议明细列表"
doc_id: "G21Qj31aO3"
updated_at: "2025-09-08 19:05:31"
---

> Source: https://open.dingtalk.com/document/development/major-account-conference-call-details-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 电话会议统计 > 获取企业电话会议明细列表
> Updated: 2025-09-08 19:05:31

# 获取企业电话会议明细列表

调用本接口查询企业在某天发起的电话会议列表及详情。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

例如，企业有多个子部门，调用本接口可以获取在某天，企业所有的电话会议明细。包括会议发起人、会议发起人所在部门信息、会议时长、会议开始时间、结束时间、会议参与人等信息。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/telconf/detail/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | TelConferenceSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20200720 | 日期标识。 |
| size | Number | 是 | 100 | 分页大小，不超过100。 |
| cursor | Number | 是 | 0 | 分页游标。首页请使用0，之后直接使用返回结果中next\_cursor的值。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| request\_id | String | njmzwmt7qyao | 请求ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | TelConferenceDetailResponse |  | 查询结果。 |
| data | TelConferenceDetailVo[] |  | 返回数据列表。 |
| conf\_id | String | 112333 | 会议id。 |
| conf\_len\_min | String | 4 | 会议时长，单位分钟。 |
| dept\_id | Number | 12 | 发起人部门id。 |
| dept\_name | String | 技术部 | 发起人部门。 |
| end\_time | String | 2020-07-20 10:54:03 | 会议结束时间。 |
| join\_user\_count | Number | 102 | 参与人数。 |
| userid | String | 123 | 员工userid。 |
| staff\_job\_num | String | 1001 | 发起人工号。 |
| staff\_name | String | 测试用户 | 发起人姓名。 |
| start\_time | String | 2020-07-20 10:50:03 | 会议开始时间。 |
| has\_more | Boolean | false | 是否有下一页，true表示存在更多分页。 |
| next\_cursor | Number | 100 | 下一次请求的分页游标。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/telconf/detail/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "request":{
                "cursor":0,
                "size":100,
                "data_id":"20200720"
        }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/telconf/detail/list");
OapiKacDatavTelconfDetailListRequest req = new OapiKacDatavTelconfDetailListRequest();
TelConferenceSummaryRequest obj1 = new TelConferenceSummaryRequest();
obj1.setDataId("20200720");
obj1.setSize(100L);
obj1.setCursor(0L);
req.setRequest(obj1);
OapiKacDatavTelconfDetailListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode":100,
    "result":{
        "data":[
            {
                "conf_id":"112333",
                "conf_len_min":"4",
                "dept_id":12,
                "dept_name":"技术部",
                "end_time":"2020-07-20 11:54:03",
                "join_user_count":10,
                "userid":"user123",
                "staff_job_num":"1002",
                "staff_name":"测试用户",
                "start_time":"2020-07-20 11:50:03"
            }
        ],
        "has_more":false,
        "next_cursor":100
    },
    "request_id":"njmzwmt7qyao"
}
```
