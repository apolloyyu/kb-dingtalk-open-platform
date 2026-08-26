---
title: "将助理技能发布到组织技能库"
source_url: "https://open.dingtalk.com/document/development/api-addtoorgskillrepository"
namespace: "development"
slug: "api-addtoorgskillrepository"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > AI 助理 > 助理管理 > 将助理技能发布到组织技能库"
doc_id: "fBLQV0Nxv5"
updated_at: "2026-03-06 09:22:55"
---

> Source: https://open.dingtalk.com/document/development/api-addtoorgskillrepository
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > AI 助理 > 助理管理 > 将助理技能发布到组织技能库
> Updated: 2026-03-06 09:22:55

# 将助理技能发布到组织技能库

调用本接口，将助理技能发布到组织技能库。该接口仅将支持自定义类型的技能发布到组织技能库。

> **[!IMPORTANT]**
>
> 本文档已于 2026年 03 月 05 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!IMPORTANT]**  暂不支持新增申请 | — |
| 第三方企业应用 | 暂不支持 | 暂不支持 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 暂不支持 | 暂不支持 |

## 请求方法

```
POST /v1.0/assistant/orgActionRepositories HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "actionId" : "String",
  "actionVersion" : "String",
  "operatorUnionId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| actionId | String | 是 | 技能唯一标识符。 |
| actionVersion | String | 是 | 技能版本。 |
| operatorUnionId | String | 是 | 操作者用户 ID（Union ID）。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 接口调用是否成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/assistant/orgActionRepositories HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:e8e3373189193a7fb715dc3xxxxxxx
Content-Type:application/json

{
  "actionId" : "AGI-349e26ba-90e7-448a-b042-ddxxxxxx",
  "actionVersion" : "1.x.x",
  "operatorUnionId" : "RHCAZvgbllRse8xrxxxxxxxx"
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
    public static com.aliyun.dingtalkassistant_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkassistant_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkassistant_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkassistant_1_0.models.AddToOrgSkillRepositoryHeaders addToOrgSkillRepositoryHeaders = new com.aliyun.dingtalkassistant_1_0.models.AddToOrgSkillRepositoryHeaders();
        addToOrgSkillRepositoryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkassistant_1_0.models.AddToOrgSkillRepositoryRequest addToOrgSkillRepositoryRequest = new com.aliyun.dingtalkassistant_1_0.models.AddToOrgSkillRepositoryRequest()
                .setActionId("AGI-349e26ba-90e7-448a-b042-ddxxxxxx")
                .setActionVersion("1.x.x")
                .setOperatorUnionId("RHCAZvgbllRse8xrxxxxxxxx");
        try {
            client.addToOrgSkillRepositoryWithOptions(addToOrgSkillRepositoryRequest, addToOrgSkillRepositoryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.assistant_1_0.client import Client as dingtalkassistant_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.assistant_1_0 import models as dingtalkassistant__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkassistant_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkassistant_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_to_org_skill_repository_headers = dingtalkassistant__1__0_models.AddToOrgSkillRepositoryHeaders()
        add_to_org_skill_repository_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_to_org_skill_repository_request = dingtalkassistant__1__0_models.AddToOrgSkillRepositoryRequest(
            action_id='AGI-349e26ba-90e7-448a-b042-ddxxxxxx',
            action_version='1.x.x',
            operator_union_id='RHCAZvgbllRse8xrxxxxxxxx'
        )
        try:
            client.add_to_org_skill_repository_with_options(add_to_org_skill_repository_request, add_to_org_skill_repository_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_to_org_skill_repository_headers = dingtalkassistant__1__0_models.AddToOrgSkillRepositoryHeaders()
        add_to_org_skill_repository_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_to_org_skill_repository_request = dingtalkassistant__1__0_models.AddToOrgSkillRepositoryRequest(
            action_id='AGI-349e26ba-90e7-448a-b042-ddxxxxxx',
            action_version='1.x.x',
            operator_union_id='RHCAZvgbllRse8xrxxxxxxxx'
        )
        try:
            await client.add_to_org_skill_repository_with_options_async(add_to_org_skill_repository_request, add_to_org_skill_repository_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\AddToOrgSkillRepositoryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vassistant_1_0\Models\AddToOrgSkillRepositoryRequest;
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
        $addToOrgSkillRepositoryHeaders = new AddToOrgSkillRepositoryHeaders([]);
        $addToOrgSkillRepositoryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addToOrgSkillRepositoryRequest = new AddToOrgSkillRepositoryRequest([
            "actionId" => "AGI-349e26ba-90e7-448a-b042-ddxxxxxx",
            "actionVersion" => "1.x.x",
            "operatorUnionId" => "RHCAZvgbllRse8xrxxxxxxxx"
        ]);
        try {
            $client->addToOrgSkillRepositoryWithOptions($addToOrgSkillRepositoryRequest, $addToOrgSkillRepositoryHeaders, new RuntimeOptions([]));
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
  dingtalkassistant_1_0  "github.com/alibabacloud-go/dingtalk/assistant_1_0"
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
func CreateClient () (_result *dingtalkassistant_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkassistant_1_0.Client{}
  _result, _err = dingtalkassistant_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addToOrgSkillRepositoryHeaders := &dingtalkassistant_1_0.AddToOrgSkillRepositoryHeaders{}
  addToOrgSkillRepositoryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addToOrgSkillRepositoryRequest := &dingtalkassistant_1_0.AddToOrgSkillRepositoryRequest{
    ActionId: tea.String("AGI-349e26ba-90e7-448a-b042-ddxxxxxx"),
    ActionVersion: tea.String("1.x.x"),
    OperatorUnionId: tea.String("RHCAZvgbllRse8xrxxxxxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddToOrgSkillRepositoryWithOptions(addToOrgSkillRepositoryRequest, addToOrgSkillRepositoryHeaders, &util.RuntimeOptions{})
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
const dingtalkassistant_1_0 = require('@alicloud/dingtalk/assistant_1_0');
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
    return new dingtalkassistant_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let addToOrgSkillRepositoryHeaders = new dingtalkassistant_1_0.AddToOrgSkillRepositoryHeaders({ });
    addToOrgSkillRepositoryHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let addToOrgSkillRepositoryRequest = new dingtalkassistant_1_0.AddToOrgSkillRepositoryRequest({
      actionId: 'AGI-349e26ba-90e7-448a-b042-ddxxxxxx',
      actionVersion: '1.x.x',
      operatorUnionId: 'RHCAZvgbllRse8xrxxxxxxxx',
    });
    try {
      await client.addToOrgSkillRepositoryWithOptions(addToOrgSkillRepositoryRequest, addToOrgSkillRepositoryHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkassistant_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkassistant_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.AddToOrgSkillRepositoryHeaders addToOrgSkillRepositoryHeaders = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.AddToOrgSkillRepositoryHeaders();
            addToOrgSkillRepositoryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.AddToOrgSkillRepositoryRequest addToOrgSkillRepositoryRequest = new AlibabaCloud.SDK.Dingtalkassistant_1_0.Models.AddToOrgSkillRepositoryRequest
            {
                ActionId = "AGI-349e26ba-90e7-448a-b042-ddxxxxxx",
                ActionVersion = "1.x.x",
                OperatorUnionId = "RHCAZvgbllRse8xrxxxxxxxx",
            };
            try
            {
                client.AddToOrgSkillRepositoryWithOptions(addToOrgSkillRepositoryRequest, addToOrgSkillRepositoryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | system.error | 系统异常 | 系统异常 |
| 500 | invalid.parameter | 非法参数 | 非法参数 |
| 500 | action.already.exist | 技能已发布到组织技能库，请勿重复发布 | 技能已发布到组织技能库，请勿重复发布 |
| 500 | plugin.not.exist | 插件不存在 | 插件不存在 |
| 500 | no.permission | 无权限，请联系管理员执行该操作 | 无权限，请联系管理员执行该操作 |
| 500 | get.uid.fail | unionId异常，请检查所属组织信息是否正确 | unionId异常，请检查所属组织信息是否正确 |
| 500 | org.benefit.error | 当前组织无操作组织技能库权益，请联系管理员升级钉钉版本权益后进行使用（E000335） | 当前组织无操作组织技能库权益，请联系管理员升级钉钉版本权益后进行使用（E000335） |
