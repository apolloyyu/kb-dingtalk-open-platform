---
title: "查询已经注册的设备信息"
source_url: "https://open.dingtalk.com/document/development/query-information-about-a-registered-device"
namespace: "development"
slug: "query-information-about-a-registered-device"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 设备上钉 > 查询已经注册的设备信息"
doc_id: "UOg7aWsTlm"
updated_at: "2025-09-23 19:22:26"
---

> Source: https://open.dingtalk.com/document/development/query-information-about-a-registered-device
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 设备上钉 > 查询已经注册的设备信息
> Updated: 2025-09-23 19:22:26

# 查询已经注册的设备信息

调用本接口，分页查询已经注册的设备信息，可以通过设备类型、分组标识和设备编号进行查询。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/devicemng/customers/devices/activations/infos |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Manufacture.DeviceData.Write-制造业设备信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| deviceTypeId | String | 否 | 设备型号。  **[!NOTE]**  该参数需线下提供，请通过[技术支持-在线答疑](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)咨询。 |
| pageNumber | Integer | 否 | 当前页码，从1开始。 |
| groupId | String | 否 | 分组标识。  **[!NOTE]**  该参数需线下提供，请通过[技术支持-在线答疑](../07-TjCzIgfQs3-平台服务/0044-ngliko.md)咨询。 |
| pageSize | Integer | 否 | 每页大小，最大值50。 |
| deviceCode | String | 否 | 设备编号，可调用[查询已经注册的设备信息](#)接口获取。 |
| deviceCategory | Integer | 否 | 设备分类。   - 0：设备 - 1：助手 |

### 请求示例

HTTP

```
GET /v1.0/devicemng/customers/devices/activations/infos?deviceTypeId=xxxxx&pageNumber=1&groupId=xxxx&pageSize=20&deviceCode=xxxx&deviceCategory=0 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdevicemng_1_0.*;
import com.aliyun.dingtalkdevicemng_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdevicemng_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdevicemng_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdevicemng_1_0.Client client = Sample.createClient();
        ListActivateDevicesHeaders listActivateDevicesHeaders = new ListActivateDevicesHeaders();
        listActivateDevicesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListActivateDevicesRequest listActivateDevicesRequest = new ListActivateDevicesRequest()
                .setDeviceTypeId("xxxxx")
                .setPageNumber(1)
                .setGroupId("xxxx")
                .setPageSize(20)
                .setDeviceCode("xxxx")
                .setDeviceCategory(0);
        try {
            client.listActivateDevicesWithOptions(listActivateDevicesRequest, listActivateDevicesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.devicemng_1_0.client import Client as dingtalkdevicemng_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.devicemng_1_0 import models as dingtalkdevicemng__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdevicemng_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdevicemng_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_activate_devices_headers = dingtalkdevicemng__1__0_models.ListActivateDevicesHeaders()
        list_activate_devices_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_activate_devices_request = dingtalkdevicemng__1__0_models.ListActivateDevicesRequest(
            device_type_id='xxxxx',
            page_number=1,
            group_id='xxxx',
            page_size=20,
            device_code='xxxx',
            device_category=0
        )
        try:
            client.list_activate_devices_with_options(list_activate_devices_request, list_activate_devices_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_activate_devices_headers = dingtalkdevicemng__1__0_models.ListActivateDevicesHeaders()
        list_activate_devices_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_activate_devices_request = dingtalkdevicemng__1__0_models.ListActivateDevicesRequest(
            device_type_id='xxxxx',
            page_number=1,
            group_id='xxxx',
            page_size=20,
            device_code='xxxx',
            device_category=0
        )
        try:
            await client.list_activate_devices_with_options_async(list_activate_devices_request, list_activate_devices_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\ListActivateDevicesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\ListActivateDevicesRequest;
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
        $listActivateDevicesHeaders = new ListActivateDevicesHeaders([]);
        $listActivateDevicesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listActivateDevicesRequest = new ListActivateDevicesRequest([
            "deviceTypeId" => "xxxxx",
            "pageNumber" => 1,
            "groupId" => "xxxx",
            "pageSize" => 20,
            "deviceCode" => "xxxx",
            "deviceCategory" => 0
        ]);
        try {
            $client->listActivateDevicesWithOptions($listActivateDevicesRequest, $listActivateDevicesHeaders, new RuntimeOptions([]));
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
  dingtalkdevicemng_1_0  "github.com/alibabacloud-go/dingtalk/devicemng_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdevicemng_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdevicemng_1_0.Client{}
  _result, _err = dingtalkdevicemng_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listActivateDevicesHeaders := &dingtalkdevicemng_1_0.ListActivateDevicesHeaders{}
  listActivateDevicesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listActivateDevicesRequest := &dingtalkdevicemng_1_0.ListActivateDevicesRequest{
    DeviceTypeId: tea.String("xxxxx"),
    PageNumber: tea.Int32(1),
    GroupId: tea.String("xxxx"),
    PageSize: tea.Int32(20),
    DeviceCode: tea.String("xxxx"),
    DeviceCategory: tea.Int32(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListActivateDevicesWithOptions(listActivateDevicesRequest, listActivateDevicesHeaders, &util.RuntimeOptions{})
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
import dingtalkdevicemng_1_0, * as $dingtalkdevicemng_1_0 from '@alicloud/dingtalk/devicemng_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdevicemng_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdevicemng_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listActivateDevicesHeaders = new $dingtalkdevicemng_1_0.ListActivateDevicesHeaders({ });
    listActivateDevicesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listActivateDevicesRequest = new $dingtalkdevicemng_1_0.ListActivateDevicesRequest({
      deviceTypeId: "xxxxx",
      pageNumber: 1,
      groupId: "xxxx",
      pageSize: 20,
      deviceCode: "xxxx",
      deviceCategory: 0,
    });
    try {
      await client.listActivateDevicesWithOptions(listActivateDevicesRequest, listActivateDevicesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListActivateDevicesHeaders listActivateDevicesHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListActivateDevicesHeaders();
            listActivateDevicesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListActivateDevicesRequest listActivateDevicesRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListActivateDevicesRequest
            {
                DeviceTypeId = "xxxxx",
                PageNumber = 1,
                GroupId = "xxxx",
                PageSize = 20,
                DeviceCode = "xxxx",
                DeviceCategory = 0,
            };
            try
            {
                client.ListActivateDevicesWithOptions(listActivateDevicesRequest, listActivateDevicesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCount | Long | 返回总数。 |
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |
| result | Array | 返回的设备列表。 |
| bizExt | String | 拓展信息。  **[!NOTE]**    该字段暂时返回为空。 |
| deviceCallbackUrl | String | 设备回调链接。 |
| deviceCode | String | 设备编号。 |
| deviceDetailUrl | String | 设备详情链接。 |
| deviceName | String | 设备名称。 |
| groupUuid | String | 设备分组标识。 |
| icon | String | 设备标题。  **[!NOTE]**    该字段暂无使用场景。 |
| introduction | String | 设备的简介。 |
| typeUuid | String | 设备型号。 |
| uuid | String | 钉钉侧设备标识。 |
| deviceCategory | Integer | 设备分类。   - 0：设备 - 1：助手 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 20,
  "success" : true,
  "result" : [ {
    "bizExt" : "xxxxxx",
    "deviceCallbackUrl" : "http://www.example.com",
    "deviceCode" : "xxxxx",
    "deviceDetailUrl" : "http://www.example.com",
    "deviceName" : "测试设备名称",
    "groupUuid" : "xxxx",
    "icon" : "xxxx",
    "introduction" : "简介",
    "typeUuid" : "xxxx",
    "uuid" : "xxxx",
    "deviceCategory" : 0
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | deviceTypeNotExist | 200001，设备类型不存在 | 设备类型不存在 |
| 400 | groupNotExist | 200002，分组不存在 | 分组不存在 |
| 500 | systemError | 100000，系统异常 | 系统异常 |
