---
title: "生产单"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-a-production-order"
namespace: "development"
slug: "add-or-edit-a-production-order"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 生产 > 生产单"
doc_id: "3fRsqh8nlJ"
updated_at: "2026-01-29 14:19:37"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-a-production-order
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 生产 > 生产单
> Updated: 2026-01-29 14:19:37

# 生产单

调用本接口新增或编辑生产单。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/productions |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Jzcrm.Common.ReadWrite-金智CRM数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| datatype | Long | 是 | 数据类型，固定值**156**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。      值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| sch\_title | String | 是 | 主题。 |
| sch\_number | String | 是 | 单号。 |
| sch\_starttime | String | 是 | 开始日期。 |
| sch\_planendtime | String | 是 | 计划完成时间。 |
| sch\_customerid | String | 否 | 对应客户。 |
| sch\_htid | String | 否 | 订单。 |
| sch\_endtime | String | 否 | 完成日期。 |
| sch\_principal | String | 否 | 负责人。 |
| sch\_makeemp | String | 否 | 生产人员。 |
| sch\_remark | String | 否 | 备注。 |
| sch\_statesstr | String | 否 | 阶段，取值。   - 计划 - 审核 - 领料 - 生产 - 验收 - 入库/退料 - 结单 - 取消 |
| sch\_finished | String | 否 | 状态，取值。   - 未生产 - 生产中 - 生产中止 - 生产完成 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/productions HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961ef7e2f3639zv1jjr76df97e21c
Content-Type:application/json

{
  "datatype" : 156,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "sch_title" : "主题",
    "sch_number" : "SCD7768687",
    "sch_starttime" : "2021-06-01",
    "sch_planendtime" : "2021-06-01",
    "sch_customerid" : "客户1",
    "sch_htid" : "订单1",
    "sch_endtime" : "2021-06-01",
    "sch_principal" : "李四",
    "sch_makeemp" : "王五",
    "sch_remark" : "备注",
    "sch_statesstr" : "计划",
    "sch_finished" : "生产中"
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
import com.aliyun.dingtalkjzcrm_1_0.*;
import com.aliyun.dingtalkjzcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkjzcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkjzcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkjzcrm_1_0.Client client = Sample.createClient();
        EditProductionHeaders editProductionHeaders = new EditProductionHeaders();
        editProductionHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditProductionRequest.EditProductionRequestData data = new EditProductionRequest.EditProductionRequestData()
                .setDataUserid("张三")
                .setSchTitle("主题")
                .setSchNumber("SCD7768687")
                .setSchStarttime("2021-06-01")
                .setSchPlanendtime("2021-06-01")
                .setSchCustomerid("客户1")
                .setSchHtid("订单1")
                .setSchEndtime("2021-06-01")
                .setSchPrincipal("李四")
                .setSchMakeemp("王五")
                .setSchRemark("备注")
                .setSchStatesstr("计划")
                .setSchFinished("生产中");
        EditProductionRequest editProductionRequest = new EditProductionRequest()
                .setDatatype(156L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editProductionWithOptions(editProductionRequest, editProductionHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.jzcrm_1_0.client import Client as dingtalkjzcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.jzcrm_1_0 import models as dingtalkjzcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkjzcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkjzcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_production_headers = dingtalkjzcrm__1__0_models.EditProductionHeaders()
        edit_production_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditProductionRequestData(
            data_userid='张三',
            sch_title='主题',
            sch_number='SCD7768687',
            sch_starttime='2021-06-01',
            sch_planendtime='2021-06-01',
            sch_customerid='客户1',
            sch_htid='订单1',
            sch_endtime='2021-06-01',
            sch_principal='李四',
            sch_makeemp='王五',
            sch_remark='备注',
            sch_statesstr='计划',
            sch_finished='生产中'
        )
        edit_production_request = dingtalkjzcrm__1__0_models.EditProductionRequest(
            datatype=156,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_production_with_options(edit_production_request, edit_production_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_production_headers = dingtalkjzcrm__1__0_models.EditProductionHeaders()
        edit_production_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditProductionRequestData(
            data_userid='张三',
            sch_title='主题',
            sch_number='SCD7768687',
            sch_starttime='2021-06-01',
            sch_planendtime='2021-06-01',
            sch_customerid='客户1',
            sch_htid='订单1',
            sch_endtime='2021-06-01',
            sch_principal='李四',
            sch_makeemp='王五',
            sch_remark='备注',
            sch_statesstr='计划',
            sch_finished='生产中'
        )
        edit_production_request = dingtalkjzcrm__1__0_models.EditProductionRequest(
            datatype=156,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_production_with_options_async(edit_production_request, edit_production_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditProductionHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditProductionRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditProductionRequest;
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
        $editProductionHeaders = new EditProductionHeaders([]);
        $editProductionHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "schTitle" => "主题",
            "schNumber" => "SCD7768687",
            "schStarttime" => "2021-06-01",
            "schPlanendtime" => "2021-06-01",
            "schCustomerid" => "客户1",
            "schHtid" => "订单1",
            "schEndtime" => "2021-06-01",
            "schPrincipal" => "李四",
            "schMakeemp" => "王五",
            "schRemark" => "备注",
            "schStatesstr" => "计划",
            "schFinished" => "生产中"
        ]);
        $editProductionRequest = new EditProductionRequest([
            "datatype" => 156,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editProductionWithOptions($editProductionRequest, $editProductionHeaders, new RuntimeOptions([]));
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
  dingtalkjzcrm_1_0  ""github.com/alibabacloud-go/dingtalk/jzcrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkjzcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkjzcrm_1_0.Client{}
  _result, _err = dingtalkjzcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  editProductionHeaders := &dingtalkjzcrm_1_0.EditProductionHeaders{}
  editProductionHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditProductionRequestData{
    DataUserid: tea.String("张三"),
    SchTitle: tea.String("主题"),
    SchNumber: tea.String("SCD7768687"),
    SchStarttime: tea.String("2021-06-01"),
    SchPlanendtime: tea.String("2021-06-01"),
    SchCustomerid: tea.String("客户1"),
    SchHtid: tea.String("订单1"),
    SchEndtime: tea.String("2021-06-01"),
    SchPrincipal: tea.String("李四"),
    SchMakeemp: tea.String("王五"),
    SchRemark: tea.String("备注"),
    SchStatesstr: tea.String("计划"),
    SchFinished: tea.String("生产中"),
  }
  editProductionRequest := &dingtalkjzcrm_1_0.EditProductionRequest{
    Datatype: tea.Int64(156),
    Stamp: tea.Int64(1621822122),
    Msgid: tea.Int64(1),
    Data: data,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.EditProductionWithOptions(editProductionRequest, editProductionHeaders, &util.RuntimeOptions{})
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
import dingtalkjzcrm_1_0, * as $dingtalkjzcrm_1_0 from '"@alicloud/dingtalk/jzcrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkjzcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkjzcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let editProductionHeaders = new $dingtalkjzcrm_1_0.EditProductionHeaders({ });
    editProductionHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditProductionRequestData({
      dataUserid: "张三",
      schTitle: "主题",
      schNumber: "SCD7768687",
      schStarttime: "2021-06-01",
      schPlanendtime: "2021-06-01",
      schCustomerid: "客户1",
      schHtid: "订单1",
      schEndtime: "2021-06-01",
      schPrincipal: "李四",
      schMakeemp: "王五",
      schRemark: "备注",
      schStatesstr: "计划",
      schFinished: "生产中",
    });
    let editProductionRequest = new $dingtalkjzcrm_1_0.EditProductionRequest({
      datatype: 156,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editProductionWithOptions(editProductionRequest, editProductionHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditProductionHeaders editProductionHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditProductionHeaders();
            editProductionHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditProductionRequest.EditProductionRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditProductionRequest.EditProductionRequestData
            {
                DataUserid = "张三",
                SchTitle = "主题",
                SchNumber = "SCD7768687",
                SchStarttime = "2021-06-01",
                SchPlanendtime = "2021-06-01",
                SchCustomerid = "客户1",
                SchHtid = "订单1",
                SchEndtime = "2021-06-01",
                SchPrincipal = "李四",
                SchMakeemp = "王五",
                SchRemark = "备注",
                SchStatesstr = "计划",
                SchFinished = "生产中",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditProductionRequest editProductionRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditProductionRequest
            {
                Datatype = 156,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditProductionWithOptions(editProductionRequest, editProductionHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkjzcrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkjzcrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkjzcrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditProductionHeaders> editProductionHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditProductionHeaders>();
  editProductionHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditProductionRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditProductionRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"schTitle", boost::any(string("主题"))},
    {"schNumber", boost::any(string("SCD7768687"))},
    {"schStarttime", boost::any(string("2021-06-01"))},
    {"schPlanendtime", boost::any(string("2021-06-01"))},
    {"schCustomerid", boost::any(string("客户1"))},
    {"schHtid", boost::any(string("订单1"))},
    {"schEndtime", boost::any(string("2021-06-01"))},
    {"schPrincipal", boost::any(string("李四"))},
    {"schMakeemp", boost::any(string("王五"))},
    {"schRemark", boost::any(string("备注"))},
    {"schStatesstr", boost::any(string("计划"))},
    {"schFinished", boost::any(string("生产中"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditProductionRequest> editProductionRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditProductionRequest>(map<string, boost::any>({
    {"datatype", boost::any(156)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editProductionWithOptions(editProductionRequest, editProductionHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| time | String | 响应时间。 |
| msgid | Long | 编辑数据的ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "time" : "2021-06-01 18:02:55",
  "msgid" : 1
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | saveFail | 保存数据发生错误 | 保存数据发生错误 |
| 400 | invalidRequestMethod | 请求方式错误，必须为post请求！ | 请求方式错误，必须为post请求！ |
| 400 | invalidParameter | 请求参数缺失或无效！ | 请求参数缺失或无效！ |
| 400 | invalidSeCretKey | 无效的SeCretKey | 无效的SeCretKey |
| 400 | invalidSign | 签名无效 | 签名无效 |
