---
title: "客户公共池"
source_url: "https://open.dingtalk.com/document/development/add-or-edit-customer-public-pools"
namespace: "development"
slug: "add-or-edit-customer-public-pools"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 客户 > 客户公共池"
doc_id: "ABhAjPrGVr"
updated_at: "2026-01-29 14:19:32"
---

> Source: https://open.dingtalk.com/document/development/add-or-edit-customer-public-pools
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 客户 > 客户公共池
> Updated: 2026-01-29 14:19:32

# 客户公共池

调用本接口新增或编辑客户公共池。本接口适用于金智CRM系统中客户公共池的新增与编辑操作。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/customerPools |
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
| datatype | Long | 是 | 数据类型，固定值**238**。 |
| stamp | Long | 是 | 时间戳。 |
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
| kh\_hottype | String | 否 | 是否热点客户，取值。   - 是 - 否 |
| kh\_hotlevel | String | 否 | 热度，取值。   - 无 - 低热 - 中热 - 高热 |
| kh\_hotfl | String | 否 | 热点分类。 |
| kh\_hotmemo | String | 否 | 热点说明。 |
| kh\_type | String | 否 | 种类。 |
| kh\_status | String | 否 | 阶段。 |
| kh\_sn | String | 否 | 编号。 |
| kh\_handset | String | 否 | 手机。 |
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
| kh\_contype | String | 否 | 联系人分类。 |
| kh\_remark | String | 否 | 备注。 |
| kh\_jibie | String | 否 | 客户级别。 |
| kh\_genzongtime | String | 否 | 最后跟踪。 |

### 请求示例

HTTP

```
POST /v1.0/jzcrm/customerPools HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:1599xxx
Content-Type:application/json

{
  "datatype" : 238,
  "stamp" : 1621822122,
  "msgid" : 1,
  "data" : {
    "data_userid" : "张三",
    "kh_pkhid" : "XX有限公司",
    "kh_class" : "企业客户",
    "kh_name" : "XX科技有限公司",
    "kh_sex" : "女",
    "kh_shortname" : "小刘",
    "kh_industry" : "电子科技",
    "kh_employees" : "50人",
    "kh_address" : "山东省青岛市市南区",
    "kh_country" : "中国",
    "kh_province" : "山东省",
    "kh_city" : "青岛市",
    "kh_coaddress" : "中国山东省青岛市市南区XX街道",
    "kh_hottype" : "是",
    "kh_hotlevel" : "无",
    "kh_hotfl" : "最近跟进客户",
    "kh_hotmemo" : "高热",
    "kh_type" : "潜在客户",
    "kh_status" : "客户跟踪",
    "kh_sn" : "KH202106011001",
    "kh_handset" : "16688889999",
    "kh_email" : "youxaing@163.com",
    "kh_dingtalk" : "youxaing",
    "kh_tel" : "8888888",
    "kh_weixin" : "JzSoft",
    "kh_qq" : "88888888",
    "kh_skype" : "Skype",
    "kh_wangwang" : "123123123",
    "kh_worktel" : "16688880000",
    "kh_fax" : "传真",
    "kh_pst" : "266000",
    "kh_department" : "销售部",
    "kh_appellation" : "李总",
    "kh_preside" : "销售",
    "kh_headship" : "厂长",
    "kh_web" : "www.baidu.com",
    "kh_befontof" : "唱跳rap篮球",
    "kh_from" : "电话采访",
    "kh_billinfo" : "未开票",
    "kh_info" : "百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。",
    "kh_ralagrade" : "一等",
    "kh_creditgrade" : "高",
    "kh_valrating" : "高",
    "kh_cttype" : "身份证",
    "kh_ctnumber" : "12312312312312312",
    "kh_contype" : "企业客户联系人",
    "kh_remark" : "备注",
    "kh_jibie" : "一级代理商",
    "kh_genzongtime" : "2021-06-01"
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
        EditCustomerPoolHeaders editCustomerPoolHeaders = new EditCustomerPoolHeaders();
        editCustomerPoolHeaders.xAcsDingtalkAccessToken = "<your access token>";
        EditCustomerPoolRequest.EditCustomerPoolRequestData data = new EditCustomerPoolRequest.EditCustomerPoolRequestData()
                .setDataUserid("张三")
                .setKhPkhid("XX有限公司")
                .setKhClass("企业客户")
                .setKhName("XX科技有限公司")
                .setKhSex("女")
                .setKhShortname("小刘")
                .setKhIndustry("电子科技")
                .setKhEmployees("50人")
                .setKhAddress("山东省青岛市市南区")
                .setKhCountry("中国")
                .setKhProvince("山东省")
                .setKhCity("青岛市")
                .setKhCoaddress("中国山东省青岛市市南区XX街道")
                .setKhHottype("是")
                .setKhHotlevel("无")
                .setKhHotfl("最近跟进客户")
                .setKhHotmemo("高热")
                .setKhType("潜在客户")
                .setKhStatus("客户跟踪")
                .setKhSn("KH202106011001")
                .setKhHandset("16688889999")
                .setKhEmail("youxaing@163.com")
                .setKhDingtalk("youxaing")
                .setKhTel("8888888")
                .setKhWeixin("JzSoft")
                .setKhQq("88888888")
                .setKhSkype("Skype")
                .setKhWangwang("123123123")
                .setKhWorktel("16688880000")
                .setKhFax("传真")
                .setKhPst("266000")
                .setKhDepartment("销售部")
                .setKhAppellation("李总")
                .setKhPreside("销售")
                .setKhHeadship("厂长")
                .setKhWeb("www.baidu.com")
                .setKhBefontof("唱跳rap篮球")
                .setKhFrom("电话采访")
                .setKhBillinfo("未开票")
                .setKhInfo("百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。")
                .setKhRalagrade("一等")
                .setKhCreditgrade("高")
                .setKhValrating("高")
                .setKhCttype("身份证")
                .setKhCtnumber("12312312312312312")
                .setKhContype("企业客户联系人")
                .setKhRemark("备注")
                .setKhJibie("一级代理商")
                .setKhGenzongtime("2021-06-01");
        EditCustomerPoolRequest editCustomerPoolRequest = new EditCustomerPoolRequest()
                .setDatatype(238L)
                .setStamp(1621822122L)
                .setMsgid(1L)
                .setData(data);
        try {
            client.editCustomerPoolWithOptions(editCustomerPoolRequest, editCustomerPoolHeaders, new RuntimeOptions());
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
        edit_customer_pool_headers = dingtalkjzcrm__1__0_models.EditCustomerPoolHeaders()
        edit_customer_pool_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditCustomerPoolRequestData(
            data_userid='张三',
            kh_pkhid='XX有限公司',
            kh_class='企业客户',
            kh_name='XX科技有限公司',
            kh_sex='女',
            kh_shortname='小刘',
            kh_industry='电子科技',
            kh_employees='50人',
            kh_address='山东省青岛市市南区',
            kh_country='中国',
            kh_province='山东省',
            kh_city='青岛市',
            kh_coaddress='中国山东省青岛市市南区XX街道',
            kh_hottype='是',
            kh_hotlevel='无',
            kh_hotfl='最近跟进客户',
            kh_hotmemo='高热',
            kh_type='潜在客户',
            kh_status='客户跟踪',
            kh_sn='KH202106011001',
            kh_handset='16688889999',
            kh_email='youxaing@163.com',
            kh_dingtalk='youxaing',
            kh_tel='8888888',
            kh_weixin='JzSoft',
            kh_qq='88888888',
            kh_skype='Skype',
            kh_wangwang='123123123',
            kh_worktel='16688880000',
            kh_fax='传真',
            kh_pst='266000',
            kh_department='销售部',
            kh_appellation='李总',
            kh_preside='销售',
            kh_headship='厂长',
            kh_web='www.baidu.com',
            kh_befontof='唱跳rap篮球',
            kh_from='电话采访',
            kh_billinfo='未开票',
            kh_info='百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。',
            kh_ralagrade='一等',
            kh_creditgrade='高',
            kh_valrating='高',
            kh_cttype='身份证',
            kh_ctnumber='12312312312312312',
            kh_contype='企业客户联系人',
            kh_remark='备注',
            kh_jibie='一级代理商',
            kh_genzongtime='2021-06-01'
        )
        edit_customer_pool_request = dingtalkjzcrm__1__0_models.EditCustomerPoolRequest(
            datatype=238,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            client.edit_customer_pool_with_options(edit_customer_pool_request, edit_customer_pool_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        edit_customer_pool_headers = dingtalkjzcrm__1__0_models.EditCustomerPoolHeaders()
        edit_customer_pool_headers.x_acs_dingtalk_access_token = '<your access token>'
        data = dingtalkjzcrm__1__0_models.EditCustomerPoolRequestData(
            data_userid='张三',
            kh_pkhid='XX有限公司',
            kh_class='企业客户',
            kh_name='XX科技有限公司',
            kh_sex='女',
            kh_shortname='小刘',
            kh_industry='电子科技',
            kh_employees='50人',
            kh_address='山东省青岛市市南区',
            kh_country='中国',
            kh_province='山东省',
            kh_city='青岛市',
            kh_coaddress='中国山东省青岛市市南区XX街道',
            kh_hottype='是',
            kh_hotlevel='无',
            kh_hotfl='最近跟进客户',
            kh_hotmemo='高热',
            kh_type='潜在客户',
            kh_status='客户跟踪',
            kh_sn='KH202106011001',
            kh_handset='16688889999',
            kh_email='youxaing@163.com',
            kh_dingtalk='youxaing',
            kh_tel='8888888',
            kh_weixin='JzSoft',
            kh_qq='88888888',
            kh_skype='Skype',
            kh_wangwang='123123123',
            kh_worktel='16688880000',
            kh_fax='传真',
            kh_pst='266000',
            kh_department='销售部',
            kh_appellation='李总',
            kh_preside='销售',
            kh_headship='厂长',
            kh_web='www.baidu.com',
            kh_befontof='唱跳rap篮球',
            kh_from='电话采访',
            kh_billinfo='未开票',
            kh_info='百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。',
            kh_ralagrade='一等',
            kh_creditgrade='高',
            kh_valrating='高',
            kh_cttype='身份证',
            kh_ctnumber='12312312312312312',
            kh_contype='企业客户联系人',
            kh_remark='备注',
            kh_jibie='一级代理商',
            kh_genzongtime='2021-06-01'
        )
        edit_customer_pool_request = dingtalkjzcrm__1__0_models.EditCustomerPoolRequest(
            datatype=238,
            stamp=1621822122,
            msgid=1,
            data=data
        )
        try:
            await client.edit_customer_pool_with_options_async(edit_customer_pool_request, edit_customer_pool_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditCustomerPoolHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditCustomerPoolRequest\data;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\EditCustomerPoolRequest;
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
        $editCustomerPoolHeaders = new EditCustomerPoolHeaders([]);
        $editCustomerPoolHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $data = new data([
            "dataUserid" => "张三",
            "khPkhid" => "XX有限公司",
            "khClass" => "企业客户",
            "khName" => "XX科技有限公司",
            "khSex" => "女",
            "khShortname" => "小刘",
            "khIndustry" => "电子科技",
            "khEmployees" => "50人",
            "khAddress" => "山东省青岛市市南区",
            "khCountry" => "中国",
            "khProvince" => "山东省",
            "khCity" => "青岛市",
            "khCoaddress" => "中国山东省青岛市市南区XX街道",
            "khHottype" => "是",
            "khHotlevel" => "无",
            "khHotfl" => "最近跟进客户",
            "khHotmemo" => "高热",
            "khType" => "潜在客户",
            "khStatus" => "客户跟踪",
            "khSn" => "KH202106011001",
            "khHandset" => "16688889999",
            "khEmail" => "youxaing@163.com",
            "khDingtalk" => "youxaing",
            "khTel" => "8888888",
            "khWeixin" => "JzSoft",
            "khQq" => "88888888",
            "khSkype" => "Skype",
            "khWangwang" => "123123123",
            "khWorktel" => "16688880000",
            "khFax" => "传真",
            "khPst" => "266000",
            "khDepartment" => "销售部",
            "khAppellation" => "李总",
            "khPreside" => "销售",
            "khHeadship" => "厂长",
            "khWeb" => "www.baidu.com",
            "khBefontof" => "唱跳rap篮球",
            "khFrom" => "电话采访",
            "khBillinfo" => "未开票",
            "khInfo" => "百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。",
            "khRalagrade" => "一等",
            "khCreditgrade" => "高",
            "khValrating" => "高",
            "khCttype" => "身份证",
            "khCtnumber" => "12312312312312312",
            "khContype" => "企业客户联系人",
            "khRemark" => "备注",
            "khJibie" => "一级代理商",
            "khGenzongtime" => "2021-06-01"
        ]);
        $editCustomerPoolRequest = new EditCustomerPoolRequest([
            "datatype" => 238,
            "stamp" => 1621822122,
            "msgid" => 1,
            "data" => $data
        ]);
        try {
            $client->editCustomerPoolWithOptions($editCustomerPoolRequest, $editCustomerPoolHeaders, new RuntimeOptions([]));
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

  editCustomerPoolHeaders := &dingtalkjzcrm_1_0.EditCustomerPoolHeaders{}
  editCustomerPoolHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  data := &dingtalkjzcrm_1_0.EditCustomerPoolRequestData{
    DataUserid: tea.String("张三"),
    KhPkhid: tea.String("XX有限公司"),
    KhClass: tea.String("企业客户"),
    KhName: tea.String("XX科技有限公司"),
    KhSex: tea.String("女"),
    KhShortname: tea.String("小刘"),
    KhIndustry: tea.String("电子科技"),
    KhEmployees: tea.String("50人"),
    KhAddress: tea.String("山东省青岛市市南区"),
    KhCountry: tea.String("中国"),
    KhProvince: tea.String("山东省"),
    KhCity: tea.String("青岛市"),
    KhCoaddress: tea.String("中国山东省青岛市市南区XX街道"),
    KhHottype: tea.String("是"),
    KhHotlevel: tea.String("无"),
    KhHotfl: tea.String("最近跟进客户"),
    KhHotmemo: tea.String("高热"),
    KhType: tea.String("潜在客户"),
    KhStatus: tea.String("客户跟踪"),
    KhSn: tea.String("KH202106011001"),
    KhHandset: tea.String("16688889999"),
    KhEmail: tea.String("youxaing@163.com"),
    KhDingtalk: tea.String("youxaing"),
    KhTel: tea.String("8888888"),
    KhWeixin: tea.String("JzSoft"),
    KhQq: tea.String("88888888"),
    KhSkype: tea.String("Skype"),
    KhWangwang: tea.String("123123123"),
    KhWorktel: tea.String("16688880000"),
    KhFax: tea.String("传真"),
    KhPst: tea.String("266000"),
    KhDepartment: tea.String("销售部"),
    KhAppellation: tea.String("李总"),
    KhPreside: tea.String("销售"),
    KhHeadship: tea.String("厂长"),
    KhWeb: tea.String("www.baidu.com"),
    KhBefontof: tea.String("唱跳rap篮球"),
    KhFrom: tea.String("电话采访"),
    KhBillinfo: tea.String("未开票"),
    KhInfo: tea.String("百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的���司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。"),
    KhRalagrade: tea.String("一等"),
    KhCreditgrade: tea.String("高"),
    KhValrating: tea.String("高"),
    KhCttype: tea.String("身份证"),
    KhCtnumber: tea.String("12312312312312312"),
    KhContype: tea.String("企业客户联系人"),
    KhRemark: tea.String("备注"),
    KhJibie: tea.String("一级代理商"),
    KhGenzongtime: tea.String("2021-06-01"),
  }
  editCustomerPoolRequest := &dingtalkjzcrm_1_0.EditCustomerPoolRequest{
    Datatype: tea.Int64(238),
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
    _, _err = client.EditCustomerPoolWithOptions(editCustomerPoolRequest, editCustomerPoolHeaders, &util.RuntimeOptions{})
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
    let editCustomerPoolHeaders = new $dingtalkjzcrm_1_0.EditCustomerPoolHeaders({ });
    editCustomerPoolHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let data = new $dingtalkjzcrm_1_0.EditCustomerPoolRequestData({
      dataUserid: "张三",
      khPkhid: "XX有限公司",
      khClass: "企业客户",
      khName: "XX科技有限公司",
      khSex: "女",
      khShortname: "小刘",
      khIndustry: "电子科技",
      khEmployees: "50人",
      khAddress: "山东省青岛市市南区",
      khCountry: "中国",
      khProvince: "山东省",
      khCity: "青岛市",
      khCoaddress: "中国山东省青岛市市南区XX街道",
      khHottype: "是",
      khHotlevel: "无",
      khHotfl: "最近跟进客户",
      khHotmemo: "高热",
      khType: "潜在客户",
      khStatus: "客户跟踪",
      khSn: "KH202106011001",
      khHandset: "16688889999",
      khEmail: "youxaing@163.com",
      khDingtalk: "youxaing",
      khTel: "8888888",
      khWeixin: "JzSoft",
      khQq: "88888888",
      khSkype: "Skype",
      khWangwang: "123123123",
      khWorktel: "16688880000",
      khFax: "传真",
      khPst: "266000",
      khDepartment: "销售部",
      khAppellation: "李总",
      khPreside: "销售",
      khHeadship: "厂长",
      khWeb: "www.baidu.com",
      khBefontof: "唱跳rap篮球",
      khFrom: "电话采访",
      khBillinfo: "未开票",
      khInfo: "百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。",
      khRalagrade: "一等",
      khCreditgrade: "高",
      khValrating: "高",
      khCttype: "身份证",
      khCtnumber: "12312312312312312",
      khContype: "企业客户联系人",
      khRemark: "备注",
      khJibie: "一级代理商",
      khGenzongtime: "2021-06-01",
    });
    let editCustomerPoolRequest = new $dingtalkjzcrm_1_0.EditCustomerPoolRequest({
      datatype: 238,
      stamp: 1621822122,
      msgid: 1,
      data: data,
    });
    try {
      await client.editCustomerPoolWithOptions(editCustomerPoolRequest, editCustomerPoolHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerPoolHeaders editCustomerPoolHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerPoolHeaders();
            editCustomerPoolHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerPoolRequest.EditCustomerPoolRequestData data = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerPoolRequest.EditCustomerPoolRequestData
            {
                DataUserid = "张三",
                KhPkhid = "XX有限公司",
                KhClass = "企业客户",
                KhName = "XX科技有限公司",
                KhSex = "女",
                KhShortname = "小刘",
                KhIndustry = "电子科技",
                KhEmployees = "50人",
                KhAddress = "山东省青岛市市南区",
                KhCountry = "中国",
                KhProvince = "山东省",
                KhCity = "青岛市",
                KhCoaddress = "中国山东省青岛市市南区XX街道",
                KhHottype = "是",
                KhHotlevel = "无",
                KhHotfl = "最近跟进客户",
                KhHotmemo = "高热",
                KhType = "潜在客户",
                KhStatus = "客户跟踪",
                KhSn = "KH202106011001",
                KhHandset = "16688889999",
                KhEmail = "youxaing@163.com",
                KhDingtalk = "youxaing",
                KhTel = "8888888",
                KhWeixin = "JzSoft",
                KhQq = "88888888",
                KhSkype = "Skype",
                KhWangwang = "123123123",
                KhWorktel = "16688880000",
                KhFax = "传真",
                KhPst = "266000",
                KhDepartment = "销售部",
                KhAppellation = "李总",
                KhPreside = "销售",
                KhHeadship = "厂长",
                KhWeb = "www.baidu.com",
                KhBefontof = "唱跳rap篮球",
                KhFrom = "电话采访",
                KhBillinfo = "未开票",
                KhInfo = "百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。",
                KhRalagrade = "一等",
                KhCreditgrade = "高",
                KhValrating = "高",
                KhCttype = "身份证",
                KhCtnumber = "12312312312312312",
                KhContype = "企业客户联系人",
                KhRemark = "备注",
                KhJibie = "一级代理商",
                KhGenzongtime = "2021-06-01",
            };
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerPoolRequest editCustomerPoolRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.EditCustomerPoolRequest
            {
                Datatype = 238,
                Stamp = 1621822122,
                Msgid = 1,
                Data = data,
            };
            try
            {
                client.EditCustomerPoolWithOptions(editCustomerPoolRequest, editCustomerPoolHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerPoolHeaders> editCustomerPoolHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerPoolHeaders>();
  editCustomerPoolHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerPoolRequestData> data = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerPoolRequestData>(map<string, boost::any>({
    {"dataUserid", boost::any(string("张三"))},
    {"khPkhid", boost::any(string("XX有限公司"))},
    {"khClass", boost::any(string("企业客户"))},
    {"khName", boost::any(string("XX科技有限公司"))},
    {"khSex", boost::any(string("女"))},
    {"khShortname", boost::any(string("小刘"))},
    {"khIndustry", boost::any(string("电子科技"))},
    {"khEmployees", boost::any(string("50人"))},
    {"khAddress", boost::any(string("山东省青岛市市南区"))},
    {"khCountry", boost::any(string("中国"))},
    {"khProvince", boost::any(string("山东省"))},
    {"khCity", boost::any(string("青岛市"))},
    {"khCoaddress", boost::any(string("中国山东省青岛市市南区XX街道"))},
    {"khHottype", boost::any(string("是"))},
    {"khHotlevel", boost::any(string("无"))},
    {"khHotfl", boost::any(string("最近跟进客户"))},
    {"khHotmemo", boost::any(string("高热"))},
    {"khType", boost::any(string("潜在客户"))},
    {"khStatus", boost::any(string("客户跟踪"))},
    {"khSn", boost::any(string("KH202106011001"))},
    {"khHandset", boost::any(string("16688889999"))},
    {"khEmail", boost::any(string("youxaing@163.com"))},
    {"khDingtalk", boost::any(string("youxaing"))},
    {"khTel", boost::any(string("8888888"))},
    {"khWeixin", boost::any(string("JzSoft"))},
    {"khQq", boost::any(string("88888888"))},
    {"khSkype", boost::any(string("Skype"))},
    {"khWangwang", boost::any(string("123123123"))},
    {"khWorktel", boost::any(string("16688880000"))},
    {"khFax", boost::any(string("传真"))},
    {"khPst", boost::any(string("266000"))},
    {"khDepartment", boost::any(string("销售部"))},
    {"khAppellation", boost::any(string("李总"))},
    {"khPreside", boost::any(string("销售"))},
    {"khHeadship", boost::any(string("厂长"))},
    {"khWeb", boost::any(string("www.baidu.com"))},
    {"khBefontof", boost::any(string("唱跳rap篮球"))},
    {"khFrom", boost::any(string("电话采访"))},
    {"khBillinfo", boost::any(string("未开票"))},
    {"khInfo", boost::any(string("百度是拥有强大互联网基础的领先AI公司。是全球为数不多的提供AI芯片、软件架构和应用程序等全栈AI技术的公司之一，被国际机构评为全球四大AI公司之一。百度以“用科技让复杂的世界更简单”为使命，坚持技术创新，致力于“成为最懂用户，并能帮助人们成长的全球顶级高科技公司”。"))},
    {"khRalagrade", boost::any(string("一等"))},
    {"khCreditgrade", boost::any(string("高"))},
    {"khValrating", boost::any(string("高"))},
    {"khCttype", boost::any(string("身份证"))},
    {"khCtnumber", boost::any(string("12312312312312312"))},
    {"khContype", boost::any(string("企业客户联系人"))},
    {"khRemark", boost::any(string("备注"))},
    {"khJibie", boost::any(string("一级代理商"))},
    {"khGenzongtime", boost::any(string("2021-06-01"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerPoolRequest> editCustomerPoolRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::EditCustomerPoolRequest>(map<string, boost::any>({
    {"datatype", boost::any(238)},
    {"stamp", boost::any(1621822122)},
    {"msgid", boost::any(1)},
    {"data", !data ? boost::any() : boost::any(*data)}
  }));
  try {
    client->editCustomerPoolWithOptions(editCustomerPoolRequest, editCustomerPoolHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
