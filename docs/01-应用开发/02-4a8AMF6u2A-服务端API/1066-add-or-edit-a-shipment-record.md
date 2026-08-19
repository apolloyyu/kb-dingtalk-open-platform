---
title: "入库单"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-a-shipment-record"
namespace: "development"
slug: "add-or-edit-a-shipment-record"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 库存 > 入库单"
doc_id: "0BPjkr1HE4"
updated_at: "2026-01-29 14:19:39"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-a-shipment-record
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 库存 > 入库单
> Updated: 2026-01-29 14:19:39

# 入库单

通过此接口可新增或编辑金智CRM系统中的入库单据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/intostocks |
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
| datatype | Long | 是 | 数据类型，固定值**189**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| libiodate | String | 是 | 入库日期。 |
| stocklibid | String | 是 | 入库仓库。 |
| libiostate | String | 是 | 入库状态，取值。   - 未入库 - 已入库 |
| billno | String | 是 | 入库单号。 |
| customerid | String | 否 | 取值。   - 供应商ID或名称 - 客户ID或名称 |
| empid | String | 是 | 入库经办人。 |
| inorout | String | 否 | 单据类型   - 入库 - 销售退货 - 生产退料 - 生产入库 - 维修退货 |
| libioname | String | 否 | 入库主题。 |
| orderid | String | 否 | 对应单据。 |
| askempid | String | 否 | 入库申请人。 |
| remark | String | 否 | 申请备注。 |
| auditreson | String | 否 | 入库备注。 |
| child\_mx | String | 是 | 产品明细，json格式。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/intostocks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961ef7e2f3639zv1jjr76df97e21c
Content-Type:application/json

{
  "datatype" : 189,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "libiodate" : "2021-06-01",
    "stocklibid" : "华东大仓",
    "libiostate" : "已入库",
    "billno" : "RK784668968",
    "customerid" : "供应商1",
    "empid" : "李四",
    "inorout" : "入库",
    "libioname" : "生产入库",
    "orderid" : "1",
    "askempid" : "王五",
    "remark" : "申请备注",
    "auditreson" : "入库备注",
    "child_mx" : "[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
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
        EditIntostockHeaders editIntostockHeaders = new EditIntostockHeaders();
        editIntostockHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditIntostockRequest.EditIntostockRequestData data = new EditIntostockRequest.EditIntostockRequestData()
                .setDataUserid("张三")
                .setLibiodate("2021-06-01")
                .setStocklibid("华东大仓")
                .setLibiostate("已入库")
                .setBillno("RK784668968")
                .setCustomerid("供应商1")
                .setEmpid("李四")
                .setInorout("入库")
                .setLibioname("生产入库")
                .setOrderid("1")
                .setAskempid("王五")
                .setRemark("申请备注")
                .setAuditreson("入库备注")
                .setChildMx("[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
        EditIntostockRequest editIntostockRequest = new EditIntostockRequest()
                .setDatatype(189L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editIntostockWithOptions(editIntostockRequest, editIntostockHeaders, new RuntimeOptions());
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
        edit_intostock_headers = dingtalkjzcrm__1__0_models.EditIntostockHeaders()
        edit_intostock_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditIntostockRequestData(
            data_userid='张三',
            libiodate='2021-06-01',
            stocklibid='华东大仓',
            libiostate='已入库',
            billno='RK784668968',
            customerid='供应商1',
            empid='李四',
            inorout='入库',
            libioname='生产入库',
            orderid='1',
            askempid='王五',
            remark='申请备注',
            auditreson='入库备注',
            child_mx='[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_intostock_request = dingtalkjzcrm__1__0_models.EditIntostockRequest(
            datatype=189,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_intostock_with_options(edit_intostock_request, edit_intostock_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_intostock_headers = dingtalkjzcrm__1__0_models.EditIntostockHeaders()
        edit_intostock_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditIntostockRequestData(
            data_userid='张三',
            libiodate='2021-06-01',
            stocklibid='华东大仓',
            libiostate='已入库',
            billno='RK784668968',
            customerid='供应商1',
            empid='李四',
            inorout='入库',
            libioname='生产入库',
            orderid='1',
            askempid='王五',
            remark='申请备注',
            auditreson='入库备注',
            child_mx='[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_intostock_request = dingtalkjzcrm__1__0_models.EditIntostockRequest(
            datatype=189,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_intostock_with_options_async(edit_intostock_request, edit_intostock_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditIntostockHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditIntostockRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditIntostockRequest;
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
        $editIntostockHeaders = new EditIntostockHeaders([]);
        $editIntostockHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "libiodate" => "2021-06-01",
            "stocklibid" => "华东大仓",
            "libiostate" => "已入库",
            "billno" => "RK784668968",
            "customerid" => "供应商1",
            "empid" => "李四",
            "inorout" => "入库",
            "libioname" => "生产入库",
            "orderid" => "1",
            "askempid" => "王五",
            "remark" => "申请备注",
            "auditreson" => "入库备注",
            "childMx" => "[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
        ]);
        $editIntostockRequest = new EditIntostockRequest([
            "datatype" => 189,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editIntostockWithOptions($editIntostockRequest, $editIntostockHeaders, new RuntimeOptions([]));
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

  editIntostockHeaders := &dingtalkjzcrm_1_0.EditIntostockHeaders{}
  editIntostockHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditIntostockRequestData{
    DataUserid: tea.String("张三"),
    Libiodate: tea.String("2021-06-01"),
    Stocklibid: tea.String("华东大仓"),
    Libiostate: tea.String("已入库"),
    Billno: tea.String("RK784668968"),
    Customerid: tea.String("供应商1"),
    Empid: tea.String("李四"),
    Inorout: tea.String("入库"),
    Libioname: tea.String("生产入库"),
    Orderid: tea.String("1"),
    Askempid: tea.String("王五"),
    Remark: tea.String("申请备注"),
    Auditreson: tea.String("入库备注"),
    ChildMx: tea.String("[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"),
  }
  editIntostockRequest := &dingtalkjzcrm_1_0.EditIntostockRequest{
    Datatype: tea.Int64(189),
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
    _, _err = client.EditIntostockWithOptions(editIntostockRequest, editIntostockHeaders, &util.RuntimeOptions{})
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
    let editIntostockHeaders = new $dingtalkjzcrm_1_0.EditIntostockHeaders({ });
    editIntostockHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditIntostockRequestData({
      dataUserid: "张三",
      libiodate: "2021-06-01",
      stocklibid: "华东大仓",
      libiostate: "已入库",
      billno: "RK784668968",
      customerid: "供应商1",
      empid: "李四",
      inorout: "入库",
      libioname: "生产入库",
      orderid: "1",
      askempid: "王五",
      remark: "申请备注",
      auditreson: "入库备注",
      childMx: "[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
    });
    let editIntostockRequest = new $dingtalkjzcrm_1_0.EditIntostockRequest({
      datatype: 189,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editIntostockWithOptions(editIntostockRequest, editIntostockHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditIntostockHeaders editIntostockHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditIntostockHeaders();
            editIntostockHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditIntostockRequest.EditIntostockRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditIntostockRequest.EditIntostockRequestData
            {
                DataUserid = "张三",
                Libiodate = "2021-06-01",
                Stocklibid = "华东大仓",
                Libiostate = "已入库",
                Billno = "RK784668968",
                Customerid = "供应商1",
                Empid = "李四",
                Inorout = "入库",
                Libioname = "生产入库",
                Orderid = "1",
                Askempid = "王五",
                Remark = "申请备注",
                Auditreson = "入库备注",
                ChildMx = "[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditIntostockRequest editIntostockRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditIntostockRequest
            {
                Datatype = 189,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditIntostockWithOptions(editIntostockRequest, editIntostockHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditIntostockHeaders> editIntostockHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditIntostockHeaders>();
  editIntostockHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditIntostockRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditIntostockRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"libiodate", boost::any(string("2021-06-01"))},
    {"stocklibid", boost::any(string("华东大仓"))},
    {"libiostate", boost::any(string("已入库"))},
    {"billno", boost::any(string("RK784668968"))},
    {"customerid", boost::any(string("供应商1"))},
    {"empid", boost::any(string("李四"))},
    {"inorout", boost::any(string("入库"))},
    {"libioname", boost::any(string("生产入库"))},
    {"orderid", boost::any(string("1"))},
    {"askempid", boost::any(string("王五"))},
    {"remark", boost::any(string("申请备注"))},
    {"auditreson", boost::any(string("入库备注"))},
    {"childMx", boost::any(string("[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditIntostockRequest> editIntostockRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditIntostockRequest>(map<string, boost::any>({
    {"datatype", boost::any(189)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editIntostockWithOptions(editIntostockRequest, editIntostockHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| time | String | 响应时间 |
| msgid | Long | 编辑数据的id |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "time" : "2021-06-01 17:55:04",
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
