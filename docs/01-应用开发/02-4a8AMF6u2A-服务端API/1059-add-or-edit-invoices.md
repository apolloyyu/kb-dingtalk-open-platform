---
title: "发货单"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-invoices"
namespace: "development"
slug: "add-or-edit-invoices"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 合同 > 发货单"
doc_id: "VrQubVTnLr"
updated_at: "2026-01-29 14:19:34"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-invoices
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 合同 > 发货单
> Updated: 2026-01-29 14:19:34

# 发货单

通过此接口新增或编辑发货单据，实现与金智CRM系统的数据同步。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/invoices |
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
| datatype | Long | 是 | 数据类型，固定值**169**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| fh\_customerid | String | 是 | 对应客户。 |
| fh\_date | String | 是 | 发货日期。 |
| fh\_number | String | 是 | 发货单号。 |
| fh\_mode | String | 是 | 发货方式。 |
| fh\_htorder | String | 否 | 对应订单。 |
| fh\_title | String | 否 | 发货主题。 |
| fh\_yunfei | String | 否 | 运费。 |
| fh\_jianshu | String | 否 | 打包件数。 |
| fh\_kg | String | 否 | 重量，单位：Kg。 |
| fh\_shipper | String | 否 | 发货人。 |
| fh\_preside | String | 否 | 所有者。 |
| fh\_lxrid | String | 否 | 联系人。 |
| fh\_linkman | String | 否 | 收货人。 |
| fh\_tel | String | 否 | 电话。 |
| fh\_handset | String | 否 | 手机。 |
| fh\_post | String | 否 | 邮编。 |
| fh\_address | String | 否 | 地址。 |
| fh\_email | String | 否 | 邮箱。 |
| fh\_msn | String | 否 | MSN账号。 |
| fh\_remark | String | 否 | 备注。 |
| fh\_state | String | 否 | 发货状态。 |
| child\_mx | String | 否 | 产品明细，json格式。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/invoices HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961exxxx
Content-Type:application/json

{
  "datatype" : 169,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "fh_customerid" : "客户1",
    "fh_date" : "2021-06-01",
    "fh_number" : "FH87997978687",
    "fh_mode" : "顺丰快递",
    "fh_htorder" : "1",
    "fh_title" : "发货主题",
    "fh_yunfei" : "10",
    "fh_jianshu" : "1",
    "fh_kg" : "12.5",
    "fh_shipper" : "李四",
    "fh_preside" : "王五",
    "fh_lxrid" : "朱六",
    "fh_linkman" : "杨七",
    "fh_tel" : "0622-8985652",
    "fh_handset" : "18965362369",
    "fh_post" : "268996",
    "fh_address" : "山东省青岛市",
    "fh_email" : "5268685@qq.com",
    "fh_msn" : "MSN",
    "fh_remark" : "备注",
    "fh_state" : "已发货",
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
        EditInvoiceHeaders editInvoiceHeaders = new EditInvoiceHeaders();
        editInvoiceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditInvoiceRequest.EditInvoiceRequestData data = new EditInvoiceRequest.EditInvoiceRequestData()
                .setDataUserid("张三")
                .setFhCustomerid("客户1")
                .setFhDate("2021-06-01")
                .setFhNumber("FH87997978687")
                .setFhMode("顺丰快递")
                .setFhHtorder("1")
                .setFhTitle("发货主题")
                .setFhYunfei("10")
                .setFhJianshu("1")
                .setFhKg("12.5")
                .setFhShipper("李四")
                .setFhPreside("王五")
                .setFhLxrid("朱六")
                .setFhLinkman("杨七")
                .setFhTel("0622-8985652")
                .setFhHandset("18965362369")
                .setFhPost("268996")
                .setFhAddress("山东省青岛市")
                .setFhEmail("5268685@qq.com")
                .setFhMsn("MSN")
                .setFhRemark("备注")
                .setFhState("已发货")
                .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
        EditInvoiceRequest editInvoiceRequest = new EditInvoiceRequest()
                .setDatatype(169L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editInvoiceWithOptions(editInvoiceRequest, editInvoiceHeaders, new RuntimeOptions());
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
        edit_invoice_headers = dingtalkjzcrm__1__0_models.EditInvoiceHeaders()
        edit_invoice_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditInvoiceRequestData(
            data_userid='张三',
            fh_customerid='客户1',
            fh_date='2021-06-01',
            fh_number='FH87997978687',
            fh_mode='顺丰快递',
            fh_htorder='1',
            fh_title='发货主题',
            fh_yunfei='10',
            fh_jianshu='1',
            fh_kg='12.5',
            fh_shipper='李四',
            fh_preside='王五',
            fh_lxrid='朱六',
            fh_linkman='杨七',
            fh_tel='0622-8985652',
            fh_handset='18965362369',
            fh_post='268996',
            fh_address='山东省青岛市',
            fh_email='5268685@qq.com',
            fh_msn='MSN',
            fh_remark='备注',
            fh_state='已发货',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_invoice_request = dingtalkjzcrm__1__0_models.EditInvoiceRequest(
            datatype=169,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_invoice_with_options(edit_invoice_request, edit_invoice_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_invoice_headers = dingtalkjzcrm__1__0_models.EditInvoiceHeaders()
        edit_invoice_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditInvoiceRequestData(
            data_userid='张三',
            fh_customerid='客户1',
            fh_date='2021-06-01',
            fh_number='FH87997978687',
            fh_mode='顺丰快递',
            fh_htorder='1',
            fh_title='发货主题',
            fh_yunfei='10',
            fh_jianshu='1',
            fh_kg='12.5',
            fh_shipper='李四',
            fh_preside='王五',
            fh_lxrid='朱六',
            fh_linkman='杨七',
            fh_tel='0622-8985652',
            fh_handset='18965362369',
            fh_post='268996',
            fh_address='山东省青岛市',
            fh_email='5268685@qq.com',
            fh_msn='MSN',
            fh_remark='备注',
            fh_state='已发货',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_invoice_request = dingtalkjzcrm__1__0_models.EditInvoiceRequest(
            datatype=169,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_invoice_with_options_async(edit_invoice_request, edit_invoice_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditInvoiceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditInvoiceRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditInvoiceRequest;
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
        $editInvoiceHeaders = new EditInvoiceHeaders([]);
        $editInvoiceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "fhCustomerid" => "客户1",
            "fhDate" => "2021-06-01",
            "fhNumber" => "FH87997978687",
            "fhMode" => "顺丰快递",
            "fhHtorder" => "1",
            "fhTitle" => "发货主题",
            "fhYunfei" => "10",
            "fhJianshu" => "1",
            "fhKg" => "12.5",
            "fhShipper" => "李四",
            "fhPreside" => "王五",
            "fhLxrid" => "朱六",
            "fhLinkman" => "杨七",
            "fhTel" => "0622-8985652",
            "fhHandset" => "18965362369",
            "fhPost" => "268996",
            "fhAddress" => "山东省青岛市",
            "fhEmail" => "5268685@qq.com",
            "fhMsn" => "MSN",
            "fhRemark" => "备注",
            "fhState" => "已发货",
            "childMx" => "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
        ]);
        $editInvoiceRequest = new EditInvoiceRequest([
            "datatype" => 169,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editInvoiceWithOptions($editInvoiceRequest, $editInvoiceHeaders, new RuntimeOptions([]));
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

  editInvoiceHeaders := &dingtalkjzcrm_1_0.EditInvoiceHeaders{}
  editInvoiceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditInvoiceRequestData{
    DataUserid: tea.String("张三"),
    FhCustomerid: tea.String("客户1"),
    FhDate: tea.String("2021-06-01"),
    FhNumber: tea.String("FH87997978687"),
    FhMode: tea.String("顺丰快递"),
    FhHtorder: tea.String("1"),
    FhTitle: tea.String("发货主题"),
    FhYunfei: tea.String("10"),
    FhJianshu: tea.String("1"),
    FhKg: tea.String("12.5"),
    FhShipper: tea.String("李四"),
    FhPreside: tea.String("王五"),
    FhLxrid: tea.String("朱六"),
    FhLinkman: tea.String("杨七"),
    FhTel: tea.String("0622-8985652"),
    FhHandset: tea.String("18965362369"),
    FhPost: tea.String("268996"),
    FhAddress: tea.String("山东省青岛市"),
    FhEmail: tea.String("5268685@qq.com"),
    FhMsn: tea.String("MSN"),
    FhRemark: tea.String("备注"),
    FhState: tea.String("已发货"),
    ChildMx: tea.String("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"),
  }
  editInvoiceRequest := &dingtalkjzcrm_1_0.EditInvoiceRequest{
    Datatype: tea.Int64(169),
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
    _, _err = client.EditInvoiceWithOptions(editInvoiceRequest, editInvoiceHeaders, &util.RuntimeOptions{})
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
    let editInvoiceHeaders = new $dingtalkjzcrm_1_0.EditInvoiceHeaders({ });
    editInvoiceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditInvoiceRequestData({
      dataUserid: "张三",
      fhCustomerid: "客户1",
      fhDate: "2021-06-01",
      fhNumber: "FH87997978687",
      fhMode: "顺丰快递",
      fhHtorder: "1",
      fhTitle: "发货主题",
      fhYunfei: "10",
      fhJianshu: "1",
      fhKg: "12.5",
      fhShipper: "李四",
      fhPreside: "王五",
      fhLxrid: "朱六",
      fhLinkman: "杨七",
      fhTel: "0622-8985652",
      fhHandset: "18965362369",
      fhPost: "268996",
      fhAddress: "山东省青岛市",
      fhEmail: "5268685@qq.com",
      fhMsn: "MSN",
      fhRemark: "备注",
      fhState: "已发货",
      childMx: "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
    });
    let editInvoiceRequest = new $dingtalkjzcrm_1_0.EditInvoiceRequest({
      datatype: 169,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editInvoiceWithOptions(editInvoiceRequest, editInvoiceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditInvoiceHeaders editInvoiceHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditInvoiceHeaders();
            editInvoiceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditInvoiceRequest.EditInvoiceRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditInvoiceRequest.EditInvoiceRequestData
            {
                DataUserid = "张三",
                FhCustomerid = "客户1",
                FhDate = "2021-06-01",
                FhNumber = "FH87997978687",
                FhMode = "顺丰快递",
                FhHtorder = "1",
                FhTitle = "发货主题",
                FhYunfei = "10",
                FhJianshu = "1",
                FhKg = "12.5",
                FhShipper = "李四",
                FhPreside = "王五",
                FhLxrid = "朱六",
                FhLinkman = "杨七",
                FhTel = "0622-8985652",
                FhHandset = "18965362369",
                FhPost = "268996",
                FhAddress = "山东省青岛市",
                FhEmail = "5268685@qq.com",
                FhMsn = "MSN",
                FhRemark = "备注",
                FhState = "已发货",
                ChildMx = "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditInvoiceRequest editInvoiceRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditInvoiceRequest
            {
                Datatype = 169,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditInvoiceWithOptions(editInvoiceRequest, editInvoiceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditInvoiceHeaders> editInvoiceHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditInvoiceHeaders>();
  editInvoiceHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditInvoiceRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditInvoiceRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"fhCustomerid", boost::any(string("客户1"))},
    {"fhDate", boost::any(string("2021-06-01"))},
    {"fhNumber", boost::any(string("FH87997978687"))},
    {"fhMode", boost::any(string("顺丰快递"))},
    {"fhHtorder", boost::any(string("1"))},
    {"fhTitle", boost::any(string("发货主题"))},
    {"fhYunfei", boost::any(string("10"))},
    {"fhJianshu", boost::any(string("1"))},
    {"fhKg", boost::any(string("12.5"))},
    {"fhShipper", boost::any(string("李四"))},
    {"fhPreside", boost::any(string("王五"))},
    {"fhLxrid", boost::any(string("朱六"))},
    {"fhLinkman", boost::any(string("杨七"))},
    {"fhTel", boost::any(string("0622-8985652"))},
    {"fhHandset", boost::any(string("18965362369"))},
    {"fhPost", boost::any(string("268996"))},
    {"fhAddress", boost::any(string("山东省青岛市"))},
    {"fhEmail", boost::any(string("5268685@qq.com"))},
    {"fhMsn", boost::any(string("MSN"))},
    {"fhRemark", boost::any(string("备注"))},
    {"fhState", boost::any(string("已发货"))},
    {"childMx", boost::any(string(""child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditInvoiceRequest> editInvoiceRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditInvoiceRequest>(map<string, boost::any>({
    {"datatype", boost::any(169)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editInvoiceWithOptions(editInvoiceRequest, editInvoiceHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
