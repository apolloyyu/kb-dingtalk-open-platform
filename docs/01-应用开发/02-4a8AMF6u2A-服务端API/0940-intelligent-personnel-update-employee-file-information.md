---
title: "更新员工花名册信息"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-update-employee-file-information"
namespace: "development"
slug: "intelligent-personnel-update-employee-file-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 花名册 > 更新员工花名册信息"
doc_id: "NRlzyHXJcI"
updated_at: "2026-05-29 09:13:56"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-update-employee-file-information
> Path: 应用开发 / 服务端API / 智能人事 > 花名册 > 更新员工花名册信息
> Updated: 2026-05-29 09:13:56

# 更新员工花名册信息

调用本接口，更新员工档案信息，支持明细分组。

## **接口调用说明**

- 调用本接口可更新员工档案信息。
- 该接口如果传入的字段是不支持更新的字段（如sys00分組内的字段，部门和直属主管），会返回 *參数错误* 的报错信息。

以更新员工花名册内的身份证姓名为例，员工小钉在智能人事花名册内的身份证姓名是**小钉**，如下图所示。![iShot2022-06-16 15](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6615735561/p449990.png)

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_manager-智能人事数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| agentid | Number | 是 | 23470561 | 应用的AgentId。   - 企业内部应用，应用详情页获取[应用 AgentId](https://open.dingtalk.com/document/orgapp/basic-concepts-beta#813cbd7067yn0)。 - 第三方企业应用，通过[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取agentid传说中。 |
| param | EmpUpdateByCustomParam | 是 |  | 员工信息。 |
| groups | EmpGroupFieldVo[] | 否 |  | 花名册分组。 |
| sections | EmpListFieldVo[] | 否 |  | 分组下明细，非明细分组仅一条明细。 |
| section | EmpFieldVo[] | 否 |  | 分组下字段列表。 |
| field\_code | String | 否 | sys01-birthTime | 更新的字段code，调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取field\_code参数值。  **[!NOTE]**   - sys00分组内字段code值为汉字，如姓名，更新时直接传入**"姓名"**作为该参数值。 - sys00分组内的字段，**部门**和**直属主管**暂不支持接口更新。 |
| value | String | 否 | 2020-10-10 | 更新的字段值。   - 如果field\_code对应字段的field\_type为**TextField**，该字段值自定义。 - 如果field\_code对应字段的field\_type为**DDDateField**，该字段值传日期格式为"yyyy-MM-dd"。 - 如果field\_code对应字段的field\_type为**DDSelectField**，该字段值传option\_text内的value。结果显示为value对应的label值。  **[!NOTE]**  例如“民族”字段获取的元数据信息如截图，此时value传1，该员工的民族会更改为“汉族”。iShot2022-02-25 10 |
| old\_index | Number | 否 | 0 | 明细下标。   - 传入该值时，表示当前传入的section为编辑员工花名册现有的第**old\_index**条明细，此时只编辑该条明细中传入的字段。 - 不传入该值时，表示当前传入的section为新增明细，此时会保存该条明细传入的字段，未传字段会清空。 |
| group\_id | String | 否 | sys01 | 分组标识，调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取group\_id参数值。 |
| userid | String | 是 | 123456 | 被更新字段信息的员工userid。  **[!NOTE]**  确保该userId是当前本企业内正确的值，否则接口会报错**系统错误**。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=577bc48c-aca8-4c24-9fc7-077128b63bd4' \
-d 'agentid=23470561' \
-d 'param=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update");
OapiSmartworkHrmEmployeeV2UpdateRequest request = new OapiSmartworkHrmEmployeeV2UpdateRequest();
request.setAgentid(23470561L);
EmpUpdateByCustomParam param = new EmpUpdateByCustomParam();
List<EmpGroupFieldVo> groups = new ArrayList<>();
EmpGroupFieldVo group = new EmpGroupFieldVo();
List<EmpListFieldVo> sections = new ArrayList<>();
EmpListFieldVo section = new EmpListFieldVo();
List<EmpFieldVo> fieldVos = new ArrayList<>();
EmpFieldVo fieldVo = new EmpFieldVo();
fieldVo.setFieldCode("test");
fieldVo.setValue("测试");
fieldVos.add(fieldVo);
section.setSection(fieldVos);
section.setOldIndex(0L);
sections.add(section);
group.setGroupId("asdsad");
group.setSections(sections);
groups.add(group);
param.setUserid("user456");
param.setGroups(groups);
request.setParam(param);
System.out.println(JSON.toJSONString(param,true));
OapiSmartworkHrmEmployeeV2UpdateResponse rsp = client.execute(request, token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiSmartworkHrmEmployeeV2UpdateRequest("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update")

req.agentid=23470561
req.param=""
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
$req = new OapiSmartworkHrmEmployeeV2UpdateRequest;
$req->setAgentid("23470561");
$param = new EmpUpdateByCustomParam;
$groups = new EmpGroupFieldVo;
$sections = new EmpListFieldVo;
$section = new EmpFieldVo;
$section->field_code="sys01-birthTime";
$section->value="2020-10-10";
$sections->section = array($section);
$sections->old_index="0";
$groups->sections = array($sections);
$groups->group_id="sys01";
$param->groups = array($groups);
$param->userid="123456";
$req->setParam($param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/v2/update");
OapiSmartworkHrmEmployeeV2UpdateRequest req = new OapiSmartworkHrmEmployeeV2UpdateRequest();
req.Agentid = 23470561L;
OapiSmartworkHrmEmployeeV2UpdateRequest.EmpUpdateByCustomParamDomain obj1 = new OapiSmartworkHrmEmployeeV2UpdateRequest.EmpUpdateByCustomParamDomain();
List<OapiSmartworkHrmEmployeeV2UpdateRequest.EmpGroupFieldVoDomain> list3 = new List<OapiSmartworkHrmEmployeeV2UpdateRequest.EmpGroupFieldVoDomain>();
OapiSmartworkHrmEmployeeV2UpdateRequest.EmpGroupFieldVoDomain obj4 = new OapiSmartworkHrmEmployeeV2UpdateRequest.EmpGroupFieldVoDomain();
list3.Add(obj4);
List<OapiSmartworkHrmEmployeeV2UpdateRequest.EmpListFieldVoDomain> list6 = new List<OapiSmartworkHrmEmployeeV2UpdateRequest.EmpListFieldVoDomain>();
OapiSmartworkHrmEmployeeV2UpdateRequest.EmpListFieldVoDomain obj7 = new OapiSmartworkHrmEmployeeV2UpdateRequest.EmpListFieldVoDomain();
list6.Add(obj7);
List<OapiSmartworkHrmEmployeeV2UpdateRequest.EmpFieldVoDomain> list9 = new List<OapiSmartworkHrmEmployeeV2UpdateRequest.EmpFieldVoDomain>();
OapiSmartworkHrmEmployeeV2UpdateRequest.EmpFieldVoDomain obj10 = new OapiSmartworkHrmEmployeeV2UpdateRequest.EmpFieldVoDomain();
list9.Add(obj10);
obj10.FieldCode = "sys01-birthTime";
obj10.Value = "2020-10-10";
obj7.Section= list9;
obj7.OldIndex = 0L;
obj4.Sections= list6;
obj4.GroupId = "sys01";
obj1.Groups= list3;
obj1.Userid = "123456";
req.Param_ = obj1;
OapiSmartworkHrmEmployeeV2UpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 更新是否成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 接口调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 调用失败时返回的错误信息。 |
| request\_id | String | 8badquf9r90f | 请求ID。 |

### **响应体示例**

```
{
  "result": true,
  "errcode": 0,
  "success": true,
  "errmsg" : "ok"
  "request_id": "8badquf9r90f"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
