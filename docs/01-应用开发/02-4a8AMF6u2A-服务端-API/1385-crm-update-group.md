---
title: "更新客户群组"
source_url: "https://open.dingtalk.com/document/development/crm-update-group"
namespace: "development"
slug: "crm-update-group"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 更新客户群组"
doc_id: "2vS1U4O2SJ"
updated_at: "2026-06-04 19:12:20"
---

> Source: https://open.dingtalk.com/document/development/crm-update-group
> Path: 应用开发 / 服务端 API / 更多开放 > 客户管理（官方CRM） > 客户群 > 更新客户群组
> Updated: 2026-06-04 19:12:20

# 更新客户群组

调用本接口更新客户群组信息，新创建的客户群将按照更新后的信息创建群，已经创建的客户群信息不会更新。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/groupSets/set |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Crm.CustomerGroup.Write-客户管理客户群写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证：  企业内部应用，可通过[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。  第三方企业应用，可通过[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| openGroupSetId | String | 是 | 群组openGroupSetId，调用[查询客户群组列表](1386-query-groups.md)接口获取openGroupSetId参数值。 |
| name | String | 否 | 群组名。 |
| memberQuota | Integer | 否 | 单个群的人数上限。 |
| ownerUserId | String | 否 | 群主userId。      裂变出的新群会自动设置该userId为群主。 |
| managerUserIds | String | 否 | 群管理员userId列表，多个用逗号隔开，裂变出的新群会自动设置这些userId为群管理员。 |
| notice | String | 否 | 群公告文本。      裂变出的新群会自动设置上该群的群公告。 |
| noticeToped | Integer | 否 | 群公告是否置顶。   - **0**：否 - **1**：是       裂变出的新群会自动设置上该属性。 |
| templateId | String | 否 | 群模板Id。      该参数暂不支持使用。 |
| welcome | String | 否 | 新成员入群后收到的欢迎语。      该参数暂不支持使用。 |

### 请求示例

HTTP

```
PUT /v1.0/crm/groupSets/set HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "openGroupSetId" : "dfgfghfghdsfdsf",
  "name" : "营销群",
  "memberQuota" : 200,
  "ownerUserId" : "301227837938",
  "managerUserIds" : "301227837938",
  "notice" : "公告",
  "noticeToped" : 1,
  "templateId" : "dfgfgh-vbbfghjghj-fdsfdsf",
  "welcome" : "欢迎入群"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcrm_1_0.*;
import com.aliyun.dingtalkcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        UpdateGroupSetHeaders updateGroupSetHeaders = new UpdateGroupSetHeaders();
        updateGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateGroupSetRequest updateGroupSetRequest = new UpdateGroupSetRequest()
                .setOpenGroupSetId("dfgfghfghdsfdsf")
                .setName("营销群")
                .setMemberQuota(200)
                .setOwnerUserId("301227837938")
                .setManagerUserIds("301227837938")
                .setNotice("公告")
                .setNoticeToped(1)
                .setTemplateId("dfgfgh-vbbfghjghj-fdsfdsf")
                .setWelcome("欢迎入群");
        try {
            client.updateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_group_set_headers = dingtalkcrm__1__0_models.UpdateGroupSetHeaders()
        update_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_group_set_request = dingtalkcrm__1__0_models.UpdateGroupSetRequest(
            open_group_set_id='dfgfghfghdsfdsf',
            name='营销群',
            member_quota=200,
            owner_user_id='301227837938',
            manager_user_ids='301227837938',
            notice='公告',
            notice_toped=1,
            template_id='dfgfgh-vbbfghjghj-fdsfdsf',
            welcome='欢迎入群'
        )
        try:
            client.update_group_set_with_options(update_group_set_request, update_group_set_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_group_set_headers = dingtalkcrm__1__0_models.UpdateGroupSetHeaders()
        update_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_group_set_request = dingtalkcrm__1__0_models.UpdateGroupSetRequest(
            open_group_set_id='dfgfghfghdsfdsf',
            name='营销群',
            member_quota=200,
            owner_user_id='301227837938',
            manager_user_ids='301227837938',
            notice='公告',
            notice_toped=1,
            template_id='dfgfgh-vbbfghjghj-fdsfdsf',
            welcome='欢迎入群'
        )
        try:
            await client.update_group_set_with_options_async(update_group_set_request, update_group_set_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\UpdateGroupSetHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\UpdateGroupSetRequest;
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
        $updateGroupSetHeaders = new UpdateGroupSetHeaders([]);
        $updateGroupSetHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateGroupSetRequest = new UpdateGroupSetRequest([
            "openGroupSetId" => "dfgfghfghdsfdsf",
            "name" => "营销群",
            "memberQuota" => 200,
            "ownerUserId" => "301227837938",
            "managerUserIds" => "301227837938",
            "notice" => "公告",
            "noticeToped" => 1,
            "templateId" => "dfgfgh-vbbfghjghj-fdsfdsf",
            "welcome" => "欢迎入群"
        ]);
        try {
            $client->updateGroupSetWithOptions($updateGroupSetRequest, $updateGroupSetHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateGroupSetHeaders := &dingtalkcrm_1_0.UpdateGroupSetHeaders{}
  updateGroupSetHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateGroupSetRequest := &dingtalkcrm_1_0.UpdateGroupSetRequest{
    OpenGroupSetId: tea.String("dfgfghfghdsfdsf"),
    Name: tea.String("营销群"),
    MemberQuota: tea.Int32(200),
    OwnerUserId: tea.String("301227837938"),
    ManagerUserIds: tea.String("301227837938"),
    Notice: tea.String("公告"),
    NoticeToped: tea.Int32(1),
    TemplateId: tea.String("dfgfgh-vbbfghjghj-fdsfdsf"),
    Welcome: tea.String("欢迎入群"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let updateGroupSetHeaders = new $dingtalkcrm_1_0.UpdateGroupSetHeaders({ });
    updateGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateGroupSetRequest = new $dingtalkcrm_1_0.UpdateGroupSetRequest({
      openGroupSetId: "dfgfghfghdsfdsf",
      name: "营销群",
      memberQuota: 200,
      ownerUserId: "301227837938",
      managerUserIds: "301227837938",
      notice: "公告",
      noticeToped: 1,
      templateId: "dfgfgh-vbbfghjghj-fdsfdsf",
      welcome: "欢迎入群",
    });
    try {
      await client.updateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateGroupSetHeaders updateGroupSetHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateGroupSetHeaders();
            updateGroupSetHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateGroupSetRequest updateGroupSetRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateGroupSetRequest
            {
                OpenGroupSetId = "dfgfghfghdsfdsf",
                Name = "营销群",
                MemberQuota = 200,
                OwnerUserId = "301227837938",
                ManagerUserIds = "301227837938",
                Notice = "公告",
                NoticeToped = 1,
                TemplateId = "dfgfgh-vbbfghjghj-fdsfdsf",
                Welcome = "欢迎入群",
            };
            try
            {
                client.UpdateGroupSetWithOptions(updateGroupSetRequest, updateGroupSetHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
|  | Boolean | 更新操作是否成功， true表示更新成功。 |

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
| 400 | overQuota | over quota. | 超过限制 |
| 400 | needParameterNotPass | need parameter not pass. | 必传参数未传 |
| 400 | recordNotExist | record not exist. | 记录不存在 |
| 400 | invalidParameter | invalid parameter. | 参数错误 |
| 500 | unknownError | unknown error. | 未知错误 |
