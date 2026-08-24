---
title: "根据迁移后的unionId查询原unionId"
source_url: "https://open.dingtalk.com/document/development/query-the-original-union-id-based-on-the-union-id"
namespace: "development"
slug: "query-the-original-union-id-based-on-the-union-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 企业账号 > 根据迁移后的unionId查询原unionId"
doc_id: "MQEnxRsBXh"
updated_at: "2026-06-01 15:43:34"
---

> Source: https://open.dingtalk.com/document/development/query-the-original-union-id-based-on-the-union-id
> Path: 应用开发 / 服务端API / 通讯录管理 > 企业账号 > 根据迁移后的unionId查询原unionId
> Updated: 2026-06-01 15:43:34

# 根据迁移后的unionId查询原unionId

普通帐号迁移为专属帐号后，根据迁移后的unionId查询原unionId

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccount/getUnionIdByMigrationUnionIds |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Contact.OrgAccountMigration.Read-通讯录企业账号迁移数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| migrationUnionId | String | 是 | 迁移后企业账号的unionId，可调用[查询企业账号用户详情](0108-queries-the-details-of-a-dedicated-account.md)接口获得unionid参数值。 |

### 请求示例

HTTP

```
GET /v1.0/contact/orgAccount/getUnionIdByMigrationUnionIds?migrationUnionId=yyyy HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcontact_1_0.*;
import com.aliyun.dingtalkcontact_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        GetUnionIdByMigrationUnionIdHeaders getUnionIdByMigrationUnionIdHeaders = new GetUnionIdByMigrationUnionIdHeaders();
        getUnionIdByMigrationUnionIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetUnionIdByMigrationUnionIdRequest getUnionIdByMigrationUnionIdRequest = new GetUnionIdByMigrationUnionIdRequest()
                .setMigrationUnionId("yyyy");
        try {
            client.getUnionIdByMigrationUnionIdWithOptions(getUnionIdByMigrationUnionIdRequest, getUnionIdByMigrationUnionIdHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_union_id_by_migration_union_id_headers = dingtalkcontact__1__0_models.GetUnionIdByMigrationUnionIdHeaders()
        get_union_id_by_migration_union_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_union_id_by_migration_union_id_request = dingtalkcontact__1__0_models.GetUnionIdByMigrationUnionIdRequest(
            migration_union_id='yyyy'
        )
        try:
            client.get_union_id_by_migration_union_id_with_options(get_union_id_by_migration_union_id_request, get_union_id_by_migration_union_id_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_union_id_by_migration_union_id_headers = dingtalkcontact__1__0_models.GetUnionIdByMigrationUnionIdHeaders()
        get_union_id_by_migration_union_id_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_union_id_by_migration_union_id_request = dingtalkcontact__1__0_models.GetUnionIdByMigrationUnionIdRequest(
            migration_union_id='yyyy'
        )
        try:
            await client.get_union_id_by_migration_union_id_with_options_async(get_union_id_by_migration_union_id_request, get_union_id_by_migration_union_id_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetUnionIdByMigrationUnionIdHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\GetUnionIdByMigrationUnionIdRequest;
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
        $getUnionIdByMigrationUnionIdHeaders = new GetUnionIdByMigrationUnionIdHeaders([]);
        $getUnionIdByMigrationUnionIdHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUnionIdByMigrationUnionIdRequest = new GetUnionIdByMigrationUnionIdRequest([
            "migrationUnionId" => "yyyy"
        ]);
        try {
            $client->getUnionIdByMigrationUnionIdWithOptions($getUnionIdByMigrationUnionIdRequest, $getUnionIdByMigrationUnionIdHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getUnionIdByMigrationUnionIdHeaders := &dingtalkcontact_1_0.GetUnionIdByMigrationUnionIdHeaders{}
  getUnionIdByMigrationUnionIdHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUnionIdByMigrationUnionIdRequest := &dingtalkcontact_1_0.GetUnionIdByMigrationUnionIdRequest{
    MigrationUnionId: tea.String("yyyy"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUnionIdByMigrationUnionIdWithOptions(getUnionIdByMigrationUnionIdRequest, getUnionIdByMigrationUnionIdHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getUnionIdByMigrationUnionIdHeaders = new $dingtalkcontact_1_0.GetUnionIdByMigrationUnionIdHeaders({ });
    getUnionIdByMigrationUnionIdHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUnionIdByMigrationUnionIdRequest = new $dingtalkcontact_1_0.GetUnionIdByMigrationUnionIdRequest({
      migrationUnionId: "yyyy",
    });
    try {
      await client.getUnionIdByMigrationUnionIdWithOptions(getUnionIdByMigrationUnionIdRequest, getUnionIdByMigrationUnionIdHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetUnionIdByMigrationUnionIdHeaders getUnionIdByMigrationUnionIdHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetUnionIdByMigrationUnionIdHeaders();
            getUnionIdByMigrationUnionIdHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetUnionIdByMigrationUnionIdRequest getUnionIdByMigrationUnionIdRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.GetUnionIdByMigrationUnionIdRequest
            {
                MigrationUnionId = "yyyy",
            };
            try
            {
                client.GetUnionIdByMigrationUnionIdWithOptions(getUnionIdByMigrationUnionIdRequest, getUnionIdByMigrationUnionIdHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcontact__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcontact_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcontact_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcontact_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetUnionIdByMigrationUnionIdHeaders> getUnionIdByMigrationUnionIdHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetUnionIdByMigrationUnionIdHeaders>();
  getUnionIdByMigrationUnionIdHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::GetUnionIdByMigrationUnionIdRequest> getUnionIdByMigrationUnionIdRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::GetUnionIdByMigrationUnionIdRequest>(map<string, boost::any>({
    {"migrationUnionId", boost::any(string("yyyy"))}
  }));
  try {
    client->getUnionIdByMigrationUnionIdWithOptions(getUnionIdByMigrationUnionIdRequest, getUnionIdByMigrationUnionIdHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| unionId | String | 原普通账号的unionId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "unionId" : "zzzz"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.param | 无效参数 | 无效参数 |
| 400 | invalid.userid | 找不到该用户 | 找不到该用户 |
| 400 | illegal.migration.unionId | 非法的migrationUnionId | 非法的migrationUnionId |
| 500 | system.busy | 系统繁忙 | 系统繁忙 |
