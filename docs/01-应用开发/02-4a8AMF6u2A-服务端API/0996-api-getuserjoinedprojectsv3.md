---
title: "获取用户参与项目"
source_url: "https://open.dingtalk.com/document/development/api-getuserjoinedprojectsv3"
namespace: "development"
slug: "api-getuserjoinedprojectsv3"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉快办 > 获取用户参与项目"
doc_id: "HrFKCFHw9Y"
updated_at: "2026-06-02 19:46:15"
---

> Source: https://open.dingtalk.com/document/development/api-getuserjoinedprojectsv3
> Path: 应用开发 / 服务端API / 钉钉快办 > 获取用户参与项目
> Updated: 2026-06-02 19:46:15

# 获取用户参与项目

调用本接口，获取用户参与项目。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/teamSphere/users/{userId}/projects/userJoined |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-TeamSphere.Project.ReadWrite-钉钉快办管理权限 |

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
| projectIds | String | 否 | 项目ID集合，逗号分隔。 |
| projectRoleLevels | String | 否 | 过滤指定的项目角色等级，逗号分割，可以填写 0,1,2 分别表示成员, 管理员, 拥有者。 |
| sortBy | String | 否 | 排序，可选 `updated:desc` 或者 `pinyin:asc`。 |
| maxResults | Integer | 否 | 每页返回最大数量。默认10，最大300。 |
| nextToken | String | 否 | 分页标，从上一次请求结果中获取。 |

### 请求示例

HTTP

```
GET /v1.0/teamSphere/users/0517xxx/projects/userJoined?projectIds=zxchjs80as,90asdx0&projectRoleLevels=1&sortBy=desc&maxResults=20&nextToken=673bf83f988ddc5091eb2ab0 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:673bf83f988ddc5091eb2xx
Content-Type:application/json
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
    public static com.aliyun.dingtalkteam_sphere_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkteam_sphere_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkteam_sphere_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkteam_sphere_1_0.models.GetUserJoinedProjectsV3Headers getUserJoinedProjectsV3Headers = new com.aliyun.dingtalkteam_sphere_1_0.models.GetUserJoinedProjectsV3Headers();
        getUserJoinedProjectsV3Headers.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkteam_sphere_1_0.models.GetUserJoinedProjectsV3Request getUserJoinedProjectsV3Request = new com.aliyun.dingtalkteam_sphere_1_0.models.GetUserJoinedProjectsV3Request()
                .setProjectIds("zxchjs80as,90asdx0")
                .setProjectRoleLevels("1")
                .setSortBy("desc")
                .setMaxResults(20)
                .setNextToken("673bf83f988ddc5091eb2ab0");
        try {
            client.getUserJoinedProjectsV3WithOptions("0517xxx", getUserJoinedProjectsV3Request, getUserJoinedProjectsV3Headers, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.team_sphere_1_0.client import Client as dingtalkteamSphere_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.team_sphere_1_0 import models as dingtalkteam_sphere__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkteamSphere_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkteamSphere_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_joined_projects_v3headers = dingtalkteam_sphere__1__0_models.GetUserJoinedProjectsV3Headers()
        get_user_joined_projects_v3headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_joined_projects_v3request = dingtalkteam_sphere__1__0_models.GetUserJoinedProjectsV3Request(
            project_ids='zxchjs80as,90asdx0',
            project_role_levels='1',
            sort_by='desc',
            max_results=20,
            next_token='673bf83f988ddc5091eb2ab0'
        )
        try:
            client.get_user_joined_projects_v3with_options('0517xxx', get_user_joined_projects_v3request, get_user_joined_projects_v3headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_user_joined_projects_v3headers = dingtalkteam_sphere__1__0_models.GetUserJoinedProjectsV3Headers()
        get_user_joined_projects_v3headers.x_acs_dingtalk_access_token = '<your access token>'
        get_user_joined_projects_v3request = dingtalkteam_sphere__1__0_models.GetUserJoinedProjectsV3Request(
            project_ids='zxchjs80as,90asdx0',
            project_role_levels='1',
            sort_by='desc',
            max_results=20,
            next_token='673bf83f988ddc5091eb2ab0'
        )
        try:
            await client.get_user_joined_projects_v3with_options_async('0517xxx', get_user_joined_projects_v3request, get_user_joined_projects_v3headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\GetUserJoinedProjectsV3Headers;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\GetUserJoinedProjectsV3Request;
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
        $getUserJoinedProjectsV3Headers = new GetUserJoinedProjectsV3Headers([]);
        $getUserJoinedProjectsV3Headers->xAcsDingtalkAccessToken = "<your access token>";
        $getUserJoinedProjectsV3Request = new GetUserJoinedProjectsV3Request([
            "projectIds" => "zxchjs80as,90asdx0",
            "projectRoleLevels" => "1",
            "sortBy" => "desc",
            "maxResults" => 20,
            "nextToken" => "673bf83f988ddc5091eb2ab0"
        ]);
        try {
            $client->getUserJoinedProjectsV3WithOptions("0517xxx", $getUserJoinedProjectsV3Request, $getUserJoinedProjectsV3Headers, new RuntimeOptions([]));
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
  dingtalkteamsphere_1_0  "github.com/alibabacloud-go/dingtalk/teamSphere_1_0"
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
func CreateClient () (_result *dingtalkteamsphere_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkteamsphere_1_0.Client{}
  _result, _err = dingtalkteamsphere_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUserJoinedProjectsV3Headers := &dingtalkteamsphere_1_0.GetUserJoinedProjectsV3Headers{}
  getUserJoinedProjectsV3Headers.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUserJoinedProjectsV3Request := &dingtalkteamsphere_1_0.GetUserJoinedProjectsV3Request{
    ProjectIds: tea.String("zxchjs80as,90asdx0"),
    ProjectRoleLevels: tea.String("1"),
    SortBy: tea.String("desc"),
    MaxResults: tea.Int32(20),
    NextToken: tea.String("673bf83f988ddc5091eb2ab0"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUserJoinedProjectsV3WithOptions(tea.String("0517xxx"), getUserJoinedProjectsV3Request, getUserJoinedProjectsV3Headers, &util.RuntimeOptions{})
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
const dingtalkteamSphere_1_0 = require('@alicloud/dingtalk/teamSphere_1_0');
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
    return new dingtalkteamSphere_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getUserJoinedProjectsV3Headers = new dingtalkteamSphere_1_0.GetUserJoinedProjectsV3Headers({ });
    getUserJoinedProjectsV3Headers.xAcsDingtalkAccessToken = '<your access token>';
    let getUserJoinedProjectsV3Request = new dingtalkteamSphere_1_0.GetUserJoinedProjectsV3Request({
      projectIds: 'zxchjs80as,90asdx0',
      projectRoleLevels: '1',
      sortBy: 'desc',
      maxResults: 20,
      nextToken: '673bf83f988ddc5091eb2ab0',
    });
    try {
      await client.getUserJoinedProjectsV3WithOptions('0517xxx', getUserJoinedProjectsV3Request, getUserJoinedProjectsV3Headers, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.GetUserJoinedProjectsV3Headers getUserJoinedProjectsV3Headers = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.GetUserJoinedProjectsV3Headers();
            getUserJoinedProjectsV3Headers.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.GetUserJoinedProjectsV3Request getUserJoinedProjectsV3Request = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.GetUserJoinedProjectsV3Request
            {
                ProjectIds = "zxchjs80as,90asdx0",
                ProjectRoleLevels = "1",
                SortBy = "desc",
                MaxResults = 20,
                NextToken = "673bf83f988ddc5091eb2ab0",
            };
            try
            {
                client.GetUserJoinedProjectsV3WithOptions("0517xxx", getUserJoinedProjectsV3Request, getUserJoinedProjectsV3Headers, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array of String | 项目ID。 |
| requestId | String | 请求 ID，请求异常时可提供此 ID，进行问题排查。 |
| nextToken | String | 分页标，供分页使用，下一页token。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ "673bf83f988ddc5091eb2ab0" ],
  "requestId" : "4759A22F-32C2-1442-8C4A-69EB6ACF8EEC",
  "nextToken" : "f279e812-e431-428d-846d-cxxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误。 |
