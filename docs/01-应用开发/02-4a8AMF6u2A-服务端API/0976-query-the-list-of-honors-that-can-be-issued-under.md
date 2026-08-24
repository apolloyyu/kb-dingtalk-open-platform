---
title: "查询当前企业下可颁发的荣誉列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-honors-that-can-be-issued-under"
namespace: "development"
slug: "query-the-list-of-honors-that-can-be-issued-under"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 荣誉 > 查询当前企业下可颁发的荣誉列表"
doc_id: "0TbFdQelVe"
updated_at: "2026-06-04 19:10:40"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-honors-that-can-be-issued-under
> Path: 应用开发 / 服务端API / 企业文化 > 荣誉 > 查询当前企业下可颁发的荣誉列表
> Updated: 2026-06-04 19:10:40

# 查询当前企业下可颁发的荣誉列表

用于查询当前企业下可颁发的荣誉列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/orgCulture/organizations/honors |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-OrgCulture.Honor.Read-组织文化荣誉信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 是 | 分页游标。   - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上次调用时接口返回的nextToken值。 |
| maxResults | Integer | 否 | 每页最大条目数，默认值20， 最大值100。 |

### 请求示例

HTTP

```
GET /v1.0/orgCulture/organizations/honors?nextToken=0&maxResults=10 HTTP/1.1
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
        QueryOrgHonorsHeaders queryOrgHonorsHeaders = new QueryOrgHonorsHeaders();
        queryOrgHonorsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryOrgHonorsRequest queryOrgHonorsRequest = new QueryOrgHonorsRequest()
                .setNextToken("0")
                .setMaxResults(10);
        try {
            client.queryOrgHonorsWithOptions(queryOrgHonorsRequest, queryOrgHonorsHeaders, new RuntimeOptions());
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
        query_org_honors_headers = dingtalkorg_culture__1__0_models.QueryOrgHonorsHeaders()
        query_org_honors_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_org_honors_request = dingtalkorg_culture__1__0_models.QueryOrgHonorsRequest(
            next_token='0',
            max_results=10
        )
        try:
            client.query_org_honors_with_options(query_org_honors_request, query_org_honors_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_org_honors_headers = dingtalkorg_culture__1__0_models.QueryOrgHonorsHeaders()
        query_org_honors_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_org_honors_request = dingtalkorg_culture__1__0_models.QueryOrgHonorsRequest(
            next_token='0',
            max_results=10
        )
        try:
            await client.query_org_honors_with_options_async(query_org_honors_request, query_org_honors_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\QueryOrgHonorsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\QueryOrgHonorsRequest;
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
        $queryOrgHonorsHeaders = new QueryOrgHonorsHeaders([]);
        $queryOrgHonorsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryOrgHonorsRequest = new QueryOrgHonorsRequest([
            "nextToken" => "0",
            "maxResults" => 10
        ]);
        try {
            $client->queryOrgHonorsWithOptions($queryOrgHonorsRequest, $queryOrgHonorsHeaders, new RuntimeOptions([]));
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

  queryOrgHonorsHeaders := &dingtalkorgculture_1_0.QueryOrgHonorsHeaders{}
  queryOrgHonorsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryOrgHonorsRequest := &dingtalkorgculture_1_0.QueryOrgHonorsRequest{
    NextToken: tea.String("0"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryOrgHonorsWithOptions(queryOrgHonorsRequest, queryOrgHonorsHeaders, &util.RuntimeOptions{})
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
    let queryOrgHonorsHeaders = new $dingtalkorgCulture_1_0.QueryOrgHonorsHeaders({ });
    queryOrgHonorsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryOrgHonorsRequest = new $dingtalkorgCulture_1_0.QueryOrgHonorsRequest({
      nextToken: "0",
      maxResults: 10,
    });
    try {
      await client.queryOrgHonorsWithOptions(queryOrgHonorsRequest, queryOrgHonorsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryOrgHonorsHeaders queryOrgHonorsHeaders = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryOrgHonorsHeaders();
            queryOrgHonorsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryOrgHonorsRequest queryOrgHonorsRequest = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.QueryOrgHonorsRequest
            {
                NextToken = "0",
                MaxResults = 10,
            };
            try
            {
                client.QueryOrgHonorsWithOptions(queryOrgHonorsRequest, queryOrgHonorsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkorg_culture__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkorg_culture_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkorg_culture_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkorg_culture_1_0::Client> client = make_shared<Alibabacloud_Dingtalkorg_culture_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkorg_culture_1_0::QueryOrgHonorsHeaders> queryOrgHonorsHeaders = make_shared<Alibabacloud_Dingtalkorg_culture_1_0::QueryOrgHonorsHeaders>();
  queryOrgHonorsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkorg_culture_1_0::QueryOrgHonorsRequest> queryOrgHonorsRequest = make_shared<Alibabacloud_Dingtalkorg_culture_1_0::QueryOrgHonorsRequest>(map<string, boost::any>({
    {"nextToken", boost::any(string("0"))},
    {"maxResults", boost::any(10)}
  }));
  try {
    client->queryOrgHonorsWithOptions(queryOrgHonorsRequest, queryOrgHonorsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 调用是否成功，true表示成功。 |
| result | Object | 返回结果。 |
| nextToken | String | 下次查询数据的游标。   - 如果未返回该字段，说明没有更多数据。 - 如果返回该字段，说明有更多数据。 |
| openHonors | Array | 荣誉信息列表。 |
| honorId | Long | 荣誉Id。 |
| honorImgUrl | String | 荣誉图标URL。 |
| honorPendantImgUrl | String | 荣誉附赠的挂件图URL。 |
| honorName | String | 荣誉名字。 |
| honorDesc | String | 荣誉含义。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "nextToken" : "0",
    "openHonors" : [ {
      "honorId" : 31,
      "honorImgUrl" : "https://static.dingtalk.com/media/lALPGpNycGGaBPbNA3vNA3s_891_891.png",
      "honorPendantImgUrl" : "https://static.dingtalk.com/media/lAHPGoGu9yrPwsDM8Mzw_240_240.gif",
      "honorName" : "潜力之星",
      "honorDesc" : "认真严谨潜力无穷"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | parameter.illegalRequest | 传入的参数为空 | 传入的参数为空 |
| 500 | parameter.nextTokenBlank | 传入的参数中nextToken为空 | 传入的参数中nextToken为空 |
| 500 | parameter.maxResultsIllegal | 传入的参数中maxResults需小于100 | 传入的参数中maxResults需小于100 |
| 500 | system.error | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
