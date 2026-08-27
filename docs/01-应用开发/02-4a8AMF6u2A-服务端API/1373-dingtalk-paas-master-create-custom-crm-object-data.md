---
title: "创建CRM自定义对象数据"
source_url: "https://open.dingtalk.com/document/development/dingtalk-paas-master-create-custom-crm-object-data"
namespace: "development"
slug: "dingtalk-paas-master-create-custom-crm-object-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 自定义对象 > 创建CRM自定义对象数据"
doc_id: "WfIz7fmyr4"
updated_at: "2026-06-08 09:53:21"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-paas-master-create-custom-crm-object-data
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 自定义对象 > 创建CRM自定义对象数据
> Updated: 2026-06-08 09:53:21

# 创建CRM自定义对象数据

调用本接口，向自定义表单内创建对象数据。

## **接口调用说明**

本接口只能创建纯表单数据，不能用于创建流程表单数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_customdata\_write-CRM自定义对象数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| instance | ObjectDataInstanceVo | 是 |  | 自定义对象数据。 |
| creator\_userid | String | 是 | user01 | 创建人的用户userId。 |
| data | String | 是 | {"TextField-xxxxxx":"李四"} | 数据内容，JSON格式字符串。传参格式详见[自定义控件字段格式说明V1](1387-custom-control-field-format-description-v1.md)。 |
| extend\_data | String | 否 | {"field\_1":"CRM"} | 扩展数据内容。 |
| permission | DataPermissionVo | 否 |  | 权限。 |
| participant\_userids | String[] | 否 | ["user01","user02"] | 协同人的用户userId。 |
| form\_code | String | 是 | PROC-A1xxxx | 自定义对象表单code，进入自定义表单编辑页面，最下方可查看。  iShot2022-11-01 20 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=4525b0a0-669c-4b58-9185-d4517b647e8b' \
-d 'instance=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create");
OapiCrmObjectdataCustomobjectCreateRequest req = new OapiCrmObjectdataCustomobjectCreateRequest();
ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
objectDataInstanceVo.setCreatorUserid("user01");
objectDataInstanceVo.setData("{\"TextField-xxxxxx\":\"李xx\"}");
objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
DataPermissionVo dataPermissionVo = new DataPermissionVo();
dataPermissionVo.setParticipantUserids(Arrays.asList("user01", "user02"));
objectDataInstanceVo.setPermission(dataPermissionVo);
objectDataInstanceVo.setFormCode("PROC-A1xxxx");
req.setInstance(objectDataInstanceVo);
OapiCrmObjectdataCustomobjectCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectdataCustomobjectCreateRequest("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create")

req.instance=""
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
$req = new OapiCrmObjectdataCustomobjectCreateRequest;
$instance = new ObjectDataInstanceVo;
$instance->creator_userid="ding_userid";
$instance->creator_nick="张三";
$permission = new DataPermissionVo;
$permission->participant_userids="[\"123\",\"456\"]";
$permission->owner_userids="[\"123\",\"456\"]";
$instance->permission = $permission;
$instance->form_code="form_code";
$req->setInstance($instance);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/create");
OapiCrmObjectdataCustomobjectCreateRequest req = new OapiCrmObjectdataCustomobjectCreateRequest();
OapiCrmObjectdataCustomobjectCreateRequest.ObjectDataInstanceVoDomain obj1 = new OapiCrmObjectdataCustomobjectCreateRequest.ObjectDataInstanceVoDomain();
obj1.CreatorUserid = "ding_userid";
obj1.CreatorNick = "张三";
OapiCrmObjectdataCustomobjectCreateRequest.DataPermissionVoDomain obj2 = new OapiCrmObjectdataCustomobjectCreateRequest.DataPermissionVoDomain();
obj2.ParticipantUserids = ""123","456"";
obj2.OwnerUserids = ""123","456"";
obj1.Permission= obj2;
obj1.FormCode = "form_code";
req.Instance_ = obj1;
OapiCrmObjectdataCustomobjectCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataCreateDto |  | 返回结果。 |
| instance\_id | String | INST\_XX | 自定义对象数据ID。 |
| success | Boolean | true | 是否执行成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result": {
    "instance_id": "INST_XX"
  },
  "errcode": 0,
  "success": true,
  "errmsg": "ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
