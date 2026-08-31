---
title: "查询自定义屏幕模板列表"
source_url: "https://open.dingtalk.com/document/development/api-querylistdevicecustomscreentemplate"
namespace: "development"
slug: "api-querylistdevicecustomscreentemplate"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 智能会议室 > 自定义屏幕模板 > 查询自定义屏幕模板列表"
doc_id: "shEdk9nDa7"
updated_at: "2026-06-02 13:18:24"
---

> Source: https://open.dingtalk.com/document/development/api-querylistdevicecustomscreentemplate
> Path: 应用开发 / 服务端 API / 音视频 > 智能会议室 > 自定义屏幕模板 > 查询自定义屏幕模板列表
> Updated: 2026-06-02 13:18:24

# 查询自定义屏幕模板列表

调用本接口，直接查询自定义屏幕模板列表信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/devices/screens/templateLists |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Rooms.DeviceTemplate.Read-钉钉会议Rooms系统自定义屏幕读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。  **[!NOTE]**    获取用户token的请求中，使用的入参`code`参数，在通过构造链接获取的过程中，scope范围必须为用户id和组织id，即`scope=openid corpid`。 |

### 请求示例

HTTP

```
GET /v1.0/rooms/devices/screens/templateLists HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxxx
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
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.QueryDeviceCustomTemplateListHeaders queryDeviceCustomTemplateListHeaders = new com.aliyun.dingtalkrooms_1_0.models.QueryDeviceCustomTemplateListHeaders();
        queryDeviceCustomTemplateListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.queryDeviceCustomTemplateListWithOptions(queryDeviceCustomTemplateListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.rooms_1_0.client import Client as dingtalkrooms_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.rooms_1_0 import models as dingtalkrooms__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrooms_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrooms_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_device_custom_template_list_headers = dingtalkrooms__1__0_models.QueryDeviceCustomTemplateListHeaders()
        query_device_custom_template_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.query_device_custom_template_list_with_options(query_device_custom_template_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_device_custom_template_list_headers = dingtalkrooms__1__0_models.QueryDeviceCustomTemplateListHeaders()
        query_device_custom_template_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.query_device_custom_template_list_with_options_async(query_device_custom_template_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\QueryDeviceCustomTemplateListHeaders;
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
        $queryDeviceCustomTemplateListHeaders = new QueryDeviceCustomTemplateListHeaders([]);
        $queryDeviceCustomTemplateListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->queryDeviceCustomTemplateListWithOptions($queryDeviceCustomTemplateListHeaders, new RuntimeOptions([]));
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
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrooms_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrooms_1_0.Client{}
  _result, _err = dingtalkrooms_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryDeviceCustomTemplateListHeaders := &dingtalkrooms_1_0.QueryDeviceCustomTemplateListHeaders{}
  queryDeviceCustomTemplateListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryDeviceCustomTemplateListWithOptions(queryDeviceCustomTemplateListHeaders, &util.RuntimeOptions{})
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
import dingtalkrooms_1_0, * as $dingtalkrooms_1_0 from '@alicloud/dingtalk/rooms_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrooms_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrooms_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryDeviceCustomTemplateListHeaders = new $dingtalkrooms_1_0.QueryDeviceCustomTemplateListHeaders({ });
    queryDeviceCustomTemplateListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.queryDeviceCustomTemplateListWithOptions(queryDeviceCustomTemplateListHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrooms_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrooms_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryDeviceCustomTemplateListHeaders queryDeviceCustomTemplateListHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.QueryDeviceCustomTemplateListHeaders();
            queryDeviceCustomTemplateListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.QueryDeviceCustomTemplateListWithOptions(queryDeviceCustomTemplateListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 响应结果。 |
| deviceCustomTemplates | Array | 模板内容列表。 |
| templateId | Long | 模板id。 |
| corpId | String | 所属企业corpId。 |
| logo | String | 模板logo。 |
| orgName | String | 模板企业名称。 |
| customDoc | String | 模板自定义文字内容。 |
| bgUrl | String | 模板自定义背景网址。 |
| bgImageList | Array of String | 图片mediaId。 |
| instruction | Boolean | 显示使用说明，取值：   - true：显示 - false：不显示 |
| bgType | Integer | 模板自定义背景类型。取值：   - 1：图片 - 2：网址 |
| isPicTop | Integer | 展示首页信息栏。取值：   - 0：展示 - 1：不展示 |
| templateName | String | 模板名称 |
| confType | Integer | 模板类型。取值：   - 1：默认模板 - 2：自定义模板 |
| showCalendarTitle | Boolean | 日程卡片展示日程标题。取值：   - true：展示 - false：不展示 |
| hideServerCodeWhenProjecting | Boolean | 投屏中隐藏投屏码。取值：   - true：隐藏 - false：不隐藏 |
| confSubType | Integer | 模板子类型，取值：   - 1：默认子类型 |
| desensitizeUserName | Boolean | 日程卡片脱敏预订人昵称。取值：   - true：脱敏 - false：不脱敏 |
| picturePlayInterval | Integer | 自定义背景图轮播间隔秒 |
| showCalendarCard | Boolean | 展示日程卡片。取值：   - true：展示 - false：不展示 |
| showFunctionCard | Boolean | 展示功能卡片。取值：   - true：展示 - false：不展示 |
| deviceTemplateMap | Map<String, Array of String> | 模板生效的设备unionId映射，key：模板id。 |
|  | Array of String | 设备unionId。 |
| groupIdTemplateMap | Map<String, Array of Long> | 模板生效的分组id映射，key：模板id。 |
|  | Array of Long | 分组id。 |
| roomIdTemplateMap | Map<String, Array of String> | 模板生效的会议室id映射，key：模板id。 |
|  | Array of String | 会议室id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "deviceCustomTemplates" : [ {
      "templateId" : 89,
      "corpId" : "dingc02f685fa06381c44acxxxxx0864d335",
      "logo" : "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
      "orgName" : "测试企业",
      "customDoc" : "测试文本",
      "bgUrl" : "https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png",
      "bgImageList" : [ "$iwElAqxxxxxxcDBgTRC0AF0QZU" ],
      "instruction" : false,
      "bgType" : 1,
      "isPicTop" : 1,
      "templateName" : "测试模板",
      "confType" : 1,
      "showCalendarTitle" : false,
      "hideServerCodeWhenProjecting" : false,
      "confSubType" : 1,
      "desensitizeUserName" : false,
      "picturePlayInterval" : 10,
      "showCalendarCard" : false,
      "showFunctionCard" : false
    } ],
    "deviceTemplateMap" : [ "2iPOLbpxxxxuwggiiqiPwiEiF" ],
    "groupIdTemplateMap" : [ 25 ],
    "roomIdTemplateMap" : [ "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4" ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数错误 |
| 400 | no.permission | No Permission | 无权限 |
| 500 | system.error | System Error | 系统错误 |
