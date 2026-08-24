---
title: "添加待入职员工"
source_url: "https://open.dingtalk.com/document/development/add-employees-to-be-hired-supports-system-and-custom-fields"
namespace: "development"
slug: "add-employees-to-be-hired-supports-system-and-custom-fields"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工管理 > 添加待入职员工"
doc_id: "4SzJHa7lZL"
updated_at: "2026-06-04 19:10:26"
---

> Source: https://open.dingtalk.com/document/development/add-employees-to-be-hired-supports-system-and-custom-fields
> Path: 应用开发 / 服务端API / 智能人事 > 员工管理 > 添加待入职员工
> Updated: 2026-06-04 19:10:26

# 添加待入职员工

调用本接口，添加待入职员工信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/preentries |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Pro.HrmPreentry.ReadWrite-智能人事待入职员工管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| preEntryTime | Long | 否 | 预计入职时间戳，单位毫秒。 |
| name | String | 是 | 待入职员工的姓名。 |
| mobile | String | 是 | 待入职员工的手机号。 |
| agentId | Long | 否 | 应用的agentId，请参考[基础概念-AgentId](https://open.dingtalk.com/document/development/basic-concepts-beta#884d363067bnq)。 |
| groups | Array | 否 | 待入职员工花名册分组列表，建议不超过5个。 |
| groupId | String | 否 | 分组ID，可调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取group\_id参数值。 |
| sections | Array | 否 | 分组内字段列表，建议不超过5个。 |
| oldIndex | Integer | 否 | 当前字段在分组内的序列号。 |
| empFieldVOList | Array | 否 | 分组内字段信息列表，建议不超过5个。 |
| value | String | 否 | 分组内字段的值。 |
| fieldCode | String | 否 | 分组内字段fieldCode，可调用[获取花名册元数据](0937-intelligent-personnel-roster-metadata-query.md)接口获取的field\_code参数值。 |
| needSendPreEntryMsg | Boolean | 否 | 是否发送完善入职登记表的IM消息给员工本人：   - true：发送 - false：不发送 |

### 请求示例

HTTP

```
POST /v1.0/hrm/preentries HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:5efdfsdfxxxx
Content-Type:application/json

{
  "preEntryTime" : 1615537493964,
  "name" : "张xx",
  "mobile" : "13899998888",
  "agentId" : 13313441,
  "groups" : [ {
    "groupId" : "4319xxxxx",
    "sections" : [ {
      "oldIndex" : 0,
      "empFieldVOList" : [ {
        "value" : "2020-10-10",
        "fieldCode" : "sys01-birthTime"
      } ]
    } ]
  } ],
  "needSendPreEntryMsg" : true
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
        com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryHeaders addHrmPreentryHeaders = new com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryHeaders();
        addHrmPreentryHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList groups0Sections0EmpFieldVOList0 = new com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList()
                .setValue("2020-10-10")
                .setFieldCode("sys01-birthTime");
        com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest.AddHrmPreentryRequestGroupsSections groups0Sections0 = new com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest.AddHrmPreentryRequestGroupsSections()
                .setOldIndex(0)
                .setEmpFieldVOList(java.util.Arrays.asList(
                    groups0Sections0EmpFieldVOList0
                ));
        com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups groups0 = new com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups()
                .setGroupId("4319xxxxx")
                .setSections(java.util.Arrays.asList(
                    groups0Sections0
                ));
        com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest addHrmPreentryRequest = new com.aliyun.dingtalkhrm_1_0.models.AddHrmPreentryRequest()
                .setPreEntryTime(1615537493964L)
                .setName("张xx")
                .setMobile("13899998888")
                .setAgentId(13313441L)
                .setGroups(java.util.Arrays.asList(
                    groups0
                ))
                .setNeedSendPreEntryMsg(true);
        try {
            client.addHrmPreentryWithOptions(addHrmPreentryRequest, addHrmPreentryHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_hrm_preentry_headers = dingtalkhrm__1__0_models.AddHrmPreentryHeaders()
        add_hrm_preentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        groups_0sections_0emp_field_volist_0 = dingtalkhrm__1__0_models.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList(
            value='2020-10-10',
            field_code='sys01-birthTime'
        )
        groups_0sections_0 = dingtalkhrm__1__0_models.AddHrmPreentryRequestGroupsSections(
            old_index=0,
            emp_field_volist=[
                groups_0sections_0emp_field_volist_0
            ]
        )
        groups_0 = dingtalkhrm__1__0_models.AddHrmPreentryRequestGroups(
            group_id='4319xxxxx',
            sections=[
                groups_0sections_0
            ]
        )
        add_hrm_preentry_request = dingtalkhrm__1__0_models.AddHrmPreentryRequest(
            pre_entry_time=1615537493964,
            name='张xx',
            mobile='13899998888',
            agent_id=13313441,
            groups=[
                groups_0
            ],
            need_send_pre_entry_msg=True
        )
        try:
            client.add_hrm_preentry_with_options(add_hrm_preentry_request, add_hrm_preentry_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_hrm_preentry_headers = dingtalkhrm__1__0_models.AddHrmPreentryHeaders()
        add_hrm_preentry_headers.x_acs_dingtalk_access_token = '<your access token>'
        groups_0sections_0emp_field_volist_0 = dingtalkhrm__1__0_models.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList(
            value='2020-10-10',
            field_code='sys01-birthTime'
        )
        groups_0sections_0 = dingtalkhrm__1__0_models.AddHrmPreentryRequestGroupsSections(
            old_index=0,
            emp_field_volist=[
                groups_0sections_0emp_field_volist_0
            ]
        )
        groups_0 = dingtalkhrm__1__0_models.AddHrmPreentryRequestGroups(
            group_id='4319xxxxx',
            sections=[
                groups_0sections_0
            ]
        )
        add_hrm_preentry_request = dingtalkhrm__1__0_models.AddHrmPreentryRequest(
            pre_entry_time=1615537493964,
            name='张xx',
            mobile='13899998888',
            agent_id=13313441,
            groups=[
                groups_0
            ],
            need_send_pre_entry_msg=True
        )
        try:
            await client.add_hrm_preentry_with_options_async(add_hrm_preentry_request, add_hrm_preentry_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\AddHrmPreentryHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\AddHrmPreentryRequest\groups\sections\empFieldVOList;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\AddHrmPreentryRequest\groups\sections;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\AddHrmPreentryRequest\groups;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\AddHrmPreentryRequest;
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
        $addHrmPreentryHeaders = new AddHrmPreentryHeaders([]);
        $addHrmPreentryHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $groups0Sections0EmpFieldVOList0 = new empFieldVOList([
            "value" => "2020-10-10",
            "fieldCode" => "sys01-birthTime"
        ]);
        $groups0Sections0 = new sections([
            "oldIndex" => 0,
            "empFieldVOList" => [
                $groups0Sections0EmpFieldVOList0
            ]
        ]);
        $groups0 = new groups([
            "groupId" => "4319xxxxx",
            "sections" => [
                $groups0Sections0
            ]
        ]);
        $addHrmPreentryRequest = new AddHrmPreentryRequest([
            "preEntryTime" => 1615537493964,
            "name" => "张xx",
            "mobile" => "13899998888",
            "agentId" => 13313441,
            "groups" => [
                $groups0
            ],
            "needSendPreEntryMsg" => true
        ]);
        try {
            $client->addHrmPreentryWithOptions($addHrmPreentryRequest, $addHrmPreentryHeaders, new RuntimeOptions([]));
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

  addHrmPreentryHeaders := &dingtalkhrm_1_0.AddHrmPreentryHeaders{}
  addHrmPreentryHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  groups0Sections0EmpFieldVOList0 := &dingtalkhrm_1_0.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList{
    Value: tea.String("2020-10-10"),
    FieldCode: tea.String("sys01-birthTime"),
  }
  groups0Sections0 := &dingtalkhrm_1_0.AddHrmPreentryRequestGroupsSections{
    OldIndex: tea.Int32(0),
    EmpFieldVOList: []*dingtalkhrm_1_0.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList{groups0Sections0EmpFieldVOList0},
  }
  groups0 := &dingtalkhrm_1_0.AddHrmPreentryRequestGroups{
    GroupId: tea.String("4319xxxxx"),
    Sections: []*dingtalkhrm_1_0.AddHrmPreentryRequestGroupsSections{groups0Sections0},
  }
  addHrmPreentryRequest := &dingtalkhrm_1_0.AddHrmPreentryRequest{
    PreEntryTime: tea.Int64(1615537493964),
    Name: tea.String("张xx"),
    Mobile: tea.String("13899998888"),
    AgentId: tea.Int64(13313441),
    Groups: []*dingtalkhrm_1_0.AddHrmPreentryRequestGroups{groups0},
    NeedSendPreEntryMsg: tea.Bool(true),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddHrmPreentryWithOptions(addHrmPreentryRequest, addHrmPreentryHeaders, &util.RuntimeOptions{})
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
    let addHrmPreentryHeaders = new $dingtalkhrm_1_0.AddHrmPreentryHeaders({ });
    addHrmPreentryHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let groups0Sections0EmpFieldVOList0 = new $dingtalkhrm_1_0.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList({
      value: "2020-10-10",
      fieldCode: "sys01-birthTime",
    });
    let groups0Sections0 = new $dingtalkhrm_1_0.AddHrmPreentryRequestGroupsSections({
      oldIndex: 0,
      empFieldVOList: [
        groups0Sections0EmpFieldVOList0
      ],
    });
    let groups0 = new $dingtalkhrm_1_0.AddHrmPreentryRequestGroups({
      groupId: "4319xxxxx",
      sections: [
        groups0Sections0
      ],
    });
    let addHrmPreentryRequest = new $dingtalkhrm_1_0.AddHrmPreentryRequest({
      preEntryTime: 1615537493964,
      name: "张xx",
      mobile: "13899998888",
      agentId: 13313441,
      groups: [
        groups0
      ],
      needSendPreEntryMsg: true,
    });
    try {
      await client.addHrmPreentryWithOptions(addHrmPreentryRequest, addHrmPreentryHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryHeaders addHrmPreentryHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryHeaders();
            addHrmPreentryHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups.AddHrmPreentryRequestGroupsSections.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList groups0Sections0EmpFieldVOList0 = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups.AddHrmPreentryRequestGroupsSections.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList
            {
                Value = "2020-10-10",
                FieldCode = "sys01-birthTime",
            };
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups.AddHrmPreentryRequestGroupsSections groups0Sections0 = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups.AddHrmPreentryRequestGroupsSections
            {
                OldIndex = 0,
                EmpFieldVOList = new List<AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups.AddHrmPreentryRequestGroupsSections.AddHrmPreentryRequestGroupsSectionsEmpFieldVOList>
                {
                    groups0Sections0EmpFieldVOList0
                },
            };
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups groups0 = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups
            {
                GroupId = "4319xxxxx",
                Sections = new List<AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups.AddHrmPreentryRequestGroupsSections>
                {
                    groups0Sections0
                },
            };
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest addHrmPreentryRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest
            {
                PreEntryTime = 1615537493964,
                Name = "张xx",
                Mobile = "13899998888",
                AgentId = 13313441,
                Groups = new List<AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.AddHrmPreentryRequest.AddHrmPreentryRequestGroups>
                {
                    groups0
                },
                NeedSendPreEntryMsg = true,
            };
            try
            {
                client.AddHrmPreentryWithOptions(addHrmPreentryRequest, addHrmPreentryHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| tmpUserId | String | 待入职员工的的userId。      待入职员工的userId为临时userId，正式入职后该员工userId会发生变化。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "tmpUserId" : "user123"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | noPermission | 无访问权限 | 无访问权限 |
| 400 | invalidParameter | 参数错误 | 参数异常 |
| 500 | systemError | 系统异常 | 系统异常 |
