---
title: "创建或更新业务分组"
source_url: "https://open.dingtalk.com/document/development/api-premiuminsertorupdatedir"
namespace: "development"
slug: "api-premiuminsertorupdatedir"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 高级版专享接口 > 自有 OA 审批 > 业务分组 > 创建或更新业务分组"
doc_id: "LZsX7Q2LoD"
updated_at: "2026-06-03 10:12:58"
---

> Source: https://open.dingtalk.com/document/development/api-premiuminsertorupdatedir
> Path: 应用开发 / 服务端API / OA 审批 > 高级版专享接口 > 自有 OA 审批 > 业务分组 > 创建或更新业务分组
> Updated: 2026-06-03 10:12:58

# 创建或更新业务分组

调用本接口，可以将三方系统内的业务分组信息同步到钉钉OA审批，并生成对应的钉钉待办任务OA审批分类下的二级业务来源分组。后续在同步待处理任务至钉钉时，可支持指定待办任务所属的业务分组信息，让审批人在查阅三方业务系统来源待办更清晰。

## **接口调用说明**

> **[!NOTE]**
>
> 当前接口为[OA高级版](dingtalk://dingtalkclient/page/link?url=https%3A%2F%2Fpage.dingtalk.com%2Fwow%2Fdingtalk%2Fdefault%2Fdingtalk%2FlnfR8GaRSWqNncZHSvLLx%3Fdd_mini_app_id%3D5000000004997171&web_wnd=general&width=480&height=800)专享接口，升级OA高级版可用，可满足更高级的开发需求，响应个性化的业务场景。[查看全部专享OpenAPI](https://open.dingtalk.com/document/orgapp/description-of-new-oa-approval-premium-exclusive-openapi-and-solutions#a56c9869e4v0i)

- 调用本接口创建分组，接口返回的分组ID请务必注意保存，方便后续调用其他接口使用。
- 单个组织在同一个应用内最多支持创建10个分组。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/premium/processCentres/directories |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Premium.Workflow.ReadWrite.All-OA审批工作流读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| bizGroup | String | 是 | 业务分组ID，调用方提供的自定义唯一分组标识。      为了保证不同三方系统同步的业务分组ID在钉钉侧唯一，钉钉侧将对业务传递的分组ID进行逻辑转换，规则如下：${应用appId} + \_ + ${bizGroup}。 |
| operateUserId | String | 是 | 操作人userId。 |
| name | String | 是 | 分组名称。 |
| name18n | String | 是 | 支持国际化的分组名称，json字符串格式。 |
| description | String | 否 | 分组描述。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/premium/processCentres/directories HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6dexxx
Content-Type:application/json

{
  "bizGroup" : "administeration",
  "operateUserId" : "user001",
  "name" : "行政管理",
  "name18n" : "{\\\"en_US\\\":\\\"test\\\",\\\"ja_JP\\\":\\\"test\\\",\\\"vi_VN\\\":\\\"test\\\",\\\"zh_CN\\\":\\\"测试\\\",\\\"zh_HK\\\":\\\"测试\\\",\\\"zh_TW\\\":\\\"测试\\\"}",
  "description" : "分组描述信息"
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.PremiumInsertOrUpdateDirHeaders premiumInsertOrUpdateDirHeaders = new com.aliyun.dingtalkworkflow_1_0.models.PremiumInsertOrUpdateDirHeaders();
        premiumInsertOrUpdateDirHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.PremiumInsertOrUpdateDirRequest premiumInsertOrUpdateDirRequest = new com.aliyun.dingtalkworkflow_1_0.models.PremiumInsertOrUpdateDirRequest()
                .setBizGroup("administeration")
                .setOperateUserId("user001")
                .setName("行政管理")
                .setName18n("{\"en_US\":\"test\",\"ja_JP\":\"test\",\"vi_VN\":\"test\",\"zh_CN\":\"测试\",\"zh_HK\":\"测试\",\"zh_TW\":\"测试\"}")
                .setDescription("分组描述信息");
        try {
            client.premiumInsertOrUpdateDirWithOptions(premiumInsertOrUpdateDirRequest, premiumInsertOrUpdateDirHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_insert_or_update_dir_headers = dingtalkworkflow__1__0_models.PremiumInsertOrUpdateDirHeaders()
        premium_insert_or_update_dir_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_insert_or_update_dir_request = dingtalkworkflow__1__0_models.PremiumInsertOrUpdateDirRequest(
            biz_group='administeration',
            operate_user_id='user001',
            name='行政管理',
            name_18n='{"en_US":"test","ja_JP":"test","vi_VN":"test","zh_CN":"测试","zh_HK":"测试","zh_TW":"测试"}',
            description='分组描述信息'
        )
        try:
            client.premium_insert_or_update_dir_with_options(premium_insert_or_update_dir_request, premium_insert_or_update_dir_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        premium_insert_or_update_dir_headers = dingtalkworkflow__1__0_models.PremiumInsertOrUpdateDirHeaders()
        premium_insert_or_update_dir_headers.x_acs_dingtalk_access_token = '<your access token>'
        premium_insert_or_update_dir_request = dingtalkworkflow__1__0_models.PremiumInsertOrUpdateDirRequest(
            biz_group='administeration',
            operate_user_id='user001',
            name='行政管理',
            name_18n='{"en_US":"test","ja_JP":"test","vi_VN":"test","zh_CN":"测试","zh_HK":"测试","zh_TW":"测试"}',
            description='分组描述信息'
        )
        try:
            await client.premium_insert_or_update_dir_with_options_async(premium_insert_or_update_dir_request, premium_insert_or_update_dir_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumInsertOrUpdateDirHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\PremiumInsertOrUpdateDirRequest;
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
        $premiumInsertOrUpdateDirHeaders = new PremiumInsertOrUpdateDirHeaders([]);
        $premiumInsertOrUpdateDirHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $premiumInsertOrUpdateDirRequest = new PremiumInsertOrUpdateDirRequest([
            "bizGroup" => "administeration",
            "operateUserId" => "user001",
            "name" => "行政管理",
            "name18n" => "{\"en_US\":\"test\",\"ja_JP\":\"test\",\"vi_VN\":\"test\",\"zh_CN\":\"测试\",\"zh_HK\":\"测试\",\"zh_TW\":\"测试\"}",
            "description" => "分组描述信息"
        ]);
        try {
            $client->premiumInsertOrUpdateDirWithOptions($premiumInsertOrUpdateDirRequest, $premiumInsertOrUpdateDirHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
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
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  premiumInsertOrUpdateDirHeaders := &dingtalkworkflow_1_0.PremiumInsertOrUpdateDirHeaders{}
  premiumInsertOrUpdateDirHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  premiumInsertOrUpdateDirRequest := &dingtalkworkflow_1_0.PremiumInsertOrUpdateDirRequest{
    BizGroup: tea.String("administeration"),
    OperateUserId: tea.String("user001"),
    Name: tea.String("行政管理"),
    Name18n: tea.String("{\"en_US\":\"test\",\"ja_JP\":\"test\",\"vi_VN\":\"test\",\"zh_CN\":\"测试\",\"zh_HK\":\"测试\",\"zh_TW\":\"测试\"}"),
    Description: tea.String("分组描述信息"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.PremiumInsertOrUpdateDirWithOptions(premiumInsertOrUpdateDirRequest, premiumInsertOrUpdateDirHeaders, &util.RuntimeOptions{})
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
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
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
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let premiumInsertOrUpdateDirHeaders = new dingtalkworkflow_1_0.PremiumInsertOrUpdateDirHeaders({ });
    premiumInsertOrUpdateDirHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let premiumInsertOrUpdateDirRequest = new dingtalkworkflow_1_0.PremiumInsertOrUpdateDirRequest({
      bizGroup: 'administeration',
      operateUserId: 'user001',
      name: '行政管理',
      name18n: '{"en_US":"test","ja_JP":"test","vi_VN":"test","zh_CN":"测试","zh_HK":"测试","zh_TW":"测试"}',
      description: '分组描述信息',
    });
    try {
      await client.premiumInsertOrUpdateDirWithOptions(premiumInsertOrUpdateDirRequest, premiumInsertOrUpdateDirHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumInsertOrUpdateDirHeaders premiumInsertOrUpdateDirHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumInsertOrUpdateDirHeaders();
            premiumInsertOrUpdateDirHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumInsertOrUpdateDirRequest premiumInsertOrUpdateDirRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.PremiumInsertOrUpdateDirRequest
            {
                BizGroup = "administeration",
                OperateUserId = "user001",
                Name = "行政管理",
                Name18n = "{\"en_US\":\"test\",\"ja_JP\":\"test\",\"vi_VN\":\"test\",\"zh_CN\":\"测试\",\"zh_HK\":\"测试\",\"zh_TW\":\"测试\"}",
                Description = "分组描述信息",
            };
            try
            {
                client.PremiumInsertOrUpdateDirWithOptions(premiumInsertOrUpdateDirRequest, premiumInsertOrUpdateDirHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| dirId | String | 分组ID。 |
| bizGroup | String | 业务分组ID，调用方提供的自定义唯一分组标识。 |
| success | Boolean | 是否创建成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "dirId" : "oaDirIdxxx",
    "bizGroup" : "{应用appId}_administeration"
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | bizDir.number.exceed | 分组的数量到达上限，每个应用最多支持创建10个分组 | 分组的数量到达上限，每个应用最多支持创建10个分组，请先清理无效分组。 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | insertOrUpdate.dir.error | 创建/更新分组失败 | 创建/更新分组失败，可能原因为分组数量达到上限等。 |
| 400 | user.not.exist | 用户不存在 | 用户不存在，请检查operateUserId参数是否正确。 |
| 400 | todo.bizcategory.error | 同步待办分组失败 | 同步待办分组失败，请稍后重试。 |
| 400 | illegal.parameter | 参数错误 | 参数错误，请检查入参。 |
| 400 | dirName.validation.failed | 目录名称校验失败 | 目录名称校验失败，不能重名，请检查入参。 |
| 400 | oaplus.query.limit | 请求过于频繁，稍后重试 | 企业访问并发超过限制 |
| 400 | benefit.status.invalid | 权益校验失败，未开通或过期 | 权益校验 |
| 400 | benefit.query.error | 权益查询失败 | 权益系统查询失败 |
| 500 | system.error | 系统错误 | 系统错误 |
