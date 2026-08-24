---
title: "创建流程中心待处理任务"
source_url: "https://open.dingtalk.com/document/development/create-pending-tasks-in-process-center"
namespace: "development"
slug: "create-pending-tasks-in-process-center"
group: "应用开发"
tab: "服务端API"
breadcrumb: "OA 审批 > 自有 OA 审批 > 流程中心任务 > 创建流程中心待处理任务"
doc_id: "mxGLeu4NYE"
updated_at: "2026-06-02 15:54:12"
---

> Source: https://open.dingtalk.com/document/development/create-pending-tasks-in-process-center
> Path: 应用开发 / 服务端API / OA 审批 > 自有 OA 审批 > 流程中心任务 > 创建流程中心待处理任务
> Updated: 2026-06-02 15:54:12

# 创建流程中心待处理任务

调用本接口，创建OA审批的待办任务。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/processCentres/tasks |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_aflow-审批流数据管理权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processInstanceId | String | 是 | OA审批流程实例ID，可调用[创建实例](0513-create-a-ticket-approval-instance.md)接口获取`processInstanceId`参数值。 |
| activityId | String | 否 | 自定义审批节点ID，自定义参数，最大长度256字符。 |
| tasks | Array | 是 | 任务列表，最多20个元素。 |
| userId | String | 否 | 用户userId，可通过[获取部门用户userid列表](0065-query-the-list-of-department-userids.md)接口获取。 |
| url | String | 否 | 待办事项跳转URL，最大长度1024字符。  **[!NOTE]**   - 创建审批实例里的url，实现的是钉钉审批应用里的审批单跳转。 - 本接口的url，实现的是钉钉待办页面，对应的待办卡片的跳转。 - 钉钉的待办页面，同时支持移动端和PC端，所以本接口传的url参数，它所对应的页面需要适配移动端和PC端。 |
| customData | String | 否 | 用户自定义数据，页面跳转时将通过url参数回传，最大长度500字符。 |
| dueTimestamp | Long | 否 | 任务截止时间，Unix时间戳，单位毫秒。设置该参数后，将在钉钉待办中心展示审批任务截止时间信息，支持按截止时间排序，今日截止、已逾期等标签筛选等。 |
| featureConfig | Object | 否 | 流程中心集成配置，支持任务维度指定待办、卡片通知中的快捷操作按钮入口配置。 |
| features | Array | 否 | 配置列表。 |
| name | String | 否 | 支持三方进行自定义配置的功能模块名称，当前支持：   - **CUSTOM\_SHORTCUT**：待办、卡片通知中的快捷操作按钮 |
| pcUrl | String | 否 | 三方自定义的pc端跳转链接，最大长度1024字符。 |
| mobileUrl | String | 否 | 三方自定义的手机端跳转链接，最大长度1024字符。 |
| runType | String | 否 | 运行方式。  当features.name为`CUSTOM_SHORTCUT`时，支持   - **ORIGIN**：原生运行，打开待办详情页时，将会跳转到官方审批的详情页地址 - **REDIRECT**：外部跳转运行，打开待办详情页时，将会跳转到pcUrl、mobileUrl中配置的地址 |
| callback | Object | 否 | 网关回调配置，需支持快捷操作按钮时该参数必填。 网关回调钉钉外数据接口需要统一在“数据源管理”中注册成网关，详细的使用说明请参考[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)。 |
| appUuid | String | 否 | 网关appUuid，需支持快捷操作按钮时该参数必填。  传[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时所属企业corpId值。 |
| apiKey | String | 否 | 网关apiKey，若需支持快捷操作按钮入口时该参数必填。通过[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)内容获取`apiKey`。  **[!NOTE]**   - 在网关回调外部接口时，钉钉侧会根据不同业务场景，回传一些业务处理所需的参数给到ISV，ISV在收到回调请求后，若需要解析获取对应参数信息，需要在[创建数据源](https://open.dingtalk.com/document/dingstart/create-a-data-source)时配置对应的参数key。   例如，TASK\_EXECUTE任务执行模块，即详情页的同意、拒绝按钮配置回调时，钉钉侧回传的固定参数如下：`{"outResult":"agree","processInstanceId":"xxx","activityId":"xxx","corpId":"dingxxx","data":[],"remark":"同意","title":"xxx提交的资产领用申请","taskId":111,"operator":"manager0001"}`。 - ISV在创建数据源时，对应的参数配置需按业务需要填对应的key进行解析：outResult,processInstanceId,activityId,corpId,remark,title,taskId,operator |
| version | String | 否 | 网关接口版本  **[!NOTE]**   - 若需支持快捷操作按钮入口时该参数必填。 - 默认传1。 |
| config | String | 否 | 三方进行自定义配置的功能模块对应的配置信息，最大长度1024字符。 |

### 请求示例

HTTP

```
POST /v1.0/workflow/processCentres/tasks HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxx
Content-Type:application/json

{
  "processInstanceId" : "S3j8rbiNT1CsXXXXXV3Q1Q04431661334483",
  "activityId" : "act_xxxxx",
  "tasks" : [ {
    "userId" : "manager001",
    "url" : "https://www.dingtalk.com",
    "customData" : "test***",
    "dueTimestamp" : 1758729600000
  } ],
  "featureConfig" : {
    "features" : [ {
      "name" : "CUSTOM_SHORTCUT",
      "pcUrl" : "www.dingtalk.com",
      "mobileUrl" : "www.dingtalk.com",
      "runType" : "REDIRECT",
      "callback" : {
        "appUuid" : "开发组织的corpId",
        "apiKey" : "数据源配置后生成的apiKey",
        "version" : "1"
      },
      "config" : "{\\\"shortcutStyle\\\":\\\"EXECUTE_ACTION\\\",       \\\"buttonConfig\\\":{\\\"agreeBtn\\\":\\\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\\\",\\\"refuseBtn\\\":\\\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\\\"}}"
    } ]
  }
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskHeaders createIntegratedTaskHeaders = new com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskHeaders();
        createIntegratedTaskHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback featureConfigFeatures0Callback = new com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback()
                .setAppUuid("开发组织的corpId")
                .setApiKey("数据源配置后生成的apiKey")
                .setVersion("1");
        com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfigFeatures featureConfigFeatures0 = new com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfigFeatures()
                .setName("CUSTOM_SHORTCUT")
                .setPcUrl("www.dingtalk.com")
                .setMobileUrl("www.dingtalk.com")
                .setRunType("REDIRECT")
                .setCallback(featureConfigFeatures0Callback)
                .setConfig("{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}");
        com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig featureConfig = new com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig()
                .setFeatures(java.util.Arrays.asList(
                    featureConfigFeatures0
                ));
        com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks tasks0 = new com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks()
                .setUserId("manager001")
                .setUrl("https://www.dingtalk.com")
                .setCustomData("test***")
                .setDueTimestamp(1758729600000L);
        com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest createIntegratedTaskRequest = new com.aliyun.dingtalkworkflow_1_0.models.CreateIntegratedTaskRequest()
                .setProcessInstanceId("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483")
                .setActivityId("act_xxxxx")
                .setTasks(java.util.Arrays.asList(
                    tasks0
                ))
                .setFeatureConfig(featureConfig);
        try {
            client.createIntegratedTaskWithOptions(createIntegratedTaskRequest, createIntegratedTaskHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.workflow_1_0.client import Client as dingtalkworkflow_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.workflow_1_0 import models as dingtalkworkflow__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkworkflow_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkworkflow_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_integrated_task_headers = dingtalkworkflow__1__0_models.CreateIntegratedTaskHeaders()
        create_integrated_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        feature_config_features_0callback = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback(
            app_uuid='开发组织的corpId',
            api_key='数据源配置后生成的apiKey',
            version='1'
        )
        feature_config_features_0 = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestFeatureConfigFeatures(
            name='CUSTOM_SHORTCUT',
            pc_url='www.dingtalk.com',
            mobile_url='www.dingtalk.com',
            run_type='REDIRECT',
            callback=feature_config_features_0callback,
            config='''{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}","refuseBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}"}}'''
        )
        feature_config = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestFeatureConfig(
            features=[
                feature_config_features_0
            ]
        )
        tasks_0 = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestTasks(
            user_id='manager001',
            url='https://www.dingtalk.com',
            custom_data='test***',
            due_timestamp=1758729600000
        )
        create_integrated_task_request = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequest(
            process_instance_id='S3j8rbiNT1CsXXXXXV3Q1Q04431661334483',
            activity_id='act_xxxxx',
            tasks=[
                tasks_0
            ],
            feature_config=feature_config
        )
        try:
            client.create_integrated_task_with_options(create_integrated_task_request, create_integrated_task_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_integrated_task_headers = dingtalkworkflow__1__0_models.CreateIntegratedTaskHeaders()
        create_integrated_task_headers.x_acs_dingtalk_access_token = '<your access token>'
        feature_config_features_0callback = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback(
            app_uuid='开发组织的corpId',
            api_key='数据源配置后生成的apiKey',
            version='1'
        )
        feature_config_features_0 = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestFeatureConfigFeatures(
            name='CUSTOM_SHORTCUT',
            pc_url='www.dingtalk.com',
            mobile_url='www.dingtalk.com',
            run_type='REDIRECT',
            callback=feature_config_features_0callback,
            config='''{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}","refuseBtn":"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}"}}'''
        )
        feature_config = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestFeatureConfig(
            features=[
                feature_config_features_0
            ]
        )
        tasks_0 = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequestTasks(
            user_id='manager001',
            url='https://www.dingtalk.com',
            custom_data='test***',
            due_timestamp=1758729600000
        )
        create_integrated_task_request = dingtalkworkflow__1__0_models.CreateIntegratedTaskRequest(
            process_instance_id='S3j8rbiNT1CsXXXXXV3Q1Q04431661334483',
            activity_id='act_xxxxx',
            tasks=[
                tasks_0
            ],
            feature_config=feature_config
        )
        try:
            await client.create_integrated_task_with_options_async(create_integrated_task_request, create_integrated_task_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CreateIntegratedTaskHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CreateIntegratedTaskRequest\featureConfig\features\callback;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CreateIntegratedTaskRequest\featureConfig\features;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CreateIntegratedTaskRequest\featureConfig;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CreateIntegratedTaskRequest\tasks;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\CreateIntegratedTaskRequest;
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
        $createIntegratedTaskHeaders = new CreateIntegratedTaskHeaders([]);
        $createIntegratedTaskHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $featureConfigFeatures0Callback = new callback([
            "appUuid" => "开发组织的corpId",
            "apiKey" => "数据源配置后生成的apiKey",
            "version" => "1"
        ]);
        $featureConfigFeatures0 = new features([
            "name" => "CUSTOM_SHORTCUT",
            "pcUrl" => "www.dingtalk.com",
            "mobileUrl" => "www.dingtalk.com",
            "runType" => "REDIRECT",
            "callback" => $featureConfigFeatures0Callback,
            "config" => "{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}"
        ]);
        $featureConfig = new featureConfig([
            "features" => [
                $featureConfigFeatures0
            ]
        ]);
        $tasks0 = new tasks([
            "userId" => "manager001",
            "url" => "https://www.dingtalk.com",
            "customData" => "test***",
            "dueTimestamp" => 1758729600000
        ]);
        $createIntegratedTaskRequest = new CreateIntegratedTaskRequest([
            "processInstanceId" => "S3j8rbiNT1CsXXXXXV3Q1Q04431661334483",
            "activityId" => "act_xxxxx",
            "tasks" => [
                $tasks0
            ],
            "featureConfig" => $featureConfig
        ]);
        try {
            $client->createIntegratedTaskWithOptions($createIntegratedTaskRequest, $createIntegratedTaskHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
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
func CreateClient () (_result *dingtalkworkflow_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkworkflow_1_0.Client{}
  _result, _err = dingtalkworkflow_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createIntegratedTaskHeaders := &dingtalkworkflow_1_0.CreateIntegratedTaskHeaders{}
  createIntegratedTaskHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  featureConfigFeatures0Callback := &dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback{
    AppUuid: tea.String("开发组织的corpId"),
    ApiKey: tea.String("数据源配置后生成的apiKey"),
    Version: tea.String("1"),
  }
  featureConfigFeatures0 := &dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfigFeatures{
    Name: tea.String("CUSTOM_SHORTCUT"),
    PcUrl: tea.String("www.dingtalk.com"),
    MobileUrl: tea.String("www.dingtalk.com"),
    RunType: tea.String("REDIRECT"),
    Callback: featureConfigFeatures0Callback,
    Config: tea.String("{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}"),
  }
  featureConfig := &dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfig{
    Features: []*dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfigFeatures{featureConfigFeatures0},
  }
  tasks0 := &dingtalkworkflow_1_0.CreateIntegratedTaskRequestTasks{
    UserId: tea.String("manager001"),
    Url: tea.String("https://www.dingtalk.com"),
    CustomData: tea.String("test***"),
    DueTimestamp: tea.Int64(1758729600000),
  }
  createIntegratedTaskRequest := &dingtalkworkflow_1_0.CreateIntegratedTaskRequest{
    ProcessInstanceId: tea.String("S3j8rbiNT1CsXXXXXV3Q1Q04431661334483"),
    ActivityId: tea.String("act_xxxxx"),
    Tasks: []*dingtalkworkflow_1_0.CreateIntegratedTaskRequestTasks{tasks0},
    FeatureConfig: featureConfig,
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateIntegratedTaskWithOptions(createIntegratedTaskRequest, createIntegratedTaskHeaders, &util.RuntimeOptions{})
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
const dingtalkworkflow_1_0 = require('@alicloud/dingtalk/workflow_1_0');
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
    return new dingtalkworkflow_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let createIntegratedTaskHeaders = new dingtalkworkflow_1_0.CreateIntegratedTaskHeaders({ });
    createIntegratedTaskHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let featureConfigFeatures0Callback = new dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback({
      appUuid: '开发组织的corpId',
      apiKey: '数据源配置后生成的apiKey',
      version: '1',
    });
    let featureConfigFeatures0 = new dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfigFeatures({
      name: 'CUSTOM_SHORTCUT',
      pcUrl: 'www.dingtalk.com',
      mobileUrl: 'www.dingtalk.com',
      runType: 'REDIRECT',
      callback: featureConfigFeatures0Callback,
      config: '{"shortcutStyle":"EXECUTE_ACTION",       "buttonConfig":{"agreeBtn":"{{\'en_US\':\'test\',\'ja_JP\':\'test\',\'vi_VN\':\'test\',\'zh_CN\':\'测试\',\'zh_HK\':\'测试\',\'zh_TW\':\'测试\'}}","refuseBtn":"{{\'en_US\':\'test\',\'ja_JP\':\'test\',\'vi_VN\':\'test\',\'zh_CN\':\'测试\',\'zh_HK\':\'测试\',\'zh_TW\':\'测试\'}}"}}',
    });
    let featureConfig = new dingtalkworkflow_1_0.CreateIntegratedTaskRequestFeatureConfig({
      features: [
        featureConfigFeatures0
      ],
    });
    let tasks0 = new dingtalkworkflow_1_0.CreateIntegratedTaskRequestTasks({
      userId: 'manager001',
      url: 'https://www.dingtalk.com',
      customData: 'test***',
      dueTimestamp: 1758729600000,
    });
    let createIntegratedTaskRequest = new dingtalkworkflow_1_0.CreateIntegratedTaskRequest({
      processInstanceId: 'S3j8rbiNT1CsXXXXXV3Q1Q04431661334483',
      activityId: 'act_xxxxx',
      tasks: [
        tasks0
      ],
      featureConfig: featureConfig,
    });
    try {
      await client.createIntegratedTaskWithOptions(createIntegratedTaskRequest, createIntegratedTaskHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskHeaders createIntegratedTaskHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskHeaders();
            createIntegratedTaskHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig.CreateIntegratedTaskRequestFeatureConfigFeatures.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback featureConfigFeatures0Callback = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig.CreateIntegratedTaskRequestFeatureConfigFeatures.CreateIntegratedTaskRequestFeatureConfigFeaturesCallback
            {
                AppUuid = "开发组织的corpId",
                ApiKey = "数据源配置后生成的apiKey",
                Version = "1",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig.CreateIntegratedTaskRequestFeatureConfigFeatures featureConfigFeatures0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig.CreateIntegratedTaskRequestFeatureConfigFeatures
            {
                Name = "CUSTOM_SHORTCUT",
                PcUrl = "www.dingtalk.com",
                MobileUrl = "www.dingtalk.com",
                RunType = "REDIRECT",
                Callback = featureConfigFeatures0Callback,
                Config = "{\"shortcutStyle\":\"EXECUTE_ACTION\",       \"buttonConfig\":{\"agreeBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\",\"refuseBtn\":\"{{'en_US':'test','ja_JP':'test','vi_VN':'test','zh_CN':'测试','zh_HK':'测试','zh_TW':'测试'}}\"}}",
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig featureConfig = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig
            {
                Features = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestFeatureConfig.CreateIntegratedTaskRequestFeatureConfigFeatures>
                {
                    featureConfigFeatures0
                },
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks tasks0 = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks
            {
                UserId = "manager001",
                Url = "https://www.dingtalk.com",
                CustomData = "test***",
                DueTimestamp = 1758729600000,
            };
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest createIntegratedTaskRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest
            {
                ProcessInstanceId = "S3j8rbiNT1CsXXXXXV3Q1Q04431661334483",
                ActivityId = "act_xxxxx",
                Tasks = new List<AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.CreateIntegratedTaskRequest.CreateIntegratedTaskRequestTasks>
                {
                    tasks0
                },
                FeatureConfig = featureConfig,
            };
            try
            {
                client.CreateIntegratedTaskWithOptions(createIntegratedTaskRequest, createIntegratedTaskHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Array | 返回结果列表。 |
| taskId | Long | OA审批任务ID。 |
| userId | String | OA审批任务执行人用户userId。 |
| success | Boolean | 是否创建成功，true表示成功。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : [ {
    "taskId" : 1234567,
    "userId" : "manager001"
  } ],
  "success" : true
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | integrated.concurrency.error | 不支持并发创建任务和实例，请稍后再试 | 不支持并发创建任务和实例，请稍后再试 |
| 400 | integrated.state.invalid | 流程实例已完结，不能继续创建任务 | 流程实例已完结，不能继续创建任务 |
| 400 | integrated.number.exceed | 流程任务的数量到达上限 | 流程任务的数量到达上限 |
| 400 | integrated.qps.exceed | 本接口调用次数超过今日上限，请明日再试 | 本接口调用次数超过今日上限，请明日再试 |
| 400 | integrated.state.invalid | 流程实例不存在 | 流程实例不存在 |
| 400 | internalError | %s | 系统内部异常 |
| 400 | process.inst.notExist | 审批单不存在或已删除 | 审批单不存在或已删除 |
| 400 | setup.no.permission | 没有操作审批流的权限，请检查审批实例是否正确 | 没有操作审批流的权限，请检查审批实例是否正确 |
| 400 | tasks.is.null | 参数错误，任务列表tasks不能为空 | 参数错误，任务列表tasks不能为空 |
| 400 | task.url.error | 任务列表tasks中url长度不能超过1024字符 | 任务列表tasks中url长度不能超过1024字符 |
| 400 | task.dueTime.error | 任务列表tasks中截止时间dueTimestamp不能小于当前任务创建时间 | 任务列表tasks中截止时间dueTimestamp不能小于当前任务创建时间 |
| 500 | system.error | 系统错误 | 系统错误 |
