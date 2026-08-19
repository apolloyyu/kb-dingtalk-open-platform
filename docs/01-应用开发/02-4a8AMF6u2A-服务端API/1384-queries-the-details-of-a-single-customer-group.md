---
title: "获取单个客户群组详情"
source_url: "https://open.dingtalk.com/document/development/queries-the-details-of-a-single-customer-group"
namespace: "development"
slug: "queries-the-details-of-a-single-customer-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 获取单个客户群组详情"
doc_id: "6cCH06hVLB"
updated_at: "2025-10-09 18:06:24"
---

> Source: https://open.dingtalk.com/document/development/queries-the-details-of-a-single-customer-group
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户群 > 获取单个客户群组详情
> Updated: 2025-10-09 18:06:24

# 获取单个客户群组详情

调用本接口，获取单个客户群组详情，包括群组内已自动创建的群数量、群组设置的群主、群组设置的管理员和群组设置的上限成员数等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/groupSets |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Crm.CustomerGroup.Read-客户管理客户群读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openGroupSetId | String | 是 | 群组openGroupSetId，调用[查询客户群组列表](1386-query-groups.md)接口获取openGroupSetId参数值。 |

### 请求示例

HTTP

```
GET /v1.0/crm/groupSets?openGroupSetId=OkldZxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fghsdffgnfghjghcvbgfghertyghjghj
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcrm_1_0.*;
import com.aliyun.dingtalkcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        GetGroupSetHeaders getGroupSetHeaders = new GetGroupSetHeaders();
        getGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetGroupSetRequest getGroupSetRequest = new GetGroupSetRequest()
                .setOpenGroupSetId("OkldZxxxx");
        try {
            client.getGroupSetWithOptions(getGroupSetRequest, getGroupSetHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_group_set_headers = dingtalkcrm__1__0_models.GetGroupSetHeaders()
        get_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_group_set_request = dingtalkcrm__1__0_models.GetGroupSetRequest(
            open_group_set_id='OkldZxxxx'
        )
        try:
            client.get_group_set_with_options(get_group_set_request, get_group_set_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_group_set_headers = dingtalkcrm__1__0_models.GetGroupSetHeaders()
        get_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_group_set_request = dingtalkcrm__1__0_models.GetGroupSetRequest(
            open_group_set_id='OkldZxxxx'
        )
        try:
            await client.get_group_set_with_options_async(get_group_set_request, get_group_set_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetGroupSetHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\GetGroupSetRequest;
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
        $getGroupSetHeaders = new GetGroupSetHeaders([]);
        $getGroupSetHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getGroupSetRequest = new GetGroupSetRequest([
            "openGroupSetId" => "OkldZxxxx"
        ]);
        try {
            $client->getGroupSetWithOptions($getGroupSetRequest, $getGroupSetHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getGroupSetHeaders := &dingtalkcrm_1_0.GetGroupSetHeaders{}
  getGroupSetHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getGroupSetRequest := &dingtalkcrm_1_0.GetGroupSetRequest{
    OpenGroupSetId: tea.String("OkldZxxxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetGroupSetWithOptions(getGroupSetRequest, getGroupSetHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getGroupSetHeaders = new $dingtalkcrm_1_0.GetGroupSetHeaders({ });
    getGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getGroupSetRequest = new $dingtalkcrm_1_0.GetGroupSetRequest({
      openGroupSetId: "OkldZxxxx",
    });
    try {
      await client.getGroupSetWithOptions(getGroupSetRequest, getGroupSetHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetGroupSetHeaders getGroupSetHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetGroupSetHeaders();
            getGroupSetHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetGroupSetRequest getGroupSetRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.GetGroupSetRequest
            {
                OpenGroupSetId = "OkldZxxxx",
            };
            try
            {
                client.GetGroupSetWithOptions(getGroupSetRequest, getGroupSetHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| name | String | 群组名称。 |
| openGroupSetId | String | 群组 openGroupSetId。 |
| relationType | String | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| memberQuota | Integer | 群组内客户群上限人数。 |
| memberCount | Integer | 群组内客户群的成员数量。 |
| templateId | String | 群模板ID。      该字段暂无使用场景。 |
| ownerUserId | String | 群主userId。      自动创建的新群会默认设置该userId为群主。 |
| managerUserIds | String | 群管理员userId列表，多个用逗号隔开。      自动创建的新群会默认设置这些userId为群管理员。 |
| notice | String | 群公告文本。      自动创建的新群会默认设置该群公告。 |
| noticeToped | Integer | 群公告是否置顶。   - **0**：否 - **1**：是       自动创建的新群会默认设置该属性。 |
| owner | Object | 群主信息。 |
| name | String | 群主姓名。 |
| userId | String | 群主userId。 |
| manager | Array | 群管理员列表。 |
| name | String | 管理员姓名。 |
| userId | String | 管理员userId。 |
| lastOpenConversationId | String | 最新自动创建的群openConversationId。 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 更新时间。 |
| groupChatCount | Integer | 群组内客户群数量。      不包含已解散的群。 |
| inviteLink | String | 邀请加入客户群组的链接。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "name" : "营销群",
  "openGroupSetId" : "sdaxxxx",
  "relationType" : "crm_customer_personal",
  "memberQuota" : 100,
  "memberCount" : 68,
  "templateId" : "dsfgdsfgh-tghjghjgh-fdsfxcvxcvcxv",
  "ownerUserId" : "user001",
  "managerUserIds" : "user002",
  "notice" : "公告",
  "noticeToped" : 0,
  "owner" : {
    "name" : "张三",
    "userId" : "user001"
  },
  "manager" : [ {
    "name" : "李四",
    "userId" : "401227837938"
  } ],
  "lastOpenConversationId" : "dfgdfhgfghfg",
  "gmtCreate" : "2021-12-21T12:03Z",
  "gmtModified" : "2021-12-21T12:03Z",
  "groupChatCount" : 5,
  "inviteLink" : "dingtalk://dingtalkclient/page/link?pc_slide=true&xxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | needParameterNotPass | need parameter, groupset id not pass. | 必传参数，群组id未传 |
| 400 | recordNotExist | record not exist. | 记录不存在 |
| 400 | invalidParameter | invalid parameter. | 无效的参数 |
| 500 | systemError | system error. | 系统错误 |
