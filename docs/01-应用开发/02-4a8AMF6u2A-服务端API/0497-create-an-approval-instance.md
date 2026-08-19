---
title: "发起审批实例"
source_url: "https://open.dingtalk.com/document/development/create-an-approval-instance"
namespace: "development"
slug: "create-an-approval-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批实例 > 发起审批实例"
doc_id: "2R6nkzxvGs"
updated_at: "2026-04-24 14:10:43"
---

> Source: https://open.dingtalk.com/document/development/create-an-approval-instance
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批实例 > 发起审批实例
> Updated: 2026-04-24 14:10:43

# 发起审批实例

调用本接口，用于发起OA审批实例，假勤、人事、财税、法务、商旅等套件暂不支持直接通过本接口发起审批实例。

## **接口调用说明**

### 特别提醒

为治理开放接口传入非法数据问题，后续本接口将加强对传入数据合法性的校验。

- 单选/多选控件，传入的选项值应当均被配置在选项列表中
- 内部联系人控件，传入的userID应当是当前组织在职成员的userID
- 部门控件，部门ID应当是当前组织下合法的部门ID
- 关联审批单控件，传入的实例ID应当是当前组织下存在的审批实例ID

违背以上规则发起的审批单，后期有因为增强的表单数据校验，导致发起审批失败的风险

### 使用场景

> **[!NOTE]**
>
> 发起审批实例后，无法通过API修改审批实例信息。

根据是否指定审批人，即是否重新设置审批流，或复用审批后台设置的审批流，发起审批实例有2种方式。

- 不指定审批人，复用审批后台设置的审批流。复用审批后台设置的审批流时，需注意以下：

  - 审批人和抄送人均复用审批后台设置的人员。
  - 审批后台支持的流程设计均支持，例如或签、会签、条件审批、发起人自选等。

    ![](https://img.alicdn.com/imgextra/i1/O1CN0174pIjt1log3f0JMW4_!!6000000004866-2-tps-874-1334.png)
- 指定审批人，不复用在OA后台设置的审批流。

  - 不支持审批模板的高级设置，例如手写签名、表单操作权限等均无法使用。 ![](https://img.alicdn.com/imgextra/i4/O1CN01rlGRQZ21hpzmhixr3_!!6000000007017-2-tps-1912-1186.png)
  - 指定审批人方式，不支持调用本接口设置审批人为发起人自选。

### 使用说明

情况一：不指定审批人，复用审批后台设置的审批流。

> **[!NOTE]**
>
> - approvers参数不传值，默认复用审批后台设置的审批流。
> - 通过接口设置的抄送人ccList和ccPosition参数不生效，会复用审批后台设置的抄送人员。

- 审批流是否有自选节点，分为2种情况。

  - 有自选节点，调用[获取审批单流程中的节点信息](0493-approval-process-prediction.md)接口，返回的所有节点中isTargetSelect值全部是true。
  > **[!NOTE]**
  >
  > 调用本接口发起审批实例时，参数approvers和targetSelectActioners均不传值。

  - 无自选节点，调用[获取审批单流程中的节点信息](0493-approval-process-prediction.md)接口，返回的信息中存在isTargetSelect值为false。
  > **[!NOTE]**
  >
  > 调用本接口发起审批实例时，参数approvers不传值，传入参数targetSelectActioners的值，用于指定发起人自选节点内的信息。

情况二：指定审批人，不复用在OA后台设置的审批流程。通过approvers参数重新指定审批人。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances |
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
| bizDetailPageUrl | String | 否 | 第三方审批系统中审批单详情页地址，用于满足三方业务自研页面 + OA审批官方工作流集成的复杂业务场景诉求。最大长度1024字符。     - 指定bizDetailPageUrl功能为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享功能，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](1442-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md#a56c9869e4v0i) - 若指定了bizDetailPageUrl，在钉钉OA审批、钉钉待办、消息卡片等入口点击跳转时，将会直接跳转对应业务系统详情页地址。 |
| originatorUserId | String | 是 | 审批发起人的userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| processCode | String | 是 | 审批流的唯一码。process\_code在审批模板编辑页面的URL中获取。 |
| deptId | Long | 否 | 审批发起人所在的部门ID。     - 若approvers已传值时（即直接指定审批人列表），则deptId不需填写。 - 若approvers未传值时（即不直接指定审批人列表），则deptId需必填，可通过[查询用户详情](0056-query-user-details.md)接口获取返回的部门ID，若为根部门ID需填-1。 |
| microappAgentId | Long | 否 | 应用标识AgentId，详情参见[基础概念](https://open.dingtalk.com/document/development/development-basic-concepts)。 |
| approvers | Array | 否 | 不使用审批流模板时，直接指定的审批人列表，最大列表长度：20。    指定审批单的执行流程，会覆盖审批单在OA后台设置的默认流程。 |
| actionType | String | 否 | 审批类型，取值：   - **AND**：会签 - **OR**：或签 - **NONE**：单人审批 |
| userIds | Array of String | 否 | 审批人 userId。 例如：["user001","user002"]。 |
| ccList | Array of String | 否 | 抄送人 userId。    最大列表长度为50。 |
| ccPosition | String | 否 | 抄送时间点，取值：   - **START**：开始时抄送 - **FINISH**：结束时抄送 - **START\_FINISH**：开始和结束时都抄送 |
| targetSelectActioners | Array | 否 | 使用审批流模板时，流程预测结果中节点规则上必填的自选操作人列表，最大列表长度：20。    使用OA后台设置的默认流程，并且流程中有审批人自选节点，该参数必填。 |
| actionerKey | String | 否 | 自选节点的规则key，可调用[获取审批单流程中的节点信息](0493-approval-process-prediction.md)接口获取actorKey参数值。 |
| actionerUserIds | Array of String | 否 | 操作人 userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| formComponentValues | Array | 是 | 表单控件列表，详情请参考[FormComponentValues 参数说明](0474-oa-formcomponent-message.md#9bcb6b14dbz03)，最大列表长度：150。 |
| id | String | 否 | 控件id。 |
| bizAlias | String | 否 | 控件别名。 |
| name | String | 是 | 控件名称，与[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口中组件`label`字段值保持一致。 |
| value | String | 是 | 控件值，最大长度65535字符。 |
| extValue | String | 否 | 控件扩展值，最大长度65535字符。 |
| componentType | String | 否 | 控件类型，取值：   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框    选项值应当被配置在选项列表中 - **DDMultiSelectField**：多选框    选项值均应当被配置在选项列表中 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件（审批模板上设置好的场景，不支持发起审批实例时修改） - **PhoneField**：电话控件 - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件    联系人控件中的userID应当是当前组织下在职成员的userID - **RelateField**：关联审批单    关联审批单传入的审批实例ID应当是当前组织下存在的审批实例ID - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件    部门控件中应当传入当前组织下存在的部门ID。 |
| details | Array | 否 | 子控件列表，最大元素个数：150。明细控件最大总长度65535字符。 |
| id | String | 否 | 控件id。 |
| bizAlias | String | 否 | 控件别名。 |
| name | String | 否 | 控件名称。 |
| value | String | 否 | 控件值。 |
| extValue | String | 否 | 控件扩展值。 |
| details | Array | 否 | 子控件列表，最大列表长度：150。 |
| id | String | 否 | 控件id。 |
| bizAlias | String | 否 | 控件别名。 |
| name | String | 否 | 控件名称。 |
| value | String | 否 | 控件值。 |
| extValue | String | 否 | 控件扩展值。 |
| componentType | String | 否 | 控件类型，取值：   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框    选项值应当被配置在选项列表中 - **DDMultiSelectField**：多选框    选项值均应被配置在选项列表中 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件（审批模板上设置好的场景，不支持发起审批实例时修改） - **PhoneField**：电话控件 - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件    联系人控件应当传入当前组织在职userID - **RelateField**：关联审批单    关联审批单应当传入当前组织下存在的审批实例ID - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件    部门控件传入的部门ID应当是当前企业下存在的部门 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processInstances HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
    /*
      该接口当前尚未支持审批应用中的所有控件，以以下列出示例的控件为准。
      基本的控件数据在传递时只需要填写 name 和 value 属性即可，两者都是字符串格式。
      如果数据是 json 格式，也需要先转义为字符串格式。
    */ 
    "processCode": "PROC-17428B8C-6C60-xxxx-924C-64F1037AE067",
    "originatorUserId": "26652461xxxx5992",
    "deptId": 1,
    "microappAgentId": 1234,
    "formComponentValues":[
        {
            "name": "[\"当前时间\",\"当前地点\"]",
            "value": "[\"2025-01-03 14:27:20\",120.021195,30.281506,\"浙江省杭州市余杭区文一西路960-1号阿里巴巴西溪C区\",100]"
        },
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
                国内手机号 +86 加不加均可，国际手机号需加国际区号，否则可能导致无法解析；
                固话区号加不加均可
            */
            "name": "电话",
              "value": "157xxxx4545"
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
    "targetSelectActioners":[
        {
            "actionerKey": "manual_f953_8c70_xxxx_7ffa",
            "actionerUserIds": ["26652461xxxx5992", "011220460xxxx8765"]
        }
    ],
    "approvers": [
        {
            "actionType": "AND",
            "userIds": ["26652461xxxx5992", "011220460xxxx8765"]
        }
    ],
    "ccList": ["25054456xxxx0123"],
    "ccPosition": "START",
    "RequestId" : "4F73A5B6-81E5-1556-BC35-C2912C84993D"
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
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceHeaders startProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceHeaders();
        startProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetailsDetails formComponentValues0Details0Details0 = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetailsDetails()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setComponentType("PhoneField");
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details0 = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValuesDetails()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setDetails(java.util.Arrays.asList(
                    formComponentValues0Details0Details0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues0 = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("myPhoneNumber")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setComponentType("PhoneField")
                .setDetails(java.util.Arrays.asList(
                    formComponentValues0Details0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestTargetSelectActioners targetSelectActioners0 = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestTargetSelectActioners()
                .setActionerKey("manual_1918_5cd3_xxxx_6a98")
                .setActionerUserIds(java.util.Arrays.asList(
                    "26652461xxxx5992"
                ));
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers0 = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest.StartProcessInstanceRequestApprovers()
                .setActionType("AND")
                .setUserIds(java.util.Arrays.asList(
                    "26652461xxxx5992"
                ));
        com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest startProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.StartProcessInstanceRequest()
                .setBizDetailPageUrl("https://www.dingtalk.com")
                .setOriginatorUserId("manager432")
                .setProcessCode("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1")
                .setDeptId(1L)
                .setMicroappAgentId(41605932L)
                .setApprovers(java.util.Arrays.asList(
                    approvers0
                ))
                .setCcList(java.util.Arrays.asList(
                    "26652461xxxx5992"
                ))
                .setCcPosition("START")
                .setTargetSelectActioners(java.util.Arrays.asList(
                    targetSelectActioners0
                ))
                .setFormComponentValues(java.util.Arrays.asList(
                    formComponentValues0
                ));
        try {
            client.startProcessInstanceWithOptions(startProcessInstanceRequest, startProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        start_process_instance_headers = dingtalkworkflow__1__0_models.StartProcessInstanceHeaders()
        start_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_component_values_0details_0details_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestFormComponentValuesDetailsDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='PhoneField'
        )
        form_component_values_0details_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestFormComponentValuesDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            details=[
                form_component_values_0details_0details_0
            ]
        )
        form_component_values_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestFormComponentValues(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='myPhoneNumber',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='PhoneField',
            details=[
                form_component_values_0details_0
            ]
        )
        target_select_actioners_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestTargetSelectActioners(
            actioner_key='manual_1918_5cd3_xxxx_6a98',
            actioner_user_ids=[
                '26652461xxxx5992'
            ]
        )
        approvers_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestApprovers(
            action_type='AND',
            user_ids=[
                '26652461xxxx5992'
            ]
        )
        start_process_instance_request = dingtalkworkflow__1__0_models.StartProcessInstanceRequest(
            biz_detail_page_url='https://www.dingtalk.com',
            originator_user_id='manager432',
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            dept_id=1,
            microapp_agent_id=41605932,
            approvers=[
                approvers_0
            ],
            cc_list=[
                '26652461xxxx5992'
            ],
            cc_position='START',
            target_select_actioners=[
                target_select_actioners_0
            ],
            form_component_values=[
                form_component_values_0
            ]
        )
        try:
            client.start_process_instance_with_options(start_process_instance_request, start_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        start_process_instance_headers = dingtalkworkflow__1__0_models.StartProcessInstanceHeaders()
        start_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_component_values_0details_0details_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestFormComponentValuesDetailsDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='PhoneField'
        )
        form_component_values_0details_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestFormComponentValuesDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            details=[
                form_component_values_0details_0details_0
            ]
        )
        form_component_values_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestFormComponentValues(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='myPhoneNumber',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='PhoneField',
            details=[
                form_component_values_0details_0
            ]
        )
        target_select_actioners_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestTargetSelectActioners(
            actioner_key='manual_1918_5cd3_xxxx_6a98',
            actioner_user_ids=[
                '26652461xxxx5992'
            ]
        )
        approvers_0 = dingtalkworkflow__1__0_models.StartProcessInstanceRequestApprovers(
            action_type='AND',
            user_ids=[
                '26652461xxxx5992'
            ]
        )
        start_process_instance_request = dingtalkworkflow__1__0_models.StartProcessInstanceRequest(
            biz_detail_page_url='https://www.dingtalk.com',
            originator_user_id='manager432',
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            dept_id=1,
            microapp_agent_id=41605932,
            approvers=[
                approvers_0
            ],
            cc_list=[
                '26652461xxxx5992'
            ],
            cc_position='START',
            target_select_actioners=[
                target_select_actioners_0
            ],
            form_component_values=[
                form_component_values_0
            ]
        )
        try:
            await client.start_process_instance_with_options_async(start_process_instance_request, start_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceRequest\formComponentValues\details\details;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceRequest\formComponentValues;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceRequest\targetSelectActioners;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceRequest\approvers;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceRequest;
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
        $startProcessInstanceHeaders = new StartProcessInstanceHeaders([]);
        $startProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $formComponentValues0Details0Details0 = new details([
            "id" => "PhoneField_IZI2LP8QF6O0",
            "bizAlias" => "Phone",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "componentType" => "PhoneField"
        ]);
        $formComponentValues0Details0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\StartProcessInstanceRequest\formComponentValues\details([
            "id" => "PhoneField_IZI2LP8QF6O0",
            "bizAlias" => "Phone",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "details" => [
                $formComponentValues0Details0Details0
            ]
        ]);
        $formComponentValues0 = new formComponentValues([
            "id" => "PhoneField_IZI2LP8QF6O0",
            "bizAlias" => "myPhoneNumber",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "componentType" => "PhoneField",
            "details" => [
                $formComponentValues0Details0
            ]
        ]);
        $targetSelectActioners0 = new targetSelectActioners([
            "actionerKey" => "manual_1918_5cd3_xxxx_6a98",
            "actionerUserIds" => [
                "26652461xxxx5992"
            ]
        ]);
        $approvers0 = new approvers([
            "actionType" => "AND",
            "userIds" => [
                "26652461xxxx5992"
            ]
        ]);
        $startProcessInstanceRequest = new StartProcessInstanceRequest([
            "bizDetailPageUrl" => "https://www.dingtalk.com",
            "originatorUserId" => "manager432",
            "processCode" => "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
            "deptId" => 1,
            "microappAgentId" => 41605932,
            "approvers" => [
                $approvers0
            ],
            "ccList" => [
                "26652461xxxx5992"
            ],
            "ccPosition" => "START",
            "targetSelectActioners" => [
                $targetSelectActioners0
            ],
            "formComponentValues" => [
                $formComponentValues0
            ]
        ]);
        try {
            $client->startProcessInstanceWithOptions($startProcessInstanceRequest, $startProcessInstanceHeaders, new RuntimeOptions([]));
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

  startProcessInstanceHeaders := &dingtalkworkflow_1_0.StartProcessInstanceHeaders{}
  startProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  formComponentValues0Details0Details0 := &dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValuesDetailsDetails{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    ComponentType: tea.String("PhoneField"),
  }
  formComponentValues0Details0 := &dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValuesDetails{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    Details: []*dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValuesDetailsDetails{formComponentValues0Details0Details0},
  }
  formComponentValues0 := &dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValues{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("myPhoneNumber"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    ComponentType: tea.String("PhoneField"),
    Details: []*dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValuesDetails{formComponentValues0Details0},
  }
  targetSelectActioners0 := &dingtalkworkflow_1_0.StartProcessInstanceRequestTargetSelectActioners{
    ActionerKey: tea.String("manual_1918_5cd3_xxxx_6a98"),
    ActionerUserIds: []*string{tea.String("26652461xxxx5992")},
  }
  approvers0 := &dingtalkworkflow_1_0.StartProcessInstanceRequestApprovers{
    ActionType: tea.String("AND"),
    UserIds: []*string{tea.String("26652461xxxx5992")},
  }
  startProcessInstanceRequest := &dingtalkworkflow_1_0.StartProcessInstanceRequest{
    BizDetailPageUrl: tea.String("https://www.dingtalk.com"),
    OriginatorUserId: tea.String("manager432"),
    ProcessCode: tea.String("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1"),
    DeptId: tea.Int64(1),
    MicroappAgentId: tea.Int64(41605932),
    Approvers: []*dingtalkworkflow_1_0.StartProcessInstanceRequestApprovers{approvers0},
    CcList: []*string{tea.String("26652461xxxx5992")},
    CcPosition: tea.String("START"),
    TargetSelectActioners: []*dingtalkworkflow_1_0.StartProcessInstanceRequestTargetSelectActioners{targetSelectActioners0},
    FormComponentValues: []*dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValues{formComponentValues0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.StartProcessInstanceWithOptions(startProcessInstanceRequest, startProcessInstanceHeaders, &util.RuntimeOptions{})
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
    let startProcessInstanceHeaders = new dingtalkworkflow_1_0.StartProcessInstanceHeaders({ });
    startProcessInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let formComponentValues0Details0Details0 = new dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValuesDetailsDetails({
      id: 'PhoneField_IZI2LP8QF6O0',
      bizAlias: 'Phone',
      name: 'PhoneField',
      value: '123xxxxxxxx',
      extValue: '总个数:1',
      componentType: 'PhoneField',
    });
    let formComponentValues0Details0 = new dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValuesDetails({
      id: 'PhoneField_IZI2LP8QF6O0',
      bizAlias: 'Phone',
      name: 'PhoneField',
      value: '123xxxxxxxx',
      extValue: '总个数:1',
      details: [
        formComponentValues0Details0Details0
      ],
    });
    let formComponentValues0 = new dingtalkworkflow_1_0.StartProcessInstanceRequestFormComponentValues({
      id: 'PhoneField_IZI2LP8QF6O0',
      bizAlias: 'myPhoneNumber',
      name: 'PhoneField',
      value: '123xxxxxxxx',
      extValue: '总个数:1',
      componentType: 'PhoneField',
      details: [
        formComponentValues0Details0
      ],
    });
    let targetSelectActioners0 = new dingtalkworkflow_1_0.StartProcessInstanceRequestTargetSelectActioners({
      actionerKey: 'manual_1918_5cd3_xxxx_6a98',
      actionerUserIds: [
        '26652461xxxx5992'
      ],
    });
    let approvers0 = new dingtalkworkflow_1_0.StartProcessInstanceRequestApprovers({
      actionType: 'AND',
      userIds: [
        '26652461xxxx5992'
      ],
    });
    let startProcessInstanceRequest = new dingtalkworkflow_1_0.StartProcessInstanceRequest({
      bizDetailPageUrl: 'https://www.dingtalk.com',
      originatorUserId: 'manager432',
      processCode: 'PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
      deptId: 1,
      microappAgentId: 41605932,
      approvers: [
        approvers0
      ],
      ccList: [
        '26652461xxxx5992'
      ],
      ccPosition: 'START',
      targetSelectActioners: [
        targetSelectActioners0
      ],
      formComponentValues: [
        formComponentValues0
      ],
    });
    try {
      await client.startProcessInstanceWithOptions(startProcessInstanceRequest, startProcessInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceHeaders startProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceHeaders();
            startProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues.StartProcessInstanceRequestFormComponentValuesDetails.StartProcessInstanceRequestFormComponentValuesDetailsDetails formComponentValues0Details0Details0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues.StartProcessInstanceRequestFormComponentValuesDetails.StartProcessInstanceRequestFormComponentValuesDetailsDetails
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                ComponentType = "PhoneField",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues.StartProcessInstanceRequestFormComponentValuesDetails formComponentValues0Details0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues.StartProcessInstanceRequestFormComponentValuesDetails
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                Details = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues.StartProcessInstanceRequestFormComponentValuesDetails.StartProcessInstanceRequestFormComponentValuesDetailsDetails>
                {
                    formComponentValues0Details0Details0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues formComponentValues0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "myPhoneNumber",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                ComponentType = "PhoneField",
                Details = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues.StartProcessInstanceRequestFormComponentValuesDetails>
                {
                    formComponentValues0Details0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestTargetSelectActioners targetSelectActioners0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestTargetSelectActioners
            {
                ActionerKey = "manual_1918_5cd3_xxxx_6a98",
                ActionerUserIds = new List<string>
                {
                    "26652461xxxx5992"
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestApprovers approvers0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestApprovers
            {
                ActionType = "AND",
                UserIds = new List<string>
                {
                    "26652461xxxx5992"
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest startProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest
            {
                BizDetailPageUrl = "https://www.dingtalk.com",
                OriginatorUserId = "manager432",
                ProcessCode = "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
                DeptId = 1,
                MicroappAgentId = 41605932,
                Approvers = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestApprovers>
                {
                    approvers0
                },
                CcList = new List<string>
                {
                    "26652461xxxx5992"
                },
                CcPosition = "START",
                TargetSelectActioners = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestTargetSelectActioners>
                {
                    targetSelectActioners0
                },
                FormComponentValues = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.StartProcessInstanceRequest.StartProcessInstanceRequestFormComponentValues>
                {
                    formComponentValues0
                },
            };
            try
            {
                client.StartProcessInstanceWithOptions(startProcessInstanceRequest, startProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| instanceId | String | 审批实例id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "instanceId" : "91ef1076-c3ed-4a78-xxxx-fa29ef2d6252"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | targetSelectApproverScopeError | 自选审批人不在规定范围内 | 自选审批人不在规定范围内 |
| 400 | targetSelectApproverMissing | 自选审批人缺失 | 自选审批人缺失 |
| 400 | invalidParameter | 发起审批参数错误。具体可能为：企业ID、审批模板code等参数错误，或发起人已离职 | 发起审批参数错误。具体可能为：企业ID、审批模板code等参数错误，或发起人已离职 |
| 400 | processInstanceInvalidParameter | 审批实例参数错误，具体可能为:发起人、审批人、抄送人的userid错误，发起部门id错误，发起人不在发起部门中 | 审批实例参数错误，具体可能为:发起人、审批人、抄送人的userid错误，发起部门id错误，发起人不在发起部门中 |
| 400 | processInstanceStartFailed | 创建审批实例失败 | 创建审批实例失败 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | processGroupGetFailed | 获取审批流分组失败 | 获取审批流分组失败 |
| 400 | processCodeError | 获取审批模板失败或者模板已被删除 | 获取审批模板失败或者模板已被删除 |
| 400 | processSetupNoPermission | 无操作审批流的权限 | 无操作审批流的权限 |
| 400 | processGetFailed | 获取审批流失败或审批单状态为非启用状态 | 获取审批流失败或审批单状态为非启用状态 |
| 400 | formConverterError | 表单数据校验失败，失败控件：%s | 表单数据校验失败 |
| 400 | illegalComponent | 表单组件入参错误 | 表单组件入参错误 |
| 400 | sysErrror | 创建审批实例系统异常 | 创建审批实例系统异常 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | autoflowLikeTriggerRateLimited | 该操作涉及自动化类业务(业务规则)并且触发限速, 请降速调用或取消相关自动化类业务配置 | 该操作涉及自动化类业务(业务规则)并且触发限速, 请降速调用或取消相关自动化类业务配置 |
| 400 | benefitStatusInvalid | 权益校验失败。指定bizDetailPageUrl为OA高级版专享功能，请开通高级版后再重试。 | 权益校验失败。指定bizDetailPageUrl为OA高级版专享功能，请开通高级版后再重试。 |
| 500 | systemError | 系统异常 | 系统异常 |
