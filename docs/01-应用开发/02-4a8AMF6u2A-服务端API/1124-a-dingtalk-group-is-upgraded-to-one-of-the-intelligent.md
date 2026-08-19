---
title: "升级普通群为服务群"
source_url: "https://open.dingtalk.com/document/development/a-dingtalk-group-is-upgraded-to-one-of-the-intelligent"
namespace: "development"
slug: "a-dingtalk-group-is-upgraded-to-one-of-the-intelligent"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 升级普通群为服务群"
doc_id: "KrDMBfRdXr"
updated_at: "2025-09-23 19:22:35"
---

> Source: https://open.dingtalk.com/document/development/a-dingtalk-group-is-upgraded-to-one-of-the-intelligent
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 服务群 > 升级普通群为服务群
> Updated: 2025-09-23 19:22:35

# 升级普通群为服务群

调用本接口将企业内部群、普通群，升级为智能服务群中的服务群。

## 接口调用说明

接口调用时如果不指定团队id和目标群组id，则必须指定服务群模板id，此时群会升级到企业默认团队下、该模板对应的默认群分组中。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/normalGroups/upgrade |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ServiceGroup.Group.ReadWrite-场景服务群读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openGroupSetId | String | 否 | 升级的目标群组ID。 |
| templateId | String | 否 | 升级的目标群模板ID。 |
| openConversationId | String | 是 | 群ID。 |
| openTeamId | String | 否 | 升级的目标团队ID。 |

### 请求示例

HTTP

```
POST /v1.0/serviceGroup/normalGroups/upgrade HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a982f822xxxx
Content-Type:application/json

{
  "openGroupSetId" : "Jciwxxx",
  "templateId" : "6b7ae69d-0f9f-4xxx",
  "openConversationId" : "cidxxxxxx==",
  "openTeamId" : "Jciwnfw"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkservice_group_1_0.*;
import com.aliyun.dingtalkservice_group_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkservice_group_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkservice_group_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkservice_group_1_0.Client client = Sample.createClient();
        UpgradeNormalGroupHeaders upgradeNormalGroupHeaders = new UpgradeNormalGroupHeaders();
        upgradeNormalGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpgradeNormalGroupRequest upgradeNormalGroupRequest = new UpgradeNormalGroupRequest()
                .setOpenGroupSetId("Jciwxxx")
                .setTemplateId("6b7ae69d-0f9f-4xxx")
                .setOpenConversationId("cidxxxxxx==")
                .setOpenTeamId("Jciwnfw");
        try {
            client.upgradeNormalGroupWithOptions(upgradeNormalGroupRequest, upgradeNormalGroupHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.serviceGroup_1_0.client import Client as dingtalkserviceGroup_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.serviceGroup_1_0 import models as dingtalkservice_group__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkserviceGroup_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkserviceGroup_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        upgrade_normal_group_headers = dingtalkservice_group__1__0_models.UpgradeNormalGroupHeaders()
        upgrade_normal_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        upgrade_normal_group_request = dingtalkservice_group__1__0_models.UpgradeNormalGroupRequest(
            open_group_set_id='Jciwxxx',
            template_id='6b7ae69d-0f9f-4xxx',
            open_conversation_id='cidxxxxxx==',
            open_team_id='Jciwnfw'
        )
        try:
            client.upgrade_normal_group_with_options(upgrade_normal_group_request, upgrade_normal_group_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        upgrade_normal_group_headers = dingtalkservice_group__1__0_models.UpgradeNormalGroupHeaders()
        upgrade_normal_group_headers.x_acs_dingtalk_access_token = '<your access token>'
        upgrade_normal_group_request = dingtalkservice_group__1__0_models.UpgradeNormalGroupRequest(
            open_group_set_id='Jciwxxx',
            template_id='6b7ae69d-0f9f-4xxx',
            open_conversation_id='cidxxxxxx==',
            open_team_id='Jciwnfw'
        )
        try:
            await client.upgrade_normal_group_with_options_async(upgrade_normal_group_request, upgrade_normal_group_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\UpgradeNormalGroupHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\UpgradeNormalGroupRequest;
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
        $upgradeNormalGroupHeaders = new UpgradeNormalGroupHeaders([]);
        $upgradeNormalGroupHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $upgradeNormalGroupRequest = new UpgradeNormalGroupRequest([
            "openGroupSetId" => "Jciwxxx",
            "templateId" => "6b7ae69d-0f9f-4xxx",
            "openConversationId" => "cidxxxxxx==",
            "openTeamId" => "Jciwnfw"
        ]);
        try {
            $client->upgradeNormalGroupWithOptions($upgradeNormalGroupRequest, $upgradeNormalGroupHeaders, new RuntimeOptions([]));
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
  dingtalkservicegroup_1_0  "github.com/alibabacloud-go/dingtalk/serviceGroup_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkservicegroup_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkservicegroup_1_0.Client{}
  _result, _err = dingtalkservicegroup_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  upgradeNormalGroupHeaders := &dingtalkservicegroup_1_0.UpgradeNormalGroupHeaders{}
  upgradeNormalGroupHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  upgradeNormalGroupRequest := &dingtalkservicegroup_1_0.UpgradeNormalGroupRequest{
    OpenGroupSetId: tea.String("Jciwxxx"),
    TemplateId: tea.String("6b7ae69d-0f9f-4xxx"),
    OpenConversationId: tea.String("cidxxxxxx=="),
    OpenTeamId: tea.String("Jciwnfw"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpgradeNormalGroupWithOptions(upgradeNormalGroupRequest, upgradeNormalGroupHeaders, &util.RuntimeOptions{})
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
import dingtalkserviceGroup_1_0, * as $dingtalkserviceGroup_1_0 from '@alicloud/dingtalk/serviceGroup_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkserviceGroup_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkserviceGroup_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let upgradeNormalGroupHeaders = new $dingtalkserviceGroup_1_0.UpgradeNormalGroupHeaders({ });
    upgradeNormalGroupHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let upgradeNormalGroupRequest = new $dingtalkserviceGroup_1_0.UpgradeNormalGroupRequest({
      openGroupSetId: "Jciwxxx",
      templateId: "6b7ae69d-0f9f-4xxx",
      openConversationId: "cidxxxxxx==",
      openTeamId: "Jciwnfw",
    });
    try {
      await client.upgradeNormalGroupWithOptions(upgradeNormalGroupRequest, upgradeNormalGroupHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpgradeNormalGroupHeaders upgradeNormalGroupHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpgradeNormalGroupHeaders();
            upgradeNormalGroupHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpgradeNormalGroupRequest upgradeNormalGroupRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpgradeNormalGroupRequest
            {
                OpenGroupSetId = "Jciwxxx",
                TemplateId = "6b7ae69d-0f9f-4xxx",
                OpenConversationId = "cidxxxxxx==",
                OpenTeamId = "Jciwnfw",
            };
            try
            {
                client.UpgradeNormalGroupWithOptions(upgradeNormalGroupRequest, upgradeNormalGroupHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkservice_group__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkservice_group_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkservice_group_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::Client> client = make_shared<Alibabacloud_Dingtalkservice_group_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::UpgradeNormalGroupHeaders> upgradeNormalGroupHeaders = make_shared<Alibabacloud_Dingtalkservice_group_1_0::UpgradeNormalGroupHeaders>();
  upgradeNormalGroupHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkservice_group_1_0::UpgradeNormalGroupRequest> upgradeNormalGroupRequest = make_shared<Alibabacloud_Dingtalkservice_group_1_0::UpgradeNormalGroupRequest>(map<string, boost::any>({
    {"openGroupSetId", boost::any(string("Jciwxxx"))},
    {"templateId", boost::any(string("6b7ae69d-0f9f-4xxx"))},
    {"openConversationId", boost::any(string("cidxxxxxx=="))},
    {"openTeamId", boost::any(string("Jciwnfw"))}
  }));
  try {
    client->upgradeNormalGroupWithOptions(upgradeNormalGroupRequest, upgradeNormalGroupHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | illegalPama | 参数非法 | 参数非法 |
| 500 | systemError | 系统异常 | 系统异常 |
