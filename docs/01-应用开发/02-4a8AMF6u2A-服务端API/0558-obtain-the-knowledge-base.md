---
title: "获取知识库"
source_url: "https://open.dingtalk.com/document/development/obtain-the-knowledge-base"
namespace: "development"
slug: "obtain-the-knowledge-base"
group: "应用开发"
tab: "服务端API"
breadcrumb: "文档/文件 > 知识库 > 知识库管理 > 获取知识库"
doc_id: "vJoDFTplgD"
updated_at: "2026-06-02 17:37:09"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-knowledge-base
> Path: 应用开发 / 服务端API / 文档/文件 > 知识库 > 知识库管理 > 获取知识库
> Updated: 2026-06-02 17:37:09

# 获取知识库

用于获取知识库。调用时通过 GET 请求。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/wiki/workspaces/{workspaceId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Wiki.Workspace.Read-知识库读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用可调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| workspaceId | String | 是 | 知识库id：   - 企业内部应用，可通过调用[获取知识库列表](https://open.dingtalk.com/document/orgapp/get-knowledge-base-list)接口，获取返回参数`workspaceId`字段。 - 第三方企业应用，可通过调用[获取知识库列表](https://open.dingtalk.com/document/isvapp/get-knowledge-base-list)接口，获取返回参数`workspaceId`字段。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| withPermissionRole | Boolean | 否 | 是否获取权限信息：   - true：获取 - false：不获取   **[!NOTE]**    默认值false。 |
| operatorId | String | 是 | 操作人unionId。 |

### 请求示例

HTTP

```
GET /v2.0/wiki/workspaces/MJ0pDSKMV9dO20E4?withPermissionRole=false&operatorId=tXguN309iPhE4roSKPlLURAiEiE HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
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
    public static com.aliyun.dingtalkwiki_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkwiki_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkwiki_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkwiki_2_0.models.GetWorkspaceHeaders getWorkspaceHeaders = new com.aliyun.dingtalkwiki_2_0.models.GetWorkspaceHeaders();
        getWorkspaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkwiki_2_0.models.GetWorkspaceRequest getWorkspaceRequest = new com.aliyun.dingtalkwiki_2_0.models.GetWorkspaceRequest()
                .setWithPermissionRole(false)
                .setOperatorId("tXguN309iPhE4roSKPlLURAiEiE");
        try {
            client.getWorkspaceWithOptions("MJ0pDSKMV9dO20E4", getWorkspaceRequest, getWorkspaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_workspace_headers = dingtalkwiki__2__0_models.GetWorkspaceHeaders()
        get_workspace_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_workspace_request = dingtalkwiki__2__0_models.GetWorkspaceRequest(
            with_permission_role=False,
            operator_id='tXguN309iPhE4roSKPlLURAiEiE'
        )
        try:
            client.get_workspace_with_options('MJ0pDSKMV9dO20E4', get_workspace_request, get_workspace_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_workspace_headers = dingtalkwiki__2__0_models.GetWorkspaceHeaders()
        get_workspace_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_workspace_request = dingtalkwiki__2__0_models.GetWorkspaceRequest(
            with_permission_role=False,
            operator_id='tXguN309iPhE4roSKPlLURAiEiE'
        )
        try:
            await client.get_workspace_with_options_async('MJ0pDSKMV9dO20E4', get_workspace_request, get_workspace_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vwiki_2_0\Models\GetWorkspaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vwiki_2_0\Models\GetWorkspaceRequest;
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
        $getWorkspaceHeaders = new GetWorkspaceHeaders([]);
        $getWorkspaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getWorkspaceRequest = new GetWorkspaceRequest([
            "withPermissionRole" => false,
            "operatorId" => "tXguN309iPhE4roSKPlLURAiEiE"
        ]);
        try {
            $client->getWorkspaceWithOptions("MJ0pDSKMV9dO20E4", $getWorkspaceRequest, $getWorkspaceHeaders, new RuntimeOptions([]));
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
  dingtalkwiki_2_0  "github.com/alibabacloud-go/dingtalk/wiki_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  getWorkspaceHeaders := &dingtalkwiki_2_0.GetWorkspaceHeaders{}
  getWorkspaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getWorkspaceRequest := &dingtalkwiki_2_0.GetWorkspaceRequest{
    WithPermissionRole: tea.Bool(false),
    OperatorId: tea.String("tXguN309iPhE4roSKPlLURAiEiE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetWorkspaceWithOptions(tea.String("MJ0pDSKMV9dO20E4"), getWorkspaceRequest, getWorkspaceHeaders, &util.RuntimeOptions{})
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
import dingtalkwiki_2_0, * as $dingtalkwiki_2_0 from '@alicloud/dingtalk/wiki_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkwiki_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkwiki_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getWorkspaceHeaders = new $dingtalkwiki_2_0.GetWorkspaceHeaders({ });
    getWorkspaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getWorkspaceRequest = new $dingtalkwiki_2_0.GetWorkspaceRequest({
      withPermissionRole: false,
      operatorId: "tXguN309iPhE4roSKPlLURAiEiE",
    });
    try {
      await client.getWorkspaceWithOptions("MJ0pDSKMV9dO20E4", getWorkspaceRequest, getWorkspaceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.GetWorkspaceHeaders getWorkspaceHeaders = new AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.GetWorkspaceHeaders();
            getWorkspaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.GetWorkspaceRequest getWorkspaceRequest = new AlibabaCloud.SDK.Dingtalkwiki_2_0.Models.GetWorkspaceRequest
            {
                WithPermissionRole = false,
                OperatorId = "tXguN309iPhE4roSKPlLURAiEiE",
            };
            try
            {
                client.GetWorkspaceWithOptions("MJ0pDSKMV9dO20E4", getWorkspaceRequest, getWorkspaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| workspace | Object | 知识库。 |
| workspaceId | String | 知识库id(spaceUuid)。 |
| corpId | String | 知识库归属企业的corpId。 |
| teamId | String | 知识库归属知识小组的id。  **[!NOTE]**    不归属任何知识小组的时候, 返回空。 |
| rootNodeId | String | 根节点id(根节点dentryUuid)。 |
| name | String | 知识库名称。 |
| type | String | 知识库类型，枚举值:   - **TEAM**：知识库 - **PERSONAL**：我的文档 |
| description | String | 知识库简介。 |
| url | String | 知识库访问url。 |
| icon | Object | 知识库图标。 |
| type | String | 图标类型，枚举值:   - **URL**：链接 - **EMOJI**：emoji图标 |
| value | String | 图标值：   - 当 type 为 URL 时，返回图标链接。 - 当 type 为 EMOJI 时，返回 emoji 图标的 unicode 值。 |
| cover | String | 知识库封面url。 |
| creatorId | String | 知识库创建者userId。 |
| modifierId | String | 知识库修改者userId。 |
| createTime | String | 知识库创建时间。 |
| modifiedTime | String | 知识库修改时间。 |
| permissionRole | String | 查询人对知识库的权限角色，枚举值:   - **OWNER**：拥有者 - **MANAGER**：管理者 - **EDITOR**：编辑者 - **DOWNLOADER**：可查看下载者 - **READER**：仅可查看者 - **NONE**：无权限者 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "workspace" : {
    "workspaceId" : "MJ0pDSKMV9dO20E4",
    "corpId" : "ding16b241fd05********288",
    "teamId" : "lHiicjNFM2iSFYSdz2iPuI8ZwiEiE",
    "rootNodeId" : "ydxXB52LJqqK7xxNTXyo390kJqjMp697",
    "name" : "workspace_name",
    "type" : "TEAM",
    "description" : "workspace_description",
    "url" : "workspace_url",
    "icon" : {
      "type" : "URL",
      "value" : "https://example/file-manage-files/zh-CN/202***13/ldet/avatar3.jpg"
    },
    "cover" : "https://example/file-manage-files/zh-CN/202***13/ldet/XXXX.jpg",
    "creatorId" : "01472825524039877041",
    "modifierId" : "01472825524039877041",
    "createTime" : "2023-05-15T11:29Z",
    "modifiedTime" : "2023-05-15T11:29Z",
    "permissionRole" : "READER"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | %s | 参数错误 |
| 400 | isNotWorkspace | %s | 不是知识库 |
| 403 | permissionDenied | %s | 当前用户无此操作权限 |
| 404 | workspaceNotExist | %s | 知识库不存在 |
| 500 | systemError | %s | 服务繁忙，请稍后重试 |
| 500 | unknownError | Unknown Error | 未知错误 |
| 503 | operationTimeout | %s | 请求超时 |
