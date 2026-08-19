---
title: "获取行政组织架构部门详情"
source_url: "https://open.dingtalk.com/document/development/api-getcollegecontactstandardstrudeptdetail"
namespace: "development"
slug: "api-getcollegecontactstandardstrudeptdetail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 获取行政组织架构部门详情"
doc_id: "MVdet4sX0C"
updated_at: "2025-09-23 19:23:30"
---

> Source: https://open.dingtalk.com/document/development/api-getcollegecontactstandardstrudeptdetail
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 获取行政组织架构部门详情
> Updated: 2025-09-23 19:23:30

# 获取行政组织架构部门详情

调用本接口，获取行政组织架构信息。

## 接口调用说明

行政组织架构及其下属的学生，教职工部门，是高校通讯录中的固定部门，请勿删除。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/depts/structures/standards |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Edu.College.Contact.Read-钉钉教育高校通讯录读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| language | String | 否 | 通讯录语言，默认zh\_CN。 |

### 请求示例

HTTP

```
GET /v1.0/edu/collegeContact/depts/structures/standards?language=zh_CN HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bE74xxxx
Content-Type:application/json
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
        com.aliyun.dingtalkedu_1_0.models.GetCollegeContactStandardStruDeptDetailHeaders getCollegeContactStandardStruDeptDetailHeaders = new com.aliyun.dingtalkedu_1_0.models.GetCollegeContactStandardStruDeptDetailHeaders();
        getCollegeContactStandardStruDeptDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.GetCollegeContactStandardStruDeptDetailRequest getCollegeContactStandardStruDeptDetailRequest = new com.aliyun.dingtalkedu_1_0.models.GetCollegeContactStandardStruDeptDetailRequest()
                .setLanguage("zh_CN");
        try {
            client.getCollegeContactStandardStruDeptDetailWithOptions(getCollegeContactStandardStruDeptDetailRequest, getCollegeContactStandardStruDeptDetailHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_college_contact_standard_stru_dept_detail_headers = dingtalkedu__1__0_models.GetCollegeContactStandardStruDeptDetailHeaders()
        get_college_contact_standard_stru_dept_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_college_contact_standard_stru_dept_detail_request = dingtalkedu__1__0_models.GetCollegeContactStandardStruDeptDetailRequest(
            language='zh_CN'
        )
        try:
            client.get_college_contact_standard_stru_dept_detail_with_options(get_college_contact_standard_stru_dept_detail_request, get_college_contact_standard_stru_dept_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_college_contact_standard_stru_dept_detail_headers = dingtalkedu__1__0_models.GetCollegeContactStandardStruDeptDetailHeaders()
        get_college_contact_standard_stru_dept_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_college_contact_standard_stru_dept_detail_request = dingtalkedu__1__0_models.GetCollegeContactStandardStruDeptDetailRequest(
            language='zh_CN'
        )
        try:
            await client.get_college_contact_standard_stru_dept_detail_with_options_async(get_college_contact_standard_stru_dept_detail_request, get_college_contact_standard_stru_dept_detail_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\GetCollegeContactStandardStruDeptDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\GetCollegeContactStandardStruDeptDetailRequest;
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
        $getCollegeContactStandardStruDeptDetailHeaders = new GetCollegeContactStandardStruDeptDetailHeaders([]);
        $getCollegeContactStandardStruDeptDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getCollegeContactStandardStruDeptDetailRequest = new GetCollegeContactStandardStruDeptDetailRequest([
            "language" => "zh_CN"
        ]);
        try {
            $client->getCollegeContactStandardStruDeptDetailWithOptions($getCollegeContactStandardStruDeptDetailRequest, $getCollegeContactStandardStruDeptDetailHeaders, new RuntimeOptions([]));
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

  getCollegeContactStandardStruDeptDetailHeaders := &dingtalkedu_1_0.GetCollegeContactStandardStruDeptDetailHeaders{}
  getCollegeContactStandardStruDeptDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getCollegeContactStandardStruDeptDetailRequest := &dingtalkedu_1_0.GetCollegeContactStandardStruDeptDetailRequest{
    Language: tea.String("zh_CN"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetCollegeContactStandardStruDeptDetailWithOptions(getCollegeContactStandardStruDeptDetailRequest, getCollegeContactStandardStruDeptDetailHeaders, &util.RuntimeOptions{})
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
    let getCollegeContactStandardStruDeptDetailHeaders = new dingtalkedu_1_0.GetCollegeContactStandardStruDeptDetailHeaders({ });
    getCollegeContactStandardStruDeptDetailHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getCollegeContactStandardStruDeptDetailRequest = new dingtalkedu_1_0.GetCollegeContactStandardStruDeptDetailRequest({
      language: 'zh_CN',
    });
    try {
      await client.getCollegeContactStandardStruDeptDetailWithOptions(getCollegeContactStandardStruDeptDetailRequest, getCollegeContactStandardStruDeptDetailHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactStandardStruDeptDetailHeaders getCollegeContactStandardStruDeptDetailHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactStandardStruDeptDetailHeaders();
            getCollegeContactStandardStruDeptDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactStandardStruDeptDetailRequest getCollegeContactStandardStruDeptDetailRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactStandardStruDeptDetailRequest
            {
                Language = "zh_CN",
            };
            try
            {
                client.GetCollegeContactStandardStruDeptDetailWithOptions(getCollegeContactStandardStruDeptDetailRequest, getCollegeContactStandardStruDeptDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| struId | Long | 行政组织架构部门ID。 |
| teacherDeptId | Long | 教职工节点组织单元ID。 |
| studentDeptId | Long | 学生节点组织单元ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "struId" : 456,
    "teacherDeptId" : 678,
    "studentDeptId" : 890
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameterInvalid | PARAMETER\_INVALID | 参数错误，请先完成高校通讯录转换 |
| 400 | systemError | SYSTEM\_ERROR | 系统异常，请重试 |
| 400 | standardStruNotExist | STANDARD\_STRU\_NOT\_EXIST | 行政组织架构不存在 |
