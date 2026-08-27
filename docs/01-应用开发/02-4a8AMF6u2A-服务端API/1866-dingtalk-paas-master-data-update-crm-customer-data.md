---
title: "更新企业客户数据"
source_url: "https://open.dingtalk.com/document/development/dingtalk-paas-master-data-update-crm-customer-data"
namespace: "development"
slug: "dingtalk-paas-master-data-update-crm-customer-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 更新企业客户数据"
doc_id: "AkrTjiDKmL"
updated_at: "2025-09-08 19:07:50"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-update-crm-customer-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 更新企业客户数据
> Updated: 2025-09-08 19:07:50

# 更新企业客户数据

调用本接口更新企业客户数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)本文旧版规范接口文档已于**2022年6月17日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[更新个人或企业客户数据](https://open.dingtalk.com/document/orgapp/update-crm-personal-customers)或者[批量更新个人或企业客户数据](https://open.dingtalk.com/document/orgapp/update-multiple-relational-data-tables-at-a-time)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 接口说明

例如，调用本接口，在企业的客户管理应用中更新客户数据，实现效果与下图类似。![更新CRM客户数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6127310461/p373595.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/customer/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| instance | ObjectDataInstanceVo | 是 |  | 客户数据。 |
| data | String | 是 | {\"customer\_name\":\"杨xx\"} | 数据内容，JSON格式字符串。 |
| extend\_data | String | 否 | {\"field\_1\":\"CRM\"} | 扩展数据内容，JSON格式字符串。 |
| permission | DataPermissionVo | 否 |  | 权限。 |
| participant\_userids | String[] | 否 | ["user01","user02"] | 协同人的用户userid。 |
| owner\_userids | String[] | 否 | ["user01","user02"] | 负责人的用户userid。 |
| instance\_id | String | 是 | INST\_XX | 客户数据ID，可通过[批量获取客户数据](https://open.dingtalk.com/document/orgapp/dingtalk-paas-master-data-customer-data-search-and-query-interface)接口获取。 |
| modifier\_userid | String | 是 | user01 | 用户userid。 |
| modifier\_nick | String | 否 | 张xx | 用户nick。 |
| skip\_duplicate\_check | Boolean | 否 | false | 是否跳过查重。  **默认值**：false。 |
| action | String | 否 | publicAssign | 取值：   - 公海领取客户：**publicDraw** - 公海分配客户：**publicAssign** - 其余场景：不用传值 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataCreateDto |  | 返回结果。 |
| instance\_id | String | INST\_XX | 客户数据ID。 |
| success | Boolean | true | 执行结果。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/customer/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "instance": {
        "extend_data": "{}",
        "instance_id": "instance_id",
        "data": "{\"customer_name\":\"杨xx\"}",
        "permission": {
            "owner_userids": [
                "user01",
                "user02"
            ],
            "participant_userids": [
                "user01",
                "user02"
            ]
        },
        "modifier_nick": "张xx",
        "modifier_userid": "user01"
    }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customer/update");
OapiCrmObjectdataCustomerUpdateRequest req = new OapiCrmObjectdataCustomerUpdateRequest();
DataPermissionVo dataPermissionVo = new DataPermissionVo();
dataPermissionVo.setParticipantUserids(Arrays.asList("user01","user02"));
dataPermissionVo.setOwnerUserids(Arrays.asList("user01","user02"));
ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
objectDataInstanceVo.setPermission(dataPermissionVo);
objectDataInstanceVo.setInstanceId("INST_XX");
objectDataInstanceVo.setModifierUserid("user01");
objectDataInstanceVo.setModifierNick("张xx");
req.setInstance(objectDataInstanceVo);
OapiCrmObjectdataCustomerUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "success": true,
    "errmsg": "ok",
    "result": {
        "instance_id": "INST_XX"
    }
}
```
