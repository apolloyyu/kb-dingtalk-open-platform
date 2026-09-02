---
title: "转交OA审批任务"
source_url: "https://open.dingtalk.com/document/development/transfer-the-oa-approval-task"
namespace: "development"
slug: "transfer-the-oa-approval-task"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批任务 > 转交OA审批任务"
doc_id: "jq1XaQ0vhT"
updated_at: "2026-06-03 10:12:34"
---

> Source: https://open.dingtalk.com/document/development/transfer-the-oa-approval-task
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批任务 > 转交OA审批任务
> Updated: 2026-06-03 10:12:34

# 转交OA审批任务

调用本接口，转交OA审批任务。

## **接口调用说明**

> **[!NOTE]**
>
> 本接口仅支持通过官方审批发起的或原生审批流程任务，不支持自有审批创建的实例任务。

添加审批附件需将文件上传至审批钉盘空间，可以获取到接口参数spaceId，fileType，fileName，fileId，fileSize。获取方式如下：

1. 调用[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
2. 根据审批钉盘空间spaceId，网页应用（H5微应用）/小程序，通过[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0332-jsapi-upload-attachment-to-ding-talk.md)获取钉盘附件file的信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/tasks/redirect |
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
| taskId | Long | 是 | OA审批任务ID，调用[获取单个审批实例详情](0498-obtains-the-details-of-a-single-approval-instance-pop.md)接口获取的taskId参数值。 |
| toUserId | String | 是 | OA审批任务被转交对象的用户userId。 |
| remark | String | 否 | 转交备注信息，最大长度：256字符。 |
| operateUserId | String | 是 | 操作人userId，需要跟任务的当前执行人保持一致，否则无法通过校验。 |
| actionName | String | 否 | 操作节点名，最大长度：128字符。 |
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
POST /v1.0/workflow/tasks/redirect HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "taskId" : 1234567,
  "toUserId" : "manager001",
  "remark" : "请XX帮忙审批一下",
  "operateUserId" : "user001",
  "actionName" : "test",
  "file" : {
    "photos" : [ "\"https://url1\"" ],
    "attachments" : [ {
      "spaceId" : "123",
      "fileSize" : "1024",
      "fileId" : "B1oQixxxx",
      "fileName" : "文件名称",
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
        com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskHeaders redirectWorkflowTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskHeaders();
        redirectWorkflowTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFileAttachments fileAttachments0 = new com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFileAttachments()
                .setSpaceId("123")
                .setFileSize("1024")
                .setFileId("B1oQixxxx")
                .setFileName("文件名称")
                .setFileType("file");
        com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile file = new com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile()
                .setPhotos(java.util.Arrays.asList(
                    "\"https://url1\""
                ))
                .setAttachments(java.util.Arrays.asList(
                    fileAttachments0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest redirectWorkflowTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.RedirectWorkflowTaskRequest()
                .setTaskId(1234567L)
                .setToUserId("manager001")
                .setRemark("请XX帮忙审批一下")
                .setOperateUserId("user001")
                .setActionName("test")
                .setFile(file);
        try {
            client.redirectWorkflowTaskWithOptions(redirectWorkflowTaskRequest, redirectWorkflowTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        redirect_workflow_task_headers = dingtalkworkflow__1__0_models.RedirectWorkflowTaskHeaders()
        redirect_workflow_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_attachments_0 = dingtalkworkflow__1__0_models.RedirectWorkflowTaskRequestFileAttachments(
            space_id='123',
            file_size='1024',
            file_id='B1oQixxxx',
            file_name='文件名称',
            file_type='file'
        )
        file = dingtalkworkflow__1__0_models.RedirectWorkflowTaskRequestFile(
            photos=[
                '"https://url1"'
            ],
            attachments=[
                file_attachments_0
            ]
        )
        redirect_workflow_task_request = dingtalkworkflow__1__0_models.RedirectWorkflowTaskRequest(
            task_id=1234567,
            to_user_id='manager001',
            remark='请XX帮忙审批一下',
            operate_user_id='user001',
            action_name='test',
            file=file
        )
        try:
            client.redirect_workflow_task_with_options(redirect_workflow_task_request, redirect_workflow_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        redirect_workflow_task_headers = dingtalkworkflow__1__0_models.RedirectWorkflowTaskHeaders()
        redirect_workflow_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_attachments_0 = dingtalkworkflow__1__0_models.RedirectWorkflowTaskRequestFileAttachments(
            space_id='123',
            file_size='1024',
            file_id='B1oQixxxx',
            file_name='文件名称',
            file_type='file'
        )
        file = dingtalkworkflow__1__0_models.RedirectWorkflowTaskRequestFile(
            photos=[
                '"https://url1"'
            ],
            attachments=[
                file_attachments_0
            ]
        )
        redirect_workflow_task_request = dingtalkworkflow__1__0_models.RedirectWorkflowTaskRequest(
            task_id=1234567,
            to_user_id='manager001',
            remark='请XX帮忙审批一下',
            operate_user_id='user001',
            action_name='test',
            file=file
        )
        try:
            await client.redirect_workflow_task_with_options_async(redirect_workflow_task_request, redirect_workflow_task_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\RedirectWorkflowTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\RedirectWorkflowTaskRequest\file\attachments;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\RedirectWorkflowTaskRequest\file;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\RedirectWorkflowTaskRequest;
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
        $redirectWorkflowTaskHeaders = new RedirectWorkflowTaskHeaders([]);
        $redirectWorkflowTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $fileAttachments0 = new attachments([
            "spaceId" => "123",
            "fileSize" => "1024",
            "fileId" => "B1oQixxxx",
            "fileName" => "文件名称",
            "fileType" => "file"
        ]);
        $file = new file([
            "photos" => [
                "\"https://url1\""
            ],
            "attachments" => [
                $fileAttachments0
            ]
        ]);
        $redirectWorkflowTaskRequest = new RedirectWorkflowTaskRequest([
            "taskId" => 1234567,
            "toUserId" => "manager001",
            "remark" => "请XX帮忙审批一下",
            "operateUserId" => "user001",
            "actionName" => "test",
            "file" => $file
        ]);
        try {
            $client->redirectWorkflowTaskWithOptions($redirectWorkflowTaskRequest, $redirectWorkflowTaskHeaders, new RuntimeOptions([]));
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

  redirectWorkflowTaskHeaders := &dingtalkworkflow_1_0.RedirectWorkflowTaskHeaders{}
  redirectWorkflowTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  fileAttachments0 := &dingtalkworkflow_1_0.RedirectWorkflowTaskRequestFileAttachments{
    SpaceId: tea.String("123"),
    FileSize: tea.String("1024"),
    FileId: tea.String("B1oQixxxx"),
    FileName: tea.String("文件名称"),
    FileType: tea.String("file"),
  }
  file := &dingtalkworkflow_1_0.RedirectWorkflowTaskRequestFile{
    Photos: []*string{tea.String("\"https://url1\"")},
    Attachments: []*dingtalkworkflow_1_0.RedirectWorkflowTaskRequestFileAttachments{fileAttachments0},
  }
  redirectWorkflowTaskRequest := &dingtalkworkflow_1_0.RedirectWorkflowTaskRequest{
    TaskId: tea.Int64(1234567),
    ToUserId: tea.String("manager001"),
    Remark: tea.String("请XX帮忙审批一下"),
    OperateUserId: tea.String("user001"),
    ActionName: tea.String("test"),
    File: file,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RedirectWorkflowTaskWithOptions(redirectWorkflowTaskRequest, redirectWorkflowTaskHeaders, &util.RuntimeOptions{})
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
    let redirectWorkflowTaskHeaders = new dingtalkworkflow_1_0.RedirectWorkflowTaskHeaders({ });
    redirectWorkflowTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let fileAttachments0 = new dingtalkworkflow_1_0.RedirectWorkflowTaskRequestFileAttachments({
      spaceId: '123',
      fileSize: '1024',
      fileId: 'B1oQixxxx',
      fileName: '文件名称',
      fileType: 'file',
    });
    let file = new dingtalkworkflow_1_0.RedirectWorkflowTaskRequestFile({
      photos: [
        '"https://url1"'
      ],
      attachments: [
        fileAttachments0
      ],
    });
    let redirectWorkflowTaskRequest = new dingtalkworkflow_1_0.RedirectWorkflowTaskRequest({
      taskId: 1234567,
      toUserId: 'manager001',
      remark: '请XX帮忙审批一下',
      operateUserId: 'user001',
      actionName: 'test',
      file: file,
    });
    try {
      await client.redirectWorkflowTaskWithOptions(redirectWorkflowTaskRequest, redirectWorkflowTaskHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskHeaders redirectWorkflowTaskHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskHeaders();
            redirectWorkflowTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile.RedirectWorkflowTaskRequestFileAttachments fileAttachments0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile.RedirectWorkflowTaskRequestFileAttachments
            {
                SpaceId = "123",
                FileSize = "1024",
                FileId = "B1oQixxxx",
                FileName = "文件名称",
                FileType = "file",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile file = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile
            {
                Photos = new List<string>
                {
                    "\"https://url1\""
                },
                Attachments = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest.RedirectWorkflowTaskRequestFile.RedirectWorkflowTaskRequestFileAttachments>
                {
                    fileAttachments0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest redirectWorkflowTaskRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.RedirectWorkflowTaskRequest
            {
                TaskId = 1234567,
                ToUserId = "manager001",
                Remark = "请XX帮忙审批一下",
                OperateUserId = "user001",
                ActionName = "test",
                File = file,
            };
            try
            {
                client.RedirectWorkflowTaskWithOptions(redirectWorkflowTaskRequest, redirectWorkflowTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否转交成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.blank | %s参数不能为空 | toUserId参数不能为空 |
| 400 | param.illegal | 不合法的参数%s | 不合法的参数taskId |
| 400 | task.status.error | 当前任务状态不是运行中不支持转交操作 | 当前任务状态不是运行中不支持转交操作 |
| 400 | instance.status.error | 当前流程实例状态不是运行中不支持转交操作 | 当前流程实例状态不是运行中不支持转交操作 |
| 400 | param.illegal.operator | 不合法的参数operateUserId | 不合法的参数operateUserId |
| 400 | internalError | %s | 系统内部异常 |
| 500 | system.error | 系统错误 | 系统错误 |
