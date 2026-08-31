---
title: "创建数据表单实例"
source_url: "https://open.dingtalk.com/document/development/api-createdatapremiumsaveforminstance"
namespace: "development"
slug: "api-createdatapremiumsaveforminstance"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 创建数据表单实例"
doc_id: "10BbxPsNVW"
updated_at: "2026-06-03 10:13:03"
---

> Source: https://open.dingtalk.com/document/development/api-createdatapremiumsaveforminstance
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 数据表单 > 表单实例 > 创建数据表单实例
> Updated: 2026-06-03 10:13:03

# 创建数据表单实例

调用本接口，创建数据表单实例。

## **接口调用说明**

- 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)
- 调用本接口创建数据表单实例，接口返回的实例ID请务必注意保存，方便后续调用其他接口使用。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/dataForms/formInstances/save |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| originatorUserId | String | 是 | 发起人的userId。 |
| processCode | String | 是 | 数据表单模板code。可在数据表单模板编辑页-基础设置-页面底部查看。 |
| formComponentValueList | Array | 是 | 表单控件列表。    具体请参照请求示例规范填写。 |
| id | String | 否 | 控件id |
| bizAlias | String | 否 | 控件别名 |
| name | String | 是 | 控件名称 |
| value | String | 是 | 控件值 |
| extValue | String | 否 | 控件扩展值 |
| componentType | String | 否 | 控件类型。详情请参考本文**FormComponent参数补充说明**。   - **TextField**：单行输入框 - **TextareaField**：多行输入框 - **NumberField**：数字输入框 - **DDSelectField**：单选框     选项值应当被配置在选项列表中   - **DDMultiSelectField**：多选框     选项值均应当被配置在选项列表中   - **DDDateField**：日期控件 - **DDDateRangeField**：时间区间控件 - **TextNote**：文字说明控件（审批模板上设置好的场景，不支持发起审批实例时修改） - **DDPhotoField**：图片控件 - **MoneyField**：金额控件 - **TableField**：明细控件 - **DDAttachment**：附件 - **InnerContactField**：联系人控件     联系人控件中的userID应当是当前组织下在职成员的userID   - **RelateField**：关联审批单     关联审批单传入的审批实例ID应当是当前组织下存在的审批实例ID   - **AddressField**：省市区控件 - **StarRatingField**：评分控件 - **DepartmentField**：部门控件     部门控件中应当传入当前组织下存在的部门ID |
| details | Array | 否 | 子控件列表，最大列表长度：150。 |
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
| componentType | String | 否 | 控件类型。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/dataForms/formInstances/save HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6dexxx
Content-Type:application/json

{
  "originatorUserId" : "manager432",
  "processCode" : "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
  "formComponentValueList" : [ {
    "id" : "TextField-abc",
    "bizAlias" : "abc",
    "name" : "文本框",
    "value" : "abc",
    "extValue" : "abc",
    "componentType" : "TextField",
    "details" : [ {
      "id" : "PhoneField_IZI2LP8QF6O0",
      "bizAlias" : "Phone",
      "name" : "PhoneField",
      "value" : "123xxxxxxxx",
      "extValue" : "总个数:1",
      "details" : [ {
        "id" : "PhoneField_IZI2LP8QF6O0",
        "bizAlias" : "Phone",
        "name" : "PhoneField",
        "value" : "123xxxxxxxx",
        "extValue" : "总个数:1",
        "componentType" : "PhoneField"
      } ]
    } ]
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
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceHeaders premiumSaveFormInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceHeaders();
        premiumSaveFormInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails formComponentValueList0Details0Details0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setComponentType("PhoneField");
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueListDetails formComponentValueList0Details0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueListDetails()
                .setId("PhoneField_IZI2LP8QF6O0")
                .setBizAlias("Phone")
                .setName("PhoneField")
                .setValue("123xxxxxxxx")
                .setExtValue("总个数:1")
                .setDetails(java.util.Arrays.asList(
                    formComponentValueList0Details0Details0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList formComponentValueList0 = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList()
                .setId("TextField-abc")
                .setBizAlias("abc")
                .setName("文本框")
                .setValue("abc")
                .setExtValue("abc")
                .setComponentType("TextField")
                .setDetails(java.util.Arrays.asList(
                    formComponentValueList0Details0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest premiumSaveFormInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumSaveFormInstanceRequest()
                .setOriginatorUserId("manager432")
                .setProcessCode("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1")
                .setFormComponentValueList(java.util.Arrays.asList(
                    formComponentValueList0
                ));
        try {
            client.premiumSaveFormInstanceWithOptions(premiumSaveFormInstanceRequest, premiumSaveFormInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        premium_save_form_instance_headers = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceHeaders()
        premium_save_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_component_value_list_0details_0details_0 = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='PhoneField'
        )
        form_component_value_list_0details_0 = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequestFormComponentValueListDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            details=[
                form_component_value_list_0details_0details_0
            ]
        )
        form_component_value_list_0 = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequestFormComponentValueList(
            id='TextField-abc',
            biz_alias='abc',
            name='文本框',
            value='abc',
            ext_value='abc',
            component_type='TextField',
            details=[
                form_component_value_list_0details_0
            ]
        )
        premium_save_form_instance_request = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequest(
            originator_user_id='manager432',
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            form_component_value_list=[
                form_component_value_list_0
            ]
        )
        try:
            client.premium_save_form_instance_with_options(premium_save_form_instance_request, premium_save_form_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_save_form_instance_headers = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceHeaders()
        premium_save_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        form_component_value_list_0details_0details_0 = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            component_type='PhoneField'
        )
        form_component_value_list_0details_0 = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequestFormComponentValueListDetails(
            id='PhoneField_IZI2LP8QF6O0',
            biz_alias='Phone',
            name='PhoneField',
            value='123xxxxxxxx',
            ext_value='总个数:1',
            details=[
                form_component_value_list_0details_0details_0
            ]
        )
        form_component_value_list_0 = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequestFormComponentValueList(
            id='TextField-abc',
            biz_alias='abc',
            name='文本框',
            value='abc',
            ext_value='abc',
            component_type='TextField',
            details=[
                form_component_value_list_0details_0
            ]
        )
        premium_save_form_instance_request = dingtalkworkflow__1__0_models.PremiumSaveFormInstanceRequest(
            originator_user_id='manager432',
            process_code='PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
            form_component_value_list=[
                form_component_value_list_0
            ]
        )
        try:
            await client.premium_save_form_instance_with_options_async(premium_save_form_instance_request, premium_save_form_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveFormInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveFormInstanceRequest\formComponentValueList\details\details;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveFormInstanceRequest\formComponentValueList;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveFormInstanceRequest;
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
        $premiumSaveFormInstanceHeaders = new PremiumSaveFormInstanceHeaders([]);
        $premiumSaveFormInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $formComponentValueList0Details0Details0 = new details([
            "id" => "PhoneField_IZI2LP8QF6O0",
            "bizAlias" => "Phone",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "componentType" => "PhoneField"
        ]);
        $formComponentValueList0Details0 = new \AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumSaveFormInstanceRequest\formComponentValueList\details([
            "id" => "PhoneField_IZI2LP8QF6O0",
            "bizAlias" => "Phone",
            "name" => "PhoneField",
            "value" => "123xxxxxxxx",
            "extValue" => "总个数:1",
            "details" => [
                $formComponentValueList0Details0Details0
            ]
        ]);
        $formComponentValueList0 = new formComponentValueList([
            "id" => "TextField-abc",
            "bizAlias" => "abc",
            "name" => "文本框",
            "value" => "abc",
            "extValue" => "abc",
            "componentType" => "TextField",
            "details" => [
                $formComponentValueList0Details0
            ]
        ]);
        $premiumSaveFormInstanceRequest = new PremiumSaveFormInstanceRequest([
            "originatorUserId" => "manager432",
            "processCode" => "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
            "formComponentValueList" => [
                $formComponentValueList0
            ]
        ]);
        try {
            $client->premiumSaveFormInstanceWithOptions($premiumSaveFormInstanceRequest, $premiumSaveFormInstanceHeaders, new RuntimeOptions([]));
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

  premiumSaveFormInstanceHeaders := &dingtalkworkflow_1_0.PremiumSaveFormInstanceHeaders{}
  premiumSaveFormInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  formComponentValueList0Details0Details0 := &dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    ComponentType: tea.String("PhoneField"),
  }
  formComponentValueList0Details0 := &dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueListDetails{
    Id: tea.String("PhoneField_IZI2LP8QF6O0"),
    BizAlias: tea.String("Phone"),
    Name: tea.String("PhoneField"),
    Value: tea.String("123xxxxxxxx"),
    ExtValue: tea.String("总个数:1"),
    Details: []*dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails{formComponentValueList0Details0Details0},
  }
  formComponentValueList0 := &dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueList{
    Id: tea.String("TextField-abc"),
    BizAlias: tea.String("abc"),
    Name: tea.String("文本框"),
    Value: tea.String("abc"),
    ExtValue: tea.String("abc"),
    ComponentType: tea.String("TextField"),
    Details: []*dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueListDetails{formComponentValueList0Details0},
  }
  premiumSaveFormInstanceRequest := &dingtalkworkflow_1_0.PremiumSaveFormInstanceRequest{
    OriginatorUserId: tea.String("manager432"),
    ProcessCode: tea.String("PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1"),
    FormComponentValueList: []*dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueList{formComponentValueList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumSaveFormInstanceWithOptions(premiumSaveFormInstanceRequest, premiumSaveFormInstanceHeaders, &util.RuntimeOptions{})
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
    let premiumSaveFormInstanceHeaders = new dingtalkworkflow_1_0.PremiumSaveFormInstanceHeaders({ });
    premiumSaveFormInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let formComponentValueList0Details0Details0 = new dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails({
      id: 'PhoneField_IZI2LP8QF6O0',
      bizAlias: 'Phone',
      name: 'PhoneField',
      value: '123xxxxxxxx',
      extValue: '总个数:1',
      componentType: 'PhoneField',
    });
    let formComponentValueList0Details0 = new dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueListDetails({
      id: 'PhoneField_IZI2LP8QF6O0',
      bizAlias: 'Phone',
      name: 'PhoneField',
      value: '123xxxxxxxx',
      extValue: '总个数:1',
      details: [
        formComponentValueList0Details0Details0
      ],
    });
    let formComponentValueList0 = new dingtalkworkflow_1_0.PremiumSaveFormInstanceRequestFormComponentValueList({
      id: 'TextField-abc',
      bizAlias: 'abc',
      name: '文本框',
      value: 'abc',
      extValue: 'abc',
      componentType: 'TextField',
      details: [
        formComponentValueList0Details0
      ],
    });
    let premiumSaveFormInstanceRequest = new dingtalkworkflow_1_0.PremiumSaveFormInstanceRequest({
      originatorUserId: 'manager432',
      processCode: 'PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1',
      formComponentValueList: [
        formComponentValueList0
      ],
    });
    try {
      await client.premiumSaveFormInstanceWithOptions(premiumSaveFormInstanceRequest, premiumSaveFormInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceHeaders premiumSaveFormInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceHeaders();
            premiumSaveFormInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList.PremiumSaveFormInstanceRequestFormComponentValueListDetails.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails formComponentValueList0Details0Details0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList.PremiumSaveFormInstanceRequestFormComponentValueListDetails.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                ComponentType = "PhoneField",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList.PremiumSaveFormInstanceRequestFormComponentValueListDetails formComponentValueList0Details0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList.PremiumSaveFormInstanceRequestFormComponentValueListDetails
            {
                Id = "PhoneField_IZI2LP8QF6O0",
                BizAlias = "Phone",
                Name = "PhoneField",
                Value = "123xxxxxxxx",
                ExtValue = "总个数:1",
                Details = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList.PremiumSaveFormInstanceRequestFormComponentValueListDetails.PremiumSaveFormInstanceRequestFormComponentValueListDetailsDetails>
                {
                    formComponentValueList0Details0Details0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList formComponentValueList0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList
            {
                Id = "TextField-abc",
                BizAlias = "abc",
                Name = "文本框",
                Value = "abc",
                ExtValue = "abc",
                ComponentType = "TextField",
                Details = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList.PremiumSaveFormInstanceRequestFormComponentValueListDetails>
                {
                    formComponentValueList0Details0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest premiumSaveFormInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest
            {
                OriginatorUserId = "manager432",
                ProcessCode = "PROC-EF6YJL35P2-SCKICSB7P750S0YISYKV3-xxxx-1",
                FormComponentValueList = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumSaveFormInstanceRequest.PremiumSaveFormInstanceRequestFormComponentValueList>
                {
                    formComponentValueList0
                },
            };
            try
            {
                client.PremiumSaveFormInstanceWithOptions(premiumSaveFormInstanceRequest, premiumSaveFormInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| instanceId | String | 数据表单实例ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "instanceId" : "91ef1076-c3ed-4a78-a7a5-fa29ef2d6252"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | permission.error | 没有访问权限 | 没有访问权限 |
| 400 | processcode.error | processCode对应的表单不存在 | processCode对应的表单不存在 |
| 400 | formschema.error | %s | 表单schema不合法 |
| 400 | formName.error | 已有相同名称表单 | 表单名称错误 |
| 400 | processes.error | 获取模板列表失败 | 获取模板列表失败 |
| 400 | needAuth | 没有发起审批的权限 | 没有发起审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | invalidSuiteKey | 无效的suiteKey | 无效的suiteKey |
| 400 | system.error | 表单扩展信息添加错误 | 添加process扩展属性错误 |
| 400 | user.not.exist | 用户不存在 | 用户不存在 |
| 500 | system.error | 系统错误 | 系统错误 |
| 500 | param.error | %s | 参数错误 |
| 500 | form.error | 参数错误，不是存表单 | 参数错误 |
| 500 | form.code.error | 表单详情查询失败 | 参数错误 |
| 500 | form.invalid | 模板被停用，联系管理员启用 | 模板被停用 |
| 500 | type.error | 表单类型错误 | 表单类型错误 |
| 500 | instance.error | 创建表单实例失败 | 创建表单实例失败 |
| 500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验失败，未开通或过期 |
| 500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 请求过于频繁，稍后重试 |
