---
title: "根据userId查询人员的标签信息"
source_url: "https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-user-tag"
namespace: "development"
slug: "you-can-call-this-operation-to-retrieve-the-user-tag"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 产业互联 > 根据userId查询人员的标签信息"
doc_id: "Tb3f21vNkJ"
updated_at: "2026-06-04 19:09:57"
---

> Source: https://open.dingtalk.com/document/development/you-can-call-this-operation-to-retrieve-the-user-tag
> Path: 应用开发 / 服务端 API / 专属钉钉 > 产业互联 > 根据userId查询人员的标签信息
> Updated: 2026-06-04 19:09:57

# 根据userId查询人员的标签信息

调用本接口查询上下游组织内人员的标签信息。

## 接口调用说明

本接口目前仅支持专属钉钉企业调用，如何申请开通专属钉钉，请参考[专属钉钉开通流程](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/KOEmgBoGwD78vZrbzdR68ndLerP9b30a?spm=ding_open_doc.document.0.0.7f40722fMQjJ5n)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/partners/users/{userId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Partner.Department.Read-伙伴钉部门信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户userId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/partners/users/001 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkexclusive_1_0.*;
import com.aliyun.dingtalkexclusive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        QueryPartnerInfoHeaders queryPartnerInfoHeaders = new QueryPartnerInfoHeaders();
        queryPartnerInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.queryPartnerInfoWithOptions("001", queryPartnerInfoHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_partner_info_headers = dingtalkexclusive__1__0_models.QueryPartnerInfoHeaders()
        query_partner_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.query_partner_info_with_options('001', query_partner_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_partner_info_headers = dingtalkexclusive__1__0_models.QueryPartnerInfoHeaders()
        query_partner_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.query_partner_info_with_options_async('001', query_partner_info_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\QueryPartnerInfoHeaders;
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
        $queryPartnerInfoHeaders = new QueryPartnerInfoHeaders([]);
        $queryPartnerInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->queryPartnerInfoWithOptions("001", $queryPartnerInfoHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryPartnerInfoHeaders := &dingtalkexclusive_1_0.QueryPartnerInfoHeaders{}
  queryPartnerInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryPartnerInfoWithOptions(tea.String("001"), queryPartnerInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryPartnerInfoHeaders = new $dingtalkexclusive_1_0.QueryPartnerInfoHeaders({ });
    queryPartnerInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    try {
      await client.queryPartnerInfoWithOptions("001", queryPartnerInfoHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryPartnerInfoHeaders queryPartnerInfoHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.QueryPartnerInfoHeaders();
            queryPartnerInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.QueryPartnerInfoWithOptions("001", queryPartnerInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| partnerDeptList | Array | 员工所在的部门列表。 |
| title | String | 部门名称。 |
| value | String | 部门ID。 |
| memberCount | Long | 成员数。 |
| partnerNum | String | 伙伴编码。 |
| partnerLabelModelLevel1 | Object | 一级伙伴信息。 |
| labelId | Long | 一级伙伴标签ID。 |
| labelname | String | 一级伙伴类型。 |
| partnerLabelList | Array | 伙伴类型下的角色列表。 |
| id | Long | 伙伴标签下的角色ID。 |
| name | String | 伙伴标签下的角色名称。 |
| userId | String | 员工userId。      如果partnerLabelList为空，该字段返回为空。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "partnerDeptList" : [ {
    "title" : "测试组织1",
    "value" : "123",
    "memberCount" : 111,
    "partnerNum" : "1",
    "partnerLabelModelLevel1" : {
      "labelId" : 111,
      "labelname" : "测试"
    }
  } ],
  "partnerLabelList" : [ {
    "id" : 111,
    "name" : "测试"
  } ],
  "userId" : "111111"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.not.found | 参数不能为空 | 参数不能为空 |
| 500 | user.not.found | 该员工不在企业中 | 该员工不在企业中 |
| 500 | hava.no.auth | 该员工无企业权限 | 该员工无企业权限 |
