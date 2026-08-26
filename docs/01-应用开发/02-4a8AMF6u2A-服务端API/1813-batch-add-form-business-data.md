---
title: "批量新增表单业务数据"
source_url: "https://open.dingtalk.com/document/development/batch-add-form-business-data"
namespace: "development"
slug: "batch-add-form-business-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 氚云 > 表单 > 批量新增表单业务数据"
doc_id: "Bxf7v96KUZ"
updated_at: "2025-09-08 19:06:22"
---

> Source: https://open.dingtalk.com/document/development/batch-add-form-business-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 氚云 > 表单 > 批量新增表单业务数据
> Updated: 2025-09-08 19:06:22

# 批量新增表单业务数据

调用本接口可批量新增表单的业务实例数据。

> **[!IMPORTANT]**
>
> 为了更进一步提升接口质量以及用户体验，我们对本接口文档做出如下调整：
>
> - 自 2024 年 8 月 1 日起，本接口文档将会被迁移至历史文档目录。
> - 氚云接口不再支持新应用接入，已接入应用可继续使用，后续若需要接入氚云接口，请使用[氚云开发者手册](https://help.h3yun.com/channels/899.html)。

![](https://img.alicdn.com/imgextra/i4/O1CN01k8zGTv1nCK3CPaFY1_!!6000000005053-2-tps-1080-662.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=h3yun_1.0%23BatchInsertBizObject) |
| 第三方企业应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=h3yun_1.0%23BatchInsertBizObject) |
| 第三方个人应用 | 暂不支持 | 氚云数据管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/h3yun/forms/instances/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "schemaCode" : "String",
  "opUserId" : "String",
  "bizObjectJsonArray" : [ "String" ],
  "isDraft" : Boolean
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| schemaCode | String | 是 | 表单编码。 |
| opUserId | String | 是 | 操作用户ID。 |
| bizObjectJsonArray | Array of String | 是 | 待新增的业对象json数组。JSON数组的key只可以调用[获取表单对象结构](https://open.dingtalk.com/document/orgapp/gets-the-form-object-structure)接口获取。  例如：   ``` {     "F0000010": "0000007",     "F0000011": "王五",     "F0000012": "D级客户",     "F0000013": 7000,     "D000183Fcd15f3a51e624bbc9945392d190b6aa8": [         {             "F0000014": "克里斯",             "F0000015": 15600000000,             "F0000016": "技术部",             "F0000017": "经理",             "F0000018": "男",             "F0000019": "lgbxunmi@dd.com",             "F0000020": true,             "F0000021": "这是备注"         }     ] } ``` |
| isDraft | Boolean | 是 | 是否是草稿，取值：   - **true**：草稿数据 - **false**：生效数据 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 状态码。 |
| message | String | 状态码描述。 |
| data | Object | 成功新增的业务对象ID数组。 |
| bizObjectIds | Array of String | 成功新增的业务对象ID数组。 |
| processIds | Array of String | 新增成功的流程实例ID列表。 |
| failedDatas | Array of String | 新增失败的数据列表。 |
| failedMessages | Array of String | 失败的提示信息列表。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/h3yun/forms/instances/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bef2c84xxx
Content-Type:application/json

{
  "schemaCode" : "D000183b42f92824b2d497fb4ddda0e6f2134d8",
  "opUserId" : "3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713",
  "bizObjectJsonArray" : [ "{ \t\"F0000010\": \"0000007\", \t\"F0000011\": \"王五\", \t\"F0000012\": \"D级客户\", \t\"F0000013\": 7000, \t\"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ \t\t{ \t\t\t\"F0000014\": \"克里斯\", \t\t\t\"F0000015\": 15600000000, \t\t\t\"F0000016\": \"技术部\", \t\t\t\"F0000017\": \"经理\", \t\t\t\"F0000018\": \"男\", \t\t\t\"F0000019\": \"lgbxunmi@dd.com\", \t\t\t\"F0000020\": true, \t\t\t\"F0000021\": \"这是备注\" \t\t} \t] }" ],
  "isDraft" : false
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkh3yun_1_0.*;
import com.aliyun.dingtalkh3yun_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkh3yun_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkh3yun_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkh3yun_1_0.Client client = Sample.createClient();
        BatchInsertBizObjectHeaders batchInsertBizObjectHeaders = new BatchInsertBizObjectHeaders();
        batchInsertBizObjectHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchInsertBizObjectRequest batchInsertBizObjectRequest = new BatchInsertBizObjectRequest()
                .setSchemaCode("D000183b42f92824b2d497fb4ddda0e6f2134d8")
                .setOpUserId("3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713")
                .setBizObjectJsonArray(java.util.Arrays.asList(
                    "{ 	\"F0000010\": \"0000007\", 	\"F0000011\": \"王五\", 	\"F0000012\": \"D级客户\", 	\"F0000013\": 7000, 	\"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ 		{ 			\"F0000014\": \"克里斯\", 			\"F0000015\": 15600000000, 			\"F0000016\": \"技术部\", 			\"F0000017\": \"经理\", 			\"F0000018\": \"男\", 			\"F0000019\": \"lgbxunmi@dd.com\", 			\"F0000020\": true, 			\"F0000021\": \"这是备注\" 		} 	] }"
                ))
                .setIsDraft(false);
        try {
            client.batchInsertBizObjectWithOptions(batchInsertBizObjectRequest, batchInsertBizObjectHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.h3yun_1_0.client import Client as dingtalkh3yun_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.h3yun_1_0 import models as dingtalkh_3yun__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkh3yun_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkh3yun_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_insert_biz_object_headers = dingtalkh_3yun__1__0_models.BatchInsertBizObjectHeaders()
        batch_insert_biz_object_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_insert_biz_object_request = dingtalkh_3yun__1__0_models.BatchInsertBizObjectRequest(
            schema_code='D000183b42f92824b2d497fb4ddda0e6f2134d8',
            op_user_id='3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713',
            biz_object_json_array=[
                '{ 	"F0000010": "0000007", 	"F0000011": "王五", 	"F0000012": "D级客户", 	"F0000013": 7000, 	"D000183Fcd15f3a51e624bbc9945392d190b6aa8": [ 		{ 			"F0000014": "克里斯", 			"F0000015": 15600000000, 			"F0000016": "技术部", 			"F0000017": "经理", 			"F0000018": "男", 			"F0000019": "lgbxunmi@dd.com", 			"F0000020": true, 			"F0000021": "这是备注" 		} 	] }'
            ],
            is_draft=False
        )
        try:
            client.batch_insert_biz_object_with_options(batch_insert_biz_object_request, batch_insert_biz_object_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_insert_biz_object_headers = dingtalkh_3yun__1__0_models.BatchInsertBizObjectHeaders()
        batch_insert_biz_object_headers.x_acs_dingtalk_access_token = '<your access token>'
        batch_insert_biz_object_request = dingtalkh_3yun__1__0_models.BatchInsertBizObjectRequest(
            schema_code='D000183b42f92824b2d497fb4ddda0e6f2134d8',
            op_user_id='3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713',
            biz_object_json_array=[
                '{ 	"F0000010": "0000007", 	"F0000011": "王五", 	"F0000012": "D级客户", 	"F0000013": 7000, 	"D000183Fcd15f3a51e624bbc9945392d190b6aa8": [ 		{ 			"F0000014": "克里斯", 			"F0000015": 15600000000, 			"F0000016": "技术部", 			"F0000017": "经理", 			"F0000018": "男", 			"F0000019": "lgbxunmi@dd.com", 			"F0000020": true, 			"F0000021": "这是备注" 		} 	] }'
            ],
            is_draft=False
        )
        try:
            await client.batch_insert_biz_object_with_options_async(batch_insert_biz_object_request, batch_insert_biz_object_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\BatchInsertBizObjectHeaders;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\BatchInsertBizObjectRequest;
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
        $batchInsertBizObjectHeaders = new BatchInsertBizObjectHeaders([]);
        $batchInsertBizObjectHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $batchInsertBizObjectRequest = new BatchInsertBizObjectRequest([
            "schemaCode" => "D000183b42f92824b2d497fb4ddda0e6f2134d8",
            "opUserId" => "3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713",
            "bizObjectJsonArray" => [
                "{ 	\"F0000010\": \"0000007\", 	\"F0000011\": \"王五\", 	\"F0000012\": \"D级客户\", 	\"F0000013\": 7000, 	\"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ 		{ 			\"F0000014\": \"克里斯\", 			\"F0000015\": 15600000000, 			\"F0000016\": \"技术部\", 			\"F0000017\": \"经理\", 			\"F0000018\": \"男\", 			\"F0000019\": \"lgbxunmi@dd.com\", 			\"F0000020\": true, 			\"F0000021\": \"这是备注\" 		} 	] }"
            ],
            "isDraft" => false
        ]);
        try {
            $client->batchInsertBizObjectWithOptions($batchInsertBizObjectRequest, $batchInsertBizObjectHeaders, new RuntimeOptions([]));
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
  dingtalkh3yun_1_0  "github.com/alibabacloud-go/dingtalk/h3yun_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkh3yun_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkh3yun_1_0.Client{}
  _result, _err = dingtalkh3yun_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchInsertBizObjectHeaders := &dingtalkh3yun_1_0.BatchInsertBizObjectHeaders{}
  batchInsertBizObjectHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  batchInsertBizObjectRequest := &dingtalkh3yun_1_0.BatchInsertBizObjectRequest{
    SchemaCode: tea.String("D000183b42f92824b2d497fb4ddda0e6f2134d8"),
    OpUserId: tea.String("3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713"),
    BizObjectJsonArray: []*string{tea.String("{ 	\"F0000010\": \"0000007\", 	\"F0000011\": \"王五\", 	\"F0000012\": \"D级客户\", 	\"F0000013\": 7000, 	\"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ 		{ 			\"F0000014\": \"克里斯\", 			\"F0000015\": 15600000000, 			\"F0000016\": \"技术部\", 			\"F0000017\": \"经理\", 			\"F0000018\": \"男\", 			\"F0000019\": \"lgbxunmi@dd.com\", 			\"F0000020\": true, 			\"F0000021\": \"这是备注\" 		} 	] }")},
    IsDraft: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchInsertBizObjectWithOptions(batchInsertBizObjectRequest, batchInsertBizObjectHeaders, &util.RuntimeOptions{})
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
import dingtalkh3yun_1_0, * as $dingtalkh3yun_1_0 from '@alicloud/dingtalk/h3yun_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkh3yun_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkh3yun_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let batchInsertBizObjectHeaders = new $dingtalkh3yun_1_0.BatchInsertBizObjectHeaders({ });
    batchInsertBizObjectHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let batchInsertBizObjectRequest = new $dingtalkh3yun_1_0.BatchInsertBizObjectRequest({
      schemaCode: "D000183b42f92824b2d497fb4ddda0e6f2134d8",
      opUserId: "3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713",
      bizObjectJsonArray: [
        "{ 	\"F0000010\": \"0000007\", 	\"F0000011\": \"王五\", 	\"F0000012\": \"D级客户\", 	\"F0000013\": 7000, 	\"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ 		{ 			\"F0000014\": \"克里斯\", 			\"F0000015\": 15600000000, 			\"F0000016\": \"技术部\", 			\"F0000017\": \"经理\", 			\"F0000018\": \"男\", 			\"F0000019\": \"lgbxunmi@dd.com\", 			\"F0000020\": true, 			\"F0000021\": \"这是备注\" 		} 	] }"
      ],
      isDraft: false,
    });
    try {
      await client.batchInsertBizObjectWithOptions(batchInsertBizObjectRequest, batchInsertBizObjectHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.BatchInsertBizObjectHeaders batchInsertBizObjectHeaders = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.BatchInsertBizObjectHeaders();
            batchInsertBizObjectHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.BatchInsertBizObjectRequest batchInsertBizObjectRequest = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.BatchInsertBizObjectRequest
            {
                SchemaCode = "D000183b42f92824b2d497fb4ddda0e6f2134d8",
                OpUserId = "3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713",
                BizObjectJsonArray = new List<string>
                {
                    "{ 	\"F0000010\": \"0000007\", 	\"F0000011\": \"王五\", 	\"F0000012\": \"D级客户\", 	\"F0000013\": 7000, 	\"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ 		{ 			\"F0000014\": \"克里斯\", 			\"F0000015\": 15600000000, 			\"F0000016\": \"技术部\", 			\"F0000017\": \"经理\", 			\"F0000018\": \"男\", 			\"F0000019\": \"lgbxunmi@dd.com\", 			\"F0000020\": true, 			\"F0000021\": \"这是备注\" 		} 	] }"
                },
                IsDraft = false,
            };
            try
            {
                client.BatchInsertBizObjectWithOptions(batchInsertBizObjectRequest, batchInsertBizObjectHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkh_3yun__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkh3yun_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkh3yun_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::Client> client = make_shared<Alibabacloud_Dingtalkh3yun_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::BatchInsertBizObjectHeaders> batchInsertBizObjectHeaders = make_shared<Alibabacloud_Dingtalkh3yun_1_0::BatchInsertBizObjectHeaders>();
  batchInsertBizObjectHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::BatchInsertBizObjectRequest> batchInsertBizObjectRequest = make_shared<Alibabacloud_Dingtalkh3yun_1_0::BatchInsertBizObjectRequest>(map<string, boost::any>({
    {"schemaCode", boost::any(string("D000183b42f92824b2d497fb4ddda0e6f2134d8"))},
    {"opUserId", boost::any(string("3d0ad4a4-d7d5-4196-9f2c-3ed246f2b713"))},
    {"bizObjectJsonArray", boost::any(vector<string>({
      "{ 	"F0000010": "0000007", 	"F0000011": "王五", 	"F0000012": "D级客户", 	"F0000013": 7000, 	"D000183Fcd15f3a51e624bbc9945392d190b6aa8": [ 		{ 			"F0000014": "克里斯", 			"F0000015": 15600000000, 			"F0000016": "技术部", 			"F0000017": "经理", 			"F0000018": "男", 			"F0000019": "lgbxunmi@dd.com", 			"F0000020": true, 			"F0000021": "这是备注" 		} 	] }"
    }))},
    {"isDraft", boost::any(false)}
  }));
  try {
    client->batchInsertBizObjectWithOptions(batchInsertBizObjectRequest, batchInsertBizObjectHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : "success",
  "message" : "OK",
  "data" : {
    "bizObjectIds" : [ "50599800-af82-487e-9386-0a7278cab69f" ],
    "processIds" : [ "3b5451bc-9fd3-4d0c-ba47-191f8bff95ab" ],
    "failedDatas" : [ "{ \"F0000010\": \"0000007\", \"F0000011\": \"王五12\", \"F0000012\": \"D1级客户\", \"F0000013\": 7000, \"D000183Fcd15f3a51e624bbc9945392d190b6aa8\": [ { \"F0000014\": \"里斯\", \"F0000015\": 156666365656, \"F0000016\": \"技术部\", \"F0000017\": \"经理1\", \"F0000018\": \"男\", \"F0000019\": \"lgbxunmi@dd.com\", \"F0000020\": true, \"F0000021\": \"无\" } ] }" ],
    "failedMessages" : [ "无效的json格式字符串参数" ]
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | dataNotExist.user.userNotExist | 操作用户不存在 | 操作用户不存在 |
| 400 | dataModified.form.batchCreateBizObjectFail | 批量创建流程或业务对象全部失败 | 批量创建流程或业务对象全部失败 |
| 500 | systemError | 系统异常 | 出现未知的系统错误 |
