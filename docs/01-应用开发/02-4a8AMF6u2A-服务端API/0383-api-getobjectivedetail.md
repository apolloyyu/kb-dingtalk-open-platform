---
title: "查询企业下个人目标详情"
source_url: "https://open.dingtalk.com/document/development/api-getobjectivedetail"
namespace: "development"
slug: "api-getobjectivedetail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Agoal > 目标与关键行动 > 查询企业下个人目标详情"
doc_id: "FwY4lkiOsv"
updated_at: "2026-06-02 11:54:14"
---

> Source: https://open.dingtalk.com/document/development/api-getobjectivedetail
> Path: 应用开发 / 服务端API / Agoal > 目标与关键行动 > 查询企业下个人目标详情
> Updated: 2026-06-02 11:54:14

# 查询企业下个人目标详情

调用该接口通过目标id，查询该目标详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/agoal/objectives/details |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Agoal.Objective.Read-Agoal目标读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| objectiveId | String | 是 | 目标Id。 |

### 请求示例

HTTP

```
GET /v1.0/agoal/objectives/details?objectiveId=68c8fd9de4b0beb95xxx45a4 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:9801a354e3d03539baa83e5f275axxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkagoal_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkagoal_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkagoal_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkagoal_1_0.models.GetObjectiveDetailHeaders getObjectiveDetailHeaders = new com.aliyun.dingtalkagoal_1_0.models.GetObjectiveDetailHeaders();
        getObjectiveDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkagoal_1_0.models.GetObjectiveDetailRequest getObjectiveDetailRequest = new com.aliyun.dingtalkagoal_1_0.models.GetObjectiveDetailRequest()
                .setObjectiveId("68c8fd9de4b0beb95xxx45a4");
        try {
            client.getObjectiveDetailWithOptions(getObjectiveDetailRequest, getObjectiveDetailHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.agoal_1_0.client import Client as dingtalkagoal_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.agoal_1_0 import models as dingtalkagoal__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkagoal_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkagoal_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_objective_detail_headers = dingtalkagoal__1__0_models.GetObjectiveDetailHeaders()
        get_objective_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_objective_detail_request = dingtalkagoal__1__0_models.GetObjectiveDetailRequest(
            objective_id='68c8fd9de4b0beb95xxx45a4'
        )
        try:
            client.get_objective_detail_with_options(get_objective_detail_request, get_objective_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_objective_detail_headers = dingtalkagoal__1__0_models.GetObjectiveDetailHeaders()
        get_objective_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_objective_detail_request = dingtalkagoal__1__0_models.GetObjectiveDetailRequest(
            objective_id='68c8fd9de4b0beb95xxx45a4'
        )
        try:
            await client.get_objective_detail_with_options_async(get_objective_detail_request, get_objective_detail_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\GetObjectiveDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\GetObjectiveDetailRequest;
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
        $getObjectiveDetailHeaders = new GetObjectiveDetailHeaders([]);
        $getObjectiveDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getObjectiveDetailRequest = new GetObjectiveDetailRequest([
            "objectiveId" => "68c8fd9de4b0beb95xxx45a4"
        ]);
        try {
            $client->getObjectiveDetailWithOptions($getObjectiveDetailRequest, $getObjectiveDetailHeaders, new RuntimeOptions([]));
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
  dingtalkagoal_1_0  "github.com/alibabacloud-go/dingtalk/agoal_1_0"
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
func CreateClient () (_result *dingtalkagoal_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkagoal_1_0.Client{}
  _result, _err = dingtalkagoal_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getObjectiveDetailHeaders := &dingtalkagoal_1_0.GetObjectiveDetailHeaders{}
  getObjectiveDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getObjectiveDetailRequest := &dingtalkagoal_1_0.GetObjectiveDetailRequest{
    ObjectiveId: tea.String("68c8fd9de4b0beb95xxx45a4"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetObjectiveDetailWithOptions(getObjectiveDetailRequest, getObjectiveDetailHeaders, &util.RuntimeOptions{})
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
const dingtalkagoal_1_0 = require('@alicloud/dingtalk/agoal_1_0');
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
    return new dingtalkagoal_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getObjectiveDetailHeaders = new dingtalkagoal_1_0.GetObjectiveDetailHeaders({ });
    getObjectiveDetailHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getObjectiveDetailRequest = new dingtalkagoal_1_0.GetObjectiveDetailRequest({
      objectiveId: '68c8fd9de4b0beb95xxx45a4',
    });
    try {
      await client.getObjectiveDetailWithOptions(getObjectiveDetailRequest, getObjectiveDetailHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkagoal_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkagoal_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetObjectiveDetailHeaders getObjectiveDetailHeaders = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetObjectiveDetailHeaders();
            getObjectiveDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetObjectiveDetailRequest getObjectiveDetailRequest = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetObjectiveDetailRequest
            {
                ObjectiveId = "68c8fd9de4b0beb95xxx45a4",
            };
            try
            {
                client.GetObjectiveDetailWithOptions(getObjectiveDetailRequest, getObjectiveDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求Id。 |
| success | Boolean | 请求是否成功。 |
| content | OpenAgoalObjectiveDTO | 个人目标对象。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
    "requestId": "E6F8BAA4-6C37-168D-858A-F2A85447755D",
    "success": true,
    "content": {
        "objectiveId": "6444f5e9a4261c6e699dxxxx",
        "title": "测试目标",
        "executor": {
            "userId": "6444f5e9a4261c6e699dxxxx",
            "dingUserId": "211042291978xxxx",
            "name": "测试"
        },
        "teams": [
            {
                "teamId": "6444f5e9a4261c6e699dxxxx",
                "deptId": "8535683xx",
                "name": "测试部门"
            }
        ],
        "period": {
            "periodId": "6444f5e9a4261c6e699dxxxx",
            "name": "2024年度",
            "startDate": 1711900800000,
            "endDate": 1743436799000,
            "periodType": "season"
        },
        "keyResults": [
            {
                "keyResultId": "6444f5e9a4261c6e699dxxxx",
                "title": "测试KR",
                "type": 1,
                "status": 1,
                "progress": 10,
                "weight": 30,
            }
        ],
        "weight": 30,
        "upAlignObjectIds": ["68c8fd9de4b0bexxx47f45a4"],
        "downAlignObjectIds": ["68c8fd9de4b0bexxx47f45a4"],
        "approveStatus":"approved",
        "created":1723690100689,
        "updated":1723690100689
    }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | error.systemError | 系统异常 | 系统异常 |
| 500 | error.invalidObjectiveId | 无效的目标Id | 无效的目标Id |
