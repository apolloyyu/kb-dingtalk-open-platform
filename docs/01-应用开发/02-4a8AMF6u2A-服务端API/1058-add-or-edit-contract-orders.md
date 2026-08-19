---
title: "合同订单"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-contract-orders"
namespace: "development"
slug: "add-or-edit-contract-orders"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 合同 > 合同订单"
doc_id: "gWQ5uO3y4I"
updated_at: "2026-01-29 14:19:33"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-contract-orders
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 合同 > 合同订单
> Updated: 2026-01-29 14:19:33

# 合同订单

通过本接口可新增或编辑合同订单，支持在企业CRM系统中进行合同数据的创建与更新操作。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/orders |
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
| datatype | Long | 是 | 数据类型，固定填写**150**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| ht\_customerid | String | 是 | 对应客户。 |
| ht\_date | String | 是 | 签单日期。 |
| ht\_preside | String | 是 | 所有者。 |
| ht\_state | String | 是 | 状态，取值。   - 执行中 - 结束 - 意外终止 |
| ht\_summoney | String | 是 | 总金额。 |
| ht\_order | String | 是 | 单据类型，取值。   - 合同 - 合同订单 - 店面单 |
| ht\_title | String | 否 | 主题。 |
| ht\_number | String | 否 | 合同单号。 |
| ht\_lxrid | String | 否 | 对应联系人。 |
| ht\_lxrinfo | String | 否 | 联系方式。 |
| ht\_xshid | String | 否 | 对应机会。 |
| ht\_type | String | 否 | 自定义分类。 |
| ht\_paymode | String | 否 | 付款方式。 |
| ht\_begindate | String | 否 | 开始日期。 |
| ht\_cusub | String | 否 | 客户签约人。 |
| ht\_wesub | String | 否 | 我方签约人。 |
| ht\_moneyzhekou | String | 否 | 优惠折扣率。 |
| ht\_kjmoney | String | 否 | 优惠抹零金额。 |
| ht\_fjmoneylx | String | 否 | 附加费用分类。 |
| ht\_fjmoney | String | 否 | 附加费用金额。 |
| ht\_summemo | String | 否 | 外币备注。 |
| ht\_deliplace | String | 否 | 交付地点。 |
| ht\_enddate | String | 否 | 最晚发货日。 |
| ht\_wuliutype | String | 否 | 发货方式。 |
| ht\_yunfeimoney | String | 否 | 预计运费。 |
| fahuoaddressid | String | 否 | 收货地址。 |
| ht\_contract | String | 否 | 合同正文。 |
| ht\_remark | String | 否 | 备注。 |
| child\_mx | String | 否 | 产品明细，json格式。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/orders HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:5ff89xxx
Content-Type:application/json

{
  "datatype" : 150,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "ht_customerid" : "客户1",
    "ht_date" : "2021-6-1",
    "ht_preside" : "李四",
    "ht_state" : "执行中",
    "ht_summoney" : "10000",
    "ht_order" : "合同",
    "ht_title" : "主体",
    "ht_number" : "DD798686767",
    "ht_lxrid" : "王五",
    "ht_lxrinfo" : "13989568656",
    "ht_xshid" : "对应机会",
    "ht_type" : "主营产品销售",
    "ht_paymode" : "微信",
    "ht_begindate" : "2021-6-1",
    "ht_cusub" : "孙大力",
    "ht_wesub" : "张大山",
    "ht_moneyzhekou" : "12",
    "ht_kjmoney" : "14",
    "ht_fjmoneylx" : "运费",
    "ht_fjmoney" : "10",
    "ht_summemo" : "外币备注",
    "ht_deliplace" : "交付地点",
    "ht_enddate" : "2021-6-2",
    "ht_wuliutype" : "顺丰快递",
    "ht_yunfeimoney" : "10",
    "fahuoaddressid" : "山西省大同市",
    "ht_contract" : "合同正文",
    "ht_remark" : "备注",
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
        EditOrderHeaders editOrderHeaders = new EditOrderHeaders();
        editOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditOrderRequest.EditOrderRequestData data = new EditOrderRequest.EditOrderRequestData()
                .setDataUserid("张三")
                .setHtCustomerid("客户1")
                .setHtDate("2021-6-1")
                .setHtPreside("李四")
                .setHtState("执行中")
                .setHtSummoney("10000")
                .setHtOrder("合同")
                .setHtTitle("主体")
                .setHtNumber("DD798686767")
                .setHtLxrid("王五")
                .setHtLxrinfo("13989568656")
                .setHtXshid("对应机会")
                .setHtType("主营产品销售")
                .setHtPaymode("微信")
                .setHtBegindate("2021-6-1")
                .setHtCusub("孙大力")
                .setHtWesub("张大山")
                .setHtMoneyzhekou("12")
                .setHtKjmoney("14")
                .setHtFjmoneylx("运费")
                .setHtFjmoney("10")
                .setHtSummemo("外币备注")
                .setHtDeliplace("交付地点")
                .setHtEnddate("2021-6-2")
                .setHtWuliutype("顺丰快递")
                .setHtYunfeimoney("10")
                .setFahuoaddressid("山西省大同市")
                .setHtContract("合同正文")
                .setHtRemark("备注")
                .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
        EditOrderRequest editOrderRequest = new EditOrderRequest()
                .setDatatype(150L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editOrderWithOptions(editOrderRequest, editOrderHeaders, new RuntimeOptions());
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
        edit_order_headers = dingtalkjzcrm__1__0_models.EditOrderHeaders()
        edit_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditOrderRequestData(
            data_userid='张三',
            ht_customerid='客户1',
            ht_date='2021-6-1',
            ht_preside='李四',
            ht_state='执行中',
            ht_summoney='10000',
            ht_order='合同',
            ht_title='主体',
            ht_number='DD798686767',
            ht_lxrid='王五',
            ht_lxrinfo='13989568656',
            ht_xshid='对应机会',
            ht_type='主营产品销售',
            ht_paymode='微信',
            ht_begindate='2021-6-1',
            ht_cusub='孙大力',
            ht_wesub='张大山',
            ht_moneyzhekou='12',
            ht_kjmoney='14',
            ht_fjmoneylx='运费',
            ht_fjmoney='10',
            ht_summemo='外币备注',
            ht_deliplace='交付地点',
            ht_enddate='2021-6-2',
            ht_wuliutype='顺丰快递',
            ht_yunfeimoney='10',
            fahuoaddressid='山西省大同市',
            ht_contract='合同正文',
            ht_remark='备注',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_order_request = dingtalkjzcrm__1__0_models.EditOrderRequest(
            datatype=150,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_order_with_options(edit_order_request, edit_order_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_order_headers = dingtalkjzcrm__1__0_models.EditOrderHeaders()
        edit_order_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditOrderRequestData(
            data_userid='张三',
            ht_customerid='客户1',
            ht_date='2021-6-1',
            ht_preside='李四',
            ht_state='执行中',
            ht_summoney='10000',
            ht_order='合同',
            ht_title='主体',
            ht_number='DD798686767',
            ht_lxrid='王五',
            ht_lxrinfo='13989568656',
            ht_xshid='对应机会',
            ht_type='主营产品销售',
            ht_paymode='微信',
            ht_begindate='2021-6-1',
            ht_cusub='孙大力',
            ht_wesub='张大山',
            ht_moneyzhekou='12',
            ht_kjmoney='14',
            ht_fjmoneylx='运费',
            ht_fjmoney='10',
            ht_summemo='外币备注',
            ht_deliplace='交付地点',
            ht_enddate='2021-6-2',
            ht_wuliutype='顺丰快递',
            ht_yunfeimoney='10',
            fahuoaddressid='山西省大同市',
            ht_contract='合同正文',
            ht_remark='备注',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_order_request = dingtalkjzcrm__1__0_models.EditOrderRequest(
            datatype=150,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_order_with_options_async(edit_order_request, edit_order_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditOrderHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditOrderRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditOrderRequest;
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
        $editOrderHeaders = new EditOrderHeaders([]);
        $editOrderHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "htCustomerid" => "客户1",
            "htDate" => "2021-6-1",
            "htPreside" => "李四",
            "htState" => "执行中",
            "htSummoney" => "10000",
            "htOrder" => "合同",
            "htTitle" => "主体",
            "htNumber" => "DD798686767",
            "htLxrid" => "王五",
            "htLxrinfo" => "13989568656",
            "htXshid" => "对应机会",
            "htType" => "主营产品销售",
            "htPaymode" => "微信",
            "htBegindate" => "2021-6-1",
            "htCusub" => "孙大力",
            "htWesub" => "张大山",
            "htMoneyzhekou" => "12",
            "htKjmoney" => "14",
            "htFjmoneylx" => "运费",
            "htFjmoney" => "10",
            "htSummemo" => "外币备注",
            "htDeliplace" => "交付地点",
            "htEnddate" => "2021-6-2",
            "htWuliutype" => "顺丰快递",
            "htYunfeimoney" => "10",
            "fahuoaddressid" => "山西省大同市",
            "htContract" => "合同正文",
            "htRemark" => "备注",
            "childMx" => "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
        ]);
        $editOrderRequest = new EditOrderRequest([
            "datatype" => 150,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editOrderWithOptions($editOrderRequest, $editOrderHeaders, new RuntimeOptions([]));
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

  editOrderHeaders := &dingtalkjzcrm_1_0.EditOrderHeaders{}
  editOrderHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditOrderRequestData{
    DataUserid: tea.String("张三"),
    HtCustomerid: tea.String("客户1"),
    HtDate: tea.String("2021-6-1"),
    HtPreside: tea.String("李四"),
    HtState: tea.String("执行中"),
    HtSummoney: tea.String("10000"),
    HtOrder: tea.String("合同"),
    HtTitle: tea.String("主体"),
    HtNumber: tea.String("DD798686767"),
    HtLxrid: tea.String("王五"),
    HtLxrinfo: tea.String("13989568656"),
    HtXshid: tea.String("对应机会"),
    HtType: tea.String("主营产品销售"),
    HtPaymode: tea.String("微信"),
    HtBegindate: tea.String("2021-6-1"),
    HtCusub: tea.String("孙大力"),
    HtWesub: tea.String("张大山"),
    HtMoneyzhekou: tea.String("12"),
    HtKjmoney: tea.String("14"),
    HtFjmoneylx: tea.String("运费"),
    HtFjmoney: tea.String("10"),
    HtSummemo: tea.String("外币备注"),
    HtDeliplace: tea.String("交付地点"),
    HtEnddate: tea.String("2021-6-2"),
    HtWuliutype: tea.String("顺丰快递"),
    HtYunfeimoney: tea.String("10"),
    Fahuoaddressid: tea.String("山西省大同市"),
    HtContract: tea.String("合同正文"),
    HtRemark: tea.String("备注"),
    ChildMx: tea.String("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"),
  }
  editOrderRequest := &dingtalkjzcrm_1_0.EditOrderRequest{
    Datatype: tea.Int64(150),
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
    _, _err = client.EditOrderWithOptions(editOrderRequest, editOrderHeaders, &util.RuntimeOptions{})
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
    let editOrderHeaders = new $dingtalkjzcrm_1_0.EditOrderHeaders({ });
    editOrderHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditOrderRequestData({
      dataUserid: "张三",
      htCustomerid: "客户1",
      htDate: "2021-6-1",
      htPreside: "李四",
      htState: "执行中",
      htSummoney: "10000",
      htOrder: "合同",
      htTitle: "主体",
      htNumber: "DD798686767",
      htLxrid: "王五",
      htLxrinfo: "13989568656",
      htXshid: "对应机会",
      htType: "主营产品销售",
      htPaymode: "微信",
      htBegindate: "2021-6-1",
      htCusub: "孙大力",
      htWesub: "张大山",
      htMoneyzhekou: "12",
      htKjmoney: "14",
      htFjmoneylx: "运费",
      htFjmoney: "10",
      htSummemo: "外币备注",
      htDeliplace: "交付地点",
      htEnddate: "2021-6-2",
      htWuliutype: "顺丰快递",
      htYunfeimoney: "10",
      fahuoaddressid: "山西省大同市",
      htContract: "合同正文",
      htRemark: "备注",
      childMx: "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
    });
    let editOrderRequest = new $dingtalkjzcrm_1_0.EditOrderRequest({
      datatype: 150,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editOrderWithOptions(editOrderRequest, editOrderHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditOrderHeaders editOrderHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditOrderHeaders();
            editOrderHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditOrderRequest.EditOrderRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditOrderRequest.EditOrderRequestData
            {
                DataUserid = "张三",
                HtCustomerid = "客户1",
                HtDate = "2021-6-1",
                HtPreside = "李四",
                HtState = "执行中",
                HtSummoney = "10000",
                HtOrder = "合同",
                HtTitle = "主体",
                HtNumber = "DD798686767",
                HtLxrid = "王五",
                HtLxrinfo = "13989568656",
                HtXshid = "对应机会",
                HtType = "主营产品销售",
                HtPaymode = "微信",
                HtBegindate = "2021-6-1",
                HtCusub = "孙大力",
                HtWesub = "张大山",
                HtMoneyzhekou = "12",
                HtKjmoney = "14",
                HtFjmoneylx = "运费",
                HtFjmoney = "10",
                HtSummemo = "外币备注",
                HtDeliplace = "交付地点",
                HtEnddate = "2021-6-2",
                HtWuliutype = "顺丰快递",
                HtYunfeimoney = "10",
                Fahuoaddressid = "山西省大同市",
                HtContract = "合同正文",
                HtRemark = "备注",
                ChildMx = "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditOrderRequest editOrderRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditOrderRequest
            {
                Datatype = 150,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditOrderWithOptions(editOrderRequest, editOrderHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditOrderHeaders> editOrderHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditOrderHeaders>();
  editOrderHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditOrderRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditOrderRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"htCustomerid", boost::any(string("客户1"))},
    {"htDate", boost::any(string("2021-6-1"))},
    {"htPreside", boost::any(string("李四"))},
    {"htState", boost::any(string("执行中"))},
    {"htSummoney", boost::any(string("10000"))},
    {"htOrder", boost::any(string("合同"))},
    {"htTitle", boost::any(string("主体"))},
    {"htNumber", boost::any(string("DD798686767"))},
    {"htLxrid", boost::any(string("王五"))},
    {"htLxrinfo", boost::any(string("13989568656"))},
    {"htXshid", boost::any(string("对应机会"))},
    {"htType", boost::any(string("主营产品销售"))},
    {"htPaymode", boost::any(string("微信"))},
    {"htBegindate", boost::any(string("2021-6-1"))},
    {"htCusub", boost::any(string("孙大力"))},
    {"htWesub", boost::any(string("张大山"))},
    {"htMoneyzhekou", boost::any(string("12"))},
    {"htKjmoney", boost::any(string("14"))},
    {"htFjmoneylx", boost::any(string("运费"))},
    {"htFjmoney", boost::any(string("10"))},
    {"htSummemo", boost::any(string("外币备注"))},
    {"htDeliplace", boost::any(string("交付地点"))},
    {"htEnddate", boost::any(string("2021-6-2"))},
    {"htWuliutype", boost::any(string("顺丰快递"))},
    {"htYunfeimoney", boost::any(string("10"))},
    {"fahuoaddressid", boost::any(string("山西省大同市"))},
    {"htContract", boost::any(string("合同正文"))},
    {"htRemark", boost::any(string("备注"))},
    {"childMx", boost::any(string(""child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditOrderRequest> editOrderRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditOrderRequest>(map<string, boost::any>({
    {"datatype", boost::any(150)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editOrderWithOptions(editOrderRequest, editOrderHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
