---
title: "更新伙伴组织在上下游组织内的属性信息"
source_url: "https://open.dingtalk.com/document/development/update-properties-of-branches-in-alibaba-group-1"
namespace: "development"
slug: "update-properties-of-branches-in-alibaba-group-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 更新伙伴组织在上下游组织内的属性信息"
doc_id: "XqJTg56oR9"
updated_at: "2026-06-01 16:31:54"
---

> Source: https://open.dingtalk.com/document/development/update-properties-of-branches-in-alibaba-group-1
> Path: 应用开发 / 服务端API / 通讯录管理 > 上下游组织（原合作空间） > 更新伙伴组织在上下游组织内的属性信息
> Updated: 2026-06-01 16:31:54

# 更新伙伴组织在上下游组织内的属性信息

调用本接口，更新伙伴组织在上下游组织内内的属性信息，包括新伙伴组织的别名，新伙伴组织在上下游组织内的通讯录位置等。

## 接口调用说明

> **[!NOTE]**
>
> 如果更新伙伴组织在通讯录的位置是一级目录，调用本接口的挂载部门参数linkDeptId，需要传-1。

例如，测试组织演示是上下游组织钉钉上下游联盟内的伙伴组织，调用本接口可以更新测试组织演示的别名和在通讯录内的位置，如图。 ![](https://img.alicdn.com/imgextra/i3/O1CN01kAYPkt24zBn8b0ua4_!!6000000007461-2-tps-1192-866.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/cooperateCorps/branchAttributes |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Contact.CooperateCorp.Write-通讯录合作空间写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。   **[!NOTE]**    调用本接口，需要使用上下游组织的访问凭证，不能使用所属组织的访问凭证。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 是 | 请求参数。 |
| branchCorpId | String | 是 | 伙伴组织的企业ID，可调用[获取已加入或正在申请加入上下游组织的组织和个人信息](0151-obtains-the-information-about-how-to-join-or-apply-to.md)获取dept\_id参数值。 |
| unionRootName | String | 是 | 伙伴组织在上下游组织内的别名。 |
| linkDeptId | Long | 是 | 挂载节点部门ID，如果是根部门，需要传-1，可调用[获取已加入或正在申请加入上下游组织的组织和个人信息](0151-obtains-the-information-about-how-to-join-or-apply-to.md)获取dept\_id参数值。 |

### 请求示例

HTTP

```
PUT /v1.0/contact/cooperateCorps/branchAttributes HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:48629axxx
Content-Type:application/json

[ {
  "branchCorpId" : "ding1234",
  "unionRootName" : "在主干的别名",
  "linkDeptId" : 23456
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
        UpdateBranchAttributesInCooperateHeaders updateBranchAttributesInCooperateHeaders = new UpdateBranchAttributesInCooperateHeaders();
        updateBranchAttributesInCooperateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateBranchAttributesInCooperateRequest.UpdateBranchAttributesInCooperateRequestBody body0 = new UpdateBranchAttributesInCooperateRequest.UpdateBranchAttributesInCooperateRequestBody()
                .setBranchCorpId("ding1234")
                .setUnionRootName("在主干的别名")
                .setLinkDeptId(23456L);
        UpdateBranchAttributesInCooperateRequest updateBranchAttributesInCooperateRequest = new UpdateBranchAttributesInCooperateRequest()
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.updateBranchAttributesInCooperateWithOptions(updateBranchAttributesInCooperateRequest, updateBranchAttributesInCooperateHeaders, new RuntimeOptions());
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
        update_branch_attributes_in_cooperate_headers = dingtalkcontact__1__0_models.UpdateBranchAttributesInCooperateHeaders()
        update_branch_attributes_in_cooperate_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkcontact__1__0_models.UpdateBranchAttributesInCooperateRequestBody(
            branch_corp_id='ding1234',
            union_root_name='在主干的别名',
            link_dept_id=23456
        )
        update_branch_attributes_in_cooperate_request = dingtalkcontact__1__0_models.UpdateBranchAttributesInCooperateRequest(
            body=[
                body_0
            ]
        )
        try:
            client.update_branch_attributes_in_cooperate_with_options(update_branch_attributes_in_cooperate_request, update_branch_attributes_in_cooperate_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_branch_attributes_in_cooperate_headers = dingtalkcontact__1__0_models.UpdateBranchAttributesInCooperateHeaders()
        update_branch_attributes_in_cooperate_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkcontact__1__0_models.UpdateBranchAttributesInCooperateRequestBody(
            branch_corp_id='ding1234',
            union_root_name='在主干的别名',
            link_dept_id=23456
        )
        update_branch_attributes_in_cooperate_request = dingtalkcontact__1__0_models.UpdateBranchAttributesInCooperateRequest(
            body=[
                body_0
            ]
        )
        try:
            await client.update_branch_attributes_in_cooperate_with_options_async(update_branch_attributes_in_cooperate_request, update_branch_attributes_in_cooperate_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateBranchAttributesInCooperateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateBranchAttributesInCooperateRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateBranchAttributesInCooperateRequest;
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
        $updateBranchAttributesInCooperateHeaders = new UpdateBranchAttributesInCooperateHeaders([]);
        $updateBranchAttributesInCooperateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "branchCorpId" => "ding1234",
            "unionRootName" => "在主干的别名",
            "linkDeptId" => 23456
        ]);
        $updateBranchAttributesInCooperateRequest = new UpdateBranchAttributesInCooperateRequest([
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->updateBranchAttributesInCooperateWithOptions($updateBranchAttributesInCooperateRequest, $updateBranchAttributesInCooperateHeaders, new RuntimeOptions([]));
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

  updateBranchAttributesInCooperateHeaders := &dingtalkcontact_1_0.UpdateBranchAttributesInCooperateHeaders{}
  updateBranchAttributesInCooperateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkcontact_1_0.UpdateBranchAttributesInCooperateRequestBody{
    BranchCorpId: tea.String("ding1234"),
    UnionRootName: tea.String("在主干的别名"),
    LinkDeptId: tea.Int64(23456),
  }
  updateBranchAttributesInCooperateRequest := &dingtalkcontact_1_0.UpdateBranchAttributesInCooperateRequest{
    Body: []*dingtalkcontact_1_0.UpdateBranchAttributesInCooperateRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateBranchAttributesInCooperateWithOptions(updateBranchAttributesInCooperateRequest, updateBranchAttributesInCooperateHeaders, &util.RuntimeOptions{})
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
    let updateBranchAttributesInCooperateHeaders = new $dingtalkcontact_1_0.UpdateBranchAttributesInCooperateHeaders({ });
    updateBranchAttributesInCooperateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let body0 = new $dingtalkcontact_1_0.UpdateBranchAttributesInCooperateRequestBody({
      branchCorpId: "ding1234",
      unionRootName: "在主干的别名",
      linkDeptId: 23456,
    });
    let updateBranchAttributesInCooperateRequest = new $dingtalkcontact_1_0.UpdateBranchAttributesInCooperateRequest({
      body: [
        body0
      ],
    });
    try {
      await client.updateBranchAttributesInCooperateWithOptions(updateBranchAttributesInCooperateRequest, updateBranchAttributesInCooperateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateHeaders updateBranchAttributesInCooperateHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateHeaders();
            updateBranchAttributesInCooperateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateRequest.UpdateBranchAttributesInCooperateRequestBody body0 = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateRequest.UpdateBranchAttributesInCooperateRequestBody
            {
                BranchCorpId = "ding1234",
                UnionRootName = "在主干的别名",
                LinkDeptId = 23456,
            };
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateRequest updateBranchAttributesInCooperateRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateRequest
            {
                Body = new List<AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchAttributesInCooperateRequest.UpdateBranchAttributesInCooperateRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.UpdateBranchAttributesInCooperateWithOptions(updateBranchAttributesInCooperateRequest, updateBranchAttributesInCooperateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcontact__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

Alibabacloud_Dingtalkcontact_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcontact_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcontact_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateHeaders> updateBranchAttributesInCooperateHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateHeaders>();
  updateBranchAttributesInCooperateHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateRequestBody> body0 = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateRequestBody>(map<string, boost::any>({
    {"branchCorpId", boost::any(string("ding1234"))},
    {"unionRootName", boost::any(string("在主干的别名"))},
    {"linkDeptId", boost::any(23456)}
  }));
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateRequest> updateBranchAttributesInCooperateRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateRequest>(map<string, boost::any>({
    {"body", boost::any(vector<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchAttributesInCooperateRequestBody>({
      body0
    }))}
  }));
  try {
    client->updateBranchAttributesInCooperateWithOptions(updateBranchAttributesInCooperateRequest, updateBranchAttributesInCooperateHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameter.blank | 参数为空 | 参数为空 |
| 400 | parameter.error | 参数错误 | 参数错误 |
| 500 | system.error | 更新失败 | 更新失败 |
