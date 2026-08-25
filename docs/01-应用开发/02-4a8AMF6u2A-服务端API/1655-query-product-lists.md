---
title: "查询商品列表"
source_url: "https://open.dingtalk.com/document/development/query-product-lists"
namespace: "development"
slug: "query-product-lists"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 权益 > 查询商品列表"
doc_id: "9ydJMEpFoU"
updated_at: "2025-09-08 19:03:57"
---

> Source: https://open.dingtalk.com/document/development/query-product-lists
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 权益 > 查询商品列表
> Updated: 2025-09-08 19:03:57

# 查询商品列表

调用本接口查询商品列表。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，宜搭接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 宜搭接口相关文档，已于**2022年3月14日**迁移至**历史文档（不推荐）**目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | 暂不支持 |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
GET /v1.0/yida/appAuth/commodities?accessKey=String&pageSize=Integer&callerUid=String&currentPage=Integer HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)获取。 - 第三方企业应用调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| accessKey | String | 否 | 访问秘钥。 |
| pageSize | Integer | 否 | 分页大小。 |
| callerUid | String | 否 | 调用者的unionId。 |
| pageNumber | Integer | 否 | 分页页码。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| pageSize | Integer | 分页大小。 |
| commodityVOList | Array | 商品列表。 |
| instanceId | String | 实例ID。 |
| buyDateGMT | String | 购买日期。 |
| expireDateGMT | String | 过期日期。 |
| activationCode | String | 激活码。 |
| accountNumber | Integer | 账户号。 |
| accountDistributionNumber | Integer | 账户分配号。 |
| version | Integer | 版本。 |
| status | String | 状态。 |
| pageNumber | Integer | 当前第几页。 |
| totalCount | Integer | 总数量。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/yida/appAuth/commodities?accessKey=hexaaaa&pageSize=100&callerUid=44234122&pageNumber=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkyida_1_0.*;
import com.aliyun.dingtalkyida_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkyida_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkyida_1_0.Client client = Sample.createClient();
        ListCommodityHeaders listCommodityHeaders = new ListCommodityHeaders();
        listCommodityHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListCommodityRequest listCommodityRequest = new ListCommodityRequest()
                .setAccessKey("hexaaaa")
                .setPageSize(100)
                .setCallerUid("44234122")
                .setPageNumber(1);
        try {
            client.listCommodityWithOptions(listCommodityRequest, listCommodityHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_commodity_headers = dingtalkyida__1__0_models.ListCommodityHeaders()
        list_commodity_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_commodity_request = dingtalkyida__1__0_models.ListCommodityRequest(
            access_key='hexaaaa',
            page_size=100,
            caller_uid='44234122',
            page_number=1
        )
        try:
            client.list_commodity_with_options(list_commodity_request, list_commodity_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_commodity_headers = dingtalkyida__1__0_models.ListCommodityHeaders()
        list_commodity_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_commodity_request = dingtalkyida__1__0_models.ListCommodityRequest(
            access_key='hexaaaa',
            page_size=100,
            caller_uid='44234122',
            page_number=1
        )
        try:
            await client.list_commodity_with_options_async(list_commodity_request, list_commodity_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\ListCommodityHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\ListCommodityRequest;
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
        $listCommodityHeaders = new ListCommodityHeaders([]);
        $listCommodityHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listCommodityRequest = new ListCommodityRequest([
            "accessKey" => "hexaaaa",
            "pageSize" => 100,
            "callerUid" => "44234122",
            "pageNumber" => 1
        ]);
        try {
            $client->listCommodityWithOptions($listCommodityRequest, $listCommodityHeaders, new RuntimeOptions([]));
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
  dingtalkyida_1_0  "github.com/alibabacloud-go/dingtalk/yida_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkyida_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_1_0.Client{}
  _result, _err = dingtalkyida_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listCommodityHeaders := &dingtalkyida_1_0.ListCommodityHeaders{}
  listCommodityHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listCommodityRequest := &dingtalkyida_1_0.ListCommodityRequest{
    AccessKey: tea.String("hexaaaa"),
    PageSize: tea.Int32(100),
    CallerUid: tea.String("44234122"),
    PageNumber: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListCommodityWithOptions(listCommodityRequest, listCommodityHeaders, &util.RuntimeOptions{})
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
import dingtalkyida_1_0, * as $dingtalkyida_1_0 from '@alicloud/dingtalk/yida_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkyida_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkyida_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listCommodityHeaders = new $dingtalkyida_1_0.ListCommodityHeaders({ });
    listCommodityHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listCommodityRequest = new $dingtalkyida_1_0.ListCommodityRequest({
      accessKey: "hexaaaa",
      pageSize: 100,
      callerUid: "44234122",
      pageNumber: 1,
    });
    try {
      await client.listCommodityWithOptions(listCommodityRequest, listCommodityHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ListCommodityHeaders listCommodityHeaders = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ListCommodityHeaders();
            listCommodityHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ListCommodityRequest listCommodityRequest = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ListCommodityRequest
            {
                AccessKey = "hexaaaa",
                PageSize = 100,
                CallerUid = "44234122",
                PageNumber = 1,
            };
            try
            {
                client.ListCommodityWithOptions(listCommodityRequest, listCommodityHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkyida__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkyida_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkyida_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::Client> client = make_shared<Alibabacloud_Dingtalkyida_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::ListCommodityHeaders> listCommodityHeaders = make_shared<Alibabacloud_Dingtalkyida_1_0::ListCommodityHeaders>();
  listCommodityHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::ListCommodityRequest> listCommodityRequest = make_shared<Alibabacloud_Dingtalkyida_1_0::ListCommodityRequest>(map<string, boost::any>({
    {"accessKey", boost::any(string("hexaaaa"))},
    {"pageSize", boost::any(100)},
    {"callerUid", boost::any(string("44234122"))},
    {"pageNumber", boost::any(1)}
  }));
  try {
    client->listCommodityWithOptions(listCommodityRequest, listCommodityHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "pageSize" : 100,
  "commodityVOList" : [ {
    "instanceId" : "12",
    "buyDateGMT" : "2021-01-01",
    "expireDateGMT" : "2021-01-01",
    "activationCode" : "acc-BNDJUxxx",
    "accountNumber" : 123,
    "accountDistributionNumber" : 123,
    "version" : 1,
    "status" : "running"
  } ],
  "pageNumber" : 1,
  "totalCount" : 10
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | unclassifiedError | 异常:%s | 通用异常信息 |
