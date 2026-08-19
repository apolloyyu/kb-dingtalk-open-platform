---
title: "按照ID列表批量获取CRM自定义表单数据"
source_url: "https://open.dingtalk.com/document/development/retrieves-custom-crm-forms-from-the-id-list"
namespace: "development"
slug: "retrieves-custom-crm-forms-from-the-id-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 自定义对象 > 按照ID列表批量获取CRM自定义表单数据"
doc_id: "L16vJSM1cP"
updated_at: "2026-06-08 09:53:18"
---

> Source: https://open.dingtalk.com/document/development/retrieves-custom-crm-forms-from-the-id-list
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 自定义对象 > 按照ID列表批量获取CRM自定义表单数据
> Updated: 2026-06-08 09:53:18

# 按照ID列表批量获取CRM自定义表单数据

调用本接口，根据实例ID列表批量获取CRM自定义对象数据，最多可一次获取200条数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectdata/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_customdata\_read-CRM自定义对象数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| current\_operator\_userid | String | 否 | user01 | 操作人用户userId。 |
| data\_id\_list | String | 是 | INST\_XX1,INST\_XX2 | 数据ID列表，多个用英文逗号隔开，可通过[根据指定条件查询自定义对象数据](1377-api-getobjectdata.md)接口获取instance\_id参数值。 |
| name | String | 是 | PROC-EFxxxx | 表单code，进入表单编辑页面，最下方可查看。iShot2022-11-01 20 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectdata/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7dad1a09-ffcb-4263-bdb1-d3b7dd55f749' \
-d 'current_operator_userid=user01' \
-d 'data_id_list=INST_XX1' \
-d 'name=PROC-EFxxxx'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/list");
OapiCrmObjectdataListRequest req = new OapiCrmObjectdataListRequest();
req.setCurrentOperatorUserid("user01");
req.setDataIdList("INST_XX1,INST_XX2");
req.setName("PROC-EFxxxx");
OapiCrmObjectdataListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectdataListRequest("https://oapi.dingtalk.com/topapi/crm/objectdata/list")

req.current_operator_userid="ding_userid"
req.data_id_list="instance_id"
req.name="PROC-10F2D9A2-0A44-4B42-B6B4-5EE9813507C5"
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
$req = new OapiCrmObjectdataListRequest;
$req->setCurrentOperatorUserid("ding_userid");
$req->setDataIdList("instance_id");
$req->setName("PROC-10F2D9A2-0A44-4B42-B6B4-5EE9813507C5");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectdata/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/list");
OapiCrmObjectdataListRequest req = new OapiCrmObjectdataListRequest();
req.CurrentOperatorUserid = "user01";
req.DataIdList = "INST_XX1,INST_XX2";
req.Name = "PROC-EFxxxx";

OapiCrmObjectdataListResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result\_list | ObjectDataInstanceVo[] |  | 实例数据。 |
| creator\_nick | String | 张xx | 记录创建人的昵称。 |
| gmt\_modified | String | 2019-12-25 15:33:12 | 修改时间。 |
| creator\_userid | String | user01 | 创建人的用户userId。 |
| instance\_id | String | INST\_XX | 数据ID。 |
| data | String | {\"contact\_name\":\"李四\"} | 数据内容。 |
| extend\_data | String | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| gmt\_create | String | 2019-12-25 15:33:12 | 记录创建时间。 |
| object\_type | String | crm\_follow\_record | 数据类型。 |
| permission | DataPermissionVo |  | 数据权限信息。 |
| participant\_userid\_list | String[] | ["user01","user02"] | 协同人用户userId列表。 |
| owner\_userid\_list | String[] | ["user01","user02"] | 负责人用户userId列表。 |
| proc\_out\_result | String | agree | 审批结果。 |
| proc\_inst\_status | String | COMPLETE | 审批状态。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result_list": [
    {
      "creator_userid": "015605066814171",
      "data": "{\"contract_no\":{\"value\":\"HT2022042100000003\"},\"contract_name\":\"1\",\"contract_related_customer\":{\"extendValue\":\"{\\\"quote\\\":1,\\\"list\\\":[{\\\"bizType\\\":\\\"crm_customer_personal\\\",\\\"instanceId\\\":\\\"IGpNsR_mTtuKqx7fGienmg04931650374020\\\"}]}\",\"value\":\"[\\\"82\\\"]\"},\"contract_amount\":2.0,\"contract_status\":{\"extendValue\":\"{\\\"extension\\\":{\\\"editFreeze\\\":true},\\\"label\\\":\\\"已作废\\\",\\\"key\\\":\\\"option_canceled\\\"}\",\"value\":\"已作废\"},\"DDDateField-KI5RLXW2\":1650470400000}",
      "gmt_create": "2022-04-21 10:06:55",
      "gmt_modified": "2022-04-21 10:06:55",
      "instance_id": "INST_XX1",
      "permission": {
        "owner_userid_list": [],
        "participant_userid_list": []
      },
      "proc_inst_status": "RUNNING"
    },
    {
      "creator_userid": "015605066814171",
      "data": "{\"contract_no\":{\"value\":\"HT2022031700000001\"},\"contract_name\":\"1\",\"contract_related_customer\":{\"extendValue\":\"{\\\"quote\\\":1,\\\"list\\\":[{\\\"bizType\\\":\\\"crm_customer_personal\\\",\\\"instanceId\\\":\\\"45a1ade5-9aea-4767-a7be-5592fc8b49ab\\\"}]}\",\"value\":\"[\\\"好的111\\\"]\"},\"contract_amount\":1.0,\"contract_status\":{\"extendValue\":\"{\\\"extension\\\":{\\\"editFreeze\\\":true},\\\"label\\\":\\\"未开始\\\",\\\"key\\\":\\\"option_not_started\\\"}\",\"value\":\"未开始\"},\"DDDateField-KI5RLXW2\":1647446400000}",
      "gmt_create": "2022-03-17 16:34:10",
      "gmt_modified": "2022-03-17 16:34:10",
      "instance_id": "INST_XX2",
      "permission": {
        "owner_userid_list": [
          "015605066814171"
        ],
        "participant_userid_list": [
          "015605066814171"
        ]
      },
      "proc_inst_status": "RUNNING"
    }
  ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
