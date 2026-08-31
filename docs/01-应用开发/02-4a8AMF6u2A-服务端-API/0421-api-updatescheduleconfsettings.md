---
title: "更新预约会议设置"
source_url: "https://open.dingtalk.com/document/development/api-updatescheduleconfsettings"
namespace: "development"
slug: "api-updatescheduleconfsettings"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 更新预约会议设置"
doc_id: "vwc2mz8MnQ"
updated_at: "2026-06-02 12:08:31"
---

> Source: https://open.dingtalk.com/document/development/api-updatescheduleconfsettings
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 更新预约会议设置
> Updated: 2026-06-02 12:08:31

# 更新预约会议设置

调用本接口，更新预约会议设置。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/scheduleConferences/settings |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| creatorUnionId | String | 是 | 预约会议创建人 unionId。 |
| scheduleConferenceId | String | 是 | 预约会议 ID。 |
| scheduleConfSettingModel | Object | 否 | 预约会议设置。 |
| hostUnionId | String | 否 | 主持人 unionId。 |
| confAllowedCorpId | String | 否 | 组织内部会议 corpId。 |
| lockRoom | Integer | 否 | 锁定会议：   - **0**：取消锁定 - **1**：锁定 |
| screenShareForbidden | Integer | 否 | 发起共享：   - **0**：允许共享 - **1**：禁止共享 |
| muteOnJoin | Integer | 否 | 成员入会时静音：   - **-1**：开启 - **0**：不开启 - **6**：超过6人自动开启静音 |
| moziConfVirtualExtraSetting | Object | 否 | 预约会议设置。 |
| waitingRoom | Integer | 否 | 等候室：   - **0**： 不开启 - **1**：开启 |
| joinBeforeHost | Integer | 否 | 在主持人进会前加入会议：   - **0**：不开启 - **1**：开启 |
| enableChat | Integer | 否 | 聊天和互动：   - **0**：不开启 - **1**：开启 |
| lockNick | Integer | 否 | 自己改名：   - **0**：允许自己改名 - **1**：禁止自己改名 |
| lockMediaStatusMicMute | Integer | 否 | 自己解除静音：   - **0**：允许自己解除静音 - **1**：禁止自己解除静音 |
| moziConfExtensionAppSettings | Array | 否 | 会议扩展应用设置列表。 |
| coolAppCode | String | 否 | 酷应用 appCode。 |
| autoOpenMode | Integer | 否 | 自动打开模式：   - **0**：不自动打开 - **1**：仅主持人/联席主持人自动打开 - **2**：全员自动打开 |
| extensionAppBizData | String | 否 | 会议维度扩展应用自定义信息。 |
| enableWebAnonymousJoin | Boolean | 否 | 是否支持web端免登入会：   - **true**：支持 - **false**：不支持 |
| pushAllMeetingRecords | Boolean | 否 | 是否推送所有的会议记录：   - **true**：所有记录都推 - **false**：仅推送实际召开时间落在预约会议计划时间段内的会议记录。   **[!NOTE]**    预约会议计划时间段之外的定义：会议开始时间 > 预约会议计划结束时间，或会议结束时间 > 预约会议计划开始时时间。 |
| pushMinutesCard | Boolean | 否 | 是否推送闪记卡片：   - **true**：推送 - **false**：不推送，默认推 |
| pushCloudRecordCard | Boolean | 否 | 是否推送云录制的闪记卡片：   - **true**：推送 - **false**：不推送，默认推 |
| minutesOwnerUnionId | String | 否 | 闪记归属人，默认归属到预约会议组织者。 |
| cloudRecordOwnerUnionId | String | 否 | 云录制归属人，默认归属到预约会议组织者。 |
| minutesSummaryTemplateType | String | 否 | 云录制摘要指定模板：   - **0**：官方提供模板 - **1**：自定义模板 |
| minutesSummaryTemplateId | String | 否 | - `minutesSummaryTemplateType = 0`，则传入官方模板对应的Id。 - `minutesSummaryTemplateType = 1`，则传入自定义模板对应id。 |
| minutesSummaryDiyTemplateVersion | String | 否 | - `minutesSummaryTemplateType = 0`，则不需要传入。 - `minutesSummaryTemplateType = 1`，则需要传入自定义模板对应的版本号。 |
| hiddenOwnerNick | Boolean | 否 | 是否隐藏云录制发起者姓名。 |
| cohostUnionIds | Array of String | 否 | 联席主持人unionId。 |
| moziConfOpenRecordSetting | Object | 否 | 自动录制设置。 |
| recordAutoStart | Integer | 否 | 是否自动开启云录制：   - **0**：不自动开启 - **1**：自动开启 |
| recordAutoStartType | Integer | 否 | 自动开启云录制类型：   - **0**：我以主持人身份入会后自动开启 - **1**：其他人以联席主持人身份入会后开启 - **2**：任何人以任何身份入会后开启 |
| mode | String | 否 | 会议录制布局：   - **grid**：宫格模式,默认9宫格（3x3） - **speech**：演讲者模式 - **full\_screen**：全屏模式 - **auto\_grid**：自动宫格模式，默认最大4x4宫格 - **screen\_cast**：屏幕共享模式，仅放置屏幕共享流 - **p2p**：双人通话模式 - **full\_screen\_and\_speaker**：共享内容+发言人模式 |
| isFollowHost | Boolean | 否 | 是否跟随主持人：   - **true**：跟随 - **false**：不跟随 |
| restrictShareMinutesSummaryOnly | Integer | 否 | 是否限制分享听记只能分享摘要：   - **0**：不限制 - **1**：限制 |
| aiAgentSummarySetting | Object | 否 | 会议AI听记设置。 |
| value | String | 否 | 是否开启AI助理总结：   - **disable**：不开启 - **enable**：开启 |
| receiverType | Integer | 否 | 会后接收听记推送范围：   - **0**：所有参会人 - **1**：仅创建人 |
| allowAllParticipantsStart | Integer | 否 | 是否允许所有参会人发起：   - **0**：不允许 - **1**：允许 |
| restrictShareMinutesSummaryOnly | Integer | 否 | 是否限制分享听记只能分享摘要：   - **0**：不限制 - **1**：限制 |
| enableAiAgentStatus | Boolean | 否 | 是否展示AI听记功能:   - **true**：展示 - **false**：不展示（安卓钉钉版本8.3.20以上生效，IOS、PC等其他端均生效） |

### 请求示例

HTTP

```
PUT /v1.0/conference/scheduleConferences/settings HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:08e68b256cc73400a8f4256c17c3ff9a
Content-Type:application/json

{
  "creatorUnionId" : "2ixxxxwiEiE",
  "scheduleConferenceId" : "f6fbxxxx50f4a9",
  "scheduleConfSettingModel" : {
    "hostUnionId" : "mE4lKxxxxMwiEi",
    "confAllowedCorpId" : "dingcxxxx4d335",
    "lockRoom" : 1,
    "screenShareForbidden" : 1,
    "muteOnJoin" : 6,
    "moziConfVirtualExtraSetting" : {
      "waitingRoom" : 1,
      "joinBeforeHost" : 1,
      "enableChat" : 1,
      "lockNick" : 1,
      "lockMediaStatusMicMute" : 1,
      "moziConfExtensionAppSettings" : [ {
        "coolAppCode" : "COOLAPPxxxx000W",
        "autoOpenMode" : 1,
        "extensionAppBizData" : "bizData"
      } ],
      "enableWebAnonymousJoin" : true,
      "pushAllMeetingRecords" : true,
      "pushMinutesCard" : true,
      "pushCloudRecordCard" : true,
      "minutesOwnerUnionId" : "mE4lK7nFiPFxxxx17AMw",
      "cloudRecordOwnerUnionId" : "mE4lxxxxh17AMw",
      "minutesSummaryTemplateType" : "0",
      "minutesSummaryTemplateId" : "default",
      "minutesSummaryDiyTemplateVersion" : "1",
      "hiddenOwnerNick" : false
    },
    "cohostUnionIds" : [ "2iPOxxxxiEiE" ],
    "moziConfOpenRecordSetting" : {
      "recordAutoStart" : 1,
      "recordAutoStartType" : 1,
      "mode" : "grid",
      "isFollowHost" : true,
      "restrictShareMinutesSummaryOnly" : 0
    },
    "aiAgentSummarySetting" : {
      "value" : "disable",
      "receiverType" : 1,
      "allowAllParticipantsStart" : 0,
      "restrictShareMinutesSummaryOnly" : 0
    }
  }
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
    public static com.aliyun.dingtalkconference_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkconference_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkconference_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsHeaders updateScheduleConfSettingsHeaders = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsHeaders();
        updateScheduleConfSettingsHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting scheduleConfSettingModelAiAgentSummarySetting = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting()
                .setValue("disable")
                .setReceiverType(1)
                .setAllowAllParticipantsStart(0)
                .setRestrictShareMinutesSummaryOnly(0);
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting scheduleConfSettingModelMoziConfOpenRecordSetting = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting()
                .setRecordAutoStart(1)
                .setRecordAutoStartType(1)
                .setMode("grid")
                .setIsFollowHost(true)
                .setRestrictShareMinutesSummaryOnly(0);
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings()
                .setCoolAppCode("COOLAPPxxxx000W")
                .setAutoOpenMode(1)
                .setExtensionAppBizData("bizData");
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting scheduleConfSettingModelMoziConfVirtualExtraSetting = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting()
                .setWaitingRoom(1)
                .setJoinBeforeHost(1)
                .setEnableChat(1)
                .setLockNick(1)
                .setLockMediaStatusMicMute(1)
                .setMoziConfExtensionAppSettings(java.util.Arrays.asList(
                    scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
                ))
                .setEnableWebAnonymousJoin(true)
                .setPushAllMeetingRecords(true)
                .setPushMinutesCard(true)
                .setPushCloudRecordCard(true)
                .setMinutesOwnerUnionId("mE4lK7nFiPFxxxx17AMw")
                .setCloudRecordOwnerUnionId("mE4lxxxxh17AMw")
                .setMinutesSummaryTemplateType("0")
                .setMinutesSummaryTemplateId("default")
                .setMinutesSummaryDiyTemplateVersion("1")
                .setHiddenOwnerNick(false);
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel scheduleConfSettingModel = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel()
                .setHostUnionId("mE4lKxxxxMwiEi")
                .setConfAllowedCorpId("dingcxxxx4d335")
                .setLockRoom(1)
                .setScreenShareForbidden(1)
                .setMuteOnJoin(6)
                .setMoziConfVirtualExtraSetting(scheduleConfSettingModelMoziConfVirtualExtraSetting)
                .setCohostUnionIds(java.util.Arrays.asList(
                    "2iPOxxxxiEiE"
                ))
                .setMoziConfOpenRecordSetting(scheduleConfSettingModelMoziConfOpenRecordSetting)
                .setAiAgentSummarySetting(scheduleConfSettingModelAiAgentSummarySetting);
        com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest updateScheduleConfSettingsRequest = new com.aliyun.dingtalkconference_1_0.models.UpdateScheduleConfSettingsRequest()
                .setCreatorUnionId("2ixxxxwiEiE")
                .setScheduleConferenceId("f6fbxxxx50f4a9")
                .setScheduleConfSettingModel(scheduleConfSettingModel);
        try {
            client.updateScheduleConfSettingsWithOptions(updateScheduleConfSettingsRequest, updateScheduleConfSettingsHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.conference_1_0.client import Client as dingtalkconference_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.conference_1_0 import models as dingtalkconference__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkconference_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkconference_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_schedule_conf_settings_headers = dingtalkconference__1__0_models.UpdateScheduleConfSettingsHeaders()
        update_schedule_conf_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        schedule_conf_setting_model_ai_agent_summary_setting = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting(
            value='disable',
            receiver_type=1,
            allow_all_participants_start=0,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_open_record_setting = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting(
            record_auto_start=1,
            record_auto_start_type=1,
            mode='grid',
            is_follow_host=True,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0 = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings(
            cool_app_code='COOLAPPxxxx000W',
            auto_open_mode=1,
            extension_app_biz_data='bizData'
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting(
            waiting_room=1,
            join_before_host=1,
            enable_chat=1,
            lock_nick=1,
            lock_media_status_mic_mute=1,
            mozi_conf_extension_app_settings=[
                schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0
            ],
            enable_web_anonymous_join=True,
            push_all_meeting_records=True,
            push_minutes_card=True,
            push_cloud_record_card=True,
            minutes_owner_union_id='mE4lK7nFiPFxxxx17AMw',
            cloud_record_owner_union_id='mE4lxxxxh17AMw',
            minutes_summary_template_type='0',
            minutes_summary_template_id='default',
            minutes_summary_diy_template_version='1',
            hidden_owner_nick=False
        )
        schedule_conf_setting_model = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModel(
            host_union_id='mE4lKxxxxMwiEi',
            conf_allowed_corp_id='dingcxxxx4d335',
            lock_room=1,
            screen_share_forbidden=1,
            mute_on_join=6,
            mozi_conf_virtual_extra_setting=schedule_conf_setting_model_mozi_conf_virtual_extra_setting,
            cohost_union_ids=[
                '2iPOxxxxiEiE'
            ],
            mozi_conf_open_record_setting=schedule_conf_setting_model_mozi_conf_open_record_setting,
            ai_agent_summary_setting=schedule_conf_setting_model_ai_agent_summary_setting
        )
        update_schedule_conf_settings_request = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequest(
            creator_union_id='2ixxxxwiEiE',
            schedule_conference_id='f6fbxxxx50f4a9',
            schedule_conf_setting_model=schedule_conf_setting_model
        )
        try:
            client.update_schedule_conf_settings_with_options(update_schedule_conf_settings_request, update_schedule_conf_settings_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_schedule_conf_settings_headers = dingtalkconference__1__0_models.UpdateScheduleConfSettingsHeaders()
        update_schedule_conf_settings_headers.x_acs_dingtalk_access_token = '<your access token>'
        schedule_conf_setting_model_ai_agent_summary_setting = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting(
            value='disable',
            receiver_type=1,
            allow_all_participants_start=0,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_open_record_setting = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting(
            record_auto_start=1,
            record_auto_start_type=1,
            mode='grid',
            is_follow_host=True,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0 = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings(
            cool_app_code='COOLAPPxxxx000W',
            auto_open_mode=1,
            extension_app_biz_data='bizData'
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting(
            waiting_room=1,
            join_before_host=1,
            enable_chat=1,
            lock_nick=1,
            lock_media_status_mic_mute=1,
            mozi_conf_extension_app_settings=[
                schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0
            ],
            enable_web_anonymous_join=True,
            push_all_meeting_records=True,
            push_minutes_card=True,
            push_cloud_record_card=True,
            minutes_owner_union_id='mE4lK7nFiPFxxxx17AMw',
            cloud_record_owner_union_id='mE4lxxxxh17AMw',
            minutes_summary_template_type='0',
            minutes_summary_template_id='default',
            minutes_summary_diy_template_version='1',
            hidden_owner_nick=False
        )
        schedule_conf_setting_model = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequestScheduleConfSettingModel(
            host_union_id='mE4lKxxxxMwiEi',
            conf_allowed_corp_id='dingcxxxx4d335',
            lock_room=1,
            screen_share_forbidden=1,
            mute_on_join=6,
            mozi_conf_virtual_extra_setting=schedule_conf_setting_model_mozi_conf_virtual_extra_setting,
            cohost_union_ids=[
                '2iPOxxxxiEiE'
            ],
            mozi_conf_open_record_setting=schedule_conf_setting_model_mozi_conf_open_record_setting,
            ai_agent_summary_setting=schedule_conf_setting_model_ai_agent_summary_setting
        )
        update_schedule_conf_settings_request = dingtalkconference__1__0_models.UpdateScheduleConfSettingsRequest(
            creator_union_id='2ixxxxwiEiE',
            schedule_conference_id='f6fbxxxx50f4a9',
            schedule_conf_setting_model=schedule_conf_setting_model
        )
        try:
            await client.update_schedule_conf_settings_with_options_async(update_schedule_conf_settings_request, update_schedule_conf_settings_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsRequest\scheduleConfSettingModel\aiAgentSummarySetting;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsRequest\scheduleConfSettingModel\moziConfOpenRecordSetting;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsRequest\scheduleConfSettingModel\moziConfVirtualExtraSetting\moziConfExtensionAppSettings;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsRequest\scheduleConfSettingModel\moziConfVirtualExtraSetting;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsRequest\scheduleConfSettingModel;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\UpdateScheduleConfSettingsRequest;
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
        $updateScheduleConfSettingsHeaders = new UpdateScheduleConfSettingsHeaders([]);
        $updateScheduleConfSettingsHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $scheduleConfSettingModelAiAgentSummarySetting = new aiAgentSummarySetting([
            "value" => "disable",
            "receiverType" => 1,
            "allowAllParticipantsStart" => 0,
            "restrictShareMinutesSummaryOnly" => 0
        ]);
        $scheduleConfSettingModelMoziConfOpenRecordSetting = new moziConfOpenRecordSetting([
            "recordAutoStart" => 1,
            "recordAutoStartType" => 1,
            "mode" => "grid",
            "isFollowHost" => true,
            "restrictShareMinutesSummaryOnly" => 0
        ]);
        $scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new moziConfExtensionAppSettings([
            "coolAppCode" => "COOLAPPxxxx000W",
            "autoOpenMode" => 1,
            "extensionAppBizData" => "bizData"
        ]);
        $scheduleConfSettingModelMoziConfVirtualExtraSetting = new moziConfVirtualExtraSetting([
            "waitingRoom" => 1,
            "joinBeforeHost" => 1,
            "enableChat" => 1,
            "lockNick" => 1,
            "lockMediaStatusMicMute" => 1,
            "moziConfExtensionAppSettings" => [
                $scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
            ],
            "enableWebAnonymousJoin" => true,
            "pushAllMeetingRecords" => true,
            "pushMinutesCard" => true,
            "pushCloudRecordCard" => true,
            "minutesOwnerUnionId" => "mE4lK7nFiPFxxxx17AMw",
            "cloudRecordOwnerUnionId" => "mE4lxxxxh17AMw",
            "minutesSummaryTemplateType" => "0",
            "minutesSummaryTemplateId" => "default",
            "minutesSummaryDiyTemplateVersion" => "1",
            "hiddenOwnerNick" => false
        ]);
        $scheduleConfSettingModel = new scheduleConfSettingModel([
            "hostUnionId" => "mE4lKxxxxMwiEi",
            "confAllowedCorpId" => "dingcxxxx4d335",
            "lockRoom" => 1,
            "screenShareForbidden" => 1,
            "muteOnJoin" => 6,
            "moziConfVirtualExtraSetting" => $scheduleConfSettingModelMoziConfVirtualExtraSetting,
            "cohostUnionIds" => [
                "2iPOxxxxiEiE"
            ],
            "moziConfOpenRecordSetting" => $scheduleConfSettingModelMoziConfOpenRecordSetting,
            "aiAgentSummarySetting" => $scheduleConfSettingModelAiAgentSummarySetting
        ]);
        $updateScheduleConfSettingsRequest = new UpdateScheduleConfSettingsRequest([
            "creatorUnionId" => "2ixxxxwiEiE",
            "scheduleConferenceId" => "f6fbxxxx50f4a9",
            "scheduleConfSettingModel" => $scheduleConfSettingModel
        ]);
        try {
            $client->updateScheduleConfSettingsWithOptions($updateScheduleConfSettingsRequest, $updateScheduleConfSettingsHeaders, new RuntimeOptions([]));
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
  dingtalkconference_1_0  "github.com/alibabacloud-go/dingtalk/conference_1_0"
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
func CreateClient () (_result *dingtalkconference_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkconference_1_0.Client{}
  _result, _err = dingtalkconference_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateScheduleConfSettingsHeaders := &dingtalkconference_1_0.UpdateScheduleConfSettingsHeaders{}
  updateScheduleConfSettingsHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  scheduleConfSettingModelAiAgentSummarySetting := &dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting{
    Value: tea.String("disable"),
    ReceiverType: tea.Int32(1),
    AllowAllParticipantsStart: tea.Int32(0),
    RestrictShareMinutesSummaryOnly: tea.Int32(0),
  }
  scheduleConfSettingModelMoziConfOpenRecordSetting := &dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting{
    RecordAutoStart: tea.Int32(1),
    RecordAutoStartType: tea.Int32(1),
    Mode: tea.String("grid"),
    IsFollowHost: tea.Bool(true),
    RestrictShareMinutesSummaryOnly: tea.Int32(0),
  }
  scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 := &dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings{
    CoolAppCode: tea.String("COOLAPPxxxx000W"),
    AutoOpenMode: tea.Int32(1),
    ExtensionAppBizData: tea.String("bizData"),
  }
  scheduleConfSettingModelMoziConfVirtualExtraSetting := &dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting{
    WaitingRoom: tea.Int32(1),
    JoinBeforeHost: tea.Int32(1),
    EnableChat: tea.Int32(1),
    LockNick: tea.Int32(1),
    LockMediaStatusMicMute: tea.Int32(1),
    MoziConfExtensionAppSettings: []*dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings{scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0},
    EnableWebAnonymousJoin: tea.Bool(true),
    PushAllMeetingRecords: tea.Bool(true),
    PushMinutesCard: tea.Bool(true),
    PushCloudRecordCard: tea.Bool(true),
    MinutesOwnerUnionId: tea.String("mE4lK7nFiPFxxxx17AMw"),
    CloudRecordOwnerUnionId: tea.String("mE4lxxxxh17AMw"),
    MinutesSummaryTemplateType: tea.String("0"),
    MinutesSummaryTemplateId: tea.String("default"),
    MinutesSummaryDiyTemplateVersion: tea.String("1"),
    HiddenOwnerNick: tea.Bool(false),
  }
  scheduleConfSettingModel := &dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModel{
    HostUnionId: tea.String("mE4lKxxxxMwiEi"),
    ConfAllowedCorpId: tea.String("dingcxxxx4d335"),
    LockRoom: tea.Int32(1),
    ScreenShareForbidden: tea.Int32(1),
    MuteOnJoin: tea.Int32(6),
    MoziConfVirtualExtraSetting: scheduleConfSettingModelMoziConfVirtualExtraSetting,
    CohostUnionIds: []*string{tea.String("2iPOxxxxiEiE")},
    MoziConfOpenRecordSetting: scheduleConfSettingModelMoziConfOpenRecordSetting,
    AiAgentSummarySetting: scheduleConfSettingModelAiAgentSummarySetting,
  }
  updateScheduleConfSettingsRequest := &dingtalkconference_1_0.UpdateScheduleConfSettingsRequest{
    CreatorUnionId: tea.String("2ixxxxwiEiE"),
    ScheduleConferenceId: tea.String("f6fbxxxx50f4a9"),
    ScheduleConfSettingModel: scheduleConfSettingModel,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateScheduleConfSettingsWithOptions(updateScheduleConfSettingsRequest, updateScheduleConfSettingsHeaders, &util.RuntimeOptions{})
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
const dingtalkconference_1_0 = require('@alicloud/dingtalk/conference_1_0');
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
    return new dingtalkconference_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateScheduleConfSettingsHeaders = new dingtalkconference_1_0.UpdateScheduleConfSettingsHeaders({ });
    updateScheduleConfSettingsHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let scheduleConfSettingModelAiAgentSummarySetting = new dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting({
      value: 'disable',
      receiverType: 1,
      allowAllParticipantsStart: 0,
      restrictShareMinutesSummaryOnly: 0,
    });
    let scheduleConfSettingModelMoziConfOpenRecordSetting = new dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting({
      recordAutoStart: 1,
      recordAutoStartType: 1,
      mode: 'grid',
      isFollowHost: true,
      restrictShareMinutesSummaryOnly: 0,
    });
    let scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings({
      coolAppCode: 'COOLAPPxxxx000W',
      autoOpenMode: 1,
      extensionAppBizData: 'bizData',
    });
    let scheduleConfSettingModelMoziConfVirtualExtraSetting = new dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting({
      waitingRoom: 1,
      joinBeforeHost: 1,
      enableChat: 1,
      lockNick: 1,
      lockMediaStatusMicMute: 1,
      moziConfExtensionAppSettings: [
        scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
      ],
      enableWebAnonymousJoin: true,
      pushAllMeetingRecords: true,
      pushMinutesCard: true,
      pushCloudRecordCard: true,
      minutesOwnerUnionId: 'mE4lK7nFiPFxxxx17AMw',
      cloudRecordOwnerUnionId: 'mE4lxxxxh17AMw',
      minutesSummaryTemplateType: '0',
      minutesSummaryTemplateId: 'default',
      minutesSummaryDiyTemplateVersion: '1',
      hiddenOwnerNick: false,
    });
    let scheduleConfSettingModel = new dingtalkconference_1_0.UpdateScheduleConfSettingsRequestScheduleConfSettingModel({
      hostUnionId: 'mE4lKxxxxMwiEi',
      confAllowedCorpId: 'dingcxxxx4d335',
      lockRoom: 1,
      screenShareForbidden: 1,
      muteOnJoin: 6,
      moziConfVirtualExtraSetting: scheduleConfSettingModelMoziConfVirtualExtraSetting,
      cohostUnionIds: [
        '2iPOxxxxiEiE'
      ],
      moziConfOpenRecordSetting: scheduleConfSettingModelMoziConfOpenRecordSetting,
      aiAgentSummarySetting: scheduleConfSettingModelAiAgentSummarySetting,
    });
    let updateScheduleConfSettingsRequest = new dingtalkconference_1_0.UpdateScheduleConfSettingsRequest({
      creatorUnionId: '2ixxxxwiEiE',
      scheduleConferenceId: 'f6fbxxxx50f4a9',
      scheduleConfSettingModel: scheduleConfSettingModel,
    });
    try {
      await client.updateScheduleConfSettingsWithOptions(updateScheduleConfSettingsRequest, updateScheduleConfSettingsHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkconference_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkconference_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkconference_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsHeaders updateScheduleConfSettingsHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsHeaders();
            updateScheduleConfSettingsHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting scheduleConfSettingModelAiAgentSummarySetting = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelAiAgentSummarySetting
            {
                Value = "disable",
                ReceiverType = 1,
                AllowAllParticipantsStart = 0,
                RestrictShareMinutesSummaryOnly = 0,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting scheduleConfSettingModelMoziConfOpenRecordSetting = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfOpenRecordSetting
            {
                RecordAutoStart = 1,
                RecordAutoStartType = 1,
                Mode = "grid",
                IsFollowHost = true,
                RestrictShareMinutesSummaryOnly = 0,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings
            {
                CoolAppCode = "COOLAPPxxxx000W",
                AutoOpenMode = 1,
                ExtensionAppBizData = "bizData",
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting scheduleConfSettingModelMoziConfVirtualExtraSetting = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting
            {
                WaitingRoom = 1,
                JoinBeforeHost = 1,
                EnableChat = 1,
                LockNick = 1,
                LockMediaStatusMicMute = 1,
                MoziConfExtensionAppSettings = new List<AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSetting.UpdateScheduleConfSettingsRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings>
                {
                    scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
                },
                EnableWebAnonymousJoin = true,
                PushAllMeetingRecords = true,
                PushMinutesCard = true,
                PushCloudRecordCard = true,
                MinutesOwnerUnionId = "mE4lK7nFiPFxxxx17AMw",
                CloudRecordOwnerUnionId = "mE4lxxxxh17AMw",
                MinutesSummaryTemplateType = "0",
                MinutesSummaryTemplateId = "default",
                MinutesSummaryDiyTemplateVersion = "1",
                HiddenOwnerNick = false,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel scheduleConfSettingModel = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest.UpdateScheduleConfSettingsRequestScheduleConfSettingModel
            {
                HostUnionId = "mE4lKxxxxMwiEi",
                ConfAllowedCorpId = "dingcxxxx4d335",
                LockRoom = 1,
                ScreenShareForbidden = 1,
                MuteOnJoin = 6,
                MoziConfVirtualExtraSetting = scheduleConfSettingModelMoziConfVirtualExtraSetting,
                CohostUnionIds = new List<string>
                {
                    "2iPOxxxxiEiE"
                },
                MoziConfOpenRecordSetting = scheduleConfSettingModelMoziConfOpenRecordSetting,
                AiAgentSummarySetting = scheduleConfSettingModelAiAgentSummarySetting,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest updateScheduleConfSettingsRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.UpdateScheduleConfSettingsRequest
            {
                CreatorUnionId = "2ixxxxwiEiE",
                ScheduleConferenceId = "f6fbxxxx50f4a9",
                ScheduleConfSettingModel = scheduleConfSettingModel,
            };
            try
            {
                client.UpdateScheduleConfSettingsWithOptions(updateScheduleConfSettingsRequest, updateScheduleConfSettingsHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| success | Boolean | 接口调用是否成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramError | paramError | 参数错误，请检查入参 |
| 400 | creatorUidError | creatorUidError | 创建人错误 |
| 400 | scheduleConferenceIdError | scheduleConferenceIdError | 预约会议id错误 |
| 400 | userNotInOrg | userNotInOrg | 用户不在组织内 |
| 400 | extensionAppSettingError | extensionAppSettingCountError | 扩展应用设置数量错误 |
| 403 | noPermission | noPermission | 无操作权限 |
| 500 | systemError | systemError | 系统错误 |
