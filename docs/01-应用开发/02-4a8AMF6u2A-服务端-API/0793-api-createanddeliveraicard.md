---
title: "创建并投放 AI 卡片"
source_url: "https://open.dingtalk.com/document/development/api-createanddeliveraicard"
namespace: "development"
slug: "api-createanddeliveraicard"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > AI 卡片 > 创建并投放 AI 卡片"
doc_id: "49U7yLEq0J"
updated_at: "2026-10-26 09:07:38"
---

> Source: https://open.dingtalk.com/document/development/api-createanddeliveraicard
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > AI 卡片 > 创建并投放 AI 卡片
> Updated: 2026-10-26 09:07:38

# 创建并投放 AI 卡片

调用本接口，创建并且投递AI卡片

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/ai/instances/createAndDeliver |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-AICard.Instance.Write-AI卡片实例写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0032-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0033-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 否 | 卡片创建者开放 ID，不是消息发送者或单聊接收者。 |
| userIdType | Integer | 否 | 用户 ID 类型：   - **1**=staffId - **2**=unionId   **[!NOTE]**  `recipients` 始终为 `staffId`。 |
| outTrackId | String | 是 | 应用和企业范围内的业务卡片标识，非空，长度限制与普通卡片一致。 |
| openSpaceId | String | 是 | 仅一个 `im_group` 或 `im_robot` 目标，不支持分号分隔多个目标。 |
| imGroupOpenSpaceModel | Object | 否 | 群聊场域属性，仅群聊目标可传。 |
| supportForward | Boolean | 否 | 是否支持转发，仅支持 false，传 true 将被拒绝。 |
| lastMessageI18n | Map<String, String> | 否 | 国际化会话摘要，与卡片降级摘要 summary 分开配置。 |
| searchSupport | Object | 否 | 搜索展示属性。 |
| searchIcon | String | 否 | 搜索图标。 |
| searchTypeName | String | 否 | 国际化搜索类型名 JSON 字符串。 |
| searchDesc | String | 否 | 搜索描述。 |
| notification | Object | 否 | 通知信息。 |
| alertContent | String | 否 | 通知文案。 |
| notificationOff | Boolean | 否 | 是否关闭通知。 |
| imRobotOpenSpaceModel | Object | 否 | 机器人单聊场域属性，仅单聊时可传。 |
| supportForward | Boolean | 否 | 是否支持转发，仅支持 false，传 true 将被拒绝。 |
| lastMessageI18n | Map<String, String> | 否 | 国际化会话摘要，与卡片降级摘要 summary 分开配置。 |
| searchSupport | Object | 否 | 搜索展示属性。 |
| searchIcon | String | 否 | 搜索图标。 |
| searchTypeName | String | 否 | 国际化搜索类型名 JSON 字符串。 |
| searchDesc | String | 否 | 搜索描述。 |
| notification | Object | 否 | 通知信息 |
| alertContent | String | 否 | 通知文案 |
| notificationOff | Boolean | 否 | 是否关闭通知：   - **true**：关闭 - **false**：不关闭 |
| imGroupOpenDeliverModel | Object | 否 | 群聊投递参数。  **[!NOTE]**  `openSpaceId` 为 `im_group` 时必填，不能同时传单聊模型。 |
| robotCode | String | 是 | 机器人 code，群聊必填。 |
| atUserIds | Map<String, String> | 否 | 消息 @ 人：用户 ID 到展示名，最多 100 项。  **[!NOTE]**  JSON 总大小不超过 16 KiB（UTF-8），由服务端校验。 |
| recipients | Array of String | 否 | 指定接收者 staffId，最多 100 个，始终按 staffId 解释。 |
| extension | Map<String, String> | 否 | 消息 Extension，最多 64 项。  **[!NOTE]**  JSON 总大小不超过 16 KiB（UTF-8），沿用普通消息扩展授权规则。 |
| imRobotOpenDeliverModel | Object | 否 | 机器人单聊投递参数。  **[!NOTE]**  `openSpaceId` 为 `im_robot` 时必填，不能同时传群聊模型。 |
| robotCode | String | 否 | 机器人 code，建议显式指定。  **[!NOTE]**  缺省沿用普通单聊机器人解析规则。 |
| atUserIds | Map<String, String> | 否 | 消息 @ 人，用户 ID 到展示名，最多 100 个。  **[!NOTE]**  JSON 总大小不超过 16 KiB（UTF-8），由服务端校验。 |
| recipients | Array of String | 否 | 指定接收者 staffId，最多 100个，始终按 staffId 解释。 |
| extension | Map<String, String> | 否 | 消息 Extension，最多 64 项。  **[!NOTE]**  JSON 总大小不超过 16 KiB（UTF-8），沿用普通消息扩展授权规则。 |
| protocolVersion | String | 否 | A2UI 协议版本，透传下游。  **[!NOTE]**  消息内部 version 使用 v1.0。 |
| flowStatus | String | 是 | 卡片流状态，使用枚举名，不使用内部数字码。 |
| a2uiMessages | Array of String | 是 | A2UI JSON 字符串列表，必填且非空，按顺序执行。  **[!NOTE]**  最多 100 条，总计不超过 256 KiB（UTF-8），由服务端校验。 |
| a2uiAnnotations | Array | 否 | 组件语义标注，最多 100 项，不传或空列表表示不新增标注。 |
| surfaceId | String | 是 | Surface 标识。 |
| componentId | String | 是 | 组件标识。 |
| type | String | 是 | 标注类型，目前仅 `artifact`。 |
| summary | String | 否 | 降级摘要纯文本，编码为 `fallbackText.summary`。  **[!NOTE]**  开放层不额外校验非空和2048字节限制。 |
| callbackType | String | 否 | 交互回调方式，仅 `HTTP/STREAM`。  **[!NOTE]**  不开放内部 HSF 回调。 |
| callbackRouteKey | String | 否 | HTTP 模式必填的已注册回调路由 key。  **[!NOTE]**  `STREAM` 模式不得传非空值。 |
| bizContext | Map<String, String> | 否 | 创建后不可变的回调业务关联信息，最多 32 项。  **[!NOTE]**  JSON 总计 4096 字节（UTF-8）；key 禁用 `__`、`sys.`、`dingtalk.` 前缀。 |
| cardAtUserIds | Array of String | 否 | `userIdType`解释。 |
| atAll | Boolean | 否 | 卡片内容是否 @ 全员，沿用普通投递权限规则。 |

### **请求示例**

HTTP

```
POST /v1.0/card/ai/instances/createAndDeliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2f52eexxxxc5ce510
Content-Type:application/json

{
  "userId" : "user1",
  "userIdType" : 2,
  "outTrackId" : "trackid123",
  "openSpaceId" : "dtv1.card//im_group.cid_example",
  "imGroupOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
      "key" : "summary"
    },
    "searchSupport" : {
      "searchIcon" : "icon",
      "searchTypeName" : "6522xxxx9784",
      "searchDesc" : "张三的设备"
    },
    "notification" : {
      "alertContent" : "测试",
      "notificationOff" : false
    }
  },
  "imRobotOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
      "key" : "summary"
    },
    "searchSupport" : {
      "searchIcon" : "icon",
      "searchTypeName" : "json字符",
      "searchDesc" : "测试一下"
    },
    "notification" : {
      "alertContent" : "测试文案",
      "notificationOff" : false
    }
  },
  "imGroupOpenDeliverModel" : {
    "robotCode" : "robot123",
    "atUserIds" : {
      "key" : "user1"
    },
    "recipients" : [ "staffId1" ],
    "extension" : {
      "key" : "Extension"
    }
  },
  "imRobotOpenDeliverModel" : {
    "robotCode" : "robot123",
    "atUserIds" : {
      "key" : "user1"
    },
    "recipients" : [ "staffId1" ],
    "extension" : {
      "key" : "xtension"
    }
  },
  "protocolVersion" : "1.0",
  "flowStatus" : "PROCESSING",
  "a2uiMessages" : [ "a2uiMessages" ],
  "a2uiAnnotations" : [ {
    "surfaceId" : "Surface",
    "componentId" : "组件",
    "type" : "artifact"
  } ],
  "summary" : "测试",
  "callbackType" : "STREAM",
  "callbackRouteKey" : "6522xxxx9784",
  "bizContext" : {
    "key" : "测试一下，确定没问题"
  },
  "cardAtUserIds" : [ "123" ],
  "atAll" : false
}
```

Java

```
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
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardHeaders createAndDeliverAICardHeaders = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardHeaders();
        createAndDeliverAICardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        java.util.Map<String, String> bizContext = TeaConverter.buildMap(
            new TeaPair("key", "测试一下，确定没问题")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestA2uiAnnotations a2uiAnnotations0 = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestA2uiAnnotations()
                .setSurfaceId("Surface")
                .setComponentId("组件")
                .setType("artifact");
        java.util.Map<String, String> imRobotOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "xtension")
        );
        java.util.Map<String, String> imRobotOpenDeliverModelAtUserIds = TeaConverter.buildMap(
            new TeaPair("key", "user1")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenDeliverModel imRobotOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenDeliverModel()
                .setRobotCode("robot123")
                .setAtUserIds(imRobotOpenDeliverModelAtUserIds)
                .setRecipients(java.util.Arrays.asList(
                    "staffId1"
                ))
                .setExtension(imRobotOpenDeliverModelExtension);
        java.util.Map<String, String> imGroupOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "Extension")
        );
        java.util.Map<String, String> imGroupOpenDeliverModelAtUserIds = TeaConverter.buildMap(
            new TeaPair("key", "user1")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenDeliverModel()
                .setRobotCode("robot123")
                .setAtUserIds(imGroupOpenDeliverModelAtUserIds)
                .setRecipients(java.util.Arrays.asList(
                    "staffId1"
                ))
                .setExtension(imGroupOpenDeliverModelExtension);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification()
                .setAlertContent("测试文案")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport()
                .setSearchIcon("icon")
                .setSearchTypeName("json字符")
                .setSearchDesc("测试一下");
        java.util.Map<String, String> imRobotOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "summary")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel()
                .setSupportForward(false)
                .setLastMessageI18n(imRobotOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imRobotOpenSpaceModelSearchSupport)
                .setNotification(imRobotOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification()
                .setAlertContent("测试")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport()
                .setSearchIcon("icon")
                .setSearchTypeName("6522xxxx9784")
                .setSearchDesc("张三的设备");
        java.util.Map<String, String> imGroupOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "summary")
        );
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel()
                .setSupportForward(false)
                .setLastMessageI18n(imGroupOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imGroupOpenSpaceModelSearchSupport)
                .setNotification(imGroupOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest createAndDeliverAICardRequest = new com.aliyun.dingtalkcard_1_0.models.CreateAndDeliverAICardRequest()
                .setUserId("user1")
                .setUserIdType(2)
                .setOutTrackId("trackid123")
                .setOpenSpaceId("dtv1.card//im_group.cid_example")
                .setImGroupOpenSpaceModel(imGroupOpenSpaceModel)
                .setImRobotOpenSpaceModel(imRobotOpenSpaceModel)
                .setImGroupOpenDeliverModel(imGroupOpenDeliverModel)
                .setImRobotOpenDeliverModel(imRobotOpenDeliverModel)
                .setProtocolVersion("1.0")
                .setFlowStatus("PROCESSING")
                .setA2uiMessages(java.util.Arrays.asList(
                    "a2uiMessages"
                ))
                .setA2uiAnnotations(java.util.Arrays.asList(
                    a2uiAnnotations0
                ))
                .setSummary("测试")
                .setCallbackType("STREAM")
                .setCallbackRouteKey("6522xxxx9784")
                .setBizContext(bizContext)
                .setCardAtUserIds(java.util.Arrays.asList(
                    "123"
                ))
                .setAtAll(false);
        try {
            client.createAndDeliverAICardWithOptions(createAndDeliverAICardRequest, createAndDeliverAICardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
import json

from typing import List

from alibabacloud_dingtalk.card_1_0.client import Client as dingtalkcard_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.card_1_0 import models as dingtalkcard__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcard_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcard_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_and_deliver_aicard_headers = dingtalkcard__1__0_models.CreateAndDeliverAICardHeaders()
        create_and_deliver_aicard_headers.x_acs_dingtalk_access_token = '<your access token>'
        biz_context = {
            'key': '测试一下，确定没问题'
        }
        a_2ui_annotations_0 = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestA2uiAnnotations(
            surface_id='Surface',
            component_id='组件',
            type='artifact'
        )
        im_robot_open_deliver_model_extension = {
            'key': 'xtension'
        }
        im_robot_open_deliver_model_at_user_ids = {
            'key': 'user1'
        }
        im_robot_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenDeliverModel(
            robot_code='robot123',
            at_user_ids=im_robot_open_deliver_model_at_user_ids,
            recipients=[
                'staffId1'
            ],
            extension=im_robot_open_deliver_model_extension
        )
        im_group_open_deliver_model_extension = {
            'key': 'Extension'
        }
        im_group_open_deliver_model_at_user_ids = {
            'key': 'user1'
        }
        im_group_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenDeliverModel(
            robot_code='robot123',
            at_user_ids=im_group_open_deliver_model_at_user_ids,
            recipients=[
                'staffId1'
            ],
            extension=im_group_open_deliver_model_extension
        )
        im_robot_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification(
            alert_content='测试文案',
            notification_off=False
        )
        im_robot_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport(
            search_icon='icon',
            search_type_name='json字符',
            search_desc='测试一下'
        )
        im_robot_open_space_model_last_message_i18n = {
            'key': 'summary'
        }
        im_robot_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_robot_open_space_model_last_message_i18n,
            search_support=im_robot_open_space_model_search_support,
            notification=im_robot_open_space_model_notification
        )
        im_group_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification(
            alert_content='测试',
            notification_off=False
        )
        im_group_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport(
            search_icon='icon',
            search_type_name='6522xxxx9784',
            search_desc='张三的设备'
        )
        im_group_open_space_model_last_message_i18n = {
            'key': 'summary'
        }
        im_group_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_group_open_space_model_last_message_i18n,
            search_support=im_group_open_space_model_search_support,
            notification=im_group_open_space_model_notification
        )
        create_and_deliver_aicard_request = dingtalkcard__1__0_models.CreateAndDeliverAICardRequest(
            user_id='user1',
            user_id_type=2,
            out_track_id='trackid123',
            open_space_id='dtv1.card//im_group.cid_example',
            im_group_open_space_model=im_group_open_space_model,
            im_robot_open_space_model=im_robot_open_space_model,
            im_group_open_deliver_model=im_group_open_deliver_model,
            im_robot_open_deliver_model=im_robot_open_deliver_model,
            protocol_version='1.0',
            flow_status='PROCESSING',
            a_2ui_messages=[
                'a2uiMessages'
            ],
            a_2ui_annotations=[
                a_2ui_annotations_0
            ],
            summary='测试',
            callback_type='STREAM',
            callback_route_key='6522xxxx9784',
            biz_context=biz_context,
            card_at_user_ids=[
                '123'
            ],
            at_all=False
        )
        try:
            client.create_and_deliver_aicard_with_options(create_and_deliver_aicard_request, create_and_deliver_aicard_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_and_deliver_aicard_headers = dingtalkcard__1__0_models.CreateAndDeliverAICardHeaders()
        create_and_deliver_aicard_headers.x_acs_dingtalk_access_token = '<your access token>'
        biz_context = {
            'key': '测试一下，确定没问题'
        }
        a_2ui_annotations_0 = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestA2uiAnnotations(
            surface_id='Surface',
            component_id='组件',
            type='artifact'
        )
        im_robot_open_deliver_model_extension = {
            'key': 'xtension'
        }
        im_robot_open_deliver_model_at_user_ids = {
            'key': 'user1'
        }
        im_robot_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenDeliverModel(
            robot_code='robot123',
            at_user_ids=im_robot_open_deliver_model_at_user_ids,
            recipients=[
                'staffId1'
            ],
            extension=im_robot_open_deliver_model_extension
        )
        im_group_open_deliver_model_extension = {
            'key': 'Extension'
        }
        im_group_open_deliver_model_at_user_ids = {
            'key': 'user1'
        }
        im_group_open_deliver_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenDeliverModel(
            robot_code='robot123',
            at_user_ids=im_group_open_deliver_model_at_user_ids,
            recipients=[
                'staffId1'
            ],
            extension=im_group_open_deliver_model_extension
        )
        im_robot_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification(
            alert_content='测试文案',
            notification_off=False
        )
        im_robot_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport(
            search_icon='icon',
            search_type_name='json字符',
            search_desc='测试一下'
        )
        im_robot_open_space_model_last_message_i18n = {
            'key': 'summary'
        }
        im_robot_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImRobotOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_robot_open_space_model_last_message_i18n,
            search_support=im_robot_open_space_model_search_support,
            notification=im_robot_open_space_model_notification
        )
        im_group_open_space_model_notification = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification(
            alert_content='测试',
            notification_off=False
        )
        im_group_open_space_model_search_support = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport(
            search_icon='icon',
            search_type_name='6522xxxx9784',
            search_desc='张三的设备'
        )
        im_group_open_space_model_last_message_i18n = {
            'key': 'summary'
        }
        im_group_open_space_model = dingtalkcard__1__0_models.CreateAndDeliverAICardRequestImGroupOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_group_open_space_model_last_message_i18n,
            search_support=im_group_open_space_model_search_support,
            notification=im_group_open_space_model_notification
        )
        create_and_deliver_aicard_request = dingtalkcard__1__0_models.CreateAndDeliverAICardRequest(
            user_id='user1',
            user_id_type=2,
            out_track_id='trackid123',
            open_space_id='dtv1.card//im_group.cid_example',
            im_group_open_space_model=im_group_open_space_model,
            im_robot_open_space_model=im_robot_open_space_model,
            im_group_open_deliver_model=im_group_open_deliver_model,
            im_robot_open_deliver_model=im_robot_open_deliver_model,
            protocol_version='1.0',
            flow_status='PROCESSING',
            a_2ui_messages=[
                'a2uiMessages'
            ],
            a_2ui_annotations=[
                a_2ui_annotations_0
            ],
            summary='测试',
            callback_type='STREAM',
            callback_route_key='6522xxxx9784',
            biz_context=biz_context,
            card_at_user_ids=[
                '123'
            ],
            at_all=False
        )
        try:
            await client.create_and_deliver_aicard_with_options_async(create_and_deliver_aicard_request, create_and_deliver_aicard_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\a2uiAnnotations;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imRobotOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imGroupOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imRobotOpenSpaceModel\notification;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imRobotOpenSpaceModel\searchSupport;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imRobotOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imGroupOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest;
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
        $createAndDeliverAICardHeaders = new CreateAndDeliverAICardHeaders([]);
        $createAndDeliverAICardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $bizContext = [
            "key" => "测试一下，确定没问题"
        ];
        $a2uiAnnotations0 = new a2uiAnnotations([
            "surfaceId" => "Surface",
            "componentId" => "组件",
            "type" => "artifact"
        ]);
        $imRobotOpenDeliverModelExtension = [
            "key" => "xtension"
        ];
        $imRobotOpenDeliverModelAtUserIds = [
            "key" => "user1"
        ];
        $imRobotOpenDeliverModel = new imRobotOpenDeliverModel([
            "robotCode" => "robot123",
            "atUserIds" => $imRobotOpenDeliverModelAtUserIds,
            "recipients" => [
                "staffId1"
            ],
            "extension" => $imRobotOpenDeliverModelExtension
        ]);
        $imGroupOpenDeliverModelExtension = [
            "key" => "Extension"
        ];
        $imGroupOpenDeliverModelAtUserIds = [
            "key" => "user1"
        ];
        $imGroupOpenDeliverModel = new imGroupOpenDeliverModel([
            "robotCode" => "robot123",
            "atUserIds" => $imGroupOpenDeliverModelAtUserIds,
            "recipients" => [
                "staffId1"
            ],
            "extension" => $imGroupOpenDeliverModelExtension
        ]);
        $imRobotOpenSpaceModelNotification = new notification([
            "alertContent" => "测试文案",
            "notificationOff" => false
        ]);
        $imRobotOpenSpaceModelSearchSupport = new searchSupport([
            "searchIcon" => "icon",
            "searchTypeName" => "json字符",
            "searchDesc" => "测试一下"
        ]);
        $imRobotOpenSpaceModelLastMessageI18n = [
            "key" => "summary"
        ];
        $imRobotOpenSpaceModel = new imRobotOpenSpaceModel([
            "supportForward" => false,
            "lastMessageI18n" => $imRobotOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imRobotOpenSpaceModelSearchSupport,
            "notification" => $imRobotOpenSpaceModelNotification
        ]);
        $imGroupOpenSpaceModelNotification = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imGroupOpenSpaceModel\notification([
            "alertContent" => "测试",
            "notificationOff" => false
        ]);
        $imGroupOpenSpaceModelSearchSupport = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\CreateAndDeliverAICardRequest\imGroupOpenSpaceModel\searchSupport([
            "searchIcon" => "icon",
            "searchTypeName" => "6522xxxx9784",
            "searchDesc" => "张三的设备"
        ]);
        $imGroupOpenSpaceModelLastMessageI18n = [
            "key" => "summary"
        ];
        $imGroupOpenSpaceModel = new imGroupOpenSpaceModel([
            "supportForward" => false,
            "lastMessageI18n" => $imGroupOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imGroupOpenSpaceModelSearchSupport,
            "notification" => $imGroupOpenSpaceModelNotification
        ]);
        $createAndDeliverAICardRequest = new CreateAndDeliverAICardRequest([
            "userId" => "user1",
            "userIdType" => 2,
            "outTrackId" => "trackid123",
            "openSpaceId" => "dtv1.card//im_group.cid_example",
            "imGroupOpenSpaceModel" => $imGroupOpenSpaceModel,
            "imRobotOpenSpaceModel" => $imRobotOpenSpaceModel,
            "imGroupOpenDeliverModel" => $imGroupOpenDeliverModel,
            "imRobotOpenDeliverModel" => $imRobotOpenDeliverModel,
            "protocolVersion" => "1.0",
            "flowStatus" => "PROCESSING",
            "a2uiMessages" => [
                "a2uiMessages"
            ],
            "a2uiAnnotations" => [
                $a2uiAnnotations0
            ],
            "summary" => "测试",
            "callbackType" => "STREAM",
            "callbackRouteKey" => "6522xxxx9784",
            "bizContext" => $bizContext,
            "cardAtUserIds" => [
                "123"
            ],
            "atAll" => false
        ]);
        try {
            $client->createAndDeliverAICardWithOptions($createAndDeliverAICardRequest, $createAndDeliverAICardHeaders, new RuntimeOptions([]));
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
package main

import (
  "encoding/json"
  "strings"
  "fmt"
  "os"
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
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
func CreateClient () (_result *dingtalkcard_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcard_1_0.Client{}
  _result, _err = dingtalkcard_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createAndDeliverAICardHeaders := &dingtalkcard_1_0.CreateAndDeliverAICardHeaders{}
  createAndDeliverAICardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  bizContext := map[string]*string{
    "key": tea.String("测试一下，确定没问题"),
  }
  a2uiAnnotations0 := &dingtalkcard_1_0.CreateAndDeliverAICardRequestA2uiAnnotations{
    SurfaceId: tea.String("Surface"),
    ComponentId: tea.String("组件"),
    Type: tea.String("artifact"),
  }
  imRobotOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("xtension"),
  }
  imRobotOpenDeliverModelAtUserIds := map[string]*string{
    "key": tea.String("user1"),
  }
  imRobotOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenDeliverModel{
    RobotCode: tea.String("robot123"),
    AtUserIds: imRobotOpenDeliverModelAtUserIds,
    Recipients: []*string{tea.String("staffId1")},
    Extension: imRobotOpenDeliverModelExtension,
  }
  imGroupOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("Extension"),
  }
  imGroupOpenDeliverModelAtUserIds := map[string]*string{
    "key": tea.String("user1"),
  }
  imGroupOpenDeliverModel := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenDeliverModel{
    RobotCode: tea.String("robot123"),
    AtUserIds: imGroupOpenDeliverModelAtUserIds,
    Recipients: []*string{tea.String("staffId1")},
    Extension: imGroupOpenDeliverModelExtension,
  }
  imRobotOpenSpaceModelNotification := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification{
    AlertContent: tea.String("测试文案"),
    NotificationOff: tea.Bool(false),
  }
  imRobotOpenSpaceModelSearchSupport := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("icon"),
    SearchTypeName: tea.String("json字符"),
    SearchDesc: tea.String("测试一下"),
  }
  imRobotOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("summary"),
  }
  imRobotOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenSpaceModel{
    SupportForward: tea.Bool(false),
    LastMessageI18n: imRobotOpenSpaceModelLastMessageI18n,
    SearchSupport: imRobotOpenSpaceModelSearchSupport,
    Notification: imRobotOpenSpaceModelNotification,
  }
  imGroupOpenSpaceModelNotification := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification{
    AlertContent: tea.String("测试"),
    NotificationOff: tea.Bool(false),
  }
  imGroupOpenSpaceModelSearchSupport := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("icon"),
    SearchTypeName: tea.String("6522xxxx9784"),
    SearchDesc: tea.String("张三的设备"),
  }
  imGroupOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("summary"),
  }
  imGroupOpenSpaceModel := &dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenSpaceModel{
    SupportForward: tea.Bool(false),
    LastMessageI18n: imGroupOpenSpaceModelLastMessageI18n,
    SearchSupport: imGroupOpenSpaceModelSearchSupport,
    Notification: imGroupOpenSpaceModelNotification,
  }
  createAndDeliverAICardRequest := &dingtalkcard_1_0.CreateAndDeliverAICardRequest{
    UserId: tea.String("user1"),
    UserIdType: tea.Int32(2),
    OutTrackId: tea.String("trackid123"),
    OpenSpaceId: tea.String("dtv1.card//im_group.cid_example"),
    ImGroupOpenSpaceModel: imGroupOpenSpaceModel,
    ImRobotOpenSpaceModel: imRobotOpenSpaceModel,
    ImGroupOpenDeliverModel: imGroupOpenDeliverModel,
    ImRobotOpenDeliverModel: imRobotOpenDeliverModel,
    ProtocolVersion: tea.String("1.0"),
    FlowStatus: tea.String("PROCESSING"),
    A2uiMessages: []*string{tea.String("a2uiMessages")},
    A2uiAnnotations: []*dingtalkcard_1_0.CreateAndDeliverAICardRequestA2uiAnnotations{a2uiAnnotations0},
    Summary: tea.String("测试"),
    CallbackType: tea.String("STREAM"),
    CallbackRouteKey: tea.String("6522xxxx9784"),
    BizContext: bizContext,
    CardAtUserIds: []*string{tea.String("123")},
    AtAll: tea.Bool(false),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateAndDeliverAICardWithOptions(createAndDeliverAICardRequest, createAndDeliverAICardHeaders, &util.RuntimeOptions{})
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
const dingtalkcard_1_0 = require('@alicloud/dingtalk/card_1_0');
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
    return new dingtalkcard_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createAndDeliverAICardHeaders = new dingtalkcard_1_0.CreateAndDeliverAICardHeaders({ });
    createAndDeliverAICardHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let bizContext = {
      key: '测试一下，确定没问题',
    };
    let a2uiAnnotations0 = new dingtalkcard_1_0.CreateAndDeliverAICardRequestA2uiAnnotations({
      surfaceId: 'Surface',
      componentId: '组件',
      type: 'artifact',
    });
    let imRobotOpenDeliverModelExtension = {
      key: 'xtension',
    };
    let imRobotOpenDeliverModelAtUserIds = {
      key: 'user1',
    };
    let imRobotOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenDeliverModel({
      robotCode: 'robot123',
      atUserIds: imRobotOpenDeliverModelAtUserIds,
      recipients: [
        'staffId1'
      ],
      extension: imRobotOpenDeliverModelExtension,
    });
    let imGroupOpenDeliverModelExtension = {
      key: 'Extension',
    };
    let imGroupOpenDeliverModelAtUserIds = {
      key: 'user1',
    };
    let imGroupOpenDeliverModel = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenDeliverModel({
      robotCode: 'robot123',
      atUserIds: imGroupOpenDeliverModelAtUserIds,
      recipients: [
        'staffId1'
      ],
      extension: imGroupOpenDeliverModelExtension,
    });
    let imRobotOpenSpaceModelNotification = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification({
      alertContent: '测试文案',
      notificationOff: false,
    });
    let imRobotOpenSpaceModelSearchSupport = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport({
      searchIcon: 'icon',
      searchTypeName: 'json字符',
      searchDesc: '测试一下',
    });
    let imRobotOpenSpaceModelLastMessageI18n = {
      key: 'summary',
    };
    let imRobotOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImRobotOpenSpaceModel({
      supportForward: false,
      lastMessageI18n: imRobotOpenSpaceModelLastMessageI18n,
      searchSupport: imRobotOpenSpaceModelSearchSupport,
      notification: imRobotOpenSpaceModelNotification,
    });
    let imGroupOpenSpaceModelNotification = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification({
      alertContent: '测试',
      notificationOff: false,
    });
    let imGroupOpenSpaceModelSearchSupport = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport({
      searchIcon: 'icon',
      searchTypeName: '6522xxxx9784',
      searchDesc: '张三的设备',
    });
    let imGroupOpenSpaceModelLastMessageI18n = {
      key: 'summary',
    };
    let imGroupOpenSpaceModel = new dingtalkcard_1_0.CreateAndDeliverAICardRequestImGroupOpenSpaceModel({
      supportForward: false,
      lastMessageI18n: imGroupOpenSpaceModelLastMessageI18n,
      searchSupport: imGroupOpenSpaceModelSearchSupport,
      notification: imGroupOpenSpaceModelNotification,
    });
    let createAndDeliverAICardRequest = new dingtalkcard_1_0.CreateAndDeliverAICardRequest({
      userId: 'user1',
      userIdType: 2,
      outTrackId: 'trackid123',
      openSpaceId: 'dtv1.card//im_group.cid_example',
      imGroupOpenSpaceModel: imGroupOpenSpaceModel,
      imRobotOpenSpaceModel: imRobotOpenSpaceModel,
      imGroupOpenDeliverModel: imGroupOpenDeliverModel,
      imRobotOpenDeliverModel: imRobotOpenDeliverModel,
      protocolVersion: '1.0',
      flowStatus: 'PROCESSING',
      a2uiMessages: [
        'a2uiMessages'
      ],
      a2uiAnnotations: [
        a2uiAnnotations0
      ],
      summary: '测试',
      callbackType: 'STREAM',
      callbackRouteKey: '6522xxxx9784',
      bizContext: bizContext,
      cardAtUserIds: [
        '123'
      ],
      atAll: false,
    });
    try {
      await client.createAndDeliverAICardWithOptions(createAndDeliverAICardRequest, createAndDeliverAICardHeaders, new Util.RuntimeOptions({ }));
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
using Newtonsoft.Json;
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
        public static AlibabaCloud.SDK.Dingtalkcard_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcard_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcard_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardHeaders createAndDeliverAICardHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardHeaders();
            createAndDeliverAICardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            Dictionary<string, string> bizContext = new Dictionary<string, string>
            {
                {"key", "测试一下，确定没问题"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestA2uiAnnotations a2uiAnnotations0 = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestA2uiAnnotations
            {
                SurfaceId = "Surface",
                ComponentId = "组件",
                Type = "artifact",
            };
            Dictionary<string, string> imRobotOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "xtension"},
            };
            Dictionary<string, string> imRobotOpenDeliverModelAtUserIds = new Dictionary<string, string>
            {
                {"key", "user1"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenDeliverModel imRobotOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenDeliverModel
            {
                RobotCode = "robot123",
                AtUserIds = imRobotOpenDeliverModelAtUserIds,
                Recipients = new List<string>
                {
                    "staffId1"
                },
                Extension = imRobotOpenDeliverModelExtension,
            };
            Dictionary<string, string> imGroupOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "Extension"},
            };
            Dictionary<string, string> imGroupOpenDeliverModelAtUserIds = new Dictionary<string, string>
            {
                {"key", "user1"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenDeliverModel
            {
                RobotCode = "robot123",
                AtUserIds = imGroupOpenDeliverModelAtUserIds,
                Recipients = new List<string>
                {
                    "staffId1"
                },
                Extension = imGroupOpenDeliverModelExtension,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel.CreateAndDeliverAICardRequestImRobotOpenSpaceModelNotification
            {
                AlertContent = "测试文案",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel.CreateAndDeliverAICardRequestImRobotOpenSpaceModelSearchSupport
            {
                SearchIcon = "icon",
                SearchTypeName = "json字符",
                SearchDesc = "测试一下",
            };
            Dictionary<string, string> imRobotOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "summary"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImRobotOpenSpaceModel
            {
                SupportForward = false,
                LastMessageI18n = imRobotOpenSpaceModelLastMessageI18n,
                SearchSupport = imRobotOpenSpaceModelSearchSupport,
                Notification = imRobotOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel.CreateAndDeliverAICardRequestImGroupOpenSpaceModelNotification
            {
                AlertContent = "测试",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel.CreateAndDeliverAICardRequestImGroupOpenSpaceModelSearchSupport
            {
                SearchIcon = "icon",
                SearchTypeName = "6522xxxx9784",
                SearchDesc = "张三的设备",
            };
            Dictionary<string, string> imGroupOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "summary"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestImGroupOpenSpaceModel
            {
                SupportForward = false,
                LastMessageI18n = imGroupOpenSpaceModelLastMessageI18n,
                SearchSupport = imGroupOpenSpaceModelSearchSupport,
                Notification = imGroupOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest createAndDeliverAICardRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest
            {
                UserId = "user1",
                UserIdType = 2,
                OutTrackId = "trackid123",
                OpenSpaceId = "dtv1.card//im_group.cid_example",
                ImGroupOpenSpaceModel = imGroupOpenSpaceModel,
                ImRobotOpenSpaceModel = imRobotOpenSpaceModel,
                ImGroupOpenDeliverModel = imGroupOpenDeliverModel,
                ImRobotOpenDeliverModel = imRobotOpenDeliverModel,
                ProtocolVersion = "1.0",
                FlowStatus = "PROCESSING",
                A2uiMessages = new List<string>
                {
                    "a2uiMessages"
                },
                A2uiAnnotations = new List<AlibabaCloud.SDK.Dingtalkcard_1_0.Models.CreateAndDeliverAICardRequest.CreateAndDeliverAICardRequestA2uiAnnotations>
                {
                    a2uiAnnotations0
                },
                Summary = "测试",
                CallbackType = "STREAM",
                CallbackRouteKey = "6522xxxx9784",
                BizContext = bizContext,
                CardAtUserIds = new List<string>
                {
                    "123"
                },
                AtAll = false,
            };
            try
            {
                client.CreateAndDeliverAICardWithOptions(createAndDeliverAICardRequest, createAndDeliverAICardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 成功 |
| result | Object | 返回结果。 |
| outTrackId | String | 业务卡片标识 |
| deliverResults | Array | 逐场域投递结果。  **[!NOTE]**  顶层 `success=true` 不代表每个场域都投递成功。 |
| spaceType | String | 场域类型，目标为`IM_GROUP` 或 `IM_ROBOT`。 |
| spaceId | String | 场域 ID。 |
| success | Boolean | 该场域是否投递成功。 |
| carrierId | String | 投递结果标识（opaque ID）。  **[!NOTE]**  不是 `cardInstanceId`。 |
| errorMsg | String | 场域投递错误信息。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "outTrackId" : "a2ui_order_001",
    "deliverResults" : [ {
      "spaceType" : "IM_GROUP",
      "spaceId" : "space123",
      "success" : true,
      "carrierId" : "opaque 12",
      "errorMsg" : "投放错误"
    } ]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | param.empty | 入参为空 |
| 400 | param.cardIdentityInvalid | param.cardIdentityInvalid | 卡片业务标识格式非法 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识 outTrackId 为空 |
| 400 | param.outTrackIdTooLong | param.outTrackIdTooLong | 业务标识编码后超长 |
| 400 | param.tokenGrantTypeInvalid | param.tokenGrantTypeInvalid | 系统身份参数 tokenGrantType 为空或非法 |
| 400 | param.orgIdEmpty | param.orgIdEmpty | 系统身份参数 orgId 为空 |
| 400 | param.suiteKeyEmpty | param.suiteKeyEmpty | ISV 系统身份参数 suiteKey 为空 |
| 400 | param.openSpaceIdEmpty | param.openSpaceIdEmpty | 投递 openSpaceId 为空 |
| 400 | param.openDeliverModelEmpty | param.openDeliverModelEmpty | 投递模型为空 |
| 400 | param.openDeliverModelError | param.openDeliverModelError | 转换后的投递模型为空 |
| 400 | param.openSpaceIdInvalid | param.openSpaceIdInvalid | openSpaceId 不符合规范 |
| 400 | param.openSpaceModelInvalid | param.openSpaceModelInvalid | 场域属性模型非法 |
| 400 | param.userIdNotExist | param.userIdNotExist | 用户不存在或无法映射 |
| 400 | param.invalid | param.invalid | 存在非法参数 |
| 400 | param.invalid | param.invalid | A2UI 参数或消息内容不合法，具体原因见动态 errorMsg |
| 400 | param.cardNotExist | param.cardNotExist | A2UI 卡片不存在 |
| 400 | param.idempotencyConflict | param.idempotencyConflict | A2UI 幂等标识对应的请求内容冲突 |
| 403 | access.denied | access.denied | A2UI 卡片操作无权限 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.featureDisabled | system.featureDisabled | A2UI 功能暂未开启 |
| 500 | system.dependencyUnavailable | system.dependencyUnavailable | A2UI 下游依赖不可用 |
| 500 | system.resultUnknown | system.resultUnknown | A2UI 处理结果未知，请核实投递结果后再决定是否重试 |
| 500 | system.operationInProgress | system.operationInProgress | A2UI 操作处理中 |
