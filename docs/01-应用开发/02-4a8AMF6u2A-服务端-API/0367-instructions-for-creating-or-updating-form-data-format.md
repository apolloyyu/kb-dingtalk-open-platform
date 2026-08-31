---
title: "宜搭数据格式和搜索结果排序说明"
source_url: "https://open.dingtalk.com/document/development/instructions-for-creating-or-updating-form-data-format"
namespace: "development"
slug: "instructions-for-creating-or-updating-form-data-format"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 宜搭数据格式和搜索结果排序说明"
doc_id: "Gs728A8lnD"
updated_at: "2026-05-15 09:04:57"
---

> Source: https://open.dingtalk.com/document/development/instructions-for-creating-or-updating-form-data-format
> Path: 应用开发 / 服务端 API / 宜搭 > 宜搭数据格式和搜索结果排序说明
> Updated: 2026-05-15 09:04:57

# 宜搭数据格式和搜索结果排序说明

本文介绍了创建或更新的表单数据格式、筛选组件格式、表单实例FormData格式和内置字段对搜索结果进行排序的相关说明。

## **创建或更新表单数据格式**

表单中每个组件都有唯一 ID，每个组件中填写的数据都有固定格式。保存/更新表单数据时，用 Map<String, Object> 的 jsonString 格式来作为参数传递表单中的数据。key 为组件 ID，Object 为组件的值。

### **单行文本**

| 数据格式 | 示例 |
| --- | --- |
| 字符串 | ``` "danhang" ``` |

### **多行文本**

| 数据格式 | 示例 |
| --- | --- |
| 字符串 | ``` "duohang" ``` |

### **数值**

| 数据格式 | 示例 |
| --- | --- |
| 数字 | ``` 1 ``` |

### **单选**

| 数据格式 | 示例 |
| --- | --- |
| 字符串 | ``` "选项一" ``` |

### **复选**

| 数据格式 | 示例 |
| --- | --- |
| 字符串数组 | ``` ["选项一","选项二"] ``` |

### **评分**

| 数据格式 | 示例 |
| --- | --- |
| 整数 | ``` 97 ``` |

### **下拉单选**

| 数据格式 | 示例 |
| --- | --- |
| 字符串 | ``` "选项一" ``` |

### **下拉复选**

| 数据格式 | 示例 |
| --- | --- |
| 字符串数组 | ``` ["选项一","选项二"] ``` |

### **级联选择**

| 数据格式 | 示例 | 备注 |
| --- | --- | --- |
| 字符串数据 | ``` ["part","part_b"] ``` | 必须按照级联顺序，依次放到数组中。 |

### **日期**

| 数据格式 | 示例 |
| --- | --- |
| 时间戳 | ``` 1516204800000 ``` |

### **日期区间**

| 数据格式 | 示例 | 备注 |
| --- | --- | --- |
| 字符串数组 | ``` ["1514736000000","1517328000000"]。 假如只有结束时间，["","1517328000000"] ``` | 第一个为开始时间的时间戳字符串，第二个为结束时间的时间戳字符串。 |

### **图片上传**

| 数据格式 | 示例 |
| --- | --- |
| JSONArray | ``` [     {       "previewUrl": "/ossFileHandle?appType=APP_K6IGJJ6PFAARLPDSWKXQ&fileName=APP_K6IGJJ6PFAARLPDSWKXQ_MTczMjU1NjYyMzg3MzI0NF8wUDk2NlQ2MVIzR1lHV1RaMjMxQ1A5U1Y1NU1NM1lMWVY1QzBMMQ$$.jpg&instId=&type=open&process=image/resize,m_fill,w_200,h_200,limit_0/quality,q_80",       "size": 2610734,       "name": "Bts2Z0e6oxA.jpg",       "downloadUrl": "/ossFileHandle?appType=APP_K6IGJJ6PFAARLPDSWKXQ&fileName=APP_K6IGJJ6PFAARLPDSWKXQ_MTczMjU1NjYyMzg3MzI0NF8wUDk2NlQ2MVIzR1lHV1RaMjMxQ1A5U1Y1NU1NM1lMWVY1QzBMMQ$$.jpg&instId=&type=download",       "url": "/ossFileHandle?appType=APP_K6IGJJ6PFAARLPDSWKXQ&fileName=APP_K6IGJJ6PFAARLPDSWKXQ_MTczMjU1NjYyMzg3MzI0NF8wUDk2NlQ2MVIzR1lHV1RaMjMxQ1A5U1Y1NU1NM1lMWVY1QzBMMQ$$.jpg&instId=&type=download"     }   ] ``` |

### **附件组件**

| 数据格式 | 示例 |
| --- | --- |
| JSONArray | ``` [    {      "downloadUrl": "文件下载地址",      "name": "文件名",      "previewUrl": "文件预览地址",      "url": "文件下载地址",      "ext": "docx"    } ] ``` |

### **成员**

| 数据格式 | 示例 | 备注 |
| --- | --- | --- |
| 字符串数组 | ``` ["user01","user02"] ``` | 传人员的userId信息，精确匹配。值必须完全匹配，userId顺序也需要一致。 |

### **子表单组件(原明细组件)**

| 数据格式 | 示例 | 备注 |
| --- | --- | --- |
| JSONArray | ``` [   {     "textField_jcr0069m": "danhang1"  //(textField_jcr0069m为子表单里的单行文本组件的组件ID)   },   {     "textField_jcr0069m": "danhang2"   } ] ``` | 由于子表单组件下有多条记录，所以用JSONARRAY。由于每条记录都是很多组件的值，因此用JSONObject来存每个组件对应的值。 |

### **部门**

| 数据格式 | 示例 |
| --- | --- |
| 字符串数组 | ``` ["xxxxx"] ``` |

### **国家/地区**

| 数据格式 | 示例 |
| --- | --- |
| JSONArray | ``` [     {       "value": "PG"     }   ] ``` |

### **地址**

| 数据格式 | 示例 |
| --- | --- |
| JSONObject | ``` {     "address": "111",     "regionIds": [       460000,       469027,       469023401     ],     "regionText": [       {         "en_US": "hai+nan+sheng",         "zh_CN": "海南省"       },       {         "en_US": "cheng+mai+xian",         "zh_CN": "澄迈县"       },       {         "en_US": "guo+ying+hong+gang+nong+chang",         "zh_CN": "国营红岗农场"       }     ]   } ``` |

### **富文本**

| 数据格式 | 示例 |
| --- | --- |
| 字符串 | ``` <div><strong>你好，这是测试</strong></div>\n<div><span style=\"font-family: kaiti;background-color: #ff0000;color: #ffff00;\"><em><strong>测试</strong></em></span></div>\n<div>&nbsp;</div> ``` |

### **城市选择**

| 数据格式 | 示例 | 备注 |
| --- | --- | --- |
| 字符串数组 | ``` ["110000","110100","110101"] ``` | 第一个必须为省份ID，第二个为城市ID，第三个为区ID。 |

### **超链接组件**

| 数据格式 | 示例 |
| --- | --- |
| JSONArray | ``` [    {        "link":"http://www.aliwork.com",        "text":"宜搭"    } ] ``` |

### **关联表单**

| 数据格式 | 示例 |
| --- | --- |
| JSONArray | ``` [   {     "appType": "APP_XXXX",     "formUuid": "被关联页面的表单编码",     "formType": "receipt",     "instanceId": "被关联的表单实例ID",     "title": "标题",     "subTitle": ""   } ] ``` |

## **表单筛选组件格式**

在**某宜搭表单** > **页面管理**页面，单击**数据管理**，可以查看宜搭产品支持筛选的组件，如下图所示。

> **[!IMPORTANT]**
>
> 通过接口筛选表单，部分组件不支持。支持的表单组件请查看本文后续章节**支持筛选条件的表单组件**。

![iShot2022-04-22 11](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/8360160561/p432644.png)

### **支持筛选条件的表单组件**

表单中每个组件都有唯一ID，不同类型组件的搜索格式不一样，不同类型组件支持的操作符不一样，例如大于、等于、小于、包含、不等于......等。

目前支持筛选的表单组件有常用控件、高级控件。

#### **常用控件**

单行文本、多行文本、数值、评分、单选、下拉单选、复选、下拉复选、级联选择、日期、日期区间、图片上传、附件、成员、成员（多选模式）、子表单、子表单内部的组件。

#### **高级控件**

部门、部门（多选模式）、国家/地区、地址。

### **支持搜索的预置字段**

除了表单组件支持搜索，部分预置字段也支持搜索。目前支持以下预置字段：

#### **普通表单**

实例标题、提交人、提交人组织、创建时间、修改时间、流水号。

#### **流程表单**

当前节点名称、流程审批结果、流程实例状态、任务ID。

### **过滤条件参数说明**

过滤条件参数是字符串，是JSONArray字符串化的值，具体形式为

```
[{
 "key": 左操作数,
 "value": 右操作数,
 "type": "组件值类型",
 "operator": 操作符,
 "componentName": 组件名称
}]
```

例如，提交人等于小钉且流程审批结果为同意，则入参可以填以下内容。

```
[{
 "key": "originator",
 "value": "1732556623873244",
 "type": "STRING",
 "operator": "eq",
 "componentName": "EmployeeField"
}, {
 "key": "processApprovedResult",
 "value": ["agree"],
 "type": "ARRAY",
 "operator": "in",
 "componentName": "SelectField"
}]
```

### **常用控件**

| 控件类型 | 操作符 | 单独的检索条件示例 |
| --- | --- | --- |
| 单行文本 | - 等于 (eq) - 匹配（like） | ``` [{  "key": "textField_kwod1oy2",  "value": "A",  "type": "TEXT",  "operator": "like",  "componentName": "TextField" }] ``` |
| 多行文本 | - 等于 (eq) - 匹配（like） | ``` [{  "key": "textareaField_kwod1oy4",  "value": "A",  "type": "TEXT",  "operator": "like",  "componentName": "TextareaField" }] ``` |
| 数值 | - 大于(gt) - 大于等于(ge) - 小于(lt) - 小于等于(le) - 介于(between) | - 大于：     ```   [{    "key": "numberField_kwod1oy6",    "value": 2,    "type": "DOUBLE",    "operator": "gt",    "componentName": "NumberField"   }]   ``` - 介于：     ```   [{    "key": "numberField_kwod1oy6",    "value": [1, 2],    "type": "DOUBLE",    "operator": "between",    "componentName": "NumberField"   }]   ``` |
| 评分 | - 大于(gt) - 大于等于(ge) - 小于(lt) - 小于等于(le) - 介于(between) | - 大于：     ```   [{    "key": "rateField_kwod1oy8",    "value": 2,    "type": "DOUBLE",    "operator": "gt",    "componentName": "RateField"   }]   ``` - 介于     ```   [{    "key": "rateField_kwod1oy8",    "value": [2, 4],    "type": "DOUBLE",    "operator": "between",    "componentName": "RateField"   }]   ``` |
| 单选 | - 等于(eq) - 包含(contains)   **[!NOTE]**   - 操作符为“等于”时只能选择单个值 - 操作符为”包含“时可选择多个值 | - 等于：     ```   [{    "key": "radioField_kwod1oya",    "value": "选项一",    "type": "ARRAY",    "operator": "eq",    "componentName": "RadioField"   }]   ``` - 包含：     ```   [{    "key": "radioField_kwod1oya",    "value": ["选项一", "选项二"],    "type": "ARRAY",    "operator": "contains",    "componentName": "RadioField"   }]   ``` |
| 下拉单选 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "selectField_kwod1oya",    "value": "选项一",    "type": "ARRAY",    "operator": "eq",    "componentName": "SelectField"   }]   ``` - 包含：     ```   [{    "key": "selectField_kwod1oya",    "value": ["选项一", "选项二"],    "type": "ARRAY",    "operator": "contains",    "componentName": "SelectField"   }]   ``` |
| 复选 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "checkboxField_kwod1oyc",    "value": ["选项一", "选项二"],    "type": "ARRAY",    "operator": "eq",    "componentName": "CheckboxField"   }]   ``` - 包含：     ```   [{    "key": "checkboxField_kwod1oyc",    "value": ["选项一", "选项三"],    "type": "ARRAY",    "operator": "contains",    "componentName": "CheckboxField"   }]   ``` |
| 下拉复选 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "multiSelectField_kwod1oyg",    "value": ["选项一", "选项二"],    "type": "ARRAY",    "operator": "eq",    "componentName": "MultiSelectField"   }]   ``` - 包含：     ```   [{    "key": "multiSelectField_kwod1oyg",    "value": ["选项一", "选项二"],    "type": "ARRAY",    "operator": "contains",    "componentName": "MultiSelectField"   }]   ``` |
| 级联选择 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "cascadeSelectField_kwod1oyo",    "value": ["product", "product_a"],    "type": "STRING",    "operator": "eq",    "componentName": "CascadeSelectField"   }]   ``` - 包含：     ```   [{    "key": "cascadeSelectField_kwod1oyo",    "value": ["part", "part_b"],    "type": "STRING",    "operator": "contains",    "componentName": "CascadeSelectField"   }]   ``` |
| 日期 | - 大于(gt) - 大于等于(ge) - 小于(lt) - 小于等于(le) - 介于(between) | - 大于：     ```   [{    "key": "dateField_kwod1oyi",    "value": 1649174400000,    "type": "DOUBLE",    "operator": "gt",    "componentName": "DateField"   }]   ``` - 介于：     ```   [{    "key": "dateField_kwod1oyi",    "value": [1649088000000, 1652198399000],    "type": "DOUBLE",    "operator": "between",    "componentName": "DateField"   }]   ``` |
| 日期区间 | 无需传操作符(采用默认操作符)  **[!NOTE]**  日期区间在数据管理里自动生成日期区间（开始）和日期区间（结束）这2个组件，各自的操作符为介于，即日期区间的开始时间介于和日期区间的结束时间介于日期区间 | ``` [{  "key": "cascadeDateField_kwod1oyk",  "value": [   [1649433600000, 1651593599000],   [1649260800000, 1652198399000]  ],  "type": "DOUBLE",  "componentName": "CascadeDateField" }] ``` |
| 图片上传 | 匹配（like） | ``` [{  "key": "imageField_kwod1oyq",  "value": "fileUpload/",  "type": "TEXT",  "operator": "like",  "componentName": "ImageField" }] ``` |
| 附件 | 匹配（like） | ``` [{  "key": "attachmentField_kwod1oys",  "value": "APP_ANNSASAS",  "type": "TEXT",  "operator": "like",  "componentName": "AttachmentField" }] ``` |
| 成员 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "employeeField_kwod1oym",    "value": "钉钉userId",    "type": "STRING",    "operator": "eq",    "componentName": "EmployeeField"   }]   ``` - 包含：     ```   [{    "key": "employeeField_kwod1oym",    "value": "[\"17325566238732445\",\"1163103157219057185\"]",    "type": "STRING",    "operator": "contains",    "componentName": "EmployeeField"   }]   ``` |
| 成员(多选模式) | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "employeeField_kwod1oym",    "value": "0124151667379678541",    "type": "STRING",    "operator": "eq",    "componentName": "EmployeeField"   }]   ``` - 包含：     ```   [{    "key": "employeeField_kwod1oym",    "value": "[\"0124151667379678541\",\"1163103157219057181\",\"0928242534266035951\"]",    "type": "STRING",    "operator": "contains",    "componentName": "EmployeeField"   }]   ``` |
| 子表单 | 包含(contains) | ``` [{  "key": "tableField_kwod1oyu",  "value": "关键词",  "type": "TEXT",  "operator": "contains",  "componentName": "TableField" }] ``` |
| 子表单内部的组件 | 和主表单里的组件支持的操作符一致，区别是条件里带有parentId(值为子表单组件的id) | ``` [{  "key": "textField_kwod1ozm",  "value": "ad",  "type": "TEXT",  "operator": "like",  "componentName": "TextField",  "parentId": "tableField_kwod1oyu" }] ``` |

### **高级控件**

| 控件类型 | 操作符 | 单独的检索条件示例 |
| --- | --- | --- |
| 部门 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "departmentSelectField_kwod1oz8",    "value": "483524872",    "type": "ARRAY",    "operator": "eq",    "componentName": "DepartmentSelectField"   }]   ``` - 包含：     ```   [{    "key": "departmentSelectField_kwod1oz8",    "value": ["483524872"],    "type": "ARRAY",    "operator": "contains",    "componentName": "DepartmentSelectField"   }]   ``` |
| 部门(多选模式) | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "departmentSelectField_kwod1oz8",    "value": "483524872",    "type": "ARRAY",    "operator": "eq",    "componentName": "DepartmentSelectField"   }]   ``` - 包含：     ```   [{    "key": "departmentSelectField_kwod1oz8",    "value": ["483524872"],    "type": "ARRAY",    "operator": "contains",    "componentName": "DepartmentSelectField"   }]   ``` |
| 国家/地区 | - 等于(eq) - 包含(contains) | - 等于：     ```   [{    "key": "countrySelectField_kwod1oz6",    "value": "PG",    "type": "ARRAY",    "operator": "eq",    "componentName": "CountrySelectField"   }]   ``` - 包含：     ```   [{    "key": "countrySelectField_kwod1oz6",    "value": ["MO", "HK", "TW"],    "type": "ARRAY",    "operator": "contains",    "componentName": "CountrySelectField"   }]   ``` |
| 地址 | - 地址：等于(eq) - 详细地址：等于(eq)/匹配（like）   **[!NOTE]**  地址组件在数据管理里自动生成地址和详细地址，其中地址部分仅支持eq，详细地址部分支持eq和like地址 | - 地址：     ```   [{    "key": "addressField_kwod1oza",    "value": {     "regionIds": ["820000", "820200", "820007"],     "address": "仓前街道"    },    "operator": "eq",    "type": "TEXT",    "componentName": "AddressField"   }]   ``` - 详细地址：     ```   [{    "key": "addressField_kwod1oza",    "value": {     "regionIds": ["820000", "820200", "820007"],     "address": "未来park"    },    "operator": "like",    "type": "TEXT",    "componentName": "AddressField"   }]   ``` |
| 富文本 | 不支持 | - |
| 布局容器 | 不支持 | - |
| 分组 | 不支持 | - |
| 关联表单 | 不支持 | - |
| 定位 | 不支持 | - |
| 手写签名 | 不支持 | - |

### **预设字段**

#### **普通表单**

| 字段名称 | 对应的组件类型 | 操作符 | 单独的检索条件示例 |
| --- | --- | --- | --- |
| 实例标题 | 不支持 | - | - |
| 提交人 | 成员/下拉单选 | 等于(eq) | ``` [{  "key": "originator",  "value": "012415166737967854",  "type": "STRING",  "operator": "eq",  "componentName": "EmployeeField" }] ``` |
| 提交人组织  **[!NOTE]**  仅支持一级，与提交人部门无关 | 成员/下拉单选 | 等于(eq) | ``` [{  "key": "originatorCorp",  "value": "ding5d17e3add038d44535c2f4657eb6378f",  "type": "ARRAY",  "operator": "eq",  "componentName": "SelectField" }] ``` |
| 创建时间 | 日期 | - 大于(gt) - 大于等于(ge) - 小于(lt) - 小于等于(le) - 介于(between) | - 大于：     ```   [{    "key": "createTime",    "value": 1649260800000,    "type": "DOUBLE",    "operator": "gt",    "componentName": "DateField"   }]   ``` - 介于：     ```   [{    "key": "createTime",    "value": [1649952000000, 1652198400000],    "type": "DOUBLE",    "operator": "between",    "componentName": "DateField"   }]   ``` |
| 修改时间 | 日期 | - 大于(gt) - 大于等于(ge) - 小于(lt) - 小于等于(le) - 介于(between) | - 大于：     ```   [{    "key": "modifiedTime",    "value": 1649260800000,    "type": "DOUBLE",    "operator": "gt",    "componentName": "DateField"   }]   ``` - 介于：     ```   [{    "key": "modifiedTime",    "value": [1649952000000, 1652198400000],    "type": "DOUBLE",    "operator": "between",    "componentName": "DateField"   }]   ``` |
| 流水号 | 文本 | 等于(eq) | ``` [{  "key": "serialNo",  "value": "TKASNJASFF",  "type": "TEXT",  "operator": "eq",  "componentName": "TextField" }] ``` |

#### **流程表单 (支持普通表单的预置字段)**

| 字段名称 | 对应的组件类型 | 操作符 | 单独的检索条件示例 |
| --- | --- | --- | --- |
| 当前节点名称 | 文本 | - 等于(eq) - 匹配（like） | ``` [{  "key": "currentNodeName",  "value": "主管审批",  "type": "TEXT",  "operator": "eq",  "componentName": "TextField" }] ``` |
| 流程审批结果 | 下拉 | 包含(in) | ``` [{  "key": "processApprovedResult",  "value": ["agree"],  "type": "ARRAY",  "operator": "in",  "componentName": "SelectField" }] ``` |
| 流程实例状态 | 下拉复选 | 包含（in）  **value枚举**:   - "RUNNING" - "NEW" - "PAUSED" - "TERMINATED" - "COMPLETED" - "ERROR" - "CANCELED" | ``` [{  "key": "processInstanceStatus",  "value": ["RUNNING", "NEW", "PAUSED", "TERMINATED", "COMPLETED", "ERROR", "CANCELED"],  "type": "ARRAY",  "operator": "in",  "componentName": "SelectField" }] ``` |
| 任务ID | 文本 | - 等于(eq) - 匹配（like） | ``` [{  "key": "taskId",  "value": "123",  "type": "TEXT",  "operator": "eq",  "componentName": "TextField" }] ``` |

## **表单实例FormData结构**

FormData示例：

```
{
  //单行文本
  "textField_l28nuccb":"单行文本",      
  //多行文本
  "textareaField_l28nuccc":"多行文本",
  //数值
  "numberField_l28nuccd":100,
  "numberField_l28nuccd_value":"100",
  //单选
  "selectField_l28nucch_id":"选项一",
  "selectField_l28nucch":"选项一",
  //复选
  "multiSelectField_l28nucci":["选项一","选项二"],
  "multiSelectField_l28nucci_id":["选项一","选项二"],
  //评分
  "rateField_l28nuccg":5,
  "rateField_l28nuccg_value":"5",
  //下拉单选
  "radioField_l28nucce":"选项一",
  "radioField_l28nucce_id":"选项一",
  //下拉复选
  "checkboxField_l28nuccf":["选项一","选项二"],
  "checkboxField_l28nuccf_id":["选项一","选项二"],
  //级联选择
  "cascadeSelectField_l28nuccj":["部门","A部门"],
  "cascadeSelectField_l28nuccj_id":["part","part_a"],
  //日期
  "dateField_l28nucck":1650470400000,
  //日期区间
  "cascadeDateField_l28nuccl":["1650470400000","1651248000000"],
  //图片
  "imageField_l28nuccm":"[
    {
      \"previewUrl\":\"/ossFileHandle?appType=A&fipe=open&siz0,limit_0/qity,q_80\",
    \"size\":42070,\"name\":\"iShot2022-04-21 14.06.21.png\",
    \"downloadUrl\":\"/ossFileHandle?appType=APe=download\",
    \"url\":\"/ossFileHandle?appType=AP$$.png&instId=&type=download\"
    }
  ]",
  //附件
  "attachmentField_l28nuccn":"[
    {
    \"downloadUrl\":\"/ossFileHandle?appType=APPd=&type=download\",
    \"name\":\"111.doc\",
    \"previewUrl\":\"/inst/preview?appType=A0VloadNQ$$.doc\",
    \"size\":15095,\"url\":\"/ossFileHandle?appTywnload\"
    }
  ]",
  //成员
  "employeeField_l28nucco":["员工小钉"],
  "employeeField_l28nucco_id":["163972776256429"]
  //子表单
  "tableField_l28nuccp":[{"textField_l28nuccq":"子表单的单行文本"}],
  //部门
  "departmentSelectField_l28nuccv":["测试部门"],
  "departmentSelectField_l28nuccv_id":["609916162"],  
  //国家/地区
  "countrySelectField_l28nuccw":["中国"], 
  "countrySelectField_l28nuccw_id":["CN"],  
  //地址
  "addressField_l28nuccx":"
  {
  \"address\":\"绿地中心阿里A座\",\"regionIds\":[110000,110100,110105,110105038],
  \"regionText\":[
  { 
  \"en_US\":\"bei jing\",\"zh_CN\":\"北京\"
},
{
  \"en_US\":\"bei jing shi\",\"zh_CN\":\"北京市\"
},
{
  \"en_US\":\"chao yang qu\",\"zh_CN\":\"朝阳区\"
},
{
  \"en_US\":\"cui ge zhuang xiang\",\"zh_CN\":\"崔各庄乡\"
}
]
}",
"addressField_l28nuccx_id":"\"北京/北京市/朝阳区/崔各庄乡/绿地中心阿里A座\"",
//电子签名
"digitalSignatureField_l28nucd5":"https://tianshu-vpc.ce451.png",
}
```

## **搜索结果排序**

搜索表单实例和流程表单实例，可以按照一定排序规则对搜索结果进行排序。

可以用于构建排序规则的字段包括:

- 表单组件ID
- 内置字段

### **排序示例**

需求1：按照提交时间降序再按照数字组件numberField\_adfeadffad的值降序排序 。

排序规则可以写成: {"gmt\_create":"-","numberField\_adfeadffad":"-"} ， 其中numberField\_adfeadffad是表单组件ID，gmt\_create是内置字段，“-”表示降序。表单组件ID可以在表单设计器里选择相应组件查看组件ID，内置字段参考下面小节。

需求2: 按照数字组件numberField\_adfeadffad的值降序再按照提交时间升序排序。

排序规则可以写成: {"numberField\_adfeadffad":"-","gmt\_create":"+"} ， 其中numberField\_adfeadffad是表单组件ID，gmt\_create是内置字段，“-”表示降序，“+”表示升序。表单组件ID可以在表单设计器里选择相应组件查看组件ID，内置字段参考下面小节。

### **内置字段说明**

> **[!NOTE]**
>
> 针对流水号、数据id（表单实例ID）等内置字段，宜搭表单的元数据有新版、旧版区别，判断方法见下表字段名。

| 字段含义 | 字段名 |
| --- | --- |
| 流水号 | - 新版元数据字段名：serial\_no - 旧版元数据字段名：yida\_serial\_no   **[!NOTE]**  通过以下方式判断：  调用[查询宜搭应用列表](0353-query-the-application-list.md)接口，返回appConfig信息是否有"SUPPORT\_META\_3":"y"。   - 包含，说明是新版元数据。 - 不包含，说明是旧版元数据。 |
| 数据id（表单实例ID） | - 新版元数据字段名：pid - 旧版元数据字段名：guid   **[!NOTE]**  通过以下方式判断：  调用[查询宜搭应用列表](0353-query-the-application-list.md)接口，返回appConfig信息，是否包含"SUPPORT\_META\_3":"y"。   - 包含"SUPPORT\_META\_3":"y"，说明是新版元数据。 - 不包含"SUPPORT\_META\_3":"y"，说明是旧版元数据。 |
| 流程实例状态 | process\_status |
| 提交人 | creator |
| 流程当前节点名称 | current\_node\_name |
| 流程审批结果 | approved\_result |
| 提交人组织 | yida\_originator\_corp\_id |
| 提交时间 | gmt\_create |
| 修改时间 | gmt\_modified |
| 流程实例标题 | title |
