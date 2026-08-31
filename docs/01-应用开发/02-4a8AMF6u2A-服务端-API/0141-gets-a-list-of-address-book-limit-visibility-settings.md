---
title: "获取限制查看通讯录设置列表"
source_url: "https://open.dingtalk.com/document/development/gets-a-list-of-address-book-limit-visibility-settings"
namespace: "development"
slug: "gets-a-list-of-address-book-limit-visibility-settings"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 通讯录可见性管理 > 获取限制查看通讯录设置列表"
doc_id: "dfXUH5CfYW"
updated_at: "2026-06-01 16:21:34"
---

> Source: https://open.dingtalk.com/document/development/gets-a-list-of-address-book-limit-visibility-settings
> Path: 应用开发 / 服务端 API / 通讯录管理 > 通讯录可见性管理 > 获取限制查看通讯录设置列表
> Updated: 2026-06-01 16:21:34

# 获取限制查看通讯录设置列表

调用本接口，获取通讯录限制可见性设置信息列表。

## 接口调用说明

企业在调用[新增或修改限制查看通讯录设置](0140-add-or-modify-visibility-settings-for-address-book-restrictions.md)接口后，可调用本接口分页查询企业下的限制查看通讯录设置的信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/restrictions/settings |
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
| nextToken | Long | 否 | 分页游标。   - 首次调用，该参数不传。 - 非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 最大返回结果数，最大值100。 |

### 请求示例

HTTP

```
GET /v1.0/contact/restrictions/settings?nextToken=1&maxResults=100 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
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
        com.aliyun.dingtalkcontact_1_0.models.ListContactRestrictSettingHeaders listContactRestrictSettingHeaders = new com.aliyun.dingtalkcontact_1_0.models.ListContactRestrictSettingHeaders();
        listContactRestrictSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.ListContactRestrictSettingRequest listContactRestrictSettingRequest = new com.aliyun.dingtalkcontact_1_0.models.ListContactRestrictSettingRequest()
                .setNextToken(1L)
                .setMaxResults(100);
        try {
            client.listContactRestrictSettingWithOptions(listContactRestrictSettingRequest, listContactRestrictSettingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_contact_restrict_setting_headers = dingtalkcontact__1__0_models.ListContactRestrictSettingHeaders()
        list_contact_restrict_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_contact_restrict_setting_request = dingtalkcontact__1__0_models.ListContactRestrictSettingRequest(
            next_token=1,
            max_results=100
        )
        try:
            client.list_contact_restrict_setting_with_options(list_contact_restrict_setting_request, list_contact_restrict_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_contact_restrict_setting_headers = dingtalkcontact__1__0_models.ListContactRestrictSettingHeaders()
        list_contact_restrict_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_contact_restrict_setting_request = dingtalkcontact__1__0_models.ListContactRestrictSettingRequest(
            next_token=1,
            max_results=100
        )
        try:
            await client.list_contact_restrict_setting_with_options_async(list_contact_restrict_setting_request, list_contact_restrict_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListContactRestrictSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ListContactRestrictSettingRequest;
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
        $listContactRestrictSettingHeaders = new ListContactRestrictSettingHeaders([]);
        $listContactRestrictSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listContactRestrictSettingRequest = new ListContactRestrictSettingRequest([
            "nextToken" => 1,
            "maxResults" => 100
        ]);
        try {
            $client->listContactRestrictSettingWithOptions($listContactRestrictSettingRequest, $listContactRestrictSettingHeaders, new RuntimeOptions([]));
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

  listContactRestrictSettingHeaders := &dingtalkcontact_1_0.ListContactRestrictSettingHeaders{}
  listContactRestrictSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listContactRestrictSettingRequest := &dingtalkcontact_1_0.ListContactRestrictSettingRequest{
    NextToken: tea.Int64(1),
    MaxResults: tea.Int32(100),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListContactRestrictSettingWithOptions(listContactRestrictSettingRequest, listContactRestrictSettingHeaders, &util.RuntimeOptions{})
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
    let listContactRestrictSettingHeaders = new $dingtalkcontact_1_0.ListContactRestrictSettingHeaders({ });
    listContactRestrictSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listContactRestrictSettingRequest = new $dingtalkcontact_1_0.ListContactRestrictSettingRequest({
      nextToken: 1,
      maxResults: 100,
    });
    try {
      await client.listContactRestrictSettingWithOptions(listContactRestrictSettingRequest, listContactRestrictSettingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactRestrictSettingHeaders listContactRestrictSettingHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactRestrictSettingHeaders();
            listContactRestrictSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactRestrictSettingRequest listContactRestrictSettingRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ListContactRestrictSettingRequest
            {
                NextToken = 1,
                MaxResults = 100,
            };
            try
            {
                client.ListContactRestrictSettingWithOptions(listContactRestrictSettingRequest, listContactRestrictSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nextToken | Long | 分页游标。 |
| list | Array | 限制查看通讯录设置列表。 |
| id | Long | 设置Id。 |
| name | String | 限制查看通讯录设置名称。 |
| description | String | 限制查看通讯录描述。 |
| subjectUserIds | Array of String | 限制查看通讯录的用户userId列表。 |
| subjectDeptIds | Array of Long | 限制查看通讯录的部门deptId列表。 |
| subjectTagIds | Array of Long | 限制查看通讯录的角色roleId。 |
| type | String | 限制类型。   - excludeNode: 只能看到白名单里的用户和部门。 - onlySelf: 只能看到自己。 - onlySelfDeptAndChild: 只能看到自己所在部门及子部门。 |
| excludeUserIds | Array of String | 白名单内用户userId列表。 |
| excludeDeptIds | Array of Long | 白名单内的部门deptId列表。 |
| excludeTagIds | Array of Long | 白名单内角色roleId列表。 |
| active | Boolean | 是否生效。   - true：生效 - false：不生效。 |
| restrictInUserProfile | Boolean | 是否同时限制查看个人资料页。   - true：是 - false：否 |
| restrictInSearch | Boolean | 是否同时限制搜索。   - true：是 - false：否 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "hasMore" : true,
  "nextToken" : 200001100,
  "list" : [ {
    "id" : 1001,
    "name" : "xxx部门限制可见设置",
    "description" : "xxx部门只能看到xxx、xxx部门、xxx角色",
    "subjectUserIds" : [ "10002" ],
    "subjectDeptIds" : [ 11222 ],
    "subjectTagIds" : [ 222333 ],
    "type" : "excludeNode",
    "excludeUserIds" : [ "0141040080" ],
    "excludeDeptIds" : [ 100200 ],
    "excludeTagIds" : [ 112233 ],
    "active" : true,
    "restrictInUserProfile" : true,
    "restrictInSearch" : true
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | system.error | 查询服务出错 | 查询服务出错 |
