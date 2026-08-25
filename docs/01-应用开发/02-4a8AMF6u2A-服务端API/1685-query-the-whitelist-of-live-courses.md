---
title: "查询直播课程的可观看白名单"
source_url: "https://open.dingtalk.com/document/development/query-the-whitelist-of-live-courses"
namespace: "development"
slug: "query-the-whitelist-of-live-courses"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 培训 > 查询直播课程的可观看白名单"
doc_id: "9TYOowL6HI"
updated_at: "2025-10-17 17:01:02"
---

> Source: https://open.dingtalk.com/document/development/query-the-whitelist-of-live-courses
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 培训 > 查询直播课程的可观看白名单
> Updated: 2025-10-17 17:01:02

# 查询直播课程的可观看白名单

调用本接口查询直播课程可观看白名单。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，查询直播课程的可观看白名单接口正在升级，本API文档已于2022年9月23日移动至历史文档（不推荐）目录，接口不再支持新应用接入，已接入的应用可继续调用。新产品开放上线时间请关注更新日志。

> **[!NOTE]**
>
> - 以个人用户为维度，可查询某用户是否在观看白名单之内。
> - 如果没有设置白名单，查询到为false，但是用户在组织内，组织维度的直播课程是可观看的。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 暂不支持 | 直播培训平台读权限 | 暂不支持 |
| 第三方企业应用 | 支持 | 直播培训平台读权限 | — |
| 第三方个人应用 | 暂不支持 | 直播培训平台读权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/live/openFeeds/{feedId}/whiteList?userId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| feedId | String | 是 | 直播课程id，可通过[创建培训课程](https://open.dingtalk.com/document/isvapp/create-live-courses)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 组织内用户的userid。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Boolean | 是否在白名单内。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/live/openFeeds/8c0ed3c3-e125/whiteList?userId=12061863517 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bf360b06a0663cd0a09afb
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalklive_1_0.*;
import com.aliyun.dingtalklive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalklive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalklive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalklive_1_0.Client client = Sample.createClient();
        QueryFeedWhiteListHeaders queryFeedWhiteListHeaders = new QueryFeedWhiteListHeaders();
        queryFeedWhiteListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryFeedWhiteListRequest queryFeedWhiteListRequest = new QueryFeedWhiteListRequest()
                .setUserId("12061863517");
        try {
            client.queryFeedWhiteListWithOptions("8c0ed3c3-e125", queryFeedWhiteListRequest, queryFeedWhiteListHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.live_1_0.client import Client as dingtalklive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.live_1_0 import models as dingtalklive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalklive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalklive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_feed_white_list_headers = dingtalklive__1__0_models.QueryFeedWhiteListHeaders()
        query_feed_white_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_feed_white_list_request = dingtalklive__1__0_models.QueryFeedWhiteListRequest(
            user_id='12061863517'
        )
        try:
            client.query_feed_white_list_with_options('8c0ed3c3-e125', query_feed_white_list_request, query_feed_white_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_feed_white_list_headers = dingtalklive__1__0_models.QueryFeedWhiteListHeaders()
        query_feed_white_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_feed_white_list_request = dingtalklive__1__0_models.QueryFeedWhiteListRequest(
            user_id='12061863517'
        )
        try:
            await client.query_feed_white_list_with_options_async('8c0ed3c3-e125', query_feed_white_list_request, query_feed_white_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\QueryFeedWhiteListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\QueryFeedWhiteListRequest;
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
        $queryFeedWhiteListHeaders = new QueryFeedWhiteListHeaders([]);
        $queryFeedWhiteListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryFeedWhiteListRequest = new QueryFeedWhiteListRequest([
            "userId" => "12061863517"
        ]);
        try {
            $client->queryFeedWhiteListWithOptions("8c0ed3c3-e125", $queryFeedWhiteListRequest, $queryFeedWhiteListHeaders, new RuntimeOptions([]));
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
  dingtalklive_1_0  "github.com/alibabacloud-go/dingtalk/live_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalklive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalklive_1_0.Client{}
  _result, _err = dingtalklive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryFeedWhiteListHeaders := &dingtalklive_1_0.QueryFeedWhiteListHeaders{}
  queryFeedWhiteListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryFeedWhiteListRequest := &dingtalklive_1_0.QueryFeedWhiteListRequest{
    UserId: tea.String("12061863517"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryFeedWhiteListWithOptions(tea.String("8c0ed3c3-e125"), queryFeedWhiteListRequest, queryFeedWhiteListHeaders, &util.RuntimeOptions{})
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
import dingtalklive_1_0, * as $dingtalklive_1_0 from '@alicloud/dingtalk/live_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalklive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalklive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryFeedWhiteListHeaders = new $dingtalklive_1_0.QueryFeedWhiteListHeaders({ });
    queryFeedWhiteListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryFeedWhiteListRequest = new $dingtalklive_1_0.QueryFeedWhiteListRequest({
      userId: "12061863517",
    });
    try {
      await client.queryFeedWhiteListWithOptions("8c0ed3c3-e125", queryFeedWhiteListRequest, queryFeedWhiteListHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalklive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalklive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalklive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryFeedWhiteListHeaders queryFeedWhiteListHeaders = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryFeedWhiteListHeaders();
            queryFeedWhiteListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryFeedWhiteListRequest queryFeedWhiteListRequest = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.QueryFeedWhiteListRequest
            {
                UserId = "12061863517",
            };
            try
            {
                client.QueryFeedWhiteListWithOptions("8c0ed3c3-e125", queryFeedWhiteListRequest, queryFeedWhiteListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalklive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalklive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalklive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalklive_1_0::Client> client = make_shared<Alibabacloud_Dingtalklive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalklive_1_0::QueryFeedWhiteListHeaders> queryFeedWhiteListHeaders = make_shared<Alibabacloud_Dingtalklive_1_0::QueryFeedWhiteListHeaders>();
  queryFeedWhiteListHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalklive_1_0::QueryFeedWhiteListRequest> queryFeedWhiteListRequest = make_shared<Alibabacloud_Dingtalklive_1_0::QueryFeedWhiteListRequest>(map<string, boost::any>({
    {"userId", boost::any(string("12061863517"))}
  }));
  try {
    client->queryFeedWhiteListWithOptions(make_shared<string>("8c0ed3c3-e125"), queryFeedWhiteListRequest, queryFeedWhiteListHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgSuiteAuthNotExit | access forbidden | 组织无权限访问 |
| 500 | systemError | error:%s | 系统错误 |
