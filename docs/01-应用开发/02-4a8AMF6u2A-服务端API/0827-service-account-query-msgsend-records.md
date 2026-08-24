---
title: "查询群发消息列表"
source_url: "https://open.dingtalk.com/document/development/service-account-query-msgsend-records"
namespace: "development"
slug: "service-account-query-msgsend-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 消息群发 > 查询群发消息列表"
doc_id: "XJIKLgbGw4"
updated_at: "2026-06-02 19:12:39"
---

> Source: https://open.dingtalk.com/document/development/service-account-query-msgsend-records
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 消息群发 > 查询群发消息列表
> Updated: 2026-06-02 19:12:39

# 查询群发消息列表

调用本接口，查询指定服务号群发消息列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/follow/message/queryMsgSendRecords |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_message-企业内部服务号消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionid | String | 是 | 服务号的unionid。 |
| page\_number | Integer | 是 | 分页页码，从1开始。 |
| page\_size | Integer | 是 | 分页大小。 |
| start\_time | Long | 否 | 按时间范围搜索，开始时间，毫秒级时间戳。 |
| end\_time | Long | 否 | 按时间范围搜索，结束时间，毫秒级时间戳。 |
| status | Integer | 否 | 消息发送状态，不传时，默认查询发送成功的群发消息记录，消息状态如下：   - **0**：待发布 - **1**：发送中 - **2**：发布成功/已发布 - **3**：发送失败 - **4**：已撤回 |
| msgTypeList | Array of String | 否 | 消息类型，参考群发消息接口说明：   - **text**：文本类型 - **news\_card**：消息卡片 - **image**：图片类型 - **markdown**：markdown消息 - **action\_card**：action\_card卡片消息，支持动作行为 - **single\_news\_card**：新样式的消息卡片，只支持发送一个文章 |
| msg\_source | Integer | 否 | 消息创建来源   - **0**：查询所有来源创建的消息发送记录 - **1**：从「互动服务窗」企业应用创建保存的消息； - **2**：通过开放接口保存的消息，参数为空时默认为此项 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/follow/message/queryMsgSendRecords HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:tokenxxx
Content-Type:application/json

{
  "unionid" : "jYdxxxx0iE",
  "page_number" : 1,
  "page_size" : 10,
  "start_time" : 1766479616000,
  "end_time" : 1766479616000,
  "status" : 2,
  "msgTypeList" : [ "text" ],
  "msg_source" : 2
}
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.QueryMsgSendRecordsHeaders queryMsgSendRecordsHeaders = new com.aliyun.dingtalkexclusive_1_0.models.QueryMsgSendRecordsHeaders();
        queryMsgSendRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.QueryMsgSendRecordsRequest queryMsgSendRecordsRequest = new com.aliyun.dingtalkexclusive_1_0.models.QueryMsgSendRecordsRequest()
                .setUnionid("jYdxxxx0iE")
                .setPageNumber(1)
                .setPageSize(10)
                .setStartTime(1766479616000L)
                .setEndTime(1766479616000L)
                .setStatus(2)
                .setMsgTypeList(java.util.Arrays.asList(
                    "text"
                ))
                .setMsgSource(2);
        try {
            client.queryMsgSendRecordsWithOptions(queryMsgSendRecordsRequest, queryMsgSendRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_msg_send_records_headers = dingtalkexclusive__1__0_models.QueryMsgSendRecordsHeaders()
        query_msg_send_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_msg_send_records_request = dingtalkexclusive__1__0_models.QueryMsgSendRecordsRequest(
            unionid='jYdxxxx0iE',
            page_number=1,
            page_size=10,
            start_time=1766479616000,
            end_time=1766479616000,
            status=2,
            msg_type_list=[
                'text'
            ],
            msg_source=2
        )
        try:
            client.query_msg_send_records_with_options(query_msg_send_records_request, query_msg_send_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_msg_send_records_headers = dingtalkexclusive__1__0_models.QueryMsgSendRecordsHeaders()
        query_msg_send_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_msg_send_records_request = dingtalkexclusive__1__0_models.QueryMsgSendRecordsRequest(
            unionid='jYdxxxx0iE',
            page_number=1,
            page_size=10,
            start_time=1766479616000,
            end_time=1766479616000,
            status=2,
            msg_type_list=[
                'text'
            ],
            msg_source=2
        )
        try:
            await client.query_msg_send_records_with_options_async(query_msg_send_records_request, query_msg_send_records_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\QueryMsgSendRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\QueryMsgSendRecordsRequest;
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
        $queryMsgSendRecordsHeaders = new QueryMsgSendRecordsHeaders([]);
        $queryMsgSendRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryMsgSendRecordsRequest = new QueryMsgSendRecordsRequest([
            "unionid" => "jYdxxxx0iE",
            "pageNumber" => 1,
            "pageSize" => 10,
            "startTime" => 1766479616000,
            "endTime" => 1766479616000,
            "status" => 2,
            "msgTypeList" => [
                "text"
            ],
            "msgSource" => 2
        ]);
        try {
            $client->queryMsgSendRecordsWithOptions($queryMsgSendRecordsRequest, $queryMsgSendRecordsHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
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

  queryMsgSendRecordsHeaders := &dingtalkexclusive_1_0.QueryMsgSendRecordsHeaders{}
  queryMsgSendRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryMsgSendRecordsRequest := &dingtalkexclusive_1_0.QueryMsgSendRecordsRequest{
    Unionid: tea.String("jYdxxxx0iE"),
    PageNumber: tea.Int32(1),
    PageSize: tea.Int32(10),
    StartTime: tea.Int64(1766479616000),
    EndTime: tea.Int64(1766479616000),
    Status: tea.Int32(2),
    MsgTypeList: []*string{tea.String("text")},
    MsgSource: tea.Int32(2),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryMsgSendRecordsWithOptions(queryMsgSendRecordsRequest, queryMsgSendRecordsHeaders, &util.RuntimeOptions{})
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
const dingtalkexclusive_1_0 = require('@alicloud/dingtalk/exclusive_1_0');
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
    return new dingtalkexclusive_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryMsgSendRecordsHeaders = new dingtalkexclusive_1_0.QueryMsgSendRecordsHeaders({ });
    queryMsgSendRecordsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryMsgSendRecordsRequest = new dingtalkexclusive_1_0.QueryMsgSendRecordsRequest({
      unionid: 'jYdxxxx0iE',
      pageNumber: 1,
      pageSize: 10,
      startTime: 1766479616000,
      endTime: 1766479616000,
      status: 2,
      msgTypeList: [
        'text'
      ],
      msgSource: 2,
    });
    try {
      await client.queryMsgSendRecordsWithOptions(queryMsgSendRecordsRequest, queryMsgSendRecordsHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryMsgSendRecordsHeaders queryMsgSendRecordsHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryMsgSendRecordsHeaders();
            queryMsgSendRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryMsgSendRecordsRequest queryMsgSendRecordsRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryMsgSendRecordsRequest
            {
                Unionid = "jYdxxxx0iE",
                PageNumber = 1,
                PageSize = 10,
                StartTime = 1766479616000,
                EndTime = 1766479616000,
                Status = 2,
                MsgTypeList = new List<string>
                {
                    "text"
                },
                MsgSource = 2,
            };
            try
            {
                client.QueryMsgSendRecordsWithOptions(queryMsgSendRecordsRequest, queryMsgSendRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| errorcode | String | 返回码。 |
| errmsg | String | 返回码描述。 |
| result | Object | 返回数据。 |
| total\_count | Integer | 总记录数。 |
| item\_count | Integer | 本次获取的记录数。 |
| items | Array | 返回的数据列表。 |
| task\_id | String | 群发消息推送任务id。 |
| send\_time | Long | 消息发送时间。 |
| create\_time | Long | 群发消息任务创建时间。 |
| msg\_type | String | 消息类型，参考群发消息接口说明：   - **text**：文本类型 - **news\_card**：消息卡片 - **image**：图片类型 - **markdown**：markdown消息 - **action\_card**：action\_card卡片消息，支持动作行为 - **single\_news\_card**：新样式的消息卡片，只支持发送一个文章 |
| title | String | 消息标题。 |
| operator\_user\_id | String | 群发消息操作人员userId，只有在群发消息时传递操作人才会有次数据返回。 |
| msg\_source | Integer | 消息记录保存来源   - **1**：从「互动服务窗」企业应用中创建的消息群发记录 - **2**：通过开放接口发送的群发消息记录 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "errorcode" : "0",
  "errmsg" : "ok",
  "result" : {
    "total_count" : 50,
    "item_count" : 10,
    "items" : [ {
      "task_id" : "pushxxxxmwiEiE",
      "send_time" : 1766028831000,
      "create_time" : 1766028831000,
      "msg_type" : "text",
      "title" : "文本消息",
      "operator_user_id" : "2569131246",
      "msg_source" : 2
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.unionid | unionid非法 | unionid非法 |
| 400 | invalid.userid | 推送号非法 | 推送号非法 |
| 400 | publisher.not.exist | 推送号不存在 | 推送号不存在 |
| 500 | system.error | 系统异常 | 系统异常 |
