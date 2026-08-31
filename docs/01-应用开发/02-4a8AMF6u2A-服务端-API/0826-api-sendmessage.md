---
title: "消息群发"
source_url: "https://open.dingtalk.com/document/development/api-sendmessage"
namespace: "development"
slug: "api-sendmessage"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 消息群发 > 消息群发"
doc_id: "xlEvnGhHPD"
updated_at: "2026-06-04 19:09:55"
---

> Source: https://open.dingtalk.com/document/development/api-sendmessage
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 消息群发 > 消息群发
> Updated: 2026-06-04 19:09:55

# 消息群发

调用本接口群发消息。

## 接口调用说明

- 使用dep\_id\_list或is\_to\_all方式做大规模人群推送时，选中人数上限为10万人。如果超过此上限，群发失败，群发任务不会执行。
- 在多人推送的情况下，同一天只会收到一条相同的内容（消息去重机制）。单人定向推送（只填一个userid）时，没有此保护机制，注意避免重复推送。
- 出于系统保护的考虑，我们对接口的调用做了频率限制，详情请参考调用[频率限制](0012-call-frequency-limit.md)。
- 接口调用成功，不代表所有接收人立马收到消息，根据系统拥堵情况收到时间会有延迟。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/follow/message/send |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_message-企业内部服务号消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，企业内部应用调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionid | String | 否 | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |
| is\_to\_all | Boolean | 否 | 是否群发给组织下所有人：   - **true**：是 - **false**：否 |
| msg\_type | String | 否 | msg\_type, 消息类型，支持如下消息类型：   - **text**：文本类型，此时文本内容填在text\_content字段中 - **news\_card**：消息卡片，可以通过[查询图文卡片列表接口](0824-query-message-card-list.md)获取media\_id - **image**：图片类型，图片类型，可以通过[上传媒体文件](0646-upload-media-files.md)接口获得media\_id - **markdown**：markdown消息，需要设置msg\_body中markdown对象的相关参数 - **single\_news\_card**：新样式的消息卡片，可以通过[查询图文卡片列表接口](0824-query-message-card-list.md)获取media\_id，只支持发送一个文章 - **link**：链接消息，以新样式的消息卡片发送，卡片点击后跳转到指定链接，需要设置msg\_body中link对象的相关参数       当你使用 markdown 或 action\_card 类型时，推荐图片比例为 16:9。如果不使用该比例，则图片可能显示不完整。 |
| uuid | String | 否 | 调用时填写随机生成的UUID，防止消息重复发送。 |
| text\_content | String | 否 | 文本内容，当msg\_type为text时有效。 |
| is\_preview | Boolean | 否 | 是否预览推送，预览推送只会发给单个用户，并且内容链接24小时后可能会失效。      取值为true时，userid\_list不能为空。 |
| media\_id | String | 否 | 消息卡片素材id。      当参数msg\_type为news\_card、image、single\_news\_card时，该参数为必填项。 |
| userid\_list | Array of String | 否 | 用户userId。 |
| dep\_id\_list | Array of Long | 否 | 部门deptId。 |
| roleIds | Array of Long | 否 | 角色id。 |
| msg\_body | Object | 否 | 消息体。       - 当msg\_type设置为markdown时，必须传入markdown对象的相关参数 - 当msg\_type设置为action\_card时，必须传入action\_card对象的相关参数 - 当msg\_type设置为link时，必须传入link对象的相关参数 |
| markdown | Object | 否 | markdown消息。      当msg\_type设置为markdown时，该字段为必填项。 |
| text | String | 否 | markdown格式的消息，建议5000字符以内。 |
| title | String | 否 | 首屏会话透出的展示内容。 |
| action\_card | Object | 否 | action\_card卡片消息。 |
| btn\_orientation | String | 否 | 使用独立跳转ActionCard样式时的按钮排列方式：   - **0**：竖直排列 - **1**：横向排列 |
| single\_title | String | 否 | 使用整体跳转ActionCard样式时的标题，最长20个字符。      必须与single\_url同时设置。 |
| markdown | String | 否 | 消息内容，支持markdown，语法请参考markdown消息。建议1000个字符以内。 |
| button\_list | Array | 否 | 使用独立跳转ActionCard样式时的按钮列表。      必须与btn\_orientation同时设置。 |
| title | String | 否 | 按钮名称。 |
| action\_url | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| single\_url | String | 否 | 消息点击链接地址，当发送消息为小程序时支持小程序跳转链接，最长500个字符。 |
| title | String | 否 | 透出到会话列表和通知的文案，最长64个字符。 |
| link | Object | 否 | 链接消息。推送图文卡片消息，点击后跳转到指定链接。 |
| cover\_image\_media\_id | String | 否 | 图文卡片消息的封面素材id,可以通过上传媒体文件接口上传图片获取mediaId。 |
| link\_url | String | 否 | 图文卡片消息点击后跳转的链接地址，支持设置多种链接打开方式。 |
| title | String | 否 | 图文卡片中显示的主文案信息，并且会透出到会话列表和通知的文案，最长64个字符。 |
| summary | String | 否 | 图文卡片上显示的摘要信息，可为空。 |
| open\_type | Integer | 否 | 链接打开方式，支持以下方式打开：   - **0**：端外浏览器打开 - **1**：端内工作台打开 - **2**：端内侧边栏打开 |
| allow\_comment | Boolean | 否 | 是否允许评论，仅在msg\_type取值为`news_card`和`single_news_card`时有效。   - **true**：允许评论 - **false**：禁止评论 |
| comment\_type | Integer | 否 | 评论展示类型 ：   - **0**：普通评论 - **1**：精选评论 |
| show\_homepage | Integer | 否 | 消息是否在主页展示，仅在msg\_type取值为`news_card`或`single_news_card` 有效。   - **0**：不展示 - **1**：展示 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/follow/message/send HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:tokenxxxxx
Content-Type:application/json

{
  "unionid" : "jYdrxxxxiE",
  "is_to_all" : false,
  "msg_type" : "text",
  "uuid" : "48566508-3f35",
  "text_content" : "hello",
  "is_preview" : false,
  "media_id" : "P16xzxxX8iE",
  "userid_list" : [ "user1" ],
  "dep_id_list" : [ 34243 ],
  "roleIds" : [ 23421 ],
  "msg_body" : {
    "markdown" : {
      "text" : "markdown text",
      "title" : "title"
    },
    "action_card" : {
      "btn_orientation" : "0",
      "single_title" : "single title",
      "markdown" : "markdown text",
      "button_list" : [ {
        "title" : "btn_title1",
        "action_url" : "btn_action_url1"
      } ],
      "single_url" : "https://dingtalk.com",
      "title" : "title"
    },
    "link" : {
      "cover_image_media_id" : "P16xxxx8iE",
      "link_url" : "https://dingtalk.com",
      "title" : "title",
      "summary" : "描述信息",
      "open_type" : 0
    }
  },
  "allow_comment" : false,
  "comment_type" : 1,
  "show_homepage" : 0
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageHeaders sendMessageHeaders = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageHeaders();
        sendMessageHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyLink msgBodyLink = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyLink()
                .setCoverImageMediaId("P16xxxx8iE")
                .setLinkUrl("https://dingtalk.com")
                .setTitle("title")
                .setSummary("描述信息")
                .setOpenType(0);
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyActionCardButtonList msgBodyActionCardButtonList0 = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyActionCardButtonList()
                .setTitle("btn_title1")
                .setActionUrl("btn_action_url1");
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyActionCard msgBodyActionCard = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyActionCard()
                .setBtnOrientation("0")
                .setSingleTitle("single title")
                .setMarkdown("markdown text")
                .setButtonList(java.util.Arrays.asList(
                    msgBodyActionCardButtonList0
                ))
                .setSingleUrl("https://dingtalk.com")
                .setTitle("title");
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyMarkdown msgBodyMarkdown = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBodyMarkdown()
                .setText("markdown text")
                .setTitle("title");
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBody msgBody = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest.SendMessageRequestMsgBody()
                .setMarkdown(msgBodyMarkdown)
                .setActionCard(msgBodyActionCard)
                .setLink(msgBodyLink);
        com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest sendMessageRequest = new com.aliyun.dingtalkexclusive_1_0.models.SendMessageRequest()
                .setUnionid("jYdrxxxxiE")
                .setIsToAll(false)
                .setMsgType("text")
                .setUuid("48566508-3f35")
                .setTextContent("hello")
                .setIsPreview(false)
                .setMediaId("P16xzxxX8iE")
                .setUseridList(java.util.Arrays.asList(
                    "user1"
                ))
                .setDepIdList(java.util.Arrays.asList(
                    34243L
                ))
                .setRoleIds(java.util.Arrays.asList(
                    23421L
                ))
                .setMsgBody(msgBody)
                .setAllowComment(false)
                .setCommentType(1)
                .setShowHomepage(0);
        try {
            client.sendMessageWithOptions(sendMessageRequest, sendMessageHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_message_headers = dingtalkexclusive__1__0_models.SendMessageHeaders()
        send_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        msg_body_link = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyLink(
            cover_image_media_id='P16xxxx8iE',
            link_url='https://dingtalk.com',
            title='title',
            summary='描述信息',
            open_type=0
        )
        msg_body_action_card_button_list_0 = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyActionCardButtonList(
            title='btn_title1',
            action_url='btn_action_url1'
        )
        msg_body_action_card = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyActionCard(
            btn_orientation='0',
            single_title='single title',
            markdown='markdown text',
            button_list=[
                msg_body_action_card_button_list_0
            ],
            single_url='https://dingtalk.com',
            title='title'
        )
        msg_body_markdown = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyMarkdown(
            text='markdown text',
            title='title'
        )
        msg_body = dingtalkexclusive__1__0_models.SendMessageRequestMsgBody(
            markdown=msg_body_markdown,
            action_card=msg_body_action_card,
            link=msg_body_link
        )
        send_message_request = dingtalkexclusive__1__0_models.SendMessageRequest(
            unionid='jYdrxxxxiE',
            is_to_all=False,
            msg_type='text',
            uuid='48566508-3f35',
            text_content='hello',
            is_preview=False,
            media_id='P16xzxxX8iE',
            userid_list=[
                'user1'
            ],
            dep_id_list=[
                34243
            ],
            role_ids=[
                23421
            ],
            msg_body=msg_body,
            allow_comment=False,
            comment_type=1,
            show_homepage=0
        )
        try:
            client.send_message_with_options(send_message_request, send_message_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_message_headers = dingtalkexclusive__1__0_models.SendMessageHeaders()
        send_message_headers.x_acs_dingtalk_access_token = '<your access token>'
        msg_body_link = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyLink(
            cover_image_media_id='P16xxxx8iE',
            link_url='https://dingtalk.com',
            title='title',
            summary='描述信息',
            open_type=0
        )
        msg_body_action_card_button_list_0 = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyActionCardButtonList(
            title='btn_title1',
            action_url='btn_action_url1'
        )
        msg_body_action_card = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyActionCard(
            btn_orientation='0',
            single_title='single title',
            markdown='markdown text',
            button_list=[
                msg_body_action_card_button_list_0
            ],
            single_url='https://dingtalk.com',
            title='title'
        )
        msg_body_markdown = dingtalkexclusive__1__0_models.SendMessageRequestMsgBodyMarkdown(
            text='markdown text',
            title='title'
        )
        msg_body = dingtalkexclusive__1__0_models.SendMessageRequestMsgBody(
            markdown=msg_body_markdown,
            action_card=msg_body_action_card,
            link=msg_body_link
        )
        send_message_request = dingtalkexclusive__1__0_models.SendMessageRequest(
            unionid='jYdrxxxxiE',
            is_to_all=False,
            msg_type='text',
            uuid='48566508-3f35',
            text_content='hello',
            is_preview=False,
            media_id='P16xzxxX8iE',
            userid_list=[
                'user1'
            ],
            dep_id_list=[
                34243
            ],
            role_ids=[
                23421
            ],
            msg_body=msg_body,
            allow_comment=False,
            comment_type=1,
            show_homepage=0
        )
        try:
            await client.send_message_with_options_async(send_message_request, send_message_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageRequest\msgBody\link;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageRequest\msgBody\actionCard\buttonList;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageRequest\msgBody\actionCard;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageRequest\msgBody\markdown;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageRequest\msgBody;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\SendMessageRequest;
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
        $sendMessageHeaders = new SendMessageHeaders([]);
        $sendMessageHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $msgBodyLink = new link([
            "coverImageMediaId" => "P16xxxx8iE",
            "linkUrl" => "https://dingtalk.com",
            "title" => "title",
            "summary" => "描述信息",
            "openType" => 0
        ]);
        $msgBodyActionCardButtonList0 = new buttonList([
            "title" => "btn_title1",
            "actionUrl" => "btn_action_url1"
        ]);
        $msgBodyActionCard = new actionCard([
            "btnOrientation" => "0",
            "singleTitle" => "single title",
            "markdown" => "markdown text",
            "buttonList" => [
                $msgBodyActionCardButtonList0
            ],
            "singleUrl" => "https://dingtalk.com",
            "title" => "title"
        ]);
        $msgBodyMarkdown = new markdown([
            "text" => "markdown text",
            "title" => "title"
        ]);
        $msgBody = new msgBody([
            "markdown" => $msgBodyMarkdown,
            "actionCard" => $msgBodyActionCard,
            "link" => $msgBodyLink
        ]);
        $sendMessageRequest = new SendMessageRequest([
            "unionid" => "jYdrxxxxiE",
            "isToAll" => false,
            "msgType" => "text",
            "uuid" => "48566508-3f35",
            "textContent" => "hello",
            "isPreview" => false,
            "mediaId" => "P16xzxxX8iE",
            "useridList" => [
                "user1"
            ],
            "depIdList" => [
                34243
            ],
            "roleIds" => [
                23421
            ],
            "msgBody" => $msgBody,
            "allowComment" => false,
            "commentType" => 1,
            "showHomepage" => 0
        ]);
        try {
            $client->sendMessageWithOptions($sendMessageRequest, $sendMessageHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
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
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  sendMessageHeaders := &dingtalkexclusive_1_0.SendMessageHeaders{}
  sendMessageHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  msgBodyLink := &dingtalkexclusive_1_0.SendMessageRequestMsgBodyLink{
    CoverImageMediaId: tea.String("P16xxxx8iE"),
    LinkUrl: tea.String("https://dingtalk.com"),
    Title: tea.String("title"),
    Summary: tea.String("描述信息"),
    OpenType: tea.Int32(0),
  }
  msgBodyActionCardButtonList0 := &dingtalkexclusive_1_0.SendMessageRequestMsgBodyActionCardButtonList{
    Title: tea.String("btn_title1"),
    ActionUrl: tea.String("btn_action_url1"),
  }
  msgBodyActionCard := &dingtalkexclusive_1_0.SendMessageRequestMsgBodyActionCard{
    BtnOrientation: tea.String("0"),
    SingleTitle: tea.String("single title"),
    Markdown: tea.String("markdown text"),
    ButtonList: []*dingtalkexclusive_1_0.SendMessageRequestMsgBodyActionCardButtonList{msgBodyActionCardButtonList0},
    SingleUrl: tea.String("https://dingtalk.com"),
    Title: tea.String("title"),
  }
  msgBodyMarkdown := &dingtalkexclusive_1_0.SendMessageRequestMsgBodyMarkdown{
    Text: tea.String("markdown text"),
    Title: tea.String("title"),
  }
  msgBody := &dingtalkexclusive_1_0.SendMessageRequestMsgBody{
    Markdown: msgBodyMarkdown,
    ActionCard: msgBodyActionCard,
    Link: msgBodyLink,
  }
  sendMessageRequest := &dingtalkexclusive_1_0.SendMessageRequest{
    Unionid: tea.String("jYdrxxxxiE"),
    IsToAll: tea.Bool(false),
    MsgType: tea.String("text"),
    Uuid: tea.String("48566508-3f35"),
    TextContent: tea.String("hello"),
    IsPreview: tea.Bool(false),
    MediaId: tea.String("P16xzxxX8iE"),
    UseridList: []*string{tea.String("user1")},
    DepIdList: []*int64{tea.Int64(34243)},
    RoleIds: []*int64{tea.Int64(23421)},
    MsgBody: msgBody,
    AllowComment: tea.Bool(false),
    CommentType: tea.Int32(1),
    ShowHomepage: tea.Int32(0),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SendMessageWithOptions(sendMessageRequest, sendMessageHeaders, &util.RuntimeOptions{})
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
const dingtalkexclusive_1_0 = require('@alicloud/dingtalk/exclusive_1_0');
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
    return new dingtalkexclusive_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let sendMessageHeaders = new dingtalkexclusive_1_0.SendMessageHeaders({ });
    sendMessageHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let msgBodyLink = new dingtalkexclusive_1_0.SendMessageRequestMsgBodyLink({
      coverImageMediaId: 'P16xxxx8iE',
      linkUrl: 'https://dingtalk.com',
      title: 'title',
      summary: '描述信息',
      openType: 0,
    });
    let msgBodyActionCardButtonList0 = new dingtalkexclusive_1_0.SendMessageRequestMsgBodyActionCardButtonList({
      title: 'btn_title1',
      actionUrl: 'btn_action_url1',
    });
    let msgBodyActionCard = new dingtalkexclusive_1_0.SendMessageRequestMsgBodyActionCard({
      btnOrientation: '0',
      singleTitle: 'single title',
      markdown: 'markdown text',
      buttonList: [
        msgBodyActionCardButtonList0
      ],
      singleUrl: 'https://dingtalk.com',
      title: 'title',
    });
    let msgBodyMarkdown = new dingtalkexclusive_1_0.SendMessageRequestMsgBodyMarkdown({
      text: 'markdown text',
      title: 'title',
    });
    let msgBody = new dingtalkexclusive_1_0.SendMessageRequestMsgBody({
      markdown: msgBodyMarkdown,
      actionCard: msgBodyActionCard,
      link: msgBodyLink,
    });
    let sendMessageRequest = new dingtalkexclusive_1_0.SendMessageRequest({
      unionid: 'jYdrxxxxiE',
      isToAll: false,
      msgType: 'text',
      uuid: '48566508-3f35',
      textContent: 'hello',
      isPreview: false,
      mediaId: 'P16xzxxX8iE',
      useridList: [
        'user1'
      ],
      depIdList: [
        34243
      ],
      roleIds: [
        23421
      ],
      msgBody: msgBody,
      allowComment: false,
      commentType: 1,
      showHomepage: 0,
    });
    try {
      await client.sendMessageWithOptions(sendMessageRequest, sendMessageHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageHeaders sendMessageHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageHeaders();
            sendMessageHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyLink msgBodyLink = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyLink
            {
                CoverImageMediaId = "P16xxxx8iE",
                LinkUrl = "https://dingtalk.com",
                Title = "title",
                Summary = "描述信息",
                OpenType = 0,
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyActionCard.SendMessageRequestMsgBodyActionCardButtonList msgBodyActionCardButtonList0 = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyActionCard.SendMessageRequestMsgBodyActionCardButtonList
            {
                Title = "btn_title1",
                ActionUrl = "btn_action_url1",
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyActionCard msgBodyActionCard = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyActionCard
            {
                BtnOrientation = "0",
                SingleTitle = "single title",
                Markdown = "markdown text",
                ButtonList = new List<AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyActionCard.SendMessageRequestMsgBodyActionCardButtonList>
                {
                    msgBodyActionCardButtonList0
                },
                SingleUrl = "https://dingtalk.com",
                Title = "title",
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyMarkdown msgBodyMarkdown = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody.SendMessageRequestMsgBodyMarkdown
            {
                Text = "markdown text",
                Title = "title",
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody msgBody = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest.SendMessageRequestMsgBody
            {
                Markdown = msgBodyMarkdown,
                ActionCard = msgBodyActionCard,
                Link = msgBodyLink,
            };
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest sendMessageRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.SendMessageRequest
            {
                Unionid = "jYdrxxxxiE",
                IsToAll = false,
                MsgType = "text",
                Uuid = "48566508-3f35",
                TextContent = "hello",
                IsPreview = false,
                MediaId = "P16xzxxX8iE",
                UseridList = new List<string>
                {
                    "user1"
                },
                DepIdList = new List<long?>
                {
                    34243
                },
                RoleIds = new List<long?>
                {
                    23421
                },
                MsgBody = msgBody,
                AllowComment = false,
                CommentType = 1,
                ShowHomepage = 0,
            };
            try
            {
                client.SendMessageWithOptions(sendMessageRequest, sendMessageHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| errorcode | String | 返回码。 |
| errmsg | String | 返回码描述。 |
| task\_id | String | 推送任务id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "errorcode" : "0",
  "errmsg" : "success",
  "task_id" : "taskIddsawwwcsa"
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.unionid | unionid非法 | unionid非法 |
| 400 | invalid.userid.list | userId列表非法 | userId列表非法 |
| 400 | receivers.list.empty | 接收人列表为空 | 接收人列表为空 |
| 400 | message.not.empty | 指定消息内容不能为空 | 指定消息内容不能为空 |
| 400 | invalid.media.id | media\_id非法 | media\_id非法 |
| 400 | link.params.missing | 链接消息参数缺失 | 链接消息参数缺失 |
| 400 | uuid.repeat | uuid重复 | uuid重复 |
| 500 | system.error | 系统异常 | 系统异常 |
