---
title: "创建知识库文档"
source_url: "https://open.dingtalk.com/document/development/create-team-space-document"
namespace: "development"
slug: "create-team-space-document"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "文档/文件 > 知识库 > 知识库目录树管理 > 创建知识库文档"
doc_id: "cS9vmubdzf"
updated_at: "2026-06-03 10:13:09"
---

> Source: https://open.dingtalk.com/document/development/create-team-space-document
> Path: 应用开发 / 服务端 API / 文档/文件 > 知识库 > 知识库目录树管理 > 创建知识库文档
> Updated: 2026-06-03 10:13:09

# 创建知识库文档

调用本接口，在知识库内创建文档或者文件夹。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/doc/workspaces/{workspaceId}/docs |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Document.WorkspaceDocument.Write-知识库文档写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workspaceId | String | 是 | 知识库ID，调用[新建知识库](0557-new-knowledge-base.md)接口或者[获取知识库列表](0560-get-knowledge-base-list.md)接口获取的workspaceId字段值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 文档名称。 |
| docType | String | 是 | 文档类型，取值：   - **DOC**：文字 - **WORKBOOK**：表格 - **MIND**：脑图 - **FOLDER**：文件夹 |
| operatorId | String | 是 | 用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| parentNodeId | String | 否 | 父节点Id，调用[获取节点列表](0571-get-node-list.md)接口获取DentryModel参数值。如果不传，默认在根目录创建。      父节点可以是文件夹，也可以是普通的文档。 |
| templateId | String | 否 | 文档模板id。 |
| templateType | String | 否 | 文档模板类型，支持以下值：   - **public\_template**：推荐模板 - **team\_template**：团队模板 - **user\_template**：个人模板 |

### 请求示例

HTTP

```
POST /v1.0/doc/workspaces/YRBGvyxxx/docs HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:7dc9ecxxx
Content-Type:application/json

{
  "name" : "文档",
  "docType" : "DOC",
  "operatorId" : "Q2xwPOxxx",
  "parentNodeId" : "YRBGv0Ye",
  "templateId" : "123243",
  "templateType" : "team_template"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdoc_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdoc_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdoc_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkdoc_1_0.models.CreateWorkspaceDocHeaders createWorkspaceDocHeaders = new com.aliyun.dingtalkdoc_1_0.models.CreateWorkspaceDocHeaders();
        createWorkspaceDocHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.CreateWorkspaceDocRequest createWorkspaceDocRequest = new com.aliyun.dingtalkdoc_1_0.models.CreateWorkspaceDocRequest()
                .setName("文档")
                .setDocType("DOC")
                .setOperatorId("Q2xwPOxxx")
                .setParentNodeId("YRBGv0Ye")
                .setTemplateId("123243")
                .setTemplateType("team_template");
        try {
            client.createWorkspaceDocWithOptions("YRBGvyxxx", createWorkspaceDocRequest, createWorkspaceDocHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_workspace_doc_headers = dingtalkdoc__1__0_models.CreateWorkspaceDocHeaders()
        create_workspace_doc_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_workspace_doc_request = dingtalkdoc__1__0_models.CreateWorkspaceDocRequest(
            name='文档',
            doc_type='DOC',
            operator_id='Q2xwPOxxx',
            parent_node_id='YRBGv0Ye',
            template_id='123243',
            template_type='team_template'
        )
        try:
            client.create_workspace_doc_with_options('YRBGvyxxx', create_workspace_doc_request, create_workspace_doc_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_workspace_doc_headers = dingtalkdoc__1__0_models.CreateWorkspaceDocHeaders()
        create_workspace_doc_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_workspace_doc_request = dingtalkdoc__1__0_models.CreateWorkspaceDocRequest(
            name='文档',
            doc_type='DOC',
            operator_id='Q2xwPOxxx',
            parent_node_id='YRBGv0Ye',
            template_id='123243',
            template_type='team_template'
        )
        try:
            await client.create_workspace_doc_with_options_async('YRBGvyxxx', create_workspace_doc_request, create_workspace_doc_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateWorkspaceDocHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\CreateWorkspaceDocRequest;
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
        $createWorkspaceDocHeaders = new CreateWorkspaceDocHeaders([]);
        $createWorkspaceDocHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createWorkspaceDocRequest = new CreateWorkspaceDocRequest([
            "name" => "文档",
            "docType" => "DOC",
            "operatorId" => "Q2xwPOxxx",
            "parentNodeId" => "YRBGv0Ye",
            "templateId" => "123243",
            "templateType" => "team_template"
        ]);
        try {
            $client->createWorkspaceDocWithOptions("YRBGvyxxx", $createWorkspaceDocRequest, $createWorkspaceDocHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkdoc_1_0  "github.com/alibabacloud-go/dingtalk/doc_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
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

  createWorkspaceDocHeaders := &dingtalkdoc_1_0.CreateWorkspaceDocHeaders{}
  createWorkspaceDocHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createWorkspaceDocRequest := &dingtalkdoc_1_0.CreateWorkspaceDocRequest{
    Name: tea.String("文档"),
    DocType: tea.String("DOC"),
    OperatorId: tea.String("Q2xwPOxxx"),
    ParentNodeId: tea.String("YRBGv0Ye"),
    TemplateId: tea.String("123243"),
    TemplateType: tea.String("team_template"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateWorkspaceDocWithOptions(tea.String("YRBGvyxxx"), createWorkspaceDocRequest, createWorkspaceDocHeaders, &util.RuntimeOptions{})
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
    let createWorkspaceDocHeaders = new $dingtalkdoc_1_0.CreateWorkspaceDocHeaders({ });
    createWorkspaceDocHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createWorkspaceDocRequest = new $dingtalkdoc_1_0.CreateWorkspaceDocRequest({
      name: "文档",
      docType: "DOC",
      operatorId: "Q2xwPOxxx",
      parentNodeId: "YRBGv0Ye",
      templateId: "123243",
      templateType: "team_template",
    });
    try {
      await client.createWorkspaceDocWithOptions("YRBGvyxxx", createWorkspaceDocRequest, createWorkspaceDocHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateWorkspaceDocHeaders createWorkspaceDocHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateWorkspaceDocHeaders();
            createWorkspaceDocHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateWorkspaceDocRequest createWorkspaceDocRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.CreateWorkspaceDocRequest
            {
                Name = "文档",
                DocType = "DOC",
                OperatorId = "Q2xwPOxxx",
                ParentNodeId = "YRBGv0Ye",
                TemplateId = "123243",
                TemplateType = "team_template",
            };
            try
            {
                client.CreateWorkspaceDocWithOptions("YRBGvyxxx", createWorkspaceDocRequest, createWorkspaceDocHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| workspaceId | String | 知识库ID。 |
| nodeId | String | 知识库文档ID。 |
| docKey | String | 文档docKey。 |
| url | String | 文档URL。 |
| dentryUuid | String | 当前返回的文件Uuid |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "workspaceId" : "YRBGvy",
  "nodeId" : "YRBGv0Ye",
  "docKey" : "QoJGq7xxx",
  "url" : "https://xxx/workspaceId/docs/nodeId",
  "dentryUuid" : "ydxXB52LJqqK7xxNTX*****697"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.workspaceNode.nameConflict | 知识库文档名称冲突 | 知识库文档名称冲突 |
| 400 | invalidRequest.inputArgs.invalid | 方法入参校验失败 | 方法入参校验失败，检查是否有必填参数未填，或者unionId是否合法等 |
| 400 | invalidRequest.workspaceNode.parentNotFound | 父节点不存在 | 父节点不存在 |
| 400 | invalidRequest.template.notFound | 文档模板不存在 | 文档模板不存在 |
| 403 | forbidden.user.notInOrg | 操作用户不在组织内 | 操作用户不在组织内 |
| 403 | forbidden.accessDenied | 用户无操作权限 | 用户无操作权限 |
| 404 | invalidRequest.resource.notFound | 资源找不到 | 资源找不到 |
| 404 | invalidRequest.workspace.deleted | 知识库已被删除 | 知识库已被删除 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
