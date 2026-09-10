---
title: "发送邀请函"
source_url: "https://open.dingtalk.com/document/development/send-invitations"
namespace: "development"
slug: "send-invitations"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 产业互联 > 发送邀请函"
doc_id: "OH12M9flPX"
updated_at: "2026-06-02 19:14:52"
---

> Source: https://open.dingtalk.com/document/development/send-invitations
> Path: 应用开发 / 服务端 API / 专属钉钉 > 产业互联 > 发送邀请函
> Updated: 2026-06-02 19:14:52

# 发送邀请函

调用本接口向下游企业发送加入合作伙伴邀请函。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/partnerDepartments/invitations/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Partner.Department.Write-伙伴钉部门信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| deptId | String | 是 | 部门ID。 |
| partnerNum | String | 是 | 伙伴编码。 |
| partnerLabelId | Long | 是 | 伙伴标签ID。 |
| phone | String | 是 | 手机号。 |
| orgAlias | String | 是 | 组织别名。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/partnerDepartments/invitations/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:8eef0xxx
Content-Type:application/json

{
  "deptId" : "1234",
  "partnerNum" : "1234",
  "partnerLabelId" : 1234,
  "phone" : "133XXXXXX57",
  "orgAlias" : "钉开放组织别名"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        SendInvitationHeaders sendInvitationHeaders = new SendInvitationHeaders();
        sendInvitationHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendInvitationRequest sendInvitationRequest = new SendInvitationRequest()
                .setDeptId("1234")
                .setPartnerNum("1234")
                .setPartnerLabelId(1234L)
                .setPhone("133XXXXXX57")
                .setOrgAlias("钉开放组织别名");
        try {
            client.sendInvitationWithOptions(sendInvitationRequest, sendInvitationHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_invitation_headers = dingtalkexclusive__1__0_models.SendInvitationHeaders()
        send_invitation_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_invitation_request = dingtalkexclusive__1__0_models.SendInvitationRequest(
            dept_id='1234',
            partner_num='1234',
            partner_label_id=1234,
            phone='133XXXXXX57',
            org_alias='钉开放组织别名'
        )
        try:
            client.send_invitation_with_options(send_invitation_request, send_invitation_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_invitation_headers = dingtalkexclusive__1__0_models.SendInvitationHeaders()
        send_invitation_headers.x_acs_dingtalk_access_token = '<your access token>'
        send_invitation_request = dingtalkexclusive__1__0_models.SendInvitationRequest(
            dept_id='1234',
            partner_num='1234',
            partner_label_id=1234,
            phone='133XXXXXX57',
            org_alias='钉开放组织别名'
        )
        try:
            await client.send_invitation_with_options_async(send_invitation_request, send_invitation_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendInvitationHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendInvitationRequest;
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
        $sendInvitationHeaders = new SendInvitationHeaders([]);
        $sendInvitationHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sendInvitationRequest = new SendInvitationRequest([
            "deptId" => "1234",
            "partnerNum" => "1234",
            "partnerLabelId" => 1234,
            "phone" => "133XXXXXX57",
            "orgAlias" => "钉开放组织别名"
        ]);
        try {
            $client->sendInvitationWithOptions($sendInvitationRequest, $sendInvitationHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendInvitationHeaders := &dingtalkexclusive_1_0.SendInvitationHeaders{}
  sendInvitationHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sendInvitationRequest := &dingtalkexclusive_1_0.SendInvitationRequest{
    DeptId: tea.String("1234"),
    PartnerNum: tea.String("1234"),
    PartnerLabelId: tea.Int64(1234),
    Phone: tea.String("133XXXXXX57"),
    OrgAlias: tea.String("钉开放组织别名"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendInvitationWithOptions(sendInvitationRequest, sendInvitationHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let sendInvitationHeaders = new $dingtalkexclusive_1_0.SendInvitationHeaders({ });
    sendInvitationHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sendInvitationRequest = new $dingtalkexclusive_1_0.SendInvitationRequest({
      deptId: "1234",
      partnerNum: "1234",
      partnerLabelId: 1234,
      phone: "133XXXXXX57",
      orgAlias: "钉开放组织别名",
    });
    try {
      await client.sendInvitationWithOptions(sendInvitationRequest, sendInvitationHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendInvitationHeaders sendInvitationHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendInvitationHeaders();
            sendInvitationHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendInvitationRequest sendInvitationRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendInvitationRequest
            {
                DeptId = "1234",
                PartnerNum = "1234",
                PartnerLabelId = 1234,
                Phone = "133XXXXXX57",
                OrgAlias = "钉开放组织别名",
            };
            try
            {
                client.SendInvitationWithOptions(sendInvitationRequest, sendInvitationHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkexclusive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkexclusive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkexclusive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkexclusive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::SendInvitationHeaders> sendInvitationHeaders = make_shared<Alibabacloud_Dingtalkexclusive_1_0::SendInvitationHeaders>();
  sendInvitationHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::SendInvitationRequest> sendInvitationRequest = make_shared<Alibabacloud_Dingtalkexclusive_1_0::SendInvitationRequest>(map<string, boost::any>({
    {"deptId", boost::any(string("1234"))},
    {"partnerNum", boost::any(string("1234"))},
    {"partnerLabelId", boost::any(1234)},
    {"phone", boost::any(string("133XXXXXX57"))},
    {"orgAlias", boost::any(string("钉开放组织别名"))}
  }));
  try {
    client->sendInvitationWithOptions(sendInvitationRequest, sendInvitationHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| 400 | param.illegal | 参数不合法 | 参数不合法 |
| 500 | system.busy | 系统内部错误 | 系统内部错误 |
