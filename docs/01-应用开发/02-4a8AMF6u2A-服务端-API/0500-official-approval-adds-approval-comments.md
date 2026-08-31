---
title: "添加审批评论"
source_url: "https://open.dingtalk.com/document/development/official-approval-adds-approval-comments"
namespace: "development"
slug: "official-approval-adds-approval-comments"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批实例 > 添加审批评论"
doc_id: "S4AcuitnEF"
updated_at: "2026-06-03 10:12:28"
---

> Source: https://open.dingtalk.com/document/development/official-approval-adds-approval-comments
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批实例 > 添加审批评论
> Updated: 2026-06-03 10:12:28

# 添加审批评论

调用本接口，对审批实例添加评论。

## **接口调用说明**

添加审批评论附件需将文件上传至审批钉盘空间，可以获取到接口参数spaceId，fileType，fileName，fileId，fileSize。获取方式如下：

1. 调用[获取审批钉盘空间信息](0502-obtains-the-information-about-approval-nail-disk.md)接口，获取钉盘空间的上传权限，并获取审批钉盘空间spaceId。
2. 根据审批钉盘空间spaceId，网页应用（H5微应用）/小程序，通过[上传附件到钉盘/从钉盘选择文件](../03-Ogu5SlPY4t-客户端-JSAPI/0333-jsapi-upload-attachment-to-ding-talk.md)获取钉盘附件file的信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processInstances/comments |
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
| processInstanceId | String | 是 | 审批实例ID：   - 调用[发起审批实例](0497-create-an-approval-instance.md)接口获取`InstanceId`参数值。 - 调用[获取单个审批实例详情](0501-obtain-an-approval-list-of-instance-ids.md)接口获取`list`参数值。 |
| text | String | 是 | 评论的内容，最大长度1024字符。 |
| commentUserId | String | 是 | 评论人的userId。 |
| file | Object | 否 | 文件。 |
| photos | Array of String | 否 | 图片URL地址。 |
| attachments | Array | 否 | 附件列表，最大列表元素个数：20。 |
| spaceId | String | 否 | 钉盘空间ID。      请参见本文接口调用说明。 |
| fileSize | String | 否 | 文件大小。      请参见本文接口调用说明。 |
| fileId | String | 否 | 文件ID，最大长度256字符。      请参见本文接口调用说明。 |
| fileName | String | 否 | 文件名称，最大长度256字符。      请参见本文接口调用说明。 |
| fileType | String | 否 | 文件类型。      请参见本文接口调用说明。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processInstances/comments HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json

{
  "processInstanceId" : "a171de6c-8bxxxx",
  "text" : "同意。",
  "commentUserId" : "user123",
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
        com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentHeaders addProcessInstanceCommentHeaders = new com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentHeaders();
        addProcessInstanceCommentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFileAttachments fileAttachments0 = new com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFileAttachments()
                .setSpaceId("123")
                .setFileSize("1024")
                .setFileId("B1oQixxxx")
                .setFileName("文件名称。")
                .setFileType("file");
        com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile file = new com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile()
                .setPhotos(java.util.Arrays.asList(
                    "https://url1"
                ))
                .setAttachments(java.util.Arrays.asList(
                    fileAttachments0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentRequest addProcessInstanceCommentRequest = new com.aliyun.dingtalkworkflow_1_0.models.AddProcessInstanceCommentRequest()
                .setProcessInstanceId("a171de6c-8bxxxx")
                .setText("同意。")
                .setCommentUserId("user123")
                .setFile(file);
        try {
            client.addProcessInstanceCommentWithOptions(addProcessInstanceCommentRequest, addProcessInstanceCommentHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_process_instance_comment_headers = dingtalkworkflow__1__0_models.AddProcessInstanceCommentHeaders()
        add_process_instance_comment_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_attachments_0 = dingtalkworkflow__1__0_models.AddProcessInstanceCommentRequestFileAttachments(
            space_id='123',
            file_size='1024',
            file_id='B1oQixxxx',
            file_name='文件名称。',
            file_type='file'
        )
        file = dingtalkworkflow__1__0_models.AddProcessInstanceCommentRequestFile(
            photos=[
                'https://url1'
            ],
            attachments=[
                file_attachments_0
            ]
        )
        add_process_instance_comment_request = dingtalkworkflow__1__0_models.AddProcessInstanceCommentRequest(
            process_instance_id='a171de6c-8bxxxx',
            text='同意。',
            comment_user_id='user123',
            file=file
        )
        try:
            client.add_process_instance_comment_with_options(add_process_instance_comment_request, add_process_instance_comment_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_process_instance_comment_headers = dingtalkworkflow__1__0_models.AddProcessInstanceCommentHeaders()
        add_process_instance_comment_headers.x_acs_dingtalk_access_token = '<your access token>'
        file_attachments_0 = dingtalkworkflow__1__0_models.AddProcessInstanceCommentRequestFileAttachments(
            space_id='123',
            file_size='1024',
            file_id='B1oQixxxx',
            file_name='文件名称。',
            file_type='file'
        )
        file = dingtalkworkflow__1__0_models.AddProcessInstanceCommentRequestFile(
            photos=[
                'https://url1'
            ],
            attachments=[
                file_attachments_0
            ]
        )
        add_process_instance_comment_request = dingtalkworkflow__1__0_models.AddProcessInstanceCommentRequest(
            process_instance_id='a171de6c-8bxxxx',
            text='同意。',
            comment_user_id='user123',
            file=file
        )
        try:
            await client.add_process_instance_comment_with_options_async(add_process_instance_comment_request, add_process_instance_comment_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddProcessInstanceCommentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddProcessInstanceCommentRequest\file\attachments;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddProcessInstanceCommentRequest\file;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\AddProcessInstanceCommentRequest;
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
        $addProcessInstanceCommentHeaders = new AddProcessInstanceCommentHeaders([]);
        $addProcessInstanceCommentHeaders->xAcsDingtalkAccessToken = "<your access token>";
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
        $addProcessInstanceCommentRequest = new AddProcessInstanceCommentRequest([
            "processInstanceId" => "a171de6c-8bxxxx",
            "text" => "同意。",
            "commentUserId" => "user123",
            "file" => $file
        ]);
        try {
            $client->addProcessInstanceCommentWithOptions($addProcessInstanceCommentRequest, $addProcessInstanceCommentHeaders, new RuntimeOptions([]));
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

  addProcessInstanceCommentHeaders := &dingtalkworkflow_1_0.AddProcessInstanceCommentHeaders{}
  addProcessInstanceCommentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  fileAttachments0 := &dingtalkworkflow_1_0.AddProcessInstanceCommentRequestFileAttachments{
    SpaceId: tea.String("123"),
    FileSize: tea.String("1024"),
    FileId: tea.String("B1oQixxxx"),
    FileName: tea.String("文件名称。"),
    FileType: tea.String("file"),
  }
  file := &dingtalkworkflow_1_0.AddProcessInstanceCommentRequestFile{
    Photos: []*string{tea.String("https://url1")},
    Attachments: []*dingtalkworkflow_1_0.AddProcessInstanceCommentRequestFileAttachments{fileAttachments0},
  }
  addProcessInstanceCommentRequest := &dingtalkworkflow_1_0.AddProcessInstanceCommentRequest{
    ProcessInstanceId: tea.String("a171de6c-8bxxxx"),
    Text: tea.String("同意。"),
    CommentUserId: tea.String("user123"),
    File: file,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddProcessInstanceCommentWithOptions(addProcessInstanceCommentRequest, addProcessInstanceCommentHeaders, &util.RuntimeOptions{})
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
    let addProcessInstanceCommentHeaders = new dingtalkworkflow_1_0.AddProcessInstanceCommentHeaders({ });
    addProcessInstanceCommentHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let fileAttachments0 = new dingtalkworkflow_1_0.AddProcessInstanceCommentRequestFileAttachments({
      spaceId: '123',
      fileSize: '1024',
      fileId: 'B1oQixxxx',
      fileName: '文件名称。',
      fileType: 'file',
    });
    let file = new dingtalkworkflow_1_0.AddProcessInstanceCommentRequestFile({
      photos: [
        'https://url1'
      ],
      attachments: [
        fileAttachments0
      ],
    });
    let addProcessInstanceCommentRequest = new dingtalkworkflow_1_0.AddProcessInstanceCommentRequest({
      processInstanceId: 'a171de6c-8bxxxx',
      text: '同意。',
      commentUserId: 'user123',
      file: file,
    });
    try {
      await client.addProcessInstanceCommentWithOptions(addProcessInstanceCommentRequest, addProcessInstanceCommentHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentHeaders addProcessInstanceCommentHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentHeaders();
            addProcessInstanceCommentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile.AddProcessInstanceCommentRequestFileAttachments fileAttachments0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile.AddProcessInstanceCommentRequestFileAttachments
            {
                SpaceId = "123",
                FileSize = "1024",
                FileId = "B1oQixxxx",
                FileName = "文件名称。",
                FileType = "file",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile file = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile
            {
                Photos = new List<string>
                {
                    "https://url1"
                },
                Attachments = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest.AddProcessInstanceCommentRequestFile.AddProcessInstanceCommentRequestFileAttachments>
                {
                    fileAttachments0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest addProcessInstanceCommentRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.AddProcessInstanceCommentRequest
            {
                ProcessInstanceId = "a171de6c-8bxxxx",
                Text = "同意。",
                CommentUserId = "user123",
                File = file,
            };
            try
            {
                client.AddProcessInstanceCommentWithOptions(addProcessInstanceCommentRequest, addProcessInstanceCommentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 评论是否成功。 |
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
| 400 | invalidParameter | 添加审批评论参数错误 | 添加审批评论参数错误 |
| 400 | userNotExist | 用户不存在 | 用户不存在 |
| 400 | aflowProcessInstNotExist | 审批实例不存在 | 审批实例不存在 |
| 400 | aflowProcessInstCanNotBeExecuted | 审批状态异常，无法执行 | 审批状态异常，无法执行 |
| 400 | invalidInstanceId | 审批实例ID不能为空 | 审批实例ID不能为空 |
| 400 | invalidInstanceCommentText | 审批实例评论内容不能为空 | 审批实例评论内容不能为空 |
| 400 | invalidInstanceCommentUserId | 审批实例评论人userId不能为空 | 审批实例评论人userId不能为空 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
