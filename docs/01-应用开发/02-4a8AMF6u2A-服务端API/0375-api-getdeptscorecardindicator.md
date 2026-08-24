---
title: "获取Agoal指定部门下的计分卡维度和指标id"
source_url: "https://open.dingtalk.com/document/development/api-getdeptscorecardindicator"
namespace: "development"
slug: "api-getdeptscorecardindicator"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Agoal > 计分卡 > 获取Agoal指定部门下的计分卡维度和指标id"
doc_id: "APsgxI3p3U"
updated_at: "2026-06-04 19:09:00"
---

> Source: https://open.dingtalk.com/document/development/api-getdeptscorecardindicator
> Path: 应用开发 / 服务端API / Agoal > 计分卡 > 获取Agoal指定部门下的计分卡维度和指标id
> Updated: 2026-06-04 19:09:00

# 获取Agoal指定部门下的计分卡维度和指标id

调用本接口获取指定部门下计分卡的维度和指标，返回对象包括维度id、指标id，以数组列表形式返回。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/agoal/scorecards/departments/indicators |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Agoal.Scorecard.Read-Agoal计分卡读取权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dingTeamId | String | 否 | 部门openId。 |

### 请求示例

HTTP

```
GET /v1.0/agoal/scorecards/departments/indicators?dingTeamId=853434729 HTTP/1.1
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
        com.aliyun.dingtalkagoal_1_0.models.GetDeptScoreCardIndicatorHeaders getDeptScoreCardIndicatorHeaders = new com.aliyun.dingtalkagoal_1_0.models.GetDeptScoreCardIndicatorHeaders();
        getDeptScoreCardIndicatorHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkagoal_1_0.models.GetDeptScoreCardIndicatorRequest getDeptScoreCardIndicatorRequest = new com.aliyun.dingtalkagoal_1_0.models.GetDeptScoreCardIndicatorRequest()
                .setDingTeamId("853434729");
        try {
            client.getDeptScoreCardIndicatorWithOptions(getDeptScoreCardIndicatorRequest, getDeptScoreCardIndicatorHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_dept_score_card_indicator_headers = dingtalkagoal__1__0_models.GetDeptScoreCardIndicatorHeaders()
        get_dept_score_card_indicator_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_dept_score_card_indicator_request = dingtalkagoal__1__0_models.GetDeptScoreCardIndicatorRequest(
            ding_team_id='853434729'
        )
        try:
            client.get_dept_score_card_indicator_with_options(get_dept_score_card_indicator_request, get_dept_score_card_indicator_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_dept_score_card_indicator_headers = dingtalkagoal__1__0_models.GetDeptScoreCardIndicatorHeaders()
        get_dept_score_card_indicator_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_dept_score_card_indicator_request = dingtalkagoal__1__0_models.GetDeptScoreCardIndicatorRequest(
            ding_team_id='853434729'
        )
        try:
            await client.get_dept_score_card_indicator_with_options_async(get_dept_score_card_indicator_request, get_dept_score_card_indicator_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\GetDeptScoreCardIndicatorHeaders;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\GetDeptScoreCardIndicatorRequest;
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
        $getDeptScoreCardIndicatorHeaders = new GetDeptScoreCardIndicatorHeaders([]);
        $getDeptScoreCardIndicatorHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getDeptScoreCardIndicatorRequest = new GetDeptScoreCardIndicatorRequest([
            "dingTeamId" => "853434729"
        ]);
        try {
            $client->getDeptScoreCardIndicatorWithOptions($getDeptScoreCardIndicatorRequest, $getDeptScoreCardIndicatorHeaders, new RuntimeOptions([]));
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

  getDeptScoreCardIndicatorHeaders := &dingtalkagoal_1_0.GetDeptScoreCardIndicatorHeaders{}
  getDeptScoreCardIndicatorHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getDeptScoreCardIndicatorRequest := &dingtalkagoal_1_0.GetDeptScoreCardIndicatorRequest{
    DingTeamId: tea.String("853434729"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetDeptScoreCardIndicatorWithOptions(getDeptScoreCardIndicatorRequest, getDeptScoreCardIndicatorHeaders, &util.RuntimeOptions{})
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
    let getDeptScoreCardIndicatorHeaders = new dingtalkagoal_1_0.GetDeptScoreCardIndicatorHeaders({ });
    getDeptScoreCardIndicatorHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getDeptScoreCardIndicatorRequest = new dingtalkagoal_1_0.GetDeptScoreCardIndicatorRequest({
      dingTeamId: '853434729',
    });
    try {
      await client.getDeptScoreCardIndicatorWithOptions(getDeptScoreCardIndicatorRequest, getDeptScoreCardIndicatorHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetDeptScoreCardIndicatorHeaders getDeptScoreCardIndicatorHeaders = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetDeptScoreCardIndicatorHeaders();
            getDeptScoreCardIndicatorHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetDeptScoreCardIndicatorRequest getDeptScoreCardIndicatorRequest = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.GetDeptScoreCardIndicatorRequest
            {
                DingTeamId = "853434729",
            };
            try
            {
                client.GetDeptScoreCardIndicatorWithOptions(getDeptScoreCardIndicatorRequest, getDeptScoreCardIndicatorHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求ID。 |
| success | Boolean | 是否成功。 |
| content | OpenScoreCardDimensionDTO | 包含维度和指标id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "ACA7BAAA-BA6F-76F3-8A1B-EF4A37E589E9",
  "success" : true,
  "content" : {
    "dimensionList" : [ {
      "indicatorIdList" : [ ]
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | error.systemError | 系统异常 | 系统异常 |
| 500 | error.emptyScoreCard | 部门下没有计分卡 | 部门下没有计分卡 |
