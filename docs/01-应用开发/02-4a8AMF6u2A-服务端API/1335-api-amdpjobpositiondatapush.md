---
title: "组织变革主数据人员任职数据推送"
source_url: "https://open.dingtalk.com/document/development/api-amdpjobpositiondatapush"
namespace: "development"
slug: "api-amdpjobpositiondatapush"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > HCM 主数据 > 组织变革主数据人员任职数据推送"
doc_id: "0G67F4z2qJ"
updated_at: "2025-09-23 19:23:41"
---

> Source: https://open.dingtalk.com/document/development/api-amdpjobpositiondatapush
> Path: 应用开发 / 服务端API / 更多开放 > HCM 主数据 > 组织变革主数据人员任职数据推送
> Updated: 2025-09-23 19:23:41

# 组织变革主数据人员任职数据推送

使用组织变革产品的组织，可以通过该API将自己业务系统中的人员任职信息推送到组织变革主数据，从而在相关产品中使用自己的人员任职数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/amdp/empJobs/datas/push |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Okr.Common.ReadWrite-OKR基础数据读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| param | Array | 否 | 数据列表 KEY。 |
| userId | String | 否 | 用户 UserId。 |
| deptId | String | 否 | 部门 ID。 |
| deptLeader | String | 否 | 部门主管 ID。 |
| leaderDeptId | String | 否 | 主管部门 ID。 |
| orderNumber | String | 否 | 主兼岗标识。 |
| isDelete | String | 否 | 是否无效：   - y：是 - n：否 |

### 请求示例

HTTP

```
POST /v1.0/amdp/empJobs/datas/push HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:cecc960157703fdc8b047665c4aa83a2
Content-Type:application/json

{
  "param" : [ {
    "userId" : "123456",
    "deptId" : "123456",
    "deptLeader" : "234564",
    "leaderDeptId" : "138581",
    "orderNumber" : "0",
    "isDelete" : "y/n"
  } ]
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
    public static com.aliyun.dingtalkamdp_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkamdp_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkamdp_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkamdp_1_0.models.AmdpJobPositionDataPushHeaders amdpJobPositionDataPushHeaders = new com.aliyun.dingtalkamdp_1_0.models.AmdpJobPositionDataPushHeaders();
        amdpJobPositionDataPushHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkamdp_1_0.models.AmdpJobPositionDataPushRequest.AmdpJobPositionDataPushRequestParam param0 = new com.aliyun.dingtalkamdp_1_0.models.AmdpJobPositionDataPushRequest.AmdpJobPositionDataPushRequestParam()
                .setUserId("123456")
                .setDeptId("123456")
                .setDeptLeader("234564")
                .setLeaderDeptId("138581")
                .setOrderNumber("0")
                .setIsDelete("y/n");
        com.aliyun.dingtalkamdp_1_0.models.AmdpJobPositionDataPushRequest amdpJobPositionDataPushRequest = new com.aliyun.dingtalkamdp_1_0.models.AmdpJobPositionDataPushRequest()
                .setParam(java.util.Arrays.asList(
                    param0
                ));
        try {
            client.amdpJobPositionDataPushWithOptions(amdpJobPositionDataPushRequest, amdpJobPositionDataPushHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.amdp_1_0.client import Client as dingtalkamdp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.amdp_1_0 import models as dingtalkamdp__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkamdp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkamdp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        amdp_job_position_data_push_headers = dingtalkamdp__1__0_models.AmdpJobPositionDataPushHeaders()
        amdp_job_position_data_push_headers.x_acs_dingtalk_access_token = '<your access token>'
        param_0 = dingtalkamdp__1__0_models.AmdpJobPositionDataPushRequestParam(
            user_id='123456',
            dept_id='123456',
            dept_leader='234564',
            leader_dept_id='138581',
            order_number='0',
            is_delete='y/n'
        )
        amdp_job_position_data_push_request = dingtalkamdp__1__0_models.AmdpJobPositionDataPushRequest(
            param=[
                param_0
            ]
        )
        try:
            client.amdp_job_position_data_push_with_options(amdp_job_position_data_push_request, amdp_job_position_data_push_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        amdp_job_position_data_push_headers = dingtalkamdp__1__0_models.AmdpJobPositionDataPushHeaders()
        amdp_job_position_data_push_headers.x_acs_dingtalk_access_token = '<your access token>'
        param_0 = dingtalkamdp__1__0_models.AmdpJobPositionDataPushRequestParam(
            user_id='123456',
            dept_id='123456',
            dept_leader='234564',
            leader_dept_id='138581',
            order_number='0',
            is_delete='y/n'
        )
        amdp_job_position_data_push_request = dingtalkamdp__1__0_models.AmdpJobPositionDataPushRequest(
            param=[
                param_0
            ]
        )
        try:
            await client.amdp_job_position_data_push_with_options_async(amdp_job_position_data_push_request, amdp_job_position_data_push_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vamdp_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vamdp_1_0\Models\AmdpJobPositionDataPushHeaders;
use AlibabaCloud\SDK\Dingtalk\Vamdp_1_0\Models\AmdpJobPositionDataPushRequest\param;
use AlibabaCloud\SDK\Dingtalk\Vamdp_1_0\Models\AmdpJobPositionDataPushRequest;
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
        $amdpJobPositionDataPushHeaders = new AmdpJobPositionDataPushHeaders([]);
        $amdpJobPositionDataPushHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $param0 = new param([
            "userId" => "123456",
            "deptId" => "123456",
            "deptLeader" => "234564",
            "leaderDeptId" => "138581",
            "orderNumber" => "0",
            "isDelete" => "y/n"
        ]);
        $amdpJobPositionDataPushRequest = new AmdpJobPositionDataPushRequest([
            "param" => [
                $param0
            ]
        ]);
        try {
            $client->amdpJobPositionDataPushWithOptions($amdpJobPositionDataPushRequest, $amdpJobPositionDataPushHeaders, new RuntimeOptions([]));
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
  dingtalkamdp_1_0  "github.com/alibabacloud-go/dingtalk/amdp_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkamdp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkamdp_1_0.Client{}
  _result, _err = dingtalkamdp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  amdpJobPositionDataPushHeaders := &dingtalkamdp_1_0.AmdpJobPositionDataPushHeaders{}
  amdpJobPositionDataPushHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  param0 := &dingtalkamdp_1_0.AmdpJobPositionDataPushRequestParam{
    UserId: tea.String("123456"),
    DeptId: tea.String("123456"),
    DeptLeader: tea.String("234564"),
    LeaderDeptId: tea.String("138581"),
    OrderNumber: tea.String("0"),
    IsDelete: tea.String("y/n"),
  }
  amdpJobPositionDataPushRequest := &dingtalkamdp_1_0.AmdpJobPositionDataPushRequest{
    Param: []*dingtalkamdp_1_0.AmdpJobPositionDataPushRequestParam{param0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AmdpJobPositionDataPushWithOptions(amdpJobPositionDataPushRequest, amdpJobPositionDataPushHeaders, &util.RuntimeOptions{})
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
const dingtalkamdp_1_0 = require('@alicloud/dingtalk/amdp_1_0');
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
    return new dingtalkamdp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let amdpJobPositionDataPushHeaders = new dingtalkamdp_1_0.AmdpJobPositionDataPushHeaders({ });
    amdpJobPositionDataPushHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let param0 = new dingtalkamdp_1_0.AmdpJobPositionDataPushRequestParam({
      userId: '123456',
      deptId: '123456',
      deptLeader: '234564',
      leaderDeptId: '138581',
      orderNumber: '0',
      isDelete: 'y/n',
    });
    let amdpJobPositionDataPushRequest = new dingtalkamdp_1_0.AmdpJobPositionDataPushRequest({
      param: [
        param0
      ],
    });
    try {
      await client.amdpJobPositionDataPushWithOptions(amdpJobPositionDataPushRequest, amdpJobPositionDataPushHeaders, new Util.RuntimeOptions({ }));
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkamdp_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkamdp_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkamdp_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushHeaders amdpJobPositionDataPushHeaders = new AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushHeaders();
            amdpJobPositionDataPushHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushRequest.AmdpJobPositionDataPushRequestParam param0 = new AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushRequest.AmdpJobPositionDataPushRequestParam
            {
                UserId = "123456",
                DeptId = "123456",
                DeptLeader = "234564",
                LeaderDeptId = "138581",
                OrderNumber = "0",
                IsDelete = "y/n",
            };
            AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushRequest amdpJobPositionDataPushRequest = new AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushRequest
            {
                Param = new List<AlibabaCloud.SDK.Dingtalkamdp_1_0.Models.AmdpJobPositionDataPushRequest.AmdpJobPositionDataPushRequestParam>
                {
                    param0
                },
            };
            try
            {
                client.AmdpJobPositionDataPushWithOptions(amdpJobPositionDataPushRequest, amdpJobPositionDataPushHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求 ID。 |
| success | Boolean | 请求是否成功。 |
| status | String | 状态码。 |
| result | Boolean | 请求结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "cecc960157703fdc8b047665c4aa83a2",
  "success" : true,
  "status" : "200",
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 200 | tenant.not.found | Tenant not found. | 租户不存在 |
| 200 | integrationConfig.not.found | Data integration config not found. | 数据集成配置不存在 |
| 200 | sizeTooLarge | Data size tool large. | 数据量过大，单次限定50 |
