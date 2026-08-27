---
title: "批量获取客户数据"
source_url: "https://open.dingtalk.com/document/development/dingtalk-paas-master-data-customer-data-search-and-query-interface"
namespace: "development"
slug: "dingtalk-paas-master-data-customer-data-search-and-query-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 批量获取客户数据"
doc_id: "vIgeMI77cA"
updated_at: "2025-09-08 19:07:52"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-customer-data-search-and-query-interface
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 批量获取客户数据
> Updated: 2025-09-08 19:07:52

# 批量获取客户数据

调用本接口根据指定查询条件批量获取客户数据，最多可一次获取200条数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月17日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[批量获取个人或企业客户数据](https://open.dingtalk.com/document/orgapp/acquire-crm-individual-customers-in-batches)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 接口说明

例如，调用本接口，在企业的客户管理应用中批量获取客户数据，实现效果与下图类似。![批量获取客户数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/5337310461/p373599.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/customer/query`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | user01 | 用户userid。 |
| cursor | String | 否 | 0 | 分页游标。 |
| page\_size | Number | 是 | 100 | 分页大小。 |
| query\_dsl | String | 否 | {\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer\_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]} | 查询条件，格式参考[查询DSL说明](https://open.dingtalk.com/document/orgapp/inner-query-dsl-description)。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | IterablePage |  | 分页查询的结果。 |
| next\_cursor | String | 100 | 下一页的游标。 |
| values | Values[] |  | 数据列表。 |
| gmt\_modified | String | 2019-12-25 15:33:12 | 记录修改时间。 |
| creator\_userid | String | user01 | 创建记录的用户userid。 |
| instance\_id | String | INST\_XX | 数据ID。 |
| data | String | {\"customer\_name\":\"杨xx\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2019-12-25 15:33:12 | 记录创建时间。 |
| object\_type | String | crm\_customer | 数据类型。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| owner\_userid\_list | String[] | ["user01","user02"] | 负责人userid列表。 |
| participant\_userid\_list | String[] | ["user01","user02"] | 协同人userid列表。 |
| has\_more | Boolean | true | 是否有下一页。 |
| page\_size | Number | 100 | 分页大小。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/customer/query?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "cursor":"0",
        "query_dsl":"{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}",
        "current_operator_userid":"user01",
        "page_size":"100"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customer/query");
OapiCrmObjectdataCustomerQueryRequest req = new OapiCrmObjectdataCustomerQueryRequest();
req.setCurrentOperatorUserid("user01");
req.setCursor("0");
req.setPageSize(100L);
req.setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"customer_name\",\"filterType\":\"EQ\",\"value\":\"xx有限公司\"}]}]}");
OapiCrmObjectdataCustomerQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "result": {
        "next_cursor": "100",
        "values": {
            "instance_id": "instance_id",
            "extend_data": "{\"field_1\":\"CRM\"}",
            "data": "{\"customer_name\":\"**公司\",\"MultiTagField-62e5f9c0\":{\"extendValue\":\"[{\\\"key\\\":\\\"e88a359d6c\\\"}]\",\"value\":\"[\\\"重要\\\"]\"},\"customer_follow_up_status\":{\"extendValue\":\"{\\\"extension\\\":{\\\"editFreeze\\\":true},\\\"label\\\":\\\"新获取\\\",\\\"key\\\":\\\"option_new_acquisition\\\"}\",\"value\":\"新获取\"},\"DDSelectField-K371T4RY\":{\"extendValue\":\"{\\\"label\\\":\\\"潜在客户\\\",\\\"key\\\":\\\"option_0\\\"}\",\"value\":\"潜在客户\"},\"DDSelectField-K2U5GX39\":{\"extendValue\":\"{\\\"label\\\":\\\"电信\\\",\\\"key\\\":\\\"option_K2U5KPJU\\\"}\",\"value\":\"电信\"}}",
            "object_type": "crm_customer",
            "creator_userid": "user01",
            "permission": {
                "participant_userid_list": [
                    "user01",
                    "user02"
                ],
                "owner_userid_list": [
                    "user01",
                    "user02"
                ]
            },
            "gmt_create": "2019-12-25 15:33:12",
            "gmt_modified": "2019-12-25 15:33:12",
        },
        "has_more": true,
        "page_size": 100
    },
    "errcode": 0,
    "errmsg": "ok"
}
```
