---
title: "获取员工花名册字段信息"
source_url: "https://open.dingtalk.com/document/development/api-getemployeerosterbyfield"
namespace: "development"
slug: "api-getemployeerosterbyfield"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 花名册 > 获取员工花名册字段信息"
doc_id: "G5IPODq9XG"
updated_at: "2026-06-04 19:10:24"
---

> Source: https://open.dingtalk.com/document/development/api-getemployeerosterbyfield
> Path: 应用开发 / 服务端 API / 智能人事 > 花名册 > 获取员工花名册字段信息
> Updated: 2026-06-04 19:10:24

# 获取员工花名册字段信息

调用本接口，查询员工花名册指定字段的信息，支持明细分组字段。

## 接口调用说明

花名册中的附件信息（如员工照片、身份证正面、反面等）不支持通过接口下载。如需获取请用户前往钉钉客户端，可以在花名册下载或者导出附件。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/rosters/lists/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIdList | Array of String | 是 | 员工的 userId 列表，多个 userId 之间使用英文逗号分隔，一次最多支持传100个值。 |
| fieldFilterList | Array of String | 否 | 需要获取的花名册字段field\_code值列表，多个字段之间使用逗号分隔，一次最多支持传100个值。       - 该参数不传时，获取全部字段信息。 - 查询字段越少，RT越低，建议按需查询。      - 企业内部应用：    - 查看[花名册自定义字段业务code](0943-roster-custom-field-business-code.md)中field\_code字段。   - 调用获取[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取field\_code参数值。 - 第三方企业应用，调用[查询花名册中有权限的字段列表](0942-query-the-list-of-fields-with-permissions-in-the-roster.md)接口获取field\_code参数值。 |
| appAgentId | Long | 是 | 应用的AgentId，详情参考[AgentId](https://open.dingtalk.com/document/development/basic-concepts-beta#884d363067bnq)。 |
| text2SelectConvert | Boolean | 否 | 文本转选项字段处理标识。   - 如果设置为false，岗位职级字段的 label 和 value 返回的都是名称，例如 :  ``` {                     "fieldName": "岗位职级",                     "fieldCode": "sys01-positionLevel",                     "groupId": "sys01",                     "fieldValueList": [                         {                             "itemIndex": 0,                             "label": "test",                             "value": "test"                         }                     ]          } ```  - 如果设置为true，岗位职级字段的 label 返回的名称，value返回的对应id，例如：  ``` {                     "fieldName": "岗位职级",                     "fieldCode": "sys01-positionLevel",                     "groupId": "sys01",                     "fieldValueList": [                         {                             "itemIndex": 0,                             "label": "test",                             "value": "10007"                         }                     ]          } ``` |

### 请求示例

HTTP

```
POST /v1.0/hrm/rosters/lists/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:af21xxx
Content-Type:application/json

{
  "userIdList" : [ "userId123" ],
  "fieldFilterList" : [ "sys01-positionLevel" ],
  "appAgentId" : 1185599675,
  "text2SelectConvert" : true
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.GetEmployeeRosterByFieldHeaders getEmployeeRosterByFieldHeaders = new com.aliyun.dingtalkhrm_1_0.models.GetEmployeeRosterByFieldHeaders();
        getEmployeeRosterByFieldHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.GetEmployeeRosterByFieldRequest getEmployeeRosterByFieldRequest = new com.aliyun.dingtalkhrm_1_0.models.GetEmployeeRosterByFieldRequest()
                .setUserIdList(java.util.Arrays.asList(
                    "userId123"
                ))
                .setFieldFilterList(java.util.Arrays.asList(
                    "sys01-positionLevel"
                ))
                .setAppAgentId(1185599675L)
                .setText2SelectConvert(true);
        try {
            client.getEmployeeRosterByFieldWithOptions(getEmployeeRosterByFieldRequest, getEmployeeRosterByFieldHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrm_1_0.client import Client as dingtalkhrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_employee_roster_by_field_headers = dingtalkhrm__1__0_models.GetEmployeeRosterByFieldHeaders()
        get_employee_roster_by_field_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_employee_roster_by_field_request = dingtalkhrm__1__0_models.GetEmployeeRosterByFieldRequest(
            user_id_list=[
                'userId123'
            ],
            field_filter_list=[
                'sys01-positionLevel'
            ],
            app_agent_id=1185599675,
            text_2select_convert=True
        )
        try:
            client.get_employee_roster_by_field_with_options(get_employee_roster_by_field_request, get_employee_roster_by_field_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_employee_roster_by_field_headers = dingtalkhrm__1__0_models.GetEmployeeRosterByFieldHeaders()
        get_employee_roster_by_field_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_employee_roster_by_field_request = dingtalkhrm__1__0_models.GetEmployeeRosterByFieldRequest(
            user_id_list=[
                'userId123'
            ],
            field_filter_list=[
                'sys01-positionLevel'
            ],
            app_agent_id=1185599675,
            text_2select_convert=True
        )
        try:
            await client.get_employee_roster_by_field_with_options_async(get_employee_roster_by_field_request, get_employee_roster_by_field_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\GetEmployeeRosterByFieldHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\GetEmployeeRosterByFieldRequest;
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
        $getEmployeeRosterByFieldHeaders = new GetEmployeeRosterByFieldHeaders([]);
        $getEmployeeRosterByFieldHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getEmployeeRosterByFieldRequest = new GetEmployeeRosterByFieldRequest([
            "userIdList" => [
                "userId123"
            ],
            "fieldFilterList" => [
                "sys01-positionLevel"
            ],
            "appAgentId" => 1185599675,
            "text2SelectConvert" => true
        ]);
        try {
            $client->getEmployeeRosterByFieldWithOptions($getEmployeeRosterByFieldRequest, $getEmployeeRosterByFieldHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
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
func CreateClient () (_result *dingtalkhrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrm_1_0.Client{}
  _result, _err = dingtalkhrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getEmployeeRosterByFieldHeaders := &dingtalkhrm_1_0.GetEmployeeRosterByFieldHeaders{}
  getEmployeeRosterByFieldHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getEmployeeRosterByFieldRequest := &dingtalkhrm_1_0.GetEmployeeRosterByFieldRequest{
    UserIdList: []*string{tea.String("userId123")},
    FieldFilterList: []*string{tea.String("sys01-positionLevel")},
    AppAgentId: tea.Int64(1185599675),
    Text2SelectConvert: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetEmployeeRosterByFieldWithOptions(getEmployeeRosterByFieldRequest, getEmployeeRosterByFieldHeaders, &util.RuntimeOptions{})
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
const dingtalkhrm_1_0 = require('@alicloud/dingtalk/hrm_1_0');
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
    return new dingtalkhrm_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getEmployeeRosterByFieldHeaders = new dingtalkhrm_1_0.GetEmployeeRosterByFieldHeaders({ });
    getEmployeeRosterByFieldHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getEmployeeRosterByFieldRequest = new dingtalkhrm_1_0.GetEmployeeRosterByFieldRequest({
      userIdList: [
        'userId123'
      ],
      fieldFilterList: [
        'sys01-positionLevel'
      ],
      appAgentId: 1185599675,
      text2SelectConvert: true,
    });
    try {
      await client.getEmployeeRosterByFieldWithOptions(getEmployeeRosterByFieldRequest, getEmployeeRosterByFieldHeaders, new Util.RuntimeOptions({ }));
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkhrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.GetEmployeeRosterByFieldHeaders getEmployeeRosterByFieldHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.GetEmployeeRosterByFieldHeaders();
            getEmployeeRosterByFieldHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.GetEmployeeRosterByFieldRequest getEmployeeRosterByFieldRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.GetEmployeeRosterByFieldRequest
            {
                UserIdList = new List<string>
                {
                    "userId123"
                },
                FieldFilterList = new List<string>
                {
                    "sys01-positionLevel"
                },
                AppAgentId = 1185599675,
                Text2SelectConvert = true,
            };
            try
            {
                client.GetEmployeeRosterByFieldWithOptions(getEmployeeRosterByFieldRequest, getEmployeeRosterByFieldHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 结果列表。 |
| corpId | String | 企业的corpId。 |
| userId | String | 员工的userId。 |
| unionId | String | 暂未开放。 |
| fieldDataList | Array | 返回的字段信息列表。 |
| fieldCode | String | 字段标识。 |
| fieldName | String | 字段名称。 |
| groupId | String | 分组标识。 |
| fieldValueList | Array | 字段值列表。       - 明细分组字段包含多条。 - 非明细分组仅一条记录。 |
| value | String | 字段取值，选项类型字段对应选项的key。 |
| label | String | 字段展示值，选项类型字段对应选项的value。 |
| itemIndex | Integer | 第几条的明细标识，下标从0开始。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "corpId" : "ding20a11xxx",
    "userId" : "042519",
    "unionId" : "无",
    "fieldDataList" : [ {
      "fieldCode" : "sys01-employeeStatus",
      "fieldName" : "员工名字",
      "groupId" : "sys01",
      "fieldValueList" : [ {
        "value" : "3",
        "label" : "正式",
        "itemIndex" : 0
      } ]
    } ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | invalidParameter | 系统参数无效或者传入的微应用Id和员工userId有误 | 系统参数无效或者微应用Id和员工userId传入有误 |
| 500 | systemError | 系统异常 | 系统异常 |
