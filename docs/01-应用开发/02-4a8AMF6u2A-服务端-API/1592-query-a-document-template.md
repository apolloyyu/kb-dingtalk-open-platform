---
title: "查询文档模板"
source_url: "https://open.dingtalk.com/document/development/query-a-document-template"
namespace: "development"
slug: "query-a-document-template"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 知识库 > 知识库目录树管理 > 查询文档模板"
doc_id: "dD9zsew7Rr"
updated_at: "2026-08-25 09:38:47"
---

> Source: https://open.dingtalk.com/document/development/query-a-document-template
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 知识库 > 知识库目录树管理 > 查询文档模板
> Updated: 2026-08-25 09:38:47

# 查询文档模板

调用本接口，查询知识库内的文档模板，包括推荐模板、我的模板和团队模板。

> **[!IMPORTANT]**
>
> 本接口后续将维持现有功能且不再新增能力，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v1.0/doc/templates?operatorId=String&templateType=String&workspaceId=String&nextToken=String&maxResults=Integer HTTP/1.1
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
| operatorId | String | 是 | 操作用户的unionId，调用[查询用户详情](0056-query-user-details.md)接口获取。 |
| templateType | String | 是 | 模板类型，支持以下值：   - **public\_template**：推荐模板 - **user\_template**：个人模板 - **team\_template**：知识库模板 |
| workspaceId | String | 否 | 知识库ID，调用[新建知识库](1586-create-a-team-space.md)接口或者[查询用户有权限的知识库列表](1588-querying-the-list-of-user-team-spaces.md)接口获取的workspaceId字段值。  **[!NOTE]**  当参数`templateType=team_template`，该参数必传。 |
| nextToken | String | 否 | 分页游标。   - 如果是首次调用，该参数不传。 - 如果是非首次调用，该参数传上次调用时返回的nextToken。 |
| maxResults | Integer | 是 | 每页最大条目数，最大值10。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| hasMore | Boolean | 是否还有更多模板。   - **true**：是 - **false**：否 |
| nextToken | String | 分页游标。 |
| templateList | Array | 模板信息列表。 |
| id | String | 模板Id。 |
| title | String | 模板标题。 |
| docType | String | 模板的文档类型。   - **DOC**：文档 - **WORKBOOK**：表格 - **MIND**：脑图 |
| coverUrl | String | 模板预览页面的URL。 |
| templateType | String | 模板类型。   - **public\_template**：推荐模板 - **user\_template**：个人模板 - **team\_template**：知识库模板 |
| workspaceId | String | 模板归属空间Id。  **[!NOTE]**  当`templateType=team_template`时，才返回该字段。 |
| createTime | Long | 模板创建的时间戳，单位毫秒。 |
| updateTime | Long | 模板修改的时间戳，单位毫秒。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/doc/templates?operatorId=xxxx&templateType=public_template&workspaceId=xxxxx&nextToken=xxxxxxxxx&maxResults=10 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json
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
        com.aliyun.dingtalkdoc_1_0.models.ListTemplateHeaders listTemplateHeaders = new com.aliyun.dingtalkdoc_1_0.models.ListTemplateHeaders();
        listTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkdoc_1_0.models.ListTemplateRequest listTemplateRequest = new com.aliyun.dingtalkdoc_1_0.models.ListTemplateRequest()
                .setOperatorId("xxxx")
                .setTemplateType("public_template")
                .setWorkspaceId("xxxxx")
                .setNextToken("xxxxxxxxx")
                .setMaxResults(10);
        try {
            client.listTemplateWithOptions(listTemplateRequest, listTemplateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        list_template_headers = dingtalkdoc__1__0_models.ListTemplateHeaders()
        list_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_template_request = dingtalkdoc__1__0_models.ListTemplateRequest(
            operator_id='xxxx',
            template_type='public_template',
            workspace_id='xxxxx',
            next_token='xxxxxxxxx',
            max_results=10
        )
        try:
            client.list_template_with_options(list_template_request, list_template_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_template_headers = dingtalkdoc__1__0_models.ListTemplateHeaders()
        list_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_template_request = dingtalkdoc__1__0_models.ListTemplateRequest(
            operator_id='xxxx',
            template_type='public_template',
            workspace_id='xxxxx',
            next_token='xxxxxxxxx',
            max_results=10
        )
        try:
            await client.list_template_with_options_async(list_template_request, list_template_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\ListTemplateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdoc_1_0\Models\ListTemplateRequest;
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
        $listTemplateHeaders = new ListTemplateHeaders([]);
        $listTemplateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listTemplateRequest = new ListTemplateRequest([
            "operatorId" => "xxxx",
            "templateType" => "public_template",
            "workspaceId" => "xxxxx",
            "nextToken" => "xxxxxxxxx",
            "maxResults" => 10
        ]);
        try {
            $client->listTemplateWithOptions($listTemplateRequest, $listTemplateHeaders, new RuntimeOptions([]));
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

  listTemplateHeaders := &dingtalkdoc_1_0.ListTemplateHeaders{}
  listTemplateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listTemplateRequest := &dingtalkdoc_1_0.ListTemplateRequest{
    OperatorId: tea.String("xxxx"),
    TemplateType: tea.String("public_template"),
    WorkspaceId: tea.String("xxxxx"),
    NextToken: tea.String("xxxxxxxxx"),
    MaxResults: tea.Int32(10),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListTemplateWithOptions(listTemplateRequest, listTemplateHeaders, &util.RuntimeOptions{})
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
    let listTemplateHeaders = new $dingtalkdoc_1_0.ListTemplateHeaders({ });
    listTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listTemplateRequest = new $dingtalkdoc_1_0.ListTemplateRequest({
      operatorId: "xxxx",
      templateType: "public_template",
      workspaceId: "xxxxx",
      nextToken: "xxxxxxxxx",
      maxResults: 10,
    });
    try {
      await client.listTemplateWithOptions(listTemplateRequest, listTemplateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.ListTemplateHeaders listTemplateHeaders = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.ListTemplateHeaders();
            listTemplateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.ListTemplateRequest listTemplateRequest = new AlibabaCloud.SDK.Dingtalkdoc_1_0.Models.ListTemplateRequest
            {
                OperatorId = "xxxx",
                TemplateType = "public_template",
                WorkspaceId = "xxxxx",
                NextToken = "xxxxxxxxx",
                MaxResults = 10,
            };
            try
            {
                client.ListTemplateWithOptions(listTemplateRequest, listTemplateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

python2

```
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

import sys

from alibabacloud_dingtalkdoc_1_0.client import Client as dingtalkdoc_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalkdoc_1_0 import models as dingtalkdoc__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample(object):
    def __init__(self):
        pass

    @staticmethod
    def create_client():
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
    def main(args):
        client = Sample.create_client()
        list_template_headers = dingtalkdoc__1__0_models.ListTemplateHeaders()
        list_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_template_request = dingtalkdoc__1__0_models.ListTemplateRequest(
            operator_id='xxxx',
            template_type='public_template',
            workspace_id='xxxxx',
            next_token='xxxxxxxxx',
            max_results=10
        )
        try:
            client.list_template_with_options(list_template_request, list_template_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

if __name__ == '__main__':
    Sample.main(sys.argv[1:])
```

Swift

```
#!/usr/bin/env xcrun swift

import Cocoa
import Foundation
import Tea
import TeaUtils
import AlibabacloudDingtalkdoc10
import AlibabacloudOpenApi

open class Client {
    public static func createClient() throws -> AlibabacloudDingtalkdoc10.Client {
        var config: AlibabacloudOpenApi.Config = AlibabacloudOpenApi.Config([:])
        config.protocol_ = "https"
        config.regionId = "central"
        return AlibabacloudDingtalkdoc10.Client(config)
    }

    @available(macOS 10.15, iOS 13, tvOS 13, watchOS 6, *)
    public static func main(_ args: [String]?) async throws -> Void {
        var client: AlibabacloudDingtalkdoc10.Client = try Client.createClient()
        var listTemplateHeaders: AlibabacloudDingtalkdoc10.ListTemplateHeaders = AlibabacloudDingtalkdoc10.ListTemplateHeaders([:])
        listTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>"
        var listTemplateRequest: AlibabacloudDingtalkdoc10.ListTemplateRequest = AlibabacloudDingtalkdoc10.ListTemplateRequest([
            "operatorId": "xxxx",
            "templateType": "public_template",
            "workspaceId": "xxxxx",
            "nextToken": "xxxxxxxxx",
            "maxResults": 10
        ])
        do {
            try await client.listTemplateWithOptions(listTemplateRequest as! AlibabacloudDingtalkdoc10.ListTemplateRequest, listTemplateHeaders as! AlibabacloudDingtalkdoc10.ListTemplateHeaders, TeaUtils.RuntimeOptions([:]))
        }
        catch {
            if error is Tea.TeaError {
                var err = error as! Tea.TeaError
                if (!TeaUtils.Client.empty(err.code) && !TeaUtils.Client.empty(err.message)) {
                }
            } else {
                throw error
            }
        }
    }
}

Client.main(CommandLine.arguments)
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "hasMore" : false,
  "nextToken" : "xxxxxx",
  "templateList" : [ {
    "id" : "123xxxxxx",
    "title" : "我的模版",
    "docType" : "DOC",
    "coverUrl" : "http://xxxxx",
    "templateType" : "user_template",
    "workspaceId" : "xxxxxx",
    "createTime" : 1596506100000,
    "updateTime" : 1596506100000
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.inputArgs.overLimit | 批量操作数量超过限制 | 批量接口操作数量超限 |
| 400 | invalidRequest.inputArgs.invalid | 方法入参校验失败 | 方法入参校验失败，检查是否有必填参数未填，或者unionId是否合法等 |
| 403 | forbidden.accessDenied | 用户无操作权限 | 当前用户无此操作权限 |
| 404 | invalidRequest.resource.notFound | 资源找不到 | 资源找不到 |
| 500 | internalError | 系统内部错误 | 系统内部错误 |
