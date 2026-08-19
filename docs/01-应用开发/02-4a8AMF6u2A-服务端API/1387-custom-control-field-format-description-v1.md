---
title: "自定义控件字段格式说明V1"
source_url: "https://open.dingtalk.com/document/development/custom-control-field-format-description-v1"
namespace: "development"
slug: "custom-control-field-format-description-v1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 控件格式 > 自定义控件字段格式说明V1"
doc_id: "UD4phkrMRx"
updated_at: "2026-07-20 16:32:34"
---

> Source: https://open.dingtalk.com/document/development/custom-control-field-format-description-v1
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 控件格式 > 自定义控件字段格式说明V1
> Updated: 2026-07-20 16:32:34

# 自定义控件字段格式说明V1

本文档介绍客户管理支持操作的自定义控件字段信息，在使用新增或更新客户、联系人、跟进记录、自定义对象相关接口时需了解自定义控件字段信息。

## 电话

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值格式为字符串：   - 国际手机号需加国际区号，否则导致无法解析。 - 国内手机号是否添加+86都符合value格式。 - 固定电话是否添加区号都符合value格式。 | ``` {     "data":{     "PhoneField-xxxxxx":"185xxxxxxxx"   } } ``` |

## 数字输入框

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值格式为字符串。 | ``` {     "data":{     "NumberField-xxxxxx":"100"   } } ``` |

## 单选框

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值需符合以下条件：   - 格式为字符串 - 填写预设的选项值之一。 | ``` {     "data":{     "DDSelectField-xxxxxx":"选项1"   } } ``` |

## 多选框

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值填写预设的选项值组成的数组转义为字符串，即使只有一个，value也需要是数组格式。 | ``` {     "data":{     "DDMultiSelectField-xxxxxx":"[\"选项1\",\"选项2\"]"   } } ``` |

## 日期

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值的格式：   - 如果控件的日期类型选择【年-月-日】，value格式为yyyy-MM-dd。 - 如果控件的日期类型选择【年-月-日 时:分】，value格式为yyyy-MM-dd HH:mm。 | ``` {     "data":{     "DDDateField-xxxxxx":"2021-08-17"   } } ``` |

## 日期区间

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值的格式：   - 如果控件的日期类型选择【年-月-日】，value格式为yyyy-MM-dd。 - 如果控件的日期类型选择【年-月-日 时:分】，value格式为yyyy-MM-dd HH:mm。 | ``` {     "data":{     "DDDateRangeField-xxxxxx":"[\"2019-02-19\",\"2019-02-25\"]"   } } ``` |

## 身份证

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值格式为字符串。 | ``` {     "data":{     "IdCardField-xxxxxx":"xxxx"   } } ``` |

## 金额

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值格式为字符串。 | ``` {     "data":{     "MoneyField-xxxxxx":"100"   } } ``` |

## 附件

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value是一个json数组转义为字符串形式。  **[!NOTE]**  数组中的每个 json 对象都是一个附件文件，每个文件都必须包含 spaceId、fileName、fileSize、fileType 和 fileId 字段。 | ``` {     "data":{     "DDAttachment-xxxxxx":"[{\"spaceId\": \"163xxxx658\", \"fileName\": \"2644.JPG\", \"fileSize\": \"333\", \"fileType\": \"jpg\", \"fileId\": "\"643xxxx140\"}]"   } } ``` |

## 联系人

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值是userId为元素的json数组格式。 | ``` {     "data":{     "InnerContactField-xxxxxx":"[\"4525xxxxxxxx77041\"]"   } } ``` |

## 省市区

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value需同时符合以下条件：   - 必须和地址控件的格式一致且正确。 - 使用英文格式逗号进行分隔。 | ``` {     "data":{     "AddressField-xxxxxx":"浙江省,杭州市,西湖区,三墩镇,XX路XX号XX大厦XX室"   } } ``` |

## 评分

| 字段类型 | Key | Value | 示例 |
| --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值格式为number。 | ``` {     "data":{     "StarRatingField-xxxxxx":"5"   } } ``` |

## 部门

| 字段类型 | Key | Value | extValue | 示例 |
| --- | --- | --- | --- | --- |
| 自定义控件 | 通过调用[获取个人或企业客户的元数据](1347-obtain-the-metadata-of-individual-enterprise-customers.md)接口，获取字段列表fields下的字段名称name。 | value值格式为字符串。 | value需同时符合以下条件：   - extValue格式必须是数组结构。 - extValue必须是相同的部门名称。 | ``` {     "data":{     "DepartmentField-xxxxxx":"{\"value\":\"部门名称\",\"extValue\":\"[{\\\"name\\\":\\\"部门名称\\\"}]\"}"   } } ``` |
