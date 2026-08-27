---
title: "查询知识库节点信息"
source_url: "https://open.dingtalk.com/document/development/query-knowledge-base-node-information"
namespace: "development"
slug: "query-knowledge-base-node-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 知识库 > 知识库目录树管理 > 查询知识库节点信息"
doc_id: "xhXpo5UQ3s"
updated_at: "2026-08-25 09:38:49"
---

> Source: https://open.dingtalk.com/document/development/query-knowledge-base-node-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 知识库 > 知识库目录树管理 > 查询知识库节点信息
> Updated: 2026-08-25 09:38:49

# 查询知识库节点信息

调用本接口，查询知识库内的节点信息，包括节点类型、节点ID、节点名称等。

> **[!IMPORTANT]**
>
> - 新老接口中的ID不兼容, 不支持混用。
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取节点](0570-get-knowledge-base-acquisition-node.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v2.0/doc/spaces/{spaceId}/dentries/{dentryId}?operatorId=String&includeSpace=Boolean HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 知识库ID，调用[新建知识库](1586-create-a-team-space.md)接口或者[查询用户有权限的知识库列表](1588-querying-the-list-of-user-team-spaces.md)接口获取的workspaceId字段值。 |
| dentryId | String | 是 | 节点ID，调用[查询知识库下的目录结构](1593-query-the-directory-tree-in-the-knowledge-base.md)接口获取DentryModel参数值。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 操作人unionId，调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| includeSpace | Boolean | 否 | 是否查询知识库信息，默认不查询。   - **true**：查询 - **false**：不查询   **[!NOTE]**  如果该参数指定为true，返回结果会包含space字段，表示当前知识库的基础信息。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
|  | DentryVO | 节点信息，参考[通用数据格式-DentryVO](0574-common-data-structure.md#DentryVO)。 |

## 示例

**请求示例**

HTTP

```
GET /v2.0/doc/spaces/abc/dentries/def?operatorId=abcd&includeSpace=false HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7dc9ecxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdoc_2_0.*;
import com.aliyun.dingtalkdoc_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdoc_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdoc_2_0.Client client = Sample.createClient();
        QueryDentryHeaders queryDentryHeaders = new QueryDentryHeaders();
        queryDentryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        QueryDentryRequest queryDentryRequest = new QueryDentryRequest()
                .setOperatorId("abcd")
                .setIncludeSpace(false);
        try {
            client.queryDentryWithOptions("abc", "def", queryDentryRequest, queryDentryHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.doc_2_0.client import Client as dingtalkdoc_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.doc_2_0 import models as dingtalkdoc__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdoc_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdoc_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_dentry_headers = dingtalkdoc__2__0_models.QueryDentryHeaders()
        query_dentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_dentry_request = dingtalkdoc__2__0_models.QueryDentryRequest(
            operator_id='abcd',
            include_space=False
        )
        try:
            client.query_dentry_with_options('abc', 'def', query_dentry_request, query_dentry_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_dentry_headers = dingtalkdoc__2__0_models.QueryDentryHeaders()
        query_dentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_dentry_request = dingtalkdoc__2__0_models.QueryDentryRequest(
            operator_id='abcd',
            include_space=False
        )
        try:
            await client.query_dentry_with_options_async('abc', 'def', query_dentry_request, query_dentry_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\QueryDentryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_2_0\Models\QueryDentryRequest;
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
        $queryDentryHeaders = new QueryDentryHeaders([]);
        $queryDentryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryDentryRequest = new QueryDentryRequest([
            "operatorId" => "abcd",
            "includeSpace" => false
        ]);
        try {
            $client->queryDentryWithOptions("abc", "def", $queryDentryRequest, $queryDentryHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_2_0  "github.com/alibabacloud-go/dingtalk/doc_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdoc_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdoc_2_0.Client{}
  _result, _err = dingtalkdoc_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryDentryHeaders := &dingtalkdoc_2_0.QueryDentryHeaders{}
  queryDentryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryDentryRequest := &dingtalkdoc_2_0.QueryDentryRequest{
    OperatorId: tea.String("abcd"),
    IncludeSpace: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryDentryWithOptions(tea.String("abc"), tea.String("def"), queryDentryRequest, queryDentryHeaders, &util.RuntimeOptions{})
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
import dingtalkdoc_2_0, * as $dingtalkdoc_2_0 from '@alicloud/dingtalk/doc_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdoc_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdoc_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let queryDentryHeaders = new $dingtalkdoc_2_0.QueryDentryHeaders({ });
    queryDentryHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let queryDentryRequest = new $dingtalkdoc_2_0.QueryDentryRequest({
      operatorId: "abcd",
      includeSpace: false,
    });
    try {
      await client.queryDentryWithOptions("abc", "def", queryDentryRequest, queryDentryHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdoc_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdoc_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.QueryDentryHeaders queryDentryHeaders = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.QueryDentryHeaders();
            queryDentryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.QueryDentryRequest queryDentryRequest = new AlibabaCloud.SDK.Dingtalkdoc_2_0.Models.QueryDentryRequest
            {
                OperatorId = "abcd",
                IncludeSpace = false,
            };
            try
            {
                client.QueryDentryWithOptions("abc", "def", queryDentryRequest, queryDentryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "contentType" : "alidoc",
  "createdTime" : 12345678,
  "updatedTime" : 12345678,
  "creator" : {
    "unionId" : "abc",
    "name" : "hello"
  },
  "dentryId" : "abc",
  "spaceId" : "bcd",
  "docKey" : "aabbcc",
  "space" : {
    "id" : "abc",
    "name" : "hello",
    "url" : "https://xx.yy",
    "owner" : {
      "unionId" : "abcd",
      "name" : "dingtalk"
    },
    "visitorInfo" : {
      "spaceActions" : [ "YYY" ],
      "dentryActions" : [ "XXX" ]
    }
  },
  "dentryUuid" : "cdefg",
  "dentryType" : "file",
  "extension" : "alidoc",
  "name" : "钉钉文档",
  "url" : "https://xxx.yy",
  "path" : "测试组织/测试知识库/abc",
  "hasChildren" : false,
  "updater" : {
    "unionId" : "abc",
    "name" : "abc"
  },
  "linkSourceInfo" : {
    "id" : "abc",
    "spaceId" : "def",
    "linkType" : 0,
    "extension" : "docx",
    "iconUrl" : {
      "small" : "def",
      "line" : "gh"
    }
  },
  "visitorInfo" : {
    "spaceActions" : [ "XXX" ],
    "dentryActions" : [ "YYY" ]
  }
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.argumentInvalid | %s | 参数非法，请查看具体错误信息 |
| 400 | invalidParameter.unionIdInvalid | %s | unionId非法，请检查参数是否正确 |
| 403 | forbidden.accessDenied | %s | 无当前节点的查看权限 |
| 403 | forbidden.accessDenied.notInOrg | %s | 组织外成员无权限 |
| 403 | forbidden.accessDenied.realmControl | %s | 企业开启了专属安全管控，操作被禁止 |
| 404 | invalidParameter.space.notFound | %s | 当前知识库不存在或已被删除 |
| 404 | invalidParameter.item.notFound | %s | 当前节点不存在或已被删除 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
