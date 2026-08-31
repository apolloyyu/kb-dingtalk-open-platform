---
title: "新增或删除花名册选项类型字段的选项"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-roster-field-option-modification"
namespace: "development"
slug: "intelligent-personnel-roster-field-option-modification"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "智能人事 > 花名册 > 新增或删除花名册选项类型字段的选项"
doc_id: "EVHoKB1Chw"
updated_at: "2026-06-04 19:10:24"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-roster-field-option-modification
> Path: 应用开发 / 服务端 API / 智能人事 > 花名册 > 新增或删除花名册选项类型字段的选项
> Updated: 2026-06-04 19:10:24

# 新增或删除花名册选项类型字段的选项

调用本接口，新增或删除智能人事花名册选项类型字段的选项。

## **接口调用说明**

本接口不支持操作系统字段，例如：性别。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/rosters/meta/fields/options |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_hrm\_manager-钉钉HRM数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| appAgentId | Long | 否 | 对应应用的agentId值，请参考[基础概念-AgentId](https://open.dingtalk.com/document/development/basic-concepts-beta#884d363067bnq)。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| groupId | String | 是 | 花名册分组ID，可调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取group\_id参数值。 |
| fieldCode | String | 是 | 花名册字段标识。   - 企业内部应用，可调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取。 - 第三方企业应用，可调用[查询花名册中有权限的字段列表](0942-query-the-list-of-fields-with-permissions-in-the-roster.md)接口获取。 |
| labels | Array of String | 是 | 需要修改的选项值列表，最大值20。   - 如果modifyType值为**OPTIONS\_ADD**，该参数值为自定义值。 - 如果modifyType值为**OPTIONS\_DELETE**，该参数值可调用[获取员工花名册字段信息](0939-api-getemployeerosterbyfield.md)接口获取label参数值。 |
| modifyType | String | 是 | 修改类型。   - **OPTIONS\_ADD**：添加选项 - **OPTIONS\_DELETE**：删除选项 |

### 请求示例

HTTP

```
PUT /v1.0/hrm/rosters/meta/fields/options HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "groupId" : "sys05",
  "fieldCode" : "sys05-contractType",
  "labels" : [ "固定期限劳动合同" ],
  "modifyType" : "OPTIONS_ADD"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrm_1_0.models.RosterMetaFieldOptionsUpdateHeaders rosterMetaFieldOptionsUpdateHeaders = new com.aliyun.dingtalkhrm_1_0.models.RosterMetaFieldOptionsUpdateHeaders();
        rosterMetaFieldOptionsUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.RosterMetaFieldOptionsUpdateRequest rosterMetaFieldOptionsUpdateRequest = new com.aliyun.dingtalkhrm_1_0.models.RosterMetaFieldOptionsUpdateRequest()
                .setGroupId("sys05")
                .setFieldCode("sys05-contractType")
                .setLabels(java.util.Arrays.asList(
                    "固定期限劳动合同"
                ))
                .setModifyType("OPTIONS_ADD");
        try {
            client.rosterMetaFieldOptionsUpdateWithOptions(rosterMetaFieldOptionsUpdateRequest, rosterMetaFieldOptionsUpdateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.hrm_1_0.client import Client as dingtalkhrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        roster_meta_field_options_update_headers = dingtalkhrm__1__0_models.RosterMetaFieldOptionsUpdateHeaders()
        roster_meta_field_options_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        roster_meta_field_options_update_request = dingtalkhrm__1__0_models.RosterMetaFieldOptionsUpdateRequest(
            group_id='sys05',
            field_code='sys05-contractType',
            labels=[
                '固定期限劳动合同'
            ],
            modify_type='OPTIONS_ADD'
        )
        try:
            client.roster_meta_field_options_update_with_options(roster_meta_field_options_update_request, roster_meta_field_options_update_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        roster_meta_field_options_update_headers = dingtalkhrm__1__0_models.RosterMetaFieldOptionsUpdateHeaders()
        roster_meta_field_options_update_headers.x_acs_dingtalk_access_token = '<your access token>'
        roster_meta_field_options_update_request = dingtalkhrm__1__0_models.RosterMetaFieldOptionsUpdateRequest(
            group_id='sys05',
            field_code='sys05-contractType',
            labels=[
                '固定期限劳动合同'
            ],
            modify_type='OPTIONS_ADD'
        )
        try:
            await client.roster_meta_field_options_update_with_options_async(roster_meta_field_options_update_request, roster_meta_field_options_update_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\RosterMetaFieldOptionsUpdateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\RosterMetaFieldOptionsUpdateRequest;
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
        $rosterMetaFieldOptionsUpdateHeaders = new RosterMetaFieldOptionsUpdateHeaders([]);
        $rosterMetaFieldOptionsUpdateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $rosterMetaFieldOptionsUpdateRequest = new RosterMetaFieldOptionsUpdateRequest([
            "groupId" => "sys05",
            "fieldCode" => "sys05-contractType",
            "labels" => [
                "固定期限劳动合同"
            ],
            "modifyType" => "OPTIONS_ADD"
        ]);
        try {
            $client->rosterMetaFieldOptionsUpdateWithOptions($rosterMetaFieldOptionsUpdateRequest, $rosterMetaFieldOptionsUpdateHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkhrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrm_1_0.Client{}
  _result, _err = dingtalkhrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  rosterMetaFieldOptionsUpdateHeaders := &dingtalkhrm_1_0.RosterMetaFieldOptionsUpdateHeaders{}
  rosterMetaFieldOptionsUpdateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  rosterMetaFieldOptionsUpdateRequest := &dingtalkhrm_1_0.RosterMetaFieldOptionsUpdateRequest{
    GroupId: tea.String("sys05"),
    FieldCode: tea.String("sys05-contractType"),
    Labels: []*string{tea.String("固定期限劳动合同")},
    ModifyType: tea.String("OPTIONS_ADD"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.RosterMetaFieldOptionsUpdateWithOptions(rosterMetaFieldOptionsUpdateRequest, rosterMetaFieldOptionsUpdateHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let rosterMetaFieldOptionsUpdateHeaders = new $dingtalkhrm_1_0.RosterMetaFieldOptionsUpdateHeaders({ });
    rosterMetaFieldOptionsUpdateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let rosterMetaFieldOptionsUpdateRequest = new $dingtalkhrm_1_0.RosterMetaFieldOptionsUpdateRequest({
      groupId: "sys05",
      fieldCode: "sys05-contractType",
      labels: [
        "固定期限劳动合同"
      ],
      modifyType: "OPTIONS_ADD",
    });
    try {
      await client.rosterMetaFieldOptionsUpdateWithOptions(rosterMetaFieldOptionsUpdateRequest, rosterMetaFieldOptionsUpdateHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaFieldOptionsUpdateHeaders rosterMetaFieldOptionsUpdateHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaFieldOptionsUpdateHeaders();
            rosterMetaFieldOptionsUpdateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaFieldOptionsUpdateRequest rosterMetaFieldOptionsUpdateRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.RosterMetaFieldOptionsUpdateRequest
            {
                GroupId = "sys05",
                FieldCode = "sys05-contractType",
                Labels = new List<string>
                {
                    "固定期限劳动合同"
                },
                ModifyType = "OPTIONS_ADD",
            };
            try
            {
                client.RosterMetaFieldOptionsUpdateWithOptions(rosterMetaFieldOptionsUpdateRequest, rosterMetaFieldOptionsUpdateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否操作成功，返回true表示成功。 |

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
| 400 | fieldIsNotSelect | 字段不是选项型 | 字段不是选项型 |
| 400 | fieldOptionsCannotModify | 字段选项不可修改 | 字段选项不可修改 |
| 400 | labelSizeBeyondLimit | 字段选项超过限制 | 字段选项超过限制 |
| 400 | invokeFrequency | 请求太频繁 | 请求太频繁 |
| 400 | paramInvalid | 参数错误 | labels太多或者modifyType不对 |
| 400 | noFieldModifyPermission | 没有字段修改权限 | isv没有字段修改权限 |
| 500 | systemError | 系统错误 | 系统错误 |
