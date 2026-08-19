---
title: "查询用户钉钉365会员信息"
source_url: "https://open.dingtalk.com/document/development/api-queryvipmemberinfo"
namespace: "development"
slug: "api-queryvipmemberinfo"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 365会员 > 查询用户钉钉365会员信息"
doc_id: "3rfCmAyhQJ"
updated_at: "2025-09-23 19:26:19"
---

> Source: https://open.dingtalk.com/document/development/api-queryvipmemberinfo
> Path: 应用开发 / 服务端API / 更多开放 > 365会员 > 查询用户钉钉365会员信息
> Updated: 2025-09-23 19:26:19

# 查询用户钉钉365会员信息

服务商提供的应用中会有部分高级功能，这部分功能需要用户开通钉钉365会员后才能使用，该接口提供查询用户是否开通365会员及会员相关属性。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/vipMember/users/memberInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用　appType-第三方个人应用 |
| 权限要求 | permission-Vip.Member.User.Read-钉钉365会员信息查看权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 - 第三方个人应用，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| channelCode | String | 否 | 标记业务场景字段，可以自定义（长度不超过32字节），用于后续对账和报表数据。 |

### 请求示例

HTTP

```
POST /v1.0/vipMember/users/memberInfos/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a6099441c0b33d8e8648a5a81eb7aa71
Content-Type:application/json

{
  "channelCode" : "Mathematics"
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
    public static com.aliyun.dingtalkvip_member_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkvip_member_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkvip_member_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkvip_member_1_0.models.QueryVipMemberInfoHeaders queryVipMemberInfoHeaders = new com.aliyun.dingtalkvip_member_1_0.models.QueryVipMemberInfoHeaders();
        queryVipMemberInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkvip_member_1_0.models.QueryVipMemberInfoRequest queryVipMemberInfoRequest = new com.aliyun.dingtalkvip_member_1_0.models.QueryVipMemberInfoRequest()
                .setChannelCode("Mathematics");
        try {
            client.queryVipMemberInfoWithOptions(queryVipMemberInfoRequest, queryVipMemberInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.vip_member_1_0.client import Client as dingtalkvipMember_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.vip_member_1_0 import models as dingtalkvip_member__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkvipMember_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkvipMember_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_vip_member_info_headers = dingtalkvip_member__1__0_models.QueryVipMemberInfoHeaders()
        query_vip_member_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_vip_member_info_request = dingtalkvip_member__1__0_models.QueryVipMemberInfoRequest(
            channel_code='Mathematics'
        )
        try:
            client.query_vip_member_info_with_options(query_vip_member_info_request, query_vip_member_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_vip_member_info_headers = dingtalkvip_member__1__0_models.QueryVipMemberInfoHeaders()
        query_vip_member_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_vip_member_info_request = dingtalkvip_member__1__0_models.QueryVipMemberInfoRequest(
            channel_code='Mathematics'
        )
        try:
            await client.query_vip_member_info_with_options_async(query_vip_member_info_request, query_vip_member_info_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vvip_member_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vvip_member_1_0\Models\QueryVipMemberInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vvip_member_1_0\Models\QueryVipMemberInfoRequest;
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
        $queryVipMemberInfoHeaders = new QueryVipMemberInfoHeaders([]);
        $queryVipMemberInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryVipMemberInfoRequest = new QueryVipMemberInfoRequest([
            "channelCode" => "Mathematics"
        ]);
        try {
            $client->queryVipMemberInfoWithOptions($queryVipMemberInfoRequest, $queryVipMemberInfoHeaders, new RuntimeOptions([]));
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
  dingtalkvipmember_1_0  "github.com/alibabacloud-go/dingtalk/vipMember_1_0"
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
func CreateClient () (_result *dingtalkvipmember_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkvipmember_1_0.Client{}
  _result, _err = dingtalkvipmember_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryVipMemberInfoHeaders := &dingtalkvipmember_1_0.QueryVipMemberInfoHeaders{}
  queryVipMemberInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryVipMemberInfoRequest := &dingtalkvipmember_1_0.QueryVipMemberInfoRequest{
    ChannelCode: tea.String("Mathematics"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryVipMemberInfoWithOptions(queryVipMemberInfoRequest, queryVipMemberInfoHeaders, &util.RuntimeOptions{})
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
const dingtalkvipMember_1_0 = require('@alicloud/dingtalk/vipMember_1_0');
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
    return new dingtalkvipMember_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryVipMemberInfoHeaders = new dingtalkvipMember_1_0.QueryVipMemberInfoHeaders({ });
    queryVipMemberInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryVipMemberInfoRequest = new dingtalkvipMember_1_0.QueryVipMemberInfoRequest({
      channelCode: 'Mathematics',
    });
    try {
      await client.queryVipMemberInfoWithOptions(queryVipMemberInfoRequest, queryVipMemberInfoHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkvip_member_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkvip_member_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkvip_member_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkvip_member_1_0.Models.QueryVipMemberInfoHeaders queryVipMemberInfoHeaders = new AlibabaCloud.SDK.Dingtalkvip_member_1_0.Models.QueryVipMemberInfoHeaders();
            queryVipMemberInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkvip_member_1_0.Models.QueryVipMemberInfoRequest queryVipMemberInfoRequest = new AlibabaCloud.SDK.Dingtalkvip_member_1_0.Models.QueryVipMemberInfoRequest
            {
                ChannelCode = "Mathematics",
            };
            try
            {
                client.QueryVipMemberInfoWithOptions(queryVipMemberInfoRequest, queryVipMemberInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| isVip | Boolean | 当前是否已经开通365会员，且会员未过期。 |
| expireTime | String | 会员权益过期时间 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "isVip" : true,
  "expireTime" : "2024-12-31"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | param.error | 参数错误 |
