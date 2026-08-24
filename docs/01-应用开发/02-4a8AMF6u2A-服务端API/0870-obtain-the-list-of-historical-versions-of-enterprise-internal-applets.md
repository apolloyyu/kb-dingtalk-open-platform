---
title: "获取企业内部小程序历史版本列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-list-of-historical-versions-of-enterprise-internal-applets"
namespace: "development"
slug: "obtain-the-list-of-historical-versions-of-enterprise-internal-applets"
group: "应用开发"
tab: "服务端API"
breadcrumb: "钉钉应用 > 版本管理 > 获取企业内部小程序历史版本列表"
doc_id: "isiqxQgE8g"
updated_at: "2026-07-14 09:22:22"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-list-of-historical-versions-of-enterprise-internal-applets
> Path: 应用开发 / 服务端API / 钉钉应用 > 版本管理 > 获取企业内部小程序历史版本列表
> Updated: 2026-07-14 09:22:22

# 获取企业内部小程序历史版本列表

通过本接口可获取企业内部小程序的历史版本列表，支持分页查询，便于进行版本追溯、回滚和分析。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/innerMiniApps/{agentId}/historyVersions |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_get\_microapp\_list-企业已安装的应用列表查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | Long | 是 | 应用AgentId。  image |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageNumber | Integer | 是 | 当前页。 |
| pageSize | Integer | 是 | 本次读取的最大数据记录数量。 |

### 请求示例

HTTP

```
GET /v1.0/microApp/innerMiniApps/1/historyVersions?pageNumber=1&pageSize=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a582bed908a53b819163a7ef8*****ed
Content-Type:application/json
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.PageInnerAppHistoryVersionHeaders pageInnerAppHistoryVersionHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.PageInnerAppHistoryVersionHeaders();
        pageInnerAppHistoryVersionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.PageInnerAppHistoryVersionRequest pageInnerAppHistoryVersionRequest = new com.aliyun.dingtalkmicro_app_1_0.models.PageInnerAppHistoryVersionRequest()
                .setPageNumber(1)
                .setPageSize(1);
        try {
            client.pageInnerAppHistoryVersionWithOptions("1", pageInnerAppHistoryVersionRequest, pageInnerAppHistoryVersionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        page_inner_app_history_version_headers = dingtalkmicro_app__1__0_models.PageInnerAppHistoryVersionHeaders()
        page_inner_app_history_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        page_inner_app_history_version_request = dingtalkmicro_app__1__0_models.PageInnerAppHistoryVersionRequest(
            page_number=1,
            page_size=1
        )
        try:
            client.page_inner_app_history_version_with_options('1', page_inner_app_history_version_request, page_inner_app_history_version_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        page_inner_app_history_version_headers = dingtalkmicro_app__1__0_models.PageInnerAppHistoryVersionHeaders()
        page_inner_app_history_version_headers.x_acs_dingtalk_access_token = '<your access token>'
        page_inner_app_history_version_request = dingtalkmicro_app__1__0_models.PageInnerAppHistoryVersionRequest(
            page_number=1,
            page_size=1
        )
        try:
            await client.page_inner_app_history_version_with_options_async('1', page_inner_app_history_version_request, page_inner_app_history_version_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\PageInnerAppHistoryVersionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\PageInnerAppHistoryVersionRequest;
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
        $pageInnerAppHistoryVersionHeaders = new PageInnerAppHistoryVersionHeaders([]);
        $pageInnerAppHistoryVersionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pageInnerAppHistoryVersionRequest = new PageInnerAppHistoryVersionRequest([
            "pageNumber" => 1,
            "pageSize" => 1
        ]);
        try {
            $client->pageInnerAppHistoryVersionWithOptions("1", $pageInnerAppHistoryVersionRequest, $pageInnerAppHistoryVersionHeaders, new RuntimeOptions([]));
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

  pageInnerAppHistoryVersionHeaders := &dingtalkmicroapp_1_0.PageInnerAppHistoryVersionHeaders{}
  pageInnerAppHistoryVersionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pageInnerAppHistoryVersionRequest := &dingtalkmicroapp_1_0.PageInnerAppHistoryVersionRequest{
    PageNumber: tea.Int32(1),
    PageSize: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PageInnerAppHistoryVersionWithOptions(tea.String("1"), pageInnerAppHistoryVersionRequest, pageInnerAppHistoryVersionHeaders, &util.RuntimeOptions{})
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
    let pageInnerAppHistoryVersionHeaders = new dingtalkmicroApp_1_0.PageInnerAppHistoryVersionHeaders({ });
    pageInnerAppHistoryVersionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let pageInnerAppHistoryVersionRequest = new dingtalkmicroApp_1_0.PageInnerAppHistoryVersionRequest({
      pageNumber: 1,
      pageSize: 1,
    });
    try {
      await client.pageInnerAppHistoryVersionWithOptions('1', pageInnerAppHistoryVersionRequest, pageInnerAppHistoryVersionHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PageInnerAppHistoryVersionHeaders pageInnerAppHistoryVersionHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PageInnerAppHistoryVersionHeaders();
            pageInnerAppHistoryVersionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PageInnerAppHistoryVersionRequest pageInnerAppHistoryVersionRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.PageInnerAppHistoryVersionRequest
            {
                PageNumber = 1,
                PageSize = 1,
            };
            try
            {
                client.PageInnerAppHistoryVersionWithOptions("1", pageInnerAppHistoryVersionRequest, pageInnerAppHistoryVersionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCount | Long | 当前小程序历史版本的总数量。 |
| miniAppVersionList | Array | 企业内部小程序版本号列表 |
| appVersionId | Long | 小程序版本号id，用于小程序的发布和回滚等操作的唯一标识。 |
| miniAppId | String | 小程序id |
| appVersion | String | 小程序版本号 |
| appVersionType | Integer | 小程序版本类型，取值：   - **0**：开发版本 - **2**：正式版本 - **3**：体验版本 |
| miniAppOnPc | Boolean | 是否支持PC端打开小程序，取值：   - **false**：只支持移动端 - **true**：既支持移动端又支持PC端 |
| createTime | String | 小程序版本创建时间，格式:yyyy-MM-dd HH:mm:ss |
| modifyTime | String | 小程序版本号更新时间，格式:yyyy-MM-dd HH:mm:ss |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 1,
  "miniAppVersionList" : [ {
    "appVersionId" : 1,
    "miniAppId" : "1",
    "appVersion" : "0.0.1",
    "appVersionType" : 0,
    "miniAppOnPc" : false,
    "createTime" : "2023-01-01 00:00:00",
    "modifyTime" : "2023-01-01 00:00:00"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | preCheckError | 前置校验失败: %s | 前置校验失败 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | appTypeNotSupport | 只支持企业自建小程序调用 | 只支持企业自建小程序调用 |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
