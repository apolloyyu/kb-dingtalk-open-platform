---
title: "学生调班"
source_url: "https://open.dingtalk.com/document/development/shift-students"
namespace: "development"
slug: "shift-students"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 学生调班"
doc_id: "E8iTXAgn6A"
updated_at: "2026-06-04 19:11:25"
---

> Source: https://open.dingtalk.com/document/development/shift-students
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 学生调班
> Updated: 2026-06-04 19:11:25

# 学生调班

调用本接口进行学生调班，如果该学生家长在本班只有当前一个学生，那么家长也会随着学生调班。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/students/move |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-钉钉教育家校通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operator | String | 是 | 操作者的userId，可调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取userid参数值。 |
| userId | String | 是 | 学生的userId，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取userid参数值。 |
| originClassId | Long | 是 | 原班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| targetClassId | Long | 是 | 目标班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |

### 请求示例

HTTP

```
POST /v1.0/edu/students/move HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxx
Content-Type:application/json

{
  "operator" : "1234",
  "userId" : "1000",
  "originClassId" : 2000,
  "targetClassId" : 2001
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkedu_1_0.*;
import com.aliyun.dingtalkedu_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkedu_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkedu_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkedu_1_0.Client client = Sample.createClient();
        MoveStudentHeaders moveStudentHeaders = new MoveStudentHeaders();
        moveStudentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        MoveStudentRequest moveStudentRequest = new MoveStudentRequest()
                .setOperator("1234")
                .setUserId("1000")
                .setOriginClassId(2000L)
                .setTargetClassId(2001L);
        try {
            client.moveStudentWithOptions(moveStudentRequest, moveStudentHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.edu_1_0.client import Client as dingtalkedu_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.edu_1_0 import models as dingtalkedu__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkedu_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkedu_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        move_student_headers = dingtalkedu__1__0_models.MoveStudentHeaders()
        move_student_headers.x_acs_dingtalk_access_token = '<your access token>'
        move_student_request = dingtalkedu__1__0_models.MoveStudentRequest(
            operator='1234',
            user_id='1000',
            origin_class_id=2000,
            target_class_id=2001
        )
        try:
            client.move_student_with_options(move_student_request, move_student_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        move_student_headers = dingtalkedu__1__0_models.MoveStudentHeaders()
        move_student_headers.x_acs_dingtalk_access_token = '<your access token>'
        move_student_request = dingtalkedu__1__0_models.MoveStudentRequest(
            operator='1234',
            user_id='1000',
            origin_class_id=2000,
            target_class_id=2001
        )
        try:
            await client.move_student_with_options_async(move_student_request, move_student_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\MoveStudentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\MoveStudentRequest;
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
        $moveStudentHeaders = new MoveStudentHeaders([]);
        $moveStudentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $moveStudentRequest = new MoveStudentRequest([
            "operator" => "1234",
            "userId" => "1000",
            "originClassId" => 2000,
            "targetClassId" => 2001
        ]);
        try {
            $client->moveStudentWithOptions($moveStudentRequest, $moveStudentHeaders, new RuntimeOptions([]));
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
  dingtalkedu_1_0  "github.com/alibabacloud-go/dingtalk/edu_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkedu_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkedu_1_0.Client{}
  _result, _err = dingtalkedu_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  moveStudentHeaders := &dingtalkedu_1_0.MoveStudentHeaders{}
  moveStudentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  moveStudentRequest := &dingtalkedu_1_0.MoveStudentRequest{
    Operator: tea.String("1234"),
    UserId: tea.String("1000"),
    OriginClassId: tea.Int64(2000),
    TargetClassId: tea.Int64(2001),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.MoveStudentWithOptions(moveStudentRequest, moveStudentHeaders, &util.RuntimeOptions{})
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
import dingtalkedu_1_0, * as $dingtalkedu_1_0 from '@alicloud/dingtalk/edu_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkedu_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkedu_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let moveStudentHeaders = new $dingtalkedu_1_0.MoveStudentHeaders({ });
    moveStudentHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let moveStudentRequest = new $dingtalkedu_1_0.MoveStudentRequest({
      operator: "1234",
      userId: "1000",
      originClassId: 2000,
      targetClassId: 2001,
    });
    try {
      await client.moveStudentWithOptions(moveStudentRequest, moveStudentHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkedu_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkedu_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkedu_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.MoveStudentHeaders moveStudentHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.MoveStudentHeaders();
            moveStudentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.MoveStudentRequest moveStudentRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.MoveStudentRequest
            {
                Operator = "1234",
                UserId = "1000",
                OriginClassId = 2000,
                TargetClassId = 2001,
            };
            try
            {
                client.MoveStudentWithOptions(moveStudentRequest, moveStudentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkedu__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkedu_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkedu_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkedu_1_0::Client> client = make_shared<Alibabacloud_Dingtalkedu_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkedu_1_0::MoveStudentHeaders> moveStudentHeaders = make_shared<Alibabacloud_Dingtalkedu_1_0::MoveStudentHeaders>();
  moveStudentHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkedu_1_0::MoveStudentRequest> moveStudentRequest = make_shared<Alibabacloud_Dingtalkedu_1_0::MoveStudentRequest>(map<string, boost::any>({
    {"operator", boost::any(string("1234"))},
    {"userId", boost::any(string("1000"))},
    {"originClassId", boost::any(2000)},
    {"targetClassId", boost::any(2001)}
  }));
  try {
    client->moveStudentWithOptions(moveStudentRequest, moveStudentHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| success | Boolean | 调班是否成功，true表示调班成功。 |

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
| 400 | noRight | NO RIGHT | 当前用户没有操作权限 |
| 400 | illegalOrg | ILLEGAL ORG | 未被组织授权 |
| 400 | invalidParameter | PARAMETER INVALID | 参数非法 |
| 500 | systemBusy | SYSTEM BUSY | 系统繁忙 |
