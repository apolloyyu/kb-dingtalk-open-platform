---
title: "创建并开启互动卡片吊顶"
source_url: "https://open.dingtalk.com/document/development/send-group-helper-message"
namespace: "development"
slug: "send-group-helper-message"
group: "应用开发"
tab: "服务端API"
breadcrumb: "即时通信 > 会话管理 > 场景群 > 群吊顶 > 创建并开启互动卡片吊顶"
doc_id: "cLFXx5OSvx"
updated_at: "2026-07-14 09:29:43"
---

> Source: https://open.dingtalk.com/document/development/send-group-helper-message
> Path: 应用开发 / 服务端API / 即时通信 > 会话管理 > 场景群 > 群吊顶 > 创建并开启互动卡片吊顶
> Updated: 2026-07-14 09:29:43

# 创建并开启互动卡片吊顶

调用本接口，创建并开启会话中的互动卡片吊顶。

## **接口调用说明**

- 对于群聊会话类型，支持以下场景使用：

  - 基于群模板创建的群，详情参见[创建场景群](0746-create-a-scene-group.md)。
  - 安装群聊酷应用的群，详情参见[酷应用](../01-XOnnmGCTbn-开发指南/0042-coolapp-overview.md)。
- 对于单聊助手会话类型，支持以下场景：

  此接口只适用于已经建立会话的单聊助手，即第一次开启吊顶前，需要先使用机器人给用户发送单聊消息，以建立单聊助手会话。

  调用[创建并投放卡片](0783-create-and-deliver-cards.md)接口或[批量发送人与机器人会话中机器人消息](0714-chatbots-send-one-on-one-chat-messages-in-batches.md)接口。
- 单个会话中最多可开启10个吊顶。若会话内已经存在10个未关闭的吊顶，需要关闭已开启的吊顶，然后再开启新的吊顶。
- 接口调用方需要自己记录每个会话内的互动卡片吊顶的相关信息（比如：outTrackId，openConversationId，userId，unionId，robotCode等信息），以便于管理会话中的互动卡片吊顶。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v2.0/im/topBoxes |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_chat\_manage-钉钉群基础信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cardTemplateId | String | 是 | 互动卡片的消息模板ID，调用[创建并投放卡片](0783-create-and-deliver-cards.md)接口获取模板ID。 |
| outTrackId | String | 是 | 一张卡片的外部ID，最大长度64，与[创建卡片](0780-interface-for-creating-a-card-instance.md)/[创建并投放卡片](0783-create-and-deliver-cards.md)中的 outTrackId 保持一致。也可在对应模板的**卡片实例管理**中获取：  image     - 需保存`outTrackId`，否则无法进行关闭互动卡片吊顶。 - 一般情况下，若使用了新的 cardTemplateId 或 cardData 等参数，则需要重新生成全新的 outTrackId，否则更改不会生效。 |
| callbackRouteKey | String | 否 | 可控制卡片回调时的路由Key，用于指定特定的callbackUrl，调用[注册卡片回调地址](0786-register-card-callback-address.md)接口获取参数`callbackRouteKey`。 |
| cardData | Object | 是 | 卡片数据。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - **普通文本类型**：key为变量名，value为文本内容。 - **多媒体类型**：key为变量名，value为媒体文件：调用[上传媒体文件](0646-upload-media-files.md)接口的获取`media_id`参数值。      - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)文档中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| userIdPrivateDataMap | Map<String, Object> | 否 | 卡片模板userId差异用户参数。   - **key**：用户userId。 - **value**：卡片数据。 |
|  | Object | 否 | 卡片数据。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - **普通文本类型**：key为变量名，value为文本内容。 - **多媒体类型**：key为变量名，value为媒体文件：调用[上传媒体文件](0646-upload-media-files.md)接口的获取`media_id`参数值。      - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)文档中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| unionIdPrivateDataMap | Map<String, Object> | 否 | 卡片模板unionId差异用户参数。   - **key**：用户unionId。 - **value**：卡片数据。 |
|  | Object | 否 | 卡片数据。 |
| cardParamMap | Map<String, String> | 否 | 卡片模板内容替换参数：   - **普通文本类型**：key为变量名，value为文本内容。 - **多媒体类型**：key为变量名，value为媒体文件：调用[上传媒体文件](0646-upload-media-files.md)接口的获取`media_id`参数值。      - 属性字段只支持 String 类型，非 String 类型的属性填写请参考文档：[常见问题](0790-faq-card.md)文档中“设置卡片数据时，如何处理非 String 类型的参数”小节。 - 务必确保属性值的类型与卡片搭建器中所配置的变量类型相匹配，否则可能出现属性不生效，或者在移动端无法显示等问题。 |
| cardSettings | Object | 否 | 卡片设置项。 |
| pullStrategy | Boolean | 否 | 是否开启卡片纯拉模式：参见[纯拉模式流程指南](0736-pure-pull-mode-process-guide.md)。   - **true**：开启 - **false**：关闭 |
| conversationType | Integer | 是 | 会话类型：   - **1**：群聊 - **2**：单聊助手 |
| openConversationId | String | 否 | 会话id：   - **群聊**（此参数必传）：    - 基于群模板创建的群，调用[创建场景群](0746-create-a-scene-group.md)接口获取`open_conversation_id`参数值。   - 安装群聊酷应用的群，通过[感知群变化（事件订阅）](../01-XOnnmGCTbn-开发指南/0058-group-chat-coolapp-event.md)获取回调参数`OpenConversationId`参数值。 - **单聊助手**：不传入此参数。 |
| userId | String | 否 | 用户userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)或[查询用户详情](0056-query-user-details.md)接口获取。   - 当会话类型为单聊助手时，userId和unionId二选一必填。 - 其他会话类型，不需要传入此参数。 |
| unionId | String | 否 | 用户unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取。   - 当会话类型为单聊助手时，userId和unionId二选一必填。 - 其他会话类型，不需要传入此参数。 |
| robotCode | String | 否 | 机器人编码：   - 单聊助手（此参数必填）。    - 企业内部开发-机器人应用的AppKey值。   - 企业内部应用机器人。   - 第三方企业应用机器人 - 其他会话类型，不需要传入此参数 |
| coolAppCode | String | 否 | 酷应用编码：   - 群聊：    - 基于群模板创建的群，不需要传入此参数。   - 安装群聊酷应用的群，**必须**传入此参数。 - 单聊助手：不需传入此参数。 |
| groupTemplateId | String | 否 | 群模板id：   - 群聊：    - ·基于群模板创建的群，**必须**传入此参数。   - 安装群聊酷应用的群，不需要传入此参数。 - 其他会话类型，不需传入此参数。 |
| receiverUserIdList | Array of String | 否 | 吊顶可见者userId，最多100个，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)或[查询用户详情](0056-query-user-details.md)接口获取。   - 群聊：    - 若不传入`receiverUserIdList`和`receiverUnionIdList`，则默认吊顶对会话内所有人可见。   - 传入参数`receiverUserIdList`或`receiverUnionIdList`，则吊顶仅对对应用户可见。 - 单聊助手：不需要传入此参数。 |
| receiverUnionIdList | Array of String | 否 | 吊顶可见者unionId，最多100个，可通过[查询用户详情](0056-query-user-details.md)接口获取。  群聊：   - 若不传入receiverUserIdList和receiverUnionIdList，则默认吊顶对会话内所有人可见。 - 传入参数receiverUserIdList或receiverUnionIdList，则吊顶仅对对应用户可见。   单聊助手：不需要传入此参数。 |
| expiredTime | Long | 否 | 吊顶的过期时间，毫秒级时间戳。      不传入此值，默认不过期。 |
| platforms | String | 否 | 期望吊顶的端，如果有多个用“｜”分隔。 例如：ios|mac|android|win表示iOS、MAC、安卓和windows端。 |

### 请求示例

HTTP

```
POST /v2.0/im/topBoxes HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxx
Content-Type:application/json

{
  "cardTemplateId" : "xxx",
  "outTrackId" : "xxx",
  "callbackRouteKey" : "xxx",
  "cardData" : {
    "cardParamMap" : {
      "key" : "xxx"
    }
  },
  "userIdPrivateDataMap" : {
    "key" : {
      "cardParamMap" : {
        "key" : "xxx"
      }
    }
  },
  "unionIdPrivateDataMap" : {
    "key" : {
      "cardParamMap" : {
        "key" : "xxx"
      }
    }
  },
  "cardSettings" : {
    "pullStrategy" : false
  },
  "conversationType" : 1,
  "openConversationId" : "cidxxxxx==",
  "userId" : "xxx",
  "unionId" : "xxx",
  "robotCode" : "xxx",
  "coolAppCode" : "COOLAPP-X-XXX",
  "groupTemplateId" : "xxx-xxx-xxx",
  "receiverUserIdList" : [ "xxx" ],
  "receiverUnionIdList" : [ "xxx" ],
  "expiredTime" : 1850042969000,
  "platforms" : "ios|win"
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
    public static com.aliyun.dingtalkim_2_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkim_2_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkim_2_0.Client client = Sample.createClient();
        com.aliyun.dingtalkim_2_0.models.CreateTopboxHeaders createTopboxHeaders = new com.aliyun.dingtalkim_2_0.models.CreateTopboxHeaders();
        createTopboxHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkim_2_0.models.CreateTopboxRequest.CreateTopboxRequestCardSettings cardSettings = new com.aliyun.dingtalkim_2_0.models.CreateTopboxRequest.CreateTopboxRequestCardSettings()
                .setPullStrategy(false);
        java.util.Map<String, String> unionIdPrivateDataMapValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "xxx")
        );
        com.aliyun.dingtalkim_2_0.models.UnionIdPrivateDataMapValue unionIdPrivateDataMapValueKey = new com.aliyun.dingtalkim_2_0.models.UnionIdPrivateDataMapValue()
                .setCardParamMap(unionIdPrivateDataMapValueKeyCardParamMap);
        java.util.Map<String, com.aliyun.dingtalkim_2_0.models.UnionIdPrivateDataMapValue> unionIdPrivateDataMap = TeaConverter.buildMap(
            new TeaPair("unionIdPrivateDataMapValueKey", unionIdPrivateDataMapValueKey)
        );
        java.util.Map<String, String> userIdPrivateDataMapValueKeyCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "xxx")
        );
        com.aliyun.dingtalkim_2_0.models.UserIdPrivateDataMapValue userIdPrivateDataMapValueKey = new com.aliyun.dingtalkim_2_0.models.UserIdPrivateDataMapValue()
                .setCardParamMap(userIdPrivateDataMapValueKeyCardParamMap);
        java.util.Map<String, com.aliyun.dingtalkim_2_0.models.UserIdPrivateDataMapValue> userIdPrivateDataMap = TeaConverter.buildMap(
            new TeaPair("userIdPrivateDataMapValueKey", userIdPrivateDataMapValueKey)
        );
        java.util.Map<String, String> cardDataCardParamMap = TeaConverter.buildMap(
            new TeaPair("key", "xxx")
        );
        com.aliyun.dingtalkim_2_0.models.CreateTopboxRequest.CreateTopboxRequestCardData cardData = new com.aliyun.dingtalkim_2_0.models.CreateTopboxRequest.CreateTopboxRequestCardData()
                .setCardParamMap(cardDataCardParamMap);
        com.aliyun.dingtalkim_2_0.models.CreateTopboxRequest createTopboxRequest = new com.aliyun.dingtalkim_2_0.models.CreateTopboxRequest()
                .setCardTemplateId("xxx")
                .setOutTrackId("xxx")
                .setCallbackRouteKey("xxx")
                .setCardData(cardData)
                .setUserIdPrivateDataMap(userIdPrivateDataMap)
                .setUnionIdPrivateDataMap(unionIdPrivateDataMap)
                .setCardSettings(cardSettings)
                .setConversationType(1)
                .setOpenConversationId("cidxxxxx==")
                .setUserId("xxx")
                .setUnionId("xxx")
                .setRobotCode("xxx")
                .setCoolAppCode("COOLAPP-X-XXX")
                .setGroupTemplateId("xxx-xxx-xxx")
                .setReceiverUserIdList(java.util.Arrays.asList(
                    "xxx"
                ))
                .setReceiverUnionIdList(java.util.Arrays.asList(
                    "xxx"
                ))
                .setExpiredTime(1850042969000L)
                .setPlatforms("ios|win");
        try {
            client.createTopboxWithOptions(createTopboxRequest, createTopboxHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.im_2_0.client import Client as dingtalkim_2_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.im_2_0 import models as dingtalkim__2__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkim_2_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkim_2_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_topbox_headers = dingtalkim__2__0_models.CreateTopboxHeaders()
        create_topbox_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_settings = dingtalkim__2__0_models.CreateTopboxRequestCardSettings(
            pull_strategy=False
        )
        union_id_private_data_map_value_key_card_param_map = {
            'key': 'xxx'
        }
        union_id_private_data_map_value_key = dingtalkim__2__0_models.UnionIdPrivateDataMapValue(
            card_param_map=union_id_private_data_map_value_key_card_param_map
        )
        union_id_private_data_map = {
            'unionIdPrivateDataMapValueKey': union_id_private_data_map_value_key
        }
        user_id_private_data_map_value_key_card_param_map = {
            'key': 'xxx'
        }
        user_id_private_data_map_value_key = dingtalkim__2__0_models.UserIdPrivateDataMapValue(
            card_param_map=user_id_private_data_map_value_key_card_param_map
        )
        user_id_private_data_map = {
            'userIdPrivateDataMapValueKey': user_id_private_data_map_value_key
        }
        card_data_card_param_map = {
            'key': 'xxx'
        }
        card_data = dingtalkim__2__0_models.CreateTopboxRequestCardData(
            card_param_map=card_data_card_param_map
        )
        create_topbox_request = dingtalkim__2__0_models.CreateTopboxRequest(
            card_template_id='xxx',
            out_track_id='xxx',
            callback_route_key='xxx',
            card_data=card_data,
            user_id_private_data_map=user_id_private_data_map,
            union_id_private_data_map=union_id_private_data_map,
            card_settings=card_settings,
            conversation_type=1,
            open_conversation_id='cidxxxxx==',
            user_id='xxx',
            union_id='xxx',
            robot_code='xxx',
            cool_app_code='COOLAPP-X-XXX',
            group_template_id='xxx-xxx-xxx',
            receiver_user_id_list=[
                'xxx'
            ],
            receiver_union_id_list=[
                'xxx'
            ],
            expired_time=1850042969000,
            platforms='ios|win'
        )
        try:
            client.create_topbox_with_options(create_topbox_request, create_topbox_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_topbox_headers = dingtalkim__2__0_models.CreateTopboxHeaders()
        create_topbox_headers.x_acs_dingtalk_access_token = '<your access token>'
        card_settings = dingtalkim__2__0_models.CreateTopboxRequestCardSettings(
            pull_strategy=False
        )
        union_id_private_data_map_value_key_card_param_map = {
            'key': 'xxx'
        }
        union_id_private_data_map_value_key = dingtalkim__2__0_models.UnionIdPrivateDataMapValue(
            card_param_map=union_id_private_data_map_value_key_card_param_map
        )
        union_id_private_data_map = {
            'unionIdPrivateDataMapValueKey': union_id_private_data_map_value_key
        }
        user_id_private_data_map_value_key_card_param_map = {
            'key': 'xxx'
        }
        user_id_private_data_map_value_key = dingtalkim__2__0_models.UserIdPrivateDataMapValue(
            card_param_map=user_id_private_data_map_value_key_card_param_map
        )
        user_id_private_data_map = {
            'userIdPrivateDataMapValueKey': user_id_private_data_map_value_key
        }
        card_data_card_param_map = {
            'key': 'xxx'
        }
        card_data = dingtalkim__2__0_models.CreateTopboxRequestCardData(
            card_param_map=card_data_card_param_map
        )
        create_topbox_request = dingtalkim__2__0_models.CreateTopboxRequest(
            card_template_id='xxx',
            out_track_id='xxx',
            callback_route_key='xxx',
            card_data=card_data,
            user_id_private_data_map=user_id_private_data_map,
            union_id_private_data_map=union_id_private_data_map,
            card_settings=card_settings,
            conversation_type=1,
            open_conversation_id='cidxxxxx==',
            user_id='xxx',
            union_id='xxx',
            robot_code='xxx',
            cool_app_code='COOLAPP-X-XXX',
            group_template_id='xxx-xxx-xxx',
            receiver_user_id_list=[
                'xxx'
            ],
            receiver_union_id_list=[
                'xxx'
            ],
            expired_time=1850042969000,
            platforms='ios|win'
        )
        try:
            await client.create_topbox_with_options_async(create_topbox_request, create_topbox_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateTopboxHeaders;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateTopboxRequest\cardSettings;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\UnionIdPrivateDataMapValue;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\UserIdPrivateDataMapValue;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateTopboxRequest\cardData;
use AlibabaCloud\SDK\Dingtalk\Vim_2_0\Models\CreateTopboxRequest;
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
        $createTopboxHeaders = new CreateTopboxHeaders([]);
        $createTopboxHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $cardSettings = new cardSettings([
            "pullStrategy" => false
        ]);
        $unionIdPrivateDataMapValueKeyCardParamMap = [
            "key" => "xxx"
        ];
        $unionIdPrivateDataMapValueKey = new UnionIdPrivateDataMapValue([
            "cardParamMap" => $unionIdPrivateDataMapValueKeyCardParamMap
        ]);
        $unionIdPrivateDataMap = [
            "unionIdPrivateDataMapValueKey" => $unionIdPrivateDataMapValueKey
        ];
        $userIdPrivateDataMapValueKeyCardParamMap = [
            "key" => "xxx"
        ];
        $userIdPrivateDataMapValueKey = new UserIdPrivateDataMapValue([
            "cardParamMap" => $userIdPrivateDataMapValueKeyCardParamMap
        ]);
        $userIdPrivateDataMap = [
            "userIdPrivateDataMapValueKey" => $userIdPrivateDataMapValueKey
        ];
        $cardDataCardParamMap = [
            "key" => "xxx"
        ];
        $cardData = new cardData([
            "cardParamMap" => $cardDataCardParamMap
        ]);
        $createTopboxRequest = new CreateTopboxRequest([
            "cardTemplateId" => "xxx",
            "outTrackId" => "xxx",
            "callbackRouteKey" => "xxx",
            "cardData" => $cardData,
            "userIdPrivateDataMap" => $userIdPrivateDataMap,
            "unionIdPrivateDataMap" => $unionIdPrivateDataMap,
            "cardSettings" => $cardSettings,
            "conversationType" => 1,
            "openConversationId" => "cidxxxxx==",
            "userId" => "xxx",
            "unionId" => "xxx",
            "robotCode" => "xxx",
            "coolAppCode" => "COOLAPP-X-XXX",
            "groupTemplateId" => "xxx-xxx-xxx",
            "receiverUserIdList" => [
                "xxx"
            ],
            "receiverUnionIdList" => [
                "xxx"
            ],
            "expiredTime" => 1850042969000,
            "platforms" => "ios|win"
        ]);
        try {
            $client->createTopboxWithOptions($createTopboxRequest, $createTopboxHeaders, new RuntimeOptions([]));
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
  dingtalkim_2_0  "github.com/alibabacloud-go/dingtalk/im_2_0"
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
func CreateClient () (_result *dingtalkim_2_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkim_2_0.Client{}
  _result, _err = dingtalkim_2_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createTopboxHeaders := &dingtalkim_2_0.CreateTopboxHeaders{}
  createTopboxHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  cardSettings := &dingtalkim_2_0.CreateTopboxRequestCardSettings{
    PullStrategy: tea.Bool(false),
  }
  unionIdPrivateDataMapValueKeyCardParamMap := map[string]*string{
    "key": tea.String("xxx"),
  }
  unionIdPrivateDataMapValueKey := &dingtalkim_2_0.UnionIdPrivateDataMapValue{
    CardParamMap: unionIdPrivateDataMapValueKeyCardParamMap,
  }
  unionIdPrivateDataMap := map[string]*dingtalkim_2_0.UnionIdPrivateDataMapValue{
    "unionIdPrivateDataMapValueKey": unionIdPrivateDataMapValueKey,
  }
  userIdPrivateDataMapValueKeyCardParamMap := map[string]*string{
    "key": tea.String("xxx"),
  }
  userIdPrivateDataMapValueKey := &dingtalkim_2_0.UserIdPrivateDataMapValue{
    CardParamMap: userIdPrivateDataMapValueKeyCardParamMap,
  }
  userIdPrivateDataMap := map[string]*dingtalkim_2_0.UserIdPrivateDataMapValue{
    "userIdPrivateDataMapValueKey": userIdPrivateDataMapValueKey,
  }
  cardDataCardParamMap := map[string]*string{
    "key": tea.String("xxx"),
  }
  cardData := &dingtalkim_2_0.CreateTopboxRequestCardData{
    CardParamMap: cardDataCardParamMap,
  }
  createTopboxRequest := &dingtalkim_2_0.CreateTopboxRequest{
    CardTemplateId: tea.String("xxx"),
    OutTrackId: tea.String("xxx"),
    CallbackRouteKey: tea.String("xxx"),
    CardData: cardData,
    UserIdPrivateDataMap: userIdPrivateDataMap,
    UnionIdPrivateDataMap: unionIdPrivateDataMap,
    CardSettings: cardSettings,
    ConversationType: tea.Int32(1),
    OpenConversationId: tea.String("cidxxxxx=="),
    UserId: tea.String("xxx"),
    UnionId: tea.String("xxx"),
    RobotCode: tea.String("xxx"),
    CoolAppCode: tea.String("COOLAPP-X-XXX"),
    GroupTemplateId: tea.String("xxx-xxx-xxx"),
    ReceiverUserIdList: []*string{tea.String("xxx")},
    ReceiverUnionIdList: []*string{tea.String("xxx")},
    ExpiredTime: tea.Int64(1850042969000),
    Platforms: tea.String("ios|win"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTopboxWithOptions(createTopboxRequest, createTopboxHeaders, &util.RuntimeOptions{})
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
const dingtalkim_2_0 = require('@alicloud/dingtalk/im_2_0');
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
    return new dingtalkim_2_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createTopboxHeaders = new dingtalkim_2_0.CreateTopboxHeaders({ });
    createTopboxHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let cardSettings = new dingtalkim_2_0.CreateTopboxRequestCardSettings({
      pullStrategy: false,
    });
    let unionIdPrivateDataMapValueKeyCardParamMap = {
      key: 'xxx',
    };
    let unionIdPrivateDataMapValueKey = new dingtalkim_2_0.UnionIdPrivateDataMapValue({
      cardParamMap: unionIdPrivateDataMapValueKeyCardParamMap,
    });
    let unionIdPrivateDataMap = {
      unionIdPrivateDataMapValueKey: unionIdPrivateDataMapValueKey,
    };
    let userIdPrivateDataMapValueKeyCardParamMap = {
      key: 'xxx',
    };
    let userIdPrivateDataMapValueKey = new dingtalkim_2_0.UserIdPrivateDataMapValue({
      cardParamMap: userIdPrivateDataMapValueKeyCardParamMap,
    });
    let userIdPrivateDataMap = {
      userIdPrivateDataMapValueKey: userIdPrivateDataMapValueKey,
    };
    let cardDataCardParamMap = {
      key: 'xxx',
    };
    let cardData = new dingtalkim_2_0.CreateTopboxRequestCardData({
      cardParamMap: cardDataCardParamMap,
    });
    let createTopboxRequest = new dingtalkim_2_0.CreateTopboxRequest({
      cardTemplateId: 'xxx',
      outTrackId: 'xxx',
      callbackRouteKey: 'xxx',
      cardData: cardData,
      userIdPrivateDataMap: userIdPrivateDataMap,
      unionIdPrivateDataMap: unionIdPrivateDataMap,
      cardSettings: cardSettings,
      conversationType: 1,
      openConversationId: 'cidxxxxx==',
      userId: 'xxx',
      unionId: 'xxx',
      robotCode: 'xxx',
      coolAppCode: 'COOLAPP-X-XXX',
      groupTemplateId: 'xxx-xxx-xxx',
      receiverUserIdList: [
        'xxx'
      ],
      receiverUnionIdList: [
        'xxx'
      ],
      expiredTime: 1850042969000,
      platforms: 'ios|win',
    });
    try {
      await client.createTopboxWithOptions(createTopboxRequest, createTopboxHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkim_2_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkim_2_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkim_2_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxHeaders createTopboxHeaders = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxHeaders();
            createTopboxHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxRequest.CreateTopboxRequestCardSettings cardSettings = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxRequest.CreateTopboxRequestCardSettings
            {
                PullStrategy = false,
            };
            Dictionary<string, string> unionIdPrivateDataMapValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "xxx"},
            };
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.UnionIdPrivateDataMapValue unionIdPrivateDataMapValueKey = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.UnionIdPrivateDataMapValue
            {
                CardParamMap = unionIdPrivateDataMapValueKeyCardParamMap,
            };
            Dictionary<string, AlibabaCloud.SDK.Dingtalkim_2_0.Models.UnionIdPrivateDataMapValue> unionIdPrivateDataMap = new Dictionary<string, AlibabaCloud.SDK.Dingtalkim_2_0.Models.UnionIdPrivateDataMapValue>
            {
                {"unionIdPrivateDataMapValueKey", unionIdPrivateDataMapValueKey},
            };
            Dictionary<string, string> userIdPrivateDataMapValueKeyCardParamMap = new Dictionary<string, string>
            {
                {"key", "xxx"},
            };
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.UserIdPrivateDataMapValue userIdPrivateDataMapValueKey = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.UserIdPrivateDataMapValue
            {
                CardParamMap = userIdPrivateDataMapValueKeyCardParamMap,
            };
            Dictionary<string, AlibabaCloud.SDK.Dingtalkim_2_0.Models.UserIdPrivateDataMapValue> userIdPrivateDataMap = new Dictionary<string, AlibabaCloud.SDK.Dingtalkim_2_0.Models.UserIdPrivateDataMapValue>
            {
                {"userIdPrivateDataMapValueKey", userIdPrivateDataMapValueKey},
            };
            Dictionary<string, string> cardDataCardParamMap = new Dictionary<string, string>
            {
                {"key", "xxx"},
            };
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxRequest.CreateTopboxRequestCardData cardData = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxRequest.CreateTopboxRequestCardData
            {
                CardParamMap = cardDataCardParamMap,
            };
            AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxRequest createTopboxRequest = new AlibabaCloud.SDK.Dingtalkim_2_0.Models.CreateTopboxRequest
            {
                CardTemplateId = "xxx",
                OutTrackId = "xxx",
                CallbackRouteKey = "xxx",
                CardData = cardData,
                UserIdPrivateDataMap = userIdPrivateDataMap,
                UnionIdPrivateDataMap = unionIdPrivateDataMap,
                CardSettings = cardSettings,
                ConversationType = 1,
                OpenConversationId = "cidxxxxx==",
                UserId = "xxx",
                UnionId = "xxx",
                RobotCode = "xxx",
                CoolAppCode = "COOLAPP-X-XXX",
                GroupTemplateId = "xxx-xxx-xxx",
                ReceiverUserIdList = new List<string>
                {
                    "xxx"
                },
                ReceiverUnionIdList = new List<string>
                {
                    "xxx"
                },
                ExpiredTime = 1850042969000,
                Platforms = "ios|win",
            };
            try
            {
                client.CreateTopboxWithOptions(createTopboxRequest, createTopboxHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 请求是否成功：   - **true**：成功 - **false**：失败 |

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
| 400 | param.empty | 请求参数为空 | 请求参数为空 |
| 400 | cidParse.wrong | 会话id解码失败 | 会话id解码失败 |
| 400 | chat.notExist | 会话不存在 | 会话不存在 |
| 400 | group.org.checkFailed | 群不属于当前企业 | 群不属于当前企业 |
| 400 | chat.coolApp.notInstalled | 酷应用未安装到会话内 | 酷应用未安装到会话内 |
| 400 | permission.coolApp.checkFailed | 无权限，酷应用不属于当前token对应的应用名下 | 无权限，酷应用不属于当前token对应的应用名下 |
| 400 | group.groupTemplate.notInstalled | 群模板未安装到群内 | 群模板未安装到群内 |
| 400 | permission.sceneGroup.checkFailed | 无权限，该群安装的群模板不属于当前token对应的应用名下 | 无权限，该群安装的群模板不属于当前token对应的应用名下 |
| 400 | card.content.checkFailed | 卡片内容违规 | 卡片内容违规 |
| 400 | cardInstance.wrong | 创建卡片实例失败，先检查卡片模板是否已发布 | 创建卡片实例失败，先检查卡片模板是否已发布 |
| 400 | receiver.id.parseFailed | 吊顶可见者id解析失败 | 吊顶可见者id解析失败 |
| 400 | open.topbox.failed | 开启吊顶失败 | 开启吊顶失败 |
| 400 | user.not.found | 用户不存在 | 用户不存在 |
| 400 | robot.not.found | 机器人不存在 | 机器人不存在 |
| 400 | conversationType.illegal | 会话类型值无效 | 会话类型值无效 |
| 400 | param.illegal | 请求参数无效 | 请求参数无效 |
| 400 | robot.queryFalied | 机器人查询失败 | 机器人查询失败 |
| 400 | mainApp.queryFailed | 主应用查询失败 | 主应用查询失败 |
| 400 | coolAppCode.empty | 酷应用编码为空 | 酷应用编码为空 |
| 400 | openConversationId.empty | 会话id为空 | 会话id为空 |
| 400 | userIdOrUnionId.empty | 用户id为空 | 用户id为空 |
| 400 | robotCode.empty | 机器人编码为空 | 机器人编码为空 |
| 400 | cardTemplate.not.exist | 卡片模板不存在 | 卡片模板不存在 |
| 400 | auth.failed | %s | 权限校验不通过 |
| 500 | system.busy | 系统繁忙 | 系统异常错误 |
