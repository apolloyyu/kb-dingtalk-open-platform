---
title: "根据指定条件查询跟进记录数据"
source_url: "https://open.dingtalk.com/document/development/query-and-dingtalk-data-of-track-records-in-apsara-stack"
namespace: "development"
slug: "query-and-dingtalk-data-of-track-records-in-apsara-stack"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 跟进记录 > 根据指定条件查询跟进记录数据"
doc_id: "RO3Ytp4ye8"
updated_at: "2026-06-08 09:53:23"
---

> Source: https://open.dingtalk.com/document/development/query-and-dingtalk-data-of-track-records-in-apsara-stack
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 跟进记录 > 根据指定条件查询跟进记录数据
> Updated: 2026-06-08 09:53:23

# 根据指定条件查询跟进记录数据

调用本接口，根据指定查询条件批量获取跟进记录数据，最多可一次获取200条数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-CRM主数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | user01 | 用户userId。 |
| cursor | String | 否 | 0 | 分页游标。 |
| page\_size | Number | 是 | 100 | 分页大小。 |
| query\_dsl | String | 否 | {\"filterGroupJSONType\":\"AND\",\"needCount\":\"true\",\"groupLogicType\":\"AND\"} | 查询条件，格式参考[查询DSL说明](1393-inner-query-dsl-description.md)。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7dad1a09-ffcb-4263-bdb1-d3b7dd55f749' \
-d 'current_operator_userid=user01' \
-d 'cursor=0' \
-d 'page_size=30' \
-d 'query_dsl=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query");
OapiCrmObjectdataFollowrecordQueryRequest req = new OapiCrmObjectdataFollowrecordQueryRequest();
req.setCurrentOperatorUserid("user01");
req.setCursor("0");
req.setPageSize(100L);
req.setQueryDsl("{\"filterGroupJSONType\":\"AND\",\"needCount\":\"true\",\"groupLogicType\":\"AND\"}");
OapiCrmObjectdataFollowrecordQueryResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectdataFollowrecordQueryRequest("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query")

req.current_operator_userid="ding_userid"
req.cursor="0"
req.page_size=100
req.query_dsl="{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}"
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiCrmObjectdataFollowrecordQueryRequest;
$req->setCurrentOperatorUserid("ding_userid");
$req->setCursor("0");
$req->setPageSize("100");
$req->setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/followrecord/query");
OapiCrmObjectdataFollowrecordQueryRequest req = new OapiCrmObjectdataFollowrecordQueryRequest();
req.CurrentOperatorUserid = "user01";
req.Cursor = "0";
req.PageSize = 100L;
req.QueryDsl = "{\"filterGroupJSONType\":\"AND\",\"needCount\":\"true\",\"groupLogicType\":\"AND\"}";
OapiCrmObjectdataFollowrecordQueryResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | IterablePage |  | 分页结果。 |
| next\_cursor | String | 100 | 下一页的游标。 |
| values | Values[] |  | 数据列表。 |
| creator\_nick | String | 张xx | 创建记录的用户昵称。 |
| gmt\_modified | String | 2019-12-25 15:33:12 | 记录修改时间。 |
| creator\_userid | String | user01 | 创建记录的用户userId。 |
| instance\_id | String | INST\_XX | 数据ID。 |
| data | String | {\"follow\_record\_related\_customer\":\"related\_instance\_id\",\"follow\_record\_related\_contact\":\"related\_instance\_id\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2019-12-25 15:33:12 | 记录创建时间。 |
| object\_type | String | crm\_follow\_record | 数据类型。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| owner\_userid\_list | String[] | ["user01","user02"] | 负责人用户userId列表。 |
| participant\_userid\_list | String[] | ["user01","user02"] | 协同人用户userId列表。 |
| has\_more | Boolean | true | 是否有下一页。   - **true**：有 - **false**：没有 |
| page\_size | Number | 100 | 分页大小。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "has_more": false,
    "next_cursor": "10",
    "values": [
      {
        "creator_userid": "01560506681417",
        "data": "{\"follow_record_related_customer\":{\"extendValue\":\"{\\\"quote\\\":1,\\\"list\\\":[{\\\"bizType\\\":\\\"crm_customer_personal\\\",\\\"instanceId\\\":\\\"DTwOZL_cQKmudBAi5Hoewg04931650374020\\\"}]}\",\"value\":\"[\\\"72\\\"]\"},\"follow_record_related_contact\":{\"extendValue\":\"{\\\"quote\\\":1,\\\"list\\\":[{\\\"instanceId\\\":\\\"fssmflb8SB-ZL2U7LO0c_g04931650447551\\\"}]}\",\"value\":\"[\\\"3-1\\\"]\"},\"DDSelectField-K2U5UJAC\":{\"extendValue\":\"{\\\"label\\\":\\\"当面拜访\\\",\\\"key\\\":\\\"option_K2U5VJBL\\\"}\",\"value\":\"当面拜访\"},\"DDSelectField-K2U5ZPYB\":{\"extendValue\":\"{\\\"label\\\":\\\"有需求跟进\\\",\\\"key\\\":\\\"option_1\\\"}\",\"value\":\"有需求跟进\"},\"TextareaField-K2U5UJAF\":\"1\"}",
        "extend_data": "{}",
        "gmt_create": "2022-04-21 10:21:07",
        "gmt_modified": "2022-04-21 10:21:07",
        "instance_id": "WgkO7GMpTxxxx507667",
        "object_type": "crm_follow_record",
        "permission": {
          "owner_userid_list": [
            "01560506681417"
          ],
          "participant_userid_list": [
            "01560506681417"
          ]
        }
      },
      {
        "creator_userid": "01560506681417",
        "data": "{\"follow_record_related_customer\":{\"extendValue\":\"{\\\"quote\\\":1,\\\"list\\\":[{\\\"instanceId\\\":\\\"c5baeea7-58de-4b61-882b-902aafd0b21f\\\"}]}\",\"value\":\"[\\\"1\\\"]\"},\"follow_record_related_contact\":{\"extendValue\":\"{\\\"quote\\\":1,\\\"list\\\":[{\\\"instanceId\\\":\\\"1f3b7ac1-88a6-4644-9a8e-8e6e8918e97f\\\"}]}\",\"value\":\"[\\\"1\\\"]\"},\"DDSelectField-K2U5UJAC\":{\"extendValue\":\"{\\\"label\\\":\\\"当面拜访\\\",\\\"key\\\":\\\"option_K2U5VJBL\\\"}\",\"value\":\"当面拜访\"},\"DDSelectField-K2U5ZPYB\":{\"extendValue\":\"{\\\"label\\\":\\\"有需求跟进\\\",\\\"key\\\":\\\"option_1\\\"}\",\"value\":\"有需求跟进\"},\"TextareaField-K2U5UJAF\":\"212\"}",
        "extend_data": "{}",
        "gmt_create": "2021-11-11 14:09:41",
        "gmt_modified": "2021-11-11 14:09:41",
        "instance_id": "a71b79xxxx54-d074a784ebd3",
        "object_type": "crm_follow_record",
        "permission": {
          "owner_userid_list": [
            "01560506681417"
          ],
          "participant_userid_list": []
        }
      }
    ]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
