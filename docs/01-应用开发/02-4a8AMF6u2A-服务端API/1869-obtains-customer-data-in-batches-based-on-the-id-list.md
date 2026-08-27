---
title: "批量获取企业客户数据"
source_url: "https://open.dingtalk.com/document/development/obtains-customer-data-in-batches-based-on-the-id-list"
namespace: "development"
slug: "obtains-customer-data-in-batches-based-on-the-id-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 批量获取企业客户数据"
doc_id: "CTZd30TsOp"
updated_at: "2025-09-08 19:07:53"
---

> Source: https://open.dingtalk.com/document/development/obtains-customer-data-in-batches-based-on-the-id-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 批量获取企业客户数据
> Updated: 2025-09-08 19:07:53

# 批量获取企业客户数据

调用本接口根据实例ID列表批量获取客户记录数据，最多可一次获取200条数据。

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

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/customer/list`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | manager1 | 操作人用户userid。 |
| data\_id\_list | String | 是 | INST1,INST2 | 数据ID列表，多个用英文逗号隔开，可通过[批量获取客户数据](https://open.dingtalk.com/document/orgapp/dingtalk-paas-master-data-customer-data-search-and-query-interface)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result\_list | ObjectDataInstanceVo[] |  | 实例数据。 |
| creator\_nick | String | 张xx | 记录创建人的昵称。 |
| gmt\_modified | String | 2020-09-15 00:00:00 | 记录修改时间。 |
| creator\_userid | String | user1 | 记录创建人的用户userid。 |
| instance\_id | String | INST-XXX | 数据ID。 |
| data | String | {\"customer\_name\":\"XX有限公司\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2020-09-15 00:00:00 | 记录创建时间。 |
| object\_type | String | crm\_customer | 数据类型。  客户管理固定值为**crm\_customer**。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| participant\_userid\_list | String[] | ["user01"] | 协同人userid列表。 |
| owner\_userid\_list | String[] | ["user01"] | 负责人userid列表。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/customer/list?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "current_operator_userid": "manager1",
  "data_id_list":"INST-XXX,INST-XXX2"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customer/list");
OapiCrmObjectdataCustomerListRequest req = new OapiCrmObjectdataCustomerListRequest();
req.setCurrentOperatorUserid("manager1");
req.setDataIdList("INST-XXX,INST-XXX2");
OapiCrmObjectdataCustomerListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result_list": [
        {
            "creator_userid": "userid01",
            "data": "{\"customer_name\":\"**公司名\",\"MultiTagField-62e5f9c0\":{\"extendValue\":\"[{\\\"key\\\":\\\"e88a359d6c\\\"}]\",\"value\":\"[\\\"重要\\\"]\"},\"customer_follow_up_status\":{\"extendValue\":\"{\\\"extension\\\":{\\\"editFreeze\\\":true},\\\"label\\\":\\\"新获取\\\",\\\"key\\\":\\\"option_new_acquisition\\\"}\",\"value\":\"新获取\"},\"DDSelectField-K371T4RY\":{\"extendValue\":\"{\\\"label\\\":\\\"潜在客户\\\",\\\"key\\\":\\\"option_0\\\"}\",\"value\":\"潜在客户\"},\"DDSelectField-K2U5GX39\":{\"extendValue\":\"{\\\"label\\\":\\\"电信\\\",\\\"key\\\":\\\"option_K2U5KPJU\\\"}\",\"value\":\"电信\"}}",
            "gmt_create": "2021-07-21 21:13:52",
            "gmt_modified": "2021-08-24 12:59:54",
            "instance_id": "c5baeea7-58de-4b61-882b-902aafd0b21f",
            "object_type": "crm_customer",
            "permission": {
                "owner_userid_list": [
                    "userid01"
                ],
                "participant_userid_list": [
                    "userid01"
                ]
            }
        }
    ],
    "request_id": "52qrvyubsqnr"
}
```
