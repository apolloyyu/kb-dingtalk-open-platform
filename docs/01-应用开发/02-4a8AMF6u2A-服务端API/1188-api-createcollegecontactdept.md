---
title: "创建组织单元"
source_url: "https://open.dingtalk.com/document/development/api-createcollegecontactdept"
namespace: "development"
slug: "api-createcollegecontactdept"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 创建组织单元"
doc_id: "kzdO2TqChW"
updated_at: "2025-09-23 19:23:27"
---

> Source: https://open.dingtalk.com/document/development/api-createcollegecontactdept
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 创建组织单元
> Updated: 2025-09-23 19:23:27

# 创建组织单元

调用本接口，创建新的组织单元(即部门)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/depts |
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
| struId | Long | 是 | 高校组织架构ID，例如对应的行政组织架构ID。 |
| deptId | Long | 否 | 部门ID。组织内唯一，不可重复。 新建时可以传入指定部门ID。  **[!NOTE]**    如果部门ID已经存在对应部门，则更新部门信息 |
| deptType | String | 是 | 高校组织单元类型，传入当前高校配置中生效的组织单元类型。 |
| deptCode | String | 否 | 高校组织单元编码，由开发者确定，高校组织内唯一标识的组织单元编码。 |
| parentId | Long | 是 | 父组织单元ID。根组织单元ID为1。 |
| outerDept | Boolean | 否 | 限制本组织单元成员查看通讯录，限制开启后，本组织单元成员只能看到限定范围内的通讯录。true表示限制开启。 |
| hideDept | Boolean | 否 | 是否隐藏组织单元：   - true：隐藏 - false：显示 |
| createDeptGroup | Boolean | 否 | 是否创建一个关联此组织单元的企业群，默认为false。 |
| order | Long | 否 | 在父组织单元中的排序值，order值小的排序靠前。 |
| name | String | 是 | 组织单元名称，长度限制为1~100个字符，不允许包含字符‘-’‘，’以及‘,’。 |
| sourceIdentifier | String | 否 | 基础通讯录部门标识。 |
| deptPermits | Array of Long | 否 | 组织单元ID。 |
| userPermits | Array of String | 否 | 组织人员userID。 |
| outerPermitUsers | Array of String | 否 | 组织人员userID。 |
| outerPermitDepts | Array of Long | 否 | 组织单元ID。 |
| outerDeptOnlySelf | Boolean | 否 | 是否只能看到所在组织单元及下级组织单元通讯录。 |
| autoApproveApply | Boolean | 否 | 开启后，加入该组织单元的申请将默认同意。 |
| empApplyJoinDept | Boolean | 否 | 开启后，允许员工加入组织单元。 |
| brief | String | 否 | 组织单元简介。 |
| telephone | String | 否 | 组织单元联系方式。 |
| code | String | 否 | 基础通讯录编码。 |
| hideSceneConfig | Object | 否 | 组织单元隐藏的生效场景配置。 |
| active | Boolean | 否 | 当前组织单元是否采用单独的配置。如果设置了false，则采用组织维度的配置。 |
| profile | Boolean | 否 | 是否在个人资料页生效。 |
| search | Boolean | 否 | 是否在搜索生效。 |
| nodeList | Boolean | 否 | 是否在查看组织架构生效。 |
| chatboxSubtitle | Boolean | 否 | 是否在单聊框生效。 |
| outerSceneConfig | Object | 否 | 组织单元限制可见的生效场景配置。 |
| active | Boolean | 否 | 当前组织单元是否采用单独的配置。如果设置了false，则采用组织维度的配置。 |
| profile | Boolean | 否 | 是否在个人资料页生效。 |
| search | Boolean | 否 | 是否在搜索生效。 |
| nodeList | Boolean | 否 | 是否在查看组织架构生效。 |
| chatboxSubtitle | Boolean | 否 | 是否在单聊框生效。 |
| extension | Map<String, String> | 否 | 扩展字段，JSON格式。 |

### 请求示例

HTTP

```
POST /v1.0/edu/collegeContact/depts HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bE74xxxx
Content-Type:application/json

{
  "struId" : 10,
  "deptType" : "contact_class_dept",
  "deptCode" : "dept456",
  "parentId" : 20,
  "outerDept" : false,
  "hideDept" : false,
  "createDeptGroup" : false,
  "order" : 20,
  "name" : "软件工程",
  "sourceIdentifier" : "软件工程标识",
  "deptPermits" : [ 20 ],
  "userPermits" : [ "user234" ],
  "outerPermitUsers" : [ "user234" ],
  "outerPermitDepts" : [ 234 ],
  "outerDeptOnlySelf" : false,
  "autoApproveApply" : false,
  "empApplyJoinDept" : false,
  "brief" : "这是组织单元简介",
  "telephone" : "138xxxx0000",
  "code" : "20000",
  "hideSceneConfig" : {
    "active" : false,
    "profile" : false,
    "search" : false,
    "nodeList" : false,
    "chatboxSubtitle" : false
  },
  "outerSceneConfig" : {
    "active" : false,
    "profile" : false,
    "search" : false,
    "nodeList" : false,
    "chatboxSubtitle" : false
  },
  "extension" : {
    "key" : "{\"姓名\":\"张三\"}"
  }
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
        com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptHeaders createCollegeContactDeptHeaders = new com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptHeaders();
        createCollegeContactDeptHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> extension = TeaConverter.buildMap(
            new TeaPair("key", "{\"姓名\":\"张三\"}")
        );
        com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestOuterSceneConfig outerSceneConfig = new com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestOuterSceneConfig()
                .setActive(false)
                .setProfile(false)
                .setSearch(false)
                .setNodeList(false)
                .setChatboxSubtitle(false);
        com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestHideSceneConfig hideSceneConfig = new com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestHideSceneConfig()
                .setActive(false)
                .setProfile(false)
                .setSearch(false)
                .setNodeList(false)
                .setChatboxSubtitle(false);
        com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptRequest createCollegeContactDeptRequest = new com.aliyun.dingtalkedu_1_0.models.CreateCollegeContactDeptRequest()
                .setStruId(10L)
                .setDeptType("contact_class_dept")
                .setDeptCode("dept456")
                .setParentId(20L)
                .setOuterDept(false)
                .setHideDept(false)
                .setCreateDeptGroup(false)
                .setOrder(20L)
                .setName("软件工程")
                .setSourceIdentifier("软件工程标识")
                .setDeptPermits(java.util.Arrays.asList(
                    20L
                ))
                .setUserPermits(java.util.Arrays.asList(
                    "user234"
                ))
                .setOuterPermitUsers(java.util.Arrays.asList(
                    "user234"
                ))
                .setOuterPermitDepts(java.util.Arrays.asList(
                    234L
                ))
                .setOuterDeptOnlySelf(false)
                .setAutoApproveApply(false)
                .setEmpApplyJoinDept(false)
                .setBrief("这是组织单元简介")
                .setTelephone("138xxxx0000")
                .setCode("20000")
                .setHideSceneConfig(hideSceneConfig)
                .setOuterSceneConfig(outerSceneConfig)
                .setExtension(extension);
        try {
            client.createCollegeContactDeptWithOptions(createCollegeContactDeptRequest, createCollegeContactDeptHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_college_contact_dept_headers = dingtalkedu__1__0_models.CreateCollegeContactDeptHeaders()
        create_college_contact_dept_headers.x_acs_dingtalk_access_token = '<your access token>'
        extension = {
            'key': '{"姓名":"张三"}'
        }
        outer_scene_config = dingtalkedu__1__0_models.CreateCollegeContactDeptRequestOuterSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        hide_scene_config = dingtalkedu__1__0_models.CreateCollegeContactDeptRequestHideSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        create_college_contact_dept_request = dingtalkedu__1__0_models.CreateCollegeContactDeptRequest(
            stru_id=10,
            dept_type='contact_class_dept',
            dept_code='dept456',
            parent_id=20,
            outer_dept=False,
            hide_dept=False,
            create_dept_group=False,
            order=20,
            name='软件工程',
            source_identifier='软件工程标识',
            dept_permits=[
                20
            ],
            user_permits=[
                'user234'
            ],
            outer_permit_users=[
                'user234'
            ],
            outer_permit_depts=[
                234
            ],
            outer_dept_only_self=False,
            auto_approve_apply=False,
            emp_apply_join_dept=False,
            brief='这是组织单元简介',
            telephone='138xxxx0000',
            code='20000',
            hide_scene_config=hide_scene_config,
            outer_scene_config=outer_scene_config,
            extension=extension
        )
        try:
            client.create_college_contact_dept_with_options(create_college_contact_dept_request, create_college_contact_dept_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_college_contact_dept_headers = dingtalkedu__1__0_models.CreateCollegeContactDeptHeaders()
        create_college_contact_dept_headers.x_acs_dingtalk_access_token = '<your access token>'
        extension = {
            'key': '{"姓名":"张三"}'
        }
        outer_scene_config = dingtalkedu__1__0_models.CreateCollegeContactDeptRequestOuterSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        hide_scene_config = dingtalkedu__1__0_models.CreateCollegeContactDeptRequestHideSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        create_college_contact_dept_request = dingtalkedu__1__0_models.CreateCollegeContactDeptRequest(
            stru_id=10,
            dept_type='contact_class_dept',
            dept_code='dept456',
            parent_id=20,
            outer_dept=False,
            hide_dept=False,
            create_dept_group=False,
            order=20,
            name='软件工程',
            source_identifier='软件工程标识',
            dept_permits=[
                20
            ],
            user_permits=[
                'user234'
            ],
            outer_permit_users=[
                'user234'
            ],
            outer_permit_depts=[
                234
            ],
            outer_dept_only_self=False,
            auto_approve_apply=False,
            emp_apply_join_dept=False,
            brief='这是组织单元简介',
            telephone='138xxxx0000',
            code='20000',
            hide_scene_config=hide_scene_config,
            outer_scene_config=outer_scene_config,
            extension=extension
        )
        try:
            await client.create_college_contact_dept_with_options_async(create_college_contact_dept_request, create_college_contact_dept_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCollegeContactDeptHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCollegeContactDeptRequest\outerSceneConfig;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCollegeContactDeptRequest\hideSceneConfig;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\CreateCollegeContactDeptRequest;
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
        $createCollegeContactDeptHeaders = new CreateCollegeContactDeptHeaders([]);
        $createCollegeContactDeptHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $extension = [
            "key" => "{\"姓名\":\"张三\"}"
        ];
        $outerSceneConfig = new outerSceneConfig([
            "active" => false,
            "profile" => false,
            "search" => false,
            "nodeList" => false,
            "chatboxSubtitle" => false
        ]);
        $hideSceneConfig = new hideSceneConfig([
            "active" => false,
            "profile" => false,
            "search" => false,
            "nodeList" => false,
            "chatboxSubtitle" => false
        ]);
        $createCollegeContactDeptRequest = new CreateCollegeContactDeptRequest([
            "struId" => 10,
            "deptType" => "contact_class_dept",
            "deptCode" => "dept456",
            "parentId" => 20,
            "outerDept" => false,
            "hideDept" => false,
            "createDeptGroup" => false,
            "order" => 20,
            "name" => "软件工程",
            "sourceIdentifier" => "软件工程标识",
            "deptPermits" => [
                20
            ],
            "userPermits" => [
                "user234"
            ],
            "outerPermitUsers" => [
                "user234"
            ],
            "outerPermitDepts" => [
                234
            ],
            "outerDeptOnlySelf" => false,
            "autoApproveApply" => false,
            "empApplyJoinDept" => false,
            "brief" => "这是组织单元简介",
            "telephone" => "138xxxx0000",
            "code" => "20000",
            "hideSceneConfig" => $hideSceneConfig,
            "outerSceneConfig" => $outerSceneConfig,
            "extension" => $extension
        ]);
        try {
            $client->createCollegeContactDeptWithOptions($createCollegeContactDeptRequest, $createCollegeContactDeptHeaders, new RuntimeOptions([]));
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

  createCollegeContactDeptHeaders := &dingtalkedu_1_0.CreateCollegeContactDeptHeaders{}
  createCollegeContactDeptHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  extension := map[string]*string{
    "key": tea.String("{\"姓名\":\"张三\"}"),
  }
  outerSceneConfig := &dingtalkedu_1_0.CreateCollegeContactDeptRequestOuterSceneConfig{
    Active: tea.Bool(false),
    Profile: tea.Bool(false),
    Search: tea.Bool(false),
    NodeList: tea.Bool(false),
    ChatboxSubtitle: tea.Bool(false),
  }
  hideSceneConfig := &dingtalkedu_1_0.CreateCollegeContactDeptRequestHideSceneConfig{
    Active: tea.Bool(false),
    Profile: tea.Bool(false),
    Search: tea.Bool(false),
    NodeList: tea.Bool(false),
    ChatboxSubtitle: tea.Bool(false),
  }
  createCollegeContactDeptRequest := &dingtalkedu_1_0.CreateCollegeContactDeptRequest{
    StruId: tea.Int64(10),
    DeptType: tea.String("contact_class_dept"),
    DeptCode: tea.String("dept456"),
    ParentId: tea.Int64(20),
    OuterDept: tea.Bool(false),
    HideDept: tea.Bool(false),
    CreateDeptGroup: tea.Bool(false),
    Order: tea.Int64(20),
    Name: tea.String("软件工程"),
    SourceIdentifier: tea.String("软件工程标识"),
    DeptPermits: []*int64{tea.Int64(20)},
    UserPermits: []*string{tea.String("user234")},
    OuterPermitUsers: []*string{tea.String("user234")},
    OuterPermitDepts: []*int64{tea.Int64(234)},
    OuterDeptOnlySelf: tea.Bool(false),
    AutoApproveApply: tea.Bool(false),
    EmpApplyJoinDept: tea.Bool(false),
    Brief: tea.String("这是组织单元简介"),
    Telephone: tea.String("138xxxx0000"),
    Code: tea.String("20000"),
    HideSceneConfig: hideSceneConfig,
    OuterSceneConfig: outerSceneConfig,
    Extension: extension,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateCollegeContactDeptWithOptions(createCollegeContactDeptRequest, createCollegeContactDeptHeaders, &util.RuntimeOptions{})
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
    let createCollegeContactDeptHeaders = new dingtalkedu_1_0.CreateCollegeContactDeptHeaders({ });
    createCollegeContactDeptHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let extension = {
      key: '{"姓名":"张三"}',
    };
    let outerSceneConfig = new dingtalkedu_1_0.CreateCollegeContactDeptRequestOuterSceneConfig({
      active: false,
      profile: false,
      search: false,
      nodeList: false,
      chatboxSubtitle: false,
    });
    let hideSceneConfig = new dingtalkedu_1_0.CreateCollegeContactDeptRequestHideSceneConfig({
      active: false,
      profile: false,
      search: false,
      nodeList: false,
      chatboxSubtitle: false,
    });
    let createCollegeContactDeptRequest = new dingtalkedu_1_0.CreateCollegeContactDeptRequest({
      struId: 10,
      deptType: 'contact_class_dept',
      deptCode: 'dept456',
      parentId: 20,
      outerDept: false,
      hideDept: false,
      createDeptGroup: false,
      order: 20,
      name: '软件工程',
      sourceIdentifier: '软件工程标识',
      deptPermits: [
        20
      ],
      userPermits: [
        'user234'
      ],
      outerPermitUsers: [
        'user234'
      ],
      outerPermitDepts: [
        234
      ],
      outerDeptOnlySelf: false,
      autoApproveApply: false,
      empApplyJoinDept: false,
      brief: '这是组织单元简介',
      telephone: '138xxxx0000',
      code: '20000',
      hideSceneConfig: hideSceneConfig,
      outerSceneConfig: outerSceneConfig,
      extension: extension,
    });
    try {
      await client.createCollegeContactDeptWithOptions(createCollegeContactDeptRequest, createCollegeContactDeptHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptHeaders createCollegeContactDeptHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptHeaders();
            createCollegeContactDeptHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> extension = new Dictionary<string, string>
            {
                {"key", "{\"姓名\":\"张三\"}"},
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestOuterSceneConfig outerSceneConfig = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestOuterSceneConfig
            {
                Active = false,
                Profile = false,
                Search = false,
                NodeList = false,
                ChatboxSubtitle = false,
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestHideSceneConfig hideSceneConfig = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptRequest.CreateCollegeContactDeptRequestHideSceneConfig
            {
                Active = false,
                Profile = false,
                Search = false,
                NodeList = false,
                ChatboxSubtitle = false,
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptRequest createCollegeContactDeptRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.CreateCollegeContactDeptRequest
            {
                StruId = 10,
                DeptType = "contact_class_dept",
                DeptCode = "dept456",
                ParentId = 20,
                OuterDept = false,
                HideDept = false,
                CreateDeptGroup = false,
                Order = 20,
                Name = "软件工程",
                SourceIdentifier = "软件工程标识",
                DeptPermits = new List<long?>
                {
                    20
                },
                UserPermits = new List<string>
                {
                    "user234"
                },
                OuterPermitUsers = new List<string>
                {
                    "user234"
                },
                OuterPermitDepts = new List<long?>
                {
                    234
                },
                OuterDeptOnlySelf = false,
                AutoApproveApply = false,
                EmpApplyJoinDept = false,
                Brief = "这是组织单元简介",
                Telephone = "138xxxx0000",
                Code = "20000",
                HideSceneConfig = hideSceneConfig,
                OuterSceneConfig = outerSceneConfig,
                Extension = extension,
            };
            try
            {
                client.CreateCollegeContactDeptWithOptions(createCollegeContactDeptRequest, createCollegeContactDeptHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| deptId | Long | 组织单元ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "deptId" : 20
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | parameterInvalid | PARAMETER\_INVALID | 参数错误，请先完成高校通讯录转换 |
| 400 | systemError | SYSTEM\_ERROR | 系统错误 |
| 400 | parameterErrror | PARAMETER\_ERROR | 参数异常 |
| 400 | orgNotExist | ORG\_NOT\_EXIST | 高校组织不存在 |
| 400 | parentDeptNotExist | PARENT\_DEPT\_NOT\_EXIST | 父组织单元不存在 |
| 400 | deptNameExist | DEPT\_NAME\_EXIST | 组织单元名已存在 |
| 400 | deptCodeExist | DEPT\_CODE\_EXIST | 组织单元编码已存在 |
| 400 | deptTypeInvalid | DEPT\_TYPE\_INVALID | 组织单元类型不合理 |
| 400 | parentDeptInvalid | PARENT\_DEPT\_INVALID | 父组织单元不合理 |
| 400 | orgUpgradeNotSuccess | ORG\_UPGRADE\_NOT\_SUCCESS | 该组织未完成高校通讯录转换 |
| 400 | struDeptNotExist | STRU\_DEPT\_NOT\_EXIST | 架构不存在 |
| 400 | noPermission | NO\_PERMISSION | 没有创建权限 |
