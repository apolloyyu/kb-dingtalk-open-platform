---
title: "查询客户群组列表"
source_url: "https://open.dingtalk.com/document/development/query-groups"
namespace: "development"
slug: "query-groups"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 查询客户群组列表"
doc_id: "X0AYHZU632"
updated_at: "2026-06-03 15:47:52"
---

> Source: https://open.dingtalk.com/document/development/query-groups
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户群 > 查询客户群组列表
> Updated: 2026-06-03 15:47:52

# 查询客户群组列表

调用本接口，根据指定的筛选条件和排序规则，查询客户群组列表数据。

## 接口调用说明

例如，设置过滤条件和排序规则如下：

- 过滤条件为：客户群组名称包含“客户”进行模糊查询。
- 排序规则为：按照创建时间降序排列。

有2个客户群，为“核心客户1群”、“供应商客户1群”，对应的群组分别为“核心客户”、“供应商客户”，如下图所示。调用本接口，获取所有名称包含“客户”的客户群组列表，按创建时间降序结果为：

- 核心客户群组信息，如群组名称是“核心客户”、群组创建时间是2022-04-28T10:43Z、创建人是小钉等。
- 供应商客户群组信息，如群组名称是“供应商客户”、群组创建时间是2022-04-28T16:20Z、创建人是小钉等。

![](https://img.alicdn.com/imgextra/i4/O1CN01LJiQwM1bxFGExmylp_!!6000000003531-2-tps-1922-374.png)

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/groupSets/lists |
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
| nextToken | String | 否 | 分页游标。   - 如果是首次查询，该参数不传。 - 如果是非首次查询，该参数值传上一次调用时返回的nextToken。 |
| maxResults | Integer | 否 | 每页条目数，最大值10。 |
| queryDsl | String | 否 | 查询DSL，参考[客户群查询DSL语法说明](1394-dsl-syntax-description.md)。 |
| relationType | String | 是 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |

### 请求示例

HTTP

```
GET /v1.0/crm/groupSets/lists?nextToken=fasafsafsd&maxResults=10&queryDsl={"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"XX","fieldId":"name"}]}]}&relationType=crm_customer_personal HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:fasafsafsd
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
        ListGroupSetHeaders listGroupSetHeaders = new ListGroupSetHeaders();
        listGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListGroupSetRequest listGroupSetRequest = new ListGroupSetRequest()
                .setNextToken("fasafsafsd")
                .setMaxResults(10)
                .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}")
                .setRelationType("crm_customer_personal");
        try {
            client.listGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, new RuntimeOptions());
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
        list_group_set_headers = dingtalkcrm__1__0_models.ListGroupSetHeaders()
        list_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_group_set_request = dingtalkcrm__1__0_models.ListGroupSetRequest(
            next_token='fasafsafsd',
            max_results=10,
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"XX","fieldId":"name"}]}]}',
            relation_type='crm_customer_personal'
        )
        try:
            client.list_group_set_with_options(list_group_set_request, list_group_set_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_group_set_headers = dingtalkcrm__1__0_models.ListGroupSetHeaders()
        list_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_group_set_request = dingtalkcrm__1__0_models.ListGroupSetRequest(
            next_token='fasafsafsd',
            max_results=10,
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"XX","fieldId":"name"}]}]}',
            relation_type='crm_customer_personal'
        )
        try:
            await client.list_group_set_with_options_async(list_group_set_request, list_group_set_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\ListGroupSetHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\ListGroupSetRequest;
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
        $listGroupSetHeaders = new ListGroupSetHeaders([]);
        $listGroupSetHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listGroupSetRequest = new ListGroupSetRequest([
            "nextToken" => "fasafsafsd",
            "maxResults" => 10,
            "queryDsl" => "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}",
            "relationType" => "crm_customer_personal"
        ]);
        try {
            $client->listGroupSetWithOptions($listGroupSetRequest, $listGroupSetHeaders, new RuntimeOptions([]));
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

  listGroupSetHeaders := &dingtalkcrm_1_0.ListGroupSetHeaders{}
  listGroupSetHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listGroupSetRequest := &dingtalkcrm_1_0.ListGroupSetRequest{
    NextToken: tea.String("fasafsafsd"),
    MaxResults: tea.Int32(10),
    QueryDsl: tea.String("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}"),
    RelationType: tea.String("crm_customer_personal"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, &util.RuntimeOptions{})
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
    let listGroupSetHeaders = new $dingtalkcrm_1_0.ListGroupSetHeaders({ });
    listGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listGroupSetRequest = new $dingtalkcrm_1_0.ListGroupSetRequest({
      nextToken: "fasafsafsd",
      maxResults: 10,
      queryDsl: "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}",
      relationType: "crm_customer_personal",
    });
    try {
      await client.listGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListGroupSetHeaders listGroupSetHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListGroupSetHeaders();
            listGroupSetHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListGroupSetRequest listGroupSetRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.ListGroupSetRequest
            {
                NextToken = "fasafsafsd",
                MaxResults = 10,
                QueryDsl = "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"XX\",\"fieldId\":\"name\"}]}]}",
                RelationType = "crm_customer_personal",
            };
            try
            {
                client.ListGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkcrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::ListGroupSetHeaders> listGroupSetHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::ListGroupSetHeaders>();
  listGroupSetHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::ListGroupSetRequest> listGroupSetRequest = make_shared<Alibabacloud_Dingtalkcrm_1_0::ListGroupSetRequest>(map<string, boost::any>({
    {"nextToken", boost::any(string("fasafsafsd"))},
    {"maxResults", boost::any(10)},
    {"queryDsl", boost::any(string("{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"XX","fieldId":"name"}]}]}"))},
    {"relationType", boost::any(string("crm_customer_personal"))}
  }));
  try {
    client->listGroupSetWithOptions(listGroupSetRequest, listGroupSetHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| hasMore | Boolean | 是否有下一页。   - **true**：有 - **false**：没有 |
| nextToken | String | 下一页的游标。 |
| resultList | Array | 群组信息列表。 |
| name | String | 群组名。 |
| openGroupSetId | String | 群组openGroupSetId。 |
| relationType | String | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| memberQuota | Integer | 群组内单个群的人数上限。 |
| memberCount | Integer | 群组内所有群的成员总数量。 |
| templateId | String | 群模板Id。  **[!NOTE]**    该参数暂无使用场景。 |
| ownerUserId | String | 群主userId，裂变出的新群会自动设置该userId为群主。 |
| managerUserIds | String | 群管理员userId列表，用逗号隔开。  **[!NOTE]**    裂变出的新群会自动设置这些userId为群管理员。 |
| notice | String | 群公告文本。  **[!NOTE]**    裂变出的新群会自动设置上该群公告。 |
| noticeToped | Integer | 群公告是否置顶。   - **0**：否 - **1**：是   裂变出的新群会自动设置上该属性。 |
| owner | Object | 群主信息。 |
| name | String | 群主姓名。 |
| userId | String | 群主userId。 |
| manager | Array | 群管理员列表。 |
| name | String | 群管理员姓名。 |
| userId | String | 群管理员userId。 |
| lastOpenConversationId | String | 该群组裂变的第一个群openConversationId。 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 修改时间。 |
| groupChatCount | Integer | 群组内群的数量。  **[!NOTE]**    不包含已解散的群。 |
| totalCount | Integer | 总条数。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "hasMore" : true,
  "nextToken" : "fasafsafsd",
  "resultList" : [ {
    "name" : "营销群",
    "openGroupSetId" : "fasafsafsd",
    "relationType" : "crm_customer_personal",
    "memberQuota" : 500,
    "corpId" : "corp1",
    "memberCount" : 10,
    "templateId" : "sfasgsab",
    "ownerUserId" : "afsd12",
    "managerUserIds" : "afsd12,afsd13",
    "notice" : "群公告",
    "noticeToped" : 0,
    "owner" : {
      "name" : "XX",
      "userId" : "afsd12"
    },
    "manager" : [ {
      "name" : "XX",
      "userId" : "afsd13"
    } ],
    "lastOpenConversationId" : "123agsg",
    "gmtCreate" : "2021-12-23T16:20Z",
    "gmtModified" : "2021-12-23T16:20Z"
  } ],
  "totalCount" : 100
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | invalid parameter. | 参数错误 |
| 500 | unknownError | unknown error. | 未知错误 |
