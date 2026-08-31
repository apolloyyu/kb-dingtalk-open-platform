---
title: "获取发起签署任务地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-address-of-the-initiating-signing-task"
namespace: "development"
slug: "obtain-the-address-of-the-initiating-signing-task"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "历史文档（不推荐） > e签宝 1.0 > 签署流程 > 获取发起签署任务地址"
doc_id: "Q4UdwwCXPq"
updated_at: "2026-08-25 09:37:35"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-address-of-the-initiating-signing-task
> Path: 应用开发 / 服务端 API / 历史文档（不推荐） > e签宝 1.0 > 签署流程 > 获取发起签署任务地址
> Updated: 2026-08-25 09:37:35

# 获取发起签署任务地址

当ISV侧企业有文件需签署时，调用本接口，获取发起签署的地址。

> **[!IMPORTANT]**
>
> - 本接口已完成升级，后续将维持现有功能且不再新增能力。
> - 未接入的开发者建议使用新版[获取发起签署任务的地址](1089-obtain-the-address-used-to-initiate-a-signed-task.md)接口，已接入用户不受影响。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/esign/process/start |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | 不支持新增 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| files | Array | 否 | 文件列表。 |
| fileId | String | 否 | 文件Id。 |
| fileName | String | 否 | 文件名称。 |
| initiatorUserId | String | 否 | 发起方userId。 |
| participants | Array | 否 | 参与方列表。 |
| accountType | String | 否 | 用户类型。   - **DING\_USER**：钉钉用户 - **OUTER\_USER**：外部用户 |
| signRequirements | String | 否 | 签署印章类型。   - **1**：企业章 - **2**：个人章 - **1,2**：个人章和企业章 |
| userId | String | 否 | 用户userId。      当**accountType**为**DING\_USER**时，该参数必填。 |
| account | String | 否 | 账户。      当**accountType**为**OUTER\_USER**时，该参数必填。 |
| accountName | String | 否 | 账户名称（默认当前企业）。      当**accountType**为**OUTER\_USER**时该参数必填，如果不传，默认会赋值当前企业名称。 |
| orgName | String | 否 | 企业名称（默认当前企业）。      当**accountType**为**OUTER\_USER**时该参数必填，如果不传，默认会赋值当前企业名称。 |
| redirectUrl | String | 否 | 回跳地址。 |
| sourceInfo | Object | 否 | 来源信息。      目前支持传入审批信息和跳转地址。 |
| mobileUrl | String | 否 | 移动端跳转地址。 |
| pcUrl | String | 否 | pc端跳转地址。 |
| showText | String | 否 | 展示文案。 |
| taskName | String | 否 | 任务名称（默认文件名）。 |
| ccs | Array | 否 | 抄送人列表。 |
| accountType | String | 否 | 用户类型。   - **DING\_USER**：钉钉用户 - **OUTER\_USER**：外部用户 |
| userId | String | 否 | 用户的userId。      当**accountType**为**DING\_USER**时，该参数必填。 |
| account | String | 否 | 账户。      当**accountType**为**OUTER\_USER**时，该参数必填。 |
| accountName | String | 否 | 账户名称。      当**accountType**为**OUTER\_USER**时，该参数必填。 |
| orgName | String | 否 | 企业名称。      发给企业方必填。 |

### 请求示例

HTTP

```
POST /v1.0/esign/process/start HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxxx
Content-Type:application/json

{
  "files" : [ {
    "fileId" : "b9ed4538adxxxx",
    "fileName" : "劳动合同.pdf"
  } ],
  "initiatorUserId" : "user01",
  "participants" : [ {
    "accountType" : "DING_USER",
    "signRequirements" : "1",
    "userId" : "user01",
    "account" : "3edsaccount",
    "accountName" : "dd",
    "orgName" : "abc"
  } ],
  "redirectUrl" : "http://xxxx.com",
  "sourceInfo" : {
    "mobileUrl" : "http://ding.talk.com",
    "pcUrl" : "http://ding.talk.com",
    "showText" : "文案"
  },
  "taskName" : "劳动合同",
  "ccs" : [ {
    "accountType" : "DING_USER",
    "userId" : "user01",
    "account" : "3edsaccount",
    "accountName" : "dd",
    "orgName" : "杭州xxxx公司"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_1_0.*;
import com.aliyun.dingtalkesign_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_1_0.Client client = Sample.createClient();
        GetProcessStartUrlHeaders getProcessStartUrlHeaders = new GetProcessStartUrlHeaders();
        getProcessStartUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetProcessStartUrlRequest.GetProcessStartUrlRequestCcs ccs0 = new GetProcessStartUrlRequest.GetProcessStartUrlRequestCcs()
                .setAccountType("DING_USER")
                .setUserId("user01")
                .setAccount("3edsaccount")
                .setAccountName("dd")
                .setOrgName("杭州xxxx公司");
        GetProcessStartUrlRequest.GetProcessStartUrlRequestSourceInfo sourceInfo = new GetProcessStartUrlRequest.GetProcessStartUrlRequestSourceInfo()
                .setMobileUrl("http://ding.talk.com")
                .setPcUrl("http://ding.talk.com")
                .setShowText("文案");
        GetProcessStartUrlRequest.GetProcessStartUrlRequestParticipants participants0 = new GetProcessStartUrlRequest.GetProcessStartUrlRequestParticipants()
                .setAccountType("DING_USER")
                .setSignRequirements("1")
                .setUserId("user01")
                .setAccount("3edsaccount")
                .setAccountName("dd")
                .setOrgName("abc");
        GetProcessStartUrlRequest.GetProcessStartUrlRequestFiles files0 = new GetProcessStartUrlRequest.GetProcessStartUrlRequestFiles()
                .setFileId("b9ed4538adxxxx")
                .setFileName("劳动合同.pdf");
        GetProcessStartUrlRequest getProcessStartUrlRequest = new GetProcessStartUrlRequest()
                .setFiles(java.util.Arrays.asList(
                    files0
                ))
                .setInitiatorUserId("user01")
                .setParticipants(java.util.Arrays.asList(
                    participants0
                ))
                .setRedirectUrl("http://xxxx.com")
                .setSourceInfo(sourceInfo)
                .setTaskName("劳动合同")
                .setCcs(java.util.Arrays.asList(
                    ccs0
                ));
        try {
            client.getProcessStartUrlWithOptions(getProcessStartUrlRequest, getProcessStartUrlHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_1_0.client import Client as dingtalkesign_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_1_0 import models as dingtalkesign__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_process_start_url_headers = dingtalkesign__1__0_models.GetProcessStartUrlHeaders()
        get_process_start_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        ccs_0 = dingtalkesign__1__0_models.GetProcessStartUrlRequestCcs(
            account_type='DING_USER',
            user_id='user01',
            account='3edsaccount',
            account_name='dd',
            org_name='杭州xxxx公司'
        )
        source_info = dingtalkesign__1__0_models.GetProcessStartUrlRequestSourceInfo(
            mobile_url='http://ding.talk.com',
            pc_url='http://ding.talk.com',
            show_text='文案'
        )
        participants_0 = dingtalkesign__1__0_models.GetProcessStartUrlRequestParticipants(
            account_type='DING_USER',
            sign_requirements='1',
            user_id='user01',
            account='3edsaccount',
            account_name='dd',
            org_name='abc'
        )
        files_0 = dingtalkesign__1__0_models.GetProcessStartUrlRequestFiles(
            file_id='b9ed4538adxxxx',
            file_name='劳动合同.pdf'
        )
        get_process_start_url_request = dingtalkesign__1__0_models.GetProcessStartUrlRequest(
            files=[
                files_0
            ],
            initiator_user_id='user01',
            participants=[
                participants_0
            ],
            redirect_url='http://xxxx.com',
            source_info=source_info,
            task_name='劳动合同',
            ccs=[
                ccs_0
            ]
        )
        try:
            client.get_process_start_url_with_options(get_process_start_url_request, get_process_start_url_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_process_start_url_headers = dingtalkesign__1__0_models.GetProcessStartUrlHeaders()
        get_process_start_url_headers.x_acs_dingtalk_access_token = '<your access token>'
        ccs_0 = dingtalkesign__1__0_models.GetProcessStartUrlRequestCcs(
            account_type='DING_USER',
            user_id='user01',
            account='3edsaccount',
            account_name='dd',
            org_name='杭州xxxx公司'
        )
        source_info = dingtalkesign__1__0_models.GetProcessStartUrlRequestSourceInfo(
            mobile_url='http://ding.talk.com',
            pc_url='http://ding.talk.com',
            show_text='文案'
        )
        participants_0 = dingtalkesign__1__0_models.GetProcessStartUrlRequestParticipants(
            account_type='DING_USER',
            sign_requirements='1',
            user_id='user01',
            account='3edsaccount',
            account_name='dd',
            org_name='abc'
        )
        files_0 = dingtalkesign__1__0_models.GetProcessStartUrlRequestFiles(
            file_id='b9ed4538adxxxx',
            file_name='劳动合同.pdf'
        )
        get_process_start_url_request = dingtalkesign__1__0_models.GetProcessStartUrlRequest(
            files=[
                files_0
            ],
            initiator_user_id='user01',
            participants=[
                participants_0
            ],
            redirect_url='http://xxxx.com',
            source_info=source_info,
            task_name='劳动合同',
            ccs=[
                ccs_0
            ]
        )
        try:
            await client.get_process_start_url_with_options_async(get_process_start_url_request, get_process_start_url_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetProcessStartUrlHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetProcessStartUrlRequest\ccs;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetProcessStartUrlRequest\sourceInfo;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetProcessStartUrlRequest\participants;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetProcessStartUrlRequest\files;
use AlibabaCloud\SDK\Dingtalk\Vesign_1_0\Models\GetProcessStartUrlRequest;
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
        $getProcessStartUrlHeaders = new GetProcessStartUrlHeaders([]);
        $getProcessStartUrlHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $ccs0 = new ccs([
            "accountType" => "DING_USER",
            "userId" => "user01",
            "account" => "3edsaccount",
            "accountName" => "dd",
            "orgName" => "杭州xxxx公司"
        ]);
        $sourceInfo = new sourceInfo([
            "mobileUrl" => "http://ding.talk.com",
            "pcUrl" => "http://ding.talk.com",
            "showText" => "文案"
        ]);
        $participants0 = new participants([
            "accountType" => "DING_USER",
            "signRequirements" => "1",
            "userId" => "user01",
            "account" => "3edsaccount",
            "accountName" => "dd",
            "orgName" => "abc"
        ]);
        $files0 = new files([
            "fileId" => "b9ed4538adxxxx",
            "fileName" => "劳动合同.pdf"
        ]);
        $getProcessStartUrlRequest = new GetProcessStartUrlRequest([
            "files" => [
                $files0
            ],
            "initiatorUserId" => "user01",
            "participants" => [
                $participants0
            ],
            "redirectUrl" => "http://xxxx.com",
            "sourceInfo" => $sourceInfo,
            "taskName" => "劳动合同",
            "ccs" => [
                $ccs0
            ]
        ]);
        try {
            $client->getProcessStartUrlWithOptions($getProcessStartUrlRequest, $getProcessStartUrlHeaders, new RuntimeOptions([]));
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
  dingtalkesign_1_0  ""github.com/alibabacloud-go/dingtalk/esign_1_0/client"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_1_0.Client{}
  _result, _err = dingtalkesign_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getProcessStartUrlHeaders := &dingtalkesign_1_0.GetProcessStartUrlHeaders{}
  getProcessStartUrlHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  ccs0 := &dingtalkesign_1_0.GetProcessStartUrlRequestCcs{
    AccountType: tea.String("DING_USER"),
    UserId: tea.String("user01"),
    Account: tea.String("3edsaccount"),
    AccountName: tea.String("dd"),
    OrgName: tea.String("杭州xxxx公司"),
  }
  sourceInfo := &dingtalkesign_1_0.GetProcessStartUrlRequestSourceInfo{
    MobileUrl: tea.String("http://ding.talk.com"),
    PcUrl: tea.String("http://ding.talk.com"),
    ShowText: tea.String("文案"),
  }
  participants0 := &dingtalkesign_1_0.GetProcessStartUrlRequestParticipants{
    AccountType: tea.String("DING_USER"),
    SignRequirements: tea.String("1"),
    UserId: tea.String("user01"),
    Account: tea.String("3edsaccount"),
    AccountName: tea.String("dd"),
    OrgName: tea.String("abc"),
  }
  files0 := &dingtalkesign_1_0.GetProcessStartUrlRequestFiles{
    FileId: tea.String("b9ed4538adxxxx"),
    FileName: tea.String("劳动合同.pdf"),
  }
  getProcessStartUrlRequest := &dingtalkesign_1_0.GetProcessStartUrlRequest{
    Files: []*dingtalkesign_1_0.GetProcessStartUrlRequestFiles{files0},
    InitiatorUserId: tea.String("user01"),
    Participants: []*dingtalkesign_1_0.GetProcessStartUrlRequestParticipants{participants0},
    RedirectUrl: tea.String("http://xxxx.com"),
    SourceInfo: sourceInfo,
    TaskName: tea.String("劳动合同"),
    Ccs: []*dingtalkesign_1_0.GetProcessStartUrlRequestCcs{ccs0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetProcessStartUrlWithOptions(getProcessStartUrlRequest, getProcessStartUrlHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_1_0, * as $dingtalkesign_1_0 from '"@alicloud/dingtalk/esign_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getProcessStartUrlHeaders = new $dingtalkesign_1_0.GetProcessStartUrlHeaders({ });
    getProcessStartUrlHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let ccs0 = new $dingtalkesign_1_0.GetProcessStartUrlRequestCcs({
      accountType: "DING_USER",
      userId: "user01",
      account: "3edsaccount",
      accountName: "dd",
      orgName: "杭州xxxx公司",
    });
    let sourceInfo = new $dingtalkesign_1_0.GetProcessStartUrlRequestSourceInfo({
      mobileUrl: "http://ding.talk.com",
      pcUrl: "http://ding.talk.com",
      showText: "文案",
    });
    let participants0 = new $dingtalkesign_1_0.GetProcessStartUrlRequestParticipants({
      accountType: "DING_USER",
      signRequirements: "1",
      userId: "user01",
      account: "3edsaccount",
      accountName: "dd",
      orgName: "abc",
    });
    let files0 = new $dingtalkesign_1_0.GetProcessStartUrlRequestFiles({
      fileId: "b9ed4538adxxxx",
      fileName: "劳动合同.pdf",
    });
    let getProcessStartUrlRequest = new $dingtalkesign_1_0.GetProcessStartUrlRequest({
      files: [
        files0
      ],
      initiatorUserId: "user01",
      participants: [
        participants0
      ],
      redirectUrl: "http://xxxx.com",
      sourceInfo: sourceInfo,
      taskName: "劳动合同",
      ccs: [
        ccs0
      ],
    });
    try {
      await client.getProcessStartUrlWithOptions(getProcessStartUrlRequest, getProcessStartUrlHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlHeaders getProcessStartUrlHeaders = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlHeaders();
            getProcessStartUrlHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestCcs ccs0 = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestCcs
            {
                AccountType = "DING_USER",
                UserId = "user01",
                Account = "3edsaccount",
                AccountName = "dd",
                OrgName = "杭州xxxx公司",
            };
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestSourceInfo sourceInfo = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestSourceInfo
            {
                MobileUrl = "http://ding.talk.com",
                PcUrl = "http://ding.talk.com",
                ShowText = "文案",
            };
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestParticipants participants0 = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestParticipants
            {
                AccountType = "DING_USER",
                SignRequirements = "1",
                UserId = "user01",
                Account = "3edsaccount",
                AccountName = "dd",
                OrgName = "abc",
            };
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestFiles files0 = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestFiles
            {
                FileId = "b9ed4538adxxxx",
                FileName = "劳动合同.pdf",
            };
            AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest getProcessStartUrlRequest = new AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest
            {
                Files = new List<AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestFiles>
                {
                    files0
                },
                InitiatorUserId = "user01",
                Participants = new List<AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestParticipants>
                {
                    participants0
                },
                RedirectUrl = "http://xxxx.com",
                SourceInfo = sourceInfo,
                TaskName = "劳动合同",
                Ccs = new List<AlibabaCloud.SDK.Dingtalkesign_1_0.Models.GetProcessStartUrlRequest.GetProcessStartUrlRequestCcs>
                {
                    ccs0
                },
            };
            try
            {
                client.GetProcessStartUrlWithOptions(getProcessStartUrlRequest, getProcessStartUrlHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlHeaders> getProcessStartUrlHeaders = make_shared<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlHeaders>();
  getProcessStartUrlHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestCcs> ccs0 = make_shared<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestCcs>(map<string, boost::any>({
    {"accountType", boost::any(string("DING_USER"))},
    {"userId", boost::any(string("user01"))},
    {"account", boost::any(string("3edsaccount"))},
    {"accountName", boost::any(string("dd"))},
    {"orgName", boost::any(string("杭州xxxx公司"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestSourceInfo> sourceInfo = make_shared<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestSourceInfo>(map<string, boost::any>({
    {"mobileUrl", boost::any(string("http://ding.talk.com"))},
    {"pcUrl", boost::any(string("http://ding.talk.com"))},
    {"showText", boost::any(string("文案"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestParticipants> participants0 = make_shared<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestParticipants>(map<string, boost::any>({
    {"accountType", boost::any(string("DING_USER"))},
    {"signRequirements", boost::any(string("1"))},
    {"userId", boost::any(string("user01"))},
    {"account", boost::any(string("3edsaccount"))},
    {"accountName", boost::any(string("dd"))},
    {"orgName", boost::any(string("abc"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestFiles> files0 = make_shared<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestFiles>(map<string, boost::any>({
    {"fileId", boost::any(string("b9ed4538adxxxx"))},
    {"fileName", boost::any(string("劳动合同.pdf"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequest> getProcessStartUrlRequest = make_shared<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequest>(map<string, boost::any>({
    {"files", boost::any(vector<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestFiles>({
      files0
    }))},
    {"initiatorUserId", boost::any(string("user01"))},
    {"participants", boost::any(vector<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestParticipants>({
      participants0
    }))},
    {"redirectUrl", boost::any(string("http://xxxx.com"))},
    {"sourceInfo", !sourceInfo ? boost::any() : boost::any(*sourceInfo)},
    {"taskName", boost::any(string("劳动合同"))},
    {"ccs", boost::any(vector<Alibabacloud_Dingtalkesign_1_0::GetProcessStartUrlRequestCcs>({
      ccs0
    }))}
  }));
  try {
    client->getProcessStartUrlWithOptions(getProcessStartUrlRequest, getProcessStartUrlHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| message | String | 返回码描述。 |
| code | Integer | 返回码。 |
| data | Object | 返回结果。 |
| taskId | String | 任务Id。 |
| pcUrl | String | PC端发起签署任务地址。 |
| mobileUrl | String | 移动端发起签署任务地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "message" : "ok",
  "code" : 0,
  "data" : {
    "taskId" : "PRO-AB31C10xxxx",
    "pcUrl" : "http://xxxx.com",
    "mobileUrl" : "http://xxxx.com"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidRequest.invalidAguemnts | invalid arguments | 参数错误 |
