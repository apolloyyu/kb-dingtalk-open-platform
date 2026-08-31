---
title: "获取组织内某人提交的任务"
source_url: "https://open.dingtalk.com/document/development/obtains-the-tasks-submitted-by-someone-in-an-organization"
namespace: "development"
slug: "obtains-the-tasks-submitted-by-someone-in-an-organization"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "宜搭 > 任务 > 获取组织内某人提交的任务"
doc_id: "1zga3cRLuS"
updated_at: "2026-06-03 10:11:53"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-tasks-submitted-by-someone-in-an-organization
> Path: 应用开发 / 服务端 API / 宜搭 > 任务 > 获取组织内某人提交的任务
> Updated: 2026-06-03 10:11:53

# 获取组织内某人提交的任务

查询已提交任务列表

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/yida/tasks/myCorpSubmission/{userId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Yida.Process.Read-宜搭流程数据读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 用户userid。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织的corpId。 |
| pageSize | Integer | 否 | 分页大小。 |
| language | String | 否 | 语言，取值：   - zh\_CN：中文（默认值） - en\_US：英文 |
| pageNumber | Integer | 否 | 分页页码。 |
| keyword | String | 否 | 表单中组件数据模糊搜索。 |
| appTypes | String | 否 | 应用标识。      仅支持传入一个应用标识。 |
| processCodes | String | 否 | 流程code。      仅支持传入一个流程code。 |
| createFromTimeGMT | Long | 否 | 创建时间起始值。 |
| createToTimeGMT | Long | 否 | 创建时间终止值。 |
| token | String | 是 | 验权token。  校验方式如下：md5(corpId + userId + code)。md5取32位大写值。      每个企业有自己的唯一code。 |
| env | String | 否 | 环境标识，不填写则默认国内版。 |

### 请求示例

HTTP

```
GET /v1.0/yida/tasks/myCorpSubmission/manager123?corpId=ding123&pageSize=10&language=zh_CN&pageNumber=1&keyword={}&appTypes=["APP_xxx","APP_xxx"]&processCodes=["xx","xxx"]&token=JHASD123HAXXX HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BExxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkyida_1_0.*;
import com.aliyun.dingtalkyida_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkyida_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkyida_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkyida_1_0.Client client = Sample.createClient();
        GetMeCorpSubmissionHeaders getMeCorpSubmissionHeaders = new GetMeCorpSubmissionHeaders();
        getMeCorpSubmissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetMeCorpSubmissionRequest getMeCorpSubmissionRequest = new GetMeCorpSubmissionRequest()
                .setCorpId("ding123")
                .setPageSize(10)
                .setLanguage("zh_CN")
                .setPageNumber(1)
                .setKeyword("{}")
                .setAppTypes("[\"APP_xxx\",\"APP_xxx\"]")
                .setProcessCodes("[\"xx\",\"xxx\"]")
                .setToken("JHASD123HAXXX");
        try {
            client.getMeCorpSubmissionWithOptions("manager123", getMeCorpSubmissionRequest, getMeCorpSubmissionHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.yida_1_0.client import Client as dingtalkyida_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.yida_1_0 import models as dingtalkyida__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkyida_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkyida_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_me_corp_submission_headers = dingtalkyida__1__0_models.GetMeCorpSubmissionHeaders()
        get_me_corp_submission_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_me_corp_submission_request = dingtalkyida__1__0_models.GetMeCorpSubmissionRequest(
            corp_id='ding123',
            page_size=10,
            language='zh_CN',
            page_number=1,
            keyword='{}',
            app_types='["APP_xxx","APP_xxx"]',
            process_codes='["xx","xxx"]',
            token='JHASD123HAXXX'
        )
        try:
            client.get_me_corp_submission_with_options('manager123', get_me_corp_submission_request, get_me_corp_submission_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_me_corp_submission_headers = dingtalkyida__1__0_models.GetMeCorpSubmissionHeaders()
        get_me_corp_submission_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_me_corp_submission_request = dingtalkyida__1__0_models.GetMeCorpSubmissionRequest(
            corp_id='ding123',
            page_size=10,
            language='zh_CN',
            page_number=1,
            keyword='{}',
            app_types='["APP_xxx","APP_xxx"]',
            process_codes='["xx","xxx"]',
            token='JHASD123HAXXX'
        )
        try:
            await client.get_me_corp_submission_with_options_async('manager123', get_me_corp_submission_request, get_me_corp_submission_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\GetMeCorpSubmissionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vyida_1_0\Models\GetMeCorpSubmissionRequest;
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
        $getMeCorpSubmissionHeaders = new GetMeCorpSubmissionHeaders([]);
        $getMeCorpSubmissionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getMeCorpSubmissionRequest = new GetMeCorpSubmissionRequest([
            "corpId" => "ding123",
            "pageSize" => 10,
            "language" => "zh_CN",
            "pageNumber" => 1,
            "keyword" => "{}",
            "appTypes" => "[\"APP_xxx\",\"APP_xxx\"]",
            "processCodes" => "[\"xx\",\"xxx\"]",
            "token" => "JHASD123HAXXX"
        ]);
        try {
            $client->getMeCorpSubmissionWithOptions("manager123", $getMeCorpSubmissionRequest, $getMeCorpSubmissionHeaders, new RuntimeOptions([]));
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
  dingtalkyida_1_0  "github.com/alibabacloud-go/dingtalk/yida_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkyida_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkyida_1_0.Client{}
  _result, _err = dingtalkyida_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  getMeCorpSubmissionHeaders := &dingtalkyida_1_0.GetMeCorpSubmissionHeaders{}
  getMeCorpSubmissionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getMeCorpSubmissionRequest := &dingtalkyida_1_0.GetMeCorpSubmissionRequest{
    CorpId: tea.String("ding123"),
    PageSize: tea.Int32(10),
    Language: tea.String("zh_CN"),
    PageNumber: tea.Int32(1),
    Keyword: tea.String("{}"),
    AppTypes: tea.String("[\"APP_xxx\",\"APP_xxx\"]"),
    ProcessCodes: tea.String("[\"xx\",\"xxx\"]"),
    Token: tea.String("JHASD123HAXXX"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetMeCorpSubmissionWithOptions(tea.String("manager123"), getMeCorpSubmissionRequest, getMeCorpSubmissionHeaders, &util.RuntimeOptions{})
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
import dingtalkyida_1_0, * as $dingtalkyida_1_0 from '@alicloud/dingtalk/yida_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkyida_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkyida_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let getMeCorpSubmissionHeaders = new $dingtalkyida_1_0.GetMeCorpSubmissionHeaders({ });
    getMeCorpSubmissionHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getMeCorpSubmissionRequest = new $dingtalkyida_1_0.GetMeCorpSubmissionRequest({
      corpId: "ding123",
      pageSize: 10,
      language: "zh_CN",
      pageNumber: 1,
      keyword: "{}",
      appTypes: "[\"APP_xxx\",\"APP_xxx\"]",
      processCodes: "[\"xx\",\"xxx\"]",
      token: "JHASD123HAXXX",
    });
    try {
      await client.getMeCorpSubmissionWithOptions("manager123", getMeCorpSubmissionRequest, getMeCorpSubmissionHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkyida_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkyida_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkyida_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.GetMeCorpSubmissionHeaders getMeCorpSubmissionHeaders = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.GetMeCorpSubmissionHeaders();
            getMeCorpSubmissionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkyida_1_0.Models.GetMeCorpSubmissionRequest getMeCorpSubmissionRequest = new AlibabaCloud.SDK.Dingtalkyida_1_0.Models.GetMeCorpSubmissionRequest
            {
                CorpId = "ding123",
                PageSize = 10,
                Language = "zh_CN",
                PageNumber = 1,
                Keyword = "{}",
                AppTypes = "[\"APP_xxx\",\"APP_xxx\"]",
                ProcessCodes = "[\"xx\",\"xxx\"]",
                Token = "JHASD123HAXXX",
            };
            try
            {
                client.GetMeCorpSubmissionWithOptions("manager123", getMeCorpSubmissionRequest, getMeCorpSubmissionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkyida__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkyida_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkyida_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::Client> client = make_shared<Alibabacloud_Dingtalkyida_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::GetMeCorpSubmissionHeaders> getMeCorpSubmissionHeaders = make_shared<Alibabacloud_Dingtalkyida_1_0::GetMeCorpSubmissionHeaders>();
  getMeCorpSubmissionHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkyida_1_0::GetMeCorpSubmissionRequest> getMeCorpSubmissionRequest = make_shared<Alibabacloud_Dingtalkyida_1_0::GetMeCorpSubmissionRequest>(map<string, boost::any>({
    {"corpId", boost::any(string("ding123"))},
    {"pageSize", boost::any(10)},
    {"language", boost::any(string("zh_CN"))},
    {"pageNumber", boost::any(1)},
    {"keyword", boost::any(string("{}"))},
    {"appTypes", boost::any(string("["APP_xxx","APP_xxx"]"))},
    {"processCodes", boost::any(string("["xx","xxx"]"))},
    {"token", boost::any(string("JHASD123HAXXX"))}
  }));
  try {
    client->getMeCorpSubmissionWithOptions(make_shared<string>("manager123"), getMeCorpSubmissionRequest, getMeCorpSubmissionHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| totalCount | Long | 总数量。 |
| pageNumber | Long | 当前第几页。 |
| data | Array | 任务列表。 |
| actionerName | Array of String | 执行人姓名。 |
| processInstanceId | String | 流程实例ID。 |
| modifiedTimeGMT | String | 修改时间。 |
| finishTimeGMT | String | 结束时间。 |
| formUuid | String | 表单ID。 |
| processInstanceStatus | String | 流程实例状态。 |
| originatorDisplayName | String | 发起人展示名称。 |
| dataType | String | 数据类型。 |
| originatorAvatar | String | 发起人头像。 |
| processInstanceStatusText | String | 流程状态展示文案。 |
| actioner | Array | 任务执行者信息。 |
| employeeTypeInformation | String | 员工类型信息。 |
| employeeType | String | 员工类型。 |
| level | String | 层级。 |
| nickName | String | 花名。 |
| orderNumber | String | 订单号。 |
| pinyinNickName | String | 花名拼音。 |
| superUserId | String | 超管的userid。 |
| userId | String | 用户的userid。 |
| buName | String | BU的名称。 |
| tbWang | String | 淘宝旺。 |
| humanResourceGroupWorkNumber | String | HRG的userid。 |
| pinyinNameAll | String | 全名拼音。 |
| name | String | 名称。 |
| state | String | 状态。 |
| personalPhotoUrl | String | 个人照片的URL。 |
| isSystemAdmin | Boolean | 是否系统管理员。 |
| email | String | 邮箱。 |
| personalPhoto | String | 个人照片。 |
| processApprovedResultText | String | 流程审批结果文字表示。 |
| formInstanceId | String | 要查询的实例的实例ID。 |
| title | String | 标题。 |
| version | Long | 版本。 |
| instanceValue | String | 实例数据。 |
| processApprovedResult | String | 流程审批结果。 |
| createTimeGMT | String | 创建时间。 |
| processId | Long | 流程ID。 |
| processName | String | 流程名称。 |
| processCode | String | 流程编码。 |
| appType | String | 应用ID。 |
| actionerId | Array of String | 操作者的userid。 |
| dataMap | Map | 任务数据。 |
| currentActivityInstances | Array | 当前流程节点实例。 |
| activityName | String | 节点名称。 |
| activityNameEn | String | 节点英文名称。 |
| activityId | String | 节点ID。 |
| id | Long | 数据ID。 |
| activityInstanceStatus | String | 节点实例状态。 |
| originatorId | String | 发起人userid。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "totalCount" : 10,
  "pageNumber" : 1,
  "data" : [ {
    "actionerName" : [ "张三" ],
    "processInstanceId" : "f30233fb-72e1-xxx",
    "modifiedTimeGMT" : "2021-01-01",
    "finishTimeGMT" : "2021-01-01",
    "formUuid" : "FORM-EF6xxx",
    "processInstanceStatus" : "finished",
    "originatorDisplayName" : "张三",
    "dataType" : "edit",
    "originatorAvatar" : "zhangsan@mediaId",
    "processInstanceStatusText" : "已同意",
    "actioner" : [ {
      "employeeTypeInformation" : "official",
      "employeeType" : "正式",
      "level" : "P7",
      "nickName" : "与心",
      "orderNumber" : "o-YDJKINSxxx",
      "pinyinNickName" : "xiaohong",
      "superUserId" : "manager123",
      "userId" : "manager123",
      "buName" : "某研究部",
      "tbWang" : "wang123",
      "humanResourceGroupWorkNumber" : "123311221",
      "pinyinNameAll" : "XIAOHONG",
      "name" : "请购单",
      "state" : "running",
      "personalPhotoUrl" : "https://oss/zhangsan.png",
      "isSystemAdmin" : true,
      "email" : "abc@alimail.com",
      "personalPhoto" : "https://abc.com/a.png"
    } ],
    "processApprovedResultText" : "通过",
    "formInstanceId" : "FINST-NJYJxxx",
    "title" : "小红发起的请购单",
    "version" : 1,
    "instanceValue" : "符合宜搭表单实例格式的json数据",
    "processApprovedResult" : "同意",
    "createTimeGMT" : "2021-01-01",
    "processName" : "小红的单子",
    "processCode" : "TPROC--X1Gxxx",
    "appType" : "APP_PBKT0xxx",
    "actionerId" : [ "manager123" ],
    "currentActivityInstances" : [ {
      "activityName" : "activity-124",
      "activityNameEn" : "redirect task",
      "activityId" : "act-xxaanfaf",
      "id" : 12345,
      "activityInstanceStatus" : "running"
    } ],
    "originatorId" : "manager123"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalidParameter.methodInputs.invalidFormat | 数据格式错误:%s | 数据格式错误 |
| 400 | invalidParameter.number.exceed | 数字超过限制:%s | 数字超过限制 |
| 400 | invalidParameter.methodInputs.invalid | 入参校验失败:%s | 入参校验失败 |
| 400 | dataNotExist.form.notExists | 表单不存在:%s | 表单不存在 |
| 500 | dataModified.form.formAlreadyModified | 实例数据已修改, 请刷新当前页面:%s | 实例数据已经修改 |
| 500 | unclassifiedError | 异常:%s | 通用异常信息 |
