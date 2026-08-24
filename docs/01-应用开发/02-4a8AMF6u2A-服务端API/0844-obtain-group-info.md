---
title: "查询企业内部群信息"
source_url: "https://open.dingtalk.com/document/development/obtain-group-info"
namespace: "development"
slug: "obtain-group-info"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 企业内部群 > 查询企业内部群信息"
doc_id: "q4yli4JERG"
updated_at: "2026-06-04 19:09:59"
---

> Source: https://open.dingtalk.com/document/development/obtain-group-info
> Path: 应用开发 / 服务端API / 专属钉钉 > 企业内部群 > 查询企业内部群信息
> Updated: 2026-06-04 19:09:59

# 查询企业内部群信息

调用本接口查询企业内部群信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/securities/orgGroupInfos |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Custom.Group.Read-专属钉钉群读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| groupMembersCountEnd | Integer | 否 | 群人数范围最大值，例如100。 |
| syncToDingpan | Integer | 否 | 是否同步到钉盘:   - **0**: 不同步 - **1**: 同步 |
| groupOwner | String | 否 | 群主的userId。 |
| createTimeEnd | Long | 否 | 创建时间查询最大时间戳。 |
| pageSize | Integer | 是 | 分页大小。 |
| createTimeStart | Long | 否 | 创建时间查询最小时间戳。 |
| uuid | String | 是 | 每次查询唯一标识，保证每次分页查询时该值不变。 |
| groupMembersCountStart | Integer | 否 | 群人数范围最小值，例如1。 |
| lastActiveTimeEnd | Long | 否 | 最后一次活跃时间戳最大值。 |
| operatorUserId | String | 是 | 当前查询人的userId。 |
| groupName | String | 否 | 群名称。 |
| pageStart | Integer | 是 | 分页号，从1开始。 |
| lastActiveTimeStart | Long | 否 | 最后一次活跃时间戳最小值。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/securities/orgGroupInfos?groupMembersCountEnd=100&syncToDingpan=1&groupOwner=user123&createTimeEnd=1618546742&pageSize=10&createTimeStart=1618546755&uuid=1111&groupMembersCountStart=1&operatorUserId=user234&groupName=群1&pageStart=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE390xxxxxx
Content-Type:application/json
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
        SearchOrgInnerGroupInfoHeaders searchOrgInnerGroupInfoHeaders = new SearchOrgInnerGroupInfoHeaders();
        searchOrgInnerGroupInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SearchOrgInnerGroupInfoRequest searchOrgInnerGroupInfoRequest = new SearchOrgInnerGroupInfoRequest()
                .setGroupMembersCountEnd(100)
                .setSyncToDingpan(1)
                .setGroupOwner("user123")
                .setCreateTimeEnd(1618546742L)
                .setPageSize(10)
                .setCreateTimeStart(1618546755L)
                .setUuid("1111")
                .setGroupMembersCountStart(1)
                .setLastActiveTimeEnd(1618546999L)
                .setOperatorUserId("user234")
                .setGroupName("群1")
                .setPageStart(1)
                .setLastActiveTimeStart(1618546999L);
        try {
            client.searchOrgInnerGroupInfoWithOptions(searchOrgInnerGroupInfoRequest, searchOrgInnerGroupInfoHeaders, new RuntimeOptions());
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
        search_org_inner_group_info_headers = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders()
        search_org_inner_group_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_org_inner_group_info_request = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest(
            group_members_count_end=100,
            sync_to_dingpan=1,
            group_owner='user123',
            create_time_end=1618546742,
            page_size=10,
            create_time_start=1618546755,
            uuid='1111',
            group_members_count_start=1,
            last_active_time_end=1618546999,
            operator_user_id='user234',
            group_name='群1',
            page_start=1,
            last_active_time_start=1618546999
        )
        try:
            client.search_org_inner_group_info_with_options(search_org_inner_group_info_request, search_org_inner_group_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        search_org_inner_group_info_headers = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoHeaders()
        search_org_inner_group_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        search_org_inner_group_info_request = dingtalkexclusive__1__0_models.SearchOrgInnerGroupInfoRequest(
            group_members_count_end=100,
            sync_to_dingpan=1,
            group_owner='user123',
            create_time_end=1618546742,
            page_size=10,
            create_time_start=1618546755,
            uuid='1111',
            group_members_count_start=1,
            last_active_time_end=1618546999,
            operator_user_id='user234',
            group_name='群1',
            page_start=1,
            last_active_time_start=1618546999
        )
        try:
            await client.search_org_inner_group_info_with_options_async(search_org_inner_group_info_request, search_org_inner_group_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SearchOrgInnerGroupInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SearchOrgInnerGroupInfoRequest;
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
        $searchOrgInnerGroupInfoHeaders = new SearchOrgInnerGroupInfoHeaders([]);
        $searchOrgInnerGroupInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $searchOrgInnerGroupInfoRequest = new SearchOrgInnerGroupInfoRequest([
            "groupMembersCountEnd" => 100,
            "syncToDingpan" => 1,
            "groupOwner" => "user123",
            "createTimeEnd" => 1618546742,
            "pageSize" => 10,
            "createTimeStart" => 1618546755,
            "uuid" => "1111",
            "groupMembersCountStart" => 1,
            "lastActiveTimeEnd" => 1618546999,
            "operatorUserId" => "user234",
            "groupName" => "群1",
            "pageStart" => 1,
            "lastActiveTimeStart" => 1618546999
        ]);
        try {
            $client->searchOrgInnerGroupInfoWithOptions($searchOrgInnerGroupInfoRequest, $searchOrgInnerGroupInfoHeaders, new RuntimeOptions([]));
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

  searchOrgInnerGroupInfoHeaders := &dingtalkexclusive_1_0.SearchOrgInnerGroupInfoHeaders{}
  searchOrgInnerGroupInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  searchOrgInnerGroupInfoRequest := &dingtalkexclusive_1_0.SearchOrgInnerGroupInfoRequest{
    GroupMembersCountEnd: tea.Int32(100),
    SyncToDingpan: tea.Int32(1),
    GroupOwner: tea.String("user123"),
    CreateTimeEnd: tea.Int64(1618546742),
    PageSize: tea.Int32(10),
    CreateTimeStart: tea.Int64(1618546755),
    Uuid: tea.String("1111"),
    GroupMembersCountStart: tea.Int32(1),
    LastActiveTimeEnd: tea.Int64(1618546999),
    OperatorUserId: tea.String("user234"),
    GroupName: tea.String("群1"),
    PageStart: tea.Int32(1),
    LastActiveTimeStart: tea.Int64(1618546999),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SearchOrgInnerGroupInfoWithOptions(searchOrgInnerGroupInfoRequest, searchOrgInnerGroupInfoHeaders, &util.RuntimeOptions{})
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
    let searchOrgInnerGroupInfoHeaders = new $dingtalkexclusive_1_0.SearchOrgInnerGroupInfoHeaders({ });
    searchOrgInnerGroupInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let searchOrgInnerGroupInfoRequest = new $dingtalkexclusive_1_0.SearchOrgInnerGroupInfoRequest({
      groupMembersCountEnd: 100,
      syncToDingpan: 1,
      groupOwner: "user123",
      createTimeEnd: 1618546742,
      pageSize: 10,
      createTimeStart: 1618546755,
      uuid: "1111",
      groupMembersCountStart: 1,
      lastActiveTimeEnd: 1618546999,
      operatorUserId: "user234",
      groupName: "群1",
      pageStart: 1,
      lastActiveTimeStart: 1618546999,
    });
    try {
      await client.searchOrgInnerGroupInfoWithOptions(searchOrgInnerGroupInfoRequest, searchOrgInnerGroupInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SearchOrgInnerGroupInfoHeaders searchOrgInnerGroupInfoHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SearchOrgInnerGroupInfoHeaders();
            searchOrgInnerGroupInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SearchOrgInnerGroupInfoRequest searchOrgInnerGroupInfoRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SearchOrgInnerGroupInfoRequest
            {
                GroupMembersCountEnd = 100,
                SyncToDingpan = 1,
                GroupOwner = "user123",
                CreateTimeEnd = 1618546742,
                PageSize = 10,
                CreateTimeStart = 1618546755,
                Uuid = "1111",
                GroupMembersCountStart = 1,
                LastActiveTimeEnd = 1618546999,
                OperatorUserId = "user234",
                GroupName = "群1",
                PageStart = 1,
                LastActiveTimeStart = 1618546999,
            };
            try
            {
                client.SearchOrgInnerGroupInfoWithOptions(searchOrgInnerGroupInfoRequest, searchOrgInnerGroupInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| totalCount | Long | 查询总数。 |
| itemCount | Integer | 当前查询结果数。 |
| items | Array | 当前结果集。 |
| openConversationId | String | 群会话开放id。 |
| groupOwner | String | 群主。 |
| groupName | String | 群名。 |
| groupAdminsCount | Integer | 群管理员个数。 |
| groupMembersCount | Integer | 群人数。 |
| groupCreateTime | Long | 群创建时间。 |
| groupLastActiveTime | Long | 群最后一次活跃时间。 |
| groupLastActiveTimeShow | String | 群最后一次活跃时间文字描述。 |
| syncToDingpan | Integer | 是否同步到钉盘。 |
| usedQuota | Long | 当前使用容量。 |
| groupOwnerUserId | String | 群主的userid。 |
| status | Integer | 群状态：   - **-1**：解散 - **0**：群人数为0 - **1**：群正常 |
| templateId | String | 群模板ID。 |
| templateName | String | 群模板名称。 |
| extensions | Map<String, String> | 群扩展信息 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 20,
  "itemCount" : 10,
  "items" : [ {
    "openConversationId" : "cidmfWxxxx",
    "groupOwner" : "小明",
    "groupName" : "测试群",
    "groupAdminsCount" : 2,
    "groupMembersCount" : 10,
    "groupCreateTime" : 123000000,
    "groupLastActiveTime" : 125000000,
    "groupLastActiveTimeShow" : "6个月前",
    "syncToDingpan" : 0,
    "usedQuota" : 12000,
    "groupOwnerUserId" : "02500",
    "status" : 1,
    "templateId" : "xxx",
    "templateName" : "测试模板"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | unknownError | 未知错误 | 未知错误 |
