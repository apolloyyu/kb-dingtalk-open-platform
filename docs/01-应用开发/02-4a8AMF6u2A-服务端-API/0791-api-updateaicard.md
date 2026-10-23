---
title: "更新 AI 卡片"
source_url: "https://open.dingtalk.com/document/development/api-updateaicard"
namespace: "development"
slug: "api-updateaicard"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > AI 卡片 > 更新 AI 卡片"
doc_id: "3EhxX76bt2"
updated_at: "2026-10-23 15:53:02"
---

> Source: https://open.dingtalk.com/document/development/api-updateaicard
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > AI 卡片 > 更新 AI 卡片
> Updated: 2026-10-23 15:53:02

# 更新 AI 卡片

调用本接口，更新AI卡片。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/ai/instances/update |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-AICard.Instance.Write-互动卡片实例写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0033-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 待更新卡片在当前应用和企业范围内的业务标识。  **[!NOTE]**  非空，长度限制与普通卡片一致。 |
| outUpdateId | String | 是 | 本次业务更新的幂等标识，1–64 位字母、数字、下划线或连字符。  **[!NOTE]**  重试保持不变，与网关 `RequestId` 独立。 |
| flowStatus | String | 是 | 本次更新后的流状态，使用枚举名，不使用内部数字码。 |
| a2uiMessages | Array of String | 是 | A2UI JSON 字符串列表，最多 100 条，必填且不能为 null。  **[!NOTE]**   - 允许空列表仅更新状态或标注。 - 总计不超过 256 KiB（UTF-8）。 - 消息 version 为 v1.0，仅支持 `updateComponents` 和 `updateDataModel`。 |
| a2uiAnnotations | Array | 否 | 组件语义标注，最多 100 项且不能重复。  **[!NOTE]**  不传或空列表表示不新增标注，不表示清空已有标注。 |
| surfaceId | String | 是 | Surface 标识。 |
| componentId | String | 是 | 组件标识。 |
| type | String | 是 | 标注类型，目前仅 `artifact`。 |

### **请求示例**

HTTP

```
PUT /v1.0/card/ai/instances/update HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2f52ee3xxxxe9c5ce510
Content-Type:application/json

{
  "outTrackId" : "a2ui_order_001",
  "outUpdateId" : "update_001",
  "flowStatus" : "PROCESSING",
  "a2uiMessages" : [ "updateComponents" ],
  "a2uiAnnotations" : [ {
    "surfaceId" : "6522xxxx9784",
    "componentId" : "6522xxxx9784",
    "type" : "artifact"
  } ]
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
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.UpdateAICardHeaders updateAICardHeaders = new com.aliyun.dingtalkcard_1_0.models.UpdateAICardHeaders();
        updateAICardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.UpdateAICardRequest.UpdateAICardRequestA2uiAnnotations a2uiAnnotations0 = new com.aliyun.dingtalkcard_1_0.models.UpdateAICardRequest.UpdateAICardRequestA2uiAnnotations()
                .setSurfaceId("6522xxxx9784")
                .setComponentId("6522xxxx9784")
                .setType("artifact");
        com.aliyun.dingtalkcard_1_0.models.UpdateAICardRequest updateAICardRequest = new com.aliyun.dingtalkcard_1_0.models.UpdateAICardRequest()
                .setOutTrackId("a2ui_order_001")
                .setOutUpdateId("update_001")
                .setFlowStatus("PROCESSING")
                .setA2uiMessages(java.util.Arrays.asList(
                    "updateComponents"
                ))
                .setA2uiAnnotations(java.util.Arrays.asList(
                    a2uiAnnotations0
                ));
        try {
            client.updateAICardWithOptions(updateAICardRequest, updateAICardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_aicard_headers = dingtalkcard__1__0_models.UpdateAICardHeaders()
        update_aicard_headers.x_acs_dingtalk_access_token = '<your access token>'
        a_2ui_annotations_0 = dingtalkcard__1__0_models.UpdateAICardRequestA2uiAnnotations(
            surface_id='6522xxxx9784',
            component_id='6522xxxx9784',
            type='artifact'
        )
        update_aicard_request = dingtalkcard__1__0_models.UpdateAICardRequest(
            out_track_id='a2ui_order_001',
            out_update_id='update_001',
            flow_status='PROCESSING',
            a_2ui_messages=[
                'updateComponents'
            ],
            a_2ui_annotations=[
                a_2ui_annotations_0
            ]
        )
        try:
            client.update_aicard_with_options(update_aicard_request, update_aicard_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_aicard_headers = dingtalkcard__1__0_models.UpdateAICardHeaders()
        update_aicard_headers.x_acs_dingtalk_access_token = '<your access token>'
        a_2ui_annotations_0 = dingtalkcard__1__0_models.UpdateAICardRequestA2uiAnnotations(
            surface_id='6522xxxx9784',
            component_id='6522xxxx9784',
            type='artifact'
        )
        update_aicard_request = dingtalkcard__1__0_models.UpdateAICardRequest(
            out_track_id='a2ui_order_001',
            out_update_id='update_001',
            flow_status='PROCESSING',
            a_2ui_messages=[
                'updateComponents'
            ],
            a_2ui_annotations=[
                a_2ui_annotations_0
            ]
        )
        try:
            await client.update_aicard_with_options_async(update_aicard_request, update_aicard_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateAICardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateAICardRequest\a2uiAnnotations;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\UpdateAICardRequest;
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
        $updateAICardHeaders = new UpdateAICardHeaders([]);
        $updateAICardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $a2uiAnnotations0 = new a2uiAnnotations([
            "surfaceId" => "6522xxxx9784",
            "componentId" => "6522xxxx9784",
            "type" => "artifact"
        ]);
        $updateAICardRequest = new UpdateAICardRequest([
            "outTrackId" => "a2ui_order_001",
            "outUpdateId" => "update_001",
            "flowStatus" => "PROCESSING",
            "a2uiMessages" => [
                "updateComponents"
            ],
            "a2uiAnnotations" => [
                $a2uiAnnotations0
            ]
        ]);
        try {
            $client->updateAICardWithOptions($updateAICardRequest, $updateAICardHeaders, new RuntimeOptions([]));
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
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
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
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateAICardHeaders := &dingtalkcard_1_0.UpdateAICardHeaders{}
  updateAICardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  a2uiAnnotations0 := &dingtalkcard_1_0.UpdateAICardRequestA2uiAnnotations{
    SurfaceId: tea.String("6522xxxx9784"),
    ComponentId: tea.String("6522xxxx9784"),
    Type: tea.String("artifact"),
  }
  updateAICardRequest := &dingtalkcard_1_0.UpdateAICardRequest{
    OutTrackId: tea.String("a2ui_order_001"),
    OutUpdateId: tea.String("update_001"),
    FlowStatus: tea.String("PROCESSING"),
    A2uiMessages: []*string{tea.String("updateComponents")},
    A2uiAnnotations: []*dingtalkcard_1_0.UpdateAICardRequestA2uiAnnotations{a2uiAnnotations0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateAICardWithOptions(updateAICardRequest, updateAICardHeaders, &util.RuntimeOptions{})
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
const dingtalkcard_1_0 = require('@alicloud/dingtalk/card_1_0');
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
    return new dingtalkcard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateAICardHeaders = new dingtalkcard_1_0.UpdateAICardHeaders({ });
    updateAICardHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let a2uiAnnotations0 = new dingtalkcard_1_0.UpdateAICardRequestA2uiAnnotations({
      surfaceId: '6522xxxx9784',
      componentId: '6522xxxx9784',
      type: 'artifact',
    });
    let updateAICardRequest = new dingtalkcard_1_0.UpdateAICardRequest({
      outTrackId: 'a2ui_order_001',
      outUpdateId: 'update_001',
      flowStatus: 'PROCESSING',
      a2uiMessages: [
        'updateComponents'
      ],
      a2uiAnnotations: [
        a2uiAnnotations0
      ],
    });
    try {
      await client.updateAICardWithOptions(updateAICardRequest, updateAICardHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardHeaders updateAICardHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardHeaders();
            updateAICardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardRequest.UpdateAICardRequestA2uiAnnotations a2uiAnnotations0 = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardRequest.UpdateAICardRequestA2uiAnnotations
            {
                SurfaceId = "6522xxxx9784",
                ComponentId = "6522xxxx9784",
                Type = "artifact",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardRequest updateAICardRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardRequest
            {
                OutTrackId = "a2ui_order_001",
                OutUpdateId = "update_001",
                FlowStatus = "PROCESSING",
                A2uiMessages = new List<string>
                {
                    "updateComponents"
                },
                A2uiAnnotations = new List<AlibabaCloud.SDK.Dingtalkcard_1_0.Models.UpdateAICardRequest.UpdateAICardRequestA2uiAnnotations>
                {
                    a2uiAnnotations0
                },
            };
            try
            {
                client.UpdateAICardWithOptions(updateAICardRequest, updateAICardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否成功。 |
| result | Object | 返回结果。 |
| outTrackId | String | 业务卡片标识。 |
| outUpdateId | String | 本次已生效的业务更新标识。 |
| flowStatus | String | 本次更新生效后的流状态。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "outTrackId" : "a2ui_order_001",
    "outUpdateId" : "update_001",
    "flowStatus" : "FINISH"
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | param.empty | 入参为空 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识 outTrackId 为空 |
| 400 | param.tokenGrantTypeInvalid | param.tokenGrantTypeInvalid | 系统身份参数 tokenGrantType 为空或非法 |
| 400 | param.orgIdEmpty | param.orgIdEmpty | 系统身份参数 orgId 为空 |
| 400 | param.suiteKeyEmpty | param.suiteKeyEmpty | ISV 系统身份参数 suiteKey 为空 |
| 400 | param.invalid | param.invalid | A2UI 更新参数或消息内容不合法，具体原因见动态 errorMsg |
| 400 | param.cardNotExist | param.cardNotExist | A2UI 卡片不存在 |
| 400 | param.idempotencyConflict | param.idempotencyConflict | A2UI 幂等标识对应的请求内容冲突 |
| 403 | access.denied | access.denied | A2UI 卡片操作无权限 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.featureDisabled | system.featureDisabled | A2UI 功能暂未开启 |
| 500 | system.dependencyUnavailable | system.dependencyUnavailable | A2UI 下游依赖不可用 |
| 500 | system.resultUnknown | system.resultUnknown | A2UI 更新结果未知，请核实卡片更新结果后再决定是否重试 |
| 500 | system.operationInProgress | system.operationInProgress | A2UI 更新操作处理中 |
