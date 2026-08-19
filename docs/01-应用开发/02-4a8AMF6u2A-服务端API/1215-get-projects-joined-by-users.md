---
title: "获取用户加入的项目"
source_url: "https://open.dingtalk.com/document/development/get-projects-joined-by-users"
namespace: "development"
slug: "get-projects-joined-by-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 项目 > 获取用户加入的项目"
doc_id: "emScPgy3gC"
updated_at: "2025-10-09 18:06:33"
---

> Source: https://open.dingtalk.com/document/development/get-projects-joined-by-users
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 项目 > 获取用户加入的项目
> Updated: 2025-10-09 18:06:33

# 获取用户加入的项目

调用本接口获取用户加入的项目。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/joinProjects |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Project.Read.All-项目应用项目读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| maxResults | Integer | 否 | 分页大小。  **[!NOTE]**    不传则显示全部项目。 |
| nextToken | String | 否 | 分页标。 |

### 请求示例

HTTP

```
GET /v1.0/project/users/0517xxx/joinProjects?maxResults=10&nextToken=f279e812xxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
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
    public static com.aliyun.dingtalkproject_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkproject_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkproject_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkproject_1_0.models.GetUserJoinedProjectHeaders getUserJoinedProjectHeaders = new com.aliyun.dingtalkproject_1_0.models.GetUserJoinedProjectHeaders();
        getUserJoinedProjectHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.GetUserJoinedProjectRequest getUserJoinedProjectRequest = new com.aliyun.dingtalkproject_1_0.models.GetUserJoinedProjectRequest()
                .setMaxResults(10)
                .setNextToken("f279e812xxxxxx");
        try {
            client.getUserJoinedProjectWithOptions("0517xxx", getUserJoinedProjectRequest, getUserJoinedProjectHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.project_1_0.client import Client as dingtalkproject_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.project_1_0 import models as dingtalkproject__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkproject_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkproject_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_joined_project_headers = dingtalkproject__1__0_models.GetUserJoinedProjectHeaders()
        get_user_joined_project_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_joined_project_request = dingtalkproject__1__0_models.GetUserJoinedProjectRequest(
            max_results=10,
            next_token='f279e812xxxxxx'
        )
        try:
            client.get_user_joined_project_with_options('0517xxx', get_user_joined_project_request, get_user_joined_project_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_joined_project_headers = dingtalkproject__1__0_models.GetUserJoinedProjectHeaders()
        get_user_joined_project_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_joined_project_request = dingtalkproject__1__0_models.GetUserJoinedProjectRequest(
            max_results=10,
            next_token='f279e812xxxxxx'
        )
        try:
            await client.get_user_joined_project_with_options_async('0517xxx', get_user_joined_project_request, get_user_joined_project_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\GetUserJoinedProjectHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\GetUserJoinedProjectRequest;
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
        $getUserJoinedProjectHeaders = new GetUserJoinedProjectHeaders([]);
        $getUserJoinedProjectHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUserJoinedProjectRequest = new GetUserJoinedProjectRequest([
            "maxResults" => 10,
            "nextToken" => "f279e812xxxxxx"
        ]);
        try {
            $client->getUserJoinedProjectWithOptions("0517xxx", $getUserJoinedProjectRequest, $getUserJoinedProjectHeaders, new RuntimeOptions([]));
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
  dingtalkproject_1_0  "github.com/alibabacloud-go/dingtalk/project_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkproject_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkproject_1_0.Client{}
  _result, _err = dingtalkproject_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUserJoinedProjectHeaders := &dingtalkproject_1_0.GetUserJoinedProjectHeaders{}
  getUserJoinedProjectHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUserJoinedProjectRequest := &dingtalkproject_1_0.GetUserJoinedProjectRequest{
    MaxResults: tea.Int32(10),
    NextToken: tea.String("f279e812xxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserJoinedProjectWithOptions(tea.String("0517xxx"), getUserJoinedProjectRequest, getUserJoinedProjectHeaders, &util.RuntimeOptions{})
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
import dingtalkproject_1_0, * as $dingtalkproject_1_0 from '@alicloud/dingtalk/project_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkproject_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkproject_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUserJoinedProjectHeaders = new $dingtalkproject_1_0.GetUserJoinedProjectHeaders({ });
    getUserJoinedProjectHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUserJoinedProjectRequest = new $dingtalkproject_1_0.GetUserJoinedProjectRequest({
      maxResults: 10,
      nextToken: "f279e812xxxxxx",
    });
    try {
      await client.getUserJoinedProjectWithOptions("0517xxx", getUserJoinedProjectRequest, getUserJoinedProjectHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkproject_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkproject_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkproject_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetUserJoinedProjectHeaders getUserJoinedProjectHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetUserJoinedProjectHeaders();
            getUserJoinedProjectHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetUserJoinedProjectRequest getUserJoinedProjectRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.GetUserJoinedProjectRequest
            {
                MaxResults = 10,
                NextToken = "f279e812xxxxxx",
            };
            try
            {
                client.GetUserJoinedProjectWithOptions("0517xxx", getUserJoinedProjectRequest, getUserJoinedProjectHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array of String | 项目id。 |
| nextToken | String | 分页标。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ "60a2187eb72xxxxxxx" ],
  "nextToken" : "f279e812xxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
