---
title: "获取流程详细信息及操作记录"
source_url: "https://open.dingtalk.com/document/development/obtains-the-task-details"
namespace: "development"
slug: "obtains-the-task-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 获取流程详细信息及操作记录"
doc_id: "opeWYyHgTw"
updated_at: "2025-09-23 19:21:46"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-task-details
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 获取流程详细信息及操作记录
> Updated: 2025-09-23 19:21:46

# 获取流程详细信息及操作记录

用于获取流程详细信息及操作记录。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/flowTasks/{taskId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-E签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceGroup | String | 否 | 预留参数，此版本无需此参数。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 是 | 签署返回的任务ID。 |

### 请求示例

HTTP

```
GET /v2.0/esign/flowTasks/PRO-E990Dxxx HTTP/1.1
Host:api.dingtalk.com
serviceGroup:-
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_2_0.*;
import com.aliyun.dingtalkesign_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_2_0.Client client = Sample.createClient();
        GetFlowDetailHeaders getFlowDetailHeaders = new GetFlowDetailHeaders();
        getFlowDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getFlowDetailWithOptions("PRO-E990Dxxx", getFlowDetailHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_2_0.client import Client as dingtalkesign_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_flow_detail_headers = dingtalkesign__2__0_models.GetFlowDetailHeaders()
        get_flow_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_flow_detail_with_options('PRO-E990Dxxx', get_flow_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_flow_detail_headers = dingtalkesign__2__0_models.GetFlowDetailHeaders()
        get_flow_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_flow_detail_with_options_async('PRO-E990Dxxx', get_flow_detail_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\GetFlowDetailHeaders;
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
        try {
            $client->getFlowDetailWithOptions("PRO-E990Dxxx", $getFlowDetailHeaders, new RuntimeOptions([]));
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
  dingtalkesign_2_0  ""github.com/alibabacloud-go/dingtalk/esign_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_2_0.Client{}
  _result, _err = dingtalkesign_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getFlowDetailHeaders := &dingtalkesign_2_0.GetFlowDetailHeaders{}
  getFlowDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFlowDetailWithOptions(tea.String("PRO-E990Dxxx"), getFlowDetailHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_2_0, * as $dingtalkesign_2_0 from '"@alicloud/dingtalk/esign_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFlowDetailHeaders = new $dingtalkesign_2_0.GetFlowDetailHeaders({ });
    getFlowDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.getFlowDetailWithOptions("PRO-E990Dxxx", getFlowDetailHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetFlowDetailHeaders getFlowDetailHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.GetFlowDetailHeaders();
            getFlowDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetFlowDetailWithOptions("PRO-E990Dxxx", getFlowDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__2__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>

using namespace std;

Alibabacloud_Dingtalkesign_2_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_2_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_2_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::GetFlowDetailHeaders> getFlowDetailHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::GetFlowDetailHeaders>();
  getFlowDetailHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  try {
    client->getFlowDetailWithOptions(make_shared<string>("PRO-E990Dxxx"), getFlowDetailHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| businessScene | String | 流程业务场景，流程主题。 |
| flowStatus | Float | 流程状态，取值：   - 0：草稿 - 1：签署中 - 2：完成 - 3：撤销 - 4：终止（由于某些异常情况，无法完成签署） - 5：过期（签署截至日志到期后触发） - 7：拒签 |
| initiatorAuthorizedName | String | 发起主体名称。 |
| initiatorName | String | 发起人名称。 |
| logs | Array | 流程操作日志。 |
| operatorAccountName | String | 操作人姓名。 |
| logType | String | 操作类型，取值：   - 1：创建流程 - 2：删除流程 - 3：更新流程 - 4：开启流程 - 5：撤回流程 - 6：流程过期 - 7：归档流程 - 8：查看流程 - 9：转交 - 20：添加签署区 - 21：删除签署区 - 22：更新签署区 - 23：签署 - 24：转签 - 25：通知签署 - 26：拒绝签署 - 27：发起用印审批 - 28：同意用印审批 - 29：拒绝用印审批 - 40：添加文档 - 41：删除文档 - 42：更新文档 - 50：添加附件 - 51：删除附件 - 52：更新附件 - 60：添加参与人 - 61：删除参与人 - 62：更新参与人 |
| operateDescription | String | 操作描述。 |
| operateTime | Float | 操作时间戳。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "businessScene" : "isv融合版发起测试3",
  "flowStatus" : 1,
  "initiatorAuthorizedName" : "上海途锦国际旅行",
  "initiatorName" : "赵xx",
  "logs" : [ {
    "operatorAccountName" : "赵xx",
    "logType" : "8",
    "operateDescription" : "查看流程",
    "operateTime" : 1618302600000
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | getFlowInfoError | 查询流程信息异常 | 查询流程信息异常 |
| 400 | queryFlowDetailError | 查询流程详情异常 | 查询流程详情异常 |
| 400 | flowNotExists | 流程信息不存在 | 流程信息不存在 |
| 400 | userInfoError | 用户信息异常 | 用户信息异常 |
