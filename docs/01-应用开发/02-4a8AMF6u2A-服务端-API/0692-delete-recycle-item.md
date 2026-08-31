---
title: "删除回收项"
source_url: "https://open.dingtalk.com/document/development/delete-recycle-item"
namespace: "development"
slug: "delete-recycle-item"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 存储管理 > 回收站管理 > 删除回收项"
doc_id: "ZpVKfJCG5K"
updated_at: "2026-06-04 19:09:44"
---

> Source: https://open.dingtalk.com/document/development/delete-recycle-item
> Path: 应用开发 / 服务端 API / 文档/文件 > 存储管理 > 回收站管理 > 删除回收项
> Updated: 2026-06-04 19:09:44

# 删除回收项

调用本接口，删除回收站内的某个回收项。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/storage/recycleBins/{recycleBinId}/recycleItems/{recycleItemId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Storage.RecycleBin.Write-企业存储回收站写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| recycleBinId | String | 是 | 回收站Id，可调用[获取回收站信息](0687-obtain-information-about-the-recycle-bin.md)接口获取。 |
| recycleItemId | String | 是 | 回收项Id，可调用[获取回收项列表](0688-gets-the-list-of-recycle-items.md)接口获取id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 操作者unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
DELETE /v1.0/storage/recycleBins/pQy3R7xxxxx/recycleItems/2190xxxxx?unionId=chyxxxxx HTTP/1.1
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
        com.aliyun.dingtalkstorage_1_0.models.DeleteRecycleItemHeaders deleteRecycleItemHeaders = new com.aliyun.dingtalkstorage_1_0.models.DeleteRecycleItemHeaders();
        deleteRecycleItemHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkstorage_1_0.models.DeleteRecycleItemRequest deleteRecycleItemRequest = new com.aliyun.dingtalkstorage_1_0.models.DeleteRecycleItemRequest()
                .setUnionId("chyxxxxx");
        try {
            client.deleteRecycleItemWithOptions("pQy3R7xxxxx", "2190xxxxx", deleteRecycleItemRequest, deleteRecycleItemHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        delete_recycle_item_headers = dingtalkstorage__1__0_models.DeleteRecycleItemHeaders()
        delete_recycle_item_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_recycle_item_request = dingtalkstorage__1__0_models.DeleteRecycleItemRequest(
            union_id='chyxxxxx'
        )
        try:
            client.delete_recycle_item_with_options('pQy3R7xxxxx', '2190xxxxx', delete_recycle_item_request, delete_recycle_item_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_recycle_item_headers = dingtalkstorage__1__0_models.DeleteRecycleItemHeaders()
        delete_recycle_item_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_recycle_item_request = dingtalkstorage__1__0_models.DeleteRecycleItemRequest(
            union_id='chyxxxxx'
        )
        try:
            await client.delete_recycle_item_with_options_async('pQy3R7xxxxx', '2190xxxxx', delete_recycle_item_request, delete_recycle_item_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteRecycleItemHeaders;
use AlibabaCloud\SDK\Dingtalk\Vstorage_1_0\Models\DeleteRecycleItemRequest;
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
        $deleteRecycleItemHeaders = new DeleteRecycleItemHeaders([]);
        $deleteRecycleItemHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteRecycleItemRequest = new DeleteRecycleItemRequest([
            "unionId" => "chyxxxxx"
        ]);
        try {
            $client->deleteRecycleItemWithOptions("pQy3R7xxxxx", "2190xxxxx", $deleteRecycleItemRequest, $deleteRecycleItemHeaders, new RuntimeOptions([]));
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

  deleteRecycleItemHeaders := &dingtalkstorage_1_0.DeleteRecycleItemHeaders{}
  deleteRecycleItemHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteRecycleItemRequest := &dingtalkstorage_1_0.DeleteRecycleItemRequest{
    UnionId: tea.String("chyxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteRecycleItemWithOptions(tea.String("pQy3R7xxxxx"), tea.String("2190xxxxx"), deleteRecycleItemRequest, deleteRecycleItemHeaders, &util.RuntimeOptions{})
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
    let deleteRecycleItemHeaders = new $dingtalkstorage_1_0.DeleteRecycleItemHeaders({ });
    deleteRecycleItemHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deleteRecycleItemRequest = new $dingtalkstorage_1_0.DeleteRecycleItemRequest({
      unionId: "chyxxxxx",
    });
    try {
      await client.deleteRecycleItemWithOptions("pQy3R7xxxxx", "2190xxxxx", deleteRecycleItemRequest, deleteRecycleItemHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteRecycleItemHeaders deleteRecycleItemHeaders = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteRecycleItemHeaders();
            deleteRecycleItemHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteRecycleItemRequest deleteRecycleItemRequest = new AlibabaCloud.SDK.Dingtalkstorage_1_0.Models.DeleteRecycleItemRequest
            {
                UnionId = "chyxxxxx",
            };
            try
            {
                client.DeleteRecycleItemWithOptions("pQy3R7xxxxx", "2190xxxxx", deleteRecycleItemRequest, deleteRecycleItemHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 本次操作是否成功。   - **true**：成功 - **false**：失败 |

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
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.recycleBinId | %s | 参数错误-recycleBinId |
| 403 | permissionDenied | %s | 用户缺少对回收项原文件(夹)的管理权限 |
| 404 | recycleBinNotExist | %s | 回收站不存在 |
| 404 | recycleItemNotExist | %s | 回收项不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
