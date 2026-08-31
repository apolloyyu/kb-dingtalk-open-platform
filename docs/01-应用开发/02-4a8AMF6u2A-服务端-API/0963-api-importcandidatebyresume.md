---
title: "导入简历创建候选人"
source_url: "https://open.dingtalk.com/document/development/api-importcandidatebyresume"
namespace: "development"
slug: "api-importcandidatebyresume"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能招聘 > 导入简历创建候选人"
doc_id: "YQxZVDw7mP"
updated_at: "2026-07-10 10:05:49"
---

> Source: https://open.dingtalk.com/document/development/api-importcandidatebyresume
> Path: 应用开发 / 服务端 API / 智能招聘 > 导入简历创建候选人
> Updated: 2026-07-10 10:05:49

# 导入简历创建候选人

调用该接口，导入简历创建候选人。

## **接口调用说明**

- 为了防止批量导入简历影响线上的简历解析服务，该接口的开放调用时间是晚上8点到次日早上8点，其他时间调用无法进行解析。
- 该接口是同步接口，调用方自动控制重试机制。
- 单个组织限制每分钟调用限制30次，请调用方控制调用频率。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/ats/candidates/importCandidateByResume |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_recruitment\_plugin-智能招聘插件管理权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUserId | String | 否 | 操作人userId。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| fileSourceType | Integer | 是 | 简历文件来源：   - **2**：链接url方式传入 - **3**：钉盘方式传入 |
| url | String | 否 | 简历文件链接，选择链接方式传入时，必填。 |
| spaceId | Long | 否 | 简历钉盘文件空间id，钉盘方式传入时必须设定。 |
| fileId | String | 否 | 钉盘文件id，钉盘方式传入时，必须设值。 |
| fileName | String | 是 | 简历文件名称。 |
| fileType | String | 是 | 简历文件类型，支持pdf、doc、docx、png、jpg、jpeg等类型。 |
| fileSize | Long | 是 | 文件字节大小。 |
| channelCode | String | 否 | 简历渠道来源：   - **liepin**：猎聘 - **zhilian**：智联招聘 - **51job**：前程无忧 - **boss**：BOSS直聘 - **lagou**：拉勾 - **58tongcheng**：58同城 - **ganji**：赶集网 - **linkedin**：领英 - **maimai**：脉脉 - **other**：其他 |

### **请求示例**

HTTP

```
POST /v1.0/ats/candidates/importCandidateByResume?opUserId=23344xxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:234xxxxxxxxx
Content-Type:application/json

{
  "fileSourceType" : 3,
  "url" : "https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf",
  "fileId" : "123333xxxx",
  "fileName" : "简历文件.pdf",
  "fileType" : "pdf",
  "fileSize" : 223000,
  "channelCode" : "boss"
}
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
    public static com.aliyun.dingtalkats_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkats_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkats_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkats_1_0.models.ImportCandidateByResumeHeaders importCandidateByResumeHeaders = new com.aliyun.dingtalkats_1_0.models.ImportCandidateByResumeHeaders();
        importCandidateByResumeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkats_1_0.models.ImportCandidateByResumeRequest importCandidateByResumeRequest = new com.aliyun.dingtalkats_1_0.models.ImportCandidateByResumeRequest()
                .setOpUserId("23344xxx")
                .setFileSourceType(3)
                .setUrl("https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf")
                .setFileId("123333xxxx")
                .setFileName("简历文件.pdf")
                .setFileType("pdf")
                .setFileSize(223000L)
                .setChannelCode("boss");
        try {
            client.importCandidateByResumeWithOptions(importCandidateByResumeRequest, importCandidateByResumeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.ats_1_0.client import Client as dingtalkats_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.ats_1_0 import models as dingtalkats__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkats_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkats_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        import_candidate_by_resume_headers = dingtalkats__1__0_models.ImportCandidateByResumeHeaders()
        import_candidate_by_resume_headers.x_acs_dingtalk_access_token = '<your access token>'
        import_candidate_by_resume_request = dingtalkats__1__0_models.ImportCandidateByResumeRequest(
            op_user_id='23344xxx',
            file_source_type=3,
            url='https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf',
            file_id='123333xxxx',
            file_name='简历文件.pdf',
            file_type='pdf',
            file_size=223000,
            channel_code='boss'
        )
        try:
            client.import_candidate_by_resume_with_options(import_candidate_by_resume_request, import_candidate_by_resume_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        import_candidate_by_resume_headers = dingtalkats__1__0_models.ImportCandidateByResumeHeaders()
        import_candidate_by_resume_headers.x_acs_dingtalk_access_token = '<your access token>'
        import_candidate_by_resume_request = dingtalkats__1__0_models.ImportCandidateByResumeRequest(
            op_user_id='23344xxx',
            file_source_type=3,
            url='https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf',
            file_id='123333xxxx',
            file_name='简历文件.pdf',
            file_type='pdf',
            file_size=223000,
            channel_code='boss'
        )
        try:
            await client.import_candidate_by_resume_with_options_async(import_candidate_by_resume_request, import_candidate_by_resume_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\ImportCandidateByResumeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vats_1_0\Models\ImportCandidateByResumeRequest;
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
        $importCandidateByResumeHeaders = new ImportCandidateByResumeHeaders([]);
        $importCandidateByResumeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $importCandidateByResumeRequest = new ImportCandidateByResumeRequest([
            "opUserId" => "23344xxx",
            "fileSourceType" => 3,
            "url" => "https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf",
            "fileId" => "123333xxxx",
            "fileName" => "简历文件.pdf",
            "fileType" => "pdf",
            "fileSize" => 223000,
            "channelCode" => "boss"
        ]);
        try {
            $client->importCandidateByResumeWithOptions($importCandidateByResumeRequest, $importCandidateByResumeHeaders, new RuntimeOptions([]));
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
  dingtalkats_1_0  "github.com/alibabacloud-go/dingtalk/ats_1_0"
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
func CreateClient () (_result *dingtalkats_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkats_1_0.Client{}
  _result, _err = dingtalkats_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  importCandidateByResumeHeaders := &dingtalkats_1_0.ImportCandidateByResumeHeaders{}
  importCandidateByResumeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  importCandidateByResumeRequest := &dingtalkats_1_0.ImportCandidateByResumeRequest{
    OpUserId: tea.String("23344xxx"),
    FileSourceType: tea.Int32(3),
    Url: tea.String("https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf"),
    FileId: tea.String("123333xxxx"),
    FileName: tea.String("简历文件.pdf"),
    FileType: tea.String("pdf"),
    FileSize: tea.Int64(223000),
    ChannelCode: tea.String("boss"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ImportCandidateByResumeWithOptions(importCandidateByResumeRequest, importCandidateByResumeHeaders, &util.RuntimeOptions{})
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
const dingtalkats_1_0 = require('@alicloud/dingtalk/ats_1_0');
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
    return new dingtalkats_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let importCandidateByResumeHeaders = new dingtalkats_1_0.ImportCandidateByResumeHeaders({ });
    importCandidateByResumeHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let importCandidateByResumeRequest = new dingtalkats_1_0.ImportCandidateByResumeRequest({
      opUserId: '23344xxx',
      fileSourceType: 3,
      url: 'https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf',
      fileId: '123333xxxx',
      fileName: '简历文件.pdf',
      fileType: 'pdf',
      fileSize: 223000,
      channelCode: 'boss',
    });
    try {
      await client.importCandidateByResumeWithOptions(importCandidateByResumeRequest, importCandidateByResumeHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkats_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkats_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkats_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.ImportCandidateByResumeHeaders importCandidateByResumeHeaders = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.ImportCandidateByResumeHeaders();
            importCandidateByResumeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkats_1_0.Models.ImportCandidateByResumeRequest importCandidateByResumeRequest = new AlibabaCloud.SDK.Dingtalkats_1_0.Models.ImportCandidateByResumeRequest
            {
                OpUserId = "23344xxx",
                FileSourceType = 3,
                Url = "https://xxx.oss-cn-hangzhou.aliyuncs.com/xxx.pdf",
                FileId = "123333xxxx",
                FileName = "简历文件.pdf",
                FileType = "pdf",
                FileSize = 223000,
                ChannelCode = "boss",
            };
            try
            {
                client.ImportCandidateByResumeWithOptions(importCandidateByResumeRequest, importCandidateByResumeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| candidateId | String | 候选人id。 |
| corpId | String | 组织corpId。 |
| name | String | 候选人名称。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "candidateId" : "b233fdfxxxxxxxx",
  "corpId" : "ding23445xxxxxx",
  "name" : "李xx"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | systemError | 系统错误 | 系统错误 |
| 500 | invalidParam | %s | 参数校验不通过，详情信息见ErrorMessage |
| 500 | userNotInCorp | 用户不在组织内 | 用户不在组织内 |
| 500 | addCandidateFail | 添加候选人失败 | 添加候选人失败 |
