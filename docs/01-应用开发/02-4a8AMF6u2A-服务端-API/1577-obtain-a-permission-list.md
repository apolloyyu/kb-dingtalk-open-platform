---
title: "获取权限列表"
source_url: "https://open.dingtalk.com/document/development/obtain-a-permission-list"
namespace: "development"
slug: "obtain-a-permission-list"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > 文档/文件 > 钉盘 > 权限管理 > 获取权限列表"
doc_id: "LkxUirZKhM"
updated_at: "2026-08-25 09:38:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-permission-list
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > 文档/文件 > 钉盘 > 权限管理 > 获取权限列表
> Updated: 2026-08-25 09:38:33

# 获取权限列表

调用本接口获取用户对钉盘空间和文件的权限列表。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取权限列表](0684-get-permission-list.md)接口，已接入用户不受影响。

## 权限

要调用此API，需要以下权限之一。

| 应用类型 | 是否支持 | 权限 | API Explorer调试 |
| --- | --- | --- | --- |
| 企业内部应用 | 支持 | **[!NOTE]**  不支持新增 | — |
| 第三方企业应用 | 支持 | — |
| 第三方个人应用 | 暂不支持 | — |

## 请求方法

```
GET /v1.0/drive/spaces/{spaceId}/files/{fileId}/permissions?unionId=String HTTP/1.1
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
| fileId | String | 是 | 文件ID，调用[获取文件或文件夹列表](0666-get-a-list-of-files-or-folders.md)接口获取fileId参数值。 |

## Query参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户unionId，调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

## 返回参数

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| members | Array | 企业内成员权限列表。 |
| role | String | 权限角色。   - **owner**：所有者 - **admin**：管理员 - **editor**：可编辑 - **viewer**：可查看/下载 - **only\_viewer**：只读 |
| member | Object | 成员信息。 |
| corpId | String | 企业的CorpId。 |
| memberType | String | 成员类型。   - **org**：企业 - **department**：部门 - **conversation**：群 - **user**：用户 |
| memberId | String | 成员ID。   - 当**memberType**为**org**时，取值为**corpId** - 当**memberType**为**department**时，取值为**deptId** - 当**memberType**为**conversation**时，取值为**chatId** - 当**memberType**为**user**时，取值为**staffId** |
| memberName | String | 成员名称。 |
| extend | Boolean | 是否是继承的权限。 |
| outMembers | Array | 企业外成员权限列表。 |
| role | String | 权限角色。 |
| member | Object | 成员信息。 |
| corpId | String | 企业的CorpId。 |
| memberType | String | 成员类型。 |
| memberId | String | 成员ID。 |
| memberName | String | 成员名称。 |
| extend | Boolean | 是否是继承的权限。 |

## 示例

**请求示例**

HTTP

```
GET /v1.0/drive/spaces/<spaceId>/files/<fileId>/permissions?unionId=sKUPRiijiSrqsuwqcPiSdbeNwiXxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2db66caxxxx
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
        ListPermissionsHeaders listPermissionsHeaders = new ListPermissionsHeaders();
        listPermissionsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ListPermissionsRequest listPermissionsRequest = new ListPermissionsRequest()
                .setUnionId("sKUPRiijiSrqsuwqcPiSdbeNwiXxx");
        try {
            client.listPermissionsWithOptions("<spaceId>", "<fileId>", listPermissionsRequest, listPermissionsHeaders, new RuntimeOptions());
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
        list_permissions_headers = dingtalkdrive__1__0_models.ListPermissionsHeaders()
        list_permissions_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_permissions_request = dingtalkdrive__1__0_models.ListPermissionsRequest(
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
        )
        try:
            client.list_permissions_with_options('<spaceId>', '<fileId>', list_permissions_request, list_permissions_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_permissions_headers = dingtalkdrive__1__0_models.ListPermissionsHeaders()
        list_permissions_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_permissions_request = dingtalkdrive__1__0_models.ListPermissionsRequest(
            union_id='sKUPRiijiSrqsuwqcPiSdbeNwiXxx'
        )
        try:
            await client.list_permissions_with_options_async('<spaceId>', '<fileId>', list_permissions_request, list_permissions_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\ListPermissionsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vdrive_1_0\Models\ListPermissionsRequest;
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
        $listPermissionsHeaders = new ListPermissionsHeaders([]);
        $listPermissionsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listPermissionsRequest = new ListPermissionsRequest([
            "unionId" => "sKUPRiijiSrqsuwqcPiSdbeNwiXxx"
        ]);
        try {
            $client->listPermissionsWithOptions("<spaceId>", "<fileId>", $listPermissionsRequest, $listPermissionsHeaders, new RuntimeOptions([]));
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

  listPermissionsHeaders := &dingtalkdrive_1_0.ListPermissionsHeaders{}
  listPermissionsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listPermissionsRequest := &dingtalkdrive_1_0.ListPermissionsRequest{
    UnionId: tea.String("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListPermissionsWithOptions(tea.String("<spaceId>"), tea.String("<fileId>"), listPermissionsRequest, listPermissionsHeaders, &util.RuntimeOptions{})
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
    let listPermissionsHeaders = new $dingtalkdrive_1_0.ListPermissionsHeaders({ });
    listPermissionsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listPermissionsRequest = new $dingtalkdrive_1_0.ListPermissionsRequest({
      unionId: "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
    });
    try {
      await client.listPermissionsWithOptions("<spaceId>", "<fileId>", listPermissionsRequest, listPermissionsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListPermissionsHeaders listPermissionsHeaders = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListPermissionsHeaders();
            listPermissionsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListPermissionsRequest listPermissionsRequest = new AlibabaCloud.SDK.Dingtalkdrive_1_0.Models.ListPermissionsRequest
            {
                UnionId = "sKUPRiijiSrqsuwqcPiSdbeNwiXxx",
            };
            try
            {
                client.ListPermissionsWithOptions("<spaceId>", "<fileId>", listPermissionsRequest, listPermissionsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::ListPermissionsHeaders> listPermissionsHeaders = make_shared<Alibabacloud_Dingtalkdrive_1_0::ListPermissionsHeaders>();
  listPermissionsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkdrive_1_0::ListPermissionsRequest> listPermissionsRequest = make_shared<Alibabacloud_Dingtalkdrive_1_0::ListPermissionsRequest>(map<string, boost::any>({
    {"unionId", boost::any(string("sKUPRiijiSrqsuwqcPiSdbeNwiXxx"))}
  }));
  try {
    client->listPermissionsWithOptions(make_shared<string>("<spaceId>"), make_shared<string>("<fileId>"), listPermissionsRequest, listPermissionsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "members" : [ {
    "role" : "viewer",
    "member" : {
      "corpId" : "ding32fff839a3e0xxxx",
      "memberType" : "user",
      "memberId" : "123",
      "memberName" : "张三"
    },
    "extend" : true
  } ],
  "outMembers" : [ {
    "role" : "editor",
    "member" : {
      "corpId" : "ding32fff8391110xxxx",
      "memberType" : "dept",
      "memberId" : "876",
      "memberName" : "测试部门"
    },
    "extend" : false
  } ]
}
```

## 错误码

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Invalid Param | 参数错误 |
| 400 | request.overlimit | You have sent too many requests. | 请求过于频繁 |
| 400 | unsupported.operation | Does not support the operation | 暂不支持该操作 |
| 400 | no.priviledge | You are not authorized to perform this operation. | 你没有权限进行此操作 |
| 404 | object.not.exist | File does not exist or has been deleted. | 文件不存在或已删除 |
| 500 | unknown.error | Unknown Error | 未知错误 |
