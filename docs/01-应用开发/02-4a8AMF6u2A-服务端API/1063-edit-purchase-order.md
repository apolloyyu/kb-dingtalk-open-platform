---
title: "采购单"
source_url: "https://open.dingtalk.com/document/development/edit-purchase-order"
namespace: "development"
slug: "edit-purchase-order"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 采购 > 采购单"
doc_id: "6BUbMt1lWj"
updated_at: "2026-01-29 14:19:37"
---

> Source: https://open.dingtalk.com/document/development/edit-purchase-order
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 采购 > 采购单
> Updated: 2026-01-29 14:19:37

# 采购单

通过此接口可新增或编辑采购单，实现企业采购流程的数字化管理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/purchases |
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
| datatype | Long | 是 | 数据类型，固定值**153**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| gysid | String | 是 | 供应商。 |
| cgno | String | 是 | 采购单号。 |
| summoney | String | 是 | 采购金额。 |
| cgdate | String | 是 | 采购日期。 |
| cg\_zxstate | String | 是 | 执行状态，取值。   - 执行中 - 结束 - 意外终止 |
| order\_khid | String | 否 | 关联订单客户。 |
| cgname | String | 否 | 采购主题。 |
| gys\_lxrid | String | 否 | 供应商联系人。 |
| gys\_lxrinfo | String | 否 | 联系方式。 |
| cgtype | String | 否 | 自定义采购分类 |
| gysjingban | String | 否 | 供应商代表。 |
| empid | String | 否 | 我方代表。 |
| cg\_moneyzhekou | String | 否 | 优惠折扣率。 |
| cg\_kjmoney | String | 否 | 优惠抹零金额。 |
| cg\_fjmoneylx | String | 否 | 附加费用分类。 |
| cg\_fjmoney | String | 否 | 附加费用金额。 |
| order\_htid | String | 否 | 关联订单。 |
| cgremark | String | 否 | 采购摘要。 |
| child\_mx | String | 否 | 产品明细，json格式。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/purchases HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961ef7e2f3639zv1jjr76df97e21c
Content-Type:application/json

{
  "datatype" : 153,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "gysid" : "供应商1",
    "cgno" : "CG7768698678",
    "summoney" : "10000",
    "cgdate" : "2021-06-01",
    "cg_zxstate" : "执行中",
    "order_khid" : "客户1",
    "cgname" : "采购主题",
    "gys_lxrid" : "王五",
    "gys_lxrinfo" : "19636989568",
    "cgtype" : "经营主产品采购",
    "gysjingban" : "代表1",
    "empid" : "代表2",
    "cg_moneyzhekou" : "12",
    "cg_kjmoney" : "190",
    "cg_fjmoneylx" : "运费",
    "cg_fjmoney" : "10",
    "order_htid" : "订单1",
    "cgremark" : "采购摘要",
    "child_mx" : "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
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
        EditPurchaseHeaders editPurchaseHeaders = new EditPurchaseHeaders();
        editPurchaseHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditPurchaseRequest.EditPurchaseRequestData data = new EditPurchaseRequest.EditPurchaseRequestData()
                .setDataUserid("张三")
                .setGysid("供应商1")
                .setCgno("CG7768698678")
                .setSummoney("10000")
                .setCgdate("2021-06-01")
                .setCgZxstate("执行中")
                .setOrderKhid("客户1")
                .setCgname("采购主题")
                .setGysLxrid("王五")
                .setGysLxrinfo("19636989568")
                .setCgtype("经营主产品采购")
                .setGysjingban("代表1")
                .setEmpid("代表2")
                .setCgMoneyzhekou("12")
                .setCgKjmoney("190")
                .setCgFjmoneylx("运费")
                .setCgFjmoney("10")
                .setOrderHtid("订单1")
                .setCgremark("采购摘要")
                .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
        EditPurchaseRequest editPurchaseRequest = new EditPurchaseRequest()
                .setDatatype(153L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editPurchaseWithOptions(editPurchaseRequest, editPurchaseHeaders, new RuntimeOptions());
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
        edit_purchase_headers = dingtalkjzcrm__1__0_models.EditPurchaseHeaders()
        edit_purchase_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditPurchaseRequestData(
            data_userid='张三',
            gysid='供应商1',
            cgno='CG7768698678',
            summoney='10000',
            cgdate='2021-06-01',
            cg_zxstate='执行中',
            order_khid='客户1',
            cgname='采购主题',
            gys_lxrid='王五',
            gys_lxrinfo='19636989568',
            cgtype='经营主产品采购',
            gysjingban='代表1',
            empid='代表2',
            cg_moneyzhekou='12',
            cg_kjmoney='190',
            cg_fjmoneylx='运费',
            cg_fjmoney='10',
            order_htid='订单1',
            cgremark='采购摘要',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_purchase_request = dingtalkjzcrm__1__0_models.EditPurchaseRequest(
            datatype=153,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_purchase_with_options(edit_purchase_request, edit_purchase_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_purchase_headers = dingtalkjzcrm__1__0_models.EditPurchaseHeaders()
        edit_purchase_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditPurchaseRequestData(
            data_userid='张三',
            gysid='供应商1',
            cgno='CG7768698678',
            summoney='10000',
            cgdate='2021-06-01',
            cg_zxstate='执行中',
            order_khid='客户1',
            cgname='采购主题',
            gys_lxrid='王五',
            gys_lxrinfo='19636989568',
            cgtype='经营主产品采购',
            gysjingban='代表1',
            empid='代表2',
            cg_moneyzhekou='12',
            cg_kjmoney='190',
            cg_fjmoneylx='运费',
            cg_fjmoney='10',
            order_htid='订单1',
            cgremark='采购摘要',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_purchase_request = dingtalkjzcrm__1__0_models.EditPurchaseRequest(
            datatype=153,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_purchase_with_options_async(edit_purchase_request, edit_purchase_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditPurchaseHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditPurchaseRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditPurchaseRequest;
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
        $editPurchaseHeaders = new EditPurchaseHeaders([]);
        $editPurchaseHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "gysid" => "供应商1",
            "cgno" => "CG7768698678",
            "summoney" => "10000",
            "cgdate" => "2021-06-01",
            "cgZxstate" => "执行中",
            "orderKhid" => "客户1",
            "cgname" => "采购主题",
            "gysLxrid" => "王��",
            "gysLxrinfo" => "19636989568",
            "cgtype" => "经营主产品采购",
            "gysjingban" => "代表1",
            "empid" => "代表2",
            "cgMoneyzhekou" => "12",
            "cgKjmoney" => "190",
            "cgFjmoneylx" => "运费",
            "cgFjmoney" => "10",
            "orderHtid" => "订单1",
            "cgremark" => "采购摘要",
            "childMx" => "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
        ]);
        $editPurchaseRequest = new EditPurchaseRequest([
            "datatype" => 153,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editPurchaseWithOptions($editPurchaseRequest, $editPurchaseHeaders, new RuntimeOptions([]));
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

  editPurchaseHeaders := &dingtalkjzcrm_1_0.EditPurchaseHeaders{}
  editPurchaseHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditPurchaseRequestData{
    DataUserid: tea.String("张三"),
    Gysid: tea.String("供应商1"),
    Cgno: tea.String("CG7768698678"),
    Summoney: tea.String("10000"),
    Cgdate: tea.String("2021-06-01"),
    CgZxstate: tea.String("执行中"),
    OrderKhid: tea.String("客户1"),
    Cgname: tea.String("采购主题"),
    GysLxrid: tea.String("王五"),
    GysLxrinfo: tea.String("19636989568"),
    Cgtype: tea.String("经营主产品采购"),
    Gysjingban: tea.String("代表1"),
    Empid: tea.String("代表2"),
    CgMoneyzhekou: tea.String("12"),
    CgKjmoney: tea.String("190"),
    CgFjmoneylx: tea.String("运费"),
    CgFjmoney: tea.String("10"),
    OrderHtid: tea.String("订单1"),
    Cgremark: tea.String("采购摘要"),
    ChildMx: tea.String("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"),
  }
  editPurchaseRequest := &dingtalkjzcrm_1_0.EditPurchaseRequest{
    Datatype: tea.Int64(153),
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
    _, _err = client.EditPurchaseWithOptions(editPurchaseRequest, editPurchaseHeaders, &util.RuntimeOptions{})
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
    let editPurchaseHeaders = new $dingtalkjzcrm_1_0.EditPurchaseHeaders({ });
    editPurchaseHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditPurchaseRequestData({
      dataUserid: "张三",
      gysid: "供应商1",
      cgno: "CG7768698678",
      summoney: "10000",
      cgdate: "2021-06-01",
      cgZxstate: "执行中",
      orderKhid: "客户1",
      cgname: "采购主题",
      gysLxrid: "王五",
      gysLxrinfo: "19636989568",
      cgtype: "经营主产品采购",
      gysjingban: "代表1",
      empid: "代表2",
      cgMoneyzhekou: "12",
      cgKjmoney: "190",
      cgFjmoneylx: "运费",
      cgFjmoney: "10",
      orderHtid: "订单1",
      cgremark: "采购摘要",
      childMx: "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
    });
    let editPurchaseRequest = new $dingtalkjzcrm_1_0.EditPurchaseRequest({
      datatype: 153,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editPurchaseWithOptions(editPurchaseRequest, editPurchaseHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditPurchaseHeaders editPurchaseHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditPurchaseHeaders();
            editPurchaseHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditPurchaseRequest.EditPurchaseRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditPurchaseRequest.EditPurchaseRequestData
            {
                DataUserid = "张三",
                Gysid = "供应商1",
                Cgno = "CG7768698678",
                Summoney = "10000",
                Cgdate = "2021-06-01",
                CgZxstate = "执行中",
                OrderKhid = "客户1",
                Cgname = "采购主题",
                GysLxrid = "王五",
                GysLxrinfo = "19636989568",
                Cgtype = "经营主产品采购",
                Gysjingban = "代表1",
                Empid = "代表2",
                CgMoneyzhekou = "12",
                CgKjmoney = "190",
                CgFjmoneylx = "运费",
                CgFjmoney = "10",
                OrderHtid = "订单1",
                Cgremark = "采购摘要",
                ChildMx = "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditPurchaseRequest editPurchaseRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditPurchaseRequest
            {
                Datatype = 153,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditPurchaseWithOptions(editPurchaseRequest, editPurchaseHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditPurchaseHeaders> editPurchaseHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditPurchaseHeaders>();
  editPurchaseHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditPurchaseRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditPurchaseRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"gysid", boost::any(string("供应商1"))},
    {"cgno", boost::any(string("CG7768698678"))},
    {"summoney", boost::any(string("10000"))},
    {"cgdate", boost::any(string("2021-06-01"))},
    {"cgZxstate", boost::any(string("执行中"))},
    {"orderKhid", boost::any(string("客户1"))},
    {"cgname", boost::any(string("采购主题"))},
    {"gysLxrid", boost::any(string("王五"))},
    {"gysLxrinfo", boost::any(string("19636989568"))},
    {"cgtype", boost::any(string("经营主产品采购"))},
    {"gysjingban", boost::any(string("代表1"))},
    {"empid", boost::any(string("代表2"))},
    {"cgMoneyzhekou", boost::any(string("12"))},
    {"cgKjmoney", boost::any(string("190"))},
    {"cgFjmoneylx", boost::any(string("运费"))},
    {"cgFjmoney", boost::any(string("10"))},
    {"orderHtid", boost::any(string("订单1"))},
    {"cgremark", boost::any(string("采购摘要"))},
    {"childMx", boost::any(string(""child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditPurchaseRequest> editPurchaseRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditPurchaseRequest>(map<string, boost::any>({
    {"datatype", boost::any(153)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editPurchaseWithOptions(editPurchaseRequest, editPurchaseHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
