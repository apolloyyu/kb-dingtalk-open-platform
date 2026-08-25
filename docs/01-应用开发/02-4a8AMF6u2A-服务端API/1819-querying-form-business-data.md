---
title: "查询表单业务数据列表"
source_url: "https://open.dingtalk.com/document/development/querying-form-business-data"
namespace: "development"
slug: "querying-form-business-data"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 氚云 > 表单 > 查询表单业务数据列表"
doc_id: "f7pbxiDj1D"
updated_at: "2025-09-08 19:06:21"
---

> Source: https://open.dingtalk.com/document/development/querying-form-business-data
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 氚云 > 表单 > 查询表单业务数据列表
> Updated: 2025-09-08 19:06:21

# 查询表单业务数据列表

调用本接口查询表单业务数据实例集合。

> **[!IMPORTANT]**
>
> 为了更进一步提升接口质量以及用户体验，我们对本接口文档做出如下调整：
>
> - 自 2024 年 8 月 1 日起，本接口文档将会被迁移至历史文档目录。
> - 氚云接口不再支持新应用接入，已接入应用可继续使用，后续若需要接入氚云接口，请使用[氚云开发者手册](https://help.h3yun.com/channels/899.html)。

![](https://img.alicdn.com/imgextra/i4/O1CN01kueFjM1keJPPNlCcV_!!6000000004708-2-tps-1080-369.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=h3yun_1.0%23LoadBizObjects) |
| 第三方企业应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=h3yun_1.0%23LoadBizObjects) |
| 第三方个人应用 | 暂不支持 | 氚云数据管理权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/h3yun/forms/instances/search HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "schemaCode" : "String",
  "pageNumber" : Integer,
  "pageSize" : Integer,
  "returnFields" : [ "String" ],
  "sortByFields" : [ {
    "fieldName" : "String",
    "direction" : "String"
  } ],
  "matcherJson" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| schemaCode | String | 是 | 表单编码。 |
| pageNumber | Integer | 是 | 分页页码。 |
| pageSize | Integer | 是 | 分页页大小，最大值500。 |
| returnFields | Array of String | 否 | 需要返回的字段名，仅支持传入主表的字段。 |
| sortByFields | Array | 否 | 排序字段结构列表。 |
| fieldName | String | 否 | 排序字段名。 |
| direction | String | 否 | 排序方向，取值：   - **Ascending**：升序 - **Descending**：降序 |
| matcherJson | String | 否 | json格式的动态条件过滤器。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 状态码。 |
| message | String | 状态码描述。 |
| data | Object | 返回结果。 |
| pageNumber | Integer | 分页页码。 |
| pageSize | Integer | 分页参数，每页显示条数。 |
| totalCount | Integer | 匹配条件的结果总数量。 |
| bizObjects | Array of Object | 业务对象实例。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/h3yun/forms/instances/search HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bef2c8xxx
Content-Type:application/json

{
  "schemaCode" : "D000183b4xxx",
  "pageNumber" : 1,
  "pageSize" : 10,
  "returnFields" : [ "Name" ],
  "sortByFields" : [ {
    "fieldName" : "Age",
    "direction" : "Ascending"
  } ],
  "matcherJson" : "{ \"Type\": \"Item\", \"Name\": \"F0000010\", \"Operator\": 2, \"Value\": \"0000007\" }"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkh3yun_1_0.*;
import com.aliyun.dingtalkh3yun_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkh3yun_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkh3yun_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkh3yun_1_0.Client client = Sample.createClient();
        LoadBizObjectsHeaders loadBizObjectsHeaders = new LoadBizObjectsHeaders();
        loadBizObjectsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        LoadBizObjectsRequest.LoadBizObjectsRequestSortByFields sortByFields0 = new LoadBizObjectsRequest.LoadBizObjectsRequestSortByFields()
                .setFieldName("Age")
                .setDirection("Ascending");
        LoadBizObjectsRequest loadBizObjectsRequest = new LoadBizObjectsRequest()
                .setSchemaCode("D000183b4xxx")
                .setPageNumber(1)
                .setPageSize(10)
                .setReturnFields(java.util.Arrays.asList(
                    "Name"
                ))
                .setSortByFields(java.util.Arrays.asList(
                    sortByFields0
                ))
                .setMatcherJson("{ \"Type\": \"Item\", \"Name\": \"F0000010\", \"Operator\": 2, \"Value\": \"0000007\" }");
        try {
            client.loadBizObjectsWithOptions(loadBizObjectsRequest, loadBizObjectsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.h3yun_1_0.client import Client as dingtalkh3yun_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.h3yun_1_0 import models as dingtalkh_3yun__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkh3yun_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkh3yun_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        load_biz_objects_headers = dingtalkh_3yun__1__0_models.LoadBizObjectsHeaders()
        load_biz_objects_headers.x_acs_dingtalk_access_token = '<your access token>'
        sort_by_fields_0 = dingtalkh_3yun__1__0_models.LoadBizObjectsRequestSortByFields(
            field_name='Age',
            direction='Ascending'
        )
        load_biz_objects_request = dingtalkh_3yun__1__0_models.LoadBizObjectsRequest(
            schema_code='D000183b4xxx',
            page_number=1,
            page_size=10,
            return_fields=[
                'Name'
            ],
            sort_by_fields=[
                sort_by_fields_0
            ],
            matcher_json='{ "Type": "Item", "Name": "F0000010", "Operator": 2, "Value": "0000007" }'
        )
        try:
            client.load_biz_objects_with_options(load_biz_objects_request, load_biz_objects_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        load_biz_objects_headers = dingtalkh_3yun__1__0_models.LoadBizObjectsHeaders()
        load_biz_objects_headers.x_acs_dingtalk_access_token = '<your access token>'
        sort_by_fields_0 = dingtalkh_3yun__1__0_models.LoadBizObjectsRequestSortByFields(
            field_name='Age',
            direction='Ascending'
        )
        load_biz_objects_request = dingtalkh_3yun__1__0_models.LoadBizObjectsRequest(
            schema_code='D000183b4xxx',
            page_number=1,
            page_size=10,
            return_fields=[
                'Name'
            ],
            sort_by_fields=[
                sort_by_fields_0
            ],
            matcher_json='{ "Type": "Item", "Name": "F0000010", "Operator": 2, "Value": "0000007" }'
        )
        try:
            await client.load_biz_objects_with_options_async(load_biz_objects_request, load_biz_objects_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\LoadBizObjectsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\LoadBizObjectsRequest\sortByFields;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\LoadBizObjectsRequest;
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
        $loadBizObjectsHeaders = new LoadBizObjectsHeaders([]);
        $loadBizObjectsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sortByFields0 = new sortByFields([
            "fieldName" => "Age",
            "direction" => "Ascending"
        ]);
        $loadBizObjectsRequest = new LoadBizObjectsRequest([
            "schemaCode" => "D000183b4xxx",
            "pageNumber" => 1,
            "pageSize" => 10,
            "returnFields" => [
                "Name"
            ],
            "sortByFields" => [
                $sortByFields0
            ],
            "matcherJson" => "{ \"Type\": \"Item\", \"Name\": \"F0000010\", \"Operator\": 2, \"Value\": \"0000007\" }"
        ]);
        try {
            $client->loadBizObjectsWithOptions($loadBizObjectsRequest, $loadBizObjectsHeaders, new RuntimeOptions([]));
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
  dingtalkh3yun_1_0  "github.com/alibabacloud-go/dingtalk/h3yun_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkh3yun_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkh3yun_1_0.Client{}
  _result, _err = dingtalkh3yun_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  loadBizObjectsHeaders := &dingtalkh3yun_1_0.LoadBizObjectsHeaders{}
  loadBizObjectsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sortByFields0 := &dingtalkh3yun_1_0.LoadBizObjectsRequestSortByFields{
    FieldName: tea.String("Age"),
    Direction: tea.String("Ascending"),
  }
  loadBizObjectsRequest := &dingtalkh3yun_1_0.LoadBizObjectsRequest{
    SchemaCode: tea.String("D000183b4xxx"),
    PageNumber: tea.Int32(1),
    PageSize: tea.Int32(10),
    ReturnFields: []*string{tea.String("Name")},
    SortByFields: []*dingtalkh3yun_1_0.LoadBizObjectsRequestSortByFields{sortByFields0},
    MatcherJson: tea.String("{ \"Type\": \"Item\", \"Name\": \"F0000010\", \"Operator\": 2, \"Value\": \"0000007\" }"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.LoadBizObjectsWithOptions(loadBizObjectsRequest, loadBizObjectsHeaders, &util.RuntimeOptions{})
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
import dingtalkh3yun_1_0, * as $dingtalkh3yun_1_0 from '@alicloud/dingtalk/h3yun_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkh3yun_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkh3yun_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let loadBizObjectsHeaders = new $dingtalkh3yun_1_0.LoadBizObjectsHeaders({ });
    loadBizObjectsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sortByFields0 = new $dingtalkh3yun_1_0.LoadBizObjectsRequestSortByFields({
      fieldName: "Age",
      direction: "Ascending",
    });
    let loadBizObjectsRequest = new $dingtalkh3yun_1_0.LoadBizObjectsRequest({
      schemaCode: "D000183b4xxx",
      pageNumber: 1,
      pageSize: 10,
      returnFields: [
        "Name"
      ],
      sortByFields: [
        sortByFields0
      ],
      matcherJson: "{ \"Type\": \"Item\", \"Name\": \"F0000010\", \"Operator\": 2, \"Value\": \"0000007\" }",
    });
    try {
      await client.loadBizObjectsWithOptions(loadBizObjectsRequest, loadBizObjectsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsHeaders loadBizObjectsHeaders = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsHeaders();
            loadBizObjectsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsRequest.LoadBizObjectsRequestSortByFields sortByFields0 = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsRequest.LoadBizObjectsRequestSortByFields
            {
                FieldName = "Age",
                Direction = "Ascending",
            };
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsRequest loadBizObjectsRequest = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsRequest
            {
                SchemaCode = "D000183b4xxx",
                PageNumber = 1,
                PageSize = 10,
                ReturnFields = new List<string>
                {
                    "Name"
                },
                SortByFields = new List<AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizObjectsRequest.LoadBizObjectsRequestSortByFields>
                {
                    sortByFields0
                },
                MatcherJson = "{ \"Type\": \"Item\", \"Name\": \"F0000010\", \"Operator\": 2, \"Value\": \"0000007\" }",
            };
            try
            {
                client.LoadBizObjectsWithOptions(loadBizObjectsRequest, loadBizObjectsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkh_3yun__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkh3yun_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkh3yun_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::Client> client = make_shared<Alibabacloud_Dingtalkh3yun_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsHeaders> loadBizObjectsHeaders = make_shared<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsHeaders>();
  loadBizObjectsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsRequestSortByFields> sortByFields0 = make_shared<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsRequestSortByFields>(map<string, boost::any>({
    {"fieldName", boost::any(string("Age"))},
    {"direction", boost::any(string("Ascending"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsRequest> loadBizObjectsRequest = make_shared<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsRequest>(map<string, boost::any>({
    {"schemaCode", boost::any(string("D000183b4xxx"))},
    {"pageNumber", boost::any(1)},
    {"pageSize", boost::any(10)},
    {"returnFields", boost::any(vector<string>({
      "Name"
    }))},
    {"sortByFields", boost::any(vector<Alibabacloud_Dingtalkh3yun_1_0::LoadBizObjectsRequestSortByFields>({
      sortByFields0
    }))},
    {"matcherJson", boost::any(string("{ "Type": "Item", "Name": "F0000010", "Operator": 2, "Value": "0000007" }"))}
  }));
  try {
    client->loadBizObjectsWithOptions(loadBizObjectsRequest, loadBizObjectsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
Content-Type:application/json

{
  "code" : "success",
  "message" : "OK",
  "data" : {
    "pageNumber" : 1,
    "pageSize" : 10,
    "totalCount" : 20,
    "bizObjects" : [ {
      "ObjectId" : "390bbffe-154f-4c55-8ef3-cd02c4e5ba5f",
      "Name" : "0000007",
      "CreatedBy" : "李四",
      "CreatedTime" : "2021/11/19 21:01:12",
      "ModifiedBy" : "",
      "ModifiedTime" : "2021/11/19 21:01:12",
      "WorkflowInstanceId" : "",
      "Status" : 1,
      "F0000010" : "0000007",
      "F0000011" : "王五12",
      "F0000012" : "D级客户",
      "F0000013" : "7000",
      "D000183Fcd15f3a51e624bbc9945392d190b6aa8" : [ {
        "ObjectId" : "5f464d90-08d1-4420-bca1-cce984548125",
        "ParentObjectId" : "390bbffe-154f-4c55-8ef3-cd02c4e5ba5f",
        "F0000014" : "克里斯"
      } ],
      "CreatedByObject" : {
        "ObjectId" : "aea4d7a7-d162-4c77-9c44-7bd9cb8316a5",
        "Name" : "李四"
      }
    } ]
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | dataNotExist.form.schemaNotExist | 表单结构不存在 | 无效的schemaCode参数 |
| 400 | invalidParameter.filterPraseFailed | %s | 入参：matcherJson无效或不正确 |
| 500 | systemError | 系统异常 | 系统异常 |
