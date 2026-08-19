---
title: "销售换货单"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-a-sales-order"
namespace: "development"
slug: "add-or-edit-a-sales-order"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 合同 > 销售换货单"
doc_id: "OhKCRb6tEN"
updated_at: "2026-01-29 14:19:35"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-a-sales-order
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 合同 > 销售换货单
> Updated: 2026-01-29 14:19:35

# 销售换货单

通过此接口新增或编辑销售换货单据。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/exchanges |
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
| datatype | Long | 是 | 数据类型，固定值**228**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| hh\_inlibid | String | 是 | 换入仓库。 |
| hh\_outlibid | String | 是 | 换出仓库。 |
| hh\_title | String | 是 | 主题。 |
| hh\_number | String | 是 | 换货单号。 |
| hh\_customerid | String | 否 | 对应客户。 |
| hh\_orderid | String | 否 | 取值。   - 合同ID或名称 - 订单ID或名称。 |
| hh\_type | String | 否 | 分类。 |
| hh\_date | String | 否 | 换货日期。 |
| hh\_inempid | String | 否 | 换入操作员。 |
| hh\_intime | String | 否 | 换入时间。 |
| hh\_outempid | String | 否 | 换出操作员。 |
| hh\_outtime | String | 否 | 换出时间。 |
| hh\_remark | String | 否 | 备注。 |
| hh\_state | String | 否 | 状态，取值。   - 未执行 - 已入待出 - 已出待入 - 结束 |
| child\_mx | String | 否 | 产品明细，json格式。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/exchanges HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:15996xxx
Content-Type:application/json

{
  "datatype" : 228,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "hh_inlibid" : "总仓库",
    "hh_outlibid" : "德克萨斯州仓库",
    "hh_title" : "笔记本换货",
    "hh_number" : "1000001",
    "hh_customerid" : "xx科技有限公司",
    "hh_orderid" : "购买两台笔记本",
    "hh_type" : "销售换货",
    "hh_date" : "2021-06-01",
    "hh_inempid" : "李四",
    "hh_intime" : "2021-06-01",
    "hh_outempid" : "王五",
    "hh_outtime" : "2021-06-01",
    "hh_remark" : "已更换",
    "hh_state" : "结束",
    "child_mx" : "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"明细备注\":\"包含的测试产品\",\"序列号-换入\":\"• in1001• in1002...无则不传递\",\"批次号-换入\":\"• in2001 (10)• in2002 (20)...无则不传递\",\"序列号-换出\":\"• out1001• out1002...无则不传递\",\"批次号-换出\":\"• out2001 (10)• out2002 (20)...无则不传递\"}]"
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
        EditExchangeHeaders editExchangeHeaders = new EditExchangeHeaders();
        editExchangeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditExchangeRequest.EditExchangeRequestData data = new EditExchangeRequest.EditExchangeRequestData()
                .setDataUserid("张三")
                .setHhInlibid("总仓库")
                .setHhOutlibid("德克萨斯州仓库")
                .setHhTitle("笔记本换货")
                .setHhNumber("1000001")
                .setHhCustomerid("xx科技有限公司")
                .setHhOrderid("购买两台笔记本")
                .setHhType("销售换货")
                .setHhDate("2021-06-01")
                .setHhInempid("李四")
                .setHhIntime("2021-06-01")
                .setHhOutempid("王五")
                .setHhOuttime("2021-06-01")
                .setHhRemark("已更换")
                .setHhState("结束")
                .setChildMx("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"明细备注\":\"包含的测试产品\",\"序列号-换入\":\"• in1001• in1002...无则不传递\",\"批次号-换入\":\"• in2001 (10)• in2002 (20)...无则不传递\",\"序列号-换出\":\"• out1001• out1002...无则不传递\",\"批次号-换出\":\"• out2001 (10)• out2002 (20)...无则不传递\"}]");
        EditExchangeRequest editExchangeRequest = new EditExchangeRequest()
                .setDatatype(228L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editExchangeWithOptions(editExchangeRequest, editExchangeHeaders, new RuntimeOptions());
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
        edit_exchange_headers = dingtalkjzcrm__1__0_models.EditExchangeHeaders()
        edit_exchange_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditExchangeRequestData(
            data_userid='张三',
            hh_inlibid='总仓库',
            hh_outlibid='德克萨斯州仓库',
            hh_title='笔记本换货',
            hh_number='1000001',
            hh_customerid='xx科技有限公司',
            hh_orderid='购买两台笔记本',
            hh_type='销售换货',
            hh_date='2021-06-01',
            hh_inempid='李四',
            hh_intime='2021-06-01',
            hh_outempid='王五',
            hh_outtime='2021-06-01',
            hh_remark='已更换',
            hh_state='结束',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","明细备注":"包含的测试产品","序列号-换入":"• in1001• in1002...无则不传递","批次号-换入":"• in2001 (10)• in2002 (20)...无则不传递","序列号-换出":"• out1001• out1002...无则不传递","批次号-换出":"• out2001 (10)• out2002 (20)...无则不传递"}]'
        )
        edit_exchange_request = dingtalkjzcrm__1__0_models.EditExchangeRequest(
            datatype=228,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_exchange_with_options(edit_exchange_request, edit_exchange_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_exchange_headers = dingtalkjzcrm__1__0_models.EditExchangeHeaders()
        edit_exchange_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditExchangeRequestData(
            data_userid='张三',
            hh_inlibid='总仓库',
            hh_outlibid='德克萨斯州仓库',
            hh_title='笔记本换货',
            hh_number='1000001',
            hh_customerid='xx科技有限公司',
            hh_orderid='购买两台笔记本',
            hh_type='销售换货',
            hh_date='2021-06-01',
            hh_inempid='李四',
            hh_intime='2021-06-01',
            hh_outempid='王五',
            hh_outtime='2021-06-01',
            hh_remark='已更换',
            hh_state='结束',
            child_mx='"child_mx":[{"产品ID":"1","数量":"10","明细备注":"包含的测试产品","序列号-换入":"• in1001• in1002...无则不传递","批次号-换入":"• in2001 (10)• in2002 (20)...无则不传递","序列号-换出":"• out1001• out1002...无则不传递","批次号-换出":"• out2001 (10)• out2002 (20)...无则不传递"}]'
        )
        edit_exchange_request = dingtalkjzcrm__1__0_models.EditExchangeRequest(
            datatype=228,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_exchange_with_options_async(edit_exchange_request, edit_exchange_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditExchangeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditExchangeRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditExchangeRequest;
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
        $editExchangeHeaders = new EditExchangeHeaders([]);
        $editExchangeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "hhInlibid" => "总仓库",
            "hhOutlibid" => "德克萨斯州仓库",
            "hhTitle" => "笔记本换货",
            "hhNumber" => "1000001",
            "hhCustomerid" => "xx科技有限公司",
            "hhOrderid" => "购买两台笔记本",
            "hhType" => "销售换货",
            "hhDate" => "2021-06-01",
            "hhInempid" => "李四",
            "hhIntime" => "2021-06-01",
            "hhOutempid" => "王五",
            "hhOuttime" => "2021-06-01",
            "hhRemark" => "已更换",
            "hhState" => "结束",
            "childMx" => "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"明细备注\":\"包含的测试产品\",\"序列号-换入\":\"• in1001• in1002...无则不传递\",\"批次号-换入\":\"• in2001 (10)• in2002 (20)...无则不传递\",\"序列号-换出\":\"• out1001• out1002...无则不传递\",\"批次号-换出\":\"• out2001 (10)• out2002 (20)...无则不传递\"}]"
        ]);
        $editExchangeRequest = new EditExchangeRequest([
            "datatype" => 228,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editExchangeWithOptions($editExchangeRequest, $editExchangeHeaders, new RuntimeOptions([]));
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

  editExchangeHeaders := &dingtalkjzcrm_1_0.EditExchangeHeaders{}
  editExchangeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditExchangeRequestData{
    DataUserid: tea.String("张三"),
    HhInlibid: tea.String("总仓库"),
    HhOutlibid: tea.String("德克萨斯州仓库"),
    HhTitle: tea.String("笔记本换货"),
    HhNumber: tea.String("1000001"),
    HhCustomerid: tea.String("xx科技有限公司"),
    HhOrderid: tea.String("购买两台笔记本"),
    HhType: tea.String("销售换货"),
    HhDate: tea.String("2021-06-01"),
    HhInempid: tea.String("李四"),
    HhIntime: tea.String("2021-06-01"),
    HhOutempid: tea.String("王五"),
    HhOuttime: tea.String("2021-06-01"),
    HhRemark: tea.String("已更换"),
    HhState: tea.String("结束"),
    ChildMx: tea.String("\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"明细备注\":\"包含的测试产品\",\"序列号-换入\":\"• in1001• in1002...无则不传递\",\"批次号-换入\":\"• in2001 (10)• in2002 (20)...无则不传递\",\"序列号-换出\":\"• out1001• out1002...无则不传递\",\"批次号-换出\":\"• out2001 (10)• out2002 (20)...无则不传递\"}]"),
  }
  editExchangeRequest := &dingtalkjzcrm_1_0.EditExchangeRequest{
    Datatype: tea.Int64(228),
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
    _, _err = client.EditExchangeWithOptions(editExchangeRequest, editExchangeHeaders, &util.RuntimeOptions{})
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
    let editExchangeHeaders = new $dingtalkjzcrm_1_0.EditExchangeHeaders({ });
    editExchangeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditExchangeRequestData({
      dataUserid: "张三",
      hhInlibid: "总仓库",
      hhOutlibid: "德克萨斯州仓库",
      hhTitle: "笔记本换货",
      hhNumber: "1000001",
      hhCustomerid: "xx科技有限公司",
      hhOrderid: "购买两台笔记本",
      hhType: "销售换货",
      hhDate: "2021-06-01",
      hhInempid: "李四",
      hhIntime: "2021-06-01",
      hhOutempid: "王五",
      hhOuttime: "2021-06-01",
      hhRemark: "已更换",
      hhState: "结束",
      childMx: "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"明细备注\":\"包含的测试产品\",\"序列号-换入\":\"• in1001• in1002...无则不传递\",\"批次号-换入\":\"• in2001 (10)• in2002 (20)...无则不传递\",\"序列号-换出\":\"• out1001• out1002...无则不传递\",\"批次号-换出\":\"• out2001 (10)• out2002 (20)...无则不传递\"}]",
    });
    let editExchangeRequest = new $dingtalkjzcrm_1_0.EditExchangeRequest({
      datatype: 228,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editExchangeWithOptions(editExchangeRequest, editExchangeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditExchangeHeaders editExchangeHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditExchangeHeaders();
            editExchangeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditExchangeRequest.EditExchangeRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditExchangeRequest.EditExchangeRequestData
            {
                DataUserid = "张三",
                HhInlibid = "总仓库",
                HhOutlibid = "德克萨斯州仓库",
                HhTitle = "笔记本换货",
                HhNumber = "1000001",
                HhCustomerid = "xx科技有限公司",
                HhOrderid = "购买两台笔记本",
                HhType = "销售换货",
                HhDate = "2021-06-01",
                HhInempid = "李四",
                HhIntime = "2021-06-01",
                HhOutempid = "王五",
                HhOuttime = "2021-06-01",
                HhRemark = "已更换",
                HhState = "结束",
                ChildMx = "\"child_mx\":[{\"产品ID\":\"1\",\"数量\":\"10\",\"明细备注\":\"包含的测试产品\",\"序列号-换入\":\"• in1001• in1002...无则不传递\",\"批次号-换入\":\"• in2001 (10)• in2002 (20)...无则不传递\",\"序列号-换出\":\"• out1001• out1002...无则不传递\",\"批次号-换出\":\"• out2001 (10)• out2002 (20)...无则不传递\"}]",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditExchangeRequest editExchangeRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditExchangeRequest
            {
                Datatype = 228,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditExchangeWithOptions(editExchangeRequest, editExchangeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditExchangeHeaders> editExchangeHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditExchangeHeaders>();
  editExchangeHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditExchangeRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditExchangeRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"hhInlibid", boost::any(string("总仓库"))},
    {"hhOutlibid", boost::any(string("德克萨斯州仓库"))},
    {"hhTitle", boost::any(string("笔记本换货"))},
    {"hhNumber", boost::any(string("1000001"))},
    {"hhCustomerid", boost::any(string("xx科技有限公司"))},
    {"hhOrderid", boost::any(string("购买两台笔记本"))},
    {"hhType", boost::any(string("销售换货"))},
    {"hhDate", boost::any(string("2021-06-01"))},
    {"hhInempid", boost::any(string("李四"))},
    {"hhIntime", boost::any(string("2021-06-01"))},
    {"hhOutempid", boost::any(string("王五"))},
    {"hhOuttime", boost::any(string("2021-06-01"))},
    {"hhRemark", boost::any(string("已更换"))},
    {"hhState", boost::any(string("结束"))},
    {"childMx", boost::any(string(""child_mx":[{"产品ID":"1","数量":"10","明细备注":"包含的测试产品","序列号-换入":"• in1001• in1002...无则不传递","批次号-换入":"• in2001 (10)• in2002 (20)...无则不传递","序列号-换出":"• out1001• out1002...无则不传递","批次号-换出":"• out2001 (10)• out2002 (20)...无则不传递"}]"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditExchangeRequest> editExchangeRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditExchangeRequest>(map<string, boost::any>({
    {"datatype", boost::any(228)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editExchangeWithOptions(editExchangeRequest, editExchangeHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
