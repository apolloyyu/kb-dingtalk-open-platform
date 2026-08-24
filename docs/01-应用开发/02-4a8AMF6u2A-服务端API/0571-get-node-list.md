---
title: "获取节点列表"
source_url: "https://open.dingtalk.com/document/development/get-node-list"
namespace: "development"
slug: "get-node-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 知识库 > 知识库目录树管理 > 获取节点列表"
doc_id: "UYvCTqiO42"
updated_at: "2026-07-15 09:29:06"
---

> Source: https://open.dingtalk.com/document/development/get-node-list
> Path: 应用开发 / 服务端API / 文档/文件 > 知识库 > 知识库目录树管理 > 获取节点列表
> Updated: 2026-07-15 09:29:06

# 获取节点列表

调用本接口，获取节点列表。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/wiki/nodes |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Wiki.Node.Read-知识库节点读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| parentNodeId | String | 是 | 父节点id(父节点dentryUuid)，可通过调用[获取知识库列表](0560-get-knowledge-base-list.md)接口，获取返回参数`rootNodeId`字段。 |
| nextToken | String | 否 | 分页游标, 首次拉取不用传。 |
| maxResults | Integer | 否 | 分页大小，默认值50。    最大值50。 |
| withPermissionRole | Boolean | 否 | 是否获取权限信息：   - **true**：获取权限 - **false**：不获取权限     默认为false。 |
| operatorId | String | 是 | 操作人unionId。 |

### 请求示例

HTTP

```
GET /v2.0/wiki/nodes?parentNodeId=MNDoxxxxmrZQ3&nextToken=next_token&maxResults=30&withPermissionRole=false&operatorId=tXguNxxxxURAiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json
```

Java

```
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkwiki_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkwiki_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkwiki_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkwiki_2_0.models.ListNodesHeaders listNodesHeaders = new com.aliyun.dingtalkwiki_2_0.models.ListNodesHeaders();
        listNodesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkwiki_2_0.models.ListNodesRequest listNodesRequest = new com.aliyun.dingtalkwiki_2_0.models.ListNodesRequest()
                .setParentNodeId("MNDoxxxxmrZQ3")
                .setNextToken("next_token")
                .setMaxResults(30)
                .setWithPermissionRole(false)
                .setOperatorId("tXguNxxxxURAiEiE");
        try {
            client.listNodesWithOptions(listNodesRequest, listNodesHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys
import json

from typing import List

from alibabacloud_dingtalk.wiki_2_0.client import Client as dingtalkwiki_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.wiki_2_0 import models as dingtalkwiki__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkwiki_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkwiki_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_nodes_headers = dingtalkwiki__2__0_models.ListNodesHeaders()
        list_nodes_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_nodes_request = dingtalkwiki__2__0_models.ListNodesRequest(
            parent_node_id='MNDoxxxxmrZQ3',
            next_token='next_token',
            max_results=30,
            with_permission_role=False,
            operator_id='tXguNxxxxURAiEiE'
        )
        try:
            client.list_nodes_with_options(list_nodes_request, list_nodes_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_nodes_headers = dingtalkwiki__2__0_models.ListNodesHeaders()
        list_nodes_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_nodes_request = dingtalkwiki__2__0_models.ListNodesRequest(
            parent_node_id='MNDoxxxxmrZQ3',
            next_token='next_token',
            max_results=30,
            with_permission_role=False,
            operator_id='tXguNxxxxURAiEiE'
        )
        try:
            await client.list_nodes_with_options_async(list_nodes_request, list_nodes_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vwiki_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vwiki_2_0\Models\ListNodesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vwiki_2_0\Models\ListNodesRequest;
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
        $listNodesHeaders = new ListNodesHeaders([]);
        $listNodesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listNodesRequest = new ListNodesRequest([
            "parentNodeId" => "MNDoxxxxmrZQ3",
            "nextToken" => "next_token",
            "maxResults" => 30,
            "withPermissionRole" => false,
            "operatorId" => "tXguNxxxxURAiEiE"
        ]);
        try {
            $client->listNodesWithOptions($listNodesRequest, $listNodesHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkwiki_2_0  "github.com/alibabacloud-go/dingtalk/wiki_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalkwiki_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkwiki_2_0.Client{}
  _result, _err = dingtalkwiki_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listNodesHeaders := &dingtalkwiki_2_0.ListNodesHeaders{}
  listNodesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listNodesRequest := &dingtalkwiki_2_0.ListNodesRequest{
    ParentNodeId: tea.String("MNDoxxxxmrZQ3"),
    NextToken: tea.String("next_token"),
    MaxResults: tea.Int32(30),
    WithPermissionRole: tea.Bool(false),
    OperatorId: tea.String("tXguNxxxxURAiEiE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListNodesWithOptions(listNodesRequest, listNodesHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkwiki_2_0 = require('@alicloud/dingtalk/wiki_2_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkwiki_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let listNodesHeaders = new dingtalkwiki_2_0.ListNodesHeaders({ });
    listNodesHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let listNodesRequest = new dingtalkwiki_2_0.ListNodesRequest({
      parentNodeId: 'MNDoxxxxmrZQ3',
      nextToken: 'next_token',
      maxResults: 30,
      withPermissionRole: false,
      operatorId: 'tXguNxxxxURAiEiE',
    });
    try {
      await client.listNodesWithOptions(listNodesRequest, listNodesHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
Client.main(process.argv.slice(2));
```

C#

```
using Newtonsoft.Json;
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkwiki_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkwiki_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkwiki_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.ListNodesHeaders listNodesHeaders = new AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.ListNodesHeaders();
            listNodesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.ListNodesRequest listNodesRequest = new AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.ListNodesRequest
            {
                ParentNodeId = "MNDoxxxxmrZQ3",
                NextToken = "next_token",
                MaxResults = 30,
                WithPermissionRole = false,
                OperatorId = "tXguNxxxxURAiEiE",
            };
            try
            {
                client.ListNodesWithOptions(listNodesRequest, listNodesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| nodes | Array | 节点列表，最大size50。 |
| nodeId | String | 节点id(dentryUuid)。 |
| workspaceId | String | 知识库id(spaceUuid)。 |
| name | String | 名称。 |
| size | Long | 大小。 |
| type | String | 类型，枚举值：   - **FILE**：文件 - **FOLDER**：文件夹 |
| category | String | 类别，枚举值:   - **ALIDOC**：钉钉文档 - **DOCUMENT**：本地文档 - **IMAGE**：图片 - **VIDEO**：视频 - **AUDIO**：音频 - **ARCHIVE**：归档文件 - **OTHER**：其他类型 |
| extension | String | 后缀。 |
| url | String | 访问url。 |
| creatorId | String | 创建者userId。 |
| modifierId | String | 修改者userId。 |
| createTime | String | 创建时间。 |
| modifiedTime | String | 修改时间。 |
| hasChildren | Boolean | 是否有子节点：   - **true**：有 - **false**：没有 |
| statisticalInfo | Object | 统计信息。 |
| wordCount | Long | 字数。 |
| permissionRole | String | 当前用户对知识库节点的权限角色，枚举值:   - **OWNER**：拥有者 - **MANAGER**：管理者 - **EDITOR**：编辑者 - **DOWNLOADER**：可查看下载者 - **READER**：仅可查看者 - **NONE**：无权限者 |
| createTimestamp | Long | 创建时间戳。 |
| modifiedTimestamp | Long | 修改时间戳。 |
| nextToken | String | 分页游标。  **[!NOTE]**  不为空表示有更多数据。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "nodes" : [ {
    "nodeId" : "MNDoBxxxx8lemrZQ3",
    "workspaceId" : "MNDoBb6xxxxemrZQ3",
    "name" : "node_name",
    "size" : 512,
    "type" : "FILE",
    "category" : "ALIDOC",
    "extension" : "adoc",
    "url" : "node_url",
    "creatorId" : "01472825524039877041",
    "modifierId" : "01472825524039877041",
    "createTime" : "2023-05-15T11:29Z",
    "modifiedTime" : "2023-05-15T11:29Z",
    "hasChildren" : false,
    "statisticalInfo" : {
      "wordCount" : 123
    },
    "permissionRole" : "READER",
    "createTimestamp" : 1776134460000,
    "modifiedTimestamp" : 1783996860000
  } ],
  "nextToken" : "next_token"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 403 | permissionDenied | %s | 当前用户无此操作权限 |
| 404 | parentNodeNotExist | %s | 父节点不存在 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
