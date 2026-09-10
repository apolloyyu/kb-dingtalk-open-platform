---
title: "数据集成转正记录同步"
source_url: "https://open.dingtalk.com/document/development/api-hrbrainimportregular"
namespace: "development"
slug: "api-hrbrainimportregular"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "组织大脑 > 数据集成 > 组织与人员 > 数据集成转正记录同步"
doc_id: "VGxQgFGh2f"
updated_at: "2026-06-02 19:25:02"
---

> Source: https://open.dingtalk.com/document/development/api-hrbrainimportregular
> Path: 应用开发 / 服务端 API / 组织大脑 > 数据集成 > 组织与人员 > 数据集成转正记录同步
> Updated: 2026-06-02 19:25:02

# 数据集成转正记录同步

调用本接口，人员转正记录同步至组织大脑，支持批量同步。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/regulars/import |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Hrbrain.Import.Write-组织大脑数据集成写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织编码。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 否 | 数据集。 |
| deptName | String | 否 | 转正时部门名称。 |
| deptNo | String | 否 | 转正时部门Id。 |
| extendInfo | Map | 否 | 额外信息，可不传。 |
| jobCodeName | String | 否 | 转正时职务。 |
| jobLevel | String | 否 | 转正时职级。 |
| name | String | 否 | 姓名。 |
| planRegularDate | String | 否 | 计划转正时间。 |
| postName | String | 否 | 转正时职位。 |
| regularDate | String | 是 | 实际转正日期。 |
| superEmpId | String | 否 | 转正时主管 UserId。 |
| superName | String | 否 | 转正时主管名称。 |
| workNo | String | 是 | 钉钉用户 UserId。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/regulars/import?corpId=ding3b*********88 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:480021443f9f37fcbf464c4a6b85d289
Content-Type:application/json

[ {
  "deptName" : "测试部",
  "deptNo" : "1234",
  "jobCodeName" : "研发",
  "jobLevel" : "P5",
  "name" : "张三",
  "planRegularDate" : "2024-02-02",
  "postName" : "经理",
  "regularDate" : "2024-02-03",
  "superEmpId" : "435654",
  "superName" : "李四",
  "workNo" : "23498734"
} ]
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
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportRegularHeaders hrbrainImportRegularHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportRegularHeaders();
        hrbrainImportRegularHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportRegularRequest.HrbrainImportRegularRequestBody body0 = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportRegularRequest.HrbrainImportRegularRequestBody()
                .setDeptName("测试部")
                .setDeptNo("1234")
                .setJobCodeName("研发")
                .setJobLevel("P5")
                .setName("张三")
                .setPlanRegularDate("2024-02-02")
                .setPostName("经理")
                .setRegularDate("2024-02-03")
                .setSuperEmpId("435654")
                .setSuperName("李四")
                .setWorkNo("23498734");
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportRegularRequest hrbrainImportRegularRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportRegularRequest()
                .setCorpId("ding3b*********88")
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.hrbrainImportRegularWithOptions(hrbrainImportRegularRequest, hrbrainImportRegularHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrbrain_1_0.client import Client as dingtalkhrbrain_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrbrain_1_0 import models as dingtalkhrbrain__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrbrain_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrbrain_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_regular_headers = dingtalkhrbrain__1__0_models.HrbrainImportRegularHeaders()
        hrbrain_import_regular_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportRegularRequestBody(
            dept_name='测试部',
            dept_no='1234',
            job_code_name='研发',
            job_level='P5',
            name='张三',
            plan_regular_date='2024-02-02',
            post_name='经理',
            regular_date='2024-02-03',
            super_emp_id='435654',
            super_name='李四',
            work_no='23498734'
        )
        hrbrain_import_regular_request = dingtalkhrbrain__1__0_models.HrbrainImportRegularRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            client.hrbrain_import_regular_with_options(hrbrain_import_regular_request, hrbrain_import_regular_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_regular_headers = dingtalkhrbrain__1__0_models.HrbrainImportRegularHeaders()
        hrbrain_import_regular_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportRegularRequestBody(
            dept_name='测试部',
            dept_no='1234',
            job_code_name='研发',
            job_level='P5',
            name='张三',
            plan_regular_date='2024-02-02',
            post_name='经理',
            regular_date='2024-02-03',
            super_emp_id='435654',
            super_name='李四',
            work_no='23498734'
        )
        hrbrain_import_regular_request = dingtalkhrbrain__1__0_models.HrbrainImportRegularRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            await client.hrbrain_import_regular_with_options_async(hrbrain_import_regular_request, hrbrain_import_regular_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportRegularHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportRegularRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportRegularRequest;
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
        $hrbrainImportRegularHeaders = new HrbrainImportRegularHeaders([]);
        $hrbrainImportRegularHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "deptName" => "测试部",
            "deptNo" => "1234",
            "jobCodeName" => "研发",
            "jobLevel" => "P5",
            "name" => "张三",
            "planRegularDate" => "2024-02-02",
            "postName" => "经理",
            "regularDate" => "2024-02-03",
            "superEmpId" => "435654",
            "superName" => "李四",
            "workNo" => "23498734"
        ]);
        $hrbrainImportRegularRequest = new HrbrainImportRegularRequest([
            "corpId" => "ding3b*********88",
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->hrbrainImportRegularWithOptions($hrbrainImportRegularRequest, $hrbrainImportRegularHeaders, new RuntimeOptions([]));
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
  dingtalkhrbrain_1_0  "github.com/alibabacloud-go/dingtalk/hrbrain_1_0"
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
func CreateClient () (_result *dingtalkhrbrain_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrbrain_1_0.Client{}
  _result, _err = dingtalkhrbrain_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrbrainImportRegularHeaders := &dingtalkhrbrain_1_0.HrbrainImportRegularHeaders{}
  hrbrainImportRegularHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkhrbrain_1_0.HrbrainImportRegularRequestBody{
    DeptName: tea.String("测试部"),
    DeptNo: tea.String("1234"),
    JobCodeName: tea.String("研发"),
    JobLevel: tea.String("P5"),
    Name: tea.String("张三"),
    PlanRegularDate: tea.String("2024-02-02"),
    PostName: tea.String("经理"),
    RegularDate: tea.String("2024-02-03"),
    SuperEmpId: tea.String("435654"),
    SuperName: tea.String("李四"),
    WorkNo: tea.String("23498734"),
  }
  hrbrainImportRegularRequest := &dingtalkhrbrain_1_0.HrbrainImportRegularRequest{
    CorpId: tea.String("ding3b*********88"),
    Body: []*dingtalkhrbrain_1_0.HrbrainImportRegularRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainImportRegularWithOptions(hrbrainImportRegularRequest, hrbrainImportRegularHeaders, &util.RuntimeOptions{})
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
const dingtalkhrbrain_1_0 = require('@alicloud/dingtalk/hrbrain_1_0');
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
    return new dingtalkhrbrain_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let hrbrainImportRegularHeaders = new dingtalkhrbrain_1_0.HrbrainImportRegularHeaders({ });
    hrbrainImportRegularHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let body0 = new dingtalkhrbrain_1_0.HrbrainImportRegularRequestBody({
      deptName: '测试部',
      deptNo: '1234',
      jobCodeName: '研发',
      jobLevel: 'P5',
      name: '张三',
      planRegularDate: '2024-02-02',
      postName: '经理',
      regularDate: '2024-02-03',
      superEmpId: '435654',
      superName: '李四',
      workNo: '23498734',
    });
    let hrbrainImportRegularRequest = new dingtalkhrbrain_1_0.HrbrainImportRegularRequest({
      corpId: 'ding3b*********88',
      body: [
        body0
      ],
    });
    try {
      await client.hrbrainImportRegularWithOptions(hrbrainImportRegularRequest, hrbrainImportRegularHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularHeaders hrbrainImportRegularHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularHeaders();
            hrbrainImportRegularHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularRequest.HrbrainImportRegularRequestBody body0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularRequest.HrbrainImportRegularRequestBody
            {
                DeptName = "测试部",
                DeptNo = "1234",
                JobCodeName = "研发",
                JobLevel = "P5",
                Name = "张三",
                PlanRegularDate = "2024-02-02",
                PostName = "经理",
                RegularDate = "2024-02-03",
                SuperEmpId = "435654",
                SuperName = "李四",
                WorkNo = "23498734",
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularRequest hrbrainImportRegularRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularRequest
            {
                CorpId = "ding3b*********88",
                Body = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportRegularRequest.HrbrainImportRegularRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.HrbrainImportRegularWithOptions(hrbrainImportRegularRequest, hrbrainImportRegularHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求 ID。 |
| result | Boolean | 更新是否成功。 |
| success | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "480021443f9f37fcbf464c4a6b85d289",
  "result" : true,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illegal. %s | 入参错误 |
