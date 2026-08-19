---
title: "查询DSL说明"
source_url: "https://open.dingtalk.com/document/development/inner-query-dsl-description"
namespace: "development"
slug: "inner-query-dsl-description"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 控件格式 > 查询DSL说明"
doc_id: "Kx3Q3ffNuq"
updated_at: "2026-07-20 16:34:25"
---

> Source: https://open.dingtalk.com/document/development/inner-query-dsl-description
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 控件格式 > 查询DSL说明
> Updated: 2026-07-20 16:34:25

# 查询DSL说明

本文介绍客户、联系人、跟进记录、自定义对象的查询DSL语法。

## DSL语法的介绍

客户管理部分接口，需要传入查询queryDsl来查询结果。例如以下接口：

| 类别 | 接口列表 |
| --- | --- |
| 客户 | - [根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md) |
| 联系人 | - [根据指定条件查询联系人数据](1365-api-getcontacts.md) |
| 跟进记录 | - [根据指定条件查询跟进记录数据](1371-query-and-dingtalk-data-of-track-records-in-apsara-stack.md) |
| 自定义对象 | - [根据指定条件查询自定义对象数据](1377-api-getobjectdata.md) |

## DSL语法的格式

queryDsl由以下两部分组成：

- 查询条件列表
- 排序字段

DSL语法包括查询条件列表、排序字段。

```
{
 "queryGroupList": [{
  "logicType": "AND", //查询条件之间的拼接方式，取值：AND/OR
  "queryObjectList": [{
   "filterType": "IN", //字段查询类型
   "fieldId": "principal", //查询字段名
   "value": ["2050193136694677"] //查询字段值
  }]
 }],
 "order": "DESC", //排序方式，取值：DESC/ASC
 "orderFieldId": "gmt_create" //排序字段名，如果没有指定则默认使用gmt_create
}
```

### 查询条件列表

字段是queryGroupList。

| 字段 | 说明 |
| --- | --- |
| logicType | 多个查询条件之间的拼接方式，取值：AND/OR。 |
| queryObjectList | 多个查询条件。 |
| filterType | 查询类型，支持以下取值：   - **SEARCH**：模糊搜索 - **EQ**：值相等 - **IN：**等同于SQL中的IN - **BETWEEN**：介于，使用该过滤类型时，value值格式为数组。 |
| value | 查询字段的值，根据filterType取值需要传入不同格式的value：   - **SEARCH**：文本，比如："公司" - **EQ**：文本，比如："公司" - **IN：**JSON数组格式，比如：["2050193136694677"] - **BETWEEN**：介于，使用该过滤类型时，value值格式为JSON数组，比如：["1636473600000", "1636646399999"]。 |
| fieldId | **客户：**  过滤字段名，支持传入两种字段类型：   - **表单字段**：通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name - **系统字段**：    - gmt\_create：创建时间   - gmt\_modified：更新时间   - principal：负责人   - participant：协同人 |
| **联系人：**  过滤字段名，支持传入两种字段类型：   - **表单字段**：通过调用[获取联系人的元数据](1364-gets-the-metadata-description-of-a-crm-contact-object.md)接口，获取字段列表fields下的字段名称name。 - **系统字段**：    - gmt\_create：创建时间   - gmt\_modified：更新时间   - principal：负责人   - participant：协同人 |

### 排序条件

| 字段 | 说明 |
| --- | --- |
| orderFieldId | 排序字段名。  **[!IMPORTANT]**  只支持gmt\_create（创建时间）、gmt\_modified（更新时间）。 |
| order | 排序方式，支持以下取值：   - **ASC**：升序 - **DESC**：降序 |

## 使用示例

### 根据负责人查询数据并根据创建时间降序排序

```
{
 "queryGroupList": [{
  "logicType": "AND",
  "queryObjectList": [{
   "filterType": "IN",
   "value": ["2050193136694677"],
   "fieldId": "principal"
  }]
 }],
 "order": "DESC",
 "orderFieldId": "gmt_create"
}
```

### 查询客户跟进状态为待跟进的数据（单选、多选控件）

```
{
 "queryGroupList": [{
  "logicType": "AND",
  {
   "filterType": "IN",
   "value": ["待跟进"],
   "fieldId": "DDSelectField-KI5S975E"
  }]
 }]
}
```

### 根据客户标签筛选数据

```
{
 "queryGroupList": [{
  "logicType": "AND",
  "queryObjectList": [{
   "filterType": "IN",
   "value": ["待邀约"],
   "fieldId": "MultiTagField-58e38fd7"
  }]
 }]
}
```

### 搜索客户名称为XX的数据（文本控件、地址控件）

```
{
 "queryGroupList": [{
  "logicType": "AND",
  "queryObjectList": [{
   "filterType": "SEARCH",
   "value": "XX",
   "fieldId": "TextField-K2U5DHAA"
  }]
 }]
}
```

### 根据创建时间筛选数据(日期控件、数字控件范围查询)

```
{
 "queryGroupList": [{
  "logicType": "AND",
  "queryObjectList": [{
   "filterType": "BETWEEN",
   "value": ["1636473600000", "1636646399999"],
   "fieldId": "gmt_create"
  }]
 }]
}
```

### 多条件组合查询

```
{
 "queryGroupList": [{
  "logicType": "AND",
  "queryObjectList": [{
   "filterType": "BETWEEN",
   "value": ["1636473600000", "1636646399999"],
   "fieldId": "gmt_create"
  },{
   "filterType": "SEARCH",
   "value": "a",
   "fieldId": "DDTextField-xxx"
  }]
 }]
}
```
