---
title: "归档审批实例"
source_url: "https://open.dingtalk.com/document/development/api-archiveprocessinstance"
namespace: "development"
slug: "api-archiveprocessinstance"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 归档审批实例"
doc_id: "EGr8KincJu"
updated_at: "2026-06-03 10:12:42"
---

> Source: https://open.dingtalk.com/document/development/api-archiveprocessinstance
> Path: 应用开发 / 服务端 API / OA 审批 > 高级版专享接口 > 官方 OA 审批 > 审批实例 > 归档审批实例
> Updated: 2026-06-03 10:12:42

# 归档审批实例

调用本接口，可归档已完成的审批实例，归档后将不允许用户再次修改该审批实例。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)。

- 当前接口仅支持已OA审批管理员身份调用，即opUserId需要传OA审批管理员userId才能归档。
- 本接口只能归档已审批完成的审批实例，不能归档流程中的审批实例。归档后将不允许用户再次修改该审批实例。
- 已被归档的审批实例，不能被重复归档。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processInstances/archive |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限（OA高级版专享） |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 审批实例ID。   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| opUserId | String | 是 | 操作人的userId。      需要传OA审批管理员的userId才能归档。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processInstances/archive HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:be311xxxx
Content-Type:application/json

{
  "processInstanceId" : "a171de6c-8bxxxx",
  "opUserId" : "133743186427339452"
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.ArchiveProcessInstanceHeaders archiveProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ArchiveProcessInstanceHeaders();
        archiveProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.ArchiveProcessInstanceRequest archiveProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.ArchiveProcessInstanceRequest()
                .setProcessInstanceId("a171de6c-8bxxxx")
                .setOpUserId("133743186427339452");
        try {
            client.archiveProcessInstanceWithOptions(archiveProcessInstanceRequest, archiveProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        archive_process_instance_headers = dingtalkworkflow__1__0_models.ArchiveProcessInstanceHeaders()
        archive_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        archive_process_instance_request = dingtalkworkflow__1__0_models.ArchiveProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx',
            op_user_id='133743186427339452'
        )
        try:
            client.archive_process_instance_with_options(archive_process_instance_request, archive_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        archive_process_instance_headers = dingtalkworkflow__1__0_models.ArchiveProcessInstanceHeaders()
        archive_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        archive_process_instance_request = dingtalkworkflow__1__0_models.ArchiveProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx',
            op_user_id='133743186427339452'
        )
        try:
            await client.archive_process_instance_with_options_async(archive_process_instance_request, archive_process_instance_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ArchiveProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ArchiveProcessInstanceRequest;
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
        $archiveProcessInstanceHeaders = new ArchiveProcessInstanceHeaders([]);
        $archiveProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $archiveProcessInstanceRequest = new ArchiveProcessInstanceRequest([
            "processInstanceId" => "a171de6c-8bxxxx",
            "opUserId" => "133743186427339452"
        ]);
        try {
            $client->archiveProcessInstanceWithOptions($archiveProcessInstanceRequest, $archiveProcessInstanceHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
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
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  archiveProcessInstanceHeaders := &dingtalkworkflow_1_0.ArchiveProcessInstanceHeaders{}
  archiveProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  archiveProcessInstanceRequest := &dingtalkworkflow_1_0.ArchiveProcessInstanceRequest{
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
    OpUserId: tea.String("133743186427339452"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ArchiveProcessInstanceWithOptions(archiveProcessInstanceRequest, archiveProcessInstanceHeaders, &util.RuntimeOptions{})
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
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
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
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let archiveProcessInstanceHeaders = new dingtalkworkflow_1_0.ArchiveProcessInstanceHeaders({ });
    archiveProcessInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let archiveProcessInstanceRequest = new dingtalkworkflow_1_0.ArchiveProcessInstanceRequest({
      processInstanceId: 'a171de6c-8bxxxx',
      opUserId: '133743186427339452',
    });
    try {
      await client.archiveProcessInstanceWithOptions(archiveProcessInstanceRequest, archiveProcessInstanceHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ArchiveProcessInstanceHeaders archiveProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ArchiveProcessInstanceHeaders();
            archiveProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ArchiveProcessInstanceRequest archiveProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ArchiveProcessInstanceRequest
            {
                ProcessInstanceId = "a171de6c-8bxxxx",
                OpUserId = "133743186427339452",
            };
            try
            {
                client.ArchiveProcessInstanceWithOptions(archiveProcessInstanceRequest, archiveProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否归档成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 归档审批实例参数错误 | 请按接口文档检查请求入参是否正确 |
| 400 | userNotExist | 用户不存在 | 请检查opUserId参数是否正确，必须为组织内用户 |
| 400 | aflowProcessInstNotExist | 审批实例不存在 | 请检查processInstanceId参数是否正确 |
| 400 | aflowProcessInstStatusException | %s | 归档失败，审批单状态异常，具体可能为：仅支持对已完成的审批单操作归档、不能重复操作归档等 |
| 400 | invalidInstanceId | 审批实例ID不能为空 | 请检查processInstanceId参数是否正确 |
| 400 | invalidInstanceArchiveIsSystem | 归档审批实例，是否通过系统操作参数不能为空 | 归档审批实例，是否通过系统操作参数不能为空 |
| 400 | invalidInstanceArchiveOpUserId | 归档审批实例，当isSystem为false时，操作人的userId不能为空 | 归档审批实例，当isSystem为false时，操作人的userId不能为空 |
| 400 | internalError | %s | 系统内部异常，具体可能为：仅支持对已完成的审批单操作归档、不能重复操作归档等 |
| 400 | invalidInstanceArchiveOpUserIdNotOriginatorId | 归档审批实例，当isSystem为false时，操作人必须为OA审批管理员 | 归档审批实例，当isSystem为false时，操作人必须为OA审批管理员 |
| 400 | notOaAdmin | 无权限操作，操作人必须为OA审批管理员 | 请检查opUserId，操作人必须为OA审批管理员 |
| 500 | systemError | 系统异常 | 系统异常 |
| 500 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验失败，未开通或过期 |
| 500 | oaplus.query.limit | 请求过于频繁，稍后重试 | 请求过于频繁，稍后重试 |
