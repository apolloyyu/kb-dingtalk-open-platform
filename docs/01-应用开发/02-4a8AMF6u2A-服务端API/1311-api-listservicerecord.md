---
title: "分页获取企业下的服务记录信息"
source_url: "https://open.dingtalk.com/document/development/api-listservicerecord"
namespace: "development"
slug: "api-listservicerecord"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 视听智能服务 > 分页获取企业下的服务记录信息"
doc_id: "AVexb0PqpV"
updated_at: "2026-07-15 17:03:04"
---

> Source: https://open.dingtalk.com/document/development/api-listservicerecord
> Path: 应用开发 / 服务端API / 更多开放 > 视听智能服务 > 分页获取企业下的服务记录信息
> Updated: 2026-07-15 17:03:04

# 分页获取企业下的服务记录信息

调用本接口，分页获取企业下的服务记录信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/service-records |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.Sale.Service.Read-钉钉AI销售管理服务数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| maxResults | Integer | 否 | 每页返回的数据量，最多20条。 |
| nextToken | String | 否 | 下一页的数据token，首次查询可空。 |
| endTime | Long | 否 | 服务结束时间，单位毫秒。 |
| startTime | Long | 否 | 服务开始时间，单位毫秒。 |
| userId | String | 否 | 员工ID。 |
| teamCode | String | 否 | 团队编码，可通过[分页查询客户列表](1300-api-listcustomer.md)接口获取。 |
| customerId | String | 否 | 服务客户的客户ID，可通过[分页查询客户列表](1300-api-listcustomer.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/service-records?maxResults=10&nextToken=d45309d81673333b&endTime=123453&startTime=432123&userId=3243ad&teamCode=1234 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:11c3588e697234f4ac04c0cf56884012
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
    public static com.aliyun.dingtalkdvi_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdvi_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdvi_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdvi_1_0.models.ListServiceRecordHeaders listServiceRecordHeaders = new com.aliyun.dingtalkdvi_1_0.models.ListServiceRecordHeaders();
        listServiceRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.ListServiceRecordRequest listServiceRecordRequest = new com.aliyun.dingtalkdvi_1_0.models.ListServiceRecordRequest()
                .setMaxResults(10)
                .setNextToken("d45309d81673333b")
                .setEndTime(123453L)
                .setStartTime(432123L)
                .setUserId("3243ad")
                .setTeamCode("1234");
        try {
            client.listServiceRecordWithOptions(listServiceRecordRequest, listServiceRecordHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_service_record_headers = dingtalkdvi__1__0_models.ListServiceRecordHeaders()
        list_service_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_service_record_request = dingtalkdvi__1__0_models.ListServiceRecordRequest(
            max_results=10,
            next_token='d45309d81673333b',
            end_time=123453,
            start_time=432123,
            user_id='3243ad',
            team_code='1234'
        )
        try:
            client.list_service_record_with_options(list_service_record_request, list_service_record_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_service_record_headers = dingtalkdvi__1__0_models.ListServiceRecordHeaders()
        list_service_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_service_record_request = dingtalkdvi__1__0_models.ListServiceRecordRequest(
            max_results=10,
            next_token='d45309d81673333b',
            end_time=123453,
            start_time=432123,
            user_id='3243ad',
            team_code='1234'
        )
        try:
            await client.list_service_record_with_options_async(list_service_record_request, list_service_record_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListServiceRecordHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListServiceRecordRequest;
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
        $listServiceRecordHeaders = new ListServiceRecordHeaders([]);
        $listServiceRecordHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listServiceRecordRequest = new ListServiceRecordRequest([
            "maxResults" => 10,
            "nextToken" => "d45309d81673333b",
            "endTime" => 123453,
            "startTime" => 432123,
            "userId" => "3243ad",
            "teamCode" => "1234"
        ]);
        try {
            $client->listServiceRecordWithOptions($listServiceRecordRequest, $listServiceRecordHeaders, new RuntimeOptions([]));
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

  listServiceRecordHeaders := &dingtalkdvi_1_0.ListServiceRecordHeaders{}
  listServiceRecordHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listServiceRecordRequest := &dingtalkdvi_1_0.ListServiceRecordRequest{
    MaxResults: tea.Int32(10),
    NextToken: tea.String("d45309d81673333b"),
    EndTime: tea.Int64(123453),
    StartTime: tea.Int64(432123),
    UserId: tea.String("3243ad"),
    TeamCode: tea.String("1234"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListServiceRecordWithOptions(listServiceRecordRequest, listServiceRecordHeaders, &util.RuntimeOptions{})
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
    let listServiceRecordHeaders = new dingtalkdvi_1_0.ListServiceRecordHeaders({ });
    listServiceRecordHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listServiceRecordRequest = new dingtalkdvi_1_0.ListServiceRecordRequest({
      maxResults: 10,
      nextToken: 'd45309d81673333b',
      endTime: 123453,
      startTime: 432123,
      userId: '3243ad',
      teamCode: '1234',
    });
    try {
      await client.listServiceRecordWithOptions(listServiceRecordRequest, listServiceRecordHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceRecordHeaders listServiceRecordHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceRecordHeaders();
            listServiceRecordHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceRecordRequest listServiceRecordRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListServiceRecordRequest
            {
                MaxResults = 10,
                NextToken = "d45309d81673333b",
                EndTime = 123453,
                StartTime = 432123,
                UserId = "3243ad",
                TeamCode = "1234",
            };
            try
            {
                client.ListServiceRecordWithOptions(listServiceRecordRequest, listServiceRecordHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | String | 下一页查询的token,有下页数据时候返回。 |
| totalCount | Integer | 总量。 |
| result | Array | 服务记录列表。 |
| recordId | String | 服务记录ID。 |
| user | Object | 服务用户。员工离职后为空。 |
| name | String | 员工姓名。 |
| userId | String | 员工ID。 |
| deviceSn | String | 服务设备SN。 |
| startTimestamp | Long | 服务开始时间戳，单位毫秒。 |
| endTimestamp | Long | 服务结束时间戳，单位毫秒。 |
| duration | String | 服务持续时长，单位毫秒。 |
| customerId | String | 客户ID，仅在服务记录绑定过客户时返回。 |
| team | Object | 服务所属团队、门店信息。 |
| name | String | 团队名。 |
| code | String | 团队唯一编号。 |
| valid | Boolean | 是否属于有效服务记录 ：   - **true**：有效 - **false**：无效 |
| outBizData | String | 外部业务自定义数据。 |
| qualityInspectionScore | Integer | 质检分数。 |
| sceneInfo | Object | 场景信息。 |
| name | String | 场景名。 |
| code | String | 场景编码。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : "003122axxxx0c3c7",
  "totalCount" : 30,
  "result" : [ {
    "recordId" : "3dea-9xxxxe-5fd0",
    "user" : {
      "name" : "rui",
      "userId" : "092165"
    },
    "deviceSn" : "T-C4474303",
    "startTimestamp" : 1765171448000,
    "endTimestamp" : 1765171452000,
    "duration" : "180000",
    "customerId" : "1234",
    "team" : {
      "name" : "文一西路店",
      "code" : "f4c8271xxxxf135fe"
    },
    "valid" : true,
    "outBizData" : "2088070812345",
    "qualityInspectionScore" : 89,
    "sceneInfo" : {
      "name" : "展厅接待",
      "code" : "ZTJD"
    }
  } ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | 入参为空 | 入参为空 |
| 400 | param.nextToken.error | nextToken参数错误 | nextToken参数错误 |
