---
title: "创建钉工牌电子码"
source_url: "https://open.dingtalk.com/document/development/create-a-badge-user-instance"
namespace: "development"
slug: "create-a-badge-user-instance"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 钉工牌 > 创建钉工牌电子码"
doc_id: "FtB2BFE1XD"
updated_at: "2025-09-11 21:03:33"
---

> Source: https://open.dingtalk.com/document/development/create-a-badge-user-instance
> Path: 应用开发 / 服务端API / 更多开放 > 钉工牌 > 创建钉工牌电子码
> Updated: 2025-09-11 21:03:33

# 创建钉工牌电子码

调用本接口，为用户创建钉工牌电子码实例，目前仅支持创建访客、会展等临时码场景。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/badge/codes/userInstances |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Badge.Common.Write-钉工牌基础数据写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| requestId | String | 是 | 业务幂等ID，由调用方随机生成。 |
| codeIdentity | String | 是 | 码标识，取值：   - **DT\_VISITOR**：访客码 - **DT\_CONFERENCE**：会展码 |
| codeValue | String | 否 | 码值，由调用方生成。       - 如果是固定码，则此参数必填。 - 如果是动态码，则此参数不填。 |
| codeValueType | String | 否 | 码值类型，可不传，默认为DING\_STATIC。 |
| status | String | 是 | 状态，传入关闭状态需要用户手动开启后才会渲染二维码。   - **OPEN**：开启 - **CLOSED**：关闭 - **INVALID**：失效 |
| corpId | String | 是 | 企业corpId。可在[钉钉开发者后台](https://open-dev.dingtalk.com/#/)首页查看。 |
| userCorpRelationType | String | 是 | 用户和企业的关系类型，用于区分内部员工，外部联系人，无关系普通用户。   - **INTERNAL\_STAFF**：企业内部员工 - **EXTERNAL\_CONTACT**：外部联系人 - **NO\_RELATION**：普通用户与组织无关 |
| userIdentity | String | 是 | 用户身份标识。取值和userCorpRelationType参数值有关。   - 如果是企业内部用户，通过[获取部门用户详情](0062-queries-the-complete-information-of-a-department-user.md)接口传用户的userId。 - 如果是外部联系人通过[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口传外部联系人的userid。 - 如果是无关系用户需传入用户手机号，手机号需带有国家码，例如86-xxxxxxxxxxx。 |
| gmtExpired | String | 是 | 临时码过期时间，格式：yyyy-MM-dd HH:mm:ss。 |
| availableTimes | Array | 是 | 有效时间列表，对于连续时间段，只需传入一个对象即可。      过期时间必须晚于最晚结束时间。 |
| gmtStart | String | 是 | 开始时间，格式：yyyy-MM-dd HH:mm:ss。  例如：`2021-10-20 00:00:00`。 |
| gmtEnd | String | 是 | 结束时间，格式：yyyy-MM-dd HH:mm:ss。  例如：`2021-11-20 00:00:00`。 |
| extInfo | Map | 是 | 扩展参数。 以下四个字段必传：   - **applicantName**：申请人名称 - **applyTime**：申请时间，格式：yyyy-MM-dd HH:mm:ss - **visitorName**：访客名称 - **visitorMobile**：访客手机号   示例：   ``` {     "applicantName":"xx",     "applyTime":"2021-10-25 12:12:12",     "visitorName":"小红",     "visitorMobile":"86-12345678901" } ``` |

### 请求示例

HTTP

```
POST /v1.0/badge/codes/userInstances HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "requestId" : "202102021212",
  "codeIdentity" : "DT_VISITOR",
  "codeValue" : "dingbadge111",
  "status" : "OPEN",
  "corpId" : "corpid1234",
  "userCorpRelationType" : "INTERNAL_STAFF",
  "userIdentity" : "86-xxxxxx",
  "gmtExpired" : "yyyy-MM-dd HH:mm:ss",
  "availableTimes" : [ {
    "gmtStart" : "yyyy-MM-dd HH:mm:ss",
    "gmtEnd" : "yyyy-MM-dd HH:mm:ss"
  } ],
  "extInfo":{
    "applicantName":"xx",
    "applyTime":"2021-10-25 12:12:12",
    "visitorName":"小红",
    "visitorMobile":"86-12345678901"
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkbadge_1_0.*;
import com.aliyun.dingtalkbadge_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkbadge_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkbadge_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkbadge_1_0.Client client = Sample.createClient();
        CreateBadgeCodeUserInstanceHeaders createBadgeCodeUserInstanceHeaders = new CreateBadgeCodeUserInstanceHeaders();
        createBadgeCodeUserInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes availableTimes0 = new CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes()
                .setGmtStart("yyyy-MM-dd HH:mm:ss")
                .setGmtEnd("yyyy-MM-dd HH:mm:ss");
        CreateBadgeCodeUserInstanceRequest createBadgeCodeUserInstanceRequest = new CreateBadgeCodeUserInstanceRequest()
                .setRequestId("202102021212")
                .setCodeIdentity("TEST")
                .setCodeValue("dingbadge111")
                .setStatus("OPEN")
                .setCorpId("corpid1234")
                .setUserCorpRelationType("INTERNAL_STAFF")
                .setUserIdentity("86-xxxxxx")
                .setGmtExpired("yyyy-MM-dd HH:mm:ss")
                .setAvailableTimes(java.util.Arrays.asList(
                    availableTimes0
                ));
        try {
            client.createBadgeCodeUserInstanceWithOptions(createBadgeCodeUserInstanceRequest, createBadgeCodeUserInstanceHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.badge_1_0.client import Client as dingtalkbadge_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.badge_1_0 import models as dingtalkbadge__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkbadge_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkbadge_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_badge_code_user_instance_headers = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceHeaders()
        create_badge_code_user_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        available_times_0 = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequestAvailableTimes(
            gmt_start='yyyy-MM-dd HH:mm:ss',
            gmt_end='yyyy-MM-dd HH:mm:ss'
        )
        create_badge_code_user_instance_request = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequest(
            request_id='202102021212',
            code_identity='TEST',
            code_value='dingbadge111',
            status='OPEN',
            corp_id='corpid1234',
            user_corp_relation_type='INTERNAL_STAFF',
            user_identity='86-xxxxxx',
            gmt_expired='yyyy-MM-dd HH:mm:ss',
            available_times=[
                available_times_0
            ]
        )
        try:
            client.create_badge_code_user_instance_with_options(create_badge_code_user_instance_request, create_badge_code_user_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_badge_code_user_instance_headers = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceHeaders()
        create_badge_code_user_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        available_times_0 = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequestAvailableTimes(
            gmt_start='yyyy-MM-dd HH:mm:ss',
            gmt_end='yyyy-MM-dd HH:mm:ss'
        )
        create_badge_code_user_instance_request = dingtalkbadge__1__0_models.CreateBadgeCodeUserInstanceRequest(
            request_id='202102021212',
            code_identity='TEST',
            code_value='dingbadge111',
            status='OPEN',
            corp_id='corpid1234',
            user_corp_relation_type='INTERNAL_STAFF',
            user_identity='86-xxxxxx',
            gmt_expired='yyyy-MM-dd HH:mm:ss',
            available_times=[
                available_times_0
            ]
        )
        try:
            await client.create_badge_code_user_instance_with_options_async(create_badge_code_user_instance_request, create_badge_code_user_instance_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\CreateBadgeCodeUserInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\CreateBadgeCodeUserInstanceRequest\availableTimes;
use AlibabaCloud\SDK\Dingtalk\Vbadge_1_0\Models\CreateBadgeCodeUserInstanceRequest;
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
        $createBadgeCodeUserInstanceHeaders = new CreateBadgeCodeUserInstanceHeaders([]);
        $createBadgeCodeUserInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $availableTimes0 = new availableTimes([
            "gmtStart" => "yyyy-MM-dd HH:mm:ss",
            "gmtEnd" => "yyyy-MM-dd HH:mm:ss"
        ]);
        $createBadgeCodeUserInstanceRequest = new CreateBadgeCodeUserInstanceRequest([
            "requestId" => "202102021212",
            "codeIdentity" => "TEST",
            "codeValue" => "dingbadge111",
            "status" => "OPEN",
            "corpId" => "corpid1234",
            "userCorpRelationType" => "INTERNAL_STAFF",
            "userIdentity" => "86-xxxxxx",
            "gmtExpired" => "yyyy-MM-dd HH:mm:ss",
            "availableTimes" => [
                $availableTimes0
            ]
        ]);
        try {
            $client->createBadgeCodeUserInstanceWithOptions($createBadgeCodeUserInstanceRequest, $createBadgeCodeUserInstanceHeaders, new RuntimeOptions([]));
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
  dingtalkbadge_1_0  "github.com/alibabacloud-go/dingtalk/badge_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkbadge_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkbadge_1_0.Client{}
  _result, _err = dingtalkbadge_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createBadgeCodeUserInstanceHeaders := &dingtalkbadge_1_0.CreateBadgeCodeUserInstanceHeaders{}
  createBadgeCodeUserInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  availableTimes0 := &dingtalkbadge_1_0.CreateBadgeCodeUserInstanceRequestAvailableTimes{
    GmtStart: tea.String("yyyy-MM-dd HH:mm:ss"),
    GmtEnd: tea.String("yyyy-MM-dd HH:mm:ss"),
  }
  createBadgeCodeUserInstanceRequest := &dingtalkbadge_1_0.CreateBadgeCodeUserInstanceRequest{
    RequestId: tea.String("202102021212"),
    CodeIdentity: tea.String("TEST"),
    CodeValue: tea.String("dingbadge111"),
    Status: tea.String("OPEN"),
    CorpId: tea.String("corpid1234"),
    UserCorpRelationType: tea.String("INTERNAL_STAFF"),
    UserIdentity: tea.String("86-xxxxxx"),
    GmtExpired: tea.String("yyyy-MM-dd HH:mm:ss"),
    AvailableTimes: []*dingtalkbadge_1_0.CreateBadgeCodeUserInstanceRequestAvailableTimes{availableTimes0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateBadgeCodeUserInstanceWithOptions(createBadgeCodeUserInstanceRequest, createBadgeCodeUserInstanceHeaders, &util.RuntimeOptions{})
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
import dingtalkbadge_1_0, * as $dingtalkbadge_1_0 from '@alicloud/dingtalk/badge_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkbadge_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkbadge_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createBadgeCodeUserInstanceHeaders = new $dingtalkbadge_1_0.CreateBadgeCodeUserInstanceHeaders({ });
    createBadgeCodeUserInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let availableTimes0 = new $dingtalkbadge_1_0.CreateBadgeCodeUserInstanceRequestAvailableTimes({
      gmtStart: "yyyy-MM-dd HH:mm:ss",
      gmtEnd: "yyyy-MM-dd HH:mm:ss",
    });
    let createBadgeCodeUserInstanceRequest = new $dingtalkbadge_1_0.CreateBadgeCodeUserInstanceRequest({
      requestId: "202102021212",
      codeIdentity: "TEST",
      codeValue: "dingbadge111",
      status: "OPEN",
      corpId: "corpid1234",
      userCorpRelationType: "INTERNAL_STAFF",
      userIdentity: "86-xxxxxx",
      gmtExpired: "yyyy-MM-dd HH:mm:ss",
      availableTimes: [
        availableTimes0
      ],
    });
    try {
      await client.createBadgeCodeUserInstanceWithOptions(createBadgeCodeUserInstanceRequest, createBadgeCodeUserInstanceHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkbadge_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkbadge_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceHeaders createBadgeCodeUserInstanceHeaders = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceHeaders();
            createBadgeCodeUserInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes availableTimes0 = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes
            {
                GmtStart = "yyyy-MM-dd HH:mm:ss",
                GmtEnd = "yyyy-MM-dd HH:mm:ss",
            };
            AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceRequest createBadgeCodeUserInstanceRequest = new AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceRequest
            {
                RequestId = "202102021212",
                CodeIdentity = "TEST",
                CodeValue = "dingbadge111",
                Status = "OPEN",
                CorpId = "corpid1234",
                UserCorpRelationType = "INTERNAL_STAFF",
                UserIdentity = "86-xxxxxx",
                GmtExpired = "yyyy-MM-dd HH:mm:ss",
                AvailableTimes = new List<AlibabaCloud.SDK.Dingtalkbadge_1_0.Models.CreateBadgeCodeUserInstanceRequest.CreateBadgeCodeUserInstanceRequestAvailableTimes>
                {
                    availableTimes0
                },
            };
            try
            {
                client.CreateBadgeCodeUserInstanceWithOptions(createBadgeCodeUserInstanceRequest, createBadgeCodeUserInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkbadge__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkbadge_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkbadge_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::Client> client = make_shared<Alibabacloud_Dingtalkbadge_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceHeaders> createBadgeCodeUserInstanceHeaders = make_shared<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceHeaders>();
  createBadgeCodeUserInstanceHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceRequestAvailableTimes> availableTimes0 = make_shared<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceRequestAvailableTimes>(map<string, boost::any>({
    {"gmtStart", boost::any(string("yyyy-MM-dd HH:mm:ss"))},
    {"gmtEnd", boost::any(string("yyyy-MM-dd HH:mm:ss"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceRequest> createBadgeCodeUserInstanceRequest = make_shared<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceRequest>(map<string, boost::any>({
    {"requestId", boost::any(string("202102021212"))},
    {"codeIdentity", boost::any(string("TEST"))},
    {"codeValue", boost::any(string("dingbadge111"))},
    {"status", boost::any(string("OPEN"))},
    {"corpId", boost::any(string("corpid1234"))},
    {"userCorpRelationType", boost::any(string("INTERNAL_STAFF"))},
    {"userIdentity", boost::any(string("86-xxxxxx"))},
    {"gmtExpired", boost::any(string("yyyy-MM-dd HH:mm:ss"))},
    {"availableTimes", boost::any(vector<Alibabacloud_Dingtalkbadge_1_0::CreateBadgeCodeUserInstanceRequestAvailableTimes>({
      availableTimes0
    }))}
  }));
  try {
    client->createBadgeCodeUserInstanceWithOptions(createBadgeCodeUserInstanceRequest, createBadgeCodeUserInstanceHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| codeId | String | 码ID。 |
| codeDetailUrl | String | 码详情跳转地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "codeId" : "codexxxxxx",
  "codeDetailUrl" : "urlxxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | remoteServiceError | 远程服务错误 | 远程服务错误 |
| 400 | missingParameter | 缺少必要参数 | 缺少必要参数 |
| 400 | userNotInExtContact | 用户不在外部联系人 | 用户不在外部联系人 |
| 400 | invalidCodeIdentity | 非法的码标识 | 非法的码标识 |
| 400 | expiredTimeInvalid | 过期时间非法 | 过期时间非法 |
| 400 | corpNotOpen | 企业未开通指定的码 | 企业未开通指定的码 |
| 400 | noAuthority | 无权限调用 | 无权限调用 |
| 400 | userCodeExist | 用户码已存在 | 用户码已存在 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | invalidMobileFormat | 手机号格式非法 | 手机号格式非法 |
| 400 | notCorpStaff | 非企业内部员工 | 非企业内部员工 |
| 400 | invalidAvailableTime | 有效时间非法 | 有效时间非法 |
| 500 | unknownError | 未知错误 | 未知错误 |
