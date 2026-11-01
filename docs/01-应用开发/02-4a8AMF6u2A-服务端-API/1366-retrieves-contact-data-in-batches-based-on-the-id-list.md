---
title: "按照ID列表批量获取联系人数据"
source_url: "https://open.dingtalk.com/document/development/retrieves-contact-data-in-batches-based-on-the-id-list"
namespace: "development"
slug: "retrieves-contact-data-in-batches-based-on-the-id-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 联系人管理 > 按照ID列表批量获取联系人数据"
doc_id: "AAf00PI4WI"
updated_at: "2026-06-08 09:53:25"
---

> Source: https://open.dingtalk.com/document/development/retrieves-contact-data-in-batches-based-on-the-id-list
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 联系人管理 > 按照ID列表批量获取联系人数据
> Updated: 2026-06-08 09:53:25

# 按照ID列表批量获取联系人数据

调用本接口，根据联系人实例id列表批量获取联系人数据，最多可一次获取200条数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_read-CRM主数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | manager1 | 操作人用户userId。 |
| data\_id\_list | String | 是 | inst\_Id1, inst\_Id2 | 数据ID列表，通过[根据指定条件查询联系人数据](1365-api-getcontacts.md)接口获取instance\_id参数值，多个用英文逗号隔开。 |
| provider\_corpid | String | 否 | dingxxxx | 自建应用时传入服务商corpId。CorpId |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7dad1a09-ffcb-4263-bdb1-d3b7dd55f749' \
-d 'current_operator_userid=manager1' \
-d 'data_id_list=1' \
-d 'provider_corpid=dingxxxx'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list");
OapiCrmObjectdataContactListRequest req = new OapiCrmObjectdataContactListRequest();
req.setCurrentOperatorUserid("manager1");
req.setDataIdList("nst_Id1, inst_Id2");
req.setProviderCorpid("dingxxxx");
OapiCrmObjectdataContactListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectdataContactListRequest("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list")

req.current_operator_userid="ding_userid"
req.data_id_list="instance_id"
req.provider_corpid="dingxx"
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
$req = new OapiCrmObjectdataContactListRequest;
$req->setCurrentOperatorUserid("ding_userid");
$req->setDataIdList("instance_id");
$req->setProviderCorpid("dingxx");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/list");
OapiCrmObjectdataContactListRequest req = new OapiCrmObjectdataContactListRequest();
req.CurrentOperatorUserid = "manager1";
req.DataIdList = "nst_Id1, inst_Id2";
req.ProviderCorpid = "dingxxxx";
OapiCrmObjectdataContactListResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result\_list | ObjectDataInstanceVo[] |  | 实例数据。 |
| gmt\_modified | String | 2020-09-15 00:00:00 | 修改时间。 |
| creator\_userid | String | user1 | 创建人的用户userId。 |
| instance\_id | String | nst\_Id1 | 数据ID。 |
| data | String | {\"customer\_name\":\"XX有限公司\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2020-09-15 00:00:00 | 记录创建时间。 |
| object\_type | String | crm\_contact | 数据类型。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| participant\_userid\_list | String[] | ["user01","user02"] | 协同人用户ID列表。 |
| owner\_userid\_list | String[] | ["user01","user02"] | 负责人用户ID列表 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result_list": [
    {
      "creator_userid": "user1",
      "data": "{\"contact_related_customer\":{\"extendValue\":\"{\\\"quote\\\":\\\"1\\\",\\\"bizType\\\":\\\"crm_customer\\\",\\\"list\\\":[{\\\"instanceId\\\":\\\"c5baeea7-58de-4b61-882b-902aafd0b212\\\"}]}\",\"value\":\"[\\\"1\\\"]\"},\"contact_name\":\"联系人1\",\"contact_position\":{\"extendValue\":\"[{\\\"label\\\":\\\"老板\\\",\\\"key\\\":\\\"option_1\\\"}]\",\"value\":\"[\\\"老板\\\"]\"},\"contact_phone\":{\"extendValue\":\"{\\\"mode\\\":\\\"phone\\\",\\\"countryKey\\\":\\\"CN\\\",\\\"flag\\\":\\\"C\\\",\\\"countryCode\\\":\\\"+86\\\",\\\"areaNumber\\\":\\\"\\\",\\\"flagPy\\\":\\\"Z\\\",\\\"countryName\\\":\\\"China\\\",\\\"countryNameZh\\\":\\\"中国\\\",\\\"countryNamePy\\\":\\\"ZHONGGUO\\\"}\",\"value\":\"136********\"}}",
      "extend_data": "{\"contactUserId\":\"userId02\",\"contactUnionId\":\"unionId02\"}",
      "gmt_create": "2020-09-15 00:00:00",
      "gmt_modified": "2020-09-15 00:00:00",
      "instance_id": "inst_Id1",
      "object_type": "crm_contact",
      "permission": {
        "owner_userid_list": [
          "user01",
          "user02"
        ],
        "participant_userid_list": [
          "user01",
          "user02"
        ]
      }
    }
  ],
  "errcode": 0,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
