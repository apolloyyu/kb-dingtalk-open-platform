---
title: "创建钉钉待办任务"
source_url: "https://open.dingtalk.com/document/development/add-dingtalk-to-do-task"
namespace: "development"
slug: "add-dingtalk-to-do-task"
group: "应用开发"
tab: "服务端API"
breadcrumb: "待办任务 > 创建钉钉待办任务"
doc_id: "H0z1RaakhS"
updated_at: "2026-06-04 19:09:50"
---

> Source: https://open.dingtalk.com/document/development/add-dingtalk-to-do-task
> Path: 应用开发 / 服务端API / 待办任务 > 创建钉钉待办任务
> Updated: 2026-06-04 19:09:50

# 创建钉钉待办任务

调用本接口，发起一个钉钉待办任务。

## 接口调用说明

- 第三方企业应用上架后，需要新增当前待办接口前，需要接入[统一授权套件](0007-function-description.md)授权类型必须为**申请个人授权**，即**type=0**
- 创建待办接口，目前已支持创建个人待办和第三方待办：

  - 个人待办：个人待办场景（与用户在钉钉客户端创建的待办完全一致）
  - 第三方待办：第三方业务自闭环场景（调用本接口时需传入自身应用详情页链接）

> **[!NOTE]**
>
> 为了提升接口质量与用户体验，针对待办任务的相关接口规范进行升级，因此我们将对本接口作出以下调整：
>
> - 从 2024 年 2 月 1 日起，本接口升级为仅支持创建工作待办（原第三方待办），即接口文档中的 detailUrl 字段将成为必填项。届时，本接口将无法创建个人待办（原钉钉官方待办），即接口文档中的 detailUrl 字段入参为空。
> - 如果尚未使用本接口创建个人待办（原钉钉官方待办），请通过[创建钉钉个人待办任务](0794-api-createpersonaltodotask.md)接口进行创建。
> - 如果已使用本接口创建个人待办（原钉钉官方待办），你需要于 2024 年 1 月 31 日之前尽快将创建个人待办任务从本接口迁移到[创建钉钉个人待办任务](0794-api-createpersonaltodotask.md)接口，若未完成迁移，后续调用本接口且未填写 detailUrl 字段的入参，则会出现拦截报错提示。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/tasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Todo.Todo.Write-待办应用中待办写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证。   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，授权后使用返回的**authCode** ，通过调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 当前访问资源所归属用户的unionId，和创建者的unionId保持一致，通过调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 否 | 当前操作者用户的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| sourceId | String | 否 | 业务系统侧的唯一标识ID，即业务ID。     - 创建个人待办时，该字段无需传入。 - 创建第三方待办时，业务系统侧的唯一标识任务ID作为sourceId，保证**一个待办任务对应一个sourceId**。 |
| subject | String | 是 | 待办标题，最大长度1024。 |
| creatorId | String | 否 | 创建者的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。 |
| description | String | 否 | 待办备注描述，最大长度4096。       - 创建第三方待办时，该字段无需传入，不会正常展示。 |
| dueTime | Long | 否 | 截止时间，Unix时间戳，单位毫秒。 |
| executorIds | Array of String | 否 | 执行者的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值，建议不超过100人。 |
| participantIds | Array of String | 否 | 参与者的unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值，建议不超过100人。 |
| detailUrl | Object | 否 | 详情页url跳转地址。     - 创建个人待办时，该字段无需传入。 - 创建第三方待办时，需传入自身应用详情页链接。 |
| appUrl | String | 否 | APP端详情页url跳转地址，该字段长度限制为1024个字节。   - 创建个人待办时，该字段无需传入。 - 创建第三方待办时，需传入自身应用详情页链接。     如果创建第三方待办时配置了DING通知能力，appUrl需要支持以dingtalk协议打开。 |
| pcUrl | String | 否 | PC端详情页url跳转地址，该字段长度限制为1024个字节。     - 创建个人待办时，该字段无需传入。 - 创建第三方待办时，需传入自身应用详情页链接。 |
| contentFieldList | Array | 否 | 待办卡片内容区表单自定义字段列表。 |
| fieldKey | String | 否 | 字段唯一标识，最大长度1024字节 |
| fieldValue | String | 否 | 字段值，最大长度1024字节 |
| isOnlyShowExecutor | Boolean | 否 | 生成的待办是否仅展示在执行者的待办列表中。 |
| priority | Integer | 否 | 优先级，取值：   - **10**：较低 - **20**：普通 - **30**：较高 - **40**：紧急 |
| notifyConfigs | Object | 否 | 待办通知配置。 |
| dingNotify | String | 否 | 是否发送钉钉弹框通知：   - **1**：发送 - **0**：不发送 |
| sendTodoApn | String | 否 | 是否发送系统APN通知：   - true：发送 - false：不发送     当未设置时取dingNotify的设置值。 |
| sendAssistantChat | String | 否 | 是否发送待办助手通知：   - true：发送，默认值 - false：不发送 |
| bizCategoryId | String | 否 | 二级分类。 |
| actionList | Array | 否 | 自定义按钮配置。 |
| title | String | 否 | 按钮的名称。 |
| actionType | Integer | 否 | 按钮类型：   - **1**：直接调用业务服务 - **2**：直接跳转 |
| param | Object | 否 | 按钮的回调参数。 |
| body | String | 否 | 回调三方服务时请求的body。 |
| header | Map | 否 | 回调三方服务时请求的header。 |
| url | String | 否 | 跳转链接或者回调请求的地址。 |
| actionKey | String | 否 | 按钮唯一标识，当有两个按钮时可以通过这个字段来区分。 |
| pcUrl | String | 否 | pc端的跳转链接，可以不填，为空时会拿url参数里面的值。 |
| todoType | String | 否 | 待办的业务类型，目前支持两种：   - **TODO**：待办业务类型 - **READ**：待阅业务类型。     不传该入参时，默认创建的是待办业务类型。 |
| reminderTimeStamp | Long | 否 | 待办任务的提醒时间，Unix时间戳，单位毫秒。 |
| remindNotifyConfigs | Object | 否 | 待办截止前的通知提醒设置。 |
| dingNotify | String | 否 | 是否发送钉钉弹框通知：   - **1**：发送 - **0**：不发送 |
| sendTodoApn | String | 否 | 是否发送系统APN通知：   - **true**：发送 - **false**：不发送。     当未设置时取dingNotify的设置值。 |
| thirdExtension | Map | 否 | 三方待办的业务拓展数据 |

### 请求示例

HTTP

```
POST /v1.0/todo/users/PUoixxxxGiP6g/tasks?operatorId=PUoiinWIpxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "sourceId" : "isv_dingtalkTodo1",
  "subject" : "接入钉钉待办",
  "creatorId" : "PUoiiP6g",
  "description" : "应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。",
  "dueTime" : 1617675000000,
  "executorIds" : [ "PUoiixxxxhiiGiP6g" ],
  "participantIds" : [ "PUoxxxxiGiP6g" ],
  "detailUrl" : {
    "appUrl" : "https://www.dingtalk.com",
    "pcUrl" : "https://www.dingtalk.com"
  },
  "contentFieldList" : [ {
    "fieldKey" : "xxx",
    "fieldValue" : "xxx"
  } ],
  "isOnlyShowExecutor" : true,
  "priority" : 20,
  "notifyConfigs" : {
    "dingNotify" : "1",
    "sendTodoApn" : "true",
    "sendAssistantChat" : "true"
  },
  "bizCategoryId" : "123",
  "actionList" : [ {
    "title" : "去查看",
    "buttonStyleType" : 101,
    "actionType" : 2,
    "param" : {
      "body" : "xxx"
    },
    "url" : "https://www.dingtalk.com/",
    "actionKey" : "ak-1-1",
    "pcUrl" : "xxx"
  } ],
  "todoType" : "TODO",
  "reminderTimeStamp" : 1748226368571,
  "remindNotifyConfigs" : {
    "dingNotify" : "1",
    "sendTodoApn" : "true"
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
    public static com.aliyun.dingtalktodo_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktodo_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalktodo_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskHeaders createTodoTaskHeaders = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskHeaders();
        createTodoTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestRemindNotifyConfigs remindNotifyConfigs = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestRemindNotifyConfigs()
                .setDingNotify("1")
                .setSendTodoApn("true");
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestActionListParam actionList0Param = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestActionListParam()
                .setBody("xxx");
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList actionList0 = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList()
                .setTitle("去查看")
                .setActionType(2)
                .setParam(actionList0Param)
                .setUrl("https://www.dingtalk.com/")
                .setActionKey("ak-1-1")
                .setPcUrl("xxx");
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestNotifyConfigs notifyConfigs = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestNotifyConfigs()
                .setDingNotify("1")
                .setSendTodoApn("true")
                .setSendAssistantChat("true");
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestContentFieldList contentFieldList0 = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestContentFieldList()
                .setFieldKey("xxx")
                .setFieldValue("xxx");
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestDetailUrl detailUrl = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest.CreateTodoTaskRequestDetailUrl()
                .setAppUrl("https://www.dingtalk.com")
                .setPcUrl("https://www.dingtalk.com");
        com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest createTodoTaskRequest = new com.aliyun.dingtalktodo_1_0.models.CreateTodoTaskRequest()
                .setOperatorId("PUoiinWIpxxx")
                .setSourceId("isv_dingtalkTodo1")
                .setSubject("接入钉钉待办")
                .setCreatorId("PUoiiP6g")
                .setDescription("应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。")
                .setDueTime(1617675000000L)
                .setExecutorIds(java.util.Arrays.asList(
                    "PUoiixxxxhiiGiP6g"
                ))
                .setParticipantIds(java.util.Arrays.asList(
                    "PUoxxxxiGiP6g"
                ))
                .setDetailUrl(detailUrl)
                .setContentFieldList(java.util.Arrays.asList(
                    contentFieldList0
                ))
                .setIsOnlyShowExecutor(true)
                .setPriority(20)
                .setNotifyConfigs(notifyConfigs)
                .setBizCategoryId("123")
                .setActionList(java.util.Arrays.asList(
                    actionList0
                ))
                .setTodoType("TODO")
                .setReminderTimeStamp(1748226368571L)
                .setRemindNotifyConfigs(remindNotifyConfigs);
        try {
            client.createTodoTaskWithOptions("PUoixxxxGiP6g", createTodoTaskRequest, createTodoTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.todo_1_0.client import Client as dingtalktodo_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.todo_1_0 import models as dingtalktodo__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalktodo_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalktodo_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_todo_task_headers = dingtalktodo__1__0_models.CreateTodoTaskHeaders()
        create_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        remind_notify_configs = dingtalktodo__1__0_models.CreateTodoTaskRequestRemindNotifyConfigs(
            ding_notify='1',
            send_todo_apn='true'
        )
        action_list_0param = dingtalktodo__1__0_models.CreateTodoTaskRequestActionListParam(
            body='xxx'
        )
        action_list_0 = dingtalktodo__1__0_models.CreateTodoTaskRequestActionList(
            title='去查看',
            action_type=2,
            param=action_list_0param,
            url='https://www.dingtalk.com/',
            action_key='ak-1-1',
            pc_url='xxx'
        )
        notify_configs = dingtalktodo__1__0_models.CreateTodoTaskRequestNotifyConfigs(
            ding_notify='1',
            send_todo_apn='true',
            send_assistant_chat='true'
        )
        content_field_list_0 = dingtalktodo__1__0_models.CreateTodoTaskRequestContentFieldList(
            field_key='xxx',
            field_value='xxx'
        )
        detail_url = dingtalktodo__1__0_models.CreateTodoTaskRequestDetailUrl(
            app_url='https://www.dingtalk.com',
            pc_url='https://www.dingtalk.com'
        )
        create_todo_task_request = dingtalktodo__1__0_models.CreateTodoTaskRequest(
            operator_id='PUoiinWIpxxx',
            source_id='isv_dingtalkTodo1',
            subject='接入钉钉待办',
            creator_id='PUoiiP6g',
            description='应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。',
            due_time=1617675000000,
            executor_ids=[
                'PUoiixxxxhiiGiP6g'
            ],
            participant_ids=[
                'PUoxxxxiGiP6g'
            ],
            detail_url=detail_url,
            content_field_list=[
                content_field_list_0
            ],
            is_only_show_executor=True,
            priority=20,
            notify_configs=notify_configs,
            biz_category_id='123',
            action_list=[
                action_list_0
            ],
            todo_type='TODO',
            reminder_time_stamp=1748226368571,
            remind_notify_configs=remind_notify_configs
        )
        try:
            client.create_todo_task_with_options('PUoixxxxGiP6g', create_todo_task_request, create_todo_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_todo_task_headers = dingtalktodo__1__0_models.CreateTodoTaskHeaders()
        create_todo_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        remind_notify_configs = dingtalktodo__1__0_models.CreateTodoTaskRequestRemindNotifyConfigs(
            ding_notify='1',
            send_todo_apn='true'
        )
        action_list_0param = dingtalktodo__1__0_models.CreateTodoTaskRequestActionListParam(
            body='xxx'
        )
        action_list_0 = dingtalktodo__1__0_models.CreateTodoTaskRequestActionList(
            title='去查看',
            action_type=2,
            param=action_list_0param,
            url='https://www.dingtalk.com/',
            action_key='ak-1-1',
            pc_url='xxx'
        )
        notify_configs = dingtalktodo__1__0_models.CreateTodoTaskRequestNotifyConfigs(
            ding_notify='1',
            send_todo_apn='true',
            send_assistant_chat='true'
        )
        content_field_list_0 = dingtalktodo__1__0_models.CreateTodoTaskRequestContentFieldList(
            field_key='xxx',
            field_value='xxx'
        )
        detail_url = dingtalktodo__1__0_models.CreateTodoTaskRequestDetailUrl(
            app_url='https://www.dingtalk.com',
            pc_url='https://www.dingtalk.com'
        )
        create_todo_task_request = dingtalktodo__1__0_models.CreateTodoTaskRequest(
            operator_id='PUoiinWIpxxx',
            source_id='isv_dingtalkTodo1',
            subject='接入钉钉待办',
            creator_id='PUoiiP6g',
            description='应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。',
            due_time=1617675000000,
            executor_ids=[
                'PUoiixxxxhiiGiP6g'
            ],
            participant_ids=[
                'PUoxxxxiGiP6g'
            ],
            detail_url=detail_url,
            content_field_list=[
                content_field_list_0
            ],
            is_only_show_executor=True,
            priority=20,
            notify_configs=notify_configs,
            biz_category_id='123',
            action_list=[
                action_list_0
            ],
            todo_type='TODO',
            reminder_time_stamp=1748226368571,
            remind_notify_configs=remind_notify_configs
        )
        try:
            await client.create_todo_task_with_options_async('PUoixxxxGiP6g', create_todo_task_request, create_todo_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest\remindNotifyConfigs;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest\actionList\param;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest\actionList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest\notifyConfigs;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest\contentFieldList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest\detailUrl;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTaskRequest;
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
        $createTodoTaskHeaders = new CreateTodoTaskHeaders([]);
        $createTodoTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $remindNotifyConfigs = new remindNotifyConfigs([
            "dingNotify" => "1",
            "sendTodoApn" => "true"
        ]);
        $actionList0Param = new param([
            "body" => "xxx"
        ]);
        $actionList0 = new actionList([
            "title" => "去查看",
            "actionType" => 2,
            "param" => $actionList0Param,
            "url" => "https://www.dingtalk.com/",
            "actionKey" => "ak-1-1",
            "pcUrl" => "xxx"
        ]);
        $notifyConfigs = new notifyConfigs([
            "dingNotify" => "1",
            "sendTodoApn" => "true",
            "sendAssistantChat" => "true"
        ]);
        $contentFieldList0 = new contentFieldList([
            "fieldKey" => "xxx",
            "fieldValue" => "xxx"
        ]);
        $detailUrl = new detailUrl([
            "appUrl" => "https://www.dingtalk.com",
            "pcUrl" => "https://www.dingtalk.com"
        ]);
        $createTodoTaskRequest = new CreateTodoTaskRequest([
            "operatorId" => "PUoiinWIpxxx",
            "sourceId" => "isv_dingtalkTodo1",
            "subject" => "接入钉钉待办",
            "creatorId" => "PUoiiP6g",
            "description" => "应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。",
            "dueTime" => 1617675000000,
            "executorIds" => [
                "PUoiixxxxhiiGiP6g"
            ],
            "participantIds" => [
                "PUoxxxxiGiP6g"
            ],
            "detailUrl" => $detailUrl,
            "contentFieldList" => [
                $contentFieldList0
            ],
            "isOnlyShowExecutor" => true,
            "priority" => 20,
            "notifyConfigs" => $notifyConfigs,
            "bizCategoryId" => "123",
            "actionList" => [
                $actionList0
            ],
            "todoType" => "TODO",
            "reminderTimeStamp" => 1748226368571,
            "remindNotifyConfigs" => $remindNotifyConfigs
        ]);
        try {
            $client->createTodoTaskWithOptions("PUoixxxxGiP6g", $createTodoTaskRequest, $createTodoTaskHeaders, new RuntimeOptions([]));
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
  dingtalktodo_1_0  "github.com/alibabacloud-go/dingtalk/todo_1_0"
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
func CreateClient () (_result *dingtalktodo_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalktodo_1_0.Client{}
  _result, _err = dingtalktodo_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createTodoTaskHeaders := &dingtalktodo_1_0.CreateTodoTaskHeaders{}
  createTodoTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  remindNotifyConfigs := &dingtalktodo_1_0.CreateTodoTaskRequestRemindNotifyConfigs{
    DingNotify: tea.String("1"),
    SendTodoApn: tea.String("true"),
  }
  actionList0Param := &dingtalktodo_1_0.CreateTodoTaskRequestActionListParam{
    Body: tea.String("xxx"),
  }
  actionList0 := &dingtalktodo_1_0.CreateTodoTaskRequestActionList{
    Title: tea.String("去查看"),
    ActionType: tea.Int32(2),
    Param: actionList0Param,
    Url: tea.String("https://www.dingtalk.com/"),
    ActionKey: tea.String("ak-1-1"),
    PcUrl: tea.String("xxx"),
  }
  notifyConfigs := &dingtalktodo_1_0.CreateTodoTaskRequestNotifyConfigs{
    DingNotify: tea.String("1"),
    SendTodoApn: tea.String("true"),
    SendAssistantChat: tea.String("true"),
  }
  contentFieldList0 := &dingtalktodo_1_0.CreateTodoTaskRequestContentFieldList{
    FieldKey: tea.String("xxx"),
    FieldValue: tea.String("xxx"),
  }
  detailUrl := &dingtalktodo_1_0.CreateTodoTaskRequestDetailUrl{
    AppUrl: tea.String("https://www.dingtalk.com"),
    PcUrl: tea.String("https://www.dingtalk.com"),
  }
  createTodoTaskRequest := &dingtalktodo_1_0.CreateTodoTaskRequest{
    OperatorId: tea.String("PUoiinWIpxxx"),
    SourceId: tea.String("isv_dingtalkTodo1"),
    Subject: tea.String("接入钉钉待办"),
    CreatorId: tea.String("PUoiiP6g"),
    Description: tea.String("应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。"),
    DueTime: tea.Int64(1617675000000),
    ExecutorIds: []*string{tea.String("PUoiixxxxhiiGiP6g")},
    ParticipantIds: []*string{tea.String("PUoxxxxiGiP6g")},
    DetailUrl: detailUrl,
    ContentFieldList: []*dingtalktodo_1_0.CreateTodoTaskRequestContentFieldList{contentFieldList0},
    IsOnlyShowExecutor: tea.Bool(true),
    Priority: tea.Int32(20),
    NotifyConfigs: notifyConfigs,
    BizCategoryId: tea.String("123"),
    ActionList: []*dingtalktodo_1_0.CreateTodoTaskRequestActionList{actionList0},
    TodoType: tea.String("TODO"),
    ReminderTimeStamp: tea.Int64(1748226368571),
    RemindNotifyConfigs: remindNotifyConfigs,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTodoTaskWithOptions(tea.String("PUoixxxxGiP6g"), createTodoTaskRequest, createTodoTaskHeaders, &util.RuntimeOptions{})
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
const dingtalktodo_1_0 = require('@alicloud/dingtalk/todo_1_0');
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
    return new dingtalktodo_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createTodoTaskHeaders = new dingtalktodo_1_0.CreateTodoTaskHeaders({ });
    createTodoTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let remindNotifyConfigs = new dingtalktodo_1_0.CreateTodoTaskRequestRemindNotifyConfigs({
      dingNotify: '1',
      sendTodoApn: 'true',
    });
    let actionList0Param = new dingtalktodo_1_0.CreateTodoTaskRequestActionListParam({
      body: 'xxx',
    });
    let actionList0 = new dingtalktodo_1_0.CreateTodoTaskRequestActionList({
      title: '去查看',
      actionType: 2,
      param: actionList0Param,
      url: 'https://www.dingtalk.com/',
      actionKey: 'ak-1-1',
      pcUrl: 'xxx',
    });
    let notifyConfigs = new dingtalktodo_1_0.CreateTodoTaskRequestNotifyConfigs({
      dingNotify: '1',
      sendTodoApn: 'true',
      sendAssistantChat: 'true',
    });
    let contentFieldList0 = new dingtalktodo_1_0.CreateTodoTaskRequestContentFieldList({
      fieldKey: 'xxx',
      fieldValue: 'xxx',
    });
    let detailUrl = new dingtalktodo_1_0.CreateTodoTaskRequestDetailUrl({
      appUrl: 'https://www.dingtalk.com',
      pcUrl: 'https://www.dingtalk.com',
    });
    let createTodoTaskRequest = new dingtalktodo_1_0.CreateTodoTaskRequest({
      operatorId: 'PUoiinWIpxxx',
      sourceId: 'isv_dingtalkTodo1',
      subject: '接入钉钉待办',
      creatorId: 'PUoiiP6g',
      description: '应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。',
      dueTime: 1617675000000,
      executorIds: [
        'PUoiixxxxhiiGiP6g'
      ],
      participantIds: [
        'PUoxxxxiGiP6g'
      ],
      detailUrl: detailUrl,
      contentFieldList: [
        contentFieldList0
      ],
      isOnlyShowExecutor: true,
      priority: 20,
      notifyConfigs: notifyConfigs,
      bizCategoryId: '123',
      actionList: [
        actionList0
      ],
      todoType: 'TODO',
      reminderTimeStamp: 1748226368571,
      remindNotifyConfigs: remindNotifyConfigs,
    });
    try {
      await client.createTodoTaskWithOptions('PUoixxxxGiP6g', createTodoTaskRequest, createTodoTaskHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalktodo_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalktodo_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalktodo_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskHeaders createTodoTaskHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskHeaders();
            createTodoTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestRemindNotifyConfigs remindNotifyConfigs = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestRemindNotifyConfigs
            {
                DingNotify = "1",
                SendTodoApn = "true",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList.CreateTodoTaskRequestActionListParam actionList0Param = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList.CreateTodoTaskRequestActionListParam
            {
                Body = "xxx",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList actionList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList
            {
                Title = "去查看",
                ActionType = 2,
                Param = actionList0Param,
                Url = "https://www.dingtalk.com/",
                ActionKey = "ak-1-1",
                PcUrl = "xxx",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestNotifyConfigs notifyConfigs = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestNotifyConfigs
            {
                DingNotify = "1",
                SendTodoApn = "true",
                SendAssistantChat = "true",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestContentFieldList contentFieldList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestContentFieldList
            {
                FieldKey = "xxx",
                FieldValue = "xxx",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestDetailUrl detailUrl = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestDetailUrl
            {
                AppUrl = "https://www.dingtalk.com",
                PcUrl = "https://www.dingtalk.com",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest createTodoTaskRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest
            {
                OperatorId = "PUoiinWIpxxx",
                SourceId = "isv_dingtalkTodo1",
                Subject = "接入钉钉待办",
                CreatorId = "PUoiiP6g",
                Description = "应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。",
                DueTime = 1617675000000,
                ExecutorIds = new List<string>
                {
                    "PUoiixxxxhiiGiP6g"
                },
                ParticipantIds = new List<string>
                {
                    "PUoxxxxiGiP6g"
                },
                DetailUrl = detailUrl,
                ContentFieldList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestContentFieldList>
                {
                    contentFieldList0
                },
                IsOnlyShowExecutor = true,
                Priority = 20,
                NotifyConfigs = notifyConfigs,
                BizCategoryId = "123",
                ActionList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTaskRequest.CreateTodoTaskRequestActionList>
                {
                    actionList0
                },
                TodoType = "TODO",
                ReminderTimeStamp = 1748226368571,
                RemindNotifyConfigs = remindNotifyConfigs,
            };
            try
            {
                client.CreateTodoTaskWithOptions("PUoixxxxGiP6g", createTodoTaskRequest, createTodoTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 待办ID。 |
| subject | String | 待办的标题。 |
| description | String | 待办描述。 |
| startTime | Long | 开始时间，Unix时间戳，单位毫秒。 |
| dueTime | Long | 截止时间，Unix时间戳，单位毫秒。 |
| finishTime | Long | 完成时间，Unix时间戳，单位毫秒。 |
| done | Boolean | 完成状态。 |
| executorIds | Array of String | 执行者的unionId。 |
| participantIds | Array of String | 参与者的unionId。 |
| detailUrl | Object | 详情页url跳转地址。 |
| pcUrl | String | PC端详情页url跳转地址。 |
| appUrl | String | APP端详情页url跳转地址。 |
| source | String | 业务来源。 |
| sourceId | String | 业务系统侧的唯一标识ID，即业务ID。 |
| createdTime | Long | 创建时间，Unix时间戳，单位毫秒。 |
| modifiedTime | Long | 更新时间，Unix时间戳，单位毫秒。 |
| creatorId | String | 创建者的unionId。 |
| modifierId | String | 更新者的unionId。 |
| bizTag | String | 接入应用标识。 |
| requestId | String | 请求ID。 |
| contentFieldList | Array | 内容区表单字段配置 |
| fieldKey | String | 字段唯一标识。 |
| fieldValue | String | 字段值。 |
| isOnlyShowExecutor | Boolean | 生成的待办是否仅展示在执行者的待办列表中。 |
| priority | Integer | 优先级，取值：   - **10**：较低 - **20**：普通 - **30**：较高 - **40**：紧急 |
| notifyConfigs | Object | 待办通知配置。 |
| dingNotify | String | DING通知配置，目前仅支持取值为**1**，表示应用内DING。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "OPJxxxxxURjrzd",
  "subject" : "接入钉钉待办",
  "description" : "应用可以调用该接口发起一个钉钉待办任务，该待办事项会出现在钉钉客户端“待办”页面，需要注意的是，通过开放接口发起的待办，目前仅支持直接跳转ISV应用详情页（ISV在调该接口时需传入自身应用详情页链接）。",
  "startTime" : 1617675000000,
  "dueTime" : 1617675100000,
  "finishTime" : 1617675200000,
  "done" : false,
  "executorIds" : [ "PUoiinxxxxGiP6g" ],
  "participantIds" : [ "PUoiinxxxxiiGiP6g" ],
  "detailUrl" : {
    "pcUrl" : "https://www.dingtalk.com",
    "appUrl" : "https://www.dingtalk.com"
  },
  "source" : "isv_dingtalkTodo",
  "sourceId" : "isv_dingtalkTodo1",
  "createdTime" : 1617675200000,
  "modifiedTime" : 1617675200000,
  "creatorId" : "PUoiixxxxx",
  "modifierId" : "PUoiinxxxxx",
  "bizTag" : "isv_dingtalkTodo",
  "requestId" : "12345",
  "contentFieldList" : [ {
    "fieldKey" : "xxx",
    "fieldValue" : "xxx"
  } ],
  "isOnlyShowExecutor" : true,
  "priority" : 20,
  "notifyConfigs" : {
    "dingNotify" : "1"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.taskCreate.lockError | todo.taskCreate.lockError | 创建待办根据sourceId加锁失败 |
| 400 | todo.taskCreate.paramError | task exist | 待办任务已存在 |
| 400 | todo.taskCreate.paramError | subject is oversize | 待办标题长度超出限制 |
| 400 | todo.taskCreate.paramError | description is oversize | 待办描述长度超出限制 |
| 400 | todo.taskCreate.paramError | executors is oversize | 待办执行人超出限制 |
| 400 | todo.taskCreate.paramError | participants is oversize | 待办参与人超出限制 |
| 400 | todo.taskCreate.paramError | dueTime is invalid | 待办截止时间非法 |
| 400 | todo.taskCreate.paramError | todo.taskCreate.paramError | 创建待办参数异常 |
| 400 | todo.taskCreate.flowControlError | flowControl because of executorId or orgId | 创建待办针对执行者或者企业进行了限流处理 |
| 500 | todo.taskCreate.systemError | todo.taskCreate.systemError | 创建待办系统内部异常 |
