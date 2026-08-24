---
title: "创建或更新审批模板"
source_url: "https://open.dingtalk.com/document/development/create-orupdate-the-approval-template-new"
namespace: "development"
slug: "create-orupdate-the-approval-template-new"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 审批表单 > 创建或更新审批模板"
doc_id: "CDZ586EPGm"
updated_at: "2026-06-03 10:12:36"
---

> Source: https://open.dingtalk.com/document/development/create-orupdate-the-approval-template-new
> Path: 应用开发 / 服务端API / OA 审批 > 自有 OA 审批 > 审批表单 > 创建或更新审批模板
> Updated: 2026-06-03 10:12:36

# 创建或更新审批模板

调用本接口，创建或更新审批模板。

## **接口调用说明**

- 每个企业最多创建流程中心200个模板，超过最大数量后调用接口会报错。
- 钉钉客户端展示审批列表时，仅展示模板表单的前三个选项。
- 调用该接口创建的自有审批流模板，使用的模板名称和接口返回的processCode值，请务必注意保存，方便后续调用其他接口使用。
- 自有OA审批模板仅支持文档下方所展示的审批组件，其他组件均不支持。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/schemas |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Form.Write-工作流模板写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 否 | 表单ProcessCode，更新表单模板时需指定ProcessCode，可通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取processCode参数值。      如果传递ProcessCode进行表单组件修改和更新，不允许删除或修改已作为流程设计中条件分支的控件数据。 例如，原表单中存在单选控件【员工类型】作为分支条件，则更新此表单时，不允许修改或删除【员工类型】字段的控件类型。     - 未填写该参数，表示新建一个模板。 - 填写该参数，表示更新所传值对应的审批模板。 |
| name | String | 是 | 表单模板名称，最大长度200字符。 |
| description | String | 否 | 表单模板描述，最大长度300字符。 |
| formComponents | Array | 是 | 表单控件列表，支持的控件列表如下，单一表单最大组件个数不超过200。  支持的控件类型，详情请参考本文**FormComponent参数补充说明**。   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件 - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件（表格控件） - **DDAttachment**：附件 - **InnerContactField**：联系人控件 - **RelateField**：关联审批单 - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件 |
| FormComponent | FormComponent | 是 | 表单控件，支持的控件参考[FormComponent参数说明](0474-oa-formcomponent-message.md#900adc515fxr6)，单一表单最大组件个数不超过200。 |
| processFeatureConfig | Object | 否 | 流程中心集成配置。 |
| features | Array | 否 | 配置列表。 |
| name | String | 否 | 支持三方进行自定义配置的功能模块名称，当前支持：   - **TASK\_EXECUTE**：任务执行模块，即详情页的同意、拒绝按钮 - **SYNC\_BOXSTER**：任务同步待办方式 - **CUSTOM\_SHORTCUT**：待办、卡片通知中的快捷操作按钮 - **AFFILIATION\_DIR**：指定待办业务分组 |
| pcUrl | String | 否 | 三方自定义的pc端跳转链接，最大长度1024字符。 |
| mobileUrl | String | 否 | 三方自定义的手机端跳转链接，最大长度1024字符。 |
| runType | String | 否 | 运行方式。 当features.name为`TASK_EXECUTE`时，支持   - **ORIGIN**：原生运行，即在官方审批内运行对应功能，将会回调callback中配置的回调接口 - **REDIRECT**：外部跳转运行，需要跳转到三方地址运行对应功能，将会跳转到pcUrl、mobileUrl中配置的地址   当features.name为`SYNC_BOXSTER`时，支持   - **DEFAULT**：默认将审批任务同步待办 - **OUTBIZ\_CUSTOM**：不同步待办，由业务自定义实现   当features.name为`CUSTOM_SHORTCUT`时，支持   - **ORIGIN**：原生运行，打开待办详情页时，将会跳转到官方审批的详情页地址 - **REDIRECT**：外部跳转运行，打开待办详情页时，将会跳转到pcUrl、mobileUrl中配置的地址   当features.name为`AFFILIATION_DIR`时，支持   - **OUTBIZ\_CUSTOM**：指定待办分组，由业务自定义指定待办归属的分类信息 |
| callback | Object | 否 | 网关回调配置，runType选ORIGIN类型时该参数必填。  网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)。 |
| appUuid | String | 否 | 网关appUuid，runType选ORIGIN类型时该参数必填。  传[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时所属企业corpId值。 |
| apiKey | String | 否 | 网关apiKey，runType选ORIGIN类型时该参数必填。通过[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)内容获取`apiKey`。       - 在网关回调外部接口时，钉钉侧会根据不同业务场景，回传一些业务处理所需的参数给到ISV，ISV在收到回调请求后，若需要解析获取对应参数信息，需要在[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时配置对应的参数key。   例如，TASK\_EXECUTE任务执行模块，即详情页的同意、拒绝按钮配置回调时，钉钉侧回传的固定参数如下：`{"outResult":"agree","processInstanceId":"xxx","activityId":"xxx","corpId":"dingxxx","data":[],"remark":"同意","title":"xxx提交的资产领用申请","taskId":111,"operator":"manager0001"}`。 - ISV在创建数据源时，对应的参数配置需按业务需要填对应的key进行解析：outResult,processInstanceId,activityId,corpId,remark,title,taskId,operator |
| version | String | 否 | 网关接口版本       - runType选ORIGIN类型时该参数必填。 - 默认传1。 |
| config | String | 否 | 三方进行自定义配置的功能模块对应的配置信息。 |
| templateConfig | Object | 否 | 流程中心模板配置。 |
| hidden | Boolean | 否 | 是否为隐藏模板：   - **true**：是隐藏模板 - **false**：不是隐藏模板 |
| createInstanceMobileUrl | String | 否 | 表单创建移动端地址，最大长度1024字符。 |
| createInstancePcUrl | String | 否 | 表单创建PC端地址，最大长度1024字符。 |
| templateEditUrl | String | 否 | 模板编辑地址，最大长度1024字符。 |
| disableSendCard | Boolean | 否 | 创建流程中心待处理任务时是否禁用消息卡片通知：   - **true**：禁用，将不发送消息卡片通知 - **false**：默认值，不禁用，将发送消息卡片通知 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processCentres/schemas HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
    "name":"出差报销审批",
    "description":"用于员工差旅费用报销使用",
    // 有processCode字段时表示更新模板，无processCode表示创建模板，本示例采用创建模板
    // "processCode":"PROC-9EA4B75F-****-****-****-AC70E0704E3D",
    "formComponents": [
        {
            "componentType": "TextField",
            "props": {
                "label": "单行输入框", // 控件标题
                "placeholder": "请输入", // 输入提示
                "componentId": "TextField_17EZKEGSOCTC0", // 控件id，表单内唯一，无业务语义
                "required": false, // 是否必填，默认非必填
                "bizAlias": "staffId" // 控件的业务标识，表单内唯一，与componentId二选一
            }
        },
        {
            "componentType": "TextareaField",
            "props": {
                "label": "多行输入框",
                "placeholder": "请输入",
                "componentId": "TextareaField_17EZKEGSOCTC0",
                "required": false
            }
        },
        {
            "componentType": "NumberField",
            "props": {
                "label": "数字输入框",
                "placeholder": "请输入数字",
                "componentId": "NumberField_108PIFZM21F40",
                "required": false,
                "unit": "元", // 数字单位
                "defaultValue": "10" // 默认值
            }
        },
        {
            "componentType": "DDSelectField",
            "props": {
                "options": [ // 可选选项列表
                    {
                        "value": "选项1", // 选项显示名称
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
        },
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
        },
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
        },
        {
            "componentType": "DDDateRangeField",
            "props": {
                "unit": "小时",
                "format": "yyyy-MM-dd HH:mm",
                "bizAlias": "",
                "label": "[\"开始时间\",\"结束时间\"]",
                "placeholder": "请选择",
                "componentId": "DDDateRangeField_7MPG14N3OOO0",
                "duration": true, // 是否自动计算时长
                "durationLabel": "时长", // 时长计算显示文本
                "required": false
            }
        },
         {
            "componentType": "TextNote",
            "props": {
                "link": "https://www.dingtalk.com/", // 超链接
                "notPrint": "0",
                "bizAlias": "",
                "componentId": "TextNote_13RP7230RAF40",
                "content": "说明文字" // 说明文字
            }
        },
        {
            "componentType": "DDPhotoField",
            "props": {
                "label": "图片",
                "componentId": "DDPhotoField_P50A0HMHB280",
                "required": false
            }
        },
        {
            "componentType": "MoneyField",
            "props": {
                "upper": "0", // 金额需要大写(0不大写，1需要大写)，默认需要大写
                "label": "金额（元）",
                "placeholder": "请输入金额",
                "componentId": "MoneyField_L1PP26ZDV400",
                "required": false
            }
        },
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
                "verticalPrint": true, // 明细打印方式，true：纵向 false：横向
                "statField": [ // 设置对数字、金额类控件进行总数统计
                    {
                        "upper": "1",
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
        },
        {
            "componentType": "DDAttachment",
            "props": {
                "label": "附件",
                "componentId": "DDAttachment_18U4QTOWLMPS0",
                "required": false
            }
        },
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
        },
        {
            "componentType": "DepartmentField",
            "props": {
                "multiple": false, // 是否支持多选，true多选，false单选
                "label": "部门",
                "placeholder": "请选择",
                "componentId": "DepartmentField_1GY5JSPOCY000",
                "required": false
            }
        },
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
                        "name": "我的模板", // 可关联的审批表单名称
                        "processCode": "PROC-9EA4B75F-****-****-****-AC70E0704E3D" // 可关联的审批表单formCode
                    }
                ]
            }
        },
        {
            "componentType": "AddressField",
            "props": {
                "addressModel": "district", // 枚举值,city省市,district省市区,street省市区-街道
                "bizAlias": "",
                "label": "省市区",
                "componentId": "AddressField_1P9H21H8R2LC0",
                "required": false
            }
        },
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
    ],
    "processFeatureConfig":{
        "features":[
            {
                "name":"TASK_EXECUTE",
                "pcUrl":"https://www.dingtalk.com",
                "mobileUrl":"https://www.dingtalk.com",
                "runType":"REDIRECT"
            }
        ]
    }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkworkflow_1_0.*;
import com.aliyun.dingtalkworkflow_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        SaveProcessHeaders saveProcessHeaders = new SaveProcessHeaders();
        saveProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
        // 1. 单行输入控件
        FormComponentProps formComponentProps1 = new FormComponentProps()
                .setComponentId("TextField-abcd")
                .setPlaceholder("请输入")
                .setLabel("单行输入")
                .setRequired(true);
        FormComponent formComponent1 = new FormComponent()
                .setComponentType("TextField")
                .setProps(formComponentProps1);
        // 2. 多行输入控件
        FormComponentProps formComponentProps2 = new FormComponentProps()
                .setComponentId("TextareaField-abcd")
                .setPlaceholder("请输入")
                .setLabel("多行输入")
                .setRequired(true);
        FormComponent formComponent2 = new FormComponent()
                .setComponentType("TextareaField")
                .setProps(formComponentProps2);
        // 3. 数字输入控件
        FormComponentProps formComponentProps3 = new FormComponentProps()
                .setComponentId("NumberField-abcd")
                .setPlaceholder("请输入")
                .setLabel("数字输入")
                .setUnit("元")
                .setRequired(true);
        FormComponent formComponent3 = new FormComponent()
                .setComponentType("NumberField")
                .setProps(formComponentProps3);
        // 4. 单选控件
        SelectOption option1 = new SelectOption();
        option1.setKey("option1");
        option1.setValue("选项1");
        SelectOption option2 = new SelectOption();
        option2.setKey("option2");
        option2.setValue("选项2");
        FormComponentProps formComponentProps4 = new FormComponentProps()
                .setComponentId("DDSelectField-abcd")
                .setPlaceholder("请选择")
                .setLabel("单选")
                .setBizAlias("staff_type")
                .setOptions(java.util.Arrays.asList(option1, option2))
                .setRequired(true);
        FormComponent formComponent4 = new FormComponent()
                .setComponentType("DDSelectField")
                .setProps(formComponentProps4);

        // 5. 多选控件
        SelectOption option3 = new SelectOption();
        option3.setKey("option1");
        option3.setValue("选项1");
        SelectOption option4 = new SelectOption();
        option4.setKey("option2");
        option4.setValue("选项2");
        FormComponentProps formComponentProps5 = new FormComponentProps()
                .setComponentId("DDMultiSelectField-abcd")
                .setPlaceholder("请选择")
                .setLabel("多选")
                .setOptions(java.util.Arrays.asList(option3, option4))
                .setRequired(true);
        FormComponent formComponent5 = new FormComponent()
                .setComponentType("DDMultiSelectField")
                .setProps(formComponentProps5);

        // 6. 日期控件
        FormComponentProps formComponentProps6 = new FormComponentProps()
                .setComponentId("DDDateField-abcd")
                .setPlaceholder("请选择")
                .setLabel("日期")
                .setUnit("小时")
                .setFormat("yyyy-MM-dd HH:mm")
                .setRequired(true);
        FormComponent formComponent6 = new FormComponent()
                .setComponentType("DDDateField")
                .setProps(formComponentProps6);

        // 7. 时间区间控件
        FormComponentProps formComponentProps7 = new FormComponentProps()
                .setComponentId("DDDateRangeField-abcd")
                .setPlaceholder("请选择")
                .setLabel("[\"开始时间\",\"结束时间\"]")
                .setUnit("小时")
                .setFormat("yyyy-MM-dd HH:mm")
                .setRequired(true);
        FormComponent formComponent7 = new FormComponent()
                .setComponentType("DDDateRangeField")
                .setProps(formComponentProps7);

        // 8. 文字说明控件
        FormComponentProps formComponentProps8 = new FormComponentProps()
                .setComponentId("TextNote-abcd")
                .setLabel("说明")
                .setContent("详细说明内容")
                .setLink("https://www.dingtalk.com/")
                .setPrint("0")
                .setRequired(false);
        FormComponent formComponent8 = new FormComponent()
                .setComponentType("TextNote")
                .setProps(formComponentProps8);

        // 10. 图片控件
        FormComponentProps formComponentProps10 = new FormComponentProps()
                .setComponentId("DDPhotoField-abcd")
                .setLabel("图片");
        FormComponent formComponent10 = new FormComponent()
                .setComponentType("DDPhotoField")
                .setProps(formComponentProps10);

        // 11. 金额控件
        FormComponentProps formComponentProps11 = new FormComponentProps()
                .setComponentId("MoneyField-abcd")
                .setUpper("0")
                .setPlaceholder("请输入金额")
                .setLabel("奖金（元）");
        FormComponent formComponent11 = new FormComponent()
                .setComponentType("MoneyField")
                .setProps(formComponentProps11);
                
        // 12. 明细控件
        // 12.1. 明细中子控件 数字输入控件
        FormComponentProps childFormComponentProps1 = new FormComponentProps()
                .setComponentId("NumberField-child-1")
                .setPlaceholder("请输入")
                .setLabel("数字输入")
                .setUnit("元")
                .setRequired(true);
        FormComponent childFormComponentChild1 = new FormComponent()
                .setComponentType("NumberField")
                .setProps(childFormComponentProps1);

        // 12.2. 明细中子控件 单行输入控件
        FormComponentProps childFormComponentProps2 = new FormComponentProps()
                .setComponentId("TextField-child-2")
                .setPlaceholder("请输入")
                .setLabel("单行输入")
                .setRequired(true);
        FormComponent childFormComponent2 = new FormComponent()
                .setComponentType("TextField")
                .setProps(childFormComponentProps2);
        // 12.2. 明细中汇总子控件数字统计
        FormComponentProps.FormComponentPropsStatField statField1 = new FormComponentProps.FormComponentPropsStatField();
        statField1.setComponentId("NumberField-child-1");
        statField1.setLabel("数字输入");

        FormComponentProps formComponentProps12 = new FormComponentProps()
                .setComponentId("TableField-abcd")
                .setUpper("0")
                .setTableViewMode("table")
                .setLabel("明细")
                .setStatField(java.util.Arrays.asList(statField1));
        FormComponent formComponent12 = new FormComponent()
                .setComponentType("TableField")
                .setProps(formComponentProps12)
                .setChildren(java.util.Arrays.asList(childFormComponentChild1, childFormComponent2));  

        // 13. 附件控件
        FormComponentProps formComponentProps13 = new FormComponentProps()
                .setComponentId("DDAttachment-abcd")
                .setLabel("附件");
        FormComponent formComponent13 = new FormComponent()
                .setComponentType("DDAttachment")
                .setProps(formComponentProps13);

        // 14. 联系人控件
        FormComponentProps formComponentProps14 = new FormComponentProps()
                .setComponentId("InnerContactField-abcd")
                .setLabel("联系人")
                .setChoice("1");
        FormComponent formComponent14 = new FormComponent()
                .setComponentType("InnerContactField")
                .setProps(formComponentProps14);

        // 15. 部门控件
        FormComponentProps formComponentProps15 = new FormComponentProps()
                .setComponentId("DepartmentField-abcd")
                .setLabel("部门")
                .setMultiple(false);
        FormComponent formComponent15 = new FormComponent()
                .setComponentType("DepartmentField")
                .setProps(formComponentProps15);

        // 16. 关联审批单控件
        AvaliableTemplate template = new AvaliableTemplate();
        template.setName("出差申请单");
        template.setProcessCode("出差申请单的ProcessCode");
        FormComponentProps formComponentProps16 = new FormComponentProps()
                .setComponentId("RelateField-abcd")
                .setLabel("关联审批单")
                .setAvailableTemplates(java.util.Arrays.asList(template));
        FormComponent formComponent16 = new FormComponent()
                .setComponentType("RelateField")
                .setProps(formComponentProps16);

        // 17. 省市区控件
        FormComponentProps formComponentProps17 = new FormComponentProps()
                .setComponentId("AddressField-abcd")
                .setLabel("省市区")
                .setPlaceholder("请选择")
                .setAddressModel("city");
        FormComponent formComponent17 = new FormComponent()
                .setComponentType("AddressField")
                .setProps(formComponentProps17);

        // 18. 评分控件
        FormComponentProps formComponentProps18 = new FormComponentProps()
                .setComponentId("StarRatingField-abcd")
                .setLabel("请输入")
                .setLimit(5);
        FormComponent formComponent18 = new FormComponent()
                .setComponentType("StarRatingField")
                .setProps(formComponentProps18);        
            
        SaveProcessRequestProcessFeatureConfigFeatures features1 = new SaveProcessRequestProcessFeatureConfigFeatures()
            .setName("TASK_EXECUTE")
            .setRunType("REDIRECT")
            .setPcUrl("https://www.dingtalk.com")
            .setMobileUrl("https://www.dingtalk.com");

      	SaveProcessRequestProcessFeatureConfig processFeatureConfig = new SaveProcessRequestProcessFeatureConfig()
        		.setFeatures(java.util.Arrays.asList(features1));
        
        SaveProcessRequest saveProcessRequest = new SaveProcessRequest()
                .setName("出差报销审批")
                .setDescription("用于员工差旅费用报销使用")
                .setFormComponents(java.util.Arrays.asList(
                        formComponent1, formComponent2, formComponent3, formComponent4, formComponent5,
                        formComponent6, formComponent7, formComponent8, formComponent9, formComponent10,
                        formComponent11, formComponent12, formComponent13, formComponent14, formComponent15,
                        formComponent16, formComponent17
                ))
                .setProcessFeatureConfig(processFeatureConfig)
;
        try {
            client.saveProcessWithOptions(saveProcessRequest, saveProcessHeaders, new RuntimeOptions());
        } catch (TeaException err) {
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        } catch (Exception _err) {
            TeaException err = new TeaException(_err.getMessage(), _err);
            if (!com.aliyun.teautil.Common.empty(err.code) && !com.aliyun.teautil.Common.empty(err.message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }

        }        
    }
}
```

Python

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        save_Process_headers = dingtalkworkflow__1__0_models.SaveProcessHeaders()
        save_Process_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_components_0children_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0children_0props_fields_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsFieldsProps(
            component_id='TextField-1',
            label='姓名',
            required=True,
            print='1',
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            options=[
                form_components_0children_0children_0props_fields_0props_options_0
            ],
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top'
        )
        form_components_0children_0children_0props_fields_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsFields(
            props=form_components_0children_0children_0props_fields_0props
        )
        form_components_0children_0children_0props_data_source_target = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsDataSourceTarget()
        form_components_0children_0children_0props_data_source = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsDataSource(
            target=form_components_0children_0children_0props_data_source_target
        )
        form_components_0children_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsStatField()
        form_components_0children_0children_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0children_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenProps(
            label='姓名',
            async_condition=True,
            required=False,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top',
            invisible=True,
            link='http://www.',
            vertical_print=True,
            common_biz_type='custom_view',
            options=[
                form_components_0children_0children_0props_options_0
            ],
            stat_field=[
                form_components_0children_0children_0props_stat_field_0
            ],
            data_source=form_components_0children_0children_0props_data_source,
            fields=[
                form_components_0children_0children_0props_fields_0
            ]
        )
        form_components_0children_0children_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildren(
            props=form_components_0children_0children_0props
        )
        form_components_0children_0props_available_templates_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsAvailableTemplates(
            name='出差审批单',
            process_code='PROC-abcd'
        )
        form_components_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0props_fields_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsFieldsProps(
            component_id='TextField-1',
            label='姓名',
            label_editable_freeze=False,
            required=True,
            required_editable_freeze=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            options=[
                form_components_0children_0props_fields_0props_options_0
            ],
            not_upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top'
        )
        form_components_0children_0props_fields_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsFields(
            props=form_components_0children_0props_fields_0props
        )
        form_components_0children_0props_data_source_target = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsDataSourceTarget()
        form_components_0children_0props_data_source = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsDataSource(
            target=form_components_0children_0props_data_source_target
        )
        form_components_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsStatField()
        form_components_0children_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenProps(
            label='姓名',
            async_condition=True,
            required=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top',
            invisible=True,
            link='http://www.',
            vertical_print=True,
            common_biz_type='custom_view',
            options=[
                form_components_0children_0props_options_0
            ],
            print='1',
            stat_field=[
                form_components_0children_0props_stat_field_0
            ],
            data_source=form_components_0children_0props_data_source,
            fields=[
                form_components_0children_0props_fields_0
            ],
            address_model='city',
            limit=5,
            available_templates=[
                form_components_0children_0props_available_templates_0
            ],
            table_view_mode='table'
        )
        form_components_0children_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildren(
            component_type='NumberField',
            props=form_components_0children_0props,
            children=[
                form_components_0children_0children_0
            ]
        )
        form_components_0props_available_templates_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsAvailableTemplates(
            name='出差申请',
            process_code='PROC-abcd'
        )
        form_components_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0props_fields_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsFieldsProps(
            component_id='TextField-1',
            label='姓名',
            label_editable_freeze=False,
            required=True,
            required_editable_freeze=True,
            print='1',
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            options=[
                form_components_0props_fields_0props_options_0
            ],
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top'
        )
        form_components_0props_fields_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsFields(
            component_type='TextField',
            props=form_components_0props_fields_0props
        )
        form_components_0props_data_source_target = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsDataSourceTarget(
            app_uuid='SWAPP-abcd',
            app_type=0
        )
        form_components_0props_data_source = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsDataSource(
            type='form',
            target=form_components_0props_data_source_target
        )
        form_components_0props_stat_field_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsStatField(
            component_id='NumberField-abcd',
            label='金额'
        )
        form_components_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsProps(
            component_id='TextField-abcd',
            label='姓名',
            async_condition=True,
            required=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top',
            invisible=True,
            link='http://www.',
            vertical_print=True,
            common_biz_type='custom_view',
            options=[
                form_components_0props_options_0
            ],
            print='1',
            stat_field=[
                form_components_0props_stat_field_0
            ],
            data_source=form_components_0props_data_source,
            fields=[
                form_components_0props_fields_0
            ],
            multiple=True,
            limit=5,
            available_templates=[
                form_components_0props_available_templates_0
            ],
            table_view_mode='table'
        )
        form_components_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponents(
            component_type='TextField',
            props=form_components_0props,
            children=[
                form_components_0children_0
            ]
        )
        save_process_request = dingtalkworkflow__1__0_models.SaveProcessRequest(
            name='出差报销审批',
            description='用于员工差旅费用报销使用',
            form_components=[
                form_components_0
            ]
        )
        try:
            client.save_process_with_options(save_process_request, save_process_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        save_process_headers = dingtalkworkflow__1__0_models.SaveProcessHeaders()
        save_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_components_0children_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0children_0props_fields_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsFieldsProps(
            component_id='TextField-1',
            label='姓名',
            required=True,
            print='1',
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            options=[
                form_components_0children_0children_0props_fields_0props_options_0
            ],
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top'
        )
        form_components_0children_0children_0props_fields_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsFields(
            props=form_components_0children_0children_0props_fields_0props
        )
        form_components_0children_0children_0props_data_source_target = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsDataSourceTarget()
        form_components_0children_0children_0props_data_source = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsDataSource(
            target=form_components_0children_0children_0props_data_source_target
        )
        form_components_0children_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsStatField()
        form_components_0children_0children_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0children_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildrenProps(
            label='姓名',
            async_condition=True,
            required=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top',
            invisible=True,
            link='http://www.',
            vertical_print=True,
            common_biz_type='custom_view',
            options=[
                form_components_0children_0children_0props_options_0
            ],
            stat_field=[
                form_components_0children_0children_0props_stat_field_0
            ],
            data_source=form_components_0children_0children_0props_data_source,
            fields=[
                form_components_0children_0children_0props_fields_0
            ]
        )
        form_components_0children_0children_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenChildren(
            props=form_components_0children_0children_0props
        )
        form_components_0children_0props_available_templates_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsAvailableTemplates(
            name='出差审批单',
            process_code='PROC-abcd'
        )
        form_components_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0props_fields_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsFieldsProps(
            component_id='TextField-1',
            label='姓名',
            label_editable_freeze=False,
            required=True,
            required_editable_freeze=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            options=[
                form_components_0children_0props_fields_0props_options_0
            ],
            not_upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top'
        )
        form_components_0children_0props_fields_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsFields(
            props=form_components_0children_0props_fields_0props
        )
        form_components_0children_0props_data_source_target = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsDataSourceTarget()
        form_components_0children_0props_data_source = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsDataSource(
            target=form_components_0children_0props_data_source_target
        )
        form_components_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsStatField()
        form_components_0children_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildrenProps(
            label='姓名',
            async_condition=True,
            required=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top',
            invisible=True,
            link='http://www.',
            vertical_print=True,
            common_biz_type='custom_view',
            options=[
                form_components_0children_0props_options_0
            ],
            print='1',
            stat_field=[
                form_components_0children_0props_stat_field_0
            ],
            data_source=form_components_0children_0props_data_source,
            fields=[
                form_components_0children_0props_fields_0
            ],
            address_model='city',
            limit=5,
            available_templates=[
                form_components_0children_0props_available_templates_0
            ],
            table_view_mode='table'
        )
        form_components_0children_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsChildren(
            component_type='NumberField',
            props=form_components_0children_0props,
            children=[
                form_components_0children_0children_0
            ]
        )
        form_components_0props_available_templates_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsAvailableTemplates(
            name='出差申请',
            process_code='PROC-abcd'
        )
        form_components_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0props_fields_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsFieldsProps(
            component_id='TextField-1',
            label='姓名',
            label_editable_freeze=False,
            required=True,
            required_editable_freeze=True,
            print='1',
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            options=[
                form_components_0props_fields_0props_options_0
            ],
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top'
        )
        form_components_0props_fields_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsFields(
            component_type='TextField',
            props=form_components_0props_fields_0props
        )
        form_components_0props_data_source_target = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsDataSourceTarget(
            app_uuid='SWAPP-abcd',
            app_type=0
        )
        form_components_0props_data_source = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsDataSource(
            type='form',
            target=form_components_0props_data_source_target
        )
        form_components_0props_stat_field_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsStatField(
            component_id='NumberField-abcd',
            label='金额'
        )
        form_components_0props_options_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0props = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponentsProps(
            component_id='TextField-abcd',
            label='姓名',
            async_condition=True,
            required=True,
            content='我是说明文字控件',
            format='yyyy-MM-dd',
            upper='1',
            unit='天',
            placeholder='请输入',
            biz_alias='finance_name',
            biz_type='attendance.leave',
            duration=True,
            choice='0',
            disabled=True,
            align='top',
            invisible=True,
            link='http://www.',
            vertical_print=True,
            common_biz_type='custom_view',
            options=[
                form_components_0props_options_0
            ],
            print='1',
            stat_field=[
                form_components_0props_stat_field_0
            ],
            data_source=form_components_0props_data_source,
            fields=[
                form_components_0props_fields_0
            ],
            multiple=True,
            limit=5,
            available_templates=[
                form_components_0props_available_templates_0
            ],
            table_view_mode='table'
        )
        form_components_0 = dingtalkworkflow__1__0_models.SaveProcessRequestFormComponents(
            component_type='TextField',
            props=form_components_0props,
            children=[
                form_components_0children_0
            ]
        )
        save_process_request = dingtalkworkflow__1__0_models.SaveProcessRequest(
            name='出差报销审批',
            description='用于员工差旅费用报销使用',
            form_components=[
                form_components_0
            ]
        )
        try:
            await client.save_process_with_options_async(save_process_request, save_process_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

PHP

```
<?php

// This file is auto-generated, don't edit it. Thanks.
namespace AlibabaCloud\SDK\Sample;

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveProcessHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveProcessRequest\formComponents;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveProcessRequest\formComponents\props;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveProcessRequest;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveProcessRequest\processFeatureConfig;
use AlibabaCloud\Tea\Utils\Utils\RuntimeOptions;

class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Dingtalk Client
     */
    public static function createClient(){
        $config = new Config([]);
        $config->protocol = "https";
        $config->regionId = "central";
        return new Dingtalk($config);
    }

    /**
     * @param string[] $args
     * @return void
     */
    public static function main($args){
        $client = self::createClient();
        $saveProcessHeaders = new SaveProcessHeaders([]);
        $saveProcessHeaders->xAcsDingtalkAccessToken = "<your access token>";
           $formComponents0Props = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props([
            "componentId" => "TextField-abcd",
            "label" => "姓名",
            "required" => true,
            "content" => "我是说明文字控件",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "disabled" => true,         
        ]);
        $formComponents0 = new formComponents([
            "componentType" => "TextField",
            "props" => $formComponents0Props,
        ]);
        
$processFeatureConfig0 = new processFeatureConfig([
        ]);
        $saveProcessRequest = new SaveProcessRequest([
            "name" => "出差报销审批",
            "description" => "用于员工差旅费用报销使用",
            "formComponents" => [
                $formComponents0
            ],
            "processFeatureConfig" => [
                $processFeatureConfig0 
            ]
        ]);
        try {
            $client->saveProcessWithOptions($saveProcessRequest, $saveProcessHeaders, new RuntimeOptions([]));
        }
        catch (Exception $err) {
            if (!($err instanceof TeaError)) {
                $err = new TeaError([], $err->getMessage(), $err->getCode(), $err);
            }
            if (!Utils::empty_($err->code) && !Utils::empty_($err->message)) {
                // err 中含有 code 和 message 属性，可帮助开发定位问题
            }
        }
    }
}
$path = __DIR__ . \DIRECTORY_SEPARATOR . '..' . \DIRECTORY_SEPARATOR . 'vendor' . \DIRECTORY_SEPARATOR . 'autoload.php';
if (file_exists($path)) {
    require_once $path;
}
Sample::main(array_slice($argv, 1));
```

Go

```
// This file is auto-generated, don't edit it. Thanks.
package main

import (
  "os"
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  saveProcessHeaders := &dingtalkworkflow_1_0.SaveProcessHeaders{}
  saveProcessHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  formComponents0Props := &dingtalkworkflow_1_0.SaveProcessRequestFormComponentsProps{
    ComponentId: tea.String("TextField-abcd"),
    Label: tea.String("姓名"),
    Required: tea.Bool(true),
    Content: tea.String("我是说明文字控件"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    Duration: tea.Bool(true),
  
  formComponents0 := &dingtalkworkflow_1_0.SaveProcessRequestFormComponents{
    ComponentType: tea.String("TextField"),
    Props: formComponents0Props,
  }
  processFeatureConfig0 := &dingtalkworkflow_1_0.SaveProcessRequestProcessFeatureConfig{
  }
  saveProcessRequest := &dingtalkworkflow_1_0.SaveProcessRequest{
    Name: tea.String("出差报销审批"),
    Description: tea.String("用于员工差旅费用报销使用"),
    FormComponents: []*dingtalkworkflow_1_0.SaveProcessRequestFormComponents{formComponents0},
    ProcessFeatureConfig: dingtalkworkflow_1_0.SaveProcessRequestProcessFeatureConfig{processFeatureConfig0}
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SaveProcessWithOptions(saveProcessRequest, saveProcessHeaders, &util.RuntimeOptions{})
    if _err != nil {
      return _err
    }

    return nil
  }()

  if tryErr != nil {
    var err = &tea.SDKError{}
    if _t, ok := tryErr.(*tea.SDKError); ok {
      err = _t
    } else {
      err.Message = tea.String(tryErr.Error())
    }
    if !tea.BoolValue(util.Empty(err.Code)) && !tea.BoolValue(util.Empty(err.Message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }

  }
  return _err
}

func main() {
  err := _main(tea.StringSlice(os.Args[1:]))
  if err != nil {
    panic(err)
  }
}
```

Node.js

```
// This file is auto-generated, don't edit it
import Util, * as $Util from '@alicloud/tea-util';
import dingtalkworkflow_1_0, * as $dingtalkworkflow_1_0 from '@alicloud/dingtalk/workflow_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkflow_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkflow_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let saveProcessHeaders = new $dingtalkworkflow_1_0.SaveProcessHeaders({ });
    saveProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let formComponents0Props = new $dingtalkworkflow_1_0.SaveProcessRequestFormComponentsProps({
      componentId: "TextField-abcd",
      label: "姓名",
      required: true,
      content: "我是说明文字控件",
      placeholder: "请输入",
      bizAlias: "finance_name",
      disabled: true,  
    });
    let formComponents0 = new $dingtalkworkflow_1_0.SaveProcessRequestFormComponents({
      componentType: "TextField",
      props: formComponents0Props,
    });
    let processFeatureConfig0 = new $dingtalkworkflow_1_0.SaveProcessRequestFormComponents({
    });
    let saveProcessRequest = new $dingtalkworkflow_1_0.SaveProcessRequest({
      name: "出差报销审批",
      description: "用于员工差旅费用报销使用",
      formComponents: [
        formComponents0
      ],
      processFeatureConfig: processFeatureConfig0,
    });
    try {
      await client.saveProcessWithOptions(saveProcessRequest, saveProcessHeaders, new $Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

Client.main(process.argv.slice(2));
```

C#

```
// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

using Tea;
using Tea.Utils;

namespace AlibabaCloud.SDK.Sample
{
    public class Sample 
    {

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessHeaders saveProcessHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessHeaders();
            saveProcessHeaders.XAcsDingtalkAccessToken = "<your access token>";
                   AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestFormComponents.SaveProcessRequestFormComponentsProps formComponents0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestFormComponents.SaveProcessRequestFormComponentsProps
            {
                ComponentId = "TextField-abcd",
                Label = "姓名",
                Required = true,
                Content = "我是说明文字控件",
                BizAlias = "finance_name",
                Disabled = true,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestFormComponents formComponents0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestFormComponents
            {
                ComponentType = "TextField",
                Props = formComponents0Props,
 
            };

AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestProcessFeatureConfig processFeatureConfig0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestProcessFeatureConfig
            {
        
 
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest saveProcessRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest
            {
                Name = "出差报销审批",
                Description = "用于员工差旅费用报销使用",
                FormComponents = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveProcessRequest.SaveProcessRequestFormComponents>
                {
                    formComponents0
                },
ProcessFeatureConfig = processFeatureConfig0,
            };
            try
            {
                client.SaveProcessWithOptions(saveProcessRequest, saveProcessHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
            }
            catch (TeaException err)
            {
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
            catch (Exception _err)
            {
                TeaException err = new TeaException(new Dictionary<string, object>
                {
                    { "message", _err.Message }
                });
                if (!AlibabaCloud.TeaUtil.Common.Empty(err.Code) && !AlibabaCloud.TeaUtil.Common.Empty(err.Message))
                {
                    // err 中含有 code 和 message 属性，可帮助开发定位问题
                }
            }
        }

    }
}
```

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkworkflow__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkworkflow_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkworkflow_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::Client> client = make_shared<Alibabacloud_Dingtalkworkflow_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessHeaders> saveProcessHeaders = make_shared<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessHeaders>();
  saveProcessHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestFormComponentsProps> formComponents0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestFormComponentsProps>(map<string, boost::any>({
    {"componentId", boost::any(string("TextField-abcd"))},
    {"label", boost::any(string("姓名"))},
    {"required", boost::any(true)},
    {"content", boost::any(string("我是说明文字控件"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
  }));

  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestProcessFeatureConfig> processFeatureConfig0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestProcessFeatureConfig>();
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestFormComponents> formComponents0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestFormComponents>(map<string, boost::any>({
    {"componentType", boost::any(string("TextField"))},
    {"props", !formComponents0Props ? boost::any() : boost::any(*formComponents0Props)},

  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequest> saveProcessRequest = make_shared<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequest>(map<string, boost::any>({
    {"name", boost::any(string("出差报销审批"))},
    {"description", boost::any(string("用于员工差旅费用报销使用"))},
    {"formComponents", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::SaveProcessRequestFormComponents>({
      formComponents0
    }))}
    {"processFeatureConfig", processFeatureConfig}
  }));
  try {
    client->saveProcessWithOptions(saveProcessRequest, saveProcessHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 表单模板信息。 |
| processCode | String | 保存或更新的表单code。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "processCode" : "PROC-abcdef-example"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | formschema.error | 流程条件分支中已使用的表单控件不可修改或删除 | 流程条件分支中使用的表单控件的类型不可修改或删除 |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | processcode.error | processCode对应的审批流程不存在 | processCode对应的审批流程不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | parameter.error | 流程中心配置参数错误：%s | 流程中心配置参数错误 |
| 400 | processes.error | 获取模板列表失败 | 获取模板列表失败 |
| 400 | processes.error | 审批流已超过最大数量 | 审批流已超过最大数量 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | internalError | %s | 系统内部错误 |
| 400 | system.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | aflowProcessSetupNoPermission | 无操作审批流的权限，请检查processCode是否正确 | 无操作审批流的权限，请检查processCode是否正确 |
| 500 | system.error | 系统错误 | 系统错误 |
