---
title: "数据集成离职信息同步"
source_url: "https://open.dingtalk.com/document/development/api-hrbrainimportdimission"
namespace: "development"
slug: "api-hrbrainimportdimission"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "组织大脑 > 数据集成 > 组织与人员 > 数据集成离职信息同步"
doc_id: "k83PePPRoK"
updated_at: "2026-06-04 19:10:10"
---

> Source: https://open.dingtalk.com/document/development/api-hrbrainimportdimission
> Path: 应用开发 / 服务端 API / 组织大脑 > 数据集成 > 组织与人员 > 数据集成离职信息同步
> Updated: 2026-06-04 19:10:10

# 数据集成离职信息同步

调用本接口，离职信息同步至组织大脑，支持批量同步。

## 接口调用说明

为了确保你在使用接口时能够顺利进行数据交互，请务必检查对应数据模型是否设置枚举值的范围。这一操作需要在组织大脑[管理后台](https://hrbrain.dingtalk.com/hrbrain/management/data-integration/model-management/basic-modal/detail?modelCode=hrbrain_import_dimission&status=read&detailNav=%5B%22modelList%22%2C%22detail%22%5D)的数据集成 > 模型管理的对应数据模型中进行查看，如果未正确设置枚举值范围，调用接口时可能会遇到错误信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/dimissionInfos/import |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrbrain.Import.Write-组织大脑数据集成写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织编码。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 是 | 数据集。 |
| name | String | 是 | 姓名。 |
| workNo | String | 是 | 钉钉用户 UserId。 |
| empType | String | 是 | 员工类型。 |
| dimissionDate | String | 是 | 离职日期。 |
| deptNo | String | 是 | 离职时部门编码。 |
| deptName | String | 是 | 离职时部门。 |
| jobLevel | String | 否 | 离职时职级。 |
| workLocAddr | String | 否 | 工作地。 |
| superName | String | 是 | 离职时主管。 |
| dimissionReason | String | 是 | 离职原因分类。 |
| dimissionReaasonDesc | String | 是 | 离职原因说明。 |
| jobCodeName | String | 否 | 离职职务。 |
| postName | String | 否 | 离职职位。 |
| extendInfo | Map | 否 | 扩展字段，KV结构。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/dimissionInfos/import?corpId=ding3b*********88 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:480021443f9f37fcbf464c4a6b85d299
Content-Type:application/json

[ {
  "name" : "张三",
  "workNo" : "14530201131175645",
  "empType" : "正式全职",
  "dimissionDate" : "2023-01-01",
  "deptNo" : "10010",
  "deptName" : "组织发展&变革",
  "jobLevel" : "P8",
  "workLocAddr" : "杭州余杭",
  "superName" : "李四",
  "dimissionReason" : "个人原因",
  "dimissionReaasonDesc" : "个人发展",
  "jobCodeName" : "产品",
  "postName" : "产品设计"
} ]
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
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportDimissionHeaders hrbrainImportDimissionHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportDimissionHeaders();
        hrbrainImportDimissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportDimissionRequest.HrbrainImportDimissionRequestBody body0 = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportDimissionRequest.HrbrainImportDimissionRequestBody()
                .setName("张三")
                .setWorkNo("14530201131175645")
                .setEmpType("正式全职")
                .setDimissionDate("2023-01-01")
                .setDeptNo("10010")
                .setDeptName("组织发展&变革")
                .setJobLevel("P8")
                .setWorkLocAddr("杭州余杭")
                .setSuperName("李四")
                .setDimissionReason("个人原因")
                .setDimissionReaasonDesc("个人发展")
                .setJobCodeName("产品")
                .setPostName("产品设计");
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportDimissionRequest hrbrainImportDimissionRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportDimissionRequest()
                .setCorpId("ding3b*********88")
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.hrbrainImportDimissionWithOptions(hrbrainImportDimissionRequest, hrbrainImportDimissionHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        hrbrain_import_dimission_headers = dingtalkhrbrain__1__0_models.HrbrainImportDimissionHeaders()
        hrbrain_import_dimission_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportDimissionRequestBody(
            name='张三',
            work_no='14530201131175645',
            emp_type='正式全职',
            dimission_date='2023-01-01',
            dept_no='10010',
            dept_name='组织发展&变革',
            job_level='P8',
            work_loc_addr='杭州余杭',
            super_name='李四',
            dimission_reason='个人原因',
            dimission_reaason_desc='个人发展',
            job_code_name='产品',
            post_name='产品设计'
        )
        hrbrain_import_dimission_request = dingtalkhrbrain__1__0_models.HrbrainImportDimissionRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            client.hrbrain_import_dimission_with_options(hrbrain_import_dimission_request, hrbrain_import_dimission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_dimission_headers = dingtalkhrbrain__1__0_models.HrbrainImportDimissionHeaders()
        hrbrain_import_dimission_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportDimissionRequestBody(
            name='张三',
            work_no='14530201131175645',
            emp_type='正式全职',
            dimission_date='2023-01-01',
            dept_no='10010',
            dept_name='组织发展&变革',
            job_level='P8',
            work_loc_addr='杭州余杭',
            super_name='李四',
            dimission_reason='个人原因',
            dimission_reaason_desc='个人发展',
            job_code_name='产品',
            post_name='产品设计'
        )
        hrbrain_import_dimission_request = dingtalkhrbrain__1__0_models.HrbrainImportDimissionRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            await client.hrbrain_import_dimission_with_options_async(hrbrain_import_dimission_request, hrbrain_import_dimission_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportDimissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportDimissionRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportDimissionRequest;
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
        $hrbrainImportDimissionHeaders = new HrbrainImportDimissionHeaders([]);
        $hrbrainImportDimissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "name" => "张三",
            "workNo" => "14530201131175645",
            "empType" => "正式全职",
            "dimissionDate" => "2023-01-01",
            "deptNo" => "10010",
            "deptName" => "组织发展&变革",
            "jobLevel" => "P8",
            "workLocAddr" => "杭州余杭",
            "superName" => "李四",
            "dimissionReason" => "个人原因",
            "dimissionReaasonDesc" => "个人发展",
            "jobCodeName" => "产品",
            "postName" => "产品设计"
        ]);
        $hrbrainImportDimissionRequest = new HrbrainImportDimissionRequest([
            "corpId" => "ding3b*********88",
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->hrbrainImportDimissionWithOptions($hrbrainImportDimissionRequest, $hrbrainImportDimissionHeaders, new RuntimeOptions([]));
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

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  hrbrainImportDimissionHeaders := &dingtalkhrbrain_1_0.HrbrainImportDimissionHeaders{}
  hrbrainImportDimissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkhrbrain_1_0.HrbrainImportDimissionRequestBody{
    Name: tea.String("张三"),
    WorkNo: tea.String("14530201131175645"),
    EmpType: tea.String("正式全职"),
    DimissionDate: tea.String("2023-01-01"),
    DeptNo: tea.String("10010"),
    DeptName: tea.String("组织发展&变革"),
    JobLevel: tea.String("P8"),
    WorkLocAddr: tea.String("杭州余杭"),
    SuperName: tea.String("李四"),
    DimissionReason: tea.String("个人原因"),
    DimissionReaasonDesc: tea.String("个人发展"),
    JobCodeName: tea.String("产品"),
    PostName: tea.String("产品设计"),
  }
  hrbrainImportDimissionRequest := &dingtalkhrbrain_1_0.HrbrainImportDimissionRequest{
    CorpId: tea.String("ding3b*********88"),
    Body: []*dingtalkhrbrain_1_0.HrbrainImportDimissionRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainImportDimissionWithOptions(hrbrainImportDimissionRequest, hrbrainImportDimissionHeaders, &util.RuntimeOptions{})
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
    let hrbrainImportDimissionHeaders = new dingtalkhrbrain_1_0.HrbrainImportDimissionHeaders({ });
    hrbrainImportDimissionHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let body0 = new dingtalkhrbrain_1_0.HrbrainImportDimissionRequestBody({
      name: '张三',
      workNo: '14530201131175645',
      empType: '正式全职',
      dimissionDate: '2023-01-01',
      deptNo: '10010',
      deptName: '组织发展&变革',
      jobLevel: 'P8',
      workLocAddr: '杭州余杭',
      superName: '李四',
      dimissionReason: '个人原因',
      dimissionReaasonDesc: '个人发展',
      jobCodeName: '产品',
      postName: '产品设计',
    });
    let hrbrainImportDimissionRequest = new dingtalkhrbrain_1_0.HrbrainImportDimissionRequest({
      corpId: 'ding3b*********88',
      body: [
        body0
      ],
    });
    try {
      await client.hrbrainImportDimissionWithOptions(hrbrainImportDimissionRequest, hrbrainImportDimissionHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
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
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionHeaders hrbrainImportDimissionHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionHeaders();
            hrbrainImportDimissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionRequest.HrbrainImportDimissionRequestBody body0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionRequest.HrbrainImportDimissionRequestBody
            {
                Name = "张三",
                WorkNo = "14530201131175645",
                EmpType = "正式全职",
                DimissionDate = "2023-01-01",
                DeptNo = "10010",
                DeptName = "组织发展&变革",
                JobLevel = "P8",
                WorkLocAddr = "杭州余杭",
                SuperName = "李四",
                DimissionReason = "个人原因",
                DimissionReaasonDesc = "个人发展",
                JobCodeName = "产品",
                PostName = "产品设计",
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionRequest hrbrainImportDimissionRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionRequest
            {
                CorpId = "ding3b*********88",
                Body = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportDimissionRequest.HrbrainImportDimissionRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.HrbrainImportDimissionWithOptions(hrbrainImportDimissionRequest, hrbrainImportDimissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新是否成功：   - true：成功 - false：失败 |
| success | Boolean | 接口调用是否成功：   - true：成功 - false：失败 |
| requestId | String | 请求 ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : false,
  "success" : true,
  "requestId" : "480021443f9f37fcbf464c4a6b85d289"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illegal. %s | 入参错误 |
