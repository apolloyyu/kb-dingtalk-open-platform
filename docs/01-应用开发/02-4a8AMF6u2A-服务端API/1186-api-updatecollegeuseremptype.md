---
title: "修改用户成员类型"
source_url: "https://open.dingtalk.com/document/development/api-updatecollegeuseremptype"
namespace: "development"
slug: "api-updatecollegeuseremptype"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 修改用户成员类型"
doc_id: "OnMrFTEELI"
updated_at: "2025-09-23 19:23:26"
---

> Source: https://open.dingtalk.com/document/development/api-updatecollegeuseremptype
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 修改用户成员类型
> Updated: 2025-09-23 19:23:26

# 修改用户成员类型

修改用户成员类型，将教职工转变成学生，或学生转变成教职工。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/empTypes/change |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Edu.College.Contact.Write-钉钉教育高校通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userid | String | 是 | 员工唯一标识ID（不可修改），企业内必须唯一。 |
| empType | String | 是 | 员工的成员类型：   - college\_teacher：教职工 - college\_student：学生 |

### 请求示例

HTTP

```
POST /v1.0/edu/collegeContact/empTypes/change HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:be3Fxxxx
Content-Type:application/json

{
  "userid" : "zhangsan666",
  "empType" : "college_student"
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
        com.aliyun.dingtalkedu_1_0.models.UpdateCollegeUserEmpTypeHeaders updateCollegeUserEmpTypeHeaders = new com.aliyun.dingtalkedu_1_0.models.UpdateCollegeUserEmpTypeHeaders();
        updateCollegeUserEmpTypeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.UpdateCollegeUserEmpTypeRequest updateCollegeUserEmpTypeRequest = new com.aliyun.dingtalkedu_1_0.models.UpdateCollegeUserEmpTypeRequest()
                .setUserid("zhangsan666")
                .setEmpType("college_student");
        try {
            client.updateCollegeUserEmpTypeWithOptions(updateCollegeUserEmpTypeRequest, updateCollegeUserEmpTypeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_college_user_emp_type_headers = dingtalkedu__1__0_models.UpdateCollegeUserEmpTypeHeaders()
        update_college_user_emp_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_college_user_emp_type_request = dingtalkedu__1__0_models.UpdateCollegeUserEmpTypeRequest(
            userid='zhangsan666',
            emp_type='college_student'
        )
        try:
            client.update_college_user_emp_type_with_options(update_college_user_emp_type_request, update_college_user_emp_type_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_college_user_emp_type_headers = dingtalkedu__1__0_models.UpdateCollegeUserEmpTypeHeaders()
        update_college_user_emp_type_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_college_user_emp_type_request = dingtalkedu__1__0_models.UpdateCollegeUserEmpTypeRequest(
            userid='zhangsan666',
            emp_type='college_student'
        )
        try:
            await client.update_college_user_emp_type_with_options_async(update_college_user_emp_type_request, update_college_user_emp_type_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateCollegeUserEmpTypeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateCollegeUserEmpTypeRequest;
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
        $updateCollegeUserEmpTypeHeaders = new UpdateCollegeUserEmpTypeHeaders([]);
        $updateCollegeUserEmpTypeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateCollegeUserEmpTypeRequest = new UpdateCollegeUserEmpTypeRequest([
            "userid" => "zhangsan666",
            "empType" => "college_student"
        ]);
        try {
            $client->updateCollegeUserEmpTypeWithOptions($updateCollegeUserEmpTypeRequest, $updateCollegeUserEmpTypeHeaders, new RuntimeOptions([]));
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

  updateCollegeUserEmpTypeHeaders := &dingtalkedu_1_0.UpdateCollegeUserEmpTypeHeaders{}
  updateCollegeUserEmpTypeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateCollegeUserEmpTypeRequest := &dingtalkedu_1_0.UpdateCollegeUserEmpTypeRequest{
    Userid: tea.String("zhangsan666"),
    EmpType: tea.String("college_student"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateCollegeUserEmpTypeWithOptions(updateCollegeUserEmpTypeRequest, updateCollegeUserEmpTypeHeaders, &util.RuntimeOptions{})
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
    let updateCollegeUserEmpTypeHeaders = new dingtalkedu_1_0.UpdateCollegeUserEmpTypeHeaders({ });
    updateCollegeUserEmpTypeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateCollegeUserEmpTypeRequest = new dingtalkedu_1_0.UpdateCollegeUserEmpTypeRequest({
      userid: 'zhangsan666',
      empType: 'college_student',
    });
    try {
      await client.updateCollegeUserEmpTypeWithOptions(updateCollegeUserEmpTypeRequest, updateCollegeUserEmpTypeHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeUserEmpTypeHeaders updateCollegeUserEmpTypeHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeUserEmpTypeHeaders();
            updateCollegeUserEmpTypeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeUserEmpTypeRequest updateCollegeUserEmpTypeRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeUserEmpTypeRequest
            {
                Userid = "zhangsan666",
                EmpType = "college_student",
            };
            try
            {
                client.UpdateCollegeUserEmpTypeWithOptions(updateCollegeUserEmpTypeRequest, updateCollegeUserEmpTypeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否成功。 |

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
| 400 | needAuth | NEED\_AUTH | 需要授权 |
| 400 | invalidIsvOrgId | INVALID\_ISV\_ORG\_ID | 无效的isv |
| 400 | invalidRequestParams | INVALID\_REQUEST\_PARAMS | 不合法的参数 |
| 400 | noPermission | NO\_PERMISSION | 没有权限 |
| 400 | systemError | SYSTEM\_ERROR | 系统异常 |
| 400 | userNotFound | USER\_NOT\_FOUND | 用户不存在 |
