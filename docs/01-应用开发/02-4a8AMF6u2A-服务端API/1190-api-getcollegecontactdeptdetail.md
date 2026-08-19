---
title: "获取组织单元详情"
source_url: "https://open.dingtalk.com/document/development/api-getcollegecontactdeptdetail"
namespace: "development"
slug: "api-getcollegecontactdeptdetail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 获取组织单元详情"
doc_id: "fhIjVnofI3"
updated_at: "2025-09-23 19:23:29"
---

> Source: https://open.dingtalk.com/document/development/api-getcollegecontactdeptdetail
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 获取组织单元详情
> Updated: 2025-09-23 19:23:29

# 获取组织单元详情

调用本接口，根据组织单元ID获取指定组织单元（即部门）详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/depts |
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
| deptId | Long | 是 | 组织单元ID，根组织单元ID为1。 |
| language | String | 否 | 通讯录语言（默认zh\_CN）。 |

### 请求示例

HTTP

```
GET /v1.0/edu/collegeContact/depts?deptId=20&language=zh_CN HTTP/1.1
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
        com.aliyun.dingtalkedu_1_0.models.GetCollegeContactDeptDetailHeaders getCollegeContactDeptDetailHeaders = new com.aliyun.dingtalkedu_1_0.models.GetCollegeContactDeptDetailHeaders();
        getCollegeContactDeptDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.GetCollegeContactDeptDetailRequest getCollegeContactDeptDetailRequest = new com.aliyun.dingtalkedu_1_0.models.GetCollegeContactDeptDetailRequest()
                .setDeptId(20L)
                .setLanguage("zh_CN");
        try {
            client.getCollegeContactDeptDetailWithOptions(getCollegeContactDeptDetailRequest, getCollegeContactDeptDetailHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_college_contact_dept_detail_headers = dingtalkedu__1__0_models.GetCollegeContactDeptDetailHeaders()
        get_college_contact_dept_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_college_contact_dept_detail_request = dingtalkedu__1__0_models.GetCollegeContactDeptDetailRequest(
            dept_id=20,
            language='zh_CN'
        )
        try:
            client.get_college_contact_dept_detail_with_options(get_college_contact_dept_detail_request, get_college_contact_dept_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_college_contact_dept_detail_headers = dingtalkedu__1__0_models.GetCollegeContactDeptDetailHeaders()
        get_college_contact_dept_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_college_contact_dept_detail_request = dingtalkedu__1__0_models.GetCollegeContactDeptDetailRequest(
            dept_id=20,
            language='zh_CN'
        )
        try:
            await client.get_college_contact_dept_detail_with_options_async(get_college_contact_dept_detail_request, get_college_contact_dept_detail_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\GetCollegeContactDeptDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\GetCollegeContactDeptDetailRequest;
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
        $getCollegeContactDeptDetailHeaders = new GetCollegeContactDeptDetailHeaders([]);
        $getCollegeContactDeptDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getCollegeContactDeptDetailRequest = new GetCollegeContactDeptDetailRequest([
            "deptId" => 20,
            "language" => "zh_CN"
        ]);
        try {
            $client->getCollegeContactDeptDetailWithOptions($getCollegeContactDeptDetailRequest, $getCollegeContactDeptDetailHeaders, new RuntimeOptions([]));
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

  getCollegeContactDeptDetailHeaders := &dingtalkedu_1_0.GetCollegeContactDeptDetailHeaders{}
  getCollegeContactDeptDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getCollegeContactDeptDetailRequest := &dingtalkedu_1_0.GetCollegeContactDeptDetailRequest{
    DeptId: tea.Int64(20),
    Language: tea.String("zh_CN"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetCollegeContactDeptDetailWithOptions(getCollegeContactDeptDetailRequest, getCollegeContactDeptDetailHeaders, &util.RuntimeOptions{})
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
    let getCollegeContactDeptDetailHeaders = new dingtalkedu_1_0.GetCollegeContactDeptDetailHeaders({ });
    getCollegeContactDeptDetailHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getCollegeContactDeptDetailRequest = new dingtalkedu_1_0.GetCollegeContactDeptDetailRequest({
      deptId: 20,
      language: 'zh_CN',
    });
    try {
      await client.getCollegeContactDeptDetailWithOptions(getCollegeContactDeptDetailRequest, getCollegeContactDeptDetailHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactDeptDetailHeaders getCollegeContactDeptDetailHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactDeptDetailHeaders();
            getCollegeContactDeptDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactDeptDetailRequest getCollegeContactDeptDetailRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.GetCollegeContactDeptDetailRequest
            {
                DeptId = 20,
                Language = "zh_CN",
            };
            try
            {
                client.GetCollegeContactDeptDetailWithOptions(getCollegeContactDeptDetailRequest, getCollegeContactDeptDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| deptId | Long | 组织单元ID。 |
| name | String | 组织单元名称。 |
| struId | Long | 高校架构ID。 |
| parentId | Long | 父组织单元ID。 |
| sourceIdentifier | String | 基础通讯录部门标识。 |
| deptType | String | 高校组织单元类型。 |
| deptCode | String | 高校组织单元编码，由开发者确定，高校组织内唯一标识的组织单元编码。 |
| createDeptGroup | Boolean | 是否同步创建一个关联此组织单元的企业群, true表示是, false表示不是。 |
| autoAddUser | Boolean | 当群已经创建后，是否有新人加入组织单元会自动加入该群。 |
| tags | String | 家校通讯录部门类型，包括campus,period,grade,class；如果不是家校通讯录则忽略。 |
| fromUnionOrg | Boolean | 组织单元是否来自关联组织。 |
| extension | String | 扩展字段。 |
| order | Long | 在父组织单元中的次序值。 |
| deptGroupChatId | String | 组织单元群ID。 |
| groupContainSubDept | Boolean | 组织单元群是否包含子组织单元。 |
| orgDeptOwner | String | 组织单元群群主userID。 |
| deptManagerUseridList | Array of String | 用户userID。 |
| outerDept | Boolean | 是否本组织单元的员工仅可见员工自己, 为true时，本组织单元员工默认只能看到员工自己。 |
| outerPermitDepts | Array of Long | 组织单元ID。 |
| outerPermitUsers | Array of String | 用户userID。 |
| userPermits | Array of String | 用户userID。 |
| hideDept | Boolean | 是否隐藏组织单元, true表示隐藏, false表示显示。 |
| deptPermits | Array of Long | 组织单元ID。 |
| brief | String | 组织单元简介。 |
| telephone | String | 联系方式（手机号码或座机号码）。 |
| code | String | 基础通讯录的部门编码。 |
| autoApproveApply | Boolean | 开启后，加入该组织单元的申请将默认同意。 |
| empApplyJoinDept | Boolean | 开启后，允许员工加入组织单元。 |
| hideSceneConfig | Object | 组织单元隐藏的生效场景配置。 |
| chatboxSubtitle | Boolean | 是否在单聊框生效。 |
| nodeList | Boolean | 是否在查看组织架构生效。 |
| search | Boolean | 是否在搜索生效。 |
| profile | Boolean | 是否在个人资料页生效。 |
| active | Boolean | 当前组织单元是否采用单独的配置。如果设置了false，则采用组织维度的配置。 |
| outerSceneConfig | Object | 组织单元限制可见的生效场景配置。 |
| chatboxSubtitle | Boolean | 是否在单聊框生效。 |
| nodeList | Boolean | 是否在查看组织架构生效。 |
| search | Boolean | 是否在搜索生效。 |
| profile | Boolean | 是否在个人资料页生效。 |
| active | Boolean | 当前组织单元是否采用单独的配置。如果设置了false，则采用组织维度的配置。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "deptId" : 200,
    "name" : "软件工程",
    "struId" : 200,
    "parentId" : 200,
    "sourceIdentifier" : "软件工程标识",
    "deptType" : "contact_class_dept",
    "deptCode" : "dept456",
    "createDeptGroup" : true,
    "autoAddUser" : true,
    "tags" : "campus",
    "fromUnionOrg" : false,
    "extension" : "{}",
    "order" : 200,
    "deptGroupChatId" : "chat234",
    "groupContainSubDept" : false,
    "orgDeptOwner" : "user345",
    "deptManagerUseridList" : [ "user456" ],
    "outerDept" : false,
    "outerPermitDepts" : [ 456 ],
    "outerPermitUsers" : [ "user456" ],
    "userPermits" : [ "user456" ],
    "hideDept" : false,
    "deptPermits" : [ 456 ],
    "brief" : "这是简介",
    "telephone" : "138xxxx0000",
    "code" : "10000",
    "autoApproveApply" : false,
    "empApplyJoinDept" : false,
    "hideSceneConfig" : {
      "chatboxSubtitle" : false,
      "nodeList" : false,
      "search" : false,
      "profile" : false,
      "active" : false
    },
    "outerSceneConfig" : {
      "chatboxSubtitle" : false,
      "nodeList" : false,
      "search" : false,
      "profile" : false,
      "active" : false
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameterInvalid | PARAMETER\_INVALID | 参数错误，请先完成高校通讯录转换 |
| 400 | invalidDepartmantId | INVALID\_DEPARTMENT\_ID | 错误的组织单元ID |
| 400 | invalidLang | INVALID\_LANG | 错误的通讯录语言 |
| 400 | deptNotExist | DEPT\_NOT\_EXIST | 组织单元不存在 |
| 400 | systemError | SYSTEM\_ERROR | 系统异常，请重试 |
