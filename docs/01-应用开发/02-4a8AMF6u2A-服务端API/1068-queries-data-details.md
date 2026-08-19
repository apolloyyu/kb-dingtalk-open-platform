---
title: "获取数据详情"
source_url: "https://open.dingtalk.com/document/development/queries-data-details"
namespace: "development"
slug: "queries-data-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 金智CRM > 数据 > 获取数据详情"
doc_id: "nDgHPhodFf"
updated_at: "2026-01-29 14:19:40"
---

> Source: https://open.dingtalk.com/document/development/queries-data-details
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 金智CRM > 数据 > 获取数据详情
> Updated: 2026-01-29 14:19:40

# 获取数据详情

调用本接口获取金智CRM中指定单据类型的字段定义及数据详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/jzcrm/dataView |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Jzcrm.Common.ReadWrite-金智CRM数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| datatype | String | 是 | 数据类型。 |
| msgid | Long | 是 | 数据ID。 |

### 请求示例

HTTP

```
GET /v1.0/jzcrm/dataView?datatype=150&msgid=1 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:159961ef7e2f3639zv1jjr76df97e21c
Content-Type:application/json
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
        GetDataViewHeaders getDataViewHeaders = new GetDataViewHeaders();
        getDataViewHeaders.xAcsDingtalkAccessToken = "<your access token>";
        GetDataViewRequest getDataViewRequest = new GetDataViewRequest()
                .setDatatype("150")
                .setMsgid(1L);
        try {
            client.getDataViewWithOptions(getDataViewRequest, getDataViewHeaders, new RuntimeOptions());
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
        get_data_view_headers = dingtalkjzcrm__1__0_models.GetDataViewHeaders()
        get_data_view_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_data_view_request = dingtalkjzcrm__1__0_models.GetDataViewRequest(
            datatype='150',
            msgid=1
        )
        try:
            client.get_data_view_with_options(get_data_view_request, get_data_view_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_data_view_headers = dingtalkjzcrm__1__0_models.GetDataViewHeaders()
        get_data_view_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_data_view_request = dingtalkjzcrm__1__0_models.GetDataViewRequest(
            datatype='150',
            msgid=1
        )
        try:
            await client.get_data_view_with_options_async(get_data_view_request, get_data_view_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\GetDataViewHeaders;
use AlibabaCloud\SDK\Dingtalk\Vjzcrm_1_0\Models\GetDataViewRequest;
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
        $getDataViewHeaders = new GetDataViewHeaders([]);
        $getDataViewHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getDataViewRequest = new GetDataViewRequest([
            "datatype" => "150",
            "msgid" => 1
        ]);
        try {
            $client->getDataViewWithOptions($getDataViewRequest, $getDataViewHeaders, new RuntimeOptions([]));
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

  getDataViewHeaders := &dingtalkjzcrm_1_0.GetDataViewHeaders{}
  getDataViewHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getDataViewRequest := &dingtalkjzcrm_1_0.GetDataViewRequest{
    Datatype: tea.String("150"),
    Msgid: tea.Int64(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetDataViewWithOptions(getDataViewRequest, getDataViewHeaders, &util.RuntimeOptions{})
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
    let getDataViewHeaders = new $dingtalkjzcrm_1_0.GetDataViewHeaders({ });
    getDataViewHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let getDataViewRequest = new $dingtalkjzcrm_1_0.GetDataViewRequest({
      datatype: "150",
      msgid: 1,
    });
    try {
      await client.getDataViewWithOptions(getDataViewRequest, getDataViewHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataViewHeaders getDataViewHeaders = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataViewHeaders();
            getDataViewHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataViewRequest getDataViewRequest = new AlibabaCloud.SDK.Dingtalkjzcrm_1_0.Models.GetDataViewRequest
            {
                Datatype = "150",
                Msgid = 1,
            };
            try
            {
                client.GetDataViewWithOptions(getDataViewRequest, getDataViewHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::GetDataViewHeaders> getDataViewHeaders = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::GetDataViewHeaders>();
  getDataViewHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkjzcrm_1_0::GetDataViewRequest> getDataViewRequest = make_shared<Alibabacloud_Dingtalkjzcrm_1_0::GetDataViewRequest>(map<string, boost::any>({
    {"datatype", boost::any(string("150"))},
    {"msgid", boost::any(1)}
  }));
  try {
    client->getDataViewWithOptions(getDataViewRequest, getDataViewHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| data | Object | 数据详情。 |
| detail | Map<String, String> | 数据详情。 |
| dataname | Map<String, Map> | 字段明细。 |
|  | Map | 字段明细。 |
| time | String | 响应时间。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "time": "2021-06-01 11:11:03",
  "success": true,
  "errcode": "0",
  "errmsg": "",
  "dataname": {
    "kh_id": "ID",
    "kh_pkhid": "上级客户",
    "readempid": "共享(读)",
    "writeempid": "共享(写)",
    "kh_class": "类别",
    "kh_name": "客户名称",
    "kh_sex": "性别",
    "kh_shortname": "助记简称",
    "kh_industry": "行业",
    "kh_employees": "人员规模",
    "kh_address": "家庭地址",
    "kh_country": "国家地区",
    "kh_province": "省份",
    "kh_city": "城市",
    "kh_coaddress": "单位地址",
    "kh_hottype": "热点客户",
    "kh_hotlevel": "热度",
    "kh_hotfl": "热点分类",
    "kh_hotmemo": "热点说明",
    "kh_type": "种类",
    "kh_status": "阶段",
    "kh_sn": "编号",
    "kh_handset": "手机",
    "kh_email": "邮箱",
    "kh_dingtalk": "钉钉号",
    "kh_tel": "家庭电话",
    "kh_weixin": "微信号",
    "kh_qq": "QQ",
    "kh_skype": "Skype",
    "kh_wangwang": "旺旺",
    "kh_worktel": "工作电话",
    "kh_fax": "传真",
    "kh_pst": "邮编",
    "kh_department": "部门",
    "kh_appellation": "称谓",
    "kh_preside": "负责业务",
    "kh_headship": "职务",
    "kh_web": "网址",
    "kh_befontof": "爱好",
    "kh_from": "来源",
    "kh_billinfo": "开票资料",
    "kh_info": "公司简介",
    "kh_ralagrade": "关系等级",
    "kh_creditgrade": "信用等级",
    "kh_valrating": "价值评估",
    "kh_contype": "联系人分类",
    "kh_cttype": "证件类型",
    "kh_ctnumber": "证件号码",
    "kh_remark": "备注",
    "kh_jibie": "客户级别",
    "kh_huishoucount": "回收次数",
    "data_userid": "所属员工",
    "kh_yopuser": "原属员工",
    "addtime": "创建时间",
    "kh_fenpeitime": "分配领用日期",
    "kh_genzongtime": "最后跟踪",
    "shenhestate": "审核状态",
    "kh_markclass": "类型",
  },
  "data": {
    "detail": {
      "kh_id": "252",
      "kh_pkhid": {
        "title": "",
        "id": "0",
        "number": ""
      },
      "readempid": "",
      "writeempid": "张三",
      "kh_class": "个人客户",
      "kh_name": "客户123456",
      "kh_sex": "",
      "kh_shortname": "客户",
      "kh_industry": "",
      "kh_employees": "",
      "kh_address": "",
      "kh_country": "",
      "kh_province": "",
      "kh_city": "",
      "kh_coaddress": "",
      "kh_hottype": "否",
      "kh_hotlevel": "无",
      "kh_hotfl": "",
      "kh_hotmemo": "",
      "kh_type": "",
      "kh_status": "",
      "kh_sn": "",
      "kh_handset": "13827280005",
      "kh_email": "",
      "kh_dingtalk": "",
      "kh_tel": "",
      "kh_weixin": "",
      "kh_qq": "",
      "kh_skype": "",
      "kh_wangwang": "",
      "kh_worktel": "",
      "kh_fax": "",
      "kh_pst": "",
      "kh_department": "",
      "kh_appellation": "",
      "kh_preside": "",
      "kh_headship": "",
      "kh_web": "",
      "kh_befontof": "",
      "kh_from": "",
      "kh_billinfo": "",
      "kh_info": "",
      "kh_ralagrade": "",
      "kh_creditgrade": "",
      "kh_valrating": "",
      "kh_contype": "",
      "kh_cttype": "",
      "kh_ctnumber": "",
      "kh_remark": "",
      "kh_jibie": "",
      "kh_huishoucount": "0",
      "data_userid": "张三",
      "kh_yopuser": "",
      "addtime": "2021/5/21 20:41:36",
      "kh_fenpeitime": "2021/5/24 15:11:46",
      "kh_genzongtime": "2021/6/1 9:53:06",
      "shenhestate": "",
      "kh_markclass": "0",
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | notFound | 未查询到指定数据%s | 未查询到指定数据%s |
| 400 | invalidRequestMethod | 请求方式错误，必须为post请求！ | 请求方式错误，必须为post请求！ |
| 400 | invalidParameter | 请求参数缺失或无效！ | 请求参数缺失或无效！ |
| 400 | invalidSeCretKey | 无效的SeCretKey | 无效的SeCretKey |
| 400 | invalidSign | 签名无效 | 签名无效 |
