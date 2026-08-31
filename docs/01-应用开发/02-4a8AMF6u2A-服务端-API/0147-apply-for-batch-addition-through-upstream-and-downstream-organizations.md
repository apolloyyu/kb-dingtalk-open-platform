---
title: "批量通过伙伴组织的加入申请"
source_url: "https://open.dingtalk.com/document/development/apply-for-batch-addition-through-upstream-and-downstream-organizations"
namespace: "development"
slug: "apply-for-batch-addition-through-upstream-and-downstream-organizations"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 批量通过伙伴组织的加入申请"
doc_id: "Yu9LHSbXJD"
updated_at: "2026-06-01 16:31:54"
---

> Source: https://open.dingtalk.com/document/development/apply-for-batch-addition-through-upstream-and-downstream-organizations
> Path: 应用开发 / 服务端 API / 通讯录管理 > 上下游组织（原合作空间） > 批量通过伙伴组织的加入申请
> Updated: 2026-06-01 16:31:54

# 批量通过伙伴组织的加入申请

调用本接口，批量通过伙伴组织加入上下游组织申请。

## 接口调用说明

例如，上下游组织的通讯录目前没有任何伙伴组织加入，如下图所示。 ![](https://img.alicdn.com/imgextra/i2/O1CN01pzDlnp1dLo7xApRsF_!!6000000003720-2-tps-2852-800.png) 上下游组织收到两条加入申请，分别为**关联组织**和**体验组织**，申请信息如下图所示。 ![](https://img.alicdn.com/imgextra/i4/O1CN01xQnX7J1ryeKtrKVNG_!!6000000005700-2-tps-1062-710.png) 调用本接口可同时同意这两条加入上下游组织的申请。接口调用成功后，上下游组织的通讯录新增了**关联组织**和**体验组织**，如下图所示。 ![](https://img.alicdn.com/imgextra/i4/O1CN013xmkYD1bZQfwG78sO_!!6000000003479-2-tps-2792-796.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/cooperateCorps/unionApplications/approve |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Contact.CooperateCorp.Write-通讯录合作空间写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 否 | 需要处理的申请列表，一次请求最多处理10个申请。 |
| branchCorpId | String | 否 | 申请的合作伙伴组织CorpId，详情参见[CorpId](https://open.dingtalk.com/document/development/basic-concepts-beta#section-bbk-mv0-oxd)。 |
| unionRootName | String | 否 | 合作伙伴组织在上下游组织内的名称。 |
| linkDeptId | Long | 否 | 合作伙伴组织在上下游组织内的位置，可调用[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取dept\_id参数值。 |

### 请求示例

HTTP

```
POST /v1.0/contact/cooperateCorps/unionApplications/approve HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:4e6ce004e9843daf86407d94939a7502
Content-Type:application/json

[ {
  "branchCorpId" : "ding1234",
  "unionRootName" : "测试",
  "linkDeptId" : 123456
} ]
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcontact_1_0.*;
import com.aliyun.dingtalkcontact_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcontact_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcontact_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcontact_1_0.Client client = Sample.createClient();
        BatchApproveUnionApplyHeaders batchApproveUnionApplyHeaders = new BatchApproveUnionApplyHeaders();
        batchApproveUnionApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        BatchApproveUnionApplyRequest.BatchApproveUnionApplyRequestBody body0 = new BatchApproveUnionApplyRequest.BatchApproveUnionApplyRequestBody()
                .setBranchCorpId("ding1234")
                .setUnionRootName("测试")
                .setLinkDeptId(123456L);
        BatchApproveUnionApplyRequest batchApproveUnionApplyRequest = new BatchApproveUnionApplyRequest()
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.batchApproveUnionApplyWithOptions(batchApproveUnionApplyRequest, batchApproveUnionApplyHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.contact_1_0.client import Client as dingtalkcontact_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.contact_1_0 import models as dingtalkcontact__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcontact_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcontact_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_approve_union_apply_headers = dingtalkcontact__1__0_models.BatchApproveUnionApplyHeaders()
        batch_approve_union_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkcontact__1__0_models.BatchApproveUnionApplyRequestBody(
            branch_corp_id='ding1234',
            union_root_name='测试',
            link_dept_id=123456
        )
        batch_approve_union_apply_request = dingtalkcontact__1__0_models.BatchApproveUnionApplyRequest(
            body=[
                body_0
            ]
        )
        try:
            client.batch_approve_union_apply_with_options(batch_approve_union_apply_request, batch_approve_union_apply_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_approve_union_apply_headers = dingtalkcontact__1__0_models.BatchApproveUnionApplyHeaders()
        batch_approve_union_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkcontact__1__0_models.BatchApproveUnionApplyRequestBody(
            branch_corp_id='ding1234',
            union_root_name='测试',
            link_dept_id=123456
        )
        batch_approve_union_apply_request = dingtalkcontact__1__0_models.BatchApproveUnionApplyRequest(
            body=[
                body_0
            ]
        )
        try:
            await client.batch_approve_union_apply_with_options_async(batch_approve_union_apply_request, batch_approve_union_apply_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\BatchApproveUnionApplyHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\BatchApproveUnionApplyRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\BatchApproveUnionApplyRequest;
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
        $batchApproveUnionApplyHeaders = new BatchApproveUnionApplyHeaders([]);
        $batchApproveUnionApplyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "branchCorpId" => "ding1234",
            "unionRootName" => "测试",
            "linkDeptId" => 123456
        ]);
        $batchApproveUnionApplyRequest = new BatchApproveUnionApplyRequest([
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->batchApproveUnionApplyWithOptions($batchApproveUnionApplyRequest, $batchApproveUnionApplyHeaders, new RuntimeOptions([]));
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
  dingtalkcontact_1_0  "github.com/alibabacloud-go/dingtalk/contact_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcontact_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcontact_1_0.Client{}
  _result, _err = dingtalkcontact_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchApproveUnionApplyHeaders := &dingtalkcontact_1_0.BatchApproveUnionApplyHeaders{}
  batchApproveUnionApplyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkcontact_1_0.BatchApproveUnionApplyRequestBody{
    BranchCorpId: tea.String("ding1234"),
    UnionRootName: tea.String("测试"),
    LinkDeptId: tea.Int64(123456),
  }
  batchApproveUnionApplyRequest := &dingtalkcontact_1_0.BatchApproveUnionApplyRequest{
    Body: []*dingtalkcontact_1_0.BatchApproveUnionApplyRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchApproveUnionApplyWithOptions(batchApproveUnionApplyRequest, batchApproveUnionApplyHeaders, &util.RuntimeOptions{})
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
import dingtalkcontact_1_0, * as $dingtalkcontact_1_0 from '@alicloud/dingtalk/contact_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcontact_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcontact_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let batchApproveUnionApplyHeaders = new $dingtalkcontact_1_0.BatchApproveUnionApplyHeaders({ });
    batchApproveUnionApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let body0 = new $dingtalkcontact_1_0.BatchApproveUnionApplyRequestBody({
      branchCorpId: "ding1234",
      unionRootName: "测试",
      linkDeptId: 123456,
    });
    let batchApproveUnionApplyRequest = new $dingtalkcontact_1_0.BatchApproveUnionApplyRequest({
      body: [
        body0
      ],
    });
    try {
      await client.batchApproveUnionApplyWithOptions(batchApproveUnionApplyRequest, batchApproveUnionApplyHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcontact_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcontact_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyHeaders batchApproveUnionApplyHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyHeaders();
            batchApproveUnionApplyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyRequest.BatchApproveUnionApplyRequestBody body0 = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyRequest.BatchApproveUnionApplyRequestBody
            {
                BranchCorpId = "ding1234",
                UnionRootName = "测试",
                LinkDeptId = 123456,
            };
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyRequest batchApproveUnionApplyRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyRequest
            {
                Body = new List<AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.BatchApproveUnionApplyRequest.BatchApproveUnionApplyRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.BatchApproveUnionApplyWithOptions(batchApproveUnionApplyRequest, batchApproveUnionApplyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否处理成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.blank | 参数为空 | 非法的系统参数 |
| 400 | parameter.error | 单次操作不能超过10个 | 单次操作不能超过10个 |
| 500 | system.error | 操作失败 | 操作失败 |
