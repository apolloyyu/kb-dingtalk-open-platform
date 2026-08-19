---
title: "同步市内用车申请单"
source_url: "https://open.dingtalk.com/document/development/synchronize-third-party-city-vehicle-approval-form"
namespace: "development"
slug: "synchronize-third-party-city-vehicle-approval-form"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 市内用车申请 > 同步市内用车申请单"
doc_id: "AFesbmIGZN"
updated_at: "2026-01-29 14:31:12"
---

> Source: https://open.dingtalk.com/document/development/synchronize-third-party-city-vehicle-approval-form
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 市内用车申请 > 同步市内用车申请单
> Updated: 2026-01-29 14:31:12

# 同步市内用车申请单

通过此接口同步市内用车申请单据至阿里商旅。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/alitrip/cityCarApprovals |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip\_write-阿里商旅专用写入权限点 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cause | String | 是 | 出差事由，用于说明本次市内用车的具体原因。 |
| city | String | 是 | 用车城市，填写城市名称，如“杭州”。 |
| corpId | String | 是 | 第三方企业的corpid，用于标识企业身份。 |
| date | String | 是 | 用车时间，按天管控，比如传值2021-03-18 20:26:56表示2021-03-18当天可用车，跨天情况配合finishedDate参数使用 |
| projectCode | String | 否 | 审批单关联的项目code。 |
| projectName | String | 否 | 审批单关联的项目名。 |
| status | Long | 是 | 审批单状态：   - **0**：申请 - **1**：同意 - **2**：拒绝 |
| thirdPartApplyId | String | 是 | 三方审批单ID。 |
| thirdPartCostCenterId | String | 是 | 审批单关联的三方成本中心ID。 |
| thirdPartInvoiceId | String | 是 | 审批单关联的三方发票抬头ID。 |
| timesTotal | Long | 是 | 审批单可用总次数。 |
| timesType | Long | 是 | 审批单可用次数类型：   - **1**：次数不限制 - **2**：用户可指定次数 - **3**：管理员限制次数   如果企业没有限制审批单使用次数的需求，这个参数传1(次数不限制)，同时timesTotal和timesUsed都传0即可 |
| timesUsed | Long | 是 | 审批单已用次数。 |
| title | String | 是 | 审批单标题。 |
| userId | String | 是 | 发起审批的第三方员工ID。 |
| finishedDate | String | 否 | 用车截止时间，按天管控，比如date传值2021-03-18 20:26:56、finishedDate传值2021-03-30 20:26:56表示2021-03-18(含)到2021-03-30(含)之间可用车，该参数不传值情况使用date作为用车截止时间； |

### 请求示例

HTTP

```
POST /v1.0/alitrip/cityCarApprovals HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1
Content-Type:application/json

{
  "cause" : "杭州出差",
  "city" : "杭州",
  "corpId" : "corpx",
  "date" : "2021-03-18 20:26:56",
  "projectCode" : "projectx",
  "projectName" : "项目x",
  "status" : 0,
  "thirdPartApplyId" : "apply1",
  "thirdPartCostCenterId" : "costcenter1",
  "thirdPartInvoiceId" : "invoice1",
  "timesTotal" : 1,
  "timesType" : 3,
  "timesUsed" : 0,
  "title" : "杭州出差",
  "userId" : "user1",
  "finishedDate" : "2021-03-30 20:26:56"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkalitrip_1_0.*;
import com.aliyun.dingtalkalitrip_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkalitrip_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkalitrip_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkalitrip_1_0.Client client = Sample.createClient();
        AddCityCarApplyHeaders addCityCarApplyHeaders = new AddCityCarApplyHeaders();
        addCityCarApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddCityCarApplyRequest addCityCarApplyRequest = new AddCityCarApplyRequest()
                .setCause("杭州出差")
                .setCity("杭州")
                .setCorpId("corpx")
                .setDate("2021-03-18 20:26:56")
                .setProjectCode("projectx")
                .setProjectName("项目x")
                .setStatus(0L)
                .setThirdPartApplyId("apply1")
                .setThirdPartCostCenterId("costcenter1")
                .setThirdPartInvoiceId("invoice1")
                .setTimesTotal(1L)
                .setTimesType(3L)
                .setTimesUsed(0L)
                .setTitle("杭州出差")
                .setUserId("user1")
                .setFinishedDate("2021-03-30 20:26:56");
        try {
            client.addCityCarApplyWithOptions(addCityCarApplyRequest, addCityCarApplyHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.alitrip_1_0.client import Client as dingtalkalitrip_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.alitrip_1_0 import models as dingtalkalitrip__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkalitrip_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkalitrip_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_city_car_apply_headers = dingtalkalitrip__1__0_models.AddCityCarApplyHeaders()
        add_city_car_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_city_car_apply_request = dingtalkalitrip__1__0_models.AddCityCarApplyRequest(
            cause='杭州出差',
            city='杭州',
            corp_id='corpx',
            date='2021-03-18 20:26:56',
            project_code='projectx',
            project_name='项目x',
            status=0,
            third_part_apply_id='apply1',
            third_part_cost_center_id='costcenter1',
            third_part_invoice_id='invoice1',
            times_total=1,
            times_type=3,
            times_used=0,
            title='杭州出差',
            user_id='user1',
            finished_date='2021-03-30 20:26:56'
        )
        try:
            client.add_city_car_apply_with_options(add_city_car_apply_request, add_city_car_apply_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_city_car_apply_headers = dingtalkalitrip__1__0_models.AddCityCarApplyHeaders()
        add_city_car_apply_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_city_car_apply_request = dingtalkalitrip__1__0_models.AddCityCarApplyRequest(
            cause='杭州出差',
            city='杭州',
            corp_id='corpx',
            date='2021-03-18 20:26:56',
            project_code='projectx',
            project_name='项目x',
            status=0,
            third_part_apply_id='apply1',
            third_part_cost_center_id='costcenter1',
            third_part_invoice_id='invoice1',
            times_total=1,
            times_type=3,
            times_used=0,
            title='杭州出差',
            user_id='user1',
            finished_date='2021-03-30 20:26:56'
        )
        try:
            await client.add_city_car_apply_with_options_async(add_city_car_apply_request, add_city_car_apply_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\AddCityCarApplyHeaders;
use AlibabaCloud\SDK\Dingtalk\Valitrip_1_0\Models\AddCityCarApplyRequest;
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
        $addCityCarApplyHeaders = new AddCityCarApplyHeaders([]);
        $addCityCarApplyHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addCityCarApplyRequest = new AddCityCarApplyRequest([
            "cause" => "杭州出差",
            "city" => "杭州",
            "corpId" => "corpx",
            "date" => "2021-03-18 20:26:56",
            "projectCode" => "projectx",
            "projectName" => "项目x",
            "status" => 0,
            "thirdPartApplyId" => "apply1",
            "thirdPartCostCenterId" => "costcenter1",
            "thirdPartInvoiceId" => "invoice1",
            "timesTotal" => 1,
            "timesType" => 3,
            "timesUsed" => 0,
            "title" => "杭州出差",
            "userId" => "user1",
            "finishedDate" => "2021-03-30 20:26:56"
        ]);
        try {
            $client->addCityCarApplyWithOptions($addCityCarApplyRequest, $addCityCarApplyHeaders, new RuntimeOptions([]));
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
  dingtalkalitrip_1_0  "github.com/alibabacloud-go/dingtalk/alitrip_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkalitrip_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkalitrip_1_0.Client{}
  _result, _err = dingtalkalitrip_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addCityCarApplyHeaders := &dingtalkalitrip_1_0.AddCityCarApplyHeaders{}
  addCityCarApplyHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addCityCarApplyRequest := &dingtalkalitrip_1_0.AddCityCarApplyRequest{
    Cause: tea.String("杭州出差"),
    City: tea.String("杭州"),
    CorpId: tea.String("corpx"),
    Date: tea.String("2021-03-18 20:26:56"),
    ProjectCode: tea.String("projectx"),
    ProjectName: tea.String("项目x"),
    Status: tea.Int64(0),
    ThirdPartApplyId: tea.String("apply1"),
    ThirdPartCostCenterId: tea.String("costcenter1"),
    ThirdPartInvoiceId: tea.String("invoice1"),
    TimesTotal: tea.Int64(1),
    TimesType: tea.Int64(3),
    TimesUsed: tea.Int64(0),
    Title: tea.String("杭州出差"),
    UserId: tea.String("user1"),
    FinishedDate: tea.String("2021-03-30 20:26:56"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddCityCarApplyWithOptions(addCityCarApplyRequest, addCityCarApplyHeaders, &util.RuntimeOptions{})
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
import dingtalkalitrip_1_0, * as $dingtalkalitrip_1_0 from '@alicloud/dingtalk/alitrip_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkalitrip_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkalitrip_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addCityCarApplyHeaders = new $dingtalkalitrip_1_0.AddCityCarApplyHeaders({ });
    addCityCarApplyHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let addCityCarApplyRequest = new $dingtalkalitrip_1_0.AddCityCarApplyRequest({
      cause: "杭州出差",
      city: "杭州",
      corpId: "corpx",
      date: "2021-03-18 20:26:56",
      projectCode: "projectx",
      projectName: "项目x",
      status: 0,
      thirdPartApplyId: "apply1",
      thirdPartCostCenterId: "costcenter1",
      thirdPartInvoiceId: "invoice1",
      timesTotal: 1,
      timesType: 3,
      timesUsed: 0,
      title: "杭州出差",
      userId: "user1",
      finishedDate: "2021-03-30 20:26:56",
    });
    try {
      await client.addCityCarApplyWithOptions(addCityCarApplyRequest, addCityCarApplyHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.AddCityCarApplyHeaders addCityCarApplyHeaders = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.AddCityCarApplyHeaders();
            addCityCarApplyHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.AddCityCarApplyRequest addCityCarApplyRequest = new AlibabaCloud.SDK.Dingtalkalitrip_1_0.Models.AddCityCarApplyRequest
            {
                Cause = "杭州出差",
                City = "杭州",
                CorpId = "corpx",
                Date = "2021-03-18 20:26:56",
                ProjectCode = "projectx",
                ProjectName = "项目x",
                Status = 0,
                ThirdPartApplyId = "apply1",
                ThirdPartCostCenterId = "costcenter1",
                ThirdPartInvoiceId = "invoice1",
                TimesTotal = 1,
                TimesType = 3,
                TimesUsed = 0,
                Title = "杭州出差",
                UserId = "user1",
                FinishedDate = "2021-03-30 20:26:56",
            };
            try
            {
                client.AddCityCarApplyWithOptions(addCityCarApplyRequest, addCityCarApplyHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkalitrip__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkalitrip_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkalitrip_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::Client> client = make_shared<Alibabacloud_Dingtalkalitrip_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::AddCityCarApplyHeaders> addCityCarApplyHeaders = make_shared<Alibabacloud_Dingtalkalitrip_1_0::AddCityCarApplyHeaders>();
  addCityCarApplyHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkalitrip_1_0::AddCityCarApplyRequest> addCityCarApplyRequest = make_shared<Alibabacloud_Dingtalkalitrip_1_0::AddCityCarApplyRequest>(map<string, boost::any>({
    {"cause", boost::any(string("杭州出差"))},
    {"city", boost::any(string("杭州"))},
    {"corpId", boost::any(string("corpx"))},
    {"date", boost::any(string("2021-03-18 20:26:56"))},
    {"projectCode", boost::any(string("projectx"))},
    {"projectName", boost::any(string("项目x"))},
    {"status", boost::any(0)},
    {"thirdPartApplyId", boost::any(string("apply1"))},
    {"thirdPartCostCenterId", boost::any(string("costcenter1"))},
    {"thirdPartInvoiceId", boost::any(string("invoice1"))},
    {"timesTotal", boost::any(1)},
    {"timesType", boost::any(3)},
    {"timesUsed", boost::any(0)},
    {"title", boost::any(string("杭州出差"))},
    {"userId", boost::any(string("user1"))},
    {"finishedDate", boost::any(string("2021-03-30 20:26:56"))}
  }));
  try {
    client->addCityCarApplyWithOptions(addCityCarApplyRequest, addCityCarApplyHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| applyId | Long | 商旅内部审批单ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "applyId" : 1
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
