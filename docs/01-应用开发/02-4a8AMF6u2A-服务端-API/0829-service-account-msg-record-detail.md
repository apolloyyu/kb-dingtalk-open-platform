---
title: "查询群发消息详情"
source_url: "https://open.dingtalk.com/document/development/service-account-msg-record-detail"
namespace: "development"
slug: "service-account-msg-record-detail"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "专属钉钉 > 互动服务窗 > 消息群发 > 查询群发消息详情"
doc_id: "Ca3kQ6QT6y"
updated_at: "2026-06-02 19:13:04"
---

> Source: https://open.dingtalk.com/document/development/service-account-msg-record-detail
> Path: 应用开发 / 服务端 API / 专属钉钉 > 互动服务窗 > 消息群发 > 查询群发消息详情
> Updated: 2026-06-02 19:13:04

# 查询群发消息详情

调用本接口，查询指定推送号群发消息详情。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/follow/message/getMsgRecordDetail |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_message-企业内部服务号消息权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionid | String | 是 | 服务号的unionid。 |
| task\_id | String | 是 | 群发消息任务id，通过分页查询指定群发消息记录或者群发消息后获取到。 |

### 请求示例

HTTP

```
POST /v1.0/exclusive/follow/message/getMsgRecordDetail HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:tokenxxx
Content-Type:application/json

{
  "unionid" : "jYdrxxxxo0iE",
  "task_id" : "pushkxQxxxxwiEiE"
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.GetMsgRecordDetailHeaders getMsgRecordDetailHeaders = new com.aliyun.dingtalkexclusive_1_0.models.GetMsgRecordDetailHeaders();
        getMsgRecordDetailHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.GetMsgRecordDetailRequest getMsgRecordDetailRequest = new com.aliyun.dingtalkexclusive_1_0.models.GetMsgRecordDetailRequest()
                .setUnionid("jYdrxxxxo0iE")
                .setTaskId("pushkxQxxxxwiEiE");
        try {
            client.getMsgRecordDetailWithOptions(getMsgRecordDetailRequest, getMsgRecordDetailHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_msg_record_detail_headers = dingtalkexclusive__1__0_models.GetMsgRecordDetailHeaders()
        get_msg_record_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_msg_record_detail_request = dingtalkexclusive__1__0_models.GetMsgRecordDetailRequest(
            unionid='jYdrxxxxo0iE',
            task_id='pushkxQxxxxwiEiE'
        )
        try:
            client.get_msg_record_detail_with_options(get_msg_record_detail_request, get_msg_record_detail_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_msg_record_detail_headers = dingtalkexclusive__1__0_models.GetMsgRecordDetailHeaders()
        get_msg_record_detail_headers.x_acs_dingtalk_access_token = '<your access token>'
        get_msg_record_detail_request = dingtalkexclusive__1__0_models.GetMsgRecordDetailRequest(
            unionid='jYdrxxxxo0iE',
            task_id='pushkxQxxxxwiEiE'
        )
        try:
            await client.get_msg_record_detail_with_options_async(get_msg_record_detail_request, get_msg_record_detail_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetMsgRecordDetailHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\GetMsgRecordDetailRequest;
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
        $getMsgRecordDetailHeaders = new GetMsgRecordDetailHeaders([]);
        $getMsgRecordDetailHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $getMsgRecordDetailRequest = new GetMsgRecordDetailRequest([
            "unionid" => "jYdrxxxxo0iE",
            "taskId" => "pushkxQxxxxwiEiE"
        ]);
        try {
            $client->getMsgRecordDetailWithOptions($getMsgRecordDetailRequest, $getMsgRecordDetailHeaders, new RuntimeOptions([]));
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

  getMsgRecordDetailHeaders := &dingtalkexclusive_1_0.GetMsgRecordDetailHeaders{}
  getMsgRecordDetailHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  getMsgRecordDetailRequest := &dingtalkexclusive_1_0.GetMsgRecordDetailRequest{
    Unionid: tea.String("jYdrxxxxo0iE"),
    TaskId: tea.String("pushkxQxxxxwiEiE"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetMsgRecordDetailWithOptions(getMsgRecordDetailRequest, getMsgRecordDetailHeaders, &util.RuntimeOptions{})
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
    let getMsgRecordDetailHeaders = new dingtalkexclusive_1_0.GetMsgRecordDetailHeaders({ });
    getMsgRecordDetailHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let getMsgRecordDetailRequest = new dingtalkexclusive_1_0.GetMsgRecordDetailRequest({
      unionid: 'jYdrxxxxo0iE',
      taskId: 'pushkxQxxxxwiEiE',
    });
    try {
      await client.getMsgRecordDetailWithOptions(getMsgRecordDetailRequest, getMsgRecordDetailHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetMsgRecordDetailHeaders getMsgRecordDetailHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetMsgRecordDetailHeaders();
            getMsgRecordDetailHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetMsgRecordDetailRequest getMsgRecordDetailRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.GetMsgRecordDetailRequest
            {
                Unionid = "jYdrxxxxo0iE",
                TaskId = "pushkxQxxxxwiEiE",
            };
            try
            {
                client.GetMsgRecordDetailWithOptions(getMsgRecordDetailRequest, getMsgRecordDetailHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 消息详情。 |
| task\_id | String | 群发消息推送任务id。 |
| send\_time | Long | 消息发送时间。 |
| create\_time | Long | 群发消息任务创建时间。 |
| msg\_type | String | 消息类型，参考群发消息接口说明：   - **text**：文本类型 - **news\_card**：消息卡片 - **image**：图片类型 - **markdown**：markdown消息 - **action\_card**：action\_card卡片消息，支持动作行为 - **single\_news\_card**：新样式的消息卡片，只支持发送一个文章 |
| title | String | 消息标题。 |
| operator\_user\_id | String | 群发消息操作人员userId，只有在群发消息时传递操作人才会有次数据返回。 |
| is\_to\_all | Boolean | 是否全员发送。 |
| userid\_list | Array of String | 用户userId。 |
| dep\_id\_list | Array of String | 部门deptId。 |
| roleIdList | Array of String | 角色id。 |
| allow\_forward | Boolean | 是否允许转发标识。 |
| allow\_comment | Boolean | 是否允许评论。 |
| view\_scope\_type | String | 文章查看权限   - **0**：仅企业内可见 - **1**：所有人可见 |
| mediaId | String | 素材id，消息类型为图片/语音/视频时返回。 |
| textContent | String | 文本消息时的消息内容。 |
| articles | Array | 图文消息内容，当消息类型msg\_type为news\_card、single\_news\_card时，会返回对应的文章信息。 |
| article\_id | Long | 文章id。 |
| title | String | 标题。 |
| thumb\_media\_id | String | 封面图。 |
| publish\_status | Long | 发布状态：   - **0**：未发布 - **1**：已发布 |
| publish\_time | Long | 发布时间。 |
| create\_time | Long | 创建时间。 |
| update\_time | Long | 更新时间。 |
| content | String | 文章内容。 |
| url | String | 文章跳转链接。 |
| digest | String | 文章摘要。 |
| link | Object | 链接消息内容。 |
| title | String | 消息标题。 |
| summary | String | 消息描述。 |
| link\_url | String | 图文卡片消息点击后跳转的链接地址，支持设置多种链接打开方式。 |
| open\_type | Integer | 链接打开方式：   - **0**：端外浏览器打开 - **1**：端内浏览器打开 - **2**：端内侧边栏打开 |
| cover\_image\_media\_id | String | 图文卡片消息的封面素材id。 |
| markdown | Object | markdown消息内容。 |
| title | String | 消息标题，首屏会话透出的展示内容。 |
| text | String | markdown格式的消息。 |
| action\_card | Object | action\_card动作卡片消息内容。 |
| bnt\_orientation | String | 使用独立跳转ActionCard样式时的按钮排列方式：   - **0**：竖直排列 - **1**：竖直排列 |
| single\_url | String | 消息点击链接地址。 |
| single\_title | String | 使用整体跳转ActionCard样式时的标题。 |
| markdown | String | 消息内容，支持markdown。 |
| title | String | 透出到会话列表和通知的文案。 |
| button\_list | Array | 使用独立跳转ActionCard样式时的按钮列表。 |
| title | String | 使用独立跳转ActionCard样式时的按钮的标题。 |
| action\_url | String | 消息点击链接地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "errorcode" : "0",
  "errmsg" : "ok",
  "result" : {
    "task_id" : "pushkxQxxxxqkTjNdKLmwiEiE",
    "send_time" : 1766028831000,
    "create_time" : 1766028831000,
    "msg_type" : "text",
    "title" : "文本消息",
    "operator_user_id" : "2569131246",
    "is_to_all" : false,
    "userid_list" : [ "023453xxxx231" ],
    "dep_id_list" : [ "256913" ],
    "roleIdList" : [ "256913" ],
    "allow_forward" : false,
    "allow_comment" : false,
    "view_scope_type" : "1",
    "mediaId" : "@sdafgffxxxxx1123",
    "textContent" : "文本消息",
    "articles" : [ {
      "article_id" : 129003,
      "title" : "标题1",
      "thumb_media_id" : "@lALPBxxxxAlg",
      "publish_status" : 1,
      "publish_time" : 1442027997327,
      "create_time" : 1442027997327,
      "update_time" : 1442027997327,
      "content" : "",
      "url" : "https://contentcenter.dingtalk.com?articleId=17xx1",
      "digest" : "摘要1"
    } ],
    "link" : {
      "title" : "标题",
      "summary" : "摘要1",
      "link_url" : "https://contentcenter.dingtalk.com?articleId=17xxxx1",
      "open_type" : 0,
      "cover_image_media_id" : "@lALPBxxxxNAlg"
    },
    "markdown" : {
      "title" : "markdown_title",
      "text" : "markdown_text"
    },
    "action_card" : {
      "bnt_orientation" : "bnt_orientation",
      "single_url" : "single_url",
      "single_title" : "single_title",
      "markdown" : "markdown",
      "title" : "title",
      "button_list" : [ {
        "title" : "but_title",
        "action_url" : "but_url"
      } ]
    }
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | invalid.unionid | unionid非法 | unionid非法 |
| 400 | invalid.userid | 推送号非法 | 推送号非法 |
| 400 | invalid.taskid | taskId非法 | taskId非法 |
| 500 | system.error | 系统异常 | 系统异常 |
