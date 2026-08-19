---
title: "更换服务群所在的群分组"
source_url: "https://open.dingtalk.com/document/development/modify-a-service-group"
namespace: "development"
slug: "modify-a-service-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 服务群 > 更换服务群所在的群分组"
doc_id: "UnMHc8jGkU"
updated_at: "2025-09-23 19:22:34"
---

> Source: https://open.dingtalk.com/document/development/modify-a-service-group
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 服务群 > 更换服务群所在的群分组
> Updated: 2025-09-23 19:22:34

# 更换服务群所在的群分组

调用本接口，更换服务群所在的群分组。

## 接口调用说明

内部群只能更换到内部服务群组，外部群只能更换到外部服务群组。例如，服务群A当前所在分组为**内部服务群组**，更换服务群A所在的分组时，只能更换到另一个**内部服务群组**内。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/serviceGroup/groups/configurations |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-ServiceGroup.Group.ReadWrite-场景服务群读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openTeamId | String | 否 | 开放团队ID。 |
| openConversationId | String | 否 | 开放群ID，可调用[创建场景服务群](1120-create-a-scenario-service-group.md)接口获取openConversationId参数值。 |
| openGroupSetId | String | 否 | 开放群组ID。 |

### 请求示例

HTTP

```
PUT /v1.0/serviceGroup/groups/configurations HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:a982f822xxxx
Content-Type:application/json

{
  "openTeamId" : "u9iSxxxxx",
  "openConversationId" : "cidkexxxxx",
  "openGroupSetId" : "iPnLAxxxxx"
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
    public static com.aliyun.dingtalkservice_group_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkservice_group_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkservice_group_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkservice_group_1_0.models.UpdateGroupSetHeaders updateGroupSetHeaders = new com.aliyun.dingtalkservice_group_1_0.models.UpdateGroupSetHeaders();
        updateGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkservice_group_1_0.models.UpdateGroupSetRequest updateGroupSetRequest = new com.aliyun.dingtalkservice_group_1_0.models.UpdateGroupSetRequest()
                .setOpenTeamId("u9iSxxxxx")
                .setOpenConversationId("cidkexxxxx")
                .setOpenGroupSetId("iPnLAxxxxx");
        try {
            client.updateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_group_set_headers = dingtalkservice_group__1__0_models.UpdateGroupSetHeaders()
        update_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_group_set_request = dingtalkservice_group__1__0_models.UpdateGroupSetRequest(
            open_team_id='u9iSxxxxx',
            open_conversation_id='cidkexxxxx',
            open_group_set_id='iPnLAxxxxx'
        )
        try:
            client.update_group_set_with_options(update_group_set_request, update_group_set_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_group_set_headers = dingtalkservice_group__1__0_models.UpdateGroupSetHeaders()
        update_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_group_set_request = dingtalkservice_group__1__0_models.UpdateGroupSetRequest(
            open_team_id='u9iSxxxxx',
            open_conversation_id='cidkexxxxx',
            open_group_set_id='iPnLAxxxxx'
        )
        try:
            await client.update_group_set_with_options_async(update_group_set_request, update_group_set_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\UpdateGroupSetHeaders;
use AlibabaCloud\SDK\Dingtalk\Vservice_group_1_0\Models\UpdateGroupSetRequest;
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
        $updateGroupSetHeaders = new UpdateGroupSetHeaders([]);
        $updateGroupSetHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateGroupSetRequest = new UpdateGroupSetRequest([
            "openTeamId" => "u9iSxxxxx",
            "openConversationId" => "cidkexxxxx",
            "openGroupSetId" => "iPnLAxxxxx"
        ]);
        try {
            $client->updateGroupSetWithOptions($updateGroupSetRequest, $updateGroupSetHeaders, new RuntimeOptions([]));
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
  dingtalkservicegroup_1_0  "github.com/alibabacloud-go/dingtalk/serviceGroup_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  updateGroupSetHeaders := &dingtalkservicegroup_1_0.UpdateGroupSetHeaders{}
  updateGroupSetHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateGroupSetRequest := &dingtalkservicegroup_1_0.UpdateGroupSetRequest{
    OpenTeamId: tea.String("u9iSxxxxx"),
    OpenConversationId: tea.String("cidkexxxxx"),
    OpenGroupSetId: tea.String("iPnLAxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, &util.RuntimeOptions{})
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
    let updateGroupSetHeaders = new $dingtalkserviceGroup_1_0.UpdateGroupSetHeaders({ });
    updateGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateGroupSetRequest = new $dingtalkserviceGroup_1_0.UpdateGroupSetRequest({
      openTeamId: "u9iSxxxxx",
      openConversationId: "cidkexxxxx",
      openGroupSetId: "iPnLAxxxxx",
    });
    try {
      await client.updateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpdateGroupSetHeaders updateGroupSetHeaders = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpdateGroupSetHeaders();
            updateGroupSetHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpdateGroupSetRequest updateGroupSetRequest = new AlibabaCloud.SDK.Dingtalkservice_group_1_0.Models.UpdateGroupSetRequest
            {
                OpenTeamId = "u9iSxxxxx",
                OpenConversationId = "cidkexxxxx",
                OpenGroupSetId = "iPnLAxxxxx",
            };
            try
            {
                client.UpdateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 更新是否成功，true表示更新成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : false
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | systemError | 系统异常 | 系统异常，内部群只能更新到内部服务群组，外部群只能更新到外部服务群组 |
| 500 | dataNotFound | 数据不存在 | 数据不存在 |
| 500 | staffNotFound | 员工信息未找到 | 员工信息未找到 |
| 500 | teamNameDuplicate | 团队名称已存在 | 团队名称已存在 |
| 500 | teamNameInvalid | 团队名称非法 | 团队名称非法 |
| 500 | microInvisibleToUser | 用户不在应用可见范围内 | 用户不在应用可见范围内 |
