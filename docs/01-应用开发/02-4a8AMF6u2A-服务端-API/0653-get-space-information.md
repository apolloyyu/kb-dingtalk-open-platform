---
title: "获取空间信息"
source_url: "https://open.dingtalk.com/document/development/get-space-information"
namespace: "development"
slug: "get-space-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 空间管理 > 获取空间信息"
doc_id: "8TUzoEG5yQ"
updated_at: "2026-06-04 19:09:31"
---

> Source: https://open.dingtalk.com/document/development/get-space-information
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 空间管理 > 获取空间信息
> Updated: 2026-06-04 19:09:31

# 获取空间信息

调用本接口，获取存储空间的信息。

## **接口调用说明**

调用本接口获取空间的详情信息，包括空间名称、已使用容量、owner类型等。

- 存储空间类型为USER时，空间拥有权限的用户都有操作权限，其他员工调用[添加权限](0681-add-permissions-file.md)接口进行授权。
- 存储空间类型为APP时，任何人操作都需要调用[添加权限](0681-add-permissions-file.md)接口进行授权。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.Space.Read-企业存储空间读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/storage/spaces/854xxxxx?unionId=cxUXxxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkstorage_1_0.models.GetSpaceHeaders getSpaceHeaders = new com.aliyun.dingtalkstorage_1_0.models.GetSpaceHeaders();
        getSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.GetSpaceRequest getSpaceRequest = new com.aliyun.dingtalkstorage_1_0.models.GetSpaceRequest()
                .setUnionId("cxUXxxxxxx");
        try {
            client.getSpaceWithOptions("854xxxxx", getSpaceRequest, getSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_space_headers = dingtalkstorage__1__0_models.GetSpaceHeaders()
        get_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_space_request = dingtalkstorage__1__0_models.GetSpaceRequest(
            union_id='cxUXxxxxxx'
        )
        try:
            client.get_space_with_options('854xxxxx', get_space_request, get_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_space_headers = dingtalkstorage__1__0_models.GetSpaceHeaders()
        get_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_space_request = dingtalkstorage__1__0_models.GetSpaceRequest(
            union_id='cxUXxxxxxx'
        )
        try:
            await client.get_space_with_options_async('854xxxxx', get_space_request, get_space_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\GetSpaceRequest;
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
        $getSpaceHeaders = new GetSpaceHeaders([]);
        $getSpaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSpaceRequest = new GetSpaceRequest([
            "unionId" => "cxUXxxxxxx"
        ]);
        try {
            $client->getSpaceWithOptions("854xxxxx", $getSpaceRequest, $getSpaceHeaders, new RuntimeOptions([]));
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

  getSpaceHeaders := &dingtalkstorage_1_0.GetSpaceHeaders{}
  getSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSpaceRequest := &dingtalkstorage_1_0.GetSpaceRequest{
    UnionId: tea.String("cxUXxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSpaceWithOptions(tea.String("854xxxxx"), getSpaceRequest, getSpaceHeaders, &util.RuntimeOptions{})
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
    let getSpaceHeaders = new $dingtalkstorage_1_0.GetSpaceHeaders({ });
    getSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getSpaceRequest = new $dingtalkstorage_1_0.GetSpaceRequest({
      unionId: "cxUXxxxxxx",
    });
    try {
      await client.getSpaceWithOptions("854xxxxx", getSpaceRequest, getSpaceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetSpaceHeaders getSpaceHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetSpaceHeaders();
            getSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetSpaceRequest getSpaceRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.GetSpaceRequest
            {
                UnionId = "cxUXxxxxxx",
            };
            try
            {
                client.GetSpaceWithOptions("854xxxxx", getSpaceRequest, getSpaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

python2

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys

from alibabacloud_dingtalkstorage_1_0.client import Client as dingtalkstorage_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalkstorage_1_0 import models as dingtalkstorage__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client():
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
    def main(args):
        client = Sample.create_client()
        get_space_headers = dingtalkstorage__1__0_models.GetSpaceHeaders()
        get_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_space_request = dingtalkstorage__1__0_models.GetSpaceRequest(
            union_id='cxUXxxxxxx'
        )
        try:
            client.get_space_with_options('854xxxxx', get_space_request, get_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

Swift

```
#!/usr/bin/env xcrun swift

import Cocoa
import Foundation
import Tea
import TeaUtils
import AlibabacloudDingtalkstorage10
import AlibabacloudOpenApi

open class Client {
    public static func createClient() throws -> AlibabacloudDingtalkstorage10.Client {
        var config: AlibabacloudOpenApi.Config = AlibabacloudOpenApi.Config([:])
        config.protocol_ = "https"
        config.regionId = "central"
        return AlibabacloudDingtalkstorage10.Client(config)
    }

    @available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
    public static func main(_ args: [String]?) async throws -> Void {
        var client: AlibabacloudDingtalkstorage10.Client = try Client.createClient()
        var getSpaceHeaders: AlibabacloudDingtalkstorage10.GetSpaceHeaders = AlibabacloudDingtalkstorage10.GetSpaceHeaders([:])
        getSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>"
        var getSpaceRequest: AlibabacloudDingtalkstorage10.GetSpaceRequest = AlibabacloudDingtalkstorage10.GetSpaceRequest([
            "unionId": "cxUXxxxxxx"
        ])
        do {
            try await client.getSpaceWithOptions("854xxxxx", getSpaceRequest as! AlibabacloudDingtalkstorage10.GetSpaceRequest, getSpaceHeaders as! AlibabacloudDingtalkstorage10.GetSpaceHeaders, TeaUtils.RuntimeOptions([:]))
        }
        catch {
            if error is Tea.TeaError {
                var err = error as! Tea.TeaError
                if (!TeaUtils.Client.empty(err.code) && !TeaUtils.Client.empty(err.message)) {
                }
            } else {
                throw error
            }
        }
    }
}

Client.main(CommandLine.arguments)
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| space | Object | 空间详情。 |
| id | String | 空间id。 |
| corpId | String | 空间归属企业的corpId。 |
| creatorId | String | 创建者unionId。 |
| ownerType | String | owner类型。   - **USER**：用户类型 - **APP**：App类型 |
| ownerId | String | 所有者标识。 |
| modifierId | String | 修改者unionId。 |
| usedQuota | Long | 已使用容量，单位Byte。 |
| quota | Long | 总容量，单位Byte。 |
| status | String | 空间状态。   - **NORMAL**：正常 - **DELETE**：已删除 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| appId | String | 开放平台应用appId |
| scene | String | 业务场景。 |
| sceneId | String | 场景Id。 |
| capabilities | Object | 空间能力项。 |
| canSearch | Boolean | 是否支持搜索。   - **true**：支持 - **false**：不支持 |
| canRename | Boolean | 是否支持重命名空间名称。   - **true**：支持 - **false**：不支持 |
| canRecordRecentFile | Boolean | 是否支持列入最近使用列表。   - **true**：支持 - **false**：不支持 |
| name | String | 空间名称。 |
| partitions | Array | 分区容量信息，最大值2。 |
| partitionType | String | 分区类型。   - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属Mini OSS存储分区 |
| quota | Object | 容量信息。 |
| used | Long | 实际已使用容量，单位Byte，最小值0。      表示该应用下所用文件占用容量的总和，文件的上传、复制、删除相关操作会对used的值做相应变更。 |
| max | Long | 最大容量，单位Byte。       - 当前应用容量被设置为max时，代表当前应用容量设置了上限，used参数值不能大于max参数值。 - 当前应用容量未设置为max时，返回空，此时应用共享该企业剩余可用容量。 |
| reserved | Long | 预分配剩余容量，单位Byte。      管理后台可以给应用或空间预分配容量，此字段表示预分配剩余容量，即预分配容量中未使用部分。如果没有设置预分配容，此字段是空。 |
| type | String | 容量类型。   - **SHARE**: 共享容量。此模式下，Quota.max为空，表示共享企业容量。 - **PRIVATE**: 预分配容量（专享容量）。此模式下，Quota.max设置值后，表示容量独占。       需要保证单个应用的可用容量不受其他应用影响时，可使用预分配容量（专享容量）。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "space" : {
    "id" : "854xxxxx",
    "corpId" : "ding12345",
    "creatorId" : "cHtUYxxxxx",
    "ownerType" : "USER",
    "ownerId" : "cHtUYxxxxx",
    "modifierId" : "xxxxx",
    "usedQuota" : 1024,
    "quota" : 1048576,
    "status" : "NORMAL",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "appId" : "app_id",
    "scene" : "scene",
    "sceneId" : "123",
    "capabilities" : {
      "canSearch" : true,
      "canRename" : true,
      "canRecordRecentFile" : true
    },
    "name" : "测试空间",
    "partitions" : [ {
      "partitionType" : "PUBLIC_OSS_PARTITION",
      "quota" : {
        "used" : 1024,
        "max" : 10000,
        "reserved" : 1000,
        "type" : "SHARE"
      }
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 403 | permissionDenied | %s | 用户缺少获取空间信息的权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
