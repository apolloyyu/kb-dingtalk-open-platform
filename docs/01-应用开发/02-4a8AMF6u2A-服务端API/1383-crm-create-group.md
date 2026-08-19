---
title: "创建客户群组"
source_url: "https://open.dingtalk.com/document/development/crm-create-group"
namespace: "development"
slug: "crm-create-group"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户群 > 创建客户群组"
doc_id: "MgkbJv4hxd"
updated_at: "2025-10-09 18:06:23"
---

> Source: https://open.dingtalk.com/document/development/crm-create-group
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户群 > 创建客户群组
> Updated: 2025-10-09 18:06:23

# 创建客户群组

调用本接口，用于创建客户群组。

## **接口调用说明**

客户群组是一组客户群的集合，有以下特点：

- 客户群组可以设置群成员数的最大值，当每个客户群成员数超过最大值，会自动创建一个新的客户群。
- 每次创建新群时，会自动设置群主、群管理员、群公告等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/groupSets |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Crm.CustomerGroup.Write-获取CRM主数据的接口访问权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| name | String | 是 | 群组名。 |
| ownerUserId | String | 是 | 群主userId。    裂变出的新群会自动设置该userId为群主。 |
| creatorUserId | String | 是 | 创建人userId。 |
| templateId | String | 否 | 群模板Id。    该参数暂不支持使用。 |
| memberQuota | Integer | 否 | 单个群的人数上限，最大值900。 |
| managerUserIds | String | 否 | 群管理员userId列表，多个用逗号隔开。    裂变出的新群会自动设置这些userId为群管理员。 |
| notice | String | 否 | 群公告文本。    裂变出的新群会自动设置上该群公告。 |
| noticeToped | Integer | 否 | 群公告是否置顶。   - **0**：否 - **1**：是     裂变出的新群会自动设置该属性，默认不置顶。 |
| relationType | String | 是 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| welcome | String | 否 | 新成员入群后收到的欢迎语。    该参数暂不支持使用。 |

### 请求示例

HTTP

```
POST /v1.0/crm/groupSets HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:access_token
Content-Type:application/json

{
  "name" : "群组名",
  "ownerUserId" : "301227837930",
  "creatorUserId" : "301227837930",
  "templateId" : "asdasd-adsfdsfdsf-www",
  "memberQuota" : 100,
  "managerUserIds" : "301227837930,301227837935",
  "notice" : "公告",
  "noticeToped" : 1,
  "relationType" : "crm_customer_personal",
  "welcome" : "欢迎加入"
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
        CreateGroupSetHeaders createGroupSetHeaders = new CreateGroupSetHeaders();
        createGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateGroupSetRequest createGroupSetRequest = new CreateGroupSetRequest()
                .setName("群组名")
                .setOwnerUserId("301227837930")
                .setCreatorUserId("301227837930")
                .setTemplateId("asdasd-adsfdsfdsf-www")
                .setMemberQuota(100)
                .setManagerUserIds("301227837930,301227837935")
                .setNotice("公告")
                .setNoticeToped(1)
                .setRelationType("crm_customer_personal")
                .setWelcome("欢迎加入");
        try {
            client.createGroupSetWithOptions(createGroupSetRequest, createGroupSetHeaders, new RuntimeOptions());
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
        create_group_set_headers = dingtalkcrm__1__0_models.CreateGroupSetHeaders()
        create_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_set_request = dingtalkcrm__1__0_models.CreateGroupSetRequest(
            name='群组名',
            owner_user_id='301227837930',
            creator_user_id='301227837930',
            template_id='asdasd-adsfdsfdsf-www',
            member_quota=100,
            manager_user_ids='301227837930,301227837935',
            notice='公告',
            notice_toped=1,
            relation_type='crm_customer_personal',
            welcome='欢迎加入'
        )
        try:
            client.create_group_set_with_options(create_group_set_request, create_group_set_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_group_set_headers = dingtalkcrm__1__0_models.CreateGroupSetHeaders()
        create_group_set_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_group_set_request = dingtalkcrm__1__0_models.CreateGroupSetRequest(
            name='群组名',
            owner_user_id='301227837930',
            creator_user_id='301227837930',
            template_id='asdasd-adsfdsfdsf-www',
            member_quota=100,
            manager_user_ids='301227837930,301227837935',
            notice='公告',
            notice_toped=1,
            relation_type='crm_customer_personal',
            welcome='欢迎加入'
        )
        try:
            await client.create_group_set_with_options_async(create_group_set_request, create_group_set_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\CreateGroupSetHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\CreateGroupSetRequest;
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
        $createGroupSetHeaders = new CreateGroupSetHeaders([]);
        $createGroupSetHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createGroupSetRequest = new CreateGroupSetRequest([
            "name" => "群组名",
            "ownerUserId" => "301227837930",
            "creatorUserId" => "301227837930",
            "templateId" => "asdasd-adsfdsfdsf-www",
            "memberQuota" => 100,
            "managerUserIds" => "301227837930,301227837935",
            "notice" => "公告",
            "noticeToped" => 1,
            "relationType" => "crm_customer_personal",
            "welcome" => "欢迎加入"
        ]);
        try {
            $client->createGroupSetWithOptions($createGroupSetRequest, $createGroupSetHeaders, new RuntimeOptions([]));
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

  createGroupSetHeaders := &dingtalkcrm_1_0.CreateGroupSetHeaders{}
  createGroupSetHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createGroupSetRequest := &dingtalkcrm_1_0.CreateGroupSetRequest{
    Name: tea.String("群组名"),
    OwnerUserId: tea.String("301227837930"),
    CreatorUserId: tea.String("301227837930"),
    TemplateId: tea.String("asdasd-adsfdsfdsf-www"),
    MemberQuota: tea.Int32(100),
    ManagerUserIds: tea.String("301227837930,301227837935"),
    Notice: tea.String("公告"),
    NoticeToped: tea.Int32(1),
    RelationType: tea.String("crm_customer_personal"),
    Welcome: tea.String("欢迎加入"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateGroupSetWithOptions(createGroupSetRequest, createGroupSetHeaders, &util.RuntimeOptions{})
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
    let createGroupSetHeaders = new $dingtalkcrm_1_0.CreateGroupSetHeaders({ });
    createGroupSetHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createGroupSetRequest = new $dingtalkcrm_1_0.CreateGroupSetRequest({
      name: "群组名",
      ownerUserId: "301227837930",
      creatorUserId: "301227837930",
      templateId: "asdasd-adsfdsfdsf-www",
      memberQuota: 100,
      managerUserIds: "301227837930,301227837935",
      notice: "公告",
      noticeToped: 1,
      relationType: "crm_customer_personal",
      welcome: "欢迎加入",
    });
    try {
      await client.createGroupSetWithOptions(createGroupSetRequest, createGroupSetHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupSetHeaders createGroupSetHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupSetHeaders();
            createGroupSetHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupSetRequest createGroupSetRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.CreateGroupSetRequest
            {
                Name = "群组名",
                OwnerUserId = "301227837930",
                CreatorUserId = "301227837930",
                TemplateId = "asdasd-adsfdsfdsf-www",
                MemberQuota = 100,
                ManagerUserIds = "301227837930,301227837935",
                Notice = "公告",
                NoticeToped = 1,
                RelationType = "crm_customer_personal",
                Welcome = "欢迎加入",
            };
            try
            {
                client.CreateGroupSetWithOptions(createGroupSetRequest, createGroupSetHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| name | String | 群组名。 |
| openGroupSetId | String | 客户群组openGroupSetId。 |
| relationType | String | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| memberQuota | Long | 单个群的人数上限。 |
| memberCount | Long | 群组内所有群的成员数量。 |
| templateId | String | 群模板Id。      该字段暂无使用场景。 |
| ownerUserId | String | 群主userId，裂变出的新群会自动设置该userId为群主。 |
| managerUserIds | String | 群管理员userId列表，多个用逗号隔开，裂变出的新群会自动设置这些userId为群管理员。 |
| notice | String | 群公告文本，裂变出的新群会自动设置上该群公告。 |
| noticeToped | Integer | 群公告是否置顶。   - **0**：否 - **1**：是       裂变出的新群会自动设置该属性，默认不置顶。 |
| owner | Object | 群主信息。 |
| name | String | 群主姓名。 |
| userId | String | 群主userId。 |
| manager | Array | 群管理员信息列表。 |
| name | String | 群管理员姓名。 |
| userId | String | 群管理员userId。 |
| lastOpenConversationId | String | 群组创建后，第一个裂变群的openConversationId。 |
| gmtCreate | String | 创建时间。 |
| gmtModified | String | 修改时间。 |
| inviteLink | String | 客户群组的邀请链接。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "name" : "群组名",
  "openGroupSetId" : "sdffhjghjfghjvddda",
  "relationType" : "crm_customer_personal",
  "memberQuota" : 100,
  "memberCount" : 35,
  "templateId" : "ddgdfg-tttthhhjj-aasdfghfgh",
  "ownerUserId" : "301227837930",
  "managerUserIds" : "301227837930,301227837931",
  "notice" : "公告",
  "noticeToped" : 1,
  "owner" : {
    "name" : "张三",
    "userId" : "301227837930"
  },
  "manager" : [ {
    "name" : "李四",
    "userId" : "401227837930"
  } ],
  "lastOpenConversationId" : "42752389106",
  "gmtCreate" : "2021-12-21T12:03Z",
  "gmtModified" : "2021-12-21T12:03Z",
  "inviteLink" : "dingtalk://dingtalkclient/page/link?pc_slide=true&redirect_type=jump&url=https%3A%2F%2Fn.dingtalk.com%2Fdingding%2Fcustomer-group%2Findex"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter | invalid parameter. | 无效的参数 |
| 400 | needParameterNotPass | need parameter, group name or owner or creator or template not pass. | 必传参数，群名称、群主、创建人或模板id参数未传 |
| 400 | recordNotExist | record not exist. | 记录不存在 |
| 400 | overQuota | over quota. | 超过限制 |
| 500 | systemError | system error. | 系统错误 |
