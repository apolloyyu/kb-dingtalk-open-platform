---
title: "分页查询看鉴记录列表"
source_url: "https://open.dingtalk.com/document/development/api-listkanjianrecords"
namespace: "development"
slug: "api-listkanjianrecords"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > BV 看鉴 > 看鉴记录 > 分页查询看鉴记录列表"
doc_id: "doc_9fd05c2b9ca44352"
updated_at: "2026-11-17 17:35:10"
---

> Source: https://open.dingtalk.com/document/development/api-listkanjianrecords
> Path: 应用开发 / 服务端 API / 视听智能服务 > BV 看鉴 > 看鉴记录 > 分页查询看鉴记录列表
> Updated: 2026-11-17 17:35:10

# 分页查询看鉴记录列表

调用本接口，分页查询企业下的看鉴 BV 设备录制记录，可按设备、时间段、主任务过滤。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/records |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Dvi.KanJian.Record.Read-钉钉AI看鉴记录数据读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUserId | String | 否 | 操作人userId，只返回该员工创建的记录。 |
| deviceSn | String | 否 | 按设备过滤，须为本企业设备，可根据[分页查询看鉴 BV 设备列表](1304-api-listkanjiandevices.md)接口获取。 |
| startTime | Long | 否 | 录制开始时间下限，毫秒时间戳。 |
| endTime | Long | 否 | 录制开始时间上限，毫秒时间戳。 |
| mainTaskId | String | 否 | 按主任务过滤。 |
| cursor | String | 否 | 不透明游标，首页不传；取上一页返回的 nextCursor。 |
| pageSize | Long | 否 | 默认 10，取值 1 到 50，超出返回 1002。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/bv/kanjian/records?operatorUserId=manager098&deviceSn=BV0000000001&startTime=1760000000000&endTime=1760086400000&mainTaskId=task0001&cursor=aWQ6MTAw&pageSize=10 HTTP/1.1
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
        com.aliyun.dingtalkdvi_1_0.models.ListKanjianRecordsHeaders listKanjianRecordsHeaders = new com.aliyun.dingtalkdvi_1_0.models.ListKanjianRecordsHeaders();
        listKanjianRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.ListKanjianRecordsRequest listKanjianRecordsRequest = new com.aliyun.dingtalkdvi_1_0.models.ListKanjianRecordsRequest()
                .setOperatorUserId("manager098")
                .setDeviceSn("BV0000000001")
                .setStartTime(1760000000000L)
                .setEndTime(1760086400000L)
                .setMainTaskId("task0001")
                .setCursor("aWQ6MTAw")
                .setPageSize(10L);
        try {
            client.listKanjianRecordsWithOptions(listKanjianRecordsRequest, listKanjianRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_kanjian_records_headers = dingtalkdvi__1__0_models.ListKanjianRecordsHeaders()
        list_kanjian_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_kanjian_records_request = dingtalkdvi__1__0_models.ListKanjianRecordsRequest(
            operator_user_id='manager098',
            device_sn='BV0000000001',
            start_time=1760000000000,
            end_time=1760086400000,
            main_task_id='task0001',
            cursor='aWQ6MTAw',
            page_size=10
        )
        try:
            client.list_kanjian_records_with_options(list_kanjian_records_request, list_kanjian_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_kanjian_records_headers = dingtalkdvi__1__0_models.ListKanjianRecordsHeaders()
        list_kanjian_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_kanjian_records_request = dingtalkdvi__1__0_models.ListKanjianRecordsRequest(
            operator_user_id='manager098',
            device_sn='BV0000000001',
            start_time=1760000000000,
            end_time=1760086400000,
            main_task_id='task0001',
            cursor='aWQ6MTAw',
            page_size=10
        )
        try:
            await client.list_kanjian_records_with_options_async(list_kanjian_records_request, list_kanjian_records_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListKanjianRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\ListKanjianRecordsRequest;
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
        $listKanjianRecordsHeaders = new ListKanjianRecordsHeaders([]);
        $listKanjianRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listKanjianRecordsRequest = new ListKanjianRecordsRequest([
            "operatorUserId" => "manager098",
            "deviceSn" => "BV0000000001",
            "startTime" => 1760000000000,
            "endTime" => 1760086400000,
            "mainTaskId" => "task0001",
            "cursor" => "aWQ6MTAw",
            "pageSize" => 10
        ]);
        try {
            $client->listKanjianRecordsWithOptions($listKanjianRecordsRequest, $listKanjianRecordsHeaders, new RuntimeOptions([]));
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

  listKanjianRecordsHeaders := &dingtalkdvi_1_0.ListKanjianRecordsHeaders{}
  listKanjianRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listKanjianRecordsRequest := &dingtalkdvi_1_0.ListKanjianRecordsRequest{
    OperatorUserId: tea.String("manager098"),
    DeviceSn: tea.String("BV0000000001"),
    StartTime: tea.Int64(1760000000000),
    EndTime: tea.Int64(1760086400000),
    MainTaskId: tea.String("task0001"),
    Cursor: tea.String("aWQ6MTAw"),
    PageSize: tea.Int64(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListKanjianRecordsWithOptions(listKanjianRecordsRequest, listKanjianRecordsHeaders, &util.RuntimeOptions{})
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
    let listKanjianRecordsHeaders = new dingtalkdvi_1_0.ListKanjianRecordsHeaders({ });
    listKanjianRecordsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listKanjianRecordsRequest = new dingtalkdvi_1_0.ListKanjianRecordsRequest({
      operatorUserId: 'manager098',
      deviceSn: 'BV0000000001',
      startTime: 1760000000000,
      endTime: 1760086400000,
      mainTaskId: 'task0001',
      cursor: 'aWQ6MTAw',
      pageSize: 10,
    });
    try {
      await client.listKanjianRecordsWithOptions(listKanjianRecordsRequest, listKanjianRecordsHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianRecordsHeaders listKanjianRecordsHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianRecordsHeaders();
            listKanjianRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianRecordsRequest listKanjianRecordsRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.ListKanjianRecordsRequest
            {
                OperatorUserId = "manager098",
                DeviceSn = "BV0000000001",
                StartTime = 1760000000000,
                EndTime = 1760086400000,
                MainTaskId = "task0001",
                Cursor = "aWQ6MTAw",
                PageSize = 10,
            };
            try
            {
                client.ListKanjianRecordsWithOptions(listKanjianRecordsRequest, listKanjianRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 业务结果。 |
| hasMore | Boolean | 是否有下一页：   - **true**：有 - **false**：没有 |
| items | Array | 看鉴记录列表。 |
| creatorName | String | 创建人姓名。 |
| deviceSn | String | 设备序列号。 |
| duration | Long | 时长，毫秒。 |
| endTime | Long | 录制结束时间，毫秒时间戳。 |
| gmtCreate | Long | 创建时间，毫秒时间戳。 |
| mainTaskId | String | 关联主任务 ID。 |
| mainTaskTitle | String | 关联主任务标题。 |
| mediaUrl | String | 视频临时签名 URL。 |
| recordId | String | 记录 ID。 |
| source | String | dingtalk\_bv BV 设备录制（开放接口只返回该来源）。 |
| startTime | Long | 录制开始时间，毫秒时间戳。 |
| status | String | 记录状态：   - **uploading**：上传中 - **uploaded**：已上传 - **pendingAnalysis**：待分析 - **analyzed**：已分析 - **aiSummaried**：已总结 |
| thumbnailUrl | String | 封面临时签名 URL。 |
| title | String | 记录标题。 |
| uploadProgress | Long | 上传进度百分比。 |
| nextCursor | String | 下一页游标，没有下一页时为空。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "hasMore" : true,
    "items" : [ {
      "creatorName" : "zhangsan",
      "deviceSn" : "BV0000000001",
      "duration" : 600000,
      "endTime" : 1760000600000,
      "gmtCreate" : 1760000000000,
      "mainTaskId" : "task0001",
      "mainTaskTitle" : "daily-check",
      "mediaUrl" : "https://example.com/media.mp4",
      "recordId" : "record0001",
      "source" : "dingtalk_bv",
      "startTime" : 1760000000000,
      "status" : "aiSummaried",
      "thumbnailUrl" : "https://example.com/thumb.jpg",
      "title" : "store-check",
      "uploadProgress" : 100
    } ],
    "nextCursor" : "aWQ6MTAw"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | pageSize 为 1 到 50，不传默认 10；cursor 不传为首页，传入须为上次返回的游标 | pageSize 为 1 到 50，不传默认 10；cursor 不传为首页，传入须为上次返回的游标 |
| 400 | emp.notExist | 操作人不是本企业员工，请检查 operatorUserId | 操作人不是本企业员工，请检查 operatorUserId |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
