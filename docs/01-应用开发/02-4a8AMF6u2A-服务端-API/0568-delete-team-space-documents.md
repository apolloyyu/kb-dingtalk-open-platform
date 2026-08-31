---
title: "删除知识库文档"
source_url: "https://open.dingtalk.com/document/development/delete-team-space-documents"
namespace: "development"
slug: "delete-team-space-documents"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 知识库目录树管理 > 删除知识库文档"
doc_id: "f6ye3xso8A"
updated_at: "2026-06-03 10:13:09"
---

> Source: https://open.dingtalk.com/document/development/delete-team-space-documents
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 知识库目录树管理 > 删除知识库文档
> Updated: 2026-06-03 10:13:09

# 删除知识库文档

调用本接口，可以删除团队空间文档或者文件夹。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workspaces/{workspaceId}/docs/{nodeId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Document.WorkspaceDocument.Write-知识库文档写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证， 可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workspaceId | String | 是 | 团队空间ID，可调用[新建知识库](0557-new-knowledge-base.md)接口或者[获取知识库列表](0560-get-knowledge-base-list.md)接口获取的workspaceId字段值。 |
| nodeId | String | 是 | 团队空间节点ID，可以传文档ID或者文件夹ID，可通过[创建知识库文档](0567-create-team-space-document.md)接口获取nodeId参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 是 | 发起删除请求的用户用户的unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求示例

HTTP

```
DELETE /v1.0/doc/workspaces/abc/docs/def?operatorId=xyz HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx_token
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
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_1_0.models.DeleteWorkspaceDocHeaders deleteWorkspaceDocHeaders = new com.aliyun.dingtalkdoc_1_0.models.DeleteWorkspaceDocHeaders();
        deleteWorkspaceDocHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.DeleteWorkspaceDocRequest deleteWorkspaceDocRequest = new com.aliyun.dingtalkdoc_1_0.models.DeleteWorkspaceDocRequest()
                .setOperatorId("xyz");
        try {
            client.deleteWorkspaceDocWithOptions("abc", "def", deleteWorkspaceDocRequest, deleteWorkspaceDocHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        delete_workspace_doc_headers = dingtalkdoc__1__0_models.DeleteWorkspaceDocHeaders()
        delete_workspace_doc_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_workspace_doc_request = dingtalkdoc__1__0_models.DeleteWorkspaceDocRequest(
            operator_id='xyz'
        )
        try:
            client.delete_workspace_doc_with_options('abc', 'def', delete_workspace_doc_request, delete_workspace_doc_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_workspace_doc_headers = dingtalkdoc__1__0_models.DeleteWorkspaceDocHeaders()
        delete_workspace_doc_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_workspace_doc_request = dingtalkdoc__1__0_models.DeleteWorkspaceDocRequest(
            operator_id='xyz'
        )
        try:
            await client.delete_workspace_doc_with_options_async('abc', 'def', delete_workspace_doc_request, delete_workspace_doc_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DeleteWorkspaceDocHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\DeleteWorkspaceDocRequest;
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
        $deleteWorkspaceDocHeaders = new DeleteWorkspaceDocHeaders([]);
        $deleteWorkspaceDocHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteWorkspaceDocRequest = new DeleteWorkspaceDocRequest([
            "operatorId" => "xyz"
        ]);
        try {
            $client->deleteWorkspaceDocWithOptions("abc", "def", $deleteWorkspaceDocRequest, $deleteWorkspaceDocHeaders, new RuntimeOptions([]));
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
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
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

  deleteWorkspaceDocHeaders := &dingtalkdoc_1_0.DeleteWorkspaceDocHeaders{}
  deleteWorkspaceDocHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteWorkspaceDocRequest := &dingtalkdoc_1_0.DeleteWorkspaceDocRequest{
    OperatorId: tea.String("xyz"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteWorkspaceDocWithOptions(tea.String("abc"), tea.String("def"), deleteWorkspaceDocRequest, deleteWorkspaceDocHeaders, &util.RuntimeOptions{})
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
const dingtalkdoc_1_0 = require('@alicloud/dingtalk/doc_1_0');
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
    return new dingtalkdoc_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let deleteWorkspaceDocHeaders = new dingtalkdoc_1_0.DeleteWorkspaceDocHeaders({ });
    deleteWorkspaceDocHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let deleteWorkspaceDocRequest = new dingtalkdoc_1_0.DeleteWorkspaceDocRequest({
      operatorId: 'xyz',
    });
    try {
      await client.deleteWorkspaceDocWithOptions('abc', 'def', deleteWorkspaceDocRequest, deleteWorkspaceDocHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceDocHeaders deleteWorkspaceDocHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceDocHeaders();
            deleteWorkspaceDocHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceDocRequest deleteWorkspaceDocRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.DeleteWorkspaceDocRequest
            {
                OperatorId = "xyz",
            };
            try
            {
                client.DeleteWorkspaceDocWithOptions("abc", "def", deleteWorkspaceDocRequest, deleteWorkspaceDocHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

### 响应体示例

```
HTTP/1.1 200 OK
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.invalid | 方法入参校验失败 | 方法入参校验失败，检查是否有必填参数未填，或者unionId是否合法等 |
| 400 | invalidRequest.workspaceNode.notInWorkspace | 节点不在知识库内 | 节点不在知识库内 |
| 403 | forbidden.user.notInOrg | 操作用户不在组织内 | 操作用户不在组织内 |
| 403 | forbidden.accessDenied | 用户无操作权限 | 用户无操作权限 |
| 404 | invalidRequest.resource.notFound | 资源找不到 | 知识库、节点等资源找不到 |
| 404 | invalidRequest.document.deleted | 知识库节点已被删除 | 知识库节点已被删除 |
| 404 | invalidRequest.workspace.deleted | 知识库已被删除 | 知识库已被删除 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
