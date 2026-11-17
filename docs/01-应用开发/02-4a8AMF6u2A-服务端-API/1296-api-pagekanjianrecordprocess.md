---
title: "分页拉取看鉴记录的过程记录结果"
source_url: "https://open.dingtalk.com/document/development/api-pagekanjianrecordprocess"
namespace: "development"
slug: "api-pagekanjianrecordprocess"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "视听智能服务 > BV 看鉴 > 看鉴记录 > 分页拉取看鉴记录的过程记录结果"
doc_id: "doc_d90378ed6e104d1c"
updated_at: "2026-11-17 17:35:14"
---

> Source: https://open.dingtalk.com/document/development/api-pagekanjianrecordprocess
> Path: 应用开发 / 服务端 API / 视听智能服务 > BV 看鉴 > 看鉴记录 > 分页拉取看鉴记录的过程记录结果
> Updated: 2026-11-17 17:35:14

# 分页拉取看鉴记录的过程记录结果

调用本接口，分页拉取看鉴 BV 记录的过程记录，返回段落和结构化事件。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/dvi/bv/kanjian/records/process |
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
| recordId | String | 是 | 记录 ID，可通过[分页查询看鉴记录列表](1293-api-listkanjianrecords.md)接口获取。 |
| cursor | String | 否 | 分页游标。 |
| pageSize | Long | 否 | 每页条数，默认值1，取值 1 到 2。 |

### **请求示例**

HTTP

```
GET /v1.0/dvi/bv/kanjian/records/process?recordId=record0001&cursor=o1&pageSize=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f0917xxxx18901d52
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
        com.aliyun.dingtalkdvi_1_0.models.PageKanjianRecordProcessHeaders pageKanjianRecordProcessHeaders = new com.aliyun.dingtalkdvi_1_0.models.PageKanjianRecordProcessHeaders();
        pageKanjianRecordProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdvi_1_0.models.PageKanjianRecordProcessRequest pageKanjianRecordProcessRequest = new com.aliyun.dingtalkdvi_1_0.models.PageKanjianRecordProcessRequest()
                .setRecordId("record0001")
                .setCursor("o1")
                .setPageSize(1L);
        try {
            client.pageKanjianRecordProcessWithOptions(pageKanjianRecordProcessRequest, pageKanjianRecordProcessHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        page_kanjian_record_process_headers = dingtalkdvi__1__0_models.PageKanjianRecordProcessHeaders()
        page_kanjian_record_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        page_kanjian_record_process_request = dingtalkdvi__1__0_models.PageKanjianRecordProcessRequest(
            record_id='record0001',
            cursor='o1',
            page_size=1
        )
        try:
            client.page_kanjian_record_process_with_options(page_kanjian_record_process_request, page_kanjian_record_process_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        page_kanjian_record_process_headers = dingtalkdvi__1__0_models.PageKanjianRecordProcessHeaders()
        page_kanjian_record_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        page_kanjian_record_process_request = dingtalkdvi__1__0_models.PageKanjianRecordProcessRequest(
            record_id='record0001',
            cursor='o1',
            page_size=1
        )
        try:
            await client.page_kanjian_record_process_with_options_async(page_kanjian_record_process_request, page_kanjian_record_process_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\PageKanjianRecordProcessHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdvi_1_0\Models\PageKanjianRecordProcessRequest;
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
        $pageKanjianRecordProcessHeaders = new PageKanjianRecordProcessHeaders([]);
        $pageKanjianRecordProcessHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $pageKanjianRecordProcessRequest = new PageKanjianRecordProcessRequest([
            "recordId" => "record0001",
            "cursor" => "o1",
            "pageSize" => 1
        ]);
        try {
            $client->pageKanjianRecordProcessWithOptions($pageKanjianRecordProcessRequest, $pageKanjianRecordProcessHeaders, new RuntimeOptions([]));
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

  pageKanjianRecordProcessHeaders := &dingtalkdvi_1_0.PageKanjianRecordProcessHeaders{}
  pageKanjianRecordProcessHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  pageKanjianRecordProcessRequest := &dingtalkdvi_1_0.PageKanjianRecordProcessRequest{
    RecordId: tea.String("record0001"),
    Cursor: tea.String("o1"),
    PageSize: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PageKanjianRecordProcessWithOptions(pageKanjianRecordProcessRequest, pageKanjianRecordProcessHeaders, &util.RuntimeOptions{})
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
    let pageKanjianRecordProcessHeaders = new dingtalkdvi_1_0.PageKanjianRecordProcessHeaders({ });
    pageKanjianRecordProcessHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let pageKanjianRecordProcessRequest = new dingtalkdvi_1_0.PageKanjianRecordProcessRequest({
      recordId: 'record0001',
      cursor: 'o1',
      pageSize: 1,
    });
    try {
      await client.pageKanjianRecordProcessWithOptions(pageKanjianRecordProcessRequest, pageKanjianRecordProcessHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.PageKanjianRecordProcessHeaders pageKanjianRecordProcessHeaders = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.PageKanjianRecordProcessHeaders();
            pageKanjianRecordProcessHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.PageKanjianRecordProcessRequest pageKanjianRecordProcessRequest = new AlibabaCloud.SDK.Dingtalkdvi_1_0.Models.PageKanjianRecordProcessRequest
            {
                RecordId = "record0001",
                Cursor = "o1",
                PageSize = 1,
            };
            try
            {
                client.PageKanjianRecordProcessWithOptions(pageKanjianRecordProcessRequest, pageKanjianRecordProcessHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| events | Array | 过程记录事件列表。 |
| attentionPriority | String | 关注优先级。 |
| chapterTitle | String | 章节标题。 |
| description | String | 段落描述。 |
| eventId | String | 事件 ID。 |
| images | Array | 证据图列表。 |
| timestamp | Long | 图片对应视频时间点，毫秒。 |
| url | String | 证据图临时签名 URL。 |
| keyFrameMs | Long | 关键帧时间点，相对视频起点毫秒。 |
| parentSegmentId | String | 所属段落 ID。 |
| subjectLabel | String | 主体标签。 |
| timestampEndMs | Long | 事件结束时间，相对视频起点毫秒。 |
| timestampStartMs | Long | 事件开始时间，相对视频起点毫秒。 |
| executionId | String | 本页内容对应的分析版本 ID。 |
| hasMore | Boolean | 是否还有下一页：   - **true**：是 - **false**：否 |
| nextCursor | String | 下一页游标，没有下一页时为空。 |
| recordId | String | 记录 ID。 |
| segments | Array | 过程记录段落列表。 |
| childEventIds | Array of String | 事件ID。 |
| description | String | 段落描述。 |
| segmentArea | String | 段落所在区域。 |
| segmentId | String | 段落 ID，与 `events[].parentSegmentId` 对应。 |
| timeIntervals | Array | 段落时间区间列表。 |
| endMs | Long | 区间结束，相对视频起点毫秒。 |
| startMs | Long | 区间开始，相对视频起点毫秒。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "events" : [ {
      "attentionPriority" : "normal",
      "chapterTitle" : "entrance",
      "description" : "shelf is tidy",
      "eventId" : "event0001",
      "images" : [ {
        "timestamp" : 12000,
        "url" : "https://example.com/frame.jpg"
      } ],
      "keyFrameMs" : 12000,
      "parentSegmentId" : "segment0001",
      "subjectLabel" : "shelf",
      "timestampEndMs" : 15000,
      "timestampStartMs" : 10000
    } ],
    "executionId" : "exec0001",
    "hasMore" : true,
    "nextCursor" : "o1",
    "recordId" : "record0001",
    "segments" : [ {
      "childEventIds" : [ "evt0001" ],
      "description" : "check the shelf",
      "segmentArea" : "shelf-area",
      "segmentId" : "seg0001",
      "timeIntervals" : [ {
        "endMs" : 60000,
        "startMs" : 0
      } ]
    } ]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数非法。pageSize 为 1 到 2，不传默认 1；cursor 不传为首页，传入须形如 o1 | 参数非法。pageSize 为 1 到 2，不传默认 1；cursor 不传为首页，传入须形如 o1 |
| 400 | param.empty | 参数为空。recordId 必填 | 参数为空。recordId 必填 |
| 400 | invalid.corpId | 企业标识无效 | 企业标识无效 |
| 400 | orgId.mismatch | 企业标识不一致 | 企业标识不一致 |
| 400 | record.notFound | 看鉴记录不存在或已删除 | 看鉴记录不存在或已删除 |
| 400 | no.permission | 无操作权限 | 无操作权限 |
