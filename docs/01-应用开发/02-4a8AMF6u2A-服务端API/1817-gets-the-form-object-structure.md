---
title: "获取表单对象结构"
source_url: "https://open.dingtalk.com/document/development/gets-the-form-object-structure"
namespace: "development"
slug: "gets-the-form-object-structure"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 生态开放 > 氚云 > 表单 > 获取表单对象结构"
doc_id: "hTrt8RfniG"
updated_at: "2025-09-08 19:06:19"
---

> Source: https://open.dingtalk.com/document/development/gets-the-form-object-structure
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 生态开放 > 氚云 > 表单 > 获取表单对象结构
> Updated: 2025-09-08 19:06:19

# 获取表单对象结构

调用本接口获取表单对象结构信息。

> **[!IMPORTANT]**
>
> 为了更进一步提升接口质量以及用户体验，我们对本接口文档做出如下调整：
>
> - 自 2024 年 8 月 1 日起，本接口文档将会被迁移至历史文档目录。
> - 氚云接口不再支持新应用接入，已接入应用可继续使用，后续若需要接入氚云接口，请使用[氚云开发者手册](https://help.h3yun.com/channels/899.html)。

![](https://img.alicdn.com/imgextra/i4/O1CN01ZXRIAX1QN6CpWRskJ_!!6000000001963-2-tps-1267-618.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=org&api=h3yun_1.0%23LoadBizFields) |
| 第三方企业应用 | 支持 | 氚云数据管理权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=h3yun_1.0%23LoadBizFields) |
| 第三方个人应用 | 暂不支持 | 氚云数据管理权限 | 暂不支持 |

## 请求方法

```
GET /v1.0/h3yun/forms/loadBizFields?schemaCode=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| schemaCode | String | 是 | 表单编码。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| code | String | 状态码。 |
| message | String | 状态码描述。 |
| data | Object | 返回结果。 |
| schemaCode | String | 表单编码。 |
| formName | String | 表单名称。 |
| fields | Array | 字段、组件结构数组。 |
| label | String | 显示名称。 |
| fieldName | String | 字段名称。 |
| bizDataType | String | 字段、自定义组件的数据类型，取值：   - **Bool**：逻辑型 - **DataTime**：日期型、日期组件 - **Double**：双精度数值型 - **Int**：整形 - **Long**：长整形 - **String**：长文本 - **ShortString**：短文本 - **ByteArray**：二进制流 - **Image**：图片类型、图片组件 - **File**：附件类型组件 - **TimeSpan**：时间段 - **Unit**：参与者（单人） - **UnitArray**：参与者（多人） - **Html**：html类型 - **Xml**：xml类型 - **BizObject**：业务对象 - **BizObjectArray**：业务对象数组、子表组件 - **Association**：关联到其他对象、关联组件 - **AssociationArray**：关联对象数组 - **Map**：地图类型 - **Address**：地址类型， - **Formula**：公式型空间 - **Signature**：签名控件 - **Plugin**：文字识别 |
| childForms | Array | 子表结构数组。 |
| schemaCode | String | 子表编码。 |
| formName | String | 子表名称。 |
| fields | Array | 子表字段数组。 |
| label | String | 显示名称。 |
| fieldName | String | 字段名或组件名。 |
| bizDataType | String | 字段数据类型。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/h3yun/forms/loadBizFields?schemaCode=D00018xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bef2c84xxx
Content-Type:application/json
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
        LoadBizFieldsHeaders loadBizFieldsHeaders = new LoadBizFieldsHeaders();
        loadBizFieldsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        LoadBizFieldsRequest loadBizFieldsRequest = new LoadBizFieldsRequest()
                .setSchemaCode("D00018xxx");
        try {
            client.loadBizFieldsWithOptions(loadBizFieldsRequest, loadBizFieldsHeaders, new RuntimeOptions());
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
        load_biz_fields_headers = dingtalkh_3yun__1__0_models.LoadBizFieldsHeaders()
        load_biz_fields_headers.x_acs_dingtalk_access_token = '<your access token>'
        load_biz_fields_request = dingtalkh_3yun__1__0_models.LoadBizFieldsRequest(
            schema_code='D00018xxx'
        )
        try:
            client.load_biz_fields_with_options(load_biz_fields_request, load_biz_fields_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        load_biz_fields_headers = dingtalkh_3yun__1__0_models.LoadBizFieldsHeaders()
        load_biz_fields_headers.x_acs_dingtalk_access_token = '<your access token>'
        load_biz_fields_request = dingtalkh_3yun__1__0_models.LoadBizFieldsRequest(
            schema_code='D00018xxx'
        )
        try:
            await client.load_biz_fields_with_options_async(load_biz_fields_request, load_biz_fields_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\LoadBizFieldsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vh3yun_1_0\Models\LoadBizFieldsRequest;
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
        $loadBizFieldsHeaders = new LoadBizFieldsHeaders([]);
        $loadBizFieldsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $loadBizFieldsRequest = new LoadBizFieldsRequest([
            "schemaCode" => "D00018xxx"
        ]);
        try {
            $client->loadBizFieldsWithOptions($loadBizFieldsRequest, $loadBizFieldsHeaders, new RuntimeOptions([]));
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

  loadBizFieldsHeaders := &dingtalkh3yun_1_0.LoadBizFieldsHeaders{}
  loadBizFieldsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  loadBizFieldsRequest := &dingtalkh3yun_1_0.LoadBizFieldsRequest{
    SchemaCode: tea.String("D00018xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.LoadBizFieldsWithOptions(loadBizFieldsRequest, loadBizFieldsHeaders, &util.RuntimeOptions{})
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
    let loadBizFieldsHeaders = new $dingtalkh3yun_1_0.LoadBizFieldsHeaders({ });
    loadBizFieldsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let loadBizFieldsRequest = new $dingtalkh3yun_1_0.LoadBizFieldsRequest({
      schemaCode: "D00018xxx",
    });
    try {
      await client.loadBizFieldsWithOptions(loadBizFieldsRequest, loadBizFieldsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizFieldsHeaders loadBizFieldsHeaders = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizFieldsHeaders();
            loadBizFieldsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizFieldsRequest loadBizFieldsRequest = new AlibabaCloud.SDK.Dingtalkh3yun_1_0.Models.LoadBizFieldsRequest
            {
                SchemaCode = "D00018xxx",
            };
            try
            {
                client.LoadBizFieldsWithOptions(loadBizFieldsRequest, loadBizFieldsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::LoadBizFieldsHeaders> loadBizFieldsHeaders = make_shared<Alibabacloud_Dingtalkh3yun_1_0::LoadBizFieldsHeaders>();
  loadBizFieldsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkh3yun_1_0::LoadBizFieldsRequest> loadBizFieldsRequest = make_shared<Alibabacloud_Dingtalkh3yun_1_0::LoadBizFieldsRequest>(map<string, boost::any>({
    {"schemaCode", boost::any(string("D00018xxx"))}
  }));
  try {
    client->loadBizFieldsWithOptions(loadBizFieldsRequest, loadBizFieldsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
    "schemaCode" : "D0001839bxxx",
    "formName" : "客户管理",
    "fields" : [ {
      "label" : "姓名",
      "fieldName" : "Name",
      "bizDataType" : "Bool"
    } ],
    "childForms" : [ {
      "schemaCode" : "D000183xxx",
      "formName" : "子表",
      "fields" : [ {
        "label" : "电话",
        "fieldName" : "Phone",
        "bizDataType" : "Short"
      } ]
    } ]
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.input.invalid | %s | 入参校验失败 |
| 400 | dataNotExist.form.schemaNotExist | 表单结构不存在 | 无效的schemaCode参数 |
