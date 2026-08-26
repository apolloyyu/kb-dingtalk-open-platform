---
title: "根据指定条件查询联系人数据"
source_url: "https://open.dingtalk.com/document/development/dingtalk-the-contact-data-query-api"
namespace: "development"
slug: "dingtalk-the-contact-data-query-api"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 根据指定条件查询联系人数据"
doc_id: "lQEiFC7we9"
updated_at: "2025-09-08 19:07:54"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-the-contact-data-query-api
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 根据指定条件查询联系人数据
> Updated: 2025-09-08 19:07:54

# 根据指定条件查询联系人数据

调用本接口，根据指定查询条件批量获取联系人数据，最多可一次获取200条数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于 2024 年 3 月 6 日迁移至**历史文档**目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[根据指定条件查询联系人数据](https://open.dingtalk.com/document/orgapp/api-getcontacts)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

调用本接口，可根据指定条件查询联系人数据。

![批量获取联系人数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1047310461/p373787.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | 获取CRM主数据的接口访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingtalk.oapi.crm.objectdata.contact.query) |
| 第三方企业应用 | 是 | 获取CRM主数据的接口访问权限 | [调试](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=dingtalk.oapi.crm.objectdata.contact.query) |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/contact/query`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取。 - 第三方企业应用，通过[获取第三方企业应用的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | user01 | 用户userId。 |
| cursor | String | 否 | 0 | 分页游标。 |
| page\_size | Number | 是 | 100 | 分页大小。 |
| provider\_corpid | String | 否 | dingxxx | 服务商组织ID。自建应用可以传入。CorpId |
| query\_dsl | String | 否 | {\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact\_phone\",\"filterType\":\"EQ\",\"value\":\"18000000000\"},{\"fieldId\":\"contact\_related\_customer\",\"filterType\":\"EQ\",\"value\":\"INST-XXX\"}]}]} | 查询条件。   - 企业内部应用，格式参考[查询DSL说明](https://open.dingtalk.com/document/orgapp/inner-query-dsl-description)。 - 第三方企业应用，格式参考[查询DSL说明](https://open.dingtalk.com/document/isvapp/isv-query-dsl-description)。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | IterablePage |  | 分页结果。 |
| next\_cursor | String | 100 | 下一页的游标。 |
| values | Values[] |  | 数据列表。 |
| gmt\_modified | String | 2019-12-25 15:33:12 | 记录修改时间。 |
| creator\_userid | String | user01 | 创建记录的用户userId。 |
| instance\_id | String | INST\_XX | 联系人数据ID。 |
| data | String | {\"contact\_name\":\"李xx\",\"contact\_related\_customer\":\"related\_instance\_id\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2019-12-25 15:33:12 | 记录创建时间。 |
| object\_type | String | crm\_contact | 数据类型。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| participant\_userid\_list | String[] | ["user01","user02"] | 协同人userId列表。 |
| owner\_userid\_list | String[] | ["user01","user02"] | 负责人userId列表。 |
| has\_more | Boolean | true | 是否有下一页。   - **true**：有 - **false**：没有 |
| page\_size | Number | 100 | 分页大小。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/contact/query?access_token=ACCESS_TOKEN
```

请求正文

```
{
        "cursor":"0",
        "query_dsl":"{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"filterType\":\"EQ\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"filterType\":\"EQ\",\"value\":\"INST-XXX\"}]}]}",
        "current_operator_userid":"user01",
        "provider_corpid":"dingxxx",
        "page_size":"100"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/query");
OapiCrmObjectdataContactQueryRequest req = new OapiCrmObjectdataContactQueryRequest();
req.setCurrentOperatorUserid("user01");
req.setCursor("0");
req.setPageSize(100L);
req.setProviderCorpid("dingxxx");
req.setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"filterType\":\"EQ\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"filterType\":\"EQ\",\"value\":\"INST-XXX\"}]}]}");
OapiCrmObjectdataContactQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "result": {
        "values": [
            {
                "gmt_create": "2019-12-25 15:33:12",
                "instance_id": "INST_XX",
                "data": "{\"contact_related_customer\":{\"extendValue\":\"{\\\"quote\\\":\\\"1\\\",\\\"bizType\\\":\\\"crm_customer\\\",\\\"list\\\":[{\\\"instanceId\\\":\\\"c5baeea7-58de-4b61-882b-902aafd0b212\\\"}]}\",\"value\":\"[\\\"1\\\"]\"},\"contact_name\":\"联系人1\",\"contact_position\":{\"extendValue\":\"[{\\\"label\\\":\\\"老板\\\",\\\"key\\\":\\\"option_1\\\"}]\",\"value\":\"[\\\"老板\\\"]\"},\"contact_phone\":{\"extendValue\":\"{\\\"mode\\\":\\\"phone\\\",\\\"countryKey\\\":\\\"CN\\\",\\\"flag\\\":\\\"C\\\",\\\"countryCode\\\":\\\"+86\\\",\\\"areaNumber\\\":\\\"\\\",\\\"flagPy\\\":\\\"Z\\\",\\\"countryName\\\":\\\"China\\\",\\\"countryNameZh\\\":\\\"中国\\\",\\\"countryNamePy\\\":\\\"ZHONGGUO\\\"}\",\"value\":\"136********\"}}",
                "extend_data": "{\"contactUserId\":\"userId02\",\"contactUnionId\":\"unionId02\"}",
                "object_type": "crm_contact",
                "creator_userid": "user01",
                "permission": [
                    {
                        "participant_userid_list": [
                            "user01",
                            "user02"
                        ],
                        "owner_userid_list": [
                            "user01",
                            "user02"
                        ]
                    }
                ],
                "gmt_modified": "2019-12-25 15:33:12",
            }
        ],
        "next_cursor": "100",
        "has_more": true,
        "page_size": 100
    }
}
```
