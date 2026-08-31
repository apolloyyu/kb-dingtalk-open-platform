---
title: "设置高管模式"
source_url: "https://open.dingtalk.com/document/development/update-executive-settings"
namespace: "development"
slug: "update-executive-settings"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 用户管理 > 设置高管模式"
doc_id: "i51DcKjLJ4"
updated_at: "2026-06-02 09:18:09"
---

> Source: https://open.dingtalk.com/document/development/update-executive-settings
> Path: 应用开发 / 服务端 API / 通讯录管理 > 用户管理 > 设置高管模式
> Updated: 2026-06-02 09:18:09

# 设置高管模式

调用本接口设置员工的高管模式。

## 接口调用说明

当设置员工为高管，则针对设置的拦截场景，同企业内只有其他高管、高管白名单内用户以及高管的好友可以联系。其他人不可联系。 例如：设置userA为高管，拦截场景为VIDEO\_CALL，白名单用户设置了userB。userB、userC为同一企业的普通员工，且跟userA没有好友关系，则userB可以对userA发起视频通话，userC不可以对userA发起视频通话。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/9803630871/p1075866.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/seniorSettings |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_manage\_addresslist-维护通讯录的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| seniorStaffId | String | 是 | 需要设置的员工userid。 |
| open | Boolean | 是 | 是否开启高管模式，取值：   - **true**：开启高管模式 - **false**：关闭高管模式 |
| permitStaffIds | Array of String | 否 | 高管白名单员工userid列表。      参数**permitStaffIds**、**permitDeptIds**、**permitTagIds**列表内元素之和最大为200。 |
| permitDeptIds | Array of Long | 否 | 高管白名单部门列表。      参数**permitStaffIds**、**permitDeptIds**、**permitTagIds**列表内元素之和最大为200。 |
| permitTagIds | Array of Long | 否 | 高管白名单角色列表。      参数**permitStaffIds**、**permitDeptIds**、**permitTagIds**列表内元素之和最大为200。 |
| protectScenes | Array of String | 否 | 高管拦截场景，取值：   - **DING\_SMS**： 短信Ding消息 - **DING\_MSG**： 应用内Ding消息 - **CHAT**： IM聊天（单聊、群聊） - **CONFERENCE\_VIDEO**：视频会议 - **CONFERENCE**：语音会议 - **VIDEO\_CALL**：视频通话 - **CONFERENCE\_VOIP**：语音通话 - **CALL**：电话会议、办公电话 - **SEARCH**： 电话会议里搜索功能 - **CALL\_CENTER**：呼叫中心 |

### 请求示例

HTTP

```
POST /v1.0/contact/seniorSettings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:afe8143b88xxx
Content-Type:application/json

{
  "seniorStaffId" : "013349365367-1094322561",
  "open" : true,
  "permitStaffIds" : [ "manager8723" ],
  "permitDeptIds" : [ 12345 ],
  "permitTagIds" : [ 11111 ],
  "protectScenes" : [ "CHAT" ]
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
        UpdateSeniorSettingHeaders updateSeniorSettingHeaders = new UpdateSeniorSettingHeaders();
        updateSeniorSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateSeniorSettingRequest updateSeniorSettingRequest = new UpdateSeniorSettingRequest()
                .setSeniorStaffId("013349365367-1094322561")
                .setOpen(true)
                .setPermitStaffIds(java.util.Arrays.asList(
                    "manager8723"
                ))
                .setPermitDeptIds(java.util.Arrays.asList(
                    12345L
                ))
                .setPermitTagIds(java.util.Arrays.asList(
                    11111L
                ))
                .setProtectScenes(java.util.Arrays.asList(
                    "CHAT"
                ));
        try {
            client.updateSeniorSettingWithOptions(updateSeniorSettingRequest, updateSeniorSettingHeaders, new RuntimeOptions());
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
        update_senior_setting_headers = dingtalkcontact__1__0_models.UpdateSeniorSettingHeaders()
        update_senior_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_senior_setting_request = dingtalkcontact__1__0_models.UpdateSeniorSettingRequest(
            senior_staff_id='013349365367-1094322561',
            open=True,
            permit_staff_ids=[
                'manager8723'
            ],
            permit_dept_ids=[
                12345
            ],
            permit_tag_ids=[
                11111
            ],
            protect_scenes=[
                'CHAT'
            ]
        )
        try:
            client.update_senior_setting_with_options(update_senior_setting_request, update_senior_setting_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_senior_setting_headers = dingtalkcontact__1__0_models.UpdateSeniorSettingHeaders()
        update_senior_setting_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_senior_setting_request = dingtalkcontact__1__0_models.UpdateSeniorSettingRequest(
            senior_staff_id='013349365367-1094322561',
            open=True,
            permit_staff_ids=[
                'manager8723'
            ],
            permit_dept_ids=[
                12345
            ],
            permit_tag_ids=[
                11111
            ],
            protect_scenes=[
                'CHAT'
            ]
        )
        try:
            await client.update_senior_setting_with_options_async(update_senior_setting_request, update_senior_setting_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateSeniorSettingHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateSeniorSettingRequest;
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
        $updateSeniorSettingHeaders = new UpdateSeniorSettingHeaders([]);
        $updateSeniorSettingHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateSeniorSettingRequest = new UpdateSeniorSettingRequest([
            "seniorStaffId" => "013349365367-1094322561",
            "open" => true,
            "permitStaffIds" => [
                "manager8723"
            ],
            "permitDeptIds" => [
                12345
            ],
            "permitTagIds" => [
                11111
            ],
            "protectScenes" => [
                "CHAT"
            ]
        ]);
        try {
            $client->updateSeniorSettingWithOptions($updateSeniorSettingRequest, $updateSeniorSettingHeaders, new RuntimeOptions([]));
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

  updateSeniorSettingHeaders := &dingtalkcontact_1_0.UpdateSeniorSettingHeaders{}
  updateSeniorSettingHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateSeniorSettingRequest := &dingtalkcontact_1_0.UpdateSeniorSettingRequest{
    SeniorStaffId: tea.String("013349365367-1094322561"),
    Open: tea.Bool(true),
    PermitStaffIds: []*string{tea.String("manager8723")},
    PermitDeptIds: []*int64{tea.Int(12345)},
    PermitTagIds: []*int64{tea.Int(11111)},
    ProtectScenes: []*string{tea.String("CHAT")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateSeniorSettingWithOptions(updateSeniorSettingRequest, updateSeniorSettingHeaders, &util.RuntimeOptions{})
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
    let updateSeniorSettingHeaders = new $dingtalkcontact_1_0.UpdateSeniorSettingHeaders({ });
    updateSeniorSettingHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateSeniorSettingRequest = new $dingtalkcontact_1_0.UpdateSeniorSettingRequest({
      seniorStaffId: "013349365367-1094322561",
      open: true,
      permitStaffIds: [
        "manager8723"
      ],
      permitDeptIds: [
        12345
      ],
      permitTagIds: [
        11111
      ],
      protectScenes: [
        "CHAT"
      ],
    });
    try {
      await client.updateSeniorSettingWithOptions(updateSeniorSettingRequest, updateSeniorSettingHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateSeniorSettingHeaders updateSeniorSettingHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateSeniorSettingHeaders();
            updateSeniorSettingHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateSeniorSettingRequest updateSeniorSettingRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateSeniorSettingRequest
            {
                SeniorStaffId = "013349365367-1094322561",
                Open = true,
                PermitStaffIds = new List<string>
                {
                    "manager8723"
                },
                PermitDeptIds = new List<long?>
                {
                    12345
                },
                PermitTagIds = new List<long?>
                {
                    11111
                },
                ProtectScenes = new List<string>
                {
                    "CHAT"
                },
            };
            try
            {
                client.UpdateSeniorSettingWithOptions(updateSeniorSettingRequest, updateSeniorSettingHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateSeniorSettingHeaders> updateSeniorSettingHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateSeniorSettingHeaders>();
  updateSeniorSettingHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateSeniorSettingRequest> updateSeniorSettingRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateSeniorSettingRequest>(map<string, boost::any>({
    {"seniorStaffId", boost::any(string("013349365367-1094322561"))},
    {"open", boost::any(true)},
    {"permitStaffIds", boost::any(vector<string>({
      "manager8723"
    }))},
    {"permitDeptIds", boost::any(vector<long>({
      12345
    }))},
    {"permitTagIds", boost::any(vector<long>({
      11111
    }))},
    {"protectScenes", boost::any(vector<string>({
      "CHAT"
    }))}
  }));
  try {
    client->updateSeniorSettingWithOptions(updateSeniorSettingRequest, updateSeniorSettingHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 500 | system.error | 获取设置出错 | 获取设置出错 |
| 500 | parameter.orgNotExists | 组织不存在 | 组织不存在 |
| 500 | parameter.userNotExists | 用户不存在 | 用户不存在 |
