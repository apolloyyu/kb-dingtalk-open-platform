---
title: "获取招聘流程标识"
source_url: "https://open.dingtalk.com/document/development/get-recruitment-process-identity"
namespace: "development"
slug: "get-recruitment-process-identity"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 获取招聘流程标识"
doc_id: "juUM4rHhHy"
updated_at: "2026-06-04 19:10:35"
---

> Source: https://open.dingtalk.com/document/development/get-recruitment-process-identity
> Path: 应用开发 / 服务端 API / 智能招聘 > 获取招聘流程标识
> Updated: 2026-06-04 19:10:35

# 获取招聘流程标识

调用本接口根据面试的标识ID，获取面试在整个招聘流程中的标识。

## **接口调用说明**

本接口需要和[获取候选人的面试信息](0962-query-the-interview-list.md)等接口结合使用，获取到招聘流程标识。后续可结合招聘流程其他功能接口使用，比如更新招聘流程表等。调用流程示例如下：

步骤一：调用[获取候选人的面试信息](0962-query-the-interview-list.md)接口获取小钉所有的面试列表。

步骤二：根据第一条面试标识ID，调用本接口，获取第一条面试在招聘流程中的标识。

步骤三：调用更新招聘流程等能力。更新招聘流程等能力后续开放，请关注文档更新。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/flows/ids |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_recruitment\_plugin-智能招聘插件管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizCode | String | 否 | 业务标识，默认值为`ddats`。    如果传该参数，只支持`ddats`。 |
| relationEntity | String | 是 | 招聘流程关联实体，参数请传interview。    目前仅支持面试。 |
| relationEntityId | String | 是 | 招聘流程关联实体标识。 |

### 请求示例

HTTP

```
GET /v1.0/ats/flows/ids?bizCode=ddats&relationEntity=interview&relationEntityId=xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkats_1_0.*;
import com.aliyun.dingtalkats_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkats_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkats_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkats_1_0.Client client = Sample.createClient();
        GetFlowIdByRelationEntityIdHeaders getFlowIdByRelationEntityIdHeaders = new GetFlowIdByRelationEntityIdHeaders();
        getFlowIdByRelationEntityIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetFlowIdByRelationEntityIdRequest getFlowIdByRelationEntityIdRequest = new GetFlowIdByRelationEntityIdRequest()
                .setBizCode("ddats")
                .setRelationEntity("interview")
                .setRelationEntityId("xxx");
        try {
            client.getFlowIdByRelationEntityIdWithOptions(getFlowIdByRelationEntityIdRequest, getFlowIdByRelationEntityIdHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.ats_1_0.client import Client as dingtalkats_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.ats_1_0 import models as dingtalkats__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkats_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkats_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_flow_id_by_relation_entity_id_headers = dingtalkats__1__0_models.GetFlowIdByRelationEntityIdHeaders()
        get_flow_id_by_relation_entity_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_flow_id_by_relation_entity_id_request = dingtalkats__1__0_models.GetFlowIdByRelationEntityIdRequest(
            biz_code='ddats',
            relation_entity='interview',
            relation_entity_id='xxx'
        )
        try:
            client.get_flow_id_by_relation_entity_id_with_options(get_flow_id_by_relation_entity_id_request, get_flow_id_by_relation_entity_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_flow_id_by_relation_entity_id_headers = dingtalkats__1__0_models.GetFlowIdByRelationEntityIdHeaders()
        get_flow_id_by_relation_entity_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_flow_id_by_relation_entity_id_request = dingtalkats__1__0_models.GetFlowIdByRelationEntityIdRequest(
            biz_code='ddats',
            relation_entity='interview',
            relation_entity_id='xxx'
        )
        try:
            await client.get_flow_id_by_relation_entity_id_with_options_async(get_flow_id_by_relation_entity_id_request, get_flow_id_by_relation_entity_id_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\GetFlowIdByRelationEntityIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\GetFlowIdByRelationEntityIdRequest;
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
        $getFlowIdByRelationEntityIdHeaders = new GetFlowIdByRelationEntityIdHeaders([]);
        $getFlowIdByRelationEntityIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getFlowIdByRelationEntityIdRequest = new GetFlowIdByRelationEntityIdRequest([
            "bizCode" => "ddats",
            "relationEntity" => "interview",
            "relationEntityId" => "xxx"
        ]);
        try {
            $client->getFlowIdByRelationEntityIdWithOptions($getFlowIdByRelationEntityIdRequest, $getFlowIdByRelationEntityIdHeaders, new RuntimeOptions([]));
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
  dingtalkats_1_0  "github.com/alibabacloud-go/dingtalk/ats_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkats_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkats_1_0.Client{}
  _result, _err = dingtalkats_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getFlowIdByRelationEntityIdHeaders := &dingtalkats_1_0.GetFlowIdByRelationEntityIdHeaders{}
  getFlowIdByRelationEntityIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getFlowIdByRelationEntityIdRequest := &dingtalkats_1_0.GetFlowIdByRelationEntityIdRequest{
    BizCode: tea.String("ddats"),
    RelationEntity: tea.String("interview"),
    RelationEntityId: tea.String("xxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetFlowIdByRelationEntityIdWithOptions(getFlowIdByRelationEntityIdRequest, getFlowIdByRelationEntityIdHeaders, &util.RuntimeOptions{})
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
import dingtalkats_1_0, * as $dingtalkats_1_0 from '@alicloud/dingtalk/ats_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkats_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkats_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getFlowIdByRelationEntityIdHeaders = new $dingtalkats_1_0.GetFlowIdByRelationEntityIdHeaders({ });
    getFlowIdByRelationEntityIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getFlowIdByRelationEntityIdRequest = new $dingtalkats_1_0.GetFlowIdByRelationEntityIdRequest({
      bizCode: "ddats",
      relationEntity: "interview",
      relationEntityId: "xxx",
    });
    try {
      await client.getFlowIdByRelationEntityIdWithOptions(getFlowIdByRelationEntityIdRequest, getFlowIdByRelationEntityIdHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkats_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkats_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkats_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFlowIdByRelationEntityIdHeaders getFlowIdByRelationEntityIdHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFlowIdByRelationEntityIdHeaders();
            getFlowIdByRelationEntityIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFlowIdByRelationEntityIdRequest getFlowIdByRelationEntityIdRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.GetFlowIdByRelationEntityIdRequest
            {
                BizCode = "ddats",
                RelationEntity = "interview",
                RelationEntityId = "xxx",
            };
            try
            {
                client.GetFlowIdByRelationEntityIdWithOptions(getFlowIdByRelationEntityIdRequest, getFlowIdByRelationEntityIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkats__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkats_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkats_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkats_1_0::Client> client = make_shared<Alibabacloud_Dingtalkats_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkats_1_0::GetFlowIdByRelationEntityIdHeaders> getFlowIdByRelationEntityIdHeaders = make_shared<Alibabacloud_Dingtalkats_1_0::GetFlowIdByRelationEntityIdHeaders>();
  getFlowIdByRelationEntityIdHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkats_1_0::GetFlowIdByRelationEntityIdRequest> getFlowIdByRelationEntityIdRequest = make_shared<Alibabacloud_Dingtalkats_1_0::GetFlowIdByRelationEntityIdRequest>(map<string, boost::any>({
    {"bizCode", boost::any(string("ddats"))},
    {"relationEntity", boost::any(string("interview"))},
    {"relationEntityId", boost::any(string("xxx"))}
  }));
  try {
    client->getFlowIdByRelationEntityIdWithOptions(getFlowIdByRelationEntityIdRequest, getFlowIdByRelationEntityIdHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| flowId | String | 招聘流程标识。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "flowId" : "rbf449996e1faa94efca9a256******c40"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParam | %s | 无效参数 |
| 500 | systemError | 系统错误 | 系统错误 |
