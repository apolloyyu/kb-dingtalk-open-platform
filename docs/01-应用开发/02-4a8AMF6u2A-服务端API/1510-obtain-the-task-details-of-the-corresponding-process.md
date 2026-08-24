---
title: "获取流程任务详情"
source_url: "https://open.dingtalk.com/document/development/obtain-the-task-details-of-the-corresponding-process"
namespace: "development"
slug: "obtain-the-task-details-of-the-corresponding-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 签署流程 > 获取流程任务详情"
doc_id: "NvirXrwBZO"
updated_at: "2026-06-23 18:10:44"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-task-details-of-the-corresponding-process
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > e签宝 1.0 > 签署流程 > 获取流程任务详情
> Updated: 2026-06-23 18:10:44

# 获取流程任务详情

调用本接口获取流程详细信息及操作记录。

## **接口调用说明**

当前接口已完成升级迭代且不再支持新应用申请，存量应用调用不受影响，建议未接入的开发者使用[获取流程的签署详情](1088-get-the-details-of-process-signing.md)接口，已接入的开发者结合实际尽快完成迁移。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/esign/flows/detail |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 不支持新增申请 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 否 | 发起签署时得到的任务id。 |

### 请求示例

HTTP

```
GET /v1.0/esign/flows/detail?taskId=hf9e762382973928 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3XXXX
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_1_0.*;
import com.aliyun.dingtalkesign_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_1_0.Client client = Sample.createClient();
        GetFlowDetailHeaders getFlowDetailHeaders = new GetFlowDetailHeaders();
        getFlowDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetFlowDetailRequest getFlowDetailRequest = new GetFlowDetailRequest()
                .setTaskId("hf9e762382973928");
        try {
            client.getFlowDetailWithOptions(getFlowDetailRequest, getFlowDetailHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_1_0.client import Client as dingtalkesign_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_flow_detail_headers = dingtalkesign__1__0_models.GetFlowDetailHeaders()
        get_flow_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_flow_detail_request = dingtalkesign__1__0_models.GetFlowDetailRequest(
            task_id='hf9e762382973928'
        )
        try:
            client.get_flow_detail_with_options(get_flow_detail_request, get_flow_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_flow_detail_headers = dingtalkesign__1__0_models.GetFlowDetailHeaders()
        get_flow_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_flow_detail_request = dingtalkesign__1__0_models.GetFlowDetailRequest(
            task_id='hf9e762382973928'
        )
        try:
            await client.get_flow_detail_with_options_async(get_flow_detail_request, get_flow_detail_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetFlowDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetFlowDetailRequest;
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
        $getFlowDetailHeaders = new GetFlowDetailHeaders([]);
        $getFlowDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFlowDetailRequest = new GetFlowDetailRequest([
            "taskId" => "hf9e762382973928"
        ]);
        try {
            $client->getFlowDetailWithOptions($getFlowDetailRequest, $getFlowDetailHeaders, new RuntimeOptions([]));
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
  dingtalkesign_1_0  ""github.com/alibabacloud-go/dingtalk/esign_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_1_0.Client{}
  _result, _err = dingtalkesign_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getFlowDetailHeaders := &dingtalkesign_1_0.GetFlowDetailHeaders{}
  getFlowDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFlowDetailRequest := &dingtalkesign_1_0.GetFlowDetailRequest{
    TaskId: tea.String("hf9e762382973928"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFlowDetailWithOptions(getFlowDetailRequest, getFlowDetailHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_1_0, * as $dingtalkesign_1_0 from '"@alicloud/dingtalk/esign_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFlowDetailHeaders = new $dingtalkesign_1_0.GetFlowDetailHeaders({ });
    getFlowDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getFlowDetailRequest = new $dingtalkesign_1_0.GetFlowDetailRequest({
      taskId: "hf9e762382973928",
    });
    try {
      await client.getFlowDetailWithOptions(getFlowDetailRequest, getFlowDetailHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetFlowDetailHeaders getFlowDetailHeaders = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetFlowDetailHeaders();
            getFlowDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetFlowDetailRequest getFlowDetailRequest = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetFlowDetailRequest
            {
                TaskId = "hf9e762382973928",
            };
            try
            {
                client.GetFlowDetailWithOptions(getFlowDetailRequest, getFlowDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetFlowDetailHeaders> getFlowDetailHeaders = make_shared<Alibabacloud_Dingtalkesign_1_0::GetFlowDetailHeaders>();
  getFlowDetailHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetFlowDetailRequest> getFlowDetailRequest = make_shared<Alibabacloud_Dingtalkesign_1_0::GetFlowDetailRequest>(map<string, boost::any>({
    {"taskId", boost::any(string("hf9e762382973928"))}
  }));
  try {
    client->getFlowDetailWithOptions(getFlowDetailRequest, getFlowDetailHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| data | Object | 返回的数据。 |
| businessSense | String | 流程业务场景。 |
| flowStatus | Integer | 流程状态，取值：   - 0：草稿 - 1：签署中 - 2：完成 - 3：撤销 - 4：终止（由于某些异常情况，无法完成签署) - 5：过期（签署截至日志到期后触发) - 7：拒签 |
| initiatorAuthorizedName | String | 发起主体名称。 |
| initiatorName | String | 发起人名称。 |
| logs | Array | 流程操作日志列表。 |
| operatorAccountName | String | 操作人姓名。 |
| logType | String | 流程操作日志类型，取值：   - 1：创建流程 - 2：删除流程 - 3：更新流程 - 4：开启流程 - 5：撤回流程 - 6：流程过期 - 7：归档流程 - 8：查看流程 - 9：转交 - 20：添加签署区 - 21：删除签署区 - 22：更新签署区 - 23：签署 - 24：转签 - 25：通知签署 - 26：拒绝签署 - 27：发起用印审批 - 28：同意用印审批 - 29：拒绝用印审批 - 40：添加文档 - 41：删除文档 - 42：更新文档 - 50：添加附件 - 51：删除附件 - 52：更新附件 - 60：添加参与人 - 61：删除参与人 - 62：更新参与人 |
| operateDescription | String | 操作描述。 |
| operateTime | Long | 操作时间戳。 |
| code | Integer | 返回码。 |
| message | String | 返回码描述。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : {
    "businessSense" : "业务场景",
    "flowStatus" : 1,
    "initiatorAuthorizedName" : "测试组织",
    "initiatorName" : "测试用户",
    "logs" : [ {
      "operatorAccountName" : "测试用户",
      "logType" : "1",
      "operateDescription" : "创建流程",
      "operateTime" : 1613718318000
    } ]
  },
  "code" : 0,
  "message" : "ok"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.invalidAguemnts | 参数错误:%s | 参数错误 |
