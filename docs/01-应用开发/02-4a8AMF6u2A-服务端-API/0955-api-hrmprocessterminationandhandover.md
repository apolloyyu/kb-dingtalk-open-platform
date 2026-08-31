---
title: "确认员工离职并删除"
source_url: "https://open.dingtalk.com/document/development/api-hrmprocessterminationandhandover"
namespace: "development"
slug: "api-hrmprocessterminationandhandover"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 员工关系 > 确认员工离职并删除"
doc_id: "I90rGNabkk"
updated_at: "2026-06-04 19:10:31"
---

> Source: https://open.dingtalk.com/document/development/api-hrmprocessterminationandhandover
> Path: 应用开发 / 服务端 API / 智能人事 > 员工关系 > 确认员工离职并删除
> Updated: 2026-06-04 19:10:31

# 确认员工离职并删除

调用本接口，根据操作员工 ID、离职人员 ID，实现企业员工离职并删除的功能。支持设置交接人。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/processes/terminateAndHandOver |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrm.Process.ReadWrite-智能人事流程读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 要离职员工的 UserId。       - 本接口调用成功后企业员工将直接离职并从企业通讯录删除。 - 本接口不支持主管理员的离职， 需要先撤销主管理员权限；且不支持上下级组织员工和行业通讯录员工。 |
| optUserId | String | 是 | 离职的操作人。      必须是本组织员工，且不能是离职员工本人。 |
| lastWorkDate | Long | 是 | 离职日期，Unix事件戳，单位毫秒。 |
| dismissionReason | Integer | 否 | 废弃字段， 建议使用`terminationReasonPassive` 和 `terminationReasonVoluntary` 离职原因字段。    离职原因：   - 1：家庭原因 - 2：个人原因 - 3：发展原因 - 4：合同到期不续签 - 5：协议解除 - 6：无法胜任工作 - 7：经济性裁员 - 8：严重违法违纪 - 9：其他 |
| terminationReasonVoluntary | Array of String | 否 | 主动离职原因的id，调用[获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md)接口获取离职原因id。      `terminationReasonPassive` 和 `terminationReasonVoluntary` 至少填写一个。 |
| terminationReasonPassive | Array of String | 否 | 被动离职原因的id，调用[获取企业已有的所有离职原因](0953-api-getalldismissionreasons.md)接口获取离职原因id。      `terminationReasonPassive` 和 `terminationReasonVoluntary` 至少填写一个。 |
| dismissionMemo | String | 是 | 离职原因备注。 |
| aflowHandOverUserId | String | 否 | 审批离职交接人。      离职人和交接人不能相同。 |
| docNoteHandoverUserId | String | 否 | 团队文档离职交接人。      离职人和交接人不能相同。 |
| dingPanHandoverUserId | String | 否 | 钉盘离职交接人。      离职人和交接人不能相同。 |
| permissionHandoverUserId | String | 否 | 权限离职交接人。      离职人和交接人不能相同。 |
| directSubordinatesHandoverUserId | String | 否 | 直属下属交接人。      离职人和交接人不能相同。 |

### 请求示例

HTTP

```
POST /v1.0/hrm/processes/terminateAndHandOver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6026d899410a3409badc3d9f5e14383b
Content-Type:application/json

{
  "userId" : "user1",
  "optUserId" : "user5678",
  "lastWorkDate" : 1704074400000,
  "dismissionReason" : 1,
  "dismissionMemo" : "离职原因备注",
  "aflowHandOverUserId" : "user123",
  "docNoteHandoverUserId" : "user123",
  "dingPanHandoverUserId" : "user123",
  "permissionHandoverUserId" : "user123",
  "directSubordinatesHandoverUserId" : "user123"
}
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
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.HrmProcessTerminationAndHandoverHeaders hrmProcessTerminationAndHandoverHeaders = new com.aliyun.dingtalkhrm_1_0.models.HrmProcessTerminationAndHandoverHeaders();
        hrmProcessTerminationAndHandoverHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.HrmProcessTerminationAndHandoverRequest hrmProcessTerminationAndHandoverRequest = new com.aliyun.dingtalkhrm_1_0.models.HrmProcessTerminationAndHandoverRequest()
                .setUserId("user1")
                .setOptUserId("user5678")
                .setLastWorkDate(1704074400000L)
                .setDismissionReason(1)
                .setDismissionMemo("离职原因备注")
                .setAflowHandOverUserId("user123")
                .setDocNoteHandoverUserId("user123")
                .setDingPanHandoverUserId("user123")
                .setPermissionHandoverUserId("user123")
                .setDirectSubordinatesHandoverUserId("user123");
        try {
            client.hrmProcessTerminationAndHandoverWithOptions(hrmProcessTerminationAndHandoverRequest, hrmProcessTerminationAndHandoverHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrm_1_0.client import Client as dingtalkhrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrm_process_termination_and_handover_headers = dingtalkhrm__1__0_models.HrmProcessTerminationAndHandoverHeaders()
        hrm_process_termination_and_handover_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_termination_and_handover_request = dingtalkhrm__1__0_models.HrmProcessTerminationAndHandoverRequest(
            user_id='user1',
            opt_user_id='user5678',
            last_work_date=1704074400000,
            dismission_reason=1,
            dismission_memo='离职原因备注',
            aflow_hand_over_user_id='user123',
            doc_note_handover_user_id='user123',
            ding_pan_handover_user_id='user123',
            permission_handover_user_id='user123',
            direct_subordinates_handover_user_id='user123'
        )
        try:
            client.hrm_process_termination_and_handover_with_options(hrm_process_termination_and_handover_request, hrm_process_termination_and_handover_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrm_process_termination_and_handover_headers = dingtalkhrm__1__0_models.HrmProcessTerminationAndHandoverHeaders()
        hrm_process_termination_and_handover_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_termination_and_handover_request = dingtalkhrm__1__0_models.HrmProcessTerminationAndHandoverRequest(
            user_id='user1',
            opt_user_id='user5678',
            last_work_date=1704074400000,
            dismission_reason=1,
            dismission_memo='离职原因备注',
            aflow_hand_over_user_id='user123',
            doc_note_handover_user_id='user123',
            ding_pan_handover_user_id='user123',
            permission_handover_user_id='user123',
            direct_subordinates_handover_user_id='user123'
        )
        try:
            await client.hrm_process_termination_and_handover_with_options_async(hrm_process_termination_and_handover_request, hrm_process_termination_and_handover_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessTerminationAndHandoverHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessTerminationAndHandoverRequest;
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
        $hrmProcessTerminationAndHandoverHeaders = new HrmProcessTerminationAndHandoverHeaders([]);
        $hrmProcessTerminationAndHandoverHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $hrmProcessTerminationAndHandoverRequest = new HrmProcessTerminationAndHandoverRequest([
            "userId" => "user1",
            "optUserId" => "user5678",
            "lastWorkDate" => 1704074400000,
            "dismissionReason" => 1,
            "dismissionMemo" => "离职原因备注",
            "aflowHandOverUserId" => "user123",
            "docNoteHandoverUserId" => "user123",
            "dingPanHandoverUserId" => "user123",
            "permissionHandoverUserId" => "user123",
            "directSubordinatesHandoverUserId" => "user123"
        ]);
        try {
            $client->hrmProcessTerminationAndHandoverWithOptions($hrmProcessTerminationAndHandoverRequest, $hrmProcessTerminationAndHandoverHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
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
func CreateClient () (_result *dingtalkhrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrm_1_0.Client{}
  _result, _err = dingtalkhrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrmProcessTerminationAndHandoverHeaders := &dingtalkhrm_1_0.HrmProcessTerminationAndHandoverHeaders{}
  hrmProcessTerminationAndHandoverHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  hrmProcessTerminationAndHandoverRequest := &dingtalkhrm_1_0.HrmProcessTerminationAndHandoverRequest{
    UserId: tea.String("user1"),
    OptUserId: tea.String("user5678"),
    LastWorkDate: tea.Int64(1704074400000),
    DismissionReason: tea.Int32(1),
    DismissionMemo: tea.String("离职原因备注"),
    AflowHandOverUserId: tea.String("user123"),
    DocNoteHandoverUserId: tea.String("user123"),
    DingPanHandoverUserId: tea.String("user123"),
    PermissionHandoverUserId: tea.String("user123"),
    DirectSubordinatesHandoverUserId: tea.String("user123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrmProcessTerminationAndHandoverWithOptions(hrmProcessTerminationAndHandoverRequest, hrmProcessTerminationAndHandoverHeaders, &util.RuntimeOptions{})
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
const dingtalkhrm_1_0 = require('@alicloud/dingtalk/hrm_1_0');
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
    return new dingtalkhrm_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let hrmProcessTerminationAndHandoverHeaders = new dingtalkhrm_1_0.HrmProcessTerminationAndHandoverHeaders({ });
    hrmProcessTerminationAndHandoverHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let hrmProcessTerminationAndHandoverRequest = new dingtalkhrm_1_0.HrmProcessTerminationAndHandoverRequest({
      userId: 'user1',
      optUserId: 'user5678',
      lastWorkDate: 1704074400000,
      dismissionReason: 1,
      dismissionMemo: '离职原因备注',
      aflowHandOverUserId: 'user123',
      docNoteHandoverUserId: 'user123',
      dingPanHandoverUserId: 'user123',
      permissionHandoverUserId: 'user123',
      directSubordinatesHandoverUserId: 'user123',
    });
    try {
      await client.hrmProcessTerminationAndHandoverWithOptions(hrmProcessTerminationAndHandoverRequest, hrmProcessTerminationAndHandoverHeaders, new Util.RuntimeOptions({ }));
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

        /**
         * 使用 Token 初始化账号Client
         * @return Client
         * @throws Exception
         */
        public static AlibabaCloud.SDK.Dingtalkhrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTerminationAndHandoverHeaders hrmProcessTerminationAndHandoverHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTerminationAndHandoverHeaders();
            hrmProcessTerminationAndHandoverHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTerminationAndHandoverRequest hrmProcessTerminationAndHandoverRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTerminationAndHandoverRequest
            {
                UserId = "user1",
                OptUserId = "user5678",
                LastWorkDate = 1704074400000,
                DismissionReason = 1,
                DismissionMemo = "离职原因备注",
                AflowHandOverUserId = "user123",
                DocNoteHandoverUserId = "user123",
                DingPanHandoverUserId = "user123",
                PermissionHandoverUserId = "user123",
                DirectSubordinatesHandoverUserId = "user123",
            };
            try
            {
                client.HrmProcessTerminationAndHandoverWithOptions(hrmProcessTerminationAndHandoverRequest, hrmProcessTerminationAndHandoverHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否离职成功。 |

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
| 400 | suiteCallInvalid | 企业没有开通微应用 | 企业没有开通微应用 |
| 400 | invokeFrequentyly | 调用频繁 | 调用频繁 |
| 400 | invalidParameter | 参数错误 | 参数错误 |
| 400 | noPermission | 无权限访问 | 无权限访问 |
| 400 | empNotExists | 员工不存在 | 员工不存在 |
| 400 | invalidRequest | %s | 请求非法 |
| 400 | businessError | %s | 业务错误 |
| 500 | systemError | 系统异常 | 系统异常 |
