---
title: "人才档案基础数据查询"
source_url: "https://open.dingtalk.com/document/development/api-hrbraintalentprofilebasicquery"
namespace: "development"
slug: "api-hrbraintalentprofilebasicquery"
group: "应用开发"
tab: "服务端API"
breadcrumb: "组织大脑 > 人才档案 > 人才档案基础数据查询"
doc_id: "q8ksOoe7Ju"
updated_at: "2026-06-02 19:34:56"
---

> Source: https://open.dingtalk.com/document/development/api-hrbraintalentprofilebasicquery
> Path: 应用开发 / 服务端API / 组织大脑 > 人才档案 > 人才档案基础数据查询
> Updated: 2026-06-02 19:34:56

# 人才档案基础数据查询

调用本接口查询人员档案基础信息，支持批量查询。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/profiles/basicData/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrbrain.Data.Read-组织大脑数据查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| dingCorpId | String | 否 | 组织编码。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array of String | 否 | 钉钉用户UserId。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/profiles/basicData/query?dingCorpId=ding3b*********88 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:480021443f9f37fcbf464c4a6b85d289
Content-Type:application/json

[ "23498734" ]
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
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainTalentProfileBasicQueryHeaders hrbrainTalentProfileBasicQueryHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainTalentProfileBasicQueryHeaders();
        hrbrainTalentProfileBasicQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainTalentProfileBasicQueryRequest hrbrainTalentProfileBasicQueryRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainTalentProfileBasicQueryRequest()
                .setDingCorpId("ding3b*********88")
                .setBody(java.util.Arrays.asList(
                    "23498734"
                ));
        try {
            client.hrbrainTalentProfileBasicQueryWithOptions(hrbrainTalentProfileBasicQueryRequest, hrbrainTalentProfileBasicQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrbrain_1_0.client import Client as dingtalkhrbrain_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrbrain_1_0 import models as dingtalkhrbrain__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrbrain_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrbrain_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_talent_profile_basic_query_headers = dingtalkhrbrain__1__0_models.HrbrainTalentProfileBasicQueryHeaders()
        hrbrain_talent_profile_basic_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrbrain_talent_profile_basic_query_request = dingtalkhrbrain__1__0_models.HrbrainTalentProfileBasicQueryRequest(
            ding_corp_id='ding3b*********88',
            body=[
                '23498734'
            ]
        )
        try:
            client.hrbrain_talent_profile_basic_query_with_options(hrbrain_talent_profile_basic_query_request, hrbrain_talent_profile_basic_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_talent_profile_basic_query_headers = dingtalkhrbrain__1__0_models.HrbrainTalentProfileBasicQueryHeaders()
        hrbrain_talent_profile_basic_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrbrain_talent_profile_basic_query_request = dingtalkhrbrain__1__0_models.HrbrainTalentProfileBasicQueryRequest(
            ding_corp_id='ding3b*********88',
            body=[
                '23498734'
            ]
        )
        try:
            await client.hrbrain_talent_profile_basic_query_with_options_async(hrbrain_talent_profile_basic_query_request, hrbrain_talent_profile_basic_query_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainTalentProfileBasicQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainTalentProfileBasicQueryRequest;
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
        $hrbrainTalentProfileBasicQueryHeaders = new HrbrainTalentProfileBasicQueryHeaders([]);
        $hrbrainTalentProfileBasicQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $hrbrainTalentProfileBasicQueryRequest = new HrbrainTalentProfileBasicQueryRequest([
            "dingCorpId" => "ding3b*********88",
            "body" => [
                "23498734"
            ]
        ]);
        try {
            $client->hrbrainTalentProfileBasicQueryWithOptions($hrbrainTalentProfileBasicQueryRequest, $hrbrainTalentProfileBasicQueryHeaders, new RuntimeOptions([]));
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
  dingtalkhrbrain_1_0  "github.com/alibabacloud-go/dingtalk/hrbrain_1_0"
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
func CreateClient () (_result *dingtalkhrbrain_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrbrain_1_0.Client{}
  _result, _err = dingtalkhrbrain_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrbrainTalentProfileBasicQueryHeaders := &dingtalkhrbrain_1_0.HrbrainTalentProfileBasicQueryHeaders{}
  hrbrainTalentProfileBasicQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  hrbrainTalentProfileBasicQueryRequest := &dingtalkhrbrain_1_0.HrbrainTalentProfileBasicQueryRequest{
    DingCorpId: tea.String("ding3b*********88"),
    Body: []*string{tea.String("23498734")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainTalentProfileBasicQueryWithOptions(hrbrainTalentProfileBasicQueryRequest, hrbrainTalentProfileBasicQueryHeaders, &util.RuntimeOptions{})
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
const dingtalkhrbrain_1_0 = require('@alicloud/dingtalk/hrbrain_1_0');
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
    return new dingtalkhrbrain_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let hrbrainTalentProfileBasicQueryHeaders = new dingtalkhrbrain_1_0.HrbrainTalentProfileBasicQueryHeaders({ });
    hrbrainTalentProfileBasicQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let hrbrainTalentProfileBasicQueryRequest = new dingtalkhrbrain_1_0.HrbrainTalentProfileBasicQueryRequest({
      dingCorpId: 'ding3b*********88',
      body: [
        '23498734'
      ],
    });
    try {
      await client.hrbrainTalentProfileBasicQueryWithOptions(hrbrainTalentProfileBasicQueryRequest, hrbrainTalentProfileBasicQueryHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainTalentProfileBasicQueryHeaders hrbrainTalentProfileBasicQueryHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainTalentProfileBasicQueryHeaders();
            hrbrainTalentProfileBasicQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainTalentProfileBasicQueryRequest hrbrainTalentProfileBasicQueryRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainTalentProfileBasicQueryRequest
            {
                DingCorpId = "ding3b*********88",
                Body = new List<string>
                {
                    "23498734"
                },
            };
            try
            {
                client.HrbrainTalentProfileBasicQueryWithOptions(hrbrainTalentProfileBasicQueryRequest, hrbrainTalentProfileBasicQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |
| result | Boolean | 查询是否成功。 |
| content | Object | 返回结果。 |
| profileBaseInfoList | Array | 人员基础信息列表。 |
| workNo | String | 钉钉用户UserId。 |
| name | String | 用户姓名。 |
| age | String | 年龄。 |
| deptName | String | 部门名称。 |
| jobcode | String | 职务。 |
| position | String | 职位。 |
| jobLevel | String | 职级。 |
| superName | String | 主管名。 |
| workPlace | String | 工作城市。 |
| gender | String | 性别。 |
| birthday | String | 生日。 |
| seniorityYears | String | 司龄（年）。 |
| superWorkNo | String | 主管的钉钉UserId。 |
| deptNo | String | 部门编码。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "480021443f9f37fcbf464c4a6b85d289",
  "success" : true,
  "result" : true,
  "content" : {
    "profileBaseInfoList" : [ {
      "workNo" : "23498734",
      "name" : "张三",
      "age" : "19",
      "deptName" : "测试部",
      "jobcode" : "经理",
      "position" : "研发",
      "jobLevel" : "p6",
      "superName" : "李四",
      "workPlace" : "杭州",
      "gender" : "男",
      "birthday" : "2000-01-01",
      "seniorityYears" : "5",
      "superWorkNo" : "238949",
      "deptNo" : "1234"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illagal. %s | 入参错误 |
