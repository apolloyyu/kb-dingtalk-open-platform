---
title: "增加或减少居民积分"
source_url: "https://open.dingtalk.com/document/development/increase-or-decrease-resident-points"
namespace: "development"
slug: "increase-or-decrease-resident-points"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 数字乡村 > 居民积分 > 增加或减少居民积分"
doc_id: "bpVpopnvyJ"
updated_at: "2025-09-23 19:22:11"
---

> Source: https://open.dingtalk.com/document/development/increase-or-decrease-resident-points
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 数字乡村 > 居民积分 > 增加或减少居民积分
> Updated: 2025-09-23 19:22:11

# 增加或减少居民积分

在积分管理或者全员圈场景中，可调用本接口添加居民积分。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/resident/points |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Village.Point.Write-数字区县居民积分写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| isCircle | Boolean | 是 | 是否查询全员圈积分规则，取值：   - **true**：是 - **false**：否（默认值）   **[!NOTE]**  取值为false时，查询积分管理积分规则。 |
| uuid | String | 是 | 加减积分的唯一幂等标志，由调用方自己生成。 |
| userId | String | 是 | 用户userid，可通过调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| ruleCode | String | 否 | 规则代码。可以为空。  **[!NOTE]**    如果不为空的话，**score**值使用**ruleCode**对应的**score**增加分数。 |
| ruleName | String | 是 | 规则名字。 |
| actionTime | Long | 否 | 增加积分的时间戳，单位毫秒。  **[!NOTE]**    如果不传使用系统当前毫秒数。 |
| score | Integer | 是 | 本次增加积分。   - 如果为正数表示增加积分。 - 如果为负数表示扣减积分。 |

### 请求示例

HTTP

```
POST /v1.0/resident/points?isCircle=false&uuid=7645&userId=123&ruleCode=rule_1&ruleName=发动态&actionTime=1634630147&score=3 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE78xxx
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
        AddPointHeaders addPointHeaders = new AddPointHeaders();
        addPointHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddPointRequest addPointRequest = new AddPointRequest()
                .setIsCircle(false)
                .setUuid("7645")
                .setUserId("123")
                .setRuleCode("rule_1")
                .setRuleName("发动态")
                .setActionTime(1634630147L)
                .setScore(3);
        try {
            client.addPointWithOptions(addPointRequest, addPointHeaders, new RuntimeOptions());
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
        add_point_headers = dingtalkresident__1__0_models.AddPointHeaders()
        add_point_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_point_request = dingtalkresident__1__0_models.AddPointRequest(
            is_circle=False,
            uuid='7645',
            user_id='123',
            rule_code='rule_1',
            rule_name='发动态',
            action_time=1634630147,
            score=3
        )
        try:
            client.add_point_with_options(add_point_request, add_point_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_point_headers = dingtalkresident__1__0_models.AddPointHeaders()
        add_point_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_point_request = dingtalkresident__1__0_models.AddPointRequest(
            is_circle=False,
            uuid='7645',
            user_id='123',
            rule_code='rule_1',
            rule_name='发动态',
            action_time=1634630147,
            score=3
        )
        try:
            await client.add_point_with_options_async(add_point_request, add_point_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\AddPointHeaders;
use AlibabaCloud\SDK\Dingtalk\Vresident_1_0\Models\AddPointRequest;
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
        $addPointHeaders = new AddPointHeaders([]);
        $addPointHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addPointRequest = new AddPointRequest([
            "isCircle" => false,
            "uuid" => "7645",
            "userId" => "123",
            "ruleCode" => "rule_1",
            "ruleName" => "发动态",
            "actionTime" => 1634630147,
            "score" => 3
        ]);
        try {
            $client->addPointWithOptions($addPointRequest, $addPointHeaders, new RuntimeOptions([]));
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

  addPointHeaders := &dingtalkresident_1_0.AddPointHeaders{}
  addPointHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addPointRequest := &dingtalkresident_1_0.AddPointRequest{
    IsCircle: tea.Bool(false),
    Uuid: tea.String("7645"),
    UserId: tea.String("123"),
    RuleCode: tea.String("rule_1"),
    RuleName: tea.String("发动态"),
    ActionTime: tea.Int64(1634630147),
    Score: tea.Int32(3),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddPointWithOptions(addPointRequest, addPointHeaders, &util.RuntimeOptions{})
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
    let addPointHeaders = new $dingtalkresident_1_0.AddPointHeaders({ });
    addPointHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let addPointRequest = new $dingtalkresident_1_0.AddPointRequest({
      isCircle: false,
      uuid: "7645",
      userId: "123",
      ruleCode: "rule_1",
      ruleName: "发动态",
      actionTime: 1634630147,
      score: 3,
    });
    try {
      await client.addPointWithOptions(addPointRequest, addPointHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.AddPointHeaders addPointHeaders = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.AddPointHeaders();
            addPointHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkresident_1_0.Models.AddPointRequest addPointRequest = new AlibabaCloud.SDK.Dingtalkresident_1_0.Models.AddPointRequest
            {
                IsCircle = false,
                Uuid = "7645",
                UserId = "123",
                RuleCode = "rule_1",
                RuleName = "发动态",
                ActionTime = 1634630147,
                Score = 3,
            };
            try
            {
                client.AddPointWithOptions(addPointRequest, addPointHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkresident__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkresident_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkresident_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkresident_1_0::Client> client = make_shared<Alibabacloud_Dingtalkresident_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkresident_1_0::AddPointHeaders> addPointHeaders = make_shared<Alibabacloud_Dingtalkresident_1_0::AddPointHeaders>();
  addPointHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkresident_1_0::AddPointRequest> addPointRequest = make_shared<Alibabacloud_Dingtalkresident_1_0::AddPointRequest>(map<string, boost::any>({
    {"isCircle", boost::any(false)},
    {"uuid", boost::any(string("7645"))},
    {"userId", boost::any(string("123"))},
    {"ruleCode", boost::any(string("rule_1"))},
    {"ruleName", boost::any(string("发动态"))},
    {"actionTime", boost::any(1634630147)},
    {"score", boost::any(3)}
  }));
  try {
    client->addPointWithOptions(addPointRequest, addPointHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgInvalid.param.error | %s | 组织非百姓通组织 |
| 400 | checkParameter.param.error | %s | 参数校验失败 |
| 400 | point.system.error | 积分服务请求失败 %s | 积分服务请求失败 |
| 500 | sytem.error | system error %s | 系统错误 |
