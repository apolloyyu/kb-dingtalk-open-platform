---
title: "创建实例"
source_url: "https://open.dingtalk.com/document/development/create-a-ticket-approval-instance"
namespace: "development"
slug: "create-a-ticket-approval-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 审批实例 > 创建实例"
doc_id: "pMujhtQZs9"
updated_at: "2026-06-03 10:12:38"
---

> Source: https://open.dingtalk.com/document/development/create-a-ticket-approval-instance
> Path: 应用开发 / 服务端API / OA 审批 > 自有 OA 审批 > 审批实例 > 创建实例
> Updated: 2026-06-03 10:12:38

# 创建实例

调用本接口，创建不带流程的审批实例，返回的审批实例ID请务必注意保存，方便后续调用其他接口使用。

## **接口调用说明**

为治理开放接口传入非法数据问题，后续本接口将加强对传入数据合法性的校验。

- 单选/多选控件，传入的选项值应当均被配置在选项列表中
- 内部联系人控件，传入的userID应当是当前组织在职成员的userID
- 部门控件，部门ID应当是当前组织下合法的部门ID
- 关联审批单控件，传入的实例ID应当是当前组织下存在的审批实例ID

违背以上规则发起的审批单，后期有因为增强的表单数据校验，导致发起审批失败的风险

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/instances |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Instance.Write-工作流实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 是 | 审批模板code，可通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取processCode参数值。 |
| originatorUserId | String | 是 | 审批实例发起人的userId。 |
| formComponentValueList | Array | 否 | 表单控件列表，详情请参考[FormComponentValues 参数说明](0474-oa-formcomponent-message.md#9bcb6b14dbz03)说明，最多元素个数：100。      该接口不支持**地点控件**、**电话控件**。 |
| name | String | 否 | 表单名称。表单每一栏的名称，对应表单组件的label字段，最大长度64字符。 |
| value | String | 否 | 表单值，最大长度65535字符。 |
| extValue | String | 否 | 表单扩展值，最大长度8192字符。      目前联系人控件、关联审批单控件需要指定该值才能生成实例成功，具体请参照请求示例规范填写。 |
| id | String | 否 | 控件id，最大长度64字符，可调用[创建或更新审批模板](https://open.dingtalk.com/document/development/create-or-update-approval-templates-new)接口，获取[FormComponent参数说明](0474-oa-formcomponent-message.md#900adc515fxr6)内的componentId参数值。 |
| bizAlias | String | 否 | 控件别名，最大长度64字符。 |
| componentType | String | 否 | 控件类型，最大长度64字符，详情请参考[FormComponent参数说明](0474-oa-formcomponent-message.md#900adc515fxr6)。   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框       选项值应当被配置在选项列表中     - **DDMultiSelectField**：多选框       选项值均应当被配置在选项列表中     - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件（审批模板上设置好的场景，不支持发起审批实例时修改） - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件       联系人控件中的userID应当是当前组织下在职成员的userID     - **RelateField**：关联审批单       关联审批单传入的审批实例ID应当是当前组织下存在的审批实例ID     - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件       部门控件中应当传入当前组织下存在的部门ID |
| title | String | 否 | 实例标题，最大长度64字符。 |
| url | String | 是 | 第三方审批系统中审批单详情页地址，最大长度1024字符。 |
| notifiers | Array | 否 | 抄送信息列表，最多元素个数：20。 |
| userid | String | 否 | 抄送接收人用户userId。 |
| position | String | 否 | 抄送位置，取值：   - **start**：审批发起时，通知抄送人 - **finish**：审批通过后，通知抄送人 - **start\_finish**：审批发起时和审批通过后，都通知抄送人 |
| featureConfig | Object | 否 | 流程中心集成配置，支持实例维度指定审批的分组和回调配置。 |
| features | Array | 否 | 配置列表。 |
| name | String | 否 | 支持三方进行自定义配置的功能模块名称，当前支持：   - **CUSTOM\_SHORTCUT**：待办、卡片通知中的快捷操作按钮 - **AFFILIATION\_DIR**：指定待办业务分组 |
| pcUrl | String | 否 | 三方自定义的pc端跳转链接，最大长度1024字符。 |
| mobileUrl | String | 否 | 三方自定义的手机端跳转链接，最大长度1024字符。 |
| runType | String | 否 | 运行方式。  当features.name为`CUSTOM_SHORTCUT`时，支持   - **ORIGIN**：原生运行，打开待办详情页时，将会跳转到官方审批的详情页地址 - **REDIRECT**：外部跳转运行，打开待办详情页时，将会跳转到pcUrl、mobileUrl中配置的地址   当features.name为`AFFILIATION_DIR`时，支持   - **OUTBIZ\_CUSTOM**：指定待办分组，由业务自定义指定待办归属的分类信息 |
| callback | Object | 否 | 网关回调配置，需支持快捷操作按钮时该参数必填。  网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)。 |
| appUuid | String | 否 | 网关appUuid，需支持快捷操作按钮时该参数必填。  传[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时所属企业corpId值。 |
| apiKey | String | 否 | 网关apiKey，需支持快捷操作按钮时该参数必填。通过[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)内容获取`apiKey`。       - 在网关回调外部接口时，钉钉侧会根据不同业务场景，回传一些业务处理所需的参数给到ISV，ISV在收到回调请求后，若需要解析获取对应参数信息，需要在[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时配置对应的参数key。   例如，TASK\_EXECUTE任务执行模块，即详情页的同意、拒绝按钮配置回调时，钉钉侧回传的固定参数如下：`{"outResult":"agree","processInstanceId":"xxx","activityId":"xxx","corpId":"dingxxx","data":[],"remark":"同意","title":"xxx提交的资产领用申请","taskId":111,"operator":"manager0001"}`。 - ISV在创建数据源时，对应的参数配置需按业务需要填对应的key进行解析：outResult,processInstanceId,activityId,corpId,remark,title,taskId,operator |
| version | String | 否 | 网关接口版本       - 需支持快捷操作按钮时该参数必填。 - 默认传1。 |
| config | String | 否 | 三方进行自定义配置的功能模块对应的配置信息，最大长度1024字符。 |
| bizData | String | 否 | 用户自定义业务参数（json字符串格式），最大长度1024字符。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processCentres/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6dexxx
Content-Type:application/json

{
    /*
      该接口当前尚未支持审批应用中的所有控件，以以下列出示例的控件为准。
      基本的控件数据在传递时只需要填写 name 和 value 属性即可，两者都是字符串格式。
      如果数据是 json 格式，也需要先转义为字符串格式。
    */     
  "processCode" : "proc",
  "originatorUserId" : "manager1234",
  "formComponentValueList" : [ 
      {
            "name": "单行输入框",
            "value": "单行输入框示例"
        },
        {
            "name": "多行输入框",
            "value": "请输入多行文本内容，需要换行时请输入\r\n"
        },
        {
            "name": "数字输入框",
            "value": "100"
        },
        {
            /*
                value 可以直接填写实际的选项值
                选项值-如"选项1"必须是配置的选项列表中的值
                非法选项值后续有发起失败风险
            */
            "name": "单选框",
            "value": "选项1"
        },
        {
            /*
                value 需要将实际的选项值组成的数组转义为字符串，即使只有一个
                选项也需要是数组形式
                选项值-如"选项1"、"选项2"必须是配置的选项列表中的值
                非法选项值后续有发起失败风险
            */
            "name": "多选框",
            "value": "[\"选项1\",\"选项2\"]"
        }, 
        {
            /*
                value 仅支持 yyyy-MM-dd 一种格式
            */
            "name": "日期",
            "value": "2021-08-17"
        },
        {
            /*
                value 是时间数组的字符串形式，同样仅支持 yyyy-MM-dd 一种格式
            */
            "name": "[\"开始时间\",\"结束时间\"]",
            "value": "[\"2019-02-19\",\"2019-02-25\"]"
        },
        {
            /*
                value 需要将实际的 url 组成的数组转义为字符串，即使只有一个
                选项也需要是数组形式
            */
            "name": "图片",
            "value": "[\"http://url1\",\"http://url2\",\"http://url3\"]"
        },
        {
            /*
                表格控件的 value 是一个 json 对象的二维数组。数组中的每一行表示了表格中的一行数据，
                一行中的每个 json 对象表示表格中的一个控件。
            */
            "name": "表格",
            "value": "[[{\"name\":\"单行输入框\",\"value\":\"明细单行输入框\"},{\"name\":\"数字输入框\",\"value\":\"100\"}]]"
        },
        {
            "name": "金额（元）",
            "value": "100"
        },
        {
            /*
                附件控件的 value 是一个 json 数组转义为字符串形式。数组中的每个 json 对象是一个附件文件，
                每个文件都必须包含 spaceId、fileName、fileSize、fileType 和 fileId 字段，这些字段
                都可以通过调用钉盘的上传附件接口获取。
            */
            "name": "附件",
            "value": "[{\"spaceId\": \"163xxxx658\", \"fileName\": \"2644.JPG\", \"fileSize\": \"333\", \"fileType\": \"jpg\", \"fileId\": " +
    "\"643xxxx140\"}]"
        },
        {
            /*
                联系人中传的值是userId
                如果传入的userId不是当前企业在职的用户userId, 后续有发起失败风险
            */
            "name": "联系人",
            "value": "[\"4525xxxxxxxx77041\"]"
        },
        {
            /*
                value 需要将实际的审批单组成的数组转义为字符串，即使只有一个
                选项也需要是数组形式
                传入不存在的审批实例ID，后续有导致发起失败的风险
            */
            "name": "关联审批单",
            "value": "[\"fa2aa864-xxxx-xxxx-xxxx-75572c0e2cdf\", \"7125778e-xxxx-xxxx-xxxx-faa987478a9b\"]"
        },
        {
            /*
                省市区必须遵照地址控件的格式正确传递才可识别，且需使用英文格式逗号进行分隔
            */
              "name": "省市区",
              "value": "北京,北京市,河东区"
        },
        {
              "name": "评分",
              "value": "5"
        },
        {
            /*
                value 是钉钉通讯录内部门的id。当选择多个部门时，value 用英文逗号分隔
                如果传入的是非法的部门ID，后续有导致审批发起失败风险
            */
              "name": "部门",
              "value": "钉钉通讯录部门1的id,钉钉通讯录部门2的id"
        }
  ],
  "title" : "xxx的审批",
  "url" : "https://www.dingtalk.com/",
  "notifiers" : [ {
    "userid" : "manager001",
    "position" : "start"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceHeaders saveIntegratedInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceHeaders();
        saveIntegratedInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback featureConfigFeatures0Callback = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback()
                .setAppUuid("开发组织的corpId")
                .setApiKey("数据源配置后生成的apiKey")
                .setVersion("1");
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfigFeatures featureConfigFeatures0 = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfigFeatures()
                .setName("AFFILIATION_DIR")
                .setPcUrl("www.dingtalk.com")
                .setMobileUrl("www.dingtalk.com")
                .setRunType("REDIRECT")
                .setCallback(featureConfigFeatures0Callback)
                .setConfig("{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}");
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig featureConfig = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig()
                .setFeatures(java.util.Arrays.asList(
                    featureConfigFeatures0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers()
                .setUserid("manager001")
                .setPosition("start");
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValueList0 = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList()
                .setName("文本框")
                .setValue("abc")
                .setExtValue("abc")
                .setId("TextField-abc")
                .setBizAlias("abc")
                .setComponentType("TextField");
        com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest saveIntegratedInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.SaveIntegratedInstanceRequest()
                .setProcessCode("proc")
                .setOriginatorUserId("manager1234")
                .setFormComponentValueList(java.util.Arrays.asList(
                    formComponentValueList0
                ))
                .setTitle("xxx的审批")
                .setUrl("https://www.dingtalk.com/")
                .setNotifiers(java.util.Arrays.asList(
                    notifiers0
                ))
                .setFeatureConfig(featureConfig)
                .setBizData("\"{\"mykey\": \"myData\"}\"");
        try {
            client.saveIntegratedInstanceWithOptions(saveIntegratedInstanceRequest, saveIntegratedInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
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
        save_integrated_instance_headers = dingtalkworkflow__1__0_models.SaveIntegratedInstanceHeaders()
        save_integrated_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        feature_config_features_0callback = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback(
            app_uuid='开发组织的corpId',
            api_key='数据源配置后生成的apiKey',
            version='1'
        )
        feature_config_features_0 = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFeatureConfigFeatures(
            name='AFFILIATION_DIR',
            pc_url='www.dingtalk.com',
            mobile_url='www.dingtalk.com',
            run_type='REDIRECT',
            callback=feature_config_features_0callback,
            config='''{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}","refuseBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}"}}'''
        )
        feature_config = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFeatureConfig(
            features=[
                feature_config_features_0
            ]
        )
        notifiers_0 = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestNotifiers(
            userid='manager001',
            position='start'
        )
        form_component_value_list_0 = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFormComponentValueList(
            name='文本框',
            value='abc',
            ext_value='abc',
            id='TextField-abc',
            biz_alias='abc',
            component_type='TextField'
        )
        save_integrated_instance_request = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequest(
            process_code='proc',
            originator_user_id='manager1234',
            form_component_value_list=[
                form_component_value_list_0
            ],
            title='xxx的审批',
            url='https://www.dingtalk.com/',
            notifiers=[
                notifiers_0
            ],
            feature_config=feature_config,
            biz_data='"{"mykey": "myData"}"'
        )
        try:
            client.save_integrated_instance_with_options(save_integrated_instance_request, save_integrated_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        save_integrated_instance_headers = dingtalkworkflow__1__0_models.SaveIntegratedInstanceHeaders()
        save_integrated_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        feature_config_features_0callback = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback(
            app_uuid='开发组织的corpId',
            api_key='数据源配置后生成的apiKey',
            version='1'
        )
        feature_config_features_0 = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFeatureConfigFeatures(
            name='AFFILIATION_DIR',
            pc_url='www.dingtalk.com',
            mobile_url='www.dingtalk.com',
            run_type='REDIRECT',
            callback=feature_config_features_0callback,
            config='''{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}","refuseBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}"}}'''
        )
        feature_config = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFeatureConfig(
            features=[
                feature_config_features_0
            ]
        )
        notifiers_0 = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestNotifiers(
            userid='manager001',
            position='start'
        )
        form_component_value_list_0 = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequestFormComponentValueList(
            name='文本框',
            value='abc',
            ext_value='abc',
            id='TextField-abc',
            biz_alias='abc',
            component_type='TextField'
        )
        save_integrated_instance_request = dingtalkworkflow__1__0_models.SaveIntegratedInstanceRequest(
            process_code='proc',
            originator_user_id='manager1234',
            form_component_value_list=[
                form_component_value_list_0
            ],
            title='xxx的审批',
            url='https://www.dingtalk.com/',
            notifiers=[
                notifiers_0
            ],
            feature_config=feature_config,
            biz_data='"{"mykey": "myData"}"'
        )
        try:
            await client.save_integrated_instance_with_options_async(save_integrated_instance_request, save_integrated_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceRequest\featureConfig\features\callback;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceRequest\featureConfig\features;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceRequest\featureConfig;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceRequest\notifiers;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceRequest\formComponentValueList;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\SaveIntegratedInstanceRequest;
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
        $saveIntegratedInstanceHeaders = new SaveIntegratedInstanceHeaders([]);
        $saveIntegratedInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $featureConfigFeatures0Callback = new callback([
            "appUuid" => "开发组织的corpId",
            "apiKey" => "数据源配置后生成的apiKey",
            "version" => "1"
        ]);
        $featureConfigFeatures0 = new features([
            "name" => "AFFILIATION_DIR",
            "pcUrl" => "www.dingtalk.com",
            "mobileUrl" => "www.dingtalk.com",
            "runType" => "REDIRECT",
            "callback" => $featureConfigFeatures0Callback,
            "config" => "{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}"
        ]);
        $featureConfig = new featureConfig([
            "features" => [
                $featureConfigFeatures0
            ]
        ]);
        $notifiers0 = new notifiers([
            "userid" => "manager001",
            "position" => "start"
        ]);
        $formComponentValueList0 = new formComponentValueList([
            "name" => "文本框",
            "value" => "abc",
            "extValue" => "abc",
            "id" => "TextField-abc",
            "bizAlias" => "abc",
            "componentType" => "TextField"
        ]);
        $saveIntegratedInstanceRequest = new SaveIntegratedInstanceRequest([
            "processCode" => "proc",
            "originatorUserId" => "manager1234",
            "formComponentValueList" => [
                $formComponentValueList0
            ],
            "title" => "xxx的审批",
            "url" => "https://www.dingtalk.com/",
            "notifiers" => [
                $notifiers0
            ],
            "featureConfig" => $featureConfig,
            "bizData" => "\"{\"mykey\": \"myData\"}\""
        ]);
        try {
            $client->saveIntegratedInstanceWithOptions($saveIntegratedInstanceRequest, $saveIntegratedInstanceHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
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

  saveIntegratedInstanceHeaders := &dingtalkworkflow_1_0.SaveIntegratedInstanceHeaders{}
  saveIntegratedInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  featureConfigFeatures0Callback := &dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback{
    AppUuid: tea.String("开发组织的corpId"),
    ApiKey: tea.String("数据源配置后生成的apiKey"),
    Version: tea.String("1"),
  }
  featureConfigFeatures0 := &dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfigFeatures{
    Name: tea.String("AFFILIATION_DIR"),
    PcUrl: tea.String("www.dingtalk.com"),
    MobileUrl: tea.String("www.dingtalk.com"),
    RunType: tea.String("REDIRECT"),
    Callback: featureConfigFeatures0Callback,
    Config: tea.String("{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}"),
  }
  featureConfig := &dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfig{
    Features: []*dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfigFeatures{featureConfigFeatures0},
  }
  notifiers0 := &dingtalkworkflow_1_0.SaveIntegratedInstanceRequestNotifiers{
    Userid: tea.String("manager001"),
    Position: tea.String("start"),
  }
  formComponentValueList0 := &dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFormComponentValueList{
    Name: tea.String("文本框"),
    Value: tea.String("abc"),
    ExtValue: tea.String("abc"),
    Id: tea.String("TextField-abc"),
    BizAlias: tea.String("abc"),
    ComponentType: tea.String("TextField"),
  }
  saveIntegratedInstanceRequest := &dingtalkworkflow_1_0.SaveIntegratedInstanceRequest{
    ProcessCode: tea.String("proc"),
    OriginatorUserId: tea.String("manager1234"),
    FormComponentValueList: []*dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFormComponentValueList{formComponentValueList0},
    Title: tea.String("xxx的审批"),
    Url: tea.String("https://www.dingtalk.com/"),
    Notifiers: []*dingtalkworkflow_1_0.SaveIntegratedInstanceRequestNotifiers{notifiers0},
    FeatureConfig: featureConfig,
    BizData: tea.String("\"{\"mykey\": \"myData\"}\""),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SaveIntegratedInstanceWithOptions(saveIntegratedInstanceRequest, saveIntegratedInstanceHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let saveIntegratedInstanceHeaders = new dingtalkworkflow_1_0.SaveIntegratedInstanceHeaders({ });
    saveIntegratedInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let featureConfigFeatures0Callback = new dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback({
      appUuid: '开发组织的corpId',
      apiKey: '数据源配置后生成的apiKey',
      version: '1',
    });
    let featureConfigFeatures0 = new dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfigFeatures({
      name: 'AFFILIATION_DIR',
      pcUrl: 'www.dingtalk.com',
      mobileUrl: 'www.dingtalk.com',
      runType: 'REDIRECT',
      callback: featureConfigFeatures0Callback,
      config: '{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{\'en_US\':\'test\',\'ja_JP\':\'test\',\'vi_VN\':\'test\',\'zh_CN\':\'测试\',\'zh_HK\':\'测试\',\'zh_TW\':\'测试\'}}","refuseBtn":"{{\'en_US\':\'test\',\'ja_JP\':\'test\',\'vi_VN\':\'test\',\'zh_CN\':\'测试\',\'zh_HK\':\'测试\',\'zh_TW\':\'测试\'}}"}}',
    });
    let featureConfig = new dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFeatureConfig({
      features: [
        featureConfigFeatures0
      ],
    });
    let notifiers0 = new dingtalkworkflow_1_0.SaveIntegratedInstanceRequestNotifiers({
      userid: 'manager001',
      position: 'start',
    });
    let formComponentValueList0 = new dingtalkworkflow_1_0.SaveIntegratedInstanceRequestFormComponentValueList({
      name: '文本框',
      value: 'abc',
      extValue: 'abc',
      id: 'TextField-abc',
      bizAlias: 'abc',
      componentType: 'TextField',
    });
    let saveIntegratedInstanceRequest = new dingtalkworkflow_1_0.SaveIntegratedInstanceRequest({
      processCode: 'proc',
      originatorUserId: 'manager1234',
      formComponentValueList: [
        formComponentValueList0
      ],
      title: 'xxx的审批',
      url: 'https://www.dingtalk.com/',
      notifiers: [
        notifiers0
      ],
      featureConfig: featureConfig,
      bizData: '"{"mykey": "myData"}"',
    });
    try {
      await client.saveIntegratedInstanceWithOptions(saveIntegratedInstanceRequest, saveIntegratedInstanceHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceHeaders saveIntegratedInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceHeaders();
            saveIntegratedInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig.SaveIntegratedInstanceRequestFeatureConfigFeatures.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback featureConfigFeatures0Callback = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig.SaveIntegratedInstanceRequestFeatureConfigFeatures.SaveIntegratedInstanceRequestFeatureConfigFeaturesCallback
            {
                AppUuid = "开发组织的corpId",
                ApiKey = "数据源配置后生成的apiKey",
                Version = "1",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig.SaveIntegratedInstanceRequestFeatureConfigFeatures featureConfigFeatures0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig.SaveIntegratedInstanceRequestFeatureConfigFeatures
            {
                Name = "AFFILIATION_DIR",
                PcUrl = "www.dingtalk.com",
                MobileUrl = "www.dingtalk.com",
                RunType = "REDIRECT",
                Callback = featureConfigFeatures0Callback,
                Config = "{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig featureConfig = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig
            {
                Features = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFeatureConfig.SaveIntegratedInstanceRequestFeatureConfigFeatures>
                {
                    featureConfigFeatures0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers notifiers0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers
            {
                Userid = "manager001",
                Position = "start",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList formComponentValueList0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList
            {
                Name = "文本框",
                Value = "abc",
                ExtValue = "abc",
                Id = "TextField-abc",
                BizAlias = "abc",
                ComponentType = "TextField",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest saveIntegratedInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest
            {
                ProcessCode = "proc",
                OriginatorUserId = "manager1234",
                FormComponentValueList = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestFormComponentValueList>
                {
                    formComponentValueList0
                },
                Title = "xxx的审批",
                Url = "https://www.dingtalk.com/",
                Notifiers = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.SaveIntegratedInstanceRequest.SaveIntegratedInstanceRequestNotifiers>
                {
                    notifiers0
                },
                FeatureConfig = featureConfig,
                BizData = "\"{\"mykey\": \"myData\"}\"",
            };
            try
            {
                client.SaveIntegratedInstanceWithOptions(saveIntegratedInstanceRequest, saveIntegratedInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 结果。 |
| processInstanceId | String | 实例id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "processInstanceId" : "1234"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | aflowProcessFormContentInvalid | 审批流的表单格式错误 | 审批流的表单格式错误 |
| 400 | process.error | 审批流不存在 | 审批流不存在 |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | permission.error | 没有审批流操作权限 | 没有审批流操作权限 |
| 400 | instance.error | 发起审批实例失败 | 发起审批实例失败 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | required.error | %s | 必填项校验错误 |
| 400 | internalError | %s | 系统内部错误 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | formConverterError | 表单数据反向转换出错 | 表单数据反向转换出错 |
| 400 | parameter.invalid | 参数错误 | 参数错误 |
| 400 | processCode.in.blackList | 当前模板code已被加入黑名单，无法发起审批实例。 | 请确认该模板是否存在死循环等造成持续发起实例的情况。 |
| 400 | isvOrgId.in.blackList | 当前isv组织id已被加入黑名单，无法发起审批实例。 | 请确认该isv组织是否存在死循环等造成持续发起实例的情况。 |
| 400 | isvAppId.in.blackList | 当前isv应用appId已被加入黑名单，无法发起审批实例。 | 请确认该isv应用是否存在死循环等造成持续发起实例的情况。 |
| 500 | system.error | 系统错误 | 系统错误 |
