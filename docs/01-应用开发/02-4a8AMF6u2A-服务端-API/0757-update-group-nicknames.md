---
title: "更新场景群成员的群昵称"
source_url: "https://open.dingtalk.com/document/development/update-group-nicknames"
namespace: "development"
slug: "update-group-nicknames"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群管理 > 更新场景群成员的群昵称"
doc_id: "tHiOmCEpdD"
updated_at: "2026-08-14 09:42:00"
---

> Source: https://open.dingtalk.com/document/development/update-group-nicknames
> Path: 应用开发 / 服务端 API / 即时通信 > 会话管理 > 场景群 > 群管理 > 更新场景群成员的群昵称
> Updated: 2026-08-14 09:42:00

# 更新场景群成员的群昵称

调用本接口，根据群id和群成员id，更新群成员的群昵称，适用于群管理员或群成员需要修改群成员在群内的昵称的场景，如群成员希望使用更具辨识度的昵称，或管理员为了统一管理修改成员昵称。

## **接口调用说明**

支持以下场景使用：基于群模板创建的群，详情参见[创建群](1486-create-a-scene-group-v2.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/im/sceneGroups/members/groupNicks |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openConversationId | String | 是 | 群ID，可调用[创建群](1486-create-a-scene-group-v2.md)接口获取`open_conversation_id`参数值。 |
| userId | String | 是 | 用户的userid，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| groupNick | String | 是 | 用户群昵称，最长不超过30字符，建议长度在10字符以内。 |

### 请求示例

HTTP

```
PUT /v1.0/im/sceneGroups/members/groupNicks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "openConversationId" : "cidXxxx",
  "userId" : "user123",
  "groupNick" : "张三的群昵称"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkim_1_0.*;
import com.aliyun.dingtalkim_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkim_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_1_0.Client client = Sample.createClient();
        UpdateMemberGroupNickHeaders updateMemberGroupNickHeaders = new UpdateMemberGroupNickHeaders();
        updateMemberGroupNickHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateMemberGroupNickRequest updateMemberGroupNickRequest = new UpdateMemberGroupNickRequest()
                .setOpenConversationId("cidXxxx")
                .setUserId("user123")
                .setGroupNick("张三的群昵称");
        try {
            client.updateMemberGroupNickWithOptions(updateMemberGroupNickRequest, updateMemberGroupNickHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.im_1_0.client import Client as dingtalkim_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.im_1_0 import models as dingtalkim__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkim_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_member_group_nick_headers = dingtalkim__1__0_models.UpdateMemberGroupNickHeaders()
        update_member_group_nick_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_member_group_nick_request = dingtalkim__1__0_models.UpdateMemberGroupNickRequest(
            open_conversation_id='cidXxxx',
            user_id='user123',
            group_nick='张三的群昵称'
        )
        try:
            client.update_member_group_nick_with_options(update_member_group_nick_request, update_member_group_nick_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_member_group_nick_headers = dingtalkim__1__0_models.UpdateMemberGroupNickHeaders()
        update_member_group_nick_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_member_group_nick_request = dingtalkim__1__0_models.UpdateMemberGroupNickRequest(
            open_conversation_id='cidXxxx',
            user_id='user123',
            group_nick='张三的群昵称'
        )
        try:
            await client.update_member_group_nick_with_options_async(update_member_group_nick_request, update_member_group_nick_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateMemberGroupNickHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_1_0\Models\UpdateMemberGroupNickRequest;
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
        $updateMemberGroupNickHeaders = new UpdateMemberGroupNickHeaders([]);
        $updateMemberGroupNickHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateMemberGroupNickRequest = new UpdateMemberGroupNickRequest([
            "openConversationId" => "cidXxxx",
            "userId" => "user123",
            "groupNick" => "张三的群昵称"
        ]);
        try {
            $client->updateMemberGroupNickWithOptions($updateMemberGroupNickRequest, $updateMemberGroupNickHeaders, new RuntimeOptions([]));
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
  dingtalkim_1_0  "github.com/alibabacloud-go/dingtalk/im_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkim_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkim_1_0.Client{}
  _result, _err = dingtalkim_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateMemberGroupNickHeaders := &dingtalkim_1_0.UpdateMemberGroupNickHeaders{}
  updateMemberGroupNickHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateMemberGroupNickRequest := &dingtalkim_1_0.UpdateMemberGroupNickRequest{
    OpenConversationId: tea.String("cidXxxx"),
    UserId: tea.String("user123"),
    GroupNick: tea.String("张三的群昵称"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateMemberGroupNickWithOptions(updateMemberGroupNickRequest, updateMemberGroupNickHeaders, &util.RuntimeOptions{})
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
import dingtalkim_1_0, * as $dingtalkim_1_0 from '@alicloud/dingtalk/im_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkim_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkim_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let updateMemberGroupNickHeaders = new $dingtalkim_1_0.UpdateMemberGroupNickHeaders({ });
    updateMemberGroupNickHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateMemberGroupNickRequest = new $dingtalkim_1_0.UpdateMemberGroupNickRequest({
      openConversationId: "cidXxxx",
      userId: "user123",
      groupNick: "张三的群昵称",
    });
    try {
      await client.updateMemberGroupNickWithOptions(updateMemberGroupNickRequest, updateMemberGroupNickHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkim_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkim_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkim_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberGroupNickHeaders updateMemberGroupNickHeaders = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberGroupNickHeaders();
            updateMemberGroupNickHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberGroupNickRequest updateMemberGroupNickRequest = new AlibabaCloud.SDK.Dingtalkim_1_0.Models.UpdateMemberGroupNickRequest
            {
                OpenConversationId = "cidXxxx",
                UserId = "user123",
                GroupNick = "张三的群昵称",
            };
            try
            {
                client.UpdateMemberGroupNickWithOptions(updateMemberGroupNickRequest, updateMemberGroupNickHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkim__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkim_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkim_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkim_1_0::Client> client = make_shared<Alibabacloud_Dingtalkim_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkim_1_0::UpdateMemberGroupNickHeaders> updateMemberGroupNickHeaders = make_shared<Alibabacloud_Dingtalkim_1_0::UpdateMemberGroupNickHeaders>();
  updateMemberGroupNickHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkim_1_0::UpdateMemberGroupNickRequest> updateMemberGroupNickRequest = make_shared<Alibabacloud_Dingtalkim_1_0::UpdateMemberGroupNickRequest>(map<string, boost::any>({
    {"openConversationId", boost::any(string("cidXxxx"))},
    {"userId", boost::any(string("user123"))},
    {"groupNick", boost::any(string("张三的群昵称"))}
  }));
  try {
    client->updateMemberGroupNickWithOptions(updateMemberGroupNickRequest, updateMemberGroupNickHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| success | Boolean | 调用是否成功：   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | systemError | 系统异常 | 系统异常 |
| 400 | paramIllegal | 参数非法 | 参数非法 |
| 400 | userNotInGroup | 用户不在群内 | 用户不在群内 |
| 400 | groupNickForbid | 昵称内容非法 | 昵称内容非法 |
| 400 | invalidUserId | 无效的用户ID | 无效的用户ID |
| 400 | openConversationIdDecriptFailed | 群 ID 解码失败 | 群 ID 解码失败 |
| 400 | groupPermissionDenied | 无权限访问此群数据 | 无权限访问此群数据 |
| 400 | grayControlDenied | 接口灰度中暂时无法使用 | 接口灰度中暂时无法使用 |
| 400 | apiPermissionDenied | 无权限访问此接口 | 无权限访问此接口 |
| 400 | commonParamIllegal | 网关入参非法 | 网关入参非法 |
| 400 | paramBlank | 请求参数为空 | 请求参数为空 |
| 500 | systemBusy | 系统繁忙 | 系统繁忙 |
