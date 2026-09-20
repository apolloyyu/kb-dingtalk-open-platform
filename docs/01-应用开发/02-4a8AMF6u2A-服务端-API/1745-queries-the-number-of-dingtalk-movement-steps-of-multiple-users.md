---
title: "批量获取钉钉运动数据"
source_url: "https://open.dingtalk.com/document/development/queries-the-number-of-dingtalk-movement-steps-of-multiple-users"
namespace: "development"
slug: "queries-the-number-of-dingtalk-movement-steps-of-multiple-users"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 企业文化 > 批量获取钉钉运动数据"
doc_id: "qiWfpcxFpG"
updated_at: "2026-08-27 14:07:30"
---

> Source: https://open.dingtalk.com/document/development/queries-the-number-of-dingtalk-movement-steps-of-multiple-users
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 企业文化 > 批量获取钉钉运动数据
> Updated: 2026-08-27 14:07:30

# 批量获取钉钉运动数据

调用本接口，批量获取钉钉运动数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/health/stepinfo/listbyuserid`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userids | String | 是 | manager1,manager2 | 员工userId列表，最多传50个，多个userId之间使用英文逗号分割。 |
| stat\_date | String | 是 | 20200101 | 查询时间，时间格式是YYMMDD。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | wicoimr4luya | 请求ID。 |
| stepinfo\_list | BasicStepInfoVo[] |  | 步数列表。 |
| stat\_date | Number | 20200907 | 统计的时间。 |
| step\_count | Number | 15013 | 步数。 |
| userid | String | manager1 | 员工userId。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/health/stepinfo/listbyuserid?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "stat_date":"20200907",
  "userids":"manager4220,user456"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/health/stepinfo/listbyuserid");
OapiHealthStepinfoListbyuseridRequest req = new OapiHealthStepinfoListbyuseridRequest();
req.setUserids("user456,manager4220");
req.setStatDate("20201119");
OapiHealthStepinfoListbyuseridResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "stepinfo_list": [
    {
      "stat_date": 20201119,
      "step_count": 11892,
      "userid": "user456"
    },
    {
      "stat_date": 20201119,
      "step_count": 15984,
      "userid": "manager4220"
    }
  ],
  "request_id": "rj8wff8bnwm4"
}
```
