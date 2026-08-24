---
title: "创建或更新项目概览中自定义字段值"
source_url: "https://open.dingtalk.com/document/development/create-or-update-field-values-project-overview"
namespace: "development"
slug: "create-or-update-field-values-project-overview"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 项目 > 创建或更新项目概览中自定义字段值"
doc_id: "e8IbsGTViU"
updated_at: "2026-06-04 19:11:38"
---

> Source: https://open.dingtalk.com/document/development/create-or-update-field-values-project-overview
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 项目 > 创建或更新项目概览中自定义字段值
> Updated: 2026-06-04 19:11:38

# 创建或更新项目概览中自定义字段值

调用本接口，创建或更新项目概览中自定义字段值。

## **接口调用说明**

- 如何创建自定义字段，详情参见[如何创建自定义字段](1258-teambition-faq.md#e9c81480d9dsf)。
- 如何添加概览，详情参见[如何添加项目概览](1258-teambition-faq.md#c1456a50d9h7s)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/project/users/{userId}/projects/{projectId}/customfields |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Project.Project.Write.All-项目应用项目写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 操作者userId。 |
| projectId | String | 是 | 项目ID，可通过调用[查询项目](1207-query-enterprise-all-projects.md)接口获取  。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| customFieldId | String | 否 | 自定义字段ID。 |
| customFieldName | String | 否 | 自定义字段名称(如果提供自定义字段ID 则忽略)。 |
| customFieldInstanceId | String | 否 | 自定义字段InstanceId(如果提供自定义字段ID 或者 自定义字段名称 则忽略)。 |
| value | Array | 是 | 字段值集合。 |
| customFieldValueId | String | 否 | 字段值id,当自定义字段是work类型该id表示文件id，当自定义字段是commongroup类型该id表示分类id，其他类型无意义。 |
| title | String | 否 | 字段值渲染值。 |
| metaString | String | 否 | 字段值元信息，json格式。 |

### 请求示例

HTTP

```
PUT /v1.0/project/users/0517xxx/projects/64ba333e4206372f3f5cxxxx/customfields HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "customfieldId" : "63a5301e420637003f5dxxxx",
  "customfieldName" : "项目进度",
  "customfieldInstanceId" : "64a5301e420637003f5dxxxx",
  "value" : [ {
    "fieldvalueId" : "63a5301e420637003f5dxxxx",
    "title" : "进行中",
    "metaString" : "{}"
  } ]
}
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
    public static com.aliyun.dingtalkproject_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkproject_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkproject_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkproject_1_0.models.CreateProjectCustomfieldStatusHeaders createProjectCustomfieldStatusHeaders = new com.aliyun.dingtalkproject_1_0.models.CreateProjectCustomfieldStatusHeaders();
        createProjectCustomfieldStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkproject_1_0.models.CreateProjectCustomfieldStatusRequest.CreateProjectCustomfieldStatusRequestValue value0 = new com.aliyun.dingtalkproject_1_0.models.CreateProjectCustomfieldStatusRequest.CreateProjectCustomfieldStatusRequestValue()
                .setFieldvalueId("63a5301e420637003f5dxxxx")
                .setTitle("进行中")
                .setMetaString("{}");
        com.aliyun.dingtalkproject_1_0.models.CreateProjectCustomfieldStatusRequest createProjectCustomfieldStatusRequest = new com.aliyun.dingtalkproject_1_0.models.CreateProjectCustomfieldStatusRequest()
                .setCustomfieldId("63a5301e420637003f5dxxxx")
                .setCustomfieldName("项目进度")
                .setCustomfieldInstanceId("64a5301e420637003f5dxxxx")
                .setValue(java.util.Arrays.asList(
                    value0
                ));
        try {
            client.createProjectCustomfieldStatusWithOptions("0517xxx", "64ba333e4206372f3f5cxxxx", createProjectCustomfieldStatusRequest, createProjectCustomfieldStatusHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.project_1_0.client import Client as dingtalkproject_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.project_1_0 import models as dingtalkproject__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkproject_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkproject_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_project_customfield_status_headers = dingtalkproject__1__0_models.CreateProjectCustomfieldStatusHeaders()
        create_project_customfield_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        value_0 = dingtalkproject__1__0_models.CreateProjectCustomfieldStatusRequestValue(
            fieldvalue_id='63a5301e420637003f5dxxxx',
            title='进行中',
            meta_string='{}'
        )
        create_project_customfield_status_request = dingtalkproject__1__0_models.CreateProjectCustomfieldStatusRequest(
            customfield_id='63a5301e420637003f5dxxxx',
            customfield_name='项目进度',
            customfield_instance_id='64a5301e420637003f5dxxxx',
            value=[
                value_0
            ]
        )
        try:
            client.create_project_customfield_status_with_options('0517xxx', '64ba333e4206372f3f5cxxxx', create_project_customfield_status_request, create_project_customfield_status_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_project_customfield_status_headers = dingtalkproject__1__0_models.CreateProjectCustomfieldStatusHeaders()
        create_project_customfield_status_headers.x_acs_dingtalk_access_token = '<your access token>'
        value_0 = dingtalkproject__1__0_models.CreateProjectCustomfieldStatusRequestValue(
            fieldvalue_id='63a5301e420637003f5dxxxx',
            title='进行中',
            meta_string='{}'
        )
        create_project_customfield_status_request = dingtalkproject__1__0_models.CreateProjectCustomfieldStatusRequest(
            customfield_id='63a5301e420637003f5dxxxx',
            customfield_name='项目进度',
            customfield_instance_id='64a5301e420637003f5dxxxx',
            value=[
                value_0
            ]
        )
        try:
            await client.create_project_customfield_status_with_options_async('0517xxx', '64ba333e4206372f3f5cxxxx', create_project_customfield_status_request, create_project_customfield_status_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateProjectCustomfieldStatusHeaders;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateProjectCustomfieldStatusRequest\value;
use AlibabaCloud\SDK\Dingtalk\Vproject_1_0\Models\CreateProjectCustomfieldStatusRequest;
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
        $createProjectCustomfieldStatusHeaders = new CreateProjectCustomfieldStatusHeaders([]);
        $createProjectCustomfieldStatusHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $value0 = new value([
            "fieldvalueId" => "63a5301e420637003f5dxxxx",
            "title" => "进行中",
            "metaString" => "{}"
        ]);
        $createProjectCustomfieldStatusRequest = new CreateProjectCustomfieldStatusRequest([
            "customfieldId" => "63a5301e420637003f5dxxxx",
            "customfieldName" => "项目进度",
            "customfieldInstanceId" => "64a5301e420637003f5dxxxx",
            "value" => [
                $value0
            ]
        ]);
        try {
            $client->createProjectCustomfieldStatusWithOptions("0517xxx", "64ba333e4206372f3f5cxxxx", $createProjectCustomfieldStatusRequest, $createProjectCustomfieldStatusHeaders, new RuntimeOptions([]));
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
  dingtalkproject_1_0  "github.com/alibabacloud-go/dingtalk/project_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkproject_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkproject_1_0.Client{}
  _result, _err = dingtalkproject_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createProjectCustomfieldStatusHeaders := &dingtalkproject_1_0.CreateProjectCustomfieldStatusHeaders{}
  createProjectCustomfieldStatusHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  value0 := &dingtalkproject_1_0.CreateProjectCustomfieldStatusRequestValue{
    FieldvalueId: tea.String("63a5301e420637003f5dxxxx"),
    Title: tea.String("进行中"),
    MetaString: tea.String("{}"),
  }
  createProjectCustomfieldStatusRequest := &dingtalkproject_1_0.CreateProjectCustomfieldStatusRequest{
    CustomfieldId: tea.String("63a5301e420637003f5dxxxx"),
    CustomfieldName: tea.String("项目进度"),
    CustomfieldInstanceId: tea.String("64a5301e420637003f5dxxxx"),
    Value: []*dingtalkproject_1_0.CreateProjectCustomfieldStatusRequestValue{value0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateProjectCustomfieldStatusWithOptions(tea.String("0517xxx"), tea.String("64ba333e4206372f3f5cxxxx"), createProjectCustomfieldStatusRequest, createProjectCustomfieldStatusHeaders, &util.RuntimeOptions{})
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
import dingtalkproject_1_0, * as $dingtalkproject_1_0 from '@alicloud/dingtalk/project_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkproject_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkproject_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createProjectCustomfieldStatusHeaders = new $dingtalkproject_1_0.CreateProjectCustomfieldStatusHeaders({ });
    createProjectCustomfieldStatusHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let value0 = new $dingtalkproject_1_0.CreateProjectCustomfieldStatusRequestValue({
      fieldvalueId: "63a5301e420637003f5dxxxx",
      title: "进行中",
      metaString: "{}",
    });
    let createProjectCustomfieldStatusRequest = new $dingtalkproject_1_0.CreateProjectCustomfieldStatusRequest({
      customfieldId: "63a5301e420637003f5dxxxx",
      customfieldName: "项目进度",
      customfieldInstanceId: "64a5301e420637003f5dxxxx",
      value: [
        value0
      ],
    });
    try {
      await client.createProjectCustomfieldStatusWithOptions("0517xxx", "64ba333e4206372f3f5cxxxx", createProjectCustomfieldStatusRequest, createProjectCustomfieldStatusHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkproject_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkproject_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkproject_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusHeaders createProjectCustomfieldStatusHeaders = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusHeaders();
            createProjectCustomfieldStatusHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusRequest.CreateProjectCustomfieldStatusRequestValue value0 = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusRequest.CreateProjectCustomfieldStatusRequestValue
            {
                FieldvalueId = "63a5301e420637003f5dxxxx",
                Title = "进行中",
                MetaString = "{}",
            };
            AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusRequest createProjectCustomfieldStatusRequest = new AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusRequest
            {
                CustomfieldId = "63a5301e420637003f5dxxxx",
                CustomfieldName = "项目进度",
                CustomfieldInstanceId = "64a5301e420637003f5dxxxx",
                Value = new List<AlibabaCloud.SDK.Dingtalkproject_1_0.Models.CreateProjectCustomfieldStatusRequest.CreateProjectCustomfieldStatusRequestValue>
                {
                    value0
                },
            };
            try
            {
                client.CreateProjectCustomfieldStatusWithOptions("0517xxx", "64ba333e4206372f3f5cxxxx", createProjectCustomfieldStatusRequest, createProjectCustomfieldStatusHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 结果。 |
| customFieldId | String | 自定义字段ID。 |
| originalId | String | 从企业选择的自定义字段ID。      如果是从企业选择的自定义字段ID，返回企业自定义字段ID，否则为空。 |
| name | String | 字段名称。 |
| type | String | 字段类型。 |
| advancedCustomFieldObjectType | String | 高级字段类型名(冗余)。 |
| value | Array | 字段值集合。 |
| customFieldValueId | String | 字段值id。 |
| title | String | 自定义字段值。 |
| metaString | String | 自定义字段值元属性。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "customfieldId" : "63a5301e420637003f5dxxxx",
    "originalId" : "62a5301e420637003f5dxxxx",
    "name" : "项目进度",
    "type" : "number",
    "advCfObjectType" : "lookup2",
    "value" : [ {
      "fieldvalueId" : "63a5301e420637003f5dxxxx",
      "title" : "13",
      "metaString" : "{}"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | user.not.exist | user not exist | 用户在当前企业中不存在。 |
| 400 | org.not.exist | org not exist | 当前企业在Teambition中不存在。 |
| 500 | server.error | system error | 系统内部服务错误 |
