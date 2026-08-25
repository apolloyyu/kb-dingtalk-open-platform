---
title: "查询用户有权限的知识库列表"
source_url: "https://open.dingtalk.com/document/development/querying-the-list-of-user-team-spaces"
namespace: "development"
slug: "querying-the-list-of-user-team-spaces"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 知识库 > 知识库管理 > 查询用户有权限的知识库列表"
doc_id: "5krEJX97m9"
updated_at: "2026-08-25 09:38:43"
---

> Source: https://open.dingtalk.com/document/development/querying-the-list-of-user-team-spaces
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 知识库 > 知识库管理 > 查询用户有权限的知识库列表
> Updated: 2026-08-25 09:38:43

# 查询用户有权限的知识库列表

调用本接口，查询某个用户有权限的知识库列表。

> **[!IMPORTANT]**
>
> - 新老接口中的ID不兼容, 不支持混用。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取知识库列表](0560-get-knowledge-base-list.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v1.0/doc/workspaces?operatorId=String&includeRecent=Boolean HTTP/1.1
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
| operatorId | String | 是 | 被获取信息的用户unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。  例如：需要查询小钉拥有权限的知识库列表，该参数传小钉的unionId。 |
| includeRecent | Boolean | 否 | 是否查询最近访问的文档列表。   - **true**：查询。 - **false**：不查询。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| workspaces | Array | 知识库列表。 |
| workspaceId | String | 知识库ID。 |
| url | String | 知识库URL。 |
| deleted | Boolean | 知识库是否被删除。   - **true**：已删除。 - **false**：未删除   **[!NOTE]**  目前知识库没有回收状态，所以已删除的知识库，本接口暂不支持获取。能获取到的知识库都是未删除的。 |
| owner | String | 此空间所有者的unionId。 |
| role | String | 用户在该知识库内的角色。   - **OWNER**：所有者。 - **MANAGER**：管理者。 - **EDITOR**：可编辑。 - **VIEWER**：可查询和下载。 - **ONLY\_VIEWER**：仅可查看。 |
| name | String | 知识库名称。 |
| recentList | Array | 最近访问的文档列表。  **[!NOTE]**  参数**includeRecent**值为**true**时才会返回。 |
| nodeId | String | 文档ID。 |
| name | String | 文档名称。 |
| url | String | 文档URL。 |
| lastEditTime | Long | 文档最后编辑时间戳，单位毫秒。 |
| createTime | Long | 知识库创建的时间戳，单位毫秒。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/doc/workspaces?operatorId=Q2xwxxx&includeRecent=true HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:37ea3bxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdoc_1_0.*;
import com.aliyun.dingtalkdoc_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        GetRelatedWorkspacesHeaders getRelatedWorkspacesHeaders = new GetRelatedWorkspacesHeaders();
        getRelatedWorkspacesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetRelatedWorkspacesRequest getRelatedWorkspacesRequest = new GetRelatedWorkspacesRequest()
                .setOperatorId("Q2xwxxx")
                .setIncludeRecent(true);
        try {
            client.getRelatedWorkspacesWithOptions(getRelatedWorkspacesRequest, getRelatedWorkspacesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.doc_1_0.client import Client as dingtalkdoc_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_1_0 import models as dingtalkdoc__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_related_workspaces_headers = dingtalkdoc__1__0_models.GetRelatedWorkspacesHeaders()
        get_related_workspaces_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_related_workspaces_request = dingtalkdoc__1__0_models.GetRelatedWorkspacesRequest(
            operator_id='Q2xwxxx',
            include_recent=True
        )
        try:
            client.get_related_workspaces_with_options(get_related_workspaces_request, get_related_workspaces_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_related_workspaces_headers = dingtalkdoc__1__0_models.GetRelatedWorkspacesHeaders()
        get_related_workspaces_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_related_workspaces_request = dingtalkdoc__1__0_models.GetRelatedWorkspacesRequest(
            operator_id='Q2xwxxx',
            include_recent=True
        )
        try:
            await client.get_related_workspaces_with_options_async(get_related_workspaces_request, get_related_workspaces_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetRelatedWorkspacesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\GetRelatedWorkspacesRequest;
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
        $getRelatedWorkspacesHeaders = new GetRelatedWorkspacesHeaders([]);
        $getRelatedWorkspacesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getRelatedWorkspacesRequest = new GetRelatedWorkspacesRequest([
            "operatorId" => "Q2xwxxx",
            "includeRecent" => true
        ]);
        try {
            $client->getRelatedWorkspacesWithOptions($getRelatedWorkspacesRequest, $getRelatedWorkspacesHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdoc_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_1_0.Client{}
  _result, _err = dingtalkdoc_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getRelatedWorkspacesHeaders := &dingtalkdoc_1_0.GetRelatedWorkspacesHeaders{}
  getRelatedWorkspacesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getRelatedWorkspacesRequest := &dingtalkdoc_1_0.GetRelatedWorkspacesRequest{
    OperatorId: tea.String("Q2xwxxx"),
    IncludeRecent: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetRelatedWorkspacesWithOptions(getRelatedWorkspacesRequest, getRelatedWorkspacesHeaders, &util.RuntimeOptions{})
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
import dingtalkdoc_1_0, * as $dingtalkdoc_1_0 from '@alicloud/dingtalk/doc_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdoc_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdoc_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getRelatedWorkspacesHeaders = new $dingtalkdoc_1_0.GetRelatedWorkspacesHeaders({ });
    getRelatedWorkspacesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getRelatedWorkspacesRequest = new $dingtalkdoc_1_0.GetRelatedWorkspacesRequest({
      operatorId: "Q2xwxxx",
      includeRecent: true,
    });
    try {
      await client.getRelatedWorkspacesWithOptions(getRelatedWorkspacesRequest, getRelatedWorkspacesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdoc_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRelatedWorkspacesHeaders getRelatedWorkspacesHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRelatedWorkspacesHeaders();
            getRelatedWorkspacesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRelatedWorkspacesRequest getRelatedWorkspacesRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.GetRelatedWorkspacesRequest
            {
                OperatorId = "Q2xwxxx",
                IncludeRecent = true,
            };
            try
            {
                client.GetRelatedWorkspacesWithOptions(getRelatedWorkspacesRequest, getRelatedWorkspacesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkdoc__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdoc_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdoc_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdoc_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::GetRelatedWorkspacesHeaders> getRelatedWorkspacesHeaders = make_shared<Alibabacloud_Dingtalkdoc_1_0::GetRelatedWorkspacesHeaders>();
  getRelatedWorkspacesHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdoc_1_0::GetRelatedWorkspacesRequest> getRelatedWorkspacesRequest = make_shared<Alibabacloud_Dingtalkdoc_1_0::GetRelatedWorkspacesRequest>(map<string, boost::any>({
    {"operatorId", boost::any(string("Q2xwxxx"))},
    {"includeRecent", boost::any(true)}
  }));
  try {
    client->getRelatedWorkspacesWithOptions(getRelatedWorkspacesRequest, getRelatedWorkspacesHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "workspaces" : [ {
    "workspaceId" : "nb9XJKdxxxxmyAp",
    "url" : "https://alidocs.xxxx/nb9XJKdxxxxmyAp",
    "deleted" : false,
    "owner" : "Q2xwPOKiSLxxxx",
    "role" : "OWNER：所有者；MANAGER：管理者；EDITOR：可编辑；VIEWER：可查询\\下载；ONLY_VIEWER：尽可查看",
    "name" : "知识库",
    "recentList" : [ {
      "nodeId" : "nb9XxxxxxxmyAp",
      "name" : "知识库文档",
      "url" : "https://alidocs.xxxx/nb9XJKdxxxxmyAp/docs/nb9XxxxxxxmyAp",
      "lastEditTime" : 1638256965936
    } ],
    "createTime" : 1638256965936
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.invalid | 方法入参校验失败 | 方法入参校验失败，检查是否有必填参数未填，或者unionId是否合法等 |
| 403 | forbidden.user.notInOrg | 操作用户不在组织内 | 操作用户不在组织内 |
| 403 | forbidden.accessDenied | 用户无操作权限 | 当前用户无此操作权限 |
| 404 | invalidRequest.resource.notFound | 资源找不到 | 资源找不到 |
| 404 | invalidRequest.workspace.deleted | 知识库被删除 | 知识库被删除 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
