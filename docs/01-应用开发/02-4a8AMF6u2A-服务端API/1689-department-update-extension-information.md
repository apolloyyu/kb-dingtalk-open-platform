---
title: "更新部门扩展信息"
source_url: "https://open.dingtalk.com/document/development/department-update-extension-information"
namespace: "development"
slug: "department-update-extension-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 组织 > 更新部门扩展信息"
doc_id: "tyyWEG6fxX"
updated_at: "2025-09-08 19:04:14"
---

> Source: https://open.dingtalk.com/document/development/department-update-extension-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 组织 > 更新部门扩展信息
> Updated: 2025-09-08 19:04:14

# 更新部门扩展信息

调用本接口根据部门ID更新部门扩展信息。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，智能人事组织接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 组织接口相关文档，已于**2021年11月24日**移动至**历史文档（不推荐）**目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/smartwork/hrm/organization/dept/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| attributeVOS | OrgDeptAttributeVo[] | 否 |  | 扩展信息。 |
| field\_value | String | 是 | 2 | 字段值。 |
| field\_code | String | 是 | deptLevel | 字段code。 |
| dept\_id | Number | 是 | 1995 | 部门ID，可通过[获取部门列表](https://open.dingtalk.com/document/orgapp/obtain-the-department-list)接口获取。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 请求是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | dzqwpok9463f | 请求ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/smartwork/hrm/organization/dept/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "dept_id": 1995,
    "attributeVOS": [
        {
            "field_code": "deptLevel",
            "field_value": "2"
        }
    ]
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/smartwork/hrm/organization/dept/update");
OapiSmartworkHrmOrganizationDeptUpdateRequest req = new OapiSmartworkHrmOrganizationDeptUpdateRequest();
List<OrgDeptAttributeVo> attributeVOS = new ArrayList<OrgDeptAttributeVo>();
OrgDeptAttributeVo attributeVo = new OrgDeptAttributeVo();
attributeVo.setFieldValue("2");
attributeVo.setFieldCode("deptLevel");
attributeVOS.add(attributeVo);
req.setAttributeVOS(attributeVOS);
req.setDeptId(1995L);
OapiSmartworkHrmOrganizationDeptUpdateResponse rsp = client.execute(req,access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
        "errcode":0,
        "success":true,
        "request_id": "dzqwpok9463f"
}
```
