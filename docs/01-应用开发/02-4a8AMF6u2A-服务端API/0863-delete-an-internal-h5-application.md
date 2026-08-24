---
title: "删除企业内部应用"
source_url: "https://open.dingtalk.com/document/development/delete-an-internal-h5-application"
namespace: "development"
slug: "delete-an-internal-h5-application"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉应用 > 应用管理 > 删除企业内部应用"
doc_id: "UCcY4sty4M"
updated_at: "2026-06-04 19:10:03"
---

> Source: https://open.dingtalk.com/document/development/delete-an-internal-h5-application
> Path: 应用开发 / 服务端API / 钉钉应用 > 应用管理 > 删除企业内部应用
> Updated: 2026-06-04 19:10:03

# 删除企业内部应用

通过本接口，管理员可安全地删除企业内部应用，删除后应用会进入24小时的待删除状态，期间可撤销删除操作，确保应用管理的安全性和可控性。

## **接口调用说明**

接口调用成功后，该应用不会被立即删除，会先进入待删除状态。

- 如果24小时内没有撤销删除操作，该应用会从企业内部应用列表中彻底删除。
- 如果24小时内单击**撤销删除**按钮，应用会恢复正常状态。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/apps/{agentId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-管理微应用的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | Long | 是 | 应用的agentId，请参考[基础概念-AgentId](https://open.dingtalk.com/document/development/basic-concepts-beta#884d363067bnq)。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUnionId | String | 是 | 操作人的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。      操作删除的员工必须满足是以下两种身份之一，才可以成功删除应用，否则接口会报错**不合法的agentId**。   - 该应用所在企业的创建者。 - 该应用的创建人。 |

### 请求示例

HTTP

```
DELETE /v1.0/microApp/apps/123?opUnionId=z275qxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:692b2xyxxxx
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.DeleteInnerAppHeaders deleteInnerAppHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.DeleteInnerAppHeaders();
        deleteInnerAppHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.DeleteInnerAppRequest deleteInnerAppRequest = new com.aliyun.dingtalkmicro_app_1_0.models.DeleteInnerAppRequest()
                .setOpUnionId("z275qxxx");
        try {
            client.deleteInnerAppWithOptions("123", deleteInnerAppRequest, deleteInnerAppHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.micro_app_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmicroApp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmicroApp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_inner_app_headers = dingtalkmicro_app__1__0_models.DeleteInnerAppHeaders()
        delete_inner_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_inner_app_request = dingtalkmicro_app__1__0_models.DeleteInnerAppRequest(
            op_union_id='z275qxxx'
        )
        try:
            client.delete_inner_app_with_options('123', delete_inner_app_request, delete_inner_app_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_inner_app_headers = dingtalkmicro_app__1__0_models.DeleteInnerAppHeaders()
        delete_inner_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_inner_app_request = dingtalkmicro_app__1__0_models.DeleteInnerAppRequest(
            op_union_id='z275qxxx'
        )
        try:
            await client.delete_inner_app_with_options_async('123', delete_inner_app_request, delete_inner_app_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\DeleteInnerAppHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\DeleteInnerAppRequest;
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
        $deleteInnerAppHeaders = new DeleteInnerAppHeaders([]);
        $deleteInnerAppHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteInnerAppRequest = new DeleteInnerAppRequest([
            "opUnionId" => "z275qxxx"
        ]);
        try {
            $client->deleteInnerAppWithOptions("123", $deleteInnerAppRequest, $deleteInnerAppHeaders, new RuntimeOptions([]));
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
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
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
func CreateClient () (_result *dingtalkmicroapp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmicroapp_1_0.Client{}
  _result, _err = dingtalkmicroapp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteInnerAppHeaders := &dingtalkmicroapp_1_0.DeleteInnerAppHeaders{}
  deleteInnerAppHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteInnerAppRequest := &dingtalkmicroapp_1_0.DeleteInnerAppRequest{
    OpUnionId: tea.String("z275qxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteInnerAppWithOptions(tea.String("123"), deleteInnerAppRequest, deleteInnerAppHeaders, &util.RuntimeOptions{})
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
const dingtalkmicroApp_1_0 = require('@alicloud/dingtalk/microApp_1_0');
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
    return new dingtalkmicroApp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let deleteInnerAppHeaders = new dingtalkmicroApp_1_0.DeleteInnerAppHeaders({ });
    deleteInnerAppHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let deleteInnerAppRequest = new dingtalkmicroApp_1_0.DeleteInnerAppRequest({
      opUnionId: 'z275qxxx',
    });
    try {
      await client.deleteInnerAppWithOptions('123', deleteInnerAppRequest, deleteInnerAppHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.DeleteInnerAppHeaders deleteInnerAppHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.DeleteInnerAppHeaders();
            deleteInnerAppHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.DeleteInnerAppRequest deleteInnerAppRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.DeleteInnerAppRequest
            {
                OpUnionId = "z275qxxx",
            };
            try
            {
                client.DeleteInnerAppWithOptions("123", deleteInnerAppRequest, deleteInnerAppHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否删除成功，true表示删除成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | invalidUser | 用户id不合法，不在对应企业中 | 用户id不合法，不在对应企业中 |
| 400 | invalidEcologicalCorpId | 不合法的合作空间corpId | 不合法的合作空间corpId |
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 500 | systemError | 系统繁忙 | 系统繁忙 |
