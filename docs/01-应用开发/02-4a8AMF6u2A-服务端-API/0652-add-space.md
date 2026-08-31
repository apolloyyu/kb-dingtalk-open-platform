---
title: "添加空间"
source_url: "https://open.dingtalk.com/document/development/add-space"
namespace: "development"
slug: "add-space"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 空间管理 > 添加空间"
doc_id: "8V20ooS7X1"
updated_at: "2026-07-14 09:21:52"
---

> Source: https://open.dingtalk.com/document/development/add-space
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 空间管理 > 添加空间
> Updated: 2026-07-14 09:21:52

# 添加空间

调用本接口，在企业云盘下创建一个新的空间，在该空间内可以进行新建文件夹、上传文件等操作。

## **接口调用说明**

**存储空间介绍：**

- 存储空间属于企业云盘的一部分，但是调用本接口添加的空间在客户端云盘内是不可见的。
- 存储空间会占用企业云盘的空间。

**存储空间分类：**

- 用户空间，即USER空间。该空间的文件只能授予永久权限，要求授权者有管理权限才能授权。
- 应用空间，即APP空间。该空间的文件只能授予临时权限，不要求授权者有管理权限。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.Space.Write-企业存储空间写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| option | Object | 否 | 可选参数。 |
| name | String | 否 | 空间名称，默认无空间名称。 |
| quota | Long | 否 | 空间能使用的最大容量，单位Byte。      该参数不传，表示该空间容量没有具体容量限制，但是不超过企业云盘总容量。 |
| capabilities | Object | 否 | 空间能力项，默认表示不设置拓展能力项。 |
| canSearch | Boolean | 否 | 是否支持搜索：   - **true**：支持 - **false**：不支持，默认值。 |
| canRename | Boolean | 否 | 是否支持重命名空间名称：   - **true**：支持 - **false**：不支持，默认值。 |
| canRecordRecentFile | Boolean | 否 | 是否支持被列入最近使用列表：   - **true**：支持 - **false**：不支持，默认值。 |
| scene | String | 否 | 空间场景，该参数由开发者自定义传入。   - 该参数不传，默认值是`default`。 - 该参数值+`sceneId`已存在，本接口返回已创建的空间，不会创建新空间。 - 如需创建新的的独立空间，请传入不同的`scene`/`sceneId`值。 |
| sceneId | String | 否 | 空间场景Id，该参数值由开发者自定义传入。   - 该参数不传，默认值是0。 - 该参数`sceneId`+该参数值已存在，本接口返回已创建的空间，不会创建新空间。 - 如需创建新的的独立空间，请传入不同的 `scene`/`sceneId`值。 |
| ownerType | String | 否 | owner类型：   - **USER**：用户类型，默认值 - **APP**：App类型 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces?unionId=cHtUYxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "option" : {
    "name" : "测试空间",
    "quota" : 1024,
    "capabilities" : {
      "canSearch" : true,
      "canRename" : true,
      "canRecordRecentFile" : true
    },
    "scene" : "scene",
    "sceneId" : "123",
    "ownerType" : "USER"
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkstorage_1_0.*;
import com.aliyun.dingtalkstorage_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkstorage_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkstorage_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkstorage_1_0.Client client = Sample.createClient();
        AddSpaceHeaders addSpaceHeaders = new AddSpaceHeaders();
        addSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddSpaceRequest.AddSpaceRequestOptionCapabilities optionCapabilities = new AddSpaceRequest.AddSpaceRequestOptionCapabilities()
                .setCanSearch(true)
                .setCanRename(true)
                .setCanRecordRecentFile(true);
        AddSpaceRequest.AddSpaceRequestOption option = new AddSpaceRequest.AddSpaceRequestOption()
                .setName("测试空间")
                .setQuota(1024L)
                .setCapabilities(optionCapabilities)
                .setScene("scene")
                .setSceneId("123")
                .setOwnerType("USER");
        AddSpaceRequest addSpaceRequest = new AddSpaceRequest()
                .setUnionId("cHtUYxxxxx")
                .setOption(option);
        try {
            client.addSpaceWithOptions(addSpaceRequest, addSpaceHeaders, new RuntimeOptions());
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
        add_space_headers = dingtalkstorage__1__0_models.AddSpaceHeaders()
        add_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_capabilities = dingtalkstorage__1__0_models.AddSpaceRequestOptionCapabilities(
            can_search=True,
            can_rename=True,
            can_record_recent_file=True
        )
        option = dingtalkstorage__1__0_models.AddSpaceRequestOption(
            name='测试空间',
            quota=1024,
            capabilities=option_capabilities,
            scene='scene',
            scene_id='123',
            owner_type='USER'
        )
        add_space_request = dingtalkstorage__1__0_models.AddSpaceRequest(
            union_id='cHtUYxxxxx',
            option=option
        )
        try:
            client.add_space_with_options(add_space_request, add_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_space_headers = dingtalkstorage__1__0_models.AddSpaceHeaders()
        add_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_capabilities = dingtalkstorage__1__0_models.AddSpaceRequestOptionCapabilities(
            can_search=True,
            can_rename=True,
            can_record_recent_file=True
        )
        option = dingtalkstorage__1__0_models.AddSpaceRequestOption(
            name='测试空间',
            quota=1024,
            capabilities=option_capabilities,
            scene='scene',
            scene_id='123',
            owner_type='USER'
        )
        add_space_request = dingtalkstorage__1__0_models.AddSpaceRequest(
            union_id='cHtUYxxxxx',
            option=option
        )
        try:
            await client.add_space_with_options_async(add_space_request, add_space_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddSpaceRequest\option\capabilities;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddSpaceRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddSpaceRequest;
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
        $addSpaceHeaders = new AddSpaceHeaders([]);
        $addSpaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $optionCapabilities = new capabilities([
            "canSearch" => true,
            "canRename" => true,
            "canRecordRecentFile" => true
        ]);
        $option = new option([
            "name" => "测试空间",
            "quota" => 1024,
            "capabilities" => $optionCapabilities,
            "scene" => "scene",
            "sceneId" => "123",
            "ownerType" => "USER"
        ]);
        $addSpaceRequest = new AddSpaceRequest([
            "unionId" => "cHtUYxxxxx",
            "option" => $option
        ]);
        try {
            $client->addSpaceWithOptions($addSpaceRequest, $addSpaceHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkstorage_1_0  "github.com/alibabacloud-go/dingtalk/storage_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  addSpaceHeaders := &dingtalkstorage_1_0.AddSpaceHeaders{}
  addSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionCapabilities := &dingtalkstorage_1_0.AddSpaceRequestOptionCapabilities{
    CanSearch: tea.Bool(true),
    CanRename: tea.Bool(true),
    CanRecordRecentFile: tea.Bool(true),
  }
  option := &dingtalkstorage_1_0.AddSpaceRequestOption{
    Name: tea.String("测试空间"),
    Quota: tea.Int64(1024),
    Capabilities: optionCapabilities,
    Scene: tea.String("scene"),
    SceneId: tea.String("123"),
    OwnerType: tea.String("USER"),
  }
  addSpaceRequest := &dingtalkstorage_1_0.AddSpaceRequest{
    UnionId: tea.String("cHtUYxxxxx"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddSpaceWithOptions(addSpaceRequest, addSpaceHeaders, &util.RuntimeOptions{})
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
    let addSpaceHeaders = new $dingtalkstorage_1_0.AddSpaceHeaders({ });
    addSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let optionCapabilities = new $dingtalkstorage_1_0.AddSpaceRequestOptionCapabilities({
      canSearch: true,
      canRename: true,
      canRecordRecentFile: true,
    });
    let option = new $dingtalkstorage_1_0.AddSpaceRequestOption({
      name: "测试空间",
      quota: 1024,
      capabilities: optionCapabilities,
      scene: "scene",
      sceneId: "123",
      ownerType: "USER",
    });
    let addSpaceRequest = new $dingtalkstorage_1_0.AddSpaceRequest({
      unionId: "cHtUYxxxxx",
      option: option,
    });
    try {
      await client.addSpaceWithOptions(addSpaceRequest, addSpaceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceHeaders addSpaceHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceHeaders();
            addSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceRequest.AddSpaceRequestOption.AddSpaceRequestOptionCapabilities optionCapabilities = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceRequest.AddSpaceRequestOption.AddSpaceRequestOptionCapabilities
            {
                CanSearch = true,
                CanRename = true,
                CanRecordRecentFile = true,
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceRequest.AddSpaceRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceRequest.AddSpaceRequestOption
            {
                Name = "测试空间",
                Quota = 1024,
                Capabilities = optionCapabilities,
                Scene = "scene",
                SceneId = "123",
                OwnerType = "USER",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceRequest addSpaceRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddSpaceRequest
            {
                UnionId = "cHtUYxxxxx",
                Option = option,
            };
            try
            {
                client.AddSpaceWithOptions(addSpaceRequest, addSpaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| space | Object | 空间信息。 |
| id | String | 空间id。 |
| corpId | String | 空间所在企业corpId。 |
| creatorId | String | 创建者unionId。 |
| ownerType | String | owner类型。   - **USER**：用户类型，默认值 - **APP**：App类型 |
| ownerId | String | 所有者标识。 |
| modifierId | String | 修改者unionId。 |
| usedQuota | Long | 已使用容量，单位Byte。 |
| quota | Long | 总容量，单位Byte。 |
| status | String | 空间状态。   - **NORMAL**：正常 - **DELETE**：已删除 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| appId | String | 开放平台应用appId |
| scene | String | 业务场景。 |
| sceneId | String | 空间场景Id。 |
| capabilities | Object | 空间能力项。 |
| canSearch | Boolean | 是否支持搜索。   - **true**：支持 - **false**：不支持，默认值。 |
| canRename | Boolean | 是否支持重命名空间名称。   - **true**：支持 - **false**：不支持，默认值。 |
| canRecordRecentFile | Boolean | 是否支持被列入最近使用列表。   - **true**：支持 - **false**：不支持，默认值。 |
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
    "id" : "833xxxxx",
    "corpId" : "ding027xxxxx",
    "creatorId" : "cHtUYxxxxx",
    "ownerType" : "USER",
    "ownerId" : "xxxxx",
    "modifierId" : "cHtUYxxxxx",
    "usedQuota" : 1024,
    "quota" : 1048576,
    "status" : "NORMAL",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "scene" : "scene",
    "sceneId" : "123",
    "capabilities" : {
      "canSearch" : true,
      "canRename" : true,
      "canRecordRecentFile" : true
    },
    "name" : "测试空间"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.name | %s | 参数错误-name |
| 400 | paramError.scene | %s | 参数错误-scene |
| 400 | paramError.sceneId | %s | 参数错误-sceneId |
| 403 | permissionDenied | %s | 用户缺少创建空间的权限 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
