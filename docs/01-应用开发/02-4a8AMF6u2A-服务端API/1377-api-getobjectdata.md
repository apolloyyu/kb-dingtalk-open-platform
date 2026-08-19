---
title: "根据指定条件查询自定义对象数据"
source_url: "https://open.dingtalk.com/document/development/api-getobjectdata"
namespace: "development"
slug: "api-getobjectdata"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 自定义对象 > 根据指定条件查询自定义对象数据"
doc_id: "dboFui1oNp"
updated_at: "2025-10-09 18:06:19"
---

> Source: https://open.dingtalk.com/document/development/api-getobjectdata
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 自定义对象 > 根据指定条件查询自定义对象数据
> Updated: 2025-10-09 18:06:19

# 根据指定条件查询自定义对象数据

调用本接口，可根据指定条件查询自定义对象数据，包括创建记录的用户昵称、审批状态、审批结果等。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/customObjects/datas/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_customdata\_read-获取CRM自定义对象数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| currentOperatorUserId | String | 否 | 用户 userId。 |
| nextToken | String | 否 | 分页游标。 |
| maxResults | Long | 是 | 分页大小。  **[!NOTE]**  最多可一次获取200条数据。 |
| name | String | 是 | 表单 code。 |
| queryDsl | String | 否 | 查询条件。 |

### 请求示例

HTTP

```
POST /v1.0/crm/customObjects/datas/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dc73axxxx
Content-Type:application/json

{
  "currentOperatorUserId" : "ding_userid",
  "nextToken" : "0",
  "maxResults" : 100,
  "name" : "PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9",
  "queryDsl" : "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}"
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
        com.aliyun.dingtalkcrm_1_0.models.GetObjectDataHeaders getObjectDataHeaders = new com.aliyun.dingtalkcrm_1_0.models.GetObjectDataHeaders();
        getObjectDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.GetObjectDataRequest getObjectDataRequest = new com.aliyun.dingtalkcrm_1_0.models.GetObjectDataRequest()
                .setCurrentOperatorUserId("ding_userid")
                .setNextToken("0")
                .setMaxResults(100L)
                .setName("PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9")
                .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}");
        try {
            client.getObjectDataWithOptions(getObjectDataRequest, getObjectDataHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_object_data_headers = dingtalkcrm__1__0_models.GetObjectDataHeaders()
        get_object_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_object_data_request = dingtalkcrm__1__0_models.GetObjectDataRequest(
            current_operator_user_id='ding_userid',
            next_token='0',
            max_results=100,
            name='PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9',
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"fieldId":"contact_phone","value":"18000000000"},{"fieldId":"contact_related_customer","value":"INST-XXX"}]}]}'
        )
        try:
            client.get_object_data_with_options(get_object_data_request, get_object_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_object_data_headers = dingtalkcrm__1__0_models.GetObjectDataHeaders()
        get_object_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_object_data_request = dingtalkcrm__1__0_models.GetObjectDataRequest(
            current_operator_user_id='ding_userid',
            next_token='0',
            max_results=100,
            name='PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9',
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"fieldId":"contact_phone","value":"18000000000"},{"fieldId":"contact_related_customer","value":"INST-XXX"}]}]}'
        )
        try:
            await client.get_object_data_with_options_async(get_object_data_request, get_object_data_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetObjectDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetObjectDataRequest;
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
        $getObjectDataHeaders = new GetObjectDataHeaders([]);
        $getObjectDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getObjectDataRequest = new GetObjectDataRequest([
            "currentOperatorUserId" => "ding_userid",
            "nextToken" => "0",
            "maxResults" => 100,
            "name" => "PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9",
            "queryDsl" => "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}"
        ]);
        try {
            $client->getObjectDataWithOptions($getObjectDataRequest, $getObjectDataHeaders, new RuntimeOptions([]));
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

  getObjectDataHeaders := &dingtalkcrm_1_0.GetObjectDataHeaders{}
  getObjectDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getObjectDataRequest := &dingtalkcrm_1_0.GetObjectDataRequest{
    CurrentOperatorUserId: tea.String("ding_userid"),
    NextToken: tea.String("0"),
    MaxResults: tea.Int64(100),
    Name: tea.String("PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9"),
    QueryDsl: tea.String("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetObjectDataWithOptions(getObjectDataRequest, getObjectDataHeaders, &util.RuntimeOptions{})
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
    let getObjectDataHeaders = new $dingtalkcrm_1_0.GetObjectDataHeaders({ });
    getObjectDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getObjectDataRequest = new $dingtalkcrm_1_0.GetObjectDataRequest({
      currentOperatorUserId: "ding_userid",
      nextToken: "0",
      maxResults: 100,
      name: "PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9",
      queryDsl: "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}",
    });
    try {
      await client.getObjectDataWithOptions(getObjectDataRequest, getObjectDataHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetObjectDataHeaders getObjectDataHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetObjectDataHeaders();
            getObjectDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetObjectDataRequest getObjectDataRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetObjectDataRequest
            {
                CurrentOperatorUserId = "ding_userid",
                NextToken = "0",
                MaxResults = 100,
                Name = "PROC-EF199CCA-8AB6-482A-AE10-85EDE5E391D9",
                QueryDsl = "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"fieldId\":\"contact_phone\",\"value\":\"18000000000\"},{\"fieldId\":\"contact_related_customer\",\"value\":\"INST-XXX\"}]}]}",
            };
            try
            {
                client.GetObjectDataWithOptions(getObjectDataRequest, getObjectDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 分页结果。 |
| nextToken | String | 下一页的游标。 |
| hasMore | Boolean | 是否有下一页：   - true：有 - false：没有 |
| maxResults | Long | 分页大小。 |
| values | Array | 数据列表。 |
| creatorNick | String | 创建记录的用户昵称。 |
| gmtModified | String | 记录修改时间。 |
| creatorUserId | String | 创建记录的用户 userId。 |
| instanceId | String | 数据 ID。 |
| data | Map<String, String> | 数据内容。 |
| extendData | Map<String, String> | 扩展数据内容。 |
| gmtCreate | String | 记录创建时间。 |
| objectType | String | 数据类型。 |
| permission | Object | 数据权限信息。 |
| participantUserIds | Array of String | 协同人用户 userId。 |
| ownerUserIds | Array of String | 负责人用户 userId。 |
| procInstStatus | String | 审批状态。 |
| procOutResult | String | 审批结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "nextToken" : "0",
    "hasMore" : true,
    "maxResults" : 100,
    "values" : [ {
      "creatorNick" : "张xx",
      "gmtModified" : "2023-12-25 15:33:12",
      "creatorUserId" : "user01",
      "instanceId" : "INST_XX",
      "data" : {
        "key" : "value"
      },
      "extendData" : {
        "key" : "value"
      },
      "gmtCreate" : "2023-11-25 15:33:12",
      "objectType" : "crm_contact",
      "permission" : {
        "participantUserIds" : [ "user01" ],
        "ownerUserIds" : [ "user01" ]
      },
      "procInstStatus" : "COMPLETE",
      "procOutResult" : "agree"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | pageSize.exceeds | pageSize must not exceeds 100 | 每页不能超过100条数据 |
| 400 | queryDsl.json.error | queryDsl is not valid json | queryDsl格式不正确 |
| 400 | system.error | system.error | 系统错误 |
