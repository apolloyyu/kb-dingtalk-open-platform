---
title: "搜索第三方火车票超标审批单"
source_url: "https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-train-get"
namespace: "development"
slug: "dingtalk-oapi-alitrip-btrip-exceedapply-train-get"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 搜索第三方火车票超标审批单"
doc_id: "cs654StwW5"
updated_at: "2026-01-29 14:31:00"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-train-get
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 搜索第三方火车票超标审批单
> Updated: 2026-01-29 14:31:00

# 搜索第三方火车票超标审批单

通过此接口查询第三方火车票超标审批单的详细信息，支持根据企业corpId和商旅审批单applyId获取审批状态、出行意向、超标原因等关键数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/exceedapply/getTrain |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限点 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 第三方企业的`corpId`。 |
| applyId | String | 是 | 商旅审批单ID，用于唯一标识一条审批记录。 |

### 请求示例

HTTP

```
GET /v1.0/alitrip/exceedapply/getTrain?corpId=ding1234&applyId=12345 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dca268xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkalitrip_1_0.*;
import com.aliyun.dingtalkalitrip_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkalitrip_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkalitrip_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkalitrip_1_0.Client client = Sample.createClient();
        GetTrainExceedApplyHeaders getTrainExceedApplyHeaders = new GetTrainExceedApplyHeaders();
        getTrainExceedApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetTrainExceedApplyRequest getTrainExceedApplyRequest = new GetTrainExceedApplyRequest()
                .setCorpId("ding1234")
                .setApplyId("12345");
        try {
            client.getTrainExceedApplyWithOptions(getTrainExceedApplyRequest, getTrainExceedApplyHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.alitrip_1_0.client import Client as dingtalkalitrip_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.alitrip_1_0 import models as dingtalkalitrip__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkalitrip_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkalitrip_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_train_exceed_apply_headers = dingtalkalitrip__1__0_models.GetTrainExceedApplyHeaders()
        get_train_exceed_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_train_exceed_apply_request = dingtalkalitrip__1__0_models.GetTrainExceedApplyRequest(
            corp_id='ding1234',
            apply_id='12345'
        )
        try:
            client.get_train_exceed_apply_with_options(get_train_exceed_apply_request, get_train_exceed_apply_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_train_exceed_apply_headers = dingtalkalitrip__1__0_models.GetTrainExceedApplyHeaders()
        get_train_exceed_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_train_exceed_apply_request = dingtalkalitrip__1__0_models.GetTrainExceedApplyRequest(
            corp_id='ding1234',
            apply_id='12345'
        )
        try:
            await client.get_train_exceed_apply_with_options_async(get_train_exceed_apply_request, get_train_exceed_apply_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\GetTrainExceedApplyHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\GetTrainExceedApplyRequest;
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
        $getTrainExceedApplyHeaders = new GetTrainExceedApplyHeaders([]);
        $getTrainExceedApplyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getTrainExceedApplyRequest = new GetTrainExceedApplyRequest([
            "corpId" => "ding1234",
            "applyId" => "12345"
        ]);
        try {
            $client->getTrainExceedApplyWithOptions($getTrainExceedApplyRequest, $getTrainExceedApplyHeaders, new RuntimeOptions([]));
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
  dingtalkalitrip_1_0  "github.com/alibabacloud-go/dingtalk/alitrip_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkalitrip_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkalitrip_1_0.Client{}
  _result, _err = dingtalkalitrip_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getTrainExceedApplyHeaders := &dingtalkalitrip_1_0.GetTrainExceedApplyHeaders{}
  getTrainExceedApplyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getTrainExceedApplyRequest := &dingtalkalitrip_1_0.GetTrainExceedApplyRequest{
    CorpId: tea.String("ding1234"),
    ApplyId: tea.String("12345"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetTrainExceedApplyWithOptions(getTrainExceedApplyRequest, getTrainExceedApplyHeaders, &util.RuntimeOptions{})
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
import dingtalkalitrip_1_0, * as $dingtalkalitrip_1_0 from '@alicloud/dingtalk/alitrip_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkalitrip_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkalitrip_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getTrainExceedApplyHeaders = new $dingtalkalitrip_1_0.GetTrainExceedApplyHeaders({ });
    getTrainExceedApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getTrainExceedApplyRequest = new $dingtalkalitrip_1_0.GetTrainExceedApplyRequest({
      corpId: "ding1234",
      applyId: "12345",
    });
    try {
      await client.getTrainExceedApplyWithOptions(getTrainExceedApplyRequest, getTrainExceedApplyHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.GetTrainExceedApplyHeaders getTrainExceedApplyHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.GetTrainExceedApplyHeaders();
            getTrainExceedApplyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.GetTrainExceedApplyRequest getTrainExceedApplyRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.GetTrainExceedApplyRequest
            {
                CorpId = "ding1234",
                ApplyId = "12345",
            };
            try
            {
                client.GetTrainExceedApplyWithOptions(getTrainExceedApplyRequest, getTrainExceedApplyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkalitrip__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkalitrip_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkalitrip_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::Client> client = make_shared<Alibabacloud_Dingtalkalitrip_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::GetTrainExceedApplyHeaders> getTrainExceedApplyHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::GetTrainExceedApplyHeaders>();
  getTrainExceedApplyHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::GetTrainExceedApplyRequest> getTrainExceedApplyRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::GetTrainExceedApplyRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding1234"))},
    {"applyId", boost::any(string("12345"))}
  }));
  try {
    client->getTrainExceedApplyWithOptions(getTrainExceedApplyRequest, getTrainExceedApplyHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| corpId | String | 第三方企业的`corpId`。 |
| applyId | Long | 商旅超标审批单ID。 |
| status | Integer | 审批单状态，取值：   - **0**：审批中 - **1**：已同意 - **2**：已拒绝 |
| btripCause | String | 出差原因。 |
| exceedType | Integer | 超标类型，取值：   - **32**：坐席超标。 |
| exceedReason | String | 超标原因。 |
| originStandard | String | 原差旅标准。 |
| submitTime | String | 审批单提交时间。 |
| userId | String | 第三方用户的userid。 |
| applyIntentionInfoDO | Object | 意向出行信息。 |
| price | Long | 意向坐席价格（分）。 |
| depCityName | String | 出发城市名。 |
| arrCityName | String | 到达城市名。 |
| depCity | String | 出发城市三字码。 |
| arrCity | String | 到达城市三字码。 |
| depTime | String | 出发时间。 |
| arrTime | String | 到达时间。 |
| arrStation | String | 到达站点名称。 |
| depStation | String | 出发站点名称。 |
| trainNo | String | 意向车次号。 |
| trainTypeDesc | String | 意向车次类型。 |
| seatName | String | 意向坐席名称。 |
| thirdpartApplyId | String | 第三方出差审批单号。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "corpId" : "ding12345",
  "applyId" : 1234567,
  "status" : 0,
  "btripCause" : "出差",
  "exceedType" : 32,
  "exceedReason" : "出差",
  "originStandard" : "二等座",
  "submitTime" : "2021-07-08 15:23:56",
  "userId" : "weifeng",
  "applyIntentionInfoDO" : {
    "price" : 1000,
    "depCityName" : "上海",
    "arrCityName" : "北京",
    "depCity" : "SHA",
    "arrCity" : "BJS",
    "depTime" : "2021-07-13 15:06:13",
    "arrTime" : "2021-07-13 15:06:13",
    "arrStation" : "上海南",
    "depStation" : "北京南",
    "trainNo" : "G39",
    "trainTypeDesc" : "高铁",
    "seatName" : "一等座"
  },
  "thirdpartApplyId" : "0001A11xxx"
}
```
