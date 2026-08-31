---
title: "获取群活跃明细列表"
source_url: "https://open.dingtalk.com/document/development/obtains-the-group-activity-details-list"
namespace: "development"
slug: "obtains-the-group-activity-details-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 企业内部群 > 获取群活跃明细列表"
doc_id: "IBfZki7Bzv"
updated_at: "2026-06-04 19:10:00"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-group-activity-details-list
> Path: 应用开发 / 服务端 API / 专属钉钉 > 企业内部群 > 获取群活跃明细列表
> Updated: 2026-06-04 19:10:00

# 获取群活跃明细列表

调用本接口获取自己企业下群组的相关信息列表。

## 接口调用说明

本接口获取专属钉钉企业下群活跃明细列表。 目前仅支持获取以下群类型的明细：

- 1：全员群
- 2：部门群
- 3：内部群（其他）
- 4：场景群

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/data/activeGroups |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Common.Read-专属钉钉专属数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| statDate | String | 是 | 统计日期，例如：20220101。 |
| dingGroupId | String | 否 | 钉钉群组ID。 |
| pageNumber | Long | 是 | 分页起始页，该参数值从1开始。 |
| pageSize | Long | 是 | 分页大小，参数值建议不超过200。 |
| groupType | Long | 否 | 群类型。   - 1：全员群 - 2：部门群 - 3：内部群 - 4：场景群 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/data/activeGroups?statDate=20200305&dingGroupId=cidV3xxxrSuxxxxxxnB8o8gJw==&pageNumber=0&pageSize=10&groupType=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        GetGroupActiveInfoHeaders getGroupActiveInfoHeaders = new GetGroupActiveInfoHeaders();
        getGroupActiveInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetGroupActiveInfoRequest getGroupActiveInfoRequest = new GetGroupActiveInfoRequest()
                .setStatDate("20200305")
                .setDingGroupId("cidV3xxxrSuxxxxxxnB8o8gJw==")
                .setPageNumber(0L)
                .setPageSize(10L)
                .setGroupType(1L);
        try {
            client.getGroupActiveInfoWithOptions(getGroupActiveInfoRequest, getGroupActiveInfoHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_group_active_info_headers = dingtalkexclusive__1__0_models.GetGroupActiveInfoHeaders()
        get_group_active_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_group_active_info_request = dingtalkexclusive__1__0_models.GetGroupActiveInfoRequest(
            stat_date='20200305',
            ding_group_id='cidV3xxxrSuxxxxxxnB8o8gJw==',
            page_number=0,
            page_size=10,
            group_type=1
        )
        try:
            client.get_group_active_info_with_options(get_group_active_info_request, get_group_active_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_group_active_info_headers = dingtalkexclusive__1__0_models.GetGroupActiveInfoHeaders()
        get_group_active_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_group_active_info_request = dingtalkexclusive__1__0_models.GetGroupActiveInfoRequest(
            stat_date='20200305',
            ding_group_id='cidV3xxxrSuxxxxxxnB8o8gJw==',
            page_number=0,
            page_size=10,
            group_type=1
        )
        try:
            await client.get_group_active_info_with_options_async(get_group_active_info_request, get_group_active_info_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetGroupActiveInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetGroupActiveInfoRequest;
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
        $getGroupActiveInfoHeaders = new GetGroupActiveInfoHeaders([]);
        $getGroupActiveInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getGroupActiveInfoRequest = new GetGroupActiveInfoRequest([
            "statDate" => "20200305",
            "dingGroupId" => "cidV3xxxrSuxxxxxxnB8o8gJw==",
            "pageNumber" => 0,
            "pageSize" => 10,
            "groupType" => 1
        ]);
        try {
            $client->getGroupActiveInfoWithOptions($getGroupActiveInfoRequest, $getGroupActiveInfoHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getGroupActiveInfoHeaders := &dingtalkexclusive_1_0.GetGroupActiveInfoHeaders{}
  getGroupActiveInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getGroupActiveInfoRequest := &dingtalkexclusive_1_0.GetGroupActiveInfoRequest{
    StatDate: tea.String("20200305"),
    DingGroupId: tea.String("cidV3xxxrSuxxxxxxnB8o8gJw=="),
    PageNumber: tea.Int64(0),
    PageSize: tea.Int64(10),
    GroupType: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetGroupActiveInfoWithOptions(getGroupActiveInfoRequest, getGroupActiveInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getGroupActiveInfoHeaders = new $dingtalkexclusive_1_0.GetGroupActiveInfoHeaders({ });
    getGroupActiveInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getGroupActiveInfoRequest = new $dingtalkexclusive_1_0.GetGroupActiveInfoRequest({
      statDate: "20200305",
      dingGroupId: "cidV3xxxrSuxxxxxxnB8o8gJw==",
      pageNumber: 0,
      pageSize: 10,
      groupType: 1,
    });
    try {
      await client.getGroupActiveInfoWithOptions(getGroupActiveInfoRequest, getGroupActiveInfoHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetGroupActiveInfoHeaders getGroupActiveInfoHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetGroupActiveInfoHeaders();
            getGroupActiveInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetGroupActiveInfoRequest getGroupActiveInfoRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetGroupActiveInfoRequest
            {
                StatDate = "20200305",
                DingGroupId = "cidV3xxxrSuxxxxxxnB8o8gJw==",
                PageNumber = 0,
                PageSize = 10,
                GroupType = 1,
            };
            try
            {
                client.GetGroupActiveInfoWithOptions(getGroupActiveInfoRequest, getGroupActiveInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| data | Array | 返回结果。 |
| statDate | String | 统计时间。 |
| dingGroupId | String | 群组ID。 |
| groupCreateTime | String | 群组创建时间。 |
| groupCreateUserId | String | 群组创建者的unionId。 |
| groupCreateUserName | String | 群组创建用户姓名。 |
| groupName | String | 群名称。 |
| groupType | Long | 群类型，取值。   - **1**：全员群 - **2**：部门群 - **3**：内部群（其他） - **4**：场景群 |
| groupUserCnt1d | Integer | 最近1天群人数。 |
| sendMessageUserCnt1d | Long | 最近1天发消息人数。 |
| sendMessageCnt1d | Long | 最近1天发消息次数。 |
| openConvUv1d | Integer | 最近1天打开群人数。 |
| totalCount | Long | 总共数据条数。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "statDate" : "20210505",
    "dingGroupId" : "cidV3xxxrSuxxxxxxnB8o8gJw==",
    "groupCreateTime" : "2021-05-06 12:23:34",
    "groupCreateUserId" : "WFBkgJxxxxxxxxxxxjK4sgiEiE",
    "groupCreateUserName" : "小明",
    "groupName" : "示例群组",
    "groupType" : 1,
    "groupUserCnt1d" : 100,
    "sendMessageUserCnt1d" : 100,
    "sendMessageCnt1d" : 100,
    "openConvUv1d" : 100
  } ],
  "totalCount" : 1
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.blank | 没有传递必传参数 | 没有传递必传参数 |
| 400 | param.illegal | 参数不合法 | 参数不合法 |
| 500 | unknownError | 未知错误 | 未知错误 |
