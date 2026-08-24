---
title: "获取单条填表实例详情"
source_url: "https://open.dingtalk.com/document/development/obtains-the-instance-details-of-a-single-fill-table"
namespace: "development"
slug: "obtains-the-instance-details-of-a-single-fill-table"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能填表 > 获取单条填表实例详情"
doc_id: "DLJ4fwHEp4"
updated_at: "2026-06-04 19:10:38"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-instance-details-of-a-single-fill-table
> Path: 应用开发 / 服务端API / 智能填表 > 获取单条填表实例详情
> Updated: 2026-06-04 19:10:38

# 获取单条填表实例详情

调用本接口，根据某条回复数据的实例ID，获取该条回复实例内的表单详情信息，包括填表实例提交时间、表单实例提交者userId等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/swform/instances/{formInstanceId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_swapp\_collection\_read-智能填表数据读取权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| formInstanceId | String | 是 | 填表实例ID，调用[获取填表实例列表](0971-obtain-the-table-filling-instance-list-data.md)接口获取formInstanceId参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizType | Integer | 否 | 填表类型。   - **0**：表示通用填表 - **1**：表示教育版填表 |

### 请求示例

HTTP

```
GET /v1.0/swform/instances/11125769-fxxxx?bizType=0 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:Be3xxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkswform_1_0.*;
import com.aliyun.dingtalkswform_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkswform_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkswform_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkswform_1_0.Client client = Sample.createClient();
        GetFormInstanceHeaders getFormInstanceHeaders = new GetFormInstanceHeaders();
        getFormInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetFormInstanceRequest getFormInstanceRequest = new GetFormInstanceRequest()
                .setBizType(0);
        try {
            client.getFormInstanceWithOptions("11125769-fxxxx", getFormInstanceRequest, getFormInstanceHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.swform_1_0.client import Client as dingtalkswform_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.swform_1_0 import models as dingtalkswform__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkswform_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkswform_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_form_instance_headers = dingtalkswform__1__0_models.GetFormInstanceHeaders()
        get_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_form_instance_request = dingtalkswform__1__0_models.GetFormInstanceRequest(
            biz_type=0
        )
        try:
            client.get_form_instance_with_options('11125769-fxxxx', get_form_instance_request, get_form_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_form_instance_headers = dingtalkswform__1__0_models.GetFormInstanceHeaders()
        get_form_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_form_instance_request = dingtalkswform__1__0_models.GetFormInstanceRequest(
            biz_type=0
        )
        try:
            await client.get_form_instance_with_options_async('11125769-fxxxx', get_form_instance_request, get_form_instance_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vswform_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vswform_1_0\Models\GetFormInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vswform_1_0\Models\GetFormInstanceRequest;
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
        $getFormInstanceHeaders = new GetFormInstanceHeaders([]);
        $getFormInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFormInstanceRequest = new GetFormInstanceRequest([
            "bizType" => 0
        ]);
        try {
            $client->getFormInstanceWithOptions("11125769-fxxxx", $getFormInstanceRequest, $getFormInstanceHeaders, new RuntimeOptions([]));
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
  dingtalkswform_1_0  "github.com/alibabacloud-go/dingtalk/swform_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkswform_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkswform_1_0.Client{}
  _result, _err = dingtalkswform_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getFormInstanceHeaders := &dingtalkswform_1_0.GetFormInstanceHeaders{}
  getFormInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFormInstanceRequest := &dingtalkswform_1_0.GetFormInstanceRequest{
    BizType: tea.Int32(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFormInstanceWithOptions(tea.String("11125769-fxxxx"), getFormInstanceRequest, getFormInstanceHeaders, &util.RuntimeOptions{})
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
import dingtalkswform_1_0, * as $dingtalkswform_1_0 from '@alicloud/dingtalk/swform_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkswform_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkswform_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFormInstanceHeaders = new $dingtalkswform_1_0.GetFormInstanceHeaders({ });
    getFormInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getFormInstanceRequest = new $dingtalkswform_1_0.GetFormInstanceRequest({
      bizType: 0,
    });
    try {
      await client.getFormInstanceWithOptions("11125769-fxxxx", getFormInstanceRequest, getFormInstanceHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkswform_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkswform_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkswform_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkswform_1_0.Models.GetFormInstanceHeaders getFormInstanceHeaders = new AlibabaCloud.SDK.Dingtalkswform_1_0.Models.GetFormInstanceHeaders();
            getFormInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkswform_1_0.Models.GetFormInstanceRequest getFormInstanceRequest = new AlibabaCloud.SDK.Dingtalkswform_1_0.Models.GetFormInstanceRequest
            {
                BizType = 0,
            };
            try
            {
                client.GetFormInstanceWithOptions("11125769-fxxxx", getFormInstanceRequest, getFormInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |
| result | Object | 返回结果。 |
| createTime | String | 填表实例提交时间，iso8601格式，例如2022-07-29T15:07Z。 |
| modifyTime | String | 填表更新时间，iso8601格式，例如2022-07-29T15:07Z。 |
| formCode | String | 表单模板code。 |
| title | String | 表单名称。 |
| creator | String | 表单实例提交者userId。 |
| forms | Array | 表单内容列表。 |
| label | String | 表单控件名称。 |
| key | String | 表单控件key。 |
| value | String | 表单控件的值。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "createTime" : "2022-07-27T18:53Z",
    "modifyTime" : "2022-07-27T18:53Z",
    "formCode" : "PROC-xxx",
    "title" : "智能填表测试",
    "creator" : "user123",
    "forms" : [ {
      "label" : "表单主题",
      "key" : "TextareaField_KGAW58AQ",
      "value" : "表单控件value"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | swform.getFormInstance.paramError | invalid biz\_type | 填表类型参数非法，当前仅支持0：通用智能填表 1：教育版填表 |
| 400 | swform.getFormInstance.paramError | invalid formInstanceId | formInstanceId请求参数不能为空 |
| 400 | swform.getFormInstance.paramError | param invalid | 获取填表实例详情参数异常 |
| 400 | swform.getFormInstance.paramError | app not exist | 应用不存在 |
| 400 | swform.getFormInstance.paramError | app has been stoped | 应用已停用 |
| 400 | swform.getFormInstance.paramError | can't find form app | 找不到应用（不存在或已停用） |
| 400 | swform.getFormInstance.bizError | getInstance fail | 获取表单详情失败 |
| 500 | swform.getFormInstance.sysError | swform.getFormInstance.sysError | 获取填表实例详情系统异常 |
