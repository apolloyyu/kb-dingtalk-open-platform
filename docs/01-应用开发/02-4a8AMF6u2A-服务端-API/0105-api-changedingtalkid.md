---
title: "企业账号修改钉钉号"
source_url: "https://open.dingtalk.com/document/development/api-changedingtalkid"
namespace: "development"
slug: "api-changedingtalkid"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 企业账号修改钉钉号"
doc_id: "9VI0AepSKW"
updated_at: "2026-06-04 14:29:35"
---

> Source: https://open.dingtalk.com/document/development/api-changedingtalkid
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 企业账号修改钉钉号
> Updated: 2026-06-04 14:29:35

# 企业账号修改钉钉号

调用本接口，修改企业账号钉钉号。

## 接口调用说明

每个账号修改钉钉号后，一年内不能再次修改。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccounts/dingTalkIds/change |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-维护通讯录的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 员工userId，只支持归属于本企业的企业账号userId。 |
| dingTalkId | String | 是 | 新的钉钉号。全局唯一，不只是组织内唯一，所以不能和已经存在的冲突，发生冲突时需要更换备选值。格式要求：   - 6<=长度<=20 - 字母开头 - 只包含字母、数字 - 不能包含违禁内容 |

### 请求示例

HTTP

```
POST /v1.0/contact/orgAccounts/dingTalkIds/change HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f788baa23xxxx
Content-Type:application/json

{
  "userId" : "userIdBB",
  "dingTalkId" : "abc123"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.ChangeDingTalkIdHeaders changeDingTalkIdHeaders = new com.aliyun.dingtalkcontact_1_0.models.ChangeDingTalkIdHeaders();
        changeDingTalkIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.ChangeDingTalkIdRequest changeDingTalkIdRequest = new com.aliyun.dingtalkcontact_1_0.models.ChangeDingTalkIdRequest()
                .setUserId("userIdBB")
                .setDingTalkId("abc123");
        try {
            client.changeDingTalkIdWithOptions(changeDingTalkIdRequest, changeDingTalkIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys

from typing import List

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        change_ding_talk_id_headers = dingtalkcontact__1__0_models.ChangeDingTalkIdHeaders()
        change_ding_talk_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        change_ding_talk_id_request = dingtalkcontact__1__0_models.ChangeDingTalkIdRequest(
            user_id='userIdBB',
            ding_talk_id='abc123'
        )
        try:
            client.change_ding_talk_id_with_options(change_ding_talk_id_request, change_ding_talk_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        change_ding_talk_id_headers = dingtalkcontact__1__0_models.ChangeDingTalkIdHeaders()
        change_ding_talk_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        change_ding_talk_id_request = dingtalkcontact__1__0_models.ChangeDingTalkIdRequest(
            user_id='userIdBB',
            ding_talk_id='abc123'
        )
        try:
            await client.change_ding_talk_id_with_options_async(change_ding_talk_id_request, change_ding_talk_id_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ChangeDingTalkIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ChangeDingTalkIdRequest;
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
        $changeDingTalkIdHeaders = new ChangeDingTalkIdHeaders([]);
        $changeDingTalkIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $changeDingTalkIdRequest = new ChangeDingTalkIdRequest([
            "userId" => "userIdBB",
            "dingTalkId" => "abc123"
        ]);
        try {
            $client->changeDingTalkIdWithOptions($changeDingTalkIdRequest, $changeDingTalkIdHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  changeDingTalkIdHeaders := &dingtalkcontact_1_0.ChangeDingTalkIdHeaders{}
  changeDingTalkIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  changeDingTalkIdRequest := &dingtalkcontact_1_0.ChangeDingTalkIdRequest{
    UserId: tea.String("userIdBB"),
    DingTalkId: tea.String("abc123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChangeDingTalkIdWithOptions(changeDingTalkIdRequest, changeDingTalkIdHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkcontact_1_0 = require('@alicloud/dingtalk/contact_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkcontact_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let changeDingTalkIdHeaders = new dingtalkcontact_1_0.ChangeDingTalkIdHeaders({ });
    changeDingTalkIdHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let changeDingTalkIdRequest = new dingtalkcontact_1_0.ChangeDingTalkIdRequest({
      userId: 'userIdBB',
      dingTalkId: 'abc123',
    });
    try {
      await client.changeDingTalkIdWithOptions(changeDingTalkIdRequest, changeDingTalkIdHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeDingTalkIdHeaders changeDingTalkIdHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeDingTalkIdHeaders();
            changeDingTalkIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeDingTalkIdRequest changeDingTalkIdRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeDingTalkIdRequest
            {
                UserId = "userIdBB",
                DingTalkId = "abc123",
            };
            try
            {
                client.ChangeDingTalkIdWithOptions(changeDingTalkIdRequest, changeDingTalkIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 执行结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | incorrect.format | 钉钉号格式不正确，请重新输入 | 钉钉号格式不正确，请重新输入 |
| 400 | have.been.set | 你已经设置过钉钉号，无法修改 | 你已经设置过钉钉号，无法修改 |
| 400 | emp.not.exist | 员工不存在 | 员工不存在 |
| 400 | internalenterpriseaccount.limit | 仅限处理归属本企业的企业账号 | 仅限处理归属本企业的企业账号 |
| 400 | incorrect.length | 钉钉号格式不正确，请重新输入 | 钉钉号格式不正确，请重新输入 |
| 400 | incorrect.reserved | 该钉钉号已被占用，请重新输入 | 该钉钉号已被占用，请重新输入 |
| 500 | system.busy | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
