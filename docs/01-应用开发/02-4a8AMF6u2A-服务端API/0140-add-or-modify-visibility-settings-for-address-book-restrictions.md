---
title: "新增或修改限制查看通讯录设置"
source_url: "https://open.dingtalk.com/document/development/add-or-modify-visibility-settings-for-address-book-restrictions"
namespace: "development"
slug: "add-or-modify-visibility-settings-for-address-book-restrictions"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 通讯录可见性管理 > 新增或修改限制查看通讯录设置"
doc_id: "hwPJ9ZDhQG"
updated_at: "2026-06-02 09:24:45"
---

> Source: https://open.dingtalk.com/document/development/add-or-modify-visibility-settings-for-address-book-restrictions
> Path: 应用开发 / 服务端API / 通讯录管理 > 通讯录可见性管理 > 新增或修改限制查看通讯录设置
> Updated: 2026-06-02 09:24:45

# 新增或修改限制查看通讯录设置

调用本接口，新增或修改员工、部门、角色限制查看通讯录的设置。

## **接口调用说明**

钉钉OA管理后台中，可以限制本部门成员查看通讯录，本接口的能力是对限制本部门成员查看通讯录的拓展，不仅能实现限制部门内成员查看通讯录，也可以实现限制员工和角色查看通讯录。

> **[!NOTE]**
>
> 本接口的限制查看设置与OA后台的限制查看设置是相互独立存储，最终生效结果两边的设置是或的关系。比如：同一个部门，本接口或者OA后台有任意一方设置了仅能查看自己，最终这个部门就只能查看自己。

![](https://img.alicdn.com/imgextra/i2/O1CN01c1IHaB1maJG9jwkSO_!!6000000004970-0-tps-2400-1350.jpg)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/restrictions/settings |
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
| id | Long | 否 | 设置ID。   - 如果需要新增设置，该参数不传。 - 如果需要修改已有的设置，需要指定该参数，通过调用[获取限制查看通讯录设置列表](0141-gets-a-list-of-address-book-limit-visibility-settings.md)接口获取。 |
| name | String | 否 | 设置名称。 |
| description | String | 否 | 设置描述。 |
| subjectUserIds | Array of String | 否 | 需要限制查看通讯录的用户userId列表，可调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取userId。      subjectUserIds、subjectDeptIds、subjectTagIds三个参数内元素个数之和不能超过50。 |
| subjectDeptIds | Array of Long | 否 | 需要限制查看通讯录的部门ID列表，可调用[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取dept\_id。      subjectUserIds、subjectDeptIds、subjectTagIds三个参数内元素个数之和不能超过50。 |
| subjectTagIds | Array of Long | 否 | 需要限制查看通讯录的角色ID，通过调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取。      subjectUserIds、subjectDeptIds、subjectTagIds三个参数内元素个数之和不能超过50。 |
| type | String | 是 | 限制类型，有以下取值：   - **onlySelf**：只能查看自己，不能看自己之外的其他部门和人。 - **onlySelfDeptAndChild**：只能看到自己所在的部门及子部门，不能看到其他部门和人。 - **excludeNode**：默认值，只能看到白名单列表中的部门和人。       当该参数值为excludeNode时，设置的白名单才生效。 |
| excludeUserIds | Array of String | 否 | 白名单用户userId，可调用[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取userId。       - excludeUserIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。 - 当type参数值为excludeNode时，设置的白名单才生效。 |
| excludeDeptIds | Array of Long | 否 | 白名单部门ID，通过调用[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取。       - excludeUserIds、excludeDeptIds、excludeTagIds三个参数内元素之和不能超过50。 - 当type参数值为excludeNode时，设置的白名单才生效。 |
| excludeTagIds | Array of Long | 否 | 白名单角色ID，通过调用[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)接口获取。       - excludeUserIds、excludeDeptIds、excludeTagIds三个参数内元素个数之和不能超过50。 - 当type参数值为excludeNode时，设置的白名单才生效。 |
| active | Boolean | 否 | 本次设置是否生效。   - true：生效 - false：不生效 |
| restrictInUserProfile | Boolean | 否 | 是否同时限制查看个人资料页。   - true：是 - false：否       如果限制查看，在钉钉客户端点击不在可看见范围内的员工头像，不会展示当前组织的资料信息。 |
| restrictInSearch | Boolean | 否 | 是否同时限制搜索。   - true：是 - false：否       如果限制搜索，在钉钉客户端搜索不在可看见范围内的员工，会搜索不到结果。 |

### 请求示例

HTTP

```
PUT /v1.0/contact/restrictions/settings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "id" : 10001,
  "name" : "xxx部门的人只能查看自己",
  "description" : "xxx部门的人限制查看外部门的人",
  "subjectUserIds" : [ "userId1" ],
  "subjectDeptIds" : [ 10000 ],
  "subjectTagIds" : [ 20000 ],
  "type" : "excludeNode",
  "excludeUserIds" : [ "userId2" ],
  "excludeDeptIds" : [ 10000 ],
  "excludeTagIds" : [ 20000 ],
  "active" : true,
  "restrictInUserProfile" : true,
  "restrictInSearch" : true
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
        com.aliyun.dingtalkcontact_1_0.models.UpdateContactRestrictSettingHeaders updateContactRestrictSettingHeaders = new com.aliyun.dingtalkcontact_1_0.models.UpdateContactRestrictSettingHeaders();
        updateContactRestrictSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcontact_1_0.models.UpdateContactRestrictSettingRequest updateContactRestrictSettingRequest = new com.aliyun.dingtalkcontact_1_0.models.UpdateContactRestrictSettingRequest()
                .setId(10001L)
                .setName("xxx部门的人只能查看自己")
                .setDescription("xxx部门的人限制查看外部门的人")
                .setSubjectUserIds(java.util.Arrays.asList(
                    "userId1"
                ))
                .setSubjectDeptIds(java.util.Arrays.asList(
                    10000L
                ))
                .setSubjectTagIds(java.util.Arrays.asList(
                    20000L
                ))
                .setType("excludeNode")
                .setExcludeUserIds(java.util.Arrays.asList(
                    "userId2"
                ))
                .setExcludeDeptIds(java.util.Arrays.asList(
                    10000L
                ))
                .setExcludeTagIds(java.util.Arrays.asList(
                    20000L
                ))
                .setActive(true)
                .setRestrictInUserProfile(true)
                .setRestrictInSearch(true);
        try {
            client.updateContactRestrictSettingWithOptions(updateContactRestrictSettingRequest, updateContactRestrictSettingHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_contact_restrict_setting_headers = dingtalkcontact__1__0_models.UpdateContactRestrictSettingHeaders()
        update_contact_restrict_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_contact_restrict_setting_request = dingtalkcontact__1__0_models.UpdateContactRestrictSettingRequest(
            id=10001,
            name='xxx部门的人只能查看自己',
            description='xxx部门的人限制查看外部门的人',
            subject_user_ids=[
                'userId1'
            ],
            subject_dept_ids=[
                10000
            ],
            subject_tag_ids=[
                20000
            ],
            type='excludeNode',
            exclude_user_ids=[
                'userId2'
            ],
            exclude_dept_ids=[
                10000
            ],
            exclude_tag_ids=[
                20000
            ],
            active=True,
            restrict_in_user_profile=True,
            restrict_in_search=True
        )
        try:
            client.update_contact_restrict_setting_with_options(update_contact_restrict_setting_request, update_contact_restrict_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_contact_restrict_setting_headers = dingtalkcontact__1__0_models.UpdateContactRestrictSettingHeaders()
        update_contact_restrict_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_contact_restrict_setting_request = dingtalkcontact__1__0_models.UpdateContactRestrictSettingRequest(
            id=10001,
            name='xxx部门的人只能查看自己',
            description='xxx部门的人限制查看外部门的人',
            subject_user_ids=[
                'userId1'
            ],
            subject_dept_ids=[
                10000
            ],
            subject_tag_ids=[
                20000
            ],
            type='excludeNode',
            exclude_user_ids=[
                'userId2'
            ],
            exclude_dept_ids=[
                10000
            ],
            exclude_tag_ids=[
                20000
            ],
            active=True,
            restrict_in_user_profile=True,
            restrict_in_search=True
        )
        try:
            await client.update_contact_restrict_setting_with_options_async(update_contact_restrict_setting_request, update_contact_restrict_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateContactRestrictSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateContactRestrictSettingRequest;
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
        $updateContactRestrictSettingHeaders = new UpdateContactRestrictSettingHeaders([]);
        $updateContactRestrictSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateContactRestrictSettingRequest = new UpdateContactRestrictSettingRequest([
            "id" => 10001,
            "name" => "xxx部门的人只能查看自己",
            "description" => "xxx部门的人限制查看外部门的人",
            "subjectUserIds" => [
                "userId1"
            ],
            "subjectDeptIds" => [
                10000
            ],
            "subjectTagIds" => [
                20000
            ],
            "type" => "excludeNode",
            "excludeUserIds" => [
                "userId2"
            ],
            "excludeDeptIds" => [
                10000
            ],
            "excludeTagIds" => [
                20000
            ],
            "active" => true,
            "restrictInUserProfile" => true,
            "restrictInSearch" => true
        ]);
        try {
            $client->updateContactRestrictSettingWithOptions($updateContactRestrictSettingRequest, $updateContactRestrictSettingHeaders, new RuntimeOptions([]));
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

  updateContactRestrictSettingHeaders := &dingtalkcontact_1_0.UpdateContactRestrictSettingHeaders{}
  updateContactRestrictSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateContactRestrictSettingRequest := &dingtalkcontact_1_0.UpdateContactRestrictSettingRequest{
    Id: tea.Int64(10001),
    Name: tea.String("xxx部门的人只能查看自己"),
    Description: tea.String("xxx部门的人限制查看外部门的人"),
    SubjectUserIds: []*string{tea.String("userId1")},
    SubjectDeptIds: []*int64{tea.Int64(10000)},
    SubjectTagIds: []*int64{tea.Int64(20000)},
    Type: tea.String("excludeNode"),
    ExcludeUserIds: []*string{tea.String("userId2")},
    ExcludeDeptIds: []*int64{tea.Int64(10000)},
    ExcludeTagIds: []*int64{tea.Int64(20000)},
    Active: tea.Bool(true),
    RestrictInUserProfile: tea.Bool(true),
    RestrictInSearch: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateContactRestrictSettingWithOptions(updateContactRestrictSettingRequest, updateContactRestrictSettingHeaders, &util.RuntimeOptions{})
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
    let updateContactRestrictSettingHeaders = new $dingtalkcontact_1_0.UpdateContactRestrictSettingHeaders({ });
    updateContactRestrictSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateContactRestrictSettingRequest = new $dingtalkcontact_1_0.UpdateContactRestrictSettingRequest({
      id: 10001,
      name: "xxx部门的人只能查看自己",
      description: "xxx部门的人限制查看外部门的人",
      subjectUserIds: [
        "userId1"
      ],
      subjectDeptIds: [
        10000
      ],
      subjectTagIds: [
        20000
      ],
      type: "excludeNode",
      excludeUserIds: [
        "userId2"
      ],
      excludeDeptIds: [
        10000
      ],
      excludeTagIds: [
        20000
      ],
      active: true,
      restrictInUserProfile: true,
      restrictInSearch: true,
    });
    try {
      await client.updateContactRestrictSettingWithOptions(updateContactRestrictSettingRequest, updateContactRestrictSettingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactRestrictSettingHeaders updateContactRestrictSettingHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactRestrictSettingHeaders();
            updateContactRestrictSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactRestrictSettingRequest updateContactRestrictSettingRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateContactRestrictSettingRequest
            {
                Id = 10001,
                Name = "xxx部门的人只能查看自己",
                Description = "xxx部门的人限制查看外部门的人",
                SubjectUserIds = new List<string>
                {
                    "userId1"
                },
                SubjectDeptIds = new List<long?>
                {
                    10000
                },
                SubjectTagIds = new List<long?>
                {
                    20000
                },
                Type = "excludeNode",
                ExcludeUserIds = new List<string>
                {
                    "userId2"
                },
                ExcludeDeptIds = new List<long?>
                {
                    10000
                },
                ExcludeTagIds = new List<long?>
                {
                    20000
                },
                Active = true,
                RestrictInUserProfile = true,
                RestrictInSearch = true,
            };
            try
            {
                client.UpdateContactRestrictSettingWithOptions(updateContactRestrictSettingRequest, updateContactRestrictSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Long | 限制设置ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : 10001
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | userIdInvalid | userId不存在 | userId不存在 |
| 400 | excludeNodeExceed | excludeUserIds、excludeDeptIds、excludeTagIds三个数组元素之和不能超过50 | excludeUserIds、excludeDeptIds、excludeTagIds三个数组元素之和不能超过50 |
| 400 | subjectNodeExceed | subjectUserIds、subjectDeptIds、subjectTagIds三个数组元素之和不能超过50 | subjectUserIds、subjectDeptIds、subjectTagIds三个数组元素之和不能超过50 |
| 400 | typeInvalid | type只能是excludeNode、onlySelf、onlySelfDeptAndChild中的一个 | type只能是excludeNode、onlySelf、onlySelfDeptAndChild中的一个 |
| 400 | subjectNodeEmpty | subjectUserIds、subjectDeptIds、subjectTagIds不能都为空 | subjectUserIds、subjectDeptIds、subjectTagIds不能都为空 |
| 400 | idInvalid | id对应的设置不存在 | id对应的设置不存在 |
| 500 | system.error | 系统错误 | 系统错误 |
