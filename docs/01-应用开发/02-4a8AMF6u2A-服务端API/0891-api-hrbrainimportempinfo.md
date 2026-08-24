---
title: "数据集成人员信息同步"
source_url: "https://open.dingtalk.com/document/development/api-hrbrainimportempinfo"
namespace: "development"
slug: "api-hrbrainimportempinfo"
group: "应用开发"
tab: "服务端API"
breadcrumb: "组织大脑 > 数据集成 > 组织与人员 > 数据集成人员信息同步"
doc_id: "ve0OHgSwcG"
updated_at: "2026-06-04 19:10:09"
---

> Source: https://open.dingtalk.com/document/development/api-hrbrainimportempinfo
> Path: 应用开发 / 服务端API / 组织大脑 > 数据集成 > 组织与人员 > 数据集成人员信息同步
> Updated: 2026-06-04 19:10:09

# 数据集成人员信息同步

调用本接口，人员信息同步至组织大脑，支持批量同步。

## 接口调用说明

为了确保你在使用接口时能够顺利进行数据交互，请务必检查对应数据模型是否设置枚举值的范围。这一操作需要在组织大脑[管理后台](https://hrbrain.dingtalk.com/hrbrain/management/data-integration/model-management/basic-modal/detail?modelCode=hrbrain_import_dimission&status=read&detailNav=%5B%22modelList%22%2C%22detail%22%5D)的数据集成 > 模型管理的对应数据模型中进行查看，如果未正确设置枚举值范围，调用接口时可能会遇到错误信息。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrbrain/datas/empInfos/import |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrbrain.Import.Write-组织大脑数据集成写入权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| corpId | String | 是 | 组织编码。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
|  | Array | 是 | 数据集。 |
| name | String | 是 | 姓名。 |
| workNo | String | 是 | 钉钉 UserId。 |
| gender | String | 是 | 性别。 |
| birthday | String | 是 | 出生日期。 |
| nation | String | 是 | 民族。 |
| nationCtry | String | 是 | 国籍。 |
| politicalStatus | String | 是 | 政治面貌。 |
| marriage | String | 否 | 婚姻状态。 |
| workEmail | String | 否 | 工作邮箱。 |
| empType | String | 是 | 员工类型。 |
| empStatus | String | 是 | 雇佣状态。 |
| empSource | String | 是 | 招聘来源。 |
| jobLevel | String | 否 | 职级。 |
| jobCodeName | String | 是 | 职务。 |
| postName | String | 是 | 职位。 |
| deptNo | String | 是 | 部门编码。 |
| deptName | String | 是 | 部门名称。 |
| superEmpId | String | 否 | 直接主管标识。 |
| superName | String | 否 | 直接主管姓名。 |
| workLocCity | String | 否 | 工作所在城市。 |
| workLocAddr | String | 否 | 工作地址。 |
| registDate | String | 否 | 入职日期。 |
| regularDate | String | 否 | 转正时间。 |
| isDimission | String | 否 | 是否离职。 |
| dimissionDate | String | 否 | 离职日期。 |
| highestEduName | String | 否 | 最高学历。 |
| highestDegree | String | 否 | 最高学位。 |
| lastSchoolName | String | 否 | 毕业院校名。 |
| extendInfo | Map | 否 | 扩展字段，KV结构。 |

### 请求示例

HTTP

```
POST /v1.0/hrbrain/datas/empInfos/import?corpId=ding3b*********88 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:480021443f9f37fcbf464c4a6b85d299
Content-Type:application/json

[ {
  "name" : "张三",
  "workNo" : "14530201131175645",
  "gender" : "男",
  "birthday" : "1986-10-02",
  "nation" : "汉族",
  "nationCtry" : "中国",
  "politicalStatus" : "党员",
  "marriage" : "已婚",
  "workEmail" : "xxx@gmail.com",
  "empType" : "正式全职",
  "empStatus" : "在职",
  "empSource" : "社招",
  "jobLevel" : "P8",
  "jobCodeName" : "产品",
  "postName" : "后端开发工程师",
  "deptNo" : "10010",
  "deptName" : "组织发展&变革",
  "superEmpId" : "122230324",
  "superName" : "李四",
  "workLocCity" : "杭州",
  "workLocAddr" : "杭州余杭",
  "registDate" : "2023-02-02",
  "regularDate" : "2023-05-03",
  "isDimission" : "否",
  "dimissionDate" : "2024-03-01",
  "highestEduName" : "本科",
  "highestDegree" : "学士学位",
  "lastSchoolName" : "清华大学"
} ]
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrbrain_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrbrain_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrbrain_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportEmpInfoHeaders hrbrainImportEmpInfoHeaders = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportEmpInfoHeaders();
        hrbrainImportEmpInfoHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportEmpInfoRequest.HrbrainImportEmpInfoRequestBody body0 = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportEmpInfoRequest.HrbrainImportEmpInfoRequestBody()
                .setName("张三")
                .setWorkNo("14530201131175645")
                .setGender("男")
                .setBirthday("1986-10-02")
                .setNation("汉族")
                .setNationCtry("中国")
                .setPoliticalStatus("党员")
                .setMarriage("已婚")
                .setWorkEmail("xxx@gmail.com")
                .setEmpType("正式全职")
                .setEmpStatus("在职")
                .setEmpSource("社招")
                .setJobLevel("P8")
                .setJobCodeName("产品")
                .setPostName("后端开发工程师")
                .setDeptNo("10010")
                .setDeptName("组织发展&变革")
                .setSuperEmpId("122230324")
                .setSuperName("李四")
                .setWorkLocCity("杭州")
                .setWorkLocAddr("杭州余杭")
                .setRegistDate("2023-02-02")
                .setRegularDate("2023-05-03")
                .setIsDimission("否")
                .setDimissionDate("2024-03-01")
                .setHighestEduName("本科")
                .setHighestDegree("学士学位")
                .setLastSchoolName("清华大学");
        com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportEmpInfoRequest hrbrainImportEmpInfoRequest = new com.aliyun.dingtalkhrbrain_1_0.models.HrbrainImportEmpInfoRequest()
                .setCorpId("ding3b*********88")
                .setBody(java.util.Arrays.asList(
                    body0
                ));
        try {
            client.hrbrainImportEmpInfoWithOptions(hrbrainImportEmpInfoRequest, hrbrainImportEmpInfoHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import os
import sys

from typing import List

from alibabacloud_dingtalk.hrbrain_1_0.client import Client as dingtalkhrbrain_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrbrain_1_0 import models as dingtalkhrbrain__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrbrain_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrbrain_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_emp_info_headers = dingtalkhrbrain__1__0_models.HrbrainImportEmpInfoHeaders()
        hrbrain_import_emp_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportEmpInfoRequestBody(
            name='张三',
            work_no='14530201131175645',
            gender='男',
            birthday='1986-10-02',
            nation='汉族',
            nation_ctry='中国',
            political_status='党员',
            marriage='已婚',
            work_email='xxx@gmail.com',
            emp_type='正式全职',
            emp_status='在职',
            emp_source='社招',
            job_level='P8',
            job_code_name='产品',
            post_name='后端开发工程师',
            dept_no='10010',
            dept_name='组织发展&变革',
            super_emp_id='122230324',
            super_name='李四',
            work_loc_city='杭州',
            work_loc_addr='杭州余杭',
            regist_date='2023-02-02',
            regular_date='2023-05-03',
            is_dimission='否',
            dimission_date='2024-03-01',
            highest_edu_name='本科',
            highest_degree='学士学位',
            last_school_name='清华大学'
        )
        hrbrain_import_emp_info_request = dingtalkhrbrain__1__0_models.HrbrainImportEmpInfoRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            client.hrbrain_import_emp_info_with_options(hrbrain_import_emp_info_request, hrbrain_import_emp_info_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrbrain_import_emp_info_headers = dingtalkhrbrain__1__0_models.HrbrainImportEmpInfoHeaders()
        hrbrain_import_emp_info_headers.x_acs_dingtalk_access_token = '<your access token>'
        body_0 = dingtalkhrbrain__1__0_models.HrbrainImportEmpInfoRequestBody(
            name='张三',
            work_no='14530201131175645',
            gender='男',
            birthday='1986-10-02',
            nation='汉族',
            nation_ctry='中国',
            political_status='党员',
            marriage='已婚',
            work_email='xxx@gmail.com',
            emp_type='正式全职',
            emp_status='在职',
            emp_source='社招',
            job_level='P8',
            job_code_name='产品',
            post_name='后端开发工程师',
            dept_no='10010',
            dept_name='组织发展&变革',
            super_emp_id='122230324',
            super_name='李四',
            work_loc_city='杭州',
            work_loc_addr='杭州余杭',
            regist_date='2023-02-02',
            regular_date='2023-05-03',
            is_dimission='否',
            dimission_date='2024-03-01',
            highest_edu_name='本科',
            highest_degree='学士学位',
            last_school_name='清华大学'
        )
        hrbrain_import_emp_info_request = dingtalkhrbrain__1__0_models.HrbrainImportEmpInfoRequest(
            corp_id='ding3b*********88',
            body=[
                body_0
            ]
        )
        try:
            await client.hrbrain_import_emp_info_with_options_async(hrbrain_import_emp_info_request, hrbrain_import_emp_info_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportEmpInfoHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportEmpInfoRequest\body;
use AlibabaCloud\SDK\Dingtalk\Vhrbrain_1_0\Models\HrbrainImportEmpInfoRequest;
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
        $hrbrainImportEmpInfoHeaders = new HrbrainImportEmpInfoHeaders([]);
        $hrbrainImportEmpInfoHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $body0 = new body([
            "name" => "张三",
            "workNo" => "14530201131175645",
            "gender" => "男",
            "birthday" => "1986-10-02",
            "nation" => "汉族",
            "nationCtry" => "中国",
            "politicalStatus" => "党员",
            "marriage" => "已婚",
            "workEmail" => "xxx@gmail.com",
            "empType" => "正式全职",
            "empStatus" => "在职",
            "empSource" => "社招",
            "jobLevel" => "P8",
            "jobCodeName" => "产品",
            "postName" => "后端开发工程师",
            "deptNo" => "10010",
            "deptName" => "组织发展&变革",
            "superEmpId" => "122230324",
            "superName" => "李四",
            "workLocCity" => "杭州",
            "workLocAddr" => "杭州余杭",
            "registDate" => "2023-02-02",
            "regularDate" => "2023-05-03",
            "isDimission" => "否",
            "dimissionDate" => "2024-03-01",
            "highestEduName" => "本科",
            "highestDegree" => "学士学位",
            "lastSchoolName" => "清华大学"
        ]);
        $hrbrainImportEmpInfoRequest = new HrbrainImportEmpInfoRequest([
            "corpId" => "ding3b*********88",
            "body" => [
                $body0
            ]
        ]);
        try {
            $client->hrbrainImportEmpInfoWithOptions($hrbrainImportEmpInfoRequest, $hrbrainImportEmpInfoHeaders, new RuntimeOptions([]));
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
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkhrbrain_1_0  "github.com/alibabacloud-go/dingtalk/hrbrain_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkhrbrain_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrbrain_1_0.Client{}
  _result, _err = dingtalkhrbrain_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrbrainImportEmpInfoHeaders := &dingtalkhrbrain_1_0.HrbrainImportEmpInfoHeaders{}
  hrbrainImportEmpInfoHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  body0 := &dingtalkhrbrain_1_0.HrbrainImportEmpInfoRequestBody{
    Name: tea.String("张三"),
    WorkNo: tea.String("14530201131175645"),
    Gender: tea.String("男"),
    Birthday: tea.String("1986-10-02"),
    Nation: tea.String("汉族"),
    NationCtry: tea.String("中国"),
    PoliticalStatus: tea.String("党员"),
    Marriage: tea.String("已婚"),
    WorkEmail: tea.String("xxx@gmail.com"),
    EmpType: tea.String("正式全职"),
    EmpStatus: tea.String("在职"),
    EmpSource: tea.String("社招"),
    JobLevel: tea.String("P8"),
    JobCodeName: tea.String("产品"),
    PostName: tea.String("后端开发工程师"),
    DeptNo: tea.String("10010"),
    DeptName: tea.String("组织发展&变革"),
    SuperEmpId: tea.String("122230324"),
    SuperName: tea.String("李四"),
    WorkLocCity: tea.String("杭州"),
    WorkLocAddr: tea.String("杭州余杭"),
    RegistDate: tea.String("2023-02-02"),
    RegularDate: tea.String("2023-05-03"),
    IsDimission: tea.String("否"),
    DimissionDate: tea.String("2024-03-01"),
    HighestEduName: tea.String("本科"),
    HighestDegree: tea.String("学士学位"),
    LastSchoolName: tea.String("清华大学"),
  }
  hrbrainImportEmpInfoRequest := &dingtalkhrbrain_1_0.HrbrainImportEmpInfoRequest{
    CorpId: tea.String("ding3b*********88"),
    Body: []*dingtalkhrbrain_1_0.HrbrainImportEmpInfoRequestBody{body0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrbrainImportEmpInfoWithOptions(hrbrainImportEmpInfoRequest, hrbrainImportEmpInfoHeaders, &util.RuntimeOptions{})
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
'use strict';
// This file is auto-generated, don't edit it
const Util = require('@alicloud/tea-util');
const dingtalkhrbrain_1_0 = require('@alicloud/dingtalk/hrbrain_1_0');
const OpenApi = require('@alicloud/openapi-client');
const Tea = require('@alicloud/tea-typescript');

class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient() {
    let config = new OpenApi.Config({ });
    config.protocol = 'https';
    config.regionId = 'central';
    return new dingtalkhrbrain_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let hrbrainImportEmpInfoHeaders = new dingtalkhrbrain_1_0.HrbrainImportEmpInfoHeaders({ });
    hrbrainImportEmpInfoHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let body0 = new dingtalkhrbrain_1_0.HrbrainImportEmpInfoRequestBody({
      name: '张三',
      workNo: '14530201131175645',
      gender: '男',
      birthday: '1986-10-02',
      nation: '汉族',
      nationCtry: '中国',
      politicalStatus: '党员',
      marriage: '已婚',
      workEmail: 'xxx@gmail.com',
      empType: '正式全职',
      empStatus: '在职',
      empSource: '社招',
      jobLevel: 'P8',
      jobCodeName: '产品',
      postName: '后端开发工程师',
      deptNo: '10010',
      deptName: '组织发展&变革',
      superEmpId: '122230324',
      superName: '李四',
      workLocCity: '杭州',
      workLocAddr: '杭州余杭',
      registDate: '2023-02-02',
      regularDate: '2023-05-03',
      isDimission: '否',
      dimissionDate: '2024-03-01',
      highestEduName: '本科',
      highestDegree: '学士学位',
      lastSchoolName: '清华大学',
    });
    let hrbrainImportEmpInfoRequest = new dingtalkhrbrain_1_0.HrbrainImportEmpInfoRequest({
      corpId: 'ding3b*********88',
      body: [
        body0
      ],
    });
    try {
      await client.hrbrainImportEmpInfoWithOptions(hrbrainImportEmpInfoRequest, hrbrainImportEmpInfoHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.empty(err.code) && !Util.empty(err.message)) {
        // err 中含有 code 和 message 属性，可帮助开发定位问题
      }

    }    
  }

}

exports.Client = Client;
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
        public static AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoHeaders hrbrainImportEmpInfoHeaders = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoHeaders();
            hrbrainImportEmpInfoHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoRequest.HrbrainImportEmpInfoRequestBody body0 = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoRequest.HrbrainImportEmpInfoRequestBody
            {
                Name = "张三",
                WorkNo = "14530201131175645",
                Gender = "男",
                Birthday = "1986-10-02",
                Nation = "汉族",
                NationCtry = "中国",
                PoliticalStatus = "党员",
                Marriage = "已婚",
                WorkEmail = "xxx@gmail.com",
                EmpType = "正式全职",
                EmpStatus = "在职",
                EmpSource = "社招",
                JobLevel = "P8",
                JobCodeName = "产品",
                PostName = "后端开发工程师",
                DeptNo = "10010",
                DeptName = "组织发展&变革",
                SuperEmpId = "122230324",
                SuperName = "李四",
                WorkLocCity = "杭州",
                WorkLocAddr = "杭州余杭",
                RegistDate = "2023-02-02",
                RegularDate = "2023-05-03",
                IsDimission = "否",
                DimissionDate = "2024-03-01",
                HighestEduName = "本科",
                HighestDegree = "学士学位",
                LastSchoolName = "清华大学",
            };
            AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoRequest hrbrainImportEmpInfoRequest = new AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoRequest
            {
                CorpId = "ding3b*********88",
                Body = new List<AlibabaCloud.SDK.Dingtalkhrbrain_1_0.Models.HrbrainImportEmpInfoRequest.HrbrainImportEmpInfoRequestBody>
                {
                    body0
                },
            };
            try
            {
                client.HrbrainImportEmpInfoWithOptions(hrbrainImportEmpInfoRequest, hrbrainImportEmpInfoHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| result | Boolean | 更新是否成功：   - true：成功 - false：失败 |
| success | Boolean | 接口调用是否成功：   - true：成功 - false：失败 |
| requestId | String | 请求 ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true,
  "success" : true,
  "requestId" : "5fa4461a87e9a0f0606a3f9aa0766998"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | serviceError | service error. %s | 执行异常 |
| 401 | paramIllegal | param illegal. %s | 入参错误 |
