---
title: "联系人"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-contacts"
namespace: "development"
slug: "add-or-edit-contacts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 联系人 > 联系人"
doc_id: "IRmWewIe79"
updated_at: "2026-01-29 14:19:33"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-contacts
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 联系人 > 联系人
> Updated: 2026-01-29 14:19:33

# 联系人

通过此接口实现金智CRM系统中联系人的新增或编辑操作，支持企业内部应用和第三方企业应用调用。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/contacts |
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
| datatype | Long | 是 | 数据类型，固定值**197**。 |
| stamp | Long | 是 | 时间戳。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| lxr\_customerid | String | 是 | 对应客户。 |
| lxr\_name | String | 是 | 姓名。 |
| lxr\_handset | String | 否 | 手机。 |
| lxr\_worktel | String | 否 | 工作电话。 |
| lxr\_sex | String | 否 | 性别，取值。   - 男 - 女 |
| lxr\_group | String | 否 | 分类。 |
| lxr\_preside | String | 否 | 负责业务。 |
| lxr\_cttype | String | 否 | 证件类型。 |
| lxr\_ctnumber | String | 否 | 证件号码。 |
| lxr\_chengwei | String | 否 | 称谓。 |
| lxr\_type | String | 否 | 类型，取值。   - 联系人 - 主联系人 |
| lxr\_department | String | 否 | 部门。 |
| lxr\_headship | String | 否 | 职务。 |
| lxr\_dingtalk | String | 否 | 钉钉号。 |
| lxr\_fax | String | 否 | 传真。 |
| lxr\_wangwang | String | 否 | 旺旺。 |
| lxr\_email | String | 否 | 邮箱。 |
| lxr\_weixin | String | 否 | 微信号 |
| lxr\_qq | String | 否 | QQ号。 |
| lxr\_tel | String | 否 | 家庭电话。 |
| lxr\_pst | String | 否 | 邮编。 |
| lxr\_skype | String | 否 | Skype账号。 |
| lxr\_address | String | 否 | 住址。 |
| lxr\_birthday | String | 否 | 生日。 |
| lxr\_like | String | 否 | 爱好。 |
| lxr\_remark | String | 否 | 备注。 |
| lxr\_photo | String | 否 | 联系名片。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/contacts HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961exxxx
Content-Type:application/json

{
  "datatype" : 197,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "lxr_customerid" : "客户1",
    "lxr_name" : "李四",
    "lxr_handset" : "169896989698",
    "lxr_worktel" : "3688-898899",
    "lxr_sex" : "男",
    "lxr_group" : "部门总监",
    "lxr_preside" : "管理",
    "lxr_cttype" : "身份证",
    "lxr_ctnumber" : "369898569856985",
    "lxr_chengwei" : "总监",
    "lxr_type" : "联系人",
    "lxr_department" : "市场部",
    "lxr_headship" : "市场部总监",
    "lxr_dingtalk" : "钉钉号",
    "lxr_fax" : "传真",
    "lxr_wangwang" : "旺旺",
    "lxr_email" : "56898998@qq.com",
    "lxr_weixin" : "wx_567435t4",
    "lxr_qq" : "89698896",
    "lxr_tel" : "3622-986568",
    "lxr_pst" : "698659",
    "lxr_skype" : "skype",
    "lxr_address" : "四川省成都市",
    "lxr_birthday" : "1991-6-9",
    "lxr_like" : "游泳",
    "lxr_remark" : "备注",
    "lxr_photo" : "名片"
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
        EditContactHeaders editContactHeaders = new EditContactHeaders();
        editContactHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditContactRequest.EditContactRequestData data = new EditContactRequest.EditContactRequestData()
                .setDataUserid("张三")
                .setLxrCustomerid("客户1")
                .setLxrName("李四")
                .setLxrHandset("169896989698")
                .setLxrWorktel("3688-898899")
                .setLxrSex("男")
                .setLxrGroup("部门总监")
                .setLxrPreside("管理")
                .setLxrCttype("身份证")
                .setLxrCtnumber("369898569856985")
                .setLxrChengwei("总监")
                .setLxrType("联系人")
                .setLxrDepartment("市场部")
                .setLxrHeadship("市场部总监")
                .setLxrDingtalk("钉钉号")
                .setLxrFax("传真")
                .setLxrWangwang("旺旺")
                .setLxrEmail("56898998@qq.com")
                .setLxrWeixin("wx_567435t4")
                .setLxrQq("89698896")
                .setLxrTel("3622-986568")
                .setLxrPst("698659")
                .setLxrSkype("skype")
                .setLxrAddress("四川省成都市")
                .setLxrBirthday("1991-6-9")
                .setLxrLike("游泳")
                .setLxrRemark("备注")
                .setLxrPhoto("名片");
        EditContactRequest editContactRequest = new EditContactRequest()
                .setDatatype(197L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editContactWithOptions(editContactRequest, editContactHeaders, new RuntimeOptions());
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
        edit_contact_headers = dingtalkjzcrm__1__0_models.EditContactHeaders()
        edit_contact_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditContactRequestData(
            data_userid='张三',
            lxr_customerid='客户1',
            lxr_name='李四',
            lxr_handset='169896989698',
            lxr_worktel='3688-898899',
            lxr_sex='男',
            lxr_group='部门总监',
            lxr_preside='管理',
            lxr_cttype='身份证',
            lxr_ctnumber='369898569856985',
            lxr_chengwei='总监',
            lxr_type='联系人',
            lxr_department='市场部',
            lxr_headship='市场部总监',
            lxr_dingtalk='钉钉号',
            lxr_fax='传真',
            lxr_wangwang='旺旺',
            lxr_email='56898998@qq.com',
            lxr_weixin='wx_567435t4',
            lxr_qq='89698896',
            lxr_tel='3622-986568',
            lxr_pst='698659',
            lxr_skype='skype',
            lxr_address='四川省成都市',
            lxr_birthday='1991-6-9',
            lxr_like='游泳',
            lxr_remark='备注',
            lxr_photo='名片'
        )
        edit_contact_request = dingtalkjzcrm__1__0_models.EditContactRequest(
            datatype=197,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_contact_with_options(edit_contact_request, edit_contact_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_contact_headers = dingtalkjzcrm__1__0_models.EditContactHeaders()
        edit_contact_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditContactRequestData(
            data_userid='张三',
            lxr_customerid='客户1',
            lxr_name='李四',
            lxr_handset='169896989698',
            lxr_worktel='3688-898899',
            lxr_sex='男',
            lxr_group='部门总监',
            lxr_preside='管理',
            lxr_cttype='身份证',
            lxr_ctnumber='369898569856985',
            lxr_chengwei='总监',
            lxr_type='联系人',
            lxr_department='市场部',
            lxr_headship='市场部总监',
            lxr_dingtalk='钉钉号',
            lxr_fax='传真',
            lxr_wangwang='旺旺',
            lxr_email='56898998@qq.com',
            lxr_weixin='wx_567435t4',
            lxr_qq='89698896',
            lxr_tel='3622-986568',
            lxr_pst='698659',
            lxr_skype='skype',
            lxr_address='四川省成都市',
            lxr_birthday='1991-6-9',
            lxr_like='游泳',
            lxr_remark='备注',
            lxr_photo='名片'
        )
        edit_contact_request = dingtalkjzcrm__1__0_models.EditContactRequest(
            datatype=197,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_contact_with_options_async(edit_contact_request, edit_contact_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditContactHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditContactRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditContactRequest;
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
        $editContactHeaders = new EditContactHeaders([]);
        $editContactHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "lxrCustomerid" => "客户1",
            "lxrName" => "李四",
            "lxrHandset" => "169896989698",
            "lxrWorktel" => "3688-898899",
            "lxrSex" => "男",
            "lxrGroup" => "部门总监",
            "lxrPreside" => "管理",
            "lxrCttype" => "身份证",
            "lxrCtnumber" => "369898569856985",
            "lxrChengwei" => "总监",
            "lxrType" => "联系人",
            "lxrDepartment" => "市场部",
            "lxrHeadship" => "市场部总监",
            "lxrDingtalk" => "钉钉号",
            "lxrFax" => "传真",
            "lxrWangwang" => "旺旺",
            "lxrEmail" => "56898998@qq.com",
            "lxrWeixin" => "wx_567435t4",
            "lxrQq" => "89698896",
            "lxrTel" => "3622-986568",
            "lxrPst" => "698659",
            "lxrSkype" => "skype",
            "lxrAddress" => "四川省成都市",
            "lxrBirthday" => "1991-6-9",
            "lxrLike" => "游泳",
            "lxrRemark" => "备注",
            "lxrPhoto" => "名片"
        ]);
        $editContactRequest = new EditContactRequest([
            "datatype" => 197,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editContactWithOptions($editContactRequest, $editContactHeaders, new RuntimeOptions([]));
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

  editContactHeaders := &dingtalkjzcrm_1_0.EditContactHeaders{}
  editContactHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditContactRequestData{
    DataUserid: tea.String("张三"),
    LxrCustomerid: tea.String("客户1"),
    LxrName: tea.String("李四"),
    LxrHandset: tea.String("169896989698"),
    LxrWorktel: tea.String("3688-898899"),
    LxrSex: tea.String("男"),
    LxrGroup: tea.String("部门总监"),
    LxrPreside: tea.String("管理"),
    LxrCttype: tea.String("身份证"),
    LxrCtnumber: tea.String("369898569856985"),
    LxrChengwei: tea.String("总监"),
    LxrType: tea.String("联系人"),
    LxrDepartment: tea.String("市场部"),
    LxrHeadship: tea.String("市场部总监"),
    LxrDingtalk: tea.String("钉钉号"),
    LxrFax: tea.String("传真"),
    LxrWangwang: tea.String("旺旺"),
    LxrEmail: tea.String("56898998@qq.com"),
    LxrWeixin: tea.String("wx_567435t4"),
    LxrQq: tea.String("89698896"),
    LxrTel: tea.String("3622-986568"),
    LxrPst: tea.String("698659"),
    LxrSkype: tea.String("skype"),
    LxrAddress: tea.String("四川省成都市"),
    LxrBirthday: tea.String("1991-6-9"),
    LxrLike: tea.String("游泳"),
    LxrRemark: tea.String("备注"),
    LxrPhoto: tea.String("名片"),
  }
  editContactRequest := &dingtalkjzcrm_1_0.EditContactRequest{
    Datatype: tea.Int64(197),
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
    _, _err = client.EditContactWithOptions(editContactRequest, editContactHeaders, &util.RuntimeOptions{})
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
    let editContactHeaders = new $dingtalkjzcrm_1_0.EditContactHeaders({ });
    editContactHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditContactRequestData({
      dataUserid: "张三",
      lxrCustomerid: "客户1",
      lxrName: "李四",
      lxrHandset: "169896989698",
      lxrWorktel: "3688-898899",
      lxrSex: "男",
      lxrGroup: "部门总监",
      lxrPreside: "管理",
      lxrCttype: "身份证",
      lxrCtnumber: "369898569856985",
      lxrChengwei: "总监",
      lxrType: "联系人",
      lxrDepartment: "市场部",
      lxrHeadship: "市场部总监",
      lxrDingtalk: "钉钉号",
      lxrFax: "传真",
      lxrWangwang: "旺旺",
      lxrEmail: "56898998@qq.com",
      lxrWeixin: "wx_567435t4",
      lxrQq: "89698896",
      lxrTel: "3622-986568",
      lxrPst: "698659",
      lxrSkype: "skype",
      lxrAddress: "四川省成都市",
      lxrBirthday: "1991-6-9",
      lxrLike: "游泳",
      lxrRemark: "备注",
      lxrPhoto: "名片",
    });
    let editContactRequest = new $dingtalkjzcrm_1_0.EditContactRequest({
      datatype: 197,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editContactWithOptions(editContactRequest, editContactHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditContactHeaders editContactHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditContactHeaders();
            editContactHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditContactRequest.EditContactRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditContactRequest.EditContactRequestData
            {
                DataUserid = "张三",
                LxrCustomerid = "客户1",
                LxrName = "李四",
                LxrHandset = "169896989698",
                LxrWorktel = "3688-898899",
                LxrSex = "男",
                LxrGroup = "部门总监",
                LxrPreside = "管理",
                LxrCttype = "身份证",
                LxrCtnumber = "369898569856985",
                LxrChengwei = "总监",
                LxrType = "联系人",
                LxrDepartment = "市场部",
                LxrHeadship = "市场部总监",
                LxrDingtalk = "钉钉号",
                LxrFax = "传真",
                LxrWangwang = "旺旺",
                LxrEmail = "56898998@qq.com",
                LxrWeixin = "wx_567435t4",
                LxrQq = "89698896",
                LxrTel = "3622-986568",
                LxrPst = "698659",
                LxrSkype = "skype",
                LxrAddress = "四川省成都市",
                LxrBirthday = "1991-6-9",
                LxrLike = "游泳",
                LxrRemark = "备注",
                LxrPhoto = "名片",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditContactRequest editContactRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditContactRequest
            {
                Datatype = 197,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditContactWithOptions(editContactRequest, editContactHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditContactHeaders> editContactHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditContactHeaders>();
  editContactHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditContactRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditContactRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"lxrCustomerid", boost::any(string("客户1"))},
    {"lxrName", boost::any(string("李四"))},
    {"lxrHandset", boost::any(string("169896989698"))},
    {"lxrWorktel", boost::any(string("3688-898899"))},
    {"lxrSex", boost::any(string("男"))},
    {"lxrGroup", boost::any(string("部门总监"))},
    {"lxrPreside", boost::any(string("管理"))},
    {"lxrCttype", boost::any(string("身份证"))},
    {"lxrCtnumber", boost::any(string("369898569856985"))},
    {"lxrChengwei", boost::any(string("总监"))},
    {"lxrType", boost::any(string("联系人"))},
    {"lxrDepartment", boost::any(string("市场部"))},
    {"lxrHeadship", boost::any(string("市场部总监"))},
    {"lxrDingtalk", boost::any(string("钉钉号"))},
    {"lxrFax", boost::any(string("传真"))},
    {"lxrWangwang", boost::any(string("旺旺"))},
    {"lxrEmail", boost::any(string("56898998@qq.com"))},
    {"lxrWeixin", boost::any(string("wx_567435t4"))},
    {"lxrQq", boost::any(string("89698896"))},
    {"lxrTel", boost::any(string("3622-986568"))},
    {"lxrPst", boost::any(string("698659"))},
    {"lxrSkype", boost::any(string("skype"))},
    {"lxrAddress", boost::any(string("四川省成都市"))},
    {"lxrBirthday", boost::any(string("1991-6-9"))},
    {"lxrLike", boost::any(string("游泳"))},
    {"lxrRemark", boost::any(string("备注"))},
    {"lxrPhoto", boost::any(string("名片"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditContactRequest> editContactRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditContactRequest>(map<string, boost::any>({
    {"datatype", boost::any(197)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editContactWithOptions(editContactRequest, editContactHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
