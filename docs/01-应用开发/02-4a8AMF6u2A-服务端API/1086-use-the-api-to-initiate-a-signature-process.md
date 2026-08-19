---
title: "创建签署流程"
source_url: "https://open.dingtalk.com/document/development/use-the-api-to-initiate-a-signature-process"
namespace: "development"
slug: "use-the-api-to-initiate-a-signature-process"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 创建签署流程"
doc_id: "e1pu2hEE5y"
updated_at: "2025-09-23 19:21:44"
---

> Source: https://open.dingtalk.com/document/development/use-the-api-to-initiate-a-signature-process
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > e签宝 2.0 > 签署流程 > 创建签署流程
> Updated: 2025-09-23 19:21:44

# 创建签署流程

当ISV侧企业有文件需签署时，可调用本接口获取发起签署地址。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/esign/process/startAtOnce |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Esign.Common.ReadWrite-E签宝数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](https://open.dingtalk.com/document/orgapp/obtain-the-access_token-of-an-internal-app)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](https://open.dingtalk.com/document/isvapp/obtain-the-access_token-of-the-authorized-enterprise)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| initiatorUserId | String | 是 | 发起人的userid。 |
| taskName | String | 是 | 任务名称，不支持特殊字符。 |
| signEndTime | Long | 否 | 签署截止时间。 |
| redirectUrl | String | 否 | 重定向跳转地址。 |
| files | Array | 否 | 文件列表，包括合同文件和附件。 |
| fileId | String | 是 | 文件ID。 |
| fileType | Integer | 是 | 文件类型，取值：   - **1**：合同文件 - **2**：附件 |
| fileName | String | 是 | 文件名称。 |
| participants | Array | 否 | 参与方列表。 |
| signRequirements | String | 是 | 签署印章类型，取值：   - **1**：企业章 - **2**：个人章 - **1,2**：个人和企业章 |
| signOrder | Integer | 否 | 签署顺序。 |
| accountType | String | 是 | 用户类型，取值：   - **DING\_USER**：钉钉用户 - **OUTER\_USER**：外部用户 |
| account | String | 否 | 邮箱/手机号账号(accountType为OUTER\_USER时必填） |
| userId | String | 否 | 钉钉用户userid。      **accountType**为**DING\_USER**时必填。 |
| accountName | String | 否 | 账号对应人姓名。      **accountType**为**OUTER\_USER**时必填。 |
| orgName | String | 否 | 企业名称。      **OUTER\_USER**需要盖企业章时必填，如果不传，默认会赋值当前企业名称。 |
| signPosList | Array | 否 | 参与方签署位置信息列表。 |
| fileId | String | 否 | 文件ID。 |
| isCrossPage | Boolean | 否 | 是否为骑缝章。 |
| needSignDate | Boolean | 否 | 是否需要显示签署时间。 |
| page | String | 否 | 签署区页码。 |
| signDate | Object | 否 | 签署区时间。 |
| format | String | 否 | 签署区时间格式， 支持：   - **yyyy/MM/dd** - **yyyy-MM-dd** - **yyyy年MM月dd日** |
| signRequirement | String | 否 | 签署要求： **1**：企业章 **2**：经办人 |
| x | double | 否 | 签署区x坐标。 |
| y | double | 否 | 签署区y坐标。 |
| ccs | Array | 否 | 抄送人列表。 |
| accountType | String | 是 | 用户类型，取值：   - **DING\_USER**：钉钉用户 - **OUTER\_USER**：外部用户 |
| account | String | 否 | 邮箱或手机号账号。      **account**与**userId**两者至少填一项，优先取userId。 |
| userId | String | 否 | 钉钉用户userid。      **account**与**userId**两者至少填一项，优先取userId。 |
| accountName | String | 否 | 账号对应人姓名。 |
| orgName | String | 否 | 企业名称。 |
| sourceInfo | Object | 否 | 来源信息，目前支持传入审批信息和跳转地址。 |
| showText | String | 否 | 展示文案。 |
| pcUrl | String | 否 | PC端签署地址。 |
| mobileUrl | String | 否 | 移动端签署地址。 |
| thirdBizId | String | 否 | 三方业务Id。      该参数值由开发者自定义，可根据自身业务添加唯一值，用于标记本次签署，串联自身前后业务（该参数会在回调通知里原样返回）。 |

### 请求示例

HTTP

```
POST /v2.0/esign/process/startAtOnce HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json

{
  "initiatorUserId" : "manager1122",
  "taskName" : "合同审批",
  "signEndTime" : 1616743221000,
  "redirectUrl" : "www.xxx.com",
  "files" : [ {
    "fileId" : "57234",
    "fileType" : 2,
    "fileName" : "买卖合同.pdf"
  } ],
  "participants" : [ {
    "signRequirements" : "1,2",
    "signOrder" : 1,
    "accountType" : "DING_USER",
    "account" : "188xxx",
    "userId" : "user456",
    "accountName" : "赵xx",
    "orgName" : "e签宝",
    "signPosList" : [ {
      "fileId" : "57234",
      "isCrossPage" : false,
      "needSignDate" : false,
      "page" : "1",
      "signDate" : {
        "format" : "yyyy/MM/dd"
      },
      "signRequirement" : "1",
      "x" : 100.12,
      "y" : 200.23
    } ]
  } ],
  "ccs" : [ {
    "accountType" : "DING_USER",
    "account" : "188xxx",
    "userId" : "user456",
    "accountName" : "赵xx",
    "orgName" : "e签宝"
  } ],
  "sourceInfo" : {
    "showText" : "买卖合同",
    "pcUrl" : "http://pc.xxx.com",
    "mobileUrl" : "http://mobile.xxx.com"
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
        CreateProcessHeaders createProcessHeaders = new CreateProcessHeaders();
        createProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateProcessRequest.CreateProcessRequestSourceInfo sourceInfo = new CreateProcessRequest.CreateProcessRequestSourceInfo()
                .setShowText("买卖合同")
                .setPcUrl("http://pc.xxx.com")
                .setMobileUrl("http://mobile.xxx.com");
        CreateProcessRequest.CreateProcessRequestCcs ccs0 = new CreateProcessRequest.CreateProcessRequestCcs()
                .setAccountType("DING_USER")
                .setAccount("188xxx")
                .setUserId("user456")
                .setAccountName("赵xx")
                .setOrgName("e签宝");
        CreateProcessRequest.CreateProcessRequestParticipantsSignPosListSignDate participants0SignPosList0SignDate = new CreateProcessRequest.CreateProcessRequestParticipantsSignPosListSignDate()
                .setFormat("yyyy/MM/dd");
        CreateProcessRequest.CreateProcessRequestParticipantsSignPosList participants0SignPosList0 = new CreateProcessRequest.CreateProcessRequestParticipantsSignPosList()
                .setFileId("57234")
                .setIsCrossPage(false)
                .setNeedSignDate(false)
                .setPage("1")
                .setSignDate(participants0SignPosList0SignDate)
                .setSignRequirement("1")
                .setX(100.12D)
                .setY(200.23D);
        CreateProcessRequest.CreateProcessRequestParticipants participants0 = new CreateProcessRequest.CreateProcessRequestParticipants()
                .setSignRequirements("1,2")
                .setSignOrder(1)
                .setAccountType("DING_USER")
                .setAccount("188xxx")
                .setUserId("user456")
                .setAccountName("赵xx")
                .setOrgName("e签宝")
                .setSignPosList(java.util.Arrays.asList(
                    participants0SignPosList0
                ));
        CreateProcessRequest.CreateProcessRequestFiles files0 = new CreateProcessRequest.CreateProcessRequestFiles()
                .setFileId("57234")
                .setFileType(2)
                .setFileName("买卖合同.pdf");
        CreateProcessRequest createProcessRequest = new CreateProcessRequest()
                .setInitiatorUserId("manager1122")
                .setTaskName("合同审批")
                .setSignEndTime(1616743221000L)
                .setRedirectUrl("www.xxx.com")
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
            client.createProcessWithOptions(createProcessRequest, createProcessHeaders, new RuntimeOptions());
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
        create_process_headers = dingtalkesign__2__0_models.CreateProcessHeaders()
        create_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        source_info = dingtalkesign__2__0_models.CreateProcessRequestSourceInfo(
            show_text='买卖合同',
            pc_url='http://pc.xxx.com',
            mobile_url='http://mobile.xxx.com'
        )
        ccs_0 = dingtalkesign__2__0_models.CreateProcessRequestCcs(
            account_type='DING_USER',
            account='188xxx',
            user_id='user456',
            account_name='赵xx',
            org_name='e签宝'
        )
        participants_0sign_pos_list_0sign_date = dingtalkesign__2__0_models.CreateProcessRequestParticipantsSignPosListSignDate(
            format='yyyy/MM/dd'
        )
        participants_0sign_pos_list_0 = dingtalkesign__2__0_models.CreateProcessRequestParticipantsSignPosList(
            file_id='57234',
            is_cross_page=False,
            need_sign_date=False,
            page='1',
            sign_date=participants_0sign_pos_list_0sign_date,
            sign_requirement='1',
            x=100.12,
            y=200.23
        )
        participants_0 = dingtalkesign__2__0_models.CreateProcessRequestParticipants(
            sign_requirements='1,2',
            sign_order=1,
            account_type='DING_USER',
            account='188xxx',
            user_id='user456',
            account_name='赵xx',
            org_name='e签宝',
            sign_pos_list=[
                participants_0sign_pos_list_0
            ]
        )
        files_0 = dingtalkesign__2__0_models.CreateProcessRequestFiles(
            file_id='57234',
            file_type=2,
            file_name='买卖合同.pdf'
        )
        create_process_request = dingtalkesign__2__0_models.CreateProcessRequest(
            initiator_user_id='manager1122',
            task_name='合同审批',
            sign_end_time=1616743221000,
            redirect_url='www.xxx.com',
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
            client.create_process_with_options(create_process_request, create_process_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_process_headers = dingtalkesign__2__0_models.CreateProcessHeaders()
        create_process_headers.x_acs_dingtalk_access_token = '<your access token>'
        source_info = dingtalkesign__2__0_models.CreateProcessRequestSourceInfo(
            show_text='买卖合同',
            pc_url='http://pc.xxx.com',
            mobile_url='http://mobile.xxx.com'
        )
        ccs_0 = dingtalkesign__2__0_models.CreateProcessRequestCcs(
            account_type='DING_USER',
            account='188xxx',
            user_id='user456',
            account_name='赵xx',
            org_name='e签宝'
        )
        participants_0sign_pos_list_0sign_date = dingtalkesign__2__0_models.CreateProcessRequestParticipantsSignPosListSignDate(
            format='yyyy/MM/dd'
        )
        participants_0sign_pos_list_0 = dingtalkesign__2__0_models.CreateProcessRequestParticipantsSignPosList(
            file_id='57234',
            is_cross_page=False,
            need_sign_date=False,
            page='1',
            sign_date=participants_0sign_pos_list_0sign_date,
            sign_requirement='1',
            x=100.12,
            y=200.23
        )
        participants_0 = dingtalkesign__2__0_models.CreateProcessRequestParticipants(
            sign_requirements='1,2',
            sign_order=1,
            account_type='DING_USER',
            account='188xxx',
            user_id='user456',
            account_name='赵xx',
            org_name='e签宝',
            sign_pos_list=[
                participants_0sign_pos_list_0
            ]
        )
        files_0 = dingtalkesign__2__0_models.CreateProcessRequestFiles(
            file_id='57234',
            file_type=2,
            file_name='买卖合同.pdf'
        )
        create_process_request = dingtalkesign__2__0_models.CreateProcessRequest(
            initiator_user_id='manager1122',
            task_name='合同审批',
            sign_end_time=1616743221000,
            redirect_url='www.xxx.com',
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
            await client.create_process_with_options_async(create_process_request, create_process_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessHeaders;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest\sourceInfo;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest\ccs;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest\participants\signPosList\signDate;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest\participants\signPosList;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest\participants;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest\files;
use AlibabaCloud\SDK\Dingtalk\Vesign_2_0\Models\CreateProcessRequest;
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
        $createProcessHeaders = new CreateProcessHeaders([]);
        $createProcessHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $sourceInfo = new sourceInfo([
            "showText" => "买卖合同",
            "pcUrl" => "http://pc.xxx.com",
            "mobileUrl" => "http://mobile.xxx.com"
        ]);
        $ccs0 = new ccs([
            "accountType" => "DING_USER",
            "account" => "188xxx",
            "userId" => "user456",
            "accountName" => "赵xx",
            "orgName" => "e签宝"
        ]);
        $participants0SignPosList0SignDate = new signDate([
            "format" => "yyyy/MM/dd"
        ]);
        $participants0SignPosList0 = new signPosList([
            "fileId" => "57234",
            "isCrossPage" => false,
            "needSignDate" => false,
            "page" => "1",
            "signDate" => $participants0SignPosList0SignDate,
            "signRequirement" => "1",
            "x" => 100.12,
            "y" => 200.23
        ]);
        $participants0 = new participants([
            "signRequirements" => "1,2",
            "signOrder" => 1,
            "accountType" => "DING_USER",
            "account" => "188xxx",
            "userId" => "user456",
            "accountName" => "赵xx",
            "orgName" => "e签宝",
            "signPosList" => [
                $participants0SignPosList0
            ]
        ]);
        $files0 = new files([
            "fileId" => "57234",
            "fileType" => 2,
            "fileName" => "买卖合同.pdf"
        ]);
        $createProcessRequest = new CreateProcessRequest([
            "initiatorUserId" => "manager1122",
            "taskName" => "合同审批",
            "signEndTime" => 1616743221000,
            "redirectUrl" => "www.xxx.com",
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
            $client->createProcessWithOptions($createProcessRequest, $createProcessHeaders, new RuntimeOptions([]));
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

  createProcessHeaders := &dingtalkesign_2_0.CreateProcessHeaders{}
  createProcessHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  sourceInfo := &dingtalkesign_2_0.CreateProcessRequestSourceInfo{
    ShowText: tea.String("买卖合同"),
    PcUrl: tea.String("http://pc.xxx.com"),
    MobileUrl: tea.String("http://mobile.xxx.com"),
  }
  ccs0 := &dingtalkesign_2_0.CreateProcessRequestCcs{
    AccountType: tea.String("DING_USER"),
    Account: tea.String("188xxx"),
    UserId: tea.String("user456"),
    AccountName: tea.String("赵xx"),
    OrgName: tea.String("e签宝"),
  }
  participants0SignPosList0SignDate := &dingtalkesign_2_0.CreateProcessRequestParticipantsSignPosListSignDate{
    Format: tea.String("yyyy/MM/dd"),
  }
  participants0SignPosList0 := &dingtalkesign_2_0.CreateProcessRequestParticipantsSignPosList{
    FileId: tea.String("57234"),
    IsCrossPage: tea.Bool(false),
    NeedSignDate: tea.Bool(false),
    Page: tea.String("1"),
    SignDate: participants0SignPosList0SignDate,
    SignRequirement: tea.String("1"),
    X: tea.Float64(100.12),
    Y: tea.Float64(200.23),
  }
  participants0 := &dingtalkesign_2_0.CreateProcessRequestParticipants{
    SignRequirements: tea.String("1,2"),
    SignOrder: tea.Int32(1),
    AccountType: tea.String("DING_USER"),
    Account: tea.String("188xxx"),
    UserId: tea.String("user456"),
    AccountName: tea.String("赵xx"),
    OrgName: tea.String("e签宝"),
    SignPosList: []*dingtalkesign_2_0.CreateProcessRequestParticipantsSignPosList{participants0SignPosList0},
  }
  files0 := &dingtalkesign_2_0.CreateProcessRequestFiles{
    FileId: tea.String("57234"),
    FileType: tea.Int32(2),
    FileName: tea.String("买卖合同.pdf"),
  }
  createProcessRequest := &dingtalkesign_2_0.CreateProcessRequest{
    InitiatorUserId: tea.String("manager1122"),
    TaskName: tea.String("合同审批"),
    SignEndTime: tea.Int64(1616743221000),
    RedirectUrl: tea.String("www.xxx.com"),
    Files: []*dingtalkesign_2_0.CreateProcessRequestFiles{files0},
    Participants: []*dingtalkesign_2_0.CreateProcessRequestParticipants{participants0},
    Ccs: []*dingtalkesign_2_0.CreateProcessRequestCcs{ccs0},
    SourceInfo: sourceInfo,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateProcessWithOptions(createProcessRequest, createProcessHeaders, &util.RuntimeOptions{})
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
    let createProcessHeaders = new $dingtalkesign_2_0.CreateProcessHeaders({ });
    createProcessHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let sourceInfo = new $dingtalkesign_2_0.CreateProcessRequestSourceInfo({
      showText: "买卖合同",
      pcUrl: "http://pc.xxx.com",
      mobileUrl: "http://mobile.xxx.com",
    });
    let ccs0 = new $dingtalkesign_2_0.CreateProcessRequestCcs({
      accountType: "DING_USER",
      account: "188xxx",
      userId: "user456",
      accountName: "赵xx",
      orgName: "e签宝",
    });
    let participants0SignPosList0SignDate = new $dingtalkesign_2_0.CreateProcessRequestParticipantsSignPosListSignDate({
      format: "yyyy/MM/dd",
    });
    let participants0SignPosList0 = new $dingtalkesign_2_0.CreateProcessRequestParticipantsSignPosList({
      fileId: "57234",
      isCrossPage: false,
      needSignDate: false,
      page: "1",
      signDate: participants0SignPosList0SignDate,
      signRequirement: "1",
      x: 100.12,
      y: 200.23,
    });
    let participants0 = new $dingtalkesign_2_0.CreateProcessRequestParticipants({
      signRequirements: "1,2",
      signOrder: 1,
      accountType: "DING_USER",
      account: "188xxx",
      userId: "user456",
      accountName: "赵xx",
      orgName: "e签宝",
      signPosList: [
        participants0SignPosList0
      ],
    });
    let files0 = new $dingtalkesign_2_0.CreateProcessRequestFiles({
      fileId: "57234",
      fileType: 2,
      fileName: "买卖合同.pdf",
    });
    let createProcessRequest = new $dingtalkesign_2_0.CreateProcessRequest({
      initiatorUserId: "manager1122",
      taskName: "合同审批",
      signEndTime: 1616743221000,
      redirectUrl: "www.xxx.com",
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
      await client.createProcessWithOptions(createProcessRequest, createProcessHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessHeaders createProcessHeaders = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessHeaders();
            createProcessHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestSourceInfo sourceInfo = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestSourceInfo
            {
                ShowText = "买卖合同",
                PcUrl = "http://pc.xxx.com",
                MobileUrl = "http://mobile.xxx.com",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestCcs ccs0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestCcs
            {
                AccountType = "DING_USER",
                Account = "188xxx",
                UserId = "user456",
                AccountName = "赵xx",
                OrgName = "e签宝",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants.CreateProcessRequestParticipantsSignPosList.CreateProcessRequestParticipantsSignPosListSignDate participants0SignPosList0SignDate = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants.CreateProcessRequestParticipantsSignPosList.CreateProcessRequestParticipantsSignPosListSignDate
            {
                Format = "yyyy/MM/dd",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants.CreateProcessRequestParticipantsSignPosList participants0SignPosList0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants.CreateProcessRequestParticipantsSignPosList
            {
                FileId = "57234",
                IsCrossPage = false,
                NeedSignDate = false,
                Page = "1",
                SignDate = participants0SignPosList0SignDate,
                SignRequirement = "1",
                X = 100.12,
                Y = 200.23,
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants participants0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants
            {
                SignRequirements = "1,2",
                SignOrder = 1,
                AccountType = "DING_USER",
                Account = "188xxx",
                UserId = "user456",
                AccountName = "赵xx",
                OrgName = "e签宝",
                SignPosList = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants.CreateProcessRequestParticipantsSignPosList>
                {
                    participants0SignPosList0
                },
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestFiles files0 = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestFiles
            {
                FileId = "57234",
                FileType = 2,
                FileName = "买卖合同.pdf",
            };
            AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest createProcessRequest = new AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest
            {
                InitiatorUserId = "manager1122",
                TaskName = "合同审批",
                SignEndTime = 1616743221000,
                RedirectUrl = "www.xxx.com",
                Files = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestFiles>
                {
                    files0
                },
                Participants = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestParticipants>
                {
                    participants0
                },
                Ccs = new List<AlibabaCloud.SDK.Dingtalkesign_2_0.Models.CreateProcessRequest.CreateProcessRequestCcs>
                {
                    ccs0
                },
                SourceInfo = sourceInfo,
            };
            try
            {
                client.CreateProcessWithOptions(createProcessRequest, createProcessHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessHeaders> createProcessHeaders = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessHeaders>();
  createProcessHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestSourceInfo> sourceInfo = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestSourceInfo>(map<string, boost::any>({
    {"showText", boost::any(string("买卖合同"))},
    {"pcUrl", boost::any(string("http://pc.xxx.com"))},
    {"mobileUrl", boost::any(string("http://mobile.xxx.com"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestCcs> ccs0 = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestCcs>(map<string, boost::any>({
    {"accountType", boost::any(string("DING_USER"))},
    {"account", boost::any(string("188xxx"))},
    {"userId", boost::any(string("user456"))},
    {"accountName", boost::any(string("赵xx"))},
    {"orgName", boost::any(string("e签宝"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipantsSignPosListSignDate> participants0SignPosList0SignDate = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipantsSignPosListSignDate>(map<string, boost::any>({
    {"format", boost::any(string("yyyy/MM/dd"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipantsSignPosList> participants0SignPosList0 = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipantsSignPosList>(map<string, boost::any>({
    {"fileId", boost::any(string("57234"))},
    {"isCrossPage", boost::any(false)},
    {"needSignDate", boost::any(false)},
    {"page", boost::any(string("1"))},
    {"signDate", !participants0SignPosList0SignDate ? boost::any() : boost::any(*participants0SignPosList0SignDate)},
    {"signRequirement", boost::any(string("1"))},
    {"x", boost::any(100.12)},
    {"y", boost::any(200.23)}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipants> participants0 = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipants>(map<string, boost::any>({
    {"signRequirements", boost::any(string("1,2"))},
    {"signOrder", boost::any(1)},
    {"accountType", boost::any(string("DING_USER"))},
    {"account", boost::any(string("188xxx"))},
    {"userId", boost::any(string("user456"))},
    {"accountName", boost::any(string("赵xx"))},
    {"orgName", boost::any(string("e签宝"))},
    {"signPosList", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipantsSignPosList>({
      participants0SignPosList0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestFiles> files0 = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestFiles>(map<string, boost::any>({
    {"fileId", boost::any(string("57234"))},
    {"fileType", boost::any(2)},
    {"fileName", boost::any(string("买卖合同.pdf"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequest> createProcessRequest = make_shared<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequest>(map<string, boost::any>({
    {"initiatorUserId", boost::any(string("manager1122"))},
    {"taskName", boost::any(string("合同审批"))},
    {"signEndTime", boost::any(1616743221000)},
    {"redirectUrl", boost::any(string("www.xxx.com"))},
    {"files", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestFiles>({
      files0
    }))},
    {"participants", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestParticipants>({
      participants0
    }))},
    {"ccs", boost::any(vector<Alibabacloud_Dingtalkesign_2_0::CreateProcessRequestCcs>({
      ccs0
    }))},
    {"sourceInfo", !sourceInfo ? boost::any() : boost::any(*sourceInfo)}
  }));
  try {
    client->createProcessWithOptions(createProcessRequest, createProcessHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "taskId" : "PRO_JSHDxxxxx"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | requestParamError | %s | 请求参数错误 |
| 400 | createUserAccountError | 创建用户账号异常 | 创建用户账号异常 |
| 400 | getUserInfoFail | 获取用户信息失败,%s，%s | 获取用户信息失败 |
| 400 | accountNotRealname | 发起人账号在e签宝未实名发起人账号在e签宝未实名 | 发起人账号在e签宝未实名 |
| 400 | createOrgAccountError | 创建企业账号异常 | 创建企业账号异常 |
| 400 | corpNotRealname | 发起人企业在e签宝未实名 | 发起人企业在e签宝未实名 |
| 400 | createFlowError | 创建流程失败: %s | 创建流程失败 |
| 400 | getOpenIsvInfoError | 获取对接服务商信息异常 | 获取对接服务商信息异常 |
| 400 | saveTaskError | 保存任务信息异常 | 保存任务信息异常 |
