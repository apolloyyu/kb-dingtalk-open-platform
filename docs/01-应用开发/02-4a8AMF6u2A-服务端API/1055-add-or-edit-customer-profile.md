---
title: "客户资料"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-customer-profile"
namespace: "development"
slug: "add-or-edit-customer-profile"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 客户 > 客户资料"
doc_id: "yr5XPoBYgr"
updated_at: "2026-01-29 14:19:31"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-customer-profile
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 客户 > 客户资料
> Updated: 2026-01-29 14:19:31

# 客户资料

通过此接口可新增或编辑客户资料，支持企业内部应用与第三方企业应用对金智CRM系统中的客户信息进行统一管理。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/customers |
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
| datatype | Long | 是 | 数据类型，固定值**148**。 |
| stamp | Long | 是 | 时间戳，单位：秒。 |
| msgid | Long | 否 | 数据ID。  **[!NOTE]**    值为0或不填时，为新增数据。 |
| data | Object | 否 | 编辑数据。 |
| data\_userid | String | 是 | 创建人。 |
| kh\_pkhid | String | 否 | 上级客户。 |
| kh\_class | String | 是 | 类别，取值。   - 企业客户 - 个人客户 - 供应商 - 个人供应商 |
| kh\_name | String | 是 | 客户名称。 |
| kh\_sex | String | 否 | 性别，取值。   - 男 - 女 |
| kh\_shortname | String | 否 | 助记简称。 |
| kh\_industry | String | 否 | 行业。 |
| kh\_employees | String | 否 | 人员规模。 |
| kh\_address | String | 否 | 家庭地址。 |
| kh\_country | String | 否 | 国家地区。 |
| kh\_province | String | 否 | 省份。 |
| kh\_city | String | 否 | 城市。 |
| kh\_coaddress | String | 否 | 单位地址。 |
| kh\_hottype | String | 否 | 是否为热点客。   - 是 - 否 |
| kh\_hotlevel | String | 否 | 热度，取值。   - 无 - 热 - 中热 - 高热 |
| kh\_hotfl | String | 否 | 热点分类。 |
| kh\_hotmemo | String | 否 | 热点说明。 |
| kh\_type | String | 否 | 种类。 |
| kh\_status | String | 否 | 阶段。 |
| kh\_sn | String | 否 | 编号。 |
| kh\_handset | String | 否 | 手机号。 |
| kh\_email | String | 否 | 邮箱。 |
| kh\_dingtalk | String | 否 | 钉钉号。 |
| kh\_tel | String | 否 | 家庭电话。 |
| kh\_weixin | String | 否 | 微信号。 |
| kh\_qq | String | 否 | QQ号。 |
| kh\_skype | String | 否 | Skype账号。 |
| kh\_wangwang | String | 否 | 旺旺。 |
| kh\_worktel | String | 否 | 工作电话。 |
| kh\_fax | String | 否 | 传真。 |
| kh\_pst | String | 否 | 邮编。 |
| kh\_department | String | 否 | 部门。 |
| kh\_appellation | String | 否 | 称谓。 |
| kh\_preside | String | 否 | 负责业务。 |
| kh\_headship | String | 否 | 职务。 |
| kh\_web | String | 否 | 网址。 |
| kh\_befontof | String | 否 | 爱好。 |
| kh\_from | String | 否 | 来源。 |
| kh\_billinfo | String | 否 | 开票资料。 |
| kh\_info | String | 否 | 公司简介。 |
| kh\_ralagrade | String | 否 | 关系等级。 |
| kh\_creditgrade | String | 否 | 信用等级，取值。   - 低 - 中 - 高 |
| kh\_valrating | String | 否 | 价值评估，取值。   - 低 - 中 - 高 |
| kh\_cttype | String | 否 | 证件类型。 |
| kh\_ctnumber | String | 否 | 证件号码。 |
| kh\_contype | String | 否 | 联系人分类 |
| kh\_remark | String | 否 | 备注。 |
| kh\_jibie | String | 否 | 客户级别。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/customers HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961ef7e2f3639zv1jjr76df97e21c
Content-Type:application/json

{
  "datatype" : 148,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "kh_pkhid" : "客户1",
    "kh_class" : "企业客户",
    "kh_name" : "客户2",
    "kh_sex" : "男",
    "kh_shortname" : "客户2",
    "kh_industry" : "服务",
    "kh_employees" : "100",
    "kh_address" : "200-300人",
    "kh_country" : "中国",
    "kh_province" : "山东",
    "kh_city" : "青岛",
    "kh_coaddress" : "香港中立",
    "kh_hottype" : "是",
    "kh_hotlevel" : "无",
    "kh_hotfl" : "高热意向客户",
    "kh_hotmemo" : "说明",
    "kh_type" : "普通客户",
    "kh_status" : "售中跟单",
    "kh_sn" : "KH20210531001",
    "kh_handset" : "18965698965",
    "kh_email" : "59867898@qq.com",
    "kh_dingtalk" : "钉钉号",
    "kh_tel" : "0533-4577963",
    "kh_weixin" : "wx_qijdjfyudj",
    "kh_qq" : "93539566",
    "kh_skype" : "Skype",
    "kh_wangwang" : "旺旺",
    "kh_worktel" : "0533-4577963",
    "kh_fax" : "传真",
    "kh_pst" : "236996",
    "kh_department" : "财务部",
    "kh_appellation" : "销售经理",
    "kh_preside" : "销售",
    "kh_headship" : "销售经理",
    "kh_web" : "https:://www.baidu.com",
    "kh_befontof" : "篮球",
    "kh_from" : "线上",
    "kh_billinfo" : "开票资料",
    "kh_info" : "公司简介",
    "kh_ralagrade" : "高",
    "kh_creditgrade" : "高",
    "kh_valrating" : "高",
    "kh_cttype" : "身份证",
    "kh_ctnumber" : "22363656369896536",
    "kh_contype" : "联系人分类",
    "kh_remark" : "备注",
    "kh_jibie" : "vip客户"
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
        EditCustomerHeaders editCustomerHeaders = new EditCustomerHeaders();
        editCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditCustomerRequest.EditCustomerRequestData data = new EditCustomerRequest.EditCustomerRequestData()
                .setDataUserid("张三")
                .setKhPkhid("客户1")
                .setKhClass("企业客户")
                .setKhName("客户2")
                .setKhSex("男")
                .setKhShortname("客户2")
                .setKhIndustry("服务")
                .setKhEmployees("100")
                .setKhAddress("200-300人")
                .setKhCountry("中国")
                .setKhProvince("山东")
                .setKhCity("青岛")
                .setKhCoaddress("香港中立")
                .setKhHottype("是")
                .setKhHotlevel("无")
                .setKhHotfl("高热意向客户")
                .setKhHotmemo("说明")
                .setKhType("普通客户")
                .setKhStatus("售中跟单")
                .setKhSn("KH20210531001")
                .setKhHandset("18965698965")
                .setKhEmail("59867898@qq.com")
                .setKhDingtalk("钉钉号")
                .setKhTel("0533-4577963")
                .setKhWeixin("wx_qijdjfyudj")
                .setKhQq("93539566")
                .setKhSkype("Skype")
                .setKhWangwang("旺旺")
                .setKhWorktel("0533-4577963")
                .setKhFax("传真")
                .setKhPst("236996")
                .setKhDepartment("财务部")
                .setKhAppellation("销售经理")
                .setKhPreside("销售")
                .setKhHeadship("销售经理")
                .setKhWeb("https:://www.baidu.com")
                .setKhBefontof("篮球")
                .setKhFrom("线上")
                .setKhBillinfo("开票资料")
                .setKhInfo("公司简介")
                .setKhRalagrade("高")
                .setKhCreditgrade("高")
                .setKhValrating("高")
                .setKhCttype("身份证")
                .setKhCtnumber("22363656369896536")
                .setKhContype("联系人分类")
                .setKhRemark("备注")
                .setKhJibie("vip客户");
        EditCustomerRequest editCustomerRequest = new EditCustomerRequest()
                .setDatatype(148L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editCustomerWithOptions(editCustomerRequest, editCustomerHeaders, new RuntimeOptions());
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
        edit_customer_headers = dingtalkjzcrm__1__0_models.EditCustomerHeaders()
        edit_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditCustomerRequestData(
            data_userid='张三',
            kh_pkhid='客户1',
            kh_class='企业客户',
            kh_name='客户2',
            kh_sex='男',
            kh_shortname='客户2',
            kh_industry='服务',
            kh_employees='100',
            kh_address='200-300人',
            kh_country='中国',
            kh_province='山东',
            kh_city='青岛',
            kh_coaddress='香港中立',
            kh_hottype='是',
            kh_hotlevel='无',
            kh_hotfl='高热意向客户',
            kh_hotmemo='说明',
            kh_type='普通客户',
            kh_status='售中跟单',
            kh_sn='KH20210531001',
            kh_handset='18965698965',
            kh_email='59867898@qq.com',
            kh_dingtalk='钉钉号',
            kh_tel='0533-4577963',
            kh_weixin='wx_qijdjfyudj',
            kh_qq='93539566',
            kh_skype='Skype',
            kh_wangwang='旺旺',
            kh_worktel='0533-4577963',
            kh_fax='传真',
            kh_pst='236996',
            kh_department='财务部',
            kh_appellation='销售经理',
            kh_preside='销售',
            kh_headship='销售经理',
            kh_web='https:://www.baidu.com',
            kh_befontof='篮球',
            kh_from='线上',
            kh_billinfo='开票资料',
            kh_info='公司简介',
            kh_ralagrade='高',
            kh_creditgrade='高',
            kh_valrating='高',
            kh_cttype='身份证',
            kh_ctnumber='22363656369896536',
            kh_contype='联系人分类',
            kh_remark='备注',
            kh_jibie='vip客户'
        )
        edit_customer_request = dingtalkjzcrm__1__0_models.EditCustomerRequest(
            datatype=148,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_customer_with_options(edit_customer_request, edit_customer_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_customer_headers = dingtalkjzcrm__1__0_models.EditCustomerHeaders()
        edit_customer_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditCustomerRequestData(
            data_userid='张三',
            kh_pkhid='客户1',
            kh_class='企业客户',
            kh_name='客户2',
            kh_sex='男',
            kh_shortname='客户2',
            kh_industry='服务',
            kh_employees='100',
            kh_address='200-300人',
            kh_country='中国',
            kh_province='山东',
            kh_city='青岛',
            kh_coaddress='香港中立',
            kh_hottype='是',
            kh_hotlevel='无',
            kh_hotfl='高热意向客户',
            kh_hotmemo='说明',
            kh_type='普通客户',
            kh_status='售中跟单',
            kh_sn='KH20210531001',
            kh_handset='18965698965',
            kh_email='59867898@qq.com',
            kh_dingtalk='钉钉号',
            kh_tel='0533-4577963',
            kh_weixin='wx_qijdjfyudj',
            kh_qq='93539566',
            kh_skype='Skype',
            kh_wangwang='旺旺',
            kh_worktel='0533-4577963',
            kh_fax='传真',
            kh_pst='236996',
            kh_department='财务部',
            kh_appellation='销售经理',
            kh_preside='销售',
            kh_headship='销售经理',
            kh_web='https:://www.baidu.com',
            kh_befontof='篮球',
            kh_from='线上',
            kh_billinfo='开票资料',
            kh_info='公司简介',
            kh_ralagrade='高',
            kh_creditgrade='高',
            kh_valrating='高',
            kh_cttype='身份证',
            kh_ctnumber='22363656369896536',
            kh_contype='联系人分类',
            kh_remark='备注',
            kh_jibie='vip客户'
        )
        edit_customer_request = dingtalkjzcrm__1__0_models.EditCustomerRequest(
            datatype=148,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_customer_with_options_async(edit_customer_request, edit_customer_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditCustomerHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditCustomerRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditCustomerRequest;
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
        $editCustomerHeaders = new EditCustomerHeaders([]);
        $editCustomerHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "khPkhid" => "客户1",
            "khClass" => "企业客户",
            "khName" => "客户2",
            "khSex" => "男",
            "khShortname" => "客户2",
            "khIndustry" => "服务",
            "khEmployees" => "100",
            "khAddress" => "200-300人",
            "khCountry" => "中国",
            "khProvince" => "山东",
            "khCity" => "青岛",
            "khCoaddress" => "香港中立",
            "khHottype" => "是",
            "khHotlevel" => "无",
            "khHotfl" => "高热意向客户",
            "khHotmemo" => "说明",
            "khType" => "普通客户",
            "khStatus" => "售中跟单",
            "khSn" => "KH20210531001",
            "khHandset" => "18965698965",
            "khEmail" => "59867898@qq.com",
            "khDingtalk" => "钉钉号",
            "khTel" => "0533-4577963",
            "khWeixin" => "wx_qijdjfyudj",
            "khQq" => "93539566",
            "khSkype" => "Skype",
            "khWangwang" => "旺旺",
            "khWorktel" => "0533-4577963",
            "khFax" => "传真",
            "khPst" => "236996",
            "khDepartment" => "财务部",
            "khAppellation" => "销售经理",
            "khPreside" => "销售",
            "khHeadship" => "销售经理",
            "khWeb" => "https:://www.baidu.com",
            "khBefontof" => "篮球",
            "khFrom" => "线上",
            "khBillinfo" => "开票资料",
            "khInfo" => "公司简介",
            "khRalagrade" => "高",
            "khCreditgrade" => "高",
            "khValrating" => "高",
            "khCttype" => "身份证",
            "khCtnumber" => "22363656369896536",
            "khContype" => "联系人分类",
            "khRemark" => "备注",
            "khJibie" => "vip客户"
        ]);
        $editCustomerRequest = new EditCustomerRequest([
            "datatype" => 148,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editCustomerWithOptions($editCustomerRequest, $editCustomerHeaders, new RuntimeOptions([]));
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

  editCustomerHeaders := &dingtalkjzcrm_1_0.EditCustomerHeaders{}
  editCustomerHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditCustomerRequestData{
    DataUserid: tea.String("张三"),
    KhPkhid: tea.String("客户1"),
    KhClass: tea.String("企业客户"),
    KhName: tea.String("客户2"),
    KhSex: tea.String("男"),
    KhShortname: tea.String("客户2"),
    KhIndustry: tea.String("服务"),
    KhEmployees: tea.String("100"),
    KhAddress: tea.String("200-300人"),
    KhCountry: tea.String("中国"),
    KhProvince: tea.String("山东"),
    KhCity: tea.String("青岛"),
    KhCoaddress: tea.String("香港中立"),
    KhHottype: tea.String("是"),
    KhHotlevel: tea.String("无"),
    KhHotfl: tea.String("高热意向客户"),
    KhHotmemo: tea.String("说明"),
    KhType: tea.String("普通客户"),
    KhStatus: tea.String("售中跟单"),
    KhSn: tea.String("KH20210531001"),
    KhHandset: tea.String("18965698965"),
    KhEmail: tea.String("59867898@qq.com"),
    KhDingtalk: tea.String("钉钉号"),
    KhTel: tea.String("0533-4577963"),
    KhWeixin: tea.String("wx_qijdjfyudj"),
    KhQq: tea.String("93539566"),
    KhSkype: tea.String("Skype"),
    KhWangwang: tea.String("旺旺"),
    KhWorktel: tea.String("0533-4577963"),
    KhFax: tea.String("传真"),
    KhPst: tea.String("236996"),
    KhDepartment: tea.String("财务部"),
    KhAppellation: tea.String("销售经理"),
    KhPreside: tea.String("销售"),
    KhHeadship: tea.String("销售经理"),
    KhWeb: tea.String("https:://www.baidu.com"),
    KhBefontof: tea.String("篮球"),
    KhFrom: tea.String("线上"),
    KhBillinfo: tea.String("开票资料"),
    KhInfo: tea.String("公司简介"),
    KhRalagrade: tea.String("高"),
    KhCreditgrade: tea.String("高"),
    KhValrating: tea.String("高"),
    KhCttype: tea.String("身份证"),
    KhCtnumber: tea.String("22363656369896536"),
    KhContype: tea.String("联系人分类"),
    KhRemark: tea.String("备注"),
    KhJibie: tea.String("vip客户"),
  }
  editCustomerRequest := &dingtalkjzcrm_1_0.EditCustomerRequest{
    Datatype: tea.Int64(148),
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
    _, _err = client.EditCustomerWithOptions(editCustomerRequest, editCustomerHeaders, &util.RuntimeOptions{})
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
    let editCustomerHeaders = new $dingtalkjzcrm_1_0.EditCustomerHeaders({ });
    editCustomerHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditCustomerRequestData({
      dataUserid: "张三",
      khPkhid: "客户1",
      khClass: "企业客户",
      khName: "客户2",
      khSex: "男",
      khShortname: "客户2",
      khIndustry: "服务",
      khEmployees: "100",
      khAddress: "200-300人",
      khCountry: "中国",
      khProvince: "山东",
      khCity: "青岛",
      khCoaddress: "香港中立",
      khHottype: "是",
      khHotlevel: "无",
      khHotfl: "高热意向客户",
      khHotmemo: "说明",
      khType: "普通客户",
      khStatus: "售中跟单",
      khSn: "KH20210531001",
      khHandset: "18965698965",
      khEmail: "59867898@qq.com",
      khDingtalk: "钉钉号",
      khTel: "0533-4577963",
      khWeixin: "wx_qijdjfyudj",
      khQq: "93539566",
      khSkype: "Skype",
      khWangwang: "旺旺",
      khWorktel: "0533-4577963",
      khFax: "传真",
      khPst: "236996",
      khDepartment: "财务部",
      khAppellation: "销售经理",
      khPreside: "销售",
      khHeadship: "销售经理",
      khWeb: "https:://www.baidu.com",
      khBefontof: "篮球",
      khFrom: "线上",
      khBillinfo: "开票资料",
      khInfo: "公司简介",
      khRalagrade: "高",
      khCreditgrade: "高",
      khValrating: "高",
      khCttype: "身份证",
      khCtnumber: "22363656369896536",
      khContype: "联系人分类",
      khRemark: "备注",
      khJibie: "vip客户",
    });
    let editCustomerRequest = new $dingtalkjzcrm_1_0.EditCustomerRequest({
      datatype: 148,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editCustomerWithOptions(editCustomerRequest, editCustomerHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerHeaders editCustomerHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerHeaders();
            editCustomerHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerRequest.EditCustomerRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerRequest.EditCustomerRequestData
            {
                DataUserid = "张三",
                KhPkhid = "客户1",
                KhClass = "企业客户",
                KhName = "客户2",
                KhSex = "男",
                KhShortname = "客户2",
                KhIndustry = "服务",
                KhEmployees = "100",
                KhAddress = "200-300人",
                KhCountry = "中国",
                KhProvince = "山东",
                KhCity = "青岛",
                KhCoaddress = "香港中立",
                KhHottype = "是",
                KhHotlevel = "无",
                KhHotfl = "高热意向客户",
                KhHotmemo = "说明",
                KhType = "普通客户",
                KhStatus = "售中跟单",
                KhSn = "KH20210531001",
                KhHandset = "18965698965",
                KhEmail = "59867898@qq.com",
                KhDingtalk = "钉钉号",
                KhTel = "0533-4577963",
                KhWeixin = "wx_qijdjfyudj",
                KhQq = "93539566",
                KhSkype = "Skype",
                KhWangwang = "旺旺",
                KhWorktel = "0533-4577963",
                KhFax = "传真",
                KhPst = "236996",
                KhDepartment = "财务部",
                KhAppellation = "销售经理",
                KhPreside = "销售",
                KhHeadship = "销售经理",
                KhWeb = "https:://www.baidu.com",
                KhBefontof = "篮球",
                KhFrom = "线上",
                KhBillinfo = "开票资料",
                KhInfo = "公司简介",
                KhRalagrade = "高",
                KhCreditgrade = "高",
                KhValrating = "高",
                KhCttype = "身份证",
                KhCtnumber = "22363656369896536",
                KhContype = "联系人分类",
                KhRemark = "备注",
                KhJibie = "vip客户",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerRequest editCustomerRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerRequest
            {
                Datatype = 148,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditCustomerWithOptions(editCustomerRequest, editCustomerHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerHeaders> editCustomerHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerHeaders>();
  editCustomerHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"khPkhid", boost::any(string("客户1"))},
    {"khClass", boost::any(string("企业客户"))},
    {"khName", boost::any(string("客户2"))},
    {"khSex", boost::any(string("男"))},
    {"khShortname", boost::any(string("客户2"))},
    {"khIndustry", boost::any(string("服务"))},
    {"khEmployees", boost::any(string("100"))},
    {"khAddress", boost::any(string("200-300人"))},
    {"khCountry", boost::any(string("中国"))},
    {"khProvince", boost::any(string("山东"))},
    {"khCity", boost::any(string("青岛"))},
    {"khCoaddress", boost::any(string("香港中立"))},
    {"khHottype", boost::any(string("是"))},
    {"khHotlevel", boost::any(string("无"))},
    {"khHotfl", boost::any(string("高热意向客户"))},
    {"khHotmemo", boost::any(string("说明"))},
    {"khType", boost::any(string("普通客户"))},
    {"khStatus", boost::any(string("售中跟单"))},
    {"khSn", boost::any(string("KH20210531001"))},
    {"khHandset", boost::any(string("18965698965"))},
    {"khEmail", boost::any(string("59867898@qq.com"))},
    {"khDingtalk", boost::any(string("钉钉号"))},
    {"khTel", boost::any(string("0533-4577963"))},
    {"khWeixin", boost::any(string("wx_qijdjfyudj"))},
    {"khQq", boost::any(string("93539566"))},
    {"khSkype", boost::any(string("Skype"))},
    {"khWangwang", boost::any(string("旺旺"))},
    {"khWorktel", boost::any(string("0533-4577963"))},
    {"khFax", boost::any(string("传真"))},
    {"khPst", boost::any(string("236996"))},
    {"khDepartment", boost::any(string("财务部"))},
    {"khAppellation", boost::any(string("销售经理"))},
    {"khPreside", boost::any(string("销售"))},
    {"khHeadship", boost::any(string("销售经理"))},
    {"khWeb", boost::any(string("https:://www.baidu.com"))},
    {"khBefontof", boost::any(string("篮球"))},
    {"khFrom", boost::any(string("线上"))},
    {"khBillinfo", boost::any(string("开票资料"))},
    {"khInfo", boost::any(string("公司简介"))},
    {"khRalagrade", boost::any(string("高"))},
    {"khCreditgrade", boost::any(string("高"))},
    {"khValrating", boost::any(string("高"))},
    {"khCttype", boost::any(string("身份证"))},
    {"khCtnumber", boost::any(string("22363656369896536"))},
    {"khContype", boost::any(string("联系人分类"))},
    {"khRemark", boost::any(string("备注"))},
    {"khJibie", boost::any(string("vip客户"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerRequest> editCustomerRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerRequest>(map<string, boost::any>({
    {"datatype", boost::any(148)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editCustomerWithOptions(editCustomerRequest, editCustomerHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
