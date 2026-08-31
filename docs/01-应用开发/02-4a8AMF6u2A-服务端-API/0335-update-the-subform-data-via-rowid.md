---
title: "通过RowId更新子表单数据"
source_url: "https://open.dingtalk.com/document/development/update-the-subform-data-via-rowid"
namespace: "development"
slug: "update-the-subform-data-via-rowid"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 表单 > 通过RowId更新子表单数据"
doc_id: "9sdVvgbYhF"
updated_at: "2026-06-15 10:53:00"
---

> Source: https://open.dingtalk.com/document/development/update-the-subform-data-via-rowid
> Path: 应用开发 / 服务端 API / 宜搭 > 表单 > 通过RowId更新子表单数据
> Updated: 2026-06-15 10:53:00

# 通过RowId更新子表单数据

调用本接口，根据RowId更新子表单数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/yida/forms/updateSubTableByRowId |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Yida.Form.Write-宜搭表单数据写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| updateSubTableDataJson | String | 是 | 用于更新子表单实例的数据，输入为数组格式：   - **key**：组件标识，宜搭表单编辑页面，高级设置中查看。 - **value**：组件内的值。 |
| systemToken | String | 是 | 宜搭应用密钥。 |
| formInstanceId | String | 是 | 表单实例id。 |
| userId | String | 是 | 用户的userId，可调用[获取部门用户基础信息](0066-queries-the-simple-information-of-a-department-user.md)接口获取用户userId。 |
| appType | String | 是 | 宜搭应用唯一标识。 |
| useLatestFormSchemaVersion | Boolean | 否 | 是否使用最新的表单版本。  **[!NOTE]**    默认为不使用 |
| tableFieldId | String | 是 | 子表ID。 |
| useAlias | Boolean | 否 | 是否使用组件别名。  **[!NOTE]**    开启之后，入参`updateSubTableDataJson`中组件id支持以别名形式传入。 |
| formUuid | String | 否 | 表单ID。 |

### **请求示例**

HTTP

```
POST /v2.0/yida/forms/updateSubTableByRowId HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "updateSubTableDataJson" : "[{\"textField_md2x1jow\":\"更新子表通过rowId\",\"textareaField_md2x1jox\":\"更新子表通过rowId\",\"rowId\":\"xxxxxxxxxxxxxxxx\"},{\"textField_md2x1jow\":\"更新子表通过rowId\",\"textareaField_md2x1jox\":\"更新子表通过rowId\",\"rowId\":\"xxxxxxxxxxxxxxxx\"}]",
  "systemToken" : "098xxxxWK7",
  "formInstanceId" : "FINST-Jxxxx24",
  "userId" : "dixxxx2232",
  "appType" : "APPxxxx",
  "useLatestFormSchemaVersion" : false,
  "tableFieldId" : "textField_xxxxjow",
  "useAlias" : false,
  "formUuid" : "FORM-8Exxxx21A"
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
        com.aliyun.dingtalkyida_2_0.models.UpdateSubTableByRowIdHeaders updateSubTableByRowIdHeaders = new com.aliyun.dingtalkyida_2_0.models.UpdateSubTableByRowIdHeaders();
        updateSubTableByRowIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkyida_2_0.models.UpdateSubTableByRowIdRequest updateSubTableByRowIdRequest = new com.aliyun.dingtalkyida_2_0.models.UpdateSubTableByRowIdRequest();
        try {
            client.updateSubTableByRowIdWithOptions(updateSubTableByRowIdRequest, updateSubTableByRowIdHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_sub_table_by_row_id_headers = dingtalkyida__2__0_models.UpdateSubTableByRowIdHeaders()
        update_sub_table_by_row_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_sub_table_by_row_id_request = dingtalkyida__2__0_models.UpdateSubTableByRowIdRequest()
        try:
            client.update_sub_table_by_row_id_with_options(update_sub_table_by_row_id_request, update_sub_table_by_row_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_sub_table_by_row_id_headers = dingtalkyida__2__0_models.UpdateSubTableByRowIdHeaders()
        update_sub_table_by_row_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_sub_table_by_row_id_request = dingtalkyida__2__0_models.UpdateSubTableByRowIdRequest()
        try:
            await client.update_sub_table_by_row_id_with_options_async(update_sub_table_by_row_id_request, update_sub_table_by_row_id_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\UpdateSubTableByRowIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_2_0\Models\UpdateSubTableByRowIdRequest;
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
        $updateSubTableByRowIdHeaders = new UpdateSubTableByRowIdHeaders([]);
        $updateSubTableByRowIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateSubTableByRowIdRequest = new UpdateSubTableByRowIdRequest([]);
        try {
            $client->updateSubTableByRowIdWithOptions($updateSubTableByRowIdRequest, $updateSubTableByRowIdHeaders, new RuntimeOptions([]));
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

  updateSubTableByRowIdHeaders := &dingtalkyida_2_0.UpdateSubTableByRowIdHeaders{}
  updateSubTableByRowIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateSubTableByRowIdRequest := &dingtalkyida_2_0.UpdateSubTableByRowIdRequest{}
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateSubTableByRowIdWithOptions(updateSubTableByRowIdRequest, updateSubTableByRowIdHeaders, &util.RuntimeOptions{})
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
    let updateSubTableByRowIdHeaders = new dingtalkyida_2_0.UpdateSubTableByRowIdHeaders({ });
    updateSubTableByRowIdHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateSubTableByRowIdRequest = new dingtalkyida_2_0.UpdateSubTableByRowIdRequest({ });
    try {
      await client.updateSubTableByRowIdWithOptions(updateSubTableByRowIdRequest, updateSubTableByRowIdHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateSubTableByRowIdHeaders updateSubTableByRowIdHeaders = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateSubTableByRowIdHeaders();
            updateSubTableByRowIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateSubTableByRowIdRequest updateSubTableByRowIdRequest = new AlibabaCloud.SDK.Dingtalkyida_2_0.Models.UpdateSubTableByRowIdRequest();
            try
            {
                client.UpdateSubTableByRowIdWithOptions(updateSubTableByRowIdRequest, updateSubTableByRowIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新结果。   - **true**：更新成功 - **false**：更新失败 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | invalidState.role.roleNotExist | 角色不存在:%s | 角色不存在 |
| 500 | unclassifiedError | 宜搭未分类的异常信息:%s | 宜搭未分类的异常信息 |
| 500 | failure.user.userNotExist | 用户不存在:%s | 用户不存在 |
| 500 | invalidParameter.corp.corpNotExist | 企业不存在:%s | 企业不存在 |
| 500 | invalidState.authorization.invalidAuthorizationInformation | 无效的认证信息:%s | 无效的认证信息 |
| 500 | failure.operation.tooManyVisitors | 平台当前访问人数过多，请稍后重试:%s | 平台当前访问人数过多，请稍后重试 |
| 500 | invalidParameter.validation.parameterValidationFailed | 参数校验失败:%s | 参数校验失败 |
| 500 | noPermission.permission.deny | 没有权限:%s | 没有权限 |
