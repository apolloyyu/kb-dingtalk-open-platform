---
title: "创建待办卡片类型配置"
source_url: "https://open.dingtalk.com/document/development/add-todo-cardtype-configuration"
namespace: "development"
slug: "add-todo-cardtype-configuration"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 创建待办卡片类型配置"
doc_id: "ta3QRjmDFp"
updated_at: "2026-07-30 10:01:52"
---

> Source: https://open.dingtalk.com/document/development/add-todo-cardtype-configuration
> Path: 应用开发 / 服务端 API / 待办任务 > 创建待办卡片类型配置
> Updated: 2026-07-30 10:01:52

# 创建待办卡片类型配置

调用本接口可以为自己业务新增一个待办卡片类型，支持业务自定义待办列表中的卡片展示样式，包含卡片icon、表单内容、操作按钮等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/configs/types |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Todo.Todo.Write-待办应用中待办写权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过 [获取用户token](0032-obtain-user-token.md)接口获取。 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户的unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 否 | 当前操作者unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cardType | Integer | 是 | 卡片类型，取值。   - **1**：标准卡片 - **2**：自定义卡片 |
| icon | String | 是 | 卡片类型图标，用于在待办列表展示。  图片资源的mediaId可通过[上传媒体文件](0646-upload-media-files.md)接口获取。  **[!NOTE]**    图标要求如下：   - 尺寸：24px \* 24px - 圆角：6px - 大小：小于500k |
| description | String | 否 | 待办卡片类型描述。 |
| pcDetailUrlOpenMode | String | 是 | 详情页链接在PC端的打开方式，取值。   - **PC\_SLIDE**：PC端侧边栏打开 - **PC\_BROWSER**：浏览器打开 |
| contentFieldList | Array | 否 | 内容区表单自定义字段配置。 |
| fieldKey | String | 否 | 字段的唯一标识 |
| fieldType | String | 否 | 字段类型，当前仅支持文本类型**text**。 |
| nameI18n | Map | 否 | 字段显示名称。  需支持zh\_CN、zh\_TW、zh\_HK、en\_US、vi\_VN、ja\_JP等语言国际化。  示例值如下：   ``` {   "nameI18n": {   "zh_CN": "老师",   "zh_TW": "老師",   "zh_HK": "老師",   "en_US": "Teacher",   "vi_VN": "Giáo viên",   "ja_JP": "先生"   } } ``` |
| actionList | Array | 否 | 待办卡片操作区按钮配置。 |
| actionKey | String | 否 | 操作按钮的唯一标识。 |
| buttonStyleType | Integer | 否 | 按钮样式类型，取值。   - **101**：蓝色线型主按钮样式 - **102**：黑色线型副按钮样式 |
| actionType | Integer | 否 | 按钮类型，当前仅支持**直接跳转**取值为**2**。 |
| url | String | 否 | 按钮对应的URL。例如：`https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}`。  **[!NOTE]**     - 当用户点击按钮时，钉钉会向此链接发送请求，并携带**sourceId**、**actionKey**和**from来源**等关键信息。 - 如果需要完成待办，则需要返回以下信息给钉钉：     ```   {   "code": 200,   "message": "OK",   "success": true   }   ``` |
| nameI18n | Map | 否 | 按钮显示名称。  需支持zh\_CN、zh\_TW、zh\_HK、en\_US、vi\_VN、ja\_JP等语言国际化。  示例值如下：   ``` {     "nameI18n": {         "zh_CN": "同意",         "zh_TW": "同意",         "zh_HK": "同意",         "en_US": "Approve",         "vi_VN": "Approve",         "ja_JP": "Approve"     } } ``` |

### **请求示例**

HTTP

```
POST /v1.0/todo/users/PUoiinxxxx/configs/types?operatorId=PUoiinxxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b3ba046cxxxx
Content-Type:application/json

{
  "cardType" : 2,
  "icon" : "https://img.alicdn.com/xxx.png",
  "description" : "应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
  "pcDetailUrlOpenMode" : "PC_SLIDE",
  "contentFieldList" : [ {
    "fieldKey" : "teacher",
    "fieldType" : "text"
  } ],
  "actionList" : [ {
    "actionKey" : "approve",
    "buttonStyleType" : 101,
    "actionType" : 2,
    "url" : "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}"
  } ]
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalktodo_1_0.*;
import com.aliyun.dingtalktodo_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalktodo_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktodo_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalktodo_1_0.Client client = Sample.createClient();
        CreateTodoTypeConfigHeaders createTodoTypeConfigHeaders = new CreateTodoTypeConfigHeaders();
        createTodoTypeConfigHeaders.xAcsDingtalkAccessToken = "<your access token>";
        CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestActionList actionList0 = new CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestActionList()
                .setActionKey("approve")
                .setButtonStyleType(101)
                .setActionType(2)
                .setUrl("https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}");
        CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestContentFieldList contentFieldList0 = new CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestContentFieldList()
                .setFieldKey("teacher")
                .setFieldType("text");
        CreateTodoTypeConfigRequest createTodoTypeConfigRequest = new CreateTodoTypeConfigRequest()
                .setCardType(2)
                .setIcon("https://img.alicdn.com/xxx.png")
                .setDescription("应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。")
                .setPcDetailUrlOpenMode("PC_SLIDE")
                .setContentFieldList(java.util.Arrays.asList(
                    contentFieldList0
                ))
                .setActionList(java.util.Arrays.asList(
                    actionList0
                ));
        try {
            client.createTodoTypeConfigWithOptions("PUoiinxxxx", createTodoTypeConfigRequest, createTodoTypeConfigHeaders, new RuntimeOptions());
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
        create_todo_type_config_headers = dingtalktodo__1__0_models.CreateTodoTypeConfigHeaders()
        create_todo_type_config_headers.x_acs_dingtalk_access_token = '<your access token>'
        action_list_0 = dingtalktodo__1__0_models.CreateTodoTypeConfigRequestActionList(
            action_key='approve',
            button_style_type=101,
            action_type=2,
            url='https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}'
        )
        content_field_list_0 = dingtalktodo__1__0_models.CreateTodoTypeConfigRequestContentFieldList(
            field_key='teacher',
            field_type='text'
        )
        create_todo_type_config_request = dingtalktodo__1__0_models.CreateTodoTypeConfigRequest(
            card_type=2,
            icon='https://img.alicdn.com/xxx.png',
            description='应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。',
            pc_detail_url_open_mode='PC_SLIDE',
            content_field_list=[
                content_field_list_0
            ],
            action_list=[
                action_list_0
            ]
        )
        try:
            client.create_todo_type_config_with_options('PUoiinxxxx', create_todo_type_config_request, create_todo_type_config_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_todo_type_config_headers = dingtalktodo__1__0_models.CreateTodoTypeConfigHeaders()
        create_todo_type_config_headers.x_acs_dingtalk_access_token = '<your access token>'
        action_list_0 = dingtalktodo__1__0_models.CreateTodoTypeConfigRequestActionList(
            action_key='approve',
            button_style_type=101,
            action_type=2,
            url='https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}'
        )
        content_field_list_0 = dingtalktodo__1__0_models.CreateTodoTypeConfigRequestContentFieldList(
            field_key='teacher',
            field_type='text'
        )
        create_todo_type_config_request = dingtalktodo__1__0_models.CreateTodoTypeConfigRequest(
            card_type=2,
            icon='https://img.alicdn.com/xxx.png',
            description='应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。',
            pc_detail_url_open_mode='PC_SLIDE',
            content_field_list=[
                content_field_list_0
            ],
            action_list=[
                action_list_0
            ]
        )
        try:
            await client.create_todo_type_config_with_options_async('PUoiinxxxx', create_todo_type_config_request, create_todo_type_config_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTypeConfigHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTypeConfigRequest\actionList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTypeConfigRequest\contentFieldList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\CreateTodoTypeConfigRequest;
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
        $createTodoTypeConfigHeaders = new CreateTodoTypeConfigHeaders([]);
        $createTodoTypeConfigHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $actionList0 = new actionList([
            "actionKey" => "approve",
            "buttonStyleType" => 101,
            "actionType" => 2,
            "url" => "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}"
        ]);
        $contentFieldList0 = new contentFieldList([
            "fieldKey" => "teacher",
            "fieldType" => "text"
        ]);
        $createTodoTypeConfigRequest = new CreateTodoTypeConfigRequest([
            "cardType" => 2,
            "icon" => "https://img.alicdn.com/xxx.png",
            "description" => "应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
            "pcDetailUrlOpenMode" => "PC_SLIDE",
            "contentFieldList" => [
                $contentFieldList0
            ],
            "actionList" => [
                $actionList0
            ]
        ]);
        try {
            $client->createTodoTypeConfigWithOptions("PUoiinxxxx", $createTodoTypeConfigRequest, $createTodoTypeConfigHeaders, new RuntimeOptions([]));
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
  dingtalktodo_1_0  "github.com/alibabacloud-go/dingtalk/todo_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  createTodoTypeConfigHeaders := &dingtalktodo_1_0.CreateTodoTypeConfigHeaders{}
  createTodoTypeConfigHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  actionList0 := &dingtalktodo_1_0.CreateTodoTypeConfigRequestActionList{
    ActionKey: tea.String("approve"),
    ButtonStyleType: tea.Int32(101),
    ActionType: tea.Int32(2),
    Url: tea.String("https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}"),
  }
  contentFieldList0 := &dingtalktodo_1_0.CreateTodoTypeConfigRequestContentFieldList{
    FieldKey: tea.String("teacher"),
    FieldType: tea.String("text"),
  }
  createTodoTypeConfigRequest := &dingtalktodo_1_0.CreateTodoTypeConfigRequest{
    CardType: tea.Int32(2),
    Icon: tea.String("https://img.alicdn.com/xxx.png"),
    Description: tea.String("应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。"),
    PcDetailUrlOpenMode: tea.String("PC_SLIDE"),
    ContentFieldList: []*dingtalktodo_1_0.CreateTodoTypeConfigRequestContentFieldList{contentFieldList0},
    ActionList: []*dingtalktodo_1_0.CreateTodoTypeConfigRequestActionList{actionList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateTodoTypeConfigWithOptions(tea.String("PUoiinxxxx"), createTodoTypeConfigRequest, createTodoTypeConfigHeaders, &util.RuntimeOptions{})
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
import dingtalktodo_1_0, * as $dingtalktodo_1_0 from '@alicloud/dingtalk/todo_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalktodo_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalktodo_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createTodoTypeConfigHeaders = new $dingtalktodo_1_0.CreateTodoTypeConfigHeaders({ });
    createTodoTypeConfigHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let actionList0 = new $dingtalktodo_1_0.CreateTodoTypeConfigRequestActionList({
      actionKey: "approve",
      buttonStyleType: 101,
      actionType: 2,
      url: "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}",
    });
    let contentFieldList0 = new $dingtalktodo_1_0.CreateTodoTypeConfigRequestContentFieldList({
      fieldKey: "teacher",
      fieldType: "text",
    });
    let createTodoTypeConfigRequest = new $dingtalktodo_1_0.CreateTodoTypeConfigRequest({
      cardType: 2,
      icon: "https://img.alicdn.com/xxx.png",
      description: "应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
      pcDetailUrlOpenMode: "PC_SLIDE",
      contentFieldList: [
        contentFieldList0
      ],
      actionList: [
        actionList0
      ],
    });
    try {
      await client.createTodoTypeConfigWithOptions("PUoiinxxxx", createTodoTypeConfigRequest, createTodoTypeConfigHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigHeaders createTodoTypeConfigHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigHeaders();
            createTodoTypeConfigHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestActionList actionList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestActionList
            {
                ActionKey = "approve",
                ButtonStyleType = 101,
                ActionType = 2,
                Url = "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestContentFieldList contentFieldList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestContentFieldList
            {
                FieldKey = "teacher",
                FieldType = "text",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest createTodoTypeConfigRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest
            {
                CardType = 2,
                Icon = "https://img.alicdn.com/xxx.png",
                Description = "应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
                PcDetailUrlOpenMode = "PC_SLIDE",
                ContentFieldList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestContentFieldList>
                {
                    contentFieldList0
                },
                ActionList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.CreateTodoTypeConfigRequest.CreateTodoTypeConfigRequestActionList>
                {
                    actionList0
                },
            };
            try
            {
                client.CreateTodoTypeConfigWithOptions("PUoiinxxxx", createTodoTypeConfigRequest, createTodoTypeConfigHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalktodo__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalktodo_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalktodo_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::Client> client = make_shared<Alibabacloud_Dingtalktodo_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigHeaders> createTodoTypeConfigHeaders = make_shared<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigHeaders>();
  createTodoTypeConfigHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequestActionList> actionList0 = make_shared<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequestActionList>(map<string, boost::any>({
    {"actionKey", boost::any(string("approve"))},
    {"buttonStyleType", boost::any(101)},
    {"actionType", boost::any(2)},
    {"url", boost::any(string("https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}"))}
  }));
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequestContentFieldList> contentFieldList0 = make_shared<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequestContentFieldList>(map<string, boost::any>({
    {"fieldKey", boost::any(string("teacher"))},
    {"fieldType", boost::any(string("text"))}
  }));
  shared_ptr<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequest> createTodoTypeConfigRequest = make_shared<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequest>(map<string, boost::any>({
    {"cardType", boost::any(2)},
    {"icon", boost::any(string("https://img.alicdn.com/xxx.png"))},
    {"description", boost::any(string("应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。"))},
    {"pcDetailUrlOpenMode", boost::any(string("PC_SLIDE"))},
    {"contentFieldList", boost::any(vector<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequestContentFieldList>({
      contentFieldList0
    }))},
    {"actionList", boost::any(vector<Alibabacloud_Dingtalktodo_1_0::CreateTodoTypeConfigRequestActionList>({
      actionList0
    }))}
  }));
  try {
    client->createTodoTypeConfigWithOptions(make_shared<string>("PUoiinxxxx"), createTodoTypeConfigRequest, createTodoTypeConfigHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## **响应**

### **响应体**

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| id | String | 待办卡片类型ID。 |
| createdTime | Long | 创建时间，13位时间戳。 |
| modifiedTime | Long | 更新时间，13位时间戳。 |
| creatorId | String | 创建者的unionId。 |
| modifierId | String | 更新者的unionId。 |
| bizTag | String | 接入应用标识。 |
| requestId | String | 请求ID。 |
| cardType | Integer | 卡片类型，取值。   - **1**：标准卡片 - **2**：自定义卡片 |
| icon | String | 卡片类型图标，用于在待办列表展示。 |
| description | String | 待办卡片类型描述。 |
| pcDetailUrlOpenMode | String | 详情页链接在PC端的打开方式，取值。   - **PC\_SLIDE**：PC端侧边栏打开 - **PC\_BROWSER**：浏览器打开 |
| contentFieldList | Array | 内容区表单自定义字段配置。 |
| fieldKey | String | 字段的唯一标识。 |
| fieldType | String | 字段类型。 |
| nameI18n | Map | 字段显示名称。 |
| actionList | Array | 待办卡片操作区按钮配置。 |
| actionKey | String | 操作按钮的唯一标识。 |
| buttonStyleType | Integer | 按钮样式类型，取值。   - **101**：蓝色线型主按钮样式 - **102**：黑色线型副按钮样式 |
| actionType | Integer | 按钮类型。 |
| url | String | 跳转的url。 |
| nameI18n | Map | 按钮显示名称。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "OPJpxxxxxrzd",
  "createdTime" : 1617675200000,
  "modifiedTime" : 1617675200000,
  "creatorId" : "PUoixxxxxGiP6g",
  "modifierId" : "PUoixxxxxP6g",
  "bizTag" : "todo_open_suitesvn6jmcyk5prz94x",
  "requestId" : "PUoiixxxxxGiP6g",
  "cardType" : 2,
  "icon" : "https://img.alixxxxx5RqcRF_!!6000000000917-2-tps-78-78.png",
  "description" : "应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
  "pcDetailUrlOpenMode" : "PC_SLIDE",
  "contentFieldList" : [ {
    "fieldKey" : "teacher",
    "fieldType" : "text"
  } ],
  "actionList" : [ {
    "actionKey" : "approve",
    "buttonStyleType" : 101,
    "actionType" : 2,
    "url" : "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}"
  } ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.typeConfigCreate.paramError | todo.typeConfigCreate.paramError | 创建待办卡片配置参数错误 |
| 400 | todo.typeConfigCreate.paramError | cardType is null | 卡片cardType为空或取值非法 |
| 400 | todo.typeConfigCreate.paramError | card icon is null | 卡片icon不能为空 |
| 400 | todo.typeConfigCreate.paramError | card description is oversize | 卡片描述过长 |
| 400 | todo.typeConfigCreate.paramError | pcDetailUrlOpenMode is invalid | 卡片打开方式非法 |
| 400 | todo.typeConfigCreate.paramError | card content is oversize | 卡片摘要长度超过限制 |
| 400 | todo.typeConfigCreate.paramError | card action is oversize | 卡片快捷按钮数量超过限制 |
| 400 | todo.typeConfigCreate.paramError | too many card config | 创建的待办卡片数量超过上限 |
| 500 | todo.typeConfigCreate.systemError | todo.typeConfigCreate.systemError | 创建待办卡片配置系统内部异常 |
