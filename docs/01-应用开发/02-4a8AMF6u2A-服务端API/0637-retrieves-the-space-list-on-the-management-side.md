---
title: "根据spaceId获取指定空间信息"
source_url: "https://open.dingtalk.com/document/development/retrieves-the-space-list-on-the-management-side"
namespace: "development"
slug: "retrieves-the-space-list-on-the-management-side"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 云盘（原钉盘） > 根据spaceId获取指定空间信息"
doc_id: "7LfWf0G09M"
updated_at: "2026-06-02 18:46:45"
---

> Source: https://open.dingtalk.com/document/development/retrieves-the-space-list-on-the-management-side
> Path: 应用开发 / 服务端API / 文档/文件 > 云盘（原钉盘） > 根据spaceId获取指定空间信息
> Updated: 2026-06-02 18:46:45

# 根据spaceId获取指定空间信息

调用本接口，根据spaceId获取指定空间的信息，包括空间名称、空间属性、空间大小等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/drive/managements/spaces/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Drive.SpaceManage.Read-钉盘应用盘空间管理信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过以下方式获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceIds | Array of String | 是 | 空间ID列表，最多允许传入30个，可调用[获取空间列表](0636-queries-a-space-list.md)接口获取。 |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/drive/managements/spaces/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2db66caxxxx
Content-Type:application/json

{
  "spaceIds" : [ "123" ],
  "unionId" : "sKUPRiijxxxxx"
}
```

Java

```
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
    public static com.aliyun.dingtalkdrive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdrive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdrive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdrive_1_0.models.ManagementListSpacesHeaders managementListSpacesHeaders = new com.aliyun.dingtalkdrive_1_0.models.ManagementListSpacesHeaders();
        managementListSpacesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdrive_1_0.models.ManagementListSpacesRequest managementListSpacesRequest = new com.aliyun.dingtalkdrive_1_0.models.ManagementListSpacesRequest()
                .setSpaceIds(java.util.Arrays.asList(
                    "123"
                ))
                .setUnionId("sKUPRiijxxxxx");
        try {
            client.managementListSpacesWithOptions(managementListSpacesRequest, managementListSpacesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.drive_1_0.client import Client as dingtalkdrive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.drive_1_0 import models as dingtalkdrive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdrive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdrive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        management_list_spaces_headers = dingtalkdrive__1__0_models.ManagementListSpacesHeaders()
        management_list_spaces_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_list_spaces_request = dingtalkdrive__1__0_models.ManagementListSpacesRequest(
            space_ids=[
                '123'
            ],
            union_id='sKUPRiijxxxxx'
        )
        try:
            client.management_list_spaces_with_options(management_list_spaces_request, management_list_spaces_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        management_list_spaces_headers = dingtalkdrive__1__0_models.ManagementListSpacesHeaders()
        management_list_spaces_headers.x_acs_dingtalk_access_token = '<your access token>'
        management_list_spaces_request = dingtalkdrive__1__0_models.ManagementListSpacesRequest(
            space_ids=[
                '123'
            ],
            union_id='sKUPRiijxxxxx'
        )
        try:
            await client.management_list_spaces_with_options_async(management_list_spaces_request, management_list_spaces_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\ManagementListSpacesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\ManagementListSpacesRequest;
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
        $managementListSpacesHeaders = new ManagementListSpacesHeaders([]);
        $managementListSpacesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $managementListSpacesRequest = new ManagementListSpacesRequest([
            "spaceIds" => [
                "123"
            ],
            "unionId" => "sKUPRiijxxxxx"
        ]);
        try {
            $client->managementListSpacesWithOptions($managementListSpacesRequest, $managementListSpacesHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkdrive_1_0  "github.com/alibabacloud-go/dingtalk/drive_1_0"
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
func CreateClient () (_result *dingtalkdrive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdrive_1_0.Client{}
  _result, _err = dingtalkdrive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  managementListSpacesHeaders := &dingtalkdrive_1_0.ManagementListSpacesHeaders{}
  managementListSpacesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  managementListSpacesRequest := &dingtalkdrive_1_0.ManagementListSpacesRequest{
    SpaceIds: []*string{tea.String("123")},
    UnionId: tea.String("sKUPRiijxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ManagementListSpacesWithOptions(managementListSpacesRequest, managementListSpacesHeaders, &util.RuntimeOptions{})
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
const dingtalkdrive_1_0 = require('@alicloud/dingtalk/drive_1_0');
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
    return new dingtalkdrive_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let managementListSpacesHeaders = new dingtalkdrive_1_0.ManagementListSpacesHeaders({ });
    managementListSpacesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let managementListSpacesRequest = new dingtalkdrive_1_0.ManagementListSpacesRequest({
      spaceIds: [
        '123'
      ],
      unionId: 'sKUPRiijxxxxx',
    });
    try {
      await client.managementListSpacesWithOptions(managementListSpacesRequest, managementListSpacesHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalkdrive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdrive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ManagementListSpacesHeaders managementListSpacesHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ManagementListSpacesHeaders();
            managementListSpacesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ManagementListSpacesRequest managementListSpacesRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ManagementListSpacesRequest
            {
                SpaceIds = new List<string>
                {
                    "123"
                },
                UnionId = "sKUPRiijxxxxx",
            };
            try
            {
                client.ManagementListSpacesWithOptions(managementListSpacesRequest, managementListSpacesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| spaces | Array | 空间列表。 |
| spaceId | String | 空间ID。 |
| spaceName | String | 空间名称。 |
| spaceType | String | 空间类型。   - **personal**：私人空间 - **org**：企业空间 |
| quota | Long | 空间总额度。   - **-1**：表示该空间额度无限制，如果有企业属性，不能超过企业空间额度。 |
| usedQuota | Long | 空间已使用额度。 |
| permissionMode | String | 授权模式，取值：   - **acl**：acl授权 - **custom**：自定义授权 |
| createTime | String | 创建时间，ISO8601格式，例如：2022-07-29T14:55Z。 |
| modifyTime | String | 修改时间，ISO8601格式，例如：2022-07-29T14:55Z。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "spaces" : [ {
    "spaceId" : "123456789",
    "spaceName" : "张三的共享文件夹",
    "spaceType" : "org",
    "quota" : 2147483648,
    "usedQuota" : 640445953,
    "permissionMode" : "acl",
    "createTime" : "2016-02-28T10:47:08Z",
    "modifyTime" : "2021-03-29T14:20:36Z"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Invalid Param | 参数错误 |
| 500 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 500 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 500 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 500 | unknown.error | Unknown Error | 未知错误 |
