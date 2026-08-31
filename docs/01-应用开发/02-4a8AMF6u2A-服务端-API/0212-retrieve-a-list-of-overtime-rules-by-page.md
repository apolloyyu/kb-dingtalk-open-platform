---
title: "分页获取加班规则列表"
source_url: "https://open.dingtalk.com/document/development/retrieve-a-list-of-overtime-rules-by-page"
namespace: "development"
slug: "retrieve-a-list-of-overtime-rules-by-page"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 考勤规则 > 分页获取加班规则列表"
doc_id: "dGUTCzvZvz"
updated_at: "2026-06-01 16:47:19"
---

> Source: https://open.dingtalk.com/document/development/retrieve-a-list-of-overtime-rules-by-page
> Path: 应用开发 / 服务端 API / 考勤 > 考勤规则 > 分页获取加班规则列表
> Updated: 2026-06-01 16:47:19

# 分页获取加班规则列表

调用本接口，分页获取考勤打卡中设置的加班规则列表，包括规则名称和规则ID。

## 接口调用说明

例如，企业的考勤规则管理内有三个加班规则，分别为**审批后的打卡时间计算加班**、**以审批时间计算加班**和**以打卡时间计算加班**，如下图所示。

调用本接口，可获取三个加班规则的规则名称和规则ID。 ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2885238471/p961081.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/overtimeSettings |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_attendance\_group\_read-考勤组查询权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| pageNumber | Long | 是 | 分页起始页。  **[!NOTE]**  该参数值从1开始。 |
| pageSize | Long | 是 | 分页大小。  **[!NOTE]**  该参数最大不能超过50。 |

### 请求示例

HTTP

```
GET /v1.0/attendance/overtimeSettings?pageNumber=1&pageSize=10 HTTP/1.1
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
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkattendance_1_0.models.GetSimpleOvertimeSettingHeaders getSimpleOvertimeSettingHeaders = new com.aliyun.dingtalkattendance_1_0.models.GetSimpleOvertimeSettingHeaders();
        getSimpleOvertimeSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.GetSimpleOvertimeSettingRequest getSimpleOvertimeSettingRequest = new com.aliyun.dingtalkattendance_1_0.models.GetSimpleOvertimeSettingRequest()
                .setPageNumber(1L)
                .setPageSize(10L);
        try {
            client.getSimpleOvertimeSettingWithOptions(getSimpleOvertimeSettingRequest, getSimpleOvertimeSettingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.attendance_1_0.client import Client as dingtalkattendance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.attendance_1_0 import models as dingtalkattendance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkattendance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkattendance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_simple_overtime_setting_headers = dingtalkattendance__1__0_models.GetSimpleOvertimeSettingHeaders()
        get_simple_overtime_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_simple_overtime_setting_request = dingtalkattendance__1__0_models.GetSimpleOvertimeSettingRequest(
            page_number=1,
            page_size=10
        )
        try:
            client.get_simple_overtime_setting_with_options(get_simple_overtime_setting_request, get_simple_overtime_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_simple_overtime_setting_headers = dingtalkattendance__1__0_models.GetSimpleOvertimeSettingHeaders()
        get_simple_overtime_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_simple_overtime_setting_request = dingtalkattendance__1__0_models.GetSimpleOvertimeSettingRequest(
            page_number=1,
            page_size=10
        )
        try:
            await client.get_simple_overtime_setting_with_options_async(get_simple_overtime_setting_request, get_simple_overtime_setting_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetSimpleOvertimeSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetSimpleOvertimeSettingRequest;
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
        $getSimpleOvertimeSettingHeaders = new GetSimpleOvertimeSettingHeaders([]);
        $getSimpleOvertimeSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getSimpleOvertimeSettingRequest = new GetSimpleOvertimeSettingRequest([
            "pageNumber" => 1,
            "pageSize" => 10
        ]);
        try {
            $client->getSimpleOvertimeSettingWithOptions($getSimpleOvertimeSettingRequest, $getSimpleOvertimeSettingHeaders, new RuntimeOptions([]));
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
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkattendance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkattendance_1_0.Client{}
  _result, _err = dingtalkattendance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getSimpleOvertimeSettingHeaders := &dingtalkattendance_1_0.GetSimpleOvertimeSettingHeaders{}
  getSimpleOvertimeSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getSimpleOvertimeSettingRequest := &dingtalkattendance_1_0.GetSimpleOvertimeSettingRequest{
    PageNumber: tea.Int64(1),
    PageSize: tea.Int64(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetSimpleOvertimeSettingWithOptions(getSimpleOvertimeSettingRequest, getSimpleOvertimeSettingHeaders, &util.RuntimeOptions{})
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
import dingtalkattendance_1_0, * as $dingtalkattendance_1_0 from '@alicloud/dingtalk/attendance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkattendance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkattendance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getSimpleOvertimeSettingHeaders = new $dingtalkattendance_1_0.GetSimpleOvertimeSettingHeaders({ });
    getSimpleOvertimeSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getSimpleOvertimeSettingRequest = new $dingtalkattendance_1_0.GetSimpleOvertimeSettingRequest({
      pageNumber: 1,
      pageSize: 10,
    });
    try {
      await client.getSimpleOvertimeSettingWithOptions(getSimpleOvertimeSettingRequest, getSimpleOvertimeSettingHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkattendance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkattendance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetSimpleOvertimeSettingHeaders getSimpleOvertimeSettingHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetSimpleOvertimeSettingHeaders();
            getSimpleOvertimeSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetSimpleOvertimeSettingRequest getSimpleOvertimeSettingRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetSimpleOvertimeSettingRequest
            {
                PageNumber = 1,
                PageSize = 10,
            };
            try
            {
                client.GetSimpleOvertimeSettingWithOptions(getSimpleOvertimeSettingRequest, getSimpleOvertimeSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 获取的结果。 |
| pageNumber | Long | 当前页码。 |
| totalPage | Long | 总页数。 |
| items | Array | 加班规则列表。 |
| id | Long | 加班规则ID。 |
| name | String | 加班规则名称。 |
| settingId | Long | 加班规则settingId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "pageNumber" : 1,
    "totalPage" : 10,
    "items" : [ {
      "id" : 221375127,
      "name" : "以审批时间计算加班",
      "settingId" : 221375127
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | system.error | 系统异常 | 系统异常 |
| 400 | paging.parameter.error | 分页参数错误 | 分页参数错误 |
