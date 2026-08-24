---
title: "智能人事员工转正"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-staff-to-become-regular"
namespace: "development"
slug: "intelligent-personnel-staff-to-become-regular"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工关系 > 智能人事员工转正"
doc_id: "OAcGsfHQ62"
updated_at: "2026-06-04 19:10:32"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-staff-to-become-regular
> Path: 应用开发 / 服务端API / 智能人事 > 员工关系 > 智能人事员工转正
> Updated: 2026-06-04 19:10:32

# 智能人事员工转正

调用本接口，实现企业员工转正。

## **接口调用说明**

- 实际转正日期若是当天或未来时间，则通过定时任务触发变更实际转正日期。
- 实际转正日期若是当天之前时间，则实际转正日期立即生效。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/processes/regulars/become |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrm.Process.ReadWrite-智能人事流程读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 待转正用户userId。 |
| regularDate | Long | 是 | 转正时间，unix时间戳，单位毫秒。 |
| remark | String | 否 | 备注信息。 |
| operationId | String | 是 | 操作用户userId。 |

### 请求示例

HTTP

```
POST /v1.0/hrm/processes/regulars/become HTTP/1.1
Host:api.dingtalk.com
Content-Type:application/json

{
  "userId" : "16690147049882572",
  "regularDate" : 1672542359000,
  "remark" : "同意转正",
  "operationId" : "16690147049882572"
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
        com.aliyun.dingtalkhrm_1_0.models.HrmProcessRegularHeaders hrmProcessRegularHeaders = new com.aliyun.dingtalkhrm_1_0.models.HrmProcessRegularHeaders();
        hrmProcessRegularHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.HrmProcessRegularRequest hrmProcessRegularRequest = new com.aliyun.dingtalkhrm_1_0.models.HrmProcessRegularRequest()
                .setUserId("16690147049882572")
                .setRegularDate(1672542359000L)
                .setRemark("同意转正")
                .setOperationId("16690147049882572");
        try {
            client.hrmProcessRegularWithOptions(hrmProcessRegularRequest, hrmProcessRegularHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        hrm_process_regular_headers = dingtalkhrm__1__0_models.HrmProcessRegularHeaders()
        hrm_process_regular_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_regular_request = dingtalkhrm__1__0_models.HrmProcessRegularRequest(
            user_id='16690147049882572',
            regular_date=1672542359000,
            remark='同意转正',
            operation_id='16690147049882572'
        )
        try:
            client.hrm_process_regular_with_options(hrm_process_regular_request, hrm_process_regular_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrm_process_regular_headers = dingtalkhrm__1__0_models.HrmProcessRegularHeaders()
        hrm_process_regular_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_regular_request = dingtalkhrm__1__0_models.HrmProcessRegularRequest(
            user_id='16690147049882572',
            regular_date=1672542359000,
            remark='同意转正',
            operation_id='16690147049882572'
        )
        try:
            await client.hrm_process_regular_with_options_async(hrm_process_regular_request, hrm_process_regular_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessRegularHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessRegularRequest;
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
        $hrmProcessRegularHeaders = new HrmProcessRegularHeaders([]);
        $hrmProcessRegularHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $hrmProcessRegularRequest = new HrmProcessRegularRequest([
            "userId" => "16690147049882572",
            "regularDate" => 1672542359000,
            "remark" => "同意转正",
            "operationId" => "16690147049882572"
        ]);
        try {
            $client->hrmProcessRegularWithOptions($hrmProcessRegularRequest, $hrmProcessRegularHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  hrmProcessRegularHeaders := &dingtalkhrm_1_0.HrmProcessRegularHeaders{}
  hrmProcessRegularHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  hrmProcessRegularRequest := &dingtalkhrm_1_0.HrmProcessRegularRequest{
    UserId: tea.String("16690147049882572"),
    RegularDate: tea.Int64(1672542359000),
    Remark: tea.String("同意转正"),
    OperationId: tea.String("16690147049882572"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrmProcessRegularWithOptions(hrmProcessRegularRequest, hrmProcessRegularHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let hrmProcessRegularHeaders = new $dingtalkhrm_1_0.HrmProcessRegularHeaders({ });
    hrmProcessRegularHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let hrmProcessRegularRequest = new $dingtalkhrm_1_0.HrmProcessRegularRequest({
      userId: "16690147049882572",
      regularDate: 1672542359000,
      remark: "同意转正",
      operationId: "16690147049882572",
    });
    try {
      await client.hrmProcessRegularWithOptions(hrmProcessRegularRequest, hrmProcessRegularHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessRegularHeaders hrmProcessRegularHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessRegularHeaders();
            hrmProcessRegularHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessRegularRequest hrmProcessRegularRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessRegularRequest
            {
                UserId = "16690147049882572",
                RegularDate = 1672542359000,
                Remark = "同意转正",
                OperationId = "16690147049882572",
            };
            try
            {
                client.HrmProcessRegularWithOptions(hrmProcessRegularRequest, hrmProcessRegularHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 转正是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | noPermission | 无权限访问 | 无权限访问 |
| 400 | invokeFrequentyly | 调用频繁 | 调用频繁 |
| 400 | invalidParameter | 用户ID或转正时间不能为空 | 用户ID或转正时间不能为空 |
| 400 | inProcessOfApproval | 已在转正审批流程中 | 已在转正审批流程中 |
| 500 | systemError | 系统异常 | 系统异常 |
