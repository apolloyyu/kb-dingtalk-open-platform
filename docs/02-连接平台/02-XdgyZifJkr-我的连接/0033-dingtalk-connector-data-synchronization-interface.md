---
title: "发送连接器事件"
source_url: "https://open.dingtalk.com/document/connection/dingtalk-connector-data-synchronization-interface"
namespace: "connection"
slug: "dingtalk-connector-data-synchronization-interface"
group: "连接平台"
tab: "我的连接"
breadcrumb: "开发参考 > API参考 > 发送连接器事件"
doc_id: "dmlr4goNnM"
updated_at: "2026-06-15 11:25:36"
---

> Source: https://open.dingtalk.com/document/connection/dingtalk-connector-data-synchronization-interface
> Path: 连接平台 / 我的连接 / 开发参考 > API参考 > 发送连接器事件
> Updated: 2026-06-15 11:25:36

# 发送连接器事件

调用本接口通过推拉结合的方式将数据同步到连接器服务中，钉钉会将这些事件再广播转发给订阅了此事件的其它业务系统。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/connector/triggers/data/sync |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_base-调用企业API时需要具备的基本权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| triggerDataList | Array | 是 | 支持批量同步数据。 |
| triggerId | String | 是 | 钉钉连接器触发器ID。 |
| customTriggerId | String | 否 | 开发者自定义触发器ID。 |
| jsonData | String | 是 | 符合数据模型标准的json格式的数据。 |
| dataGmtCreate | Long | 是 | 数据创建时间。 |
| dataGmtModified | Long | 是 | 数据最后被修改的时间。 |
| action | String | 是 | 本次操作的行为，取值：   - **add**：增加 - **delete**：删除 - **update**：更新 |
| integrationObject | String | 否 | 集成元素的唯一标识。 |
| triggerCondition | String | 否 | 触发条件。       - 同一个触发器下，过滤掉不符合条件的流。     示例如下：  如`{"flowIds":["G-FLOW-XXX"]}`，表示只触发flowId =G-FLOW-XXX 的流。 |
| appId | String | 否 | 同步数据的应用ID：       - 第三方企业应用传应用的appId， - 企业自建应用传应用agentId。 |

### 请求示例

HTTP

```
POST /v1.0/connector/triggers/data/sync HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "triggerDataList" : [ {
    "triggerId" : "TRIGGER-XXXX",
    "customTriggerId" : "ABC",
    "jsonData" : "{\"a\":\"aa\",\"b\":\"bb\"}",
    "dataGmtCreate" : 1621482274000,
    "dataGmtModified" : 1621482274000,
    "action" : "add",
    "integrationObject" : "11",
    "triggerCondition" : "{\"flowIds\":[\"G-FLOW-XXX\"]}"
  } ],
  "appId" : "123"
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
    public static com.aliyun.dingtalkconnector_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconnector_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkconnector_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconnector_1_0.models.SyncDataHeaders syncDataHeaders = new com.aliyun.dingtalkconnector_1_0.models.SyncDataHeaders();
        syncDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconnector_1_0.models.SyncDataRequest.SyncDataRequestTriggerDataList triggerDataList0 = new com.aliyun.dingtalkconnector_1_0.models.SyncDataRequest.SyncDataRequestTriggerDataList()
                .setTriggerId("TRIGGER-XXXX")
                .setCustomTriggerId("ABC")
                .setJsonData("{\"a\":\"aa\",\"b\":\"bb\"}")
                .setDataGmtCreate(1621482274000L)
                .setDataGmtModified(1621482274000L)
                .setAction("add")
                .setIntegrationObject("11")
                .setTriggerCondition("{\"flowIds\":[\"G-FLOW-XXX\"]}");
        com.aliyun.dingtalkconnector_1_0.models.SyncDataRequest syncDataRequest = new com.aliyun.dingtalkconnector_1_0.models.SyncDataRequest()
                .setTriggerDataList(java.util.Arrays.asList(
                    triggerDataList0
                ))
                .setAppId("123");
        try {
            client.syncDataWithOptions(syncDataRequest, syncDataHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.connector_1_0.client import Client as dingtalkconnector_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.connector_1_0 import models as dingtalkconnector__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconnector_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconnector_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sync_data_headers = dingtalkconnector__1__0_models.SyncDataHeaders()
        sync_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        trigger_data_list_0 = dingtalkconnector__1__0_models.SyncDataRequestTriggerDataList(
            trigger_id='TRIGGER-XXXX',
            custom_trigger_id='ABC',
            json_data='{"a":"aa","b":"bb"}',
            data_gmt_create=1621482274000,
            data_gmt_modified=1621482274000,
            action='add',
            integration_object='11',
            trigger_condition='{"flowIds":["G-FLOW-XXX"]}'
        )
        sync_data_request = dingtalkconnector__1__0_models.SyncDataRequest(
            trigger_data_list=[
                trigger_data_list_0
            ],
            app_id='123'
        )
        try:
            client.sync_data_with_options(sync_data_request, sync_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sync_data_headers = dingtalkconnector__1__0_models.SyncDataHeaders()
        sync_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        trigger_data_list_0 = dingtalkconnector__1__0_models.SyncDataRequestTriggerDataList(
            trigger_id='TRIGGER-XXXX',
            custom_trigger_id='ABC',
            json_data='{"a":"aa","b":"bb"}',
            data_gmt_create=1621482274000,
            data_gmt_modified=1621482274000,
            action='add',
            integration_object='11',
            trigger_condition='{"flowIds":["G-FLOW-XXX"]}'
        )
        sync_data_request = dingtalkconnector__1__0_models.SyncDataRequest(
            trigger_data_list=[
                trigger_data_list_0
            ],
            app_id='123'
        )
        try:
            await client.sync_data_with_options_async(sync_data_request, sync_data_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconnector_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconnector_1_0\Models\SyncDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconnector_1_0\Models\SyncDataRequest\triggerDataList;
use AlibabaCloud\SDK\Dingtalk\Vconnector_1_0\Models\SyncDataRequest;
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
        $syncDataHeaders = new SyncDataHeaders([]);
        $syncDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $triggerDataList0 = new triggerDataList([
            "triggerId" => "TRIGGER-XXXX",
            "customTriggerId" => "ABC",
            "jsonData" => "{\"a\":\"aa\",\"b\":\"bb\"}",
            "dataGmtCreate" => 1621482274000,
            "dataGmtModified" => 1621482274000,
            "action" => "add",
            "integrationObject" => "11",
            "triggerCondition" => "{\"flowIds\":[\"G-FLOW-XXX\"]}"
        ]);
        $syncDataRequest = new SyncDataRequest([
            "triggerDataList" => [
                $triggerDataList0
            ],
            "appId" => "123"
        ]);
        try {
            $client->syncDataWithOptions($syncDataRequest, $syncDataHeaders, new RuntimeOptions([]));
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
  dingtalkconnector_1_0  "github.com/alibabacloud-go/dingtalk/connector_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkconnector_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconnector_1_0.Client{}
  _result, _err = dingtalkconnector_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  syncDataHeaders := &dingtalkconnector_1_0.SyncDataHeaders{}
  syncDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  triggerDataList0 := &dingtalkconnector_1_0.SyncDataRequestTriggerDataList{
    TriggerId: tea.String("TRIGGER-XXXX"),
    CustomTriggerId: tea.String("ABC"),
    JsonData: tea.String("{\"a\":\"aa\",\"b\":\"bb\"}"),
    DataGmtCreate: tea.Int64(1621482274000),
    DataGmtModified: tea.Int64(1621482274000),
    Action: tea.String("add"),
    IntegrationObject: tea.String("11"),
    TriggerCondition: tea.String("{\"flowIds\":[\"G-FLOW-XXX\"]}"),
  }
  syncDataRequest := &dingtalkconnector_1_0.SyncDataRequest{
    TriggerDataList: []*dingtalkconnector_1_0.SyncDataRequestTriggerDataList{triggerDataList0},
    AppId: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SyncDataWithOptions(syncDataRequest, syncDataHeaders, &util.RuntimeOptions{})
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
import dingtalkconnector_1_0, * as $dingtalkconnector_1_0 from '@alicloud/dingtalk/connector_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkconnector_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkconnector_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let syncDataHeaders = new $dingtalkconnector_1_0.SyncDataHeaders({ });
    syncDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let triggerDataList0 = new $dingtalkconnector_1_0.SyncDataRequestTriggerDataList({
      triggerId: "TRIGGER-XXXX",
      customTriggerId: "ABC",
      jsonData: "{\"a\":\"aa\",\"b\":\"bb\"}",
      dataGmtCreate: 1621482274000,
      dataGmtModified: 1621482274000,
      action: "add",
      integrationObject: "11",
      triggerCondition: "{\"flowIds\":[\"G-FLOW-XXX\"]}",
    });
    let syncDataRequest = new $dingtalkconnector_1_0.SyncDataRequest({
      triggerDataList: [
        triggerDataList0
      ],
      appId: "123",
    });
    try {
      await client.syncDataWithOptions(syncDataRequest, syncDataHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkconnector_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconnector_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconnector_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataHeaders syncDataHeaders = new AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataHeaders();
            syncDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataRequest.SyncDataRequestTriggerDataList triggerDataList0 = new AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataRequest.SyncDataRequestTriggerDataList
            {
                TriggerId = "TRIGGER-XXXX",
                CustomTriggerId = "ABC",
                JsonData = "{\"a\":\"aa\",\"b\":\"bb\"}",
                DataGmtCreate = 1621482274000,
                DataGmtModified = 1621482274000,
                Action = "add",
                IntegrationObject = "11",
                TriggerCondition = "{\"flowIds\":[\"G-FLOW-XXX\"]}",
            };
            AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataRequest syncDataRequest = new AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataRequest
            {
                TriggerDataList = new List<AlibabaCloud.SDK.Dingtalkconnector_1_0.Models.SyncDataRequest.SyncDataRequestTriggerDataList>
                {
                    triggerDataList0
                },
                AppId = "123",
            };
            try
            {
                client.SyncDataWithOptions(syncDataRequest, syncDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| list | Array | 返回结果。 |
| triggerId | String | 钉钉连接器触发器ID。 |
| bizPrimaryKey | String | 数据模型中的业务主键字段值。 |
| success | Boolean | 本条数据是否同步成功。 |
| subErrCode | String | 本条数据执行同步的错误码。 |
| subErrMsg | String | 本条数据执行同步的错误描述。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "list" : [ {
    "triggerId" : "TRIGGER-XXXX",
    "bizPrimaryKey" : "product_code",
    "success" : true,
    "subErrCode" : "\"\"",
    "subErrMsg" : "\"\""
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](../../01-应用开发/02-4a8AMF6u2A-服务端-API/0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | moreThanMaxListSize | Exceeded the maximum number limit | 超出最大个数限制 |
| 400 | invalidTriggerId | Invalid triggerId | 无效的触发器ID |
| 400 | invalid.data.action | Invalid data action | 无效的数据操作行为，只支持add、update和delete。 |
| 400 | jsonData.empty | Invalid jsonData | 请求参数中的jsonData字段为空。 |
| 400 | invalid.appid | Invalid appId | 入参需要提供应用id字段，且应用id需要和当前token相匹配。 |
