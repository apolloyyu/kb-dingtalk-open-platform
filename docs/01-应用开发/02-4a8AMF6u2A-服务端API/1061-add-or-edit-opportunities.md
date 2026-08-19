---
title: "销售机会"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-opportunities"
namespace: "development"
slug: "add-or-edit-opportunities"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 销售 > 销售机会"
doc_id: "A6YFNMtEGq"
updated_at: "2026-01-29 14:19:35"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-opportunities
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 销售 > 销售机会
> Updated: 2026-01-29 14:19:35

# 销售机会

通过此接口新增或编辑销售机会，实现CRM系统中商机数据的创建与更新。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/sales |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-Jzcrm.Common.ReadWrite-金智CRM数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| datatype | Long | 是 | 数据类型，固定值**158**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID、    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| xsh\_customerid | String | 是 | 对应客户。 |
| xsh\_title | String | 是 | 主题。 |
| xsh\_date | String | 是 | 发现时间。 |
| xsh\_number | String | 否 | 机会编号。 |
| xsh\_lxrid | String | 否 | 联系人。 |
| xsh\_lianxi | String | 否 | 联系方式。 |
| xsh\_type | String | 否 | 类型。 |
| xsh\_from | String | 否 | 来源。 |
| xsh\_preside | String | 否 | 所有者。 |
| xsh\_provider | String | 否 | 提供人。 |
| xsh\_require | String | 否 | 客户需求。 |
| xsh\_expdate | String | 否 | 预计签单日。 |
| xsh\_expmoney | String | 否 | 预期金额。 |
| xsh\_moneynote | String | 否 | 外币备注。 |
| xsh\_phase | String | 否 | 阶段。 |
| xsh\_knx | String | 否 | 可能性。 |
| xsh\_state | String | 否 | 状态。 |
| xsh\_phasenote | String | 否 | 阶段备注。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/sales HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:15996xxx
Content-Type:application/json

{
  "datatype" : 158,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "xsh_customerid" : "金智电子科技有限公司",
    "xsh_title" : "有意向待跟进",
    "xsh_date" : "2020-06-01",
    "xsh_number" : "100001",
    "xsh_lxrid" : "王五",
    "xsh_lianxi" : "16688889999",
    "xsh_type" : "经营合作",
    "xsh_from" : "电话来访",
    "xsh_preside" : "李四",
    "xsh_provider" : "张三",
    "xsh_require" : "需要购买两瓶可爱多",
    "xsh_expdate" : "2020-06-02",
    "xsh_expmoney" : "61",
    "xsh_moneynote" : "美元",
    "xsh_phase" : "初期沟通",
    "xsh_knx" : "99%",
    "xsh_state" : "售前跟踪",
    "xsh_phasenote" : "未购买"
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
        EditSalesHeaders editSalesHeaders = new EditSalesHeaders();
        editSalesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditSalesRequest.EditSalesRequestData data = new EditSalesRequest.EditSalesRequestData()
                .setDataUserid("张三")
                .setXshCustomerid("金智电子科技有限公司")
                .setXshTitle("有意向待跟进")
                .setXshDate("2020-06-01")
                .setXshNumber("100001")
                .setXshLxrid("王五")
                .setXshLianxi("16688889999")
                .setXshType("经营合作")
                .setXshFrom("电话来访")
                .setXshPreside("李四")
                .setXshProvider("张三")
                .setXshRequire("需要购买两瓶可爱多")
                .setXshExpdate("2020-06-02")
                .setXshExpmoney("61")
                .setXshMoneynote("美元")
                .setXshPhase("初期沟通")
                .setXshKnx("99%")
                .setXshState("售前跟踪")
                .setXshPhasenote("未购买");
        EditSalesRequest editSalesRequest = new EditSalesRequest()
                .setDatatype(158L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editSalesWithOptions(editSalesRequest, editSalesHeaders, new RuntimeOptions());
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
        edit_sales_headers = dingtalkjzcrm__1__0_models.EditSalesHeaders()
        edit_sales_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditSalesRequestData(
            data_userid='张三',
            xsh_customerid='金智电子科技有限公司',
            xsh_title='有意向待跟进',
            xsh_date='2020-06-01',
            xsh_number='100001',
            xsh_lxrid='王五',
            xsh_lianxi='16688889999',
            xsh_type='经营合作',
            xsh_from='电话来访',
            xsh_preside='李四',
            xsh_provider='张三',
            xsh_require='需要购买两瓶可爱多',
            xsh_expdate='2020-06-02',
            xsh_expmoney='61',
            xsh_moneynote='美元',
            xsh_phase='初期沟通',
            xsh_knx='99%',
            xsh_state='售前跟踪',
            xsh_phasenote='未购买'
        )
        edit_sales_request = dingtalkjzcrm__1__0_models.EditSalesRequest(
            datatype=158,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_sales_with_options(edit_sales_request, edit_sales_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_sales_headers = dingtalkjzcrm__1__0_models.EditSalesHeaders()
        edit_sales_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditSalesRequestData(
            data_userid='张三',
            xsh_customerid='金智电子科技有限公司',
            xsh_title='有意向待跟进',
            xsh_date='2020-06-01',
            xsh_number='100001',
            xsh_lxrid='王五',
            xsh_lianxi='16688889999',
            xsh_type='经营合作',
            xsh_from='电话来访',
            xsh_preside='李四',
            xsh_provider='张三',
            xsh_require='需要购买两瓶可爱多',
            xsh_expdate='2020-06-02',
            xsh_expmoney='61',
            xsh_moneynote='美元',
            xsh_phase='初期沟通',
            xsh_knx='99%',
            xsh_state='售前跟踪',
            xsh_phasenote='未购买'
        )
        edit_sales_request = dingtalkjzcrm__1__0_models.EditSalesRequest(
            datatype=158,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_sales_with_options_async(edit_sales_request, edit_sales_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditSalesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditSalesRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditSalesRequest;
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
        $editSalesHeaders = new EditSalesHeaders([]);
        $editSalesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "xshCustomerid" => "金智电子科技有限公司",
            "xshTitle" => "有意向待跟进",
            "xshDate" => "2020-06-01",
            "xshNumber" => "100001",
            "xshLxrid" => "王五",
            "xshLianxi" => "16688889999",
            "xshType" => "经营合作",
            "xshFrom" => "电话来访",
            "xshPreside" => "李四",
            "xshProvider" => "张三",
            "xshRequire" => "需要购买两瓶可爱多",
            "xshExpdate" => "2020-06-02",
            "xshExpmoney" => "61",
            "xshMoneynote" => "美元",
            "xshPhase" => "初期沟通",
            "xshKnx" => "99%",
            "xshState" => "售前跟踪",
            "xshPhasenote" => "未购买"
        ]);
        $editSalesRequest = new EditSalesRequest([
            "datatype" => 158,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editSalesWithOptions($editSalesRequest, $editSalesHeaders, new RuntimeOptions([]));
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

  editSalesHeaders := &dingtalkjzcrm_1_0.EditSalesHeaders{}
  editSalesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditSalesRequestData{
    DataUserid: tea.String("张三"),
    XshCustomerid: tea.String("金智电子科技有限公司"),
    XshTitle: tea.String("有意向待跟进"),
    XshDate: tea.String("2020-06-01"),
    XshNumber: tea.String("100001"),
    XshLxrid: tea.String("王五"),
    XshLianxi: tea.String("16688889999"),
    XshType: tea.String("经营合作"),
    XshFrom: tea.String("电话来访"),
    XshPreside: tea.String("李四"),
    XshProvider: tea.String("张三"),
    XshRequire: tea.String("需要购买两瓶可爱多"),
    XshExpdate: tea.String("2020-06-02"),
    XshExpmoney: tea.String("61"),
    XshMoneynote: tea.String("美元"),
    XshPhase: tea.String("初期沟通"),
    XshKnx: tea.String("99%"),
    XshState: tea.String("售前跟踪"),
    XshPhasenote: tea.String("未购买"),
  }
  editSalesRequest := &dingtalkjzcrm_1_0.EditSalesRequest{
    Datatype: tea.Int64(158),
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
    _, _err = client.EditSalesWithOptions(editSalesRequest, editSalesHeaders, &util.RuntimeOptions{})
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
    let editSalesHeaders = new $dingtalkjzcrm_1_0.EditSalesHeaders({ });
    editSalesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditSalesRequestData({
      dataUserid: "张三",
      xshCustomerid: "金智电子科技有限公司",
      xshTitle: "有意向待跟进",
      xshDate: "2020-06-01",
      xshNumber: "100001",
      xshLxrid: "王五",
      xshLianxi: "16688889999",
      xshType: "经营合作",
      xshFrom: "电话来访",
      xshPreside: "李四",
      xshProvider: "张三",
      xshRequire: "需要购买两瓶可爱多",
      xshExpdate: "2020-06-02",
      xshExpmoney: "61",
      xshMoneynote: "美元",
      xshPhase: "初期沟通",
      xshKnx: "99%",
      xshState: "售前跟踪",
      xshPhasenote: "未购买",
    });
    let editSalesRequest = new $dingtalkjzcrm_1_0.EditSalesRequest({
      datatype: 158,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editSalesWithOptions(editSalesRequest, editSalesHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditSalesHeaders editSalesHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditSalesHeaders();
            editSalesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditSalesRequest.EditSalesRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditSalesRequest.EditSalesRequestData
            {
                DataUserid = "张三",
                XshCustomerid = "金智电子科技有限公司",
                XshTitle = "有意向待跟进",
                XshDate = "2020-06-01",
                XshNumber = "100001",
                XshLxrid = "王五",
                XshLianxi = "16688889999",
                XshType = "经营合作",
                XshFrom = "电话来访",
                XshPreside = "李四",
                XshProvider = "张三",
                XshRequire = "需要购买两瓶可爱多",
                XshExpdate = "2020-06-02",
                XshExpmoney = "61",
                XshMoneynote = "美元",
                XshPhase = "初期沟通",
                XshKnx = "99%",
                XshState = "售前跟踪",
                XshPhasenote = "未购买",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditSalesRequest editSalesRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditSalesRequest
            {
                Datatype = 158,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditSalesWithOptions(editSalesRequest, editSalesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditSalesHeaders> editSalesHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditSalesHeaders>();
  editSalesHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditSalesRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditSalesRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"xshCustomerid", boost::any(string("金智电子科技有限公司"))},
    {"xshTitle", boost::any(string("有意向待跟进"))},
    {"xshDate", boost::any(string("2020-06-01"))},
    {"xshNumber", boost::any(string("100001"))},
    {"xshLxrid", boost::any(string("王五"))},
    {"xshLianxi", boost::any(string("16688889999"))},
    {"xshType", boost::any(string("经营合作"))},
    {"xshFrom", boost::any(string("电话来访"))},
    {"xshPreside", boost::any(string("李四"))},
    {"xshProvider", boost::any(string("张三"))},
    {"xshRequire", boost::any(string("需要购买两瓶可爱多"))},
    {"xshExpdate", boost::any(string("2020-06-02"))},
    {"xshExpmoney", boost::any(string("61"))},
    {"xshMoneynote", boost::any(string("美元"))},
    {"xshPhase", boost::any(string("初期沟通"))},
    {"xshKnx", boost::any(string("99%"))},
    {"xshState", boost::any(string("售前跟踪"))},
    {"xshPhasenote", boost::any(string("未购买"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditSalesRequest> editSalesRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditSalesRequest>(map<string, boost::any>({
    {"datatype", boost::any(158)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editSalesWithOptions(editSalesRequest, editSalesHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
