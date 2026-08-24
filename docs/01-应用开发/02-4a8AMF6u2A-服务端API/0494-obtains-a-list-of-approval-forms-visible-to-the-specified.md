---
title: "获取指定用户可见的审批表单列表"
source_url: "https://open.dingtalk.com/document/development/obtains-a-list-of-approval-forms-visible-to-the-specified"
namespace: "development"
slug: "obtains-a-list-of-approval-forms-visible-to-the-specified"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批表单 > 获取指定用户可见的审批表单列表"
doc_id: "UNCZI46dqz"
updated_at: "2026-06-03 10:12:23"
---

> Source: https://open.dingtalk.com/document/development/obtains-a-list-of-approval-forms-visible-to-the-specified
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批表单 > 获取指定用户可见的审批表单列表
> Updated: 2026-06-03 10:12:23

# 获取指定用户可见的审批表单列表

调用本接口，可根据员工的userId分页获取该用户可见的审批表单列表，每次最多获取100个表单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/userVisibilities/templates |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workflow.Form.Read-工作流模板读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 要查询的员工的userId。      不传表示查询企业下所有审批表单。 |
| maxResults | Long | 是 | 分页大小，最大值100。 |
| nextToken | Long | 是 | 分页游标。   - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/processes/userVisibilities/templates?userId=manager7078&maxResults=10&nextToken=0 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesHeaders listUserVisibleBpmsProcessesHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesHeaders();
        listUserVisibleBpmsProcessesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesRequest listUserVisibleBpmsProcessesRequest = new com.aliyun.dingtalkworkflow_1_0.models.ListUserVisibleBpmsProcessesRequest()
                .setUserId("manager7078")
                .setMaxResults(10L)
                .setNextToken(0L);
        try {
            client.listUserVisibleBpmsProcessesWithOptions(listUserVisibleBpmsProcessesRequest, listUserVisibleBpmsProcessesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_user_visible_bpms_processes_headers = dingtalkworkflow__1__0_models.ListUserVisibleBpmsProcessesHeaders()
        list_user_visible_bpms_processes_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_user_visible_bpms_processes_request = dingtalkworkflow__1__0_models.ListUserVisibleBpmsProcessesRequest(
            user_id='manager7078',
            max_results=10,
            next_token=0
        )
        try:
            client.list_user_visible_bpms_processes_with_options(list_user_visible_bpms_processes_request, list_user_visible_bpms_processes_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_user_visible_bpms_processes_headers = dingtalkworkflow__1__0_models.ListUserVisibleBpmsProcessesHeaders()
        list_user_visible_bpms_processes_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_user_visible_bpms_processes_request = dingtalkworkflow__1__0_models.ListUserVisibleBpmsProcessesRequest(
            user_id='manager7078',
            max_results=10,
            next_token=0
        )
        try:
            await client.list_user_visible_bpms_processes_with_options_async(list_user_visible_bpms_processes_request, list_user_visible_bpms_processes_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ListUserVisibleBpmsProcessesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ListUserVisibleBpmsProcessesRequest;
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
        $listUserVisibleBpmsProcessesHeaders = new ListUserVisibleBpmsProcessesHeaders([]);
        $listUserVisibleBpmsProcessesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listUserVisibleBpmsProcessesRequest = new ListUserVisibleBpmsProcessesRequest([
            "userId" => "manager7078",
            "maxResults" => 10,
            "nextToken" => 0
        ]);
        try {
            $client->listUserVisibleBpmsProcessesWithOptions($listUserVisibleBpmsProcessesRequest, $listUserVisibleBpmsProcessesHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  listUserVisibleBpmsProcessesHeaders := &dingtalkworkflow_1_0.ListUserVisibleBpmsProcessesHeaders{}
  listUserVisibleBpmsProcessesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listUserVisibleBpmsProcessesRequest := &dingtalkworkflow_1_0.ListUserVisibleBpmsProcessesRequest{
    UserId: tea.String("manager7078"),
    MaxResults: tea.Int64(10),
    NextToken: tea.Int64(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListUserVisibleBpmsProcessesWithOptions(listUserVisibleBpmsProcessesRequest, listUserVisibleBpmsProcessesHeaders, &util.RuntimeOptions{})
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
import dingtalkworkflow_1_0, * as $dingtalkworkflow_1_0 from '@alicloud/dingtalk/workflow_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkflow_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkflow_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listUserVisibleBpmsProcessesHeaders = new $dingtalkworkflow_1_0.ListUserVisibleBpmsProcessesHeaders({ });
    listUserVisibleBpmsProcessesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listUserVisibleBpmsProcessesRequest = new $dingtalkworkflow_1_0.ListUserVisibleBpmsProcessesRequest({
      userId: "manager7078",
      maxResults: 10,
      nextToken: 0,
    });
    try {
      await client.listUserVisibleBpmsProcessesWithOptions(listUserVisibleBpmsProcessesRequest, listUserVisibleBpmsProcessesHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListUserVisibleBpmsProcessesHeaders listUserVisibleBpmsProcessesHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListUserVisibleBpmsProcessesHeaders();
            listUserVisibleBpmsProcessesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListUserVisibleBpmsProcessesRequest listUserVisibleBpmsProcessesRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListUserVisibleBpmsProcessesRequest
            {
                UserId = "manager7078",
                MaxResults = 10,
                NextToken = 0,
            };
            try
            {
                client.ListUserVisibleBpmsProcessesWithOptions(listUserVisibleBpmsProcessesRequest, listUserVisibleBpmsProcessesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| processList | Array | 可见表单列表。 |
| name | String | 表单名称。 |
| url | String | 表单URL。 |
| iconUrl | String | 图标URL。 |
| processCode | String | 表单唯一标识。 |
| dirId | String | 模板所在分组 ID。 |
| dirName | String | 模板所在分组名称。 |
| nextToken | Long | 分页游标。      不为空表示有更多数据。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "processList" : [ {
      "name" : "物品领用",
      "url" : "https://aflow.dingtalk.com/dingtalk/mobile/homepage.htm?xxxx",
      "iconUrl" : "https://gw.xxxx/T-102-102.png",
      "processCode" : "PROC-YMLA1-xxxx-11WFJ-1",
      "dirId" : "12347899",
      "dirName" : "财务管理"
    } ],
    "nextToken" : 10
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidNextToken | 获取指定用户可见的审批表单列表，分页查询的游标不能为空 | 获取指定用户可见的审批表单列表，分页查询的游标不能为空 |
| 400 | invalidMaxResults | 获取指定用户可见的审批表单列表，分页参数非法，每页大小，最多传100。 | 获取指定用户可见的审批表单列表，每页大小，最多传100。 |
| 400 | invalidParameter | 获取指定用户可见的审批表单列表参数错误 | 获取指定用户可见的审批表单列表参数错误 |
| 400 | aflowProcessGetFailed | 获取用户可见的审批模板失败 | 获取用户可见的审批模板失败 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
