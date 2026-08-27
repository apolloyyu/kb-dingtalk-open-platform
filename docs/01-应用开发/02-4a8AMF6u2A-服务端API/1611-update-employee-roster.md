---
title: "更新员工花名册"
source_url: "https://open.dingtalk.com/document/development/update-employee-roster"
namespace: "development"
slug: "update-employee-roster"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能人事 > 花名册 > 更新员工花名册"
doc_id: "QSOMK1JTw8"
updated_at: "2026-08-25 09:39:07"
---

> Source: https://open.dingtalk.com/document/development/update-employee-roster
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能人事 > 花名册 > 更新员工花名册
> Updated: 2026-08-25 09:39:07

# 更新员工花名册

调用本接口更新指定员工的花名册信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新员工花名册信息](0940-intelligent-personnel-update-employee-file-information.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端接口的授权凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| param | UnionExportParam | 是 |  | 修改员工信息。 |
| userid | String | 是 | manager781 | 员工userid。 |
| groups | GroupMetaInfo[] | 否 |  | 组明细。 |
| group\_id | String | 否 | sys01 | 需改的字段所在组ID。 |
| sections | EmpListFieldVO[] | 否 |  | 同类型组明细。 |
| section | EmpFieldVo[] | 否 |  | 单个组所有字段。 |
| value | String | 否 | 123123 | 更新的字段值。 |
| field\_code | String | 否 | sys01-dept | 更新的字段code。 |
| agentid | Number | 是 | 23470561 | 应用的AgentID，可在开发者后台的应用详情页获取应用ID。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 修改是否成功。 |
| errcode | Number | ok | 返回码。 |
| errmsg | String | 0 | 返回码描述。 |
| success | Boolean | true | 调用结果。 |
| request\_id | String | dzqwpok9463f | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "agentid": "868810166",
  "param": {
    "groups": [{
      "group_id": "sys02",
      "sections": [{
        "section": [{
          "field_code": "sys01-dept",
          "value": "研发部"
        }]
      }]
    }],
    "userid": "user123"
  }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/update");
OapiSmartworkHrmEmployeeUpdateRequest req = new OapiSmartworkHrmEmployeeUpdateRequest();
PreEntryEmployeeAddParam param = new PreEntryEmployeeAddParam();
param.setUserid("user123");
OapiSmartworkHrmEmployeeUpdateRequest.GroupMetaInfo groupMetaInfo = new OapiSmartworkHrmEmployeeUpdateRequest.GroupMetaInfo();
groupMetaInfo.setGroupId("sys02");
EmpListFieldVO empListFieldVO = new EmpListFieldVO();
EmpFieldVo empFieldVo = new EmpFieldVo();
empFieldVo.setFieldCode("sys01-dept");
empFieldVo.setValue("研发部");
empListFieldVO.setSection(Arrays.asList(empFieldVo));
groupMetaInfo.setSections(Arrays.asList(empListFieldVO));
param.setGroups(Arrays.asList(groupMetaInfo));
req.setParam(param);
req.setAgentid(868810166L);
OapiSmartworkHrmEmployeeUpdateResponse rsp = client.execute(req, "access_token");
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": true,
  "success": true,
  "request_id": "dzqwpok9463f"
}
```
