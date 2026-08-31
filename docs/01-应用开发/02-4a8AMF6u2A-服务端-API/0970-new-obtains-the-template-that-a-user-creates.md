---
title: "获取用户创建的填表模板列表"
source_url: "https://open.dingtalk.com/document/development/new-obtains-the-template-that-a-user-creates"
namespace: "development"
slug: "new-obtains-the-template-that-a-user-creates"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能填表 > 获取用户创建的填表模板列表"
doc_id: "F6MybUWUYe"
updated_at: "2026-06-04 19:10:37"
---

> Source: https://open.dingtalk.com/document/development/new-obtains-the-template-that-a-user-creates
> Path: 应用开发 / 服务端 API / 智能填表 > 获取用户创建的填表模板列表
> Updated: 2026-06-04 19:10:37

# 获取用户创建的填表模板列表

用于获取用户创建的填表模板列表。

## 接口调用说明

目前智能填表目前仅支持查询旧版界面创建的表单数据，新版界面创建的表单无法查询。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/swform/users/forms |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_swapp\_collection\_read-智能填表数据读取权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| maxResults | Integer | 是 | 每页最大条目数，最大值200。 |
| bizType | Integer | 否 | 填表类型。   - **0**：表示通用填表 - **1**：表示教育版填表 |
| creator | String | 否 | 填表创建人userid。 |
| nextToken | Long | 是 | 分页游标。   - 如果是首次查询，该参数传0。 - 如果是非首次查询，该参数传上次调用时返回的nextToken值。 |

### 请求示例

HTTP

```
GET /v1.0/swform/users/forms?maxResults=10&bizType=0&creator=manager4220&nextToken=0 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:Be3xxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkswform_1_0.*;
import com.aliyun.dingtalkswform_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkswform_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkswform_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkswform_1_0.Client client = Sample.createClient();
        ListFormSchemasByCreatorHeaders listFormSchemasByCreatorHeaders = new ListFormSchemasByCreatorHeaders();
        listFormSchemasByCreatorHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListFormSchemasByCreatorRequest listFormSchemasByCreatorRequest = new ListFormSchemasByCreatorRequest()
                .setMaxResults(10)
                .setBizType(0)
                .setCreator("manager4220")
                .setNextToken(0L);
        try {
            client.listFormSchemasByCreatorWithOptions(listFormSchemasByCreatorRequest, listFormSchemasByCreatorHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.swform_1_0.client import Client as dingtalkswform_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.swform_1_0 import models as dingtalkswform__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkswform_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkswform_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_form_schemas_by_creator_headers = dingtalkswform__1__0_models.ListFormSchemasByCreatorHeaders()
        list_form_schemas_by_creator_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_form_schemas_by_creator_request = dingtalkswform__1__0_models.ListFormSchemasByCreatorRequest(
            max_results=10,
            biz_type=0,
            creator='manager4220',
            next_token=0
        )
        try:
            client.list_form_schemas_by_creator_with_options(list_form_schemas_by_creator_request, list_form_schemas_by_creator_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_form_schemas_by_creator_headers = dingtalkswform__1__0_models.ListFormSchemasByCreatorHeaders()
        list_form_schemas_by_creator_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_form_schemas_by_creator_request = dingtalkswform__1__0_models.ListFormSchemasByCreatorRequest(
            max_results=10,
            biz_type=0,
            creator='manager4220',
            next_token=0
        )
        try:
            await client.list_form_schemas_by_creator_with_options_async(list_form_schemas_by_creator_request, list_form_schemas_by_creator_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vswform_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vswform_1_0\Models\ListFormSchemasByCreatorHeaders;
use AlibabaCloud\SDK\Dingtalk\Vswform_1_0\Models\ListFormSchemasByCreatorRequest;
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
        $listFormSchemasByCreatorHeaders = new ListFormSchemasByCreatorHeaders([]);
        $listFormSchemasByCreatorHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listFormSchemasByCreatorRequest = new ListFormSchemasByCreatorRequest([
            "maxResults" => 10,
            "bizType" => 0,
            "creator" => "manager4220",
            "nextToken" => 0
        ]);
        try {
            $client->listFormSchemasByCreatorWithOptions($listFormSchemasByCreatorRequest, $listFormSchemasByCreatorHeaders, new RuntimeOptions([]));
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
  dingtalkswform_1_0  "github.com/alibabacloud-go/dingtalk/swform_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkswform_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkswform_1_0.Client{}
  _result, _err = dingtalkswform_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listFormSchemasByCreatorHeaders := &dingtalkswform_1_0.ListFormSchemasByCreatorHeaders{}
  listFormSchemasByCreatorHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listFormSchemasByCreatorRequest := &dingtalkswform_1_0.ListFormSchemasByCreatorRequest{
    MaxResults: tea.Int32(10),
    BizType: tea.Int32(0),
    Creator: tea.String("manager4220"),
    NextToken: tea.Int64(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListFormSchemasByCreatorWithOptions(listFormSchemasByCreatorRequest, listFormSchemasByCreatorHeaders, &util.RuntimeOptions{})
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
import dingtalkswform_1_0, * as $dingtalkswform_1_0 from '@alicloud/dingtalk/swform_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkswform_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkswform_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listFormSchemasByCreatorHeaders = new $dingtalkswform_1_0.ListFormSchemasByCreatorHeaders({ });
    listFormSchemasByCreatorHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listFormSchemasByCreatorRequest = new $dingtalkswform_1_0.ListFormSchemasByCreatorRequest({
      maxResults: 10,
      bizType: 0,
      creator: "manager4220",
      nextToken: 0,
    });
    try {
      await client.listFormSchemasByCreatorWithOptions(listFormSchemasByCreatorRequest, listFormSchemasByCreatorHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkswform_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkswform_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkswform_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkswform_1_0.Models.ListFormSchemasByCreatorHeaders listFormSchemasByCreatorHeaders = new AlibabaCloud.SDK.Dingtalkswform_1_0.Models.ListFormSchemasByCreatorHeaders();
            listFormSchemasByCreatorHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkswform_1_0.Models.ListFormSchemasByCreatorRequest listFormSchemasByCreatorRequest = new AlibabaCloud.SDK.Dingtalkswform_1_0.Models.ListFormSchemasByCreatorRequest
            {
                MaxResults = 10,
                BizType = 0,
                Creator = "manager4220",
                NextToken = 0,
            };
            try
            {
                client.ListFormSchemasByCreatorWithOptions(listFormSchemasByCreatorRequest, listFormSchemasByCreatorHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |
| result | Object | 返回结果。 |
| hasMore | Boolean | 是否有下一页数据。   - **true**：是 - **false**：否 |
| nextToken | Long | 分页游标。 |
| list | Array | 创建的表单模板列表。 |
| creator | String | 创建人userId。 |
| formCode | String | 填表code。 |
| name | String | 填表名称。 |
| memo | String | 填表提示。 |
| setting | Object | 表单设置信息。 |
| bizType | Integer | 填表类型。   - **0**：通用填表 - **1**：教育版填表 |
| createTime | String | 创建时间，iso8601格式，例如：2022-07-29T14:55Z。 |
| formType | Integer | 表单类型。   - **0**：一次性填表 - **1**：周期性填表 |
| stop | Boolean | 填表是否已终止。   - **true**：已经终止 - **false**：未终止 |
| loopTime | String | 周期性填表的提醒时间点。      一次性填表类型，不返回该字段。 |
| loopDays | Array of Integer | 填表周期，周一到周日分别用1-7表示。 |
| endTime | String | 填表截止时间，iso8601格式，例如：2022-07-29T14:55Z。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "hasMore" : true,
    "nextToken" : 10,
    "list" : [ {
      "creator" : "manager4220",
      "formCode" : "PROC-E5BD2166-B6F4-xxxx",
      "name" : "智能填表测试",
      "memo" : "请大家仔细填写，谢谢合作",
      "setting" : {
        "bizType" : 0,
        "createTime" : "2022-07-27T18:53Z",
        "formType" : 0,
        "stop" : true,
        "loopTime" : "18:00",
        "loopDays" : [ 1 ],
        "endTime" : "2022-07-27T18:53Z"
      }
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | swform.listFormSchemasByCreator.paramError | invalid biz\_type | 填表类型参数非法，当前仅支持0：通用智能填表 1：教育版填表 |
| 400 | swform.listFormSchemasByCreator.paramError | param invalid | 获取用户创建的填表模板列表参数异常 |
| 400 | swform.listFormSchemasByCreator.paramError | invalid offset | nextToken请求参数不合法 |
| 400 | swform.listFormSchemasByCreator.paramError | invalid size | maxResults请求参数不合法，最大支持200 |
| 400 | swform.listFormSchemasByCreator.paramError | app not exist | 应用不存在 |
| 400 | swform.listFormSchemasByCreator.paramError | app has been stoped | 应用已停用 |
| 400 | swform.listFormSchemasByCreator.paramError | getFormListByCreator fail | 获取用户创建的表单模板列表失败 |
| 500 | swform.listFormSchemasByCreator.sysError | swform.listFormInstances.sysError | 获取用户创建的填表模板列表系统异常 |
