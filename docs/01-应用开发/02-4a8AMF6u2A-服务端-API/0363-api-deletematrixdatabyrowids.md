---
title: "批量删除指定矩阵的明细数据"
source_url: "https://open.dingtalk.com/document/development/api-deletematrixdatabyrowids"
namespace: "development"
slug: "api-deletematrixdatabyrowids"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 平台管理 > 批量删除指定矩阵的明细数据"
doc_id: "JUdhBuleo2"
updated_at: "2026-06-15 10:49:33"
---

> Source: https://open.dingtalk.com/document/development/api-deletematrixdatabyrowids
> Path: 应用开发 / 服务端 API / 宜搭 > 平台管理 > 批量删除指定矩阵的明细数据
> Updated: 2026-06-15 10:49:33

# 批量删除指定矩阵的明细数据

调用本接口，通过矩阵ID和行ID列表批量删除指定矩阵的明细数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/yida/forms/resources/matrices/remove |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Yida.PlatformResource.Write-宜搭平台资源写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| matrixId | String | 是 | 矩阵唯一标识，获取方式：平台管理-权限矩阵管理-权限矩阵ID。 |
| corpId | String | 是 | 组织的corpId。 |
| userId | String | 是 | 用户的userid。 |
| token | String | 是 | 验权token，校验方式如下：`md5(corpId + userId + code)`。md5取32位大写值。  **[!NOTE]**    每个企业有自己的唯一code。 |
| rowIds | String | 是 | 矩阵行数据rowId列表，多个以英文逗号分隔。 |

### **请求示例**

HTTP

```
POST /v2.0/yida/forms/resources/matrices/remove HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "matrixId" : "MATRIX-C8I4J40EM81XLWZH61ZK",
  "corpId" : "dingxxxx",
  "userId" : "manager123",
  "token" : "IASUDYxxx",
  "rowIds" : "row_123,row_456"
}
```

Java

```
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
    public static com.aliyun.dingtalkyida_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkyida_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkyida_2_0.models.DeleteMatrixDataByRowIdsHeaders deleteMatrixDataByRowIdsHeaders = new com.aliyun.dingtalkyida_2_0.models.DeleteMatrixDataByRowIdsHeaders();
        deleteMatrixDataByRowIdsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkyida_2_0.models.DeleteMatrixDataByRowIdsRequest deleteMatrixDataByRowIdsRequest = new com.aliyun.dingtalkyida_2_0.models.DeleteMatrixDataByRowIdsRequest();
        try {
            client.deleteMatrixDataByRowIdsWithOptions(deleteMatrixDataByRowIdsRequest, deleteMatrixDataByRowIdsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.yida_2_0.client import Client as dingtalkyida_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_2_0 import models as dingtalkyida__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_matrix_data_by_row_ids_headers = dingtalkyida__2__0_models.DeleteMatrixDataByRowIdsHeaders()
        delete_matrix_data_by_row_ids_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_matrix_data_by_row_ids_request = dingtalkyida__2__0_models.DeleteMatrixDataByRowIdsRequest()
        try:
            client.delete_matrix_data_by_row_ids_with_options(delete_matrix_data_by_row_ids_request, delete_matrix_data_by_row_ids_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_matrix_data_by_row_ids_headers = dingtalkyida__2__0_models.DeleteMatrixDataByRowIdsHeaders()
        delete_matrix_data_by_row_ids_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_matrix_data_by_row_ids_request = dingtalkyida__2__0_models.DeleteMatrixDataByRowIdsRequest()
        try:
            await client.delete_matrix_data_by_row_ids_with_options_async(delete_matrix_data_by_row_ids_request, delete_matrix_data_by_row_ids_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\DeleteMatrixDataByRowIdsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\DeleteMatrixDataByRowIdsRequest;
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
        $deleteMatrixDataByRowIdsHeaders = new DeleteMatrixDataByRowIdsHeaders([]);
        $deleteMatrixDataByRowIdsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteMatrixDataByRowIdsRequest = new DeleteMatrixDataByRowIdsRequest([]);
        try {
            $client->deleteMatrixDataByRowIdsWithOptions($deleteMatrixDataByRowIdsRequest, $deleteMatrixDataByRowIdsHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkyida_2_0  "github.com/alibabacloud-go/dingtalk/yida_2_0"
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
func CreateClient () (_result *dingtalkyida_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_2_0.Client{}
  _result, _err = dingtalkyida_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteMatrixDataByRowIdsHeaders := &dingtalkyida_2_0.DeleteMatrixDataByRowIdsHeaders{}
  deleteMatrixDataByRowIdsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteMatrixDataByRowIdsRequest := &dingtalkyida_2_0.DeleteMatrixDataByRowIdsRequest{}
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteMatrixDataByRowIdsWithOptions(deleteMatrixDataByRowIdsRequest, deleteMatrixDataByRowIdsHeaders, &util.RuntimeOptions{})
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
const dingtalkyida_2_0 = require('@alicloud/dingtalk/yida_2_0');
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
    return new dingtalkyida_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let deleteMatrixDataByRowIdsHeaders = new dingtalkyida_2_0.DeleteMatrixDataByRowIdsHeaders({ });
    deleteMatrixDataByRowIdsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let deleteMatrixDataByRowIdsRequest = new dingtalkyida_2_0.DeleteMatrixDataByRowIdsRequest({ });
    try {
      await client.deleteMatrixDataByRowIdsWithOptions(deleteMatrixDataByRowIdsRequest, deleteMatrixDataByRowIdsHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalkyida_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.DeleteMatrixDataByRowIdsHeaders deleteMatrixDataByRowIdsHeaders = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.DeleteMatrixDataByRowIdsHeaders();
            deleteMatrixDataByRowIdsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.DeleteMatrixDataByRowIdsRequest deleteMatrixDataByRowIdsRequest = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.DeleteMatrixDataByRowIdsRequest();
            try
            {
                client.DeleteMatrixDataByRowIdsWithOptions(deleteMatrixDataByRowIdsRequest, deleteMatrixDataByRowIdsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 接口调用是否成功。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": "1734xxxxxxe08500e",
  "request_id": "5kaikoe9uc8i"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | invalidState.matrix.matrixBeUsed | 该矩阵正在被使用，不能删除，请查看「使用详情」:%s | 该矩阵正在被使用，不能删除，请查看「使用详情」 |
| 500 | unclassifiedError | 宜搭未分类的异常信息:%s | 宜搭未分类的异常信息 |
| 500 | failure.user.userNotExist | 用户不存在:%s | 用户不存在 |
| 500 | invalidParameter.corp.corpNotExist | 企业不存在:%s | 企业不存在 |
| 500 | invalidState.authorization.invalidAuthorizationInformation | 无效的认证信息:%s | 无效的认证信息 |
| 500 | failure.operation.tooManyVisitors | 平台当前访问人数过多，请稍后重试:%s | 平台当前访问人数过多，请稍后重试 |
| 500 | invalidParameter.validation.parameterValidationFailed | 参数校验失败:%s | 参数校验失败 |
| 500 | noPermission.permission.deny | 没有权限:%s | 没有权限 |
| 500 | invalidState.matrix.matrixTableInfoInvalid | 矩阵表头校验异常，请检查表头设计:%s | 矩阵表头校验异常，请检查表头设计 |
| 500 | invalidState.matrix.matrixColumnsOverLimit | 超过矩阵列上限:%s | 超过矩阵列上限 |
| 500 | invalidState.matrix.matrixRowsOverLimit | 超过矩阵行数上限:%s | 超过矩阵行数上限 |
| 500 | invalidState.matrix.matrixNotExist | 数据不存在:%s | 数据不存在 |
