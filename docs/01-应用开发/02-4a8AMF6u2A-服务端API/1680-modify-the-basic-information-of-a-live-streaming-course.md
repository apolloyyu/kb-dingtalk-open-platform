---
title: "修改培训课程"
source_url: "https://open.dingtalk.com/document/development/modify-the-basic-information-of-a-live-streaming-course"
namespace: "development"
slug: "modify-the-basic-information-of-a-live-streaming-course"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 培训 > 修改培训课程"
doc_id: "MDIVml2x2Z"
updated_at: "2025-10-17 17:00:37"
---

> Source: https://open.dingtalk.com/document/development/modify-the-basic-information-of-a-live-streaming-course
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 培训 > 修改培训课程
> Updated: 2025-10-17 17:00:37

# 修改培训课程

调用本接口修改培训课程的基本信息，如课程标题、课程简介、课程封面等。如果课程类型为直播，在没开始直播时，可修改预计的开播时间。

> **[!IMPORTANT]**
>
> 为提升接口使用体验，针对培训课程相关接口规范进行升级，本文接口文档已于2022年9月23日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力。
>
> - 如果未使用本接口，推荐使用[修改直播属性信息](https://open.dingtalk.com/document/isvapp/modify-live-streaming)接口。
> - 如果已使用本接口，建议您根据自身实际情况评估是否切换至推荐接口。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 暂不支持 | 直播培训平台写权限 | 暂不支持 |
| 第三方企业应用 | 支持 | 直播培训平台写权限 | [API Explorer](https://open-dev.dingtalk.com/apiExplorer#/?devType=isv&api=live_1.0%23UpdateLiveFeed) |
| 第三方个人应用 | 暂不支持 | 直播培训平台写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/live/openFeeds/{feedId}?userId=String&startTime=Long&coverUrl=String&title=String&introduction=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| feedId | String | 是 | 课程id，可通过[创建培训课程](https://open.dingtalk.com/document/isvapp/create-live-courses)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 修改者在组织内的userid。 |
| startTime | Long | 否 | 预计开始时间，单位为毫秒值。  **[!NOTE]**  课程必须预告状态才可以修改该项。 |
| coverUrl | String | 否 | 封面图url。 |
| title | String | 否 | 课程标题。 |
| introduction | String | 否 | 课程简介。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| hasUpdate | Boolean | 是否修改成功。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/live/openFeeds/7d296823-d0d3-?userId=12061863517&startTime=1617436058000&coverUrl=http:xxx.png&title=标题&introduction=简介 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bf360b06a0663c
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalklive_1_0.*;
import com.aliyun.dingtalklive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalklive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalklive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalklive_1_0.Client client = Sample.createClient();
        UpdateLiveFeedHeaders updateLiveFeedHeaders = new UpdateLiveFeedHeaders();
        updateLiveFeedHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateLiveFeedRequest updateLiveFeedRequest = new UpdateLiveFeedRequest()
                .setUserId("12061863517")
                .setStartTime(1617436058000L)
                .setCoverUrl("http:xxx.png")
                .setTitle("标题")
                .setIntroduction("简介");
        try {
            client.updateLiveFeedWithOptions("7d296823-d0d3-", updateLiveFeedRequest, updateLiveFeedHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.live_1_0.client import Client as dingtalklive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.live_1_0 import models as dingtalklive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalklive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalklive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_live_feed_headers = dingtalklive__1__0_models.UpdateLiveFeedHeaders()
        update_live_feed_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_live_feed_request = dingtalklive__1__0_models.UpdateLiveFeedRequest(
            user_id='12061863517',
            start_time=1617436058000,
            cover_url='http:xxx.png',
            title='标题',
            introduction='简介'
        )
        try:
            client.update_live_feed_with_options('7d296823-d0d3-', update_live_feed_request, update_live_feed_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_live_feed_headers = dingtalklive__1__0_models.UpdateLiveFeedHeaders()
        update_live_feed_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_live_feed_request = dingtalklive__1__0_models.UpdateLiveFeedRequest(
            user_id='12061863517',
            start_time=1617436058000,
            cover_url='http:xxx.png',
            title='标题',
            introduction='简介'
        )
        try:
            await client.update_live_feed_with_options_async('7d296823-d0d3-', update_live_feed_request, update_live_feed_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\UpdateLiveFeedHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\UpdateLiveFeedRequest;
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
        $updateLiveFeedHeaders = new UpdateLiveFeedHeaders([]);
        $updateLiveFeedHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateLiveFeedRequest = new UpdateLiveFeedRequest([
            "userId" => "12061863517",
            "startTime" => 1617436058000,
            "coverUrl" => "http:xxx.png",
            "title" => "标题",
            "introduction" => "简介"
        ]);
        try {
            $client->updateLiveFeedWithOptions("7d296823-d0d3-", $updateLiveFeedRequest, $updateLiveFeedHeaders, new RuntimeOptions([]));
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
  dingtalklive_1_0  "github.com/alibabacloud-go/dingtalk/live_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalklive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalklive_1_0.Client{}
  _result, _err = dingtalklive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateLiveFeedHeaders := &dingtalklive_1_0.UpdateLiveFeedHeaders{}
  updateLiveFeedHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateLiveFeedRequest := &dingtalklive_1_0.UpdateLiveFeedRequest{
    UserId: tea.String("12061863517"),
    StartTime: tea.Int64(1617436058000),
    CoverUrl: tea.String("http:xxx.png"),
    Title: tea.String("标题"),
    Introduction: tea.String("简介"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateLiveFeedWithOptions(tea.String("7d296823-d0d3-"), updateLiveFeedRequest, updateLiveFeedHeaders, &util.RuntimeOptions{})
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
import dingtalklive_1_0, * as $dingtalklive_1_0 from '@alicloud/dingtalk/live_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalklive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalklive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let updateLiveFeedHeaders = new $dingtalklive_1_0.UpdateLiveFeedHeaders({ });
    updateLiveFeedHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateLiveFeedRequest = new $dingtalklive_1_0.UpdateLiveFeedRequest({
      userId: "12061863517",
      startTime: 1617436058000,
      coverUrl: "http:xxx.png",
      title: "标题",
      introduction: "简介",
    });
    try {
      await client.updateLiveFeedWithOptions("7d296823-d0d3-", updateLiveFeedRequest, updateLiveFeedHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalklive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalklive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalklive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.UpdateLiveFeedHeaders updateLiveFeedHeaders = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.UpdateLiveFeedHeaders();
            updateLiveFeedHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.UpdateLiveFeedRequest updateLiveFeedRequest = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.UpdateLiveFeedRequest
            {
                UserId = "12061863517",
                StartTime = 1617436058000,
                CoverUrl = "http:xxx.png",
                Title = "标题",
                Introduction = "简介",
            };
            try
            {
                client.UpdateLiveFeedWithOptions("7d296823-d0d3-", updateLiveFeedRequest, updateLiveFeedHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalklive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalklive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalklive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalklive_1_0::Client> client = make_shared<Alibabacloud_Dingtalklive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalklive_1_0::UpdateLiveFeedHeaders> updateLiveFeedHeaders = make_shared<Alibabacloud_Dingtalklive_1_0::UpdateLiveFeedHeaders>();
  updateLiveFeedHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalklive_1_0::UpdateLiveFeedRequest> updateLiveFeedRequest = make_shared<Alibabacloud_Dingtalklive_1_0::UpdateLiveFeedRequest>(map<string, boost::any>({
    {"userId", boost::any(string("12061863517"))},
    {"startTime", boost::any(1617436058000)},
    {"coverUrl", boost::any(string("http:xxx.png"))},
    {"title", boost::any(string("标题"))},
    {"introduction", boost::any(string("简介"))}
  }));
  try {
    client->updateLiveFeedWithOptions(make_shared<string>("7d296823-d0d3-"), updateLiveFeedRequest, updateLiveFeedHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
Content-Type:application/json

{
  "hasUpdate" : true
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgSuiteAuthNotExit | access forbidden | 组织无权限访问 |
| 500 | systemError | error:%s | 系统错误 |
