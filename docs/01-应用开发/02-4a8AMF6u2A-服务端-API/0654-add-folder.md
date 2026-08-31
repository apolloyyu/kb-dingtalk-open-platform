---
title: "添加文件夹"
source_url: "https://open.dingtalk.com/document/development/add-folder"
namespace: "development"
slug: "add-folder"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 文件管理 > 添加文件夹"
doc_id: "OhjbwS18tS"
updated_at: "2026-06-04 19:09:32"
---

> Source: https://open.dingtalk.com/document/development/add-folder
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 文件管理 > 添加文件夹
> Updated: 2026-06-04 19:09:32

# 添加文件夹

调用本接口，在存储空间内添加文件夹。

## **接口调用说明**

在添加存储空间后，可调用本接口在空间内添加文件夹。

- 存储空间类型为USER时，空间拥有权限的用户都有操作权限，其他员工调用[添加权限](0681-add-permissions-file.md)接口进行授权。
- 存储空间类型为APP时，任何人操作都需要调用[添加权限](0681-add-permissions-file.md)接口进行授权。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/spaces/{spaceId}/dentries/{parentId}/folders |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.File.Write-企业存储文件写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 空间Id，可调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| parentId | String | 是 | 父目录Id，调用[获取文件或文件夹列表](https://open.dingtalk.com/document/development/obtain-the-file-list-storage)接口获取。根目录时，该参数是0。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 文件夹的名称，命名有以下要求：   - 头尾不能包含空格，否则会自动去除 - 不能包含特殊字符，包括：制表符、\*、"、<、>、| - 不能以"."结尾 |
| option | Object | 否 | 可选参数。 |
| conflictStrategy | String | 否 | 文件夹名称冲突策略。   - **AUTO\_RENAME**：自动重命名，默认值 - **OVERWRITE**：覆盖 - **RETURN\_DENTRY\_IF\_EXISTS**：返回已存在文件夹 - **RETURN\_ERROR\_IF\_EXISTS**：文件夹已存在时报错 |
| appProperties | Array | 否 | 当前文件夹的应用属性列表，最大值3。 |
| name | String | 是 | 属性名称。 |
| value | String | 是 | 属性值。 |
| visibility | String | 是 | 属性可见性。   - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见 |

### 请求示例

HTTP

```
POST /v1.0/storage/spaces/833xxxxx/dentries/0/folders?unionId=cHtUxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "name" : "测试文件夹",
  "option" : {
    "conflictStrategy" : "AUTO_RENAME",
    "appProperties" : [ {
      "name" : "属性1",
      "value" : "属性值1",
      "visibility" : "PUBLIC"
    } ]
  }
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
        com.aliyun.dingtalkstorage_1_0.models.AddFolderHeaders addFolderHeaders = new com.aliyun.dingtalkstorage_1_0.models.AddFolderHeaders();
        addFolderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.AddFolderRequest.AddFolderRequestOptionAppProperties optionAppProperties0 = new com.aliyun.dingtalkstorage_1_0.models.AddFolderRequest.AddFolderRequestOptionAppProperties()
                .setName("属性1")
                .setValue("属性值1")
                .setVisibility("PUBLIC");
        com.aliyun.dingtalkstorage_1_0.models.AddFolderRequest.AddFolderRequestOption option = new com.aliyun.dingtalkstorage_1_0.models.AddFolderRequest.AddFolderRequestOption()
                .setConflictStrategy("AUTO_RENAME")
                .setAppProperties(java.util.Arrays.asList(
                    optionAppProperties0
                ));
        com.aliyun.dingtalkstorage_1_0.models.AddFolderRequest addFolderRequest = new com.aliyun.dingtalkstorage_1_0.models.AddFolderRequest()
                .setUnionId("cHtUxxxxx")
                .setName("测试文件夹")
                .setOption(option);
        try {
            client.addFolderWithOptions("833xxxxx", "0", addFolderRequest, addFolderHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_folder_headers = dingtalkstorage__1__0_models.AddFolderHeaders()
        add_folder_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_app_properties_0 = dingtalkstorage__1__0_models.AddFolderRequestOptionAppProperties(
            name='属性1',
            value='属性值1',
            visibility='PUBLIC'
        )
        option = dingtalkstorage__1__0_models.AddFolderRequestOption(
            conflict_strategy='AUTO_RENAME',
            app_properties=[
                option_app_properties_0
            ]
        )
        add_folder_request = dingtalkstorage__1__0_models.AddFolderRequest(
            union_id='cHtUxxxxx',
            name='测试文件夹',
            option=option
        )
        try:
            client.add_folder_with_options('833xxxxx', '0', add_folder_request, add_folder_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_folder_headers = dingtalkstorage__1__0_models.AddFolderHeaders()
        add_folder_headers.x_acs_dingtalk_access_token = '<your access token>'
        option_app_properties_0 = dingtalkstorage__1__0_models.AddFolderRequestOptionAppProperties(
            name='属性1',
            value='属性值1',
            visibility='PUBLIC'
        )
        option = dingtalkstorage__1__0_models.AddFolderRequestOption(
            conflict_strategy='AUTO_RENAME',
            app_properties=[
                option_app_properties_0
            ]
        )
        add_folder_request = dingtalkstorage__1__0_models.AddFolderRequest(
            union_id='cHtUxxxxx',
            name='测试文件夹',
            option=option
        )
        try:
            await client.add_folder_with_options_async('833xxxxx', '0', add_folder_request, add_folder_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddFolderHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddFolderRequest\option\appProperties;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddFolderRequest\option;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\AddFolderRequest;
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
        $addFolderHeaders = new AddFolderHeaders([]);
        $addFolderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $optionAppProperties0 = new appProperties([
            "name" => "属性1",
            "value" => "属性值1",
            "visibility" => "PUBLIC"
        ]);
        $option = new option([
            "conflictStrategy" => "AUTO_RENAME",
            "appProperties" => [
                $optionAppProperties0
            ]
        ]);
        $addFolderRequest = new AddFolderRequest([
            "unionId" => "cHtUxxxxx",
            "name" => "测试文件夹",
            "option" => $option
        ]);
        try {
            $client->addFolderWithOptions("833xxxxx", "0", $addFolderRequest, $addFolderHeaders, new RuntimeOptions([]));
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

  addFolderHeaders := &dingtalkstorage_1_0.AddFolderHeaders{}
  addFolderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  optionAppProperties0 := &dingtalkstorage_1_0.AddFolderRequestOptionAppProperties{
    Name: tea.String("属性1"),
    Value: tea.String("属性值1"),
    Visibility: tea.String("PUBLIC"),
  }
  option := &dingtalkstorage_1_0.AddFolderRequestOption{
    ConflictStrategy: tea.String("AUTO_RENAME"),
    AppProperties: []*dingtalkstorage_1_0.AddFolderRequestOptionAppProperties{optionAppProperties0},
  }
  addFolderRequest := &dingtalkstorage_1_0.AddFolderRequest{
    UnionId: tea.String("cHtUxxxxx"),
    Name: tea.String("测试文件夹"),
    Option: option,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddFolderWithOptions(tea.String("833xxxxx"), tea.String("0"), addFolderRequest, addFolderHeaders, &util.RuntimeOptions{})
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
    let addFolderHeaders = new $dingtalkstorage_1_0.AddFolderHeaders({ });
    addFolderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let optionAppProperties0 = new $dingtalkstorage_1_0.AddFolderRequestOptionAppProperties({
      name: "属性1",
      value: "属性值1",
      visibility: "PUBLIC",
    });
    let option = new $dingtalkstorage_1_0.AddFolderRequestOption({
      conflictStrategy: "AUTO_RENAME",
      appProperties: [
        optionAppProperties0
      ],
    });
    let addFolderRequest = new $dingtalkstorage_1_0.AddFolderRequest({
      unionId: "cHtUxxxxx",
      name: "测试文件夹",
      option: option,
    });
    try {
      await client.addFolderWithOptions("833xxxxx", "0", addFolderRequest, addFolderHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderHeaders addFolderHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderHeaders();
            addFolderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest.AddFolderRequestOption.AddFolderRequestOptionAppProperties optionAppProperties0 = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest.AddFolderRequestOption.AddFolderRequestOptionAppProperties
            {
                Name = "属性1",
                Value = "属性值1",
                Visibility = "PUBLIC",
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest.AddFolderRequestOption option = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest.AddFolderRequestOption
            {
                ConflictStrategy = "AUTO_RENAME",
                AppProperties = new List<AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest.AddFolderRequestOption.AddFolderRequestOptionAppProperties>
                {
                    optionAppProperties0
                },
            };
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest addFolderRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.AddFolderRequest
            {
                UnionId = "cHtUxxxxx",
                Name = "测试文件夹",
                Option = option,
            };
            try
            {
                client.AddFolderWithOptions("833xxxxx", "0", addFolderRequest, addFolderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| dentry | Object | 文件夹信息。 |
| id | String | 文件夹id。 |
| spaceId | String | 所在空间Id。 |
| parentId | String | 父目录Id。      该字段为0，表示根目录。 |
| type | String | 类型，本接口返回类型是固定值。   - **FOLDER**：文件夹 |
| name | String | 文件夹的名称。 |
| size | Long | 大小, 单位Byte。      本接口添加文件夹，不返回该字段。 |
| path | String | 文件夹在空间内的路径。 |
| version | Long | 版本。      本接口添加文件夹，不返回该字段。 |
| status | String | 状态。   - **NORMAL**：正常 - **DELETED**：已删除 |
| extension | String | 后缀。      本接口添加文件夹，不返回该字段。 |
| creatorId | String | 创建者unionId。 |
| modifierId | String | 修改者unionId。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| properties | Object | 文件夹属性。 |
| readOnly | Boolean | 是否只读。   - **true**：是 - **false**：否 |
| appProperties | Map<String, Array> | 在特定应用上的属性。key是空间的ownerId，value是属性列表。 |
|  | Array | 属性列表。 |
| name | String | 属性名。 |
| value | String | 属性值。 |
| visibility | String | 属性可见性。   - **PUBLIC**：所有应用都可见 - **PRIVATE**：仅限当前应用可见 |
| uuid | String | 标识字段。 |
| partitionType | String | 存储分区。   - **PUBLIC\_OSS\_PARTITION**：公有云OSS存储分区 - **MINI\_OSS\_PARTITION**：专属MiniOSS存储分区 |
| storageDriver | String | 驱动类型。   - **DINGTALK**：钉钉统一存储驱动 - **ALIDOC**：钉钉文档存储驱动 - **UNKNOWN**：未知驱动 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "dentry" : {
    "id" : "123",
    "spaceId" : "854xxxxx",
    "parentId" : "0",
    "type" : "FOLDER",
    "name" : "测试文件夹",
    "size" : 512,
    "path" : "/测试文件夹",
    "version" : 1,
    "status" : "NORMAL",
    "extension" : "txt",
    "creatorId" : "cHtUxxxxx",
    "modifierId" : "modifier_id",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z",
    "properties" : {
      "readOnly" : true
    },
    "appProperties" : [ {
      "name" : "property_name",
      "value" : "property_value",
      "visibility" : "PRIVATE"
    } ],
    "uuid" : "uuid",
    "partitionType" : "PUBLIC_OSS_PARTITION",
    "storageDriver" : "DINGTALK"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | operationConcurrentControl | %s | 并发控制 |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.conflictStrategy | %s | 参数错误-conflictStrategy |
| 400 | dentryNameIllegal | %s | 文件名非法 |
| 400 | dentryAlreadyExist | %s | 文件已存在 |
| 403 | permissionDenied | %s | 用户缺少添加文件夹的权限 |
| 404 | dentryNotExist | %s | 父目录不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
