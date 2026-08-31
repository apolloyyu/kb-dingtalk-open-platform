---
title: "设置伙伴组织在上下游组织内的可见范围"
source_url: "https://open.dingtalk.com/document/development/set-the-visible-range-of-the-branch-in-the-group-1"
namespace: "development"
slug: "set-the-visible-range-of-the-branch-in-the-group-1"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 设置伙伴组织在上下游组织内的可见范围"
doc_id: "NTOntm4lJv"
updated_at: "2026-06-01 16:31:55"
---

> Source: https://open.dingtalk.com/document/development/set-the-visible-range-of-the-branch-in-the-group-1
> Path: 应用开发 / 服务端 API / 通讯录管理 > 上下游组织（原合作空间） > 设置伙伴组织在上下游组织内的可见范围
> Updated: 2026-06-01 16:31:55

# 设置伙伴组织在上下游组织内的可见范围

调用本接口，设置伙伴组织在上下游组织内的可见范围，也可以设置伙伴组织在上下游组织内可以被哪些部门可见。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/cooperateCorps/branchVisibleSettings |
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
| branchCorpId | String | 是 | 伙伴组织的企业corpId，详情参见[CorpId](https://open.dingtalk.com/document/development/basic-concepts-beta#section-bbk-mv0-oxd)。 |
| type | Long | 是 | 设置可见性类型，取值：   - **0**：在上下游组织通讯录隐藏伙伴组织，即其它伙伴组织都看不到，额外设置的分支和部门可以看到。 - **1**：仅可见伙伴组织自己，即只能看到自己企业加入的成员，额外设置分支和部门可以被看到。 |
| open | Boolean | 是 | 是否开启，取值：   - **true**：开启 - **false**：关闭 |
| visibleBranchCorpIds | Array of String | 否 | 设置例外的加入合作空间或关联组织的分支企业corpId列表，详情参见[CorpId](https://open.dingtalk.com/document/development/basic-concepts-beta#section-bbk-mv0-oxd)。 |
| visibleDeptIds | Array of Long | 否 | 设置例外的部门deptId列表，可调用[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取dept\_id参数值。 |

### 请求示例

HTTP

```
PUT /v1.0/contact/cooperateCorps/branchVisibleSettings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:48629xxx
Content-Type:application/json

[ {
  "branchCorpId" : "ding1234",
  "type" : 0,
  "open" : true,
  "visibleBranchCorpIds" : [ "ding45678" ],
  "visibleDeptIds" : [ 345567 ]
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
        UpdateBranchVisibleSettingInCooperateHeaders updateBranchVisibleSettingInCooperateHeaders = new UpdateBranchVisibleSettingInCooperateHeaders();
        updateBranchVisibleSettingInCooperateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateBranchVisibleSettingInCooperateRequest.UpdateBranchVisibleSettingInCooperateRequestBody body0 = new UpdateBranchVisibleSettingInCooperateRequest.UpdateBranchVisibleSettingInCooperateRequestBody()
                .setBranchCorpId("ding1234")
                .setType(0L)
                .setOpen(true)
                .setVisibleBranchCorpIds(java.util.Arrays.asList(
                    "ding45678"
                ))
                .setVisibleDeptIds(java.util.Arrays.asList(
                    345567L
                ));
        UpdateBranchVisibleSettingInCooperateRequest updateBranchVisibleSettingInCooperateRequest = new UpdateBranchVisibleSettingInCooperateRequest()
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.updateBranchVisibleSettingInCooperateWithOptions(updateBranchVisibleSettingInCooperateRequest, updateBranchVisibleSettingInCooperateHeaders, new RuntimeOptions());
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
        update_branch_visible_setting_in_cooperate_headers = dingtalkcontact__1__0_models.UpdateBranchVisibleSettingInCooperateHeaders()
        update_branch_visible_setting_in_cooperate_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkcontact__1__0_models.UpdateBranchVisibleSettingInCooperateRequestBody(
            branch_corp_id='ding1234',
            type=0,
            open=True,
            visible_branch_corp_ids=[
                'ding45678'
            ],
            visible_dept_ids=[
                345567
            ]
        )
        update_branch_visible_setting_in_cooperate_request = dingtalkcontact__1__0_models.UpdateBranchVisibleSettingInCooperateRequest(
            body=[
                body_0
            ]
        )
        try:
            client.update_branch_visible_setting_in_cooperate_with_options(update_branch_visible_setting_in_cooperate_request, update_branch_visible_setting_in_cooperate_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_branch_visible_setting_in_cooperate_headers = dingtalkcontact__1__0_models.UpdateBranchVisibleSettingInCooperateHeaders()
        update_branch_visible_setting_in_cooperate_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkcontact__1__0_models.UpdateBranchVisibleSettingInCooperateRequestBody(
            branch_corp_id='ding1234',
            type=0,
            open=True,
            visible_branch_corp_ids=[
                'ding45678'
            ],
            visible_dept_ids=[
                345567
            ]
        )
        update_branch_visible_setting_in_cooperate_request = dingtalkcontact__1__0_models.UpdateBranchVisibleSettingInCooperateRequest(
            body=[
                body_0
            ]
        )
        try:
            await client.update_branch_visible_setting_in_cooperate_with_options_async(update_branch_visible_setting_in_cooperate_request, update_branch_visible_setting_in_cooperate_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateBranchVisibleSettingInCooperateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateBranchVisibleSettingInCooperateRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\UpdateBranchVisibleSettingInCooperateRequest;
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
        $updateBranchVisibleSettingInCooperateHeaders = new UpdateBranchVisibleSettingInCooperateHeaders([]);
        $updateBranchVisibleSettingInCooperateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "branchCorpId" => "ding1234",
            "type" => 0,
            "open" => true,
            "visibleBranchCorpIds" => [
                "ding45678"
            ],
            "visibleDeptIds" => [
                345567
            ]
        ]);
        $updateBranchVisibleSettingInCooperateRequest = new UpdateBranchVisibleSettingInCooperateRequest([
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->updateBranchVisibleSettingInCooperateWithOptions($updateBranchVisibleSettingInCooperateRequest, $updateBranchVisibleSettingInCooperateHeaders, new RuntimeOptions([]));
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

  updateBranchVisibleSettingInCooperateHeaders := &dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateHeaders{}
  updateBranchVisibleSettingInCooperateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateRequestBody{
    BranchCorpId: tea.String("ding1234"),
    Type: tea.Int64(0),
    Open: tea.Bool(true),
    VisibleBranchCorpIds: []*string{tea.String("ding45678")},
    VisibleDeptIds: []*int64{tea.Int(345567)},
  }
  updateBranchVisibleSettingInCooperateRequest := &dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateRequest{
    Body: []*dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateBranchVisibleSettingInCooperateWithOptions(updateBranchVisibleSettingInCooperateRequest, updateBranchVisibleSettingInCooperateHeaders, &util.RuntimeOptions{})
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
    let updateBranchVisibleSettingInCooperateHeaders = new $dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateHeaders({ });
    updateBranchVisibleSettingInCooperateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let body0 = new $dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateRequestBody({
      branchCorpId: "ding1234",
      type: 0,
      open: true,
      visibleBranchCorpIds: [
        "ding45678"
      ],
      visibleDeptIds: [
        345567
      ],
    });
    let updateBranchVisibleSettingInCooperateRequest = new $dingtalkcontact_1_0.UpdateBranchVisibleSettingInCooperateRequest({
      body: [
        body0
      ],
    });
    try {
      await client.updateBranchVisibleSettingInCooperateWithOptions(updateBranchVisibleSettingInCooperateRequest, updateBranchVisibleSettingInCooperateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateHeaders updateBranchVisibleSettingInCooperateHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateHeaders();
            updateBranchVisibleSettingInCooperateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateRequest.UpdateBranchVisibleSettingInCooperateRequestBody body0 = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateRequest.UpdateBranchVisibleSettingInCooperateRequestBody
            {
                BranchCorpId = "ding1234",
                Type = 0,
                Open = true,
                VisibleBranchCorpIds = new List<string>
                {
                    "ding45678"
                },
                VisibleDeptIds = new List<long?>
                {
                    345567
                },
            };
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateRequest updateBranchVisibleSettingInCooperateRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateRequest
            {
                Body = new List<AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.UpdateBranchVisibleSettingInCooperateRequest.UpdateBranchVisibleSettingInCooperateRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.UpdateBranchVisibleSettingInCooperateWithOptions(updateBranchVisibleSettingInCooperateRequest, updateBranchVisibleSettingInCooperateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateHeaders> updateBranchVisibleSettingInCooperateHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateHeaders>();
  updateBranchVisibleSettingInCooperateHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateRequestBody> body0 = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateRequestBody>(map<string, boost::any>({
    {"branchCorpId", boost::any(string("ding1234"))},
    {"type", boost::any(0)},
    {"open", boost::any(true)},
    {"visibleBranchCorpIds", boost::any(vector<string>({
      "ding45678"
    }))},
    {"visibleDeptIds", boost::any(vector<long>({
      345567
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateRequest> updateBranchVisibleSettingInCooperateRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateRequest>(map<string, boost::any>({
    {"body", boost::any(vector<Alibabacloud_Dingtalkcontact_1_0::UpdateBranchVisibleSettingInCooperateRequestBody>({
      body0
    }))}
  }));
  try {
    client->updateBranchVisibleSettingInCooperateWithOptions(updateBranchVisibleSettingInCooperateRequest, updateBranchVisibleSettingInCooperateHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| 500 | system.error | 可见性更新失败 | 可见性更新失败 |
