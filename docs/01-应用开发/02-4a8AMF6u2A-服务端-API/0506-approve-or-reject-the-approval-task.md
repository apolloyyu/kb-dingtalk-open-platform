---
title: "同意或拒绝审批任务"
source_url: "https://open.dingtalk.com/document/development/approve-or-reject-the-approval-task"
namespace: "development"
slug: "approve-or-reject-the-approval-task"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批任务 > 同意或拒绝审批任务"
doc_id: "sTnrg5oUWi"
updated_at: "2026-06-03 10:12:33"
---

> Source: https://open.dingtalk.com/document/development/approve-or-reject-the-approval-task
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批任务 > 同意或拒绝审批任务
> Updated: 2026-06-03 10:12:33

# 同意或拒绝审批任务

调用本接口，根据指定模板ID、审批实例ID、任务节点ID和操作人userId，对单个审批任务进行处理。

## **接口调用说明**

1. 审批流程可以包含多个审批节点，单个审批节点可能包含一个或多个审批任务。操作单个审批任务，不代表审批流程结束。

   - 审批流程只有一个审批人，对单个审批任务操作同意或拒绝，审批流程结束。

     ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1064156361/p349526.png)
   - 审批流程有多个审批人，整个审批流程受多个任务影响。

     - 对单个审批任务操作拒绝，审批流程结束。
     - 对单个审批任务操作同意，审批流程转到下一个审批人。

       ![](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/1064156361/p349521.png)
2. 添加审批评论附件需将文件上传至审批钉盘空间，可以获取到接口参数spaceId，fileType，fileName，fileId，fileSize。获取方式如下：

   1. 调用[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
   2. 根据审批钉盘空间spaceId，网页应用（H5微应用）/小程序，通过[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)获取钉盘附件file的信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances/execute |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Workflow.Instance.Write-工作流实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | 审批实例ID：   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用调用[获取审批实例ID列表](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| remark | String | 否 | 审批意见，最大长度1024字符，可为空。 |
| result | String | 是 | 审批操作，取值：   - **agree**：同意 - **refuse**：拒绝 |
| actionerUserId | String | 是 | 操作人userId，可通过调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取`userId`参数值。 |
| taskId | Long | 是 | 任务ID，可通过调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取`taskId`参数值。 |
| file | Object | 否 | 文件。 |
| photos | Array of String | 否 | 图片URL地址，最大长度：1024字符。 |
| attachments | Array | 否 | 附件列表，最多元素个数：20。 |
| spaceId | String | 否 | 钉盘空间ID。      请参见本文接口调用说明。 |
| fileSize | String | 否 | 文件大小。      请参见本文接口调用说明。 |
| fileId | String | 否 | 文件ID，最大长度：256字符。      请参见本文接口调用说明。 |
| fileName | String | 否 | 文件名称，最大长度：256字符。      请参见本文接口调用说明。 |
| fileType | String | 否 | 文件类型。      请参见本文接口调用说明。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processInstances/execute HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processInstanceId" : "a171de6c-8bxxxx",
  "remark" : "同意。",
  "result" : "agree",
  "actionerUserId" : "133743186427339452",
  "taskId" : 67583405630,
  "file" : {
    "photos" : [ "https://url1" ],
    "attachments" : [ {
      "spaceId" : "123",
      "fileSize" : "1024",
      "fileId" : "B1oQixxxx",
      "fileName" : "文件名称。",
      "fileType" : "file"
    } ]
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceHeaders executeProcessInstanceHeaders = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceHeaders();
        executeProcessInstanceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFileAttachments fileAttachments0 = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFileAttachments()
                .setSpaceId("123")
                .setFileSize("1024")
                .setFileId("B1oQixxxx")
                .setFileName("文件名称。")
                .setFileType("file");
        com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile file = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile()
                .setPhotos(java.util.Arrays.asList(
                    "https://url1"
                ))
                .setAttachments(java.util.Arrays.asList(
                    fileAttachments0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest executeProcessInstanceRequest = new com.aliyun.dingtalkworkflow_1_0.models.ExecuteProcessInstanceRequest()
                .setProcessInstanceId("a171de6c-8bxxxx")
                .setRemark("同意。")
                .setResult("agree")
                .setActionerUserId("133743186427339452")
                .setTaskId(67583405630L)
                .setFile(file);
        try {
            client.executeProcessInstanceWithOptions(executeProcessInstanceRequest, executeProcessInstanceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        execute_process_instance_headers = dingtalkworkflow__1__0_models.ExecuteProcessInstanceHeaders()
        execute_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_attachments_0 = dingtalkworkflow__1__0_models.ExecuteProcessInstanceRequestFileAttachments(
            space_id='123',
            file_size='1024',
            file_id='B1oQixxxx',
            file_name='文件名称。',
            file_type='file'
        )
        file = dingtalkworkflow__1__0_models.ExecuteProcessInstanceRequestFile(
            photos=[
                'https://url1'
            ],
            attachments=[
                file_attachments_0
            ]
        )
        execute_process_instance_request = dingtalkworkflow__1__0_models.ExecuteProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx',
            remark='同意。',
            result='agree',
            actioner_user_id='133743186427339452',
            task_id=67583405630,
            file=file
        )
        try:
            client.execute_process_instance_with_options(execute_process_instance_request, execute_process_instance_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        execute_process_instance_headers = dingtalkworkflow__1__0_models.ExecuteProcessInstanceHeaders()
        execute_process_instance_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_attachments_0 = dingtalkworkflow__1__0_models.ExecuteProcessInstanceRequestFileAttachments(
            space_id='123',
            file_size='1024',
            file_id='B1oQixxxx',
            file_name='文件名称。',
            file_type='file'
        )
        file = dingtalkworkflow__1__0_models.ExecuteProcessInstanceRequestFile(
            photos=[
                'https://url1'
            ],
            attachments=[
                file_attachments_0
            ]
        )
        execute_process_instance_request = dingtalkworkflow__1__0_models.ExecuteProcessInstanceRequest(
            process_instance_id='a171de6c-8bxxxx',
            remark='同意。',
            result='agree',
            actioner_user_id='133743186427339452',
            task_id=67583405630,
            file=file
        )
        try:
            await client.execute_process_instance_with_options_async(execute_process_instance_request, execute_process_instance_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ExecuteProcessInstanceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ExecuteProcessInstanceRequest\file\attachments;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ExecuteProcessInstanceRequest\file;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\ExecuteProcessInstanceRequest;
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
        $executeProcessInstanceHeaders = new ExecuteProcessInstanceHeaders([]);
        $executeProcessInstanceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $fileAttachments0 = new attachments([
            "spaceId" => "123",
            "fileSize" => "1024",
            "fileId" => "B1oQixxxx",
            "fileName" => "文件名称。",
            "fileType" => "file"
        ]);
        $file = new file([
            "photos" => [
                "https://url1"
            ],
            "attachments" => [
                $fileAttachments0
            ]
        ]);
        $executeProcessInstanceRequest = new ExecuteProcessInstanceRequest([
            "processInstanceId" => "a171de6c-8bxxxx",
            "remark" => "同意。",
            "result" => "agree",
            "actionerUserId" => "133743186427339452",
            "taskId" => 67583405630,
            "file" => $file
        ]);
        try {
            $client->executeProcessInstanceWithOptions($executeProcessInstanceRequest, $executeProcessInstanceHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
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

  executeProcessInstanceHeaders := &dingtalkworkflow_1_0.ExecuteProcessInstanceHeaders{}
  executeProcessInstanceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  fileAttachments0 := &dingtalkworkflow_1_0.ExecuteProcessInstanceRequestFileAttachments{
    SpaceId: tea.String("123"),
    FileSize: tea.String("1024"),
    FileId: tea.String("B1oQixxxx"),
    FileName: tea.String("文件名称。"),
    FileType: tea.String("file"),
  }
  file := &dingtalkworkflow_1_0.ExecuteProcessInstanceRequestFile{
    Photos: []*string{tea.String("https://url1")},
    Attachments: []*dingtalkworkflow_1_0.ExecuteProcessInstanceRequestFileAttachments{fileAttachments0},
  }
  executeProcessInstanceRequest := &dingtalkworkflow_1_0.ExecuteProcessInstanceRequest{
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
    Remark: tea.String("同意。"),
    Result: tea.String("agree"),
    ActionerUserId: tea.String("133743186427339452"),
    TaskId: tea.Int64(67583405630),
    File: file,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ExecuteProcessInstanceWithOptions(executeProcessInstanceRequest, executeProcessInstanceHeaders, &util.RuntimeOptions{})
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
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
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
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let executeProcessInstanceHeaders = new dingtalkworkflow_1_0.ExecuteProcessInstanceHeaders({ });
    executeProcessInstanceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let fileAttachments0 = new dingtalkworkflow_1_0.ExecuteProcessInstanceRequestFileAttachments({
      spaceId: '123',
      fileSize: '1024',
      fileId: 'B1oQixxxx',
      fileName: '文件名称。',
      fileType: 'file',
    });
    let file = new dingtalkworkflow_1_0.ExecuteProcessInstanceRequestFile({
      photos: [
        'https://url1'
      ],
      attachments: [
        fileAttachments0
      ],
    });
    let executeProcessInstanceRequest = new dingtalkworkflow_1_0.ExecuteProcessInstanceRequest({
      processInstanceId: 'a171de6c-8bxxxx',
      remark: '同意。',
      result: 'agree',
      actionerUserId: '133743186427339452',
      taskId: 67583405630,
      file: file,
    });
    try {
      await client.executeProcessInstanceWithOptions(executeProcessInstanceRequest, executeProcessInstanceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceHeaders executeProcessInstanceHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceHeaders();
            executeProcessInstanceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile.ExecuteProcessInstanceRequestFileAttachments fileAttachments0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile.ExecuteProcessInstanceRequestFileAttachments
            {
                SpaceId = "123",
                FileSize = "1024",
                FileId = "B1oQixxxx",
                FileName = "文件名称。",
                FileType = "file",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile file = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile
            {
                Photos = new List<string>
                {
                    "https://url1"
                },
                Attachments = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest.ExecuteProcessInstanceRequestFile.ExecuteProcessInstanceRequestFileAttachments>
                {
                    fileAttachments0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest executeProcessInstanceRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.ExecuteProcessInstanceRequest
            {
                ProcessInstanceId = "a171de6c-8bxxxx",
                Remark = "同意。",
                Result = "agree",
                ActionerUserId = "133743186427339452",
                TaskId = 67583405630,
                File = file,
            };
            try
            {
                client.ExecuteProcessInstanceWithOptions(executeProcessInstanceRequest, executeProcessInstanceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否同意审批任务：   - **true**：同意 - **false**：拒绝 |
| success | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true,
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | 同意或拒绝审批任务参数错误 | 同意或拒绝审批任务参数错误 |
| 400 | needAuth | 没有同意拒绝审批的权限 | 没有同意拒绝审批的权限 |
| 400 | invalidAgentId | 无效的微应用ID | 无效的微应用ID |
| 400 | aflowProcessNotExist | 审批流不存在 | 审批流不存在 |
| 400 | invalidInstanceId | 审批实例ID不能为空 | 审批实例ID不能为空 |
| 400 | invalidInstanceExecuteActionerUserId | 同意拒绝审批任务，操作人的userId不能为空 | 同意拒绝审批任务，操作人的userId不能为空 |
| 400 | invalidInstanceExecuteTaskId | 同意拒绝审批任务，任务节点id不能为空 | 同意拒绝审批任务，任务节点id不能为空 |
| 400 | invalidInstanceExecuteResult | 同意拒绝审批任务，审批操作取值必填 且值必须为agree/refuse | 同意拒绝审批任务，审批操作取值必填 且值必须为agree/refuse |
| 400 | aflowProcessFormDataIsNull | 流程表单数据为空 | 流程表单数据为空 |
| 400 | aflowProcessInstStatusException | 审批单状态异常 | 审批单状态异常 |
| 400 | aflowProcessInstCanNotBeExecuted | 审批状态异常，无法执行 | 审批状态异常，无法执行 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 500 | systemError | 系统异常 | 系统异常 |
