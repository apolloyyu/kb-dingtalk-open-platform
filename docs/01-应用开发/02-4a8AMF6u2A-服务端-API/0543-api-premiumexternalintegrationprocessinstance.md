---
title: "保存流程中心外部集成审批实例"
source_url: "https://open.dingtalk.com/document/development/api-premiumexternalintegrationprocessinstance"
namespace: "development"
slug: "api-premiumexternalintegrationprocessinstance"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 自有 OA 审批 > 审批实例 > 保存流程中心外部集成审批实例"
doc_id: "CPzgg9K5Sf"
updated_at: "2026-06-03 10:13:00"
---

> Source: https://open.dingtalk.com/document/development/api-premiumexternalintegrationprocessinstance
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 自有 OA 审批 > 审批实例 > 保存流程中心外部集成审批实例
> Updated: 2026-06-03 10:13:00

# 保存流程中心外部集成审批实例

调用本接口，可以将三方业务系统中的自有审批实例数据同步到钉钉OA审批，同时支持在实例维度进行审批页面托管、自定义业务分组、自定义快捷审批等多个高级功能模块自定义集成配置。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

### 特别提醒

为治理开放接口传入非法数据问题，后续本接口将加强对传入数据合法性的校验。

- 单选/多选控件，传入的选项值应当均被配置在选项列表中
- 内部联系人控件，传入的userID应当是当前组织在职成员的userID
- 部门控件，部门ID应当是当前组织下合法的部门ID
- 关联审批单控件，传入的实例ID应当是当前组织下存在的审批实例ID

违背以上规则发起的审批单，后期有因为增强的表单数据校验，导致发起审批失败的风险

### **调用说明**

例如，调用本接口创建了一个审批实例，可在**钉钉工作台 > OA审批 > 审批中心 > 已发起**查看，接口调用效果如下图所示。

![](https://img.alicdn.com/imgextra/i3/O1CN01TDKbCW28HuskT5vnR_!!6000000007908-2-tps-2724-650.png)

调用本接口，同时支持在实例维度进行审批页面托管、自定义业务分组、自定义快捷审批等多个高级功能模块自定义集成配置。

- 审批页面托管集成：支持三方业务使用钉钉官方统一详情页样式，0成本拥有钉钉一方功能。

  ![](https://img.alicdn.com/imgextra/i1/O1CN01KD3qSr1mIuNoPIqPU_!!6000000004932-0-tps-2454-1872.jpg)
- 审批页面托管集成：支持三方业务自定义配置/渲染审批操作区按钮（同意、拒绝等），且可透出三方业务执行异常报错文案详情。

  ![](https://img.alicdn.com/imgextra/i1/O1CN01hhUFwl1eMYc10iM62_!!6000000003857-0-tps-1062-810.jpg)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processCentres/instances |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 是 | 审批模板code，可通过调用[获取模板code](0511-obtain-the-template-code.md)接口获取processCode参数值。 |
| originatorUserId | String | 是 | 审批实例发起人的userId。 |
| formComponentValueList | Array | 否 | 表单控件列表。    具体请参照请求示例规范填写。 |
| name | String | 否 | 表单名称。表单每一栏的名称，对应表单组件的label字段。 |
| value | String | 否 | 表单值。 |
| extValue | String | 否 | 表单扩展值。    目前联系人控件、关联审批单控件需要指定该值才能生成实例成功，具体请参照请求示例规范填写。 |
| id | String | 否 | 控件id，可调用[创建或更新审批模板](https://open.dingtalk.com/document/development/create-or-update-approval-templates-new)接口，获取**FormComponent参数补充说明**内的componentId参数值。 |
| bizAlias | String | 否 | 控件别名。 |
| componentType | String | 否 | 控件类型。详情请参考本文**FormComponent参数补充说明**。   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框     选项值应当被配置在选项列表中   - **DDMultiSelectField**：多选框     选项值均应当被配置在选项列表中   - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件（审批模板上设置好的场景，不支持发起审批实例时修改） - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件     联系人控件中的userID应当是当前组织下在职成员的userID   - **RelateField**：关联审批单     关联审批单传入的审批实例ID应当是当前组织下存在的审批实例ID   - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件     部门控件中应当传入当前组织下存在的部门ID |
| title | String | 否 | 实例标题。 |
| url | String | 是 | 第三方审批系统中审批单详情页地址。 |
| notifiers | Array | 否 | 抄送信息列表。 |
| userid | String | 否 | 抄送接收人用户userId。 |
| position | String | 否 | 抄送位置，取值：   - **start**：审批发起时，通知抄送人 - **finish**：审批通过后，通知抄送人 - **start\_finish**：审批发起时和审批通过后，都通知抄送人 |
| featureConfig | Object | 否 | 流程中心集成配置，支持实例维度指定审批托管、自定义业务分组等回调配置。若同时在模板/实例维度进行了配置，优先以实例维度为准。 |
| features | Array | 否 | 配置列表。 |
| name | String | 否 | 支持三方进行自定义配置的功能模块名称，本接口当前支持：   - **TASK\_EXECUTE**：任务执行模块，即详情页的同意、拒绝按钮 - **SYNC\_BOXSTER**：任务同步待办方式 - **CUSTOM\_SHORTCUT**：待办、卡片通知中的快捷操作按钮 - **AFFILIATION\_DIR**：指定待办业务分组 - **CUSTOM\_ACTION\_DEFINITION**：以审批页面托管模式集成时使用，表示获取操作区（按钮）数据的回调地址（按钮渲染） - **CUSTOM\_ACTION\_APPLY**：以审批页面托管模式集成时使用，表示进行审批操作时回调的回调地址（操作审批） |
| pcUrl | String | 否 | 三方自定义的pc端跳转链接。 |
| mobileUrl | String | 否 | 三方自定义的手机端跳转链接。 |
| runType | String | 否 | 运行方式。 当features.name为`TASK_EXECUTE`时，支持   - **ORIGIN**：原生运行，即在官方审批内运行对应功能，将会回调callback中配置的回调接口 - **REDIRECT**：外部跳转运行，需要跳转到三方地址运行对应功能，将会跳转到pcUrl、mobileUrl中配置的地址   当features.name为`SYNC_BOXSTER`时，支持   - **DEFAULT**：默认将审批任务同步待办 - **OUTBIZ\_CUSTOM**：不同步待办，由业务自定义实现   当features.name为`CUSTOM_SHORTCUT`时，支持   - **REDIRECT**：外部跳转运行，打开待办详情页时，将会跳转到三方业务系统详情页地址。在待办列表执行同意/拒绝快捷审批操作时，将会回调callback中配置的回调接口。   当features.name为`AFFILIATION_DIR`时，支持   - **OUTBIZ\_CUSTOM**：指定待办分组，由业务自定义指定待办归属的分类信息   当features.name为`CUSTOM_ACTION_DEFINITION`时，支持   - **OUTBIZ\_CUSTOM**：审批页面托管模式集成时使用，表示在审批详情页获取操作区（按钮）数据的回调地址（按钮渲染），将会回调callback中配置的回调接口。   当features.name为`CUSTOM_ACTION_APPLY`时，支持   - **OUTBIZ\_CUSTOM**：审批页面托管模式集成时使用，表示在审批详情页进行审批操作时回调的回调地址（操作审批），将会回调callback中配置的回调接口。 |
| callback | Object | 否 | 网关回调配置，当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。  网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[创建数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)。 |
| appUuid | String | 否 | 网关appUuid，当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。  传[创建数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)时所属企业corpId值。 |
| apiKey | String | 否 | 网关apiKey，当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。通过[创建数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)内容获取`apiKey`。     - 在网关回调外部接口时，钉钉侧会根据不同业务场景，回传一些业务处理所需的参数给到ISV，ISV在收到回调请求后，若需要解析获取对应参数信息，需要在[创建数据源](../../08-工作台/02-Qzb8Lpee2t-使用教程/0009-dashboard-create-data-source.md)时配置对应的参数key。   例如，TASK\_EXECUTE任务执行模块，即详情页的同意、拒绝按钮配置回调时，钉钉侧回传的固定参数如下：`{"outResult":"agree","processInstanceId":"xxx","activityId":"xxx","corpId":"dingxxx","data":[],"remark":"同意","title":"xxx提交的资产领用申请","taskId":111,"operator":"manager0001"}`。 - ISV在创建数据源时，对应的参数配置需按业务需要填对应的key进行解析：outResult,processInstanceId,activityId,corpId,remark,title,taskId,operator |
| version | String | 否 | 网关接口版本     - 当需支持三方自定义实现审批页面托管、快捷操作按钮等feature时该参数必填。 - 默认传1。 |
| config | String | 否 | 三方进行自定义配置的功能模块对应的配置信息。 |
| bizData | String | 否 | 用户自定义业务参数（json字符串格式）。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processCentres/instances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6dexxx
Content-Type:application/json

{
  "processCode" : "proc-xxxx",
  "originatorUserId" : "manager1234",
  "formComponentValueList" : [ {
    "name" : "文本框",
    "value" : "abc",
    "extValue" : "abc",
    "id" : "TextField-abc",
    "bizAlias" : "abc",
    "componentType" : "TextField"
  } ],
  "title" : "xxx的审批",
  "url" : "https://www.dingtalk.com/",
  "notifiers" : [ {
    "userid" : "manager001",
    "position" : "start"
  } ],
  "featureConfig" : {
    "features" : [ {
      "name" : "TASK_EXECUTE",
      "pcUrl" : "www.dingtalk.com",
      "mobileUrl" : "www.dingtalk.com",
      "runType" : "ORIGIN",
      "callback" : {
        "appUuid" : "appUuid",
        "apiKey" : "apiKey",
        "version" : "1"
      },
      "config" : "{\\\"shortcutStyle\\\":\\\"EXECUTE_ACTION\\\",       \\\"buttonConfig\\\":{\\\"agreeBtn\\\":\\\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\\\",\\\"refuseBtn\\\":\\\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\\\"}}"
    } ]
  },
  "bizData" : "\"{\\\"mykey\\\": \\\"myData\\\"}\""
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
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceHeaders premiumSaveIntegratedProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceHeaders();
        premiumSaveIntegratedProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback featureConfigFeatures0Callback = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback()
                .setAppUuid("appUuid")
                .setApiKey("apiKey")
                .setVersion("1");
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures featureConfigFeatures0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures()
                .setName("TASK_EXECUTE")
                .setPcUrl("www.dingtalk.com")
                .setMobileUrl("www.dingtalk.com")
                .setRunType("ORIGIN")
                .setCallback(featureConfigFeatures0Callback)
                .setConfig("{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}");
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig featureConfig = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig()
                .setFeatures(java.util.Arrays.asList(
                    featureConfigFeatures0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestNotifiers notifiers0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestNotifiers()
                .setUserid("manager001")
                .setPosition("start");
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList formComponentValueList0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList()
                .setName("文本框")
                .setValue("abc")
                .setExtValue("abc")
                .setId("TextField-abc")
                .setBizAlias("abc")
                .setComponentType("TextField");
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest premiumSaveIntegratedProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveIntegratedProcessInstanceRequest()
                .setProcessCode("proc-xxxx")
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
            client.premiumSaveIntegratedProcessInstanceWithOptions(premiumSaveIntegratedProcessInstanceRequest, premiumSaveIntegratedProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_save_integrated_process_instance_headers = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceHeaders()
        premium_save_integrated_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        feature_config_features_0callback = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback(
            app_uuid='appUuid',
            api_key='apiKey',
            version='1'
        )
        feature_config_features_0 = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures(
            name='TASK_EXECUTE',
            pc_url='www.dingtalk.com',
            mobile_url='www.dingtalk.com',
            run_type='ORIGIN',
            callback=feature_config_features_0callback,
            config='''{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}","refuseBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}"}}'''
        )
        feature_config = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig(
            features=[
                feature_config_features_0
            ]
        )
        notifiers_0 = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestNotifiers(
            userid='manager001',
            position='start'
        )
        form_component_value_list_0 = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList(
            name='文本框',
            value='abc',
            ext_value='abc',
            id='TextField-abc',
            biz_alias='abc',
            component_type='TextField'
        )
        premium_save_integrated_process_instance_request = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequest(
            process_code='proc-xxxx',
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
            client.premium_save_integrated_process_instance_with_options(premium_save_integrated_process_instance_request, premium_save_integrated_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_save_integrated_process_instance_headers = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceHeaders()
        premium_save_integrated_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        feature_config_features_0callback = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback(
            app_uuid='appUuid',
            api_key='apiKey',
            version='1'
        )
        feature_config_features_0 = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures(
            name='TASK_EXECUTE',
            pc_url='www.dingtalk.com',
            mobile_url='www.dingtalk.com',
            run_type='ORIGIN',
            callback=feature_config_features_0callback,
            config='''{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}","refuseBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}"}}'''
        )
        feature_config = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig(
            features=[
                feature_config_features_0
            ]
        )
        notifiers_0 = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestNotifiers(
            userid='manager001',
            position='start'
        )
        form_component_value_list_0 = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList(
            name='文本框',
            value='abc',
            ext_value='abc',
            id='TextField-abc',
            biz_alias='abc',
            component_type='TextField'
        )
        premium_save_integrated_process_instance_request = dingtalkworkflow__1__0_models.PremiumSaveIntegratedProcessInstanceRequest(
            process_code='proc-xxxx',
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
            await client.premium_save_integrated_process_instance_with_options_async(premium_save_integrated_process_instance_request, premium_save_integrated_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceRequest\featureConfig\features\callback;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceRequest\featureConfig\features;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceRequest\featureConfig;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceRequest\notifiers;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceRequest\formComponentValueList;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveIntegratedProcessInstanceRequest;
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
        $premiumSaveIntegratedProcessInstanceHeaders = new PremiumSaveIntegratedProcessInstanceHeaders([]);
        $premiumSaveIntegratedProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $featureConfigFeatures0Callback = new callback([
            "appUuid" => "appUuid",
            "apiKey" => "apiKey",
            "version" => "1"
        ]);
        $featureConfigFeatures0 = new features([
            "name" => "TASK_EXECUTE",
            "pcUrl" => "www.dingtalk.com",
            "mobileUrl" => "www.dingtalk.com",
            "runType" => "ORIGIN",
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
        $premiumSaveIntegratedProcessInstanceRequest = new PremiumSaveIntegratedProcessInstanceRequest([
            "processCode" => "proc-xxxx",
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
            $client->premiumSaveIntegratedProcessInstanceWithOptions($premiumSaveIntegratedProcessInstanceRequest, $premiumSaveIntegratedProcessInstanceHeaders, new RuntimeOptions([]));
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

  premiumSaveIntegratedProcessInstanceHeaders := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceHeaders{}
  premiumSaveIntegratedProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  featureConfigFeatures0Callback := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback{
    AppUuid: tea.String("appUuid"),
    ApiKey: tea.String("apiKey"),
    Version: tea.String("1"),
  }
  featureConfigFeatures0 := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures{
    Name: tea.String("TASK_EXECUTE"),
    PcUrl: tea.String("www.dingtalk.com"),
    MobileUrl: tea.String("www.dingtalk.com"),
    RunType: tea.String("ORIGIN"),
    Callback: featureConfigFeatures0Callback,
    Config: tea.String("{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}"),
  }
  featureConfig := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig{
    Features: []*dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures{featureConfigFeatures0},
  }
  notifiers0 := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestNotifiers{
    Userid: tea.String("manager001"),
    Position: tea.String("start"),
  }
  formComponentValueList0 := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList{
    Name: tea.String("文本框"),
    Value: tea.String("abc"),
    ExtValue: tea.String("abc"),
    Id: tea.String("TextField-abc"),
    BizAlias: tea.String("abc"),
    ComponentType: tea.String("TextField"),
  }
  premiumSaveIntegratedProcessInstanceRequest := &dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequest{
    ProcessCode: tea.String("proc-xxxx"),
    OriginatorUserId: tea.String("manager1234"),
    FormComponentValueList: []*dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList{formComponentValueList0},
    Title: tea.String("xxx的审批"),
    Url: tea.String("https://www.dingtalk.com/"),
    Notifiers: []*dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestNotifiers{notifiers0},
    FeatureConfig: featureConfig,
    BizData: tea.String("\"{\"mykey\": \"myData\"}\""),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumSaveIntegratedProcessInstanceWithOptions(premiumSaveIntegratedProcessInstanceRequest, premiumSaveIntegratedProcessInstanceHeaders, &util.RuntimeOptions{})
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
    let premiumSaveIntegratedProcessInstanceHeaders = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceHeaders({ });
    premiumSaveIntegratedProcessInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let featureConfigFeatures0Callback = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback({
      appUuid: 'appUuid',
      apiKey: 'apiKey',
      version: '1',
    });
    let featureConfigFeatures0 = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures({
      name: 'TASK_EXECUTE',
      pcUrl: 'www.dingtalk.com',
      mobileUrl: 'www.dingtalk.com',
      runType: 'ORIGIN',
      callback: featureConfigFeatures0Callback,
      config: '{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{\'en_US\':\'test\',\'ja_JP\':\'test\',\'vi_VN\':\'test\',\'zh_CN\':\'测试\',\'zh_HK\':\'测试\',\'zh_TW\':\'测试\'}}","refuseBtn":"{{\'en_US\':\'test\',\'ja_JP\':\'test\',\'vi_VN\':\'test\',\'zh_CN\':\'测试\',\'zh_HK\':\'测试\',\'zh_TW\':\'测试\'}}"}}',
    });
    let featureConfig = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig({
      features: [
        featureConfigFeatures0
      ],
    });
    let notifiers0 = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestNotifiers({
      userid: 'manager001',
      position: 'start',
    });
    let formComponentValueList0 = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList({
      name: '文本框',
      value: 'abc',
      extValue: 'abc',
      id: 'TextField-abc',
      bizAlias: 'abc',
      componentType: 'TextField',
    });
    let premiumSaveIntegratedProcessInstanceRequest = new dingtalkworkflow_1_0.PremiumSaveIntegratedProcessInstanceRequest({
      processCode: 'proc-xxxx',
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
      await client.premiumSaveIntegratedProcessInstanceWithOptions(premiumSaveIntegratedProcessInstanceRequest, premiumSaveIntegratedProcessInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceHeaders premiumSaveIntegratedProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceHeaders();
            premiumSaveIntegratedProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback featureConfigFeatures0Callback = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeaturesCallback
            {
                AppUuid = "appUuid",
                ApiKey = "apiKey",
                Version = "1",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures featureConfigFeatures0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures
            {
                Name = "TASK_EXECUTE",
                PcUrl = "www.dingtalk.com",
                MobileUrl = "www.dingtalk.com",
                RunType = "ORIGIN",
                Callback = featureConfigFeatures0Callback,
                Config = "{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig featureConfig = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig
            {
                Features = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFeatureConfig.PremiumSaveIntegratedProcessInstanceRequestFeatureConfigFeatures>
                {
                    featureConfigFeatures0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestNotifiers notifiers0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestNotifiers
            {
                Userid = "manager001",
                Position = "start",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList formComponentValueList0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList
            {
                Name = "文本框",
                Value = "abc",
                ExtValue = "abc",
                Id = "TextField-abc",
                BizAlias = "abc",
                ComponentType = "TextField",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest premiumSaveIntegratedProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest
            {
                ProcessCode = "proc-xxxx",
                OriginatorUserId = "manager1234",
                FormComponentValueList = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestFormComponentValueList>
                {
                    formComponentValueList0
                },
                Title = "xxx的审批",
                Url = "https://www.dingtalk.com/",
                Notifiers = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveIntegratedProcessInstanceRequest.PremiumSaveIntegratedProcessInstanceRequestNotifiers>
                {
                    notifiers0
                },
                FeatureConfig = featureConfig,
                BizData = "\"{\"mykey\": \"myData\"}\"",
            };
            try
            {
                client.PremiumSaveIntegratedProcessInstanceWithOptions(premiumSaveIntegratedProcessInstanceRequest, premiumSaveIntegratedProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| processInstanceId | String | 实例ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "processInstanceId" : "proc-abc"
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
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 400 | processCode.in.blackList | 当前模板code已被加入黑名单，无法发起审批实例。 | 请确认该模板是否存在死循环等造成持续发起实例的情况。 |
| 400 | isvOrgId.in.blackList | 当前isv组织id已被加入黑名单，无法发起审批实例。 | 请确认该isv组织是否存在死循环等造成持续发起实例的情况。 |
| 400 | isvAppId.in.blackList | 当前isv应用appId已被加入黑名单，无法发起审批实例。 | 请确认该isv应用是否存在死循环等造成持续发起实例的情况。 |
| 500 | system.error | 系统错误 | 系统错误 |
