---
title: "新增和更新客户字段格式说明V2"
source_url: "https://open.dingtalk.com/document/development/the-model-fields-supported-by-the-interface-and-their-value"
namespace: "development"
slug: "the-model-fields-supported-by-the-interface-and-their-value"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 控件格式 > 新增和更新客户字段格式说明V2"
doc_id: "B3knZd5xC9"
updated_at: "2026-07-20 16:34:22"
---

> Source: https://open.dingtalk.com/document/development/the-model-fields-supported-by-the-interface-and-their-value
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 控件格式 > 新增和更新客户字段格式说明V2
> Updated: 2026-07-20 16:34:22

# 新增和更新客户字段格式说明V2

本文档介绍客户管理支持操作的客户字段信息，在使用新增或更新客户相关接口时需了解客户字段信息。

## 适用接口

本文介绍的字段格式说明适用于以下接口：

- [批量新增个人或企业客户数据](1351-add-multiple-relationship-data-in-batches.md)
- [批量更新个人或企业客户数据](1352-update-multiple-relational-data-tables-at-a-time.md)

## 客户字段说明

个人客户、企业客户存在两种字段：

- 预设字段：预设字段用户不可删除，字段key是固定的（比如客户名称的字段key为customer\_name），本文主要描述预设字段的传参格式。
- 自定义控件字段：自定义控件字段是用户可自定义的，用户可以随时进入客户管理后台新增或删除自定义控件字段，自定义控件字段的key可以通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name，自定义控件字段的格式请参见[自定义控件字段格式说明V2](1388-custom-control-field-format-description-v2.md)。

## 客户名称

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户、企业客户预设字段 | customer\_name | value值格式为字符串。 | ``` {     "key":"customer_name",     "value":"小钉" } ``` |

## 客户跟进状态

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户、企业客户预设字段 | customer\_follow\_up\_status | value值格式为字符串，填客户跟进状态字段元数据中的任一选项值即可。 | ``` {     "key":"customer_follow_up_status",     "value":"成交" } ``` |

## 地址

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户、企业客户预设字段 | address | value需同时符合以下条件：   - 必须和地址控件的格式一致且正确。 - 使用英文格式逗号进行分隔。 | ``` {     "key":"address",     "value":"浙江省,杭州市,西湖区,三墩镇,XX路XX号XX大厦XX室" } ``` |

## 个人客户-电话

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 个人客户预设字段 | customer\_phone | value值格式为字符串：   - 国际手机号需加国际区号，否则导致无法解析。 - 国内手机号是否添加+86都符合value格式。 - 固定电话是否添加区号都符合value格式。 | ``` //个人客户关系 {     "key":"customer_phone",     "value":"185xxxxxxxx" } ``` |

## 客户-标签

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值需满足：将该字段选项值组成的数组转义为字符串。如果只有一个，value也需要是数组形式。 | ``` {     "key":"MultiTagField-xxxxxx",     "value":"[\"高意向\",\"低意向\"]" } ``` |
