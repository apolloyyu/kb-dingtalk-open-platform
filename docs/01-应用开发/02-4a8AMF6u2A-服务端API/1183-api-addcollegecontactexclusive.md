---
title: "创建高校账号用户"
source_url: "https://open.dingtalk.com/document/development/api-addcollegecontactexclusive"
namespace: "development"
slug: "api-addcollegecontactexclusive"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 创建高校账号用户"
doc_id: "LUJy1oUhaC"
updated_at: "2025-09-23 19:23:24"
---

> Source: https://open.dingtalk.com/document/development/api-addcollegecontactexclusive
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 创建高校账号用户
> Updated: 2025-09-23 19:23:24

# 创建高校账号用户

调用本接口，创建新的高校账号（企业账号）用户，如果是创建普通用户，请调用另外一个创建个人账号用户的接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/exclusiveAccounts/users |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Edu.College.Contact.Write-钉钉教育高校通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userid | String | 否 | 员工唯一标识ID（不可修改），企业内必须唯一。  长度为1~64个字符，如果不传，将自动生成一个userid。 |
| name | String | 是 | 员工名称，长度最大80个字符。 |
| mobile | String | 否 | 手机号码，企业内必须唯一，不可重复。  目前仅支持国内手机号。 |
| empType | String | 是 | 员工的成员类型：   - college\_teacher：教职工 - college\_student：学生 |
| telephone | String | 否 | 分机号，长度最大50个字符。 |
| jobNumber | String | 否 | 教职工工号/学生学号，长度最长为50个字符。 |
| title | String | 否 | 职位，长度最大为200个字符。 |
| email | String | 否 | 员工个人邮箱，长度最大50个字符。 |
| orgEmail | String | 否 | 员工的企业邮箱，长度最大100个字符。 |
| orgEmailType | String | 否 | 员工的企业邮箱类型：   - profession: 标准版 - base：基础版 |
| workPlace | String | 否 | 办公地点，长度最大100个字符。 |
| remark | String | 否 | 备注，长度最大2000个字符。 |
| deptIdList | Array of Long | 是 | 部门id。 |
| mainDeptId | Long | 是 | 主部门ID。 |
| deptOrderList | Array | 否 | 员工在对应的部门中的排序。 |
| deptId | Long | 否 | 部门ID。 |
| order | Integer | 否 | 员工在部门中的排序。 |
| deptTitleList | Array | 否 | 员工在对应的部门中的职位。 |
| deptId | Long | 否 | 部门ID。 |
| title | String | 否 | 员工在部门内的职位 |
| extension | Map<String, String> | 否 | 扩展属性，可以设置多种属性，最大长度2000个字符。 具体支持的key可见成员字段管理。      身份证号是高敏信息，查询用户信息接口中不返回。 |
| seniorMode | Boolean | 否 | 是否开启高管模式，默认值false：   - true：开启 - false：不开启 |
| hiredDate | Long | 否 | 入职时间，Unix时间戳，单位毫秒。 |
| managerUserid | String | 否 | 直属主管的userId。 |
| sendActiveSms | Boolean | 否 | 首次创建是否发送邀请短信。 |
| exclusiveAccount | Boolean | 是 | 必须填true，表示要创建高校账号。 |
| exclusiveAccountType | String | 是 | 高校账号类型（dingtalk、sso），默认dingtalk，表示钉钉自建高校账号。sso表示SSO高校账号 |
| initPassword | String | 否 | 钉钉自建高校账号必填。初始密码， 至少8个字符。 不能全是字母或者数字。  SSO高校账号不需要填写 |
| loginIdType | String | 否 | 钉钉自建高校账号必填。登录类型：   - studentNo：学号 - teacherNo：职工号 - cardNo：身份证号 - candidateNo：考生号        - 使用studentNo或teacherNo，此时jobNumber必传。 - 使用cardNo或者candidateNo，则extension中必传{"身份证号":"xxxx"}或者{"考生号":"xxxx"}。 - 身份证号是高敏信息，查询用户信息接口中不返回。     SSO高校账号不需要填写 |
| avatarMediaId | String | 否 | 创建高校账号时可指定头像MediaId，只支持jpg/png。  可调用上传媒体文件接口获取。 |
| nickname | String | 否 | 创建高校账号时可指定昵称。 |
| deptPositionSet | Array | 否 | 部门多任职，其任职主部门由mainDeptId确定。      仅组织开通了多任职才生效。 |
| deptId | Long | 否 | 部门id。 |
| title | String | 否 | 职位。 |
| workPlace | String | 否 | 工作地点。 |
| managerUserId | String | 否 | 直属主管。 |

### 请求示例

HTTP

```
POST /v1.0/edu/collegeContact/exclusiveAccounts/users HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:BE3xxxx
Content-Type:application/json

{
  "userid" : "zhangsan666",
  "name" : "张三",
  "mobile" : "185xxxx8888",
  "empType" : "college_student",
  "telephone" : "010-86123456-2345",
  "jobNumber" : "666666",
  "title" : "学生会主席",
  "email" : "test@xxx.com",
  "orgEmail" : "test@xxx.com",
  "orgEmailType" : "profession",
  "workPlace" : "学工处办公室",
  "remark" : "备注",
  "deptIdList" : [ 123456 ],
  "mainDeptId" : 123456,
  "deptOrderList" : [ {
    "deptId" : 123456,
    "order" : 1
  } ],
  "deptTitleList" : [ {
    "deptId" : 123456,
    "title" : "学工处处长"
  } ],
  "extension" : {
    "key" : "{\"在校类别\":\"本科生\",\"学生状态\":\"新生\",\"性别\":\"男\"}"
  },
  "seniorMode" : false,
  "hiredDate" : 1597573616828,
  "managerUserid" : "001",
  "sendActiveSms" : false,
  "exclusiveAccount" : true,
  "exclusiveAccountType" : "dingtalk",
  "initPassword" : "zs123456",
  "loginIdType" : "studentNo",
  "avatarMediaId" : "@lALPDfmVUw19YdrNA-jNA-g",
  "nickname" : "昵称",
  "deptPositionSet" : [ {
    "deptId" : 123456,
    "title" : "学工处处长",
    "workPlace" : "学工处办公室",
    "managerUserId" : "001"
  } ]
}
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
        com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveHeaders addCollegeContactExclusiveHeaders = new com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveHeaders();
        addCollegeContactExclusiveHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptPositionSet deptPositionSet0 = new com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptPositionSet()
                .setDeptId(123456L)
                .setTitle("学工处处长")
                .setWorkPlace("学工处办公室")
                .setManagerUserId("001");
        java.util.Map<String, String> extension = TeaConverter.buildMap(
            new TeaPair("key", "{\"在校类别\":\"本科生\",\"学生状态\":\"新生\",\"性别\":\"男\"}")
        );
        com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptTitleList deptTitleList0 = new com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptTitleList()
                .setDeptId(123456L)
                .setTitle("学工处处长");
        com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptOrderList deptOrderList0 = new com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptOrderList()
                .setDeptId(123456L)
                .setOrder(1);
        com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest addCollegeContactExclusiveRequest = new com.aliyun.dingtalkedu_1_0.models.AddCollegeContactExclusiveRequest()
                .setUserid("zhangsan666")
                .setName("张三")
                .setMobile("185xxxx8888")
                .setEmpType("college_student")
                .setTelephone("010-86123456-2345")
                .setJobNumber("666666")
                .setTitle("学生会主席")
                .setEmail("test@xxx.com")
                .setOrgEmail("test@xxx.com")
                .setOrgEmailType("profession")
                .setWorkPlace("学工处办公室")
                .setRemark("备注")
                .setDeptIdList(java.util.Arrays.asList(
                    123456L
                ))
                .setMainDeptId(123456L)
                .setDeptOrderList(java.util.Arrays.asList(
                    deptOrderList0
                ))
                .setDeptTitleList(java.util.Arrays.asList(
                    deptTitleList0
                ))
                .setExtension(extension)
                .setSeniorMode(false)
                .setHiredDate(1597573616828L)
                .setManagerUserid("001")
                .setSendActiveSms(false)
                .setExclusiveAccount(true)
                .setExclusiveAccountType("dingtalk")
                .setInitPassword("zs123456")
                .setLoginIdType("studentNo")
                .setAvatarMediaId("@lALPDfmVUw19YdrNA-jNA-g")
                .setNickname("昵称")
                .setDeptPositionSet(java.util.Arrays.asList(
                    deptPositionSet0
                ));
        try {
            client.addCollegeContactExclusiveWithOptions(addCollegeContactExclusiveRequest, addCollegeContactExclusiveHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        add_college_contact_exclusive_headers = dingtalkedu__1__0_models.AddCollegeContactExclusiveHeaders()
        add_college_contact_exclusive_headers.x_acs_dingtalk_access_token = '<your access token>'
        dept_position_set_0 = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequestDeptPositionSet(
            dept_id=123456,
            title='学工处处长',
            work_place='学工处办公室',
            manager_user_id='001'
        )
        extension = {
            'key': '{"在校类别":"本科生","学生状态":"新生","性别":"男"}'
        }
        dept_title_list_0 = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequestDeptTitleList(
            dept_id=123456,
            title='学工处处长'
        )
        dept_order_list_0 = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequestDeptOrderList(
            dept_id=123456,
            order=1
        )
        add_college_contact_exclusive_request = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequest(
            userid='zhangsan666',
            name='张三',
            mobile='185xxxx8888',
            emp_type='college_student',
            telephone='010-86123456-2345',
            job_number='666666',
            title='学生会主席',
            email='test@xxx.com',
            org_email='test@xxx.com',
            org_email_type='profession',
            work_place='学工处办公室',
            remark='备注',
            dept_id_list=[
                123456
            ],
            main_dept_id=123456,
            dept_order_list=[
                dept_order_list_0
            ],
            dept_title_list=[
                dept_title_list_0
            ],
            extension=extension,
            senior_mode=False,
            hired_date=1597573616828,
            manager_userid='001',
            send_active_sms=False,
            exclusive_account=True,
            exclusive_account_type='dingtalk',
            init_password='zs123456',
            login_id_type='studentNo',
            avatar_media_id='@lALPDfmVUw19YdrNA-jNA-g',
            nickname='昵称',
            dept_position_set=[
                dept_position_set_0
            ]
        )
        try:
            client.add_college_contact_exclusive_with_options(add_college_contact_exclusive_request, add_college_contact_exclusive_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        add_college_contact_exclusive_headers = dingtalkedu__1__0_models.AddCollegeContactExclusiveHeaders()
        add_college_contact_exclusive_headers.x_acs_dingtalk_access_token = '<your access token>'
        dept_position_set_0 = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequestDeptPositionSet(
            dept_id=123456,
            title='学工处处长',
            work_place='学工处办公室',
            manager_user_id='001'
        )
        extension = {
            'key': '{"在校类别":"本科生","学生状态":"新生","性别":"男"}'
        }
        dept_title_list_0 = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequestDeptTitleList(
            dept_id=123456,
            title='学工处处长'
        )
        dept_order_list_0 = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequestDeptOrderList(
            dept_id=123456,
            order=1
        )
        add_college_contact_exclusive_request = dingtalkedu__1__0_models.AddCollegeContactExclusiveRequest(
            userid='zhangsan666',
            name='张三',
            mobile='185xxxx8888',
            emp_type='college_student',
            telephone='010-86123456-2345',
            job_number='666666',
            title='学生会主席',
            email='test@xxx.com',
            org_email='test@xxx.com',
            org_email_type='profession',
            work_place='学工处办公室',
            remark='备注',
            dept_id_list=[
                123456
            ],
            main_dept_id=123456,
            dept_order_list=[
                dept_order_list_0
            ],
            dept_title_list=[
                dept_title_list_0
            ],
            extension=extension,
            senior_mode=False,
            hired_date=1597573616828,
            manager_userid='001',
            send_active_sms=False,
            exclusive_account=True,
            exclusive_account_type='dingtalk',
            init_password='zs123456',
            login_id_type='studentNo',
            avatar_media_id='@lALPDfmVUw19YdrNA-jNA-g',
            nickname='昵称',
            dept_position_set=[
                dept_position_set_0
            ]
        )
        try:
            await client.add_college_contact_exclusive_with_options_async(add_college_contact_exclusive_request, add_college_contact_exclusive_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\AddCollegeContactExclusiveHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\AddCollegeContactExclusiveRequest\deptPositionSet;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\AddCollegeContactExclusiveRequest\deptTitleList;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\AddCollegeContactExclusiveRequest\deptOrderList;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\AddCollegeContactExclusiveRequest;
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
        $addCollegeContactExclusiveHeaders = new AddCollegeContactExclusiveHeaders([]);
        $addCollegeContactExclusiveHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deptPositionSet0 = new deptPositionSet([
            "deptId" => 123456,
            "title" => "学工处处长",
            "workPlace" => "学工处办公室",
            "managerUserId" => "001"
        ]);
        $extension = [
            "key" => "{\"在校类别\":\"本科生\",\"学生状态\":\"新生\",\"性别\":\"男\"}"
        ];
        $deptTitleList0 = new deptTitleList([
            "deptId" => 123456,
            "title" => "学工处处长"
        ]);
        $deptOrderList0 = new deptOrderList([
            "deptId" => 123456,
            "order" => 1
        ]);
        $addCollegeContactExclusiveRequest = new AddCollegeContactExclusiveRequest([
            "userid" => "zhangsan666",
            "name" => "张三",
            "mobile" => "185xxxx8888",
            "empType" => "college_student",
            "telephone" => "010-86123456-2345",
            "jobNumber" => "666666",
            "title" => "学生会主席",
            "email" => "test@xxx.com",
            "orgEmail" => "test@xxx.com",
            "orgEmailType" => "profession",
            "workPlace" => "学工处办公室",
            "remark" => "备注",
            "deptIdList" => [
                123456
            ],
            "mainDeptId" => 123456,
            "deptOrderList" => [
                $deptOrderList0
            ],
            "deptTitleList" => [
                $deptTitleList0
            ],
            "extension" => $extension,
            "seniorMode" => false,
            "hiredDate" => 1597573616828,
            "managerUserid" => "001",
            "sendActiveSms" => false,
            "exclusiveAccount" => true,
            "exclusiveAccountType" => "dingtalk",
            "initPassword" => "zs123456",
            "loginIdType" => "studentNo",
            "avatarMediaId" => "@lALPDfmVUw19YdrNA-jNA-g",
            "nickname" => "昵称",
            "deptPositionSet" => [
                $deptPositionSet0
            ]
        ]);
        try {
            $client->addCollegeContactExclusiveWithOptions($addCollegeContactExclusiveRequest, $addCollegeContactExclusiveHeaders, new RuntimeOptions([]));
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

  addCollegeContactExclusiveHeaders := &dingtalkedu_1_0.AddCollegeContactExclusiveHeaders{}
  addCollegeContactExclusiveHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deptPositionSet0 := &dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptPositionSet{
    DeptId: tea.Int64(123456),
    Title: tea.String("学工处处长"),
    WorkPlace: tea.String("学工处办公室"),
    ManagerUserId: tea.String("001"),
  }
  extension := map[string]*string{
    "key": tea.String("{\"在校类别\":\"本科生\",\"学生状态\":\"新生\",\"性别\":\"男\"}"),
  }
  deptTitleList0 := &dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptTitleList{
    DeptId: tea.Int64(123456),
    Title: tea.String("学工处处长"),
  }
  deptOrderList0 := &dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptOrderList{
    DeptId: tea.Int64(123456),
    Order: tea.Int32(1),
  }
  addCollegeContactExclusiveRequest := &dingtalkedu_1_0.AddCollegeContactExclusiveRequest{
    Userid: tea.String("zhangsan666"),
    Name: tea.String("张三"),
    Mobile: tea.String("185xxxx8888"),
    EmpType: tea.String("college_student"),
    Telephone: tea.String("010-86123456-2345"),
    JobNumber: tea.String("666666"),
    Title: tea.String("学生会主席"),
    Email: tea.String("test@xxx.com"),
    OrgEmail: tea.String("test@xxx.com"),
    OrgEmailType: tea.String("profession"),
    WorkPlace: tea.String("学工处办公室"),
    Remark: tea.String("备注"),
    DeptIdList: []*int64{tea.Int64(123456)},
    MainDeptId: tea.Int64(123456),
    DeptOrderList: []*dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptOrderList{deptOrderList0},
    DeptTitleList: []*dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptTitleList{deptTitleList0},
    Extension: extension,
    SeniorMode: tea.Bool(false),
    HiredDate: tea.Int64(1597573616828),
    ManagerUserid: tea.String("001"),
    SendActiveSms: tea.Bool(false),
    ExclusiveAccount: tea.Bool(true),
    ExclusiveAccountType: tea.String("dingtalk"),
    InitPassword: tea.String("zs123456"),
    LoginIdType: tea.String("studentNo"),
    AvatarMediaId: tea.String("@lALPDfmVUw19YdrNA-jNA-g"),
    Nickname: tea.String("昵称"),
    DeptPositionSet: []*dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptPositionSet{deptPositionSet0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AddCollegeContactExclusiveWithOptions(addCollegeContactExclusiveRequest, addCollegeContactExclusiveHeaders, &util.RuntimeOptions{})
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
    let addCollegeContactExclusiveHeaders = new dingtalkedu_1_0.AddCollegeContactExclusiveHeaders({ });
    addCollegeContactExclusiveHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let deptPositionSet0 = new dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptPositionSet({
      deptId: 123456,
      title: '学工处处长',
      workPlace: '学工处办公室',
      managerUserId: '001',
    });
    let extension = {
      key: '{"在校类别":"本科生","学生状态":"新生","性别":"男"}',
    };
    let deptTitleList0 = new dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptTitleList({
      deptId: 123456,
      title: '学工处处长',
    });
    let deptOrderList0 = new dingtalkedu_1_0.AddCollegeContactExclusiveRequestDeptOrderList({
      deptId: 123456,
      order: 1,
    });
    let addCollegeContactExclusiveRequest = new dingtalkedu_1_0.AddCollegeContactExclusiveRequest({
      userid: 'zhangsan666',
      name: '张三',
      mobile: '185xxxx8888',
      empType: 'college_student',
      telephone: '010-86123456-2345',
      jobNumber: '666666',
      title: '学生会主席',
      email: 'test@xxx.com',
      orgEmail: 'test@xxx.com',
      orgEmailType: 'profession',
      workPlace: '学工处办公室',
      remark: '备注',
      deptIdList: [
        123456
      ],
      mainDeptId: 123456,
      deptOrderList: [
        deptOrderList0
      ],
      deptTitleList: [
        deptTitleList0
      ],
      extension: extension,
      seniorMode: false,
      hiredDate: 1597573616828,
      managerUserid: '001',
      sendActiveSms: false,
      exclusiveAccount: true,
      exclusiveAccountType: 'dingtalk',
      initPassword: 'zs123456',
      loginIdType: 'studentNo',
      avatarMediaId: '@lALPDfmVUw19YdrNA-jNA-g',
      nickname: '昵称',
      deptPositionSet: [
        deptPositionSet0
      ],
    });
    try {
      await client.addCollegeContactExclusiveWithOptions(addCollegeContactExclusiveRequest, addCollegeContactExclusiveHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveHeaders addCollegeContactExclusiveHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveHeaders();
            addCollegeContactExclusiveHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptPositionSet deptPositionSet0 = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptPositionSet
            {
                DeptId = 123456,
                Title = "学工处处长",
                WorkPlace = "学工处办公室",
                ManagerUserId = "001",
            };
            Dictionary<string, string> extension = new Dictionary<string, string>
            {
                {"key", "{\"在校类别\":\"本科生\",\"学生状态\":\"新生\",\"性别\":\"男\"}"},
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptTitleList deptTitleList0 = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptTitleList
            {
                DeptId = 123456,
                Title = "学工处处长",
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptOrderList deptOrderList0 = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptOrderList
            {
                DeptId = 123456,
                Order = 1,
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest addCollegeContactExclusiveRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest
            {
                Userid = "zhangsan666",
                Name = "张三",
                Mobile = "185xxxx8888",
                EmpType = "college_student",
                Telephone = "010-86123456-2345",
                JobNumber = "666666",
                Title = "学生会主席",
                Email = "test@xxx.com",
                OrgEmail = "test@xxx.com",
                OrgEmailType = "profession",
                WorkPlace = "学工处办公室",
                Remark = "备注",
                DeptIdList = new List<long?>
                {
                    123456
                },
                MainDeptId = 123456,
                DeptOrderList = new List<AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptOrderList>
                {
                    deptOrderList0
                },
                DeptTitleList = new List<AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptTitleList>
                {
                    deptTitleList0
                },
                Extension = extension,
                SeniorMode = false,
                HiredDate = 1597573616828,
                ManagerUserid = "001",
                SendActiveSms = false,
                ExclusiveAccount = true,
                ExclusiveAccountType = "dingtalk",
                InitPassword = "zs123456",
                LoginIdType = "studentNo",
                AvatarMediaId = "@lALPDfmVUw19YdrNA-jNA-g",
                Nickname = "昵称",
                DeptPositionSet = new List<AlibabaCloud.SDK.Dingtalkedu_1_0.Models.AddCollegeContactExclusiveRequest.AddCollegeContactExclusiveRequestDeptPositionSet>
                {
                    deptPositionSet0
                },
            };
            try
            {
                client.AddCollegeContactExclusiveWithOptions(addCollegeContactExclusiveRequest, addCollegeContactExclusiveHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| userid | String | 员工id。 |
| unionId | String | 员工唯一id。 |
| createResult | Integer | 添加接口：   - 0：直接加入到组织。 - 1：需要用户确认邀请后，才会加入到组织。       如果需要用户确认，且接口入参未指定userId，则不会返回userId和unionId。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "userid" : "zhangsan666",
    "unionId" : "xxxx",
    "createResult" : 0
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
| 400 | saveFailed | SAVE\_EMPLOYEE\_INFO\_FAILED | 创建用户信息失败 |
| 400 | noPermission | NO\_PERMISSION | 没有权限 |
| 400 | illegalMobile | ILLEGAL\_MOBILE | 无效的手机号 |
| 400 | userIdExist | USERID\_EXIST\_IN\_ORG | userId已存在 |
| 400 | deptCannotFind | DEPT\_CAN\_NOT\_FIND | 部门不存在 |
| 400 | userOpenAccountProtect | USER\_OPEN\_ACCOUNT\_PROTECT | 用户开启了账号保护 |
| 400 | systemError | SYSTEM\_ERROR | 系统异常 |
