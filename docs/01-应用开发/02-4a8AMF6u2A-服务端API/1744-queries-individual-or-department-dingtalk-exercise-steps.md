---
title: "获取个人或部门钉钉运动数据"
source_url: "https://open.dingtalk.com/document/development/queries-individual-or-department-dingtalk-exercise-steps"
namespace: "development"
slug: "queries-individual-or-department-dingtalk-exercise-steps"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 企业文化 > 获取个人或部门钉钉运动数据"
doc_id: "BfmmburMWs"
updated_at: "2025-09-08 19:05:15"
---

> Source: https://open.dingtalk.com/document/development/queries-individual-or-department-dingtalk-exercise-steps
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 企业文化 > 获取个人或部门钉钉运动数据
> Updated: 2025-09-08 19:05:15

# 获取个人或部门钉钉运动数据

调用本接口，查询用户个人或企业部门每天的钉钉运动步数，最多可以查询31天的数据。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

**只能通过钉钉手机端查看：**

在工作台页面，打开钉钉运动，单击步数榜，查看个人或部门排行数据。

![iShot2021-12-17 09](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/3495279361/p370793.png)

> **[!NOTE]**
>
> 调用本接口需要满足以下条件：
>
> 1. 用户需要加入当前企业排行榜：
>
>    - 企业内部应用，调用[查询用户是否参与企业步数排行榜](https://open.dingtalk.com/document/orgapp/check-whether-dingtalk-is-enabled)查看用户是否加入企业排行榜。
>    - 第三方企业应用，调用[查询用户是否参与企业步数排行榜](https://open.dingtalk.com/document/isvapp/check-whether-dingtalk-is-enabled)查看用户是否加入企业排行榜。
> 2. 用户需要打开手机钉钉客户端，运动数据会从端上同步，调用本接口才可以获取到运动数据。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 钉钉健康数据查询权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 是 | 钉钉健康数据查询权限 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/health/stepinfo/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| type | Number | 是 | 1 | 获取数据类型。   - **0**：获取用户步数 - **1**：获取部门步数 |
| object\_id | String | 是 | 1 | 查询的用户userId或部门ID。   - 当type为1，输入部门ID - 当type为0，输入userId |
| stat\_dates | String | 是 | 20180101,20180102 | 时间列表，时间格式是YYYYMMDD，多个日期之间使用英文逗号分割。  **[!NOTE]**  最多可以查询31天的数据。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | wicoimr4luya | 请求ID。 |
| stepinfo\_list | BasicStepInfoVo[] |  | 步数列表。 |
| stat\_date | Number | 20200907 | 统计的时间。 |
| step\_count | Number | 5013 | 步数。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/health/stepinfo/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "stat_dates":"20200907,20200908",
        "type":0,
        "object_id":"manager4220"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/health/stepinfo/list");
OapiHealthStepinfoListRequest req = new OapiHealthStepinfoListRequest();
req.setType(0L);
req.setObjectId("manager4220");
req.setStatDates("20200907,20200908");
OapiHealthStepinfoListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

```
{
    "errcode": 0,
    "stepinfo_list": [
        {
            "stat_date": 20200907,
            "step_count": 15013
        },
        {
            "stat_date": 20200908,
            "step_count": 12358
        }
    ],
    "request_id": "14zrgef5j219v"
}
```
