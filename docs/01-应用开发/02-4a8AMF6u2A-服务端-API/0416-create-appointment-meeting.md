---
title: "创建预约会议"
source_url: "https://open.dingtalk.com/document/development/create-appointment-meeting"
namespace: "development"
slug: "create-appointment-meeting"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "音视频 > 会议 > 创建预约会议"
doc_id: "Np5d69Hrgu"
updated_at: "2026-06-10 18:28:07"
---

> Source: https://open.dingtalk.com/document/development/create-appointment-meeting
> Path: 应用开发 / 服务端 API / 音视频 > 会议 > 创建预约会议
> Updated: 2026-06-10 18:28:07

# 创建预约会议

根据创建人、预约会议标题和开始结束时间等信息创建预约会议。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/conference/scheduleConferences |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-VideoConference.Conference.Write-视频会议信息管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求头**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证：   - 企业内部应用，可调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，可调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| creatorUnionId | String | 是 | 创建者unionId。 |
| title | String | 是 | 预约会议标题。标题最大长度限制不允许超过50。超过50字符时会被截断。超过256字符时调用接口会失败。 |
| startTime | Long | 是 | 预约会议开始时间，毫秒级UTC时间戳。 |
| endTime | Long | 是 | 预约会议结束时间，毫秒级UTC时间戳。 |
| scheduleConfSettingModel | Object | 否 | 预约会议设置。 |
| hostUnionId | String | 否 | 主持人 unionId。 |
| confAllowedCorpId | String | 否 | 组织内部会议 corpId。 |
| lockRoom | Integer | 否 | 锁定会议：   - **0**：取消锁定 - **1**：锁定 |
| screenShareForbidden | Integer | 否 | 发起共享：   - **0**：允许共享 - **1**：禁止共享 |
| muteOnJoin | Integer | 否 | 成员入会时静音：   - **-1**：开启 - **0**：不开启 - **6**：超过6人自动开启静音 |
| moziConfVirtualExtraSetting | Object | 否 | 预约会议设置。 |
| waitingRoom | Integer | 否 | 等候室：   - **1**：开启 - **2**： 不开启 |
| joinBeforeHost | Integer | 否 | 在主持人进会前加入会议：   - **0**：不开启 - **1**：开启 |
| enableChat | Integer | 否 | 聊天和互动：   - **0**：不开启 - **1**：开启 |
| lockNick | Integer | 否 | 自己改名：   - **0**：允许自己改名 - **1**：禁止自己改名 |
| lockMediaStatusMicMute | Integer | 否 | 自己解除静音：   - **0**：允许自己解除静音 - **1**：禁止自己解除静音 |
| moziConfExtensionAppSettings | Array | 否 | 会议扩展应用设置列表。 |
| coolAppCode | String | 否 | 酷应用 appCode。 |
| autoOpenMode | Integer | 否 | 是否自动打开：   - **0**：不自动打开 - **1**：仅主持人/联席主持人自动打开 - **2**：全员自动打开 |
| extensionAppBizData | String | 否 | 会议维度扩展应用自定义信息。 |
| enableWebAnonymousJoin | Boolean | 否 | 是否支持web端免登入会：   - **true**：支持 - **false**：不支持 |
| pushAllMeetingRecords | Boolean | 否 | 是否推送所有的会议记录：   - **true**：所有记录都推 - **false**：仅推送实际召开时间落在预约会议计划时间段内的会议记录。   预约会议计划时间段之外的定义：  会议开始时间 > 预约会议计划结束时间，或会议结束时间 > 预约会议计划开始时时间。 |
| pushMinutesCard | Boolean | 否 | 是否推送闪记卡片：   - **true**：推送 - **false**：不推送   默认推送。 |
| pushCloudRecordCard | Boolean | 否 | 是否推送云录制的闪记卡片：   - **true**：推送 - **false**：不推送   默认推送。 |
| minutesOwnerUnionId | String | 否 | 闪记归属人，默认归属到预约会议组织者。 |
| cloudRecordOwnerUnionId | String | 否 | 云录制归属人，默认归属到预约会议组织者 |
| minutesSummaryTemplateType | String | 否 | 云录制摘要指定模板：   - **0**：官方提供模板。 - **1**：自定义模板。 |
| minutesSummaryTemplateId | String | 否 | - `minutesSummaryTemplateType= 0`，则传入官方模板对应的Id。 - `minutesSummaryTemplateType = 1`，则传入自定义模板对应id。 |
| minutesSummaryDiyTemplateVersion | String | 否 | - `minutesSummaryTemplateType = 0`，则不需要传入。 - `minutesSummaryTemplateType = 1`， 则需要传入自定义模板对应的版本号。 |
| hiddenOwnerNick | Boolean | 否 | 是否隐藏云录制发起者姓名：   - **true**：隐藏发起者姓名 - **false**（默认）：不隐藏 |
| cohostUnionIds | Array of String | 否 | 联席主持人unionId。 |
| moziConfOpenRecordSetting | Object | 否 | 自动录制设置。 |
| recordAutoStart | Integer | 否 | 是否自动开启云录制：   - **0**：不自动开启 - **1**：自动开启 |
| recordAutoStartType | Integer | 否 | 自动开启云录制类型：   - **0**：我以主持人身份入会后自动开启 - **1**：其他人以联席主持人身份入会后开启 - **2**：任何人以任何身份入会后开启 |
| mode | String | 否 | 会议录制布局：   - **grid**：宫格模式,默认9宫格(3x3) - **speech**：演讲者模式 - **full\_screen**：全屏模式 - **auto\_grid**：自动宫格模式，默认最大4x4宫格 - **screen\_cast**：屏幕共享模式，仅放置屏幕共享流 - **p2p**：双人通话模式 - **full\_screen\_and\_speaker**：共享内容+发言人模式 |
| isFollowHost | Boolean | 否 | 是否跟随主持人：   - **true**：跟随 - **false**：不跟随 |
| restrictShareMinutesSummaryOnly | Integer | 否 | 是否限制分享听记只能分享摘要：   - **0**：不限制 - **1**：限制 |
| aiAgentSummarySetting | Object | 否 | 会议AI听记设置。 |
| value | String | 否 | 是否开启AI助理总结：   - **disable**：不开启 - **enable**：开启 |
| receiverType | Integer | 否 | 会后接收听记推送范围：   - **0**：所有参会人 - **1**：仅创建人 |
| allowAllParticipantsStart | Integer | 否 | 是否允许所有参会人发起听记：   - **0**：不允许 - **1**：允许 |
| restrictShareMinutesSummaryOnly | Integer | 否 | 是否限制分享听记只能分享摘要：   - **0**：不限制 - **1**：限制 |
| enableAiAgentStatus | Boolean | 否 | 是否展示AI听记功能:   - **true**：展示 - **false**：不展示（安卓钉钉版本8.3.20以上生效，IOS、PC等其他端均生效） |
| allowParticipantShowAiAgentRecord | Boolean | 否 | 会议结束后是否向参会人展示AI听记总结信息：   - **true**：向所有人展示展示 - **false**：只向主持人与联合主持人展示，普通参会人不展示 |

### **请求示例**

HTTP

```
POST /v1.0/conference/scheduleConferences HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:2d7fbxxxxaeb3d
Content-Type:application/json

{
  "creatorUnionId" : "qzR1ixxxx9iP7",
  "title" : "预约会议标题",
  "startTime" : 1687924800000,
  "endTime" : 1687928400000,
  "scheduleConfSettingModel" : {
    "hostUnionId" : "2iPOxxxxwiEiE",
    "confAllowedCorpId" : "dingxxxx335",
    "lockRoom" : 0,
    "screenShareForbidden" : 0,
    "muteOnJoin" : -1,
    "moziConfVirtualExtraSetting" : {
      "waitingRoom" : 0,
      "joinBeforeHost" : 0,
      "enableChat" : 0,
      "lockNick" : 0,
      "lockMediaStatusMicMute" : 0,
      "moziConfExtensionAppSettings" : [ {
        "coolAppCode" : "COOxxxxB000W",
        "autoOpenMode" : 0,
        "extensionAppBizData" : "bizData"
      } ],
      "enableWebAnonymousJoin" : true,
      "pushAllMeetingRecords" : true,
      "pushMinutesCard" : true,
      "pushCloudRecordCard" : true,
      "minutesOwnerUnionId" : "2iPxxxxwiEiE",
      "cloudRecordOwnerUnionId" : "2iPxxxxwiEiE",
      "minutesSummaryTemplateType" : "0",
      "minutesSummaryTemplateId" : "default",
      "minutesSummaryDiyTemplateVersion" : "1",
      "hiddenOwnerNick" : true
    },
    "cohostUnionIds" : [ "mE4lKxxxxwiEi" ],
    "moziConfOpenRecordSetting" : {
      "recordAutoStart" : 0,
      "recordAutoStartType" : 0,
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
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceHeaders createScheduleConferenceHeaders = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceHeaders();
        createScheduleConferenceHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting scheduleConfSettingModelAiAgentSummarySetting = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting()
                .setValue("disable")
                .setReceiverType(1)
                .setAllowAllParticipantsStart(0)
                .setRestrictShareMinutesSummaryOnly(0);
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting scheduleConfSettingModelMoziConfOpenRecordSetting = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting()
                .setRecordAutoStart(0)
                .setRecordAutoStartType(0)
                .setMode("grid")
                .setIsFollowHost(true)
                .setRestrictShareMinutesSummaryOnly(0);
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings()
                .setCoolAppCode("COOxxxxB000W")
                .setAutoOpenMode(0)
                .setExtensionAppBizData("bizData");
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting scheduleConfSettingModelMoziConfVirtualExtraSetting = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting()
                .setWaitingRoom(0)
                .setJoinBeforeHost(0)
                .setEnableChat(0)
                .setLockNick(0)
                .setLockMediaStatusMicMute(0)
                .setMoziConfExtensionAppSettings(java.util.Arrays.asList(
                    scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
                ))
                .setEnableWebAnonymousJoin(true)
                .setPushAllMeetingRecords(true)
                .setPushMinutesCard(true)
                .setPushCloudRecordCard(true)
                .setMinutesOwnerUnionId("2iPxxxxwiEiE")
                .setCloudRecordOwnerUnionId("2iPxxxxwiEiE")
                .setMinutesSummaryTemplateType("0")
                .setMinutesSummaryTemplateId("default")
                .setMinutesSummaryDiyTemplateVersion("1")
                .setHiddenOwnerNick(true);
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel scheduleConfSettingModel = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel()
                .setHostUnionId("2iPOxxxxwiEiE")
                .setConfAllowedCorpId("dingxxxx335")
                .setLockRoom(0)
                .setScreenShareForbidden(0)
                .setMuteOnJoin(-1)
                .setMoziConfVirtualExtraSetting(scheduleConfSettingModelMoziConfVirtualExtraSetting)
                .setCohostUnionIds(java.util.Arrays.asList(
                    "mE4lKxxxxwiEi"
                ))
                .setMoziConfOpenRecordSetting(scheduleConfSettingModelMoziConfOpenRecordSetting)
                .setAiAgentSummarySetting(scheduleConfSettingModelAiAgentSummarySetting);
        com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest createScheduleConferenceRequest = new com.aliyun.dingtalkconference_1_0.models.CreateScheduleConferenceRequest()
                .setCreatorUnionId("qzR1ixxxx9iP7")
                .setTitle("预约会议标题")
                .setStartTime(1687924800000L)
                .setEndTime(1687928400000L)
                .setScheduleConfSettingModel(scheduleConfSettingModel);
        try {
            client.createScheduleConferenceWithOptions(createScheduleConferenceRequest, createScheduleConferenceHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        create_schedule_conference_headers = dingtalkconference__1__0_models.CreateScheduleConferenceHeaders()
        create_schedule_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        schedule_conf_setting_model_ai_agent_summary_setting = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting(
            value='disable',
            receiver_type=1,
            allow_all_participants_start=0,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_open_record_setting = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting(
            record_auto_start=0,
            record_auto_start_type=0,
            mode='grid',
            is_follow_host=True,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0 = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings(
            cool_app_code='COOxxxxB000W',
            auto_open_mode=0,
            extension_app_biz_data='bizData'
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting(
            waiting_room=0,
            join_before_host=0,
            enable_chat=0,
            lock_nick=0,
            lock_media_status_mic_mute=0,
            mozi_conf_extension_app_settings=[
                schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0
            ],
            enable_web_anonymous_join=True,
            push_all_meeting_records=True,
            push_minutes_card=True,
            push_cloud_record_card=True,
            minutes_owner_union_id='2iPxxxxwiEiE',
            cloud_record_owner_union_id='2iPxxxxwiEiE',
            minutes_summary_template_type='0',
            minutes_summary_template_id='default',
            minutes_summary_diy_template_version='1',
            hidden_owner_nick=True
        )
        schedule_conf_setting_model = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModel(
            host_union_id='2iPOxxxxwiEiE',
            conf_allowed_corp_id='dingxxxx335',
            lock_room=0,
            screen_share_forbidden=0,
            mute_on_join=-1,
            mozi_conf_virtual_extra_setting=schedule_conf_setting_model_mozi_conf_virtual_extra_setting,
            cohost_union_ids=[
                'mE4lKxxxxwiEi'
            ],
            mozi_conf_open_record_setting=schedule_conf_setting_model_mozi_conf_open_record_setting,
            ai_agent_summary_setting=schedule_conf_setting_model_ai_agent_summary_setting
        )
        create_schedule_conference_request = dingtalkconference__1__0_models.CreateScheduleConferenceRequest(
            creator_union_id='qzR1ixxxx9iP7',
            title='预约会议标题',
            start_time=1687924800000,
            end_time=1687928400000,
            schedule_conf_setting_model=schedule_conf_setting_model
        )
        try:
            client.create_schedule_conference_with_options(create_schedule_conference_request, create_schedule_conference_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_schedule_conference_headers = dingtalkconference__1__0_models.CreateScheduleConferenceHeaders()
        create_schedule_conference_headers.x_acs_dingtalk_access_token = '<your access token>'
        schedule_conf_setting_model_ai_agent_summary_setting = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting(
            value='disable',
            receiver_type=1,
            allow_all_participants_start=0,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_open_record_setting = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting(
            record_auto_start=0,
            record_auto_start_type=0,
            mode='grid',
            is_follow_host=True,
            restrict_share_minutes_summary_only=0
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0 = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings(
            cool_app_code='COOxxxxB000W',
            auto_open_mode=0,
            extension_app_biz_data='bizData'
        )
        schedule_conf_setting_model_mozi_conf_virtual_extra_setting = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting(
            waiting_room=0,
            join_before_host=0,
            enable_chat=0,
            lock_nick=0,
            lock_media_status_mic_mute=0,
            mozi_conf_extension_app_settings=[
                schedule_conf_setting_model_mozi_conf_virtual_extra_setting_mozi_conf_extension_app_settings_0
            ],
            enable_web_anonymous_join=True,
            push_all_meeting_records=True,
            push_minutes_card=True,
            push_cloud_record_card=True,
            minutes_owner_union_id='2iPxxxxwiEiE',
            cloud_record_owner_union_id='2iPxxxxwiEiE',
            minutes_summary_template_type='0',
            minutes_summary_template_id='default',
            minutes_summary_diy_template_version='1',
            hidden_owner_nick=True
        )
        schedule_conf_setting_model = dingtalkconference__1__0_models.CreateScheduleConferenceRequestScheduleConfSettingModel(
            host_union_id='2iPOxxxxwiEiE',
            conf_allowed_corp_id='dingxxxx335',
            lock_room=0,
            screen_share_forbidden=0,
            mute_on_join=-1,
            mozi_conf_virtual_extra_setting=schedule_conf_setting_model_mozi_conf_virtual_extra_setting,
            cohost_union_ids=[
                'mE4lKxxxxwiEi'
            ],
            mozi_conf_open_record_setting=schedule_conf_setting_model_mozi_conf_open_record_setting,
            ai_agent_summary_setting=schedule_conf_setting_model_ai_agent_summary_setting
        )
        create_schedule_conference_request = dingtalkconference__1__0_models.CreateScheduleConferenceRequest(
            creator_union_id='qzR1ixxxx9iP7',
            title='预约会议标题',
            start_time=1687924800000,
            end_time=1687928400000,
            schedule_conf_setting_model=schedule_conf_setting_model
        )
        try:
            await client.create_schedule_conference_with_options_async(create_schedule_conference_request, create_schedule_conference_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceHeaders;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceRequest\scheduleConfSettingModel\aiAgentSummarySetting;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceRequest\scheduleConfSettingModel\moziConfOpenRecordSetting;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceRequest\scheduleConfSettingModel\moziConfVirtualExtraSetting\moziConfExtensionAppSettings;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceRequest\scheduleConfSettingModel\moziConfVirtualExtraSetting;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceRequest\scheduleConfSettingModel;
use AlibabaCloud\SDK\Dingtalk\Vconference_1_0\Models\CreateScheduleConferenceRequest;
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
        $createScheduleConferenceHeaders = new CreateScheduleConferenceHeaders([]);
        $createScheduleConferenceHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $scheduleConfSettingModelAiAgentSummarySetting = new aiAgentSummarySetting([
            "value" => "disable",
            "receiverType" => 1,
            "allowAllParticipantsStart" => 0,
            "restrictShareMinutesSummaryOnly" => 0
        ]);
        $scheduleConfSettingModelMoziConfOpenRecordSetting = new moziConfOpenRecordSetting([
            "recordAutoStart" => 0,
            "recordAutoStartType" => 0,
            "mode" => "grid",
            "isFollowHost" => true,
            "restrictShareMinutesSummaryOnly" => 0
        ]);
        $scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new moziConfExtensionAppSettings([
            "coolAppCode" => "COOxxxxB000W",
            "autoOpenMode" => 0,
            "extensionAppBizData" => "bizData"
        ]);
        $scheduleConfSettingModelMoziConfVirtualExtraSetting = new moziConfVirtualExtraSetting([
            "waitingRoom" => 0,
            "joinBeforeHost" => 0,
            "enableChat" => 0,
            "lockNick" => 0,
            "lockMediaStatusMicMute" => 0,
            "moziConfExtensionAppSettings" => [
                $scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
            ],
            "enableWebAnonymousJoin" => true,
            "pushAllMeetingRecords" => true,
            "pushMinutesCard" => true,
            "pushCloudRecordCard" => true,
            "minutesOwnerUnionId" => "2iPxxxxwiEiE",
            "cloudRecordOwnerUnionId" => "2iPxxxxwiEiE",
            "minutesSummaryTemplateType" => "0",
            "minutesSummaryTemplateId" => "default",
            "minutesSummaryDiyTemplateVersion" => "1",
            "hiddenOwnerNick" => true
        ]);
        $scheduleConfSettingModel = new scheduleConfSettingModel([
            "hostUnionId" => "2iPOxxxxwiEiE",
            "confAllowedCorpId" => "dingxxxx335",
            "lockRoom" => 0,
            "screenShareForbidden" => 0,
            "muteOnJoin" => -1,
            "moziConfVirtualExtraSetting" => $scheduleConfSettingModelMoziConfVirtualExtraSetting,
            "cohostUnionIds" => [
                "mE4lKxxxxwiEi"
            ],
            "moziConfOpenRecordSetting" => $scheduleConfSettingModelMoziConfOpenRecordSetting,
            "aiAgentSummarySetting" => $scheduleConfSettingModelAiAgentSummarySetting
        ]);
        $createScheduleConferenceRequest = new CreateScheduleConferenceRequest([
            "creatorUnionId" => "qzR1ixxxx9iP7",
            "title" => "预约会议标题",
            "startTime" => 1687924800000,
            "endTime" => 1687928400000,
            "scheduleConfSettingModel" => $scheduleConfSettingModel
        ]);
        try {
            $client->createScheduleConferenceWithOptions($createScheduleConferenceRequest, $createScheduleConferenceHeaders, new RuntimeOptions([]));
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

  createScheduleConferenceHeaders := &dingtalkconference_1_0.CreateScheduleConferenceHeaders{}
  createScheduleConferenceHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  scheduleConfSettingModelAiAgentSummarySetting := &dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting{
    Value: tea.String("disable"),
    ReceiverType: tea.Int32(1),
    AllowAllParticipantsStart: tea.Int32(0),
    RestrictShareMinutesSummaryOnly: tea.Int32(0),
  }
  scheduleConfSettingModelMoziConfOpenRecordSetting := &dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting{
    RecordAutoStart: tea.Int32(0),
    RecordAutoStartType: tea.Int32(0),
    Mode: tea.String("grid"),
    IsFollowHost: tea.Bool(true),
    RestrictShareMinutesSummaryOnly: tea.Int32(0),
  }
  scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 := &dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings{
    CoolAppCode: tea.String("COOxxxxB000W"),
    AutoOpenMode: tea.Int32(0),
    ExtensionAppBizData: tea.String("bizData"),
  }
  scheduleConfSettingModelMoziConfVirtualExtraSetting := &dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting{
    WaitingRoom: tea.Int32(0),
    JoinBeforeHost: tea.Int32(0),
    EnableChat: tea.Int32(0),
    LockNick: tea.Int32(0),
    LockMediaStatusMicMute: tea.Int32(0),
    MoziConfExtensionAppSettings: []*dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings{scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0},
    EnableWebAnonymousJoin: tea.Bool(true),
    PushAllMeetingRecords: tea.Bool(true),
    PushMinutesCard: tea.Bool(true),
    PushCloudRecordCard: tea.Bool(true),
    MinutesOwnerUnionId: tea.String("2iPxxxxwiEiE"),
    CloudRecordOwnerUnionId: tea.String("2iPxxxxwiEiE"),
    MinutesSummaryTemplateType: tea.String("0"),
    MinutesSummaryTemplateId: tea.String("default"),
    MinutesSummaryDiyTemplateVersion: tea.String("1"),
    HiddenOwnerNick: tea.Bool(true),
  }
  scheduleConfSettingModel := &dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModel{
    HostUnionId: tea.String("2iPOxxxxwiEiE"),
    ConfAllowedCorpId: tea.String("dingxxxx335"),
    LockRoom: tea.Int32(0),
    ScreenShareForbidden: tea.Int32(0),
    MuteOnJoin: tea.Int32(-1),
    MoziConfVirtualExtraSetting: scheduleConfSettingModelMoziConfVirtualExtraSetting,
    CohostUnionIds: []*string{tea.String("mE4lKxxxxwiEi")},
    MoziConfOpenRecordSetting: scheduleConfSettingModelMoziConfOpenRecordSetting,
    AiAgentSummarySetting: scheduleConfSettingModelAiAgentSummarySetting,
  }
  createScheduleConferenceRequest := &dingtalkconference_1_0.CreateScheduleConferenceRequest{
    CreatorUnionId: tea.String("qzR1ixxxx9iP7"),
    Title: tea.String("预约会议标题"),
    StartTime: tea.Int64(1687924800000),
    EndTime: tea.Int64(1687928400000),
    ScheduleConfSettingModel: scheduleConfSettingModel,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateScheduleConferenceWithOptions(createScheduleConferenceRequest, createScheduleConferenceHeaders, &util.RuntimeOptions{})
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
    let createScheduleConferenceHeaders = new dingtalkconference_1_0.CreateScheduleConferenceHeaders({ });
    createScheduleConferenceHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let scheduleConfSettingModelAiAgentSummarySetting = new dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting({
      value: 'disable',
      receiverType: 1,
      allowAllParticipantsStart: 0,
      restrictShareMinutesSummaryOnly: 0,
    });
    let scheduleConfSettingModelMoziConfOpenRecordSetting = new dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting({
      recordAutoStart: 0,
      recordAutoStartType: 0,
      mode: 'grid',
      isFollowHost: true,
      restrictShareMinutesSummaryOnly: 0,
    });
    let scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings({
      coolAppCode: 'COOxxxxB000W',
      autoOpenMode: 0,
      extensionAppBizData: 'bizData',
    });
    let scheduleConfSettingModelMoziConfVirtualExtraSetting = new dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting({
      waitingRoom: 0,
      joinBeforeHost: 0,
      enableChat: 0,
      lockNick: 0,
      lockMediaStatusMicMute: 0,
      moziConfExtensionAppSettings: [
        scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
      ],
      enableWebAnonymousJoin: true,
      pushAllMeetingRecords: true,
      pushMinutesCard: true,
      pushCloudRecordCard: true,
      minutesOwnerUnionId: '2iPxxxxwiEiE',
      cloudRecordOwnerUnionId: '2iPxxxxwiEiE',
      minutesSummaryTemplateType: '0',
      minutesSummaryTemplateId: 'default',
      minutesSummaryDiyTemplateVersion: '1',
      hiddenOwnerNick: true,
    });
    let scheduleConfSettingModel = new dingtalkconference_1_0.CreateScheduleConferenceRequestScheduleConfSettingModel({
      hostUnionId: '2iPOxxxxwiEiE',
      confAllowedCorpId: 'dingxxxx335',
      lockRoom: 0,
      screenShareForbidden: 0,
      muteOnJoin: -1,
      moziConfVirtualExtraSetting: scheduleConfSettingModelMoziConfVirtualExtraSetting,
      cohostUnionIds: [
        'mE4lKxxxxwiEi'
      ],
      moziConfOpenRecordSetting: scheduleConfSettingModelMoziConfOpenRecordSetting,
      aiAgentSummarySetting: scheduleConfSettingModelAiAgentSummarySetting,
    });
    let createScheduleConferenceRequest = new dingtalkconference_1_0.CreateScheduleConferenceRequest({
      creatorUnionId: 'qzR1ixxxx9iP7',
      title: '预约会议标题',
      startTime: 1687924800000,
      endTime: 1687928400000,
      scheduleConfSettingModel: scheduleConfSettingModel,
    });
    try {
      await client.createScheduleConferenceWithOptions(createScheduleConferenceRequest, createScheduleConferenceHeaders, new Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceHeaders createScheduleConferenceHeaders = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceHeaders();
            createScheduleConferenceHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting scheduleConfSettingModelAiAgentSummarySetting = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelAiAgentSummarySetting
            {
                Value = "disable",
                ReceiverType = 1,
                AllowAllParticipantsStart = 0,
                RestrictShareMinutesSummaryOnly = 0,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting scheduleConfSettingModelMoziConfOpenRecordSetting = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfOpenRecordSetting
            {
                RecordAutoStart = 0,
                RecordAutoStartType = 0,
                Mode = "grid",
                IsFollowHost = true,
                RestrictShareMinutesSummaryOnly = 0,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0 = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings
            {
                CoolAppCode = "COOxxxxB000W",
                AutoOpenMode = 0,
                ExtensionAppBizData = "bizData",
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting scheduleConfSettingModelMoziConfVirtualExtraSetting = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting
            {
                WaitingRoom = 0,
                JoinBeforeHost = 0,
                EnableChat = 0,
                LockNick = 0,
                LockMediaStatusMicMute = 0,
                MoziConfExtensionAppSettings = new List<AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSetting.CreateScheduleConferenceRequestScheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings>
                {
                    scheduleConfSettingModelMoziConfVirtualExtraSettingMoziConfExtensionAppSettings0
                },
                EnableWebAnonymousJoin = true,
                PushAllMeetingRecords = true,
                PushMinutesCard = true,
                PushCloudRecordCard = true,
                MinutesOwnerUnionId = "2iPxxxxwiEiE",
                CloudRecordOwnerUnionId = "2iPxxxxwiEiE",
                MinutesSummaryTemplateType = "0",
                MinutesSummaryTemplateId = "default",
                MinutesSummaryDiyTemplateVersion = "1",
                HiddenOwnerNick = true,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel scheduleConfSettingModel = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest.CreateScheduleConferenceRequestScheduleConfSettingModel
            {
                HostUnionId = "2iPOxxxxwiEiE",
                ConfAllowedCorpId = "dingxxxx335",
                LockRoom = 0,
                ScreenShareForbidden = 0,
                MuteOnJoin = -1,
                MoziConfVirtualExtraSetting = scheduleConfSettingModelMoziConfVirtualExtraSetting,
                CohostUnionIds = new List<string>
                {
                    "mE4lKxxxxwiEi"
                },
                MoziConfOpenRecordSetting = scheduleConfSettingModelMoziConfOpenRecordSetting,
                AiAgentSummarySetting = scheduleConfSettingModelAiAgentSummarySetting,
            };
            AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest createScheduleConferenceRequest = new AlibabaCloud.SDK.Dingtalkconference_1_0.Models.CreateScheduleConferenceRequest
            {
                CreatorUnionId = "qzR1ixxxx9iP7",
                Title = "预约会议标题",
                StartTime = 1687924800000,
                EndTime = 1687928400000,
                ScheduleConfSettingModel = scheduleConfSettingModel,
            };
            try
            {
                client.CreateScheduleConferenceWithOptions(createScheduleConferenceRequest, createScheduleConferenceHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| requestId | String | 请求id。 |
| scheduleConferenceId | String | 预约会议id。 |
| roomCode | String | 会议号。 |
| url | String | 预约会议分享链接。 |
| phones | Array of String | 呼入电话号码。 |

### **响应体示例**

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "requestId" : "1234567",
  "scheduleConferenceId" : "5c7c9bb1-xxxx-4dc5",
  "roomCode" : "83150xxxxxx",
  "url" : "https://meeting.dingtalk.com/j/knvMq1ixxxx",
  "phones" : [ "+861234567" ]
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | paramsError | error:%s | 参数错误 |
| 400 | paramsError | error:%s | 参数错误，用户unionId错误 |
| 500 | systemError | systemError:%s | 系统错误 |
