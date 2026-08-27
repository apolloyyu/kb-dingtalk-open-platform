---
title: "删除企业客户数据"
source_url: "https://open.dingtalk.com/document/development/delete-crm-customer"
namespace: "development"
slug: "delete-crm-customer"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 删除企业客户数据"
doc_id: "BRH3j2YyY6"
updated_at: "2025-09-08 19:07:51"
---

> Source: https://open.dingtalk.com/document/development/delete-crm-customer
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 删除企业客户数据
> Updated: 2025-09-08 19:07:51

# 删除企业客户数据

调用本接口删除指定的CRM企业客户数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月17日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[删除个人或企业客户数据](https://open.dingtalk.com/document/orgapp/delete-crm-personal-customer)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 接口说明

例如，调用本接口，在企业的客户管理应用中删除客户数据，实现效果与下图类似。![删除客户CRM](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7227310461/p373597.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/customer/delete`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| operator\_userid | String | 是 | user01 | 操作人用户userid。 |
| data\_id | String | 是 | INST\_XX | 客户实例ID，可通过[根据指定条件查询个人或企业客户数据](https://open.dingtalk.com/document/orgapp/obtains-crm-individual-customers-in-batches-based-on-specified-query)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataDeleteDto |  | 返回结果。 |
| instance\_id | String | iNST\_XX | 删除的客户实例ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/customer/delete?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "operator_userid":"user01",
        "data_id":"INST_XX"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customer/delete");
OapiCrmObjectdataCustomerDeleteRequest req = new OapiCrmObjectdataCustomerDeleteRequest();
req.setOperatorUserid("userid_xxx");
req.setDataId("INST_XX");
OapiCrmObjectdataCustomerDeleteResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    " result": {
        "instance_id": "iNST_XX"
    }
}
```
