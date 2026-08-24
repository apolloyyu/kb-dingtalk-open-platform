---
title: "下载审批附件"
source_url: "https://open.dingtalk.com/document/development/download-an-approval-attachment"
namespace: "development"
slug: "download-an-approval-attachment"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批钉盘空间&附件 > 下载审批附件"
doc_id: "5AivRFT75Z"
updated_at: "2026-06-03 10:12:33"
---

> Source: https://open.dingtalk.com/document/development/download-an-approval-attachment
> Path: 应用开发 / 服务端API / OA 审批 > 官方 OA 审批 > 审批钉盘空间&附件 > 下载审批附件
> Updated: 2026-06-03 10:12:33

# 下载审批附件

调用本接口，获取审批文件下载授权，并且生成下载链接。

## **接口调用说明**

- 如果审批单是手动在钉钉客户端发起的，手动选择本地文件作为附件，调用本接口获取的附件下载地址的格式为#zifgs49xxxxx.file。需要与[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口结合使用，获取实例详情接口得到附件的fileName和fileType，按照本接口返回的#zifgs49xxxxx.file进行名称和后缀替换，该附件才可正常打开。
- 附件文件大小不能为0，否则不支持获取下载链接。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances/spaces/files/urls/download |
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
| processInstanceId | String | 是 | 审批实例ID。   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| fileId | String | 是 | 文件fileId，调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取`fileId`参数值。      文件id是审批组件中上传的fileId（如下图所示），评论中上传的附件fileId暂不支持获取下载链接。 |
| withCommentAttatchment | Boolean | 否 | 是否包含评论中的附件，默认忽略评论中附件 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processInstances/spaces/files/urls/download HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processInstanceId" : "a17444d1-075b-4a4d-xxxx",
  "fileId" : "111"
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
        com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileHeaders grantProcessInstanceForDownloadFileHeaders = new com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileHeaders();
        grantProcessInstanceForDownloadFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileRequest grantProcessInstanceForDownloadFileRequest = new com.aliyun.dingtalkworkflow_1_0.models.GrantProcessInstanceForDownloadFileRequest()
                .setProcessInstanceId("a17444d1-075b-4a4d-xxxx")
                .setFileId("111");
        try {
            client.grantProcessInstanceForDownloadFileWithOptions(grantProcessInstanceForDownloadFileRequest, grantProcessInstanceForDownloadFileHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        grant_process_instance_for_download_file_headers = dingtalkworkflow__1__0_models.GrantProcessInstanceForDownloadFileHeaders()
        grant_process_instance_for_download_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        grant_process_instance_for_download_file_request = dingtalkworkflow__1__0_models.GrantProcessInstanceForDownloadFileRequest(
            process_instance_id='a17444d1-075b-4a4d-xxxx',
            file_id='111'
        )
        try:
            client.grant_process_instance_for_download_file_with_options(grant_process_instance_for_download_file_request, grant_process_instance_for_download_file_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        grant_process_instance_for_download_file_headers = dingtalkworkflow__1__0_models.GrantProcessInstanceForDownloadFileHeaders()
        grant_process_instance_for_download_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        grant_process_instance_for_download_file_request = dingtalkworkflow__1__0_models.GrantProcessInstanceForDownloadFileRequest(
            process_instance_id='a17444d1-075b-4a4d-xxxx',
            file_id='111'
        )
        try:
            await client.grant_process_instance_for_download_file_with_options_async(grant_process_instance_for_download_file_request, grant_process_instance_for_download_file_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GrantProcessInstanceForDownloadFileHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\GrantProcessInstanceForDownloadFileRequest;
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
        $grantProcessInstanceForDownloadFileHeaders = new GrantProcessInstanceForDownloadFileHeaders([]);
        $grantProcessInstanceForDownloadFileHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $grantProcessInstanceForDownloadFileRequest = new GrantProcessInstanceForDownloadFileRequest([
            "processInstanceId" => "a17444d1-075b-4a4d-xxxx",
            "fileId" => "111"
        ]);
        try {
            $client->grantProcessInstanceForDownloadFileWithOptions($grantProcessInstanceForDownloadFileRequest, $grantProcessInstanceForDownloadFileHeaders, new RuntimeOptions([]));
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

  grantProcessInstanceForDownloadFileHeaders := &dingtalkworkflow_1_0.GrantProcessInstanceForDownloadFileHeaders{}
  grantProcessInstanceForDownloadFileHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  grantProcessInstanceForDownloadFileRequest := &dingtalkworkflow_1_0.GrantProcessInstanceForDownloadFileRequest{
    ProcessInstanceId: tea.String("a17444d1-075b-4a4d-xxxx"),
    FileId: tea.String("111"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GrantProcessInstanceForDownloadFileWithOptions(grantProcessInstanceForDownloadFileRequest, grantProcessInstanceForDownloadFileHeaders, &util.RuntimeOptions{})
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
    let grantProcessInstanceForDownloadFileHeaders = new $dingtalkworkflow_1_0.GrantProcessInstanceForDownloadFileHeaders({ });
    grantProcessInstanceForDownloadFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let grantProcessInstanceForDownloadFileRequest = new $dingtalkworkflow_1_0.GrantProcessInstanceForDownloadFileRequest({
      processInstanceId: "a17444d1-075b-4a4d-xxxx",
      fileId: "111",
    });
    try {
      await client.grantProcessInstanceForDownloadFileWithOptions(grantProcessInstanceForDownloadFileRequest, grantProcessInstanceForDownloadFileHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GrantProcessInstanceForDownloadFileHeaders grantProcessInstanceForDownloadFileHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GrantProcessInstanceForDownloadFileHeaders();
            grantProcessInstanceForDownloadFileHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GrantProcessInstanceForDownloadFileRequest grantProcessInstanceForDownloadFileRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.GrantProcessInstanceForDownloadFileRequest
            {
                ProcessInstanceId = "a17444d1-075b-4a4d-xxxx",
                FileId = "111",
            };
            try
            {
                client.GrantProcessInstanceForDownloadFileWithOptions(grantProcessInstanceForDownloadFileRequest, grantProcessInstanceForDownloadFileHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| spaceId | Long | 钉盘空间ID。 |
| fileId | String | 文件ID。 |
| downloadUri | String | 文件下载地址。      文件下载地址有效期15分钟。 |
| success | Boolean | 接口调用是否成功。   - **true**：成功 - **false**：失败 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "spaceId" : 3996960664,
    "fileId" : "26748422566",
    "downloadUri" : "http://lippi-space-zjk.oss-cn-zhangjiakou.aliyuncs.com/xxxxx"
  },
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 下载审批附件参数错误 | 下载审批附件参数错误 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | invalidProcessInstanceId | 实例id不能为空 | 实例id不能为空 |
| 400 | hsfIntegrationErrorCspaceGetCustomSpace | 获取钉盘space的信息失败 | 获取钉盘space的信息失败 |
| 400 | hsfIntegrationErrorCspaceGetSimpleMicroAppByRelatedAppId | 根据relatedAppId查询获取微应用信息失败 | 根据relatedAppId查询获取微应用信息失败 |
| 400 | hsfIntegrationErrorCspaceDentryServiceGrant | 授权访问钉盘失败 | 授权访问钉盘失败 |
| 400 | hsfIntegrationErrorCspace | 钉盘附件依赖三方错误 | 钉盘附件依赖三方错误 |
| 400 | invalidFileId | 审批附件fileId不能为空 | 审批附件fileId不能为空 |
| 400 | processInstNotExist | 审批实例不存在 | 审批实例不存在 |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | processNotExist | 审批流不存在 | 审批流不存在 |
| 400 | processGetFailedByParameter | 无操作审批流的权限，请检查审批实例或者模板是否正确 | 无操作审批流的权限，请检查审批实例或者模板是否正确 |
| 400 | hsfIntegrationErrorCspaceDentryServiceGenerateDownloadPresignedUrl | 产生文件下载的链接失败 | 产生文件下载的链接失败 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
