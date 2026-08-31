---
title: "以应用身份发送文件给指定用户"
source_url: "https://open.dingtalk.com/document/development/sends-a-storage-file-to-a-specified-user"
namespace: "development"
slug: "sends-a-storage-file-to-a-specified-user"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 群文件 > 以应用身份发送文件给指定用户"
doc_id: "8jD6jKyfXo"
updated_at: "2026-06-04 19:09:29"
---

> Source: https://open.dingtalk.com/document/development/sends-a-storage-file-to-a-specified-user
> Path: 应用开发 / 服务端 API / 文档/文件 > 群文件 > 以应用身份发送文件给指定用户
> Updated: 2026-06-04 19:09:29

# 以应用身份发送文件给指定用户

调用本接口，以应用身份发送文件给指定用户。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/convFile/apps/conversations/files/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-ConvFile.File.Send-群文件发送权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 接收文件的用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 文件所在空间ID，调用[添加空间](0652-add-space.md)接口获取id参数值。 |
| dentryId | String | 是 | 文件ID，可调用[获取文件或文件夹列表](https://open.dingtalk.com/document/development/obtain-the-file-list-storage)接口获取id参数值。 |

### 请求示例

HTTP

```
POST /v1.0/convFile/apps/conversations/files/send?unionId=cHtUYxxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "spaceId" : "864xxxxx",
  "dentryId" : "674xxxxx"
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
    public static com.aliyun.dingtalkconv_file_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconv_file_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconv_file_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconv_file_1_0.models.SendByAppHeaders sendByAppHeaders = new com.aliyun.dingtalkconv_file_1_0.models.SendByAppHeaders();
        sendByAppHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconv_file_1_0.models.SendByAppRequest sendByAppRequest = new com.aliyun.dingtalkconv_file_1_0.models.SendByAppRequest()
                .setUnionId("cHtUYxxxxx")
                .setSpaceId("864xxxxx")
                .setDentryId("674xxxxx");
        try {
            client.sendByAppWithOptions(sendByAppRequest, sendByAppHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.convFile_1_0.client import Client as dingtalkconvFile_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.convFile_1_0 import models as dingtalkconv_file__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconvFile_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconvFile_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_by_app_headers = dingtalkconv_file__1__0_models.SendByAppHeaders()
        send_by_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_by_app_request = dingtalkconv_file__1__0_models.SendByAppRequest(
            union_id='cHtUYxxxxx',
            space_id='864xxxxx',
            dentry_id='674xxxxx'
        )
        try:
            client.send_by_app_with_options(send_by_app_request, send_by_app_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_by_app_headers = dingtalkconv_file__1__0_models.SendByAppHeaders()
        send_by_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_by_app_request = dingtalkconv_file__1__0_models.SendByAppRequest(
            union_id='cHtUYxxxxx',
            space_id='864xxxxx',
            dentry_id='674xxxxx'
        )
        try:
            await client.send_by_app_with_options_async(send_by_app_request, send_by_app_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconv_file_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconv_file_1_0\Models\SendByAppHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconv_file_1_0\Models\SendByAppRequest;
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
        $sendByAppHeaders = new SendByAppHeaders([]);
        $sendByAppHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendByAppRequest = new SendByAppRequest([
            "unionId" => "cHtUYxxxxx",
            "spaceId" => "864xxxxx",
            "dentryId" => "674xxxxx"
        ]);
        try {
            $client->sendByAppWithOptions($sendByAppRequest, $sendByAppHeaders, new RuntimeOptions([]));
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
  dingtalkconvfile_1_0  "github.com/alibabacloud-go/dingtalk/convFile_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkconvfile_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconvfile_1_0.Client{}
  _result, _err = dingtalkconvfile_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendByAppHeaders := &dingtalkconvfile_1_0.SendByAppHeaders{}
  sendByAppHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendByAppRequest := &dingtalkconvfile_1_0.SendByAppRequest{
    UnionId: tea.String("cHtUYxxxxx"),
    SpaceId: tea.String("864xxxxx"),
    DentryId: tea.String("674xxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendByAppWithOptions(sendByAppRequest, sendByAppHeaders, &util.RuntimeOptions{})
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
import dingtalkconvFile_1_0, * as $dingtalkconvFile_1_0 from '@alicloud/dingtalk/convFile_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkconvFile_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkconvFile_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let sendByAppHeaders = new $dingtalkconvFile_1_0.SendByAppHeaders({ });
    sendByAppHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sendByAppRequest = new $dingtalkconvFile_1_0.SendByAppRequest({
      unionId: "cHtUYxxxxx",
      spaceId: "864xxxxx",
      dentryId: "674xxxxx",
    });
    try {
      await client.sendByAppWithOptions(sendByAppRequest, sendByAppHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkconv_file_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconv_file_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconv_file_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.SendByAppHeaders sendByAppHeaders = new AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.SendByAppHeaders();
            sendByAppHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.SendByAppRequest sendByAppRequest = new AlibabaCloud.SDK.Dingtalkconv_file_1_0.Models.SendByAppRequest
            {
                UnionId = "cHtUYxxxxx",
                SpaceId = "864xxxxx",
                DentryId = "674xxxxx",
            };
            try
            {
                client.SendByAppWithOptions(sendByAppRequest, sendByAppHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| file | Object | 发送到目标会话的文件信息。 |
| id | String | 文件ID。 |
| conversationId | String | 文件所在会话ID。 |
| spaceId | String | 文件所在空间ID。 |
| parentId | String | 文件所在的父目录ID。根目录时，该参数是0。 |
| type | String | 文件类型。   - **FILE**：文件 - **FOLDER**：文件夹       本接口只能发送文件。 |
| name | String | 文件名称。 |
| size | Long | 文件大小，单位Byte。 |
| path | String | 文件路径。 |
| version | Long | 文件版本。 |
| status | String | 文件状态。   - **NORMAL**：正常 - **DELETED**：已删除 - **EXPIRED**：已过期 |
| extension | String | 文件后缀。 |
| creatorId | String | 创建者unionId。 |
| modifierId | String | 修改者unionId。 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| modifiedTime | String | 修改时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| uuid | String | 业务uuid。      本接口不返回该字段。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "file" : {
    "id" : "674xxxxx",
    "conversationId" : "cidB1xxxxx",
    "spaceId" : "864xxxxx",
    "parentId" : "0",
    "type" : "FILE",
    "name" : "测试文件.xls",
    "size" : 256,
    "path" : "/测试文件.xls",
    "version" : 1,
    "status" : "NORMAL",
    "extension" : "xls",
    "creatorId" : "cHtUYxxxxx",
    "modifierId" : "cHtUYxxxxx",
    "createTime" : "2022-01-01T10:00:00Z",
    "modifiedTime" : "2022-01-01T10:00:00Z"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | paramError.spaceId | %s | 参数错误-spaceId |
| 400 | paramError.dentryId | %s | 参数错误-dentryId |
| 400 | permissionDenied | %s | 无权限 |
| 404 | spaceNotExist | %s | 空间不存在 |
| 404 | dentryNotExist | %s | 文件不存在 |
| 500 | systemError | %s | 系统错误 |
| 500 | unknownError | Unknown Error | 未知错误 |
