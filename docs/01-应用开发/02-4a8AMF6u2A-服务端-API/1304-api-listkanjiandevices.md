---
title: "分页查询看鉴 BV 设备列表"
source_url: "https://open.dingtalk.com/document/development/api-listkanjiandevices"
namespace: "development"
slug: "api-listkanjiandevices"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > DingTalk BV > 看鉴设备 > 分页查询看鉴 BV 设备列表"
doc_id: "doc_0997f1dd1aab4b7d"
updated_at: "2026-11-17 17:35:22"
---

> Source: https://open.dingtalk.com/document/development/api-listkanjiandevices
> Path: 应用开发 / 服务端 API / 视听智能服务 > DingTalk BV > 看鉴设备 > 分页查询看鉴 BV 设备列表
> Updated: 2026-11-17 17:35:22

# 分页查询看鉴 BV 设备列表

调用本接口，分页查询企业下的看鉴 BV 设备，返回设备序列号、名称、类型、绑定人 userId 和在线状态。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/devices |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Device.Read-钉钉AI看鉴设备数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cursor | String | 否 | 不透明游标，首页不传，取上一页返回的 nextCursor。 |
| pageSize | Long | 否 | 每页条数，默认10条，最小为1，最大为50。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/bv/kanjian/devices?cursor=MTA&pageSize=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0917f20187238a78c067e2f18901d52
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
    public static com.aliyun.dingtalkdvi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdvi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdvi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdvi_1_0.models.ListKanjianDevicesHeaders listKanjianDevicesHeaders = new com.aliyun.dingtalkdvi_1_0.models.ListKanjianDevicesHeaders();
        listKanjianDevicesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.ListKanjianDevicesRequest listKanjianDevicesRequest = new com.aliyun.dingtalkdvi_1_0.models.ListKanjianDevicesRequest()
                .setCursor("MTA")
                .setPageSize(10L);
        try {
            client.listKanjianDevicesWithOptions(listKanjianDevicesRequest, listKanjianDevicesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.dvi_1_0.client import Client as dingtalkdvi_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.dvi_1_0 import models as dingtalkdvi__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdvi_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdvi_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_kanjian_devices_headers = dingtalkdvi__1__0_models.ListKanjianDevicesHeaders()
        list_kanjian_devices_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_kanjian_devices_request = dingtalkdvi__1__0_models.ListKanjianDevicesRequest(
            cursor='MTA',
            page_size=10
        )
        try:
            client.list_kanjian_devices_with_options(list_kanjian_devices_request, list_kanjian_devices_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_kanjian_devices_headers = dingtalkdvi__1__0_models.ListKanjianDevicesHeaders()
        list_kanjian_devices_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_kanjian_devices_request = dingtalkdvi__1__0_models.ListKanjianDevicesRequest(
            cursor='MTA',
            page_size=10
        )
        try:
            await client.list_kanjian_devices_with_options_async(list_kanjian_devices_request, list_kanjian_devices_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListKanjianDevicesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListKanjianDevicesRequest;
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
        $listKanjianDevicesHeaders = new ListKanjianDevicesHeaders([]);
        $listKanjianDevicesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listKanjianDevicesRequest = new ListKanjianDevicesRequest([
            "cursor" => "MTA",
            "pageSize" => 10
        ]);
        try {
            $client->listKanjianDevicesWithOptions($listKanjianDevicesRequest, $listKanjianDevicesHeaders, new RuntimeOptions([]));
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
  dingtalkdvi_1_0  "github.com/alibabacloud-go/dingtalk/dvi_1_0"
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
func CreateClient () (_result *dingtalkdvi_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdvi_1_0.Client{}
  _result, _err = dingtalkdvi_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listKanjianDevicesHeaders := &dingtalkdvi_1_0.ListKanjianDevicesHeaders{}
  listKanjianDevicesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listKanjianDevicesRequest := &dingtalkdvi_1_0.ListKanjianDevicesRequest{
    Cursor: tea.String("MTA"),
    PageSize: tea.Int64(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListKanjianDevicesWithOptions(listKanjianDevicesRequest, listKanjianDevicesHeaders, &util.RuntimeOptions{})
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
const dingtalkdvi_1_0 = require('@alicloud/dingtalk/dvi_1_0');
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
    return new dingtalkdvi_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let listKanjianDevicesHeaders = new dingtalkdvi_1_0.ListKanjianDevicesHeaders({ });
    listKanjianDevicesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listKanjianDevicesRequest = new dingtalkdvi_1_0.ListKanjianDevicesRequest({
      cursor: 'MTA',
      pageSize: 10,
    });
    try {
      await client.listKanjianDevicesWithOptions(listKanjianDevicesRequest, listKanjianDevicesHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdvi_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdvi_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianDevicesHeaders listKanjianDevicesHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianDevicesHeaders();
            listKanjianDevicesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianDevicesRequest listKanjianDevicesRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianDevicesRequest
            {
                Cursor = "MTA",
                PageSize = 10,
            };
            try
            {
                client.ListKanjianDevicesWithOptions(listKanjianDevicesRequest, listKanjianDevicesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Object | 任务结果。 |
| hasMore | Boolean | 是否还有下一页：   - **true**：是 - **false**：否 |
| items | Array | 设备列表。 |
| bindUserId | String | 绑定人 userId，未绑定为空。 |
| deviceName | String | 设备名称。 |
| deviceSn | String | 设备序列号。 |
| nextCursor | String | 下一页游标，没有下一页时为空。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "hasMore" : true,
    "items" : [ {
      "bindUserId" : "manager1234",
      "deviceName" : "store-front",
      "deviceSn" : "BV0000000001"
    } ],
    "nextCursor" : "MTA"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数非法 | 分页参数或游标不合法 |
| 400 | invalid.corpId | 企业ID无效 | 企业标识无效 |
| 400 | orgId.mismatch | orgId 与任务记录不一致 | 企业标识不一致 |
| 400 | no.permission | 无操作权限 | 无调用权限 |
| 400 | param.empty | 参数为空 | 请求参数为空 |
