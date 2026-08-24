---
title: "新建空间"
source_url: "https://open.dingtalk.com/document/development/new-space"
namespace: "development"
slug: "new-space"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 云盘（原钉盘） > 新建空间"
doc_id: "yivAgLdjsL"
updated_at: "2026-06-04 19:09:25"
---

> Source: https://open.dingtalk.com/document/development/new-space
> Path: 应用开发 / 服务端API / 文档/文件 > 云盘（原钉盘） > 新建空间
> Updated: 2026-06-04 19:09:25

# 新建空间

调用本接口，新建企业共享空间。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/drive/spaces |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Drive.Space.Write-钉盘应用盘空间写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 空间名称（不能为空）。 |
| unionId | String | 是 | 用户unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/drive/spaces HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:956exxx
Content-Type:application/json

{
  "name" : "新建空间名称",
  "unionId" : "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdrive_1_0.*;
import com.aliyun.dingtalkdrive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdrive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdrive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdrive_1_0.Client client = Sample.createClient();
        AddSpaceHeaders addSpaceHeaders = new AddSpaceHeaders();
        addSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddSpaceRequest addSpaceRequest = new AddSpaceRequest()
                .setName("新建空间名称")
                .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx");
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
        add_space_headers = dingtalkdrive__1__0_models.AddSpaceHeaders()
        add_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_space_request = dingtalkdrive__1__0_models.AddSpaceRequest(
            name='新建空间名称',
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
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
        add_space_headers = dingtalkdrive__1__0_models.AddSpaceHeaders()
        add_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_space_request = dingtalkdrive__1__0_models.AddSpaceRequest(
            name='新建空间名称',
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
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

use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddSpaceRequest;
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
        $addSpaceRequest = new AddSpaceRequest([
            "name" => "新建空间名称",
            "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
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
  dingtalkdrive_1_0  "github.com/alibabacloud-go/dingtalk/drive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  addSpaceHeaders := &dingtalkdrive_1_0.AddSpaceHeaders{}
  addSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addSpaceRequest := &dingtalkdrive_1_0.AddSpaceRequest{
    Name: tea.String("新建空间名称"),
    UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
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
import dingtalkdrive_1_0, * as $dingtalkdrive_1_0 from '@alicloud/dingtalk/drive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdrive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdrive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addSpaceHeaders = new $dingtalkdrive_1_0.AddSpaceHeaders({ });
    addSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let addSpaceRequest = new $dingtalkdrive_1_0.AddSpaceRequest({
      name: "新建空间名称",
      unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
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
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddSpaceHeaders addSpaceHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddSpaceHeaders();
            addSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddSpaceRequest addSpaceRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddSpaceRequest
            {
                Name = "新建空间名称",
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkdrive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdrive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdrive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdrive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddSpaceHeaders> addSpaceHeaders = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddSpaceHeaders>();
  addSpaceHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddSpaceRequest> addSpaceRequest = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddSpaceRequest>(map<string, boost::any>({
    {"name", boost::any(string("新建空间名称"))},
    {"unionId", boost::any(string("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"))}
  }));
  try {
    client->addSpaceWithOptions(addSpaceRequest, addSpaceHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| spaceId | String | 空间ID。 |
| spaceName | String | 空间名称。 |
| spaceType | String | 空间类型。 |
| quota | Long | 空间总额度。 |
| usedQuota | Long | 空间已使用额度。 |
| permissionMode | String | 授权模式，取值：   - **acl**：acl授权 - **custom**：自定义授权 |
| createTime | String | 创建时间。 |
| modifyTime | String | 修改时间。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "spaceId" : "12345",
  "spaceName" : "新建空间名称",
  "spaceType" : "org",
  "quota" : 1024000,
  "usedQuota" : 512000,
  "permissionMode" : "acl",
  "createTime" : "2016-02-28T10:47:08Z",
  "modifyTime" : "2016-02-28T10:47:08Z"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Invalid Param | 参数错误 |
| 400 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 400 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 400 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 400 | addSpace.forbiden | Add space is forbiden. | 你所在的组织的管理员已设置：禁止新建共享空间，已创建空间可正常使用 |
| 400 | name.invalid | Space name is invalid. | 空间名称非法 |
| 500 | unknown.error | Unknown Error | 未知错误 |
