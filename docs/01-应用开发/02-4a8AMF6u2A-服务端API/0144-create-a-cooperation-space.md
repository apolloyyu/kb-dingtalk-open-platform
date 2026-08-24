---
title: "创建上下游组织"
source_url: "https://open.dingtalk.com/document/development/create-a-cooperation-space"
namespace: "development"
slug: "create-a-cooperation-space"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 创建上下游组织"
doc_id: "oLgFCOlK8p"
updated_at: "2026-06-02 09:24:46"
---

> Source: https://open.dingtalk.com/document/development/create-a-cooperation-space
> Path: 应用开发 / 服务端API / 通讯录管理 > 上下游组织（原合作空间） > 创建上下游组织
> Updated: 2026-06-02 09:24:46

# 创建上下游组织

调用本接口，创建上下游组织。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/cooperateCorps |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Contact.CooperateCorp.Write-通讯录上下游组织写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| orgName | String | 是 | 上下游组织名称。 |
| logoMediaId | String | 否 | 上下游组织的logo，调用[上传媒体文件](0646-upload-media-files.md)接口获取图片的media\_id参数值。 |
| industryCode | Long | 否 | 行业code。 |

### 请求示例

HTTP

```
POST /v1.0/contact/cooperateCorps HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BFXXXXX
Content-Type:application/json

{
  "orgName" : "测试联盟",
  "logoMediaId" : "mediaId",
  "industryCode" : 123456
}
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
        CreateCooperateOrgHeaders createCooperateOrgHeaders = new CreateCooperateOrgHeaders();
        createCooperateOrgHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateCooperateOrgRequest createCooperateOrgRequest = new CreateCooperateOrgRequest()
                .setOrgName("测试联盟")
                .setLogoMediaId("mediaId")
                .setIndustryCode(123456L);
        try {
            client.createCooperateOrgWithOptions(createCooperateOrgRequest, createCooperateOrgHeaders, new RuntimeOptions());
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
        create_cooperate_org_headers = dingtalkcontact__1__0_models.CreateCooperateOrgHeaders()
        create_cooperate_org_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_cooperate_org_request = dingtalkcontact__1__0_models.CreateCooperateOrgRequest(
            org_name='测试联盟',
            logo_media_id='mediaId',
            industry_code=123456
        )
        try:
            client.create_cooperate_org_with_options(create_cooperate_org_request, create_cooperate_org_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_cooperate_org_headers = dingtalkcontact__1__0_models.CreateCooperateOrgHeaders()
        create_cooperate_org_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_cooperate_org_request = dingtalkcontact__1__0_models.CreateCooperateOrgRequest(
            org_name='测试联盟',
            logo_media_id='mediaId',
            industry_code=123456
        )
        try:
            await client.create_cooperate_org_with_options_async(create_cooperate_org_request, create_cooperate_org_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\CreateCooperateOrgHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\CreateCooperateOrgRequest;
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
        $createCooperateOrgHeaders = new CreateCooperateOrgHeaders([]);
        $createCooperateOrgHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createCooperateOrgRequest = new CreateCooperateOrgRequest([
            "orgName" => "测试联盟",
            "logoMediaId" => "mediaId",
            "industryCode" => 123456
        ]);
        try {
            $client->createCooperateOrgWithOptions($createCooperateOrgRequest, $createCooperateOrgHeaders, new RuntimeOptions([]));
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

  createCooperateOrgHeaders := &dingtalkcontact_1_0.CreateCooperateOrgHeaders{}
  createCooperateOrgHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createCooperateOrgRequest := &dingtalkcontact_1_0.CreateCooperateOrgRequest{
    OrgName: tea.String("测试联盟"),
    LogoMediaId: tea.String("mediaId"),
    IndustryCode: tea.Int64(123456),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateCooperateOrgWithOptions(createCooperateOrgRequest, createCooperateOrgHeaders, &util.RuntimeOptions{})
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
    let createCooperateOrgHeaders = new $dingtalkcontact_1_0.CreateCooperateOrgHeaders({ });
    createCooperateOrgHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createCooperateOrgRequest = new $dingtalkcontact_1_0.CreateCooperateOrgRequest({
      orgName: "测试联盟",
      logoMediaId: "mediaId",
      industryCode: 123456,
    });
    try {
      await client.createCooperateOrgWithOptions(createCooperateOrgRequest, createCooperateOrgHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.CreateCooperateOrgHeaders createCooperateOrgHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.CreateCooperateOrgHeaders();
            createCooperateOrgHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.CreateCooperateOrgRequest createCooperateOrgRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.CreateCooperateOrgRequest
            {
                OrgName = "测试联盟",
                LogoMediaId = "mediaId",
                IndustryCode = 123456,
            };
            try
            {
                client.CreateCooperateOrgWithOptions(createCooperateOrgRequest, createCooperateOrgHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::CreateCooperateOrgHeaders> createCooperateOrgHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::CreateCooperateOrgHeaders>();
  createCooperateOrgHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::CreateCooperateOrgRequest> createCooperateOrgRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::CreateCooperateOrgRequest>(map<string, boost::any>({
    {"orgName", boost::any(string("测试联盟"))},
    {"logoMediaId", boost::any(string("mediaId"))},
    {"industryCode", boost::any(123456)}
  }));
  try {
    client->createCooperateOrgWithOptions(createCooperateOrgRequest, createCooperateOrgHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| cooperateCorpId | String | 上下游组织的CorpId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "cooperateCorpId" : "corpidxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.blank | 参数为空 | 参数为空 |
| 400 | parameter.error | 归属企业不存在 | 归属企业不存在 |
| 500 | system.error | 系统错误 | 系统错误 |
