---
title: "获取发起签署任务的地址"
source_url: "https://open.dingtalk.com/document/development/obtain-the-address-used-to-initiate-a-signed-task"
namespace: "development"
slug: "obtain-the-address-used-to-initiate-a-signed-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 获取发起签署任务的地址"
doc_id: "2XcoVETuRo"
updated_at: "2025-09-23 19:21:43"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-address-used-to-initiate-a-signed-task
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 获取发起签署任务的地址
> Updated: 2025-09-23 19:21:43

# 获取发起签署任务的地址

调用本接口，获取发起签署任务的地址。本接口还支持传入与此签署任务关联的来源事项地址。在盖企业章后将触发企业设置的用印审批流，可传入此文件在isv侧的相关流程（例如：合同审批流），传入后在e签宝用印审批时，审批人可查看关联的流程，便于审批决策。如果不传入，则不展示。 在用印同意前可点击查看关联的事项。

## 接口调用说明

用于发起签署页面时，可以传入以下参数：

- 任务主题
- 文件
- 签署方
- 抄送人
- 签署截止时间
- 文件到期时间

在以上信息中，文件必须传入，且传入后不支持删除、新增或替换，其于信息可以不传，如果传入后也支持在页面中修改。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/processes/startUrls |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-E签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| serviceGroup | String | 否 | 预留参数，此版本无需此参数。 |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| initiatorUserId | String | 是 | 任务发起方的userid。 |
| taskName | String | 否 | 任务名称，默认为文件名。 |
| redirectUrl | String | 否 | 重定向跳转地址。 |
| files | Array | 是 | 文件列表。 |
| fileId | String | 是 | 文件ID。 |
| fileName | String | 是 | 文件名称。 |
| participants | Array | 否 | 参与方列表。 |
| accountType | String | 是 | 用户类型，取值：   - **DING\_USER**：钉钉用户 - **OUTER\_USER**：外部用户 |
| signRequirements | String | 否 | 签署印章类型，取值：   - **1**：企业章 - **2**：个人章 - **1,2**：个人和企业章 |
| userId | String | 否 | 钉钉用户userid。      当**accountType**为**DING\_USER**时必填。 |
| account | String | 否 | 外部用户账号、手机号或邮箱。      当**accountType**为**OUTER\_USER**时必填。 |
| accountName | String | 否 | 外部用户姓名。      当**accountType**为**OUTER\_USER**时必填。 |
| orgName | String | 否 | 外部企业名称。      **OUTER\_USER**需要盖企业章必填，如果不传，默认会赋值当前企业名称。 |
| ccs | Array | 否 | 抄送人列表。 |
| accountType | String | 是 | 用户类型，取值：   - **DING\_USER**：钉钉用户 - **OUTER\_USER**：外部用户 |
| userId | String | 否 | 钉钉用户userid。      当**accountType**为**DING\_USER**时必填。 |
| account | String | 否 | 外部用户账号、手机号或邮箱。      当**accountType**为**OUTER\_USER**时必填。 |
| accountName | String | 否 | 外部用户姓名。      当**accountType**为**OUTER\_USER**时必填。 |
| orgName | String | 否 | 外部企业名称，发给企业方必填。 |
| sourceInfo | Object | 否 | 来源信息。      支持传入审批信息和跳转地址。 |
| showText | String | 否 | 展示文案。 |
| pcUrl | String | 否 | pc端跳转地址。 |
| mobileUrl | String | 否 | 移动端跳转地址。 |
| autoStart | String | 否 | 是否跳过发起签署页直接发起。 |
| thirdBizId | String | 否 | 三方业务Id。      该参数值由开发者自定义，可根据自身业务添加唯一值，用于标记本次签署，串联自身前后业务（该参数会在回调通知里原样返回）。 |

### 请求示例

HTTP

```
POST /v2.0/esign/processes/startUrls HTTP/1.1
Host:api.dingtalk.com
serviceGroup:-
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "autoStart" : "false",
  "initiatorUserId" : "user456",
  "taskName" : "xxx发起的流程",
  "redirectUrl" : "https: //dingsign.esign.cn/contract",
  "files" : [ {
    "fileId" : "5b500xxx",
    "fileName" : "劳动合同.pdf"
  } ],
  "participants" : [ {
    "accountType" : "DING_USER",
    "signRequirements" : "1",
    "userId" : "user456",
    "account" : "17770164159",
    "accountName" : "赵xx",
    "orgName" : "杭州xx"
  } ],
  "ccs" : [ {
    "accountType" : "OUTER_USER",
    "userId" : "user456",
    "account" : "13567394099",
    "accountName" : "赵xx",
    "orgName" : "杭州xx"
  } ],
  "sourceInfo" : {
    "showText" : "审批信息",
    "pcUrl" : "https: //dingsign.esign.cn/contract",
    "mobileUrl" : "https: //dingsign.esign.cn/contract"
  }
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkesign_2_0.*;
import com.aliyun.dingtalkesign_2_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkesign_2_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkesign_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkesign_2_0.Client client = Sample.createClient();
        ProcessStartHeaders processStartHeaders = new ProcessStartHeaders();
        processStartHeaders.xAcsDingtalkAccessToken = "<your access token>";
        ProcessStartRequest.ProcessStartRequestSourceInfo sourceInfo = new ProcessStartRequest.ProcessStartRequestSourceInfo()
                .setShowText("审批信息")
                .setPcUrl("https: //dingsign.esign.cn/contract")
                .setMobileUrl("https: //dingsign.esign.cn/contract");
        ProcessStartRequest.ProcessStartRequestCcs ccs0 = new ProcessStartRequest.ProcessStartRequestCcs()
                .setAccountType("OUTER_USER")
                .setUserId("user456")
                .setAccount("13567394099")
                .setAccountName("赵xx")
                .setOrgName("杭州xx");
        ProcessStartRequest.ProcessStartRequestParticipants participants0 = new ProcessStartRequest.ProcessStartRequestParticipants()
                .setAccountType("DING_USER")
                .setSignRequirements("1")
                .setUserId("user456")
                .setAccount("17770164159")
                .setAccountName("赵xx")
                .setOrgName("杭州xx");
        ProcessStartRequest.ProcessStartRequestFiles files0 = new ProcessStartRequest.ProcessStartRequestFiles()
                .setFileId("5b500xxx")
                .setFileName("劳动合同.pdf");
        ProcessStartRequest processStartRequest = new ProcessStartRequest()
                .setAutoStart("false")
                .setInitiatorUserId("user456")
                .setTaskName("xxx发起的流程")
                .setRedirectUrl("https: //dingsign.esign.cn/contract")
                .setFiles(java.util.Arrays.asList(
                    files0
                ))
                .setParticipants(java.util.Arrays.asList(
                    participants0
                ))
                .setCcs(java.util.Arrays.asList(
                    ccs0
                ))
                .setSourceInfo(sourceInfo);
        try {
            client.processStartWithOptions(processStartRequest, processStartHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.esign_2_0.client import Client as dingtalkesign_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.esign_2_0 import models as dingtalkesign__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkesign_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkesign_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        process_start_headers = dingtalkesign__2__0_models.ProcessStartHeaders()
        process_start_headers.x_acs_dingtalk_access_token = '<your access token>'
        source_info = dingtalkesign__2__0_models.ProcessStartRequestSourceInfo(
            show_text='审批信息',
            pc_url='https: //dingsign.esign.cn/contract',
            mobile_url='https: //dingsign.esign.cn/contract'
        )
        ccs_0 = dingtalkesign__2__0_models.ProcessStartRequestCcs(
            account_type='OUTER_USER',
            user_id='user456',
            account='13567394099',
            account_name='赵xx',
            org_name='杭州xx'
        )
        participants_0 = dingtalkesign__2__0_models.ProcessStartRequestParticipants(
            account_type='DING_USER',
            sign_requirements='1',
            user_id='user456',
            account='17770164159',
            account_name='赵xx',
            org_name='杭州xx'
        )
        files_0 = dingtalkesign__2__0_models.ProcessStartRequestFiles(
            file_id='5b500xxx',
            file_name='劳动合同.pdf'
        )
        process_start_request = dingtalkesign__2__0_models.ProcessStartRequest(
            auto_start='false',
            initiator_user_id='user456',
            task_name='xxx发起的流程',
            redirect_url='https: //dingsign.esign.cn/contract',
            files=[
                files_0
            ],
            participants=[
                participants_0
            ],
            ccs=[
                ccs_0
            ],
            source_info=source_info
        )
        try:
            client.process_start_with_options(process_start_request, process_start_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        process_start_headers = dingtalkesign__2__0_models.ProcessStartHeaders()
        process_start_headers.x_acs_dingtalk_access_token = '<your access token>'
        source_info = dingtalkesign__2__0_models.ProcessStartRequestSourceInfo(
            show_text='审批信息',
            pc_url='https: //dingsign.esign.cn/contract',
            mobile_url='https: //dingsign.esign.cn/contract'
        )
        ccs_0 = dingtalkesign__2__0_models.ProcessStartRequestCcs(
            account_type='OUTER_USER',
            user_id='user456',
            account='13567394099',
            account_name='赵xx',
            org_name='杭州xx'
        )
        participants_0 = dingtalkesign__2__0_models.ProcessStartRequestParticipants(
            account_type='DING_USER',
            sign_requirements='1',
            user_id='user456',
            account='17770164159',
            account_name='赵xx',
            org_name='杭州xx'
        )
        files_0 = dingtalkesign__2__0_models.ProcessStartRequestFiles(
            file_id='5b500xxx',
            file_name='劳动合同.pdf'
        )
        process_start_request = dingtalkesign__2__0_models.ProcessStartRequest(
            auto_start='false',
            initiator_user_id='user456',
            task_name='xxx发起的流程',
            redirect_url='https: //dingsign.esign.cn/contract',
            files=[
                files_0
            ],
            participants=[
                participants_0
            ],
            ccs=[
                ccs_0
            ],
            source_info=source_info
        )
        try:
            await client.process_start_with_options_async(process_start_request, process_start_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ProcessStartHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ProcessStartRequest\sourceInfo;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ProcessStartRequest\ccs;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ProcessStartRequest\participants;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ProcessStartRequest\files;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\ProcessStartRequest;
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
        $processStartHeaders = new ProcessStartHeaders([]);
        $processStartHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sourceInfo = new sourceInfo([
            "showText" => "审批信息",
            "pcUrl" => "https: //dingsign.esign.cn/contract",
            "mobileUrl" => "https: //dingsign.esign.cn/contract"
        ]);
        $ccs0 = new ccs([
            "accountType" => "OUTER_USER",
            "userId" => "user456",
            "account" => "13567394099",
            "accountName" => "赵xx",
            "orgName" => "杭州xx"
        ]);
        $participants0 = new participants([
            "accountType" => "DING_USER",
            "signRequirements" => "1",
            "userId" => "user456",
            "account" => "17770164159",
            "accountName" => "赵xx",
            "orgName" => "杭州xx"
        ]);
        $files0 = new files([
            "fileId" => "5b500xxx",
            "fileName" => "劳动合同.pdf"
        ]);
        $processStartRequest = new ProcessStartRequest([
            "autoStart" => "false",
            "initiatorUserId" => "user456",
            "taskName" => "xxx发起的流程",
            "redirectUrl" => "https: //dingsign.esign.cn/contract",
            "files" => [
                $files0
            ],
            "participants" => [
                $participants0
            ],
            "ccs" => [
                $ccs0
            ],
            "sourceInfo" => $sourceInfo
        ]);
        try {
            $client->processStartWithOptions($processStartRequest, $processStartHeaders, new RuntimeOptions([]));
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
  dingtalkesign_2_0  "github.com/alibabacloud-go/dingtalk/esign_2_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkesign_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkesign_2_0.Client{}
  _result, _err = dingtalkesign_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  processStartHeaders := &dingtalkesign_2_0.ProcessStartHeaders{}
  processStartHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sourceInfo := &dingtalkesign_2_0.ProcessStartRequestSourceInfo{
    ShowText: tea.String("审批信息"),
    PcUrl: tea.String("https: //dingsign.esign.cn/contract"),
    MobileUrl: tea.String("https: //dingsign.esign.cn/contract"),
  }
  ccs0 := &dingtalkesign_2_0.ProcessStartRequestCcs{
    AccountType: tea.String("OUTER_USER"),
    UserId: tea.String("user456"),
    Account: tea.String("13567394099"),
    AccountName: tea.String("赵xx"),
    OrgName: tea.String("杭州xx"),
  }
  participants0 := &dingtalkesign_2_0.ProcessStartRequestParticipants{
    AccountType: tea.String("DING_USER"),
    SignRequirements: tea.String("1"),
    UserId: tea.String("user456"),
    Account: tea.String("17770164159"),
    AccountName: tea.String("赵xx"),
    OrgName: tea.String("杭州xx"),
  }
  files0 := &dingtalkesign_2_0.ProcessStartRequestFiles{
    FileId: tea.String("5b500xxx"),
    FileName: tea.String("劳动合同.pdf"),
  }
  processStartRequest := &dingtalkesign_2_0.ProcessStartRequest{
    AutoStart: tea.String("false"),
    InitiatorUserId: tea.String("user456"),
    TaskName: tea.String("xxx发起的流程"),
    RedirectUrl: tea.String("https: //dingsign.esign.cn/contract"),
    Files: []*dingtalkesign_2_0.ProcessStartRequestFiles{files0},
    Participants: []*dingtalkesign_2_0.ProcessStartRequestParticipants{participants0},
    Ccs: []*dingtalkesign_2_0.ProcessStartRequestCcs{ccs0},
    SourceInfo: sourceInfo,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ProcessStartWithOptions(processStartRequest, processStartHeaders, &util.RuntimeOptions{})
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
import dingtalkesign_2_0, * as $dingtalkesign_2_0 from '@alicloud/dingtalk/esign_2_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkesign_2_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkesign_2_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let processStartHeaders = new $dingtalkesign_2_0.ProcessStartHeaders({ });
    processStartHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sourceInfo = new $dingtalkesign_2_0.ProcessStartRequestSourceInfo({
      showText: "审批信息",
      pcUrl: "https: //dingsign.esign.cn/contract",
      mobileUrl: "https: //dingsign.esign.cn/contract",
    });
    let ccs0 = new $dingtalkesign_2_0.ProcessStartRequestCcs({
      accountType: "OUTER_USER",
      userId: "user456",
      account: "13567394099",
      accountName: "赵xx",
      orgName: "杭州xx",
    });
    let participants0 = new $dingtalkesign_2_0.ProcessStartRequestParticipants({
      accountType: "DING_USER",
      signRequirements: "1",
      userId: "user456",
      account: "17770164159",
      accountName: "赵xx",
      orgName: "杭州xx",
    });
    let files0 = new $dingtalkesign_2_0.ProcessStartRequestFiles({
      fileId: "5b500xxx",
      fileName: "劳动合同.pdf",
    });
    let processStartRequest = new $dingtalkesign_2_0.ProcessStartRequest({
      autoStart: "false",
      initiatorUserId: "user456",
      taskName: "xxx发起的流程",
      redirectUrl: "https: //dingsign.esign.cn/contract",
      files: [
        files0
      ],
      participants: [
        participants0
      ],
      ccs: [
        ccs0
      ],
      sourceInfo: sourceInfo,
    });
    try {
      await client.processStartWithOptions(processStartRequest, processStartHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkesign_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkesign_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkesign_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartHeaders processStartHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartHeaders();
            processStartHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestSourceInfo sourceInfo = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestSourceInfo
            {
                ShowText = "审批信息",
                PcUrl = "https: //dingsign.esign.cn/contract",
                MobileUrl = "https: //dingsign.esign.cn/contract",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestCcs ccs0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestCcs
            {
                AccountType = "OUTER_USER",
                UserId = "user456",
                Account = "13567394099",
                AccountName = "赵xx",
                OrgName = "杭州xx",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestParticipants participants0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestParticipants
            {
                AccountType = "DING_USER",
                SignRequirements = "1",
                UserId = "user456",
                Account = "17770164159",
                AccountName = "赵xx",
                OrgName = "杭州xx",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestFiles files0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestFiles
            {
                FileId = "5b500xxx",
                FileName = "劳动合同.pdf",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest processStartRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest
            {
                AutoStart = "false",
                InitiatorUserId = "user456",
                TaskName = "xxx发起的流程",
                RedirectUrl = "https: //dingsign.esign.cn/contract",
                Files = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestFiles>
                {
                    files0
                },
                Participants = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestParticipants>
                {
                    participants0
                },
                Ccs = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.ProcessStartRequest.ProcessStartRequestCcs>
                {
                    ccs0
                },
                SourceInfo = sourceInfo,
            };
            try
            {
                client.ProcessStartWithOptions(processStartRequest, processStartHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkesign__2__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkesign_2_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkesign_2_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::Client> client = make_shared<Alibabacloud_Dingtalkesign_2_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ProcessStartHeaders> processStartHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::ProcessStartHeaders>();
  processStartHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestSourceInfo> sourceInfo = make_shared<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestSourceInfo>(map<string, boost::any>({
    {"showText", boost::any(string("审批信息"))},
    {"pcUrl", boost::any(string("https: //dingsign.esign.cn/contract"))},
    {"mobileUrl", boost::any(string("https: //dingsign.esign.cn/contract"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestCcs> ccs0 = make_shared<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestCcs>(map<string, boost::any>({
    {"accountType", boost::any(string("OUTER_USER"))},
    {"userId", boost::any(string("user456"))},
    {"account", boost::any(string("13567394099"))},
    {"accountName", boost::any(string("赵xx"))},
    {"orgName", boost::any(string("杭州xx"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestParticipants> participants0 = make_shared<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestParticipants>(map<string, boost::any>({
    {"accountType", boost::any(string("DING_USER"))},
    {"signRequirements", boost::any(string("1"))},
    {"userId", boost::any(string("user456"))},
    {"account", boost::any(string("17770164159"))},
    {"accountName", boost::any(string("赵xx"))},
    {"orgName", boost::any(string("杭州xx"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestFiles> files0 = make_shared<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestFiles>(map<string, boost::any>({
    {"fileId", boost::any(string("5b500xxx"))},
    {"fileName", boost::any(string("劳动合同.pdf"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequest> processStartRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequest>(map<string, boost::any>({
    {"autoStart", boost::any(string("false"))},
    {"initiatorUserId", boost::any(string("user456"))},
    {"taskName", boost::any(string("xxx发起的流程"))},
    {"redirectUrl", boost::any(string("https: //dingsign.esign.cn/contract"))},
    {"files", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestFiles>({
      files0
    }))},
    {"participants", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestParticipants>({
      participants0
    }))},
    {"ccs", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::ProcessStartRequestCcs>({
      ccs0
    }))},
    {"sourceInfo", !sourceInfo ? boost::any() : boost::any(*sourceInfo)}
  }));
  try {
    client->processStartWithOptions(processStartRequest, processStartHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| taskId | String | 任务ID。 |
| pcUrl | String | PC端发起签署任务地址。 |
| mobileUrl | String | 移动端发起签署任务地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "taskId" : "65A86D2Bxxx",
  "pcUrl" : "https://developers.dingtalk.com/",
  "mobileUrl" : "https://developers.dingtalk.com/"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | serviceError | 服务错误 | 服务错误 |
| 400 | saveOrgTaskError | 保存任务信息异常,盖企业印章,请传入企业名称 | 保存任务信息异常盖企业印章,请传入企业名称 |
| 400 | saveTaskError | 保存任务信息异常 | 保存任务信息异常 |
