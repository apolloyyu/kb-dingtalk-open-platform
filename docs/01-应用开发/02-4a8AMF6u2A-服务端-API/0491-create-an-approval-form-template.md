---
title: "创建或更新审批表单模板"
source_url: "https://open.dingtalk.com/document/development/create-an-approval-form-template"
namespace: "development"
slug: "create-an-approval-form-template"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批表单 > 创建或更新审批表单模板"
doc_id: "rjHpOgnBJs"
updated_at: "2026-06-03 10:12:21"
---

> Source: https://open.dingtalk.com/document/development/create-an-approval-form-template
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批表单 > 创建或更新审批表单模板
> Updated: 2026-06-03 10:12:21

# 创建或更新审批表单模板

调用本接口，创建或更新一个OA审批的流程表单模板，可指定表单控件列表并生成默认审批流程。

## 接口调用说明

- 每个企业最多创建200个官方审批模板，超过最大数量后调用接口会报错。
- 官方OA审批模板仅支持文档下方所展示的审批组件，其他组件均不支持。
- 官方OA审批模板仅支持文档下方所展示的审批组件，其他组件均不支持。
- 更新审批模板时更新的组件在流程设计中设置为分支条件，则该模板表单不支持修改。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/forms |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Form.Write-工作流模板写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 否 | 表单ProcessCode，更新表单模板时需指定ProcessCode。    如果传递**ProcessCode**进行表单组件修改和更新，不允许删除或修改已作为流程设计中条件分支的控件数据。 例如原表单中存在**单选控件**【员工类型】作为分支条件，则更新此表单时，不允许修改【员工类型】字段的控件类型，也不允许删除。   - 未填写该参数，表示新建一个模板。 - 填写该参数，表示更新所传值对应的审批模板。   **如何获取process\_code**：在钉钉管理后台-审批模板查看。    新旧版钉钉管理后台，获取方式不同：可参见[OA审批概述-名词解释-processCode](0473-workflow-overview.md)。  **新版钉钉管理后台**：在审批模板编辑页-基础设置-页面底部查看。 **旧版钉钉管理后台**：在审批模板编辑页的URL中查看。 |
| name | String | 是 | 表单模板名称，最大长度200字符。 |
| description | String | 否 | 表单模板描述，最大长度300字符。 |
| formComponents | Array | 是 | 表单控件列表，单一表单最大组件个数不超过200。 |
| FormComponent | FormComponent | 是 | 表单控件列表，详情请参考[FormComponent参数说明](0474-oa-formcomponent-message.md#900adc515fxr6)参数补充说明。 |
| templateConfig | Object | 否 | 表单全局属性配置。 |
| disableStopProcessButton | Boolean | 否 | 管理列表页是否禁用**停用**按钮：   - **true**：是 - **false**：否 |
| hidden | Boolean | 否 | 是否全局隐藏流程模板入口。   - **true**：是 - **false**：否 |
| disableDeleteProcess | Boolean | 否 | 是否禁用模板**删除**按钮。   - **true**：是 - **false**：否 |
| disableFormEdit | Boolean | 否 | 是否禁止表单**编辑**功能。   - **true**：是 - **false**：否 |
| disableResubmit | Boolean | 否 | 是否禁用详情页**再次发起**按钮。   - **true**：是 - **false**：否 |
| disableHomepage | Boolean | 否 | 是否在首页隐藏模板。   - **true**：是 - **false**：否 |
| dirId | String | 否 | 模板的目录ID，创建模板目录时指定。 |
| originDirId | String | 否 | 原目录ID，更新模板目录时，需指定源目录ID。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/forms HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
    "name": "出差报销审批",
    "description": "用于员工差旅费用报销使用",
    "formComponents": [
        {
            "componentType": "TextField",
            "props": {
                "componentId": "TextField-abcd",
                "label": "文本框",
                "required": true,
                "bizAlias": "TextField-bizAlias",
                "disabled": false
            }
        },
        {
            "componentType": "TextareaField",
            "props": {
                "placeholder": "请输入",
                "label": "多行输入框"
            }
        },
        {
            "componentType": "NumberField",
            "props": {
                "placeholder": "请输入数字",
                "label": "数字输入框",
                "id": "NumberField-1"
            }
        },
        {
            "children": [
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
                        "upper": "0",
                        "bizAlias": "",
                        "label": "金额（元）",
                        "placeholder": "请输入金额",
                        "componentId": "MoneyField_1S85G0",
                        "required": false
                    }
                },
                {
                    "componentType": "NumberField",
                    "props": {
                        "unit": "元",
                        "bizAlias": "",
                        "label": "数字输入框",
                        "placeholder": "请输入数字",
                        "componentId": "NumberField_1XP6A",
                        "required": false
                    }
                }
            ],
            "componentType": "TableField",
            "props": {
                "tableViewMode": "table",
                "verticalPrint": true,
                "statField": [
                    {
                        "componentId": "MoneyField_1S85G0",
                        "label": "金额（元）"
                    },
                    {
                        "componentId": "NumberField_1XP6A",
                        "label": "数字输入框"
                    }
                ],
                "bizAlias": "table",
                "label": "表格",
                "componentId": "TableField_1MLEPEA"
            }
        }
    ]
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
        FormCreateHeaders formCreateHeaders = new FormCreateHeaders();
        formCreateHeaders.xAcsDingtalkAccessToken = "<your access token>";
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

        // 9. 电话控件
        FormComponentProps formComponentProps9 = new FormComponentProps()
                .setComponentId("PhoneField-abcd")
                .setLabel("电话")
                .setMode("phone")
                .setRequired(true);
        FormComponent formComponent9 = new FormComponent()
                .setComponentType("PhoneField")
                .setProps(formComponentProps9);

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

        FormCreateRequest formCreateRequest = new FormCreateRequest()
                .setName("出差报销审批")
                .setDescription("用于员工差旅费用报销使用")
                .setFormComponents(java.util.Arrays.asList(
                        formComponent1, formComponent2, formComponent3, formComponent4, formComponent5,
                        formComponent6, formComponent7, formComponent8, formComponent9, formComponent10,
                        formComponent11, formComponent12, formComponent13, formComponent14, formComponent15,
                        formComponent16, formComponent17
                ));
        try {
            client.formCreateWithOptions(formCreateRequest, formCreateHeaders, new RuntimeOptions());
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
        form_create_headers = dingtalkworkflow__1__0_models.FormCreateHeaders()
        form_create_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_components_0children_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0children_0props_fields_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps(
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
        form_components_0children_0children_0props_fields_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsFields(
            props=form_components_0children_0children_0props_fields_0props
        )
        form_components_0children_0children_0props_data_source_target = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget()
        form_components_0children_0children_0props_data_source = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource(
            target=form_components_0children_0children_0props_data_source_target
        )
        form_components_0children_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsStatField()
        form_components_0children_0children_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0children_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenProps(
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
        form_components_0children_0children_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildren(
            props=form_components_0children_0children_0props
        )
        form_components_0children_0props_available_templates_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates(
            name='出差审批单',
            process_code='PROC-abcd'
        )
        form_components_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0props_fields_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsFieldsProps(
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
        form_components_0children_0props_fields_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsFields(
            props=form_components_0children_0props_fields_0props
        )
        form_components_0children_0props_data_source_target = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsDataSourceTarget()
        form_components_0children_0props_data_source = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsDataSource(
            target=form_components_0children_0props_data_source_target
        )
        form_components_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsStatField()
        form_components_0children_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenProps(
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
        form_components_0children_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildren(
            component_type='NumberField',
            props=form_components_0children_0props,
            children=[
                form_components_0children_0children_0
            ]
        )
        form_components_0props_available_templates_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsAvailableTemplates(
            name='出差申请',
            process_code='PROC-abcd'
        )
        form_components_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0props_fields_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsFieldsProps(
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
        form_components_0props_fields_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsFields(
            component_type='TextField',
            props=form_components_0props_fields_0props
        )
        form_components_0props_data_source_target = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsDataSourceTarget(
            app_uuid='SWAPP-abcd',
            app_type=0
        )
        form_components_0props_data_source = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsDataSource(
            type='form',
            target=form_components_0props_data_source_target
        )
        form_components_0props_stat_field_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsStatField(
            component_id='NumberField-abcd',
            label='金额'
        )
        form_components_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsProps(
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
        form_components_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponents(
            component_type='TextField',
            props=form_components_0props,
            children=[
                form_components_0children_0
            ]
        )
        form_create_request = dingtalkworkflow__1__0_models.FormCreateRequest(
            name='出差报销审批',
            description='用于员工差旅费用报销使用',
            form_components=[
                form_components_0
            ]
        )
        try:
            client.form_create_with_options(form_create_request, form_create_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        form_create_headers = dingtalkworkflow__1__0_models.FormCreateHeaders()
        form_create_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_components_0children_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0children_0props_fields_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps(
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
        form_components_0children_0children_0props_fields_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsFields(
            props=form_components_0children_0children_0props_fields_0props
        )
        form_components_0children_0children_0props_data_source_target = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget()
        form_components_0children_0children_0props_data_source = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource(
            target=form_components_0children_0children_0props_data_source_target
        )
        form_components_0children_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsStatField()
        form_components_0children_0children_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0children_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildrenProps(
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
        form_components_0children_0children_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenChildren(
            props=form_components_0children_0children_0props
        )
        form_components_0children_0props_available_templates_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates(
            name='出差审批单',
            process_code='PROC-abcd'
        )
        form_components_0children_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0children_0props_fields_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsFieldsProps(
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
        form_components_0children_0props_fields_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsFields(
            props=form_components_0children_0props_fields_0props
        )
        form_components_0children_0props_data_source_target = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsDataSourceTarget()
        form_components_0children_0props_data_source = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsDataSource(
            target=form_components_0children_0props_data_source_target
        )
        form_components_0children_0props_stat_field_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsStatField()
        form_components_0children_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0children_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildrenProps(
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
        form_components_0children_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsChildren(
            component_type='NumberField',
            props=form_components_0children_0props,
            children=[
                form_components_0children_0children_0
            ]
        )
        form_components_0props_available_templates_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsAvailableTemplates(
            name='出差申请',
            process_code='PROC-abcd'
        )
        form_components_0props_fields_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsFieldsPropsOptions(
            key='finance',
            value='财务'
        )
        form_components_0props_fields_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsFieldsProps(
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
        form_components_0props_fields_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsFields(
            component_type='TextField',
            props=form_components_0props_fields_0props
        )
        form_components_0props_data_source_target = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsDataSourceTarget(
            app_uuid='SWAPP-abcd',
            app_type=0
        )
        form_components_0props_data_source = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsDataSource(
            type='form',
            target=form_components_0props_data_source_target
        )
        form_components_0props_stat_field_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsStatField(
            component_id='NumberField-abcd',
            label='金额'
        )
        form_components_0props_options_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsPropsOptions(
            value='选项1',
            key='option_1'
        )
        form_components_0props = dingtalkworkflow__1__0_models.FormCreateRequestFormComponentsProps(
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
        form_components_0 = dingtalkworkflow__1__0_models.FormCreateRequestFormComponents(
            component_type='TextField',
            props=form_components_0props,
            children=[
                form_components_0children_0
            ]
        )
        form_create_request = dingtalkworkflow__1__0_models.FormCreateRequest(
            name='出差报销审批',
            description='用于员工差旅费用报销使用',
            form_components=[
                form_components_0
            ]
        )
        try:
            await client.form_create_with_options_async(form_create_request, form_create_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\fields\props\options;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\fields\props;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\fields;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\dataSource\target;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\dataSource;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\statField;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\availableTemplates;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest;
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
        $formCreateHeaders = new FormCreateHeaders([]);
        $formCreateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $formComponents0Children0Children0PropsFields0PropsOptions0 = new options([
            "key" => "finance",
            "value" => "财务"
        ]);
        $formComponents0Children0Children0PropsFields0Props = new props([
            "componentId" => "TextField-1",
            "label" => "姓名",
            "required" => true,
            "print" => "1",
            "content" => "我是说明文字控件",
            "format" => "yyyy-MM-dd",
            "options" => [
                $formComponents0Children0Children0PropsFields0PropsOptions0
            ],
            "upper" => "1",
            "unit" => "天",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "bizType" => "attendance.leave",
            "duration" => true,
            "choice" => "0",
            "disabled" => true,
            "align" => "top"
        ]);
        $formComponents0Children0Children0PropsFields0 = new fields([
            "props" => $formComponents0Children0Children0PropsFields0Props
        ]);
        $formComponents0Children0Children0PropsDataSourceTarget = new target([]);
        $formComponents0Children0Children0PropsDataSource = new dataSource([
            "target" => $formComponents0Children0Children0PropsDataSourceTarget
        ]);
        $formComponents0Children0Children0PropsStatField0 = new statField([]);
        $formComponents0Children0Children0PropsOptions0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props\options([
            "value" => "选项1",
            "key" => "option_1"
        ]);
        $formComponents0Children0Children0Props = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\children\props([
            "label" => "姓名",
            "asyncCondition" => true,
            "required" => true,
            "content" => "我是说明文字控件",
            "format" => "yyyy-MM-dd",
            "upper" => "1",
            "unit" => "天",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "bizType" => "attendance.leave",
            "duration" => true,
            "choice" => "0",
            "disabled" => true,
            "align" => "top",
            "invisible" => true,
            "link" => "http://www.",
            "verticalPrint" => true,
            "commonBizType" => "custom_view",
            "options" => [
                $formComponents0Children0Children0PropsOptions0
            ],
            "statField" => [
                $formComponents0Children0Children0PropsStatField0
            ],
            "dataSource" => $formComponents0Children0Children0PropsDataSource,
            "fields" => [
                $formComponents0Children0Children0PropsFields0
            ]
        ]);
        $formComponents0Children0Children0 = new children([
            "props" => $formComponents0Children0Children0Props
        ]);
        $formComponents0Children0PropsAvailableTemplates0 = new availableTemplates([
            "name" => "出差审批单",
            "processCode" => "PROC-abcd"
        ]);
        $formComponents0Children0PropsFields0PropsOptions0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\fields\props\options([
            "key" => "finance",
            "value" => "财务"
        ]);
        $formComponents0Children0PropsFields0Props = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\fields\props([
            "componentId" => "TextField-1",
            "label" => "姓名",
            "labelEditableFreeze" => false,
            "required" => true,
            "requiredEditableFreeze" => true,
            "content" => "我是说明文字控件",
            "format" => "yyyy-MM-dd",
            "options" => [
                $formComponents0Children0PropsFields0PropsOptions0
            ],
            "notUpper" => "1",
            "unit" => "天",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "bizType" => "attendance.leave",
            "duration" => true,
            "choice" => "0",
            "disabled" => true,
            "align" => "top"
        ]);
        $formComponents0Children0PropsFields0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\fields([
            "props" => $formComponents0Children0PropsFields0Props
        ]);
        $formComponents0Children0PropsDataSourceTarget = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\dataSource\target([]);
        $formComponents0Children0PropsDataSource = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\dataSource([
            "target" => $formComponents0Children0PropsDataSourceTarget
        ]);
        $formComponents0Children0PropsStatField0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\statField([]);
        $formComponents0Children0PropsOptions0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props\options([
            "value" => "选项1",
            "key" => "option_1"
        ]);
        $formComponents0Children0Props = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children\props([
            "label" => "姓名",
            "asyncCondition" => true,
            "required" => true,
            "content" => "我是说明文字控件",
            "format" => "yyyy-MM-dd",
            "upper" => "1",
            "unit" => "天",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "bizType" => "attendance.leave",
            "duration" => true,
            "choice" => "0",
            "disabled" => true,
            "align" => "top",
            "invisible" => true,
            "link" => "http://www.",
            "verticalPrint" => true,
            "commonBizType" => "custom_view",
            "options" => [
                $formComponents0Children0PropsOptions0
            ],
            "print" => "1",
            "statField" => [
                $formComponents0Children0PropsStatField0
            ],
            "dataSource" => $formComponents0Children0PropsDataSource,
            "fields" => [
                $formComponents0Children0PropsFields0
            ],
            "addressModel" => "city",
            "limit" => 5,
            "availableTemplates" => [
                $formComponents0Children0PropsAvailableTemplates0
            ],
            "tableViewMode" => "table"
        ]);
        $formComponents0Children0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\children([
            "componentType" => "NumberField",
            "props" => $formComponents0Children0Props,
            "children" => [
                $formComponents0Children0Children0
            ]
        ]);
        $formComponents0PropsAvailableTemplates0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\availableTemplates([
            "name" => "出差申请",
            "processCode" => "PROC-abcd"
        ]);
        $formComponents0PropsFields0PropsOptions0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\fields\props\options([
            "key" => "finance",
            "value" => "财务"
        ]);
        $formComponents0PropsFields0Props = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\fields\props([
            "componentId" => "TextField-1",
            "label" => "姓名",
            "labelEditableFreeze" => false,
            "required" => true,
            "requiredEditableFreeze" => true,
            "print" => "1",
            "content" => "我是说明文字控件",
            "format" => "yyyy-MM-dd",
            "options" => [
                $formComponents0PropsFields0PropsOptions0
            ],
            "upper" => "1",
            "unit" => "天",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "bizType" => "attendance.leave",
            "duration" => true,
            "choice" => "0",
            "disabled" => true,
            "align" => "top"
        ]);
        $formComponents0PropsFields0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\fields([
            "componentType" => "TextField",
            "props" => $formComponents0PropsFields0Props
        ]);
        $formComponents0PropsDataSourceTarget = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\dataSource\target([
            "appUuid" => "SWAPP-abcd",
            "appType" => 0
        ]);
        $formComponents0PropsDataSource = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\dataSource([
            "type" => "form",
            "target" => $formComponents0PropsDataSourceTarget
        ]);
        $formComponents0PropsStatField0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\statField([
            "componentId" => "NumberField-abcd",
            "label" => "金额"
        ]);
        $formComponents0PropsOptions0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props\options([
            "value" => "选项1",
            "key" => "option_1"
        ]);
        $formComponents0Props = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\FormCreateRequest\formComponents\props([
            "componentId" => "TextField-abcd",
            "label" => "姓名",
            "asyncCondition" => true,
            "required" => true,
            "content" => "我是说明文字控件",
            "format" => "yyyy-MM-dd",
            "upper" => "1",
            "unit" => "天",
            "placeholder" => "请输入",
            "bizAlias" => "finance_name",
            "bizType" => "attendance.leave",
            "duration" => true,
            "choice" => "0",
            "disabled" => true,
            "align" => "top",
            "invisible" => true,
            "link" => "http://www.",
            "verticalPrint" => true,
            "commonBizType" => "custom_view",
            "options" => [
                $formComponents0PropsOptions0
            ],
            "print" => "1",
            "statField" => [
                $formComponents0PropsStatField0
            ],
            "dataSource" => $formComponents0PropsDataSource,
            "fields" => [
                $formComponents0PropsFields0
            ],
            "multiple" => true,
            "limit" => 5,
            "availableTemplates" => [
                $formComponents0PropsAvailableTemplates0
            ],
            "tableViewMode" => "table"
        ]);
        $formComponents0 = new formComponents([
            "componentType" => "TextField",
            "props" => $formComponents0Props,
            "children" => [
                $formComponents0Children0
            ]
        ]);
        $formCreateRequest = new FormCreateRequest([
            "name" => "出差报销审批",
            "description" => "用于员工差旅费用报销使用",
            "formComponents" => [
                $formComponents0
            ]
        ]);
        try {
            $client->formCreateWithOptions($formCreateRequest, $formCreateHeaders, new RuntimeOptions([]));
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

  formCreateHeaders := &dingtalkworkflow_1_0.FormCreateHeaders{}
  formCreateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  formComponents0Children0Children0PropsFields0PropsOptions0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions{
    Key: tea.String("finance"),
    Value: tea.String("财务"),
  }
  formComponents0Children0Children0PropsFields0Props := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps{
    ComponentId: tea.String("TextField-1"),
    Label: tea.String("姓名"),
    Required: tea.Bool(true),
    Print: tea.String("1"),
    Content: tea.String("我是说明文字控件"),
    Format: tea.String("yyyy-MM-dd"),
    Options: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions{formComponents0Children0Children0PropsFields0PropsOptions0},
    Upper: tea.String("1"),
    Unit: tea.String("天"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    BizType: tea.String("attendance.leave"),
    Duration: tea.Bool(true),
    Choice: tea.String("0"),
    Disabled: tea.Bool(true),
    Align: tea.String("top"),
  }
  formComponents0Children0Children0PropsFields0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFields{
    Props: formComponents0Children0Children0PropsFields0Props,
  }
  formComponents0Children0Children0PropsDataSourceTarget := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget{}
  formComponents0Children0Children0PropsDataSource := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource{
    Target: formComponents0Children0Children0PropsDataSourceTarget,
  }
  formComponents0Children0Children0PropsStatField0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsStatField{}
  formComponents0Children0Children0PropsOptions0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsOptions{
    Value: tea.String("选项1"),
    Key: tea.String("option_1"),
  }
  formComponents0Children0Children0Props := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenProps{
    Label: tea.String("姓名"),
    AsyncCondition: tea.Bool(true),
    Required: tea.Bool(true),
    Content: tea.String("我是说明文字控件"),
    Format: tea.String("yyyy-MM-dd"),
    Upper: tea.String("1"),
    Unit: tea.String("天"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    BizType: tea.String("attendance.leave"),
    Duration: tea.Bool(true),
    Choice: tea.String("0"),
    Disabled: tea.Bool(true),
    Align: tea.String("top"),
    Invisible: tea.Bool(true),
    Link: tea.String("http://www."),
    VerticalPrint: tea.Bool(true),
    CommonBizType: tea.String("custom_view"),
    Options: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsOptions{formComponents0Children0Children0PropsOptions0},
    StatField: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsStatField{formComponents0Children0Children0PropsStatField0},
    DataSource: formComponents0Children0Children0PropsDataSource,
    Fields: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFields{formComponents0Children0Children0PropsFields0},
  }
  formComponents0Children0Children0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildren{
    Props: formComponents0Children0Children0Props,
  }
  formComponents0Children0PropsAvailableTemplates0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates{
    Name: tea.String("出差审批单"),
    ProcessCode: tea.String("PROC-abcd"),
  }
  formComponents0Children0PropsFields0PropsOptions0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions{
    Key: tea.String("finance"),
    Value: tea.String("财务"),
  }
  formComponents0Children0PropsFields0Props := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFieldsProps{
    ComponentId: tea.String("TextField-1"),
    Label: tea.String("姓名"),
    LabelEditableFreeze: tea.Bool(false),
    Required: tea.Bool(true),
    RequiredEditableFreeze: tea.Bool(true),
    Content: tea.String("我是说明文字控件"),
    Format: tea.String("yyyy-MM-dd"),
    Options: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions{formComponents0Children0PropsFields0PropsOptions0},
    NotUpper: tea.String("1"),
    Unit: tea.String("天"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    BizType: tea.String("attendance.leave"),
    Duration: tea.Bool(true),
    Choice: tea.String("0"),
    Disabled: tea.Bool(true),
    Align: tea.String("top"),
  }
  formComponents0Children0PropsFields0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFields{
    Props: formComponents0Children0PropsFields0Props,
  }
  formComponents0Children0PropsDataSourceTarget := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsDataSourceTarget{}
  formComponents0Children0PropsDataSource := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsDataSource{
    Target: formComponents0Children0PropsDataSourceTarget,
  }
  formComponents0Children0PropsStatField0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsStatField{}
  formComponents0Children0PropsOptions0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsOptions{
    Value: tea.String("选项1"),
    Key: tea.String("option_1"),
  }
  formComponents0Children0Props := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenProps{
    Label: tea.String("姓名"),
    AsyncCondition: tea.Bool(true),
    Required: tea.Bool(true),
    Content: tea.String("我是说明文字控件"),
    Format: tea.String("yyyy-MM-dd"),
    Upper: tea.String("1"),
    Unit: tea.String("天"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    BizType: tea.String("attendance.leave"),
    Duration: tea.Bool(true),
    Choice: tea.String("0"),
    Disabled: tea.Bool(true),
    Align: tea.String("top"),
    Invisible: tea.Bool(true),
    Link: tea.String("http://www."),
    VerticalPrint: tea.Bool(true),
    CommonBizType: tea.String("custom_view"),
    Options: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsOptions{formComponents0Children0PropsOptions0},
    Print: tea.String("1"),
    StatField: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsStatField{formComponents0Children0PropsStatField0},
    DataSource: formComponents0Children0PropsDataSource,
    Fields: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFields{formComponents0Children0PropsFields0},
    AddressModel: tea.String("city"),
    Limit: tea.Int32(5),
    AvailableTemplates: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates{formComponents0Children0PropsAvailableTemplates0},
    TableViewMode: tea.String("table"),
  }
  formComponents0Children0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildren{
    ComponentType: tea.String("NumberField"),
    Props: formComponents0Children0Props,
    Children: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildren{formComponents0Children0Children0},
  }
  formComponents0PropsAvailableTemplates0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsAvailableTemplates{
    Name: tea.String("出差申请"),
    ProcessCode: tea.String("PROC-abcd"),
  }
  formComponents0PropsFields0PropsOptions0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFieldsPropsOptions{
    Key: tea.String("finance"),
    Value: tea.String("财务"),
  }
  formComponents0PropsFields0Props := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFieldsProps{
    ComponentId: tea.String("TextField-1"),
    Label: tea.String("姓名"),
    LabelEditableFreeze: tea.Bool(false),
    Required: tea.Bool(true),
    RequiredEditableFreeze: tea.Bool(true),
    Print: tea.String("1"),
    Content: tea.String("我是说明文字控件"),
    Format: tea.String("yyyy-MM-dd"),
    Options: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFieldsPropsOptions{formComponents0PropsFields0PropsOptions0},
    Upper: tea.String("1"),
    Unit: tea.String("天"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    BizType: tea.String("attendance.leave"),
    Duration: tea.Bool(true),
    Choice: tea.String("0"),
    Disabled: tea.Bool(true),
    Align: tea.String("top"),
  }
  formComponents0PropsFields0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFields{
    ComponentType: tea.String("TextField"),
    Props: formComponents0PropsFields0Props,
  }
  formComponents0PropsDataSourceTarget := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsDataSourceTarget{
    AppUuid: tea.String("SWAPP-abcd"),
    AppType: tea.Int32(0),
  }
  formComponents0PropsDataSource := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsDataSource{
    Type: tea.String("form"),
    Target: formComponents0PropsDataSourceTarget,
  }
  formComponents0PropsStatField0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsStatField{
    ComponentId: tea.String("NumberField-abcd"),
    Label: tea.String("金额"),
  }
  formComponents0PropsOptions0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsOptions{
    Value: tea.String("选项1"),
    Key: tea.String("option_1"),
  }
  formComponents0Props := &dingtalkworkflow_1_0.FormCreateRequestFormComponentsProps{
    ComponentId: tea.String("TextField-abcd"),
    Label: tea.String("姓名"),
    AsyncCondition: tea.Bool(true),
    Required: tea.Bool(true),
    Content: tea.String("我是说明文字控件"),
    Format: tea.String("yyyy-MM-dd"),
    Upper: tea.String("1"),
    Unit: tea.String("天"),
    Placeholder: tea.String("请输入"),
    BizAlias: tea.String("finance_name"),
    BizType: tea.String("attendance.leave"),
    Duration: tea.Bool(true),
    Choice: tea.String("0"),
    Disabled: tea.Bool(true),
    Align: tea.String("top"),
    Invisible: tea.Bool(true),
    Link: tea.String("http://www."),
    VerticalPrint: tea.Bool(true),
    CommonBizType: tea.String("custom_view"),
    Options: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsOptions{formComponents0PropsOptions0},
    Print: tea.String("1"),
    StatField: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsStatField{formComponents0PropsStatField0},
    DataSource: formComponents0PropsDataSource,
    Fields: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFields{formComponents0PropsFields0},
    Multiple: tea.Bool(true),
    Limit: tea.Int32(5),
    AvailableTemplates: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsAvailableTemplates{formComponents0PropsAvailableTemplates0},
    TableViewMode: tea.String("table"),
  }
  formComponents0 := &dingtalkworkflow_1_0.FormCreateRequestFormComponents{
    ComponentType: tea.String("TextField"),
    Props: formComponents0Props,
    Children: []*dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildren{formComponents0Children0},
  }
  formCreateRequest := &dingtalkworkflow_1_0.FormCreateRequest{
    Name: tea.String("出差报销审批"),
    Description: tea.String("用于员工差旅费用报销使用"),
    FormComponents: []*dingtalkworkflow_1_0.FormCreateRequestFormComponents{formComponents0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.FormCreateWithOptions(formCreateRequest, formCreateHeaders, &util.RuntimeOptions{})
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
    let formCreateHeaders = new $dingtalkworkflow_1_0.FormCreateHeaders({ });
    formCreateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let formComponents0Children0Children0PropsFields0PropsOptions0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions({
      key: "finance",
      value: "财务",
    });
    let formComponents0Children0Children0PropsFields0Props = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps({
      componentId: "TextField-1",
      label: "姓名",
      required: true,
      print: "1",
      content: "我是说明文字控件",
      format: "yyyy-MM-dd",
      options: [
        formComponents0Children0Children0PropsFields0PropsOptions0
      ],
      upper: "1",
      unit: "天",
      placeholder: "请输入",
      bizAlias: "finance_name",
      bizType: "attendance.leave",
      duration: true,
      choice: "0",
      disabled: true,
      align: "top",
    });
    let formComponents0Children0Children0PropsFields0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsFields({
      props: formComponents0Children0Children0PropsFields0Props,
    });
    let formComponents0Children0Children0PropsDataSourceTarget = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget({ });
    let formComponents0Children0Children0PropsDataSource = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource({
      target: formComponents0Children0Children0PropsDataSourceTarget,
    });
    let formComponents0Children0Children0PropsStatField0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsStatField({ });
    let formComponents0Children0Children0PropsOptions0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenPropsOptions({
      value: "选项1",
      key: "option_1",
    });
    let formComponents0Children0Children0Props = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildrenProps({
      label: "姓名",
      asyncCondition: true,
      required: true,
      content: "我是说明文字控件",
      format: "yyyy-MM-dd",
      upper: "1",
      unit: "天",
      placeholder: "请输入",
      bizAlias: "finance_name",
      bizType: "attendance.leave",
      duration: true,
      choice: "0",
      disabled: true,
      align: "top",
      invisible: true,
      link: "http://www.",
      verticalPrint: true,
      commonBizType: "custom_view",
      options: [
        formComponents0Children0Children0PropsOptions0
      ],
      statField: [
        formComponents0Children0Children0PropsStatField0
      ],
      dataSource: formComponents0Children0Children0PropsDataSource,
      fields: [
        formComponents0Children0Children0PropsFields0
      ],
    });
    let formComponents0Children0Children0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenChildren({
      props: formComponents0Children0Children0Props,
    });
    let formComponents0Children0PropsAvailableTemplates0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates({
      name: "出差审批单",
      processCode: "PROC-abcd",
    });
    let formComponents0Children0PropsFields0PropsOptions0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions({
      key: "finance",
      value: "财务",
    });
    let formComponents0Children0PropsFields0Props = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFieldsProps({
      componentId: "TextField-1",
      label: "姓名",
      labelEditableFreeze: false,
      required: true,
      requiredEditableFreeze: true,
      content: "我是说明文字控件",
      format: "yyyy-MM-dd",
      options: [
        formComponents0Children0PropsFields0PropsOptions0
      ],
      notUpper: "1",
      unit: "天",
      placeholder: "请输入",
      bizAlias: "finance_name",
      bizType: "attendance.leave",
      duration: true,
      choice: "0",
      disabled: true,
      align: "top",
    });
    let formComponents0Children0PropsFields0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsFields({
      props: formComponents0Children0PropsFields0Props,
    });
    let formComponents0Children0PropsDataSourceTarget = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsDataSourceTarget({ });
    let formComponents0Children0PropsDataSource = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsDataSource({
      target: formComponents0Children0PropsDataSourceTarget,
    });
    let formComponents0Children0PropsStatField0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsStatField({ });
    let formComponents0Children0PropsOptions0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenPropsOptions({
      value: "选项1",
      key: "option_1",
    });
    let formComponents0Children0Props = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildrenProps({
      label: "姓名",
      asyncCondition: true,
      required: true,
      content: "我是说明文字控件",
      format: "yyyy-MM-dd",
      upper: "1",
      unit: "天",
      placeholder: "请输入",
      bizAlias: "finance_name",
      bizType: "attendance.leave",
      duration: true,
      choice: "0",
      disabled: true,
      align: "top",
      invisible: true,
      link: "http://www.",
      verticalPrint: true,
      commonBizType: "custom_view",
      options: [
        formComponents0Children0PropsOptions0
      ],
      print: "1",
      statField: [
        formComponents0Children0PropsStatField0
      ],
      dataSource: formComponents0Children0PropsDataSource,
      fields: [
        formComponents0Children0PropsFields0
      ],
      addressModel: "city",
      limit: 5,
      availableTemplates: [
        formComponents0Children0PropsAvailableTemplates0
      ],
      tableViewMode: "table",
    });
    let formComponents0Children0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsChildren({
      componentType: "NumberField",
      props: formComponents0Children0Props,
      children: [
        formComponents0Children0Children0
      ],
    });
    let formComponents0PropsAvailableTemplates0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsAvailableTemplates({
      name: "出差申请",
      processCode: "PROC-abcd",
    });
    let formComponents0PropsFields0PropsOptions0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFieldsPropsOptions({
      key: "finance",
      value: "财务",
    });
    let formComponents0PropsFields0Props = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFieldsProps({
      componentId: "TextField-1",
      label: "姓名",
      labelEditableFreeze: false,
      required: true,
      requiredEditableFreeze: true,
      print: "1",
      content: "我是说明文字控件",
      format: "yyyy-MM-dd",
      options: [
        formComponents0PropsFields0PropsOptions0
      ],
      upper: "1",
      unit: "天",
      placeholder: "请输入",
      bizAlias: "finance_name",
      bizType: "attendance.leave",
      duration: true,
      choice: "0",
      disabled: true,
      align: "top",
    });
    let formComponents0PropsFields0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsFields({
      componentType: "TextField",
      props: formComponents0PropsFields0Props,
    });
    let formComponents0PropsDataSourceTarget = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsDataSourceTarget({
      appUuid: "SWAPP-abcd",
      appType: 0,
    });
    let formComponents0PropsDataSource = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsDataSource({
      type: "form",
      target: formComponents0PropsDataSourceTarget,
    });
    let formComponents0PropsStatField0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsStatField({
      componentId: "NumberField-abcd",
      label: "金额",
    });
    let formComponents0PropsOptions0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsPropsOptions({
      value: "选项1",
      key: "option_1",
    });
    let formComponents0Props = new $dingtalkworkflow_1_0.FormCreateRequestFormComponentsProps({
      componentId: "TextField-abcd",
      label: "姓名",
      asyncCondition: true,
      required: true,
      content: "我是说明文字控件",
      format: "yyyy-MM-dd",
      upper: "1",
      unit: "天",
      placeholder: "请输入",
      bizAlias: "finance_name",
      bizType: "attendance.leave",
      duration: true,
      choice: "0",
      disabled: true,
      align: "top",
      invisible: true,
      link: "http://www.",
      verticalPrint: true,
      commonBizType: "custom_view",
      options: [
        formComponents0PropsOptions0
      ],
      print: "1",
      statField: [
        formComponents0PropsStatField0
      ],
      dataSource: formComponents0PropsDataSource,
      fields: [
        formComponents0PropsFields0
      ],
      multiple: true,
      limit: 5,
      availableTemplates: [
        formComponents0PropsAvailableTemplates0
      ],
      tableViewMode: "table",
    });
    let formComponents0 = new $dingtalkworkflow_1_0.FormCreateRequestFormComponents({
      componentType: "TextField",
      props: formComponents0Props,
      children: [
        formComponents0Children0
      ],
    });
    let formCreateRequest = new $dingtalkworkflow_1_0.FormCreateRequest({
      name: "出差报销审批",
      description: "用于员工差旅费用报销使用",
      formComponents: [
        formComponents0
      ],
    });
    try {
      await client.formCreateWithOptions(formCreateRequest, formCreateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateHeaders formCreateHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateHeaders();
            formCreateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions formComponents0Children0Children0PropsFields0PropsOptions0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions
            {
                Key = "finance",
                Value = "财务",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps formComponents0Children0Children0PropsFields0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps
            {
                ComponentId = "TextField-1",
                Label = "姓名",
                Required = true,
                Print = "1",
                Content = "我是说明文字控件",
                Format = "yyyy-MM-dd",
                Options = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps.FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions>
                {
                    formComponents0Children0Children0PropsFields0PropsOptions0
                },
                Upper = "1",
                Unit = "天",
                Placeholder = "请输入",
                BizAlias = "finance_name",
                BizType = "attendance.leave",
                Duration = true,
                Choice = "0",
                Disabled = true,
                Align = "top",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields formComponents0Children0Children0PropsFields0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields
            {
                Props = formComponents0Children0Children0PropsFields0Props,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource.FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget formComponents0Children0Children0PropsDataSourceTarget = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource.FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource formComponents0Children0Children0PropsDataSource = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsDataSource
            {
                Target = formComponents0Children0Children0PropsDataSourceTarget,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsStatField formComponents0Children0Children0PropsStatField0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsStatField();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsOptions formComponents0Children0Children0PropsOptions0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsOptions
            {
                Value = "选项1",
                Key = "option_1",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps formComponents0Children0Children0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps
            {
                Label = "姓名",
                AsyncCondition = true,
                Required = true,
                Content = "我是说明文字控件",
                Format = "yyyy-MM-dd",
                Upper = "1",
                Unit = "天",
                Placeholder = "请输入",
                BizAlias = "finance_name",
                BizType = "attendance.leave",
                Duration = true,
                Choice = "0",
                Disabled = true,
                Align = "top",
                Invisible = true,
                Link = "http://www.",
                VerticalPrint = true,
                CommonBizType = "custom_view",
                Options = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsOptions>
                {
                    formComponents0Children0Children0PropsOptions0
                },
                StatField = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsStatField>
                {
                    formComponents0Children0Children0PropsStatField0
                },
                DataSource = formComponents0Children0Children0PropsDataSource,
                Fields = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren.FormCreateRequestFormComponentsChildrenChildrenProps.FormCreateRequestFormComponentsChildrenChildrenPropsFields>
                {
                    formComponents0Children0Children0PropsFields0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren formComponents0Children0Children0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren
            {
                Props = formComponents0Children0Children0Props,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates formComponents0Children0PropsAvailableTemplates0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates
            {
                Name = "出差审批单",
                ProcessCode = "PROC-abcd",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields.FormCreateRequestFormComponentsChildrenPropsFieldsProps.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions formComponents0Children0PropsFields0PropsOptions0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields.FormCreateRequestFormComponentsChildrenPropsFieldsProps.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions
            {
                Key = "finance",
                Value = "财务",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields.FormCreateRequestFormComponentsChildrenPropsFieldsProps formComponents0Children0PropsFields0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields.FormCreateRequestFormComponentsChildrenPropsFieldsProps
            {
                ComponentId = "TextField-1",
                Label = "姓名",
                LabelEditableFreeze = false,
                Required = true,
                RequiredEditableFreeze = true,
                Content = "我是说明文字控件",
                Format = "yyyy-MM-dd",
                Options = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields.FormCreateRequestFormComponentsChildrenPropsFieldsProps.FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions>
                {
                    formComponents0Children0PropsFields0PropsOptions0
                },
                NotUpper = "1",
                Unit = "天",
                Placeholder = "请输入",
                BizAlias = "finance_name",
                BizType = "attendance.leave",
                Duration = true,
                Choice = "0",
                Disabled = true,
                Align = "top",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields formComponents0Children0PropsFields0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields
            {
                Props = formComponents0Children0PropsFields0Props,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsDataSource.FormCreateRequestFormComponentsChildrenPropsDataSourceTarget formComponents0Children0PropsDataSourceTarget = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsDataSource.FormCreateRequestFormComponentsChildrenPropsDataSourceTarget();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsDataSource formComponents0Children0PropsDataSource = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsDataSource
            {
                Target = formComponents0Children0PropsDataSourceTarget,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsStatField formComponents0Children0PropsStatField0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsStatField();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsOptions formComponents0Children0PropsOptions0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsOptions
            {
                Value = "选项1",
                Key = "option_1",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps formComponents0Children0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps
            {
                Label = "姓名",
                AsyncCondition = true,
                Required = true,
                Content = "我是说明文字控件",
                Format = "yyyy-MM-dd",
                Upper = "1",
                Unit = "天",
                Placeholder = "请输入",
                BizAlias = "finance_name",
                BizType = "attendance.leave",
                Duration = true,
                Choice = "0",
                Disabled = true,
                Align = "top",
                Invisible = true,
                Link = "http://www.",
                VerticalPrint = true,
                CommonBizType = "custom_view",
                Options = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsOptions>
                {
                    formComponents0Children0PropsOptions0
                },
                Print = "1",
                StatField = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsStatField>
                {
                    formComponents0Children0PropsStatField0
                },
                DataSource = formComponents0Children0PropsDataSource,
                Fields = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsFields>
                {
                    formComponents0Children0PropsFields0
                },
                AddressModel = "city",
                Limit = 5,
                AvailableTemplates = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenProps.FormCreateRequestFormComponentsChildrenPropsAvailableTemplates>
                {
                    formComponents0Children0PropsAvailableTemplates0
                },
                TableViewMode = "table",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren formComponents0Children0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren
            {
                ComponentType = "NumberField",
                Props = formComponents0Children0Props,
                Children = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren.FormCreateRequestFormComponentsChildrenChildren>
                {
                    formComponents0Children0Children0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsAvailableTemplates formComponents0PropsAvailableTemplates0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsAvailableTemplates
            {
                Name = "出差申请",
                ProcessCode = "PROC-abcd",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields.FormCreateRequestFormComponentsPropsFieldsProps.FormCreateRequestFormComponentsPropsFieldsPropsOptions formComponents0PropsFields0PropsOptions0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields.FormCreateRequestFormComponentsPropsFieldsProps.FormCreateRequestFormComponentsPropsFieldsPropsOptions
            {
                Key = "finance",
                Value = "财务",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields.FormCreateRequestFormComponentsPropsFieldsProps formComponents0PropsFields0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields.FormCreateRequestFormComponentsPropsFieldsProps
            {
                ComponentId = "TextField-1",
                Label = "姓名",
                LabelEditableFreeze = false,
                Required = true,
                RequiredEditableFreeze = true,
                Print = "1",
                Content = "我是说明文字控件",
                Format = "yyyy-MM-dd",
                Options = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields.FormCreateRequestFormComponentsPropsFieldsProps.FormCreateRequestFormComponentsPropsFieldsPropsOptions>
                {
                    formComponents0PropsFields0PropsOptions0
                },
                Upper = "1",
                Unit = "天",
                Placeholder = "请输入",
                BizAlias = "finance_name",
                BizType = "attendance.leave",
                Duration = true,
                Choice = "0",
                Disabled = true,
                Align = "top",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields formComponents0PropsFields0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields
            {
                ComponentType = "TextField",
                Props = formComponents0PropsFields0Props,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsDataSource.FormCreateRequestFormComponentsPropsDataSourceTarget formComponents0PropsDataSourceTarget = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsDataSource.FormCreateRequestFormComponentsPropsDataSourceTarget
            {
                AppUuid = "SWAPP-abcd",
                AppType = 0,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsDataSource formComponents0PropsDataSource = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsDataSource
            {
                Type = "form",
                Target = formComponents0PropsDataSourceTarget,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsStatField formComponents0PropsStatField0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsStatField
            {
                ComponentId = "NumberField-abcd",
                Label = "金额",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsOptions formComponents0PropsOptions0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsOptions
            {
                Value = "选项1",
                Key = "option_1",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps formComponents0Props = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps
            {
                ComponentId = "TextField-abcd",
                Label = "姓名",
                AsyncCondition = true,
                Required = true,
                Content = "我是说明文字控件",
                Format = "yyyy-MM-dd",
                Upper = "1",
                Unit = "天",
                Placeholder = "请输入",
                BizAlias = "finance_name",
                BizType = "attendance.leave",
                Duration = true,
                Choice = "0",
                Disabled = true,
                Align = "top",
                Invisible = true,
                Link = "http://www.",
                VerticalPrint = true,
                CommonBizType = "custom_view",
                Options = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsOptions>
                {
                    formComponents0PropsOptions0
                },
                Print = "1",
                StatField = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsStatField>
                {
                    formComponents0PropsStatField0
                },
                DataSource = formComponents0PropsDataSource,
                Fields = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsFields>
                {
                    formComponents0PropsFields0
                },
                Multiple = true,
                Limit = 5,
                AvailableTemplates = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsProps.FormCreateRequestFormComponentsPropsAvailableTemplates>
                {
                    formComponents0PropsAvailableTemplates0
                },
                TableViewMode = "table",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents formComponents0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents
            {
                ComponentType = "TextField",
                Props = formComponents0Props,
                Children = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents.FormCreateRequestFormComponentsChildren>
                {
                    formComponents0Children0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest formCreateRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest
            {
                Name = "出差报销审批",
                Description = "用于员工差旅费用报销使用",
                FormComponents = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.FormCreateRequest.FormCreateRequestFormComponents>
                {
                    formComponents0
                },
            };
            try
            {
                client.FormCreateWithOptions(formCreateRequest, formCreateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateHeaders> formCreateHeaders = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateHeaders>();
  formCreateHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions> formComponents0Children0Children0PropsFields0PropsOptions0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions>(map<string, boost::any>({
    {"key", boost::any(string("finance"))},
    {"value", boost::any(string("财务"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps> formComponents0Children0Children0PropsFields0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFieldsProps>(map<string, boost::any>({
    {"componentId", boost::any(string("TextField-1"))},
    {"label", boost::any(string("姓名"))},
    {"required", boost::any(true)},
    {"print", boost::any(string("1"))},
    {"content", boost::any(string("我是说明文字控件"))},
    {"format", boost::any(string("yyyy-MM-dd"))},
    {"options", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFieldsPropsOptions>({
      formComponents0Children0Children0PropsFields0PropsOptions0
    }))},
    {"upper", boost::any(string("1"))},
    {"unit", boost::any(string("天"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
    {"bizType", boost::any(string("attendance.leave"))},
    {"duration", boost::any(true)},
    {"choice", boost::any(string("0"))},
    {"disabled", boost::any(true)},
    {"align", boost::any(string("top"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFields> formComponents0Children0Children0PropsFields0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFields>(map<string, boost::any>({
    {"props", !formComponents0Children0Children0PropsFields0Props ? boost::any() : boost::any(*formComponents0Children0Children0PropsFields0Props)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget> formComponents0Children0Children0PropsDataSourceTarget = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsDataSourceTarget>();
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsDataSource> formComponents0Children0Children0PropsDataSource = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsDataSource>(map<string, boost::any>({
    {"target", !formComponents0Children0Children0PropsDataSourceTarget ? boost::any() : boost::any(*formComponents0Children0Children0PropsDataSourceTarget)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsStatField> formComponents0Children0Children0PropsStatField0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsStatField>();
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsOptions> formComponents0Children0Children0PropsOptions0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsOptions>(map<string, boost::any>({
    {"value", boost::any(string("选项1"))},
    {"key", boost::any(string("option_1"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenProps> formComponents0Children0Children0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenProps>(map<string, boost::any>({
    {"label", boost::any(string("姓名"))},
    {"asyncCondition", boost::any(true)},
    {"required", boost::any(true)},
    {"content", boost::any(string("我是说明文字控件"))},
    {"format", boost::any(string("yyyy-MM-dd"))},
    {"upper", boost::any(string("1"))},
    {"unit", boost::any(string("天"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
    {"bizType", boost::any(string("attendance.leave"))},
    {"duration", boost::any(true)},
    {"choice", boost::any(string("0"))},
    {"disabled", boost::any(true)},
    {"align", boost::any(string("top"))},
    {"invisible", boost::any(true)},
    {"link", boost::any(string("http://www."))},
    {"verticalPrint", boost::any(true)},
    {"commonBizType", boost::any(string("custom_view"))},
    {"options", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsOptions>({
      formComponents0Children0Children0PropsOptions0
    }))},
    {"statField", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsStatField>({
      formComponents0Children0Children0PropsStatField0
    }))},
    {"dataSource", !formComponents0Children0Children0PropsDataSource ? boost::any() : boost::any(*formComponents0Children0Children0PropsDataSource)},
    {"fields", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildrenPropsFields>({
      formComponents0Children0Children0PropsFields0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildren> formComponents0Children0Children0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildren>(map<string, boost::any>({
    {"props", !formComponents0Children0Children0Props ? boost::any() : boost::any(*formComponents0Children0Children0Props)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsAvailableTemplates> formComponents0Children0PropsAvailableTemplates0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsAvailableTemplates>(map<string, boost::any>({
    {"name", boost::any(string("出差审批单"))},
    {"processCode", boost::any(string("PROC-abcd"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions> formComponents0Children0PropsFields0PropsOptions0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions>(map<string, boost::any>({
    {"key", boost::any(string("finance"))},
    {"value", boost::any(string("财务"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFieldsProps> formComponents0Children0PropsFields0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFieldsProps>(map<string, boost::any>({
    {"componentId", boost::any(string("TextField-1"))},
    {"label", boost::any(string("姓名"))},
    {"labelEditableFreeze", boost::any(false)},
    {"required", boost::any(true)},
    {"requiredEditableFreeze", boost::any(true)},
    {"content", boost::any(string("我是说明文字控件"))},
    {"format", boost::any(string("yyyy-MM-dd"))},
    {"options", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFieldsPropsOptions>({
      formComponents0Children0PropsFields0PropsOptions0
    }))},
    {"notUpper", boost::any(string("1"))},
    {"unit", boost::any(string("天"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
    {"bizType", boost::any(string("attendance.leave"))},
    {"duration", boost::any(true)},
    {"choice", boost::any(string("0"))},
    {"disabled", boost::any(true)},
    {"align", boost::any(string("top"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFields> formComponents0Children0PropsFields0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFields>(map<string, boost::any>({
    {"props", !formComponents0Children0PropsFields0Props ? boost::any() : boost::any(*formComponents0Children0PropsFields0Props)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsDataSourceTarget> formComponents0Children0PropsDataSourceTarget = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsDataSourceTarget>();
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsDataSource> formComponents0Children0PropsDataSource = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsDataSource>(map<string, boost::any>({
    {"target", !formComponents0Children0PropsDataSourceTarget ? boost::any() : boost::any(*formComponents0Children0PropsDataSourceTarget)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsStatField> formComponents0Children0PropsStatField0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsStatField>();
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsOptions> formComponents0Children0PropsOptions0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsOptions>(map<string, boost::any>({
    {"value", boost::any(string("选项1"))},
    {"key", boost::any(string("option_1"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenProps> formComponents0Children0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenProps>(map<string, boost::any>({
    {"label", boost::any(string("姓名"))},
    {"asyncCondition", boost::any(true)},
    {"required", boost::any(true)},
    {"content", boost::any(string("我是说明文字控件"))},
    {"format", boost::any(string("yyyy-MM-dd"))},
    {"upper", boost::any(string("1"))},
    {"unit", boost::any(string("天"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
    {"bizType", boost::any(string("attendance.leave"))},
    {"duration", boost::any(true)},
    {"choice", boost::any(string("0"))},
    {"disabled", boost::any(true)},
    {"align", boost::any(string("top"))},
    {"invisible", boost::any(true)},
    {"link", boost::any(string("http://www."))},
    {"verticalPrint", boost::any(true)},
    {"commonBizType", boost::any(string("custom_view"))},
    {"options", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsOptions>({
      formComponents0Children0PropsOptions0
    }))},
    {"print", boost::any(string("1"))},
    {"statField", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsStatField>({
      formComponents0Children0PropsStatField0
    }))},
    {"dataSource", !formComponents0Children0PropsDataSource ? boost::any() : boost::any(*formComponents0Children0PropsDataSource)},
    {"fields", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsFields>({
      formComponents0Children0PropsFields0
    }))},
    {"addressModel", boost::any(string("city"))},
    {"limit", boost::any(5)},
    {"availableTemplates", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenPropsAvailableTemplates>({
      formComponents0Children0PropsAvailableTemplates0
    }))},
    {"tableViewMode", boost::any(string("table"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildren> formComponents0Children0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildren>(map<string, boost::any>({
    {"componentType", boost::any(string("NumberField"))},
    {"props", !formComponents0Children0Props ? boost::any() : boost::any(*formComponents0Children0Props)},
    {"children", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildrenChildren>({
      formComponents0Children0Children0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsAvailableTemplates> formComponents0PropsAvailableTemplates0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsAvailableTemplates>(map<string, boost::any>({
    {"name", boost::any(string("出差申请"))},
    {"processCode", boost::any(string("PROC-abcd"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFieldsPropsOptions> formComponents0PropsFields0PropsOptions0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFieldsPropsOptions>(map<string, boost::any>({
    {"key", boost::any(string("finance"))},
    {"value", boost::any(string("财务"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFieldsProps> formComponents0PropsFields0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFieldsProps>(map<string, boost::any>({
    {"componentId", boost::any(string("TextField-1"))},
    {"label", boost::any(string("姓名"))},
    {"labelEditableFreeze", boost::any(false)},
    {"required", boost::any(true)},
    {"requiredEditableFreeze", boost::any(true)},
    {"print", boost::any(string("1"))},
    {"content", boost::any(string("我是说明文字控件"))},
    {"format", boost::any(string("yyyy-MM-dd"))},
    {"options", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFieldsPropsOptions>({
      formComponents0PropsFields0PropsOptions0
    }))},
    {"upper", boost::any(string("1"))},
    {"unit", boost::any(string("天"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
    {"bizType", boost::any(string("attendance.leave"))},
    {"duration", boost::any(true)},
    {"choice", boost::any(string("0"))},
    {"disabled", boost::any(true)},
    {"align", boost::any(string("top"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFields> formComponents0PropsFields0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFields>(map<string, boost::any>({
    {"componentType", boost::any(string("TextField"))},
    {"props", !formComponents0PropsFields0Props ? boost::any() : boost::any(*formComponents0PropsFields0Props)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsDataSourceTarget> formComponents0PropsDataSourceTarget = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsDataSourceTarget>(map<string, boost::any>({
    {"appUuid", boost::any(string("SWAPP-abcd"))},
    {"appType", boost::any(0)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsDataSource> formComponents0PropsDataSource = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsDataSource>(map<string, boost::any>({
    {"type", boost::any(string("form"))},
    {"target", !formComponents0PropsDataSourceTarget ? boost::any() : boost::any(*formComponents0PropsDataSourceTarget)}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsStatField> formComponents0PropsStatField0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsStatField>(map<string, boost::any>({
    {"componentId", boost::any(string("NumberField-abcd"))},
    {"label", boost::any(string("金额"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsOptions> formComponents0PropsOptions0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsOptions>(map<string, boost::any>({
    {"value", boost::any(string("选项1"))},
    {"key", boost::any(string("option_1"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsProps> formComponents0Props = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsProps>(map<string, boost::any>({
    {"componentId", boost::any(string("TextField-abcd"))},
    {"label", boost::any(string("姓名"))},
    {"asyncCondition", boost::any(true)},
    {"required", boost::any(true)},
    {"content", boost::any(string("我是说明文字控件"))},
    {"format", boost::any(string("yyyy-MM-dd"))},
    {"upper", boost::any(string("1"))},
    {"unit", boost::any(string("天"))},
    {"placeholder", boost::any(string("请输入"))},
    {"bizAlias", boost::any(string("finance_name"))},
    {"bizType", boost::any(string("attendance.leave"))},
    {"duration", boost::any(true)},
    {"choice", boost::any(string("0"))},
    {"disabled", boost::any(true)},
    {"align", boost::any(string("top"))},
    {"invisible", boost::any(true)},
    {"link", boost::any(string("http://www."))},
    {"verticalPrint", boost::any(true)},
    {"commonBizType", boost::any(string("custom_view"))},
    {"options", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsOptions>({
      formComponents0PropsOptions0
    }))},
    {"print", boost::any(string("1"))},
    {"statField", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsStatField>({
      formComponents0PropsStatField0
    }))},
    {"dataSource", !formComponents0PropsDataSource ? boost::any() : boost::any(*formComponents0PropsDataSource)},
    {"fields", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsFields>({
      formComponents0PropsFields0
    }))},
    {"multiple", boost::any(true)},
    {"limit", boost::any(5)},
    {"availableTemplates", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsPropsAvailableTemplates>({
      formComponents0PropsAvailableTemplates0
    }))},
    {"tableViewMode", boost::any(string("table"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponents> formComponents0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponents>(map<string, boost::any>({
    {"componentType", boost::any(string("TextField"))},
    {"props", !formComponents0Props ? boost::any() : boost::any(*formComponents0Props)},
    {"children", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponentsChildren>({
      formComponents0Children0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequest> formCreateRequest = make_shared<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequest>(map<string, boost::any>({
    {"name", boost::any(string("出差报销审批"))},
    {"description", boost::any(string("用于员工差旅费用报销使用"))},
    {"formComponents", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::FormCreateRequestFormComponents>({
      formComponents0
    }))}
  }));
  try {
    client->formCreateWithOptions(formCreateRequest, formCreateHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Object | 返回的表单模板信息。 |
| processCode | String | 表单模板Code，企业内唯一 。      生成企业内唯一的审批模板编码，可使用此**processCode**发起表单实例。 |

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
| 400 | permission.error | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | processcode.error | processCode对应的审批流程不存在 | processCode对应的审批流程不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | schema.sysAttrs.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 500 | system.error | 系统内部异常 | 系统内部异常 |
