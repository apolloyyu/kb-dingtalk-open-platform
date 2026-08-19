---
title: "获取流程任务用印审批列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-process-task-print-approval-list-1"
namespace: "development"
slug: "obtain-the-process-task-print-approval-list-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 签署流程 > 获取流程任务用印审批列表"
doc_id: "sGov9QCMOW"
updated_at: "2025-09-23 19:21:29"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-process-task-print-approval-list-1
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > e签宝 1.0 > 签署流程 > 获取流程任务用印审批列表
> Updated: 2025-09-23 19:21:29

# 获取流程任务用印审批列表

调用本接口获取流程中需审批印章的审批信息列表。

## **接口调用说明**

当前接口已完成升级迭代且不再支持新应用申请，存量应用调用不受影响，建议未接入的开发者使用[获取流程任务用印审批列表](1090-obtains-the-print-approval-list-for-process-tasks.md)接口，已接入的开发者结合实际尽快完成迁移。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/esign/seals/approval/list |
| HTTP Method | GET |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 不支持新增申请 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| taskId | String | 否 | 签署返回的任务id。 |

### 请求示例

HTTP

```
GET /v1.0/esign/seals/approval/list?taskId=hf9e762 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_1_0.*;
import com.aliyun.dingtalkesign_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_1_0.Client client = Sample.createClient();
        ListSealApprovalHeaders listSealApprovalHeaders = new ListSealApprovalHeaders();
        listSealApprovalHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListSealApprovalRequest listSealApprovalRequest = new ListSealApprovalRequest()
                .setTaskId("hf9e762");
        try {
            client.listSealApprovalWithOptions(listSealApprovalRequest, listSealApprovalHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_1_0.client import Client as dingtalkesign_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_seal_approval_headers = dingtalkesign__1__0_models.ListSealApprovalHeaders()
        list_seal_approval_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_seal_approval_request = dingtalkesign__1__0_models.ListSealApprovalRequest(
            task_id='hf9e762'
        )
        try:
            client.list_seal_approval_with_options(list_seal_approval_request, list_seal_approval_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_seal_approval_headers = dingtalkesign__1__0_models.ListSealApprovalHeaders()
        list_seal_approval_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_seal_approval_request = dingtalkesign__1__0_models.ListSealApprovalRequest(
            task_id='hf9e762'
        )
        try:
            await client.list_seal_approval_with_options_async(list_seal_approval_request, list_seal_approval_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\ListSealApprovalHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\ListSealApprovalRequest;
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
        $listSealApprovalHeaders = new ListSealApprovalHeaders([]);
        $listSealApprovalHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listSealApprovalRequest = new ListSealApprovalRequest([
            "taskId" => "hf9e762"
        ]);
        try {
            $client->listSealApprovalWithOptions($listSealApprovalRequest, $listSealApprovalHeaders, new RuntimeOptions([]));
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
  dingtalkesign_1_0  ""github.com/alibabacloud-go/dingtalk/esign_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_1_0.Client{}
  _result, _err = dingtalkesign_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listSealApprovalHeaders := &dingtalkesign_1_0.ListSealApprovalHeaders{}
  listSealApprovalHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listSealApprovalRequest := &dingtalkesign_1_0.ListSealApprovalRequest{
    TaskId: tea.String("hf9e762"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListSealApprovalWithOptions(listSealApprovalRequest, listSealApprovalHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_1_0, * as $dingtalkesign_1_0 from '"@alicloud/dingtalk/esign_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listSealApprovalHeaders = new $dingtalkesign_1_0.ListSealApprovalHeaders({ });
    listSealApprovalHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listSealApprovalRequest = new $dingtalkesign_1_0.ListSealApprovalRequest({
      taskId: "hf9e762",
    });
    try {
      await client.listSealApprovalWithOptions(listSealApprovalRequest, listSealApprovalHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ListSealApprovalHeaders listSealApprovalHeaders = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ListSealApprovalHeaders();
            listSealApprovalHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ListSealApprovalRequest listSealApprovalRequest = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.ListSealApprovalRequest
            {
                TaskId = "hf9e762",
            };
            try
            {
                client.ListSealApprovalWithOptions(listSealApprovalRequest, listSealApprovalHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::ListSealApprovalHeaders> listSealApprovalHeaders = make_shared<Alibabacloud_Dingtalkesign_1_0::ListSealApprovalHeaders>();
  listSealApprovalHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::ListSealApprovalRequest> listSealApprovalRequest = make_shared<Alibabacloud_Dingtalkesign_1_0::ListSealApprovalRequest>(map<string, boost::any>({
    {"taskId", boost::any(string("hf9e762"))}
  }));
  try {
    client->listSealApprovalWithOptions(listSealApprovalRequest, listSealApprovalHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| data | Array | 调用返回的结果。 |
| approvalName | String | 审批名称。 |
| status | String | 审批状态，取值：   - WAIT：等待审批 - APPROVING：审批中 - AGREED：审批通过 - REFUSED：审批拒绝 |
| refuseReason | String | 审批拒绝原因。 |
| sponsorAccountName | String | 审批发起人姓名。 |
| startTime | Long | 审批开始时间戳。 |
| endTime | Long | 审批结束时间。 |
| sealIdImg | String | 印章图片地址。 |
| approvalNodes | Array | 审批节点信息集合。 |
| approverName | String | 审批人姓名。 |
| status | String | 审批状态，取值：   - WAIT：等待审批 - APPROVING：审批中 - AGREED：审批通过 - REFUSED：审批拒绝 |
| startTime | Long | 节点开始时间。 |
| approvalTime | Long | 节点审批时间。 |
| code | Integer | 返回码。 |
| message | String | 返回码描述。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "data" : [ {
    "approvalName" : "xx的用印申请",
    "status" : "REFUSED",
    "refuseReason" : "权限不足",
    "sponsorAccountName" : "某某",
    "startTime" : 1613720267000,
    "endTime" : 1613720267000,
    "sealIdImg" : "https://xxxxxx/720-1280.png",
    "approvalNodes" : [ {
      "approverName" : "管理员",
      "status" : "REFUSED",
      "startTime" : 1613720267000,
      "approvalTime" : 1613720267000
    } ]
  } ],
  "code" : 0,
  "message" : "ok"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.invalidAguemnts | invalid arguments | 参数错误 |
