---
title: "设置用户属性可见性"
source_url: "https://open.dingtalk.com/document/development/add-or-update-the-hidden-settings-of-the-employee-property"
namespace: "development"
slug: "add-or-update-the-hidden-settings-of-the-employee-property"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 用户管理 > 设置用户属性可见性"
doc_id: "uhDRwD28Uw"
updated_at: "2026-06-02 09:18:11"
---

> Source: https://open.dingtalk.com/document/development/add-or-update-the-hidden-settings-of-the-employee-property
> Path: 应用开发 / 服务端API / 通讯录管理 > 用户管理 > 设置用户属性可见性
> Updated: 2026-06-02 09:18:11

# 设置用户属性可见性

调用本接口，设置用户属性可见性。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/staffAttributes/visibilitySettings |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Contact.ReachableRule.ReadWrite-通讯录数据可见性的管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| id | Long | 否 | 设置ID。       - 新增时设置ID为空。 - 修改时设置ID为需要修改的ID。 |
| name | String | 否 | 设置的名称。 |
| description | String | 否 | 设置的描述信息。 |
| objectStaffIds | Array of String | 否 | 需要隐藏字段的员工userId，可通过[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)获得userid参数值。 |
| objectDeptIds | Array of Long | 否 | 需要隐藏字段的部门deptId，可通过[获取部门列表](0082-user-management-acquires-the-list-departments.md)获得dept\_id参数值。 |
| objectTagIds | Array of Long | 否 | 需要隐藏字段的角色roleId，可通过[获取角色列表](0089-obtains-a-list-of-enterprise-roles.md)获得id参数值。 |
| hideFields | Array of String | 否 | 需要隐藏的用户属性ID列表。   - 当需要隐藏的用户属性是企业自定义属性时，传入该属性的属性ID。 - 当需要隐藏的用户属性是系统默认属性时，传入系统默认属性列表。       系统默认属性列表如下：   - **name**： 姓名 - **department**： 部门 - **email**： 邮箱 - **manager**： 直属主管 - **title**： 职位 - **mobile**： 手机号 - **ext\_number**： 分机号 - **work\_station**： 办公地点 - **remark**： 备注 - **hire\_date**： 入职时间 - **job\_number**： 工号 |
| excludeStaffIds | Array of String | 否 | 可见隐藏字段的员工userId。 |
| excludeDeptIds | Array of Long | 否 | 可见隐藏字段的部门deptId。 |
| excludeTagIds | Array of Long | 否 | 可见隐藏字段的角色roleId。 |
| active | Boolean | 否 | 是否生效。   - **true**：生效 - **false**：不生效 |

### 请求示例

HTTP

```
POST /v1.0/contact/staffAttributes/visibilitySettings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:aec2bd0xxx
Content-Type:application/json

{
  "id" : 12364,
  "name" : "隐藏Field1",
  "description" : "部门A的人隐藏字段Field1",
  "objectStaffIds" : [ "123456" ],
  "objectDeptIds" : [ 111 ],
  "objectTagIds" : [ 222 ],
  "hideFields" : [ "12837","name" ],
  "excludeStaffIds" : [ "userId" ],
  "excludeDeptIds" : [ 111 ],
  "excludeTagIds" : [ 222 ],
  "active" : true
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
        UpdateEmpAttrbuteVisibilitySettingHeaders updateEmpAttrbuteVisibilitySettingHeaders = new UpdateEmpAttrbuteVisibilitySettingHeaders();
        updateEmpAttrbuteVisibilitySettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateEmpAttrbuteVisibilitySettingRequest updateEmpAttrbuteVisibilitySettingRequest = new UpdateEmpAttrbuteVisibilitySettingRequest()
                .setId(12364L)
                .setName("隐藏Field1")
                .setDescription("部门A的人隐藏字段Field1")
                .setObjectStaffIds(java.util.Arrays.asList(
                    "123456"
                ))
                .setObjectDeptIds(java.util.Arrays.asList(
                    111L
                ))
                .setObjectTagIds(java.util.Arrays.asList(
                    222L
                ))
                .setHideFields(java.util.Arrays.asList(
                    "12837"
                ))
                .setExcludeStaffIds(java.util.Arrays.asList(
                    "userId"
                ))
                .setExcludeDeptIds(java.util.Arrays.asList(
                    111L
                ))
                .setExcludeTagIds(java.util.Arrays.asList(
                    222L
                ))
                .setActive(true);
        try {
            client.updateEmpAttrbuteVisibilitySettingWithOptions(updateEmpAttrbuteVisibilitySettingRequest, updateEmpAttrbuteVisibilitySettingHeaders, new RuntimeOptions());
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
        update_emp_attrbute_visibility_setting_headers = dingtalkcontact__1__0_models.UpdateEmpAttrbuteVisibilitySettingHeaders()
        update_emp_attrbute_visibility_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_emp_attrbute_visibility_setting_request = dingtalkcontact__1__0_models.UpdateEmpAttrbuteVisibilitySettingRequest(
            id=12364,
            name='隐藏Field1',
            description='部门A的人隐藏字段Field1',
            object_staff_ids=[
                '123456'
            ],
            object_dept_ids=[
                111
            ],
            object_tag_ids=[
                222
            ],
            hide_fields=[
                '12837'
            ],
            exclude_staff_ids=[
                'userId'
            ],
            exclude_dept_ids=[
                111
            ],
            exclude_tag_ids=[
                222
            ],
            active=True
        )
        try:
            client.update_emp_attrbute_visibility_setting_with_options(update_emp_attrbute_visibility_setting_request, update_emp_attrbute_visibility_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_emp_attrbute_visibility_setting_headers = dingtalkcontact__1__0_models.UpdateEmpAttrbuteVisibilitySettingHeaders()
        update_emp_attrbute_visibility_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_emp_attrbute_visibility_setting_request = dingtalkcontact__1__0_models.UpdateEmpAttrbuteVisibilitySettingRequest(
            id=12364,
            name='隐藏Field1',
            description='部门A的人隐藏字段Field1',
            object_staff_ids=[
                '123456'
            ],
            object_dept_ids=[
                111
            ],
            object_tag_ids=[
                222
            ],
            hide_fields=[
                '12837'
            ],
            exclude_staff_ids=[
                'userId'
            ],
            exclude_dept_ids=[
                111
            ],
            exclude_tag_ids=[
                222
            ],
            active=True
        )
        try:
            await client.update_emp_attrbute_visibility_setting_with_options_async(update_emp_attrbute_visibility_setting_request, update_emp_attrbute_visibility_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateEmpAttrbuteVisibilitySettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateEmpAttrbuteVisibilitySettingRequest;
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
        $updateEmpAttrbuteVisibilitySettingHeaders = new UpdateEmpAttrbuteVisibilitySettingHeaders([]);
        $updateEmpAttrbuteVisibilitySettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateEmpAttrbuteVisibilitySettingRequest = new UpdateEmpAttrbuteVisibilitySettingRequest([
            "id" => 12364,
            "name" => "隐藏Field1",
            "description" => "部门A的人隐藏字段Field1",
            "objectStaffIds" => [
                "123456"
            ],
            "objectDeptIds" => [
                111
            ],
            "objectTagIds" => [
                222
            ],
            "hideFields" => [
                "12837"
            ],
            "excludeStaffIds" => [
                "userId"
            ],
            "excludeDeptIds" => [
                111
            ],
            "excludeTagIds" => [
                222
            ],
            "active" => true
        ]);
        try {
            $client->updateEmpAttrbuteVisibilitySettingWithOptions($updateEmpAttrbuteVisibilitySettingRequest, $updateEmpAttrbuteVisibilitySettingHeaders, new RuntimeOptions([]));
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

  updateEmpAttrbuteVisibilitySettingHeaders := &dingtalkcontact_1_0.UpdateEmpAttrbuteVisibilitySettingHeaders{}
  updateEmpAttrbuteVisibilitySettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateEmpAttrbuteVisibilitySettingRequest := &dingtalkcontact_1_0.UpdateEmpAttrbuteVisibilitySettingRequest{
    Id: tea.Int64(12364),
    Name: tea.String("隐藏Field1"),
    Description: tea.String("部门A的人隐藏字段Field1"),
    ObjectStaffIds: []*string{tea.String("123456")},
    ObjectDeptIds: []*int64{tea.Int(111)},
    ObjectTagIds: []*int64{tea.Int(222)},
    HideFields: []*string{tea.String("12837")},
    ExcludeStaffIds: []*string{tea.String("userId")},
    ExcludeDeptIds: []*int64{tea.Int(111)},
    ExcludeTagIds: []*int64{tea.Int(222)},
    Active: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateEmpAttrbuteVisibilitySettingWithOptions(updateEmpAttrbuteVisibilitySettingRequest, updateEmpAttrbuteVisibilitySettingHeaders, &util.RuntimeOptions{})
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
    let updateEmpAttrbuteVisibilitySettingHeaders = new $dingtalkcontact_1_0.UpdateEmpAttrbuteVisibilitySettingHeaders({ });
    updateEmpAttrbuteVisibilitySettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateEmpAttrbuteVisibilitySettingRequest = new $dingtalkcontact_1_0.UpdateEmpAttrbuteVisibilitySettingRequest({
      id: 12364,
      name: "隐藏Field1",
      description: "部门A的人隐藏字段Field1",
      objectStaffIds: [
        "123456"
      ],
      objectDeptIds: [
        111
      ],
      objectTagIds: [
        222
      ],
      hideFields: [
        "12837"
      ],
      excludeStaffIds: [
        "userId"
      ],
      excludeDeptIds: [
        111
      ],
      excludeTagIds: [
        222
      ],
      active: true,
    });
    try {
      await client.updateEmpAttrbuteVisibilitySettingWithOptions(updateEmpAttrbuteVisibilitySettingRequest, updateEmpAttrbuteVisibilitySettingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateEmpAttrbuteVisibilitySettingHeaders updateEmpAttrbuteVisibilitySettingHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateEmpAttrbuteVisibilitySettingHeaders();
            updateEmpAttrbuteVisibilitySettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateEmpAttrbuteVisibilitySettingRequest updateEmpAttrbuteVisibilitySettingRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateEmpAttrbuteVisibilitySettingRequest
            {
                Id = 12364,
                Name = "隐藏Field1",
                Description = "部门A的人隐藏字段Field1",
                ObjectStaffIds = new List<string>
                {
                    "123456"
                },
                ObjectDeptIds = new List<long?>
                {
                    111
                },
                ObjectTagIds = new List<long?>
                {
                    222
                },
                HideFields = new List<string>
                {
                    "12837"
                },
                ExcludeStaffIds = new List<string>
                {
                    "userId"
                },
                ExcludeDeptIds = new List<long?>
                {
                    111
                },
                ExcludeTagIds = new List<long?>
                {
                    222
                },
                Active = true,
            };
            try
            {
                client.UpdateEmpAttrbuteVisibilitySettingWithOptions(updateEmpAttrbuteVisibilitySettingRequest, updateEmpAttrbuteVisibilitySettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateEmpAttrbuteVisibilitySettingHeaders> updateEmpAttrbuteVisibilitySettingHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateEmpAttrbuteVisibilitySettingHeaders>();
  updateEmpAttrbuteVisibilitySettingHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateEmpAttrbuteVisibilitySettingRequest> updateEmpAttrbuteVisibilitySettingRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateEmpAttrbuteVisibilitySettingRequest>(map<string, boost::any>({
    {"id", boost::any(12364)},
    {"name", boost::any(string("隐藏Field1"))},
    {"description", boost::any(string("部门A的人隐藏字段Field1"))},
    {"objectStaffIds", boost::any(vector<string>({
      "123456"
    }))},
    {"objectDeptIds", boost::any(vector<long>({
      111
    }))},
    {"objectTagIds", boost::any(vector<long>({
      222
    }))},
    {"hideFields", boost::any(vector<string>({
      "12837"
    }))},
    {"excludeStaffIds", boost::any(vector<string>({
      "userId"
    }))},
    {"excludeDeptIds", boost::any(vector<long>({
      111
    }))},
    {"excludeTagIds", boost::any(vector<long>({
      222
    }))},
    {"active", boost::any(true)}
  }));
  try {
    client->updateEmpAttrbuteVisibilitySettingWithOptions(updateEmpAttrbuteVisibilitySettingRequest, updateEmpAttrbuteVisibilitySettingHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Long | 设置ID。 |

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
| 400 | parameter.error | 参数错误 | 参数错误 |
| 400 | ruleNum.exceed.limit | 该类型可见性规则数量已达上限 | 规则数量已达上限 |
| 400 | forbid.add.rule | 当前企业可见性规则数量超限，禁止新增规则 | 禁止新增规则 |
| 400 | directory.invalid | 规则directory不可用 | 规则directory不可用 |
| 500 | system.error | 更新错误 | 更新错误 |
