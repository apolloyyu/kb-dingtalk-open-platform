---
title: "根据指定条件查询自定义对象数据"
source_url: "https://open.dingtalk.com/document/development/retrieve-custom-crm-object-data"
namespace: "development"
slug: "retrieve-custom-crm-object-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 根据指定条件查询自定义对象数据"
doc_id: "wzf5VcDEJq"
updated_at: "2025-09-08 19:07:55"
---

> Source: https://open.dingtalk.com/document/development/retrieve-custom-crm-object-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 根据指定条件查询自定义对象数据
> Updated: 2025-09-08 19:07:55

# 根据指定条件查询自定义对象数据

调用本接口，带条件分页查询自定义对象数据，最多可一次获取200条数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档预计于 2024 年 4 月 6 日迁移至**历史文档**目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[根据指定条件查询自定义对象数据](https://open.dingtalk.com/document/orgapp/api-getobjectdata)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

调用本接口，可根据指定条件查询自定义对象数据，包括创建记录的用户昵称、审批状态、审批结果等。

![批量获取CRM自定义对象](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2847310461/p373860.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 获取CRM自定义对象数据的接口访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.crm.objectdata.query) |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/query`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | user01 | 用户userId。 |
| cursor | String | 否 | 0 | 分页游标。 |
| page\_size | Number | 是 | 100 | 分页大小。 |
| name | String | 是 | PROC-EFxxxx | 自定义表单code，进入自定义表单编辑页面，最下方可查看。  iShot2022-11-01 20 |
| query\_dsl | String | 否 | {\"filterGroupJSONType\":\"AND\",\"needCount\":true,\"groupLogicType\":\"AND\",\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"label\":\"创建时间\",\"displayPosition\":\"inner\",\"componentName\":\"DDDateField\",\"formField\":false,\"filterType\":\"GT\",\"fieldId\":\"gmt\_create\",\"value\":\"1615305600000\",\"valueExtension\":[]}]}]} | 查询条件，格式参考[查询DSL说明](https://open.dingtalk.com/document/orgapp/inner-query-dsl-description)。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | IterablePage |  | 分页结果。 |
| next\_cursor | String | 100 | 下一页的游标。 |
| values | Values[] |  | 数据列表。 |
| creator\_nick | String | 张xx | 创建记录的用户昵称。 |
| gmt\_modified | String | 2019-12-25 15:33:12 | 记录修改时间。 |
| creator\_userid | String | user01 | 创建记录的用户userid。 |
| instance\_id | String | INST\_XX | 数据ID。 |
| data | String | {\"contact\_name\":\"李四\",\"contact\_related\_customer\":\"related\_instance\_id\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2019-12-25 15:33:12 | 记录创建时间。 |
| object\_type | String | crm\_contact | 数据类型。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| participant\_userid\_list | String[] | ["user01","user02"] | 协同人用户userId列表。 |
| owner\_userid\_list | String[] | ["user01","user02"] | 负责人用户userId列表。 |
| proc\_inst\_status | String | COMPLETE | 审批状态。 |
| proc\_out\_result | String | agree | 审批结果。 |
| has\_more | Boolean | true | 是否有下一页。   - **true**：有 - **false**：没有 |
| page\_size | Number | 100 | 分页大小。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/query?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "cursor": "0",
    "name": "PROC-EFxxxx",
    "current_operator_userid": "user01",
    "page_size": 100,
    "query_dsl":"{\"filterGroupJSONType\":\"AND\",\"needCount\":true,\"groupLogicType\":\"AND\",\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"label\":\"创建时间\",\"displayPosition\":\"inner\",\"componentName\":\"DDDateField\",\"formField\":false,\"filterType\":\"GT\",\"fieldId\":\"gmt_create\",\"value\":\"1615305600000\",\"valueExtension\":[]}]}]}"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/query");
OapiCrmObjectdataQueryRequest req = new OapiCrmObjectdataQueryRequest();
req.setCurrentOperatorUserid("user01");
req.setCursor("0");
req.setPageSize(100L);
req.setName("PROC-EFxxxx");
req.serQueryDsl("{\"filterGroupJSONType\":\"AND\",\"needCount\":true,\"groupLogicType\":\"AND\",\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"label\":\"创建时间\",\"displayPosition\":\"inner\",\"componentName\":\"DDDateField\",\"formField\":false,\"filterType\":\"GT\",\"fieldId\":\"gmt_create\",\"value\":\"1615305600000\",\"valueExtension\":[]}]}]}");
OapiCrmObjectdataQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "result": {
        "next_cursor": "100",
        "values": {
            "gmt_create": "2019-12-25 15:33:12",
            "creator_nick": "张xx",
            "instance_id": "INST_XX",
            "extend_data": "{\"field_1\":\"CRM\"}",
            "data": "{\"contact_name\":\"李xx\",\"contact_related_customer\":\"related_instance_id\"}",
            "object_type": "crm_contact",
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
            "proc_inst_status": "COMPLETE",
            "gmt_modified": "2019-12-25 15:33:12",
            "proc_out_result": "agree"
        },
        "has_more": true,
        "page_size": 100
    },
    "errcode": 0,
    "errmsg": "ok"
}
```
