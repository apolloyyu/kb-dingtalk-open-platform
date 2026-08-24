---
title: "获取巡检或保养记录"
source_url: "https://open.dingtalk.com/document/development/obtain-inspection-and-maintenance-records"
namespace: "development"
slug: "obtain-inspection-and-maintenance-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 设备上钉 > 获取巡检或保养记录"
doc_id: "hLsN31FzGu"
updated_at: "2026-06-04 19:11:20"
---

> Source: https://open.dingtalk.com/document/development/obtain-inspection-and-maintenance-records
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 设备上钉 > 获取巡检或保养记录
> Updated: 2026-06-04 19:11:20

# 获取巡检或保养记录

调用本接口，获取设备上钉应用内，设备的巡检记录或者保养记录。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/devicemng/customers/devices/inspectInfos/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Manufacture.DeviceData.Write-制造业设备信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageNumber | Integer | 否 | 当前页码，从1开始。 |
| pageSize | Integer | 否 | 当页大小，最大值20。 |
| deviceUuid | Array of String | 否 | 设备uuIi列表，调用[查询已经注册的设备信息](1113-query-information-about-a-registered-device.md)接口获取的uuid，最大值10。 |
| type | String | 否 | 类型。   - inspect：巡检 - protect：保养 |

### 请求示例

HTTP

```
POST /v1.0/devicemng/customers/devices/inspectInfos/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "pageNumber" : 1,
  "pageSize" : 10,
  "deviceUuid" : [ "deviceUuid-sdfsdf-sdfsdfsdf" ],
  "type" : "inspect"
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
    public static com.aliyun.dingtalkdevicemng_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdevicemng_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdevicemng_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdevicemng_1_0.models.ListInspectInfoHeaders listInspectInfoHeaders = new com.aliyun.dingtalkdevicemng_1_0.models.ListInspectInfoHeaders();
        listInspectInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdevicemng_1_0.models.ListInspectInfoRequest listInspectInfoRequest = new com.aliyun.dingtalkdevicemng_1_0.models.ListInspectInfoRequest()
                .setPageNumber(1)
                .setPageSize(10)
                .setDeviceUuid(java.util.Arrays.asList(
                    "deviceUuid-sdfsdf-sdfsdfsdf"
                ))
                .setType("inspect");
        try {
            client.listInspectInfoWithOptions(listInspectInfoRequest, listInspectInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_inspect_info_headers = dingtalkdevicemng__1__0_models.ListInspectInfoHeaders()
        list_inspect_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_inspect_info_request = dingtalkdevicemng__1__0_models.ListInspectInfoRequest(
            page_number=1,
            page_size=10,
            device_uuid=[
                'deviceUuid-sdfsdf-sdfsdfsdf'
            ],
            type='inspect'
        )
        try:
            client.list_inspect_info_with_options(list_inspect_info_request, list_inspect_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_inspect_info_headers = dingtalkdevicemng__1__0_models.ListInspectInfoHeaders()
        list_inspect_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_inspect_info_request = dingtalkdevicemng__1__0_models.ListInspectInfoRequest(
            page_number=1,
            page_size=10,
            device_uuid=[
                'deviceUuid-sdfsdf-sdfsdfsdf'
            ],
            type='inspect'
        )
        try:
            await client.list_inspect_info_with_options_async(list_inspect_info_request, list_inspect_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\ListInspectInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdevicemng_1_0\Models\ListInspectInfoRequest;
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
        $listInspectInfoHeaders = new ListInspectInfoHeaders([]);
        $listInspectInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listInspectInfoRequest = new ListInspectInfoRequest([
            "pageNumber" => 1,
            "pageSize" => 10,
            "deviceUuid" => [
                "deviceUuid-sdfsdf-sdfsdfsdf"
            ],
            "type" => "inspect"
        ]);
        try {
            $client->listInspectInfoWithOptions($listInspectInfoRequest, $listInspectInfoHeaders, new RuntimeOptions([]));
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
  dingtalkdevicemng_1_0  "github.com/alibabacloud-go/dingtalk/devicemng_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  listInspectInfoHeaders := &dingtalkdevicemng_1_0.ListInspectInfoHeaders{}
  listInspectInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listInspectInfoRequest := &dingtalkdevicemng_1_0.ListInspectInfoRequest{
    PageNumber: tea.Int32(1),
    PageSize: tea.Int32(10),
    DeviceUuid: []*string{tea.String("deviceUuid-sdfsdf-sdfsdfsdf")},
    Type: tea.String("inspect"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListInspectInfoWithOptions(listInspectInfoRequest, listInspectInfoHeaders, &util.RuntimeOptions{})
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
    let listInspectInfoHeaders = new $dingtalkdevicemng_1_0.ListInspectInfoHeaders({ });
    listInspectInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listInspectInfoRequest = new $dingtalkdevicemng_1_0.ListInspectInfoRequest({
      pageNumber: 1,
      pageSize: 10,
      deviceUuid: [
        "deviceUuid-sdfsdf-sdfsdfsdf"
      ],
      type: "inspect",
    });
    try {
      await client.listInspectInfoWithOptions(listInspectInfoRequest, listInspectInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListInspectInfoHeaders listInspectInfoHeaders = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListInspectInfoHeaders();
            listInspectInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListInspectInfoRequest listInspectInfoRequest = new AlibabaCloud.SDK.Dingtalkdevicemng_1_0.Models.ListInspectInfoRequest
            {
                PageNumber = 1,
                PageSize = 10,
                DeviceUuid = new List<string>
                {
                    "deviceUuid-sdfsdf-sdfsdfsdf"
                },
                Type = "inspect",
            };
            try
            {
                client.ListInspectInfoWithOptions(listInspectInfoRequest, listInspectInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCount | Long | 总共数量。 |
| success | Boolean | 是否成功，true表示成功。 |
| result | Array | 返回的结果列表。 |
| deviceName | String | 设备名称。 |
| deviceCode | String | 设备码。 |
| type | String | 类型。   - inspect：巡检 - protect：保养 |
| status | Integer | 巡检或者保养结果。   - 0：正常 - 1：异常 |
| repairStatus | Integer | 处理结果。   - 1：未修复 - 2：已修复 |
| maintenanceStaff | Array of String | 维修人员姓名列表。 |
| handleTime | String | 处理时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| remark | String | 巡检或保养表填写的内容。 |
| name | String | 巡检表或者保养表的名称。 |
| gmtCreate | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 111,
  "success" : true,
  "result" : [ {
    "deviceName" : "测试设备名称",
    "deviceCode" : "testDeviceCode",
    "type" : "inspect",
    "status" : 0,
    "repairStatus" : 1,
    "maintenanceStaff" : [ "小钉" ],
    "handleTime" : "2022-09-10T12:00Z",
    "remark" : "巡检项1：高度（正常)",
    "name" : "巡检表F",
    "gmtCreate" : "2022-09-10T12:00Z"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | deviceNotExist | 30000，设备不存在 | 设备不存在 |
| 400 | deviceIdError | 30006，设备id异常 | 设备id异常 |
