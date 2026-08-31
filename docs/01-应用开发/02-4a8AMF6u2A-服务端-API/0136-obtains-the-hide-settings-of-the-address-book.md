---
title: "获取通讯录隐藏设置"
source_url: "https://open.dingtalk.com/document/development/obtains-the-hide-settings-of-the-address-book"
namespace: "development"
slug: "obtains-the-hide-settings-of-the-address-book"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 通讯录可见性管理 > 获取通讯录隐藏设置"
doc_id: "kAQNpYtpSQ"
updated_at: "2026-06-01 16:21:32"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-hide-settings-of-the-address-book
> Path: 应用开发 / 服务端 API / 通讯录管理 > 通讯录可见性管理 > 获取通讯录隐藏设置
> Updated: 2026-06-01 16:21:32

# 获取通讯录隐藏设置

调用本接口，批量获取通讯录隐藏设置信息列表。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/contactHideSettings |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.Visibility.ReadWrite-通讯录数据可见范围管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| nextToken | Long | 否 | 分页游标。   - 首次调用，该参数传0。 - 非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 分页大小，最大值100。 |

### 请求示例

HTTP

```
GET /v1.0/contact/contactHideSettings?nextToken=0&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c2c5b1cxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.ListContactHideSettingsHeaders listContactHideSettingsHeaders = new com.aliyun.dingtalkcontact_1_0.models.ListContactHideSettingsHeaders();
        listContactHideSettingsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.ListContactHideSettingsRequest listContactHideSettingsRequest = new com.aliyun.dingtalkcontact_1_0.models.ListContactHideSettingsRequest()
                .setNextToken(0L)
                .setMaxResults(10);
        try {
            client.listContactHideSettingsWithOptions(listContactHideSettingsRequest, listContactHideSettingsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_contact_hide_settings_headers = dingtalkcontact__1__0_models.ListContactHideSettingsHeaders()
        list_contact_hide_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_contact_hide_settings_request = dingtalkcontact__1__0_models.ListContactHideSettingsRequest(
            next_token=0,
            max_results=10
        )
        try:
            client.list_contact_hide_settings_with_options(list_contact_hide_settings_request, list_contact_hide_settings_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_contact_hide_settings_headers = dingtalkcontact__1__0_models.ListContactHideSettingsHeaders()
        list_contact_hide_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_contact_hide_settings_request = dingtalkcontact__1__0_models.ListContactHideSettingsRequest(
            next_token=0,
            max_results=10
        )
        try:
            await client.list_contact_hide_settings_with_options_async(list_contact_hide_settings_request, list_contact_hide_settings_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListContactHideSettingsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListContactHideSettingsRequest;
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
        $listContactHideSettingsHeaders = new ListContactHideSettingsHeaders([]);
        $listContactHideSettingsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listContactHideSettingsRequest = new ListContactHideSettingsRequest([
            "nextToken" => 0,
            "maxResults" => 10
        ]);
        try {
            $client->listContactHideSettingsWithOptions($listContactHideSettingsRequest, $listContactHideSettingsHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  listContactHideSettingsHeaders := &dingtalkcontact_1_0.ListContactHideSettingsHeaders{}
  listContactHideSettingsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listContactHideSettingsRequest := &dingtalkcontact_1_0.ListContactHideSettingsRequest{
    NextToken: tea.Int64(0),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListContactHideSettingsWithOptions(listContactHideSettingsRequest, listContactHideSettingsHeaders, &util.RuntimeOptions{})
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
    let listContactHideSettingsHeaders = new $dingtalkcontact_1_0.ListContactHideSettingsHeaders({ });
    listContactHideSettingsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listContactHideSettingsRequest = new $dingtalkcontact_1_0.ListContactHideSettingsRequest({
      nextToken: 0,
      maxResults: 10,
    });
    try {
      await client.listContactHideSettingsWithOptions(listContactHideSettingsRequest, listContactHideSettingsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactHideSettingsHeaders listContactHideSettingsHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactHideSettingsHeaders();
            listContactHideSettingsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactHideSettingsRequest listContactHideSettingsRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactHideSettingsRequest
            {
                NextToken = 0,
                MaxResults = 10,
            };
            try
            {
                client.ListContactHideSettingsWithOptions(listContactHideSettingsRequest, listContactHideSettingsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| hasMore | Boolean | 是否还有更多数据。   - true：是 - false：否 |
| nextToken | Long | 下一页的游标，为空字符串则表示分页结束。 |
| list | Array | 通讯录隐藏的设置列表。 |
| name | String | 设置名称。 |
| description | String | 设置描述。 |
| objectStaffIds | Array of String | 要隐藏的员工userId列表。 |
| objectDeptIds | Array of Long | 要隐藏的部门ID列表。 |
| objectTagIds | Array of Long | 要影藏的角色Id列表。 |
| excludeStaffIds | Array of String | 不受本次隐藏设置影响的用户userId列表。 |
| excludeDeptIds | Array of Long | 不受本次隐藏影响的部门ID列表。 |
| excludeTagIds | Array of Long | 不受本次隐藏设置影响的角色Id列表。 |
| active | Boolean | 规则是否生效。   - true：生效 - false：不生效 |
| id | Long | 设置ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "hasMore" : true,
  "nextToken" : 1632725845000,
  "list" : [ {
    "name" : "测试规则",
    "description" : "隐藏对deptA但是user1可见。",
    "objectStaffIds" : [ "176152-1826" ],
    "objectDeptIds" : [ 12345 ],
    "objectTagIds" : [ 111222 ],
    "excludeStaffIds" : [ "userId2" ],
    "excludeDeptIds" : [ 13456 ],
    "excludeTagIds" : [ 223344 ],
    "active" : true,
    "id" : 2277001
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 500 | system.error | 获取设置出错 | 获取设置出错 |
