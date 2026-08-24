---
title: "订阅文件变更事件"
source_url: "https://open.dingtalk.com/document/development/subscribe-to-file-change-events"
namespace: "development"
slug: "subscribe-to-file-change-events"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 存储管理 > 事件订阅 > 订阅文件变更事件"
doc_id: "ClEmSORWIC"
updated_at: "2026-06-04 19:09:47"
---

> Source: https://open.dingtalk.com/document/development/subscribe-to-file-change-events
> Path: 应用开发 / 服务端API / 文档/文件 > 存储管理 > 事件订阅 > 订阅文件变更事件
> Updated: 2026-06-04 19:09:47

# 订阅文件变更事件

调用本接口，订阅文件变更事件。

## **接口调用说明**

1. 在开发者后台应用事件订阅中，先开启订阅存储事件。

   ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7831750871/p1077002.png)
2. 调用本接口，指定订阅范围是企业或者指定的存储空间。

   > **[!NOTE]**
   >
   > 如果仅在开发者后台开启存储事件订阅开关，无法接收回调事件，必须与本接口配合使用。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/events/subscribe |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.Event.Write-企业存储文件变更事件订阅写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| scopeId | String | 是 | 订阅范围对应的ID。   - 当scope参数值为ORG时，scopeId对应的是企业corpId，请参考[基础概念-CorpId](https://open.dingtalk.com/document/development/basic-concepts-beta#section-bbk-mv0-oxd)。 - 当scope为SPACE时，scopeId对应的是存储空间ID，可调用[添加空间](0652-add-space.md)接口获取id。 |
| scope | String | 是 | 订阅范围。   - ORG：企业 - SPACE：空间 |

### 请求示例

HTTP

```
POST /v1.0/storage/events/subscribe?unionId=union_id HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "scopeId" : "SPACE",
  "scope" : "SPACE"
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
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.SubscribeEventHeaders subscribeEventHeaders = new com.aliyun.dingtalkstorage_1_0.models.SubscribeEventHeaders();
        subscribeEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.SubscribeEventRequest subscribeEventRequest = new com.aliyun.dingtalkstorage_1_0.models.SubscribeEventRequest()
                .setUnionId("union_id")
                .setScopeId("SPACE")
                .setScope("SPACE");
        try {
            client.subscribeEventWithOptions(subscribeEventRequest, subscribeEventHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.storage_1_0.client import Client as dingtalkstorage_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.storage_1_0 import models as dingtalkstorage__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkstorage_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkstorage_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        subscribe_event_headers = dingtalkstorage__1__0_models.SubscribeEventHeaders()
        subscribe_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        subscribe_event_request = dingtalkstorage__1__0_models.SubscribeEventRequest(
            union_id='union_id',
            scope_id='SPACE',
            scope='SPACE'
        )
        try:
            client.subscribe_event_with_options(subscribe_event_request, subscribe_event_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        subscribe_event_headers = dingtalkstorage__1__0_models.SubscribeEventHeaders()
        subscribe_event_headers.x_acs_dingtalk_access_token = '<your access token>'
        subscribe_event_request = dingtalkstorage__1__0_models.SubscribeEventRequest(
            union_id='union_id',
            scope_id='SPACE',
            scope='SPACE'
        )
        try:
            await client.subscribe_event_with_options_async(subscribe_event_request, subscribe_event_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\SubscribeEventHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\SubscribeEventRequest;
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
        $subscribeEventHeaders = new SubscribeEventHeaders([]);
        $subscribeEventHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $subscribeEventRequest = new SubscribeEventRequest([
            "unionId" => "union_id",
            "scopeId" => "SPACE",
            "scope" => "SPACE"
        ]);
        try {
            $client->subscribeEventWithOptions($subscribeEventRequest, $subscribeEventHeaders, new RuntimeOptions([]));
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
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkstorage_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkstorage_1_0.Client{}
  _result, _err = dingtalkstorage_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  subscribeEventHeaders := &dingtalkstorage_1_0.SubscribeEventHeaders{}
  subscribeEventHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  subscribeEventRequest := &dingtalkstorage_1_0.SubscribeEventRequest{
    UnionId: tea.String("union_id"),
    ScopeId: tea.String("SPACE"),
    Scope: tea.String("SPACE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SubscribeEventWithOptions(subscribeEventRequest, subscribeEventHeaders, &util.RuntimeOptions{})
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
import dingtalkstorage_1_0, * as $dingtalkstorage_1_0 from '@alicloud/dingtalk/storage_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkstorage_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkstorage_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let subscribeEventHeaders = new $dingtalkstorage_1_0.SubscribeEventHeaders({ });
    subscribeEventHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let subscribeEventRequest = new $dingtalkstorage_1_0.SubscribeEventRequest({
      unionId: "union_id",
      scopeId: "SPACE",
      scope: "SPACE",
    });
    try {
      await client.subscribeEventWithOptions(subscribeEventRequest, subscribeEventHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkstorage_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkstorage_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.SubscribeEventHeaders subscribeEventHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.SubscribeEventHeaders();
            subscribeEventHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.SubscribeEventRequest subscribeEventRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.SubscribeEventRequest
            {
                UnionId = "union_id",
                ScopeId = "SPACE",
                Scope = "SPACE",
            };
            try
            {
                client.SubscribeEventWithOptions(subscribeEventRequest, subscribeEventHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 本次操作是否成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.scope | %s | 参数错误-scope |
| 400 | paramError.scopeId | %s | 参数错误-scopeId |
| 403 | permissionDenied | %s | 用户缺少订阅事件的权限 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
