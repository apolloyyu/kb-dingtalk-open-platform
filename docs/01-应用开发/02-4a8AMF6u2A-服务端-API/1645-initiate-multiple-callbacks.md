---
title: "批量发起回调"
source_url: "https://open.dingtalk.com/document/development/initiate-multiple-callbacks"
namespace: "development"
slug: "initiate-multiple-callbacks"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 宜搭 > 应用 > 批量发起回调"
doc_id: "eolj1ZYA6N"
updated_at: "2026-08-25 13:50:04"
---

> Source: https://open.dingtalk.com/document/development/initiate-multiple-callbacks
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 宜搭 > 应用 > 批量发起回调
> Updated: 2026-08-25 13:50:04

# 批量发起回调

调用本接口批量发起宜搭VPC回调。

> **[!IMPORTANT]**
>
> 本接口后续不再支持新应用接入，已接入的应用可以正常调用。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 不支持 | — |

## 请求方法

```
POST /v1.0/yida/printings/callbacks/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "ossUrl" : "String",
  "corpId" : "String",
  "fileSize" : Long,
  "appType" : "String",
  "systemToken" : "String",
  "namespace" : "String",
  "timeZone" : "String",
  "language" : "String",
  "source" : "String",
  "sequenceId" : "String",
  "userId" : "String",
  "status" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| ossUrl | String | 否 | oss文件链接。 |
| corpId | String | 否 | 组织的corpId。 |
| fileSize | Long | 否 | 文件大小。 |
| appType | String | 否 | 应用ID。 |
| systemToken | String | 否 | 应用密钥，在应用数据中获取。 |
| namespace | String | 否 | 名称空间。 |
| timeZone | String | 否 | 时间区域。 |
| language | String | 否 | 语言，取值：   - zh\_CN：中文（默认值） - en\_US：英文 |
| source | String | 否 | 源。 |
| sequenceId | String | 否 | 流水号。 |
| userId | String | 否 | 用户的userid。 |
| status | String | 否 | 状态。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/yida/printings/callbacks/batch HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "ossUrl" : "https://oss/com/a/b.pdf",
  "corpId" : "ding123",
  "fileSize" : 123789,
  "appType" : "APP_PBKT0MFBEBTDO8T7SLVP",
  "systemToken" : "hexxxx",
  "namespace" : "dingtalk",
  "timeZone" : "GMT",
  "language" : "zh_CN",
  "source" : "宜搭",
  "sequenceId" : "seq-xxx",
  "userId" : "manager123",
  "status" : "running"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkyida_1_0.*;
import com.aliyun.dingtalkyida_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkyida_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkyida_1_0.Client client = Sample.createClient();
        RenderBatchCallbackHeaders renderBatchCallbackHeaders = new RenderBatchCallbackHeaders();
        renderBatchCallbackHeaders.xAcsDingtalkAccessToken = "<your access token>";
        RenderBatchCallbackRequest renderBatchCallbackRequest = new RenderBatchCallbackRequest()
                .setOssUrl("https://oss/com/a/b.pdf")
                .setCorpId("ding123")
                .setFileSize(123789L)
                .setAppType("APP_PBKT0MFBEBTDO8T7SLVP")
                .setSystemToken("hexxxx")
                .setNamespace("dingtalk")
                .setTimeZone("GMT")
                .setLanguage("zh_CN")
                .setSource("宜搭")
                .setSequenceId("seq-xxx")
                .setUserId("manager123")
                .setStatus("running");
        try {
            client.renderBatchCallbackWithOptions(renderBatchCallbackRequest, renderBatchCallbackHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        render_batch_callback_headers = dingtalkyida__1__0_models.RenderBatchCallbackHeaders()
        render_batch_callback_headers.x_acs_dingtalk_access_token = '<your access token>'
        render_batch_callback_request = dingtalkyida__1__0_models.RenderBatchCallbackRequest(
            oss_url='https://oss/com/a/b.pdf',
            corp_id='ding123',
            file_size=123789,
            app_type='APP_PBKT0MFBEBTDO8T7SLVP',
            system_token='hexxxx',
            namespace='dingtalk',
            time_zone='GMT',
            language='zh_CN',
            source='宜搭',
            sequence_id='seq-xxx',
            user_id='manager123',
            status='running'
        )
        try:
            client.render_batch_callback_with_options(render_batch_callback_request, render_batch_callback_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        render_batch_callback_headers = dingtalkyida__1__0_models.RenderBatchCallbackHeaders()
        render_batch_callback_headers.x_acs_dingtalk_access_token = '<your access token>'
        render_batch_callback_request = dingtalkyida__1__0_models.RenderBatchCallbackRequest(
            oss_url='https://oss/com/a/b.pdf',
            corp_id='ding123',
            file_size=123789,
            app_type='APP_PBKT0MFBEBTDO8T7SLVP',
            system_token='hexxxx',
            namespace='dingtalk',
            time_zone='GMT',
            language='zh_CN',
            source='宜搭',
            sequence_id='seq-xxx',
            user_id='manager123',
            status='running'
        )
        try:
            await client.render_batch_callback_with_options_async(render_batch_callback_request, render_batch_callback_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\RenderBatchCallbackHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\RenderBatchCallbackRequest;
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
        $renderBatchCallbackHeaders = new RenderBatchCallbackHeaders([]);
        $renderBatchCallbackHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $renderBatchCallbackRequest = new RenderBatchCallbackRequest([
            "ossUrl" => "https://oss/com/a/b.pdf",
            "corpId" => "ding123",
            "fileSize" => 123789,
            "appType" => "APP_PBKT0MFBEBTDO8T7SLVP",
            "systemToken" => "hexxxx",
            "namespace" => "dingtalk",
            "timeZone" => "GMT",
            "language" => "zh_CN",
            "source" => "宜搭",
            "sequenceId" => "seq-xxx",
            "userId" => "manager123",
            "status" => "running"
        ]);
        try {
            $client->renderBatchCallbackWithOptions($renderBatchCallbackRequest, $renderBatchCallbackHeaders, new RuntimeOptions([]));
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
  dingtalkyida_1_0  "github.com/alibabacloud-go/dingtalk/yida_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkyida_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_1_0.Client{}
  _result, _err = dingtalkyida_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  renderBatchCallbackHeaders := &dingtalkyida_1_0.RenderBatchCallbackHeaders{}
  renderBatchCallbackHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  renderBatchCallbackRequest := &dingtalkyida_1_0.RenderBatchCallbackRequest{
    OssUrl: tea.String("https://oss/com/a/b.pdf"),
    CorpId: tea.String("ding123"),
    FileSize: tea.Int64(123789),
    AppType: tea.String("APP_PBKT0MFBEBTDO8T7SLVP"),
    SystemToken: tea.String("hexxxx"),
    Namespace: tea.String("dingtalk"),
    TimeZone: tea.String("GMT"),
    Language: tea.String("zh_CN"),
    Source: tea.String("宜搭"),
    SequenceId: tea.String("seq-xxx"),
    UserId: tea.String("manager123"),
    Status: tea.String("running"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RenderBatchCallbackWithOptions(renderBatchCallbackRequest, renderBatchCallbackHeaders, &util.RuntimeOptions{})
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
import dingtalkyida_1_0, * as $dingtalkyida_1_0 from '@alicloud/dingtalk/yida_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkyida_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkyida_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let renderBatchCallbackHeaders = new $dingtalkyida_1_0.RenderBatchCallbackHeaders({ });
    renderBatchCallbackHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let renderBatchCallbackRequest = new $dingtalkyida_1_0.RenderBatchCallbackRequest({
      ossUrl: "https://oss/com/a/b.pdf",
      corpId: "ding123",
      fileSize: 123789,
      appType: "APP_PBKT0MFBEBTDO8T7SLVP",
      systemToken: "hexxxx",
      namespace: "dingtalk",
      timeZone: "GMT",
      language: "zh_CN",
      source: "宜搭",
      sequenceId: "seq-xxx",
      userId: "manager123",
      status: "running",
    });
    try {
      await client.renderBatchCallbackWithOptions(renderBatchCallbackRequest, renderBatchCallbackHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.RenderBatchCallbackHeaders renderBatchCallbackHeaders = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.RenderBatchCallbackHeaders();
            renderBatchCallbackHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.RenderBatchCallbackRequest renderBatchCallbackRequest = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.RenderBatchCallbackRequest
            {
                OssUrl = "https://oss/com/a/b.pdf",
                CorpId = "ding123",
                FileSize = 123789,
                AppType = "APP_PBKT0MFBEBTDO8T7SLVP",
                SystemToken = "hexxxx",
                Namespace = "dingtalk",
                TimeZone = "GMT",
                Language = "zh_CN",
                Source = "宜搭",
                SequenceId = "seq-xxx",
                UserId = "manager123",
                Status = "running",
            };
            try
            {
                client.RenderBatchCallbackWithOptions(renderBatchCallbackRequest, renderBatchCallbackHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkyida__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkyida_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkyida_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::Client> client = make_shared<Alibabacloud_Dingtalkyida_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::RenderBatchCallbackHeaders> renderBatchCallbackHeaders = make_shared<Alibabacloud_Dingtalkyida_1_0::RenderBatchCallbackHeaders>();
  renderBatchCallbackHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::RenderBatchCallbackRequest> renderBatchCallbackRequest = make_shared<Alibabacloud_Dingtalkyida_1_0::RenderBatchCallbackRequest>(map<string, boost::any>({
    {"ossUrl", boost::any(string("https://oss/com/a/b.pdf"))},
    {"corpId", boost::any(string("ding123"))},
    {"fileSize", boost::any(123789)},
    {"appType", boost::any(string("APP_PBKT0MFBEBTDO8T7SLVP"))},
    {"systemToken", boost::any(string("hexxxx"))},
    {"namespace", boost::any(string("dingtalk"))},
    {"timeZone", boost::any(string("GMT"))},
    {"language", boost::any(string("zh_CN"))},
    {"source", boost::any(string("宜搭"))},
    {"sequenceId", boost::any(string("seq-xxx"))},
    {"userId", boost::any(string("manager123"))},
    {"status", boost::any(string("running"))}
  }));
  try {
    client->renderBatchCallbackWithOptions(renderBatchCallbackRequest, renderBatchCallbackHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | unclassifiedError | 异常:%s | 通用异常信息 |
