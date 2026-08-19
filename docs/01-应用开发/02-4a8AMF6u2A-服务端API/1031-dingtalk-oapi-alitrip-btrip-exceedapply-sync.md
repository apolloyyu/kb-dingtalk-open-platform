---
title: "回传第三方超标审批结果"
source_url: "https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-sync"
namespace: "development"
slug: "dingtalk-oapi-alitrip-btrip-exceedapply-sync"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 回传第三方超标审批结果"
doc_id: "XHJlaFVhmJ"
updated_at: "2026-01-29 14:31:00"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-oapi-alitrip-btrip-exceedapply-sync
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 回传第三方超标审批结果
> Updated: 2026-01-29 14:31:00

# 回传第三方超标审批结果

通过此接口回传第三方商旅系统中的超标审批结果至阿里商旅与钉钉平台，实现审批状态的同步。

## 接口调用说明

第三方超标审批单推送到企业后，企业审批结束，将审批结果回传给阿里商旅。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/exceedapply/sync |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限点 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| remark | String | 是 | 审批意见。 |
| applyId | String | 是 | 商旅超标审批单号。 |
| corpId | String | 是 | 企业的corpId。 |
| thirdpartyFlowId | String | 是 | 第三方流程实例ID。 |
| userId | String | 是 | 员工的userid。 |
| status | Integer | 是 | 审批单状态，取值：   - **1**：同意 - **2**：拒绝 |

### 请求示例

HTTP

```
POST /v1.0/alitrip/exceedapply/sync?remark=不同意&applyId=2345&corpId=ding12345&thirdpartyFlowId=12345&userId=weifeng&status=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:dca26861ca183b759de732ea5abe0b79
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkalitrip_1_0.*;
import com.aliyun.dingtalkalitrip_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkalitrip_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkalitrip_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkalitrip_1_0.Client client = Sample.createClient();
        SyncExceedApplyHeaders syncExceedApplyHeaders = new SyncExceedApplyHeaders();
        syncExceedApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SyncExceedApplyRequest syncExceedApplyRequest = new SyncExceedApplyRequest()
                .setRemark("不同意")
                .setApplyId("2345")
                .setCorpId("ding12345")
                .setThirdpartyFlowId("12345")
                .setUserId("weifeng")
                .setStatus(1);
        try {
            client.syncExceedApplyWithOptions(syncExceedApplyRequest, syncExceedApplyHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.alitrip_1_0.client import Client as dingtalkalitrip_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.alitrip_1_0 import models as dingtalkalitrip__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkalitrip_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkalitrip_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sync_exceed_apply_headers = dingtalkalitrip__1__0_models.SyncExceedApplyHeaders()
        sync_exceed_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        sync_exceed_apply_request = dingtalkalitrip__1__0_models.SyncExceedApplyRequest(
            remark='不同意',
            apply_id='2345',
            corp_id='ding12345',
            thirdparty_flow_id='12345',
            user_id='weifeng',
            status=1
        )
        try:
            client.sync_exceed_apply_with_options(sync_exceed_apply_request, sync_exceed_apply_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        sync_exceed_apply_headers = dingtalkalitrip__1__0_models.SyncExceedApplyHeaders()
        sync_exceed_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        sync_exceed_apply_request = dingtalkalitrip__1__0_models.SyncExceedApplyRequest(
            remark='不同意',
            apply_id='2345',
            corp_id='ding12345',
            thirdparty_flow_id='12345',
            user_id='weifeng',
            status=1
        )
        try:
            await client.sync_exceed_apply_with_options_async(sync_exceed_apply_request, sync_exceed_apply_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\SyncExceedApplyHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\SyncExceedApplyRequest;
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
        $syncExceedApplyHeaders = new SyncExceedApplyHeaders([]);
        $syncExceedApplyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $syncExceedApplyRequest = new SyncExceedApplyRequest([
            "remark" => "不同意",
            "applyId" => "2345",
            "corpId" => "ding12345",
            "thirdpartyFlowId" => "12345",
            "userId" => "weifeng",
            "status" => 1
        ]);
        try {
            $client->syncExceedApplyWithOptions($syncExceedApplyRequest, $syncExceedApplyHeaders, new RuntimeOptions([]));
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
  dingtalkalitrip_1_0  "github.com/alibabacloud-go/dingtalk/alitrip_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkalitrip_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkalitrip_1_0.Client{}
  _result, _err = dingtalkalitrip_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  syncExceedApplyHeaders := &dingtalkalitrip_1_0.SyncExceedApplyHeaders{}
  syncExceedApplyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  syncExceedApplyRequest := &dingtalkalitrip_1_0.SyncExceedApplyRequest{
    Remark: tea.String("不同意"),
    ApplyId: tea.String("2345"),
    CorpId: tea.String("ding12345"),
    ThirdpartyFlowId: tea.String("12345"),
    UserId: tea.String("weifeng"),
    Status: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SyncExceedApplyWithOptions(syncExceedApplyRequest, syncExceedApplyHeaders, &util.RuntimeOptions{})
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
import dingtalkalitrip_1_0, * as $dingtalkalitrip_1_0 from '@alicloud/dingtalk/alitrip_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkalitrip_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkalitrip_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let syncExceedApplyHeaders = new $dingtalkalitrip_1_0.SyncExceedApplyHeaders({ });
    syncExceedApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let syncExceedApplyRequest = new $dingtalkalitrip_1_0.SyncExceedApplyRequest({
      remark: "不同意",
      applyId: "2345",
      corpId: "ding12345",
      thirdpartyFlowId: "12345",
      userId: "weifeng",
      status: 1,
    });
    try {
      await client.syncExceedApplyWithOptions(syncExceedApplyRequest, syncExceedApplyHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.SyncExceedApplyHeaders syncExceedApplyHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.SyncExceedApplyHeaders();
            syncExceedApplyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.SyncExceedApplyRequest syncExceedApplyRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.SyncExceedApplyRequest
            {
                Remark = "不同意",
                ApplyId = "2345",
                CorpId = "ding12345",
                ThirdpartyFlowId = "12345",
                UserId = "weifeng",
                Status = 1,
            };
            try
            {
                client.SyncExceedApplyWithOptions(syncExceedApplyRequest, syncExceedApplyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkalitrip__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkalitrip_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkalitrip_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::Client> client = make_shared<Alibabacloud_Dingtalkalitrip_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::SyncExceedApplyHeaders> syncExceedApplyHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::SyncExceedApplyHeaders>();
  syncExceedApplyHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::SyncExceedApplyRequest> syncExceedApplyRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::SyncExceedApplyRequest>(map<string, boost::any>({
    {"remark", boost::any(string("不同意"))},
    {"applyId", boost::any(string("2345"))},
    {"corpId", boost::any(string("ding12345"))},
    {"thirdpartyFlowId", boost::any(string("12345"))},
    {"userId", boost::any(string("weifeng"))},
    {"status", boost::any(1)}
  }));
  try {
    client->syncExceedApplyWithOptions(syncExceedApplyRequest, syncExceedApplyHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| module | Boolean | 调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "module" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.param | 审批单已完成 | 审批单已完成 |
| 400 | invalid.authority | 没有操作企业数据权限 | 没有操作企业数据权限 |
| 400 | invalid.param | 找不到超标审批单 | 找不到超标审批单 |
| 500 | systemError | 系统错误 | 系统错误 |
