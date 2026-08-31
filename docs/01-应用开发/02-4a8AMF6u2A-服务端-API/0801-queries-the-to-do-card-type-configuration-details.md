---
title: "根据id获取待办卡片类型配置"
source_url: "https://open.dingtalk.com/document/development/queries-the-to-do-card-type-configuration-details"
namespace: "development"
slug: "queries-the-to-do-card-type-configuration-details"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "待办任务 > 根据id获取待办卡片类型配置"
doc_id: "wEbk2x5cti"
updated_at: "2026-07-30 10:01:50"
---

> Source: https://open.dingtalk.com/document/development/queries-the-to-do-card-type-configuration-details
> Path: 应用开发 / 服务端 API / 待办任务 > 根据id获取待办卡片类型配置
> Updated: 2026-07-30 10:01:50

# 根据id获取待办卡片类型配置

调用本接口可以根据ID获取一个自己业务系统已定义的待办卡片类型配置详情，包含卡片icon、表单内容、操作按钮等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/todo/users/{unionId}/configs/types/{cardTypeId} |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Todo.Todo.Read-待办应用中待办读权限 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过 [获取用户token](0032-obtain-user-token.md)接口获取。 |

### **路径参数**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| unionId | String | 是 | 用户的unionId，可通过[查询用户详情](0056-query-user-details.md)接口获取。 |
| cardTypeId | String | 是 | 待办卡片类型ID，可通过[创建待办卡片类型配置](0799-add-todo-cardtype-configuration.md)接口获取。 |

### **请求示例**

HTTP

```
GET /v1.0/todo/users/PUoiixxxx/configs/types/7MII6Exxxx HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:b3ba04xxxx
Content-Type:application/json
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
        com.aliyun.dingtalktodo_1_0.models.GetTodoTypeConfigHeaders getTodoTypeConfigHeaders = new com.aliyun.dingtalktodo_1_0.models.GetTodoTypeConfigHeaders();
        getTodoTypeConfigHeaders.xAcsDingtalkAccessToken = "<your access token>";
        try {
            client.getTodoTypeConfigWithOptions("PUoiixxxx", "7MII6Exxxx", getTodoTypeConfigHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        get_todo_type_config_headers = dingtalktodo__1__0_models.GetTodoTypeConfigHeaders()
        get_todo_type_config_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            client.get_todo_type_config_with_options('PUoiixxxx', '7MII6Exxxx', get_todo_type_config_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        get_todo_type_config_headers = dingtalktodo__1__0_models.GetTodoTypeConfigHeaders()
        get_todo_type_config_headers.x_acs_dingtalk_access_token = '<your access token>'
        try:
            await client.get_todo_type_config_with_options_async('PUoiixxxx', '7MII6Exxxx', get_todo_type_config_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vtodo_1_0\Models\GetTodoTypeConfigHeaders;
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
        $getTodoTypeConfigHeaders = new GetTodoTypeConfigHeaders([]);
        $getTodoTypeConfigHeaders->xAcsDingtalkAccessToken = "<your access token>";
        try {
            $client->getTodoTypeConfigWithOptions("PUoiixxxx", "7MII6Exxxx", $getTodoTypeConfigHeaders, new RuntimeOptions([]));
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

  getTodoTypeConfigHeaders := &dingtalktodo_1_0.GetTodoTypeConfigHeaders{}
  getTodoTypeConfigHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.GetTodoTypeConfigWithOptions(tea.String("PUoiixxxx"), tea.String("7MII6Exxxx"), getTodoTypeConfigHeaders, &util.RuntimeOptions{})
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
    let getTodoTypeConfigHeaders = new dingtalktodo_1_0.GetTodoTypeConfigHeaders({ });
    getTodoTypeConfigHeaders.xAcsDingtalkAccessToken = '<your access token>';
    try {
      await client.getTodoTypeConfigWithOptions('PUoiixxxx', '7MII6Exxxx', getTodoTypeConfigHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalktodo_1_0.Models.GetTodoTypeConfigHeaders getTodoTypeConfigHeaders = new AlibabaCloud.SDK.Dingtalktodo_1_0.Models.GetTodoTypeConfigHeaders();
            getTodoTypeConfigHeaders.XAcsDingtalkAccessToken = "<your access token>";
            try
            {
                client.GetTodoTypeConfigWithOptions("PUoiixxxx", "7MII6Exxxx", getTodoTypeConfigHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| id | String | 待办卡片ID。 |
| createdTime | Long | 创建时间。 |
| modifiedTime | Long | 更新时间。 |
| creatorId | String | 创建者的unionId。 |
| modifierId | String | 更新者的unionId。 |
| bizTag | String | 接入应用标识。 |
| requestId | String | 请求ID。 |
| cardType | Integer | 卡片类型，取值。   - **1**：标准卡片 - **2**：自定义卡片 |
| icon | String | 卡片类型icon，用于在待办列表展示。 |
| description | String | 待办卡片类型描述。 |
| pcDetailUrlOpenMode | String | 详情页链接在PC端的打开方式，取值。   - **PC\_SLIDE：PC**端侧边栏打开 - **PC\_BROWSER**：浏览器打开 |
| contentFieldList | Array | 待办卡片内容区表单自定义字段配置。 |
| fieldKey | String | 字段唯一标识。 |
| fieldType | String | 字段类型（取值为：text-文本，url-链接） |
| nameI18n | Map | 字段显示名称。  需支持zh\_CN、zh\_TW、zh\_HK、en\_US、vi\_VN、ja\_JP等语言国际化。  示例值如下：   ``` {     "nameI18n": {     "zh_CN": "老师",     "zh_TW": "老師",     "zh_HK": "老師",     "en_US": "Teacher",     "vi_VN": "Giáo viên",     "ja_JP": "先生"     } } ``` |
| actionList | Array | 待办卡片操作区按钮配置。 |
| actionKey | String | 操作按钮的唯一标识。 |
| buttonStyleType | Integer | 按钮样式类型，取值。   - **101**：蓝色线型主按钮样式 - **102**：黑色线型副按钮样式 |
| actionType | Integer | 按钮类型，当前仅支持**直接跳转**取值为**2**。 |
| url | String | 按钮对应的URL。例如：`https://api.dingtalk.com/v1.0/todo/tasks?sourceId={0}&actionKey={1}&from={2}`。  **[!NOTE]**     - 当用户点击按钮时，钉钉会向此链接发送请求，并携带**sourceId**、**actionKey**和**from来源**等关键信息。 - 如果需要完成待办，则需要返回以下信息给钉钉：     ```   {   "code": 200,   "message": "OK",   "success": true   }   ``` |
| nameI18n | Map | 按钮显示名称。  需支持zh\_CN、zh\_TW、zh\_HK、en\_US、vi\_VN、ja\_JP等语言国际化。  示例值如下：   ``` {     "nameI18n": {     "zh_CN": "老师",     "zh_TW": "老師",     "zh_HK": "老師",     "en_US": "Teacher",     "vi_VN": "Giáo viên",     "ja_JP": "先生"     } } ``` |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "id" : "7MxxxxJLIiE",
  "createdTime" : 1621843486534,
  "modifiedTime" : 1621843486534,
  "creatorId" : "PUoxxxxiP6g",
  "modifierId" : "PUoiixxxxiP6g",
  "bizTag" : "todo_open_suitesvn6jmcyk5prz94x",
  "requestId" : "PUoiixxxx6g",
  "cardType" : 2,
  "icon" : "https://img.alicdn.com/xxx.png",
  "description" : "全面支持业务自定义待办列表卡片展示样式，随心搭配适合的卡片形态和操作。",
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
| 400 | todo.typeConfigGet.paramError | todo.typeConfigGet.paramError | 获取待办卡片配置参数错误 |
| 400 | todo.typeConfigGet.paramError | cardTypeId is null | 待办卡片id为空 |
| 500 | todo.typeConfigGet.systemError | todo.typeConfigGet.systemError | 获取待办卡片配置系统内部异常 |
