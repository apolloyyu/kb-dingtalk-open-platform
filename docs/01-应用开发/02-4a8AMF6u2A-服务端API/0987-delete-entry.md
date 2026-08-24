---
title: "删除词条"
source_url: "https://open.dingtalk.com/document/development/delete-entry"
namespace: "development"
slug: "delete-entry"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 企业百科 > 删除词条"
doc_id: "6Mm22kdAZh"
updated_at: "2026-06-02 19:45:00"
---

> Source: https://open.dingtalk.com/document/development/delete-entry
> Path: 应用开发 / 服务端API / 企业文化 > 企业百科 > 删除词条
> Updated: 2026-06-02 19:45:00

# 删除词条

调用本接口，删除词条，删除词条后，会有3秒缓存。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/pedia/words |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Pedia.Words.Write-企业百科写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| uuid | Long | 是 | 当前需要删除的词条主键编号，可调用[分页获取企业词条信息](0988-entry-search.md)接口获取。 |
| userId | String | 是 | 当前操作用户的userId。 |

### 请求示例

HTTP

```
DELETE /v1.0/pedia/words?uuid=212112&userId=2123132 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkpedia_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkpedia_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkpedia_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsDeleteHeaders pediaWordsDeleteHeaders = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsDeleteHeaders();
        pediaWordsDeleteHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkpedia_1_0.models.PediaWordsDeleteRequest pediaWordsDeleteRequest = new com.aliyun.dingtalkpedia_1_0.models.PediaWordsDeleteRequest()
                .setUuid(212112L)
                .setUserId("2123132");
        try {
            client.pediaWordsDeleteWithOptions(pediaWordsDeleteRequest, pediaWordsDeleteHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.pedia_1_0.client import Client as dingtalkpedia_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.pedia_1_0 import models as dingtalkpedia__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkpedia_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkpedia_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_delete_headers = dingtalkpedia__1__0_models.PediaWordsDeleteHeaders()
        pedia_words_delete_headers.x_acs_dingtalk_access_token = '<your access token>'
        pedia_words_delete_request = dingtalkpedia__1__0_models.PediaWordsDeleteRequest(
            uuid=212112,
            user_id='2123132'
        )
        try:
            client.pedia_words_delete_with_options(pedia_words_delete_request, pedia_words_delete_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        pedia_words_delete_headers = dingtalkpedia__1__0_models.PediaWordsDeleteHeaders()
        pedia_words_delete_headers.x_acs_dingtalk_access_token = '<your access token>'
        pedia_words_delete_request = dingtalkpedia__1__0_models.PediaWordsDeleteRequest(
            uuid=212112,
            user_id='2123132'
        )
        try:
            await client.pedia_words_delete_with_options_async(pedia_words_delete_request, pedia_words_delete_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsDeleteHeaders;
use AlibabaCloud\SDK\Dingtalk\Vpedia_1_0\Models\PediaWordsDeleteRequest;
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
        $pediaWordsDeleteHeaders = new PediaWordsDeleteHeaders([]);
        $pediaWordsDeleteHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pediaWordsDeleteRequest = new PediaWordsDeleteRequest([
            "uuid" => 212112,
            "userId" => "2123132"
        ]);
        try {
            $client->pediaWordsDeleteWithOptions($pediaWordsDeleteRequest, $pediaWordsDeleteHeaders, new RuntimeOptions([]));
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
  dingtalkpedia_1_0  "github.com/alibabacloud-go/dingtalk/pedia_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkpedia_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkpedia_1_0.Client{}
  _result, _err = dingtalkpedia_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  pediaWordsDeleteHeaders := &dingtalkpedia_1_0.PediaWordsDeleteHeaders{}
  pediaWordsDeleteHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pediaWordsDeleteRequest := &dingtalkpedia_1_0.PediaWordsDeleteRequest{
    Uuid: tea.Int64(212112),
    UserId: tea.String("2123132"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PediaWordsDeleteWithOptions(pediaWordsDeleteRequest, pediaWordsDeleteHeaders, &util.RuntimeOptions{})
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
import dingtalkpedia_1_0, * as $dingtalkpedia_1_0 from '@alicloud/dingtalk/pedia_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkpedia_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkpedia_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let pediaWordsDeleteHeaders = new $dingtalkpedia_1_0.PediaWordsDeleteHeaders({ });
    pediaWordsDeleteHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let pediaWordsDeleteRequest = new $dingtalkpedia_1_0.PediaWordsDeleteRequest({
      uuid: 212112,
      userId: "2123132",
    });
    try {
      await client.pediaWordsDeleteWithOptions(pediaWordsDeleteRequest, pediaWordsDeleteHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkpedia_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkpedia_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsDeleteHeaders pediaWordsDeleteHeaders = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsDeleteHeaders();
            pediaWordsDeleteHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsDeleteRequest pediaWordsDeleteRequest = new AlibabaCloud.SDK.Dingtalkpedia_1_0.Models.PediaWordsDeleteRequest
            {
                Uuid = 212112,
                UserId = "2123132",
            };
            try
            {
                client.PediaWordsDeleteWithOptions(pediaWordsDeleteRequest, pediaWordsDeleteHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| uuid | Long | 删除成功，返回删除的uuid。 |
| success | Boolean | 请求是否成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "uuid" : 123456789,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError.corpId | 获取到的企业编号不能为空 | 获取到的企业编号不能为空 |
| 400 | paramError.uuid | 词条操作主键uuid不能为空 | 词条操作主键uuid不能为空 |
| 400 | paramError.userId | 操作员工编号userId不能为空 | 操作员工编号userId不能为空 |
| 400 | paramError.userId | 操作员工编号userId填写错误未找到对应员工信息 | 操作员工编号userId填写错误未找到对应员工信息 |
| 400 | paramError.uuid | 当前词条不存在，请确认后uuid后再操作 | 当前词条不存在，请确认后uuid后再操作 |
| 400 | paramError.userId | 当前操作人员不是管理员,只有管理员可以进行该操作 | 当前操作人员不是管理员,只有管理员可以进行该操作 |
