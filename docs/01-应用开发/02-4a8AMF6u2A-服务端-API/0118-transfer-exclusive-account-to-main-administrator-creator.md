---
title: "企业账号转交主管理员（创建者）"
source_url: "https://open.dingtalk.com/document/development/transfer-exclusive-account-to-main-administrator-creator"
namespace: "development"
slug: "transfer-exclusive-account-to-main-administrator-creator"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 企业账号 > 企业账号转交主管理员（创建者）"
doc_id: "7lOl6H6zqn"
updated_at: "2026-06-01 16:05:16"
---

> Source: https://open.dingtalk.com/document/development/transfer-exclusive-account-to-main-administrator-creator
> Path: 应用开发 / 服务端 API / 通讯录管理 > 企业账号 > 企业账号转交主管理员（创建者）
> Updated: 2026-06-01 16:05:16

# 企业账号转交主管理员（创建者）

调用本接口，将本组织内某企业账号有所有权的组织，转交给另一企业账号，如果接收的账号不在该组织内则自动加入。

## 接口调用说明

例如，钉钉组织A下有两个企业账号，分别为企业账号A1和企业账号A2，其中企业账号A1是另一企业名称为钉钉组织B的创建者身份（当前测试企业OA管理后台-安全与权限-主管理员列表可查看）。调用本接口可用于把钉钉组织B的创建者身份变更为企业账号A2。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/orgAccounts/mainAdministrators/change |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Contact.OrgAccountSecurity.ReadWrite-通讯录企业账号安全数据读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| sourceUserId | String | 是 | 原企业账号userid，可通过以下四种方式获得：   - [根据手机号查询企业账号用户](0117-obtain-the-userid-of-your-mobile-phone-number.md) - [创建SSO企业账号](0104-create-an-sso-account.md) - [创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md) - [邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md) |
| targetUserId | String | 是 | 接收专属账号userid，可通过以下四种方式获得：   - [根据手机号查询企业账号用户](0117-obtain-the-userid-of-your-mobile-phone-number.md) - [创建SSO企业账号](0104-create-an-sso-account.md) - [创建钉钉自建企业账号](0106-create-dingtalk-user-created-dedicated-account.md) - [邀请其他组织企业账号加入](0115-invite-other-organization-specific-accounts-to-join.md) |
| effectCorpId | String | 是 | 被转交的组织corpId。详情参见基础概念-[CorpId](https://open.dingtalk.com/document/development/basic-concepts-beta#section-bbk-mv0-oxd)。 |

### 请求示例

HTTP

```
POST /v1.0/contact/orgAccounts/mainAdministrators/change HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "sourceUserId" : "userIdAA",
  "targetUserId" : "userIdBB",
  "effectCorpId" : "corpIdCCC"
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
        ChangeMainAdminHeaders changeMainAdminHeaders = new ChangeMainAdminHeaders();
        changeMainAdminHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ChangeMainAdminRequest changeMainAdminRequest = new ChangeMainAdminRequest()
                .setSourceUserId("userIdAA")
                .setTargetUserId("userIdBB")
                .setEffectCorpId("corpIdCCC");
        try {
            client.changeMainAdminWithOptions(changeMainAdminRequest, changeMainAdminHeaders, new RuntimeOptions());
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
        change_main_admin_headers = dingtalkcontact__1__0_models.ChangeMainAdminHeaders()
        change_main_admin_headers.x_acs_dingtalk_access_token = '<your access token>'
        change_main_admin_request = dingtalkcontact__1__0_models.ChangeMainAdminRequest(
            source_user_id='userIdAA',
            target_user_id='userIdBB',
            effect_corp_id='corpIdCCC'
        )
        try:
            client.change_main_admin_with_options(change_main_admin_request, change_main_admin_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        change_main_admin_headers = dingtalkcontact__1__0_models.ChangeMainAdminHeaders()
        change_main_admin_headers.x_acs_dingtalk_access_token = '<your access token>'
        change_main_admin_request = dingtalkcontact__1__0_models.ChangeMainAdminRequest(
            source_user_id='userIdAA',
            target_user_id='userIdBB',
            effect_corp_id='corpIdCCC'
        )
        try:
            await client.change_main_admin_with_options_async(change_main_admin_request, change_main_admin_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ChangeMainAdminHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\ChangeMainAdminRequest;
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
        $changeMainAdminHeaders = new ChangeMainAdminHeaders([]);
        $changeMainAdminHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $changeMainAdminRequest = new ChangeMainAdminRequest([
            "sourceUserId" => "userIdAA",
            "targetUserId" => "userIdBB",
            "effectCorpId" => "corpIdCCC"
        ]);
        try {
            $client->changeMainAdminWithOptions($changeMainAdminRequest, $changeMainAdminHeaders, new RuntimeOptions([]));
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

  changeMainAdminHeaders := &dingtalkcontact_1_0.ChangeMainAdminHeaders{}
  changeMainAdminHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  changeMainAdminRequest := &dingtalkcontact_1_0.ChangeMainAdminRequest{
    SourceUserId: tea.String("userIdAA"),
    TargetUserId: tea.String("userIdBB"),
    EffectCorpId: tea.String("corpIdCCC"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ChangeMainAdminWithOptions(changeMainAdminRequest, changeMainAdminHeaders, &util.RuntimeOptions{})
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
    let changeMainAdminHeaders = new $dingtalkcontact_1_0.ChangeMainAdminHeaders({ });
    changeMainAdminHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let changeMainAdminRequest = new $dingtalkcontact_1_0.ChangeMainAdminRequest({
      sourceUserId: "userIdAA",
      targetUserId: "userIdBB",
      effectCorpId: "corpIdCCC",
    });
    try {
      await client.changeMainAdminWithOptions(changeMainAdminRequest, changeMainAdminHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeMainAdminHeaders changeMainAdminHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeMainAdminHeaders();
            changeMainAdminHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeMainAdminRequest changeMainAdminRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.ChangeMainAdminRequest
            {
                SourceUserId = "userIdAA",
                TargetUserId = "userIdBB",
                EffectCorpId = "corpIdCCC",
            };
            try
            {
                client.ChangeMainAdminWithOptions(changeMainAdminRequest, changeMainAdminHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::ChangeMainAdminHeaders> changeMainAdminHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::ChangeMainAdminHeaders>();
  changeMainAdminHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::ChangeMainAdminRequest> changeMainAdminRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::ChangeMainAdminRequest>(map<string, boost::any>({
    {"sourceUserId", boost::any(string("userIdAA"))},
    {"targetUserId", boost::any(string("userIdBB"))},
    {"effectCorpId", boost::any(string("corpIdCCC"))}
  }));
  try {
    client->changeMainAdminWithOptions(changeMainAdminRequest, changeMainAdminHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Boolean | 转接操作结果。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | not.main.administrator | 不是主管理员(创建者) | 不是主管理员(创建者) |
| 400 | exclusive.account.limit | 只能操作归属该组织的专属账号 | 只能操作归属该组织的专属账号 |
| 400 | profile.not.exist | 账号不存在 | 账号不存在 |
| 400 | employee.not.exist | 员工不存在 | 员工不存在 |
| 400 | invalid.param | 无效参数 | sourceUserId/targetUserId/effectCorpId不能为空，并且effectCorpId需要是真实存在的组织id |
| 500 | system.busy | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
