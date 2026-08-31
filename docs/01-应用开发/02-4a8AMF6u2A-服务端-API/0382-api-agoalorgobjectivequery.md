---
title: "查询组织目标详情"
source_url: "https://open.dingtalk.com/document/development/api-agoalorgobjectivequery"
namespace: "development"
slug: "api-agoalorgobjectivequery"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "Agoal > 目标与关键行动 > 查询组织目标详情"
doc_id: "DhndTvu0Hq"
updated_at: "2026-07-08 14:13:50"
---

> Source: https://open.dingtalk.com/document/development/api-agoalorgobjectivequery
> Path: 应用开发 / 服务端 API / Agoal > 目标与关键行动 > 查询组织目标详情
> Updated: 2026-07-08 14:13:50

# 查询组织目标详情

调用该接口通过组织目标Id，查询该目标详情信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/agoal/orgObjectives |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Agoal.OrgObjective.Read-Agoal组织目标读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| objectiveId | String | 是 | 组织目标 id。 |

### 请求示例

HTTP

```
GET /v1.0/agoal/orgObjectives?objectiveId=662e00xxxxbb HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:9801a354e3d03539baa83e5f275axxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkagoal_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkagoal_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkagoal_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkagoal_1_0.models.AgoalOrgObjectiveQueryHeaders agoalOrgObjectiveQueryHeaders = new com.aliyun.dingtalkagoal_1_0.models.AgoalOrgObjectiveQueryHeaders();
        agoalOrgObjectiveQueryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkagoal_1_0.models.AgoalOrgObjectiveQueryRequest agoalOrgObjectiveQueryRequest = new com.aliyun.dingtalkagoal_1_0.models.AgoalOrgObjectiveQueryRequest()
                .setObjectiveId("662e00xxxxbb");
        try {
            client.agoalOrgObjectiveQueryWithOptions(agoalOrgObjectiveQueryRequest, agoalOrgObjectiveQueryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.agoal_1_0.client import Client as dingtalkagoal_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.agoal_1_0 import models as dingtalkagoal__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkagoal_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkagoal_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        agoal_org_objective_query_headers = dingtalkagoal__1__0_models.AgoalOrgObjectiveQueryHeaders()
        agoal_org_objective_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_org_objective_query_request = dingtalkagoal__1__0_models.AgoalOrgObjectiveQueryRequest(
            objective_id='662e00xxxxbb'
        )
        try:
            client.agoal_org_objective_query_with_options(agoal_org_objective_query_request, agoal_org_objective_query_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        agoal_org_objective_query_headers = dingtalkagoal__1__0_models.AgoalOrgObjectiveQueryHeaders()
        agoal_org_objective_query_headers.x_acs_dingtalk_access_token = '<your access token>'
        agoal_org_objective_query_request = dingtalkagoal__1__0_models.AgoalOrgObjectiveQueryRequest(
            objective_id='662e00xxxxbb'
        )
        try:
            await client.agoal_org_objective_query_with_options_async(agoal_org_objective_query_request, agoal_org_objective_query_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalOrgObjectiveQueryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vagoal_1_0\Models\AgoalOrgObjectiveQueryRequest;
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
        $agoalOrgObjectiveQueryHeaders = new AgoalOrgObjectiveQueryHeaders([]);
        $agoalOrgObjectiveQueryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $agoalOrgObjectiveQueryRequest = new AgoalOrgObjectiveQueryRequest([
            "objectiveId" => "662e00xxxxbb"
        ]);
        try {
            $client->agoalOrgObjectiveQueryWithOptions($agoalOrgObjectiveQueryRequest, $agoalOrgObjectiveQueryHeaders, new RuntimeOptions([]));
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
  dingtalkagoal_1_0  "github.com/alibabacloud-go/dingtalk/agoal_1_0"
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
func CreateClient () (_result *dingtalkagoal_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkagoal_1_0.Client{}
  _result, _err = dingtalkagoal_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  agoalOrgObjectiveQueryHeaders := &dingtalkagoal_1_0.AgoalOrgObjectiveQueryHeaders{}
  agoalOrgObjectiveQueryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  agoalOrgObjectiveQueryRequest := &dingtalkagoal_1_0.AgoalOrgObjectiveQueryRequest{
    ObjectiveId: tea.String("662e00xxxxbb"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AgoalOrgObjectiveQueryWithOptions(agoalOrgObjectiveQueryRequest, agoalOrgObjectiveQueryHeaders, &util.RuntimeOptions{})
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
const dingtalkagoal_1_0 = require('@alicloud/dingtalk/agoal_1_0');
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
    return new dingtalkagoal_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let agoalOrgObjectiveQueryHeaders = new dingtalkagoal_1_0.AgoalOrgObjectiveQueryHeaders({ });
    agoalOrgObjectiveQueryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let agoalOrgObjectiveQueryRequest = new dingtalkagoal_1_0.AgoalOrgObjectiveQueryRequest({
      objectiveId: '662e00xxxxbb',
    });
    try {
      await client.agoalOrgObjectiveQueryWithOptions(agoalOrgObjectiveQueryRequest, agoalOrgObjectiveQueryHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkagoal_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkagoal_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgObjectiveQueryHeaders agoalOrgObjectiveQueryHeaders = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgObjectiveQueryHeaders();
            agoalOrgObjectiveQueryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgObjectiveQueryRequest agoalOrgObjectiveQueryRequest = new AlibabaCloud.SDK.Dingtalkagoal_1_0.Models.AgoalOrgObjectiveQueryRequest
            {
                ObjectiveId = "662e00xxxxbb",
            };
            try
            {
                client.AgoalOrgObjectiveQueryWithOptions(agoalOrgObjectiveQueryRequest, agoalOrgObjectiveQueryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求Id。 |
| success | Boolean | 请求是否成功。 |
| content | OpenAgoalOrgObjectiveDTO | 组织目标对象。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "E6F8BAA4-6C37-168D-858A-F2A83437755D",
  "success" : true,
  "content" : {
    "objectiveId" : "6444f5e9a4261c6e699dxxxx",
    "title" : "测试目标",
    "status" : "formalEffective",
    "executor" : {
      "userId" : "6444f5e9a4261c6e699dxxxx",
      "dingUserId" : "211042291978xxxx",
      "name" : "测试"
    },
    "team" : {
      "teamId" : "6444f5e9a4261c6e699dxxxx",
      "deptId" : "8535683xx",
      "name" : "测试部门"
    },
    "period" : {
      "periodId" : "6444f5e9a4261c6e699dxxxx",
      "name" : "2024年度",
      "startDate" : 1711900800000,
      "endDate" : 1743436799000,
      "periodType" : "season"
    },
    "upAlignObjects" : [ {
      "objectiveId" : "662e006fe4b0f579bbcxxxxx",
      "objectType" : "objective",
      "objectId" : "662e006fe4b0f579bbcxxxxx",
      "alignType" : "COOPERATION"
    } ],
    "downAlignObjects" : [ {
      "objectiveId" : "662e006fe4b0f579bbcxxxxx",
      "objectType" : "objective",
      "objectId" : "662e006fe4b0f579bbcxxxxx",
      "alignType" : "COOPERATION"
    } ],
    "fieldConfig" : [ {
      "fieldId" : "662e006fe4b0f579bbcxxxxx",
      "code" : "foo",
      "title" : "字段名",
      "alias" : "字段别名",
      "note" : "字段备注",
      "source" : "OPEN",
      "active" : true,
      "type" : "string",
      "entityType" : "OBJECTIVE"
    } ],
    "fieldValueMap" : {
      "name" : "xxx"
    },
    "dimension" : {
      "dimensionId" : "662e006fe4b0f579bbcxxxxx",
      "fieldConfig" : [ {
        "fieldId" : "662e006fe4b0f579bbcxxxxx",
        "code" : "foo",
        "title" : "字段名",
        "alias" : "字段别名",
        "note" : "字段备注",
        "source" : "OPEN",
        "active" : true,
        "type" : "string",
        "entityType" : "OBJECTIVE"
      } ],
      "fieldValueMap" : {
        "name" : "xxx"
      },
      "children" : [ {
        "dimensionId" : "662e006fe4b0f57ccbcxxxxx",
        "title" : "这是子维度标题",
        "weight" : 100
      } ],
      "title" : "这是维度标题",
      "weight" : 100
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | error.systemError | 系统异常 | 系统异常 |
| 500 | error.invalidObjectiveId | 无效的组织目标 id | 无效的组织目标 id |
