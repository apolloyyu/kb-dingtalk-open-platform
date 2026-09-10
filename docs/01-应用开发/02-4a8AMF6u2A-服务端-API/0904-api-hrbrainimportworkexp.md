---
title: "数据集成工作经历同步"
source_url: "https://open.dingtalk.com/document/development/api-hrbrainimportworkexp"
namespace: "development"
slug: "api-hrbrainimportworkexp"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "组织大脑 > 数据集成 > 经历与档案 > 数据集成工作经历同步"
doc_id: "diKaTfmh7S"
updated_at: "2026-06-04 19:10:11"
---

> Source: https://open.dingtalk.com/document/development/api-hrbrainimportworkexp
> Path: 应用开发 / 服务端 API / 组织大脑 > 数据集成 > 经历与档案 > 数据集成工作经历同步
> Updated: 2026-06-04 19:10:11

# 数据集成工作经历同步

调用本接口，工作经历同步至组织大脑，支持批量同步。

## 接口调用说明

为了确保你在使用接口时能够顺利进行数据交互，请务必检查对应数据模型是否设置枚举值的范围。这一操作需要在组织大脑[管理后台](https://hrbrain.dingtalk.com/hrbrain/management/data-integration/model-management/basic-modal/detail?modelCode=hrbrain_import_dimission&status=read&detailNav=%5B%22modelList%22%2C%22detail%22%5D)的数据集成 > 模型管理的对应数据模型中进行查看，如果未正确设置枚举值范围，调用接口时可能会遇到错误信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/workExperiences/import |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrbrain.Import.Write-组织大脑数据集成写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织编码。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 是 | 数据集。 |
| name | String | 是 | 姓名。 |
| workNo | String | 是 | 钉钉用户 UserId。 |
| companyName | String | 是 | 公司名称。 |
| startDate | String | 是 | 开始日期。 |
| endDate | String | 是 | 结束日期。 |
| postName | String | 否 | 职位。 |
| jobDesc | String | 否 | 职位说明。 |
| extendInfo | Map | 否 | 扩展字段，KV结构。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/workExperiences/import?corpId=ding3b*********88 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:480021443f9f37fcbf464c4a6b85d299
Content-Type:application/json

[ {
  "name" : "张三",
  "workNo" : "14530201131175645",
  "companyName" : "阿里巴巴",
  "startDate" : "2024-01-01",
  "endDate" : "2024-04-01",
  "postName" : "开发工程师",
  "jobDesc" : "服务端开发"
} ]
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
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportWorkExpHeaders hrbrainImportWorkExpHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportWorkExpHeaders();
        hrbrainImportWorkExpHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportWorkExpRequest.HrbrainImportWorkExpRequestBody body0 = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportWorkExpRequest.HrbrainImportWorkExpRequestBody()
                .setName("张三")
                .setWorkNo("14530201131175645")
                .setCompanyName("阿里巴巴")
                .setStartDate("2024-01-01")
                .setEndDate("2024-04-01")
                .setPostName("开发工程师")
                .setJobDesc("服务端开发");
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportWorkExpRequest hrbrainImportWorkExpRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportWorkExpRequest()
                .setCorpId("ding3b*********88")
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.hrbrainImportWorkExpWithOptions(hrbrainImportWorkExpRequest, hrbrainImportWorkExpHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrbrain_1_0.client import Client as dingtalkhrbrain_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrbrain_1_0 import models as dingtalkhrbrain__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrbrain_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrbrain_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_work_exp_headers = dingtalkhrbrain__1__0_models.HrbrainImportWorkExpHeaders()
        hrbrain_import_work_exp_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportWorkExpRequestBody(
            name='张三',
            work_no='14530201131175645',
            company_name='阿里巴巴',
            start_date='2024-01-01',
            end_date='2024-04-01',
            post_name='开发工程师',
            job_desc='服务端开发'
        )
        hrbrain_import_work_exp_request = dingtalkhrbrain__1__0_models.HrbrainImportWorkExpRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            client.hrbrain_import_work_exp_with_options(hrbrain_import_work_exp_request, hrbrain_import_work_exp_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_work_exp_headers = dingtalkhrbrain__1__0_models.HrbrainImportWorkExpHeaders()
        hrbrain_import_work_exp_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportWorkExpRequestBody(
            name='张三',
            work_no='14530201131175645',
            company_name='阿里巴巴',
            start_date='2024-01-01',
            end_date='2024-04-01',
            post_name='开发工程师',
            job_desc='服务端开发'
        )
        hrbrain_import_work_exp_request = dingtalkhrbrain__1__0_models.HrbrainImportWorkExpRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            await client.hrbrain_import_work_exp_with_options_async(hrbrain_import_work_exp_request, hrbrain_import_work_exp_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportWorkExpHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportWorkExpRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportWorkExpRequest;
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
        $hrbrainImportWorkExpHeaders = new HrbrainImportWorkExpHeaders([]);
        $hrbrainImportWorkExpHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "name" => "张三",
            "workNo" => "14530201131175645",
            "companyName" => "阿里巴巴",
            "startDate" => "2024-01-01",
            "endDate" => "2024-04-01",
            "postName" => "开发工程师",
            "jobDesc" => "服务端开发"
        ]);
        $hrbrainImportWorkExpRequest = new HrbrainImportWorkExpRequest([
            "corpId" => "ding3b*********88",
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->hrbrainImportWorkExpWithOptions($hrbrainImportWorkExpRequest, $hrbrainImportWorkExpHeaders, new RuntimeOptions([]));
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
  dingtalkhrbrain_1_0  "github.com/alibabacloud-go/dingtalk/hrbrain_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkhrbrain_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrbrain_1_0.Client{}
  _result, _err = dingtalkhrbrain_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrbrainImportWorkExpHeaders := &dingtalkhrbrain_1_0.HrbrainImportWorkExpHeaders{}
  hrbrainImportWorkExpHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkhrbrain_1_0.HrbrainImportWorkExpRequestBody{
    Name: tea.String("张三"),
    WorkNo: tea.String("14530201131175645"),
    CompanyName: tea.String("阿里巴巴"),
    StartDate: tea.String("2024-01-01"),
    EndDate: tea.String("2024-04-01"),
    PostName: tea.String("开发工程师"),
    JobDesc: tea.String("服务端开发"),
  }
  hrbrainImportWorkExpRequest := &dingtalkhrbrain_1_0.HrbrainImportWorkExpRequest{
    CorpId: tea.String("ding3b*********88"),
    Body: []*dingtalkhrbrain_1_0.HrbrainImportWorkExpRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainImportWorkExpWithOptions(hrbrainImportWorkExpRequest, hrbrainImportWorkExpHeaders, &util.RuntimeOptions{})
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
const dingtalkhrbrain_1_0 = require('@alicloud/dingtalk/hrbrain_1_0');
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
    return new dingtalkhrbrain_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let hrbrainImportWorkExpHeaders = new dingtalkhrbrain_1_0.HrbrainImportWorkExpHeaders({ });
    hrbrainImportWorkExpHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let body0 = new dingtalkhrbrain_1_0.HrbrainImportWorkExpRequestBody({
      name: '张三',
      workNo: '14530201131175645',
      companyName: '阿里巴巴',
      startDate: '2024-01-01',
      endDate: '2024-04-01',
      postName: '开发工程师',
      jobDesc: '服务端开发',
    });
    let hrbrainImportWorkExpRequest = new dingtalkhrbrain_1_0.HrbrainImportWorkExpRequest({
      corpId: 'ding3b*********88',
      body: [
        body0
      ],
    });
    try {
      await client.hrbrainImportWorkExpWithOptions(hrbrainImportWorkExpRequest, hrbrainImportWorkExpHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
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
        public static AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpHeaders hrbrainImportWorkExpHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpHeaders();
            hrbrainImportWorkExpHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpRequest.HrbrainImportWorkExpRequestBody body0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpRequest.HrbrainImportWorkExpRequestBody
            {
                Name = "张三",
                WorkNo = "14530201131175645",
                CompanyName = "阿里巴巴",
                StartDate = "2024-01-01",
                EndDate = "2024-04-01",
                PostName = "开发工程师",
                JobDesc = "服务端开发",
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpRequest hrbrainImportWorkExpRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpRequest
            {
                CorpId = "ding3b*********88",
                Body = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportWorkExpRequest.HrbrainImportWorkExpRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.HrbrainImportWorkExpWithOptions(hrbrainImportWorkExpRequest, hrbrainImportWorkExpHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新是否成功：   - true：成功 - false：失败 |
| success | Boolean | 接口调用是否成功：   - true：成功 - false：失败 |
| requestId | String | 请求 ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true,
  "success" : true,
  "requestId" : "480021443f9f37fcbf464c4a6b85d289"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illegal. %s | 入参错误 |
