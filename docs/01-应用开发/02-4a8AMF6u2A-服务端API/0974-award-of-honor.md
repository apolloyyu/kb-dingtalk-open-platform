---
title: "给员工颁发荣誉"
source_url: "https://open.dingtalk.com/document/development/award-of-honor"
namespace: "development"
slug: "award-of-honor"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 荣誉 > 给员工颁发荣誉"
doc_id: "ADB0QZGDS0"
updated_at: "2026-07-20 09:21:33"
---

> Source: https://open.dingtalk.com/document/development/award-of-honor
> Path: 应用开发 / 服务端API / 企业文化 > 荣誉 > 给员工颁发荣誉
> Updated: 2026-07-20 09:21:33

# 给员工颁发荣誉

调用本接口，用于给组织内的员工颁发荣誉。

## 接口调用说明

同一个企业corpid、同一个颁发人userId，不允许并发执行，防止颁发顺序出错。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/orgCulture/honors/{honorId}/grant |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-OrgCulture.Honor.Write-组织文化荣誉信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| honorId | String | 是 | 荣誉Id，可调用[查询当前企业下可颁发的荣誉列表](0976-query-the-list-of-honors-that-can-be-issued-under.md)接口获取honorId参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| senderUserId | String | 是 | 发送人userId。      如果是同一个发送人给多个员工颁发荣誉，请分别按照顺序执行，不允许并发执行，防止颁发顺序出错。 |
| grantReason | String | 是 | 颁奖词，最多100个字符。 |
| granterName | String | 是 | 颁奖人名字，最多50个字符。 |
| expirationTime | Long | 否 | 荣誉有效期到期时间戳，单位毫秒。   - 该参数值可不传，代表永久有效。 - 该参数值不允许传当天的时间戳。       有效期时间范围要求1~366天后，例如调用本接口的时间为2022-01-01 12:00:00，有效期时间范围是2022-01-01 12:00:00——2023-01-02 12:00:00。 |
| noticeSingle | Boolean | 否 | 是否发送单聊通知。   - **true**：发送 - **false**：不发送       如果该参数传true，荣誉接收人会收到发送人的单聊消息。 |
| noticeAnnouncer | Boolean | 否 | 是否使用官宣号通知获奖人。   - **true**：通知 - **false**：不通知       如果该参数传true，荣誉接收人会收到工作通知消息。 |
| receiverUserIds | Array of String | 是 | 接受人userId列表，最大值10。 |
| openConversationIds | Array of String | 否 | 接收荣誉消息的群openConversationId列表，最大值。   - 企业内部应用，可调用[创建群会话](0738-create-common-group-new-version-v2.md)接口获取openConversationId。 - 第三方企业应用，可调用[创建场景群](0746-create-a-scene-group.md)接口获取openConversationId。       荣誉发送人senderUserId，必须是群成员。 |

### 请求示例

HTTP

```
POST /v1.0/orgCulture/honors/10/grant HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bcsaf
Content-Type:application/json

{
  "senderUserId" : "user001",
  "grantReason" : "颁奖词",
  "granterName" : "张三",
  "expirationTime" : 1648437071000,
  "noticeSingle" : true,
  "noticeAnnouncer" : true,
  "receiverUserIds" : [ "user001" ],
  "openConversationIds" : [ "chxxxxx" ]
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
    public static com.aliyun.dingtalkorg_culture_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkorg_culture_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkorg_culture_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkorg_culture_1_0.models.GrantHonorHeaders grantHonorHeaders = new com.aliyun.dingtalkorg_culture_1_0.models.GrantHonorHeaders();
        grantHonorHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkorg_culture_1_0.models.GrantHonorRequest grantHonorRequest = new com.aliyun.dingtalkorg_culture_1_0.models.GrantHonorRequest()
                .setSenderUserId("user001")
                .setGrantReason("颁奖词")
                .setGranterName("张三")
                .setExpirationTime(1648437071000L)
                .setNoticeSingle(true)
                .setNoticeAnnouncer(true)
                .setReceiverUserIds(java.util.Arrays.asList(
                    "user001"
                ))
                .setOpenConversationIds(java.util.Arrays.asList(
                    "chxxxxx"
                ));
        try {
            client.grantHonorWithOptions("10", grantHonorRequest, grantHonorHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.orgCulture_1_0.client import Client as dingtalkorgCulture_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.orgCulture_1_0 import models as dingtalkorg_culture__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkorgCulture_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkorgCulture_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        grant_honor_headers = dingtalkorg_culture__1__0_models.GrantHonorHeaders()
        grant_honor_headers.x_acs_dingtalk_access_token = '<your access token>'
        grant_honor_request = dingtalkorg_culture__1__0_models.GrantHonorRequest(
            sender_user_id='user001',
            grant_reason='颁奖词',
            granter_name='张三',
            expiration_time=1648437071000,
            notice_single=True,
            notice_announcer=True,
            receiver_user_ids=[
                'user001'
            ],
            open_conversation_ids=[
                'chxxxxx'
            ]
        )
        try:
            client.grant_honor_with_options('10', grant_honor_request, grant_honor_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        grant_honor_headers = dingtalkorg_culture__1__0_models.GrantHonorHeaders()
        grant_honor_headers.x_acs_dingtalk_access_token = '<your access token>'
        grant_honor_request = dingtalkorg_culture__1__0_models.GrantHonorRequest(
            sender_user_id='user001',
            grant_reason='颁奖词',
            granter_name='张三',
            expiration_time=1648437071000,
            notice_single=True,
            notice_announcer=True,
            receiver_user_ids=[
                'user001'
            ],
            open_conversation_ids=[
                'chxxxxx'
            ]
        )
        try:
            await client.grant_honor_with_options_async('10', grant_honor_request, grant_honor_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\GrantHonorHeaders;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\GrantHonorRequest;
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
        $grantHonorHeaders = new GrantHonorHeaders([]);
        $grantHonorHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $grantHonorRequest = new GrantHonorRequest([
            "senderUserId" => "user001",
            "grantReason" => "颁奖词",
            "granterName" => "张三",
            "expirationTime" => 1648437071000,
            "noticeSingle" => true,
            "noticeAnnouncer" => true,
            "receiverUserIds" => [
                "user001"
            ],
            "openConversationIds" => [
                "chxxxxx"
            ]
        ]);
        try {
            $client->grantHonorWithOptions("10", $grantHonorRequest, $grantHonorHeaders, new RuntimeOptions([]));
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
  dingtalkorgculture_1_0  "github.com/alibabacloud-go/dingtalk/orgCulture_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkorgculture_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkorgculture_1_0.Client{}
  _result, _err = dingtalkorgculture_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  grantHonorHeaders := &dingtalkorgculture_1_0.GrantHonorHeaders{}
  grantHonorHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  grantHonorRequest := &dingtalkorgculture_1_0.GrantHonorRequest{
    SenderUserId: tea.String("user001"),
    GrantReason: tea.String("颁奖词"),
    GranterName: tea.String("张三"),
    ExpirationTime: tea.Int64(1648437071000),
    NoticeSingle: tea.Bool(true),
    NoticeAnnouncer: tea.Bool(true),
    ReceiverUserIds: []*string{tea.String("user001")},
    OpenConversationIds: []*string{tea.String("chxxxxx")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GrantHonorWithOptions(tea.String("10"), grantHonorRequest, grantHonorHeaders, &util.RuntimeOptions{})
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
import dingtalkorgCulture_1_0, * as $dingtalkorgCulture_1_0 from '@alicloud/dingtalk/orgCulture_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkorgCulture_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkorgCulture_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let grantHonorHeaders = new $dingtalkorgCulture_1_0.GrantHonorHeaders({ });
    grantHonorHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let grantHonorRequest = new $dingtalkorgCulture_1_0.GrantHonorRequest({
      senderUserId: "user001",
      grantReason: "颁奖词",
      granterName: "张三",
      expirationTime: 1648437071000,
      noticeSingle: true,
      noticeAnnouncer: true,
      receiverUserIds: [
        "user001"
      ],
      openConversationIds: [
        "chxxxxx"
      ],
    });
    try {
      await client.grantHonorWithOptions("10", grantHonorRequest, grantHonorHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.GrantHonorHeaders grantHonorHeaders = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.GrantHonorHeaders();
            grantHonorHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.GrantHonorRequest grantHonorRequest = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.GrantHonorRequest
            {
                SenderUserId = "user001",
                GrantReason = "颁奖词",
                GranterName = "张三",
                ExpirationTime = 1648437071000,
                NoticeSingle = true,
                NoticeAnnouncer = true,
                ReceiverUserIds = new List<string>
                {
                    "user001"
                },
                OpenConversationIds = new List<string>
                {
                    "chxxxxx"
                },
            };
            try
            {
                client.GrantHonorWithOptions("10", grantHonorRequest, grantHonorHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否调用成功，true表示调用成功。 |
| result | Object | 响应结果。 |
| successUserIds | Array of String | 返回成功的userId。 |
| failedUserIds | Array of String | 返回失败的userId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "successUserIds" : [ "user001" ],
    "failedUserIds" : [ "user002" ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | parameter.grantNameOverLength | 授予人名称需在50个字以内 | 授予人名称需在50个字以内 |
| 500 | parameter.grantOverSize | 最多可以颁发给10个人 | 最多可以颁发给10个人 |
| 500 | parameter.requestNull | 传入的参数为空 | 传入的参数为空 |
| 500 | parameter.grantReasonOverSize | 颁奖词需在100个字以内 | 颁奖词需在100个字以内 |
| 500 | request.often | 请求太频繁 | 请求太频繁 |
| 500 | parameter.userNotExist | 用户不在组织内 | 用户不在组织内 |
| 500 | system.error | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
| 500 | conversation.limit | 最大颁发通知到群的数量为5 | 最大颁发通知到群的数量为5 |
| 500 | conversation.wrong | 群不存在或者发送人不是群成员 | 群不存在或者发送人不是群成员 |
| 500 | parameter.expirationTimeWrong | 过期时间如果传值，需大于发放当天，且小于365天后 | 过期时间如果传值，则需大于发放当天，且小于365天后 |
