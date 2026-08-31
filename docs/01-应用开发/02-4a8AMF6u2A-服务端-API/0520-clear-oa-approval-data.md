---
title: "清理OA审批数据"
source_url: "https://open.dingtalk.com/document/development/clear-oa-approval-data"
namespace: "development"
slug: "clear-oa-approval-data"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 流程中心任务 > 清理OA审批数据"
doc_id: "8HoNK9SKMc"
updated_at: "2026-06-03 10:12:41"
---

> Source: https://open.dingtalk.com/document/development/clear-oa-approval-data
> Path: 应用开发 / 服务端 API / OA 审批 > 自有 OA 审批 > 流程中心任务 > 清理OA审批数据
> Updated: 2026-06-03 10:12:41

# 清理OA审批数据

调用本接口，清理审批相关数据。

## **接口调用说明**

企业在某种情况下不再使用第三方企业应用，比如服务到期或主动解除授权（非停用），产品方案商可以调用本接口，删除企业的审批模板、实例、任务等数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/clean |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Data.Clean-工作流数据清理专用权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用本接口的访问凭证，通过调用[获取第三方企业应用的suiteAccessToken](0036-obtains-the-suite-acess-token-of-third-party-enterprise-applications.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 是 | 模板唯一码，通过[创建或更新审批模板](https://open.dingtalk.com/document/development/create-or-update-approval-templates-new)接口获取。 |
| corpId | String | 是 | 授权企业的corpId。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processes/clean HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processCode" : "PROC-EF6Yxxxxx",
  "corpId" : "ding1234"
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.CleanProcessDataHeaders cleanProcessDataHeaders = new com.aliyun.dingtalkworkflow_1_0.models.CleanProcessDataHeaders();
        cleanProcessDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.CleanProcessDataRequest cleanProcessDataRequest = new com.aliyun.dingtalkworkflow_1_0.models.CleanProcessDataRequest()
                .setProcessCode("PROC-EF6Yxxxxx")
                .setCorpId("ding1234");
        try {
            client.cleanProcessDataWithOptions(cleanProcessDataRequest, cleanProcessDataHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        clean_process_data_headers = dingtalkworkflow__1__0_models.CleanProcessDataHeaders()
        clean_process_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        clean_process_data_request = dingtalkworkflow__1__0_models.CleanProcessDataRequest(
            process_code='PROC-EF6Yxxxxx',
            corp_id='ding1234'
        )
        try:
            client.clean_process_data_with_options(clean_process_data_request, clean_process_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        clean_process_data_headers = dingtalkworkflow__1__0_models.CleanProcessDataHeaders()
        clean_process_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        clean_process_data_request = dingtalkworkflow__1__0_models.CleanProcessDataRequest(
            process_code='PROC-EF6Yxxxxx',
            corp_id='ding1234'
        )
        try:
            await client.clean_process_data_with_options_async(clean_process_data_request, clean_process_data_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CleanProcessDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CleanProcessDataRequest;
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
        $cleanProcessDataHeaders = new CleanProcessDataHeaders([]);
        $cleanProcessDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cleanProcessDataRequest = new CleanProcessDataRequest([
            "processCode" => "PROC-EF6Yxxxxx",
            "corpId" => "ding1234"
        ]);
        try {
            $client->cleanProcessDataWithOptions($cleanProcessDataRequest, $cleanProcessDataHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  cleanProcessDataHeaders := &dingtalkworkflow_1_0.CleanProcessDataHeaders{}
  cleanProcessDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cleanProcessDataRequest := &dingtalkworkflow_1_0.CleanProcessDataRequest{
    ProcessCode: tea.String("PROC-EF6Yxxxxx"),
    CorpId: tea.String("ding1234"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CleanProcessDataWithOptions(cleanProcessDataRequest, cleanProcessDataHeaders, &util.RuntimeOptions{})
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
    let cleanProcessDataHeaders = new $dingtalkworkflow_1_0.CleanProcessDataHeaders({ });
    cleanProcessDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let cleanProcessDataRequest = new $dingtalkworkflow_1_0.CleanProcessDataRequest({
      processCode: "PROC-EF6Yxxxxx",
      corpId: "ding1234",
    });
    try {
      await client.cleanProcessDataWithOptions(cleanProcessDataRequest, cleanProcessDataHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CleanProcessDataHeaders cleanProcessDataHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CleanProcessDataHeaders();
            cleanProcessDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CleanProcessDataRequest cleanProcessDataRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CleanProcessDataRequest
            {
                ProcessCode = "PROC-EF6Yxxxxx",
                CorpId = "ding1234",
            };
            try
            {
                client.CleanProcessDataWithOptions(cleanProcessDataRequest, cleanProcessDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 清除操作是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidProcessCode | 审批模板processCode不能为空 | 审批模板processCode不能为空 |
| 400 | processNotExist | 审批流不存在 | 审批流不存在 |
| 400 | needAuth | 需要授权 | 需要授权 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | processGetFailedByParameter | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 500 | systemError | 系统异常 | 系统异常 |
