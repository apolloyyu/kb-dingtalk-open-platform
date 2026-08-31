---
title: "获取审批单流程中的节点信息"
source_url: "https://open.dingtalk.com/document/development/approval-process-prediction"
namespace: "development"
slug: "approval-process-prediction"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批表单 > 获取审批单流程中的节点信息"
doc_id: "4VxVQgHOVU"
updated_at: "2026-06-03 10:12:22"
---

> Source: https://open.dingtalk.com/document/development/approval-process-prediction
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批表单 > 获取审批单流程中的节点信息
> Updated: 2026-06-03 10:12:22

# 获取审批单流程中的节点信息

调用本接口，获取审批单流程中的节点信息。

## **接口调用说明**

### 调用说明

调用本接口，可获取到节点的以下信息：

- 自选节点，可以获取节点名称、审批类型、设置审批人信息、选择范围、多人审批时采用的审批方式、节点激活类型等。
- 非自选节点，可以获取节点名称、审批类型、设置审批人信息、多人审批时采用的审批方式、节点激活类型等。

  ![](https://img.alicdn.com/imgextra/i1/O1CN01LpxV4b1f6M20NzZNY_!!6000000003957-2-tps-1916-950.png)

### 使用场景

1. 用于判断是否有自选节点，和[发起审批实例](0497-create-an-approval-instance.md)接口配合使用。

   > **[!NOTE]**
   >
   > 仅适用于调用**发起审批实例**接口时，不指定审批流程，复用审批后台设置的审批流程情况。

   ![](https://img.alicdn.com/imgextra/i1/O1CN01JClTWm1lU4EXAZn3f_!!6000000004821-2-tps-1906-920.png)
2. 企业希望获取某审批模板设置的节点信息，如获取节点类型、节点名称等。

### 是否有自选节点

#### 有自选节点

调用本文接口，返回信息中存在`activityType`字段值为`target_select`的节点。

在和**发起审批实例**接口配合使用时，需注意以下：

- 将当前节点内的`actorKey`字段值作为发起审批接口的actionerKey参数。
- `actorSelectionRange`内的`workNo`字段值做为发起审批实例接口的`actionerUserIds`参数。

  ![](https://img.alicdn.com/imgextra/i2/O1CN010b2wGy1QuzaU1MHJb_!!6000000002037-2-tps-1904-916.png)

#### 无自选节点

调用本文接口，返回信息中不存在`activityType`字段值为`target_approval`的节点。

![](https://img.alicdn.com/imgextra/i4/O1CN01t0X30U28ZJwNFoWOa_!!6000000007946-2-tps-1896-918.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/forecast |
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
| processCode | String | 是 | 审批流的唯一码，调用[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口或[OA审批概述-名词解释](0473-workflow-overview.md)获取。 |
| deptId | Integer | 是 | 即将发起审批单的员工所在部门ID，可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)接口获取。 |
| userId | String | 是 | 即将发起审批单的员工userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| formComponentValues | Array | 是 | 表单控件数据列表，最多长度150。 |
| id | String | 否 | 控件id。 |
| bizAlias | String | 否 | 控件别名。 |
| name | String | 是 | 控件名称。 |
| value | String | 是 | 控件值。 |
| extValue | String | 否 | 控件扩展值。 |
| componentType | String | 否 | 控件类型，取值：   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件 - **PhoneField**：电话控件 - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件 - **RelateField**：关联审批单 - **FormRelateField**：关联控件 |
| details | Array | 否 | 子控件列表，最大列表长度150。 |
| id | String | 否 | 控件id。 |
| bizAlias | String | 否 | 控件别名。 |
| name | String | 否 | 控件名称。 |
| value | String | 否 | 控件值。 |
| extValue | String | 否 | 控件扩展值。 |
| details | Array | 否 | 子控件列表，最大列表长度150。 |
| id | String | 否 | 控件id。 |
| bizAlias | String | 否 | 控件别名。 |
| name | String | 否 | 控件名称。 |
| value | String | 否 | 控件值。 |
| extValue | String | 否 | 控件扩展值。 |
| componentType | String | 否 | 控件类型，取值：   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框 - **DDMultiSelectField**：多选框 - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件 - **PhoneField**：电话控件 - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件 - **RelateField**：关联审批单 - **FormRelateField**：关联控件 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processes/forecast HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:ea96fed0eda0325e8b30f182805f5f4e
Content-Type:application/json

{ 
    /*
      该接口当前尚未支持审批应用中的所有控件，以以下列出示例的控件为准。
      基本的控件数据在传递时只需要填写 name 和 value 属性即可，两者都是字符串格式。
      如果数据是 json 格式，也需要先转义为字符串格式。
    */ 
    "userId": "26652461xxxx5992",
    "deptId": 1,
    "processCode": "PROC-17428B8C-6C60-xxxx-924C-64F1037AE067",
    "formComponentValues": [
        {
          "name": "单行输入框",
          "value": "单行输入框示例"
        },
        {
          "name": "多行输入框",
          "value": "多行输入框示例"
        },
        {
          "name": "数字输入框",
          "value": "100"
        },
        {
          /*
            value 可以直接填写实际的选项值
          */
          "name": "单选框",
          "value": "选项1"
        },
        {
          /*
            value 需要将实际的选项值组成的数组转义为字符串，即使只有一个
            选项也需要是数组形式
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
          "name": "身份证",
          "value": "xxxx"
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
          "value": "[[{\"id\":\"TextField_CM2IN2SOB600\", \"value\":\"hello\"}, {\"id\":\"TextField_QQOAK1OA2G00\", \"value\":\"world\"}]]"
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
          "name": "联系人",
          "value": "[\"4525xxxxxxxx77041\"]"
        },
        {
          /*
            value 需要将实际的审批单组成的数组转义为字符串，即使只有一个
            选项也需要是数组形式
          */
          "name": "关联审批单",
          "value": "[\"fa2aa864-xxxx-xxxx-xxxx-75572c0e2cdf\", \"7125778e-xxxx-xxxx-xxxx-faa987478a9b\"]"
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
        ProcessForecastHeaders processForecastHeaders = new ProcessForecastHeaders();
        processForecastHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ProcessForecastRequest.ProcessForecastRequestFormComponentValuesDetailsDetails formComponentValues0Details0Details0 = new ProcessForecastRequest.ProcessForecastRequestFormComponentValuesDetailsDetails()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setComponentType("TextField");
        ProcessForecastRequest.ProcessForecastRequestFormComponentValuesDetails formComponentValues0Details0 = new ProcessForecastRequest.ProcessForecastRequestFormComponentValuesDetails()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setDetails(java.util.Arrays.asList(
                    formComponentValues0Details0Details0
                ));
        ProcessForecastRequest.ProcessForecastRequestFormComponentValues formComponentValues0 = new ProcessForecastRequest.ProcessForecastRequestFormComponentValues()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setComponentType("TextField")
                .setDetails(java.util.Arrays.asList(
                    formComponentValues0Details0
                ));
        ProcessForecastRequest processForecastRequest = new ProcessForecastRequest()
                .setProcessCode("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1")
                .setDeptId(1)
                .setUserId("manager432")
                .setFormComponentValues(java.util.Arrays.asList(
                    formComponentValues0
                ));
        try {
            client.processForecastWithOptions(processForecastRequest, processForecastHeaders, new RuntimeOptions());
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
        process_forecast_headers = dingtalkworkflow__1__0_models.ProcessForecastHeaders()
        process_forecast_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_component_values_0details_0details_0 = dingtalkworkflow__1__0_models.ProcessForecastRequestFormComponentValuesDetailsDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='TextField'
        )
        form_component_values_0details_0 = dingtalkworkflow__1__0_models.ProcessForecastRequestFormComponentValuesDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            details=[
                form_component_values_0details_0details_0
            ]
        )
        form_component_values_0 = dingtalkworkflow__1__0_models.ProcessForecastRequestFormComponentValues(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='TextField',
            details=[
                form_component_values_0details_0
            ]
        )
        process_forecast_request = dingtalkworkflow__1__0_models.ProcessForecastRequest(
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            dept_id=1,
            user_id='manager432',
            form_component_values=[
                form_component_values_0
            ]
        )
        try:
            client.process_forecast_with_options(process_forecast_request, process_forecast_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        process_forecast_headers = dingtalkworkflow__1__0_models.ProcessForecastHeaders()
        process_forecast_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_component_values_0details_0details_0 = dingtalkworkflow__1__0_models.ProcessForecastRequestFormComponentValuesDetailsDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='TextField'
        )
        form_component_values_0details_0 = dingtalkworkflow__1__0_models.ProcessForecastRequestFormComponentValuesDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            details=[
                form_component_values_0details_0details_0
            ]
        )
        form_component_values_0 = dingtalkworkflow__1__0_models.ProcessForecastRequestFormComponentValues(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='TextField',
            details=[
                form_component_values_0details_0
            ]
        )
        process_forecast_request = dingtalkworkflow__1__0_models.ProcessForecastRequest(
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            dept_id=1,
            user_id='manager432',
            form_component_values=[
                form_component_values_0
            ]
        )
        try:
            await client.process_forecast_with_options_async(process_forecast_request, process_forecast_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ProcessForecastHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ProcessForecastRequest\formComponentValues\details\details;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ProcessForecastRequest\formComponentValues;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ProcessForecastRequest;
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
        $processForecastHeaders = new ProcessForecastHeaders([]);
        $processForecastHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $formComponentValues0Details0Details0 = new details([
            "id" => "PhoneField_IZI2LP8QF6O0",
            "bizAlias" => "Phone",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "componentType" => "TextField"
        ]);
        $formComponentValues0Details0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ProcessForecastRequest\formComponentValues\details([
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
            "bizAlias" => "Phone",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "componentType" => "TextField",
            "details" => [
                $formComponentValues0Details0
            ]
        ]);
        $processForecastRequest = new ProcessForecastRequest([
            "processCode" => "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
            "deptId" => 1,
            "userId" => "manager432",
            "formComponentValues" => [
                $formComponentValues0
            ]
        ]);
        try {
            $client->processForecastWithOptions($processForecastRequest, $processForecastHeaders, new RuntimeOptions([]));
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

  processForecastHeaders := &dingtalkworkflow_1_0.ProcessForecastHeaders{}
  processForecastHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  formComponentValues0Details0Details0 := &dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValuesDetailsDetails{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    ComponentType: tea.String("TextField"),
  }
  formComponentValues0Details0 := &dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValuesDetails{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    Details: []*dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValuesDetailsDetails{formComponentValues0Details0Details0},
  }
  formComponentValues0 := &dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValues{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    ComponentType: tea.String("TextField"),
    Details: []*dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValuesDetails{formComponentValues0Details0},
  }
  processForecastRequest := &dingtalkworkflow_1_0.ProcessForecastRequest{
    ProcessCode: tea.String("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1"),
    DeptId: tea.Int32(1),
    UserId: tea.String("manager432"),
    FormComponentValues: []*dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValues{formComponentValues0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ProcessForecastWithOptions(processForecastRequest, processForecastHeaders, &util.RuntimeOptions{})
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
    let processForecastHeaders = new $dingtalkworkflow_1_0.ProcessForecastHeaders({ });
    processForecastHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let formComponentValues0Details0Details0 = new $dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValuesDetailsDetails({
      id: "PhoneField_IZI2LP8QF6O0",
      bizAlias: "Phone",
      name: "PhoneField",
      value: "123xxxxxxxx",
      extValue: "总个数:1",
      componentType: "TextField",
    });
    let formComponentValues0Details0 = new $dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValuesDetails({
      id: "PhoneField_IZI2LP8QF6O0",
      bizAlias: "Phone",
      name: "PhoneField",
      value: "123xxxxxxxx",
      extValue: "总个数:1",
      details: [
        formComponentValues0Details0Details0
      ],
    });
    let formComponentValues0 = new $dingtalkworkflow_1_0.ProcessForecastRequestFormComponentValues({
      id: "PhoneField_IZI2LP8QF6O0",
      bizAlias: "Phone",
      name: "PhoneField",
      value: "123xxxxxxxx",
      extValue: "总个数:1",
      componentType: "TextField",
      details: [
        formComponentValues0Details0
      ],
    });
    let processForecastRequest = new $dingtalkworkflow_1_0.ProcessForecastRequest({
      processCode: "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
      deptId: 1,
      userId: "manager432",
      formComponentValues: [
        formComponentValues0
      ],
    });
    try {
      await client.processForecastWithOptions(processForecastRequest, processForecastHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastHeaders processForecastHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastHeaders();
            processForecastHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues.ProcessForecastRequestFormComponentValuesDetails.ProcessForecastRequestFormComponentValuesDetailsDetails formComponentValues0Details0Details0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues.ProcessForecastRequestFormComponentValuesDetails.ProcessForecastRequestFormComponentValuesDetailsDetails
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                ComponentType = "TextField",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues.ProcessForecastRequestFormComponentValuesDetails formComponentValues0Details0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues.ProcessForecastRequestFormComponentValuesDetails
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                Details = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues.ProcessForecastRequestFormComponentValuesDetails.ProcessForecastRequestFormComponentValuesDetailsDetails>
                {
                    formComponentValues0Details0Details0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues formComponentValues0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                ComponentType = "TextField",
                Details = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues.ProcessForecastRequestFormComponentValuesDetails>
                {
                    formComponentValues0Details0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest processForecastRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest
            {
                ProcessCode = "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
                DeptId = 1,
                UserId = "manager432",
                FormComponentValues = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ProcessForecastRequest.ProcessForecastRequestFormComponentValues>
                {
                    formComponentValues0
                },
            };
            try
            {
                client.ProcessForecastWithOptions(processForecastRequest, processForecastHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastHeaders> processForecastHeaders = make_shared<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastHeaders>();
  processForecastHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValuesDetailsDetails> formComponentValues0Details0Details0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValuesDetailsDetails>(map<string, boost::any>({
    {"id", boost::any(string("PhoneField_IZI2LP8QF6O0"))},
    {"bizAlias", boost::any(string("Phone"))},
    {"name", boost::any(string("PhoneField"))},
    {"value", boost::any(string("123xxxxxxxx"))},
    {"extValue", boost::any(string("总个数:1"))},
    {"componentType", boost::any(string("TextField"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValuesDetails> formComponentValues0Details0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValuesDetails>(map<string, boost::any>({
    {"id", boost::any(string("PhoneField_IZI2LP8QF6O0"))},
    {"bizAlias", boost::any(string("Phone"))},
    {"name", boost::any(string("PhoneField"))},
    {"value", boost::any(string("123xxxxxxxx"))},
    {"extValue", boost::any(string("总个数:1"))},
    {"details", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValuesDetailsDetails>({
      formComponentValues0Details0Details0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValues> formComponentValues0 = make_shared<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValues>(map<string, boost::any>({
    {"id", boost::any(string("PhoneField_IZI2LP8QF6O0"))},
    {"bizAlias", boost::any(string("Phone"))},
    {"name", boost::any(string("PhoneField"))},
    {"value", boost::any(string("123xxxxxxxx"))},
    {"extValue", boost::any(string("总个数:1"))},
    {"componentType", boost::any(string("TextField"))},
    {"details", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValuesDetails>({
      formComponentValues0Details0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequest> processForecastRequest = make_shared<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequest>(map<string, boost::any>({
    {"processCode", boost::any(string("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1"))},
    {"deptId", boost::any(1)},
    {"userId", boost::any(string("manager432"))},
    {"formComponentValues", boost::any(vector<Alibabacloud_Dingtalkworkflow_1_0::ProcessForecastRequestFormComponentValues>({
      formComponentValues0
    }))}
  }));
  try {
    client->processForecastWithOptions(processForecastRequest, processForecastHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Object | 返回结果详情。 |
| isForecastSuccess | Boolean | 是否预测成功，成功返回true。 |
| processCode | String | 表单的唯一码。 |
| userId | String | 用户id。 |
| processId | Long | 流程ID，暂无使用场景。 |
| isStaticWorkflow | Boolean | 是否静态流程。   - **true**： - **false**： |
| workflowActivityRules | Array | 工作流节点规则。 |
| activityId | String | 节点ID，暂无使用场景。 |
| prevActivityId | String | 流程中前一个节点的 id。 |
| activityName | String | 节点名称。 |
| activityType | String | 规则类型，取值：   - **target\_select**：自选审批人节点 - **target\_approval**：指定审批人节点 |
| isTargetSelect | Boolean | 是否为自选审批节点。  activityType 值为target\_select时，该字段值为true。 |
| workflowActor | Object | 节点操作人信息。 |
| actorKey | String | 节点操作人 key。 |
| actorType | String | 节点操作人类型，取值：   - **approver**：审批人 - **notifier**：抄送人 - **audit**：办理人 |
| actorSelectionType | String | 节点操作人选择范围类型，取值：   - **allStaff**：全公司 - **approvals**：指定成员 - **labels**：角色 |
| actorSelectionRange | Object | 节点操作人选择范围。 |
| approvals | Array | 审批指定成员，节点设置方式如下图，会返回该字段。 |
| workNo | String | 员工 userId。 |
| userName | String | 员工姓名。 |
| labels | Array | 审批指定角色，节点设置如下图，会返回该字段。 |
| labels | String | 角色 id。 |
| labelNames | String | 角色名字。 |
| allowedMulti | Boolean | 是否允许多选，还是仅允许选一人。 |
| approvalType | String | 节点审批类型，取值：   - MANUAL：人工审批 - AUTO\_AGREE：自动通过 - AUTO\_REFUSE：自动拒绝 |
| approvalMethod | String | 节点审批方式，取值：   - ONE\_BY\_ONE：依次审批 - AND：会签审批 - OR：或签审批 |
| actorActivateType | String | 节点激活类型，取值：   - ALL：并行 - ONE\_BY\_ONE：串行 |
| required | Boolean | 该审批人节点在发起审批时是否必填。 |
| activityActioners | Array | 节点审批人列表。 |
| userId | String | 审批人userId。 |
| name | String | 审批人名称。 |
| avatar | String | 审批人头像。 |
| workflowForecastNodes | Array | 工作流节点流。 |
| activityId | String | 节点 id。 |
| outId | String | 节点出线 id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "isForecastSuccess" : true,
    "processCode" : "PROC-2B60E506-D6CB-43F3-B661-359B27F90947",
    "userId" : "2665246100805992",
    "processId" : 63657309999,
    "isStaticWorkflow" : true,
    "workflowActivityRules" : [ {
      "activityId" : "1918_5cd3",
      "prevActivityId" : "1918_5cd3",
      "activityName" : "审批人",
      "activityType" : "target_select",
      "isTargetSelect" : true,
      "workflowActor" : {
        "actorKey" : "manual_e203_14a3_895a_45ad",
        "actorType" : "approver:审批人，notifier:抄送人，audit：办理人",
        "actorSelectionType" : "allStaff",
        "actorSelectionRange" : {
          "approvals" : [ {
            "workNo" : "26652461xxxx5992",
            "userName" : "张三"
          } ],
          "labels" : [ {
            "labels" : "200649095",
            "labelNames" : "财务"
          } ]
        },
        "allowedMulti" : true,
        "approvalType" : "MANUAL",
        "approvalMethod" : "ONE_BY_ONE",
        "actorActivateType" : "ALL",
        "required" : true
      },
      "activityActioners" : [ {
        "userId" : "2665246100805992",
        "name" : "钉三多",
        "avatar" : "https://url1"
      } ]
    } ],
    "workflowForecastNodes" : [ {
      "activityId" : "1cc3_959a",
      "outId" : "line-random-1cc3_959a-831a_607b"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | forecastError | 流程预测失败 | 流程预测失败 |
| 400 | invalidParameter | 参数错误 | 参数错误 |
| 400 | componentIsNull | 表单数据为空 | 表单数据为空 |
| 400 | processCodeError | 获取审批模板失败或模板已删除 | 获取审批模板失败或模板已删除 |
| 400 | formNotExist | 表单不存在 | 表单不存在 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | invalidUserId | 用户userId为空 | 用户userId为空 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 500 | systemError | 系统异常 | 系统异常 |
