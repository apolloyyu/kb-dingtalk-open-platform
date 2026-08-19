---
title: "获取单个客户群详情"
source_url: "https://open.dingtalk.com/document/development/obtain-a-single-customer-group"
namespace: "development"
slug: "obtain-a-single-customer-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 获取单个客户群详情"
doc_id: "KkD2HzjBXY"
updated_at: "2025-10-09 18:06:22"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-single-customer-group
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户群 > 获取单个客户群详情
> Updated: 2025-10-09 18:06:22

# 获取单个客户群详情

调用本接口，获取单个客户群的详情数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/crmGroupChats/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Crm.CustomerGroup.Read-客户管理客户群读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 客户群openConversationId，调用[查询客户群列表](1380-query-the-list-of-customer-groups.md)接口获取openConversationId参数值。 |

### 请求示例

HTTP

```
POST /v1.0/crm/crmGroupChats/query?openConversationId=afasd1321 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:asfsda
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcrm_1_0.*;
import com.aliyun.dingtalkcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        GetCrmGroupChatSingleHeaders getCrmGroupChatSingleHeaders = new GetCrmGroupChatSingleHeaders();
        getCrmGroupChatSingleHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetCrmGroupChatSingleRequest getCrmGroupChatSingleRequest = new GetCrmGroupChatSingleRequest()
                .setOpenConversationId("afasd1321");
        try {
            client.getCrmGroupChatSingleWithOptions(getCrmGroupChatSingleRequest, getCrmGroupChatSingleHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_crm_group_chat_single_headers = dingtalkcrm__1__0_models.GetCrmGroupChatSingleHeaders()
        get_crm_group_chat_single_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_crm_group_chat_single_request = dingtalkcrm__1__0_models.GetCrmGroupChatSingleRequest(
            open_conversation_id='afasd1321'
        )
        try:
            client.get_crm_group_chat_single_with_options(get_crm_group_chat_single_request, get_crm_group_chat_single_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_crm_group_chat_single_headers = dingtalkcrm__1__0_models.GetCrmGroupChatSingleHeaders()
        get_crm_group_chat_single_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_crm_group_chat_single_request = dingtalkcrm__1__0_models.GetCrmGroupChatSingleRequest(
            open_conversation_id='afasd1321'
        )
        try:
            await client.get_crm_group_chat_single_with_options_async(get_crm_group_chat_single_request, get_crm_group_chat_single_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetCrmGroupChatSingleHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetCrmGroupChatSingleRequest;
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
        $getCrmGroupChatSingleHeaders = new GetCrmGroupChatSingleHeaders([]);
        $getCrmGroupChatSingleHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getCrmGroupChatSingleRequest = new GetCrmGroupChatSingleRequest([
            "openConversationId" => "afasd1321"
        ]);
        try {
            $client->getCrmGroupChatSingleWithOptions($getCrmGroupChatSingleRequest, $getCrmGroupChatSingleHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getCrmGroupChatSingleHeaders := &dingtalkcrm_1_0.GetCrmGroupChatSingleHeaders{}
  getCrmGroupChatSingleHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getCrmGroupChatSingleRequest := &dingtalkcrm_1_0.GetCrmGroupChatSingleRequest{
    OpenConversationId: tea.String("afasd1321"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetCrmGroupChatSingleWithOptions(getCrmGroupChatSingleRequest, getCrmGroupChatSingleHeaders, &util.RuntimeOptions{})
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetCrmGroupChatSingleHeaders getCrmGroupChatSingleHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetCrmGroupChatSingleHeaders();
            getCrmGroupChatSingleHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetCrmGroupChatSingleRequest getCrmGroupChatSingleRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetCrmGroupChatSingleRequest
            {
                OpenConversationId = "afasd1321",
            };
            try
            {
                client.GetCrmGroupChatSingleWithOptions(getCrmGroupChatSingleRequest, getCrmGroupChatSingleHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::GetCrmGroupChatSingleHeaders> getCrmGroupChatSingleHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::GetCrmGroupChatSingleHeaders>();
  getCrmGroupChatSingleHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::GetCrmGroupChatSingleRequest> getCrmGroupChatSingleRequest = make_shared<Alibabacloud_Dingtalkcrm_1_0::GetCrmGroupChatSingleRequest>(map<string, boost::any>({
    {"openConversationId", boost::any(string("afasd1321"))}
  }));
  try {
    client->getCrmGroupChatSingleWithOptions(getCrmGroupChatSingleRequest, getCrmGroupChatSingleHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| openConversationId | String | 客户群openConversationId。 |
| openGroupSetId | String | 客户群所在的群组openGroupSetId。   - 如果是客户群组裂变出的客户群，会返回该字段。 - 如果是调用[创建客户群](1379-create-a-customer-group.md)接口创建的客户群，不返回该字段。 |
| ownerUserId | String | 群主的userId。 |
| ownerUserName | String | 群主的名字。 |
| name | String | 客户群的名称。 |
| memberCount | Integer | 客户群成员数量。 |
| gmtCreate | Long | 客户群的创建时间戳，单位毫秒。 |
| iconUrl | String | 群头像地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "openConversationId" : "abc123",
  "openGroupSetId" : "abc123",
  "ownerUserId" : "abc123",
  "ownerUserName" : "abc123",
  "name" : "营销1群",
  "memberCount" : 10,
  "gmtCreate" : 1640270012301,
  "iconUrl" : "https://static/xx.com/xx.jpg"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | incorrectOpenConversationId | %s | openConversionId不存在 |
| 500 | systemError | %s | 系统错误 |
