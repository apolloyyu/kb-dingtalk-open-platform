---
title: "更新联系人数据"
source_url: "https://open.dingtalk.com/document/development/dingtalk-paas-master-data-update-crm-contact-data"
namespace: "development"
slug: "dingtalk-paas-master-data-update-crm-contact-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 更新联系人数据"
doc_id: "eF5DC1oGaf"
updated_at: "2025-09-08 19:07:48"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-paas-master-data-update-crm-contact-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 更新联系人数据
> Updated: 2025-09-08 19:07:48

# 更新联系人数据

调用本接口更新联系人数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对客户管理相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于2022年11月30日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用新版规范[批量修改联系人数据](https://open.dingtalk.com/document/orgapp/modify-contact-data-in-batches)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

> **[!NOTE]**
>
> 联系人有如下限制：
>
> 1. 一个客户下最多存在30个联系人。
> 2. 一个客户下不能存在两个或以上手机号相同的联系人。
> 3. 同一个手机号最多存在5个联系人。
> 4. 一个组织创建的联系人数量不能超过50万。
> 5. 更新联系人时不允许修改关联客户。

![更新CRM联系人](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8737310461/p373778.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | — | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectdata/contact/update`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## Body参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| instance | ObjectDataInstanceVo | 是 |  | 联系人数据。 |
| data | String | 是 | {"contact\_name":"李xx"} | 联系人数据内容，JSON格式字符串。传参格式详见[新增和更新联系人字段格式说明V1](https://open.dingtalk.com/document/orgapp/add-and-update-contact-field-format-description-v1)。 |
| extend\_data | String | 否 | {"field\_1":"CRM"} | 扩展数据内容。 |
| instance\_id | String | 是 | instance\_id | 联系人数据ID，可通过[根据指定条件查询联系人数据](https://open.dingtalk.com/document/orgapp/dingtalk-the-contact-data-query-api)接口获取。 |
| modifier\_userid | String | 是 | user01 | 钉钉用户userId。 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | ObjectDataCreateDto |  | 返回结果。 |
| instance\_id | String | INST\_XX | 联系人数据ID。 |
| success | Boolean | true | 执行结果。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectdata/contact/update?access_token=ACCESS_TOKEN
```

请求正文

```
{
    "instance": {
        "extend_data": {
            "field_1":"CRM"
        },
        "instance_id": "INST_XX",
        "data": {
            "contact_name":"李xx"
        },
        "modifier_userid": "user01"
    }
}
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectdata/contact/update");
OapiCrmObjectdataContactUpdateRequest req = new OapiCrmObjectdataContactUpdateRequest();
ObjectDataInstanceVo objectDataInstanceVo = new ObjectDataInstanceVo();
objectDataInstanceVo.setInstanceId("INST_XX");
objectDataInstanceVo.setModifierUserid("user01");
objectDataInstanceVo.setModifierNick("张xx");
objectDataInstanceVo.setExtendData("{\"field_1\":\"CRM\"}");
objectDataInstanceVo.setData("{\"contact_name\":\"李xx\"}");
req.setInstance(objectDataInstanceVo);
OapiCrmObjectdataContactUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "success": true,
    "errmsg": "ok",
    "result": {
        "instance_id": "INST_XX"
    }
}
```
