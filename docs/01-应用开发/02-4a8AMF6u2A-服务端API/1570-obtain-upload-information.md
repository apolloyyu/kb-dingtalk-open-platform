---
title: "获取文件上传信息"
source_url: "https://open.dingtalk.com/document/development/obtain-upload-information"
namespace: "development"
slug: "obtain-upload-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 文件传输 > 获取文件上传信息"
doc_id: "Y3kSXNBVJv"
updated_at: "2026-08-25 09:38:27"
---

> Source: https://open.dingtalk.com/document/development/obtain-upload-information
> Path: 应用开发 / 服务端API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 文件传输 > 获取文件上传信息
> Updated: 2026-08-25 09:38:27

# 获取文件上传信息

调用本接口获取文件上传信息。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取文件上传信息](0674-obtain-file-upload-informations.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v1.0/drive/spaces/{spaceId}/files/{parentId}/uploadInfos?unionId=String&fileName=String&fileSize=Long&md5=String&addConflictPolicy=String&mediaId=String HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:String
Content-Type:application/json
```

## Header参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

## Path参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| spaceId | String | 是 | 钉盘空间ID，调用[获取空间列表](0636-queries-a-space-list.md)接口获取spaceId参数值。 |
| parentId | String | 是 | 父目录ID。  **[!NOTE]**  根目录时传**0**。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
| fileName | String | 是 | 文件名，带文件扩展名。 |
| fileSize | Long | 是 | 文件大小。 |
| md5 | String | 是 | 文件md5。 |
| addConflictPolicy | String | 否 | 文件名称冲突策略，取值：   - **autoRename**：自动重命名 - **overwrite**：覆写 - **returnExisting**：返回已存在文件 - **returnError**：报错 |
| mediaId | String | 否 | 对应OSS Object Key。   - 如果首次调用本接口，为了获取文件的上传信息，无需填写**mediaId**。 - 如果非首次调用本接口，为了刷新上次调用时返回值中的**accessToken**，需要传入上次调用返回值的**mediaId**。 |
| withRegion | Boolean | 否 | 是否返回区域信息。默认不返回。 |
| withInternalEndPoint | Boolean | 否 | 是否返回内部OSS访问域名。默认不返回。 |
| callerRegion | String | 否 | 区域亲和性。文件会尽可能存储到指定的区域，但不是一定。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| stsUploadInfo | Object | sts加签上传信息。 |
| bucket | String | OSS存储空间。 |
| endPoint | String | OSS访问域名。 |
| internalEndPoint | String | 内部OSS访问域名。 |
| accessKeyId | String | 阿里云账号的临时accessKeyId。 |
| accessKeySecret | String | 阿里云账号的临时accessKeySecret。 |
| accessToken | String | 临时访问密钥。  **[!NOTE]**  密钥过期后，可再次调用本接口，并传入返回值中的mediaId刷新密钥。 |
| accessTokenExpirationMillis | Long | 密钥过期时间，毫秒。 |
| mediaId | String | 对应OSS Object Key，可用于刷新token以及调用[添加文件（夹）](1564-add-file-and-folder.md)接口添加文件记录。 |
| headerSignatureUploadInfo | Object | hdader加签上传信息。 |
| resourceUrl | String | 上传地址 |
| internalResourceUrl | String | 内网上传地址 |
| expirationSeconds | Integer | 过期秒数 |
| headers | Map | header加签信息 |
| mediaId | String | 对应OSS Object Key，可用于刷新token以及调用[添加文件（夹）](1564-add-file-and-folder.md)接口添加文件记录。 |
| region | String | 文件所存储的区域 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/drive/spaces/3245325/files/0/uploadInfos?unionId=sKUPRiijiSrqsuwqcPiSdbeNwiXxx&fileName=测试文件.txt&fileSize=156&md5=fekafjekfe&addConflictPolicy=autoRename&mediaId=#12345kkk HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2db66ca1xxx
Content-Type:application/json
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
        GetUploadInfoHeaders getUploadInfoHeaders = new GetUploadInfoHeaders();
        getUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetUploadInfoRequest getUploadInfoRequest = new GetUploadInfoRequest()
                .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx")
                .setFileName("测试文件.txt")
                .setFileSize(156L)
                .setMd5("fekafjekfe")
                .setAddConflictPolicy("autoRename")
                .setMediaId("#12345kkk");
        try {
            client.getUploadInfoWithOptions("3245325", "0", getUploadInfoRequest, getUploadInfoHeaders, new RuntimeOptions());
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
        get_upload_info_headers = dingtalkdrive__1__0_models.GetUploadInfoHeaders()
        get_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_upload_info_request = dingtalkdrive__1__0_models.GetUploadInfoRequest(
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx',
            file_name='测试文件.txt',
            file_size=156,
            md_5='fekafjekfe',
            add_conflict_policy='autoRename',
            media_id='#12345kkk'
        )
        try:
            client.get_upload_info_with_options('3245325', '0', get_upload_info_request, get_upload_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_upload_info_headers = dingtalkdrive__1__0_models.GetUploadInfoHeaders()
        get_upload_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_upload_info_request = dingtalkdrive__1__0_models.GetUploadInfoRequest(
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx',
            file_name='测试文件.txt',
            file_size=156,
            md_5='fekafjekfe',
            add_conflict_policy='autoRename',
            media_id='#12345kkk',
            with_region=False,
            with_internal_end_point=False,
            caller_region='cn-zhangjiakou'
        )
        try:
            await client.get_upload_info_with_options_async('3245325', '0', get_upload_info_request, get_upload_info_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\GetUploadInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\GetUploadInfoRequest;
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
        $getUploadInfoHeaders = new GetUploadInfoHeaders([]);
        $getUploadInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getUploadInfoRequest = new GetUploadInfoRequest([
            "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
            "fileName" => "测试文件.txt",
            "fileSize" => 156,
            "md5" => "fekafjekfe",
            "addConflictPolicy" => "autoRename",
            "mediaId" => "#12345kkk"
        ]);
        try {
            $client->getUploadInfoWithOptions("3245325", "0", $getUploadInfoRequest, $getUploadInfoHeaders, new RuntimeOptions([]));
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

  getUploadInfoHeaders := &dingtalkdrive_1_0.GetUploadInfoHeaders{}
  getUploadInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getUploadInfoRequest := &dingtalkdrive_1_0.GetUploadInfoRequest{
    UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
    FileName: tea.String("测试文件.txt"),
    FileSize: tea.Int64(156),
    Md5: tea.String("fekafjekfe"),
    AddConflictPolicy: tea.String("autoRename"),
    MediaId: tea.String("#12345kkk"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetUploadInfoWithOptions(tea.String("3245325"), tea.String("0"), getUploadInfoRequest, getUploadInfoHeaders, &util.RuntimeOptions{})
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
    let getUploadInfoHeaders = new $dingtalkdrive_1_0.GetUploadInfoHeaders({ });
    getUploadInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getUploadInfoRequest = new $dingtalkdrive_1_0.GetUploadInfoRequest({
      unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
      fileName: "测试文件.txt",
      fileSize: 156,
      md5: "fekafjekfe",
      addConflictPolicy: "autoRename",
      mediaId: "#12345kkk",
    });
    try {
      await client.getUploadInfoWithOptions("3245325", "0", getUploadInfoRequest, getUploadInfoHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoHeaders getUploadInfoHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoHeaders();
            getUploadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoRequest getUploadInfoRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoRequest
            {
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
                FileName = "测试文件.txt",
                FileSize = 156,
                Md5 = "fekafjekfe",
                AddConflictPolicy = "autoRename",
                MediaId = "#12345kkk",
            };
            try
            {
                client.GetUploadInfoWithOptions("3245325", "0", getUploadInfoRequest, getUploadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoHeaders getUploadInfoHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoHeaders();
            getUploadInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoRequest getUploadInfoRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.GetUploadInfoRequest
            {
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
                FileName = "测试文件.txt",
                FileSize = 156,
                Md5 = "fekafjekfe",
                AddConflictPolicy = "autoRename",
                MediaId = "#12345kkk",

            };
            try
            {
                client.GetUploadInfoWithOptions("3245325", "0", getUploadInfoRequest, getUploadInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

**返回示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "stsUploadInfo" : {
    "bucket" : "lippi-space-zjk",
    "endPoint" : "oss-cn-zhangjiakou.aliyuncs.com",
    "internalEndPoint" : "oss-cn-zhangjiakou-internal.aliyuncs.com",
    "accessKeyId" : "accessKeyId",
    "accessKeySecret" : "accessKeySecret",
    "accessToken" : "accesxxx",
    "accessTokenExpirationMillis" : 900000,
    "mediaId" : "yundisk0/xxx.file"
  }
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
| 400 | insufficient.capacity | Insufficient capacity | 剩余空间不足 |
| 403 | unsupported.operation | Does not support cross-org access | 不支持跨企业访问 |
| 404 | object.not.exist | File does not exist or has been deleted. | 文件不存在或已删除 |
| 500 | unknown.error | Unknown Error | 未知错误 |
