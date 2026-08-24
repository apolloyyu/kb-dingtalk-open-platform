---
title: "获取防截屏操作记录"
source_url: "https://open.dingtalk.com/document/development/obtain-anti-screen-capture-operation-records"
namespace: "development"
slug: "obtain-anti-screen-capture-operation-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 获取防截屏操作记录"
doc_id: "vUEgWYqwPO"
updated_at: "2026-06-04 19:10:01"
---

> Source: https://open.dingtalk.com/document/development/obtain-anti-screen-capture-operation-records
> Path: 应用开发 / 服务端API / 专属钉钉 > 获取防截屏操作记录
> Updated: 2026-06-04 19:10:01

# 获取防截屏操作记录

调用本接口，获取防截屏操作记录。

## **接口调用说明**

获取防截屏操作记录，需同时满足以下条件才可调用：

1. 调用的组织类型是**专属钉钉**组织，如果是非专属钉钉组织，可点击[开通专属钉钉](https://oa.dingtalk.com/register_new.htm?spm=ding_open_doc.document.0.0.10423c33KgZ0UA&source=50061&useMt2=1#/)咨询。
2. 创建的应用类型是企业内部应用。

> **[!NOTE]**
>
> 如果用户是普通账号且没有签署协议，则只能获取用户操作行为，不能获取图片的url。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/enterpriseSecurities/userBehaviors/screenshots/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.ScreenShot.Read-专属钉钉防截屏读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| type | Integer | 是 | 用户行为：   - **0**：全部 - **1**：截屏 - **2**：录屏 |
| platform | Integer | 是 | 端类型：   - **0**：全部 - **1**：iOS - **2**：Android - **3**：Mac - **4**：Windows |
| startTime | Long | 否 | 开始时间，时间戳，单位毫秒。      默认当前时间前7天。 |
| endTime | Long | 否 | 结束时间，时间戳，单位毫秒。      默认当前时间。 |
| pageSize | Integer | 是 | 分页大小。      最大值100。 |
| pageNumber | Long | 是 | 起始页。      默认从1开始。 |
| userId | String | 否 | 用户userId信息，可调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取userId。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/enterpriseSecurities/userBehaviors/screenshots/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "type" : 0,
  "platform" : 1,
  "startTime" : 1577340931837,
  "endTime" : 1577945731837,
  "pageSize" : 100,
  "pageNumber" : 1,
  "userId" : "manager7675"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.QueryUserBehaviorHeaders queryUserBehaviorHeaders = new com.aliyun.dingtalkexclusive_1_0.models.QueryUserBehaviorHeaders();
        queryUserBehaviorHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.QueryUserBehaviorRequest queryUserBehaviorRequest = new com.aliyun.dingtalkexclusive_1_0.models.QueryUserBehaviorRequest()
                .setType(0)
                .setPlatform(1)
                .setStartTime(1577340931837L)
                .setEndTime(1577945731837L)
                .setPageSize(100)
                .setPageNumber(1L)
                .setUserId("manager7675");
        try {
            client.queryUserBehaviorWithOptions(queryUserBehaviorRequest, queryUserBehaviorHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_user_behavior_headers = dingtalkexclusive__1__0_models.QueryUserBehaviorHeaders()
        query_user_behavior_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_behavior_request = dingtalkexclusive__1__0_models.QueryUserBehaviorRequest(
            type=0,
            platform=1,
            start_time=1577340931837,
            end_time=1577945731837,
            page_size=100,
            page_number=1,
            user_id='manager7675'
        )
        try:
            client.query_user_behavior_with_options(query_user_behavior_request, query_user_behavior_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_user_behavior_headers = dingtalkexclusive__1__0_models.QueryUserBehaviorHeaders()
        query_user_behavior_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_user_behavior_request = dingtalkexclusive__1__0_models.QueryUserBehaviorRequest(
            type=0,
            platform=1,
            start_time=1577340931837,
            end_time=1577945731837,
            page_size=100,
            page_number=1,
            user_id='manager7675'
        )
        try:
            await client.query_user_behavior_with_options_async(query_user_behavior_request, query_user_behavior_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\QueryUserBehaviorHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\QueryUserBehaviorRequest;
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
        $queryUserBehaviorHeaders = new QueryUserBehaviorHeaders([]);
        $queryUserBehaviorHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryUserBehaviorRequest = new QueryUserBehaviorRequest([
            "type" => 0,
            "platform" => 1,
            "startTime" => 1577340931837,
            "endTime" => 1577945731837,
            "pageSize" => 100,
            "pageNumber" => 1,
            "userId" => "manager7675"
        ]);
        try {
            $client->queryUserBehaviorWithOptions($queryUserBehaviorRequest, $queryUserBehaviorHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryUserBehaviorHeaders := &dingtalkexclusive_1_0.QueryUserBehaviorHeaders{}
  queryUserBehaviorHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryUserBehaviorRequest := &dingtalkexclusive_1_0.QueryUserBehaviorRequest{
    Type: tea.Int32(0),
    Platform: tea.Int32(1),
    StartTime: tea.Int64(1577340931837),
    EndTime: tea.Int64(1577945731837),
    PageSize: tea.Int32(100),
    PageNumber: tea.Int64(1),
    UserId: tea.String("manager7675"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryUserBehaviorWithOptions(queryUserBehaviorRequest, queryUserBehaviorHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryUserBehaviorHeaders = new $dingtalkexclusive_1_0.QueryUserBehaviorHeaders({ });
    queryUserBehaviorHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryUserBehaviorRequest = new $dingtalkexclusive_1_0.QueryUserBehaviorRequest({
      type: 0,
      platform: 1,
      startTime: 1577340931837,
      endTime: 1577945731837,
      pageSize: 100,
      pageNumber: 1,
      userId: "manager7675",
    });
    try {
      await client.queryUserBehaviorWithOptions(queryUserBehaviorRequest, queryUserBehaviorHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryUserBehaviorHeaders queryUserBehaviorHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryUserBehaviorHeaders();
            queryUserBehaviorHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryUserBehaviorRequest queryUserBehaviorRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryUserBehaviorRequest
            {
                Type = 0,
                Platform = 1,
                StartTime = 1577340931837,
                EndTime = 1577945731837,
                PageSize = 100,
                PageNumber = 1,
                UserId = "manager7675",
            };
            try
            {
                client.QueryUserBehaviorWithOptions(queryUserBehaviorRequest, queryUserBehaviorHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Array | 数据列表。 |
| userName | String | 用户昵称。 |
| time | Long | 用户操作时间，时间戳，单位毫秒。 |
| type | Integer | 用户操作类型：   - **1**：截屏 - **2**：录屏 |
| pictureUrl | String | 用户截屏图片url。      当用户签署响应条款后，才能获取到图片URL。 |
| platform | Integer | 端类型：   - **1**：iOS - **2**：Android - **3**：Mac - **4**：Windows |
| scene | String | 场景。 |
| userId | String | 用户userId。 |
| totalCnt | Integer | 数据总量。 |
| dataCnt | Integer | 当前页数据量。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "userName" : "测试账号",
    "time" : 1577340931837,
    "type" : 1,
    "pictureUrl" : "https://***",
    "platform" : 1,
    "scene" : "测试",
    "userId" : "user001"
  } ],
  "totalCnt" : 100,
  "dataCnt" : 20
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.invalid | 参数错误:%s | 参数不合法,包含platform、type、pageSize、pageNumber... |
| 500 | system.error | %s | 系统错误 |
