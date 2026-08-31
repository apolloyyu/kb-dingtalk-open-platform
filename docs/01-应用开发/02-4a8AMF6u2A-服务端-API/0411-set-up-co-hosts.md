---
title: "设置联席主持人"
source_url: "https://open.dingtalk.com/document/development/set-up-co-hosts"
namespace: "development"
slug: "set-up-co-hosts"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 设置联席主持人"
doc_id: "QqYFiuMcnv"
updated_at: "2026-06-02 12:07:28"
---

> Source: https://open.dingtalk.com/document/development/set-up-co-hosts
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 设置联席主持人
> Updated: 2026-06-02 12:07:28

# 设置联席主持人

会议过程中，新增联席主持人或者删除联席主持人。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/videoConferences/{conferenceId}/coHosts/set |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| conferenceId | String | 是 | 会议id，可调用[创建视频会议](0399-create-a-video-conference.md)接口获取返回参数`conferenceId`字段。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| action | String | 是 | 行为动作：   - **add**:添加联席主持人 - **remove**：移除联系主持人 |
| userList | Array | 是 | 被操作用户列表。 |
| unionId | String | 是 | 用户unionId。 |

### 请求示例

HTTP

```
POST /v1.0/conference/videoConferences/644272f14ba33101xxxx-xxxxx/coHosts/set HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:d8be6dc28b123e7682312ac55xxxx-xxx
Content-Type:application/json

{
  "action" : "add",
  "userList" : [ {
    "unionId" : "qzR1iSMDvzR9iP7P0ZKxxxxxxxxx"
  } ]
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
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconference_1_0.models.CohostsHeaders cohostsHeaders = new com.aliyun.dingtalkconference_1_0.models.CohostsHeaders();
        cohostsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.CohostsRequest.CohostsRequestUserList userList0 = new com.aliyun.dingtalkconference_1_0.models.CohostsRequest.CohostsRequestUserList()
                .setUnionId("qzR1iSMDvzR9iP7P0ZKxxxxxxxxx");
        com.aliyun.dingtalkconference_1_0.models.CohostsRequest cohostsRequest = new com.aliyun.dingtalkconference_1_0.models.CohostsRequest()
                .setAction("add")
                .setUserList(java.util.Arrays.asList(
                    userList0
                ));
        try {
            client.cohostsWithOptions("644272f14ba33101xxxx-xxxxx", cohostsRequest, cohostsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.conference_1_0.client import Client as dingtalkconference_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.conference_1_0 import models as dingtalkconference__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconference_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconference_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        cohosts_headers = dingtalkconference__1__0_models.CohostsHeaders()
        cohosts_headers.x_acs_dingtalk_access_token = '<your access token>'
        user_list_0 = dingtalkconference__1__0_models.CohostsRequestUserList(
            union_id='qzR1iSMDvzR9iP7P0ZKxxxxxxxxx'
        )
        cohosts_request = dingtalkconference__1__0_models.CohostsRequest(
            action='add',
            user_list=[
                user_list_0
            ]
        )
        try:
            client.cohosts_with_options('644272f14ba33101xxxx-xxxxx', cohosts_request, cohosts_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        cohosts_headers = dingtalkconference__1__0_models.CohostsHeaders()
        cohosts_headers.x_acs_dingtalk_access_token = '<your access token>'
        user_list_0 = dingtalkconference__1__0_models.CohostsRequestUserList(
            union_id='qzR1iSMDvzR9iP7P0ZKxxxxxxxxx'
        )
        cohosts_request = dingtalkconference__1__0_models.CohostsRequest(
            action='add',
            user_list=[
                user_list_0
            ]
        )
        try:
            await client.cohosts_with_options_async('644272f14ba33101xxxx-xxxxx', cohosts_request, cohosts_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CohostsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CohostsRequest\userList;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CohostsRequest;
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
        $cohostsHeaders = new CohostsHeaders([]);
        $cohostsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $userList0 = new userList([
            "unionId" => "qzR1iSMDvzR9iP7P0ZKxxxxxxxxx"
        ]);
        $cohostsRequest = new CohostsRequest([
            "action" => "add",
            "userList" => [
                $userList0
            ]
        ]);
        try {
            $client->cohostsWithOptions("644272f14ba33101xxxx-xxxxx", $cohostsRequest, $cohostsHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkconference_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconference_1_0.Client{}
  _result, _err = dingtalkconference_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  cohostsHeaders := &dingtalkconference_1_0.CohostsHeaders{}
  cohostsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  userList0 := &dingtalkconference_1_0.CohostsRequestUserList{
    UnionId: tea.String("qzR1iSMDvzR9iP7P0ZKxxxxxxxxx"),
  }
  cohostsRequest := &dingtalkconference_1_0.CohostsRequest{
    Action: tea.String("add"),
    UserList: []*dingtalkconference_1_0.CohostsRequestUserList{userList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CohostsWithOptions(tea.String("644272f14ba33101xxxx-xxxxx"), cohostsRequest, cohostsHeaders, &util.RuntimeOptions{})
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
import dingtalkconference_1_0, * as $dingtalkconference_1_0 from '@alicloud/dingtalk/conference_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkconference_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkconference_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let cohostsHeaders = new $dingtalkconference_1_0.CohostsHeaders({ });
    cohostsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let userList0 = new $dingtalkconference_1_0.CohostsRequestUserList({
      unionId: "qzR1iSMDvzR9iP7P0ZKxxxxxxxxx",
    });
    let cohostsRequest = new $dingtalkconference_1_0.CohostsRequest({
      action: "add",
      userList: [
        userList0
      ],
    });
    try {
      await client.cohostsWithOptions("644272f14ba33101xxxx-xxxxx", cohostsRequest, cohostsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkconference_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconference_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconference_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsHeaders cohostsHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsHeaders();
            cohostsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsRequest.CohostsRequestUserList userList0 = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsRequest.CohostsRequestUserList
            {
                UnionId = "qzR1iSMDvzR9iP7P0ZKxxxxxxxxx",
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsRequest cohostsRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsRequest
            {
                Action = "add",
                UserList = new List<AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CohostsRequest.CohostsRequestUserList>
                {
                    userList0
                },
            };
            try
            {
                client.CohostsWithOptions("644272f14ba33101xxxx-xxxxx", cohostsRequest, cohostsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否成功。 |

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
| 400 | unknownUserError | unknownUserError | 无法识别的用户 |
| 400 | paramsError | error:%s | 参数错误，缺失会议id |
| 500 | systemError | systemError:%s | 系统错误 |
