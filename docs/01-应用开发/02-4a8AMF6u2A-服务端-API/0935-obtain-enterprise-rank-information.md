---
title: "获取企业职级列表"
source_url: "https://open.dingtalk.com/document/development/obtain-enterprise-rank-information"
namespace: "development"
slug: "obtain-enterprise-rank-information"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 职位管理 > 获取企业职级列表"
doc_id: "vV4pq5NA3E"
updated_at: "2026-07-14 09:22:31"
---

> Source: https://open.dingtalk.com/document/development/obtain-enterprise-rank-information
> Path: 应用开发 / 服务端 API / 智能人事 > 职位管理 > 获取企业职级列表
> Updated: 2026-07-14 09:22:31

# 获取企业职级列表

调用本接口，分页查询企业的职级相关信息，包括职级ID、职级名称等信息。

## **接口调用说明**

调用本接口前，需要对智能人事产品进行升级。有以下两种升级方式，选择方式一或者方式二进行升级。

> **[!NOTE]**
>
> 选择方式二升级后，调用通讯录部分接口时会报错，详情请查看本文后续方式二说明。

**方式一**: 智能人事内的**岗位职级**字段，升级为选项类型。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1512993871/p1087124.png)

**方式二**: 智能人事升级**职位管理**功能。

> **[!NOTE]**
>
> 智能人事升级职位管理功能后，需注意以下：
>
> 调用通讯录[更新用户信息v1](1457-update-user-details.md)接口和[更新用户信息v2](0057-user-information-update.md)接口更新员工部门或者员工职位时，接口会出现报错。如果需要更新员工部门或者员工职位，请参考使用[智能人事员工调岗](0954-intelligent-personnel-staff-transfer.md)接口。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1512993871/p1087125.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/jobRanks |
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
| rankCategoryId | String | 否 | 职级序列ID。   - **首次查询**：需先调用本接口获取rankCategoryId。 - **非首次查询**：从首次查询中的信息中获取需要的rankCategoryId值。       该参数为非必填参数。 |
| rankCode | String | 否 | 职级编码。   - **首次查询**：需先调用本接口获取rankCode。 - **非首次查询**：从首次查询中的信息中获取需要的rankCode值。       该参数为非必填参数。 |
| rankName | String | 否 | 职级名称。   - **首次查询**：需先调用本接口获取rankName。 - **非首次查询**：从首次查询中的信息中获取需要的rankName值。       该参数为非必填参数。 |
| nextToken | Integer | 是 | 分页游标。   - 首次调用，该参数传0。 - 非首次调用，该参数传上次调用本接口返回的nextToken。 |
| maxResults | Integer | 是 | 每页最大条目数，最大值200。 |

### 请求示例

HTTP

```
GET /v1.0/hrm/jobRanks?rankCategoryId=168dbcf2292a45858297e116a0bd2113&rankCode=测试职级&rankName=测试职级&nextToken=0&maxResults=100 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:168dbcf22
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkhrm_1_0.*;
import com.aliyun.dingtalkhrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        QueryJobRanksHeaders queryJobRanksHeaders = new QueryJobRanksHeaders();
        queryJobRanksHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryJobRanksRequest queryJobRanksRequest = new QueryJobRanksRequest()
                .setRankCategoryId("168dbcf2292a45858297e116a0bd2113")
                .setRankCode("测试职级")
                .setRankName("测试职级")
                .setNextToken(0)
                .setMaxResults(100);
        try {
            client.queryJobRanksWithOptions(queryJobRanksRequest, queryJobRanksHeaders, new RuntimeOptions());
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
        query_job_ranks_headers = dingtalkhrm__1__0_models.QueryJobRanksHeaders()
        query_job_ranks_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_job_ranks_request = dingtalkhrm__1__0_models.QueryJobRanksRequest(
            rank_category_id='168dbcf2292a45858297e116a0bd2113',
            rank_code='测试职级',
            rank_name='测试职级',
            next_token=0,
            max_results=100
        )
        try:
            client.query_job_ranks_with_options(query_job_ranks_request, query_job_ranks_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_job_ranks_headers = dingtalkhrm__1__0_models.QueryJobRanksHeaders()
        query_job_ranks_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_job_ranks_request = dingtalkhrm__1__0_models.QueryJobRanksRequest(
            rank_category_id='168dbcf2292a45858297e116a0bd2113',
            rank_code='测试职级',
            rank_name='测试职级',
            next_token=0,
            max_results=100
        )
        try:
            await client.query_job_ranks_with_options_async(query_job_ranks_request, query_job_ranks_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryJobRanksHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryJobRanksRequest;
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
        $queryJobRanksHeaders = new QueryJobRanksHeaders([]);
        $queryJobRanksHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryJobRanksRequest = new QueryJobRanksRequest([
            "rankCategoryId" => "168dbcf2292a45858297e116a0bd2113",
            "rankCode" => "测试职级",
            "rankName" => "测试职级",
            "nextToken" => 0,
            "maxResults" => 100
        ]);
        try {
            $client->queryJobRanksWithOptions($queryJobRanksRequest, $queryJobRanksHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  queryJobRanksHeaders := &dingtalkhrm_1_0.QueryJobRanksHeaders{}
  queryJobRanksHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryJobRanksRequest := &dingtalkhrm_1_0.QueryJobRanksRequest{
    RankCategoryId: tea.String("168dbcf2292a45858297e116a0bd2113"),
    RankCode: tea.String("测试职级"),
    RankName: tea.String("测试职级"),
    NextToken: tea.Int32(0),
    MaxResults: tea.Int32(100),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryJobRanksWithOptions(queryJobRanksRequest, queryJobRanksHeaders, &util.RuntimeOptions{})
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
    let queryJobRanksHeaders = new $dingtalkhrm_1_0.QueryJobRanksHeaders({ });
    queryJobRanksHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryJobRanksRequest = new $dingtalkhrm_1_0.QueryJobRanksRequest({
      rankCategoryId: "168dbcf2292a45858297e116a0bd2113",
      rankCode: "测试职级",
      rankName: "测试职级",
      nextToken: 0,
      maxResults: 100,
    });
    try {
      await client.queryJobRanksWithOptions(queryJobRanksRequest, queryJobRanksHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobRanksHeaders queryJobRanksHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobRanksHeaders();
            queryJobRanksHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobRanksRequest queryJobRanksRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryJobRanksRequest
            {
                RankCategoryId = "168dbcf2292a45858297e116a0bd2113",
                RankCode = "测试职级",
                RankName = "测试职级",
                NextToken = 0,
                MaxResults = 100,
            };
            try
            {
                client.QueryJobRanksWithOptions(queryJobRanksRequest, queryJobRanksHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | Long | 分页游标。      如果该字段未返回，表示数据已经读取完毕。 |
| hasMore | Boolean | 是否有更多数据。   - **true**：是 - **false**：否 |
| list | Array | 职级信息列表。 |
| rankId | String | 职级ID。 |
| rankCategoryId | String | 职级序列ID。      只有使用方式二-升级职位管理，调用接口才可以获取该字段。 |
| rankCode | String | 职级编码。      只有使用方式二-升级职位管理，调用接口才可以获取该字段。 |
| rankName | String | 职级名称。 |
| minJobGrade | Integer | 最小等级。      只有使用方式二-升级职位管理，调用接口才可以获取该字段。 |
| maxJobGrade | Integer | 最大等级。      只有使用方式二-升级职位管理，调用接口才可以获取该字段。 |
| rankDescription | String | 职级描述。      只有使用方式二-升级职位管理，调用接口才可以获取该字段。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nextToken" : 0,
  "hasMore" : true,
  "list" : [ {
    "rankId" : "d27a2ba85c4943b9b4f7be6c21387f1c",
    "rankCategoryId" : "168dbcf2292a45858297e116a0bd2113",
    "rankCode" : "测试职级",
    "rankName" : "测试职级",
    "minJobGrade" : 1,
    "maxJobGrade" : 30,
    "rankDescription" : "职级描述"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 参数错误 |
| 500 | systemError | 系统异常 | 系统异常 |
