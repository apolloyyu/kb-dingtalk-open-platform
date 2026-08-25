---
title: "查询回收站文件（夹）列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-recycle-bin-folder-list"
namespace: "development"
slug: "obtain-the-recycle-bin-folder-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 回收站 > 查询回收站文件（夹）列表"
doc_id: "Z41ULc1pgi"
updated_at: "2026-08-25 09:38:29"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-recycle-bin-folder-list
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 回收站 > 查询回收站文件（夹）列表
> Updated: 2026-08-25 09:38:29

# 查询回收站文件（夹）列表

调用本接口查询回收站内文件（夹）列表。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取回收项列表](0688-gets-the-list-of-recycle-items.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v1.0/drive/recycleItems?unionId=String&recycleType=String&nextToken=String&maxResults=Integer&orderType=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
| recycleType | String | 是 | 回收站类型。   - **org**：企业 - **personal**：私人 |
| nextToken | String | 否 | 分页游标。 |
| maxResults | Integer | 是 | 分页大小。 |
| orderType | String | 否 | 文件排序类型。   - **deleteTimeDesc**：按删除时间排序 - **fileNameAsc**：按文件名排序 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| recycleItems | Array | 回收站文件列表。 |
| recycleItemId | String | 回收站记录ID。 |
| deleteStaffId | String | 删除员工工号。 |
| deleteTime | String | 删除时间。 |
| fileSize | Long | 文件大小。 |
| fileType | String | 文件类型。 |
| contentType | String | 文件内容类型。 |
| fileName | String | 文件名称。 |
| filePath | String | 文件路径。 |
| nextToken | String | 下一页的游标，为空字符串则表示分页结束。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/drive/recycleItems?unionId=sKUPRiijiSrqsuwqcPiSdbeNwiXxx&recycleType=org&nextToken=jfekfafe&maxResults=50&orderType=deleteTimeDesc HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2db66xxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdrive_1_0.*;
import com.aliyun.dingtalkdrive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdrive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdrive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdrive_1_0.Client client = Sample.createClient();
        ListRecycleFilesHeaders listRecycleFilesHeaders = new ListRecycleFilesHeaders();
        listRecycleFilesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListRecycleFilesRequest listRecycleFilesRequest = new ListRecycleFilesRequest()
                .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx")
                .setRecycleType("org")
                .setNextToken("jfekfafe")
                .setMaxResults(50)
                .setOrderType("deleteTimeDesc");
        try {
            client.listRecycleFilesWithOptions(listRecycleFilesRequest, listRecycleFilesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.drive_1_0.client import Client as dingtalkdrive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.drive_1_0 import models as dingtalkdrive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdrive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdrive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_recycle_files_headers = dingtalkdrive__1__0_models.ListRecycleFilesHeaders()
        list_recycle_files_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_recycle_files_request = dingtalkdrive__1__0_models.ListRecycleFilesRequest(
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx',
            recycle_type='org',
            next_token='jfekfafe',
            max_results=50,
            order_type='deleteTimeDesc'
        )
        try:
            client.list_recycle_files_with_options(list_recycle_files_request, list_recycle_files_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_recycle_files_headers = dingtalkdrive__1__0_models.ListRecycleFilesHeaders()
        list_recycle_files_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_recycle_files_request = dingtalkdrive__1__0_models.ListRecycleFilesRequest(
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx',
            recycle_type='org',
            next_token='jfekfafe',
            max_results=50,
            order_type='deleteTimeDesc'
        )
        try:
            await client.list_recycle_files_with_options_async(list_recycle_files_request, list_recycle_files_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\ListRecycleFilesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\ListRecycleFilesRequest;
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
        $listRecycleFilesHeaders = new ListRecycleFilesHeaders([]);
        $listRecycleFilesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listRecycleFilesRequest = new ListRecycleFilesRequest([
            "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
            "recycleType" => "org",
            "nextToken" => "jfekfafe",
            "maxResults" => 50,
            "orderType" => "deleteTimeDesc"
        ]);
        try {
            $client->listRecycleFilesWithOptions($listRecycleFilesRequest, $listRecycleFilesHeaders, new RuntimeOptions([]));
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
  dingtalkdrive_1_0  "github.com/alibabacloud-go/dingtalk/drive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdrive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdrive_1_0.Client{}
  _result, _err = dingtalkdrive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listRecycleFilesHeaders := &dingtalkdrive_1_0.ListRecycleFilesHeaders{}
  listRecycleFilesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listRecycleFilesRequest := &dingtalkdrive_1_0.ListRecycleFilesRequest{
    UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
    RecycleType: tea.String("org"),
    NextToken: tea.String("jfekfafe"),
    MaxResults: tea.Int32(50),
    OrderType: tea.String("deleteTimeDesc"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListRecycleFilesWithOptions(listRecycleFilesRequest, listRecycleFilesHeaders, &util.RuntimeOptions{})
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
import dingtalkdrive_1_0, * as $dingtalkdrive_1_0 from '@alicloud/dingtalk/drive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdrive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdrive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listRecycleFilesHeaders = new $dingtalkdrive_1_0.ListRecycleFilesHeaders({ });
    listRecycleFilesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listRecycleFilesRequest = new $dingtalkdrive_1_0.ListRecycleFilesRequest({
      unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
      recycleType: "org",
      nextToken: "jfekfafe",
      maxResults: 50,
      orderType: "deleteTimeDesc",
    });
    try {
      await client.listRecycleFilesWithOptions(listRecycleFilesRequest, listRecycleFilesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdrive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdrive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListRecycleFilesHeaders listRecycleFilesHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListRecycleFilesHeaders();
            listRecycleFilesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListRecycleFilesRequest listRecycleFilesRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListRecycleFilesRequest
            {
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
                RecycleType = "org",
                NextToken = "jfekfafe",
                MaxResults = 50,
                OrderType = "deleteTimeDesc",
            };
            try
            {
                client.ListRecycleFilesWithOptions(listRecycleFilesRequest, listRecycleFilesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdrive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdrive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdrive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdrive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::ListRecycleFilesHeaders> listRecycleFilesHeaders = make_shared<Alibabacloud_Dingtalkdrive_1_0::ListRecycleFilesHeaders>();
  listRecycleFilesHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::ListRecycleFilesRequest> listRecycleFilesRequest = make_shared<Alibabacloud_Dingtalkdrive_1_0::ListRecycleFilesRequest>(map<string, boost::any>({
    {"unionId", boost::any(string("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"))},
    {"recycleType", boost::any(string("org"))},
    {"nextToken", boost::any(string("jfekfafe"))},
    {"maxResults", boost::any(50)},
    {"orderType", boost::any(string("deleteTimeDesc"))}
  }));
  try {
    client->listRecycleFilesWithOptions(listRecycleFilesRequest, listRecycleFilesHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "recycleItems" : [ {
    "recycleItemId" : "123456",
    "deleteStaffId" : "088211",
    "deleteTime" : "2021-04-11T09:29:56Z",
    "fileSize" : 17311,
    "fileType" : "file",
    "contentType" : "document",
    "fileName" : "111.txt",
    "filePath" : "/测试目录/111.txt"
  } ],
  "nextToken" : "2CMlB97VtVJWfoVliPIXPUQiEiE"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Invalid Param | 参数错误 |
| 400 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 400 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 400 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 500 | unknown.error | Unknown Error | 未知错误 |
