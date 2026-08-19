---
title: "第三方个人应用发送服务窗单人消息"
source_url: "https://open.dingtalk.com/document/development/a-third-party-personal-application-sends-a-message-to-a-single"
namespace: "development"
slug: "a-third-party-personal-application-sends-a-message-to-a-single"
group: "应用开发"
tab: "服务端API"
breadcrumb: "更多开放 > 服务窗 > 第三方个人应用发送服务窗单人消息"
doc_id: "rH3in84zT7"
updated_at: "2025-09-11 21:03:51"
---

> Source: https://open.dingtalk.com/document/development/a-third-party-personal-application-sends-a-message-to-a-single
> Path: 应用开发 / 服务端API / 更多开放 > 服务窗 > 第三方个人应用发送服务窗单人消息
> Updated: 2025-09-11 21:03:51

# 第三方个人应用发送服务窗单人消息

面向第三方个人应用调用本接口向指定的用户发送服务窗消息。

## 接口调用说明

- 调用此接口前需要先通过授权组件获得用户`OfficialAccount.SnsMessage.Send`授权，获取授权code方式请参考[钉钉统一授权套件](0007-function-description.md)。
- 此接口一天最多允许调用次数等于服务窗粉丝数量。
- 每位粉丝用户一天最多允许接收三条来自服务窗的消息（包括服务窗后台群发、批量发送接口及单人消息接口）。
- 服务窗为减少内容相同消息对用户的打扰，默认场景下会对相同内容的消息推送会进行前去重处理，相同内容消息同一用户一天内仅会收到一条。
- 目前支持的消息格式有文本、链接、卡片、markdown等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/crm/officialAccounts/snsMessages/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方个人应用 |
| 权限要求 | permission-OfficialAccount.SnsMessage.Send-服务窗个人消息发送权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| detail | Object | 是 | 消息详情。 |
| msgType | String | 是 | 消息类型。 |
| uuid | String | 是 | 消息发送请求唯一ID，长度不超过128个字符。 |
| messageBody | Object | 是 | 消息体。 |
| text | Object | 否 | 文本消息内容。      如果消息类型为文本消息则此参数必填。 |
| content | String | 否 | 消息内容，建议500字符以内。 |
| markdown | Object | 否 | markdown消息，仅对消息类型为markdown时有效。 |
| title | String | 否 | 首屏会话透出的展示内容。 |
| text | String | 否 | markdown格式的消息，建议500字符以内。 |
| link | Object | 否 | 链接消息类型。 |
| picUrl | String | 否 | 图片地址。 |
| messageUrl | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接。 |
| title | String | 否 | 消息标题，建议100字符以内。 |
| text | String | 否 | 消息描述，建议500字符以内。 |
| actionCard | Object | 否 | 卡片消息。 |
| buttonOrientation | String | 否 | 按钮排列方式。   - **0**：竖直排列 - **1**：横向排列       必须与**buttonList**同时设置。 |
| singleUrl | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| singleTitle | String | 否 | 使用整体跳转ActionCard样式时的标题。      必须与**singleUrl**同时设置，最长20个字符。 |
| markdown | String | 否 | 消息内容，支持markdown。      语法参考标准markdown语法，1000个字符以内。 |
| title | String | 否 | 透出到会话列表和通知的文案。 |
| buttonList | Array | 否 | 使用独立跳转ActionCard样式时的按钮列表。      必须与**buttonOrientation**同时设置，且长度不超过1000字符。 |
| title | String | 否 | 使用独立跳转ActionCard样式时的按钮的标题，最长20个字符。 |
| actionUrl | String | 否 | 使用独立跳转ActionCard样式时的跳转链接。 |
| bizId | String | 否 | 可选参数，API调用方标识，仅用于定制调用方场景。      该参数需要线下对接，请线下联系对接的钉钉小二。 |
| bindingToken | String | 是 | 服务窗与第三方个人应用绑定时生成的授权码，可通过服务窗微应用-开放互联功能进行账号与第三方个人应用的绑定后获取。 |

### 请求示例

HTTP

```
POST /v1.0/crm/officialAccounts/snsMessages/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:3c890xxx
Content-Type:application/json

{
  "detail" : {
    "msgType" : "text",
    "uuid" : "bdb81c6f-xxxx-xxxx-xxxx-6",
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
      }
    }
  },
  "bizId" : "abc",
  "bindingToken" : "三方个人应用绑定服务窗的授权token"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkcrm_1_0.*;
import com.aliyun.dingtalkcrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkcrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkcrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkcrm_1_0.Client client = Sample.createClient();
        SendOfficialAccountSNSMessageHeaders sendOfficialAccountSNSMessageHeaders = new SendOfficialAccountSNSMessageHeaders();
        sendOfficialAccountSNSMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList detailMessageBodyActionCardButtonList0 = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList()
                .setTitle("淘宝首页")
                .setActionUrl("https://www.taobao.com");
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard detailMessageBodyActionCard = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard()
                .setButtonOrientation("1")
                .setSingleUrl("https://open.dingtalk.com")
                .setSingleTitle("查看详情")
                .setMarkdown("支持markdown格式的正文内容")
                .setTitle("透出到会话列表和通知的文案")
                .setButtonList(java.util.Arrays.asList(
                    detailMessageBodyActionCardButtonList0
                ));
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink detailMessageBodyLink = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink()
                .setPicUrl("@lADOADmaWMzazQKA")
                .setMessageUrl("https://www.dingtalk.com/")
                .setTitle("link消息标题")
                .setText("link消息内容");
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown detailMessageBodyMarkdown = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown()
                .setTitle("欢迎您关注服务窗")
                .setText("# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)");
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyText detailMessageBodyText = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBodyText()
                .setContent("你好，服务窗。");
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBody detailMessageBody = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetailMessageBody()
                .setText(detailMessageBodyText)
                .setMarkdown(detailMessageBodyMarkdown)
                .setLink(detailMessageBodyLink)
                .setActionCard(detailMessageBodyActionCard);
        SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail detail = new SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail()
                .setMsgType("text")
                .setUuid("bdb81c6f-xxxx-xxxx-xxxx-6")
                .setMessageBody(detailMessageBody);
        SendOfficialAccountSNSMessageRequest sendOfficialAccountSNSMessageRequest = new SendOfficialAccountSNSMessageRequest()
                .setDetail(detail)
                .setBizId("abc")
                .setBindingToken("三方个人应用绑定服务窗的授权token");
        try {
            client.sendOfficialAccountSNSMessageWithOptions(sendOfficialAccountSNSMessageRequest, sendOfficialAccountSNSMessageHeaders, new RuntimeOptions());
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
        send_official_account_snsmessage_headers = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageHeaders()
        send_official_account_snsmessage_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_message_body_action_card_button_list_0 = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList(
            title='淘宝首页',
            action_url='https://www.taobao.com'
        )
        detail_message_body_action_card = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard(
            button_orientation='1',
            single_url='https://open.dingtalk.com',
            single_title='查看详情',
            markdown='支持markdown格式的正文内容',
            title='透出到会话列表和通知的文案',
            button_list=[
                detail_message_body_action_card_button_list_0
            ]
        )
        detail_message_body_link = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink(
            pic_url='@lADOADmaWMzazQKA',
            message_url='https://www.dingtalk.com/',
            title='link消息标题',
            text='link消息内容'
        )
        detail_message_body_markdown = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown(
            title='欢迎您关注服务窗',
            text='# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)'
        )
        detail_message_body_text = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyText(
            content='你好，服务窗。'
        )
        detail_message_body = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBody(
            text=detail_message_body_text,
            markdown=detail_message_body_markdown,
            link=detail_message_body_link,
            action_card=detail_message_body_action_card
        )
        detail = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetail(
            msg_type='text',
            uuid='bdb81c6f-xxxx-xxxx-xxxx-6',
            message_body=detail_message_body
        )
        send_official_account_snsmessage_request = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequest(
            detail=detail,
            biz_id='abc',
            binding_token='三方个人应用绑定服务窗的授权token'
        )
        try:
            client.send_official_account_snsmessage_with_options(send_official_account_snsmessage_request, send_official_account_snsmessage_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_official_account_snsmessage_headers = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageHeaders()
        send_official_account_snsmessage_headers.x_acs_dingtalk_access_token = '<your access token>'
        detail_message_body_action_card_button_list_0 = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList(
            title='淘宝首页',
            action_url='https://www.taobao.com'
        )
        detail_message_body_action_card = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard(
            button_orientation='1',
            single_url='https://open.dingtalk.com',
            single_title='查看详情',
            markdown='支持markdown格式的正文内容',
            title='透出到会话列表和通知的文案',
            button_list=[
                detail_message_body_action_card_button_list_0
            ]
        )
        detail_message_body_link = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink(
            pic_url='@lADOADmaWMzazQKA',
            message_url='https://www.dingtalk.com/',
            title='link消息标题',
            text='link消息内容'
        )
        detail_message_body_markdown = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown(
            title='欢迎您关注服务窗',
            text='# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)'
        )
        detail_message_body_text = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBodyText(
            content='你好，服务窗。'
        )
        detail_message_body = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetailMessageBody(
            text=detail_message_body_text,
            markdown=detail_message_body_markdown,
            link=detail_message_body_link,
            action_card=detail_message_body_action_card
        )
        detail = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequestDetail(
            msg_type='text',
            uuid='bdb81c6f-xxxx-xxxx-xxxx-6',
            message_body=detail_message_body
        )
        send_official_account_snsmessage_request = dingtalkcrm__1__0_models.SendOfficialAccountSNSMessageRequest(
            detail=detail,
            biz_id='abc',
            binding_token='三方个人应用绑定服务窗的授权token'
        )
        try:
            await client.send_official_account_snsmessage_with_options_async(send_official_account_snsmessage_request, send_official_account_snsmessage_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail\messageBody\actionCard\buttonList;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail\messageBody\actionCard;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail\messageBody\link;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail\messageBody\markdown;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail\messageBody\text;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail\messageBody;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest\detail;
use AlibabaCloud\SDK\Dingtalk\Vcrm_1_0\Models\SendOfficialAccountSNSMessageRequest;
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
        $sendOfficialAccountSNSMessageHeaders = new SendOfficialAccountSNSMessageHeaders([]);
        $sendOfficialAccountSNSMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
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
            "actionCard" => $detailMessageBodyActionCard
        ]);
        $detail = new detail([
            "msgType" => "text",
            "uuid" => "bdb81c6f-xxxx-xxxx-xxxx-6",
            "messageBody" => $detailMessageBody
        ]);
        $sendOfficialAccountSNSMessageRequest = new SendOfficialAccountSNSMessageRequest([
            "detail" => $detail,
            "bizId" => "abc",
            "bindingToken" => "三方个人应用绑定服务窗的授权token"
        ]);
        try {
            $client->sendOfficialAccountSNSMessageWithOptions($sendOfficialAccountSNSMessageRequest, $sendOfficialAccountSNSMessageHeaders, new RuntimeOptions([]));
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
  util  "github.com/alibabacloud-go/tea-utils/service"
  dingtalkcrm_1_0  "github.com/alibabacloud-go/dingtalk/crm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
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

  sendOfficialAccountSNSMessageHeaders := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageHeaders{}
  sendOfficialAccountSNSMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  detailMessageBodyActionCardButtonList0 := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList{
    Title: tea.String("淘宝首页"),
    ActionUrl: tea.String("https://www.taobao.com"),
  }
  detailMessageBodyActionCard := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard{
    ButtonOrientation: tea.String("1"),
    SingleUrl: tea.String("https://open.dingtalk.com"),
    SingleTitle: tea.String("查看详情"),
    Markdown: tea.String("支持markdown格式的正文内容"),
    Title: tea.String("透出到会话列表和通知的文案"),
    ButtonList: []*dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList{detailMessageBodyActionCardButtonList0},
  }
  detailMessageBodyLink := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink{
    PicUrl: tea.String("@lADOADmaWMzazQKA"),
    MessageUrl: tea.String("https://www.dingtalk.com/"),
    Title: tea.String("link消息标题"),
    Text: tea.String("link消息内容"),
  }
  detailMessageBodyMarkdown := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown{
    Title: tea.String("欢迎您关注服务窗"),
    Text: tea.String("# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"),
  }
  detailMessageBodyText := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBodyText{
    Content: tea.String("你好，服务窗。"),
  }
  detailMessageBody := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetailMessageBody{
    Text: detailMessageBodyText,
    Markdown: detailMessageBodyMarkdown,
    Link: detailMessageBodyLink,
    ActionCard: detailMessageBodyActionCard,
  }
  detail := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequestDetail{
    MsgType: tea.String("text"),
    Uuid: tea.String("bdb81c6f-xxxx-xxxx-xxxx-6"),
    MessageBody: detailMessageBody,
  }
  sendOfficialAccountSNSMessageRequest := &dingtalkcrm_1_0.SendOfficialAccountSNSMessageRequest{
    Detail: detail,
    BizId: tea.String("abc"),
    BindingToken: tea.String("三方个人应用绑定服务窗的授权token"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendOfficialAccountSNSMessageWithOptions(sendOfficialAccountSNSMessageRequest, sendOfficialAccountSNSMessageHeaders, &util.RuntimeOptions{})
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
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageHeaders sendOfficialAccountSNSMessageHeaders = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageHeaders();
            sendOfficialAccountSNSMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList detailMessageBodyActionCardButtonList0 = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList
            {
                Title = "淘宝首页",
                ActionUrl = "https://www.taobao.com",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard detailMessageBodyActionCard = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard
            {
                ButtonOrientation = "1",
                SingleUrl = "https://open.dingtalk.com",
                SingleTitle = "查看详情",
                Markdown = "支持markdown格式的正文内容",
                Title = "透出到会话列表和通知的文案",
                ButtonList = new List<AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard.SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList>
                {
                    detailMessageBodyActionCardButtonList0
                },
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink detailMessageBodyLink = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyLink
            {
                PicUrl = "@lADOADmaWMzazQKA",
                MessageUrl = "https://www.dingtalk.com/",
                Title = "link消息标题",
                Text = "link消息内容",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown detailMessageBodyMarkdown = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown
            {
                Title = "欢迎您关注服务窗",
                Text = "# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyText detailMessageBodyText = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody.SendOfficialAccountSNSMessageRequestDetailMessageBodyText
            {
                Content = "你好，服务窗。",
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody detailMessageBody = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail.SendOfficialAccountSNSMessageRequestDetailMessageBody
            {
                Text = detailMessageBodyText,
                Markdown = detailMessageBodyMarkdown,
                Link = detailMessageBodyLink,
                ActionCard = detailMessageBodyActionCard,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail detail = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest.SendOfficialAccountSNSMessageRequestDetail
            {
                MsgType = "text",
                Uuid = "bdb81c6f-xxxx-xxxx-xxxx-6",
                MessageBody = detailMessageBody,
            };
            AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest sendOfficialAccountSNSMessageRequest = new AlibabaCloud.SDK.Dingtalkcrm_1_0.Models.SendOfficialAccountSNSMessageRequest
            {
                Detail = detail,
                BizId = "abc",
                BindingToken = "三方个人应用绑定服务窗的授权token",
            };
            try
            {
                client.SendOfficialAccountSNSMessageWithOptions(sendOfficialAccountSNSMessageRequest, sendOfficialAccountSNSMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

C++

```
// This file is auto-generated, don't edit it. Thanks.

#include <alibabacloud/dingtalkcrm__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkcrm_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkcrm_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::Client> client = make_shared<Alibabacloud_Dingtalkcrm_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageHeaders> sendOfficialAccountSNSMessageHeaders = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageHeaders>();
  sendOfficialAccountSNSMessageHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList> detailMessageBodyActionCardButtonList0 = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList>(map<string, boost::any>({
    {"title", boost::any(string("淘宝首页"))},
    {"actionUrl", boost::any(string("https://www.taobao.com"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard> detailMessageBodyActionCard = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCard>(map<string, boost::any>({
    {"buttonOrientation", boost::any(string("1"))},
    {"singleUrl", boost::any(string("https://open.dingtalk.com"))},
    {"singleTitle", boost::any(string("查看详情"))},
    {"markdown", boost::any(string("支持markdown格式的正文内容"))},
    {"title", boost::any(string("透出到会话列表和通知的文案"))},
    {"buttonList", boost::any(vector<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyActionCardButtonList>({
      detailMessageBodyActionCardButtonList0
    }))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyLink> detailMessageBodyLink = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyLink>(map<string, boost::any>({
    {"picUrl", boost::any(string("@lADOADmaWMzazQKA"))},
    {"messageUrl", boost::any(string("https://www.dingtalk.com/"))},
    {"title", boost::any(string("link消息标题"))},
    {"text", boost::any(string("link消息内容"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown> detailMessageBodyMarkdown = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyMarkdown>(map<string, boost::any>({
    {"title", boost::any(string("欢迎您关注服务窗"))},
    {"text", boost::any(string("# 这是支持markdown的文本 \n## 标题2 \n* 列表1 \n![alt 啊](https://img.alicdn.com/tps/TB1XLjqNVXXXXc4XVXXXXXXXXXX-170-64.png)"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyText> detailMessageBodyText = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBodyText>(map<string, boost::any>({
    {"content", boost::any(string("你好，服务窗。"))}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBody> detailMessageBody = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetailMessageBody>(map<string, boost::any>({
    {"text", !detailMessageBodyText ? boost::any() : boost::any(*detailMessageBodyText)},
    {"markdown", !detailMessageBodyMarkdown ? boost::any() : boost::any(*detailMessageBodyMarkdown)},
    {"link", !detailMessageBodyLink ? boost::any() : boost::any(*detailMessageBodyLink)},
    {"actionCard", !detailMessageBodyActionCard ? boost::any() : boost::any(*detailMessageBodyActionCard)}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetail> detail = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequestDetail>(map<string, boost::any>({
    {"msgType", boost::any(string("text"))},
    {"uuid", boost::any(string("bdb81c6f-xxxx-xxxx-xxxx-6"))},
    {"messageBody", !detailMessageBody ? boost::any() : boost::any(*detailMessageBody)}
  }));
  shared_ptr<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequest> sendOfficialAccountSNSMessageRequest = make_shared<Alibabacloud_Dingtalkcrm_1_0::SendOfficialAccountSNSMessageRequest>(map<string, boost::any>({
    {"detail", !detail ? boost::any() : boost::any(*detail)},
    {"bizId", boost::any(string("abc"))},
    {"bindingToken", boost::any(string("三方个人应用绑定服务窗的授权token"))}
  }));
  try {
    client->sendOfficialAccountSNSMessageWithOptions(sendOfficialAccountSNSMessageRequest, sendOfficialAccountSNSMessageHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
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
