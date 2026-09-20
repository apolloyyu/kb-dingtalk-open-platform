---
title: "更新自定义对象数据"
source_url: "https://open.dingtalk.com/document/development/crm-master-data-opens-interface-for-updating-custom-object-data"
namespace: "development"
slug: "crm-master-data-opens-interface-for-updating-custom-object-data"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 自定义对象 > 更新自定义对象数据"
doc_id: "ZQ3qGl80Y0"
updated_at: "2026-06-08 09:53:20"
---

> Source: https://open.dingtalk.com/document/development/crm-master-data-opens-interface-for-updating-custom-object-data
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 自定义对象 > 更新自定义对象数据
> Updated: 2026-06-08 09:53:20

# 更新自定义对象数据

调用本接口，更新CRM自定义对象数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_customdata\_write-CRM自定义对象数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| instance | ObjectDataInstanceVo | 是 |  | 自定义对象数据。 |
| data | String | 是 | {\"contact\_name\":\"李四\"} | 数据内容。 |
| extend\_data | String | 否 | {\"field\_1\":\"CRM\"} | 扩展数据内容。 |
| permission | DataPermissionVo | 否 |  | 权限。 |
| participant\_userids | String[] | 否 | ["123","456"] | 协同人的用户userId。 |
| instance\_id | String | 是 | INST\_XX | 自定义对象数据ID，可通过[根据指定条件查询自定义对象数据](1377-api-getobjectdata.md)接口获取instance\_id参数值。 |
| form\_code | String | 是 | PROC-EFxxxx | 自定义对象表单code，进入自定义表单编辑页面，最下方可查看。iShot2022-11-01 20 |
| modifier\_userid | String | 是 | user01 | 钉钉用户userId。 |
| modifier\_nick | String | 否 | 张xx | 钉钉用户nick。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=01da3b0f-35fc-4e3b-a9ee-6d080beb2c58' \
-d 'instance=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update");
OapiCrmObjectdataCustomobjectUpdateRequest req = new OapiCrmObjectdataCustomobjectUpdateRequest();
ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
DataPermissionVo dataPermissionVo = new DataPermissionVo();
dataPermissionVo.setParticipantUserids(Arrays.asList("user01", "user02"));
objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
objectDataInstanceVo.setPermission(dataPermissionVo);
objectDataInstanceVo.setInstanceId("INST_XX");
objectDataInstanceVo.setFormCode("PROC-EFxxxx");
objectDataInstanceVo.setModifierUserid("user01");
objectDataInstanceVo.setModifierNick("张xx");
req.setInstance(objectDataInstanceVo);
OapiCrmObjectdataCustomobjectUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiCrmObjectdataCustomobjectUpdateRequest("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update")

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
$req = new OapiCrmObjectdataCustomobjectUpdateRequest;
$instance = new ObjectDataInstanceVo;
$permission = new DataPermissionVo;
$permission->participant_userids="[\"123\",\"456\"]";
$permission->owner_userids="[\"123\",\"456\"]";
$instance->permission = $permission;
$instance->instance_id="instance_id";
$instance->form_code="form_code";
$instance->modifier_userid="钉钉userId";
$instance->modifier_nick="张三";
$req->setInstance($instance);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customobject/update");
OapiCrmObjectdataCustomobjectUpdateRequest req = new OapiCrmObjectdataCustomobjectUpdateRequest();
ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
DataPermissionVo dataPermissionVo = new DataPermissionVo();
dataPermissionVo.ParticipantUserids = new List<string> { "user01", "user02" };
objectDataInstanceVo.ExtendData = "{\"field_1\":\"CRM\"}";
objectDataInstanceVo.Permission = dataPermissionVo;
objectDataInstanceVo.InstanceId = "INST_XX";
objectDataInstanceVo.FormCode = "PROC-EFxxxx";
objectDataInstanceVo.ModifierUserid = "user01";
objectDataInstanceVo.ModifierNick = "张xx";
req.Instance = objectDataInstanceVo;
OapiCrmObjectdataCustomobjectUpdateResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataCreateDto |  | 返回结果。 |
| instance\_id | String | INST\_XX | 自定义对象数据ID。 |
| success | Boolean | true | 是否更新成功。   - **true**：成功 - **false**：失败 |
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
