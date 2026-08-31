---
title: "补充参数说明"
source_url: "https://open.dingtalk.com/document/development/oa-formcomponent-message"
namespace: "development"
slug: "oa-formcomponent-message"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 补充参数说明"
doc_id: "LiLwS3pdAi"
updated_at: "2025-11-24 21:12:19"
---

> Source: https://open.dingtalk.com/document/development/oa-formcomponent-message
> Path: 应用开发 / 服务端 API / OA 审批 > 补充参数说明
> Updated: 2025-11-24 21:12:19

# 补充参数说明

## FormComponent参数说明

**formComponents**为表单组件列表，组件并非支持Props中的所有属性，每个控件支持的属性请参见下文请求示例。部分容器类控件，例如审批套件、明细控件支持子控件结构，使用children进行定义子控件类型和属性，子控件仍遵循控件属性定义。 控件模型如下：

> **[!IMPORTANT]**
>
> 表单控件通用限制：
>
> - componentId：控件id，最大长度64字符。
> - bizAlias：控件的业务标识，表单内唯一，与componentId二选一，最大长度64字符。
> - label：控件标题，最大长度20字符。
> - placeholder：输入提示，最大长度128字符。
> - content：文字说明控件TextNote中的content内容，最大长度500字符。
> - 表格明细控件总长度上限65535字符，建议明细不超过100行。

#### 控件通用属性

```
{
  "componentId": "TextField-12345677",   // 控件id，表单内唯一，与bizAlias二选一
  "required":true,  // 控件是否必填
  "label": "单行文本",   // 控件标题
  "placeholder": "请输入",    // 输入提示
  "bizAlias": "staffId", // 控件的业务标识，表单内唯一，与componentId二选一
  "print": "0", // 是否参与打印(0标识字段不参与打印、1标识字段可打印)，默认可打印
  "disabled": false, // 是否可编辑
}
```

#### **地点控件**

```
{
   "componentType": "TimeAndLocationField",
   "props": {
       "label": "[\"当前时间\",\"当前地点\"]",
       "componentId": "TimeAndLocationField_1CVHM5TIIWR9C",
       "required": false,
       "mask": true
    }
}
```

#### 单行输入控件

```
{
    "componentType": "TextField",
    "props": {
       "label": "单行输入框",  // 控件标题
       "placeholder": "请输入", // 输入提示
       "componentId": "TextField_17EZKEGSOCTC0", // 控件id，表单内唯一，无业务语义
       "required": false, // 是否必填，默认非必填
       "bizAlias": "staffId" // 控件的业务标识，表单内唯一，与componentId二选一
    }
}
```

#### 多行输入控件

```
{
    "componentType": "TextareaField",
    "props": {
       "label": "多行输入框",
       "placeholder": "请输入多行文本内容，需要换行时请输入\r\n", // 输入提示
       "componentId": "TextareaField_17EZKEGSOCTC0",
       "required": false
    }
}
```

#### 数字输入控件

```
{
    "componentType": "NumberField",
    "props": {
       "label": "数字输入框",
       "placeholder": "请输入数字",
       "componentId": "NumberField_108PIFZM21F40",
       "required": false,
       "unit":"元", // 数字单位
       "defaultValue":"10",  // 默认值
    }
}
```

#### 单选控件

```
{
    "componentType": "DDSelectField",
    "props": {
        "options": [ // 可选选项列表
        {
            "value": "选项1",  // 选项显示名称
            "key": "option_0" // 控件内唯一key，非必填，系统会默认生成
        },
        {
            "value": "选项2",
            "key": "option_1"
        },
        {
            "value": "选项3",
            "key": "option_2"
        },
        {
            "key": "other", // 其他项特殊key
           "value": "其它"
        }
      ],
      "label": "单选框",
      "placeholder": "请选择",
      "componentId": "DDSelectField_14T8M4EKXAV40",
      "required": false
    }
}
```

#### 多选控件

```
{
    "componentType": "DDMultiSelectField",
    "props": {
       "options": [
        {
           "value": "选项1",
           "key": "option_0"
        },
        {
           "value": "选项2",
           "key": "option_1"
        },
        {
           "value": "选项3",
           "key": "option_2"
        },
        {
           "key": "other", // 其他项特殊key
           "value": "其它"
        }
      ],
      "label": "多选框",
      "placeholder": "请选择",
      "componentId": "DDMultiSelectField_1XJ7NG1GSD6O0",
      "required": false
    }
}
```

#### 日期控件

```
 {
    "componentType": "DDDateField",
    "props": {
       "unit": "小时", // 日期格式，枚举值（小时、天）
       "format": "yyyy-MM-dd HH:mm", // 日期格式，非必填，小时对应yyyy-MM-dd HH:mm，天对应yyyy-MM-dd HH:mm
       "bizAlias": "",
       "label": "日期",
       "placeholder": "请选择",
       "componentId": "DDDateField_SQL0DF3MS9C0",
       "required": false,
       "defaultValue": "2021-12-21 17:46" // 默认值
    }
}
```

#### 时间区间控件

```
{
    "componentType": "DDDateRangeField",
    "props": {
       "unit": "小时", // 日期格式，枚举值（小时、天）
       "format": "yyyy-MM-dd HH:mm", // 日期格式，非必填，小时对应yyyy-MM-dd HH:mm，天对应yyyy-MM-dd HH:mm
       "bizAlias": "",
       "label": "[\"开始时间\",\"结束时间\"]",
       "placeholder": "请选择",
       "componentId": "DDDateRangeField_7MPG14N3OOO0",
       "duration": true, // 是否自动计算时长
       "required": false
    }
}
```

#### 文字说明控件

```
{
    "componentType": "TextNote",
    "props": {
       "link": "https://www.dingtalk.com/", // 超链接
       "notPrint": "0",
       "bizAlias": "",
       "componentId": "TextNote_13RP7230RAF40",
       "content": "说明文字"  // 说明文字
    }
}
```

#### 图片控件

```
{
    "componentType": "DDPhotoField",
    "props": {
        "label": "图片",
        "componentId": "DDPhotoField_P50A0HMHB280",
        "required": false
    }
}
```

#### 金额控件

```
{
    "componentType": "MoneyField",
    "props": {
        "upper": "0", // 金额需要大写(0不大写，1需要大写)，默认需要大写
        "label": "金额（元）",
        "placeholder": "请输入金额",
        "componentId": "MoneyField_L1PP26ZDV400",
        "required": false
    }
}
```

#### **明细控件（表格控件）**

```
{
    "children": [ // 明细中的子控件列表，子控件列表遵循各控件属性标准
        {
            "componentType": "TextField",
            "props": {
                "label": "单行输入框",
                "placeholder": "请输入",
                "componentId": "TextField_1UE1ZY1A28AO0",
                "required": false
            }
        },
        {
            "componentType": "MoneyField",
            "props": {
                "payEnable": false,
                "upper": "0",
                "bizAlias": "",
                "label": "金额（元）",
                "placeholder": "请输入金额",
                "componentId": "MoneyField_1S85G4YLMM5C0",
                "required": false
            }
        },
        {
            "componentType": "NumberField",
            "props": {
                "unit": "元",
                "payEnable": false,
                "bizAlias": "",
                "label": "数字输入框",
                "placeholder": "请输入数字",
                "componentId": "NumberField_1XP6AWG50SE80",
                "required": false
            }
        }
    ],
    "componentType": "TableField",
    "props": {
        "tableViewMode": "table", // 明细填写方式，枚举值：list：列表,table：表格
        "verticalPrint": true,  // 明细打印方式，true：纵向 false：横向
        "statField": [  // 设置对数字、金额类控件进行总数统计
            {
                "upper": "",
                "componentId": "MoneyField_1S85G4YLMM5C0",
                "label": "金额（元）"
            },
            {
                "componentId": "NumberField_1XP6AWG50SE80",
                "label": "数字输入框"
            }
        ],
        "bizAlias": "",
        "label": "表格",
        "componentId": "TableField_1MLEPEAQSXHC0"
    }
}
```

#### 附件

```
{
    "componentType": "DDAttachment",
    "props": {
       "label": "附件",
       "componentId": "DDAttachment_18U4QTOWLMPS0",
       "required": false
    }
}
```

#### 联系人控件

```
 {
    "componentType": "InnerContactField",
    "props": {
      "label": "联系人",
      "placeholder": "请选择",
      "componentId": "InnerContactField_162USP4V1BC00",
      "choice": "1", //枚举值：1标识支持多选，0标识单选，默认为0
      "required": false,
      "bizAlias": ""
    }
}
```

#### 部门控件

```
{
    "componentType": "DepartmentField",
    "props": {
      "multiple": false, // 是否支持多选，true多选，false单选
      "label": "部门",
      "placeholder": "请选择",
      "componentId": "DepartmentField_1GY5JSPOCY000",
      "required": false
    }
}
```

#### 关联审批单

```
{
    "componentType": "RelateField",
    "props": {
       "label": "关联审批单",
       "placeholder": "请选择",
       "componentId": "RelateField_5X1DL4KMKUW0",
       "required": false,
       "bizAlias": "",
       "availableTemplates": [ // 可被关联的审批模板列表，为空时表示可关联所有审批模板的实例数据
        {
           "name": "产品演示", // 可关联的审批表单名称
           "processCode": "PROC-1B8FC788-D2B4-4DA2-BEAE-E56F5EC17C5B" // 可关联的审批表单formCode
        },
        {
           "name": "调岗套件演示",
           "processCode": "PROC-6C383FEC-3ED6-4B90-8019-401629CB8275"
        }
      ]
   }
}
```

#### 省市区控件

```
{
    "componentType": "AddressField",
    "props": {
       "addressModel": "district", // 枚举值,city省市,district省市区,street省市区-街道
       "bizAlias": "",
       "label": "省市区",
       "componentId": "AddressField_1P9H21H8R2LC0",
       "required": false
    }
}
```

#### 评分控件

```
{
    "componentType": "StarRatingField",
    "props": {
       "limit": 5, // 枚举值：5分制、10分制
       "label": "评分",
       "placeholder": "请输入",
       "componentId": "StarRatingField_10E5NHTA2W0G0",
       "required": false,
       "bizAlias": ""
    }
}
```

## **FormComponentValues 参数说明**

严格按照创建模板时的组件进行定义。可参考[FormComponent参数说明](#900adc505f44g) 为表单组件赋值：

### **地点控件**

```
{
    "name": "[\"当前时间\",\"当前地点\"]", // 控件 label 名称
    "value": "[\"2025-05-27 14:27:20\",120.021195,30.281506,\"浙江省杭州市余杭区文一西路960-1号阿里巴巴西溪C区\",100]"
}
```

### **单行输入控件**

```
{
    "name": "标题（单行输入框）", // 控件 label 名称
    "value": "测试标题（单行输入框）"
}
```

### **多行输入控件**

```
{
    "name": "说明（多行输入框）", // 控件 label 名称
    "value": "测试说明（多行输入框）"
}
```

### **数字输入控件**

```
{
    "name": "数字（数字输入框）",// 控件 label 名称
    "value": "10"
}
```

### **单选控件**

```
{
    "name": "单选",// 控件 label 名称
    "value": "1"
}
```

### **多选控件**

```
{
    "name": "多选",// 控件 label 名称
    "value": "[\"1\",\"2\"]"
}
```

### **日期控件**

```
{
    "name": "日期", // 控件 label 名称
    "value": "2025-05-27 10:00"
}
```

### **时间区间控件**

```
{
    "name": "[\"开始时间\",\"结束时间\"]", // 控件 label 名称
    "value": "[\"2025-05-27\",\"2025-05-28\"]"
}
```

### **电话控件**

```
{
    "name": "电话", // 控件 label 名称
    "value": "155****3240" //严格按照你创建模板时选择的电话组件设置的 mode 类型传参。
}
```

### **图片控件**

```
{
    "name": "图片", // 控件 label 名称
    "value": "[\"https://example.com/32-2-tps-1024-1024.png\",\"https://example.com/52-0-tps-717-670.jpg\"]"
}
```

### **金额控件**

```
{
    "name": "金额（元）", // 控件 label 名称
    "value": "5"
}
```

### **表格（明细）控件**

> **[!NOTE]**
>
> value值严格按照创建模板的子组件label进行定义，可参考[表格（明细）控件](#96dbc05ff0q43)。

```
{
    "name": "表格", // 控件 label 名称
    "value": "[[{\"name\":\"项目名称（单行输入框）\",\"value\":\"项目名称\"},{\"name\":\"项目金额（元）\",\"value\":\"100\"},{\"name\":\"项目人数（数字输入框）\",\"value\":\"10\"}]]"
}
```

### **附件**

```
{
    "name": "附件", // 控件 label 名称
    "value": "[{\"spaceId\": \"2662**5867\", \"fileName\": \"IMG_1561.JPG\", \"fileSize\": \"72891\", \"fileType\": \"jpg\", \"fileId\": \"1811****559\"}]"
}
```

### **联系人**

```
{
    "name": "联系人", // 控件 label 名称
    "value": "[\"0147282552401293909\", \"manager4974\"]" // 用户 userId 
}
```

### **部门控件**

```
{
    "name": "部门", // 控件 label 名称
    "value": "部门ID1,部门ID2"
}
```

### **关联审批单**

```
{
    "name": "关联审批单", // 控件 label 名称
    "value": "[\"RgJJ1veyQl2A****6841748395993\", \"p-OLRbmXSJeiN9*****841748395677\"]"
}
```

### **省市区**

```
{
    "name": "省市区", // 控件 label 名称
    "value": "北京,北京市,东城区"
}
```

### **评分**

```
{
    "name": "评分", // 控件 label 名称
    "value": "5"
}
```
