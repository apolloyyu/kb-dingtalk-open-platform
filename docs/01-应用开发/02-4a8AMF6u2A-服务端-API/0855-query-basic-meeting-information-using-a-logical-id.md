---
title: "根据会议逻辑ID查询会议基本信息"
source_url: "https://open.dingtalk.com/document/development/query-basic-meeting-information-using-a-logical-id"
namespace: "development"
slug: "query-basic-meeting-information-using-a-logical-id"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 根据会议逻辑ID查询会议基本信息"
doc_id: "lmD5T4HpBi"
updated_at: "2026-07-14 09:22:17"
---

> Source: https://open.dingtalk.com/document/development/query-basic-meeting-information-using-a-logical-id
> Path: 应用开发 / 服务端 API / 专属钉钉 > 根据会议逻辑ID查询会议基本信息
> Updated: 2026-07-14 09:22:17

# 根据会议逻辑ID查询会议基本信息

调用本接口，根据会议逻辑ID查询会议基本信息，包括会议标题、创建者昵称、开始时间等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/data/conferences |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Common.Read-专属钉钉专属数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| logicalConferenceId | String | 是 | 会议逻辑ID，可调用[创建日程](0250-create-schedule.md)接口获取conferenceId参数值。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/data/conferences?logicalConferenceId=xxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.GetConfBaseInfoByLogicalIdHeaders getConfBaseInfoByLogicalIdHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetConfBaseInfoByLogicalIdHeaders();
        getConfBaseInfoByLogicalIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetConfBaseInfoByLogicalIdRequest getConfBaseInfoByLogicalIdRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetConfBaseInfoByLogicalIdRequest()
                .setLogicalConferenceId("xxxxx");
        try {
            client.getConfBaseInfoByLogicalIdWithOptions(getConfBaseInfoByLogicalIdRequest, getConfBaseInfoByLogicalIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_conf_base_info_by_logical_id_headers = dingtalkexclusive__1__0_models.GetConfBaseInfoByLogicalIdHeaders()
        get_conf_base_info_by_logical_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_conf_base_info_by_logical_id_request = dingtalkexclusive__1__0_models.GetConfBaseInfoByLogicalIdRequest(
            logical_conference_id='xxxxx'
        )
        try:
            client.get_conf_base_info_by_logical_id_with_options(get_conf_base_info_by_logical_id_request, get_conf_base_info_by_logical_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_conf_base_info_by_logical_id_headers = dingtalkexclusive__1__0_models.GetConfBaseInfoByLogicalIdHeaders()
        get_conf_base_info_by_logical_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_conf_base_info_by_logical_id_request = dingtalkexclusive__1__0_models.GetConfBaseInfoByLogicalIdRequest(
            logical_conference_id='xxxxx'
        )
        try:
            await client.get_conf_base_info_by_logical_id_with_options_async(get_conf_base_info_by_logical_id_request, get_conf_base_info_by_logical_id_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetConfBaseInfoByLogicalIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetConfBaseInfoByLogicalIdRequest;
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
        $getConfBaseInfoByLogicalIdHeaders = new GetConfBaseInfoByLogicalIdHeaders([]);
        $getConfBaseInfoByLogicalIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getConfBaseInfoByLogicalIdRequest = new GetConfBaseInfoByLogicalIdRequest([
            "logicalConferenceId" => "xxxxx"
        ]);
        try {
            $client->getConfBaseInfoByLogicalIdWithOptions($getConfBaseInfoByLogicalIdRequest, $getConfBaseInfoByLogicalIdHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getConfBaseInfoByLogicalIdHeaders := &dingtalkexclusive_1_0.GetConfBaseInfoByLogicalIdHeaders{}
  getConfBaseInfoByLogicalIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getConfBaseInfoByLogicalIdRequest := &dingtalkexclusive_1_0.GetConfBaseInfoByLogicalIdRequest{
    LogicalConferenceId: tea.String("xxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetConfBaseInfoByLogicalIdWithOptions(getConfBaseInfoByLogicalIdRequest, getConfBaseInfoByLogicalIdHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getConfBaseInfoByLogicalIdHeaders = new $dingtalkexclusive_1_0.GetConfBaseInfoByLogicalIdHeaders({ });
    getConfBaseInfoByLogicalIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getConfBaseInfoByLogicalIdRequest = new $dingtalkexclusive_1_0.GetConfBaseInfoByLogicalIdRequest({
      logicalConferenceId: "xxxxx",
    });
    try {
      await client.getConfBaseInfoByLogicalIdWithOptions(getConfBaseInfoByLogicalIdRequest, getConfBaseInfoByLogicalIdHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetConfBaseInfoByLogicalIdHeaders getConfBaseInfoByLogicalIdHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetConfBaseInfoByLogicalIdHeaders();
            getConfBaseInfoByLogicalIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetConfBaseInfoByLogicalIdRequest getConfBaseInfoByLogicalIdRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetConfBaseInfoByLogicalIdRequest
            {
                LogicalConferenceId = "xxxxx",
            };
            try
            {
                client.GetConfBaseInfoByLogicalIdWithOptions(getConfBaseInfoByLogicalIdRequest, getConfBaseInfoByLogicalIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| conferenceId | String | 会议实体ID。      会议正式开始后才会返回该字段。 |
| title | String | 会议标题。 |
| startTime | Long | 开始时间戳，单位毫秒。 |
| logicalConferenceId | String | 会议逻辑ID。 |
| unionId | String | 会议创建者的unionId。 |
| nickname | String | 会议创建者的昵称。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "conferenceId" : "60f804681405e037xxxxxxxx",
  "title" : "测试会议",
  "startTime" : 1653634440722,
  "logicalConferenceId" : "28d35e8e-3880-4971-XXXX-c82c6878a419",
  "unionId" : "WFBkxxxxxxxxtSaA1jK4sgiEiE",
  "nickname" : "钉三多"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | params.error | error:%s | 未找到会议 |
| 500 | conference.not.found | error:%s | 视频发起者不属于当前组织 |
| 500 | system.error | systemError:%s | 系统错误 |
