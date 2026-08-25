---
title: "执行宜搭的审批任务"
source_url: "https://open.dingtalk.com/document/development/execute-appropriate-approval-tasks"
namespace: "development"
slug: "execute-appropriate-approval-tasks"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 任务 > 执行宜搭的审批任务"
doc_id: "Cqn75YWCWt"
updated_at: "2025-09-08 19:04:03"
---

> Source: https://open.dingtalk.com/document/development/execute-appropriate-approval-tasks
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 宜搭 > 任务 > 执行宜搭的审批任务
> Updated: 2025-09-08 19:04:03

# 执行宜搭的审批任务

调动本接口执行宜搭平台审批任务。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，宜搭接口计划升级，后续完善更多功能，重新开放时间请关注文档更新日志。
>
> - 宜搭接口相关文档，已于**2022年3月11日**迁移至**历史文档（不推荐）**目录。
> - 不再支持新应用接入，已接入的应用可以正常调用。

![](https://img.alicdn.com/imgextra/i1/O1CN01wHCtUk21Sir8MOpuU_!!6000000006984-2-tps-1016-558.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | 暂不支持 |
| 第三方企业应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请。 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/yida/tasks/platformTasks/execute HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "outResult" : "String",
  "noExecuteExpressions" : "String",
  "appType" : "String",
  "formDataJson" : "String",
  "systemToken" : "String",
  "language" : "String",
  "remark" : "String",
  "processInstanceId" : "String",
  "userId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)获取。 - 第三方企业应用调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outResult | String | 是 | 审批结果，取值：   - **agree**：同意 - disagree：拒绝 |
| noExecuteExpressions | String | 否 | 是否不执行校验和关联操作，取值：   - **y**：不执行校验规则&关联操作 - **n**：执行校验规则&关联操作（默认值） |
| appType | String | 是 | 应用ID。 |
| formDataJson | String | 否 | 更新的表单数据。 |
| systemToken | String | 是 | 应用秘钥。 |
| language | String | 否 | 语言，取值：   - zh\_CN：中文（默认值） - en\_US：英文 |
| remark | String | 是 | 审批意见。 |
| processInstanceId | String | 是 | 流程实例ID。 |
| userId | String | 是 | 用户的userid。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/yida/tasks/platformTasks/execute HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "outResult" : "agree",
  "noExecuteExpressions" : "y",
  "appType" : "APP_PBKT0xxx",
  "formDataJson" : "未知",
  "systemToken" : "hexxyyddd",
  "language" : "zh_CN",
  "remark" : "确认同意",
  "processInstanceId" : "f30233fb-72exxx",
  "userId" : "yida_pub_account"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkyida_1_0.*;
import com.aliyun.dingtalkyida_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkyida_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkyida_1_0.Client client = Sample.createClient();
        ExecutePlatformTaskHeaders executePlatformTaskHeaders = new ExecutePlatformTaskHeaders();
        executePlatformTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ExecutePlatformTaskRequest executePlatformTaskRequest = new ExecutePlatformTaskRequest()
                .setOutResult("agree")
                .setNoExecuteExpressions("y")
                .setAppType("APP_PBKT0xxx")
                .setFormDataJson("未知")
                .setSystemToken("hexxyyddd")
                .setLanguage("zh_CN")
                .setRemark("确认同意")
                .setProcessInstanceId("f30233fb-72exxx")
                .setUserId("yida_pub_account");
        try {
            client.executePlatformTaskWithOptions(executePlatformTaskRequest, executePlatformTaskHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        execute_platform_task_headers = dingtalkyida__1__0_models.ExecutePlatformTaskHeaders()
        execute_platform_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        execute_platform_task_request = dingtalkyida__1__0_models.ExecutePlatformTaskRequest(
            out_result='agree',
            no_execute_expressions='y',
            app_type='APP_PBKT0xxx',
            form_data_json='未知',
            system_token='hexxyyddd',
            language='zh_CN',
            remark='确认同意',
            process_instance_id='f30233fb-72exxx',
            user_id='yida_pub_account'
        )
        try:
            client.execute_platform_task_with_options(execute_platform_task_request, execute_platform_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        execute_platform_task_headers = dingtalkyida__1__0_models.ExecutePlatformTaskHeaders()
        execute_platform_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        execute_platform_task_request = dingtalkyida__1__0_models.ExecutePlatformTaskRequest(
            out_result='agree',
            no_execute_expressions='y',
            app_type='APP_PBKT0xxx',
            form_data_json='未知',
            system_token='hexxyyddd',
            language='zh_CN',
            remark='确认同意',
            process_instance_id='f30233fb-72exxx',
            user_id='yida_pub_account'
        )
        try:
            await client.execute_platform_task_with_options_async(execute_platform_task_request, execute_platform_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\ExecutePlatformTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\ExecutePlatformTaskRequest;
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
        $executePlatformTaskHeaders = new ExecutePlatformTaskHeaders([]);
        $executePlatformTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $executePlatformTaskRequest = new ExecutePlatformTaskRequest([
            "outResult" => "agree",
            "noExecuteExpressions" => "y",
            "appType" => "APP_PBKT0xxx",
            "formDataJson" => "未知",
            "systemToken" => "hexxyyddd",
            "language" => "zh_CN",
            "remark" => "确认同意",
            "processInstanceId" => "f30233fb-72exxx",
            "userId" => "yida_pub_account"
        ]);
        try {
            $client->executePlatformTaskWithOptions($executePlatformTaskRequest, $executePlatformTaskHeaders, new RuntimeOptions([]));
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
  dingtalkyida_1_0  "github.com/alibabacloud-go/dingtalk/yida_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkyida_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_1_0.Client{}
  _result, _err = dingtalkyida_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  executePlatformTaskHeaders := &dingtalkyida_1_0.ExecutePlatformTaskHeaders{}
  executePlatformTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  executePlatformTaskRequest := &dingtalkyida_1_0.ExecutePlatformTaskRequest{
    OutResult: tea.String("agree"),
    NoExecuteExpressions: tea.String("y"),
    AppType: tea.String("APP_PBKT0xxx"),
    FormDataJson: tea.String("未知"),
    SystemToken: tea.String("hexxyyddd"),
    Language: tea.String("zh_CN"),
    Remark: tea.String("确认同意"),
    ProcessInstanceId: tea.String("f30233fb-72exxx"),
    UserId: tea.String("yida_pub_account"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ExecutePlatformTaskWithOptions(executePlatformTaskRequest, executePlatformTaskHeaders, &util.RuntimeOptions{})
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
import dingtalkyida_1_0, * as $dingtalkyida_1_0 from '@alicloud/dingtalk/yida_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkyida_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkyida_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let executePlatformTaskHeaders = new $dingtalkyida_1_0.ExecutePlatformTaskHeaders({ });
    executePlatformTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let executePlatformTaskRequest = new $dingtalkyida_1_0.ExecutePlatformTaskRequest({
      outResult: "agree",
      noExecuteExpressions: "y",
      appType: "APP_PBKT0xxx",
      formDataJson: "未知",
      systemToken: "hexxyyddd",
      language: "zh_CN",
      remark: "确认同意",
      processInstanceId: "f30233fb-72exxx",
      userId: "yida_pub_account",
    });
    try {
      await client.executePlatformTaskWithOptions(executePlatformTaskRequest, executePlatformTaskHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ExecutePlatformTaskHeaders executePlatformTaskHeaders = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ExecutePlatformTaskHeaders();
            executePlatformTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ExecutePlatformTaskRequest executePlatformTaskRequest = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.ExecutePlatformTaskRequest
            {
                OutResult = "agree",
                NoExecuteExpressions = "y",
                AppType = "APP_PBKT0xxx",
                FormDataJson = "未知",
                SystemToken = "hexxyyddd",
                Language = "zh_CN",
                Remark = "确认同意",
                ProcessInstanceId = "f30233fb-72exxx",
                UserId = "yida_pub_account",
            };
            try
            {
                client.ExecutePlatformTaskWithOptions(executePlatformTaskRequest, executePlatformTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkyida__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkyida_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkyida_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::Client> client = make_shared<Alibabacloud_Dingtalkyida_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::ExecutePlatformTaskHeaders> executePlatformTaskHeaders = make_shared<Alibabacloud_Dingtalkyida_1_0::ExecutePlatformTaskHeaders>();
  executePlatformTaskHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::ExecutePlatformTaskRequest> executePlatformTaskRequest = make_shared<Alibabacloud_Dingtalkyida_1_0::ExecutePlatformTaskRequest>(map<string, boost::any>({
    {"outResult", boost::any(string("agree"))},
    {"noExecuteExpressions", boost::any(string("y"))},
    {"appType", boost::any(string("APP_PBKT0xxx"))},
    {"formDataJson", boost::any(string("未知"))},
    {"systemToken", boost::any(string("hexxyyddd"))},
    {"language", boost::any(string("zh_CN"))},
    {"remark", boost::any(string("确认同意"))},
    {"processInstanceId", boost::any(string("f30233fb-72exxx"))},
    {"userId", boost::any(string("yida_pub_account"))}
  }));
  try {
    client->executePlatformTaskWithOptions(executePlatformTaskRequest, executePlatformTaskHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | unclassifiedError | 异常:%s | 通用异常信息 |
