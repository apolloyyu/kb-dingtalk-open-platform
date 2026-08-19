---
title: "报价记录"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-quotation-records"
namespace: "development"
slug: "add-or-edit-quotation-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 销售 > 报价记录"
doc_id: "zOdbQl1xm9"
updated_at: "2026-01-29 14:19:36"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-quotation-records
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 销售 > 报价记录
> Updated: 2026-01-29 14:19:36

# 报价记录

通过此接口新增或编辑报价记录。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/quotationRecords |
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
| datatype | Long | 是 | 数据类型，固定值**161**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。      值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| bj\_customerid | String | 是 | 对应客户。 |
| bj\_bjren | String | 是 | 报价人。 |
| bj\_date | String | 是 | 报价日期。 |
| bj\_price | String | 是 | 报价（总）。 |
| bj\_title | String | 否 | 主题。 |
| bj\_number | String | 否 | 报价单号。 |
| bj\_state | String | 否 | 转成订单。 |
| bj\_jshren | String | 否 | 接收人。 |
| bj\_lianxi | String | 否 | 联系方式。 |
| bj\_xshid | String | 否 | 对应机会。 |
| bj\_moneyzhekou | String | 否 | 优惠折扣率。 |
| bj\_kjmoney | String | 否 | 优惠抹零金额。 |
| bj\_fjmoneylx | String | 否 | 附加费用分类。 |
| bj\_fjmoney | String | 否 | 附加费用金额。 |
| bj\_jfremark | String | 否 | 交付说明。 |
| bj\_fkremark | String | 否 | 付款说明。 |
| bj\_bzremark | String | 否 | 包装运输。 |
| bj\_remark | String | 否 | 备注。 |
| child\_mx | String | 否 | 产品明细，json格式。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/quotationRecords HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961xxx
Content-Type:application/json

{
  "datatype" : 161,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "bj_customerid" : "金智电子科技有限公司",
    "bj_bjren" : "张三",
    "bj_date" : "2021-06-01",
    "bj_price" : "99",
    "bj_title" : "购买可爱多",
    "bj_number" : "1000001",
    "bj_state" : "允许",
    "bj_jshren" : "王五",
    "bj_lianxi" : "16688889999",
    "bj_xshid" : "存在购买意向",
    "bj_moneyzhekou" : "50%",
    "bj_kjmoney" : "20",
    "bj_fjmoneylx" : "运费",
    "bj_fjmoney" : "300",
    "bj_jfremark" : "暂未交付",
    "bj_fkremark" : "已付款",
    "bj_bzremark" : "滴滴到家",
    "bj_remark" : "该报价无问题",
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
        EditQuotationRecordHeaders editQuotationRecordHeaders = new EditQuotationRecordHeaders();
        editQuotationRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditQuotationRecordRequest.EditQuotationRecordRequestData data = new EditQuotationRecordRequest.EditQuotationRecordRequestData()
                .setDataUserid("张三")
                .setBjCustomerid("金智电子科技有限公司")
                .setBjBjren("张三")
                .setBjDate("2021-06-01")
                .setBjPrice("99")
                .setBjTitle("购买可爱多")
                .setBjNumber("1000001")
                .setBjState("允许")
                .setBjJshren("王五")
                .setBjLianxi("16688889999")
                .setBjXshid("存在购买意向")
                .setBjMoneyzhekou("50%")
                .setBjKjmoney("20")
                .setBjFjmoneylx("运费")
                .setBjFjmoney("300")
                .setBjJfremark("暂未交付")
                .setBjFkremark("已付款")
                .setBjBzremark("滴滴到家")
                .setBjRemark("该报价无问题")
                .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]");
        EditQuotationRecordRequest editQuotationRecordRequest = new EditQuotationRecordRequest()
                .setDatatype(161L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editQuotationRecordWithOptions(editQuotationRecordRequest, editQuotationRecordHeaders, new RuntimeOptions());
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
        edit_quotation_record_headers = dingtalkjzcrm__1__0_models.EditQuotationRecordHeaders()
        edit_quotation_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditQuotationRecordRequestData(
            data_userid='张三',
            bj_customerid='金智电子科技有限公司',
            bj_bjren='张三',
            bj_date='2021-06-01',
            bj_price='99',
            bj_title='购买可爱多',
            bj_number='1000001',
            bj_state='允许',
            bj_jshren='王五',
            bj_lianxi='16688889999',
            bj_xshid='存在购买意向',
            bj_moneyzhekou='50%',
            bj_kjmoney='20',
            bj_fjmoneylx='运费',
            bj_fjmoney='300',
            bj_jfremark='暂未交付',
            bj_fkremark='已付款',
            bj_bzremark='滴滴到家',
            bj_remark='该报价无问题',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_quotation_record_request = dingtalkjzcrm__1__0_models.EditQuotationRecordRequest(
            datatype=161,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_quotation_record_with_options(edit_quotation_record_request, edit_quotation_record_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_quotation_record_headers = dingtalkjzcrm__1__0_models.EditQuotationRecordHeaders()
        edit_quotation_record_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditQuotationRecordRequestData(
            data_userid='张三',
            bj_customerid='金智电子科技有限公司',
            bj_bjren='张三',
            bj_date='2021-06-01',
            bj_price='99',
            bj_title='购买可爱多',
            bj_number='1000001',
            bj_state='允许',
            bj_jshren='王五',
            bj_lianxi='16688889999',
            bj_xshid='存在购买意向',
            bj_moneyzhekou='50%',
            bj_kjmoney='20',
            bj_fjmoneylx='运费',
            bj_fjmoney='300',
            bj_jfremark='暂未交付',
            bj_fkremark='已付款',
            bj_bzremark='滴滴到家',
            bj_remark='该报价无问题',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]'
        )
        edit_quotation_record_request = dingtalkjzcrm__1__0_models.EditQuotationRecordRequest(
            datatype=161,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_quotation_record_with_options_async(edit_quotation_record_request, edit_quotation_record_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditQuotationRecordHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditQuotationRecordRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditQuotationRecordRequest;
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
        $editQuotationRecordHeaders = new EditQuotationRecordHeaders([]);
        $editQuotationRecordHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "bjCustomerid" => "金智电子科技有限公司",
            "bjBjren" => "张三",
            "bjDate" => "2021-06-01",
            "bjPrice" => "99",
            "bjTitle" => "购买可爱多",
            "bjNumber" => "1000001",
            "bjState" => "允许",
            "bjJshren" => "王五",
            "bjLianxi" => "16688889999",
            "bjXshid" => "存在购买意向",
            "bjMoneyzhekou" => "50%",
            "bjKjmoney" => "20",
            "bjFjmoneylx" => "运费",
            "bjFjmoney" => "300",
            "bjJfremark" => "暂未交付",
            "bjFkremark" => "已付款",
            "bjBzremark" => "滴滴到家",
            "bjRemark" => "该报价无问题",
            "childMx" => "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"
        ]);
        $editQuotationRecordRequest = new EditQuotationRecordRequest([
            "datatype" => 161,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editQuotationRecordWithOptions($editQuotationRecordRequest, $editQuotationRecordHeaders, new RuntimeOptions([]));
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

  editQuotationRecordHeaders := &dingtalkjzcrm_1_0.EditQuotationRecordHeaders{}
  editQuotationRecordHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditQuotationRecordRequestData{
    DataUserid: tea.String("张三"),
    BjCustomerid: tea.String("金智电子科技有限公司"),
    BjBjren: tea.String("张三"),
    BjDate: tea.String("2021-06-01"),
    BjPrice: tea.String("99"),
    BjTitle: tea.String("购买可爱多"),
    BjNumber: tea.String("1000001"),
    BjState: tea.String("允许"),
    BjJshren: tea.String("王五"),
    BjLianxi: tea.String("16688889999"),
    BjXshid: tea.String("存在购买意向"),
    BjMoneyzhekou: tea.String("50%"),
    BjKjmoney: tea.String("20"),
    BjFjmoneylx: tea.String("运费"),
    BjFjmoney: tea.String("300"),
    BjJfremark: tea.String("暂未交付"),
    BjFkremark: tea.String("已付款"),
    BjBzremark: tea.String("滴滴到家"),
    BjRemark: tea.String("该报价无问题"),
    ChildMx: tea.String("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]"),
  }
  editQuotationRecordRequest := &dingtalkjzcrm_1_0.EditQuotationRecordRequest{
    Datatype: tea.Int64(161),
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
    _, _err = client.EditQuotationRecordWithOptions(editQuotationRecordRequest, editQuotationRecordHeaders, &util.RuntimeOptions{})
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
    let editQuotationRecordHeaders = new $dingtalkjzcrm_1_0.EditQuotationRecordHeaders({ });
    editQuotationRecordHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditQuotationRecordRequestData({
      dataUserid: "张三",
      bjCustomerid: "金智电子科技有限公司",
      bjBjren: "张三",
      bjDate: "2021-06-01",
      bjPrice: "99",
      bjTitle: "购买可爱多",
      bjNumber: "1000001",
      bjState: "允许",
      bjJshren: "王五",
      bjLianxi: "16688889999",
      bjXshid: "存在购买意向",
      bjMoneyzhekou: "50%",
      bjKjmoney: "20",
      bjFjmoneylx: "运费",
      bjFjmoney: "300",
      bjJfremark: "暂未交付",
      bjFkremark: "已付款",
      bjBzremark: "滴滴到家",
      bjRemark: "该报价无问题",
      childMx: "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
    });
    let editQuotationRecordRequest = new $dingtalkjzcrm_1_0.EditQuotationRecordRequest({
      datatype: 161,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editQuotationRecordWithOptions(editQuotationRecordRequest, editQuotationRecordHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditQuotationRecordHeaders editQuotationRecordHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditQuotationRecordHeaders();
            editQuotationRecordHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditQuotationRecordRequest.EditQuotationRecordRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditQuotationRecordRequest.EditQuotationRecordRequestData
            {
                DataUserid = "张三",
                BjCustomerid = "金智电子科技有限公司",
                BjBjren = "张三",
                BjDate = "2021-06-01",
                BjPrice = "99",
                BjTitle = "购买可爱多",
                BjNumber = "1000001",
                BjState = "允许",
                BjJshren = "王五",
                BjLianxi = "16688889999",
                BjXshid = "存在购买意向",
                BjMoneyzhekou = "50%",
                BjKjmoney = "20",
                BjFjmoneylx = "运费",
                BjFjmoney = "300",
                BjJfremark = "暂未交付",
                BjFkremark = "已付款",
                BjBzremark = "滴滴到家",
                BjRemark = "该报价无问题",
                ChildMx = "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"单价\":\"58.5\",\"总价\":\"585\",\"明细备注\":\"包含的测试产品\"}]",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditQuotationRecordRequest editQuotationRecordRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditQuotationRecordRequest
            {
                Datatype = 161,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditQuotationRecordWithOptions(editQuotationRecordRequest, editQuotationRecordHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditQuotationRecordHeaders> editQuotationRecordHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditQuotationRecordHeaders>();
  editQuotationRecordHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditQuotationRecordRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditQuotationRecordRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"bjCustomerid", boost::any(string("金智电子科技有限公司"))},
    {"bjBjren", boost::any(string("张三"))},
    {"bjDate", boost::any(string("2021-06-01"))},
    {"bjPrice", boost::any(string("99"))},
    {"bjTitle", boost::any(string("购买可爱多"))},
    {"bjNumber", boost::any(string("1000001"))},
    {"bjState", boost::any(string("允许"))},
    {"bjJshren", boost::any(string("王五"))},
    {"bjLianxi", boost::any(string("16688889999"))},
    {"bjXshid", boost::any(string("存在购买意向"))},
    {"bjMoneyzhekou", boost::any(string("50%"))},
    {"bjKjmoney", boost::any(string("20"))},
    {"bjFjmoneylx", boost::any(string("运费"))},
    {"bjFjmoney", boost::any(string("300"))},
    {"bjJfremark", boost::any(string("暂未交付"))},
    {"bjFkremark", boost::any(string("已付款"))},
    {"bjBzremark", boost::any(string("滴滴到家"))},
    {"bjRemark", boost::any(string("该报价无问题"))},
    {"childMx", boost::any(string(""child_mx":[{"产品ID":"1","数量":"10","单价":"58.5","总价":"585","明细备注":"包含的测试产品"}]"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditQuotationRecordRequest> editQuotationRecordRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditQuotationRecordRequest>(map<string, boost::any>({
    {"datatype", boost::any(161)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editQuotationRecordWithOptions(editQuotationRecordRequest, editQuotationRecordHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
  "time" : "2021-06-01 10:43:51",
  "success" : true,
  "errcode" : "0",
  "errmsg" : "",
  "msgid" : "1"
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
