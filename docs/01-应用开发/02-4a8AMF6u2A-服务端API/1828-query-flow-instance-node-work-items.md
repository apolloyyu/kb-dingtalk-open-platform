---
title: "查询流程实例节点工作项"
source_url: "https://open.dingtalk.com/document/development/query-flow-instance-node-work-items"
namespace: "development"
slug: "query-flow-instance-node-work-items"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 氚云 > 流程 > 查询流程实例节点工作项"
doc_id: "HnSLk7fwwH"
updated_at: "2025-09-08 19:06:27"
---

> Source: https://open.dingtalk.com/document/development/query-flow-instance-node-work-items
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 氚云 > 流程 > 查询流程实例节点工作项
> Updated: 2025-09-08 19:06:27

# 查询流程实例节点工作项

调用本接口获取流程实例节点工作项的相关信息。

> **[!IMPORTANT]**
>
> 为了更进一步提升接口质量以及用户体验，我们对本接口文档做出如下调整：
>
> - 自 2024 年 8 月 1 日起，本接口文档将会被迁移至历史文档目录。
> - 氚云接口不再支持新应用接入，已接入应用可继续使用，后续若需要接入氚云接口，请使用[氚云开发者手册](https://help.h3yun.com/channels/899.html)。

![](https://img.alicdn.com/imgextra/i2/O1CN01hojbHe1jQHezWtbLv_!!6000000004542-2-tps-1080-527.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=h3yun_1.0%23QueryProcessesWorkItems) |
| 第三方企业应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=h3yun_1.0%23QueryProcessesWorkItems) |
| 第三方个人应用 | 暂不支持 | 氚云数据管理权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/h3yun/processes/workItems?processInstanceId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 流程实例ID。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 状态码。 |
| message | String | 状态码描述。 |
| data | Array | 工作项实例信息列表。 |
| workItemId | String | 工作任务ID。 |
| workItemType | String | 工作项类型，取值：   - **Fill**：普通工作项 - **Approve**：审批类型工作项 - **Circulate**：传阅 |
| processInstanceId | String | 流程实例ID。 |
| appCode | String | 应用编码。 |
| schemaCode | String | 表单编码。 |
| bizObjectId | String | 工作项所关联的业务对象ID。 |
| processVersion | String | 工作流版本。 |
| activityCode | String | 活动编码。 |
| activityName | String | 当前活动名称。 |
| displayName | String | 显示名称。 |
| state | String | 状态，取值：   - **Waiting**：等待的状态 - **Working**：正在工作中的状态 - **Finished**：处于完成状态 - **Canceled**：已经被取消 - **Forwarded**：已转交状态 - **Revoked**：撤回 |
| isFinish | Boolean | 是否已完成。 |
| receiveTimeGMT | String | 接收时间。 |
| startTimeGMT | String | 开始这个任务的时间。 |
| finishTimeGMT | String | 完成时间。 |
| comment | String | 对该工作项的意见。 |
| isApproval | Boolean | 对该工作项是否同意。 |
| participant | Object | 参与者。 |
| userId | String | 用户ID。 |
| name | String | 用户名称。 |
| departmentId | String | 用户直属的部门ID。 |
| departmentName | String | 用户直属的部门名称。 |
| finisher | Object | 完成者。 |
| userId | String | 用户ID。 |
| name | String | 用户名称。 |
| departmentId | String | 用户直属的部门ID。 |
| departmentName | String | 用户直属的部门名称。 |
| receiptor | Object | 转交工作的接收人。如无转接人，则为空。 |
| userId | String | 用户ID。 |
| name | String | 用户名称。 |
| departmentId | String | 用户直属的部门ID。 |
| departmentName | String | 用户直属的部门名称。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/h3yun/processes/workItems?processInstanceId=006f870b-4d1c-xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bef2c84c7xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkh3yun_1_0.*;
import com.aliyun.dingtalkh3yun_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkh3yun_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkh3yun_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkh3yun_1_0.Client client = Sample.createClient();
        QueryProcessesWorkItemsHeaders queryProcessesWorkItemsHeaders = new QueryProcessesWorkItemsHeaders();
        queryProcessesWorkItemsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryProcessesWorkItemsRequest queryProcessesWorkItemsRequest = new QueryProcessesWorkItemsRequest()
                .setProcessInstanceId("006f870b-4d1c-xxx");
        try {
            client.queryProcessesWorkItemsWithOptions(queryProcessesWorkItemsRequest, queryProcessesWorkItemsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.h3yun_1_0.client import Client as dingtalkh3yun_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.h3yun_1_0 import models as dingtalkh_3yun__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkh3yun_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkh3yun_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_processes_work_items_headers = dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsHeaders()
        query_processes_work_items_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_processes_work_items_request = dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsRequest(
            process_instance_id='006f870b-4d1c-xxx'
        )
        try:
            client.query_processes_work_items_with_options(query_processes_work_items_request, query_processes_work_items_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_processes_work_items_headers = dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsHeaders()
        query_processes_work_items_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_processes_work_items_request = dingtalkh_3yun__1__0_models.QueryProcessesWorkItemsRequest(
            process_instance_id='006f870b-4d1c-xxx'
        )
        try:
            await client.query_processes_work_items_with_options_async(query_processes_work_items_request, query_processes_work_items_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\QueryProcessesWorkItemsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\QueryProcessesWorkItemsRequest;
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
        $queryProcessesWorkItemsHeaders = new QueryProcessesWorkItemsHeaders([]);
        $queryProcessesWorkItemsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryProcessesWorkItemsRequest = new QueryProcessesWorkItemsRequest([
            "processInstanceId" => "006f870b-4d1c-xxx"
        ]);
        try {
            $client->queryProcessesWorkItemsWithOptions($queryProcessesWorkItemsRequest, $queryProcessesWorkItemsHeaders, new RuntimeOptions([]));
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
  dingtalkh3yun_1_0  "github.com/alibabacloud-go/dingtalk/h3yun_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkh3yun_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkh3yun_1_0.Client{}
  _result, _err = dingtalkh3yun_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryProcessesWorkItemsHeaders := &dingtalkh3yun_1_0.QueryProcessesWorkItemsHeaders{}
  queryProcessesWorkItemsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryProcessesWorkItemsRequest := &dingtalkh3yun_1_0.QueryProcessesWorkItemsRequest{
    ProcessInstanceId: tea.String("006f870b-4d1c-xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryProcessesWorkItemsWithOptions(queryProcessesWorkItemsRequest, queryProcessesWorkItemsHeaders, &util.RuntimeOptions{})
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
import dingtalkh3yun_1_0, * as $dingtalkh3yun_1_0 from '@alicloud/dingtalk/h3yun_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkh3yun_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkh3yun_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryProcessesWorkItemsHeaders = new $dingtalkh3yun_1_0.QueryProcessesWorkItemsHeaders({ });
    queryProcessesWorkItemsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryProcessesWorkItemsRequest = new $dingtalkh3yun_1_0.QueryProcessesWorkItemsRequest({
      processInstanceId: "006f870b-4d1c-xxx",
    });
    try {
      await client.queryProcessesWorkItemsWithOptions(queryProcessesWorkItemsRequest, queryProcessesWorkItemsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.QueryProcessesWorkItemsHeaders queryProcessesWorkItemsHeaders = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.QueryProcessesWorkItemsHeaders();
            queryProcessesWorkItemsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.QueryProcessesWorkItemsRequest queryProcessesWorkItemsRequest = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.QueryProcessesWorkItemsRequest
            {
                ProcessInstanceId = "006f870b-4d1c-xxx",
            };
            try
            {
                client.QueryProcessesWorkItemsWithOptions(queryProcessesWorkItemsRequest, queryProcessesWorkItemsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkh_3yun__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkh3yun_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkh3yun_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::Client> client = make_shared<Alibabacloud_Dingtalkh3yun_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::QueryProcessesWorkItemsHeaders> queryProcessesWorkItemsHeaders = make_shared<Alibabacloud_Dingtalkh3yun_1_0::QueryProcessesWorkItemsHeaders>();
  queryProcessesWorkItemsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::QueryProcessesWorkItemsRequest> queryProcessesWorkItemsRequest = make_shared<Alibabacloud_Dingtalkh3yun_1_0::QueryProcessesWorkItemsRequest>(map<string, boost::any>({
    {"processInstanceId", boost::any(string("006f870b-4d1c-xxx"))}
  }));
  try {
    client->queryProcessesWorkItemsWithOptions(queryProcessesWorkItemsRequest, queryProcessesWorkItemsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "code" : "success",
  "message" : "OK",
  "data" : [ {
    "workItemId" : "3d0ad4a4-d7d5-xxx",
    "workItemType" : "Fill",
    "processInstanceId" : "006f870b-4d1c-xxx",
    "appCode" : "D000001",
    "schemaCode" : "D0001833abbxxx",
    "bizObjectId" : "106f870b-4d1c-4xxx",
    "processVersion" : "3",
    "activityCode" : "Activity1",
    "activityName" : "发起流程",
    "displayName" : "发起流程",
    "state" : "Waiting",
    "isFinish" : false,
    "receiveTimeGMT" : "2021-11-19 19:36:54",
    "startTimeGMT" : "2021-11-19 19:36:54",
    "finishTimeGMT" : "null",
    "comment" : "同意",
    "isApproval" : true,
    "participant" : {
      "userId" : "aea4d7a7-d162-xxx",
      "name" : "张三",
      "departmentId" : "18f923a7-5a5e-xxx",
      "departmentName" : "研发中心"
    },
    "finisher" : {
      "userId" : "aea4d7a7-d162-4xxx",
      "name" : "张三",
      "departmentId" : "18f923a7-5a5e-4xxx",
      "departmentName" : "研发中心"
    },
    "receiptor" : {
      "userId" : "aea4d7a7-d162-4xxx",
      "name" : "小红",
      "departmentId" : "18f923a7-5a5e-4xxx",
      "departmentName" : "研发中心"
    }
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | dataNotExist.process.instanceNotExist | 流程实例不存在 | 流程实例不存在 |
