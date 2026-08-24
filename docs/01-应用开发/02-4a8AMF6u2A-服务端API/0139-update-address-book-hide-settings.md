---
title: "新增或更新通讯录隐藏设置"
source_url: "https://open.dingtalk.com/document/development/update-address-book-hide-settings"
namespace: "development"
slug: "update-address-book-hide-settings"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 通讯录可见性管理 > 新增或更新通讯录隐藏设置"
doc_id: "tm0L0laGVe"
updated_at: "2026-06-02 09:24:43"
---

> Source: https://open.dingtalk.com/document/development/update-address-book-hide-settings
> Path: 应用开发 / 服务端API / 通讯录管理 > 通讯录可见性管理 > 新增或更新通讯录隐藏设置
> Updated: 2026-06-02 09:24:43

# 新增或更新通讯录隐藏设置

用于新增或更新通讯录隐藏设置。调用时通过 PUT 请求提交 name、description、objectStaffIds、objectDeptIds、objectTagIds、excludeStaffIds 等业务字段。

## **接口调用说明**

钉钉OA管理后台中，可以实现对部门进行隐藏设置，本接口的能力是对部门隐藏的拓展，不仅能实现部门的隐藏，**也可以实现员工和角色的隐藏**。

> **[!NOTE]**
>
> 本接口的隐藏设置与OA后台的隐藏设置是相互独立存储，最终生效结果两边的设置是或的关系。比如：同一个部门，本接口或者OA后台设置了隐藏，那最终这个部门就是隐藏。

![](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20221121/wmzg/隐藏设置.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/contactHideSettings |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.Visibility.ReadWrite-通讯录数据可见范围管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 否 | 设置名称。 |
| description | String | 否 | 设置描述信息。 |
| objectStaffIds | Array of String | 否 | 需要被隐藏的员工userId列表，可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获得userId参数值。      objectStaffIds、objectDeptIds、objectTagIds三个参数内元素个数之和不能超过50。 |
| objectDeptIds | Array of Long | 否 | 需要被隐藏的部门ID列表，可通过[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获得dept\_id参数值。      objectStaffIds、objectDeptIds、objectTagIds三个参数内元素个数之和不能超过50。 |
| objectTagIds | Array of Long | 否 | 需要被隐藏的角色roleId列表，可通过[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获得id参数值。      objectStaffIds、objectDeptIds、objectTagIds三个参数内元素个数之和不能超过50。 |
| excludeStaffIds | Array of String | 否 | 不受本次隐藏设置影响的员工userId列表，可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获得userId参数值。      excludeStaffIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。 |
| excludeDeptIds | Array of Long | 否 | 不受本次隐藏设置影响的部门ID列表，可通过[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获得dept\_id参数值。      excludeStaffIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。 |
| excludeTagIds | Array of Long | 否 | 不受本次隐藏设置影响的角色ID列表，可通过[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获得id参数值。      excludeStaffIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。 |
| active | Boolean | 否 | 该设置是否激活，取值为：   - true：激活 - false：不激活 |
| id | Long | 否 | 设置ID。     - 新增时设置ID为空。 - 修改时设置ID为需要修改的ID。 |
| hideInUserProfile | Boolean | 否 | 是否同时在被查看个人资料页时隐藏，取值为：   - true：是 - false：否 |
| hideInSearch | Boolean | 否 | 是否同时在被搜索时隐藏，取值为：   - true：是 - false：否 |

### 请求示例

HTTP

```
PUT /v1.0/contact/contactHideSettings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c2c5bxxx
Content-Type:application/json

{
  "name" : "名称",
  "description" : "这是一个描述",
  "objectStaffIds" : [ "userId" ],
  "objectDeptIds" : [ 12345 ],
  "objectTagIds" : [ 112233 ],
  "excludeStaffIds" : [ "54321-1122" ],
  "excludeDeptIds" : [ 123987 ],
  "excludeTagIds" : [ 223344 ],
  "active" : true,
  "id" : 11234,
  "hideInUserProfile" : true,
  "hideInSearch" : true
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
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcontact_1_0.models.UpdateContactHideSettingHeaders updateContactHideSettingHeaders = new com.aliyun.dingtalkcontact_1_0.models.UpdateContactHideSettingHeaders();
        updateContactHideSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.UpdateContactHideSettingRequest updateContactHideSettingRequest = new com.aliyun.dingtalkcontact_1_0.models.UpdateContactHideSettingRequest()
                .setName("名称")
                .setDescription("这是一个描述")
                .setObjectStaffIds(java.util.Arrays.asList(
                    "userId"
                ))
                .setObjectDeptIds(java.util.Arrays.asList(
                    12345L
                ))
                .setObjectTagIds(java.util.Arrays.asList(
                    112233L
                ))
                .setExcludeStaffIds(java.util.Arrays.asList(
                    "54321-1122"
                ))
                .setExcludeDeptIds(java.util.Arrays.asList(
                    123987L
                ))
                .setExcludeTagIds(java.util.Arrays.asList(
                    223344L
                ))
                .setActive(true)
                .setId(11234L)
                .setHideInUserProfile(true)
                .setHideInSearch(true);
        try {
            client.updateContactHideSettingWithOptions(updateContactHideSettingRequest, updateContactHideSettingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_contact_hide_setting_headers = dingtalkcontact__1__0_models.UpdateContactHideSettingHeaders()
        update_contact_hide_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_contact_hide_setting_request = dingtalkcontact__1__0_models.UpdateContactHideSettingRequest(
            name='名称',
            description='这是一个描述',
            object_staff_ids=[
                'userId'
            ],
            object_dept_ids=[
                12345
            ],
            object_tag_ids=[
                112233
            ],
            exclude_staff_ids=[
                '54321-1122'
            ],
            exclude_dept_ids=[
                123987
            ],
            exclude_tag_ids=[
                223344
            ],
            active=True,
            id=11234,
            hide_in_user_profile=True,
            hide_in_search=True
        )
        try:
            client.update_contact_hide_setting_with_options(update_contact_hide_setting_request, update_contact_hide_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_contact_hide_setting_headers = dingtalkcontact__1__0_models.UpdateContactHideSettingHeaders()
        update_contact_hide_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_contact_hide_setting_request = dingtalkcontact__1__0_models.UpdateContactHideSettingRequest(
            name='名称',
            description='这是一个描述',
            object_staff_ids=[
                'userId'
            ],
            object_dept_ids=[
                12345
            ],
            object_tag_ids=[
                112233
            ],
            exclude_staff_ids=[
                '54321-1122'
            ],
            exclude_dept_ids=[
                123987
            ],
            exclude_tag_ids=[
                223344
            ],
            active=True,
            id=11234,
            hide_in_user_profile=True,
            hide_in_search=True
        )
        try:
            await client.update_contact_hide_setting_with_options_async(update_contact_hide_setting_request, update_contact_hide_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateContactHideSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateContactHideSettingRequest;
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
        $updateContactHideSettingHeaders = new UpdateContactHideSettingHeaders([]);
        $updateContactHideSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateContactHideSettingRequest = new UpdateContactHideSettingRequest([
            "name" => "名称",
            "description" => "这是一个描述",
            "objectStaffIds" => [
                "userId"
            ],
            "objectDeptIds" => [
                12345
            ],
            "objectTagIds" => [
                112233
            ],
            "excludeStaffIds" => [
                "54321-1122"
            ],
            "excludeDeptIds" => [
                123987
            ],
            "excludeTagIds" => [
                223344
            ],
            "active" => true,
            "id" => 11234,
            "hideInUserProfile" => true,
            "hideInSearch" => true
        ]);
        try {
            $client->updateContactHideSettingWithOptions($updateContactHideSettingRequest, $updateContactHideSettingHeaders, new RuntimeOptions([]));
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

  updateContactHideSettingHeaders := &dingtalkcontact_1_0.UpdateContactHideSettingHeaders{}
  updateContactHideSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateContactHideSettingRequest := &dingtalkcontact_1_0.UpdateContactHideSettingRequest{
    Name: tea.String("名称"),
    Description: tea.String("这是一个描述"),
    ObjectStaffIds: []*string{tea.String("userId")},
    ObjectDeptIds: []*int64{tea.Int64(12345)},
    ObjectTagIds: []*int64{tea.Int64(112233)},
    ExcludeStaffIds: []*string{tea.String("54321-1122")},
    ExcludeDeptIds: []*int64{tea.Int64(123987)},
    ExcludeTagIds: []*int64{tea.Int64(223344)},
    Active: tea.Bool(true),
    Id: tea.Int64(11234),
    HideInUserProfile: tea.Bool(true),
    HideInSearch: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateContactHideSettingWithOptions(updateContactHideSettingRequest, updateContactHideSettingHeaders, &util.RuntimeOptions{})
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
    let updateContactHideSettingHeaders = new $dingtalkcontact_1_0.UpdateContactHideSettingHeaders({ });
    updateContactHideSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateContactHideSettingRequest = new $dingtalkcontact_1_0.UpdateContactHideSettingRequest({
      name: "名称",
      description: "这是一个描述",
      objectStaffIds: [
        "userId"
      ],
      objectDeptIds: [
        12345
      ],
      objectTagIds: [
        112233
      ],
      excludeStaffIds: [
        "54321-1122"
      ],
      excludeDeptIds: [
        123987
      ],
      excludeTagIds: [
        223344
      ],
      active: true,
      id: 11234,
      hideInUserProfile: true,
      hideInSearch: true,
    });
    try {
      await client.updateContactHideSettingWithOptions(updateContactHideSettingRequest, updateContactHideSettingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactHideSettingHeaders updateContactHideSettingHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactHideSettingHeaders();
            updateContactHideSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactHideSettingRequest updateContactHideSettingRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactHideSettingRequest
            {
                Name = "名称",
                Description = "这是一个描述",
                ObjectStaffIds = new List<string>
                {
                    "userId"
                },
                ObjectDeptIds = new List<long?>
                {
                    12345
                },
                ObjectTagIds = new List<long?>
                {
                    112233
                },
                ExcludeStaffIds = new List<string>
                {
                    "54321-1122"
                },
                ExcludeDeptIds = new List<long?>
                {
                    123987
                },
                ExcludeTagIds = new List<long?>
                {
                    223344
                },
                Active = true,
                Id = 11234,
                HideInUserProfile = true,
                HideInSearch = true,
            };
            try
            {
                client.UpdateContactHideSettingWithOptions(updateContactHideSettingRequest, updateContactHideSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Long | 设置ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : 1234001
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 500 | system.error | 更新设置出错 | 更新设置出错 |
