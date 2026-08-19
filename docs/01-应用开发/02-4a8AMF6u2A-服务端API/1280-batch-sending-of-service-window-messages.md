---
title: "批量发送服务窗消息"
source_url: "https://open.dingtalk.com/document/development/batch-sending-of-service-window-messages"
namespace: "development"
slug: "batch-sending-of-service-window-messages"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 服务窗 > 批量发送服务窗消息"
doc_id: "lW4pHmRFUI"
updated_at: "2025-09-11 21:03:45"
---

> Source: https://open.dingtalk.com/document/development/batch-sending-of-service-window-messages
> Path: 应用开发 / 服务端API / 更多开放 > 服务窗 > 批量发送服务窗消息
> Updated: 2025-09-11 21:03:45

# 批量发送服务窗消息

调用本接口，向服务窗的一批粉丝用户发送消息。

## 接口调用说明

- 服务窗消息开放接口均为新版规范接口，请参考[服务端SDK下载](0002-download-the-server-side-sdk.md)。
- 目前此接口每天最多允许调用100次。
- 每位粉丝用户一天内最多允许收到三条来自同一服务窗的消息（包括服务窗后台群发、批量接口及单发接口）。
- 服务窗为减少内容相同消息对用户的打扰，默认场景下会对相同内容的消息推送会进行前去重处理，相同内容消息同一用户一天内仅会收到一条。
- 目前支持的消息格式有文本、链接、卡片、markdown等,消息类型详见[消息类型介绍](1278-service-window-message-types-1.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/officialAccounts/oToMessages/batchSend |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-OfficialAccount.Message.Send-服务窗发送消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| detail | Object | 是 | 消息详情。 |
| msgType | String | 是 | 消息类型。 |
| uuid | String | 是 | 消息请求唯一ID。长度不超过128位字符。 |
| bizRequestId | String | 否 | 业务请求标识。      当一次业务请求需要多次调用发送API时可以设置此参数，方便后续跟踪处理。 |
| userIdList | Array of String | 否 | 消息接收人列表，最多支持1000人。      值为服务窗粉丝userid，可以通过粉丝关注事件获取对应的userid。 |
| messageBody | Object | 是 | 消息体。 |
| text | Object | 否 | 文本消息内容。      如果消息类型为文本消息则此参数必填。 |
| content | String | 是 | 文本消息内容，建议500字符以内。 |
| markdown | Object | 否 | markdown消息，仅对消息类型为markdown时有效。 |
| title | String | 是 | 首屏会话透出的展示内容。 |
| text | String | 是 | markdown格式的消息，建议500字符以内。 |
| link | Object | 否 | 链接消息类型。 |
| picUrl | String | 是 | 图片地址。 |
| messageUrl | String | 是 | 消息链接地址，当发送消息为小程序时支持小程序跳转链接。 |
| title | String | 是 | 消息标题，建议100字符以内。 |
| text | String | 是 | 消息描述，建议500字符以内。 |
| actionCard | Object | 否 | 卡片消息。 |
| buttonOrientation | String | 否 | 按钮排列方式。   - **0**：竖直排列。 - **1**：横向排列       必须与**buttonList**同时设置。 |
| singleUrl | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| singleTitle | String | 否 | 使用整体跳转ActionCard样式时的标题。      必须与**singleUrl**同时设置，最长20个字符。 |
| markdown | String | 否 | 消息内容，支持markdown。      语法参考标准markdown语法。1000个字符以内。 |
| title | String | 是 | 首屏会话透出的展示内容。 |
| buttonList | Array | 否 | 使用独立跳转ActionCard样式时的按钮列表。      必须与**buttonOrientation**同时设置，且长度不超过1000字符。 |
| title | String | 是 | 使用独立跳转ActionCard样式时的按钮的标题，最长20个字符。 |
| actionUrl | String | 是 | 使用独立跳转ActionCard样式时的跳转链接。 |
| sendToAll | Boolean | 否 | 全员群发。 |
| bizId | String | 否 | 服务窗授权的调用方标识，可以为空。 |
| accountId | String | 否 | 服务窗账号id，[自建服务窗应用](1279-self-built-service-window-application.md)调用时不需要传此参数。  非自建服务窗应用需要传此参数，此参数可以通过[获取企业下服务窗列表](1282-queries-the-list-of-services-under-an-enterprise.md)接口获得。 |

### 请求示例

HTTP

```
POST /v1.0/crm/officialAccounts/oToMessages/batchSend HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:3abbexxxx
Content-Type:application/json

{
  "detail" : {
    "msgType" : "text",
    "uuid" : "bdb81c6f-506f-4d4f-9752-68c8ddc61cf0",
    "bizRequestId" : "20210520-news",
    "userIdList" : [ "idzb2eyudksdojgw6gfi" ],
    "messageBody" : {
      "text" : {
        "content" : "你好，服务窗。"
      },
      "markdown" : {
        "title" : "欢迎您关注服务窗",
        "text" : "# 这是支持markdown的文本 \\n## 标题2  \\n* 列表1 \\n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
      },
      "link" : {
        "picUrl" : "@lADOADmaWMzazQKA",
        "messageUrl" : "https://www.dingtalk.com/",
        "title" : "link消息标题",
        "text" : "消息内容"
      },
      "actionCard" : {
        "buttonOrientation" : "1",
        "singleUrl" : "https://open.dingtalk.com",
        "singleTitle" : "查看详情",
        "markdown" : "支持markdown格式的正文内容",
        "title" : "透出到会话列表和通知的文案",
        "buttonList" : [ {
          "title" : "淘宝首页",
          "actionUrl" : "https://www.taobao.com"
        } ]
      }
    },
    "sendToAll" : true
  },
  "bizId" : "dingtalk-biz-20210520-9752",
  "accountId" : "123"
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
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageHeaders batchSendOfficialAccountOTOMessageHeaders = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageHeaders();
        batchSendOfficialAccountOTOMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList detailMessageBodyActionCardButtonList0 = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList()
                .setTitle("淘宝首页")
                .setActionUrl("https://www.taobao.com");
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard detailMessageBodyActionCard = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard()
                .setButtonOrientation("1")
                .setSingleUrl("https://open.dingtalk.com")
                .setSingleTitle("查看详情")
                .setMarkdown("支持markdown格式的正文内容")
                .setTitle("透出到会话列表和通知的文案")
                .setButtonList(java.util.Arrays.asList(
                    detailMessageBodyActionCardButtonList0
                ));
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink detailMessageBodyLink = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink()
                .setPicUrl("@lADOADmaWMzazQKA")
                .setMessageUrl("https://www.dingtalk.com/")
                .setTitle("link消息标题")
                .setText("消息内容");
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown detailMessageBodyMarkdown = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown()
                .setTitle("欢迎您关注服务窗")
                .setText("# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)");
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText detailMessageBodyText = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText()
                .setContent("你好，服务窗。");
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody detailMessageBody = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody()
                .setText(detailMessageBodyText)
                .setMarkdown(detailMessageBodyMarkdown)
                .setLink(detailMessageBodyLink)
                .setActionCard(detailMessageBodyActionCard);
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail detail = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail()
                .setMsgType("text")
                .setUuid("bdb81c6f-506f-4d4f-9752-68c8ddc61cf0")
                .setBizRequestId("20210520-news")
                .setUserIdList(java.util.Arrays.asList(
                    "idzb2eyudksdojgw6gfi"
                ))
                .setMessageBody(detailMessageBody)
                .setSendToAll(true);
        com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest batchSendOfficialAccountOTOMessageRequest = new com.aliyun.dingtalkcrm_1_0.models.BatchSendOfficialAccountOTOMessageRequest()
                .setDetail(detail)
                .setBizId("dingtalk-biz-20210520-9752")
                .setAccountId("123");
        try {
            client.batchSendOfficialAccountOTOMessageWithOptions(batchSendOfficialAccountOTOMessageRequest, batchSendOfficialAccountOTOMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.crm_1_0.client import Client as dingtalkcrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.crm_1_0 import models as dingtalkcrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkcrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkcrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_send_official_account_otomessage_headers = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageHeaders()
        batch_send_official_account_otomessage_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_message_body_action_card_button_list_0 = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList(
            title='淘宝首页',
            action_url='https://www.taobao.com'
        )
        detail_message_body_action_card = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard(
            button_orientation='1',
            single_url='https://open.dingtalk.com',
            single_title='查看详情',
            markdown='支持markdown格式的正文内容',
            title='透出到会话列表和通知的文案',
            button_list=[
                detail_message_body_action_card_button_list_0
            ]
        )
        detail_message_body_link = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink(
            pic_url='@lADOADmaWMzazQKA',
            message_url='https://www.dingtalk.com/',
            title='link消息标题',
            text='消息内容'
        )
        detail_message_body_markdown = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown(
            title='欢迎您关注服务窗',
            text='# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)'
        )
        detail_message_body_text = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText(
            content='你好，服务窗。'
        )
        detail_message_body = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody(
            text=detail_message_body_text,
            markdown=detail_message_body_markdown,
            link=detail_message_body_link,
            action_card=detail_message_body_action_card
        )
        detail = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetail(
            msg_type='text',
            uuid='bdb81c6f-506f-4d4f-9752-68c8ddc61cf0',
            biz_request_id='20210520-news',
            user_id_list=[
                'idzb2eyudksdojgw6gfi'
            ],
            message_body=detail_message_body,
            send_to_all=True
        )
        batch_send_official_account_otomessage_request = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequest(
            detail=detail,
            biz_id='dingtalk-biz-20210520-9752',
            account_id='123'
        )
        try:
            client.batch_send_official_account_otomessage_with_options(batch_send_official_account_otomessage_request, batch_send_official_account_otomessage_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        batch_send_official_account_otomessage_headers = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageHeaders()
        batch_send_official_account_otomessage_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_message_body_action_card_button_list_0 = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList(
            title='淘宝首页',
            action_url='https://www.taobao.com'
        )
        detail_message_body_action_card = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard(
            button_orientation='1',
            single_url='https://open.dingtalk.com',
            single_title='查看详情',
            markdown='支持markdown格式的正文内容',
            title='透出到会话列表和通知的文案',
            button_list=[
                detail_message_body_action_card_button_list_0
            ]
        )
        detail_message_body_link = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink(
            pic_url='@lADOADmaWMzazQKA',
            message_url='https://www.dingtalk.com/',
            title='link消息标题',
            text='消息内容'
        )
        detail_message_body_markdown = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown(
            title='欢迎您关注服务窗',
            text='# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)'
        )
        detail_message_body_text = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText(
            content='你好，服务窗。'
        )
        detail_message_body = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody(
            text=detail_message_body_text,
            markdown=detail_message_body_markdown,
            link=detail_message_body_link,
            action_card=detail_message_body_action_card
        )
        detail = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequestDetail(
            msg_type='text',
            uuid='bdb81c6f-506f-4d4f-9752-68c8ddc61cf0',
            biz_request_id='20210520-news',
            user_id_list=[
                'idzb2eyudksdojgw6gfi'
            ],
            message_body=detail_message_body,
            send_to_all=True
        )
        batch_send_official_account_otomessage_request = dingtalkcrm__1__0_models.BatchSendOfficialAccountOTOMessageRequest(
            detail=detail,
            biz_id='dingtalk-biz-20210520-9752',
            account_id='123'
        )
        try:
            await client.batch_send_official_account_otomessage_with_options_async(batch_send_official_account_otomessage_request, batch_send_official_account_otomessage_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail\messageBody\actionCard\buttonList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail\messageBody\actionCard;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail\messageBody\link;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail\messageBody\markdown;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail\messageBody\text;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail\messageBody;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest\detail;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\BatchSendOfficialAccountOTOMessageRequest;
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
        $batchSendOfficialAccountOTOMessageHeaders = new BatchSendOfficialAccountOTOMessageHeaders([]);
        $batchSendOfficialAccountOTOMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $detailMessageBodyActionCardButtonList0 = new buttonList([
            "title" => "淘宝首页",
            "actionUrl" => "https://www.taobao.com"
        ]);
        $detailMessageBodyActionCard = new actionCard([
            "buttonOrientation" => "1",
            "singleUrl" => "https://open.dingtalk.com",
            "singleTitle" => "查看详情",
            "markdown" => "支持markdown格式的正文内容",
            "title" => "透出到会话列表和通知的文案",
            "buttonList" => [
                $detailMessageBodyActionCardButtonList0
            ]
        ]);
        $detailMessageBodyLink = new link([
            "picUrl" => "@lADOADmaWMzazQKA",
            "messageUrl" => "https://www.dingtalk.com/",
            "title" => "link消息标题",
            "text" => "消息内容"
        ]);
        $detailMessageBodyMarkdown = new markdown([
            "title" => "欢迎您关注服务窗",
            "text" => "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
        ]);
        $detailMessageBodyText = new text([
            "content" => "你好，服务窗。"
        ]);
        $detailMessageBody = new messageBody([
            "text" => $detailMessageBodyText,
            "markdown" => $detailMessageBodyMarkdown,
            "link" => $detailMessageBodyLink,
            "actionCard" => $detailMessageBodyActionCard
        ]);
        $detail = new detail([
            "msgType" => "text",
            "uuid" => "bdb81c6f-506f-4d4f-9752-68c8ddc61cf0",
            "bizRequestId" => "20210520-news",
            "userIdList" => [
                "idzb2eyudksdojgw6gfi"
            ],
            "messageBody" => $detailMessageBody,
            "sendToAll" => true
        ]);
        $batchSendOfficialAccountOTOMessageRequest = new BatchSendOfficialAccountOTOMessageRequest([
            "detail" => $detail,
            "bizId" => "dingtalk-biz-20210520-9752",
            "accountId" => "123"
        ]);
        try {
            $client->batchSendOfficialAccountOTOMessageWithOptions($batchSendOfficialAccountOTOMessageRequest, $batchSendOfficialAccountOTOMessageHeaders, new RuntimeOptions([]));
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
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkcrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkcrm_1_0.Client{}
  _result, _err = dingtalkcrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  batchSendOfficialAccountOTOMessageHeaders := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageHeaders{}
  batchSendOfficialAccountOTOMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  detailMessageBodyActionCardButtonList0 := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList{
    Title: tea.String("淘宝首页"),
    ActionUrl: tea.String("https://www.taobao.com"),
  }
  detailMessageBodyActionCard := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard{
    ButtonOrientation: tea.String("1"),
    SingleUrl: tea.String("https://open.dingtalk.com"),
    SingleTitle: tea.String("查看详情"),
    Markdown: tea.String("支持markdown格式的正文内容"),
    Title: tea.String("透出到会话列表和通知的文案"),
    ButtonList: []*dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList{detailMessageBodyActionCardButtonList0},
  }
  detailMessageBodyLink := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink{
    PicUrl: tea.String("@lADOADmaWMzazQKA"),
    MessageUrl: tea.String("https://www.dingtalk.com/"),
    Title: tea.String("link消息标题"),
    Text: tea.String("消息内容"),
  }
  detailMessageBodyMarkdown := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown{
    Title: tea.String("欢迎您关注服务窗"),
    Text: tea.String("# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"),
  }
  detailMessageBodyText := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText{
    Content: tea.String("你好，服务窗。"),
  }
  detailMessageBody := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody{
    Text: detailMessageBodyText,
    Markdown: detailMessageBodyMarkdown,
    Link: detailMessageBodyLink,
    ActionCard: detailMessageBodyActionCard,
  }
  detail := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetail{
    MsgType: tea.String("text"),
    Uuid: tea.String("bdb81c6f-506f-4d4f-9752-68c8ddc61cf0"),
    BizRequestId: tea.String("20210520-news"),
    UserIdList: []*string{tea.String("idzb2eyudksdojgw6gfi")},
    MessageBody: detailMessageBody,
    SendToAll: tea.Bool(true),
  }
  batchSendOfficialAccountOTOMessageRequest := &dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequest{
    Detail: detail,
    BizId: tea.String("dingtalk-biz-20210520-9752"),
    AccountId: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.BatchSendOfficialAccountOTOMessageWithOptions(batchSendOfficialAccountOTOMessageRequest, batchSendOfficialAccountOTOMessageHeaders, &util.RuntimeOptions{})
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
import dingtalkcrm_1_0, * as $dingtalkcrm_1_0 from '@alicloud/dingtalk/crm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkcrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkcrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let batchSendOfficialAccountOTOMessageHeaders = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageHeaders({ });
    batchSendOfficialAccountOTOMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let detailMessageBodyActionCardButtonList0 = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList({
      title: "淘宝首页",
      actionUrl: "https://www.taobao.com",
    });
    let detailMessageBodyActionCard = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard({
      buttonOrientation: "1",
      singleUrl: "https://open.dingtalk.com",
      singleTitle: "查看详情",
      markdown: "支持markdown格式的正文内容",
      title: "透出到会话列表和通知的文案",
      buttonList: [
        detailMessageBodyActionCardButtonList0
      ],
    });
    let detailMessageBodyLink = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink({
      picUrl: "@lADOADmaWMzazQKA",
      messageUrl: "https://www.dingtalk.com/",
      title: "link消息标题",
      text: "消息内容",
    });
    let detailMessageBodyMarkdown = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown({
      title: "欢迎您关注服务窗",
      text: "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)",
    });
    let detailMessageBodyText = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText({
      content: "你好，服务窗。",
    });
    let detailMessageBody = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody({
      text: detailMessageBodyText,
      markdown: detailMessageBodyMarkdown,
      link: detailMessageBodyLink,
      actionCard: detailMessageBodyActionCard,
    });
    let detail = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequestDetail({
      msgType: "text",
      uuid: "bdb81c6f-506f-4d4f-9752-68c8ddc61cf0",
      bizRequestId: "20210520-news",
      userIdList: [
        "idzb2eyudksdojgw6gfi"
      ],
      messageBody: detailMessageBody,
      sendToAll: true,
    });
    let batchSendOfficialAccountOTOMessageRequest = new $dingtalkcrm_1_0.BatchSendOfficialAccountOTOMessageRequest({
      detail: detail,
      bizId: "dingtalk-biz-20210520-9752",
      accountId: "123",
    });
    try {
      await client.batchSendOfficialAccountOTOMessageWithOptions(batchSendOfficialAccountOTOMessageRequest, batchSendOfficialAccountOTOMessageHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkcrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkcrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageHeaders batchSendOfficialAccountOTOMessageHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageHeaders();
            batchSendOfficialAccountOTOMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList detailMessageBodyActionCardButtonList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList
            {
                Title = "淘宝首页",
                ActionUrl = "https://www.taobao.com",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard detailMessageBodyActionCard = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard
            {
                ButtonOrientation = "1",
                SingleUrl = "https://open.dingtalk.com",
                SingleTitle = "查看详情",
                Markdown = "支持markdown格式的正文内容",
                Title = "透出到会话列表和通知的文案",
                ButtonList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList>
                {
                    detailMessageBodyActionCardButtonList0
                },
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink detailMessageBodyLink = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyLink
            {
                PicUrl = "@lADOADmaWMzazQKA",
                MessageUrl = "https://www.dingtalk.com/",
                Title = "link消息标题",
                Text = "消息内容",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown detailMessageBodyMarkdown = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown
            {
                Title = "欢迎您关注服务窗",
                Text = "# 这是支持markdown的文本 \n## 标题2  \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText detailMessageBodyText = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody.BatchSendOfficialAccountOTOMessageRequestDetailMessageBodyText
            {
                Content = "你好，服务窗。",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody detailMessageBody = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail.BatchSendOfficialAccountOTOMessageRequestDetailMessageBody
            {
                Text = detailMessageBodyText,
                Markdown = detailMessageBodyMarkdown,
                Link = detailMessageBodyLink,
                ActionCard = detailMessageBodyActionCard,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail detail = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest.BatchSendOfficialAccountOTOMessageRequestDetail
            {
                MsgType = "text",
                Uuid = "bdb81c6f-506f-4d4f-9752-68c8ddc61cf0",
                BizRequestId = "20210520-news",
                UserIdList = new List<string>
                {
                    "idzb2eyudksdojgw6gfi"
                },
                MessageBody = detailMessageBody,
                SendToAll = true,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest batchSendOfficialAccountOTOMessageRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.BatchSendOfficialAccountOTOMessageRequest
            {
                Detail = detail,
                BizId = "dingtalk-biz-20210520-9752",
                AccountId = "123",
            };
            try
            {
                client.BatchSendOfficialAccountOTOMessageWithOptions(batchSendOfficialAccountOTOMessageRequest, batchSendOfficialAccountOTOMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果。 |
| openPushId | String | 消息推送ID，长度不超过256位，可用于消息发送进度排查。 |
| requestId | String | 请求ID。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "openPushId" : "UH849RExxx"
  },
  "requestId" : "8ppk7XXX"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.tast | request too fast. | 请求过快被限流。 |
| 400 | idempotentParameterMismatch.uuid | illegal parameter %s | UUID 不存在 |
| 400 | illegalParameter.uuid | illegal uuid | UUID 不合法 |
| 400 | illegalParameter.messageContent | illegal message content | 消息内容不正确 |
| 400 | illegalParameter.messageBody | illegal message body | 消息体不正确 |
| 400 | illegalParameter.messageType | illegal message type | 消息类型不正确 |
| 400 | illegalParameter.messageReceiver | illegal message receiver | 消息接收人不正确 |
| 400 | illegalParameter.accountOrg | illegal account org | 服务窗账号不存在 |
| 400 | illegalParameter.account | illegal account | 服务窗账号不存在 |
| 400 | illegalRequest.overQuota | request over quota. | 请求超过配额。 |
| 500 | systemError | System error. | 系统异常 |
| 500 | systemError.messageStatus | illegal message status | 消息状态异常 |
