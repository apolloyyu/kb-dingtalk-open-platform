---
title: "批量获取服务窗联系人数据"
source_url: "https://open.dingtalk.com/document/development/obtain-contact-data-from-the-service-window"
namespace: "development"
slug: "obtain-contact-data-from-the-service-window"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 批量获取服务窗联系人数据"
doc_id: "2vXTGHMigm"
updated_at: "2025-09-08 19:07:58"
---

> Source: https://open.dingtalk.com/document/development/obtain-contact-data-from-the-service-window
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 客户管理（官方CRM） > 服务窗 > 批量获取服务窗联系人数据
> Updated: 2025-09-08 19:07:58

# 批量获取服务窗联系人数据

调用本接口分页获取服务窗联系人数据。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，客户管理的服务窗接口已升级。客户管理-服务窗API文档已于2022年11月30日移动至历史文档（不推荐）目录，接口不再支持新应用接入，已接入的应用可继续调用。
>
> - 如果未使用本接口，推荐使用[批量获取关注服务窗用户信息](https://open.dingtalk.com/document/orgapp/obtains-the-follower-information-from-the-service-window)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

例如，在服务窗页面单击左侧菜单栏的用户管理，查看服务窗用户信息列表，调用本接口获取的信息，包括用户的创建时间、用户昵称等。如图
![](https://img.alicdn.com/imgextra/i3/O1CN01FIVzA11WrDxyX7YTp_!!6000000002841-2-tps-2874-1238.png)

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | — | — |
| 第三方企业应用 | 支持 | — | — |
| 第三方个人应用 | 暂不支持 | — | — |

## 请求方法

```
GET /v1.0/crm/officialAccounts/contacts?nextToken=String&maxResults=Long HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | String | 是 | 分页游标。   - 如果是首次查询，nextToken值传空。 - 如果查询结果nextToken为null，表示已获取全部数据。 - 如果查询结果返回nextToken值，表示未获取到全部数据，需传入该nextToken值继续查询。 |
| maxResults | Long | 是 | 查询返回结果数，最大值10。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| nextToken | String | 分页游标。   - 如果查询结果nextToken为null，表示已获取全部数据。 - 如果查询结果返回nextToken值，表示未获取到全部数据，需传入该nextToken值继续查询。 |
| maxResults | Long | 分页大小。 |
| values | Array | 服务窗联系人信息列表。 |
| userId | String | 用户userid。 |
| contacts | Array | 用户的联系人数据列表。 |
| creatorNick | String | 创建记录的用户昵称。 |
| modifyTime | String | 记录修改时间。 |
| createTime | String | 记录创建时间。 |
| creatorUserId | String | 创建记录的用户userId。 |
| instanceId | String | 数据ID。 |
| data | Map | 数据内容。 |
| extendData | Map | 扩展数据内容。 |
| permission | Object | 数据权限信息。 |
| participantStaffIds | Array of String | 协同人用户userId。 |
| ownerStaffIds | Array of String | 负责人用户userId。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/crm/officialAccounts/contacts?nextToken=123567 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:sdsha1xxx
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
        GetOfficialAccountContactsHeaders getOfficialAccountContactsHeaders = new GetOfficialAccountContactsHeaders();
        getOfficialAccountContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetOfficialAccountContactsRequest getOfficialAccountContactsRequest = new GetOfficialAccountContactsRequest()
                .setNextToken("123567");
        try {
            client.getOfficialAccountContactsWithOptions(getOfficialAccountContactsRequest, getOfficialAccountContactsHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalkcrm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalkcrm_1_0 import models as dingtalkcrm__1__0_models
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
        get_official_account_contacts_headers = dingtalkcrm__1__0_models.GetOfficialAccountContactsHeaders()
        get_official_account_contacts_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_official_account_contacts_request = dingtalkcrm__1__0_models.GetOfficialAccountContactsRequest(
            next_token='123567'
        )
        try:
            client.get_official_account_contacts_with_options(get_official_account_contacts_request, get_official_account_contacts_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_official_account_contacts_headers = dingtalkcrm__1__0_models.GetOfficialAccountContactsHeaders()
        get_official_account_contacts_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_official_account_contacts_request = dingtalkcrm__1__0_models.GetOfficialAccountContactsRequest(
            next_token='123567'
        )
        try:
            await client.get_official_account_contacts_with_options_async(get_official_account_contacts_request, get_official_account_contacts_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetOfficialAccountContactsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetOfficialAccountContactsRequest;
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
        $getOfficialAccountContactsHeaders = new GetOfficialAccountContactsHeaders([]);
        $getOfficialAccountContactsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getOfficialAccountContactsRequest = new GetOfficialAccountContactsRequest([
            "nextToken" => "123567"
        ]);
        try {
            $client->getOfficialAccountContactsWithOptions($getOfficialAccountContactsRequest, $getOfficialAccountContactsHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk-crm_1_0"
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

  getOfficialAccountContactsHeaders := &dingtalkcrm_1_0.GetOfficialAccountContactsHeaders{}
  getOfficialAccountContactsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getOfficialAccountContactsRequest := &dingtalkcrm_1_0.GetOfficialAccountContactsRequest{
    NextToken: tea.String("123567"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetOfficialAccountContactsWithOptions(getOfficialAccountContactsRequest, getOfficialAccountContactsHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '"@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getOfficialAccountContactsHeaders = new $dingtalkcrm_1_0.GetOfficialAccountContactsHeaders({ });
    getOfficialAccountContactsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getOfficialAccountContactsRequest = new $dingtalkcrm_1_0.GetOfficialAccountContactsRequest({
      nextToken: "123567",
    });
    try {
      await client.getOfficialAccountContactsWithOptions(getOfficialAccountContactsRequest, getOfficialAccountContactsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetOfficialAccountContactsHeaders getOfficialAccountContactsHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetOfficialAccountContactsHeaders();
            getOfficialAccountContactsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetOfficialAccountContactsRequest getOfficialAccountContactsRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetOfficialAccountContactsRequest
            {
                NextToken = "123567",
            };
            try
            {
                client.GetOfficialAccountContactsWithOptions(getOfficialAccountContactsRequest, getOfficialAccountContactsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  "nextToken" : "1432423423",
  "maxResults" : 10,
  "values" : [ {
    "userId" : "user456",
    "contacts" : [ {
      "creatorNick" : "张某",
      "modifyTime" : "2019-12-25 15:33:12",
      "createTime" : "2019-12-25 15:33:12",
      "creatorUserId" : "user123",
      "instanceId" : "74865387456",
      "permission" : {
        "participantStaffIds" : [ "user_id_123" ],
        "ownerStaffIds" : [ "user_id_456" ]
      }
    } ]
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | hidden.org.only | 必须以隐藏组织身份来调用接口 | 必须以隐藏组织身份来调用接口 |
| 403 | systenError | 服务器内部错误 | 服务器内部错误 |
| 429 | systemBusy | 请求太频繁 | 系统繁忙，请求被限流 |
