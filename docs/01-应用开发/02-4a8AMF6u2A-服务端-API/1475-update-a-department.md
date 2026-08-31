---
title: "更新部门"
source_url: "https://open.dingtalk.com/document/development/update-a-department"
namespace: "development"
slug: "update-a-department"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 更新部门"
doc_id: "D1kZuS555D"
updated_at: "2026-08-25 09:37:04"
---

> Source: https://open.dingtalk.com/document/development/update-a-department
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 通讯录管理 > 部门管理1.0(不推荐) > 更新部门
> Updated: 2026-08-25 09:37:04

# 更新部门

调用本接口更新部门信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[更新部门](0078-address-book-update-department.md)接口，已接入用户不受影响。

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 否 | — |
| 第三方个人应用 | 否 | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/department/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用服务端API的应用凭证，可通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| id | Number | 是 | 420727358 | 部门ID，可调用[获取部门列表](1469-obtain-the-department-list.md)接口获取。 |
| orgDeptOwner | String | 否 | manager420 | 企业群群主的userid。 |
| outerPermitUsers | String | 否 | 111|222 | **outerDept**为**true**时，可以配置额外可见人，值为userid组成的的字符串，使用“|”符号进行分隔，总数不能超过200。 |
| outerPermitDepts | String | 否 | 12|13 | **outerDept**为**true**时，可以配置额外可见部门，值为部门id组成的的字符串，使用“|”符号进行分隔，总数不能超过200。 |
| outerDept | Boolean | 否 | true | 是否限制本部门成员查看通讯录：   - **true**：开启限制，开启后本部门成员只能看到限定范围内的通讯录 - **false**：不限制 |
| deptHiding | Boolean | 否 | true | 是否隐藏部门：   - **true**：表示隐藏 - **false**：表示显示 |
| deptManagerUseridList | String | 否 | 1 | 部门的主管列表，取值为由主管的userid组成的字符串，不同的userid使用"|"符号进行分隔。 |
| createDeptGroup | Boolean | 否 | true | 是否创建一个关联此部门的企业群，默认为false。 |
| autoAddUser | Boolean | 否 | true | 当群已经创建后，是否有新人加入部门时会自动加入该群：   - **true**：自动加入群 - **false**：不会自动加入群 |
| autoApproveApply | Boolean | 否 | false | 是否默认同意加入该部门的申请：   - **true：**表示加入该部门的申请将默认同意 - **false：**表示加入该部门的申请需要有权限的管理员同意 |
| order | String | 否 | 1 | 在父部门中的次序值，order值小的排序靠前。 |
| parentid | String | 否 | 1 | 父部门ID，1为根部门。 |
| lang | String | 否 | zh\_CN | 通讯录语言，默认zh\_CN。 |
| name | String | 否 | 1 | 部门名称。  长度限制为1~64个字符，不允许包含字符"-"","以及","。 |
| sourceIdentifier | String | 否 | 1 | 部门标识字段，开发者可用该字段来唯一标识一个部门，并与钉钉外部通讯录里的部门做映射。 |
| userPermits | String | 否 | 1|1 | 可以查看指定隐藏部门的其他人员列表，如果部门隐藏，则此值生效，取值为其他的人员userid组成的的字符串，使用"|"符号进行分隔。总数不能超过200。 |
| deptPermits | String | 否 | 1|2 | 可以查看指定隐藏部门的其他部门列表，如果部门隐藏，则此值生效，取值为其他的部门ID组成的的字符串，使用"|"符号进行分隔。总数不能超过200。 |
| outerDeptOnlySelf | Boolean | 否 | false | 是否只能看到所在部门及下级部门通讯录：   - **true**：表示只能看到所在部门及下级部门通讯录 - **false**：不能查看所在部门及下级部门通讯录   **[!NOTE]**  outerDept为true时，可以配置该字段。 |
| groupContainSubDept | Boolean | 否 | false | 部门群是否包含子部门：   - **true**：包含 - **false**：不包含 |
| groupContainOuterDept | Boolean | 否 | false | 部门群是否包含外包部门：   - **true**：包含 - **false**：不包含 |
| groupContainHiddenDept | Boolean | 否 | false | 部门群是否包含隐藏部门：   - **true**：包含 - **false**：不包含 |
| ext | String | 否 | {} | 部门自定义字段，格式为文本类型的Json格式。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| id | Number | 420727358 | id |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/department/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
  "sourceIdentifier":"1",
  "userPermits":"1|1",
  "userPerimits":"1",
  "orgDeptOwner":"0115074162",
  "outerDept":"true",
  "deptManagerUseridList":"0115074162|01150741646",
  "parentid":"1",
  "groupContainSubDept":"false",
  "outerPermitUsers":"1",
  "outerDeptOnlySelf":"false",
  "outerPermitDepts":"1",
  "deptPerimits":"1",
  "groupContainHiddenDept":"false",
  "createDeptGroup":"true",
  "groupContainOuterDept":"false",
  "name":"接口测试",
  "id":420727358,
  "lang":"zh_CN",
  "autoAddUser":"true",
  "deptHiding":"true",
  "deptPermits":"1|2",
  "order":"1"
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/department/update");
OapiDepartmentUpdateRequest req = new OapiDepartmentUpdateRequest();
req.setId(420727358L);
req.setOrgDeptOwner("0115074162");
req.setOuterPermitUsers("1");
req.setOuterPermitDepts("1");
req.setOuterDept(true);
req.setUserPerimits("1");
req.setDeptPerimits("1");
req.setDeptHiding(true);
req.setDeptManagerUseridList("0115074162|01150741646");
req.setAutoAddUser(true);
req.setCreateDeptGroup(true);
req.setOrder("1");
req.setParentid("1");
req.setLang("zh_CN");
req.setName("接口测试");
req.setSourceIdentifier("1");
req.setUserPermits("1|1");
req.setDeptPermits("1|2");
req.setOuterDeptOnlySelf(false);
req.setGroupContainSubDept(false);
req.setGroupContainOuterDept(false);
req.setGroupContainHiddenDept(false);
OapiDepartmentUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
  "errcode":0,
  "errmsg":"ok",
  "id":420727358
}
```
