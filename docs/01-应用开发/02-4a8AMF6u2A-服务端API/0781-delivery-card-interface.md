---
title: "投放卡片"
source_url: "https://open.dingtalk.com/document/development/delivery-card-interface"
namespace: "development"
slug: "delivery-card-interface"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 互动卡片 > 投放卡片"
doc_id: "2LFDy1k75G"
updated_at: "2026-06-04 19:12:21"
---

> Source: https://open.dingtalk.com/document/development/delivery-card-interface
> Path: 应用开发 / 服务端API / 即时通信 > 互动卡片 > 投放卡片
> Updated: 2026-06-04 19:12:21

# 投放卡片

调用本接口实现多个指定场域的卡片投放。

## **接口调用说明**

在将卡片投放到不同的场域时，使用`outTrackId`唯一标识一张卡片，通过`openSpaceId`标识需要被投放的场域及其场域Id，通过`openDeliverModels`传入不同场域下的投放属性。

> **[!NOTE]**
>
> - 目前支持将卡片投放至以下场域：IM群聊、IM单聊酷应用、IM机器人单聊、吊顶、协作、文档。
> - 若需要被投放的卡片实例不支持该场域，需要先调用appendSpace接口增加该场域（将卡片投放至文档不需要）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/card/instances/deliver |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Card.Instance.Write-互动卡片实例写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| outTrackId | String | 是 | 外部卡片实例Id。     - 由开发者自己生成并作为入参传递给钉钉的，钉钉只在对应使用到outTrackId的场景，帮助开发者对TrackId进行记录。 - 一个 outTrackId 唯一标识一张卡片。 |
| openSpaceId | String | 是 | 表示场域及其场域id，其格式为`dtv1.card//spaceType1.spaceId1;spaceType2.spaceId2_1;spaceType2.spaceId2_2;spaceType3.spaceId3`。 |
| imSingleOpenDeliverModel | Object | 否 | 单聊场域投放参数。 |
| atUserIds | Map<String, String> | 否 | 消息@人。格式：{"key":"value"}。   - key：用户的userId - value：用户名。     如果key、value都为"@ALL"则判断@所有人。  示例：   ``` "atUserIds" : {     "123456" : "小明" } ``` |
| extension | Map<String, String> | 否 | 扩展字段，示例如下：   ``` {"key":"value"} ``` |
| imRobotOpenDeliverModel | Object | 否 | IM机器人单聊投放参数。    机器人与人的单聊，直接用支持机器人单聊的应用来发送。 |
| spaceType | String | 否 | IM机器人单聊若未设置其他投放属性，需设置spaeType为`IM_ROBOT`。 |
| extension | Map<String, String> | 否 | 扩展字段，示例如下：   ``` {"key":"value"} ``` |
| robotCode | String | 否 | 机器人编码。 |
| imGroupOpenDeliverModel | Object | 否 | 群聊投放参数。 |
| robotCode | String | 否 | 用于发送卡片的机器人编码。   - 场景群机器人发送群聊使用群机器人robotCode - 非场景群的企业内部开发的机器人发送群聊，使用机器人的AppKey - 第三方企业机器人，使用机器人的robotCode     若使用`imGroupOpenDeliverModel`对象，则该字段必填。 |
| atUserIds | Map<String, String> | 否 | 消息@人。格式：{"key":"value"}。   - key：用户的userId - value：用户名。     如果key、value都为"@ALL"则判断@所有人。  示例：   ``` "atUserIds" : {     "123456" : "小明" } ``` |
| recipients | Array of String | 否 | 指定接收者的userId。 |
| extension | Map<String, String> | 否 | 扩展字段，示例如下：   ``` {"key":"value"} ``` |
| topOpenDeliverModel | Object | 否 | 吊顶投放参数。 |
| expiredTimeMillis | Long | 否 | 过期时间戳。    若使用`topOpenDeliverModel`对象，则该字段必填。 |
| userIds | Array of String | 否 | 可以查看该吊顶卡片的userId。 |
| platforms | Array of String | 否 | 可以查看该吊顶卡片的设备，包含`android｜ios｜win｜mac`，示例：   ``` "platforms" : [     "android"，     "ios" ] ```     若为空，则所有设备可见 |
| coFeedOpenDeliverModel | Object | 否 | 协作投放参数（废弃） |
| bizTag | String | 否 | 业务标识。     - 若使用`coFeedOpenDeliverModel`对象，则该字段必填。 - 需要先申请在协作中投放该bizTag，申请通过后才能使用。 |
| gmtTimeLine | Long | 否 | 协作场域下的排序时间。    若使用`coFeedOpenDeliverModel`对象，则该字段必填。 |
| docOpenDeliverModel | Object | 否 | 文档投放参数（废弃） |
| userId | String | 否 | 员工userId信息。    若使用`docOpenDeliverModel`对象，则该字段必填。 |
| userIdType | Integer | 否 | 用户id类型：   - **1**（默认）：userId模式 - **2**：unionId模式     `userIdType` 字段的填写请参考：[userIdType 字段的填写说明](0790-faq-card.md#8cad7f90a8mzg)。 |

### 请求示例

HTTP

```
POST /v1.0/card/instances/deliver HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token-xxx
Content-Type:application/json

{
  "outTrackId" : "example_out_track_id",
  "openSpaceId" : "dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==",
  "imSingleOpenDeliverModel" : {
    "atUserIds" : {
      "key" : "example_user_name"
    },
    "extension" : {
      "key" : "example_ext_value"
    }
  },
  "imRobotOpenDeliverModel" : {
    "spaceType" : "IM_ROBOT",
    "extension" : {
      "key" : "example_ext_value"
    },
    "robotCode" : "example_robot_code"
  },
  "imGroupOpenDeliverModel" : {
    "robotCode" : "example_robot_code",
    "atUserIds" : {
      "key" : "example_user_name"
    },
    "recipients" : [ "example_user_id" ],
    "extension" : {
      "key" : "example_ext_value"
    }
  },
  "topOpenDeliverModel" : {
    "expiredTimeMillis" : 1665473229000,
    "userIds" : [ "example_user_id" ],
    "platforms" : [ "android" ]
  },
  "coFeedOpenDeliverModel" : {
    "bizTag" : "example_biz_tag",
    "gmtTimeLine" : 1665473229000
  },
  "docOpenDeliverModel" : {
    "userId" : "example_user_id"
  },
  "userIdType" : 1
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
        com.aliyun.dingtalkcard_1_0.models.DeliverCardHeaders deliverCardHeaders = new com.aliyun.dingtalkcard_1_0.models.DeliverCardHeaders();
        deliverCardHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestDocOpenDeliverModel docOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestDocOpenDeliverModel()
                .setUserId("example_user_id");
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestCoFeedOpenDeliverModel coFeedOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestCoFeedOpenDeliverModel()
                .setBizTag("example_biz_tag")
                .setGmtTimeLine(1665473229000L);
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestTopOpenDeliverModel topOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestTopOpenDeliverModel()
                .setExpiredTimeMillis(1665473229000L)
                .setUserIds(java.util.Arrays.asList(
                    "example_user_id"
                ))
                .setPlatforms(java.util.Arrays.asList(
                    "android"
                ));
        java.util.Map<String, String> imGroupOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "example_ext_value")
        );
        java.util.Map<String, String> imGroupOpenDeliverModelAtUserIds = TeaConverter.buildMap(
            new TeaPair("key", "example_user_name")
        );
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImGroupOpenDeliverModel()
                .setRobotCode("example_robot_code")
                .setAtUserIds(imGroupOpenDeliverModelAtUserIds)
                .setRecipients(java.util.Arrays.asList(
                    "example_user_id"
                ))
                .setExtension(imGroupOpenDeliverModelExtension);
        java.util.Map<String, String> imRobotOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "example_ext_value")
        );
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImRobotOpenDeliverModel imRobotOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImRobotOpenDeliverModel()
                .setSpaceType("IM_ROBOT")
                .setExtension(imRobotOpenDeliverModelExtension)
                .setRobotCode("example_robot_code");
        java.util.Map<String, String> imSingleOpenDeliverModelExtension = TeaConverter.buildMap(
            new TeaPair("key", "example_ext_value")
        );
        java.util.Map<String, String> imSingleOpenDeliverModelAtUserIds = TeaConverter.buildMap(
            new TeaPair("key", "example_user_name")
        );
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImSingleOpenDeliverModel imSingleOpenDeliverModel = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest.DeliverCardRequestImSingleOpenDeliverModel()
                .setAtUserIds(imSingleOpenDeliverModelAtUserIds)
                .setExtension(imSingleOpenDeliverModelExtension);
        com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest deliverCardRequest = new com.aliyun.dingtalkcard_1_0.models.DeliverCardRequest()
                .setOutTrackId("example_out_track_id")
                .setOpenSpaceId("dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==")
                .setImSingleOpenDeliverModel(imSingleOpenDeliverModel)
                .setImRobotOpenDeliverModel(imRobotOpenDeliverModel)
                .setImGroupOpenDeliverModel(imGroupOpenDeliverModel)
                .setTopOpenDeliverModel(topOpenDeliverModel)
                .setCoFeedOpenDeliverModel(coFeedOpenDeliverModel)
                .setDocOpenDeliverModel(docOpenDeliverModel)
                .setUserIdType(1);
        try {
            client.deliverCardWithOptions(deliverCardRequest, deliverCardHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        deliver_card_headers = dingtalkcard__1__0_models.DeliverCardHeaders()
        deliver_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestDocOpenDeliverModel(
            user_id='example_user_id'
        )
        co_feed_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestCoFeedOpenDeliverModel(
            biz_tag='example_biz_tag',
            gmt_time_line=1665473229000
        )
        top_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestTopOpenDeliverModel(
            expired_time_millis=1665473229000,
            user_ids=[
                'example_user_id'
            ],
            platforms=[
                'android'
            ]
        )
        im_group_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_group_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_group_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestImGroupOpenDeliverModel(
            robot_code='example_robot_code',
            at_user_ids=im_group_open_deliver_model_at_user_ids,
            recipients=[
                'example_user_id'
            ],
            extension=im_group_open_deliver_model_extension
        )
        im_robot_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_robot_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestImRobotOpenDeliverModel(
            space_type='IM_ROBOT',
            extension=im_robot_open_deliver_model_extension,
            robot_code='example_robot_code'
        )
        im_single_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_single_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_single_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestImSingleOpenDeliverModel(
            at_user_ids=im_single_open_deliver_model_at_user_ids,
            extension=im_single_open_deliver_model_extension
        )
        deliver_card_request = dingtalkcard__1__0_models.DeliverCardRequest(
            out_track_id='example_out_track_id',
            open_space_id='dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==',
            im_single_open_deliver_model=im_single_open_deliver_model,
            im_robot_open_deliver_model=im_robot_open_deliver_model,
            im_group_open_deliver_model=im_group_open_deliver_model,
            top_open_deliver_model=top_open_deliver_model,
            co_feed_open_deliver_model=co_feed_open_deliver_model,
            doc_open_deliver_model=doc_open_deliver_model,
            user_id_type=1
        )
        try:
            client.deliver_card_with_options(deliver_card_request, deliver_card_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        deliver_card_headers = dingtalkcard__1__0_models.DeliverCardHeaders()
        deliver_card_headers.x_acs_dingtalk_access_token = '<your access token>'
        doc_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestDocOpenDeliverModel(
            user_id='example_user_id'
        )
        co_feed_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestCoFeedOpenDeliverModel(
            biz_tag='example_biz_tag',
            gmt_time_line=1665473229000
        )
        top_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestTopOpenDeliverModel(
            expired_time_millis=1665473229000,
            user_ids=[
                'example_user_id'
            ],
            platforms=[
                'android'
            ]
        )
        im_group_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_group_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_group_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestImGroupOpenDeliverModel(
            robot_code='example_robot_code',
            at_user_ids=im_group_open_deliver_model_at_user_ids,
            recipients=[
                'example_user_id'
            ],
            extension=im_group_open_deliver_model_extension
        )
        im_robot_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_robot_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestImRobotOpenDeliverModel(
            space_type='IM_ROBOT',
            extension=im_robot_open_deliver_model_extension,
            robot_code='example_robot_code'
        )
        im_single_open_deliver_model_extension = {
            'key': 'example_ext_value'
        }
        im_single_open_deliver_model_at_user_ids = {
            'key': 'example_user_name'
        }
        im_single_open_deliver_model = dingtalkcard__1__0_models.DeliverCardRequestImSingleOpenDeliverModel(
            at_user_ids=im_single_open_deliver_model_at_user_ids,
            extension=im_single_open_deliver_model_extension
        )
        deliver_card_request = dingtalkcard__1__0_models.DeliverCardRequest(
            out_track_id='example_out_track_id',
            open_space_id='dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==',
            im_single_open_deliver_model=im_single_open_deliver_model,
            im_robot_open_deliver_model=im_robot_open_deliver_model,
            im_group_open_deliver_model=im_group_open_deliver_model,
            top_open_deliver_model=top_open_deliver_model,
            co_feed_open_deliver_model=co_feed_open_deliver_model,
            doc_open_deliver_model=doc_open_deliver_model,
            user_id_type=1
        )
        try:
            await client.deliver_card_with_options_async(deliver_card_request, deliver_card_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest\docOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest\coFeedOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest\topOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest\imGroupOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest\imRobotOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest\imSingleOpenDeliverModel;
use AlibabaCloud\SDK\Dingtalk\Vcard_1_0\Models\DeliverCardRequest;
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
        $deliverCardHeaders = new DeliverCardHeaders([]);
        $deliverCardHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $docOpenDeliverModel = new docOpenDeliverModel([
            "userId" => "example_user_id"
        ]);
        $coFeedOpenDeliverModel = new coFeedOpenDeliverModel([
            "bizTag" => "example_biz_tag",
            "gmtTimeLine" => 1665473229000
        ]);
        $topOpenDeliverModel = new topOpenDeliverModel([
            "expiredTimeMillis" => 1665473229000,
            "userIds" => [
                "example_user_id"
            ],
            "platforms" => [
                "android"
            ]
        ]);
        $imGroupOpenDeliverModelExtension = [
            "key" => "example_ext_value"
        ];
        $imGroupOpenDeliverModelAtUserIds = [
            "key" => "example_user_name"
        ];
        $imGroupOpenDeliverModel = new imGroupOpenDeliverModel([
            "robotCode" => "example_robot_code",
            "atUserIds" => $imGroupOpenDeliverModelAtUserIds,
            "recipients" => [
                "example_user_id"
            ],
            "extension" => $imGroupOpenDeliverModelExtension
        ]);
        $imRobotOpenDeliverModelExtension = [
            "key" => "example_ext_value"
        ];
        $imRobotOpenDeliverModel = new imRobotOpenDeliverModel([
            "spaceType" => "IM_ROBOT",
            "extension" => $imRobotOpenDeliverModelExtension,
            "robotCode" => "example_robot_code"
        ]);
        $imSingleOpenDeliverModelExtension = [
            "key" => "example_ext_value"
        ];
        $imSingleOpenDeliverModelAtUserIds = [
            "key" => "example_user_name"
        ];
        $imSingleOpenDeliverModel = new imSingleOpenDeliverModel([
            "atUserIds" => $imSingleOpenDeliverModelAtUserIds,
            "extension" => $imSingleOpenDeliverModelExtension
        ]);
        $deliverCardRequest = new DeliverCardRequest([
            "outTrackId" => "example_out_track_id",
            "openSpaceId" => "dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==",
            "imSingleOpenDeliverModel" => $imSingleOpenDeliverModel,
            "imRobotOpenDeliverModel" => $imRobotOpenDeliverModel,
            "imGroupOpenDeliverModel" => $imGroupOpenDeliverModel,
            "topOpenDeliverModel" => $topOpenDeliverModel,
            "coFeedOpenDeliverModel" => $coFeedOpenDeliverModel,
            "docOpenDeliverModel" => $docOpenDeliverModel,
            "userIdType" => 1
        ]);
        try {
            $client->deliverCardWithOptions($deliverCardRequest, $deliverCardHeaders, new RuntimeOptions([]));
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

  deliverCardHeaders := &dingtalkcard_1_0.DeliverCardHeaders{}
  deliverCardHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  docOpenDeliverModel := &dingtalkcard_1_0.DeliverCardRequestDocOpenDeliverModel{
    UserId: tea.String("example_user_id"),
  }
  coFeedOpenDeliverModel := &dingtalkcard_1_0.DeliverCardRequestCoFeedOpenDeliverModel{
    BizTag: tea.String("example_biz_tag"),
    GmtTimeLine: tea.Int64(1665473229000),
  }
  topOpenDeliverModel := &dingtalkcard_1_0.DeliverCardRequestTopOpenDeliverModel{
    ExpiredTimeMillis: tea.Int64(1665473229000),
    UserIds: []*string{tea.String("example_user_id")},
    Platforms: []*string{tea.String("android")},
  }
  imGroupOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("example_ext_value"),
  }
  imGroupOpenDeliverModelAtUserIds := map[string]*string{
    "key": tea.String("example_user_name"),
  }
  imGroupOpenDeliverModel := &dingtalkcard_1_0.DeliverCardRequestImGroupOpenDeliverModel{
    RobotCode: tea.String("example_robot_code"),
    AtUserIds: imGroupOpenDeliverModelAtUserIds,
    Recipients: []*string{tea.String("example_user_id")},
    Extension: imGroupOpenDeliverModelExtension,
  }
  imRobotOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("example_ext_value"),
  }
  imRobotOpenDeliverModel := &dingtalkcard_1_0.DeliverCardRequestImRobotOpenDeliverModel{
    SpaceType: tea.String("IM_ROBOT"),
    Extension: imRobotOpenDeliverModelExtension,
    RobotCode: tea.String("example_robot_code"),
  }
  imSingleOpenDeliverModelExtension := map[string]*string{
    "key": tea.String("example_ext_value"),
  }
  imSingleOpenDeliverModelAtUserIds := map[string]*string{
    "key": tea.String("example_user_name"),
  }
  imSingleOpenDeliverModel := &dingtalkcard_1_0.DeliverCardRequestImSingleOpenDeliverModel{
    AtUserIds: imSingleOpenDeliverModelAtUserIds,
    Extension: imSingleOpenDeliverModelExtension,
  }
  deliverCardRequest := &dingtalkcard_1_0.DeliverCardRequest{
    OutTrackId: tea.String("example_out_track_id"),
    OpenSpaceId: tea.String("dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ=="),
    ImSingleOpenDeliverModel: imSingleOpenDeliverModel,
    ImRobotOpenDeliverModel: imRobotOpenDeliverModel,
    ImGroupOpenDeliverModel: imGroupOpenDeliverModel,
    TopOpenDeliverModel: topOpenDeliverModel,
    CoFeedOpenDeliverModel: coFeedOpenDeliverModel,
    DocOpenDeliverModel: docOpenDeliverModel,
    UserIdType: tea.Int32(1),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeliverCardWithOptions(deliverCardRequest, deliverCardHeaders, &util.RuntimeOptions{})
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
    let deliverCardHeaders = new dingtalkcard_1_0.DeliverCardHeaders({ });
    deliverCardHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let docOpenDeliverModel = new dingtalkcard_1_0.DeliverCardRequestDocOpenDeliverModel({
      userId: 'example_user_id',
    });
    let coFeedOpenDeliverModel = new dingtalkcard_1_0.DeliverCardRequestCoFeedOpenDeliverModel({
      bizTag: 'example_biz_tag',
      gmtTimeLine: 1665473229000,
    });
    let topOpenDeliverModel = new dingtalkcard_1_0.DeliverCardRequestTopOpenDeliverModel({
      expiredTimeMillis: 1665473229000,
      userIds: [
        'example_user_id'
      ],
      platforms: [
        'android'
      ],
    });
    let imGroupOpenDeliverModelExtension = {
      key: 'example_ext_value',
    };
    let imGroupOpenDeliverModelAtUserIds = {
      key: 'example_user_name',
    };
    let imGroupOpenDeliverModel = new dingtalkcard_1_0.DeliverCardRequestImGroupOpenDeliverModel({
      robotCode: 'example_robot_code',
      atUserIds: imGroupOpenDeliverModelAtUserIds,
      recipients: [
        'example_user_id'
      ],
      extension: imGroupOpenDeliverModelExtension,
    });
    let imRobotOpenDeliverModelExtension = {
      key: 'example_ext_value',
    };
    let imRobotOpenDeliverModel = new dingtalkcard_1_0.DeliverCardRequestImRobotOpenDeliverModel({
      spaceType: 'IM_ROBOT',
      extension: imRobotOpenDeliverModelExtension,
      robotCode: 'example_robot_code',
    });
    let imSingleOpenDeliverModelExtension = {
      key: 'example_ext_value',
    };
    let imSingleOpenDeliverModelAtUserIds = {
      key: 'example_user_name',
    };
    let imSingleOpenDeliverModel = new dingtalkcard_1_0.DeliverCardRequestImSingleOpenDeliverModel({
      atUserIds: imSingleOpenDeliverModelAtUserIds,
      extension: imSingleOpenDeliverModelExtension,
    });
    let deliverCardRequest = new dingtalkcard_1_0.DeliverCardRequest({
      outTrackId: 'example_out_track_id',
      openSpaceId: 'dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==',
      imSingleOpenDeliverModel: imSingleOpenDeliverModel,
      imRobotOpenDeliverModel: imRobotOpenDeliverModel,
      imGroupOpenDeliverModel: imGroupOpenDeliverModel,
      topOpenDeliverModel: topOpenDeliverModel,
      coFeedOpenDeliverModel: coFeedOpenDeliverModel,
      docOpenDeliverModel: docOpenDeliverModel,
      userIdType: 1,
    });
    try {
      await client.deliverCardWithOptions(deliverCardRequest, deliverCardHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardHeaders deliverCardHeaders = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardHeaders();
            deliverCardHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestDocOpenDeliverModel docOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestDocOpenDeliverModel
            {
                UserId = "example_user_id",
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestCoFeedOpenDeliverModel coFeedOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestCoFeedOpenDeliverModel
            {
                BizTag = "example_biz_tag",
                GmtTimeLine = 1665473229000,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestTopOpenDeliverModel topOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestTopOpenDeliverModel
            {
                ExpiredTimeMillis = 1665473229000,
                UserIds = new List<string>
                {
                    "example_user_id"
                },
                Platforms = new List<string>
                {
                    "android"
                },
            };
            Dictionary<string, string> imGroupOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "example_ext_value"},
            };
            Dictionary<string, string> imGroupOpenDeliverModelAtUserIds = new Dictionary<string, string>
            {
                {"key", "example_user_name"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestImGroupOpenDeliverModel imGroupOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestImGroupOpenDeliverModel
            {
                RobotCode = "example_robot_code",
                AtUserIds = imGroupOpenDeliverModelAtUserIds,
                Recipients = new List<string>
                {
                    "example_user_id"
                },
                Extension = imGroupOpenDeliverModelExtension,
            };
            Dictionary<string, string> imRobotOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "example_ext_value"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestImRobotOpenDeliverModel imRobotOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestImRobotOpenDeliverModel
            {
                SpaceType = "IM_ROBOT",
                Extension = imRobotOpenDeliverModelExtension,
                RobotCode = "example_robot_code",
            };
            Dictionary<string, string> imSingleOpenDeliverModelExtension = new Dictionary<string, string>
            {
                {"key", "example_ext_value"},
            };
            Dictionary<string, string> imSingleOpenDeliverModelAtUserIds = new Dictionary<string, string>
            {
                {"key", "example_user_name"},
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestImSingleOpenDeliverModel imSingleOpenDeliverModel = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest.DeliverCardRequestImSingleOpenDeliverModel
            {
                AtUserIds = imSingleOpenDeliverModelAtUserIds,
                Extension = imSingleOpenDeliverModelExtension,
            };
            AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest deliverCardRequest = new AlibabaCloud.SDK.Dingtalkcard_1_0.Models.DeliverCardRequest
            {
                OutTrackId = "example_out_track_id",
                OpenSpaceId = "dtv1.card//im_group.cidp4Gh*******VCQ==;im_robot.manager****67;co_feed.manager****67;one_box.cidp4Gh*******VCQ==",
                ImSingleOpenDeliverModel = imSingleOpenDeliverModel,
                ImRobotOpenDeliverModel = imRobotOpenDeliverModel,
                ImGroupOpenDeliverModel = imGroupOpenDeliverModel,
                TopOpenDeliverModel = topOpenDeliverModel,
                CoFeedOpenDeliverModel = coFeedOpenDeliverModel,
                DocOpenDeliverModel = docOpenDeliverModel,
                UserIdType = 1,
            };
            try
            {
                client.DeliverCardWithOptions(deliverCardRequest, deliverCardHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 调用结果。 |
| result | Array | 投放结果列表。 |
| spaceType | String | 场域类型 ：   - **IM**: IM - **IM\_GROUP**: IM群聊 - **IM\_ROBOT**: IM机器人单聊 - **ONE\_BOX**: 群吊顶 - **COOPERATION\_FEED**: 协作 |
| spaceId | String | 场域Id。 |
| success | Boolean | 投放成功。 |
| carrierId | String | 投放结果id。    IM场域返processQueryKey，用于业务后续查看消息已读列表，其他场域暂不返回。 |
| errorMsg | String | 场域投放错误信息。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : [ {
    "spaceType" : "IM_GROUP",
    "spaceId" : "cid1234abcd",
    "success" : true,
    "carrierId" : "4v+AzUEDuC0dKuO*********J0w8=",
    "errorMsg" : "system error"
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.empty | param.empty | 入参为空 |
| 400 | param.outTrackIdEmpty | param.outTrackIdEmpty | 业务标识outTrackId为空 |
| 400 | param.openSpaceIdEmpty | param.openSpaceIdEmpty | 投放openSpaceId为空 |
| 400 | param.openDeliverModelEmpty | param.openDeliverModelEmpty | 场域投放模型为空 |
| 400 | param.spaceDeliverModelEmpty | param.spaceDeliverModelError | 场域投放模型格式错误 |
| 400 | param.openSpaceIdInvalid | param.openSpaceIdInvalid | openSpaceId不符合规范 |
| 400 | param.cardNotExist | param.cardNotExist | 卡片不存在 |
| 500 | system.busy | system.busy | 系统繁忙 |
| 500 | system.busy | system.busy | 系统繁忙 |
