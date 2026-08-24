---
title: "批量获取员工离职信息"
source_url: "https://open.dingtalk.com/document/development/obtain-resignation-information-of-employees-new-version"
namespace: "development"
slug: "obtain-resignation-information-of-employees-new-version"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工管理 > 批量获取员工离职信息"
doc_id: "ILaPL4GaKQ"
updated_at: "2026-06-04 19:10:27"
---

> Source: https://open.dingtalk.com/document/development/obtain-resignation-information-of-employees-new-version
> Path: 应用开发 / 服务端API / 智能人事 > 员工管理 > 批量获取员工离职信息
> Updated: 2026-06-04 19:10:27

# 批量获取员工离职信息

根据用户userId，批量查询员工的离职信息，如离职人员的部门ID、离职主动原因和被动原因等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/employees/dimissionInfos |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_read\_user-智能人事个人信息读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userIdList | Array of String | 是 | 员工userId列表，最大长度50。 |

### 请求示例

HTTP

```
GET /v1.0/hrm/employees/dimissionInfos?userIdList=["\"123\""] HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:"3b1e371d2cb136f684367e05097d2"
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkhrm_1_0.*;
import com.aliyun.dingtalkhrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        QueryHrmEmployeeDismissionInfoHeaders queryHrmEmployeeDismissionInfoHeaders = new QueryHrmEmployeeDismissionInfoHeaders();
        queryHrmEmployeeDismissionInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryHrmEmployeeDismissionInfoRequest queryHrmEmployeeDismissionInfoRequest = new QueryHrmEmployeeDismissionInfoRequest()
                .setUserIdList(java.util.Arrays.asList(
                    null
                ));
        try {
            client.queryHrmEmployeeDismissionInfoWithOptions(queryHrmEmployeeDismissionInfoRequest, queryHrmEmployeeDismissionInfoHeaders, new RuntimeOptions());
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
        query_hrm_employee_dismission_info_headers = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoHeaders()
        query_hrm_employee_dismission_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_hrm_employee_dismission_info_request = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoRequest(
            user_id_list=[
                None
            ]
        )
        try:
            client.query_hrm_employee_dismission_info_with_options(query_hrm_employee_dismission_info_request, query_hrm_employee_dismission_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_hrm_employee_dismission_info_headers = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoHeaders()
        query_hrm_employee_dismission_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_hrm_employee_dismission_info_request = dingtalkhrm__1__0_models.QueryHrmEmployeeDismissionInfoRequest(
            user_id_list=[
                None
            ]
        )
        try:
            await client.query_hrm_employee_dismission_info_with_options_async(query_hrm_employee_dismission_info_request, query_hrm_employee_dismission_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryHrmEmployeeDismissionInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\QueryHrmEmployeeDismissionInfoRequest;
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
        $queryHrmEmployeeDismissionInfoHeaders = new QueryHrmEmployeeDismissionInfoHeaders([]);
        $queryHrmEmployeeDismissionInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryHrmEmployeeDismissionInfoRequest = new QueryHrmEmployeeDismissionInfoRequest([
            "userIdList" => [
                null
            ]
        ]);
        try {
            $client->queryHrmEmployeeDismissionInfoWithOptions($queryHrmEmployeeDismissionInfoRequest, $queryHrmEmployeeDismissionInfoHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  queryHrmEmployeeDismissionInfoHeaders := &dingtalkhrm_1_0.QueryHrmEmployeeDismissionInfoHeaders{}
  queryHrmEmployeeDismissionInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryHrmEmployeeDismissionInfoRequest := &dingtalkhrm_1_0.QueryHrmEmployeeDismissionInfoRequest{
    UserIdList: []*string{nil},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryHrmEmployeeDismissionInfoWithOptions(queryHrmEmployeeDismissionInfoRequest, queryHrmEmployeeDismissionInfoHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryHrmEmployeeDismissionInfoHeaders = new $dingtalkhrm_1_0.QueryHrmEmployeeDismissionInfoHeaders({ });
    queryHrmEmployeeDismissionInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryHrmEmployeeDismissionInfoRequest = new $dingtalkhrm_1_0.QueryHrmEmployeeDismissionInfoRequest({
      userIdList: [
        null
      ],
    });
    try {
      await client.queryHrmEmployeeDismissionInfoWithOptions(queryHrmEmployeeDismissionInfoRequest, queryHrmEmployeeDismissionInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryHrmEmployeeDismissionInfoHeaders queryHrmEmployeeDismissionInfoHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryHrmEmployeeDismissionInfoHeaders();
            queryHrmEmployeeDismissionInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryHrmEmployeeDismissionInfoRequest queryHrmEmployeeDismissionInfoRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.QueryHrmEmployeeDismissionInfoRequest
            {
                UserIdList = new List<null>
                {
                    null
                },
            };
            try
            {
                client.QueryHrmEmployeeDismissionInfoWithOptions(queryHrmEmployeeDismissionInfoRequest, queryHrmEmployeeDismissionInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkhrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

Alibabacloud_Dingtalkhrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkhrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkhrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkhrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkhrm_1_0::QueryHrmEmployeeDismissionInfoHeaders> queryHrmEmployeeDismissionInfoHeaders = make_shared<Alibabacloud_Dingtalkhrm_1_0::QueryHrmEmployeeDismissionInfoHeaders>();
  queryHrmEmployeeDismissionInfoHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkhrm_1_0::QueryHrmEmployeeDismissionInfoRequest> queryHrmEmployeeDismissionInfoRequest = make_shared<Alibabacloud_Dingtalkhrm_1_0::QueryHrmEmployeeDismissionInfoRequest>(map<string, boost::any>({
    {"userIdList", boost::any(vector<nullptr>({
      nullptr
    }))}
  }));
  try {
    client->queryHrmEmployeeDismissionInfoWithOptions(queryHrmEmployeeDismissionInfoRequest, queryHrmEmployeeDismissionInfoHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| result | Array | 返回结果。 |
| userId | String | 员工userId。 |
| lastWorkDay | Long | 最后工作日。 |
| deptList | Array | 离职部门列表。 |
| dept\_path | String | 部门路径。 |
| dept\_id | Long | 部门ID。 |
| reasonMemo | String | 离职原因备注。 |
| preStatus | Integer | 离职前工作状态：   - 1：待入职； - 2：试用期； - 3：正式。 |
| handoverUserId | String | 离职交接人的userId。 |
| status | Integer | 离职状态：   - 1：待离职。 - 2：已离职。 - 3：非待离职或非已离职。 - 4：已提交离职审批单，审批单暂未通过。 |
| mainDeptName | String | 离职前主部门名称。 |
| mainDeptId | Long | 离职前主部门ID。 |
| voluntaryReason | Array of String | 主动原因。 |
| passiveReason | Array of String | 被动原因。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "userId" : "123",
    "lastWorkDay" : 1534569419008,
    "deptList" : [ {
      "dept_path" : "门诊部-门诊外科",
      "dept_id" : 1234
    } ],
    "reasonMemo" : "世界太大想去看看",
    "preStatus" : 1,
    "handoverUserId" : "123456",
    "status" : 1,
    "mainDeptName" : "门诊外科",
    "mainDeptId" : 1234,
    "voluntaryReason" : [ "个人原因" ],
    "passiveReason" : [ "无法胜任工作" ]
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 员工 id列表大小不在[1,50]范围 | 员工 id列表大小不在[1,50]范围 |
| 400 | corpNotOpenHrm | 企业未开通通智能人事 | 企业未开通通智能人事 |
| 500 | systemError | 系统异常 | 系统异常 |
