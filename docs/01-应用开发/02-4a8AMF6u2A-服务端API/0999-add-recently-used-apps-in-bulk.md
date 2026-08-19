---
title: "批量添加最近使用应用"
source_url: "https://open.dingtalk.com/document/development/add-recently-used-apps-in-bulk"
namespace: "development"
slug: "add-recently-used-apps-in-bulk"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉工作台 > 批量添加最近使用应用"
doc_id: "DZRBJ8hUti"
updated_at: "2025-09-11 21:03:43"
---

> Source: https://open.dingtalk.com/document/development/add-recently-used-apps-in-bulk
> Path: 应用开发 / 服务端API / 钉钉工作台 > 批量添加最近使用应用
> Updated: 2025-09-11 21:03:43

# 批量添加最近使用应用

批量添加最近使用应用，企业可以把员工点击过的应用批量写入到工作台员工”最近使用“类型中。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workbench/components/recentUsed/batch |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workbench.Component.Write-工作台组件信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织corpId。 |
| usedAppDetailList | Array | 是 | 最近使用应用列表。 |
| agentId | String | 是 | 组织开通的应用Id，可通过调用[获取企业所有应用列表](0864-obtains-a-list-of-all-enterprise-applications.md)接口获取返回参数`agentId`字段。 |
| userId | String | 是 | 员工userId。 |

### 请求示例

HTTP

```
POST /v1.0/workbench/components/recentUsed/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:accessToken
Content-Type:application/json

{
  "corpId" : "ding48143d56cd15327624f2f5cc6abecb85",
  "usedAppDetailList" : [ {
    "agentId" : "2636835622"
  } ],
  "userId" : "642325391030949"
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
    public static com.aliyun.dingtalkworkbench_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkbench_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkbench_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkbench_1_0.models.AddRecentUserAppListHeaders addRecentUserAppListHeaders = new com.aliyun.dingtalkworkbench_1_0.models.AddRecentUserAppListHeaders();
        addRecentUserAppListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkbench_1_0.models.AddRecentUserAppListRequest.AddRecentUserAppListRequestUsedAppDetailList usedAppDetailList0 = new com.aliyun.dingtalkworkbench_1_0.models.AddRecentUserAppListRequest.AddRecentUserAppListRequestUsedAppDetailList()
                .setAgentId("2636835622");
        com.aliyun.dingtalkworkbench_1_0.models.AddRecentUserAppListRequest addRecentUserAppListRequest = new com.aliyun.dingtalkworkbench_1_0.models.AddRecentUserAppListRequest()
                .setCorpId("ding48143d56cd15327624f2f5cc6abecb85")
                .setUsedAppDetailList(java.util.Arrays.asList(
                    usedAppDetailList0
                ))
                .setUserId("642325391030949");
        try {
            client.addRecentUserAppListWithOptions(addRecentUserAppListRequest, addRecentUserAppListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workbench_1_0.client import Client as dingtalkworkbench_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workbench_1_0 import models as dingtalkworkbench__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkbench_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkbench_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_recent_user_app_list_headers = dingtalkworkbench__1__0_models.AddRecentUserAppListHeaders()
        add_recent_user_app_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        used_app_detail_list_0 = dingtalkworkbench__1__0_models.AddRecentUserAppListRequestUsedAppDetailList(
            agent_id='2636835622'
        )
        add_recent_user_app_list_request = dingtalkworkbench__1__0_models.AddRecentUserAppListRequest(
            corp_id='ding48143d56cd15327624f2f5cc6abecb85',
            used_app_detail_list=[
                used_app_detail_list_0
            ],
            user_id='642325391030949'
        )
        try:
            client.add_recent_user_app_list_with_options(add_recent_user_app_list_request, add_recent_user_app_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_recent_user_app_list_headers = dingtalkworkbench__1__0_models.AddRecentUserAppListHeaders()
        add_recent_user_app_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        used_app_detail_list_0 = dingtalkworkbench__1__0_models.AddRecentUserAppListRequestUsedAppDetailList(
            agent_id='2636835622'
        )
        add_recent_user_app_list_request = dingtalkworkbench__1__0_models.AddRecentUserAppListRequest(
            corp_id='ding48143d56cd15327624f2f5cc6abecb85',
            used_app_detail_list=[
                used_app_detail_list_0
            ],
            user_id='642325391030949'
        )
        try:
            await client.add_recent_user_app_list_with_options_async(add_recent_user_app_list_request, add_recent_user_app_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Models\AddRecentUserAppListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Models\AddRecentUserAppListRequest\usedAppDetailList;
use AlibabaCloud\SDK\Dingtalk\Vworkbench_1_0\Models\AddRecentUserAppListRequest;
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
        $addRecentUserAppListHeaders = new AddRecentUserAppListHeaders([]);
        $addRecentUserAppListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $usedAppDetailList0 = new usedAppDetailList([
            "agentId" => "2636835622"
        ]);
        $addRecentUserAppListRequest = new AddRecentUserAppListRequest([
            "corpId" => "ding48143d56cd15327624f2f5cc6abecb85",
            "usedAppDetailList" => [
                $usedAppDetailList0
            ],
            "userId" => "642325391030949"
        ]);
        try {
            $client->addRecentUserAppListWithOptions($addRecentUserAppListRequest, $addRecentUserAppListHeaders, new RuntimeOptions([]));
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
  dingtalkworkbench_1_0  "github.com/alibabacloud-go/dingtalk/workbench_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkworkbench_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkbench_1_0.Client{}
  _result, _err = dingtalkworkbench_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addRecentUserAppListHeaders := &dingtalkworkbench_1_0.AddRecentUserAppListHeaders{}
  addRecentUserAppListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  usedAppDetailList0 := &dingtalkworkbench_1_0.AddRecentUserAppListRequestUsedAppDetailList{
    AgentId: tea.String("2636835622"),
  }
  addRecentUserAppListRequest := &dingtalkworkbench_1_0.AddRecentUserAppListRequest{
    CorpId: tea.String("ding48143d56cd15327624f2f5cc6abecb85"),
    UsedAppDetailList: []*dingtalkworkbench_1_0.AddRecentUserAppListRequestUsedAppDetailList{usedAppDetailList0},
    UserId: tea.String("642325391030949"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddRecentUserAppListWithOptions(addRecentUserAppListRequest, addRecentUserAppListHeaders, &util.RuntimeOptions{})
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
import dingtalkworkbench_1_0, * as $dingtalkworkbench_1_0 from '@alicloud/dingtalk/workbench_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkbench_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkbench_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addRecentUserAppListHeaders = new $dingtalkworkbench_1_0.AddRecentUserAppListHeaders({ });
    addRecentUserAppListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let usedAppDetailList0 = new $dingtalkworkbench_1_0.AddRecentUserAppListRequestUsedAppDetailList({
      agentId: "2636835622",
    });
    let addRecentUserAppListRequest = new $dingtalkworkbench_1_0.AddRecentUserAppListRequest({
      corpId: "ding48143d56cd15327624f2f5cc6abecb85",
      usedAppDetailList: [
        usedAppDetailList0
      ],
      userId: "642325391030949",
    });
    try {
      await client.addRecentUserAppListWithOptions(addRecentUserAppListRequest, addRecentUserAppListHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkbench_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListHeaders addRecentUserAppListHeaders = new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListHeaders();
            addRecentUserAppListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListRequest.AddRecentUserAppListRequestUsedAppDetailList usedAppDetailList0 = new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListRequest.AddRecentUserAppListRequestUsedAppDetailList
            {
                AgentId = "2636835622",
            };
            AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListRequest addRecentUserAppListRequest = new AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListRequest
            {
                CorpId = "ding48143d56cd15327624f2f5cc6abecb85",
                UsedAppDetailList = new List<AlibabaCloud.SDK.Dingtalkworkbench_1_0.Models.AddRecentUserAppListRequest.AddRecentUserAppListRequestUsedAppDetailList>
                {
                    usedAppDetailList0
                },
                UserId = "642325391030949",
            };
            try
            {
                client.AddRecentUserAppListWithOptions(addRecentUserAppListRequest, addRecentUserAppListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 返回结果 |

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
| 400 | illegalParameter | illegal\_parameter | 必选参数错误 |
