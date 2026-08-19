---
title: "获取审批中创建与CRM客户关联的TAB表单元数据"
source_url: "https://open.dingtalk.com/document/development/api-getrelatedviewtabmeta"
namespace: "development"
slug: "api-getrelatedviewtabmeta"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 获取审批中创建与CRM客户关联的TAB表单元数据"
doc_id: "3nHvbYlut9"
updated_at: "2025-10-09 18:06:12"
---

> Source: https://open.dingtalk.com/document/development/api-getrelatedviewtabmeta
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户 > 获取审批中创建与CRM客户关联的TAB表单元数据
> Updated: 2025-10-09 18:06:12

# 获取审批中创建与CRM客户关联的TAB表单元数据

调用本接口，获取OA审批里创建的与CRM客户关联的tab表单元数据，包括表单标题、关联的联系人控件id。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/formRelatedTabs/meta/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_customdata\_read-获取CRM自定义对象数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| formCode | String | 是 | 个人客户或者企业客户的表单代码 。 |
| viewUserId | String | 是 | 企业内的用户 userid。 |

### 请求示例

HTTP

```
POST /v1.0/crm/formRelatedTabs/meta/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6765b981bd6c381ba3374a0bef0ba76d
Content-Type:application/json

{
  "formCode" : "PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568",
  "viewUserId" : "manager6034"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcrm_1_0.models.GetRelatedViewTabMetaHeaders getRelatedViewTabMetaHeaders = new com.aliyun.dingtalkcrm_1_0.models.GetRelatedViewTabMetaHeaders();
        getRelatedViewTabMetaHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.GetRelatedViewTabMetaRequest getRelatedViewTabMetaRequest = new com.aliyun.dingtalkcrm_1_0.models.GetRelatedViewTabMetaRequest()
                .setFormCode("PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568")
                .setViewUserId("manager6034");
        try {
            client.getRelatedViewTabMetaWithOptions(getRelatedViewTabMetaRequest, getRelatedViewTabMetaHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_related_view_tab_meta_headers = dingtalkcrm__1__0_models.GetRelatedViewTabMetaHeaders()
        get_related_view_tab_meta_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_related_view_tab_meta_request = dingtalkcrm__1__0_models.GetRelatedViewTabMetaRequest(
            form_code='PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568',
            view_user_id='manager6034'
        )
        try:
            client.get_related_view_tab_meta_with_options(get_related_view_tab_meta_request, get_related_view_tab_meta_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_related_view_tab_meta_headers = dingtalkcrm__1__0_models.GetRelatedViewTabMetaHeaders()
        get_related_view_tab_meta_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_related_view_tab_meta_request = dingtalkcrm__1__0_models.GetRelatedViewTabMetaRequest(
            form_code='PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568',
            view_user_id='manager6034'
        )
        try:
            await client.get_related_view_tab_meta_with_options_async(get_related_view_tab_meta_request, get_related_view_tab_meta_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetRelatedViewTabMetaHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetRelatedViewTabMetaRequest;
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
        $getRelatedViewTabMetaHeaders = new GetRelatedViewTabMetaHeaders([]);
        $getRelatedViewTabMetaHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getRelatedViewTabMetaRequest = new GetRelatedViewTabMetaRequest([
            "formCode" => "PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568",
            "viewUserId" => "manager6034"
        ]);
        try {
            $client->getRelatedViewTabMetaWithOptions($getRelatedViewTabMetaRequest, $getRelatedViewTabMetaHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
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

  getRelatedViewTabMetaHeaders := &dingtalkcrm_1_0.GetRelatedViewTabMetaHeaders{}
  getRelatedViewTabMetaHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getRelatedViewTabMetaRequest := &dingtalkcrm_1_0.GetRelatedViewTabMetaRequest{
    FormCode: tea.String("PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568"),
    ViewUserId: tea.String("manager6034"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetRelatedViewTabMetaWithOptions(getRelatedViewTabMetaRequest, getRelatedViewTabMetaHeaders, &util.RuntimeOptions{})
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
const dingtalkcrm_1_0 = require('@alicloud/dingtalk/crm_1_0');
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
    return new dingtalkcrm_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getRelatedViewTabMetaHeaders = new dingtalkcrm_1_0.GetRelatedViewTabMetaHeaders({ });
    getRelatedViewTabMetaHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getRelatedViewTabMetaRequest = new dingtalkcrm_1_0.GetRelatedViewTabMetaRequest({
      formCode: 'PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568',
      viewUserId: 'manager6034',
    });
    try {
      await client.getRelatedViewTabMetaWithOptions(getRelatedViewTabMetaRequest, getRelatedViewTabMetaHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetRelatedViewTabMetaHeaders getRelatedViewTabMetaHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetRelatedViewTabMetaHeaders();
            getRelatedViewTabMetaHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetRelatedViewTabMetaRequest getRelatedViewTabMetaRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetRelatedViewTabMetaRequest
            {
                FormCode = "PROC-CE6BDC9A-701A-4C41-B9CE-6D614DB80568",
                ViewUserId = "manager6034",
            };
            try
            {
                client.GetRelatedViewTabMetaWithOptions(getRelatedViewTabMetaRequest, getRelatedViewTabMetaHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| results | Array | 返回结果列表。 |
| formCode | String | 表单代码。 |
| relateComponentId | String | 相关联的组件id。 |
| tabTitle | String | tab的标题。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "results" : [ {
    "formCode" : "PROC-4EFE895D-A291-4A65-9FD6-99431604DF67",
    "relateComponentId" : "OpenDataField_K99RPMMRGJ40",
    "tabTitle" : "212"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.isNull | request请求参数为空 | request请求参数未传递空 |
| 401 | sys.error | 系统错误 | 系统错误 |
| 402 | params.isNull | corpId或者viewUserId为空 | corpId或者viewUserId为空 |
| 403 | crm.not.created | crm应用未安装 | crm应用未安装 |
