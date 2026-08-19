---
title: "产品信息"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-product-information"
namespace: "development"
slug: "add-or-edit-product-information"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 产品 > 产品信息"
doc_id: "rn6mj1gnwd"
updated_at: "2026-01-29 14:19:38"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-product-information
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 产品 > 产品信息
> Updated: 2026-01-29 14:19:38

# 产品信息

通过此接口新增或编辑金智CRM系统中的产品信息，支持企业内部应用与第三方企业应用的数据同步。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/goods |
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
| datatype | Long | 是 | 数据类型，固定值**154**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| cpname | String | 是 | 产品名称。 |
| cpunit | String | 是 | 产品单位。 |
| unitrate | String | 是 | 单位换算。 |
| cp\_parentid | String | 否 | 基准产品。 |
| cptype | String | 否 | 产品型号。 |
| cpguige | String | 否 | 产品规格。 |
| typeid | String | 否 | 产品类别。 |
| cpno | String | 否 | 产品编号。 |
| isstop | String | 否 | 产品状态，取值。   - 正常 - 停售 - 下架 |
| addedtime | String | 否 | 上架时间。 |
| cparea | String | 否 | 产品产地。 |
| cpbrand | String | 否 | 产品品牌。 |
| cbprice | String | 否 | 成本价格。 |
| issnmanage | String | 否 | 序列号管理，取值。   - 是 - 否 |
| ispicimanage | String | 否 | 批次号管理，取值。   - 是 - 否 |
| gysid | String | 否 | 默认供应商。 |
| cpimg | String | 否 | 产品图片。 |
| cpbarcode | String | 否 | 条形码。 |
| cpweight | String | 否 | 产品重量。 |
| preprice1 | String | 否 | 零售价格。 |
| preprice2 | String | 否 | 预设价格1。 |
| preprice3 | String | 否 | 预设价格2。 |
| preprice4 | String | 否 | 预设价格3。 |
| isstock | String | 否 | 是否算库存，取值。   - 计算 - 不计算 - 计算(按基准规格) |
| stockup | String | 否 | 库存上限。 |
| stockdown | String | 否 | 库存下限。 |
| cpcontent | String | 否 | 产品说明。 |
| cpremark | String | 否 | 产品备注。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/goods HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961xxxx
Content-Type:application/json

{
  "datatype" : 154,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "cpname" : "笔记本电脑",
    "cpunit" : "台",
    "unitrate" : "单位换算",
    "cp_parentid" : "基准产品",
    "cptype" : "S200",
    "cpguige" : "12.5kg/台",
    "typeid" : "电子",
    "cpno" : "CP6877979689",
    "isstop" : "正常",
    "addedtime" : "2021-06-01",
    "cparea" : "西北",
    "cpbrand" : "华为",
    "cbprice" : "109999",
    "issnmanage" : "是",
    "ispicimanage" : "是",
    "gysid" : "华为",
    "cpimg" : "产品图片链接",
    "cpbarcode" : "234234453452",
    "cpweight" : "12.5kg",
    "preprice1" : "209999",
    "preprice2" : "209999",
    "preprice3" : "209999",
    "preprice4" : "209999",
    "isstock" : "计算(按基准规格)",
    "stockup" : "100",
    "stockdown" : "1",
    "cpcontent" : "产品说明",
    "cpremark" : "产品备注"
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
        EditGoodsHeaders editGoodsHeaders = new EditGoodsHeaders();
        editGoodsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditGoodsRequest.EditGoodsRequestData data = new EditGoodsRequest.EditGoodsRequestData()
                .setDataUserid("张三")
                .setCpname("笔记本电脑")
                .setCpunit("台")
                .setUnitrate("单位换算")
                .setCpParentid("基准产品")
                .setCptype("S200")
                .setCpguige("12.5kg/台")
                .setTypeid("电子")
                .setCpno("CP6877979689")
                .setIsstop("正常")
                .setAddedtime("2021-06-01")
                .setCparea("西北")
                .setCpbrand("华为")
                .setCbprice("109999")
                .setIssnmanage("是")
                .setIspicimanage("是")
                .setGysid("华为")
                .setCpimg("产品图片链接")
                .setCpbarcode("234234453452")
                .setCpweight("12.5kg")
                .setPreprice1("209999")
                .setPreprice2("209999")
                .setPreprice3("209999")
                .setPreprice4("209999")
                .setIsstock("计算(按基准规格)")
                .setStockup("100")
                .setStockdown("1")
                .setCpcontent("产品说明")
                .setCpremark("产品备注");
        EditGoodsRequest editGoodsRequest = new EditGoodsRequest()
                .setDatatype(154L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editGoodsWithOptions(editGoodsRequest, editGoodsHeaders, new RuntimeOptions());
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
        edit_goods_headers = dingtalkjzcrm__1__0_models.EditGoodsHeaders()
        edit_goods_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditGoodsRequestData(
            data_userid='张三',
            cpname='笔记本电脑',
            cpunit='台',
            unitrate='单位换算',
            cp_parentid='基准产品',
            cptype='S200',
            cpguige='12.5kg/台',
            typeid='电子',
            cpno='CP6877979689',
            isstop='正常',
            addedtime='2021-06-01',
            cparea='西北',
            cpbrand='华为',
            cbprice='109999',
            issnmanage='是',
            ispicimanage='是',
            gysid='华为',
            cpimg='产品图片链接',
            cpbarcode='234234453452',
            cpweight='12.5kg',
            preprice_1='209999',
            preprice_2='209999',
            preprice_3='209999',
            preprice_4='209999',
            isstock='计算(按基准规格)',
            stockup='100',
            stockdown='1',
            cpcontent='产品说明',
            cpremark='产品备注'
        )
        edit_goods_request = dingtalkjzcrm__1__0_models.EditGoodsRequest(
            datatype=154,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_goods_with_options(edit_goods_request, edit_goods_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_goods_headers = dingtalkjzcrm__1__0_models.EditGoodsHeaders()
        edit_goods_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditGoodsRequestData(
            data_userid='张三',
            cpname='笔记本电脑',
            cpunit='台',
            unitrate='单位换算',
            cp_parentid='基准产品',
            cptype='S200',
            cpguige='12.5kg/台',
            typeid='电子',
            cpno='CP6877979689',
            isstop='正常',
            addedtime='2021-06-01',
            cparea='西北',
            cpbrand='华为',
            cbprice='109999',
            issnmanage='是',
            ispicimanage='是',
            gysid='华为',
            cpimg='产品图片链接',
            cpbarcode='234234453452',
            cpweight='12.5kg',
            preprice_1='209999',
            preprice_2='209999',
            preprice_3='209999',
            preprice_4='209999',
            isstock='计算(按基准规格)',
            stockup='100',
            stockdown='1',
            cpcontent='产品说明',
            cpremark='产品备注'
        )
        edit_goods_request = dingtalkjzcrm__1__0_models.EditGoodsRequest(
            datatype=154,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_goods_with_options_async(edit_goods_request, edit_goods_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditGoodsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditGoodsRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditGoodsRequest;
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
        $editGoodsHeaders = new EditGoodsHeaders([]);
        $editGoodsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "cpname" => "笔记本电脑",
            "cpunit" => "台",
            "unitrate" => "单位换算",
            "cpParentid" => "基准产品",
            "cptype" => "S200",
            "cpguige" => "12.5kg/台",
            "typeid" => "电子",
            "cpno" => "CP6877979689",
            "isstop" => "正常",
            "addedtime" => "2021-06-01",
            "cparea" => "西北",
            "cpbrand" => "华为",
            "cbprice" => "109999",
            "issnmanage" => "是",
            "ispicimanage" => "是",
            "gysid" => "华为",
            "cpimg" => "产品图片链接",
            "cpbarcode" => "234234453452",
            "cpweight" => "12.5kg",
            "preprice1" => "209999",
            "preprice2" => "209999",
            "preprice3" => "209999",
            "preprice4" => "209999",
            "isstock" => "计算(按基准规格)",
            "stockup" => "100",
            "stockdown" => "1",
            "cpcontent" => "产品说明",
            "cpremark" => "产品备注"
        ]);
        $editGoodsRequest = new EditGoodsRequest([
            "datatype" => 154,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editGoodsWithOptions($editGoodsRequest, $editGoodsHeaders, new RuntimeOptions([]));
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

  editGoodsHeaders := &dingtalkjzcrm_1_0.EditGoodsHeaders{}
  editGoodsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditGoodsRequestData{
    DataUserid: tea.String("张三"),
    Cpname: tea.String("笔记本电脑"),
    Cpunit: tea.String("台"),
    Unitrate: tea.String("单位换算"),
    CpParentid: tea.String("基准产品"),
    Cptype: tea.String("S200"),
    Cpguige: tea.String("12.5kg/台"),
    Typeid: tea.String("电子"),
    Cpno: tea.String("CP6877979689"),
    Isstop: tea.String("正常"),
    Addedtime: tea.String("2021-06-01"),
    Cparea: tea.String("西北"),
    Cpbrand: tea.String("华为"),
    Cbprice: tea.String("109999"),
    Issnmanage: tea.String("是"),
    Ispicimanage: tea.String("是"),
    Gysid: tea.String("华为"),
    Cpimg: tea.String("产品图片链接"),
    Cpbarcode: tea.String("234234453452"),
    Cpweight: tea.String("12.5kg"),
    Preprice1: tea.String("209999"),
    Preprice2: tea.String("209999"),
    Preprice3: tea.String("209999"),
    Preprice4: tea.String("209999"),
    Isstock: tea.String("计算(按基准规格)"),
    Stockup: tea.String("100"),
    Stockdown: tea.String("1"),
    Cpcontent: tea.String("产品说明"),
    Cpremark: tea.String("产品备注"),
  }
  editGoodsRequest := &dingtalkjzcrm_1_0.EditGoodsRequest{
    Datatype: tea.Int64(154),
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
    _, _err = client.EditGoodsWithOptions(editGoodsRequest, editGoodsHeaders, &util.RuntimeOptions{})
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
    let editGoodsHeaders = new $dingtalkjzcrm_1_0.EditGoodsHeaders({ });
    editGoodsHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditGoodsRequestData({
      dataUserid: "张三",
      cpname: "笔记本电脑",
      cpunit: "台",
      unitrate: "单位换算",
      cpParentid: "基准产品",
      cptype: "S200",
      cpguige: "12.5kg/台",
      typeid: "电子",
      cpno: "CP6877979689",
      isstop: "正常",
      addedtime: "2021-06-01",
      cparea: "西北",
      cpbrand: "华为",
      cbprice: "109999",
      issnmanage: "是",
      ispicimanage: "是",
      gysid: "华为",
      cpimg: "产品图片链接",
      cpbarcode: "234234453452",
      cpweight: "12.5kg",
      preprice1: "209999",
      preprice2: "209999",
      preprice3: "209999",
      preprice4: "209999",
      isstock: "计算(按基准规格)",
      stockup: "100",
      stockdown: "1",
      cpcontent: "产品说明",
      cpremark: "产品备注",
    });
    let editGoodsRequest = new $dingtalkjzcrm_1_0.EditGoodsRequest({
      datatype: 154,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editGoodsWithOptions(editGoodsRequest, editGoodsHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditGoodsHeaders editGoodsHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditGoodsHeaders();
            editGoodsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditGoodsRequest.EditGoodsRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditGoodsRequest.EditGoodsRequestData
            {
                DataUserid = "张三",
                Cpname = "笔记本电脑",
                Cpunit = "台",
                Unitrate = "单位换算",
                CpParentid = "基准产品",
                Cptype = "S200",
                Cpguige = "12.5kg/台",
                Typeid = "电子",
                Cpno = "CP6877979689",
                Isstop = "正常",
                Addedtime = "2021-06-01",
                Cparea = "西北",
                Cpbrand = "华为",
                Cbprice = "109999",
                Issnmanage = "是",
                Ispicimanage = "是",
                Gysid = "华为",
                Cpimg = "产品图片链接",
                Cpbarcode = "234234453452",
                Cpweight = "12.5kg",
                Preprice1 = "209999",
                Preprice2 = "209999",
                Preprice3 = "209999",
                Preprice4 = "209999",
                Isstock = "计算(按基准规格)",
                Stockup = "100",
                Stockdown = "1",
                Cpcontent = "产品说明",
                Cpremark = "产品备注",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditGoodsRequest editGoodsRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditGoodsRequest
            {
                Datatype = 154,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditGoodsWithOptions(editGoodsRequest, editGoodsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditGoodsHeaders> editGoodsHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditGoodsHeaders>();
  editGoodsHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditGoodsRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditGoodsRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"cpname", boost::any(string("笔记本电脑"))},
    {"cpunit", boost::any(string("台"))},
    {"unitrate", boost::any(string("单位换算"))},
    {"cpParentid", boost::any(string("基准产品"))},
    {"cptype", boost::any(string("S200"))},
    {"cpguige", boost::any(string("12.5kg/台"))},
    {"typeid", boost::any(string("电子"))},
    {"cpno", boost::any(string("CP6877979689"))},
    {"isstop", boost::any(string("正常"))},
    {"addedtime", boost::any(string("2021-06-01"))},
    {"cparea", boost::any(string("西北"))},
    {"cpbrand", boost::any(string("华为"))},
    {"cbprice", boost::any(string("109999"))},
    {"issnmanage", boost::any(string("是"))},
    {"ispicimanage", boost::any(string("是"))},
    {"gysid", boost::any(string("华为"))},
    {"cpimg", boost::any(string("产品图片链接"))},
    {"cpbarcode", boost::any(string("234234453452"))},
    {"cpweight", boost::any(string("12.5kg"))},
    {"preprice1", boost::any(string("209999"))},
    {"preprice2", boost::any(string("209999"))},
    {"preprice3", boost::any(string("209999"))},
    {"preprice4", boost::any(string("209999"))},
    {"isstock", boost::any(string("计算(按基准规格)"))},
    {"stockup", boost::any(string("100"))},
    {"stockdown", boost::any(string("1"))},
    {"cpcontent", boost::any(string("产品说明"))},
    {"cpremark", boost::any(string("产品备注"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditGoodsRequest> editGoodsRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditGoodsRequest>(map<string, boost::any>({
    {"datatype", boost::any(154)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editGoodsWithOptions(editGoodsRequest, editGoodsHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
