---
title: "授权下载审批钉盘文件"
source_url: "https://open.dingtalk.com/document/development/download-the-approval-nail-file"
namespace: "development"
slug: "download-the-approval-nail-file"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批钉盘空间&附件 > 授权下载审批钉盘文件"
doc_id: "dR8ed9ouC2"
updated_at: "2026-06-03 10:12:32"
---

> Source: https://open.dingtalk.com/document/development/download-the-approval-nail-file
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批钉盘空间&附件 > 授权下载审批钉盘文件
> Updated: 2026-06-03 10:12:32

# 授权下载审批钉盘文件

调用本接口，根据钉盘空间spaceId和文件fileId对钉盘文件进行授权审批钉盘空间下载权限。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances/spaces/files/authDownload |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Instance.Write-工作流实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 授权的用户userId。 |
| fileInfos | Array | 是 | 授权的钉盘文件信息列表。支持批量授权，最大列表长度为10。 |
| fileId | String | 是 | 文件fileId，调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取`fileId`参数值。      文件id是审批组件中上传的fileId。 |
| spaceId | Long | 是 | 审批钉盘空间spaceId，可调用[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口获取`spaceId`参数值。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processInstances/spaces/files/authDownload HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "userId" : "user123",
  "fileInfos" : [ {
    "fileId" : "B1oQixxxx",
    "spaceId" : 111
  } ]
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthHeaders addApproveDentryAuthHeaders = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthHeaders();
        addApproveDentryAuthHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos fileInfos0 = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos()
                .setFileId("B1oQixxxx")
                .setSpaceId(111L);
        com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest addApproveDentryAuthRequest = new com.aliyun.dingtalkworkflow_1_0.models.AddApproveDentryAuthRequest()
                .setUserId("user123")
                .setFileInfos(java.util.Arrays.asList(
                    fileInfos0
                ));
        try {
            client.addApproveDentryAuthWithOptions(addApproveDentryAuthRequest, addApproveDentryAuthHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_approve_dentry_auth_headers = dingtalkworkflow__1__0_models.AddApproveDentryAuthHeaders()
        add_approve_dentry_auth_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_infos_0 = dingtalkworkflow__1__0_models.AddApproveDentryAuthRequestFileInfos(
            file_id='B1oQixxxx',
            space_id=111
        )
        add_approve_dentry_auth_request = dingtalkworkflow__1__0_models.AddApproveDentryAuthRequest(
            user_id='user123',
            file_infos=[
                file_infos_0
            ]
        )
        try:
            client.add_approve_dentry_auth_with_options(add_approve_dentry_auth_request, add_approve_dentry_auth_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_approve_dentry_auth_headers = dingtalkworkflow__1__0_models.AddApproveDentryAuthHeaders()
        add_approve_dentry_auth_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_infos_0 = dingtalkworkflow__1__0_models.AddApproveDentryAuthRequestFileInfos(
            file_id='B1oQixxxx',
            space_id=111
        )
        add_approve_dentry_auth_request = dingtalkworkflow__1__0_models.AddApproveDentryAuthRequest(
            user_id='user123',
            file_infos=[
                file_infos_0
            ]
        )
        try:
            await client.add_approve_dentry_auth_with_options_async(add_approve_dentry_auth_request, add_approve_dentry_auth_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddApproveDentryAuthHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddApproveDentryAuthRequest\fileInfos;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddApproveDentryAuthRequest;
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
        $addApproveDentryAuthHeaders = new AddApproveDentryAuthHeaders([]);
        $addApproveDentryAuthHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $fileInfos0 = new fileInfos([
            "fileId" => "B1oQixxxx",
            "spaceId" => 111
        ]);
        $addApproveDentryAuthRequest = new AddApproveDentryAuthRequest([
            "userId" => "user123",
            "fileInfos" => [
                $fileInfos0
            ]
        ]);
        try {
            $client->addApproveDentryAuthWithOptions($addApproveDentryAuthRequest, $addApproveDentryAuthHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addApproveDentryAuthHeaders := &dingtalkworkflow_1_0.AddApproveDentryAuthHeaders{}
  addApproveDentryAuthHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  fileInfos0 := &dingtalkworkflow_1_0.AddApproveDentryAuthRequestFileInfos{
    FileId: tea.String("B1oQixxxx"),
    SpaceId: tea.Int64(111),
  }
  addApproveDentryAuthRequest := &dingtalkworkflow_1_0.AddApproveDentryAuthRequest{
    UserId: tea.String("user123"),
    FileInfos: []*dingtalkworkflow_1_0.AddApproveDentryAuthRequestFileInfos{fileInfos0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddApproveDentryAuthWithOptions(addApproveDentryAuthRequest, addApproveDentryAuthHeaders, &util.RuntimeOptions{})
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
import dingtalkworkflow_1_0, * as $dingtalkworkflow_1_0 from '@alicloud/dingtalk/workflow_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkflow_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkflow_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addApproveDentryAuthHeaders = new $dingtalkworkflow_1_0.AddApproveDentryAuthHeaders({ });
    addApproveDentryAuthHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let fileInfos0 = new $dingtalkworkflow_1_0.AddApproveDentryAuthRequestFileInfos({
      fileId: "B1oQixxxx",
      spaceId: 111,
    });
    let addApproveDentryAuthRequest = new $dingtalkworkflow_1_0.AddApproveDentryAuthRequest({
      userId: "user123",
      fileInfos: [
        fileInfos0
      ],
    });
    try {
      await client.addApproveDentryAuthWithOptions(addApproveDentryAuthRequest, addApproveDentryAuthHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthHeaders addApproveDentryAuthHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthHeaders();
            addApproveDentryAuthHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos fileInfos0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos
            {
                FileId = "B1oQixxxx",
                SpaceId = 111,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthRequest addApproveDentryAuthRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthRequest
            {
                UserId = "user123",
                FileInfos = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddApproveDentryAuthRequest.AddApproveDentryAuthRequestFileInfos>
                {
                    fileInfos0
                },
            };
            try
            {
                client.AddApproveDentryAuthWithOptions(addApproveDentryAuthRequest, addApproveDentryAuthHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |
| result | Boolean | 授权是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 授权下载审批钉盘文件参数错误 | 授权下载审批钉盘文件参数错误 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | invalidFileInfos | 授权下载审批钉盘文件，授权的钉盘文件信息列表不能为空 | 授权下载审批钉盘文件，授权的钉盘文件信息列表不能为空 |
| 400 | invalidParameterCspace | 使用授权码方式认证时，isvOrgId不能为空 | 使用授权码方式认证时，isvOrgId不能为空 |
| 400 | hsfIntegrationErrorCspaceGetCustomSpace | 获取钉盘space的信息失败 | 获取钉盘space的信息失败 |
| 400 | hsfIntegrationErrorCspaceGetSimpleMicroAppByRelatedAppId | 根据relatedAppId查询获取微应用信息失败 | 根据relatedAppId查询获取微应用信息失败 |
| 400 | hsfIntegrationErrorCspaceDentryServiceGrant | 授权访问钉盘失败 | 授权访问钉盘失败 |
| 400 | hsfIntegrationErrorCspace | 钉盘附件依赖三方错误 | 钉盘附件依赖三方错误 |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | hsfIntegrationErrorCspaceDentryServiceInfo | 查看具体文件信息失败 | 查看具体文件信息失败 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
