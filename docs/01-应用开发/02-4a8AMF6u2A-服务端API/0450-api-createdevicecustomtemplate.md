---
title: "创建自定义屏幕模板"
source_url: "https://open.dingtalk.com/document/development/api-createdevicecustomtemplate"
namespace: "development"
slug: "api-createdevicecustomtemplate"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 自定义屏幕模板 > 创建自定义屏幕模板"
doc_id: "ETdCNj4zuL"
updated_at: "2026-06-02 13:18:20"
---

> Source: https://open.dingtalk.com/document/development/api-createdevicecustomtemplate
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 自定义屏幕模板 > 创建自定义屏幕模板
> Updated: 2026-06-02 13:18:20

# 创建自定义屏幕模板

调用本接口，根据模板名称创建自定义屏幕模板。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/devices/screens/templates |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Rooms.DeviceTemplate.Write-钉钉会议Rooms系统自定义屏幕写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 接口调用凭证，调用[获取用户token](0032-obtain-user-token.md)接口获取。  **[!NOTE]**    获取用户token的请求中，使用的入参`code`参数，在通过构造链接获取的过程中，scope范围必须为用户id和组织id，即`scope=openid corpid`。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| templateName | String | 是 | 模板名称。 |
| logo | String | 否 | 模板logo，可调用[上传媒体文件](0646-upload-media-files.md)接口获取。上传图片后的meidaId，图片尺寸：240\*240，单个图片大小不超过1M。 |
| orgName | String | 否 | 模板企业名称。 |
| customDoc | String | 否 | 模板自定义文字内容。 |
| bgUrl | String | 否 | 模板自定义背景网址。 |
| bgImgList | Array of String | 否 | 图片mediaId，可调用[上传媒体文件](0646-upload-media-files.md)接口获取，最多可上传9张图片，单个图片大小不超过5M。 |
| instruction | Boolean | 否 | 显示使用说明：   - **true**：显示 - **false**：不显示 |
| bgType | Integer | 否 | 模板自定义背景类型：   - **1**：图片 - **2**：网址 |
| isPicTop | Integer | 否 | 展示首页信息栏：   - **0**：展示 - **1**：不展示 |
| hideServerCodeWhenProjecting | Boolean | 否 | 投屏中隐藏投屏码：   - **true**：隐藏 - **false**：不隐藏 |
| showCalendarTitle | Boolean | 否 | 日程卡片展示日程标题：   - **true**：展示 - **false**：不展示 |
| desensitizeUserName | Boolean | 否 | 日程卡片脱敏预订人昵称：   - **true**：脱敏 - **false**：不脱敏 |
| picturePlayInterval | Integer | 否 | 自定义背景图轮播间隔（s） |
| showCalendarCard | Boolean | 否 | 展示日程卡片：   - **true**：展示 - **false**：不展示 |
| showFunctionCard | Boolean | 否 | 展示功能卡片：   - **true**：展示 - **false**：不展示 |
| deviceUnionIds | Array of String | 否 | 设备unionId。该参数从订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件中获取。 |
| groupIds | Array of Long | 否 | 分组id，可调用[查询会议室分组列表](0448-query-meeting-rooms-groups.md)接口获取。 |
| roomIds | Array of String | 否 | 会议室id，可调用[查询会议室列表](0437-check-the-meeting-room-list.md)接口获取。 |

### 请求示例

HTTP

```
POST /v1.0/rooms/devices/screens/templates HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:XXXXXXXX
Content-Type:application/json

{
  "templateName" : "测试模板",
  "logo" : "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
  "orgName" : "测试企业",
  "customDoc" : "测试文本",
  "bgUrl" : "https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png",
  "bgImgList" : [ "$iwElAqxxxxxxcDBgTRC0AF0QZU" ],
  "instruction" : true,
  "bgType" : 1,
  "isPicTop" : 1,
  "hideServerCodeWhenProjecting" : true,
  "showCalendarTitle" : true,
  "desensitizeUserName" : true,
  "picturePlayInterval" : 10,
  "showCalendarCard" : true,
  "showFunctionCard" : true,
  "deviceUnionIds" : [ "2iPOLbpxxxxuwggiiqiPwiEiF" ],
  "groupIds" : [ 172 ],
  "roomIds" : [ "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4" ]
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
    public static com.aliyun.dingtalkrooms_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkrooms_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkrooms_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkrooms_1_0.models.CreateDeviceCustomTemplateHeaders createDeviceCustomTemplateHeaders = new com.aliyun.dingtalkrooms_1_0.models.CreateDeviceCustomTemplateHeaders();
        createDeviceCustomTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.CreateDeviceCustomTemplateRequest createDeviceCustomTemplateRequest = new com.aliyun.dingtalkrooms_1_0.models.CreateDeviceCustomTemplateRequest()
                .setTemplateName("测试模板")
                .setLogo("$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg")
                .setOrgName("测试企业")
                .setCustomDoc("测试文本")
                .setBgUrl("https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png")
                .setBgImgList(java.util.Arrays.asList(
                    "$iwElAqxxxxxxcDBgTRC0AF0QZU"
                ))
                .setInstruction(true)
                .setBgType(1)
                .setIsPicTop(1)
                .setHideServerCodeWhenProjecting(true)
                .setShowCalendarTitle(true)
                .setDesensitizeUserName(true)
                .setPicturePlayInterval(10)
                .setShowCalendarCard(true)
                .setShowFunctionCard(true)
                .setDeviceUnionIds(java.util.Arrays.asList(
                    "2iPOLbpxxxxuwggiiqiPwiEiF"
                ))
                .setGroupIds(java.util.Arrays.asList(
                    172L
                ))
                .setRoomIds(java.util.Arrays.asList(
                    "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
                ));
        try {
            client.createDeviceCustomTemplateWithOptions(createDeviceCustomTemplateRequest, createDeviceCustomTemplateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.rooms_1_0.client import Client as dingtalkrooms_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.rooms_1_0 import models as dingtalkrooms__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkrooms_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkrooms_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_device_custom_template_headers = dingtalkrooms__1__0_models.CreateDeviceCustomTemplateHeaders()
        create_device_custom_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_device_custom_template_request = dingtalkrooms__1__0_models.CreateDeviceCustomTemplateRequest(
            template_name='测试模板',
            logo='$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg',
            org_name='测试企业',
            custom_doc='测试文本',
            bg_url='https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png',
            bg_img_list=[
                '$iwElAqxxxxxxcDBgTRC0AF0QZU'
            ],
            instruction=True,
            bg_type=1,
            is_pic_top=1,
            hide_server_code_when_projecting=True,
            show_calendar_title=True,
            desensitize_user_name=True,
            picture_play_interval=10,
            show_calendar_card=True,
            show_function_card=True,
            device_union_ids=[
                '2iPOLbpxxxxuwggiiqiPwiEiF'
            ],
            group_ids=[
                172
            ],
            room_ids=[
                '239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4'
            ]
        )
        try:
            client.create_device_custom_template_with_options(create_device_custom_template_request, create_device_custom_template_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_device_custom_template_headers = dingtalkrooms__1__0_models.CreateDeviceCustomTemplateHeaders()
        create_device_custom_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_device_custom_template_request = dingtalkrooms__1__0_models.CreateDeviceCustomTemplateRequest(
            template_name='测试模板',
            logo='$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg',
            org_name='测试企业',
            custom_doc='测试文本',
            bg_url='https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png',
            bg_img_list=[
                '$iwElAqxxxxxxcDBgTRC0AF0QZU'
            ],
            instruction=True,
            bg_type=1,
            is_pic_top=1,
            hide_server_code_when_projecting=True,
            show_calendar_title=True,
            desensitize_user_name=True,
            picture_play_interval=10,
            show_calendar_card=True,
            show_function_card=True,
            device_union_ids=[
                '2iPOLbpxxxxuwggiiqiPwiEiF'
            ],
            group_ids=[
                172
            ],
            room_ids=[
                '239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4'
            ]
        )
        try:
            await client.create_device_custom_template_with_options_async(create_device_custom_template_request, create_device_custom_template_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\CreateDeviceCustomTemplateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\CreateDeviceCustomTemplateRequest;
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
        $createDeviceCustomTemplateHeaders = new CreateDeviceCustomTemplateHeaders([]);
        $createDeviceCustomTemplateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createDeviceCustomTemplateRequest = new CreateDeviceCustomTemplateRequest([
            "templateName" => "测试模板",
            "logo" => "\$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
            "orgName" => "测试企业",
            "customDoc" => "测试文本",
            "bgUrl" => "https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png",
            "bgImgList" => [
                "\$iwElAqxxxxxxcDBgTRC0AF0QZU"
            ],
            "instruction" => true,
            "bgType" => 1,
            "isPicTop" => 1,
            "hideServerCodeWhenProjecting" => true,
            "showCalendarTitle" => true,
            "desensitizeUserName" => true,
            "picturePlayInterval" => 10,
            "showCalendarCard" => true,
            "showFunctionCard" => true,
            "deviceUnionIds" => [
                "2iPOLbpxxxxuwggiiqiPwiEiF"
            ],
            "groupIds" => [
                172
            ],
            "roomIds" => [
                "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
            ]
        ]);
        try {
            $client->createDeviceCustomTemplateWithOptions($createDeviceCustomTemplateRequest, $createDeviceCustomTemplateHeaders, new RuntimeOptions([]));
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
  dingtalkrooms_1_0  "github.com/alibabacloud-go/dingtalk/rooms_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkrooms_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkrooms_1_0.Client{}
  _result, _err = dingtalkrooms_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createDeviceCustomTemplateHeaders := &dingtalkrooms_1_0.CreateDeviceCustomTemplateHeaders{}
  createDeviceCustomTemplateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createDeviceCustomTemplateRequest := &dingtalkrooms_1_0.CreateDeviceCustomTemplateRequest{
    TemplateName: tea.String("测试模板"),
    Logo: tea.String("$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg"),
    OrgName: tea.String("测试企业"),
    CustomDoc: tea.String("测试文本"),
    BgUrl: tea.String("https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png"),
    BgImgList: []*string{tea.String("$iwElAqxxxxxxcDBgTRC0AF0QZU")},
    Instruction: tea.Bool(true),
    BgType: tea.Int32(1),
    IsPicTop: tea.Int32(1),
    HideServerCodeWhenProjecting: tea.Bool(true),
    ShowCalendarTitle: tea.Bool(true),
    DesensitizeUserName: tea.Bool(true),
    PicturePlayInterval: tea.Int32(10),
    ShowCalendarCard: tea.Bool(true),
    ShowFunctionCard: tea.Bool(true),
    DeviceUnionIds: []*string{tea.String("2iPOLbpxxxxuwggiiqiPwiEiF")},
    GroupIds: []*int64{tea.Int64(172)},
    RoomIds: []*string{tea.String("239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateDeviceCustomTemplateWithOptions(createDeviceCustomTemplateRequest, createDeviceCustomTemplateHeaders, &util.RuntimeOptions{})
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
import dingtalkrooms_1_0, * as $dingtalkrooms_1_0 from '@alicloud/dingtalk/rooms_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkrooms_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkrooms_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createDeviceCustomTemplateHeaders = new $dingtalkrooms_1_0.CreateDeviceCustomTemplateHeaders({ });
    createDeviceCustomTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createDeviceCustomTemplateRequest = new $dingtalkrooms_1_0.CreateDeviceCustomTemplateRequest({
      templateName: "测试模板",
      logo: "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
      orgName: "测试企业",
      customDoc: "测试文本",
      bgUrl: "https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png",
      bgImgList: [
        "$iwElAqxxxxxxcDBgTRC0AF0QZU"
      ],
      instruction: true,
      bgType: 1,
      isPicTop: 1,
      hideServerCodeWhenProjecting: true,
      showCalendarTitle: true,
      desensitizeUserName: true,
      picturePlayInterval: 10,
      showCalendarCard: true,
      showFunctionCard: true,
      deviceUnionIds: [
        "2iPOLbpxxxxuwggiiqiPwiEiF"
      ],
      groupIds: [
        172
      ],
      roomIds: [
        "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
      ],
    });
    try {
      await client.createDeviceCustomTemplateWithOptions(createDeviceCustomTemplateRequest, createDeviceCustomTemplateHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkrooms_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkrooms_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateDeviceCustomTemplateHeaders createDeviceCustomTemplateHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateDeviceCustomTemplateHeaders();
            createDeviceCustomTemplateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateDeviceCustomTemplateRequest createDeviceCustomTemplateRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.CreateDeviceCustomTemplateRequest
            {
                TemplateName = "测试模板",
                Logo = "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
                OrgName = "测试企业",
                CustomDoc = "测试文本",
                BgUrl = "https://img.alicdn.com/imgextra/i2/O1CN01GWWCCR1y2D9D9EHej_!!6000000006520-2-tps-1920-470.png",
                BgImgList = new List<string>
                {
                    "$iwElAqxxxxxxcDBgTRC0AF0QZU"
                },
                Instruction = true,
                BgType = 1,
                IsPicTop = 1,
                HideServerCodeWhenProjecting = true,
                ShowCalendarTitle = true,
                DesensitizeUserName = true,
                PicturePlayInterval = 10,
                ShowCalendarCard = true,
                ShowFunctionCard = true,
                DeviceUnionIds = new List<string>
                {
                    "2iPOLbpxxxxuwggiiqiPwiEiF"
                },
                GroupIds = new List<long?>
                {
                    172
                },
                RoomIds = new List<string>
                {
                    "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
                },
            };
            try
            {
                client.CreateDeviceCustomTemplateWithOptions(createDeviceCustomTemplateRequest, createDeviceCustomTemplateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| templateId | Long | 模板id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "templateId" : 89
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | Param Error | 参数错误 |
| 400 | no.permission | No Permission | 无权限 |
| 400 | duplicate.template.name | Duplicate Template Name | 模板名称重复 |
| 400 | picture.format.error | Picture Format Error | 图片格式错误 |
| 400 | template.not.found | Template Not Found | 模板找不到 |
| 400 | no.smart.permission | No Smart Room Permission | 未购买高级版无法使用 |
| 500 | system.error | System Error | 系统错误 |
