---
title: "获取员工离职信息"
source_url: "https://open.dingtalk.com/document/development/obtain-multiple-employee-demission-information"
namespace: "development"
slug: "obtain-multiple-employee-demission-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 智能人事 > 员工管理 > 获取员工离职信息"
doc_id: "cd5VRixRYu"
updated_at: "2026-08-25 09:39:10"
---

> Source: https://open.dingtalk.com/document/development/obtain-multiple-employee-demission-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 智能人事 > 员工管理 > 获取员工离职信息
> Updated: 2026-08-25 09:39:10

# 获取员工离职信息

调用本接口根据传入的userid列表，批量查询员工的离职信息。

> **[!IMPORTANT]**
>
> - 浏览器可能会转义某些字符导致请求失败，调试时请使用curl或者代码模拟请求。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[批量获取员工离职信息](0949-obtain-resignation-information-of-employees-new-version.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 是 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/listdimission`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用可通过[服务商获取第三方应用授权企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid\_list | String | 是 | user123,user456 | 要查询的离职员工userid，多个员工用逗号分隔，最大长度50，通过[获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md)接口获取data\_list参数值。  如果传入为非离职员工userid，不会返回信息。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | EmpDimissionInfoVo[] | [] | 返回结果。 |
| userid | String | 123 | 离职员工的userid。 |
| last\_work\_day | Number | 1534569419008 | 最后工作日。 |
| dept\_list | EmpDeptVO[] |  | 离职部门列表。 |
| dept\_path | String | 技术支持 | 部门名称。 |
| dept\_id | Number | 399388496 | 部门ID。 |
| reason\_memo | String | 世界太大想去看看 | 离职原因备注 |
| reason\_type | Number | 1 | 离职原因类型：   - **1**：家庭原因 - **2**：个人原因 - **3**：发展原因 - **4**：合同到期不续签 - **5**：协议解除 - **6**：无法胜任工作 - **7**：经济性裁员 - **8**：严重违法违纪 - **9**：其他   **[!NOTE]**  由于智能人事产品升级，请根据实际使用产品确定是否返回该字段：   - 升级后产品如下图所示，产品可以自定义离职原因，调用本接口不会返回该字段。8269D655-1822-4731-9A57-7430A062C2A6 - 升级前，调用接口返回该字段。 |
| pre\_status | Number | 1 | 离职前工作状态：   - **1**：待入职 - **2**：试用期 - **3**：正式 |
| handover\_userid | String | manager123 | 离职交接人的userid。 |
| status | Number | 2 | 离职状态：   - **1**：待离职 - **2**：已离职 - **3**：未离职 - **4**：发起离职审批但还未通过 - **5**：失效（离职流程被其他流程强制终止后的状态） |
| main\_dept\_name | String | 技术支持 | 离职前主部门名称。 |
| main\_dept\_id | Number | 399388496 | 离职前主部门ID。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 是否调用成功。   - **true**：成功 - **false**：失败 |
| request\_id | String | u257sw0hr54 | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/listdimission?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "userid_list": "user123,user456"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/employee/listdimission");
OapiSmartworkHrmEmployeeListdimissionRequest req = new OapiSmartworkHrmEmployeeListdimissionRequest();
req.setUseridList("user123,user456");
OapiSmartworkHrmEmployeeListdimissionResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": [
    {
      "dept_list": [
        {
          "dept_id": 399388496,
          "dept_path": "技术支持"
        }
      ],
      "handover_userid": "manager4220",
      "last_work_day": 1599494400000,
      "main_dept_id": 399388496,
      "main_dept_name": "技术支持",
      "pre_status": 3,
      "reason_memo": "世界太大想去看看",
      "reason_type":1,
      "status": 2,
      "userid": "66220007745510"
    }
  ],
  "success": true,
  "request_id": "6i7hj9622udt"
}
```
