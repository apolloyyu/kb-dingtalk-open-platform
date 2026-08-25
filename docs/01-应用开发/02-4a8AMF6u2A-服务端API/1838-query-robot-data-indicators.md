---
title: "查询机器人基础指标数据"
source_url: "https://open.dingtalk.com/document/development/query-robot-data-indicators"
namespace: "development"
slug: "query-robot-data-indicators"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 小蜜客服 > 查询机器人基础指标数据"
doc_id: "DgpBHY00dh"
updated_at: "2025-09-08 19:06:32"
---

> Source: https://open.dingtalk.com/document/development/query-robot-data-indicators
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 小蜜客服 > 查询机器人基础指标数据
> Updated: 2025-09-08 19:06:32

# 查询机器人基础指标数据

调用本接口根据机器人ID查询某时间段机器人的基础指标数据，例如访问指标数据、问答指标数据等。

查询机器人基础指标数据，如：

### 访问指标数据

• 总服务次数

• 机器人直接解决次数

• 机器人未解决跳出次数

• 机器人解决率

### 问答指标数据

• 咨询问题数

• 机器人知识完全匹配问题数

• 知识完全匹配问题比例

• 未回答问题数

• 有效知识占比

![](https://img.alicdn.com/imgextra/i1/O1CN01dLQbcA1WUmXyBvS1x_!!6000000002792-2-tps-934-424.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 小蜜客服通用权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=dingmi_1.0%23GetDingMeBaseData) |
| 第三方企业应用 | 暂不支持 | 小蜜客服通用权限 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 小蜜客服通用权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/dingmi/robots/data?appKey=String&startDay=String&endDay=String&byDay=Boolean HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appKey | String | 是 | 机器人ID。 |
| startDay | String | 是 | 开始时间。  例如：20211220。 |
| endDay | String | 是 | 结束时间。  例如：20211230。 |
| byDay | Boolean | 是 | 是否按天分组。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| fromCache | Boolean | 是否缓存。 |
| runtime | Long | 运行时间。 |
| rawset | Array of Object | 指标集合。 |
| tips | Map | 字段解释。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/dingmi/robots/data?appKey=ewrjfndjfsndjn&startDay=20210405&endDay=20210506&byDay=true HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:95e96f61bd6f38a496448618e085b3c2
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdingmi_1_0.*;
import com.aliyun.dingtalkdingmi_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdingmi_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdingmi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdingmi_1_0.Client client = Sample.createClient();
        GetDingMeBaseDataHeaders getDingMeBaseDataHeaders = new GetDingMeBaseDataHeaders();
        getDingMeBaseDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetDingMeBaseDataRequest getDingMeBaseDataRequest = new GetDingMeBaseDataRequest()
                .setAppKey("ewrjfndjfsndjn")
                .setStartDay("20210405")
                .setEndDay("20210506")
                .setByDay(true);
        try {
            client.getDingMeBaseDataWithOptions(getDingMeBaseDataRequest, getDingMeBaseDataHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.dingmi_1_0.client import Client as dingtalkdingmi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dingmi_1_0 import models as dingtalkdingmi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdingmi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdingmi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_ding_me_base_data_headers = dingtalkdingmi__1__0_models.GetDingMeBaseDataHeaders()
        get_ding_me_base_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_ding_me_base_data_request = dingtalkdingmi__1__0_models.GetDingMeBaseDataRequest(
            app_key='ewrjfndjfsndjn',
            start_day='20210405',
            end_day='20210506',
            by_day=True
        )
        try:
            client.get_ding_me_base_data_with_options(get_ding_me_base_data_request, get_ding_me_base_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_ding_me_base_data_headers = dingtalkdingmi__1__0_models.GetDingMeBaseDataHeaders()
        get_ding_me_base_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_ding_me_base_data_request = dingtalkdingmi__1__0_models.GetDingMeBaseDataRequest(
            app_key='ewrjfndjfsndjn',
            start_day='20210405',
            end_day='20210506',
            by_day=True
        )
        try:
            await client.get_ding_me_base_data_with_options_async(get_ding_me_base_data_request, get_ding_me_base_data_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\GetDingMeBaseDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdingmi_1_0\Models\GetDingMeBaseDataRequest;
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
        $getDingMeBaseDataHeaders = new GetDingMeBaseDataHeaders([]);
        $getDingMeBaseDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getDingMeBaseDataRequest = new GetDingMeBaseDataRequest([
            "appKey" => "ewrjfndjfsndjn",
            "startDay" => "20210405",
            "endDay" => "20210506",
            "byDay" => true
        ]);
        try {
            $client->getDingMeBaseDataWithOptions($getDingMeBaseDataRequest, $getDingMeBaseDataHeaders, new RuntimeOptions([]));
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
  dingtalkdingmi_1_0  "github.com/alibabacloud-go/dingtalk/dingmi_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdingmi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdingmi_1_0.Client{}
  _result, _err = dingtalkdingmi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getDingMeBaseDataHeaders := &dingtalkdingmi_1_0.GetDingMeBaseDataHeaders{}
  getDingMeBaseDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getDingMeBaseDataRequest := &dingtalkdingmi_1_0.GetDingMeBaseDataRequest{
    AppKey: tea.String("ewrjfndjfsndjn"),
    StartDay: tea.String("20210405"),
    EndDay: tea.String("20210506"),
    ByDay: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetDingMeBaseDataWithOptions(getDingMeBaseDataRequest, getDingMeBaseDataHeaders, &util.RuntimeOptions{})
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
import dingtalkdingmi_1_0, * as $dingtalkdingmi_1_0 from '@alicloud/dingtalk/dingmi_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdingmi_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdingmi_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getDingMeBaseDataHeaders = new $dingtalkdingmi_1_0.GetDingMeBaseDataHeaders({ });
    getDingMeBaseDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getDingMeBaseDataRequest = new $dingtalkdingmi_1_0.GetDingMeBaseDataRequest({
      appKey: "ewrjfndjfsndjn",
      startDay: "20210405",
      endDay: "20210506",
      byDay: true,
    });
    try {
      await client.getDingMeBaseDataWithOptions(getDingMeBaseDataRequest, getDingMeBaseDataHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetDingMeBaseDataHeaders getDingMeBaseDataHeaders = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetDingMeBaseDataHeaders();
            getDingMeBaseDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetDingMeBaseDataRequest getDingMeBaseDataRequest = new AlibabaCloud.SDK.Dingtalkdingmi_1_0.Models.GetDingMeBaseDataRequest
            {
                AppKey = "ewrjfndjfsndjn",
                StartDay = "20210405",
                EndDay = "20210506",
                ByDay = true,
            };
            try
            {
                client.GetDingMeBaseDataWithOptions(getDingMeBaseDataRequest, getDingMeBaseDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdingmi__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdingmi_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdingmi_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdingmi_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::GetDingMeBaseDataHeaders> getDingMeBaseDataHeaders = make_shared<Alibabacloud_Dingtalkdingmi_1_0::GetDingMeBaseDataHeaders>();
  getDingMeBaseDataHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdingmi_1_0::GetDingMeBaseDataRequest> getDingMeBaseDataRequest = make_shared<Alibabacloud_Dingtalkdingmi_1_0::GetDingMeBaseDataRequest>(map<string, boost::any>({
    {"appKey", boost::any(string("ewrjfndjfsndjn"))},
    {"startDay", boost::any(string("20210405"))},
    {"endDay", boost::any(string("20210506"))},
    {"byDay", boost::any(true)}
  }));
  try {
    client->getDingMeBaseDataWithOptions(getDingMeBaseDataRequest, getDingMeBaseDataHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "fromCache" : true,
  "runtime" : 23,
  "rawset" : [ {
    "key" : "0.34"
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.illegal | 参数错误：%s | 接口参数错误 |
| 400 | executor.error | 执行错误 | 取数执行错误 |
| 500 | systerm.error | 系统错误 | 系统错误 |
