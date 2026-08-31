---
title: "查询花名册中有权限的字段列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-fields-with-permissions-in-the-roster"
namespace: "development"
slug: "query-the-list-of-fields-with-permissions-in-the-roster"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 花名册 > 查询花名册中有权限的字段列表"
doc_id: "ShGePqnuem"
updated_at: "2026-06-04 19:10:25"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-fields-with-permissions-in-the-roster
> Path: 应用开发 / 服务端 API / 智能人事 > 花名册 > 查询花名册中有权限的字段列表
> Updated: 2026-06-04 19:10:25

# 查询花名册中有权限的字段列表

调用本接口，产品方案商查询花名册的员工档案信息中有权限的字段列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/rosters/meta/authorities/fields |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appAgentId | Long | 是 | 应用的agentId，可调用获取[获取企业授权信息](0042-obtains-the-basic-information-of-an-enterprise.md)接口获取agentId参数值。 |

### 请求示例

HTTP

```
GET /v1.0/hrm/rosters/meta/authorities/fields?appAgentId=12345 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.RosterMetaAvailableFieldListHeaders rosterMetaAvailableFieldListHeaders = new com.aliyun.dingtalkhrm_1_0.models.RosterMetaAvailableFieldListHeaders();
        rosterMetaAvailableFieldListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.RosterMetaAvailableFieldListRequest rosterMetaAvailableFieldListRequest = new com.aliyun.dingtalkhrm_1_0.models.RosterMetaAvailableFieldListRequest()
                .setAppAgentId(12345L);
        try {
            client.rosterMetaAvailableFieldListWithOptions(rosterMetaAvailableFieldListRequest, rosterMetaAvailableFieldListHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        roster_meta_available_field_list_headers = dingtalkhrm__1__0_models.RosterMetaAvailableFieldListHeaders()
        roster_meta_available_field_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        roster_meta_available_field_list_request = dingtalkhrm__1__0_models.RosterMetaAvailableFieldListRequest(
            app_agent_id=12345
        )
        try:
            client.roster_meta_available_field_list_with_options(roster_meta_available_field_list_request, roster_meta_available_field_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        roster_meta_available_field_list_headers = dingtalkhrm__1__0_models.RosterMetaAvailableFieldListHeaders()
        roster_meta_available_field_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        roster_meta_available_field_list_request = dingtalkhrm__1__0_models.RosterMetaAvailableFieldListRequest(
            app_agent_id=12345
        )
        try:
            await client.roster_meta_available_field_list_with_options_async(roster_meta_available_field_list_request, roster_meta_available_field_list_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\RosterMetaAvailableFieldListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\RosterMetaAvailableFieldListRequest;
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
        $rosterMetaAvailableFieldListHeaders = new RosterMetaAvailableFieldListHeaders([]);
        $rosterMetaAvailableFieldListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $rosterMetaAvailableFieldListRequest = new RosterMetaAvailableFieldListRequest([
            "appAgentId" => 12345
        ]);
        try {
            $client->rosterMetaAvailableFieldListWithOptions($rosterMetaAvailableFieldListRequest, $rosterMetaAvailableFieldListHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  rosterMetaAvailableFieldListHeaders := &dingtalkhrm_1_0.RosterMetaAvailableFieldListHeaders{}
  rosterMetaAvailableFieldListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  rosterMetaAvailableFieldListRequest := &dingtalkhrm_1_0.RosterMetaAvailableFieldListRequest{
    AppAgentId: tea.Int64(12345),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RosterMetaAvailableFieldListWithOptions(rosterMetaAvailableFieldListRequest, rosterMetaAvailableFieldListHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let rosterMetaAvailableFieldListHeaders = new $dingtalkhrm_1_0.RosterMetaAvailableFieldListHeaders({ });
    rosterMetaAvailableFieldListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let rosterMetaAvailableFieldListRequest = new $dingtalkhrm_1_0.RosterMetaAvailableFieldListRequest({
      appAgentId: 12345,
    });
    try {
      await client.rosterMetaAvailableFieldListWithOptions(rosterMetaAvailableFieldListRequest, rosterMetaAvailableFieldListHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaAvailableFieldListHeaders rosterMetaAvailableFieldListHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaAvailableFieldListHeaders();
            rosterMetaAvailableFieldListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaAvailableFieldListRequest rosterMetaAvailableFieldListRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaAvailableFieldListRequest
            {
                AppAgentId = 12345,
            };
            try
            {
                client.RosterMetaAvailableFieldListWithOptions(rosterMetaAvailableFieldListRequest, rosterMetaAvailableFieldListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 结果列表。  **[!NOTE]**  由于个人信息安全限制，产品方案商在获取授权企业内员工的花名册信息时，无法获取全部的字段值。 |
| fieldCode | String | 字段标识。 |
| fieldName | String | 字段名称。 |
| fieldType | String | 字段类型。   - **TextField**：文本类型 - **DDPhotoField**：附件类型 - **DDSelectField**：选项类型 - **DDDateField**：时间类型 |
| optionText | String | 字段的选项内容， 只有是选项类型的字段才会有值 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "fieldCode" : "sys01-employeeType",
    "fieldName" : "员工类型",
    "fieldType" : "DDSelectField"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | invalidAgentId | agentId错误 | agentId错误 |
