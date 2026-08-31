---
title: "创建部门"
source_url: "https://open.dingtalk.com/document/development/create-a-department"
namespace: "development"
slug: "create-a-department"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 创建部门"
doc_id: "JBVy4AWFMM"
updated_at: "2026-08-25 09:37:02"
---

> Source: https://open.dingtalk.com/document/development/create-a-department
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 创建部门
> Updated: 2026-08-25 09:37:02

# 创建部门

调用本接口创建新部门。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[创建部门](0077-address-book-creation-department-established-department.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/department/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| name | String | 是 | 文档部门 | 部门名称。  长度限制为1~64个字符，不允许包含字符"-"","以及","。 |
| parentid | String | 是 | 123 | 父部门ID，根部门ID为1。 |
| parentBalanceFirst | Boolean | 否 | false | 是否优先使用父部门的预算。 |
| shareBalance | Boolean | 否 | false | 是否共享预算：   - **true**：是 - **false**：否 |
| autoApproveApply | Boolean | 否 | false | 是否默认同意加入该部门的申请：   - **true：**表示加入该部门的申请将默认同意 - **false：**表示加入该部门的申请需要有权限的管理员同意 |
| outerPermitUsers | String | 否 | 111|222 | **outerDept**为**true**时，可以配置额外可见人，值为userid组成的的字符串，使用“|”符号进行分隔，总数不能超过200。 |
| outerPermitDepts | String | 否 | 12|13 | **outerDept**为**true**时，可以配置额外可见部门，值为部门id组成的的字符串，使用“|”符号进行分隔，总数不能超过200。 |
| outerDept | Boolean | 否 | false | 是否限制本部门成员查看通讯录：   - **true**：开启限制，开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制 |
| deptHiding | Boolean | 否 | false | 是否隐藏部门：   - **true**：表示隐藏 - **false**：表示显示 |
| createDeptGroup | Boolean | 否 | false | 是否创建一个关联此部门的企业群，默认为false。 |
| order | String | 否 | 1 | 在父部门中的次序值。order值小的排序靠前。 |
| sourceIdentifier | String | 否 | 111 | 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。 |
| deptPermits | String | 否 | 12|13 | 可以查看指定隐藏部门的其他部门列表，如果部门隐藏，则此值生效，取值为其他的部门ID组成的的字符串，使用"|"符号进行分隔。总数不能超过200。 |
| userPermits | String | 否 | 111|222 | 可以查看指定隐藏部门的其他人员列表，如果部门隐藏，则此值生效，取值为其他的人员userid组成的的字符串，使用"|"符号进行分隔。总数不能超过200。 |
| outerDeptOnlySelf | Boolean | 否 | true | 是否只能看到所在部门及下级部门通讯录：   - **true**：表示只能看到所在部门及下级部门通讯录 - **false**：不能查看所在部门及下级部门通讯录   **[!NOTE]**  outerDept为true时，可以配置该字段。 |
| ext | String | 否 | {\"职能\":\"人事\"} | 部门自定义字段，格式为文本类型的Json格式。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| id | Number | 400887483 | 部门ID。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/department/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "name": "管理3部",
  "parentid": "1",
  "outerDept": "true",
  "outerPermitUsers": "manager4220|user123",
  "ext": "{\"职能\":\"总裁办\"}"

}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/department/create");
OapiDepartmentCreateRequest req = new OapiDepartmentCreateRequest();
req.setParentid("1");
req.setParentBalanceFirst(false);
req.setShareBalance(false);
req.setOuterPermitUsers("manager4220|user123");
req.setOuterPermitDepts("12|13");
req.setOuterDept(true);
req.setDeptHiding(false);
req.setCreateDeptGroup(false);
req.setOrder("1");
req.setName("管理3部");
req.setSourceIdentifier("111");
req.setDeptPermits("12|13");
req.setUserPermits("111|222");
req.setOuterDeptOnlySelf(false);
OapiDepartmentCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "id":400887483
}
```
