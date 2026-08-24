---
title: "获取当前企业所有可管理的表单"
source_url: "https://open.dingtalk.com/document/development/get-all-manageable-forms-for-the-current-enterprise"
namespace: "development"
slug: "get-all-manageable-forms-for-the-current-enterprise"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批表单 > 获取当前企业所有可管理的表单"
doc_id: "v7nE41k4cZ"
updated_at: "2026-06-03 10:12:24"
---

> Source: https://open.dingtalk.com/document/development/get-all-manageable-forms-for-the-current-enterprise
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批表单 > 获取当前企业所有可管理的表单
> Updated: 2026-06-03 10:12:24

# 获取当前企业所有可管理的表单

调用本接口，获取用户在当前企业所有可管理的审批表单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processes/managements/templates |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workflow.Form.Read-工作流模板读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户的userId。  **[!NOTE]**  userId对应的人员必须拥有该企业OA审批的权限。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/processes/managements/templates?userId=manager7078 HTTP/1.1
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
        com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdHeaders getManageProcessByStaffIdHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdHeaders();
        getManageProcessByStaffIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdRequest getManageProcessByStaffIdRequest = new com.aliyun.dingtalkworkflow_1_0.models.GetManageProcessByStaffIdRequest()
                .setUserId("manager7078");
        try {
            client.getManageProcessByStaffIdWithOptions(getManageProcessByStaffIdRequest, getManageProcessByStaffIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_manage_process_by_staff_id_headers = dingtalkworkflow__1__0_models.GetManageProcessByStaffIdHeaders()
        get_manage_process_by_staff_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_manage_process_by_staff_id_request = dingtalkworkflow__1__0_models.GetManageProcessByStaffIdRequest(
            user_id='manager7078'
        )
        try:
            client.get_manage_process_by_staff_id_with_options(get_manage_process_by_staff_id_request, get_manage_process_by_staff_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_manage_process_by_staff_id_headers = dingtalkworkflow__1__0_models.GetManageProcessByStaffIdHeaders()
        get_manage_process_by_staff_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_manage_process_by_staff_id_request = dingtalkworkflow__1__0_models.GetManageProcessByStaffIdRequest(
            user_id='manager7078'
        )
        try:
            await client.get_manage_process_by_staff_id_with_options_async(get_manage_process_by_staff_id_request, get_manage_process_by_staff_id_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetManageProcessByStaffIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GetManageProcessByStaffIdRequest;
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
        $getManageProcessByStaffIdHeaders = new GetManageProcessByStaffIdHeaders([]);
        $getManageProcessByStaffIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getManageProcessByStaffIdRequest = new GetManageProcessByStaffIdRequest([
            "userId" => "manager7078"
        ]);
        try {
            $client->getManageProcessByStaffIdWithOptions($getManageProcessByStaffIdRequest, $getManageProcessByStaffIdHeaders, new RuntimeOptions([]));
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

  getManageProcessByStaffIdHeaders := &dingtalkworkflow_1_0.GetManageProcessByStaffIdHeaders{}
  getManageProcessByStaffIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getManageProcessByStaffIdRequest := &dingtalkworkflow_1_0.GetManageProcessByStaffIdRequest{
    UserId: tea.String("manager7078"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetManageProcessByStaffIdWithOptions(getManageProcessByStaffIdRequest, getManageProcessByStaffIdHeaders, &util.RuntimeOptions{})
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
    let getManageProcessByStaffIdHeaders = new $dingtalkworkflow_1_0.GetManageProcessByStaffIdHeaders({ });
    getManageProcessByStaffIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getManageProcessByStaffIdRequest = new $dingtalkworkflow_1_0.GetManageProcessByStaffIdRequest({
      userId: "manager7078",
    });
    try {
      await client.getManageProcessByStaffIdWithOptions(getManageProcessByStaffIdRequest, getManageProcessByStaffIdHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetManageProcessByStaffIdHeaders getManageProcessByStaffIdHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetManageProcessByStaffIdHeaders();
            getManageProcessByStaffIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetManageProcessByStaffIdRequest getManageProcessByStaffIdRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GetManageProcessByStaffIdRequest
            {
                UserId = "manager7078",
            };
            try
            {
                client.GetManageProcessByStaffIdWithOptions(getManageProcessByStaffIdRequest, getManageProcessByStaffIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 模板列表。 |
| iconName | String | 模板图标名。 |
| flowTitle | String | 模板名称。 |
| processCode | String | 模板code。 |
| newProcess | Boolean | 是否为新模板。   - **true**：是 - **false**：不是 |
| gmtModified | String | 修改时间。 |
| attendanceType | Integer | 关联考勤类型，取值。   - **0**：无 - **1**：补卡申请 - **2**：请假 |
| iconUrl | String | 图标URL地址。 |
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "iconName" : "common",
    "flowTitle" : "通用审批",
    "processCode" : "PROC-44E84FC1-16E2-4A69-BB3C-xxxx",
    "newProcess" : true,
    "gmtModified" : "2022-08-23T17:09Z",
    "attendanceType" : 0,
    "iconUrl" : "https://gw.alicdn.com/tfs/xxxx-112-112.png"
  } ],
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidUserId | 获取当前企业所有可管理的表单，要查询的用户userId不能为空 | 获取当前企业所有可管理的表单，要查询的用户userId不能为空 |
| 400 | invalidParameter | 获取当前企业所有可管理的表单参数错误 | 获取当前企业所有可管理的表单参数错误 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
