---
title: "获取离职员工列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-list-of-employees-who-have-left"
namespace: "development"
slug: "obtain-the-list-of-employees-who-have-left"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 员工管理 > 获取离职员工列表"
doc_id: "kY0wgVqoE6"
updated_at: "2026-06-04 19:10:26"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-list-of-employees-who-have-left
> Path: 应用开发 / 服务端 API / 智能人事 > 员工管理 > 获取离职员工列表
> Updated: 2026-06-04 19:10:26

# 获取离职员工列表

调用本接口，查询企业离职员工userId列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/employees/dismissions |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | Long | 否 | 分页查询的游标。   - 如果是首次查询，该参数传0或者不传。 - 如果是非首次查询，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 每页条目数，默认值30，最大值50。 |

### 请求示例

HTTP

```
GET /v1.0/hrm/employees/dismissions?nextToken=0&maxResults=30 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.QueryDismissionStaffIdListHeaders queryDismissionStaffIdListHeaders = new com.aliyun.dingtalkhrm_1_0.models.QueryDismissionStaffIdListHeaders();
        queryDismissionStaffIdListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.QueryDismissionStaffIdListRequest queryDismissionStaffIdListRequest = new com.aliyun.dingtalkhrm_1_0.models.QueryDismissionStaffIdListRequest()
                .setNextToken(0L)
                .setMaxResults(30);
        try {
            client.queryDismissionStaffIdListWithOptions(queryDismissionStaffIdListRequest, queryDismissionStaffIdListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrm_1_0.client import Client as dingtalkhrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_dismission_staff_id_list_headers = dingtalkhrm__1__0_models.QueryDismissionStaffIdListHeaders()
        query_dismission_staff_id_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_dismission_staff_id_list_request = dingtalkhrm__1__0_models.QueryDismissionStaffIdListRequest(
            next_token=0,
            max_results=30
        )
        try:
            client.query_dismission_staff_id_list_with_options(query_dismission_staff_id_list_request, query_dismission_staff_id_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_dismission_staff_id_list_headers = dingtalkhrm__1__0_models.QueryDismissionStaffIdListHeaders()
        query_dismission_staff_id_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_dismission_staff_id_list_request = dingtalkhrm__1__0_models.QueryDismissionStaffIdListRequest(
            next_token=0,
            max_results=30
        )
        try:
            await client.query_dismission_staff_id_list_with_options_async(query_dismission_staff_id_list_request, query_dismission_staff_id_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryDismissionStaffIdListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryDismissionStaffIdListRequest;
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
        $queryDismissionStaffIdListHeaders = new QueryDismissionStaffIdListHeaders([]);
        $queryDismissionStaffIdListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryDismissionStaffIdListRequest = new QueryDismissionStaffIdListRequest([
            "nextToken" => 0,
            "maxResults" => 30
        ]);
        try {
            $client->queryDismissionStaffIdListWithOptions($queryDismissionStaffIdListRequest, $queryDismissionStaffIdListHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkhrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrm_1_0.Client{}
  _result, _err = dingtalkhrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryDismissionStaffIdListHeaders := &dingtalkhrm_1_0.QueryDismissionStaffIdListHeaders{}
  queryDismissionStaffIdListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryDismissionStaffIdListRequest := &dingtalkhrm_1_0.QueryDismissionStaffIdListRequest{
    NextToken: tea.Int64(0),
    MaxResults: tea.Int32(30),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryDismissionStaffIdListWithOptions(queryDismissionStaffIdListRequest, queryDismissionStaffIdListHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryDismissionStaffIdListHeaders = new $dingtalkhrm_1_0.QueryDismissionStaffIdListHeaders({ });
    queryDismissionStaffIdListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryDismissionStaffIdListRequest = new $dingtalkhrm_1_0.QueryDismissionStaffIdListRequest({
      nextToken: 0,
      maxResults: 30,
    });
    try {
      await client.queryDismissionStaffIdListWithOptions(queryDismissionStaffIdListRequest, queryDismissionStaffIdListHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryDismissionStaffIdListHeaders queryDismissionStaffIdListHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryDismissionStaffIdListHeaders();
            queryDismissionStaffIdListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryDismissionStaffIdListRequest queryDismissionStaffIdListRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryDismissionStaffIdListRequest
            {
                NextToken = 0,
                MaxResults = 30,
            };
            try
            {
                client.QueryDismissionStaffIdListWithOptions(queryDismissionStaffIdListRequest, queryDismissionStaffIdListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | Long | 分页游标。 |
| hasMore | Boolean | 是否还有更多数据， 以此为依据判断是否继续查询下一页。   - **true**：有 - **false**：没有 |
| userIdList | Array of String | 返回的离职人员userId列表。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : 0,
  "hasMore" : true,
  "userIdList" : [ "user001" ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 分页参数错误 |
| 500 | systemError | 系统异常 | 系统异常 |
