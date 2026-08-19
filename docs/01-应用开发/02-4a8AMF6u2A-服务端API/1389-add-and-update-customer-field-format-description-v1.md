---
title: "新增和更新客户字段格式说明V1"
source_url: "https://open.dingtalk.com/document/development/add-and-update-customer-field-format-description-v1"
namespace: "development"
slug: "add-and-update-customer-field-format-description-v1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 控件格式 > 新增和更新客户字段格式说明V1"
doc_id: "zplATRNZ15"
updated_at: "2026-07-20 16:34:21"
---

> Source: https://open.dingtalk.com/document/development/add-and-update-customer-field-format-description-v1
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 控件格式 > 新增和更新客户字段格式说明V1
> Updated: 2026-07-20 16:34:21

# 新增和更新客户字段格式说明V1

本文档介绍客户管理支持操作的客户字段信息，在使用新增或更新客户相关接口时需了解客户字段信息。

## 适用接口

本文介绍的字段格式说明适用于以下接口：

- [创建个人或企业客户数据](1348-add-crm-personal-customers.md)
- [更新个人或企业客户数据](1349-update-crm-personal-customers.md)

## 客户字段说明

个人客户、企业客户存在两种字段：

- **预设字段**：预设字段用户不可删除，字段key是固定的（比如客户名称的字段key为customer\_name），本文档主要描述预设字段的传参格式。
- **自定义控件字段**：自定义控件字段是用户可自定义的，用户可以进入客户管理后台新增或删除自定义控件字段。自定义控件字段的key可以通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name，自定义控件字段的格式参见[自定义控件字段格式说明V1](1387-custom-control-field-format-description-v1.md)。

以下字段可以任意组合使用，例如需要同时设置客户名称和客户跟进状态：

```
{  
  "data":{
    "customer_name":"小钉",
    "customer_follow_up_status":"成交"
  }
}
```

## 客户名称

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户、企业客户预设字段 | customer\_name | value值格式为字符串。 | ``` {     "data":{     "customer_name":"小钉"   } } ``` |

## 客户跟进状态

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户、企业客户预设字段 | customer\_follow\_up\_status | value值格式为字符串，填客户跟进状态字段元数据中的任一选项值即可。 | ``` {     "data":{     "customer_follow_up_status":"成交"   } } ``` |

## 地址

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户、企业客户预设字段 | address | value需同时符合以下条件：   - 必须和地址控件的格式一致且正确。 - 使用英文格式逗号进行分隔。 | ``` {     "data":{     "address":"浙江省,杭州市,西湖区,三墩镇,XX路XX号XX大厦XX室"   } } ``` |

## 个人客户-电话

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户预设字段 | customer\_phone | value值格式为字符串：   - 国际手机号需加国际区号，否则导致无法解析。 - 国内手机号是否添加+86都符合value格式。 - 固定电话是否添加区号都符合value格式。 | ``` {     "data":{     "customer_phone":"185xxxxxxxx"   } } ``` |

## 客户-标签

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值需满足：将该字段选项值组成的数组转义为字符串。如果只有一个，value也需要是数组形式。 | ``` {     "data":{     "MultiTagField-xxxxxx":"[\"高意向\",\"低意向\"]"   } } ``` |
