---
title: "修改已离职员工信息"
source_url: "https://open.dingtalk.com/document/development/modify-resigned-employee-information"
namespace: "development"
slug: "modify-resigned-employee-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 员工管理 > 修改已离职员工信息"
doc_id: "5DlAg1fVZ6"
updated_at: "2026-06-04 19:10:27"
---

> Source: https://open.dingtalk.com/document/development/modify-resigned-employee-information
> Path: 应用开发 / 服务端 API / 智能人事 > 员工管理 > 修改已离职员工信息
> Updated: 2026-06-04 19:10:27

# 修改已离职员工信息

调用本接口，修改智能人事中已离职员工的信息，包括员工离职时间和离职备注等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/processes/employees/terminations |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrm.Process.ReadWrite-智能人事流程读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 已离职员工的userId，可调用[获取离职员工列表](0947-obtain-the-list-of-employees-who-have-left.md)接口获取离职员工userId。 |
| lastWorkDate | Long | 是 | 最后工作日，即离职日期，格式为毫秒值时间戳。 |
| dismissionMemo | String | 是 | 离职备注信息。 |

### 请求示例

HTTP

```
PUT /v1.0/hrm/processes/employees/terminations HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "userId" : "user001",
  "lastWorkDate" : 1672502400000,
  "dismissionMemo" : "因个人原因离职"
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
        com.aliyun.dingtalkhrm_1_0.models.HrmProcessUpdateTerminationInfoHeaders hrmProcessUpdateTerminationInfoHeaders = new com.aliyun.dingtalkhrm_1_0.models.HrmProcessUpdateTerminationInfoHeaders();
        hrmProcessUpdateTerminationInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.HrmProcessUpdateTerminationInfoRequest hrmProcessUpdateTerminationInfoRequest = new com.aliyun.dingtalkhrm_1_0.models.HrmProcessUpdateTerminationInfoRequest()
                .setUserId("user001")
                .setLastWorkDate(1672502400000L)
                .setDismissionMemo("因个人原因离职");
        try {
            client.hrmProcessUpdateTerminationInfoWithOptions(hrmProcessUpdateTerminationInfoRequest, hrmProcessUpdateTerminationInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        hrm_process_update_termination_info_headers = dingtalkhrm__1__0_models.HrmProcessUpdateTerminationInfoHeaders()
        hrm_process_update_termination_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_update_termination_info_request = dingtalkhrm__1__0_models.HrmProcessUpdateTerminationInfoRequest(
            user_id='user001',
            last_work_date=1672502400000,
            dismission_memo='因个人原因离职'
        )
        try:
            client.hrm_process_update_termination_info_with_options(hrm_process_update_termination_info_request, hrm_process_update_termination_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrm_process_update_termination_info_headers = dingtalkhrm__1__0_models.HrmProcessUpdateTerminationInfoHeaders()
        hrm_process_update_termination_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_update_termination_info_request = dingtalkhrm__1__0_models.HrmProcessUpdateTerminationInfoRequest(
            user_id='user001',
            last_work_date=1672502400000,
            dismission_memo='因个人原因离职'
        )
        try:
            await client.hrm_process_update_termination_info_with_options_async(hrm_process_update_termination_info_request, hrm_process_update_termination_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessUpdateTerminationInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessUpdateTerminationInfoRequest;
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
        $hrmProcessUpdateTerminationInfoHeaders = new HrmProcessUpdateTerminationInfoHeaders([]);
        $hrmProcessUpdateTerminationInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $hrmProcessUpdateTerminationInfoRequest = new HrmProcessUpdateTerminationInfoRequest([
            "userId" => "user001",
            "lastWorkDate" => 1672502400000,
            "dismissionMemo" => "因个人原因离职"
        ]);
        try {
            $client->hrmProcessUpdateTerminationInfoWithOptions($hrmProcessUpdateTerminationInfoRequest, $hrmProcessUpdateTerminationInfoHeaders, new RuntimeOptions([]));
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

  hrmProcessUpdateTerminationInfoHeaders := &dingtalkhrm_1_0.HrmProcessUpdateTerminationInfoHeaders{}
  hrmProcessUpdateTerminationInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  hrmProcessUpdateTerminationInfoRequest := &dingtalkhrm_1_0.HrmProcessUpdateTerminationInfoRequest{
    UserId: tea.String("user001"),
    LastWorkDate: tea.Int64(1672502400000),
    DismissionMemo: tea.String("因个人原因离职"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrmProcessUpdateTerminationInfoWithOptions(hrmProcessUpdateTerminationInfoRequest, hrmProcessUpdateTerminationInfoHeaders, &util.RuntimeOptions{})
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
    let hrmProcessUpdateTerminationInfoHeaders = new $dingtalkhrm_1_0.HrmProcessUpdateTerminationInfoHeaders({ });
    hrmProcessUpdateTerminationInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let hrmProcessUpdateTerminationInfoRequest = new $dingtalkhrm_1_0.HrmProcessUpdateTerminationInfoRequest({
      userId: "user001",
      lastWorkDate: 1672502400000,
      dismissionMemo: "因个人原因离职",
    });
    try {
      await client.hrmProcessUpdateTerminationInfoWithOptions(hrmProcessUpdateTerminationInfoRequest, hrmProcessUpdateTerminationInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessUpdateTerminationInfoHeaders hrmProcessUpdateTerminationInfoHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessUpdateTerminationInfoHeaders();
            hrmProcessUpdateTerminationInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessUpdateTerminationInfoRequest hrmProcessUpdateTerminationInfoRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessUpdateTerminationInfoRequest
            {
                UserId = "user001",
                LastWorkDate = 1672502400000,
                DismissionMemo = "因个人原因离职",
            };
            try
            {
                client.HrmProcessUpdateTerminationInfoWithOptions(hrmProcessUpdateTerminationInfoRequest, hrmProcessUpdateTerminationInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否更新成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : false
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | noPermission | 无权限访问 | 无权限访问 |
| 400 | illegalParam | 参数错误 | 员工id或者最后工作日错误 |
| 400 | empNotExists | 员工不存在 | 员工不存在 |
| 400 | empNotDismission | 员工当前非离职状态 | 员工当前非离职状态 |
| 400 | empStatusError | 员工离职状态出错，请联系钉钉智能人事 | 员工离职状态出错，请联系钉钉智能人事 |
