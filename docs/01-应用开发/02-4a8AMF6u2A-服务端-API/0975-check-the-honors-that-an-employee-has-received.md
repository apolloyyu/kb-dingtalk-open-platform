---
title: "查询员工已获得的组织荣誉"
source_url: "https://open.dingtalk.com/document/development/check-the-honors-that-an-employee-has-received"
namespace: "development"
slug: "check-the-honors-that-an-employee-has-received"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "企业文化 > 荣誉 > 查询员工已获得的组织荣誉"
doc_id: "qO3hZ7g5vi"
updated_at: "2026-06-04 19:10:40"
---

> Source: https://open.dingtalk.com/document/development/check-the-honors-that-an-employee-has-received
> Path: 应用开发 / 服务端 API / 企业文化 > 荣誉 > 查询员工已获得的组织荣誉
> Updated: 2026-06-04 19:10:40

# 查询员工已获得的组织荣誉

调用本接口，查询某个员工获得的组织荣誉记录，包括荣誉的Id、荣誉被授予的时间、荣誉名称等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/orgCulture/honors/users/{userId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-OrgCulture.Honor.Read-组织文化荣誉信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 员工的userId。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 是 | 分页游标值。   - 如果是首次查询，该参数传0。 - 如果是非首次查询，该参数传上次查询时返回的nextToken。 |
| maxResults | Integer | 否 | 每页返回的最大条目数，默认20， 最大100。 |

### 请求示例

HTTP

```
GET /v1.0/orgCulture/honors/users/user001?nextToken=0&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkorg_culture_1_0.*;
import com.aliyun.dingtalkorg_culture_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkorg_culture_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkorg_culture_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkorg_culture_1_0.Client client = Sample.createClient();
        QueryUserHonorsHeaders queryUserHonorsHeaders = new QueryUserHonorsHeaders();
        queryUserHonorsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryUserHonorsRequest queryUserHonorsRequest = new QueryUserHonorsRequest()
                .setNextToken("0")
                .setMaxResults(10);
        try {
            client.queryUserHonorsWithOptions("user001", queryUserHonorsRequest, queryUserHonorsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.orgCulture_1_0.client import Client as dingtalkorgCulture_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.orgCulture_1_0 import models as dingtalkorg_culture__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkorgCulture_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkorgCulture_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_user_honors_headers = dingtalkorg_culture__1__0_models.QueryUserHonorsHeaders()
        query_user_honors_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_honors_request = dingtalkorg_culture__1__0_models.QueryUserHonorsRequest(
            next_token='0',
            max_results=10
        )
        try:
            client.query_user_honors_with_options('user001', query_user_honors_request, query_user_honors_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_user_honors_headers = dingtalkorg_culture__1__0_models.QueryUserHonorsHeaders()
        query_user_honors_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_honors_request = dingtalkorg_culture__1__0_models.QueryUserHonorsRequest(
            next_token='0',
            max_results=10
        )
        try:
            await client.query_user_honors_with_options_async('user001', query_user_honors_request, query_user_honors_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\QueryUserHonorsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\QueryUserHonorsRequest;
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
        $queryUserHonorsHeaders = new QueryUserHonorsHeaders([]);
        $queryUserHonorsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryUserHonorsRequest = new QueryUserHonorsRequest([
            "nextToken" => "0",
            "maxResults" => 10
        ]);
        try {
            $client->queryUserHonorsWithOptions("user001", $queryUserHonorsRequest, $queryUserHonorsHeaders, new RuntimeOptions([]));
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
  dingtalkorgculture_1_0  "github.com/alibabacloud-go/dingtalk/orgCulture_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkorgculture_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkorgculture_1_0.Client{}
  _result, _err = dingtalkorgculture_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryUserHonorsHeaders := &dingtalkorgculture_1_0.QueryUserHonorsHeaders{}
  queryUserHonorsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryUserHonorsRequest := &dingtalkorgculture_1_0.QueryUserHonorsRequest{
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryUserHonorsWithOptions(tea.String("user001"), queryUserHonorsRequest, queryUserHonorsHeaders, &util.RuntimeOptions{})
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
import dingtalkorgCulture_1_0, * as $dingtalkorgCulture_1_0 from '@alicloud/dingtalk/orgCulture_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkorgCulture_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkorgCulture_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryUserHonorsHeaders = new $dingtalkorgCulture_1_0.QueryUserHonorsHeaders({ });
    queryUserHonorsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryUserHonorsRequest = new $dingtalkorgCulture_1_0.QueryUserHonorsRequest({
      nextToken: "0",
      maxResults: 10,
    });
    try {
      await client.queryUserHonorsWithOptions("user001", queryUserHonorsRequest, queryUserHonorsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryUserHonorsHeaders queryUserHonorsHeaders = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryUserHonorsHeaders();
            queryUserHonorsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryUserHonorsRequest queryUserHonorsRequest = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryUserHonorsRequest
            {
                NextToken = "0",
                MaxResults = 10,
            };
            try
            {
                client.QueryUserHonorsWithOptions("user001", queryUserHonorsRequest, queryUserHonorsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否调用成功，true表示调用成功。 |
| result | Object | 返回结果。 |
| nextToken | String | 下次查询数据的游标。   - 如果未返回该字段，说明没有更多数据。 - 如果返回该字段，说明还有更多数据。 |
| honors | Array | 荣誉信息列表。 |
| grantHistory | Array | 授予历史记录列表。 |
| senderUserid | String | 荣誉发放人userId。 |
| grantTime | Long | 授予时间戳，单位毫秒。 |
| honorId | String | 荣誉Id。 |
| honorName | String | 荣誉名称。 |
| honorDesc | String | 荣誉含义。 |
| expirationTime | Long | 荣誉有效期截止时间戳，单位毫秒。   - 如果未返回该字段，代表永久有效。 - 如果该字段有值，代表有有效截止时间戳。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "nextToken" : "0",
    "honors" : [ {
      "grantHistory" : [ {
        "senderUserid" : "user001",
        "grantTime" : 1645517383000
      } ],
      "honorId" : "31",
      "honorName" : "武林大侠",
      "honorDesc" : "冲锋陷阵真英雄$$深度认知促创新",
      "expirationTime" : 1645517383000
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | parameter.userNotExist | 用户不存在 | 用户不存在 |
| 500 | parameter.userIdBlank | userId为空 | 传入的参数中userId为空 |
| 500 | parameter.nextTokenBlank | nextToken为空 | 传入的参数中nextToken为空 |
| 500 | parameter.maxResultsIllegal | maxResults需小于100 | maxResults的取值范围为1～100 |
| 500 | parameter.illeaglParam | 传入的参数为空 | 传入的参数为空 |
| 500 | system.error | 系统繁忙，请稍后再试 | 系统发生异常 |
