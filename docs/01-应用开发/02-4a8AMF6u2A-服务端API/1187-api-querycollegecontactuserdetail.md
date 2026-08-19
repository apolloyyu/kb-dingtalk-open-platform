---
title: "查询用户信息详情"
source_url: "https://open.dingtalk.com/document/development/api-querycollegecontactuserdetail"
namespace: "development"
slug: "api-querycollegecontactuserdetail"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 查询用户信息详情"
doc_id: "qp4adKApfn"
updated_at: "2025-09-23 19:23:26"
---

> Source: https://open.dingtalk.com/document/development/api-querycollegecontactuserdetail
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 查询用户信息详情
> Updated: 2025-09-23 19:23:26

# 查询用户信息详情

获取指定用户的详细信息。该接口不区分高校账号和个人账号，部分字段仅为高校账号时返回，注意甄别。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/users |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Edu.College.Contact.Read-钉钉教育高校通讯录读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userid | String | 否 | 员工唯一标识ID（不可修改），企业内必须唯一。 |
| jobNumber | String | 否 | 学号/职工号(可以修改)，学校内必须唯一。  **[!NOTE]**    与userid二选一，都传入时以userid为准。 |
| language | String | 否 | 通讯录语言：   - zh\_CN：中文（默认值） - en\_US：英文 |

### 请求示例

HTTP

```
GET /v1.0/edu/collegeContact/users?userid=zhangsan666&jobNumber=12122294&language=zh_CN HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:be3Fxxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;

public class Sample {

    /**
     * <b>description</b> :
     * <p>使用 Token 初始化账号Client</p>
     * @return Client
     * 
     * @throws Exception
     */
    public static com.aliyun.dingtalkedu_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkedu_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkedu_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkedu_1_0.models.QueryCollegeContactUserDetailHeaders queryCollegeContactUserDetailHeaders = new com.aliyun.dingtalkedu_1_0.models.QueryCollegeContactUserDetailHeaders();
        queryCollegeContactUserDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.QueryCollegeContactUserDetailRequest queryCollegeContactUserDetailRequest = new com.aliyun.dingtalkedu_1_0.models.QueryCollegeContactUserDetailRequest()
                .setUserid("zhangsan666")
                .setJobNumber("12122294")
                .setLanguage("zh_CN");
        try {
            client.queryCollegeContactUserDetailWithOptions(queryCollegeContactUserDetailRequest, queryCollegeContactUserDetailHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.edu_1_0.client import Client as dingtalkedu_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.edu_1_0 import models as dingtalkedu__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkedu_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkedu_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_college_contact_user_detail_headers = dingtalkedu__1__0_models.QueryCollegeContactUserDetailHeaders()
        query_college_contact_user_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_college_contact_user_detail_request = dingtalkedu__1__0_models.QueryCollegeContactUserDetailRequest(
            userid='zhangsan666',
            job_number='12122294',
            language='zh_CN'
        )
        try:
            client.query_college_contact_user_detail_with_options(query_college_contact_user_detail_request, query_college_contact_user_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_college_contact_user_detail_headers = dingtalkedu__1__0_models.QueryCollegeContactUserDetailHeaders()
        query_college_contact_user_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_college_contact_user_detail_request = dingtalkedu__1__0_models.QueryCollegeContactUserDetailRequest(
            userid='zhangsan666',
            job_number='12122294',
            language='zh_CN'
        )
        try:
            await client.query_college_contact_user_detail_with_options_async(query_college_contact_user_detail_request, query_college_contact_user_detail_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\QueryCollegeContactUserDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\QueryCollegeContactUserDetailRequest;
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
        $queryCollegeContactUserDetailHeaders = new QueryCollegeContactUserDetailHeaders([]);
        $queryCollegeContactUserDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $queryCollegeContactUserDetailRequest = new QueryCollegeContactUserDetailRequest([
            "userid" => "zhangsan666",
            "jobNumber" => "12122294",
            "language" => "zh_CN"
        ]);
        try {
            $client->queryCollegeContactUserDetailWithOptions($queryCollegeContactUserDetailRequest, $queryCollegeContactUserDetailHeaders, new RuntimeOptions([]));
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
  dingtalkedu_1_0  "github.com/alibabacloud-go/dingtalk/edu_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

// Description:
// 
// 使用 Token 初始化账号Client
// 
// @return Client
// 
// @throws Exception
func CreateClient () (_result *dingtalkedu_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkedu_1_0.Client{}
  _result, _err = dingtalkedu_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  queryCollegeContactUserDetailHeaders := &dingtalkedu_1_0.QueryCollegeContactUserDetailHeaders{}
  queryCollegeContactUserDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  queryCollegeContactUserDetailRequest := &dingtalkedu_1_0.QueryCollegeContactUserDetailRequest{
    Userid: tea.String("zhangsan666"),
    JobNumber: tea.String("12122294"),
    Language: tea.String("zh_CN"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QueryCollegeContactUserDetailWithOptions(queryCollegeContactUserDetailRequest, queryCollegeContactUserDetailHeaders, &util.RuntimeOptions{})
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
const dingtalkedu_1_0 = require('@alicloud/dingtalk/edu_1_0');
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
    return new dingtalkedu_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let queryCollegeContactUserDetailHeaders = new dingtalkedu_1_0.QueryCollegeContactUserDetailHeaders({ });
    queryCollegeContactUserDetailHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let queryCollegeContactUserDetailRequest = new dingtalkedu_1_0.QueryCollegeContactUserDetailRequest({
      userid: 'zhangsan666',
      jobNumber: '12122294',
      language: 'zh_CN',
    });
    try {
      await client.queryCollegeContactUserDetailWithOptions(queryCollegeContactUserDetailRequest, queryCollegeContactUserDetailHeaders, new Util.RuntimeOptions({ }));
    } catch (err) {
      if (!Util.default.empty(err.code) && !Util.default.empty(err.message)) {
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

        /// <term><b>Description:</b></term>
        /// <description>
        /// <para>使用 Token 初始化账号Client</para>
        /// </description>
        /// 
        /// <returns>
        /// Client
        /// </returns>
        /// 
        /// <term><b>Exception:</b></term>
        /// Exception
        public static AlibabaCloud.SDK.Dingtalkedu_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkedu_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkedu_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.QueryCollegeContactUserDetailHeaders queryCollegeContactUserDetailHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.QueryCollegeContactUserDetailHeaders();
            queryCollegeContactUserDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.QueryCollegeContactUserDetailRequest queryCollegeContactUserDetailRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.QueryCollegeContactUserDetailRequest
            {
                Userid = "zhangsan666",
                JobNumber = "12122294",
                Language = "zh_CN",
            };
            try
            {
                client.QueryCollegeContactUserDetailWithOptions(queryCollegeContactUserDetailRequest, queryCollegeContactUserDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 是否成功。 |
| result | Object | 返回结果。 |
| userid | String | 员工的userId。 |
| unionId | String | 员工在当前开发者企业账号范围内的唯一标识。 |
| name | String | 员工姓名。 |
| avatar | String | 头像。 |
| empType | String | 成员类型：   - college\_student：学生 - college\_teacher：教职工 |
| stateCode | String | 电话区号。 |
| mobile | String | 手机号码。 |
| managerUserid | String | 员工的直属主管。 |
| hideMobile | Boolean | 是否号码隐藏：   - true：隐藏 - false：不隐藏 |
| telephone | String | 分机号。 |
| jobNumber | String | 学号/职工号。 |
| title | String | 职位。 |
| email | String | 员工邮箱。 |
| workPlace | String | 办公地点。 |
| remark | String | 备注。 |
| exclusiveAccount | Boolean | 是否是高校账号：   - true：是 - false：不是 |
| orgEmail | String | 员工的企业邮箱。  **[!NOTE]**    如果员工的企业邮箱没有开通，返回信息中不包含该数据。 |
| deptIdList | Array of Long | 部门id。 |
| mainDeptId | Long | 主部门id。 |
| deptOrderList | Array | 所属部门id列表。 |
| deptId | Long | 部门id。 |
| order | Integer | 员工在部门中的排序。 |
| deptTypeSet | Array | 部门所属架构信息。 |
| deptId | Long | 部门id。 |
| deptName | String | 部门名称。 |
| deptType | String | 部门类型。  `具体部门类型枚举可见高校通讯录获取部门类型接口。` |
| deptStructType | String | 部门所属架构类型。  stru\_standard\_dept：行政组织架构  `具体架构类型枚举可见高校通讯录部门接口。` |
| structDeptId | Long | 所属架构部门id。 |
| extension | String | 扩展属性，最大长度2000个字符。 具体支持的字段可见成员信息管理  `身份证号在该字段内不返回` |
| hiredDate | Long | 入职时间，Unix时间戳，单位毫秒。 |
| active | Boolean | 是否激活了钉钉：   - true：已激活 - false：未激活 |
| realAuthed | Boolean | 是否完成了实名认证：   - true：已认证 - false：未认证 |
| senior | Boolean | 是否为企业的高管：   - true：是 - false：不是 |
| admin | Boolean | 是否为企业的管理员：   - true：是 - false：不是 |
| boss | Boolean | 是否为企业的老板：   - true：是 - false：不是 |
| orgEmailType | String | 员工的企业邮箱类型：   - profession：标准版 - base：基础版 |
| leaderInDept | Array | 员工在对应的部门中是否是领导：   - true：是 - false：不是 |
| deptId | Long | 部门ID。 |
| leader | Boolean | 是否是领导：   - true：是 - false：不是 |
| roleList | Array | 角色列表。 |
| id | Long | 角色ID。 |
| name | String | 角色名称。 |
| groupName | String | 角色组名称。 |
| loginId | String | 高校账号登录账号（**仅高校账号返回**）。  `如果类型是身份证号登录，该字段不返回` |
| loginType | String | 高校账号登录类型（**仅高校账号返回**）:   - studentNo：学号 - teacherNo：教职工号 - cardNo：身份证号 - candidateNo：考生号 |
| exclusiveAccountType | String | 高校账号类型（**仅高校账号返回**）：   - sso：学校自建账号 - dingtalk：钉钉自建账号 |
| exclusiveAccountCorpName | String | 高校账号归属组织的组织名称（**仅高校账号返回**）。 |
| exclusiveAccountCorpId | String | 高校账号归属组织的组织CorpId（**仅高校账号返回**）。 |
| unionEmpExt | Object | 当用户来自于关联组织时的关联信息。 |
| userid | String | 员工的UserId。 |
| corpId | String | 当前用户所属的组织的企业CorpId。 |
| unionEmpMapList | Array | 关联映射关系。 |
| userid | String | 关联分支组织中的员工UserId。 |
| corpId | String | 关联分支组织的企业CorpId。 |
| deptPositionSet | Array | 部门多任职相关，其主部门和mainDeptId一致。  仅组织开通了多任职才生效。 |
| deptId | Long | 部门id。 |
| title | String | 职位。 |
| isMain | Boolean | 是否主部门。 |
| workPlace | String | 办公地点。 |
| managerUserId | String | 直属主管的userid。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "userid" : "zhangsan666",
    "unionId" : "z21HjQliSzpw0YWCNxmii6u2Os62cZ62iSZ",
    "name" : "张三",
    "avatar" : "xxxxxx",
    "empType" : "college_student",
    "stateCode" : "86",
    "mobile" : "188****4567",
    "managerUserid" : "111111",
    "hideMobile" : false,
    "telephone" : "010-86123456-2345",
    "jobNumber" : "12122294",
    "title" : "寝室长",
    "email" : "test@xxx.com",
    "workPlace" : "勤奋楼",
    "remark" : "这是一个备注",
    "exclusiveAccount" : true,
    "orgEmail" : "test@xxx.com",
    "deptIdList" : [ 123456 ],
    "mainDeptId" : 123456,
    "deptOrderList" : [ {
      "deptId" : 123456,
      "order" : 1
    } ],
    "deptTypeSet" : [ {
      "deptId" : 123456,
      "deptName" : "土木202班",
      "deptType" : "contact_class_dept",
      "deptStructType" : "stru_standard_dept",
      "structDeptId" : 10000
    } ],
    "extension" : "{\"学号\":\"12122294\",\"在校状态\":\"新生\",\"学生类别\":\"本科生\",\"考生号\":\"999888\"}",
    "hiredDate" : 1597573616828,
    "active" : true,
    "realAuthed" : true,
    "senior" : false,
    "admin" : false,
    "boss" : false,
    "orgEmailType" : "profession",
    "leaderInDept" : [ {
      "deptId" : 123456,
      "leader" : false
    } ],
    "roleList" : [ {
      "id" : 100,
      "name" : "宿舍长",
      "groupName" : "职务"
    } ],
    "loginId" : "12122294",
    "loginType" : "studentNo",
    "exclusiveAccountType" : "dingtalk",
    "exclusiveAccountCorpName" : "测试123",
    "exclusiveAccountCorpId" : "dingxxxxx",
    "unionEmpExt" : {
      "userid" : "500",
      "corpId" : "dingxxx",
      "unionEmpMapList" : [ {
        "userid" : "5000",
        "corpId" : "dingxxx"
      } ]
    },
    "deptPositionSet" : [ {
      "deptId" : 123456,
      "title" : "学工处处长",
      "isMain" : true,
      "workPlace" : "学工处办公室",
      "managerUserId" : "001"
    } ]
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | needAuth | NEED\_AUTH | 需要授权 |
| 400 | invalidIsvOrgId | INVALID\_ISV\_ORG\_ID | 无效的isv |
| 400 | invalidRequestParams | INVALID\_REQUEST\_PARAMS | 不合法的参数 |
| 400 | noPermission | NO\_PERMISSION | 没有权限 |
| 400 | systemError | SYSTEM\_ERROR | 系统异常 |
| 400 | userNotFound | USER\_NOT\_FOUND | 用户不存在 |
