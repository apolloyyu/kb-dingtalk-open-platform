---
title: "创建企业客户数据"
source_url: "https://open.dingtalk.com/document/development/dingtalk-paas-master-data-create-crm-customer-data"
namespace: "development"
slug: "dingtalk-paas-master-data-create-crm-customer-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 创建企业客户数据"
doc_id: "3OdWaAuNfH"
updated_at: "2025-09-08 19:07:49"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-create-crm-customer-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 创建企业客户数据
> Updated: 2025-09-08 19:07:49

# 创建企业客户数据

调用本接口创建企业客户数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月17日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[创建个人或企业客户数据](https://open.dingtalk.com/document/orgapp/add-crm-personal-customers) 或者 [批量新增个人或企业客户数据](https://open.dingtalk.com/document/orgapp/add-multiple-relationship-data-in-batches)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 接口说明

在高级版客户管理中，客户被分为公海和私池。公海是没有负责人的客户，而有负责人的客户会显示在各自负责人的列表页。

对于私池会有对应的掉保规则，符合掉保规则的客户会从私池进入公海。因此在客户管理高级版里创建客户和查询客户与普通版用户管理有些许区别。

- 在批量获取客户时，默认获取私池客户。基础版和高级版有以下区别：

  - 基础版客户管理不受影响，可以正常查询。
  - 高级版用户管理如果想要获取公海客户，则需要在参数的**query\_dsl**中添加一个一级参数：`"bizScene": "open_customer"`。

![创建CRM客户 ](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2766310461/p373592.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/customer/create`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 - 第三方企业应用可通[获取第三方应用授权企业的access\_token](https://open.dingtalk.com/document/isvapp/obtains-the-enterprise-authorized-credential) |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| instance | ObjectDataInstanceVo | 是 |  | 企业客户数据。 |
| action | String | 否 | publicDraw | 取值：   - 公海领取客户：**publicDraw** - 公海分配客户：**publicAssign** - 其余场景：不用传值 |
| skip\_duplicate\_check | Boolean | 否 | false | 是否跳过查重。  **默认值**：false。 |
| creator\_userid | String | 是 | user01 | 记录创建人的用户ID。 |
| data | String | 是 | {"customer\_name":"杨xx"} | 客户数据内容，JSON格式字符串。传参格式详见[自定义控件字段格式说明V1](https://open.dingtalk.com/document/orgapp/custom-control-field-format-description-v1)。 |
| extend\_data | String | 否 | {"field\_1":"CRM"} | 主数据扩展值，JSON格式字符串。 |
| permission | DataPermissionVo | 否 |  | 权限。 |
| participant\_userids | String[] | 否 | ["user01","user02"] | 协同人的用户userid列表。 |
| owner\_userids | String[] | 否 | ["user01","user02"] | 负责人的用户userid列表。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataCreateDto |  | 返回结果。 |
| instance\_id | String | INST\_XX | 企业客户数据ID。 |
| success | Boolean | true | 执行结果。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/customer/create?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "instance": {
        "creator_userid": "user01",
        "extend_data": {
            "field_1":"CRM"
        },
        "data": {
            "customer_name":"杨xx"
        },
        "permission": {
            "owner_userids": [
                "user01",
                "user02"
            ],
            "participant_userids": [
                "user01",
                "user02"
            ]
        }
    }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/customer/create");
OapiCrmObjectdataCustomerCreateRequest req = new OapiCrmObjectdataCustomerCreateRequest();
ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
objectDataInstanceVo.setCreatorUserid("user01");
objectDataInstanceVo.setData("{\"customer_name\":\"杨xx\"}");
DataPermissionVo dataPermissionVo = new DataPermissionVo();
dataPermissionVo.setParticipantUserids(Arrays.asList("user01","user02"));
dataPermissionVo.setOwnerUserids(Arrays.asList("user01","user02"));
objectDataInstanceVo.setPermission(dataPermissionVo);
req.setInstance(objectDataInstanceVo);
OapiCrmObjectdataCustomerCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "errmsg": "ok",
    "success": true,
    "result": {
        "instance_id": "INST_XX"
    }
}
```
