---
title: "剪辑直播课程回放"
source_url: "https://open.dingtalk.com/document/development/clip-live-course-playback"
namespace: "development"
slug: "clip-live-course-playback"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 培训 > 剪辑直播课程回放"
doc_id: "vO5Rc1qh94"
updated_at: "2025-10-17 17:01:36"
---

> Source: https://open.dingtalk.com/document/development/clip-live-course-playback
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 培训 > 剪辑直播课程回放
> Updated: 2025-10-17 17:01:36

# 剪辑直播课程回放

调用本接口剪辑课程直播的回放。

> **[!IMPORTANT]**
>
> 为提升接口的使用体验，剪辑直播课程回放接口正在升级，本API文档已于2022年9月23日移动至历史文档（不推荐）目录，接口不再支持新应用接入，已接入的应用可继续调用。新产品开放上线时间请关注文档更新日志。

> **[!NOTE]**
>
> - 剪辑回放会保存需要的片段，不会影响原有直播回放。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 暂不支持 | 直播培训平台写权限 | 暂不支持 |
| 第三方企业应用 | 支持 | 直播培训平台写权限 | — |
| 第三方个人应用 | 暂不支持 | 直播培训平台写权限 | 暂不支持 |

## 请求方法

```
POST /v1.0/live/openFeeds/{feedId}/cutReplay HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "userId" : "String",
  "editStartTime" : Long,
  "editEndTime" : Long
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| feedId | String | 是 | 直播课程ID，可通过[创建培训课程](https://open.dingtalk.com/document/isvapp/create-live-courses)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 剪辑者在组织内的userid。 |
| editStartTime | Long | 是 | 剪辑的起始位置的时间戳（在原开始结束的时间戳之内）。 |
| editEndTime | Long | 是 | 剪辑的结束位置的时间戳（在原开始结束的时间戳之内）。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | String | 剪辑后的视频地址（含authkey）。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/live/openFeeds/8c0ed3c3-e125-4a9d-aa40-18ad999398d4/cutReplay HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bf360b06a0663cd0a09afb5xxxx
Content-Type:application/json

{
  "userId" : "12061863",
  "editStartTime" : 1617336058000,
  "editEndTime" : 1617356058000
}
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
        EditFeedReplayHeaders editFeedReplayHeaders = new EditFeedReplayHeaders();
        editFeedReplayHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditFeedReplayRequest editFeedReplayRequest = new EditFeedReplayRequest()
                .setUserId("12061863")
                .setEditStartTime(1617336058000L)
                .setEditEndTime(1617356058000L);
        try {
            client.editFeedReplayWithOptions("8c0ed3c3-e125-4a9d-aa40-18ad999398d4", editFeedReplayRequest, editFeedReplayHeaders, new RuntimeOptions());
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
        edit_feed_replay_headers = dingtalklive__1__0_models.EditFeedReplayHeaders()
        edit_feed_replay_headers.x_acs_dingtalk_access_token = '<your access token>'
        edit_feed_replay_request = dingtalklive__1__0_models.EditFeedReplayRequest(
            user_id='12061863',
            edit_start_time=1617336058000,
            edit_end_time=1617356058000
        )
        try:
            client.edit_feed_replay_with_options('8c0ed3c3-e125-4a9d-aa40-18ad999398d4', edit_feed_replay_request, edit_feed_replay_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_feed_replay_headers = dingtalklive__1__0_models.EditFeedReplayHeaders()
        edit_feed_replay_headers.x_acs_dingtalk_access_token = '<your access token>'
        edit_feed_replay_request = dingtalklive__1__0_models.EditFeedReplayRequest(
            user_id='12061863',
            edit_start_time=1617336058000,
            edit_end_time=1617356058000
        )
        try:
            await client.edit_feed_replay_with_options_async('8c0ed3c3-e125-4a9d-aa40-18ad999398d4', edit_feed_replay_request, edit_feed_replay_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\EditFeedReplayHeaders;
use AlibabaCloud\SDK\Dingtalk\Vlive_1_0\Models\EditFeedReplayRequest;
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
        $editFeedReplayHeaders = new EditFeedReplayHeaders([]);
        $editFeedReplayHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $editFeedReplayRequest = new EditFeedReplayRequest([
            "userId" => "12061863",
            "editStartTime" => 1617336058000,
            "editEndTime" => 1617356058000
        ]);
        try {
            $client->editFeedReplayWithOptions("8c0ed3c3-e125-4a9d-aa40-18ad999398d4", $editFeedReplayRequest, $editFeedReplayHeaders, new RuntimeOptions([]));
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

  editFeedReplayHeaders := &dingtalklive_1_0.EditFeedReplayHeaders{}
  editFeedReplayHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  editFeedReplayRequest := &dingtalklive_1_0.EditFeedReplayRequest{
    UserId: tea.String("12061863"),
    EditStartTime: tea.Int64(1617336058000),
    EditEndTime: tea.Int64(1617356058000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.EditFeedReplayWithOptions(tea.String("8c0ed3c3-e125-4a9d-aa40-18ad999398d4"), editFeedReplayRequest, editFeedReplayHeaders, &util.RuntimeOptions{})
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
    let editFeedReplayHeaders = new $dingtalklive_1_0.EditFeedReplayHeaders({ });
    editFeedReplayHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let editFeedReplayRequest = new $dingtalklive_1_0.EditFeedReplayRequest({
      userId: "12061863",
      editStartTime: 1617336058000,
      editEndTime: 1617356058000,
    });
    try {
      await client.editFeedReplayWithOptions("8c0ed3c3-e125-4a9d-aa40-18ad999398d4", editFeedReplayRequest, editFeedReplayHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.EditFeedReplayHeaders editFeedReplayHeaders = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.EditFeedReplayHeaders();
            editFeedReplayHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalklive_1_0.Models.EditFeedReplayRequest editFeedReplayRequest = new AlibabaCloud.SDK.Dingtalklive_1_0.Models.EditFeedReplayRequest
            {
                UserId = "12061863",
                EditStartTime = 1617336058000,
                EditEndTime = 1617356058000,
            };
            try
            {
                client.EditFeedReplayWithOptions("8c0ed3c3-e125-4a9d-aa40-18ad999398d4", editFeedReplayRequest, editFeedReplayHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalklive_1_0::EditFeedReplayHeaders> editFeedReplayHeaders = make_shared<Alibabacloud_Dingtalklive_1_0::EditFeedReplayHeaders>();
  editFeedReplayHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalklive_1_0::EditFeedReplayRequest> editFeedReplayRequest = make_shared<Alibabacloud_Dingtalklive_1_0::EditFeedReplayRequest>(map<string, boost::any>({
    {"userId", boost::any(string("12061863"))},
    {"editStartTime", boost::any(1617336058000)},
    {"editEndTime", boost::any(1617356058000)}
  }));
  try {
    client->editFeedReplayWithOptions(make_shared<string>("8c0ed3c3-e125-4a9d-aa40-18ad999398d4"), editFeedReplayRequest, editFeedReplayHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "result" : "http://aliliving.alicdn.com/live_hpaxxxx"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | orgAccessForbidden | orgAccessForbidden | 组织访问受限 |
| 400 | paramsError | error:%s | 参数错误 |
| 400 | feedNotExist | feedNotExist | 课程不存在 |
| 400 | staffChangeError | staffChangeError | staffId转化失败 |
| 500 | systemError | systemError:%s | 系统错误 |
