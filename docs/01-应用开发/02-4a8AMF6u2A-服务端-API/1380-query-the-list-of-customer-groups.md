---
title: "查询客户群列表"
source_url: "https://open.dingtalk.com/document/development/query-the-list-of-customer-groups"
namespace: "development"
slug: "query-the-list-of-customer-groups"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 查询客户群列表"
doc_id: "AbdLvSP5Uu"
updated_at: "2026-06-04 19:12:17"
---

> Source: https://open.dingtalk.com/document/development/query-the-list-of-customer-groups
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 客户群 > 查询客户群列表
> Updated: 2026-06-04 19:12:17

# 查询客户群列表

调用本接口，根据指定过滤条件和排序规则，查询客户群列表数据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/crmGroupChats |
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
| relationType | String | 是 | 关系类型。   - **crm\_customer**：企业客户。 - **crm\_customer\_personal**：个人客户。 |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上次调用返回的nextToken。 |
| maxResults | Integer | 是 | 每页最大条目数，最大值100。 |
| queryDsl | String | 否 | 查询DSL语法，参考[客户群查询DSL语法说明](1394-dsl-syntax-description.md)。 |

### 请求示例

HTTP

```
GET /v1.0/crm/crmGroupChats?relationType=crm_customer_personal&nextToken=fasdfs1&maxResults=10&queryDsl={"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"测试客户群","fieldId":"name"},{"filterType":"LT","value":"2640002249001","fieldId":"gmtCreate"}]}],"orderByFields":[{"orderByFieldId":"gmtCreate","orderByDirection":"ASC"}]} HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:asfsdfa1
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
        QueryCrmGroupChatsHeaders queryCrmGroupChatsHeaders = new QueryCrmGroupChatsHeaders();
        queryCrmGroupChatsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryCrmGroupChatsRequest queryCrmGroupChatsRequest = new QueryCrmGroupChatsRequest()
                .setRelationType("crm_customer_personal")
                .setNextToken("fasdfs1")
                .setMaxResults(10)
                .setQueryDsl("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}");
        try {
            client.queryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, new RuntimeOptions());
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
        query_crm_group_chats_headers = dingtalkcrm__1__0_models.QueryCrmGroupChatsHeaders()
        query_crm_group_chats_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_crm_group_chats_request = dingtalkcrm__1__0_models.QueryCrmGroupChatsRequest(
            relation_type='crm_customer_personal',
            next_token='fasdfs1',
            max_results=10,
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"测试客户群","fieldId":"name"},{"filterType":"LT","value":"2640002249001","fieldId":"gmtCreate"}]}],"orderByFields":[{"orderByFieldId":"gmtCreate","orderByDirection":"ASC"}]}'
        )
        try:
            client.query_crm_group_chats_with_options(query_crm_group_chats_request, query_crm_group_chats_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_crm_group_chats_headers = dingtalkcrm__1__0_models.QueryCrmGroupChatsHeaders()
        query_crm_group_chats_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_crm_group_chats_request = dingtalkcrm__1__0_models.QueryCrmGroupChatsRequest(
            relation_type='crm_customer_personal',
            next_token='fasdfs1',
            max_results=10,
            query_dsl='{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"测试客户群","fieldId":"name"},{"filterType":"LT","value":"2640002249001","fieldId":"gmtCreate"}]}],"orderByFields":[{"orderByFieldId":"gmtCreate","orderByDirection":"ASC"}]}'
        )
        try:
            await client.query_crm_group_chats_with_options_async(query_crm_group_chats_request, query_crm_group_chats_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryCrmGroupChatsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\QueryCrmGroupChatsRequest;
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
        $queryCrmGroupChatsHeaders = new QueryCrmGroupChatsHeaders([]);
        $queryCrmGroupChatsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryCrmGroupChatsRequest = new QueryCrmGroupChatsRequest([
            "relationType" => "crm_customer_personal",
            "nextToken" => "fasdfs1",
            "maxResults" => 10,
            "queryDsl" => "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}"
        ]);
        try {
            $client->queryCrmGroupChatsWithOptions($queryCrmGroupChatsRequest, $queryCrmGroupChatsHeaders, new RuntimeOptions([]));
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

  queryCrmGroupChatsHeaders := &dingtalkcrm_1_0.QueryCrmGroupChatsHeaders{}
  queryCrmGroupChatsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryCrmGroupChatsRequest := &dingtalkcrm_1_0.QueryCrmGroupChatsRequest{
    RelationType: tea.String("crm_customer_personal"),
    NextToken: tea.String("fasdfs1"),
    MaxResults: tea.Int32(10),
    QueryDsl: tea.String("{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, &util.RuntimeOptions{})
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
    let queryCrmGroupChatsHeaders = new $dingtalkcrm_1_0.QueryCrmGroupChatsHeaders({ });
    queryCrmGroupChatsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryCrmGroupChatsRequest = new $dingtalkcrm_1_0.QueryCrmGroupChatsRequest({
      relationType: "crm_customer_personal",
      nextToken: "fasdfs1",
      maxResults: 10,
      queryDsl: "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}",
    });
    try {
      await client.queryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmGroupChatsHeaders queryCrmGroupChatsHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmGroupChatsHeaders();
            queryCrmGroupChatsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmGroupChatsRequest queryCrmGroupChatsRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.QueryCrmGroupChatsRequest
            {
                RelationType = "crm_customer_personal",
                NextToken = "fasdfs1",
                MaxResults = 10,
                QueryDsl = "{\"queryGroupList\":[{\"logicType\":\"AND\",\"queryObjectList\":[{\"filterType\":\"SEARCH\",\"value\":\"测试客户群\",\"fieldId\":\"name\"},{\"filterType\":\"LT\",\"value\":\"2640002249001\",\"fieldId\":\"gmtCreate\"}]}],\"orderByFields\":[{\"orderByFieldId\":\"gmtCreate\",\"orderByDirection\":\"ASC\"}]}",
            };
            try
            {
                client.QueryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::QueryCrmGroupChatsHeaders> queryCrmGroupChatsHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::QueryCrmGroupChatsHeaders>();
  queryCrmGroupChatsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::QueryCrmGroupChatsRequest> queryCrmGroupChatsRequest = make_shared<Alibabacloud_Dingtalkcrm_1_0::QueryCrmGroupChatsRequest>(map<string, boost::any>({
    {"relationType", boost::any(string("crm_customer_personal"))},
    {"nextToken", boost::any(string("fasdfs1"))},
    {"maxResults", boost::any(10)},
    {"queryDsl", boost::any(string("{"queryGroupList":[{"logicType":"AND","queryObjectList":[{"filterType":"SEARCH","value":"测试客户群","fieldId":"name"},{"filterType":"LT","value":"2640002249001","fieldId":"gmtCreate"}]}],"orderByFields":[{"orderByFieldId":"gmtCreate","orderByDirection":"ASC"}]}"))}
  }));
  try {
    client->queryCrmGroupChatsWithOptions(queryCrmGroupChatsRequest, queryCrmGroupChatsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| resultList | Array | 数据列表。 |
| openConversationId | String | 客户群openConversationId。 |
| openGroupSetId | String | 客户群所在的群组openGroupSetId。   - 如果是客户群组裂变出的客户群，会返回该字段。 - 如果是调用[创建客户群](1379-create-a-customer-group.md)接口创建的客户群，不返回该字段。 |
| ownerUserId | String | 群主userId。 |
| ownerUserName | String | 群主userName。 |
| name | String | 客户群名称。 |
| memberCount | Integer | 客户群成员数。 |
| gmtCreate | Long | 客户群创建时间。 |
| hasMore | Boolean | 是否还有下一页。   - **true**：有 - **false**：没有 |
| nextToken | String | 下一页的游标。 |
| totalCount | Integer | 总条数。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "resultList" : [ {
    "openConversationId" : "afsad21",
    "openGroupSetId" : "afsdba23",
    "ownerUserId" : "afds12",
    "ownerUserName" : "XX",
    "name" : "营销1群",
    "memberCount" : 100,
    "gmtCreate" : 1640239655539
  } ],
  "hasMore" : true,
  "nextToken" : "agds12",
  "totalCount" : 1000
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | invalid parameter. | 无效的参数 |
| 400 | notSupportedFilterType | %s | 不支持的查询类型 |
| 400 | userIdNotExists | %s | 用户不存在 |
| 500 | systemError | %s | 系统错误 |
