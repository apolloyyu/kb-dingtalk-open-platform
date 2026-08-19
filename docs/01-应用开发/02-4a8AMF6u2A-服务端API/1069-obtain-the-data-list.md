---
title: "获取数据列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-data-list"
namespace: "development"
slug: "obtain-the-data-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 数据 > 获取数据列表"
doc_id: "mNfNgceNve"
updated_at: "2026-01-29 14:19:41"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-data-list
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 数据 > 获取数据列表
> Updated: 2026-01-29 14:19:41

# 获取数据列表

调用本接口获取各种单据的列表数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/data |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Jzcrm.Common.ReadWrite-金智CRM数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| datatype | String | 是 | 数据类型。 |
| page | Long | 是 | 页码。 |
| pagesize | Long | 是 | 分页条数。 |

### 请求示例

HTTP

```
GET /v1.0/jzcrm/data?datatype=150&page=1&pagesize=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961ef7e2f3639zv1jjr76df97e21c
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkjzcrm_1_0.*;
import com.aliyun.dingtalkjzcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkjzcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkjzcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkjzcrm_1_0.Client client = Sample.createClient();
        GetDataListHeaders getDataListHeaders = new GetDataListHeaders();
        getDataListHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetDataListRequest getDataListRequest = new GetDataListRequest()
                .setDatatype("150")
                .setPage(1L)
                .setPagesize(10L);
        try {
            client.getDataListWithOptions(getDataListRequest, getDataListHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.jzcrm_1_0.client import Client as dingtalkjzcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.jzcrm_1_0 import models as dingtalkjzcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkjzcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkjzcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_data_list_headers = dingtalkjzcrm__1__0_models.GetDataListHeaders()
        get_data_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_data_list_request = dingtalkjzcrm__1__0_models.GetDataListRequest(
            datatype='150',
            page=1,
            pagesize=10
        )
        try:
            client.get_data_list_with_options(get_data_list_request, get_data_list_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_data_list_headers = dingtalkjzcrm__1__0_models.GetDataListHeaders()
        get_data_list_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_data_list_request = dingtalkjzcrm__1__0_models.GetDataListRequest(
            datatype='150',
            page=1,
            pagesize=10
        )
        try:
            await client.get_data_list_with_options_async(get_data_list_request, get_data_list_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\GetDataListHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\GetDataListRequest;
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
        $getDataListHeaders = new GetDataListHeaders([]);
        $getDataListHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getDataListRequest = new GetDataListRequest([
            "datatype" => "150",
            "page" => 1,
            "pagesize" => 10
        ]);
        try {
            $client->getDataListWithOptions($getDataListRequest, $getDataListHeaders, new RuntimeOptions([]));
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
  dingtalkjzcrm_1_0  ""github.com/alibabacloud-go/dingtalk/jzcrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkjzcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkjzcrm_1_0.Client{}
  _result, _err = dingtalkjzcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getDataListHeaders := &dingtalkjzcrm_1_0.GetDataListHeaders{}
  getDataListHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getDataListRequest := &dingtalkjzcrm_1_0.GetDataListRequest{
    Datatype: tea.String("150"),
    Page: tea.Int64(1),
    Pagesize: tea.Int64(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetDataListWithOptions(getDataListRequest, getDataListHeaders, &util.RuntimeOptions{})
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
import dingtalkjzcrm_1_0, * as $dingtalkjzcrm_1_0 from '"@alicloud/dingtalk/jzcrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkjzcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkjzcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getDataListHeaders = new $dingtalkjzcrm_1_0.GetDataListHeaders({ });
    getDataListHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getDataListRequest = new $dingtalkjzcrm_1_0.GetDataListRequest({
      datatype: "150",
      page: 1,
      pagesize: 10,
    });
    try {
      await client.getDataListWithOptions(getDataListRequest, getDataListHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataListHeaders getDataListHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataListHeaders();
            getDataListHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataListRequest getDataListRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataListRequest
            {
                Datatype = "150",
                Page = 1,
                Pagesize = 10,
            };
            try
            {
                client.GetDataListWithOptions(getDataListRequest, getDataListHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkjzcrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkjzcrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkjzcrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::GetDataListHeaders> getDataListHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::GetDataListHeaders>();
  getDataListHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::GetDataListRequest> getDataListRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::GetDataListRequest>(map<string, boost::any>({
    {"datatype", boost::any(string("150"))},
    {"page", boost::any(1)},
    {"pagesize", boost::any(10)}
  }));
  try {
    client->getDataListWithOptions(getDataListRequest, getDataListHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| data | Array | 数据列表。 |
| detail | Map<String, String> | 数据列表。 |
| dataname | Map<String, String> | 字段明细。 |
| page | Long | 当前页码。 |
| pageSize | Long | 分页条数。 |
| totalCount | Long | 总条数。 |
| time | String | 响应时间。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "time" : "2021-06-01 11:06:56",
  "success" : true,
  "errcode" : "0",
  "errmsg" : "",
  "totalCount" : "82",
  "page" : "1",
  "pageSize" : "1",
  "dataname" : {
    "kh_id" : "ID",
    "kh_name" : "客户名称",
    "kh_shortname" : "助记简称",
    "kh_country" : "国家地区",
    "kh_province" : "省份",
    "kh_city" : "城市",
    "kh_coaddress" : "单位地址",
    "kh_type" : "种类",
    "kh_handset" : "手机",
    "kh_worktel" : "工作电话",
    "kh_remark" : "备注",
    "data_userid" : "所属员工",
    "addtime" : "创建时间"
  },
  "data" : [ {
    "detail" : {
      "kh_id" : "1",
      "kh_name" : "客户123456",
      "kh_shortname" : "客户",
      "kh_country" : "中国",
      "kh_province" : "山东省",
      "kh_city" : "青岛市",
      "kh_coaddress" : "",
      "kh_type" : "",
      "kh_handset" : "17696589365",
      "kh_worktel" : "",
      "kh_remark" : "",
      "data_userid" : "张三",
      "addtime" : "2021/1/15 16:01:51"
    }
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequestMethod | 请求方式错误，必须为post请求！ | 请求方式错误，必须为post请求！ |
| 400 | invalidParameter | 请求参数缺失或无效！ | 请求参数缺失或无效！ |
| 400 | invalidSeCretKey | 无效的SeCretKey | 无效的SeCretKey |
| 400 | invalidSign | 签名无效 | 签名无效 |
