---
title: "更新待离职员工离职信息"
source_url: "https://open.dingtalk.com/document/development/api-updateempdismissioninfo"
namespace: "development"
slug: "api-updateempdismissioninfo"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 员工管理 > 更新待离职员工离职信息"
doc_id: "xGVeP9hiKs"
updated_at: "2026-06-04 19:10:29"
---

> Source: https://open.dingtalk.com/document/development/api-updateempdismissioninfo
> Path: 应用开发 / 服务端 API / 智能人事 > 员工管理 > 更新待离职员工离职信息
> Updated: 2026-06-04 19:10:29

# 更新待离职员工离职信息

根据离职用户 userId 和 离职原因 ID 等信息，更新待离职员工的离职信息

## 接口调用说明

用此接口更新的待离职员工信息，必须用智能人事的确认离职接口删除的人，离职信息才会生效，如果用非人事接口删人（如通讯录接口删人），更新的离职信息不会生效。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/pendingDismission/infos |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrm.Process.ReadWrite-智能人事流程读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 离职人userId。 |
| terminationReasonVoluntary | Array of String | 否 | 主动原因id，可调用[获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md)接口获取。 |
| terminationReasonPassive | Array of String | 否 | 被动原因id，可调用[获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md)接口获取。 |
| dismissionMemo | String | 否 | 离职原因备注。 |
| lastWorkDate | Long | 是 | 最后工作日。 |
| partner | Boolean | 否 | 是否加入HRM统计。 |

### 请求示例

HTTP

```
PUT /v1.0/hrm/pendingDismission/infos HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e73d7d0e99d234368c4f5b0088edc9c9
Content-Type:application/json

{
  "userId" : "2163515669935611",
  "terminationReasonVoluntary" : [ "1" ],
  "terminationReasonPassive" : [ "1" ],
  "dismissionMemo" : "备注信息",
  "lastWorkDate" : 1736489016000,
  "partner" : false
}
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
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.UpdateEmpDismissionInfoHeaders updateEmpDismissionInfoHeaders = new com.aliyun.dingtalkhrm_1_0.models.UpdateEmpDismissionInfoHeaders();
        updateEmpDismissionInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.UpdateEmpDismissionInfoRequest updateEmpDismissionInfoRequest = new com.aliyun.dingtalkhrm_1_0.models.UpdateEmpDismissionInfoRequest()
                .setUserId("2163515669935611")
                .setTerminationReasonVoluntary(java.util.Arrays.asList(
                    "1"
                ))
                .setTerminationReasonPassive(java.util.Arrays.asList(
                    "1"
                ))
                .setDismissionMemo("备注信息")
                .setLastWorkDate(1736489016000L)
                .setPartner(false);
        try {
            client.updateEmpDismissionInfoWithOptions(updateEmpDismissionInfoRequest, updateEmpDismissionInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_emp_dismission_info_headers = dingtalkhrm__1__0_models.UpdateEmpDismissionInfoHeaders()
        update_emp_dismission_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_emp_dismission_info_request = dingtalkhrm__1__0_models.UpdateEmpDismissionInfoRequest(
            user_id='2163515669935611',
            termination_reason_voluntary=[
                '1'
            ],
            termination_reason_passive=[
                '1'
            ],
            dismission_memo='备注信息',
            last_work_date=1736489016000,
            partner=False
        )
        try:
            client.update_emp_dismission_info_with_options(update_emp_dismission_info_request, update_emp_dismission_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_emp_dismission_info_headers = dingtalkhrm__1__0_models.UpdateEmpDismissionInfoHeaders()
        update_emp_dismission_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_emp_dismission_info_request = dingtalkhrm__1__0_models.UpdateEmpDismissionInfoRequest(
            user_id='2163515669935611',
            termination_reason_voluntary=[
                '1'
            ],
            termination_reason_passive=[
                '1'
            ],
            dismission_memo='备注信息',
            last_work_date=1736489016000,
            partner=False
        )
        try:
            await client.update_emp_dismission_info_with_options_async(update_emp_dismission_info_request, update_emp_dismission_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\UpdateEmpDismissionInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\UpdateEmpDismissionInfoRequest;
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
        $updateEmpDismissionInfoHeaders = new UpdateEmpDismissionInfoHeaders([]);
        $updateEmpDismissionInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateEmpDismissionInfoRequest = new UpdateEmpDismissionInfoRequest([
            "userId" => "2163515669935611",
            "terminationReasonVoluntary" => [
                "1"
            ],
            "terminationReasonPassive" => [
                "1"
            ],
            "dismissionMemo" => "备注信息",
            "lastWorkDate" => 1736489016000,
            "partner" => false
        ]);
        try {
            $client->updateEmpDismissionInfoWithOptions($updateEmpDismissionInfoRequest, $updateEmpDismissionInfoHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
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

  updateEmpDismissionInfoHeaders := &dingtalkhrm_1_0.UpdateEmpDismissionInfoHeaders{}
  updateEmpDismissionInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateEmpDismissionInfoRequest := &dingtalkhrm_1_0.UpdateEmpDismissionInfoRequest{
    UserId: tea.String("2163515669935611"),
    TerminationReasonVoluntary: []*string{tea.String("1")},
    TerminationReasonPassive: []*string{tea.String("1")},
    DismissionMemo: tea.String("备注信息"),
    LastWorkDate: tea.Int64(1736489016000),
    Partner: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateEmpDismissionInfoWithOptions(updateEmpDismissionInfoRequest, updateEmpDismissionInfoHeaders, &util.RuntimeOptions{})
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
const dingtalkhrm_1_0 = require('@alicloud/dingtalk/hrm_1_0');
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
    return new dingtalkhrm_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateEmpDismissionInfoHeaders = new dingtalkhrm_1_0.UpdateEmpDismissionInfoHeaders({ });
    updateEmpDismissionInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateEmpDismissionInfoRequest = new dingtalkhrm_1_0.UpdateEmpDismissionInfoRequest({
      userId: '2163515669935611',
      terminationReasonVoluntary: [
        '1'
      ],
      terminationReasonPassive: [
        '1'
      ],
      dismissionMemo: '备注信息',
      lastWorkDate: 1736489016000,
      partner: false,
    });
    try {
      await client.updateEmpDismissionInfoWithOptions(updateEmpDismissionInfoRequest, updateEmpDismissionInfoHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.UpdateEmpDismissionInfoHeaders updateEmpDismissionInfoHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.UpdateEmpDismissionInfoHeaders();
            updateEmpDismissionInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.UpdateEmpDismissionInfoRequest updateEmpDismissionInfoRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.UpdateEmpDismissionInfoRequest
            {
                UserId = "2163515669935611",
                TerminationReasonVoluntary = new List<string>
                {
                    "1"
                },
                TerminationReasonPassive = new List<string>
                {
                    "1"
                },
                DismissionMemo = "备注信息",
                LastWorkDate = 1736489016000,
                Partner = false,
            };
            try
            {
                client.UpdateEmpDismissionInfoWithOptions(updateEmpDismissionInfoRequest, updateEmpDismissionInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |
| result | Boolean | 结果内容。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "679477AA-74B9-764E-9B2C-BD73540FD227",
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 参数错误 | 未填最后工作日、离职人userId等 |
| 401 | businessError | 业务异常 | 例如员工不是待离职状态、所填离职原因不存在等异常 |
| 500 | systemError | 系统异常 | 系统异常 |
