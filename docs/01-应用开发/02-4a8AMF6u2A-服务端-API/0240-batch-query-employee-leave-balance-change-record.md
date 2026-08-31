---
title: "批量查询员工假期余额变更记录"
source_url: "https://open.dingtalk.com/document/development/batch-query-employee-leave-balance-change-record"
namespace: "development"
slug: "batch-query-employee-leave-balance-change-record"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "考勤 > 假期管理 > 批量查询员工假期余额变更记录"
doc_id: "f8PgW8FwWT"
updated_at: "2026-06-02 09:24:54"
---

> Source: https://open.dingtalk.com/document/development/batch-query-employee-leave-balance-change-record
> Path: 应用开发 / 服务端 API / 考勤 > 假期管理 > 批量查询员工假期余额变更记录
> Updated: 2026-06-02 09:24:54

# 批量查询员工假期余额变更记录

调用本接口实现可获取关于某员工的所有假期余额的变更记录，包括假期余额初始化、员工消费额度、假期余额更新记录等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/attendance/vacations/records/query |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_holiday\_readonly-钉钉假期查询的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUserId | String | 是 | 当前企业内拥有OA审批应用权限的管理员的userId，建议传入企业主管理员userId，可调用[获取管理员列表](0068-query-the-administrator-list.md)接口，获取返回参数主管理员`userId`字段。 |
| leaveCode | String | 是 | 假期类型唯一标识，调用[查询假期规则列表](0238-holiday-type-query.md)接口获取`leave_code`参数值。 |
| userIds | Array of String | 是 | 待查询员工userId列表，每次调用最多传50个userId。 |
| pageNumber | Long | 是 | 分页游标：   - 首次查询，该参数传0。 - 非首次查询，根据上一次的偏移量的累积值进行传参。 |
| pageSize | Integer | 是 | 分页偏移量，最大200。 |

### 请求示例

HTTP

```
POST /v1.0/attendance/vacations/records/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "opUserId" : "user01",
  "leaveCode" : "f84a2dxxxx",
  "userIds" : [ "user1" ],
  "pageNumber" : 1,
  "pageSize" : 100
}
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
    public static com.aliyun.dingtalkattendance_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkattendance_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkattendance_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkattendance_1_0.models.GetLeaveRecordsHeaders getLeaveRecordsHeaders = new com.aliyun.dingtalkattendance_1_0.models.GetLeaveRecordsHeaders();
        getLeaveRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkattendance_1_0.models.GetLeaveRecordsRequest getLeaveRecordsRequest = new com.aliyun.dingtalkattendance_1_0.models.GetLeaveRecordsRequest()
                .setOpUserId("user01")
                .setLeaveCode("f84a2dxxxx")
                .setUserIds(java.util.Arrays.asList(
                    "user1"
                ))
                .setPageNumber(1L)
                .setPageSize(100);
        try {
            client.getLeaveRecordsWithOptions(getLeaveRecordsRequest, getLeaveRecordsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.attendance_1_0.client import Client as dingtalkattendance_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.attendance_1_0 import models as dingtalkattendance__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkattendance_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkattendance_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_leave_records_headers = dingtalkattendance__1__0_models.GetLeaveRecordsHeaders()
        get_leave_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_leave_records_request = dingtalkattendance__1__0_models.GetLeaveRecordsRequest(
            op_user_id='user01',
            leave_code='f84a2dxxxx',
            user_ids=[
                'user1'
            ],
            page_number=1,
            page_size=100
        )
        try:
            client.get_leave_records_with_options(get_leave_records_request, get_leave_records_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_leave_records_headers = dingtalkattendance__1__0_models.GetLeaveRecordsHeaders()
        get_leave_records_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_leave_records_request = dingtalkattendance__1__0_models.GetLeaveRecordsRequest(
            op_user_id='user01',
            leave_code='f84a2dxxxx',
            user_ids=[
                'user1'
            ],
            page_number=1,
            page_size=100
        )
        try:
            await client.get_leave_records_with_options_async(get_leave_records_request, get_leave_records_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetLeaveRecordsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vattendance_1_0\Models\GetLeaveRecordsRequest;
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
        $getLeaveRecordsHeaders = new GetLeaveRecordsHeaders([]);
        $getLeaveRecordsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getLeaveRecordsRequest = new GetLeaveRecordsRequest([
            "opUserId" => "user01",
            "leaveCode" => "f84a2dxxxx",
            "userIds" => [
                "user1"
            ],
            "pageNumber" => 1,
            "pageSize" => 100
        ]);
        try {
            $client->getLeaveRecordsWithOptions($getLeaveRecordsRequest, $getLeaveRecordsHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkattendance_1_0  "github.com/alibabacloud-go/dingtalk/attendance_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkattendance_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkattendance_1_0.Client{}
  _result, _err = dingtalkattendance_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getLeaveRecordsHeaders := &dingtalkattendance_1_0.GetLeaveRecordsHeaders{}
  getLeaveRecordsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getLeaveRecordsRequest := &dingtalkattendance_1_0.GetLeaveRecordsRequest{
    OpUserId: tea.String("user01"),
    LeaveCode: tea.String("f84a2dxxxx"),
    UserIds: []*string{tea.String("user1")},
    PageNumber: tea.Int64(1),
    PageSize: tea.Int32(100),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetLeaveRecordsWithOptions(getLeaveRecordsRequest, getLeaveRecordsHeaders, &util.RuntimeOptions{})
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
import dingtalkattendance_1_0, * as $dingtalkattendance_1_0 from '@alicloud/dingtalk/attendance_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkattendance_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkattendance_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getLeaveRecordsHeaders = new $dingtalkattendance_1_0.GetLeaveRecordsHeaders({ });
    getLeaveRecordsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getLeaveRecordsRequest = new $dingtalkattendance_1_0.GetLeaveRecordsRequest({
      opUserId: "user01",
      leaveCode: "f84a2dxxxx",
      userIds: [
        "user1"
      ],
      pageNumber: 1,
      pageSize: 100,
    });
    try {
      await client.getLeaveRecordsWithOptions(getLeaveRecordsRequest, getLeaveRecordsHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkattendance_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkattendance_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetLeaveRecordsHeaders getLeaveRecordsHeaders = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetLeaveRecordsHeaders();
            getLeaveRecordsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetLeaveRecordsRequest getLeaveRecordsRequest = new AlibabaCloud.SDK.Dingtalkattendance_1_0.Models.GetLeaveRecordsRequest
            {
                OpUserId = "user01",
                LeaveCode = "f84a2dxxxx",
                UserIds = new List<string>
                {
                    "user1"
                },
                PageNumber = 1,
                PageSize = 100,
            };
            try
            {
                client.GetLeaveRecordsWithOptions(getLeaveRecordsRequest, getLeaveRecordsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| hasMore | Boolean | 是否存在更多结果。   - **true**：存在 - **false**：不存在 |
| leaveRecords | Array | 假期消费记录列表。 |
| userId | String | 员工userId。 |
| leaveCode | String | 假期类型唯一标识。 |
| recordId | String | 假期消费记录唯一标识。 |
| quotaId | String | 假期额度唯一标识。 |
| calType | String | 计算类型。   - **insert**：新纪录 - **add**：新增 - **delete**：删除 - **update**：更新 - **null**（或者不返回该字段）：请假消耗 |
| startTime | Long | 额度有效期开始时间或请假开始时间，毫秒级时间戳。 |
| endTime | Long | 额度有效期结束时间或请假结束时间，毫秒级时间戳。 |
| leaveViewUnit | String | 显示单位。   - **day**：天 - **hour**：小时 |
| leaveReason | String | 原因。 |
| leaveRecordType | String | 假期记录类型。   - **leave**：请假 - **update**：更新配额 - **modify\_quota**:初始化余额或者更新余额 |
| leaveStatus | String | 请假状态。   - **init**：请假申请中 - **success**：请假并已通过 - **refuse**：请假但被被拒 - **abort**：请假撤销 - **revoke**：请假已通过但是撤销了请假并已同意 |
| recordNumPerDay | Long | 以天计算的消费额度。   - **说明**  假期类型按天计算时，该值不为空且按百分之一天折算。 例如：1000=10天。 |
| recordNumPerHour | Long | 以小时计算的消费额度。   - **说明**  假期类型按小时，计算该值不为空且按百分之一小时折算。例如：1000=10小时。 |
| gmtCreate | Long | 记录创建时间，毫秒级时间戳。 |
| gmtModified | Long | 记录修改时间，毫秒级时间戳。 |
| opUserId | String | 记录的操作人Id。 |
| success | Boolean | 是否正确访问。   - **true**：是 - **false**：不是 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "hasMore" : true,
    "leaveRecords" : [ {
      "userId" : "user1",
      "leaveCode" : "f84a2dxxxx",
      "recordId" : "db1d74xxxxbaa",
      "quotaId" : "db1d74xxxxbaa",
      "calType" : "add",
      "startTime" : 1653851001000,
      "endTime" : 1753851001000,
      "leaveViewUnit" : "day",
      "leaveReason" : "管理员导入",
      "leaveRecordType" : "update",
      "leaveStatus" : "init",
      "recordNumPerDay" : 100,
      "recordNumPerHour" : 100,
      "gmtCreate" : 1653851001000,
      "gmtModified" : 1753851001000,
      "opUserId" : "manage2323"
    } ]
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | leaveOpuserIdIsNotAdmin | 非管理员只能查询本人相关信息 | 非管理员只能查询本人相关信息 |
| 400 | leaveTypeNotFound | 未找到该假期类型 | 未找到该假期类型 |
| 400 | paramterInvalid | 参数错误 | opUserId和userId参数不能为空 |
| 400 | leaveUserIdListMax | 每次最多查询50条记录 | 每次最多查询50个员工userIds |
| 400 | pageIndexIllegal | 分页参数错误 | 分页参数从0开始非负整数 |
| 400 | pageSizeIllegal | 分页大小超过限制 | 分页大小最大200条 |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | leaveOrgIsUsed | 只允许企业接入使用 | 只允许企业接入使用 |
