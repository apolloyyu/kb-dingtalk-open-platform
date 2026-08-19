---
title: "新增和更新联系人字段格式说明V2"
source_url: "https://open.dingtalk.com/document/development/add-and-update-contact-field-format-description-v2"
namespace: "development"
slug: "add-and-update-contact-field-format-description-v2"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 控件格式 > 新增和更新联系人字段格式说明V2"
doc_id: "EqHaoCxK5u"
updated_at: "2026-07-20 16:34:24"
---

> Source: https://open.dingtalk.com/document/development/add-and-update-contact-field-format-description-v2
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 控件格式 > 新增和更新联系人字段格式说明V2
> Updated: 2026-07-20 16:34:24

# 新增和更新联系人字段格式说明V2

本文档介绍客户管理支持操作的联系人字段信息，在使用新增或更新联系人相关接口时需了解联系人字段信息。

## 适用接口

本文档所示的字段格式说明适用于这几个接口：

- [批量新增联系人数据](1361-add-contact-data-in-batches.md)
- [批量修改联系人数据](1363-modify-contact-data-in-batches.md)

## 联系人字段说明

联系人存在两种字段：

- **预设字段**：预设字段用户不可删除，字段key是固定的（比如联系人名称的字段key为contact\_name），本文档主要描述预设字段的传参格式。
- **自定义控件字段**：自定义控件字段是用户可自定义的，用户可以随时进入客户管理后台新增或删除自定义控件字段，自定义控件字段的key可以通过调用[批量修改联系人数据](1363-modify-contact-data-in-batches.md)接口，获取字段列表fields下的字段名称name，自定义控件字段的传参格式详见[自定义控件字段格式说明V2](1388-custom-control-field-format-description-v2.md)。

## 联系人-客户

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 联系人预设字段 | contact\_related\_customer | value为关联客户名称的json数组格式，extendValue指向关联的客户Id（可以复制并替换掉INST\_ID即可）。 | ``` {  "key": "contact_related_customer",  "value": "[\"XX公司\"]",  "extendValue": "{\"list\":[{\"instanceId\":\"INST_ID\"}]}" } ``` |

## 联系人-姓名

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 联系人预设字段 | contact\_name | value值格式为字符串。 | ``` {     "key":"contact_name",     "value":"小钉" } ``` |

## 联系人-手机号

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 联系人预设字段 | contact\_phone | value值格式为字符串：   - 国际手机号需加国际区号，否则导致无法解析。 - 国内手机号是否添加+86都符合value格式。 | ``` {     "key":"contact_phone",     "value":"185xxxxxxxx" } ``` |

## 联系人-职位

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 联系人预设字段 | contact\_position | value值需满足以下条件：   - 将该字段选项值组成的数组转义为字符串。如果只有一个，value也需要是数组形式。 | ``` {     "key":"contact_position",     "value":"[\"销售\",\"财务\"]" } ``` |
