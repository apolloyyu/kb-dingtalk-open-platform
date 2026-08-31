---
title: "更新待办卡片类型配置"
source_url: "https://open.dingtalk.com/document/development/update-the-to-do-card-type-configuration"
namespace: "development"
slug: "update-the-to-do-card-type-configuration"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 更新待办卡片类型配置"
doc_id: "ux4CGQk80S"
updated_at: "2026-07-30 10:01:51"
---

> Source: https://open.dingtalk.com/document/development/update-the-to-do-card-type-configuration
> Path: 应用开发 / 服务端 API / 待办任务 > 更新待办卡片类型配置
> Updated: 2026-07-30 10:01:51

# 更新待办卡片类型配置

调用本接口可以更新自己业务已有的待办卡片类型配置，支持业务自定义待办列表中的卡片展示样式，包含卡片icon、表单内容、操作按钮等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/configs/types/{cardTypeId} |
| HTTP Method | PUT |
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
| cardTypeId | String | 是 | 待办卡片类型ID，可通过调用[根据id获取待办卡片类型配置](0801-queries-the-to-do-card-type-configuration-details.md)接口获取。 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operatorId | String | 否 | 当前操作者unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| cardType | Integer | 否 | 卡片类型，取值。   - **1**：标准卡片 - **2**：自定义卡片 |
| icon | String | 否 | 卡片类型图标，用于在待办列表展示。图片资源的mediaId可通过[上传媒体文件](0646-upload-media-files.md)接口获取。  **[!NOTE]**    图标要求如下：   - 尺寸：24px \* 24px - 圆角：6px - 大小：小于500k |
| description | String | 否 | 待办卡片类型描述。 |
| pcDetailUrlOpenMode | String | 否 | 详情页链接在PC端的打开方式，取值。   - **PC\_SLIDE**：PC端侧边栏打开 - **PC\_BROWSER**：浏览器打开 |
| contentFieldList | Array | 否 | 内容区表单自定义字段配置。 |
| fieldKey | String | 否 | 字段的唯一标识。 |
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
PUT /v1.0/todo/users/PUoiinWxxxx/configs/types/7MII6Exxxx?operatorId=PUoixxxx2ymhiiGiP6g HTTP/1.1
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
    "url" : "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}",
    "handlers" : [ null ]
  } ]
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
    public static com.aliyun.dingtalktodo_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalktodo_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalktodo_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigHeaders updateTodoTypeConfigHeaders = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigHeaders();
        updateTodoTypeConfigHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestActionList actionList0 = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestActionList()
                .setActionKey("approve")
                .setButtonStyleType(101)
                .setActionType(2)
                .setUrl("https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}");
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestContentFieldList contentFieldList0 = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestContentFieldList()
                .setFieldKey("teacher")
                .setFieldType("text");
        com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigRequest updateTodoTypeConfigRequest = new com.aliyun.dingtalktodo_1_0.models.UpdateTodoTypeConfigRequest()
                .setOperatorId("PUoixxxx2ymhiiGiP6g")
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
            client.updateTodoTypeConfigWithOptions("PUoiinWxxxx", "7MII6Exxxx", updateTodoTypeConfigRequest, updateTodoTypeConfigHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_todo_type_config_headers = dingtalktodo__1__0_models.UpdateTodoTypeConfigHeaders()
        update_todo_type_config_headers.x_acs_dingtalk_access_token = '<your access token>'
        action_list_0 = dingtalktodo__1__0_models.UpdateTodoTypeConfigRequestActionList(
            action_key='approve',
            button_style_type=101,
            action_type=2,
            url='https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}'
        )
        content_field_list_0 = dingtalktodo__1__0_models.UpdateTodoTypeConfigRequestContentFieldList(
            field_key='teacher',
            field_type='text'
        )
        update_todo_type_config_request = dingtalktodo__1__0_models.UpdateTodoTypeConfigRequest(
            operator_id='PUoixxxx2ymhiiGiP6g',
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
            client.update_todo_type_config_with_options('PUoiinWxxxx', '7MII6Exxxx', update_todo_type_config_request, update_todo_type_config_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_todo_type_config_headers = dingtalktodo__1__0_models.UpdateTodoTypeConfigHeaders()
        update_todo_type_config_headers.x_acs_dingtalk_access_token = '<your access token>'
        action_list_0 = dingtalktodo__1__0_models.UpdateTodoTypeConfigRequestActionList(
            action_key='approve',
            button_style_type=101,
            action_type=2,
            url='https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}'
        )
        content_field_list_0 = dingtalktodo__1__0_models.UpdateTodoTypeConfigRequestContentFieldList(
            field_key='teacher',
            field_type='text'
        )
        update_todo_type_config_request = dingtalktodo__1__0_models.UpdateTodoTypeConfigRequest(
            operator_id='PUoixxxx2ymhiiGiP6g',
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
            await client.update_todo_type_config_with_options_async('PUoiinWxxxx', '7MII6Exxxx', update_todo_type_config_request, update_todo_type_config_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTypeConfigHeaders;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTypeConfigRequest\actionList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTypeConfigRequest\contentFieldList;
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\UpdateTodoTypeConfigRequest;
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
        $updateTodoTypeConfigHeaders = new UpdateTodoTypeConfigHeaders([]);
        $updateTodoTypeConfigHeaders->xAcsDingtalkAccessToken = "<your access token>";
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
        $updateTodoTypeConfigRequest = new UpdateTodoTypeConfigRequest([
            "operatorId" => "PUoixxxx2ymhiiGiP6g",
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
            $client->updateTodoTypeConfigWithOptions("PUoiinWxxxx", "7MII6Exxxx", $updateTodoTypeConfigRequest, $updateTodoTypeConfigHeaders, new RuntimeOptions([]));
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
  dingtalktodo_1_0  "github.com/alibabacloud-go/dingtalk/todo_1_0"
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

  updateTodoTypeConfigHeaders := &dingtalktodo_1_0.UpdateTodoTypeConfigHeaders{}
  updateTodoTypeConfigHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  actionList0 := &dingtalktodo_1_0.UpdateTodoTypeConfigRequestActionList{
    ActionKey: tea.String("approve"),
    ButtonStyleType: tea.Int32(101),
    ActionType: tea.Int32(2),
    Url: tea.String("https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}"),
  }
  contentFieldList0 := &dingtalktodo_1_0.UpdateTodoTypeConfigRequestContentFieldList{
    FieldKey: tea.String("teacher"),
    FieldType: tea.String("text"),
  }
  updateTodoTypeConfigRequest := &dingtalktodo_1_0.UpdateTodoTypeConfigRequest{
    OperatorId: tea.String("PUoixxxx2ymhiiGiP6g"),
    CardType: tea.Int32(2),
    Icon: tea.String("https://img.alicdn.com/xxx.png"),
    Description: tea.String("应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。"),
    PcDetailUrlOpenMode: tea.String("PC_SLIDE"),
    ContentFieldList: []*dingtalktodo_1_0.UpdateTodoTypeConfigRequestContentFieldList{contentFieldList0},
    ActionList: []*dingtalktodo_1_0.UpdateTodoTypeConfigRequestActionList{actionList0},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateTodoTypeConfigWithOptions(tea.String("PUoiinWxxxx"), tea.String("7MII6Exxxx"), updateTodoTypeConfigRequest, updateTodoTypeConfigHeaders, &util.RuntimeOptions{})
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
const dingtalktodo_1_0 = require('@alicloud/dingtalk/todo_1_0');
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
    return new dingtalktodo_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateTodoTypeConfigHeaders = new dingtalktodo_1_0.UpdateTodoTypeConfigHeaders({ });
    updateTodoTypeConfigHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let actionList0 = new dingtalktodo_1_0.UpdateTodoTypeConfigRequestActionList({
      actionKey: 'approve',
      buttonStyleType: 101,
      actionType: 2,
      url: 'https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}',
    });
    let contentFieldList0 = new dingtalktodo_1_0.UpdateTodoTypeConfigRequestContentFieldList({
      fieldKey: 'teacher',
      fieldType: 'text',
    });
    let updateTodoTypeConfigRequest = new dingtalktodo_1_0.UpdateTodoTypeConfigRequest({
      operatorId: 'PUoixxxx2ymhiiGiP6g',
      cardType: 2,
      icon: 'https://img.alicdn.com/xxx.png',
      description: '应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。',
      pcDetailUrlOpenMode: 'PC_SLIDE',
      contentFieldList: [
        contentFieldList0
      ],
      actionList: [
        actionList0
      ],
    });
    try {
      await client.updateTodoTypeConfigWithOptions('PUoiinWxxxx', '7MII6Exxxx', updateTodoTypeConfigRequest, updateTodoTypeConfigHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigHeaders updateTodoTypeConfigHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigHeaders();
            updateTodoTypeConfigHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestActionList actionList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestActionList
            {
                ActionKey = "approve",
                ButtonStyleType = 101,
                ActionType = 2,
                Url = "https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestContentFieldList contentFieldList0 = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestContentFieldList
            {
                FieldKey = "teacher",
                FieldType = "text",
            };
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest updateTodoTypeConfigRequest = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest
            {
                OperatorId = "PUoixxxx2ymhiiGiP6g",
                CardType = 2,
                Icon = "https://img.alicdn.com/xxx.png",
                Description = "应用可以调用本接口新增一个待办卡片类型，全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
                PcDetailUrlOpenMode = "PC_SLIDE",
                ContentFieldList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestContentFieldList>
                {
                    contentFieldList0
                },
                ActionList = new List<AlibabaCloud.SDK.Dingtalktodo_1_0.Models.UpdateTodoTypeConfigRequest.UpdateTodoTypeConfigRequestActionList>
                {
                    actionList0
                },
            };
            try
            {
                client.UpdateTodoTypeConfigWithOptions("PUoiinWxxxx", "7MII6Exxxx", updateTodoTypeConfigRequest, updateTodoTypeConfigHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新结果。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | todo.typeConfigUpdate.paramError | todo.typeConfigUpdate.paramError | 更新待办卡片配置参数错误 |
| 400 | todo.typeConfigUpdate.paramError | cardType is null | 卡片cardType为空或取值非法 |
| 400 | todo.typeConfigUpdate.paramError | card icon is null | 卡片icon不能为空 |
| 400 | todo.typeConfigUpdate.paramError | card description is oversize | 卡片描述过长 |
| 400 | todo.typeConfigUpdate.paramError | pcDetailUrlOpenMode is invalid | 卡片打开方式非法 |
| 400 | todo.typeConfigUpdate.paramError | card content is oversize | 卡片摘要长度超过限制 |
| 400 | todo.typeConfigUpdate.paramError | card action is oversize | 卡片快捷按钮数量超过限制 |
| 500 | todo.typeConfigUpdate.systemError | todo.typeConfigUpdate.systemError | 更新待办卡片配置系统内部异常 |
