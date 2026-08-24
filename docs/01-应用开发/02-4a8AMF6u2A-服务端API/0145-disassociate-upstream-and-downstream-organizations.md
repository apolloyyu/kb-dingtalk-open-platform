---
title: "解除关联组织"
source_url: "https://open.dingtalk.com/document/development/disassociate-upstream-and-downstream-organizations"
namespace: "development"
slug: "disassociate-upstream-and-downstream-organizations"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 解除关联组织"
doc_id: "PknyHppNIK"
updated_at: "2026-06-02 09:24:47"
---

> Source: https://open.dingtalk.com/document/development/disassociate-upstream-and-downstream-organizations
> Path: 应用开发 / 服务端API / 通讯录管理 > 上下游组织（原合作空间） > 解除关联组织
> Updated: 2026-06-02 09:24:47

# 解除关联组织

调用本接口，用于解除关联组织关系。

## 接口调用说明

例如，上下游组织“测试演示组织”已关联“体验组织”。

![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/7843630871/p1075886.png)

调用本接口，解除“测试演示组织”、“体验组织”上下游组织关联，效果同下图产品功能解除上下游组织关联。解除关联关系前”测试演示组织“只有1个关联组织，解除关联后，解除后”体验组织“不在”测试演示组织“的关联组织列表中，关联组织列表为空。

![iShot2022-03-24 19](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2713218461/p422661.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/contact/cooperateCorps/separate |
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
| attachDeptId | Long | 是 | 伙伴组织在上下游组织内的部门ID，上下游组织通过[获取部门列表](https://open.dingtalk.com/document/development/obtain-the-department-list-v2)接口获取dept\_id参数值。 |

### 请求示例

HTTP

```
POST /v1.0/contact/cooperateCorps/separate HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:tokenxxx
Content-Type:application/json

{
  "attachDeptId" : 123
}
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
        SeparateBranchOrgHeaders separateBranchOrgHeaders = new SeparateBranchOrgHeaders();
        separateBranchOrgHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SeparateBranchOrgRequest separateBranchOrgRequest = new SeparateBranchOrgRequest()
                .setAttachDeptId(123L);
        try {
            client.separateBranchOrgWithOptions(separateBranchOrgRequest, separateBranchOrgHeaders, new RuntimeOptions());
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
        separate_branch_org_headers = dingtalkcontact__1__0_models.SeparateBranchOrgHeaders()
        separate_branch_org_headers.x_acs_dingtalk_access_token = '<your access token>'
        separate_branch_org_request = dingtalkcontact__1__0_models.SeparateBranchOrgRequest(
            attach_dept_id=123
        )
        try:
            client.separate_branch_org_with_options(separate_branch_org_request, separate_branch_org_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        separate_branch_org_headers = dingtalkcontact__1__0_models.SeparateBranchOrgHeaders()
        separate_branch_org_headers.x_acs_dingtalk_access_token = '<your access token>'
        separate_branch_org_request = dingtalkcontact__1__0_models.SeparateBranchOrgRequest(
            attach_dept_id=123
        )
        try:
            await client.separate_branch_org_with_options_async(separate_branch_org_request, separate_branch_org_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\SeparateBranchOrgHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcontact_1_0\Models\SeparateBranchOrgRequest;
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
        $separateBranchOrgHeaders = new SeparateBranchOrgHeaders([]);
        $separateBranchOrgHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $separateBranchOrgRequest = new SeparateBranchOrgRequest([
            "attachDeptId" => 123
        ]);
        try {
            $client->separateBranchOrgWithOptions($separateBranchOrgRequest, $separateBranchOrgHeaders, new RuntimeOptions([]));
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

  separateBranchOrgHeaders := &dingtalkcontact_1_0.SeparateBranchOrgHeaders{}
  separateBranchOrgHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  separateBranchOrgRequest := &dingtalkcontact_1_0.SeparateBranchOrgRequest{
    AttachDeptId: tea.Int64(123),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SeparateBranchOrgWithOptions(separateBranchOrgRequest, separateBranchOrgHeaders, &util.RuntimeOptions{})
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
    let separateBranchOrgHeaders = new $dingtalkcontact_1_0.SeparateBranchOrgHeaders({ });
    separateBranchOrgHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let separateBranchOrgRequest = new $dingtalkcontact_1_0.SeparateBranchOrgRequest({
      attachDeptId: 123,
    });
    try {
      await client.separateBranchOrgWithOptions(separateBranchOrgRequest, separateBranchOrgHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SeparateBranchOrgHeaders separateBranchOrgHeaders = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SeparateBranchOrgHeaders();
            separateBranchOrgHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SeparateBranchOrgRequest separateBranchOrgRequest = new AlibabaCloud.SDK.Dingtalkcontact_1_0.Models.SeparateBranchOrgRequest
            {
                AttachDeptId = 123,
            };
            try
            {
                client.SeparateBranchOrgWithOptions(separateBranchOrgRequest, separateBranchOrgHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::SeparateBranchOrgHeaders> separateBranchOrgHeaders = make_shared<Alibabacloud_Dingtalkcontact_1_0::SeparateBranchOrgHeaders>();
  separateBranchOrgHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcontact_1_0::SeparateBranchOrgRequest> separateBranchOrgRequest = make_shared<Alibabacloud_Dingtalkcontact_1_0::SeparateBranchOrgRequest>(map<string, boost::any>({
    {"attachDeptId", boost::any(123)}
  }));
  try {
    client->separateBranchOrgWithOptions(separateBranchOrgRequest, separateBranchOrgHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Boolean | 处理结果。   - 如果解除成功，该值为true。 - 如果解除失败，不返回result，接口会响应对应报错信息。 |

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
| 400 | parameter.error | 参数不合法，请确认关联关系 | 参数不合法，请确认关联关系 |
| 400 | parameter.blank | 参数为空 | 参数为空 |
| 500 | system.error | 系统错误 | 系统错误 |
