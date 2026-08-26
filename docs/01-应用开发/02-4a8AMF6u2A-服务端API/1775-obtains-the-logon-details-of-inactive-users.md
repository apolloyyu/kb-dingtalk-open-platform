---
title: "获取未活跃用户登录明细"
source_url: "https://open.dingtalk.com/document/development/obtains-the-logon-details-of-inactive-users"
namespace: "development"
slug: "obtains-the-logon-details-of-inactive-users"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据 > 获取未活跃用户登录明细"
doc_id: "1f3Nj4I55U"
updated_at: "2025-10-09 18:08:18"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-logon-details-of-inactive-users
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 数据目录 > 数据统计 > 企业其他数据 > 获取未活跃用户登录明细
> Updated: 2025-10-09 18:08:18

# 获取未活跃用户登录明细

调用本接口未活跃用户登录明细统计信息。

> **[!IMPORTANT]**
>
> 1. 为了更好支持组织对钉钉数据分析和管理的需求，钉钉数据资产平台将统一所有数据资产相关的产品和服务，从数据层、功能层、业务层做升级，提供更好的服务体验。为此，我们将数据资产类 OpenAPI 接口的使用路径和产品定位做了调整，本开发者文档中所述 OpenAPI 接口及 60 个其他的[数据资产类OpenAPI](https://open.dingtalk.com/document/dataservice/data-asset-interface-adjustment-description)接口，已于 2023 年 9 月 1 日**关闭开发者后台应用开发的权限申请入口**，客户可以通过[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)获取相应的数据服务。
> 2. 本文档已于 2023 年 9 月 1 日迁移至历史文档（不推荐）目录，且本接口仅保持现有功能，不再新增支持其他能力，说明如下：
>
>    - 如果未使用本接口，推荐使用[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。
>    - 如果已使用本接口，建议您根据自身实际情况评估是否切换至[钉钉数据资产平台](https://open.dingtalk.com/document/dataservice/overview)。

> **[!NOTE]**
>
> 用本接口前请务必完成接口权限申请，详情请参考[添加接口调用权限](https://open.dingtalk.com/document/orgapp/add-api-permission)和[开发须知](https://open.dingtalk.com/document/orgapp/before-you-start)。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | 钉钉数据产品权限包 | **[!IMPORTANT]**  暂不支持新增申请。 |
| 第三方企业应用 | 暂不支持 | 钉钉数据产品权限包 | 暂不支持 |
| 第三方个人应用 | 暂不支持 | 钉钉数据产品权限包 | 暂不支持 |

## 请求方法

```
POST /v1.0/exclusive/inactives/users/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "statDate" : "String",
  "pageNumber" : Long,
  "pageSize" : Long,
  "deptIds" : [ "String" ]
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| statDate | String | 是 | 查询时间，日期格式为yyyyMMdd。 |
| pageNumber | Long | 是 | 分页页码。 |
| pageSize | Long | 是 | 分页大小。 |
| deptIds | Array of String | 否 | 部门ID列表。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| dataList | Array of Object | 指标数据列表。  **[!NOTE]**  指标数据为Map类型，指标值的取值key为指标ID\_指标周期，例如：4001\_DAY。 |
| metaList | Array | 指标元数据列表，包括指标ID、指标名称、指标周期、指标口径等信息。 |
| kpiId | String | 指标ID。 |
| kpiName | String | 指标名称。 |
| unit | String | 指标单位。 |
| kpiCaliber | String | 指标口径。 |
| period | String | 指标周期。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/exclusive/inactives/users/query HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:85dd6axxx
Content-Type:application/json

{
  "statDate" : "20210620",
  "pageNumber" : 1,
  "pageSize" : 10,
  "deptIds" : [ "10051xxxx" ]
}
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
        GetInActiveUserListHeaders getInActiveUserListHeaders = new GetInActiveUserListHeaders();
        getInActiveUserListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetInActiveUserListRequest getInActiveUserListRequest = new GetInActiveUserListRequest()
                .setStatDate("20210620")
                .setPageNumber(1L)
                .setPageSize(10L)
                .setDeptIds(java.util.Arrays.asList(
                    "10051xxxx"
                ));
        try {
            client.getInActiveUserListWithOptions(getInActiveUserListRequest, getInActiveUserListHeaders, new RuntimeOptions());
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
        get_in_active_user_list_headers = dingtalkexclusive__1__0_models.GetInActiveUserListHeaders()
        get_in_active_user_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_in_active_user_list_request = dingtalkexclusive__1__0_models.GetInActiveUserListRequest(
            stat_date='20210620',
            page_number=1,
            page_size=10,
            dept_ids=[
                '10051xxxx'
            ]
        )
        try:
            client.get_in_active_user_list_with_options(get_in_active_user_list_request, get_in_active_user_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_in_active_user_list_headers = dingtalkexclusive__1__0_models.GetInActiveUserListHeaders()
        get_in_active_user_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_in_active_user_list_request = dingtalkexclusive__1__0_models.GetInActiveUserListRequest(
            stat_date='20210620',
            page_number=1,
            page_size=10,
            dept_ids=[
                '10051xxxx'
            ]
        )
        try:
            await client.get_in_active_user_list_with_options_async(get_in_active_user_list_request, get_in_active_user_list_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetInActiveUserListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetInActiveUserListRequest;
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
        $getInActiveUserListHeaders = new GetInActiveUserListHeaders([]);
        $getInActiveUserListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getInActiveUserListRequest = new GetInActiveUserListRequest([
            "statDate" => "20210620",
            "pageNumber" => 1,
            "pageSize" => 10,
            "deptIds" => [
                "10051xxxx"
            ]
        ]);
        try {
            $client->getInActiveUserListWithOptions($getInActiveUserListRequest, $getInActiveUserListHeaders, new RuntimeOptions([]));
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

  getInActiveUserListHeaders := &dingtalkexclusive_1_0.GetInActiveUserListHeaders{}
  getInActiveUserListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getInActiveUserListRequest := &dingtalkexclusive_1_0.GetInActiveUserListRequest{
    StatDate: tea.String("20210620"),
    PageNumber: tea.Int64(1),
    PageSize: tea.Int64(10),
    DeptIds: []*string{tea.String("10051xxxx")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetInActiveUserListWithOptions(getInActiveUserListRequest, getInActiveUserListHeaders, &util.RuntimeOptions{})
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
    let getInActiveUserListHeaders = new $dingtalkexclusive_1_0.GetInActiveUserListHeaders({ });
    getInActiveUserListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getInActiveUserListRequest = new $dingtalkexclusive_1_0.GetInActiveUserListRequest({
      statDate: "20210620",
      pageNumber: 1,
      pageSize: 10,
      deptIds: [
        "10051xxxx"
      ],
    });
    try {
      await client.getInActiveUserListWithOptions(getInActiveUserListRequest, getInActiveUserListHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetInActiveUserListHeaders getInActiveUserListHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetInActiveUserListHeaders();
            getInActiveUserListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetInActiveUserListRequest getInActiveUserListRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetInActiveUserListRequest
            {
                StatDate = "20210620",
                PageNumber = 1,
                PageSize = 10,
                DeptIds = new List<string>
                {
                    "10051xxxx"
                },
            };
            try
            {
                client.GetInActiveUserListWithOptions(getInActiveUserListRequest, getInActiveUserListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkexclusive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkexclusive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkexclusive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkexclusive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::GetInActiveUserListHeaders> getInActiveUserListHeaders = make_shared<Alibabacloud_Dingtalkexclusive_1_0::GetInActiveUserListHeaders>();
  getInActiveUserListHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkexclusive_1_0::GetInActiveUserListRequest> getInActiveUserListRequest = make_shared<Alibabacloud_Dingtalkexclusive_1_0::GetInActiveUserListRequest>(map<string, boost::any>({
    {"statDate", boost::any(string("20210620"))},
    {"pageNumber", boost::any(1)},
    {"pageSize", boost::any(10)},
    {"deptIds", boost::any(vector<string>({
      "10051xxxx"
    }))}
  }));
  try {
    client->getInActiveUserListWithOptions(getInActiveUserListRequest, getInActiveUserListHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "metaList" : [ {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14001",
    "kpiCaliber" : "未活跃员工工号",
    "kpiName" : "未活跃员工工号"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14002",
    "kpiCaliber" : "未活跃员工姓名",
    "kpiName" : "未活跃员工姓名"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14003",
    "kpiCaliber" : "未活跃员工部门名称",
    "kpiName" : "未活跃员工部门名称"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14004",
    "kpiCaliber" : "未活跃员工用户ID",
    "kpiName" : "未活跃员工用户ID"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14005",
    "kpiCaliber" : "最近1天是否登录【Y/N】",
    "kpiName" : "最近1天是否登录"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14006",
    "kpiCaliber" : "最近7天是否登录【Y/N】",
    "kpiName" : "最近7天是否登录"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14007",
    "kpiCaliber" : "最近14天是否登录【Y/N】",
    "kpiName" : "最近14天是否登录"
  }, {
    "unit" : "",
    "period" : "DAY",
    "kpiId" : "14008",
    "kpiCaliber" : "最近30天是否登录【Y/N】",
    "kpiName" : "最近30天是否登录"
  } ],
  "dataList" : [ {
    "14001_DAY" : "0102276329xxxxxx",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "张x",
    "14007_DAY" : "Y",
    "14004_DAY" : "24832xxx",
    "corp_id" : "ding29f62cbb01638d68ffe934787xxxxxx",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "0104440938191508xxxxxx",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "N",
    "14002_DAY" : "333333",
    "14007_DAY" : "N",
    "14004_DAY" : "179187xxxxx",
    "corp_id" : "ding29f62cbb01638d68ffe9347875xxxxxx",
    "14005_DAY" : "N",
    "14006_DAY" : "N"
  }, {
    "14001_DAY" : "010601632750xxxxxx",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "易画",
    "14007_DAY" : "Y",
    "14004_DAY" : "182541xxxx",
    "corp_id" : "ding29f62cbb01638d68ffe9347875xxxxxx",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "0108204129528xxxxx",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "海华1",
    "14007_DAY" : "Y",
    "14004_DAY" : "18798xxxxx2",
    "corp_id" : "ding29f62cbb01638d68ffe9347875xxxxxx",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "01094xxxxxx3473",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "炎伏",
    "14007_DAY" : "Y",
    "14004_DAY" : "999999",
    "corp_id" : "ding29f62cbb01638d68xxxxxx753d9884",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "01114361xxxxxxx0296",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "姚娜",
    "14007_DAY" : "Y",
    "14004_DAY" : "399971",
    "corp_id" : "ding29f62cbb01xxxxxx93478753d9884",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "0111681xxxxxx26879",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "千玺",
    "14007_DAY" : "Y",
    "14004_DAY" : "19000000261",
    "corp_id" : "ding29f62cbb016xxxxxxxx78753d9884",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "011229xxxxxxx1172017",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "那年",
    "14007_DAY" : "Y",
    "14004_DAY" : "1900000057",
    "corp_id" : "ding29f62cbb01638d6xxxxxxx753d9884",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "0118xxxxxx833359",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "明天宝",
    "14007_DAY" : "Y",
    "14004_DAY" : "00000075",
    "corp_id" : "ding29f62cbb01638xxxxxxxx478753d9884",
    "14005_DAY" : "Y",
    "14006_DAY" : "Y"
  }, {
    "14001_DAY" : "0119190000000061403",
    "stat_date" : "20211102",
    "14003_DAY" : "专属钉钉SDK测试组织1",
    "14008_DAY" : "Y",
    "14002_DAY" : "茶云拉",
    "14007_DAY" : "Y",
    "14004_DAY" : "2100000066",
    "corp_id" : "ding29f62cbbxxxxxxxxxx78753d9884",
    "14005_DAY" : "N",
    "14006_DAY" : "Y"
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | IdempotentParameterMismatch | The request uses the same client token as a previous, but non-identical request. Do not reuse a client token with different requests, unless the requests are identical. | client token不合法。 |
| 500 | unknownError | 未知错误 | 未知错误 |
| 500 | statDate.format.iserror | statDate请求参数格式不正确，正确格式：yyyyMMdd | statDate请求参数格式不正确，正确格式：yyyyMMdd |
| 500 | orgId.is.null | orgId请求参数为空 | orgId请求参数为空 |
| 500 | systemError | 系统异常 | 系统异常，请稍后重试 |
| 500 | serviceId.is.null | serviceId为空 | serviceId为空 |
| 500 | service.meta.isNull | service meta信息为空 | service meta信息为空 |
| 500 | statDate.is.null | statDate请求参数为空 | statDate请求参数为空 |
