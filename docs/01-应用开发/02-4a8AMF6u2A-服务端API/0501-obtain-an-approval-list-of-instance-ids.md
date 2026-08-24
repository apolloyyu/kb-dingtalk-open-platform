---
title: "获取审批实例ID列表"
source_url: "https://open.dingtalk.com/document/development/obtain-an-approval-list-of-instance-ids"
namespace: "development"
slug: "obtain-an-approval-list-of-instance-ids"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批实例 > 获取审批实例ID列表"
doc_id: "EzsYM7fkLL"
updated_at: "2026-06-03 10:12:29"
---

> Source: https://open.dingtalk.com/document/development/obtain-an-approval-list-of-instance-ids
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批实例 > 获取审批实例ID列表
> Updated: 2026-06-03 10:12:29

# 获取审批实例ID列表

调用本接口，获取权限范围内的相关部门审批实例ID列表。

## **接口调用说明**

### 特别提醒

当前接口针对[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)客户可支持查询最多5年内的实例数据（即startTime时间距当前时间不能超过5年），升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景，查看全部[专享OpenAPI](1442-description-of-new-oa-approval-premium-exclusive-openapi-and-solutions.md)。

### 接口调用流程

1. 可以调用本接口获取审批流对应的审批实例ID。
2. 调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口，获取审批实例详情信息。

### 调用说明

- 如果只传入**startTime**参数，要求时间距离当前时间不能超过120天，**endTime**不传则默认取当前时间。
- 如果传入**startTime**参数和**endTime**参数，要求时间范围不能超过120天，同时**startTime**时间距当前时间不能超过365天。
- 批量获取的实例ID个数（循环获取），最多不能超过10000个。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/instanceIds/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workflow.Instance.Read-工作流实例读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 是 | 审批流的唯一码。   - 调用[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口获取`processCode`参数值。 - 通过[名词解释-processCode](0473-workflow-overview.md)获取。 |
| startTime | Long | 是 | 审批实例开始时间，Unix时间戳，单位毫秒。    例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.10 00:00:00对应的时间戳1586448000000。 |
| endTime | Long | 否 | 审批实例结束时间，Unix时间戳，单位毫秒。    例如，获取审批单发起时间在2020.4.10-2020.4.14之间，该值传2020.4.14 23:59:59对应的时间戳1586879999000。 |
| nextToken | Long | 是 | 分页游标。   - 如果是首次调用，该参数传0。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Long | 是 | 分页参数，每页大小，最多传20。 |
| userIds | Array of String | 否 | 发起人userId列表，最大列表长度为10，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| statuses | Array of String | 否 | 流程实例状态：   - **RUNNING**：审批中 - **TERMINATED**：已撤销 - **COMPLETED**：审批完成     未传值代表查询所有状态的实例ID列表。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processes/instanceIds/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processCode" : "PROC-FF6Y2xxxx",
  "startTime" : 1496678400000,
  "endTime" : 1496678400000,
  "nextToken" : 0,
  "maxResults" : 10,
  "userIds" : [ "发起userid" ],
  "statuses" : [ "RUNNING" ]
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsHeaders listProcessInstanceIdsHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsHeaders();
        listProcessInstanceIdsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsRequest listProcessInstanceIdsRequest = new com.aliyun.dingtalkworkflow_1_0.models.ListProcessInstanceIdsRequest()
                .setProcessCode("PROC-FF6Y2xxxx")
                .setStartTime(1496678400000L)
                .setEndTime(1496678400000L)
                .setNextToken(0L)
                .setMaxResults(10L)
                .setUserIds(java.util.Arrays.asList(
                    "发起userid"
                ))
                .setStatuses(java.util.Arrays.asList(
                    "RUNNING"
                ));
        try {
            client.listProcessInstanceIdsWithOptions(listProcessInstanceIdsRequest, listProcessInstanceIdsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_process_instance_ids_headers = dingtalkworkflow__1__0_models.ListProcessInstanceIdsHeaders()
        list_process_instance_ids_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_process_instance_ids_request = dingtalkworkflow__1__0_models.ListProcessInstanceIdsRequest(
            process_code='PROC-FF6Y2xxxx',
            start_time=1496678400000,
            end_time=1496678400000,
            next_token=0,
            max_results=10,
            user_ids=[
                '发起userid'
            ],
            statuses=[
                'RUNNING'
            ]
        )
        try:
            client.list_process_instance_ids_with_options(list_process_instance_ids_request, list_process_instance_ids_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_process_instance_ids_headers = dingtalkworkflow__1__0_models.ListProcessInstanceIdsHeaders()
        list_process_instance_ids_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_process_instance_ids_request = dingtalkworkflow__1__0_models.ListProcessInstanceIdsRequest(
            process_code='PROC-FF6Y2xxxx',
            start_time=1496678400000,
            end_time=1496678400000,
            next_token=0,
            max_results=10,
            user_ids=[
                '发起userid'
            ],
            statuses=[
                'RUNNING'
            ]
        )
        try:
            await client.list_process_instance_ids_with_options_async(list_process_instance_ids_request, list_process_instance_ids_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ListProcessInstanceIdsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ListProcessInstanceIdsRequest;
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
        $listProcessInstanceIdsHeaders = new ListProcessInstanceIdsHeaders([]);
        $listProcessInstanceIdsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listProcessInstanceIdsRequest = new ListProcessInstanceIdsRequest([
            "processCode" => "PROC-FF6Y2xxxx",
            "startTime" => 1496678400000,
            "endTime" => 1496678400000,
            "nextToken" => 0,
            "maxResults" => 10,
            "userIds" => [
                "发起userid"
            ],
            "statuses" => [
                "RUNNING"
            ]
        ]);
        try {
            $client->listProcessInstanceIdsWithOptions($listProcessInstanceIdsRequest, $listProcessInstanceIdsHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  listProcessInstanceIdsHeaders := &dingtalkworkflow_1_0.ListProcessInstanceIdsHeaders{}
  listProcessInstanceIdsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listProcessInstanceIdsRequest := &dingtalkworkflow_1_0.ListProcessInstanceIdsRequest{
    ProcessCode: tea.String("PROC-FF6Y2xxxx"),
    StartTime: tea.Int64(1496678400000),
    EndTime: tea.Int64(1496678400000),
    NextToken: tea.Int64(0),
    MaxResults: tea.Int64(10),
    UserIds: []*string{tea.String("发起userid")},
    Statuses: []*string{tea.String("RUNNING")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListProcessInstanceIdsWithOptions(listProcessInstanceIdsRequest, listProcessInstanceIdsHeaders, &util.RuntimeOptions{})
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
    let listProcessInstanceIdsHeaders = new $dingtalkworkflow_1_0.ListProcessInstanceIdsHeaders({ });
    listProcessInstanceIdsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listProcessInstanceIdsRequest = new $dingtalkworkflow_1_0.ListProcessInstanceIdsRequest({
      processCode: "PROC-FF6Y2xxxx",
      startTime: 1496678400000,
      endTime: 1496678400000,
      nextToken: 0,
      maxResults: 10,
      userIds: [
        "发起userid"
      ],
      statuses: [
        "RUNNING"
      ],
    });
    try {
      await client.listProcessInstanceIdsWithOptions(listProcessInstanceIdsRequest, listProcessInstanceIdsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListProcessInstanceIdsHeaders listProcessInstanceIdsHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListProcessInstanceIdsHeaders();
            listProcessInstanceIdsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListProcessInstanceIdsRequest listProcessInstanceIdsRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ListProcessInstanceIdsRequest
            {
                ProcessCode = "PROC-FF6Y2xxxx",
                StartTime = 1496678400000,
                EndTime = 1496678400000,
                NextToken = 0,
                MaxResults = 10,
                UserIds = new List<string>
                {
                    "发起userid"
                },
                Statuses = new List<string>
                {
                    "RUNNING"
                },
            };
            try
            {
                client.ListProcessInstanceIdsWithOptions(listProcessInstanceIdsRequest, listProcessInstanceIdsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| list | Array of String | 审批实例ID。 |
| nextToken | String | 分页游标。    不为空表示有更多数据。 |
| success | Boolean | 接口请求是否成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "list" : [ "123" ],
    "nextToken" : "10"
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidProcessCode | 审批模板processCode不能为空 | 审批模板processCode不能为空 |
| 400 | invalidInstanceListIdsStartTime | 获取审批实例ID列表，审批实例开始时间不能为空 | 获取审批实例ID列表，审批实例开始时间不能为空 |
| 400 | invalidNextToken | 获取审批实例ID列表，分页查询的游标不能为空 | 获取审批实例ID列表，分页查询的游标不能为空 |
| 400 | invalidMaxResults | 获取审批实例ID列表，分页参数非法，每页大小，最多传20。 | 获取审批实例ID列表，分页参数非法，每页大小，最多传20。 |
| 400 | invalidEndTime | 获取审批实例ID列表，审批实例结束时间不能小于开始时间；且查询时间范围不能超过120天。 | 获取审批实例ID列表，审批实例结束时间不能小于开始时间；且查询时间范围不能超过120天。 |
| 400 | invalidUserIds | 获取审批实例ID列表，发起userid列表参数非法，最大列表长度为10。 | 获取审批实例ID列表，发起userid列表参数非法，最大列表长度为10。 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
