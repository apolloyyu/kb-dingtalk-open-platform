---
title: "获取协作空间列表"
source_url: "https://open.dingtalk.com/document/development/api-searchprojectsv3-1"
namespace: "development"
slug: "api-searchprojectsv3-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉快办 > 获取协作空间列表"
doc_id: "LJj5rKquQ3"
updated_at: "2026-06-02 19:46:14"
---

> Source: https://open.dingtalk.com/document/development/api-searchprojectsv3-1
> Path: 应用开发 / 服务端API / 钉钉快办 > 获取协作空间列表
> Updated: 2026-06-02 19:46:14

# 获取协作空间列表

调用本接口，可以拉取钉钉快办协作空间列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/teamSphere/projects |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-TeamSphere.Project.ReadWrite-钉钉快办管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |
| projectIds | String | 否 | 协作空间ID集合，逗号分隔。 |
| name | String | 否 | 协作空间名字(模糊匹配)。 |
| maxResults | Integer | 否 | 每页返回最大数量。默认10，最大300。 |
| nextToken | String | 否 | 分页标，从上一次请求结果中获取。 |
| sourceId | String | 否 | 协作空间ID。 |
| includeTemplate | Boolean | 否 | 是否包含模板协作空间，默认 false。 |

### 请求示例

HTTP

```
GET /v1.0/teamSphere/projects?userId=0517xxx&projectIds=1234&name=测试&maxResults=19&nextToken=null&sourceId=1234&includeTemplate=false HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1234
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
        com.aliyun.dingtalkteam_sphere_1_0.models.SearchProjectsV3Headers searchProjectsV3Headers = new com.aliyun.dingtalkteam_sphere_1_0.models.SearchProjectsV3Headers();
        searchProjectsV3Headers.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkteam_sphere_1_0.models.SearchProjectsV3Request searchProjectsV3Request = new com.aliyun.dingtalkteam_sphere_1_0.models.SearchProjectsV3Request()
                .setUserId("0517xxx")
                .setProjectIds("1234")
                .setName("测试")
                .setMaxResults(19)
                .setNextToken("null")
                .setSourceId("1234")
                .setIncludeTemplate(false);
        try {
            client.searchProjectsV3WithOptions(searchProjectsV3Request, searchProjectsV3Headers, new com.aliyun.teautil.models.RuntimeOptions());
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
        search_projects_v3headers = dingtalkteam_sphere__1__0_models.SearchProjectsV3Headers()
        search_projects_v3headers.x_acs_dingtalk_access_token = '<your access token>'
        search_projects_v3request = dingtalkteam_sphere__1__0_models.SearchProjectsV3Request(
            user_id='0517xxx',
            project_ids='1234',
            name='测试',
            max_results=19,
            next_token='null',
            source_id='1234',
            include_template=False
        )
        try:
            client.search_projects_v3with_options(search_projects_v3request, search_projects_v3headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_projects_v3headers = dingtalkteam_sphere__1__0_models.SearchProjectsV3Headers()
        search_projects_v3headers.x_acs_dingtalk_access_token = '<your access token>'
        search_projects_v3request = dingtalkteam_sphere__1__0_models.SearchProjectsV3Request(
            user_id='0517xxx',
            project_ids='1234',
            name='测试',
            max_results=19,
            next_token='null',
            source_id='1234',
            include_template=False
        )
        try:
            await client.search_projects_v3with_options_async(search_projects_v3request, search_projects_v3headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\SearchProjectsV3Headers;
use AlibabaCloud\SDK\Dingtalk\Vteam_sphere_1_0\Models\SearchProjectsV3Request;
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
        $searchProjectsV3Headers = new SearchProjectsV3Headers([]);
        $searchProjectsV3Headers->xAcsDingtalkAccessToken = "<your access token>";
        $searchProjectsV3Request = new SearchProjectsV3Request([
            "userId" => "0517xxx",
            "projectIds" => "1234",
            "name" => "测试",
            "maxResults" => 19,
            "nextToken" => "null",
            "sourceId" => "1234",
            "includeTemplate" => false
        ]);
        try {
            $client->searchProjectsV3WithOptions($searchProjectsV3Request, $searchProjectsV3Headers, new RuntimeOptions([]));
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

  searchProjectsV3Headers := &dingtalkteamsphere_1_0.SearchProjectsV3Headers{}
  searchProjectsV3Headers.XAcsDingtalkAccessToken = tea.String("<your access token>")
  searchProjectsV3Request := &dingtalkteamsphere_1_0.SearchProjectsV3Request{
    UserId: tea.String("0517xxx"),
    ProjectIds: tea.String("1234"),
    Name: tea.String("测试"),
    MaxResults: tea.Int32(19),
    NextToken: tea.String("null"),
    SourceId: tea.String("1234"),
    IncludeTemplate: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SearchProjectsV3WithOptions(searchProjectsV3Request, searchProjectsV3Headers, &util.RuntimeOptions{})
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
    let searchProjectsV3Headers = new dingtalkteamSphere_1_0.SearchProjectsV3Headers({ });
    searchProjectsV3Headers.xAcsDingtalkAccessToken = '<your access token>';
    let searchProjectsV3Request = new dingtalkteamSphere_1_0.SearchProjectsV3Request({
      userId: '0517xxx',
      projectIds: '1234',
      name: '测试',
      maxResults: 19,
      nextToken: 'null',
      sourceId: '1234',
      includeTemplate: false,
    });
    try {
      await client.searchProjectsV3WithOptions(searchProjectsV3Request, searchProjectsV3Headers, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.SearchProjectsV3Headers searchProjectsV3Headers = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.SearchProjectsV3Headers();
            searchProjectsV3Headers.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.SearchProjectsV3Request searchProjectsV3Request = new AlibabaCloud.SDK.Dingtalkteam_sphere_1_0.Models.SearchProjectsV3Request
            {
                UserId = "0517xxx",
                ProjectIds = "1234",
                Name = "测试",
                MaxResults = 19,
                NextToken = "null",
                SourceId = "1234",
                IncludeTemplate = false,
            };
            try
            {
                client.SearchProjectsV3WithOptions(searchProjectsV3Request, searchProjectsV3Headers, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 协作空间列表。 |
| id | String | 协作空间ID。 |
| name | String | 协作空间名称。 |
| logo | String | 协作空间LOGO。 |
| description | String | 协作空间描述。 |
| organizationId | String | 企业ID。 |
| isTemplate | Boolean | 是模板协作空间。 |
| creatorId | String | 创建人ID。 |
| created | String | 创建时间。 |
| updated | String | 更新时间。 |
| sourceId | String | 来源协作空间 ID。 |
| requestId | String | 请求 ID，请求异常时可提供此 ID，进行问题排查。 |
| nextToken | String | 分页标，供分页使用，下一页token。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "id" : "1234",
    "name" : "测试",
    "logo" : "http://test.com",
    "description" : "测试",
    "organizationId" : "1234",
    "isTemplate" : false,
    "creatorId" : "1234",
    "created" : "2022-07-04T03:29:34.770Z",
    "updated" : "2022-07-04T03:29:34.770Z",
    "sourceId" : "1234"
  } ],
  "requestId" : "1234",
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
