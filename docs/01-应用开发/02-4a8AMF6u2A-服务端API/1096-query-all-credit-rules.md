---
title: "查询组织维度配置的所有积分规则"
source_url: "https://open.dingtalk.com/document/development/query-all-credit-rules"
namespace: "development"
slug: "query-all-credit-rules"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 数字乡村 > 居民积分 > 查询组织维度配置的所有积分规则"
doc_id: "WePfaAgPwK"
updated_at: "2025-09-23 19:22:11"
---

> Source: https://open.dingtalk.com/document/development/query-all-credit-rules
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 数字乡村 > 居民积分 > 查询组织维度配置的所有积分规则
> Updated: 2025-09-23 19:22:11

# 查询组织维度配置的所有积分规则

在全员圈和积分管理场景下，可调用本接口查询组织维度配置的的积分规则。查询结果不分页，查询出该组织下所有的规则。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/resident/points/rules |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Village.Point.Read-数字区县居民积分读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| isCircle | Boolean | 是 | 是否查询全员圈积分规则，否则查询积分管理积分规则，取值：   - **true**：是 - **false**：否（默认值） |

### 请求示例

HTTP

```
GET /v1.0/resident/points/rules?isCircle=false HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE567xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkresident_1_0.*;
import com.aliyun.dingtalkresident_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkresident_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkresident_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkresident_1_0.Client client = Sample.createClient();
        ListPointRulesHeaders listPointRulesHeaders = new ListPointRulesHeaders();
        listPointRulesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListPointRulesRequest listPointRulesRequest = new ListPointRulesRequest()
                .setIsCircle(false);
        try {
            client.listPointRulesWithOptions(listPointRulesRequest, listPointRulesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.resident_1_0.client import Client as dingtalkresident_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.resident_1_0 import models as dingtalkresident__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkresident_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkresident_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_point_rules_headers = dingtalkresident__1__0_models.ListPointRulesHeaders()
        list_point_rules_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_point_rules_request = dingtalkresident__1__0_models.ListPointRulesRequest(
            is_circle=False
        )
        try:
            client.list_point_rules_with_options(list_point_rules_request, list_point_rules_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_point_rules_headers = dingtalkresident__1__0_models.ListPointRulesHeaders()
        list_point_rules_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_point_rules_request = dingtalkresident__1__0_models.ListPointRulesRequest(
            is_circle=False
        )
        try:
            await client.list_point_rules_with_options_async(list_point_rules_request, list_point_rules_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\ListPointRulesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\ListPointRulesRequest;
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
        $listPointRulesHeaders = new ListPointRulesHeaders([]);
        $listPointRulesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listPointRulesRequest = new ListPointRulesRequest([
            "isCircle" => false
        ]);
        try {
            $client->listPointRulesWithOptions($listPointRulesRequest, $listPointRulesHeaders, new RuntimeOptions([]));
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
  dingtalkresident_1_0  "github.com/alibabacloud-go/dingtalk/resident_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkresident_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkresident_1_0.Client{}
  _result, _err = dingtalkresident_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listPointRulesHeaders := &dingtalkresident_1_0.ListPointRulesHeaders{}
  listPointRulesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listPointRulesRequest := &dingtalkresident_1_0.ListPointRulesRequest{
    IsCircle: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListPointRulesWithOptions(listPointRulesRequest, listPointRulesHeaders, &util.RuntimeOptions{})
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
import dingtalkresident_1_0, * as $dingtalkresident_1_0 from '@alicloud/dingtalk/resident_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkresident_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkresident_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listPointRulesHeaders = new $dingtalkresident_1_0.ListPointRulesHeaders({ });
    listPointRulesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listPointRulesRequest = new $dingtalkresident_1_0.ListPointRulesRequest({
      isCircle: false,
    });
    try {
      await client.listPointRulesWithOptions(listPointRulesRequest, listPointRulesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkresident_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkresident_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkresident_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListPointRulesHeaders listPointRulesHeaders = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListPointRulesHeaders();
            listPointRulesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListPointRulesRequest listPointRulesRequest = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.ListPointRulesRequest
            {
                IsCircle = false,
            };
            try
            {
                client.ListPointRulesWithOptions(listPointRulesRequest, listPointRulesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| pointRuleList | Array | 积分规则列表。 |
| score | Integer | 增加或减少的分数。  **[!NOTE]**    增加为正数，减少为负数。 |
| dayLimitTimes | Integer | 单日计次上限，0表示无上限。 |
| status | Integer | 生效状态 ，取值：   - **0**：不生效 - **1**：生效 |
| ruleCode | String | 对应的行为代码。 |
| ruleName | String | 对应的行为名字。 |
| extension | String | 扩展字段。 |
| groupId | Integer | 分组ID。 |
| orderId | Integer | 排序ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "pointRuleList" : [ {
    "score" : 3,
    "dayLimitTimes" : 50,
    "status" : 0,
    "ruleCode" : "rule_1",
    "ruleName" : "发动态",
    "extension" : "text",
    "groupId" : 100
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgInvalid.param.error | %s | 组织非百姓通组织 |
| 400 | checkParameter.param.error | %s | 参数校验失败 |
| 400 | point.system.error | 积分服务请求失败 %s | 积分服务请求失败 |
| 500 | sytem.error | system error %s | 系统错误 |
