---
title: "获取公告详情"
source_url: "https://open.dingtalk.com/document/development/obtains-the-details-get-blackboard"
namespace: "development"
slug: "obtains-the-details-get-blackboard"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 获取公告详情"
doc_id: "IN8RnUASa6"
updated_at: "2026-06-02 09:18:06"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-details-get-blackboard
> Path: 应用开发 / 服务端API / 公告 > 获取公告详情
> Updated: 2026-06-02 09:18:06

# 获取公告详情

调用本接口，根据公告ID获取未删除的公告的详情。

## 接口调用说明

公告的查看权限要求如下：

- **非保密公告**：全部员工
- **保密公告**：管理员和公告的接收人

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/blackboard/get\_blackboard |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_manage-钉钉公告管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，企业内部应用通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operationUserId | String | 否 | 操作人userId。 |
| blackboardId | String | 否 | 公告id，可以通过[获取公告ID列表接口](0283-obtains-the-id-list-of-announcements-that-are-not-deleted.md)获取id参数值。 |

### 请求示例

HTTP

```
GET /v1.0/blackboard/get_blackboard?operationUserId=manager01&blackboardId=ca80xxxx0a04 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6d1bxxxx
Content-Type:application/json
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
    public static com.aliyun.dingtalkblackboard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkblackboard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkblackboard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkblackboard_1_0.models.GetBlackboardHeaders getBlackboardHeaders = new com.aliyun.dingtalkblackboard_1_0.models.GetBlackboardHeaders();
        getBlackboardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkblackboard_1_0.models.GetBlackboardRequest getBlackboardRequest = new com.aliyun.dingtalkblackboard_1_0.models.GetBlackboardRequest()
                .setOperationUserId("manager01")
                .setBlackboardId("ca80xxxx0a04");
        try {
            client.getBlackboardWithOptions(getBlackboardRequest, getBlackboardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.blackboard_1_0.client import Client as dingtalkblackboard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.blackboard_1_0 import models as dingtalkblackboard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkblackboard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkblackboard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_blackboard_headers = dingtalkblackboard__1__0_models.GetBlackboardHeaders()
        get_blackboard_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_blackboard_request = dingtalkblackboard__1__0_models.GetBlackboardRequest(
            operation_user_id='manager01',
            blackboard_id='ca80xxxx0a04'
        )
        try:
            client.get_blackboard_with_options(get_blackboard_request, get_blackboard_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_blackboard_headers = dingtalkblackboard__1__0_models.GetBlackboardHeaders()
        get_blackboard_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_blackboard_request = dingtalkblackboard__1__0_models.GetBlackboardRequest(
            operation_user_id='manager01',
            blackboard_id='ca80xxxx0a04'
        )
        try:
            await client.get_blackboard_with_options_async(get_blackboard_request, get_blackboard_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Models\GetBlackboardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vblackboard_1_0\Models\GetBlackboardRequest;
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
        $getBlackboardHeaders = new GetBlackboardHeaders([]);
        $getBlackboardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getBlackboardRequest = new GetBlackboardRequest([
            "operationUserId" => "manager01",
            "blackboardId" => "ca80xxxx0a04"
        ]);
        try {
            $client->getBlackboardWithOptions($getBlackboardRequest, $getBlackboardHeaders, new RuntimeOptions([]));
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
  dingtalkblackboard_1_0  "github.com/alibabacloud-go/dingtalk/blackboard_1_0"
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
func CreateClient () (_result *dingtalkblackboard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkblackboard_1_0.Client{}
  _result, _err = dingtalkblackboard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getBlackboardHeaders := &dingtalkblackboard_1_0.GetBlackboardHeaders{}
  getBlackboardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getBlackboardRequest := &dingtalkblackboard_1_0.GetBlackboardRequest{
    OperationUserId: tea.String("manager01"),
    BlackboardId: tea.String("ca80xxxx0a04"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetBlackboardWithOptions(getBlackboardRequest, getBlackboardHeaders, &util.RuntimeOptions{})
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
const dingtalkblackboard_1_0 = require('@alicloud/dingtalk/blackboard_1_0');
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
    return new dingtalkblackboard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let getBlackboardHeaders = new dingtalkblackboard_1_0.GetBlackboardHeaders({ });
    getBlackboardHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getBlackboardRequest = new dingtalkblackboard_1_0.GetBlackboardRequest({
      operationUserId: 'manager01',
      blackboardId: 'ca80xxxx0a04',
    });
    try {
      await client.getBlackboardWithOptions(getBlackboardRequest, getBlackboardHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkblackboard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.GetBlackboardHeaders getBlackboardHeaders = new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.GetBlackboardHeaders();
            getBlackboardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.GetBlackboardRequest getBlackboardRequest = new AlibabaCloud.SDK.Dingtalkblackboard_1_0.Models.GetBlackboardRequest
            {
                OperationUserId = "manager01",
                BlackboardId = "ca80xxxx0a04",
            };
            try
            {
                client.GetBlackboardWithOptions(getBlackboardRequest, getBlackboardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 公告id。 |
| senderStaffId | String | 发送公告的员工 staffId。 |
| title | String | 公告标题。 |
| content | String | 公告内容。 |
| categoryId | String | 分类id。 |
| categoryName | String | 分类名称。 |
| coverPicUrl | String | 封面图片链接。 |
| privateLevel | Long | 保密等级：   - **0**：公开 - **20**：保密 |
| isPushTop | Long | 是否置顶：   - **0**：否 - **1**：是 |
| depNameList | Array of String | 部门名称。 |
| userNameList | Array of String | 接收人名称。 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 修改时间。 |
| readCount | Long | 已读数。 |
| unReadCount | Long | 未读数。 |
| userList | Array | 用户列表。 |
| corpId | String | 企业Id。 |
| staffId | String | 员工Id。 |
| name | String | 员工名称。 |
| deptList | Array | 接收部门列表。 |
| deptId | String | 部门id。 |
| name | String | 部门名称。 |
| attachments | Array | 附件列表      如需下载公告附件，请参考文档[获取文件下载信息](0678-obtains-the-download-information-about-a-file.md)，使用本接口返回的附件信息进行下载。 |
| fileName | String | 文件名称。 |
| fileType | String | 文件类型。 |
| dentryId | String | 文件id。 |
| spaceId | String | 钉盘空间id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "fbeaxxxxxxxxxxxxxxxxxxxxxxxxe292",
  "senderStaffId" : "manager01",
  "title" : "公告标题示例",
  "content" : "公告内容示例",
  "categoryId" : "example_category_id",
  "categoryName" : "分类示例",
  "coverPicUrl" : "https://down.dingtalk.com/ddmedia/xxxx.png?ddFrom=blackboard.pic",
  "privateLevel" : 0,
  "isPushTop" : 0,
  "depNameList" : [ "xxxx部门" ],
  "userNameList" : [ "示例接收人" ],
  "gmtCreate" : "2025-01-01 00:00:00",
  "gmtModified" : "2025-01-01 00:00:00",
  "readCount" : 10,
  "unReadCount" : 1,
  "userList" : [ {
    "corpId" : "dingxxxx",
    "staffId" : "manager01",
    "name" : "示例员工名称"
  } ],
  "deptList" : [ {
    "deptId" : "example_dept_id",
    "name" : "xxxx部门"
  } ],
  "attachments" : [ {
    "fileName" : "附件.pdf",
    "fileType" : "pdf",
    "dentryId" : "1976xxxx5884",
    "spaceId" : "275xxxx5820"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | badRequest | badRequest | 参数错误，请确保 operationUserId、blackboardId 参数合法。 |
| 403 | accessDenied | accessDenied | 请求被拒绝，请确认操作人是企业主管理员或者是公告的发送人，并且公告归属于当前组织。 |
| 500 | serviceBusy | The server is busy and unable to complete your request. Please try again later. | 服务繁忙，请稍后重试。 |
| 500 | internalError | The server encountered an internal error and was unable to complete your request. Please try again later. | 服务内部错误，请稍后再试。 |
