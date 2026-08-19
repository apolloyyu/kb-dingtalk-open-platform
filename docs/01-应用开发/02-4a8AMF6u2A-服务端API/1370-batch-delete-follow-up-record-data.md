---
title: "批量删除跟进记录数据"
source_url: "https://open.dingtalk.com/document/development/batch-delete-follow-up-record-data"
namespace: "development"
slug: "batch-delete-follow-up-record-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 跟进记录 > 批量删除跟进记录数据"
doc_id: "jflR2bg4pi"
updated_at: "2025-10-09 18:06:18"
---

> Source: https://open.dingtalk.com/document/development/batch-delete-follow-up-record-data
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 跟进记录 > 批量删除跟进记录数据
> Updated: 2025-10-09 18:06:18

# 批量删除跟进记录数据

调用本接口，从客户管理的跟进记录列表中删除一个或多个跟进记录。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/followRecords/batchRemove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_write-维护CRM主数据的接口写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorUserId | String | 是 | 操作人userId。 |
| instanceIds | Array of String | 是 | 跟进记录ID。   - 企业内部应用，调用接口获取。 - 第三方企业应用，调用接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/crm/followRecords/batchRemove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c364097xxx
Content-Type:application/json

{
  "operatorUserId" : "manager021a",
  "instanceIds" : [ "yU9TbER1TDazjPq1rRCzwg04841675924041" ]
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
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcrm_1_0.models.BatchRemoveFollowRecordsHeaders batchRemoveFollowRecordsHeaders = new com.aliyun.dingtalkcrm_1_0.models.BatchRemoveFollowRecordsHeaders();
        batchRemoveFollowRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.BatchRemoveFollowRecordsRequest batchRemoveFollowRecordsRequest = new com.aliyun.dingtalkcrm_1_0.models.BatchRemoveFollowRecordsRequest()
                .setOperatorUserId("manager021a")
                .setInstanceIds(java.util.Arrays.asList(
                    "yU9TbER1TDazjPq1rRCzwg04841675924041"
                ));
        try {
            client.batchRemoveFollowRecordsWithOptions(batchRemoveFollowRecordsRequest, batchRemoveFollowRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_remove_follow_records_headers = dingtalkcrm__1__0_models.BatchRemoveFollowRecordsHeaders()
        batch_remove_follow_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_remove_follow_records_request = dingtalkcrm__1__0_models.BatchRemoveFollowRecordsRequest(
            operator_user_id='manager021a',
            instance_ids=[
                'yU9TbER1TDazjPq1rRCzwg04841675924041'
            ]
        )
        try:
            client.batch_remove_follow_records_with_options(batch_remove_follow_records_request, batch_remove_follow_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_remove_follow_records_headers = dingtalkcrm__1__0_models.BatchRemoveFollowRecordsHeaders()
        batch_remove_follow_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_remove_follow_records_request = dingtalkcrm__1__0_models.BatchRemoveFollowRecordsRequest(
            operator_user_id='manager021a',
            instance_ids=[
                'yU9TbER1TDazjPq1rRCzwg04841675924041'
            ]
        )
        try:
            await client.batch_remove_follow_records_with_options_async(batch_remove_follow_records_request, batch_remove_follow_records_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchRemoveFollowRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchRemoveFollowRecordsRequest;
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
        $batchRemoveFollowRecordsHeaders = new BatchRemoveFollowRecordsHeaders([]);
        $batchRemoveFollowRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchRemoveFollowRecordsRequest = new BatchRemoveFollowRecordsRequest([
            "operatorUserId" => "manager021a",
            "instanceIds" => [
                "yU9TbER1TDazjPq1rRCzwg04841675924041"
            ]
        ]);
        try {
            $client->batchRemoveFollowRecordsWithOptions($batchRemoveFollowRecordsRequest, $batchRemoveFollowRecordsHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchRemoveFollowRecordsHeaders := &dingtalkcrm_1_0.BatchRemoveFollowRecordsHeaders{}
  batchRemoveFollowRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchRemoveFollowRecordsRequest := &dingtalkcrm_1_0.BatchRemoveFollowRecordsRequest{
    OperatorUserId: tea.String("manager021a"),
    InstanceIds: []*string{tea.String("yU9TbER1TDazjPq1rRCzwg04841675924041")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchRemoveFollowRecordsWithOptions(batchRemoveFollowRecordsRequest, batchRemoveFollowRecordsHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let batchRemoveFollowRecordsHeaders = new $dingtalkcrm_1_0.BatchRemoveFollowRecordsHeaders({ });
    batchRemoveFollowRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let batchRemoveFollowRecordsRequest = new $dingtalkcrm_1_0.BatchRemoveFollowRecordsRequest({
      operatorUserId: "manager021a",
      instanceIds: [
        "yU9TbER1TDazjPq1rRCzwg04841675924041"
      ],
    });
    try {
      await client.batchRemoveFollowRecordsWithOptions(batchRemoveFollowRecordsRequest, batchRemoveFollowRecordsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchRemoveFollowRecordsHeaders batchRemoveFollowRecordsHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchRemoveFollowRecordsHeaders();
            batchRemoveFollowRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchRemoveFollowRecordsRequest batchRemoveFollowRecordsRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchRemoveFollowRecordsRequest
            {
                OperatorUserId = "manager021a",
                InstanceIds = new List<string>
                {
                    "yU9TbER1TDazjPq1rRCzwg04841675924041"
                },
            };
            try
            {
                client.BatchRemoveFollowRecordsWithOptions(batchRemoveFollowRecordsRequest, batchRemoveFollowRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| results | Array | 批量删除结果列表，results返回结果和删除数据顺序是一致的，可以查看每条跟进记录数据分别对应的结果是否成功。      例如，调用本接口批量删除了两个跟进记录，第一个跟进记录删除失败；第二个跟进记录删除成功。返回的信息格式为 |
| success | Boolean | 删除是否成功，true表示成功。 |
| errorCode | String | 错误码。   - 如果删除失败，表示失败的错误码。 - 如果删除成功，该字段不返回。 |
| errorMsg | String | 错误信息。   - 如果删除失败，表示失败的错误原因。 - 如果删除成功，该字段不返回。 |
| instanceId | String | 删除成功的跟进记录instanceId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "results" : [ {
    "success" : true,
    "instanceId" : "yU9TbER1TDazjPq1rRCzwg04841675924041"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | no.permission | %s | 无权限 |
| 400 | operatorUserId.not.exist | operatorUserId not exist | 操作者不存在 |
| 400 | crmApp.not.installed | crm app is not installed | CRM应用未安装 |
| 400 | system.busy | system busy | 请求过于频繁 |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 500 | unknown.error | unknownError | 未知错误 |
