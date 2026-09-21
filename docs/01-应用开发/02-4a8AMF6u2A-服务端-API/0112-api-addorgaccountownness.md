---
title: "新增企业账号工作状态"
source_url: "https://open.dingtalk.com/document/development/api-addorgaccountownness"
namespace: "development"
slug: "api-addorgaccountownness"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 新增企业账号工作状态"
doc_id: "05n0G5r9xQ"
updated_at: "2026-09-21 17:06:41"
---

> Source: https://open.dingtalk.com/document/development/api-addorgaccountownness
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 新增企业账号工作状态
> Updated: 2026-09-21 17:06:41

# 新增企业账号工作状态

调用本接口，根据用户ID、业务标识ID和状态类型，增加用户企业账号的工作状态。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccounts/owness |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Contact.OrgAccountOwnness.Write-企业账号工作状态修改权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0033-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 员工id。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| ownnessId | Long | 是 | 业务标识ID，用于后续修改和删除用户企业账号的工作状态。 |
| text | String | 是 | 文案。 |
| ownenssType | Long | 是 | 状态类型，仅支持：   - **1**：请假中 - **3**：出差中 - **4**：会议中 - **7**：外出中 |
| startTime | Long | 是 | 开始时间戳。 |
| endTime | Long | 是 | 结束时间戳。 |

### **请求示例**

HTTP

```
POST /v1.0/contact/orgAccounts/owness?userId=123 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:abXXXXXX
Content-Type:application/json

{
  "ownnessId" : 123,
  "text" : "会议中",
  "ownenssType" : 2,
  "startTime" : 1698335999000,
  "endTime" : 1698335999000
}
```

Java

```
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
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.AddOrgAccountOwnnessHeaders addOrgAccountOwnnessHeaders = new com.aliyun.dingtalkcontact_1_0.models.AddOrgAccountOwnnessHeaders();
        addOrgAccountOwnnessHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.AddOrgAccountOwnnessRequest addOrgAccountOwnnessRequest = new com.aliyun.dingtalkcontact_1_0.models.AddOrgAccountOwnnessRequest()
                .setUserId("123")
                .setOwnnessId(123L)
                .setText("会议中")
                .setOwnenssType(2L)
                .setStartTime(1698335999000L)
                .setEndTime(1698335999000L);
        try {
            client.addOrgAccountOwnnessWithOptions(addOrgAccountOwnnessRequest, addOrgAccountOwnnessHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

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
        add_org_account_ownness_headers = dingtalkcontact__1__0_models.AddOrgAccountOwnnessHeaders()
        add_org_account_ownness_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_org_account_ownness_request = dingtalkcontact__1__0_models.AddOrgAccountOwnnessRequest(
            user_id='123',
            ownness_id=123,
            text='会议中',
            ownenss_type=2,
            start_time=1698335999000,
            end_time=1698335999000
        )
        try:
            client.add_org_account_ownness_with_options(add_org_account_ownness_request, add_org_account_ownness_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_org_account_ownness_headers = dingtalkcontact__1__0_models.AddOrgAccountOwnnessHeaders()
        add_org_account_ownness_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_org_account_ownness_request = dingtalkcontact__1__0_models.AddOrgAccountOwnnessRequest(
            user_id='123',
            ownness_id=123,
            text='会议中',
            ownenss_type=2,
            start_time=1698335999000,
            end_time=1698335999000
        )
        try:
            await client.add_org_account_ownness_with_options_async(add_org_account_ownness_request, add_org_account_ownness_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\AddOrgAccountOwnnessHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\AddOrgAccountOwnnessRequest;
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
        $addOrgAccountOwnnessHeaders = new AddOrgAccountOwnnessHeaders([]);
        $addOrgAccountOwnnessHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addOrgAccountOwnnessRequest = new AddOrgAccountOwnnessRequest([
            "userId" => "123",
            "ownnessId" => 123,
            "text" => "会议中",
            "ownenssType" => 2,
            "startTime" => 1698335999000,
            "endTime" => 1698335999000
        ]);
        try {
            $client->addOrgAccountOwnnessWithOptions($addOrgAccountOwnnessRequest, $addOrgAccountOwnnessHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
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

  addOrgAccountOwnnessHeaders := &dingtalkcontact_1_0.AddOrgAccountOwnnessHeaders{}
  addOrgAccountOwnnessHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addOrgAccountOwnnessRequest := &dingtalkcontact_1_0.AddOrgAccountOwnnessRequest{
    UserId: tea.String("123"),
    OwnnessId: tea.Int64(123),
    Text: tea.String("会议中"),
    OwnenssType: tea.Int64(2),
    StartTime: tea.Int64(1698335999000),
    EndTime: tea.Int64(1698335999000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddOrgAccountOwnnessWithOptions(addOrgAccountOwnnessRequest, addOrgAccountOwnnessHeaders, &util.RuntimeOptions{})
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
const dingtalkcontact_1_0 = require('@alicloud/dingtalk/contact_1_0');
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
    return new dingtalkcontact_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let addOrgAccountOwnnessHeaders = new dingtalkcontact_1_0.AddOrgAccountOwnnessHeaders({ });
    addOrgAccountOwnnessHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let addOrgAccountOwnnessRequest = new dingtalkcontact_1_0.AddOrgAccountOwnnessRequest({
      userId: '123',
      ownnessId: 123,
      text: '会议中',
      ownenssType: 2,
      startTime: 1698335999000,
      endTime: 1698335999000,
    });
    try {
      await client.addOrgAccountOwnnessWithOptions(addOrgAccountOwnnessRequest, addOrgAccountOwnnessHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.AddOrgAccountOwnnessHeaders addOrgAccountOwnnessHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.AddOrgAccountOwnnessHeaders();
            addOrgAccountOwnnessHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.AddOrgAccountOwnnessRequest addOrgAccountOwnnessRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.AddOrgAccountOwnnessRequest
            {
                UserId = "123",
                OwnnessId = 123,
                Text = "会议中",
                OwnenssType = 2,
                StartTime = 1698335999000,
                EndTime = 1698335999000,
            };
            try
            {
                client.AddOrgAccountOwnnessWithOptions(addOrgAccountOwnnessRequest, addOrgAccountOwnnessHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Long | 业务标识ID，与`ownnessId`保持一致。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : 123456
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | 参数异常 | 参数异常 |
| 400 | emp.not.exist | 员工不存在 | 员工不存在 |
| 400 | user.not.exist | 用户不存在 | 用户不存在 |
| 400 | org.account.only | 只允许修改企业账号 | 只允许修改企业账号 |
| 400 | org.account.notCurr | 只允许修改本企业的企业账号 | 只允许修改本企业的企业账号 |
| 400 | endTime.expired | 结束时间小于当前时间，已过期 | 结束时间小于当前时间，已过期 |
| 400 | startTime.max.endTime | 开始时间不能大于结束时间 | 开始时间不能大于结束时间 |
| 400 | ownessType.update.close | 用户已关闭此类型状态同步 | 用户已关闭此类型状态同步 |
| 400 | owness.exist | 状态已存在 | 状态已存在 |
| 500 | system.error | 更新配置异常 | 更新配置异常 |
