---
title: "获取企业客户的元数据"
source_url: "https://open.dingtalk.com/document/development/get-metadata-description-of-crm-customer-object"
namespace: "development"
slug: "get-metadata-description-of-crm-customer-object"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 获取企业客户的元数据"
doc_id: "sW8FnNmgp7"
updated_at: "2025-09-08 19:07:53"
---

> Source: https://open.dingtalk.com/document/development/get-metadata-description-of-crm-customer-object
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 获取企业客户的元数据
> Updated: 2025-09-08 19:07:53

# 获取企业客户的元数据

调用本接口获取钉钉CRM企业客户的元数据。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对**客户管理**相关接口规范进行升级，从[旧版升级到新版](https://open.dingtalk.com/document/orgapp/differences-between-server-apis-and-new-server-apis)。本文旧版规范接口文档已于**2022年6月17日**迁移至**历史文档（不推荐）**目录，且**本接口仅保持现有功能，不再新增支持其他能力。**
>
> - 如果未使用本接口，推荐使用新版规范[获取个人或企业客户的元数据](https://open.dingtalk.com/document/orgapp/get-metadata-description-of-crm-customer-object-1)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 接口说明

例如，调用本接口，在企业的客户管理应用中获取客户的元数据，实现效果与下图类似。![客户数据元数据](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/4262155461/p407541.png)

## 权限

服务端API是以应用维度授权的，在调用接口前，确保已经为应用添加了接口权限。

| 应用类型 | 是否支持调用 | 权限申请方式 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 是 | **[!IMPORTANT]**  暂不支持新增申请。 | — |
| 第三方企业应用 | 否 | — | — |
| 第三方个人应用 | 否 | — | — |

## 基本信息

**请求方式**：POST

**请求地址**：`https://oapi.dingtalk.com/topapi/crm/objectmeta/customer/describe`

## Query参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | dc73axxxx | 调用服务端API的应用凭证。   - 企业内部应用可通过[获取企业内部应用的access\_token](https://open.dingtalk.com/document/orgapp/obtain-orgapp-token)接口获取 |

## 返回参数

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | DObject |  | 返回结果。 |
| name | String | crm\_customer | 对象名称。 |
| customized | Boolean | false | 是否自定义对象。 |
| fields | Fields[] |  | 字段列表。 |
| name | String | customer\_name | 字段名称。 |
| customized | Boolean | false | 是否自定义字段，为false则字段不能删除。 |
| label | String | 客户名称 | 字段展示名。 |
| type | String | Text | 字段类型。 |
| nillable | Boolean | false | 是否可以为空。 |
| format | String | yyyy-MM-dd | 日期格式。  对**Date**和**DateRange**类型有效。 |
| unit | String | 天 | 日期单位或金额单位。 |
| select\_options | SelectOptions[] |  | 选项列表。 |
| key | String | option\_1 | 选项key。 |
| value | String | 选项1 | 选项名。 |
| quote | Boolean | true | 是否引用关联。 |
| reference\_to | String | crm\_contact | 关联对象名称。 |
| reference\_fields | ReferenceFields[] |  | 引用的关联对象的字段列表。 |
| label | String | 联系人名称 | 引用的关联对象字段显示名。 |
| type | String | Text | 引用的关联对象字段类型。 |
| nillable | Boolean | false | 引用的关联对象字段是否可空。 |
| format | String | yyyy-MM-dd | 引用的关联对象字段格式。 |
| unit | String | 天 | 引用的关联对象字段单位。 |
| select\_options | SelectOptions[] |  | 引用的关联对象的字段选项列表。 |
| key | String | option\_2 | 引用的关联对象的字段选项key。 |
| value | String | 选项2 | 引用的关联对象的字段选项值。 |
| name | String | crm\_customer | 引用的关联对象的字段名称。 |
| roll\_up\_summary\_fields | RollUpSummaryFields[] |  | 对MasterDetail类型有效：roll-up summary字段列表。 |
| name | String | Money-XDADDF | 需要汇总的明细内字段名。 |
| aggregator | String | SUM | 汇总方法。 |
| errcode | Number | 10001 | 返回码。 |
| errmsg | String | 系统出错 | 调用失败时返回的错误信息。 |

## 示例

**请求示例（HTTP）**

```
POST https://oapi.dingtalk.com/topapi/crm/objectmeta/customer/describe?access_token=ACCESS_TOKEN
```

**请求示例（JAVA SDK）**

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/crm/objectmeta/customer/describe");
OapiCrmObjectmetaCustomerDescribeRequest req = new OapiCrmObjectmetaCustomerDescribeRequest();
OapiCrmObjectmetaCustomerDescribeResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

**返回示例**

```
{
    "errcode": 0,
    "result": {
        "code": "PROC-D1CD928E-CCB1-4F68-AA1F-7E03A94047E5",
        "customized": false,
        "fields": [
            {
                "customized": false,
                "label": "客户名称",
                "name": "customer_name",
                "nillable": false,
                "type": "Text"
            },
            {
                "customized": true,
                "label": "是否重要",
                "name": "MultiTagField-62e5f9c0",
                "nillable": true,
                "select_options": [
                    {
                        "key": "e88a359d6c",
                        "value": "重要"
                    },
                    {
                        "key": "f81a83233e",
                        "value": "不重要"
                    }
                ],
                "type": "MultiTag"
            },
            {
                "customized": true,
                "label": "客户意向",
                "name": "MultiTagField-27c1d1f2",
                "nillable": true,
                "select_options": [
                    {
                        "key": "0b97069a91",
                        "value": "高意向"
                    },
                    {
                        "key": "6df0b3ea92",
                        "value": "中意向"
                    },
                    {
                        "key": "2b9c84bdd3",
                        "value": "低意向"
                    }
                ],
                "type": "MultiTag"
            },
            {
                "customized": false,
                "label": "客户跟进状态",
                "name": "customer_follow_up_status",
                "nillable": false,
                "select_options": [
                    {
                        "key": "option_new_acquisition",
                        "value": "新获取"
                    },
                    {
                        "key": "option_1",
                        "value": "待跟进"
                    },
                    {
                        "key": "option_KIBAJKEH",
                        "value": "初步意向"
                    },
                    {
                        "key": "option_KI5SP2LY",
                        "value": "商机客户"
                    },
                    {
                        "key": "option_done",
                        "value": "成交"
                    },
                    {
                        "key": "option_invalid",
                        "value": "失效"
                    }
                ],
                "type": "Select"
            },
            {
                "customized": true,
                "label": "客户状态",
                "name": "DDSelectField-K371T4RY",
                "nillable": true,
                "select_options": [
                    {
                        "key": "option_0",
                        "value": "潜在客户"
                    },
                    {
                        "key": "option_1",
                        "value": "初步接触"
                    },
                    {
                        "key": "option_2",
                        "value": "持续跟进"
                    },
                    {
                        "key": "option_K371U1YG",
                        "value": "成交客户"
                    },
                    {
                        "key": "option_K371U1YF",
                        "value": "忠诚客户"
                    },
                    {
                        "key": "option_K371U9NC",
                        "value": "无效客户"
                    },
                    {
                        "key": "option_K39R1E59",
                        "value": "其他"
                    }
                ],
                "type": "Select"
            },
            {
                "customized": true,
                "label": "重要程度",
                "name": "DDSelectField-K55CWZ2C",
                "nillable": true,
                "select_options": [
                    {
                        "key": "option_0",
                        "value": "一般"
                    },
                    {
                        "key": "option_1",
                        "value": "重要"
                    },
                    {
                        "key": "option_2",
                        "value": "很重要"
                    }
                ],
                "type": "Select"
            },
            {
                "customized": true,
                "label": "客户来源",
                "name": "DDSelectField-K2U5GX3B",
                "nillable": true,
                "select_options": [
                    {
                        "key": "option_K2U5LXIN",
                        "value": "网络销售"
                    },
                    {
                        "key": "option_K2U5LXIO",
                        "value": "电话销售"
                    },
                    {
                        "key": "option_K2U5LXIP",
                        "value": "渠道代理"
                    },
                    {
                        "key": "option_K2U5LXIQ",
                        "value": "其他"
                    }
                ],
                "type": "Select"
            },
            {
                "customized": true,
                "label": "客户行业",
                "name": "DDSelectField-K2U5GX39",
                "nillable": true,
                "select_options": [
                    {
                        "key": "option_K2U5KPJT",
                        "value": "金融"
                    },
                    {
                        "key": "option_K2U5KPJU",
                        "value": "电信"
                    },
                    {
                        "key": "option_K2U5KPJV",
                        "value": "政府"
                    },
                    {
                        "key": "option_K2U5KPJW",
                        "value": "教育"
                    },
                    {
                        "key": "option_K2U5KPJX",
                        "value": "制造"
                    },
                    {
                        "key": "option_K2U5KPJY",
                        "value": "服务"
                    },
                    {
                        "key": "option_K2U5KPJZ",
                        "value": "其他"
                    }
                ],
                "type": "Select"
            },
            {
                "customized": true,
                "label": "区域城市",
                "name": "TextField-K55CWZ2D",
                "nillable": true,
                "type": "Text"
            },
            {
                "customized": true,
                "label": "单行输入框(2)",
                "name": "TextField-K85VR0IG",
                "nillable": true,
                "type": "Text"
            },
            {
                "customized": true,
                "label": "备注",
                "name": "TextareaField-K55CWZ2E",
                "nillable": true,
                "type": "Textarea"
            },
            {
                "customized": true,
                "label": "单行输入框",
                "name": "TextField-K85VOGS8",
                "nillable": true,
                "type": "Text"
            }
        ],
        "name": "crm_customer",
        "status": "PUBLISHED"
    },
    "request_id": "15r52c40a5k5z"
}
```
