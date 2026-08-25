---
title: "添加文件（夹）"
source_url: "https://open.dingtalk.com/document/development/add-file-and-folder"
namespace: "development"
slug: "add-file-and-folder"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件管理 > 添加文件（夹）"
doc_id: "t1n6kRefor"
updated_at: "2026-08-25 09:38:21"
---

> Source: https://open.dingtalk.com/document/development/add-file-and-folder
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件管理 > 添加文件（夹）
> Updated: 2026-08-25 09:38:21

# 添加文件（夹）

调用本接口添加文件（夹）。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用以下新版接口，已接入用户不受影响：
>
>   - **添加文件**：使用[获取文件上传信息](0674-obtain-file-upload-informations.md)和[提交文件](0675-submittal-file.md)接口。
>   - **添加文件夹**：使用[添加文件夹](0654-add-folder.md)接口。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
POST /v1.0/drive/spaces/{spaceId}/files HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json

{
  "parentId" : "String",
  "fileType" : "String",
  "fileName" : "String",
  "mediaId" : "String",
  "addConflictPolicy" : "String",
  "unionId" : "String"
}
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 钉盘空间ID，可调用[获取空间信息](0653-get-space-information.md)接口获取spaceId参数值。 |

## Body参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| parentId | String | 否 | 父目录ID。  **[!NOTE]**  根目录时传**0**。 |
| fileType | String | 是 | 文件类型。   - **file**：文件 - **folder**：文件夹 |
| fileName | String | 是 | 文件名。 |
| mediaId | String | 否 | 对应OSS Object Key，可调用[获取文件上传信息](0674-obtain-file-upload-informations.md)接口获取。  **[!NOTE]**   - 当**fileType**值为**file**文件时，此参数必填。 - 当**fileType**值为**folder**文件夹时，此参数可不填。 |
| addConflictPolicy | String | 否 | 文件名称冲突策略，取值：   - **autoRename**：自动重命名 - **overwrite**：覆写 - **returnExisting**：返回已存在文件 - **returnError**：报错   **[!NOTE]**  第三方企业应用，不支持**overwrite**。 |
| unionId | String | 是 | 用户unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| spaceId | String | 钉盘空间ID。 |
| parentId | String | 父目录ID。根目录为0。 |
| fileId | String | 文件ID。 |
| fileName | String | 文件名称。 |
| filePath | String | 文件路径。 |
| fileType | String | 文件类型。   - **file**：文件 - **folder**：文件夹 |
| contentType | String | 文件内容类型，取值：   - **image**：图片 - **document**：一般文档 - **alidoc**：阿里文档 - **text**：文本 - **video**：视频 - **audio**：音频 - **archive**：归档 - **app**：应用 - **link**：快捷方式 - **other**：其他 |
| fileExtension | String | 文件后缀名。 |
| fileSize | Long | 文件大小。 |
| createTime | String | 创建时间。 |
| modifyTime | String | 修改时间。 |
| creator | String | 创建者。 |
| modifier | String | 修改者。 |

## 示例

**请求示例**

HTTP

```
POST /v1.0/drive/spaces/712546/files HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2db66cxxxx
Content-Type:application/json

{
  "parentId" : "1234567",
  "fileType" : "file",
  "fileName" : "测试文件.txt",
  "mediaId" : "#1234kkk",
  "addConflictPolicy" : "autoRename",
  "unionId" : "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkdrive_1_0.*;
import com.aliyun.dingtalkdrive_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkdrive_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkdrive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkdrive_1_0.Client client = Sample.createClient();
        AddFileHeaders addFileHeaders = new AddFileHeaders();
        addFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
        AddFileRequest addFileRequest = new AddFileRequest()
                .setParentId("1234567")
                .setFileType("file")
                .setFileName("测试文件.txt")
                .setMediaId("#1234kkk")
                .setAddConflictPolicy("autoRename")
                .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx");
        try {
            client.addFileWithOptions("712546", addFileRequest, addFileHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.drive_1_0.client import Client as dingtalkdrive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.drive_1_0 import models as dingtalkdrive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkdrive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkdrive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_file_headers = dingtalkdrive__1__0_models.AddFileHeaders()
        add_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_file_request = dingtalkdrive__1__0_models.AddFileRequest(
            parent_id='1234567',
            file_type='file',
            file_name='测试文件.txt',
            media_id='#1234kkk',
            add_conflict_policy='autoRename',
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
        )
        try:
            client.add_file_with_options('712546', add_file_request, add_file_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_file_headers = dingtalkdrive__1__0_models.AddFileHeaders()
        add_file_headers.x_acs_dingtalk_access_token = '<your access token>'
        add_file_request = dingtalkdrive__1__0_models.AddFileRequest(
            parent_id='1234567',
            file_type='file',
            file_name='测试文件.txt',
            media_id='#1234kkk',
            add_conflict_policy='autoRename',
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
        )
        try:
            await client.add_file_with_options_async('712546', add_file_request, add_file_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddFileHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\AddFileRequest;
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
        $addFileHeaders = new AddFileHeaders([]);
        $addFileHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $addFileRequest = new AddFileRequest([
            "parentId" => "1234567",
            "fileType" => "file",
            "fileName" => "测试文件.txt",
            "mediaId" => "#1234kkk",
            "addConflictPolicy" => "autoRename",
            "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
        ]);
        try {
            $client->addFileWithOptions("712546", $addFileRequest, $addFileHeaders, new RuntimeOptions([]));
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
  dingtalkdrive_1_0  "github.com/alibabacloud-go/dingtalk/drive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkdrive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkdrive_1_0.Client{}
  _result, _err = dingtalkdrive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  addFileHeaders := &dingtalkdrive_1_0.AddFileHeaders{}
  addFileHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  addFileRequest := &dingtalkdrive_1_0.AddFileRequest{
    ParentId: tea.String("1234567"),
    FileType: tea.String("file"),
    FileName: tea.String("测试文件.txt"),
    MediaId: tea.String("#1234kkk"),
    AddConflictPolicy: tea.String("autoRename"),
    UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddFileWithOptions(tea.String("712546"), addFileRequest, addFileHeaders, &util.RuntimeOptions{})
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
import dingtalkdrive_1_0, * as $dingtalkdrive_1_0 from '@alicloud/dingtalk/drive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkdrive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkdrive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let addFileHeaders = new $dingtalkdrive_1_0.AddFileHeaders({ });
    addFileHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let addFileRequest = new $dingtalkdrive_1_0.AddFileRequest({
      parentId: "1234567",
      fileType: "file",
      fileName: "测试文件.txt",
      mediaId: "#1234kkk",
      addConflictPolicy: "autoRename",
      unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
    });
    try {
      await client.addFileWithOptions("712546", addFileRequest, addFileHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkdrive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkdrive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddFileHeaders addFileHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddFileHeaders();
            addFileHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddFileRequest addFileRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.AddFileRequest
            {
                ParentId = "1234567",
                FileType = "file",
                FileName = "测试文件.txt",
                MediaId = "#1234kkk",
                AddConflictPolicy = "autoRename",
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
            };
            try
            {
                client.AddFileWithOptions("712546", addFileRequest, addFileHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkdrive__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkdrive_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkdrive_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::Client> client = make_shared<Alibabacloud_Dingtalkdrive_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddFileHeaders> addFileHeaders = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddFileHeaders>();
  addFileHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::AddFileRequest> addFileRequest = make_shared<Alibabacloud_Dingtalkdrive_1_0::AddFileRequest>(map<string, boost::any>({
    {"parentId", boost::any(string("1234567"))},
    {"fileType", boost::any(string("file"))},
    {"fileName", boost::any(string("测试文件.txt"))},
    {"mediaId", boost::any(string("#1234kkk"))},
    {"addConflictPolicy", boost::any(string("autoRename"))},
    {"unionId", boost::any(string("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"))}
  }));
  try {
    client->addFileWithOptions(make_shared<string>("712546"), addFileRequest, addFileHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "spaceId" : "123456789",
  "parentId" : "1234567",
  "fileId" : "123456",
  "fileName" : "测试文件.txt",
  "filePath" : "/测试目录/测试文件.txt",
  "fileType" : "image",
  "contentType" : "file",
  "fileExtension" : "txt",
  "fileSize" : 23,
  "createTime" : "2016-02-28T10:47:08Z",
  "modifyTime" : "2016-02-28T10:47:08Z",
  "creator" : "user123",
  "modifier" : "user123"
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Invalid Param | 参数错误 |
| 400 | filename.invalid | File name error. | 文件名非法 |
| 400 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 400 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 400 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 400 | folder.exist | Folder already exist. | 目录已存在 |
| 400 | quota.insufficient | Remain quota is insufficient. | 剩余容量不足 |
| 500 | unknown.error | Unknown Error | 未知错误 |
