---
title: "更新班级"
source_url: "https://open.dingtalk.com/document/development/api-updateclass"
namespace: "development"
slug: "api-updateclass"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 更新班级"
doc_id: "2c61mMGD6A"
updated_at: "2025-09-23 19:23:15"
---

> Source: https://open.dingtalk.com/document/development/api-updateclass
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 更新班级
> Updated: 2025-09-23 19:23:15

# 更新班级

调用本接口，可在指定的班级下更新班级信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/classes/infos |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-钉钉教育家校通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| deptId | Long | 是 | 班级ID。 |
| gradeLevel | Integer | 是 | 年级Level。 |
| operator | String | 是 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |
| openClass | Object | 是 | 班级信息。 |
| nick | String | 是 | 班级昵称。 |
| onlyUseNick | String | 是 | 是否只展现nick。 |
| classLevel | Integer | 是 | 每个年级下班级级数，1班为1，2班为2。 |
| superId | Long | 是 | 年级ID。 |

### 请求示例

HTTP

```
PUT /v1.0/edu/classes/infos HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "deptId" : 23424324324,
  "gradeLevel" : 1,
  "operator" : "manager234234",
  "openClass" : {
    "nick" : "熊猫班",
    "onlyUseNick" : "true",
    "classLevel" : 1
  },
  "superId" : 23423423
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkedu_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkedu_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkedu_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkedu_1_0.models.UpdateClassHeaders updateClassHeaders = new com.aliyun.dingtalkedu_1_0.models.UpdateClassHeaders();
        updateClassHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.UpdateClassRequest.UpdateClassRequestOpenClass openClass = new com.aliyun.dingtalkedu_1_0.models.UpdateClassRequest.UpdateClassRequestOpenClass()
                .setNick("熊猫班")
                .setOnlyUseNick("true")
                .setClassLevel(1);
        com.aliyun.dingtalkedu_1_0.models.UpdateClassRequest updateClassRequest = new com.aliyun.dingtalkedu_1_0.models.UpdateClassRequest()
                .setDeptId(23424324324L)
                .setGradeLevel(1)
                .setOperator("manager234234")
                .setOpenClass(openClass)
                .setSuperId(23423423L);
        try {
            client.updateClassWithOptions(updateClassRequest, updateClassHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
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
        update_class_headers = dingtalkedu__1__0_models.UpdateClassHeaders()
        update_class_headers.x_acs_dingtalk_access_token = '<your access token>'
        open_class = dingtalkedu__1__0_models.UpdateClassRequestOpenClass(
            nick='熊猫班',
            only_use_nick='true',
            class_level=1
        )
        update_class_request = dingtalkedu__1__0_models.UpdateClassRequest(
            dept_id=23424324324,
            grade_level=1,
            operator='manager234234',
            open_class=open_class,
            super_id=23423423
        )
        try:
            client.update_class_with_options(update_class_request, update_class_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_class_headers = dingtalkedu__1__0_models.UpdateClassHeaders()
        update_class_headers.x_acs_dingtalk_access_token = '<your access token>'
        open_class = dingtalkedu__1__0_models.UpdateClassRequestOpenClass(
            nick='熊猫班',
            only_use_nick='true',
            class_level=1
        )
        update_class_request = dingtalkedu__1__0_models.UpdateClassRequest(
            dept_id=23424324324,
            grade_level=1,
            operator='manager234234',
            open_class=open_class,
            super_id=23423423
        )
        try:
            await client.update_class_with_options_async(update_class_request, update_class_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateClassHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateClassRequest\openClass;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateClassRequest;
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
        $updateClassHeaders = new UpdateClassHeaders([]);
        $updateClassHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $openClass = new openClass([
            "nick" => "熊猫班",
            "onlyUseNick" => "true",
            "classLevel" => 1
        ]);
        $updateClassRequest = new UpdateClassRequest([
            "deptId" => 23424324324,
            "gradeLevel" => 1,
            "operator" => "manager234234",
            "openClass" => $openClass,
            "superId" => 23423423
        ]);
        try {
            $client->updateClassWithOptions($updateClassRequest, $updateClassHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkedu_1_0  "github.com/alibabacloud-go/dingtalk/edu_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
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

  updateClassHeaders := &dingtalkedu_1_0.UpdateClassHeaders{}
  updateClassHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  openClass := &dingtalkedu_1_0.UpdateClassRequestOpenClass{
    Nick: tea.String("熊猫班"),
    OnlyUseNick: tea.String("true"),
    ClassLevel: tea.Int32(1),
  }
  updateClassRequest := &dingtalkedu_1_0.UpdateClassRequest{
    DeptId: tea.Int64(23424324324),
    GradeLevel: tea.Int32(1),
    Operator: tea.String("manager234234"),
    OpenClass: openClass,
    SuperId: tea.Int64(23423423),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateClassWithOptions(updateClassRequest, updateClassHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkedu_1_0 = require('@alicloud/dingtalk/edu_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkedu_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateClassHeaders = new dingtalkedu_1_0.UpdateClassHeaders({ });
    updateClassHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let openClass = new dingtalkedu_1_0.UpdateClassRequestOpenClass({
      nick: '熊猫班',
      onlyUseNick: 'true',
      classLevel: 1,
    });
    let updateClassRequest = new dingtalkedu_1_0.UpdateClassRequest({
      deptId: 23424324324,
      gradeLevel: 1,
      operator: 'manager234234',
      openClass: openClass,
      superId: 23423423,
    });
    try {
      await client.updateClassWithOptions(updateClassRequest, updateClassHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateClassHeaders updateClassHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateClassHeaders();
            updateClassHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateClassRequest.UpdateClassRequestOpenClass openClass = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateClassRequest.UpdateClassRequestOpenClass
            {
                Nick = "熊猫班",
                OnlyUseNick = "true",
                ClassLevel = 1,
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateClassRequest updateClassRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateClassRequest
            {
                DeptId = 23424324324,
                GradeLevel = 1,
                Operator = "manager234234",
                OpenClass = openClass,
                SuperId = 23423423,
            };
            try
            {
                client.UpdateClassWithOptions(updateClassRequest, updateClassHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |
| result | Object | 调用结果。 |
| deptId | Long | 班级ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "deptId" : 234324
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameterInvalid | PARAMETER\_INVALID | 参数错误，请先完成家校通讯录转换 |
| 400 | systemError | SYSTEM\_ERROR | 系统错误 |
| 400 | concurrentError | CONCURRENT\_ERROR | 并发错误 |
| 400 | illegalOrg | ILLEGAL\_ORG | 违法组织，不能使用 |
| 400 | noRight | NO\_RIGHT | 没有权限 |
