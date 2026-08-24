---
title: "更新自定义屏幕模板"
source_url: "https://open.dingtalk.com/document/development/api-updatedevicecustomtemplate"
namespace: "development"
slug: "api-updatedevicecustomtemplate"
group: "应用开发"
tab: "服务端API"
breadcrumb: "音视频 > 智能会议室 > 自定义屏幕模板 > 更新自定义屏幕模板"
doc_id: "u6kpLHkXcy"
updated_at: "2026-06-02 13:18:22"
---

> Source: https://open.dingtalk.com/document/development/api-updatedevicecustomtemplate
> Path: 应用开发 / 服务端API / 音视频 > 智能会议室 > 自定义屏幕模板 > 更新自定义屏幕模板
> Updated: 2026-06-02 13:18:22

# 更新自定义屏幕模板

根据自定义屏幕模板ID，更新自定义屏幕模板信息内容。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/rooms/devices/screens/templates |
| HTTP Method | PUT |
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
| logo | String | 否 | 模板logo，可调用[上传媒体文件](0646-upload-media-files.md)接口获取meidaId，图片尺寸：240\*240，单个图片大小不超过1M。 |
| orgName | String | 否 | 模板企业名称。 |
| customDoc | String | 否 | 模板自定义文字内容。 |
| bgUrl | String | 否 | 模板自定义背景网址。 |
| bgImgList | Array of String | 否 | 图片mediaId，可调用[上传媒体文件](0646-upload-media-files.md)接口获取出参`media_id`参数，最多可上传9张图片，单个图片大小不超过5M。 |
| instruction | Boolean | 否 | 显示使用说明，默认false。取值：   - true：显示 - false：不显示 |
| bgType | Integer | 否 | 模板自定义背景类型，默认1。取值：   - 1：图片 - 2：网址 |
| isPicTop | Integer | 否 | 展示首页信息栏，默认 1。取值：   - 0：展示 - 1：不展示 |
| hideServerCodeWhenProjecting | Boolean | 否 | 投屏中隐藏投屏码，默认false。取值：   - true：隐藏 - false：不隐藏 |
| showCalendarTitle | Boolean | 否 | 日程卡片展示日程标题，默认false。取值：   - true：展示 - false：不展示 |
| desensitizeUserName | Boolean | 否 | 日程卡片脱敏预订人昵称，默认false。取值：   - true：脱敏 - false：不脱敏 |
| picturePlayInterval | Integer | 否 | 自定义背景图轮播间隔秒。 |
| showCalendarCard | Boolean | 否 | 展示日程卡片，默认false。取值：   - true：展示 - false：不展示 |
| showFunctionCard | Boolean | 否 | 展示功能卡片，默认false。取值：   - true：展示 - false：不展示 |
| deviceUnionIds | Array of String | 否 | 设备unionId。该参数从订阅[设备绑定会议室变更](../04-LFcRvVD08N-事件订阅/0002-org-event-overview.md)事件中获取。 |
| groupIds | Array of Long | 否 | 分组id，可调用[查询会议室分组列表](0448-query-meeting-rooms-groups.md)接口获取。 |
| roomIds | Array of String | 否 | 会议室id，可调用[查询会议室列表](0437-check-the-meeting-room-list.md)接口获取。 |
| templateId | Long | 是 | 模板id，可调用[查询自定义屏幕模板列表](https://open.dingtalk.com/document/development/api-querydevicecustomtemplatelist)接口获取。 |

### 请求示例

HTTP

```
PUT /v1.0/rooms/devices/screens/templates HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxxxxxxxx
Content-Type:application/json

{
  "templateName" : "测试模板",
  "logo" : "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
  "orgName" : "测试企业",
  "customDoc" : "测试文本",
  "bgUrl" : "https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png",
  "bgImgList" : [ "$iwElAqxxxxxxcDBgTRC0AF0QZU" ],
  "instruction" : false,
  "bgType" : 1,
  "isPicTop" : 1,
  "hideServerCodeWhenProjecting" : false,
  "showCalendarTitle" : false,
  "desensitizeUserName" : false,
  "picturePlayInterval" : 10,
  "showCalendarCard" : false,
  "showFunctionCard" : false,
  "deviceUnionIds" : [ "2iPOLbpxxxxuwggiiqiPwiEiF" ],
  "groupIds" : [ 172 ],
  "roomIds" : [ "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4" ],
  "templateId" : 89
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
        com.aliyun.dingtalkrooms_1_0.models.UpdateDeviceCustomTemplateHeaders updateDeviceCustomTemplateHeaders = new com.aliyun.dingtalkrooms_1_0.models.UpdateDeviceCustomTemplateHeaders();
        updateDeviceCustomTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkrooms_1_0.models.UpdateDeviceCustomTemplateRequest updateDeviceCustomTemplateRequest = new com.aliyun.dingtalkrooms_1_0.models.UpdateDeviceCustomTemplateRequest()
                .setTemplateName("测试模板")
                .setLogo("$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg")
                .setOrgName("测试企业")
                .setCustomDoc("测试文本")
                .setBgUrl("https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png")
                .setBgImgList(java.util.Arrays.asList(
                    "$iwElAqxxxxxxcDBgTRC0AF0QZU"
                ))
                .setInstruction(false)
                .setBgType(1)
                .setIsPicTop(1)
                .setHideServerCodeWhenProjecting(false)
                .setShowCalendarTitle(false)
                .setDesensitizeUserName(false)
                .setPicturePlayInterval(10)
                .setShowCalendarCard(false)
                .setShowFunctionCard(false)
                .setDeviceUnionIds(java.util.Arrays.asList(
                    "2iPOLbpxxxxuwggiiqiPwiEiF"
                ))
                .setGroupIds(java.util.Arrays.asList(
                    172L
                ))
                .setRoomIds(java.util.Arrays.asList(
                    "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
                ))
                .setTemplateId(89L);
        try {
            client.updateDeviceCustomTemplateWithOptions(updateDeviceCustomTemplateRequest, updateDeviceCustomTemplateHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        update_device_custom_template_headers = dingtalkrooms__1__0_models.UpdateDeviceCustomTemplateHeaders()
        update_device_custom_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_device_custom_template_request = dingtalkrooms__1__0_models.UpdateDeviceCustomTemplateRequest(
            template_name='测试模板',
            logo='$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg',
            org_name='测试企业',
            custom_doc='测试文本',
            bg_url='https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png',
            bg_img_list=[
                '$iwElAqxxxxxxcDBgTRC0AF0QZU'
            ],
            instruction=False,
            bg_type=1,
            is_pic_top=1,
            hide_server_code_when_projecting=False,
            show_calendar_title=False,
            desensitize_user_name=False,
            picture_play_interval=10,
            show_calendar_card=False,
            show_function_card=False,
            device_union_ids=[
                '2iPOLbpxxxxuwggiiqiPwiEiF'
            ],
            group_ids=[
                172
            ],
            room_ids=[
                '239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4'
            ],
            template_id=89
        )
        try:
            client.update_device_custom_template_with_options(update_device_custom_template_request, update_device_custom_template_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_device_custom_template_headers = dingtalkrooms__1__0_models.UpdateDeviceCustomTemplateHeaders()
        update_device_custom_template_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_device_custom_template_request = dingtalkrooms__1__0_models.UpdateDeviceCustomTemplateRequest(
            template_name='测试模板',
            logo='$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg',
            org_name='测试企业',
            custom_doc='测试文本',
            bg_url='https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png',
            bg_img_list=[
                '$iwElAqxxxxxxcDBgTRC0AF0QZU'
            ],
            instruction=False,
            bg_type=1,
            is_pic_top=1,
            hide_server_code_when_projecting=False,
            show_calendar_title=False,
            desensitize_user_name=False,
            picture_play_interval=10,
            show_calendar_card=False,
            show_function_card=False,
            device_union_ids=[
                '2iPOLbpxxxxuwggiiqiPwiEiF'
            ],
            group_ids=[
                172
            ],
            room_ids=[
                '239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4'
            ],
            template_id=89
        )
        try:
            await client.update_device_custom_template_with_options_async(update_device_custom_template_request, update_device_custom_template_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateDeviceCustomTemplateHeaders;
use AlibabaCloud\SDK\Dingtalk\Vrooms_1_0\Models\UpdateDeviceCustomTemplateRequest;
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
        $updateDeviceCustomTemplateHeaders = new UpdateDeviceCustomTemplateHeaders([]);
        $updateDeviceCustomTemplateHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateDeviceCustomTemplateRequest = new UpdateDeviceCustomTemplateRequest([
            "templateName" => "测试模板",
            "logo" => "\$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
            "orgName" => "测试企业",
            "customDoc" => "测试文本",
            "bgUrl" => "https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png",
            "bgImgList" => [
                "\$iwElAqxxxxxxcDBgTRC0AF0QZU"
            ],
            "instruction" => false,
            "bgType" => 1,
            "isPicTop" => 1,
            "hideServerCodeWhenProjecting" => false,
            "showCalendarTitle" => false,
            "desensitizeUserName" => false,
            "picturePlayInterval" => 10,
            "showCalendarCard" => false,
            "showFunctionCard" => false,
            "deviceUnionIds" => [
                "2iPOLbpxxxxuwggiiqiPwiEiF"
            ],
            "groupIds" => [
                172
            ],
            "roomIds" => [
                "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
            ],
            "templateId" => 89
        ]);
        try {
            $client->updateDeviceCustomTemplateWithOptions($updateDeviceCustomTemplateRequest, $updateDeviceCustomTemplateHeaders, new RuntimeOptions([]));
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

  updateDeviceCustomTemplateHeaders := &dingtalkrooms_1_0.UpdateDeviceCustomTemplateHeaders{}
  updateDeviceCustomTemplateHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateDeviceCustomTemplateRequest := &dingtalkrooms_1_0.UpdateDeviceCustomTemplateRequest{
    TemplateName: tea.String("测试模板"),
    Logo: tea.String("$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg"),
    OrgName: tea.String("测试企业"),
    CustomDoc: tea.String("测试文本"),
    BgUrl: tea.String("https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png"),
    BgImgList: []*string{tea.String("$iwElAqxxxxxxcDBgTRC0AF0QZU")},
    Instruction: tea.Bool(false),
    BgType: tea.Int32(1),
    IsPicTop: tea.Int32(1),
    HideServerCodeWhenProjecting: tea.Bool(false),
    ShowCalendarTitle: tea.Bool(false),
    DesensitizeUserName: tea.Bool(false),
    PicturePlayInterval: tea.Int32(10),
    ShowCalendarCard: tea.Bool(false),
    ShowFunctionCard: tea.Bool(false),
    DeviceUnionIds: []*string{tea.String("2iPOLbpxxxxuwggiiqiPwiEiF")},
    GroupIds: []*int64{tea.Int64(172)},
    RoomIds: []*string{tea.String("239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4")},
    TemplateId: tea.Int64(89),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateDeviceCustomTemplateWithOptions(updateDeviceCustomTemplateRequest, updateDeviceCustomTemplateHeaders, &util.RuntimeOptions{})
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
    let updateDeviceCustomTemplateHeaders = new $dingtalkrooms_1_0.UpdateDeviceCustomTemplateHeaders({ });
    updateDeviceCustomTemplateHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let updateDeviceCustomTemplateRequest = new $dingtalkrooms_1_0.UpdateDeviceCustomTemplateRequest({
      templateName: "测试模板",
      logo: "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
      orgName: "测试企业",
      customDoc: "测试文本",
      bgUrl: "https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png",
      bgImgList: [
        "$iwElAqxxxxxxcDBgTRC0AF0QZU"
      ],
      instruction: false,
      bgType: 1,
      isPicTop: 1,
      hideServerCodeWhenProjecting: false,
      showCalendarTitle: false,
      desensitizeUserName: false,
      picturePlayInterval: 10,
      showCalendarCard: false,
      showFunctionCard: false,
      deviceUnionIds: [
        "2iPOLbpxxxxuwggiiqiPwiEiF"
      ],
      groupIds: [
        172
      ],
      roomIds: [
        "239b9bxxxxxf4a898518e41172afcf003e6834fdd7fee4"
      ],
      templateId: 89,
    });
    try {
      await client.updateDeviceCustomTemplateWithOptions(updateDeviceCustomTemplateRequest, updateDeviceCustomTemplateHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateDeviceCustomTemplateHeaders updateDeviceCustomTemplateHeaders = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateDeviceCustomTemplateHeaders();
            updateDeviceCustomTemplateHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateDeviceCustomTemplateRequest updateDeviceCustomTemplateRequest = new AlibabaCloud.SDK.Dingtalkrooms_1_0.Models.UpdateDeviceCustomTemplateRequest
            {
                TemplateName = "测试模板",
                Logo = "$iwElAqNwbmcDBgTRAMgxxxx8FAgACattZWV0aW5nUm9vbQoAC9EYzg",
                OrgName = "测试企业",
                CustomDoc = "测试文本",
                BgUrl = "https://img.alicdn.com/imgextra/i2/O1CN01GxxxxD9EHej_!!600000000xxx.png",
                BgImgList = new List<string>
                {
                    "$iwElAqxxxxxxcDBgTRC0AF0QZU"
                },
                Instruction = false,
                BgType = 1,
                IsPicTop = 1,
                HideServerCodeWhenProjecting = false,
                ShowCalendarTitle = false,
                DesensitizeUserName = false,
                PicturePlayInterval = 10,
                ShowCalendarCard = false,
                ShowFunctionCard = false,
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
                TemplateId = 89,
            };
            try
            {
                client.UpdateDeviceCustomTemplateWithOptions(updateDeviceCustomTemplateRequest, updateDeviceCustomTemplateHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : true
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
