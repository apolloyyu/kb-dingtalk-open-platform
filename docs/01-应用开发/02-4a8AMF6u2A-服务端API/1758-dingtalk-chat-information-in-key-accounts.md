---
title: "获取企业部门聊天数据（部门维度）"
source_url: "https://open.dingtalk.com/document/development/dingtalk-chat-information-in-key-accounts"
namespace: "development"
slug: "dingtalk-chat-information-in-key-accounts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业部门聊天数据（部门维度）"
doc_id: "S2MfFUITvC"
updated_at: "2025-09-08 19:05:35"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-chat-information-in-key-accounts
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据统计 > 获取企业部门聊天数据（部门维度）
> Updated: 2025-09-08 19:05:35

# 获取企业部门聊天数据（部门维度）

调用本接口查询企业各部门聊天数据。

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
| 企业内部应用 | 是 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/kac/datav/dept/chat/summary/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6adfxxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| request | ImSummaryRequest | 是 |  | 请求对象。 |
| data\_id | String | 是 | 20201111 | 日期标识。 |
| cursor | Number | 是 | 100 | 分页游标。首页请使用0，之后直接使用返回结果中next\_cursor的值。 |
| size | Number | 是 | 0 | 分页大小，不超过100。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Object |  | 返回结果。 |
| data | Object[] |  | 返回数据列表。 |
| send\_message\_avg\_cnt | String | 11.1 | 最近一天人均发送消息数。 |
| send\_group\_message\_user\_cnt | Number | 13 | 最近一天群聊消息人数。 |
| send\_single\_message\_user\_cnt | Number | 12 | 最近一天单聊消息人数。 |
| send\_message\_user\_cnt | Number | 10 | 最近一天发消息人数。 |
| group\_message\_cnt | Number | 100 | 最近天一天群聊消息数。 |
| single\_message\_cnt | Number | 10 | 最近一天单聊消息数。 |
| message\_cnt | Number | 100 | 最近1天发消息数。 |
| dept\_name | String | 技术部 | 部门名称。 |
| dept\_id | Number | 111 | 部门ID。 |
| group\_send\_file\_message\_cnt | String | 111 | 最近1天发送群文件数。 |
| next\_cursor | Number | 0 | 下一次请求的分页游标。 |
| has\_more | Boolean | false | 是否有下一页。true表示存在更多分页。 |
| errcode | Number | 400002 | 返回码。 |
| errmsg | String | 参数错误 | 返回码描述。 |
| request\_id | String | 4zn5yen6cc6t | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/kac/datav/dept/chat/summary/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
 "request":{
  "cursor":0,
  "size":2,
  "data_id":"20201111"
 }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/kac/datav/dept/chat/summary/list");
OapiKacDatavDeptChatSummaryListRequest req = new OapiKacDatavDeptChatSummaryListRequest();
ImSummaryRequest obj1 = new ImSummaryRequest();
obj1.setDataId("20201111");
obj1.setCursor(0L);
obj1.setSize(2L);
req.setRequest(obj1);
OapiKacDatavDeptChatSummaryListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "data": [
            {
                "dept_id": -1,
                "dept_name": "互动服务窗测试",
                "group_message_cnt": 760,
                "message_cnt": 3907,
                "send_group_message_user_cnt": 28,
                "send_message_avg_cnt": "118.39",
                "send_message_user_cnt": 33,
                "send_single_message_user_cnt": 32,
                "single_message_cnt": 3147,
                "group_send_file_message_cnt": "111"
            },
            {
                "dept_id": 130934572,
                "dept_name": "数据统计测试",
                "group_message_cnt": 53,
                "message_cnt": 124,
                "send_group_message_user_cnt": 3,
                "send_message_avg_cnt": "41.33",
                "send_message_user_cnt": 3,
                "send_single_message_user_cnt": 3,
                "single_message_cnt": 71,
                "group_send_file_message_cnt": "111"
            }
        ],
        "has_more": true,
        "next_cursor": 2
    },
    "request_id": "4zn5yen6cc6t"
}
```
