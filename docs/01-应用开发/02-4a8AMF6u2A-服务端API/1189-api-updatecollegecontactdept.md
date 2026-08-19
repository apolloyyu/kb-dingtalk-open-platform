---
title: "更新组织单元"
source_url: "https://open.dingtalk.com/document/development/api-updatecollegecontactdept"
namespace: "development"
slug: "api-updatecollegecontactdept"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 更新组织单元"
doc_id: "qaylwmpulF"
updated_at: "2025-09-23 19:23:28"
---

> Source: https://open.dingtalk.com/document/development/api-updatecollegecontactdept
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 高校通迅录 > 更新组织单元
> Updated: 2025-09-23 19:23:28

# 更新组织单元

调用本接口，更新指定的组织单元（即部门）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/collegeContact/depts |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Edu.College.Contact.Write-钉钉教育高校通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| deptId | Long | 是 | 组织单元ID。 |
| parentId | Long | 否 | 父组织单元ID。根组织单元ID为1。 |
| deptType | String | 否 | 高校组织单元类型，传入当前高校配置中生效的组织单元类型。 |
| deptCode | String | 否 | 高校组织单元编码，由开发者确定，高校组织内唯一标识的组织单元编码。 |
| outerDept | Boolean | 否 | 限制本组织单元成员查看通讯录，限制开启后，本组织单元成员只能看到限定范围内的通讯录。true 表示限制开启。 |
| hideDept | Boolean | 否 | 是否隐藏组织单元：   - true：隐藏 - false：显示 |
| createDeptGroup | Boolean | 否 | 是否创建一个关联此组织单元的企业群，默认为false。 |
| order | Long | 否 | 在父组织单元中的排序值，order值小的排序靠前。 |
| name | String | 否 | 组织单元名称，长度限制为1~100个字符，不允许包含字符‘-’‘，’以及‘,’。 |
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
| language | String | 否 | 通讯录语言。 |
| autoAddUser | Boolean | 否 | 如果有新人加入组织单元是否会自动加入对应群。 |
| deptManagerUseridList | Array of String | 否 | 组织人员userID。 |
| groupContainSubDept | Boolean | 否 | 组织单元群是否包含子组织单元。 |
| groupContainOuterDept | Boolean | 否 | 组织单元群是否包含外部组织单元。 |
| groupContainHiddenDept | Boolean | 否 | 组织单元群是否包含隐藏组织单元。 |
| orgDeptOwner | String | 否 | 组织单元群群主的userID。 |
| forceUpdateFields | Array of String | 否 | 强制更新的字段。 |

### 请求示例

HTTP

```
PUT /v1.0/edu/collegeContact/depts HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:bE74xxxx
Content-Type:application/json

{
  "deptId" : 200,
  "parentId" : 20,
  "deptType" : "contact_class_dept",
  "deptCode" : "dept456",
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
  },
  "language" : "zh_CN",
  "autoAddUser" : false,
  "deptManagerUseridList" : [ "user234" ],
  "groupContainSubDept" : false,
  "groupContainOuterDept" : false,
  "groupContainHiddenDept" : false,
  "orgDeptOwner" : "user234",
  "forceUpdateFields" : [ "dept_manager_userid_list" ]
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
        com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptHeaders updateCollegeContactDeptHeaders = new com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptHeaders();
        updateCollegeContactDeptHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> extension = TeaConverter.buildMap(
            new TeaPair("key", "{\"姓名\":\"张三\"}")
        );
        com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestOuterSceneConfig outerSceneConfig = new com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestOuterSceneConfig()
                .setActive(false)
                .setProfile(false)
                .setSearch(false)
                .setNodeList(false)
                .setChatboxSubtitle(false);
        com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestHideSceneConfig hideSceneConfig = new com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestHideSceneConfig()
                .setActive(false)
                .setProfile(false)
                .setSearch(false)
                .setNodeList(false)
                .setChatboxSubtitle(false);
        com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptRequest updateCollegeContactDeptRequest = new com.aliyun.dingtalkedu_1_0.models.UpdateCollegeContactDeptRequest()
                .setDeptId(200L)
                .setParentId(20L)
                .setDeptType("contact_class_dept")
                .setDeptCode("dept456")
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
                .setExtension(extension)
                .setLanguage("zh_CN")
                .setAutoAddUser(false)
                .setDeptManagerUseridList(java.util.Arrays.asList(
                    "user234"
                ))
                .setGroupContainSubDept(false)
                .setGroupContainOuterDept(false)
                .setGroupContainHiddenDept(false)
                .setOrgDeptOwner("user234")
                .setForceUpdateFields(java.util.Arrays.asList(
                    "dept_manager_userid_list"
                ));
        try {
            client.updateCollegeContactDeptWithOptions(updateCollegeContactDeptRequest, updateCollegeContactDeptHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_college_contact_dept_headers = dingtalkedu__1__0_models.UpdateCollegeContactDeptHeaders()
        update_college_contact_dept_headers.x_acs_dingtalk_access_token = '<your access token>'
        extension = {
            'key': '{"姓名":"张三"}'
        }
        outer_scene_config = dingtalkedu__1__0_models.UpdateCollegeContactDeptRequestOuterSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        hide_scene_config = dingtalkedu__1__0_models.UpdateCollegeContactDeptRequestHideSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        update_college_contact_dept_request = dingtalkedu__1__0_models.UpdateCollegeContactDeptRequest(
            dept_id=200,
            parent_id=20,
            dept_type='contact_class_dept',
            dept_code='dept456',
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
            extension=extension,
            language='zh_CN',
            auto_add_user=False,
            dept_manager_userid_list=[
                'user234'
            ],
            group_contain_sub_dept=False,
            group_contain_outer_dept=False,
            group_contain_hidden_dept=False,
            org_dept_owner='user234',
            force_update_fields=[
                'dept_manager_userid_list'
            ]
        )
        try:
            client.update_college_contact_dept_with_options(update_college_contact_dept_request, update_college_contact_dept_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_college_contact_dept_headers = dingtalkedu__1__0_models.UpdateCollegeContactDeptHeaders()
        update_college_contact_dept_headers.x_acs_dingtalk_access_token = '<your access token>'
        extension = {
            'key': '{"姓名":"张三"}'
        }
        outer_scene_config = dingtalkedu__1__0_models.UpdateCollegeContactDeptRequestOuterSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        hide_scene_config = dingtalkedu__1__0_models.UpdateCollegeContactDeptRequestHideSceneConfig(
            active=False,
            profile=False,
            search=False,
            node_list=False,
            chatbox_subtitle=False
        )
        update_college_contact_dept_request = dingtalkedu__1__0_models.UpdateCollegeContactDeptRequest(
            dept_id=200,
            parent_id=20,
            dept_type='contact_class_dept',
            dept_code='dept456',
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
            extension=extension,
            language='zh_CN',
            auto_add_user=False,
            dept_manager_userid_list=[
                'user234'
            ],
            group_contain_sub_dept=False,
            group_contain_outer_dept=False,
            group_contain_hidden_dept=False,
            org_dept_owner='user234',
            force_update_fields=[
                'dept_manager_userid_list'
            ]
        )
        try:
            await client.update_college_contact_dept_with_options_async(update_college_contact_dept_request, update_college_contact_dept_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateCollegeContactDeptHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateCollegeContactDeptRequest\outerSceneConfig;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateCollegeContactDeptRequest\hideSceneConfig;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\UpdateCollegeContactDeptRequest;
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
        $updateCollegeContactDeptHeaders = new UpdateCollegeContactDeptHeaders([]);
        $updateCollegeContactDeptHeaders->xAcsDingtalkAccessToken = "<your access token>";
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
        $updateCollegeContactDeptRequest = new UpdateCollegeContactDeptRequest([
            "deptId" => 200,
            "parentId" => 20,
            "deptType" => "contact_class_dept",
            "deptCode" => "dept456",
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
            "extension" => $extension,
            "language" => "zh_CN",
            "autoAddUser" => false,
            "deptManagerUseridList" => [
                "user234"
            ],
            "groupContainSubDept" => false,
            "groupContainOuterDept" => false,
            "groupContainHiddenDept" => false,
            "orgDeptOwner" => "user234",
            "forceUpdateFields" => [
                "dept_manager_userid_list"
            ]
        ]);
        try {
            $client->updateCollegeContactDeptWithOptions($updateCollegeContactDeptRequest, $updateCollegeContactDeptHeaders, new RuntimeOptions([]));
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

  updateCollegeContactDeptHeaders := &dingtalkedu_1_0.UpdateCollegeContactDeptHeaders{}
  updateCollegeContactDeptHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  extension := map[string]*string{
    "key": tea.String("{\"姓名\":\"张三\"}"),
  }
  outerSceneConfig := &dingtalkedu_1_0.UpdateCollegeContactDeptRequestOuterSceneConfig{
    Active: tea.Bool(false),
    Profile: tea.Bool(false),
    Search: tea.Bool(false),
    NodeList: tea.Bool(false),
    ChatboxSubtitle: tea.Bool(false),
  }
  hideSceneConfig := &dingtalkedu_1_0.UpdateCollegeContactDeptRequestHideSceneConfig{
    Active: tea.Bool(false),
    Profile: tea.Bool(false),
    Search: tea.Bool(false),
    NodeList: tea.Bool(false),
    ChatboxSubtitle: tea.Bool(false),
  }
  updateCollegeContactDeptRequest := &dingtalkedu_1_0.UpdateCollegeContactDeptRequest{
    DeptId: tea.Int64(200),
    ParentId: tea.Int64(20),
    DeptType: tea.String("contact_class_dept"),
    DeptCode: tea.String("dept456"),
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
    Language: tea.String("zh_CN"),
    AutoAddUser: tea.Bool(false),
    DeptManagerUseridList: []*string{tea.String("user234")},
    GroupContainSubDept: tea.Bool(false),
    GroupContainOuterDept: tea.Bool(false),
    GroupContainHiddenDept: tea.Bool(false),
    OrgDeptOwner: tea.String("user234"),
    ForceUpdateFields: []*string{tea.String("dept_manager_userid_list")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateCollegeContactDeptWithOptions(updateCollegeContactDeptRequest, updateCollegeContactDeptHeaders, &util.RuntimeOptions{})
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
    let updateCollegeContactDeptHeaders = new dingtalkedu_1_0.UpdateCollegeContactDeptHeaders({ });
    updateCollegeContactDeptHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let extension = {
      key: '{"姓名":"张三"}',
    };
    let outerSceneConfig = new dingtalkedu_1_0.UpdateCollegeContactDeptRequestOuterSceneConfig({
      active: false,
      profile: false,
      search: false,
      nodeList: false,
      chatboxSubtitle: false,
    });
    let hideSceneConfig = new dingtalkedu_1_0.UpdateCollegeContactDeptRequestHideSceneConfig({
      active: false,
      profile: false,
      search: false,
      nodeList: false,
      chatboxSubtitle: false,
    });
    let updateCollegeContactDeptRequest = new dingtalkedu_1_0.UpdateCollegeContactDeptRequest({
      deptId: 200,
      parentId: 20,
      deptType: 'contact_class_dept',
      deptCode: 'dept456',
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
      language: 'zh_CN',
      autoAddUser: false,
      deptManagerUseridList: [
        'user234'
      ],
      groupContainSubDept: false,
      groupContainOuterDept: false,
      groupContainHiddenDept: false,
      orgDeptOwner: 'user234',
      forceUpdateFields: [
        'dept_manager_userid_list'
      ],
    });
    try {
      await client.updateCollegeContactDeptWithOptions(updateCollegeContactDeptRequest, updateCollegeContactDeptHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptHeaders updateCollegeContactDeptHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptHeaders();
            updateCollegeContactDeptHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> extension = new Dictionary<string, string>
            {
                {"key", "{\"姓名\":\"张三\"}"},
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestOuterSceneConfig outerSceneConfig = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestOuterSceneConfig
            {
                Active = false,
                Profile = false,
                Search = false,
                NodeList = false,
                ChatboxSubtitle = false,
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestHideSceneConfig hideSceneConfig = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptRequest.UpdateCollegeContactDeptRequestHideSceneConfig
            {
                Active = false,
                Profile = false,
                Search = false,
                NodeList = false,
                ChatboxSubtitle = false,
            };
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptRequest updateCollegeContactDeptRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.UpdateCollegeContactDeptRequest
            {
                DeptId = 200,
                ParentId = 20,
                DeptType = "contact_class_dept",
                DeptCode = "dept456",
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
                Language = "zh_CN",
                AutoAddUser = false,
                DeptManagerUseridList = new List<string>
                {
                    "user234"
                },
                GroupContainSubDept = false,
                GroupContainOuterDept = false,
                GroupContainHiddenDept = false,
                OrgDeptOwner = "user234",
                ForceUpdateFields = new List<string>
                {
                    "dept_manager_userid_list"
                },
            };
            try
            {
                client.UpdateCollegeContactDeptWithOptions(updateCollegeContactDeptRequest, updateCollegeContactDeptHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
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
| 400 | orgUpgradeNotSuccess | ORG\_UPGRADE\_NOT\_SUCCESS | 该组织未完成高校通讯录转换 |
| 400 | noPermission | NO\_PERMISSION | 没有创建权限 |
| 400 | invalidDepartmentId | INVALID\_DEPARTMENT\_ID | 不合理的组织单元ID |
| 400 | rootDeptCanNotUpdate | ROOT\_DEPT\_CAN\_NOT\_UPDATE | 根组织单元不允许更新 |
| 400 | struDeptCanNotUpdateStandardParam | STRU\_DEPT\_CAN\_NOT\_UPDATE\_STANDARD\_PARAM | 架构组织单元不允许更新标准字段(dept\_type/dept\_code/parent\_id/name) |
| 400 | deptMoveParamIllegal | DEPT\_MOVE\_PARAM\_ILLEGAL | 新的父组织单元参数异常 |
| 400 | deptMoveIllegal | DEPT\_MOVE\_ILLEGAL | 新的父组织单元设定异常 |
| 400 | updateSubDeptGroupFailed | UPDATE\_SUB\_DEPT\_GROUP\_FAILED | 更新组织单元群包含子组织单元异常 |
