---
title: "删除CRM自定义对象数据"
source_url: "https://open.dingtalk.com/document/development/delete-crm-custom-object-data"
namespace: "development"
slug: "delete-crm-custom-object-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 自定义对象 > 删除CRM自定义对象数据"
doc_id: "EmvpMXNXQx"
updated_at: "2025-10-09 18:06:19"
---

> Source: https://open.dingtalk.com/document/development/delete-crm-custom-object-data
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 自定义对象 > 删除CRM自定义对象数据
> Updated: 2025-10-09 18:06:19

# 删除CRM自定义对象数据

调用本接口，删除指定的自定义对象数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/customObjectDatas/instances/{instanceId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_write-维护CRM主数据的接口写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| instanceId | String | 是 | CRM自定义对象数据ID，可通过[根据指定条件查询自定义对象数据](1377-api-getobjectdata.md)接口获取instance\_id参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| formCode | String | 是 | 自定义对象表单code。    在客户管理应用的**客户管理管理后台**页面，进入表单编辑页面，在最下方可查看表单code。 |

### 请求示例

HTTP

```
DELETE /v1.0/crm/customObjectDatas/instances/INST_XX?formCode=PROC-EFxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c364097xxx
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
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataHeaders deleteCrmCustomObjectDataHeaders = new com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataHeaders();
        deleteCrmCustomObjectDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataRequest deleteCrmCustomObjectDataRequest = new com.aliyun.dingtalkcrm_1_0.models.DeleteCrmCustomObjectDataRequest()
                .setFormCode("PROC-EFxxxx");
        try {
            client.deleteCrmCustomObjectDataWithOptions("INST_XX", deleteCrmCustomObjectDataRequest, deleteCrmCustomObjectDataHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_crm_custom_object_data_headers = dingtalkcrm__1__0_models.DeleteCrmCustomObjectDataHeaders()
        delete_crm_custom_object_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_crm_custom_object_data_request = dingtalkcrm__1__0_models.DeleteCrmCustomObjectDataRequest(
            form_code='PROC-EFxxxx'
        )
        try:
            client.delete_crm_custom_object_data_with_options('INST_XX', delete_crm_custom_object_data_request, delete_crm_custom_object_data_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_crm_custom_object_data_headers = dingtalkcrm__1__0_models.DeleteCrmCustomObjectDataHeaders()
        delete_crm_custom_object_data_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_crm_custom_object_data_request = dingtalkcrm__1__0_models.DeleteCrmCustomObjectDataRequest(
            form_code='PROC-EFxxxx'
        )
        try:
            await client.delete_crm_custom_object_data_with_options_async('INST_XX', delete_crm_custom_object_data_request, delete_crm_custom_object_data_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\DeleteCrmCustomObjectDataHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\DeleteCrmCustomObjectDataRequest;
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
        $deleteCrmCustomObjectDataHeaders = new DeleteCrmCustomObjectDataHeaders([]);
        $deleteCrmCustomObjectDataHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteCrmCustomObjectDataRequest = new DeleteCrmCustomObjectDataRequest([
            "formCode" => "PROC-EFxxxx"
        ]);
        try {
            $client->deleteCrmCustomObjectDataWithOptions("INST_XX", $deleteCrmCustomObjectDataRequest, $deleteCrmCustomObjectDataHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteCrmCustomObjectDataHeaders := &dingtalkcrm_1_0.DeleteCrmCustomObjectDataHeaders{}
  deleteCrmCustomObjectDataHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteCrmCustomObjectDataRequest := &dingtalkcrm_1_0.DeleteCrmCustomObjectDataRequest{
    FormCode: tea.String("PROC-EFxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteCrmCustomObjectDataWithOptions(tea.String("INST_XX"), deleteCrmCustomObjectDataRequest, deleteCrmCustomObjectDataHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let deleteCrmCustomObjectDataHeaders = new $dingtalkcrm_1_0.DeleteCrmCustomObjectDataHeaders({ });
    deleteCrmCustomObjectDataHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deleteCrmCustomObjectDataRequest = new $dingtalkcrm_1_0.DeleteCrmCustomObjectDataRequest({
      formCode: "PROC-EFxxxx",
    });
    try {
      await client.deleteCrmCustomObjectDataWithOptions("INST_XX", deleteCrmCustomObjectDataRequest, deleteCrmCustomObjectDataHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DeleteCrmCustomObjectDataHeaders deleteCrmCustomObjectDataHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DeleteCrmCustomObjectDataHeaders();
            deleteCrmCustomObjectDataHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DeleteCrmCustomObjectDataRequest deleteCrmCustomObjectDataRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.DeleteCrmCustomObjectDataRequest
            {
                FormCode = "PROC-EFxxxx",
            };
            try
            {
                client.DeleteCrmCustomObjectDataWithOptions("INST_XX", deleteCrmCustomObjectDataRequest, deleteCrmCustomObjectDataHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| instanceId | String | 删除成功的CRM自定义对象数据ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "instanceId" : "INST_XX"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.frequent | request too frequent | 请求过于频繁 |
| 400 | systemError.appNotExists | %s | 应用不存在 |
| 400 | systemError.notPermittedAccess | %s | 无权限操作 |
| 400 | formCode.notExists | formCode not exists | formCode不存在 |
| 400 | daily.call.limit | daily call limit | 单日调用数量已达上限，请择日再次调用 |
| 500 | systemError | system error %s | 系统错误 |
