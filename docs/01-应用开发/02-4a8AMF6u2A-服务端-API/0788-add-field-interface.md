---
title: "新增或者更新卡片的场域信息"
source_url: "https://open.dingtalk.com/document/development/add-field-interface"
namespace: "development"
slug: "add-field-interface"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "即时通信 > 互动卡片 > 新增或者更新卡片的场域信息"
doc_id: "lFCU7AkePM"
updated_at: "2026-06-04 19:12:23"
---

> Source: https://open.dingtalk.com/document/development/add-field-interface
> Path: 应用开发 / 服务端 API / 即时通信 > 互动卡片 > 新增或者更新卡片的场域信息
> Updated: 2026-06-04 19:12:23

# 新增或者更新卡片的场域信息

调用本接口新增或者更新卡片实例的场域信息。

## **接口调用说明**

目前卡片支持以下场域：IM群聊、IM机器人、吊顶、协作。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/instances/spaces |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Instance.Write-互动卡片实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 外部卡片实例Id。      由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。 |
| imGroupOpenSpaceModel | Object | 否 | IM群聊场域信息。 |
| supportForward | Boolean | 否 | 是否支持转发：   - **true**：支持 - **false**：不支持       若使用`imGroupOpenSpaceModel`对象，则该字段必填。 |
| lastMessageI18n | Map<String, String> | 否 | 支持国际化的LastMessage，目前支持的语言枚举值：   - **ZH\_CN**：简体中文 - **ZH\_TW**：繁体中文: - **EN\_US**：英文 - **JA\_JP**：日语 - **VI\_VN**：越南语       key为语言枚举值，value为lastMessage内容。    示例：   ``` {"ZH_CN":"卡片", "EN_US" : "card"} ``` |
| searchSupport | Object | 否 | 支持卡片消息可被搜索字段。 |
| searchIcon | String | 否 | 类型的icon，供搜索展示使用。 |
| searchTypeName | String | 否 | 卡片类型名。 |
| searchDesc | String | 否 | 供消息展示与搜索的字段。      最大限制200个字符，超过存储截断200。 |
| notification | Object | 否 | 通知信息。 |
| alertContent | String | 否 | 通知内容。      若不填写则使用默认文案：如你收到1条新消息 |
| notificationOff | Boolean | 否 | 是否关闭推送通知：   - **true**：关闭 - **false**：不关闭       默认为false。 |
| imRobotOpenSpaceModel | Object | 否 | 机器人单聊场域参数。 |
| supportForward | Boolean | 否 | 是否支持转发：   - **true**：转发 - **false**：不转发       若使用`imRobotOpenSpaceModel`对象，则该字段必填。 |
| lastMessageI18n | Map<String, String> | 否 | 支持国际化的LastMessage，目前支持的语言枚举值：   - **ZH\_CN**：简体中文 - **ZH\_TW**：繁体中文: - **EN\_US**：英文 - **JA\_JP**：日语 - **VI\_VN**：越南语       key为语言枚举值，value为lastMessage内容。    示例：   ``` {"ZH_CN":"卡片", "EN_US" : "card"} ``` |
| searchSupport | Object | 否 | 支持卡片消息可被搜索字段。 |
| searchIcon | String | 否 | 类型的icon，供搜索展示使用。 |
| searchTypeName | String | 否 | 卡片类型名。 |
| searchDesc | String | 否 | 卡片的具体描述。 |
| notification | Object | 否 | 通知信息。 |
| alertContent | String | 否 | 通知内容。      若不填写则使用默认文案：如你收到1条新消息。 |
| notificationOff | Boolean | 否 | 是否关闭推送通知：   - **true**：关闭 - **false**：不关闭       默认为 false |
| topOpenSpaceModel | Object | 否 | 吊顶场域信息。 |
| spaceType | String | 否 | 吊顶场域属性，通过增加spaeType使卡片支持吊顶场域。       - 吊顶对应spaceType为**ONE\_BOX**。 - 若使用`topOpenSpaceModel`对象，则该字段必填。 |
| coFeedOpenSpaceModel | Object | 否 | 协作场域信息（废弃）。 |
| title | String | 否 | 卡片标题（废弃）。      若使用`coFeedOpenSpaceModel`对象，则该字段必填。 |

### 请求示例

HTTP

```
PUT /v1.0/card/instances/spaces HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token-xxx
Content-Type:application/json

{
  "outTrackId" : "example_out_track_id",
  "imGroupOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
      "key" : "卡片消息"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了一个卡片消息",
      "notificationOff" : false
    }
  },
  "imRobotOpenSpaceModel" : {
    "supportForward" : false,
    "lastMessageI18n" : {
      "key" : "卡片"
    },
    "searchSupport" : {
      "searchIcon" : "@lALPDgQ9q8hFhlHNAXzNAqI",
      "searchTypeName" : "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
      "searchDesc" : "卡片的具体描述"
    },
    "notification" : {
      "alertContent" : "你收到了一个卡片消息",
      "notificationOff" : false
    }
  },
  "topOpenSpaceModel" : {
    "spaceType" : "ONE_BOX"
  },
  "coFeedOpenSpaceModel" : {
    "title" : "xxxx卡片"
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
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcard_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcard_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcard_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceHeaders appendSpaceHeaders = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceHeaders();
        appendSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestCoFeedOpenSpaceModel coFeedOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestCoFeedOpenSpaceModel()
                .setTitle("xxxx卡片");
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestTopOpenSpaceModel topOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestTopOpenSpaceModel()
                .setSpaceType("ONE_BOX");
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModelNotification()
                .setAlertContent("你收到了一个卡片消息")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport()
                .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
                .setSearchTypeName("{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}")
                .setSearchDesc("卡片的具体描述");
        java.util.Map<String, String> imRobotOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "卡片")
        );
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel()
                .setSupportForward(false)
                .setLastMessageI18n(imRobotOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imRobotOpenSpaceModelSearchSupport)
                .setNotification(imRobotOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModelNotification()
                .setAlertContent("你收到了一个卡片消息")
                .setNotificationOff(false);
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport()
                .setSearchIcon("@lALPDgQ9q8hFhlHNAXzNAqI")
                .setSearchTypeName("{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}")
                .setSearchDesc("卡片的具体描述");
        java.util.Map<String, String> imGroupOpenSpaceModelLastMessageI18n = TeaConverter.buildMap(
            new TeaPair("key", "卡片消息")
        );
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel()
                .setSupportForward(false)
                .setLastMessageI18n(imGroupOpenSpaceModelLastMessageI18n)
                .setSearchSupport(imGroupOpenSpaceModelSearchSupport)
                .setNotification(imGroupOpenSpaceModelNotification);
        com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest appendSpaceRequest = new com.aliyun.dingtalkcard_1_0.models.AppendSpaceRequest()
                .setOutTrackId("example_out_track_id")
                .setImGroupOpenSpaceModel(imGroupOpenSpaceModel)
                .setImRobotOpenSpaceModel(imRobotOpenSpaceModel)
                .setTopOpenSpaceModel(topOpenSpaceModel)
                .setCoFeedOpenSpaceModel(coFeedOpenSpaceModel);
        try {
            client.appendSpaceWithOptions(appendSpaceRequest, appendSpaceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        append_space_headers = dingtalkcard__1__0_models.AppendSpaceHeaders()
        append_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        co_feed_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestCoFeedOpenSpaceModel(
            title='xxxx卡片'
        )
        top_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestTopOpenSpaceModel(
            space_type='ONE_BOX'
        )
        im_robot_open_space_model_notification = dingtalkcard__1__0_models.AppendSpaceRequestImRobotOpenSpaceModelNotification(
            alert_content='你收到了一个卡片消息',
            notification_off=False
        )
        im_robot_open_space_model_search_support = dingtalkcard__1__0_models.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"zh_CN":"待办","zh_TW":"待辦","en_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_robot_open_space_model_last_message_i18n = {
            'key': '卡片'
        }
        im_robot_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestImRobotOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_robot_open_space_model_last_message_i18n,
            search_support=im_robot_open_space_model_search_support,
            notification=im_robot_open_space_model_notification
        )
        im_group_open_space_model_notification = dingtalkcard__1__0_models.AppendSpaceRequestImGroupOpenSpaceModelNotification(
            alert_content='你收到了一个卡片消息',
            notification_off=False
        )
        im_group_open_space_model_search_support = dingtalkcard__1__0_models.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"zh_CN":"待办","zh_TW":"待辦","en_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_group_open_space_model_last_message_i18n = {
            'key': '卡片消息'
        }
        im_group_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestImGroupOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_group_open_space_model_last_message_i18n,
            search_support=im_group_open_space_model_search_support,
            notification=im_group_open_space_model_notification
        )
        append_space_request = dingtalkcard__1__0_models.AppendSpaceRequest(
            out_track_id='example_out_track_id',
            im_group_open_space_model=im_group_open_space_model,
            im_robot_open_space_model=im_robot_open_space_model,
            top_open_space_model=top_open_space_model,
            co_feed_open_space_model=co_feed_open_space_model
        )
        try:
            client.append_space_with_options(append_space_request, append_space_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        append_space_headers = dingtalkcard__1__0_models.AppendSpaceHeaders()
        append_space_headers.x_acs_dingtalk_access_token = '<your access token>'
        co_feed_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestCoFeedOpenSpaceModel(
            title='xxxx卡片'
        )
        top_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestTopOpenSpaceModel(
            space_type='ONE_BOX'
        )
        im_robot_open_space_model_notification = dingtalkcard__1__0_models.AppendSpaceRequestImRobotOpenSpaceModelNotification(
            alert_content='你收到了一个卡片消息',
            notification_off=False
        )
        im_robot_open_space_model_search_support = dingtalkcard__1__0_models.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"zh_CN":"待办","zh_TW":"待辦","en_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_robot_open_space_model_last_message_i18n = {
            'key': '卡片'
        }
        im_robot_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestImRobotOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_robot_open_space_model_last_message_i18n,
            search_support=im_robot_open_space_model_search_support,
            notification=im_robot_open_space_model_notification
        )
        im_group_open_space_model_notification = dingtalkcard__1__0_models.AppendSpaceRequestImGroupOpenSpaceModelNotification(
            alert_content='你收到了一个卡片消息',
            notification_off=False
        )
        im_group_open_space_model_search_support = dingtalkcard__1__0_models.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport(
            search_icon='@lALPDgQ9q8hFhlHNAXzNAqI',
            search_type_name='{"zh_CN":"待办","zh_TW":"待辦","en_US":"ToDo"}',
            search_desc='卡片的具体描述'
        )
        im_group_open_space_model_last_message_i18n = {
            'key': '卡片消息'
        }
        im_group_open_space_model = dingtalkcard__1__0_models.AppendSpaceRequestImGroupOpenSpaceModel(
            support_forward=False,
            last_message_i18n=im_group_open_space_model_last_message_i18n,
            search_support=im_group_open_space_model_search_support,
            notification=im_group_open_space_model_notification
        )
        append_space_request = dingtalkcard__1__0_models.AppendSpaceRequest(
            out_track_id='example_out_track_id',
            im_group_open_space_model=im_group_open_space_model,
            im_robot_open_space_model=im_robot_open_space_model,
            top_open_space_model=top_open_space_model,
            co_feed_open_space_model=co_feed_open_space_model
        )
        try:
            await client.append_space_with_options_async(append_space_request, append_space_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\coFeedOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\topOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\imRobotOpenSpaceModel\notification;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\imRobotOpenSpaceModel\searchSupport;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\imRobotOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\imGroupOpenSpaceModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest;
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
        $appendSpaceHeaders = new AppendSpaceHeaders([]);
        $appendSpaceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $coFeedOpenSpaceModel = new coFeedOpenSpaceModel([
            "title" => "xxxx卡片"
        ]);
        $topOpenSpaceModel = new topOpenSpaceModel([
            "spaceType" => "ONE_BOX"
        ]);
        $imRobotOpenSpaceModelNotification = new notification([
            "alertContent" => "你收到了一个卡片消息",
            "notificationOff" => false
        ]);
        $imRobotOpenSpaceModelSearchSupport = new searchSupport([
            "searchIcon" => "@lALPDgQ9q8hFhlHNAXzNAqI",
            "searchTypeName" => "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
            "searchDesc" => "卡片的具体描述"
        ]);
        $imRobotOpenSpaceModelLastMessageI18n = [
            "key" => "卡片"
        ];
        $imRobotOpenSpaceModel = new imRobotOpenSpaceModel([
            "supportForward" => false,
            "lastMessageI18n" => $imRobotOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imRobotOpenSpaceModelSearchSupport,
            "notification" => $imRobotOpenSpaceModelNotification
        ]);
        $imGroupOpenSpaceModelNotification = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\imGroupOpenSpaceModel\notification([
            "alertContent" => "你收到了一个卡片消息",
            "notificationOff" => false
        ]);
        $imGroupOpenSpaceModelSearchSupport = new \AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\AppendSpaceRequest\imGroupOpenSpaceModel\searchSupport([
            "searchIcon" => "@lALPDgQ9q8hFhlHNAXzNAqI",
            "searchTypeName" => "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
            "searchDesc" => "卡片的具体描述"
        ]);
        $imGroupOpenSpaceModelLastMessageI18n = [
            "key" => "卡片消息"
        ];
        $imGroupOpenSpaceModel = new imGroupOpenSpaceModel([
            "supportForward" => false,
            "lastMessageI18n" => $imGroupOpenSpaceModelLastMessageI18n,
            "searchSupport" => $imGroupOpenSpaceModelSearchSupport,
            "notification" => $imGroupOpenSpaceModelNotification
        ]);
        $appendSpaceRequest = new AppendSpaceRequest([
            "outTrackId" => "example_out_track_id",
            "imGroupOpenSpaceModel" => $imGroupOpenSpaceModel,
            "imRobotOpenSpaceModel" => $imRobotOpenSpaceModel,
            "topOpenSpaceModel" => $topOpenSpaceModel,
            "coFeedOpenSpaceModel" => $coFeedOpenSpaceModel
        ]);
        try {
            $client->appendSpaceWithOptions($appendSpaceRequest, $appendSpaceHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/v2/service"
  dingtalkcard_1_0  "github.com/alibabacloud-go/dingtalk/card_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  appendSpaceHeaders := &dingtalkcard_1_0.AppendSpaceHeaders{}
  appendSpaceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  coFeedOpenSpaceModel := &dingtalkcard_1_0.AppendSpaceRequestCoFeedOpenSpaceModel{
    Title: tea.String("xxxx卡片"),
  }
  topOpenSpaceModel := &dingtalkcard_1_0.AppendSpaceRequestTopOpenSpaceModel{
    SpaceType: tea.String("ONE_BOX"),
  }
  imRobotOpenSpaceModelNotification := &dingtalkcard_1_0.AppendSpaceRequestImRobotOpenSpaceModelNotification{
    AlertContent: tea.String("你收到了一个卡片消息"),
    NotificationOff: tea.Bool(false),
  }
  imRobotOpenSpaceModelSearchSupport := &dingtalkcard_1_0.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("@lALPDgQ9q8hFhlHNAXzNAqI"),
    SearchTypeName: tea.String("{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}"),
    SearchDesc: tea.String("卡片的具体描述"),
  }
  imRobotOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("卡片"),
  }
  imRobotOpenSpaceModel := &dingtalkcard_1_0.AppendSpaceRequestImRobotOpenSpaceModel{
    SupportForward: tea.Bool(false),
    LastMessageI18n: imRobotOpenSpaceModelLastMessageI18n,
    SearchSupport: imRobotOpenSpaceModelSearchSupport,
    Notification: imRobotOpenSpaceModelNotification,
  }
  imGroupOpenSpaceModelNotification := &dingtalkcard_1_0.AppendSpaceRequestImGroupOpenSpaceModelNotification{
    AlertContent: tea.String("你收到了一个卡片消息"),
    NotificationOff: tea.Bool(false),
  }
  imGroupOpenSpaceModelSearchSupport := &dingtalkcard_1_0.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport{
    SearchIcon: tea.String("@lALPDgQ9q8hFhlHNAXzNAqI"),
    SearchTypeName: tea.String("{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}"),
    SearchDesc: tea.String("卡片的具体描述"),
  }
  imGroupOpenSpaceModelLastMessageI18n := map[string]*string{
    "key": tea.String("卡片消息"),
  }
  imGroupOpenSpaceModel := &dingtalkcard_1_0.AppendSpaceRequestImGroupOpenSpaceModel{
    SupportForward: tea.Bool(false),
    LastMessageI18n: imGroupOpenSpaceModelLastMessageI18n,
    SearchSupport: imGroupOpenSpaceModelSearchSupport,
    Notification: imGroupOpenSpaceModelNotification,
  }
  appendSpaceRequest := &dingtalkcard_1_0.AppendSpaceRequest{
    OutTrackId: tea.String("example_out_track_id"),
    ImGroupOpenSpaceModel: imGroupOpenSpaceModel,
    ImRobotOpenSpaceModel: imRobotOpenSpaceModel,
    TopOpenSpaceModel: topOpenSpaceModel,
    CoFeedOpenSpaceModel: coFeedOpenSpaceModel,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.AppendSpaceWithOptions(appendSpaceRequest, appendSpaceHeaders, &util.RuntimeOptions{})
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
import dingtalkcard_1_0, * as $dingtalkcard_1_0 from '@alicloud/dingtalk/card_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcard_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcard_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let appendSpaceHeaders = new $dingtalkcard_1_0.AppendSpaceHeaders({ });
    appendSpaceHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let coFeedOpenSpaceModel = new $dingtalkcard_1_0.AppendSpaceRequestCoFeedOpenSpaceModel({
      title: "xxxx卡片",
    });
    let topOpenSpaceModel = new $dingtalkcard_1_0.AppendSpaceRequestTopOpenSpaceModel({
      spaceType: "ONE_BOX",
    });
    let imRobotOpenSpaceModelNotification = new $dingtalkcard_1_0.AppendSpaceRequestImRobotOpenSpaceModelNotification({
      alertContent: "你收到了一个卡片消息",
      notificationOff: false,
    });
    let imRobotOpenSpaceModelSearchSupport = new $dingtalkcard_1_0.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport({
      searchIcon: "@lALPDgQ9q8hFhlHNAXzNAqI",
      searchTypeName: "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
      searchDesc: "卡片的具体描述",
    });
    let imRobotOpenSpaceModelLastMessageI18n = {
      key: "卡片",
    };
    let imRobotOpenSpaceModel = new $dingtalkcard_1_0.AppendSpaceRequestImRobotOpenSpaceModel({
      supportForward: false,
      lastMessageI18n: imRobotOpenSpaceModelLastMessageI18n,
      searchSupport: imRobotOpenSpaceModelSearchSupport,
      notification: imRobotOpenSpaceModelNotification,
    });
    let imGroupOpenSpaceModelNotification = new $dingtalkcard_1_0.AppendSpaceRequestImGroupOpenSpaceModelNotification({
      alertContent: "你收到了一个卡片消息",
      notificationOff: false,
    });
    let imGroupOpenSpaceModelSearchSupport = new $dingtalkcard_1_0.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport({
      searchIcon: "@lALPDgQ9q8hFhlHNAXzNAqI",
      searchTypeName: "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
      searchDesc: "卡片的具体描述",
    });
    let imGroupOpenSpaceModelLastMessageI18n = {
      key: "卡片消息",
    };
    let imGroupOpenSpaceModel = new $dingtalkcard_1_0.AppendSpaceRequestImGroupOpenSpaceModel({
      supportForward: false,
      lastMessageI18n: imGroupOpenSpaceModelLastMessageI18n,
      searchSupport: imGroupOpenSpaceModelSearchSupport,
      notification: imGroupOpenSpaceModelNotification,
    });
    let appendSpaceRequest = new $dingtalkcard_1_0.AppendSpaceRequest({
      outTrackId: "example_out_track_id",
      imGroupOpenSpaceModel: imGroupOpenSpaceModel,
      imRobotOpenSpaceModel: imRobotOpenSpaceModel,
      topOpenSpaceModel: topOpenSpaceModel,
      coFeedOpenSpaceModel: coFeedOpenSpaceModel,
    });
    try {
      await client.appendSpaceWithOptions(appendSpaceRequest, appendSpaceHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceHeaders appendSpaceHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceHeaders();
            appendSpaceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestCoFeedOpenSpaceModel coFeedOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestCoFeedOpenSpaceModel
            {
                Title = "xxxx卡片",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestTopOpenSpaceModel topOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestTopOpenSpaceModel
            {
                SpaceType = "ONE_BOX",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel.AppendSpaceRequestImRobotOpenSpaceModelNotification imRobotOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel.AppendSpaceRequestImRobotOpenSpaceModelNotification
            {
                AlertContent = "你收到了一个卡片消息",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport imRobotOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel.AppendSpaceRequestImRobotOpenSpaceModelSearchSupport
            {
                SearchIcon = "@lALPDgQ9q8hFhlHNAXzNAqI",
                SearchTypeName = "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
                SearchDesc = "卡片的具体描述",
            };
            Dictionary<string, string> imRobotOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "卡片"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel imRobotOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImRobotOpenSpaceModel
            {
                SupportForward = false,
                LastMessageI18n = imRobotOpenSpaceModelLastMessageI18n,
                SearchSupport = imRobotOpenSpaceModelSearchSupport,
                Notification = imRobotOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel.AppendSpaceRequestImGroupOpenSpaceModelNotification imGroupOpenSpaceModelNotification = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel.AppendSpaceRequestImGroupOpenSpaceModelNotification
            {
                AlertContent = "你收到了一个卡片消息",
                NotificationOff = false,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport imGroupOpenSpaceModelSearchSupport = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel.AppendSpaceRequestImGroupOpenSpaceModelSearchSupport
            {
                SearchIcon = "@lALPDgQ9q8hFhlHNAXzNAqI",
                SearchTypeName = "{\"zh_CN\":\"待办\",\"zh_TW\":\"待辦\",\"en_US\":\"ToDo\"}",
                SearchDesc = "卡片的具体描���",
            };
            Dictionary<string, string> imGroupOpenSpaceModelLastMessageI18n = new Dictionary<string, string>
            {
                {"key", "卡片消息"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel imGroupOpenSpaceModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest.AppendSpaceRequestImGroupOpenSpaceModel
            {
                SupportForward = false,
                LastMessageI18n = imGroupOpenSpaceModelLastMessageI18n,
                SearchSupport = imGroupOpenSpaceModelSearchSupport,
                Notification = imGroupOpenSpaceModelNotification,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest appendSpaceRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.AppendSpaceRequest
            {
                OutTrackId = "example_out_track_id",
                ImGroupOpenSpaceModel = imGroupOpenSpaceModel,
                ImRobotOpenSpaceModel = imRobotOpenSpaceModel,
                TopOpenSpaceModel = topOpenSpaceModel,
                CoFeedOpenSpaceModel = coFeedOpenSpaceModel,
            };
            try
            {
                client.AppendSpaceWithOptions(appendSpaceRequest, appendSpaceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 调用是否成功。 |
| result | Boolean | 新增场域或更新场域是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | param.empty | 入参为空 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识outTrackId为空 |
| 400 | param.emptyAppendSpaces | param.emptyAppendSpaces | appendSpaces为空 |
| 400 | param.openSpaceModelInvalid | param.openSpaceModelInvalid | 错误的场域属性模型 |
| 400 | param.cardNotExist | param.cardNotExist | 卡片不存在 |
