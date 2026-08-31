---
title: "发送服务窗单人消息"
source_url: "https://open.dingtalk.com/document/development/sends-a-single-message-from-the-service-window"
namespace: "development"
slug: "sends-a-single-message-from-the-service-window"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "更多开放 > 服务窗 > 发送服务窗单人消息"
doc_id: "nRzXacXnOA"
updated_at: "2026-06-04 19:12:01"
---

> Source: https://open.dingtalk.com/document/development/sends-a-single-message-from-the-service-window
> Path: 应用开发 / 服务端 API / 更多开放 > 服务窗 > 发送服务窗单人消息
> Updated: 2026-06-04 19:12:01

# 发送服务窗单人消息

调用本接口，向指定的用户发送服务窗消息。

## 接口调用说明

- 服务窗消息开放接口均为新版规范接口，请参考[服务端SDK下载](0002-download-the-server-side-sdk.md)。
- 此接口一天最多允许调用次数等于服务窗粉丝数量。
- 每位粉丝用户一天最多允许接收三条来自服务窗的消息（包括服务窗后台群发、批量发送接口及单人消息接口）。
- 服务窗为减少内容相同消息对用户的打扰，默认场景下会对相同内容的消息推送会进行前去重处理，相同内容消息同一用户一天内仅会收到一条。
- 目前支持的消息格式有文本、链接、卡片、markdown等，消息类型详见[消息类型介绍](1278-service-window-message-types-1.md)。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/officialAccounts/oToMessages/send |
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
| uuid | String | 是 | 消息发送请求唯一ID，长度不超过128位字符。 |
| userId | String | 否 | 消息接收人的userid。**此参数与unionId参数二选一且不允许同时存在。** 获取userId的途径有： 1. 通过接入服务窗免登后，在服务窗粉丝用户登录自建应用时通过JSAPI获得。 2. 通过服务窗关注回调事件获得关注用户。 |
| unionId | String | 否 | 消息接收人的unionId。此参数用于三方应用场景。 **此参数与userId参数二选一且不允许同时存在。** |
| messageBody | Object | 是 | 消息体。 |
| text | Object | 否 | 文本消息内容。      如果消息类型为文本消息则此参数必填。 |
| content | String | 是 | 消息内容，建议500字符以内。 |
| markdown | Object | 否 | markdown消息，仅对消息类型为markdown时有效。 |
| title | String | 是 | 首屏会话透出的展示内容。 |
| text | String | 是 | markdown格式的消息，建议500字符以内。 |
| link | Object | 否 | 链接消息类型。 |
| picUrl | String | 是 | 图片地址。 |
| messageUrl | String | 是 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接。 |
| title | String | 是 | 消息标题，建议100字符以内。 |
| text | String | 是 | 消息描述，建议500字符以内。 |
| actionCard | Object | 否 | 卡片消息。 |
| buttonOrientation | String | 否 | 按钮排列方式。   - **0**：竖直排列 - **1**：横向排列       必须与**buttonList**同时设置。 |
| singleUrl | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| singleTitle | String | 否 | 使用整体跳转ActionCard样式时的标题。      必须与**singleUrl**同时设置，最长20个字符。 |
| markdown | String | 否 | 消息内容，支持markdown。      语法参考标准markdown语法，1000个字符以内。 |
| title | String | 是 | 透出到会话列表和通知的文案。 |
| buttonList | Array | 否 | 使用独立跳转ActionCard样式时的按钮列表。      必须与**buttonOrientation**同时设置，且长度不超过1000字符。 |
| title | String | 是 | 使用独立跳转ActionCard样式时的按钮的标题，最长20个字符。 |
| actionUrl | String | 是 | 使用独立跳转ActionCard样式时的跳转链接。 |
| image | Object | 否 | 图片信息。 |
| mediaId | String | 否 | 图片media\_id，可调用[上传媒体文件](0646-upload-media-files.md)接口获取。 |
| bizId | String | 否 | 可选参数，API调用方标识，仅用于定制调用方场景。 |
| accountId | String | 否 | 服务窗账号id，[自建服务窗应用](1279-self-built-service-window-application.md)调用时不需要传此参数。  非自建服务窗应用需要传此参数，此参数可以通过[获取企业下服务窗列表](1282-queries-the-list-of-services-under-an-enterprise.md)接口获得。 |

### 请求示例

HTTP

```
POST /v1.0/crm/officialAccounts/oToMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:3abbe0xxxx
Content-Type:application/json

{
  "detail" : {
    "msgType" : "text",
    "uuid" : "bdb81c6f-xxxx-xxxx-xxxx-6",
    "userId" : "idzb2eyxxxx",
    "unionId" : "1234",
    "messageBody" : {
      "text" : {
        "content" : "你好，服务窗。"
      },
      "markdown" : {
        "title" : "欢迎您关注服务窗",
        "text" : "# 这是支持markdown的文本 \\n## 标题2 \\n* 列表1 \\n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
      },
      "link" : {
        "picUrl" : "@lADOADmaWMzazQKA",
        "messageUrl" : "https://www.dingtalk.com/",
        "title" : "link消息标题",
        "text" : "link消息内容"
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
      },
      "image" : {
        "mediaId" : "@rxxc"
      }
    }
  },
  "bizId" : "abc",
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
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageHeaders sendOfficialAccountOTOMessageHeaders = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageHeaders();
        sendOfficialAccountOTOMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage detailMessageBodyImage = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage()
                .setMediaId("@rxxc");
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList detailMessageBodyActionCardButtonList0 = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList()
                .setTitle("淘宝首页")
                .setActionUrl("https://www.taobao.com");
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard detailMessageBodyActionCard = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard()
                .setButtonOrientation("1")
                .setSingleUrl("https://open.dingtalk.com")
                .setSingleTitle("查看详情")
                .setMarkdown("支持markdown格式的正文内容")
                .setTitle("透出到会话列表和通知的文案")
                .setButtonList(java.util.Arrays.asList(
                    detailMessageBodyActionCardButtonList0
                ));
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink detailMessageBodyLink = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink()
                .setPicUrl("@lADOADmaWMzazQKA")
                .setMessageUrl("https://www.dingtalk.com/")
                .setTitle("link消息标题")
                .setText("link消息内容");
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown detailMessageBodyMarkdown = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown()
                .setTitle("欢迎您关注服务窗")
                .setText("# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)");
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyText detailMessageBodyText = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBodyText()
                .setContent("你好，服务窗。");
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBody detailMessageBody = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetailMessageBody()
                .setText(detailMessageBodyText)
                .setMarkdown(detailMessageBodyMarkdown)
                .setLink(detailMessageBodyLink)
                .setActionCard(detailMessageBodyActionCard)
                .setImage(detailMessageBodyImage);
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail detail = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail()
                .setMsgType("text")
                .setUuid("bdb81c6f-xxxx-xxxx-xxxx-6")
                .setUserId("idzb2eyxxxx")
                .setUnionId("1234")
                .setMessageBody(detailMessageBody);
        com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest sendOfficialAccountOTOMessageRequest = new com.aliyun.dingtalkcrm_1_0.models.SendOfficialAccountOTOMessageRequest()
                .setDetail(detail)
                .setBizId("abc")
                .setAccountId("123");
        try {
            client.sendOfficialAccountOTOMessageWithOptions(sendOfficialAccountOTOMessageRequest, sendOfficialAccountOTOMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        send_official_account_otomessage_headers = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageHeaders()
        send_official_account_otomessage_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_message_body_image = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage(
            media_id='@rxxc'
        )
        detail_message_body_action_card_button_list_0 = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList(
            title='淘宝首页',
            action_url='https://www.taobao.com'
        )
        detail_message_body_action_card = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard(
            button_orientation='1',
            single_url='https://open.dingtalk.com',
            single_title='查看详情',
            markdown='支持markdown格式的正文内容',
            title='透出到会话列表和通知的文案',
            button_list=[
                detail_message_body_action_card_button_list_0
            ]
        )
        detail_message_body_link = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink(
            pic_url='@lADOADmaWMzazQKA',
            message_url='https://www.dingtalk.com/',
            title='link消息标题',
            text='link消息内容'
        )
        detail_message_body_markdown = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown(
            title='欢迎您关注服务窗',
            text='# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)'
        )
        detail_message_body_text = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyText(
            content='你好，服务窗。'
        )
        detail_message_body = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBody(
            text=detail_message_body_text,
            markdown=detail_message_body_markdown,
            link=detail_message_body_link,
            action_card=detail_message_body_action_card,
            image=detail_message_body_image
        )
        detail = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetail(
            msg_type='text',
            uuid='bdb81c6f-xxxx-xxxx-xxxx-6',
            user_id='idzb2eyxxxx',
            union_id='1234',
            message_body=detail_message_body
        )
        send_official_account_otomessage_request = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequest(
            detail=detail,
            biz_id='abc',
            account_id='123'
        )
        try:
            client.send_official_account_otomessage_with_options(send_official_account_otomessage_request, send_official_account_otomessage_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_official_account_otomessage_headers = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageHeaders()
        send_official_account_otomessage_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_message_body_image = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage(
            media_id='@rxxc'
        )
        detail_message_body_action_card_button_list_0 = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList(
            title='淘宝首页',
            action_url='https://www.taobao.com'
        )
        detail_message_body_action_card = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard(
            button_orientation='1',
            single_url='https://open.dingtalk.com',
            single_title='查看详情',
            markdown='支持markdown格式的正文内容',
            title='透出到会话列表和通知的文案',
            button_list=[
                detail_message_body_action_card_button_list_0
            ]
        )
        detail_message_body_link = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink(
            pic_url='@lADOADmaWMzazQKA',
            message_url='https://www.dingtalk.com/',
            title='link消息标题',
            text='link消息内容'
        )
        detail_message_body_markdown = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown(
            title='欢迎您关注服务窗',
            text='# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)'
        )
        detail_message_body_text = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBodyText(
            content='你好，服务窗。'
        )
        detail_message_body = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetailMessageBody(
            text=detail_message_body_text,
            markdown=detail_message_body_markdown,
            link=detail_message_body_link,
            action_card=detail_message_body_action_card,
            image=detail_message_body_image
        )
        detail = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequestDetail(
            msg_type='text',
            uuid='bdb81c6f-xxxx-xxxx-xxxx-6',
            user_id='idzb2eyxxxx',
            union_id='1234',
            message_body=detail_message_body
        )
        send_official_account_otomessage_request = dingtalkcrm__1__0_models.SendOfficialAccountOTOMessageRequest(
            detail=detail,
            biz_id='abc',
            account_id='123'
        )
        try:
            await client.send_official_account_otomessage_with_options_async(send_official_account_otomessage_request, send_official_account_otomessage_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody\image;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody\actionCard\buttonList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody\actionCard;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody\link;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody\markdown;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody\text;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail\messageBody;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest\detail;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountOTOMessageRequest;
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
        $sendOfficialAccountOTOMessageHeaders = new SendOfficialAccountOTOMessageHeaders([]);
        $sendOfficialAccountOTOMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $detailMessageBodyImage = new image([
            "mediaId" => "@rxxc"
        ]);
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
            "text" => "link消息内容"
        ]);
        $detailMessageBodyMarkdown = new markdown([
            "title" => "欢迎您关注服务窗",
            "text" => "# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"
        ]);
        $detailMessageBodyText = new text([
            "content" => "你好，服务窗。"
        ]);
        $detailMessageBody = new messageBody([
            "text" => $detailMessageBodyText,
            "markdown" => $detailMessageBodyMarkdown,
            "link" => $detailMessageBodyLink,
            "actionCard" => $detailMessageBodyActionCard,
            "image" => $detailMessageBodyImage
        ]);
        $detail = new detail([
            "msgType" => "text",
            "uuid" => "bdb81c6f-xxxx-xxxx-xxxx-6",
            "userId" => "idzb2eyxxxx",
            "unionId" => "1234",
            "messageBody" => $detailMessageBody
        ]);
        $sendOfficialAccountOTOMessageRequest = new SendOfficialAccountOTOMessageRequest([
            "detail" => $detail,
            "bizId" => "abc",
            "accountId" => "123"
        ]);
        try {
            $client->sendOfficialAccountOTOMessageWithOptions($sendOfficialAccountOTOMessageRequest, $sendOfficialAccountOTOMessageHeaders, new RuntimeOptions([]));
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

  sendOfficialAccountOTOMessageHeaders := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageHeaders{}
  sendOfficialAccountOTOMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  detailMessageBodyImage := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage{
    MediaId: tea.String("@rxxc"),
  }
  detailMessageBodyActionCardButtonList0 := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList{
    Title: tea.String("淘宝首页"),
    ActionUrl: tea.String("https://www.taobao.com"),
  }
  detailMessageBodyActionCard := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard{
    ButtonOrientation: tea.String("1"),
    SingleUrl: tea.String("https://open.dingtalk.com"),
    SingleTitle: tea.String("查看详情"),
    Markdown: tea.String("支持markdown格式的正文内容"),
    Title: tea.String("透出到会话列表和通知的文案"),
    ButtonList: []*dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList{detailMessageBodyActionCardButtonList0},
  }
  detailMessageBodyLink := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink{
    PicUrl: tea.String("@lADOADmaWMzazQKA"),
    MessageUrl: tea.String("https://www.dingtalk.com/"),
    Title: tea.String("link消息标题"),
    Text: tea.String("link消息内容"),
  }
  detailMessageBodyMarkdown := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown{
    Title: tea.String("欢迎您关注服务窗"),
    Text: tea.String("# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"),
  }
  detailMessageBodyText := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyText{
    Content: tea.String("你好，服务窗。"),
  }
  detailMessageBody := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBody{
    Text: detailMessageBodyText,
    Markdown: detailMessageBodyMarkdown,
    Link: detailMessageBodyLink,
    ActionCard: detailMessageBodyActionCard,
    Image: detailMessageBodyImage,
  }
  detail := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetail{
    MsgType: tea.String("text"),
    Uuid: tea.String("bdb81c6f-xxxx-xxxx-xxxx-6"),
    UserId: tea.String("idzb2eyxxxx"),
    UnionId: tea.String("1234"),
    MessageBody: detailMessageBody,
  }
  sendOfficialAccountOTOMessageRequest := &dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequest{
    Detail: detail,
    BizId: tea.String("abc"),
    AccountId: tea.String("123"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendOfficialAccountOTOMessageWithOptions(sendOfficialAccountOTOMessageRequest, sendOfficialAccountOTOMessageHeaders, &util.RuntimeOptions{})
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
    let sendOfficialAccountOTOMessageHeaders = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageHeaders({ });
    sendOfficialAccountOTOMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let detailMessageBodyImage = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage({
      mediaId: "@rxxc",
    });
    let detailMessageBodyActionCardButtonList0 = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList({
      title: "淘宝首页",
      actionUrl: "https://www.taobao.com",
    });
    let detailMessageBodyActionCard = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard({
      buttonOrientation: "1",
      singleUrl: "https://open.dingtalk.com",
      singleTitle: "查看详情",
      markdown: "支持markdown格式的正文内容",
      title: "透出到会话列表和通知的文案",
      buttonList: [
        detailMessageBodyActionCardButtonList0
      ],
    });
    let detailMessageBodyLink = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink({
      picUrl: "@lADOADmaWMzazQKA",
      messageUrl: "https://www.dingtalk.com/",
      title: "link消息标题",
      text: "link消息内容",
    });
    let detailMessageBodyMarkdown = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown({
      title: "欢迎您关注服务窗",
      text: "# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)",
    });
    let detailMessageBodyText = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBodyText({
      content: "你好，服务窗。",
    });
    let detailMessageBody = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetailMessageBody({
      text: detailMessageBodyText,
      markdown: detailMessageBodyMarkdown,
      link: detailMessageBodyLink,
      actionCard: detailMessageBodyActionCard,
      image: detailMessageBodyImage,
    });
    let detail = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequestDetail({
      msgType: "text",
      uuid: "bdb81c6f-xxxx-xxxx-xxxx-6",
      userId: "idzb2eyxxxx",
      unionId: "1234",
      messageBody: detailMessageBody,
    });
    let sendOfficialAccountOTOMessageRequest = new $dingtalkcrm_1_0.SendOfficialAccountOTOMessageRequest({
      detail: detail,
      bizId: "abc",
      accountId: "123",
    });
    try {
      await client.sendOfficialAccountOTOMessageWithOptions(sendOfficialAccountOTOMessageRequest, sendOfficialAccountOTOMessageHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageHeaders sendOfficialAccountOTOMessageHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageHeaders();
            sendOfficialAccountOTOMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage detailMessageBodyImage = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyImage
            {
                MediaId = "@rxxc",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList detailMessageBodyActionCardButtonList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList
            {
                Title = "淘宝首页",
                ActionUrl = "https://www.taobao.com",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard detailMessageBodyActionCard = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard
            {
                ButtonOrientation = "1",
                SingleUrl = "https://open.dingtalk.com",
                SingleTitle = "查看详情",
                Markdown = "支持markdown格式的正文内容",
                Title = "透出到会话列表和通知的文案",
                ButtonList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCard.SendOfficialAccountOTOMessageRequestDetailMessageBodyActionCardButtonList>
                {
                    detailMessageBodyActionCardButtonList0
                },
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink detailMessageBodyLink = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyLink
            {
                PicUrl = "@lADOADmaWMzazQKA",
                MessageUrl = "https://www.dingtalk.com/",
                Title = "link消息标题",
                Text = "link消息内容",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown detailMessageBodyMarkdown = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyMarkdown
            {
                Title = "欢迎您关注服务窗",
                Text = "# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyText detailMessageBodyText = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody.SendOfficialAccountOTOMessageRequestDetailMessageBodyText
            {
                Content = "你好，服务窗。",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody detailMessageBody = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail.SendOfficialAccountOTOMessageRequestDetailMessageBody
            {
                Text = detailMessageBodyText,
                Markdown = detailMessageBodyMarkdown,
                Link = detailMessageBodyLink,
                ActionCard = detailMessageBodyActionCard,
                Image = detailMessageBodyImage,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail detail = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest.SendOfficialAccountOTOMessageRequestDetail
            {
                MsgType = "text",
                Uuid = "bdb81c6f-xxxx-xxxx-xxxx-6",
                UserId = "idzb2eyxxxx",
                UnionId = "1234",
                MessageBody = detailMessageBody,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest sendOfficialAccountOTOMessageRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountOTOMessageRequest
            {
                Detail = detail,
                BizId = "abc",
                AccountId = "123",
            };
            try
            {
                client.SendOfficialAccountOTOMessageWithOptions(sendOfficialAccountOTOMessageRequest, sendOfficialAccountOTOMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求ID。 |
| result | Object | 返回结果。 |
| openPushId | String | 消息推送ID，长度不超过256位字符串，可用于消息发送进度排查。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "809773xxxx",
  "result" : {
    "openPushId" : "asxxxx"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | request.too.tast | request too fast. | 请求过快被限流。 |
| 400 | illegalParameter | Illegal parameter | 参数错误 |
| 400 | idempotentParameterMismatch.uuid | uuid not found. | uuid参数非法。 |
| 400 | illegalParameter.uuid | illegal uuid. | uuid参数非法。 |
| 400 | illegalParameter.messageContent | illegal message content. | 消息内容不合法。 |
| 400 | illegalParameter.messageBody | illegal message body. | 消息体不合法。 |
| 400 | illegalParameter.messageType | illegal message type. | 消息类型不合法。 |
| 400 | illegalParameter.messageReceiver | illegal message receiver. | 消息接收人不正确。 |
| 400 | illegalParameter.account | illegal account. | 服务窗账号异常。 |
| 400 | illegalRequest.overQuota | request over quota. | 请求超过配额。 |
| 500 | systemError | system error. | 系统异常。 |
