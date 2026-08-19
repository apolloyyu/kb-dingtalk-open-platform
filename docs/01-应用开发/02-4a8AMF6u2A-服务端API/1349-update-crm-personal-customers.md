---
title: "更新个人或企业客户数据"
source_url: "https://open.dingtalk.com/document/development/update-crm-personal-customers"
namespace: "development"
slug: "update-crm-personal-customers"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 客户管理（官方CRM） > 客户 > 更新个人或企业客户数据"
doc_id: "Kd5FT4pM7n"
updated_at: "2025-10-09 18:06:04"
---

> Source: https://open.dingtalk.com/document/development/update-crm-personal-customers
> Path: 应用开发 / 服务端API / 更多开放 > 客户管理（官方CRM） > 客户 > 更新个人或企业客户数据
> Updated: 2025-10-09 18:06:04

# 更新个人或企业客户数据

调用本接口，更新CRM个人客户或企业客户信息，包括客户的负责人列表、协同人列表和关系类型等信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/personalCustomers |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_crm\_maindata\_write-维护CRM主数据的接口写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| instanceId | String | 是 | 客户数据ID，调用[根据指定条件查询个人或企业客户数据](1355-obtains-crm-individual-customers-in-batches-based-on-specified-query.md)接口获取instanceId参数值。 |
| modifierUserId | String | 是 | 操作人的用户userId。 |
| modifierNick | String | 否 | 操作人的用户昵称。 |
| data | Map | 是 | 客户数据内容，JSON格式字符串，格式请参见[新增和更新客户字段格式说明V1](1389-add-and-update-customer-field-format-description-v1.md)。 |
| extendData | Map | 否 | 扩展数据。 |
| permission | Object | 否 | 权限。 |
| ownerStaffIds | Array of String | 否 | 负责人的用户userId。 |
| participantStaffIds | Array of String | 否 | 协同人的用户userId。 |
| relationType | String | 否 | 关系类型。   - **crm\_customer**：企业客户 - **crm\_customer\_personal**：个人客户 |
| skipDuplicateCheck | Boolean | 否 | 是否跳过查重字段。   - **true**：是 - **false**：否       企业可在查重设置中设置查重字段，如下图所示。 |
| action | String | 否 | 取值。   - **publicDraw**：公海领取客户 - **publicAssign**：公海分配客户 - 其余场景：不用传 |

### 请求示例

HTTP

```
PUT /v1.0/crm/personalCustomers HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:c3640971xxx
Content-Type:application/json

{
  "instanceId" : "8a0d5031-xxx-",
  "modifierUserId" : "26652461xxx",
  "modifierNick" : "钉三多",
  "permission" : {
    "ownerStaffIds" : [ "266524xxx" ],
    "participantStaffIds" : [ "266524xxx" ]
  },
  "relationType" : "crm_customer",
  "skipDuplicateCheck" : false,
  "action" : "publicDraw"
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
        UpdateCrmPersonalCustomerHeaders updateCrmPersonalCustomerHeaders = new UpdateCrmPersonalCustomerHeaders();
        updateCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission permission = new UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission()
                .setOwnerStaffIds(java.util.Arrays.asList(
                    "266524xxx"
                ))
                .setParticipantStaffIds(java.util.Arrays.asList(
                    "266524xxx"
                ));
        UpdateCrmPersonalCustomerRequest updateCrmPersonalCustomerRequest = new UpdateCrmPersonalCustomerRequest()
                .setInstanceId("8a0d5031-xxx-")
                .setModifierUserId("26652461xxx")
                .setModifierNick("钉三多")
                .setPermission(permission)
                .setRelationType("crm_customer")
                .setSkipDuplicateCheck(false)
                .setAction("publicDraw");
        try {
            client.updateCrmPersonalCustomerWithOptions(updateCrmPersonalCustomerRequest, updateCrmPersonalCustomerHeaders, new RuntimeOptions());
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
        update_crm_personal_customer_headers = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerHeaders()
        update_crm_personal_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        permission = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequestPermission(
            owner_staff_ids=[
                '266524xxx'
            ],
            participant_staff_ids=[
                '266524xxx'
            ]
        )
        update_crm_personal_customer_request = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequest(
            instance_id='8a0d5031-xxx-',
            modifier_user_id='26652461xxx',
            modifier_nick='钉三多',
            permission=permission,
            relation_type='crm_customer',
            skip_duplicate_check=False,
            action='publicDraw'
        )
        try:
            client.update_crm_personal_customer_with_options(update_crm_personal_customer_request, update_crm_personal_customer_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_crm_personal_customer_headers = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerHeaders()
        update_crm_personal_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        permission = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequestPermission(
            owner_staff_ids=[
                '266524xxx'
            ],
            participant_staff_ids=[
                '266524xxx'
            ]
        )
        update_crm_personal_customer_request = dingtalkcrm__1__0_models.UpdateCrmPersonalCustomerRequest(
            instance_id='8a0d5031-xxx-',
            modifier_user_id='26652461xxx',
            modifier_nick='钉三多',
            permission=permission,
            relation_type='crm_customer',
            skip_duplicate_check=False,
            action='publicDraw'
        )
        try:
            await client.update_crm_personal_customer_with_options_async(update_crm_personal_customer_request, update_crm_personal_customer_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\UpdateCrmPersonalCustomerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\UpdateCrmPersonalCustomerRequest\permission;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\UpdateCrmPersonalCustomerRequest;
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
        $updateCrmPersonalCustomerHeaders = new UpdateCrmPersonalCustomerHeaders([]);
        $updateCrmPersonalCustomerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $permission = new permission([
            "ownerStaffIds" => [
                "266524xxx"
            ],
            "participantStaffIds" => [
                "266524xxx"
            ]
        ]);
        $updateCrmPersonalCustomerRequest = new UpdateCrmPersonalCustomerRequest([
            "instanceId" => "8a0d5031-xxx-",
            "modifierUserId" => "26652461xxx",
            "modifierNick" => "钉三多",
            "permission" => $permission,
            "relationType" => "crm_customer",
            "skipDuplicateCheck" => false,
            "action" => "publicDraw"
        ]);
        try {
            $client->updateCrmPersonalCustomerWithOptions($updateCrmPersonalCustomerRequest, $updateCrmPersonalCustomerHeaders, new RuntimeOptions([]));
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

  updateCrmPersonalCustomerHeaders := &dingtalkcrm_1_0.UpdateCrmPersonalCustomerHeaders{}
  updateCrmPersonalCustomerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  permission := &dingtalkcrm_1_0.UpdateCrmPersonalCustomerRequestPermission{
    OwnerStaffIds: []*string{tea.String("266524xxx")},
    ParticipantStaffIds: []*string{tea.String("266524xxx")},
  }
  updateCrmPersonalCustomerRequest := &dingtalkcrm_1_0.UpdateCrmPersonalCustomerRequest{
    InstanceId: tea.String("8a0d5031-xxx-"),
    ModifierUserId: tea.String("26652461xxx"),
    ModifierNick: tea.String("钉三多"),
    Permission: permission,
    RelationType: tea.String("crm_customer"),
    SkipDuplicateCheck: tea.Bool(false),
    Action: tea.String("publicDraw"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateCrmPersonalCustomerWithOptions(updateCrmPersonalCustomerRequest, updateCrmPersonalCustomerHeaders, &util.RuntimeOptions{})
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
    let updateCrmPersonalCustomerHeaders = new $dingtalkcrm_1_0.UpdateCrmPersonalCustomerHeaders({ });
    updateCrmPersonalCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let permission = new $dingtalkcrm_1_0.UpdateCrmPersonalCustomerRequestPermission({
      ownerStaffIds: [
        "266524xxx"
      ],
      participantStaffIds: [
        "266524xxx"
      ],
    });
    let updateCrmPersonalCustomerRequest = new $dingtalkcrm_1_0.UpdateCrmPersonalCustomerRequest({
      instanceId: "8a0d5031-xxx-",
      modifierUserId: "26652461xxx",
      modifierNick: "钉三多",
      permission: permission,
      relationType: "crm_customer",
      skipDuplicateCheck: false,
      action: "publicDraw",
    });
    try {
      await client.updateCrmPersonalCustomerWithOptions(updateCrmPersonalCustomerRequest, updateCrmPersonalCustomerHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateCrmPersonalCustomerHeaders updateCrmPersonalCustomerHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateCrmPersonalCustomerHeaders();
            updateCrmPersonalCustomerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission permission = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateCrmPersonalCustomerRequest.UpdateCrmPersonalCustomerRequestPermission
            {
                OwnerStaffIds = new List<string>
                {
                    "266524xxx"
                },
                ParticipantStaffIds = new List<string>
                {
                    "266524xxx"
                },
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateCrmPersonalCustomerRequest updateCrmPersonalCustomerRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.UpdateCrmPersonalCustomerRequest
            {
                InstanceId = "8a0d5031-xxx-",
                ModifierUserId = "26652461xxx",
                ModifierNick = "钉三多",
                Permission = permission,
                RelationType = "crm_customer",
                SkipDuplicateCheck = false,
                Action = "publicDraw",
            };
            try
            {
                client.UpdateCrmPersonalCustomerWithOptions(updateCrmPersonalCustomerRequest, updateCrmPersonalCustomerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| instanceId | String | 客户数据ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "instanceId" : "8a0d5031-xxx-"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.frequent | request too frequent | 请求过于频繁 |
| 400 | noPermission.to.update | no permission to update this customer | 没有更新此数据的权限 |
| 400 | relationType.not.exists | relationType not exists | relationType不存在 |
| 400 | data.format.error | %s | 表单数据格式错误 |
| 400 | noPermission.to.setField | %s | 没有设置字段的权限 |
| 400 | count.exceeds.limit | count exceeds limit | 数量达到上限 |
| 400 | same.data.exists | same data exists | 已存在相同数据 |
| 400 | invalid.uk.parameter | invalid uk parameter | 查重字段为空 |
| 400 | customerCountUnderPrincipal.exceeds.limit | customer count under principal exceeds limit | 负责人名下客户数量达到上限 |
| 400 | sameMobileCount.exceeds.limit | same mobile count exceeds limit | 同一个手机号不能被添加超过10次 |
| 400 | duplicate.operation | duplicate operation | 重复操作 |
| 400 | data.not.exists | data not exists | 数据不存在 |
| 400 | non.open.customer | draw or assign is not allowed for non-open-customer | 该实例非公海客户，不允许操作 |
| 400 | systemError.appNotExists | %s | 应用不存在 |
| 400 | systemError.notPermittedAccess | %s | 无权限操作 |
| 400 | no.valid.parameter | no valid parameter, can not update | 没有传入有效参数，禁止更新 |
| 400 | modifierUserId.not.exists | modifierUserId not exists | modifierUserId不是企业员工 |
| 400 | mobileFormatError | mobileFormatError | 手机号格式错误 |
| 400 | canNotModifyOutLeadsId | can not modify outLeadsId | 不允许修改outLeadsId |
| 500 | systemError | system error %s %s | 系统错误 |
| 500 | systemError | system error, %s %s | 系统错误 |
