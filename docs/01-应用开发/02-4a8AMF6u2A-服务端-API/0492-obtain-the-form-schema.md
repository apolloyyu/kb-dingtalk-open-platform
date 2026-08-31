---
title: "获取表单 schema"
source_url: "https://open.dingtalk.com/document/development/obtain-the-form-schema"
namespace: "development"
slug: "obtain-the-form-schema"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "OA 审批 > 官方 OA 审批 > 审批表单 > 获取表单 schema"
doc_id: "0FcWJCMDIi"
updated_at: "2026-06-03 10:12:21"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-form-schema
> Path: 应用开发 / 服务端 API / OA 审批 > 官方 OA 审批 > 审批表单 > 获取表单 schema
> Updated: 2026-06-03 10:12:21

# 获取表单 schema

调用本接口，通过 processCode，获取对应表单的 schema 信息。

## 接口调用说明

第三方企业应用没有权限获取组织内的表单schema。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/workflow/forms/schemas/processCodes |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-Workflow.Form.Read-工作流模板读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| processCode | String | 是 | 表单的唯一码，，调用[创建或更新审批表单模板](0491-create-an-approval-form-template.md)接口或[OA审批概述-名词解释](0473-workflow-overview.md)获取。 |
| appUuid | String | 否 | 应用搭建隔离信息。 |

### 请求示例

HTTP

```
GET /v1.0/workflow/forms/schemas/processCodes?processCode=PROC-17428B8C-6C60-xxxx-924C-64F1037AE067&appUuid=SWAPP-abcd-example HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:f31f78b59d9438b9859e40xxxx9882f0
Content-Type:application/json
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
    public static com.aliyun.dingtalkworkflow_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkworkflow_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkworkflow_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeHeaders querySchemaByProcessCodeHeaders = new com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeHeaders();
        querySchemaByProcessCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeRequest querySchemaByProcessCodeRequest = new com.aliyun.dingtalkworkflow_1_0.models.QuerySchemaByProcessCodeRequest()
                .setProcessCode("PROC-17428B8C-6C60-xxxx-924C-64F1037AE067")
                .setAppUuid("SWAPP-abcd-example");
        try {
            client.querySchemaByProcessCodeWithOptions(querySchemaByProcessCodeRequest, querySchemaByProcessCodeHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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
        query_schema_by_process_code_headers = dingtalkworkflow__1__0_models.QuerySchemaByProcessCodeHeaders()
        query_schema_by_process_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_schema_by_process_code_request = dingtalkworkflow__1__0_models.QuerySchemaByProcessCodeRequest(
            process_code='PROC-17428B8C-6C60-xxxx-924C-64F1037AE067',
            app_uuid='SWAPP-abcd-example'
        )
        try:
            client.query_schema_by_process_code_with_options(query_schema_by_process_code_request, query_schema_by_process_code_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        query_schema_by_process_code_headers = dingtalkworkflow__1__0_models.QuerySchemaByProcessCodeHeaders()
        query_schema_by_process_code_headers.x_acs_dingtalk_access_token = '<your access token>'
        query_schema_by_process_code_request = dingtalkworkflow__1__0_models.QuerySchemaByProcessCodeRequest(
            process_code='PROC-17428B8C-6C60-xxxx-924C-64F1037AE067',
            app_uuid='SWAPP-abcd-example'
        )
        try:
            await client.query_schema_by_process_code_with_options_async(query_schema_by_process_code_request, query_schema_by_process_code_headers, util_models.RuntimeOptions())
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
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\QuerySchemaByProcessCodeHeaders;
use AlibabaCloud\SDK\Dingtalk\Vworkflow_1_0\Models\QuerySchemaByProcessCodeRequest;
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
        $querySchemaByProcessCodeHeaders = new QuerySchemaByProcessCodeHeaders([]);
        $querySchemaByProcessCodeHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $querySchemaByProcessCodeRequest = new QuerySchemaByProcessCodeRequest([
            "processCode" => "PROC-17428B8C-6C60-xxxx-924C-64F1037AE067",
            "appUuid" => "SWAPP-abcd-example"
        ]);
        try {
            $client->querySchemaByProcessCodeWithOptions($querySchemaByProcessCodeRequest, $querySchemaByProcessCodeHeaders, new RuntimeOptions([]));
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
  dingtalkworkflow_1_0  "github.com/alibabacloud-go/dingtalk/workflow_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
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

  querySchemaByProcessCodeHeaders := &dingtalkworkflow_1_0.QuerySchemaByProcessCodeHeaders{}
  querySchemaByProcessCodeHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  querySchemaByProcessCodeRequest := &dingtalkworkflow_1_0.QuerySchemaByProcessCodeRequest{
    ProcessCode: tea.String("PROC-17428B8C-6C60-xxxx-924C-64F1037AE067"),
    AppUuid: tea.String("SWAPP-abcd-example"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.QuerySchemaByProcessCodeWithOptions(querySchemaByProcessCodeRequest, querySchemaByProcessCodeHeaders, &util.RuntimeOptions{})
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
import dingtalkworkflow_1_0, * as $dingtalkworkflow_1_0 from '@alicloud/dingtalk/workflow_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkworkflow_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkworkflow_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let querySchemaByProcessCodeHeaders = new $dingtalkworkflow_1_0.QuerySchemaByProcessCodeHeaders({ });
    querySchemaByProcessCodeHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let querySchemaByProcessCodeRequest = new $dingtalkworkflow_1_0.QuerySchemaByProcessCodeRequest({
      processCode: "PROC-17428B8C-6C60-xxxx-924C-64F1037AE067",
      appUuid: "SWAPP-abcd-example",
    });
    try {
      await client.querySchemaByProcessCodeWithOptions(querySchemaByProcessCodeRequest, querySchemaByProcessCodeHeaders, new $Util.RuntimeOptions({ }));
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
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QuerySchemaByProcessCodeHeaders querySchemaByProcessCodeHeaders = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QuerySchemaByProcessCodeHeaders();
            querySchemaByProcessCodeHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QuerySchemaByProcessCodeRequest querySchemaByProcessCodeRequest = new AlibabaCloud.SDK.Dingtalkworkflow_1_0.Models.QuerySchemaByProcessCodeRequest
            {
                ProcessCode = "PROC-17428B8C-6C60-xxxx-924C-64F1037AE067",
                AppUuid = "SWAPP-abcd-example",
            };
            try
            {
                client.QuerySchemaByProcessCodeWithOptions(querySchemaByProcessCodeRequest, querySchemaByProcessCodeHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 返回结果详情。 |
| creatorUserId | String | 创建人 userId。 |
| appUuid | String | 表单应用 uuid 或者 corpId。 |
| formCode | String | 表单的唯一码。 |
| formUuid | String | 表单 uuid。 |
| name | String | 表单名称。 |
| memo | String | 说明文案。 |
| ownerIdType | String | 数据归属者的 id 类型，取值：   - orgId：企业 - cid：群 - uid：人 |
| schemaContent | Object | 表单 schema 详情。 |
| title | String | 表单名称。 |
| icon | String | 图标 |
| items | Array | 控件列表。 |
| componentName | String | 控件类型，取值：   - TextField：单行输入框 - TextareaField：多行输入框 - NumberField：数字输入框 - DDSelectField：单选框 - DDMultiSelectField：多选框 - DDDateField：日期控件 - DDDateRangeField：时间区间控件 - TextNote：文字说明控件 - PhoneField：电话控件 - DDPhotoField：图片控件 - MoneyField：金额控件 - TableField：明细控件 - DDAttachment：附件 - InnerContactField：联系人控件 - DepartmentField：部门控件 - RelateField：关联审批单 - AddressField：省市区控件 - StarRatingField：评分控件 - FormRelateField：关联控件 |
| props | Object | 控件属性。 |
| id | String | 控件 id。 |
| tableViewMode | String | 明细填写方式，枚举值：   - list：列表 - table：表格 |
| label | String | 控件名称。 |
| bizAlias | String | 控件业务自定义别名。 |
| required | Boolean | 是否必填，取值：   - true：是 - false：否 |
| placeholder | String | 占位符。 |
| options | Array of String | 单选框选项值。 |
| appId | Long | ISV 微应用 appId，用于ISV身份权限识别，ISV可获得相应数据。 |
| durationLabel | String | 兼容字段。 |
| pushToCalendar | Integer | 是否推送管理日历(DDDateRangeField, 该属性为兼容保留)，取值：   - 1：推送 - 0：不推送 |
| align | String | textNote的样式，取值：   - top：顶部 - middle：中部 - bottom：底部 |
| statField | Array | 需要计算总和的明细组件。 |
| id | String | id 值。 |
| label | String | 名称。 |
| upper | Boolean | 是否大写，取值：   - true：是 - false：否 |
| unit | String | 单位。 |
| hideLabel | Boolean | 加班套件4.0新增，加班明细是否隐藏标签，取值：   - true：是 - false：否 |
| objOptions | Array | 选项内容列表，提供给业务方更多的选择器操作。 |
| value | String | 选项值。 |
| format | String | 时间格式(DDDateField和DDDateRangeField)。 |
| pushToAttendance | Boolean | 是否推送到考勤, 子类型(DDSelectField)，取值：   - true：是 - false：否 |
| labelEditableFreeze | Boolean | label是否可修改，取值：   - true：不可修改 - false：可修改 |
| push | Object | 同步到考勤, 表示是否设置为员工状态。 |
| pushSwitch | Integer | 开启状态，取值：   - 1：开启 - 0：关闭 |
| pushTag | String | 状态显示名称 |
| attendanceRule | Integer | 考勤类型，取值：   - 1：请假 - 2：出差 - 3：加班 - 4：外出 |
| commonBizType | String | common field的commonBizType。 |
| requiredEditableFreeze | Boolean | 必填是否可修改，取值：   - true：不可修改 - false：可修改 |
| unit | String | 数字组件/日期区间组件单位属性。 |
| extract | Boolean | 套件值是否打平，取值：   - true：是 - false：否 |
| link | String | 说明文案的链接地址。 |
| payEnable | Boolean | 是否有支付属性，取值：   - true：是 - false：否 |
| hidden | Boolean | 加班套件4.0新增 加班明细是否隐藏，取值：   - true：是 - false：否 |
| bizType | String | 业务套件类型。 |
| staffStatusEnabled | Boolean | 是否开启员工状态，取值：   - true：是 - false：否 |
| actionName | String | 加班套件4.0新增 加班明细名称。 |
| attendTypeLabel | String | 请假、出差、外出、加班类型标签。 |
| childFieldVisible | Map<String, Boolean> | 套件内子组件可见性，取值：   - true：是 - false：否 |
|  | Boolean | 套件内子组件可见性，取值：   - true：是 - false：否 |
| notPrint | String | 是否参与打印，取值：   - 1：不打印 - 0：打印 |
| verticalPrint | Boolean | 明细打印排版方式，取值：   - true：纵向 - false：横向 |
| duration | Boolean | 是否自动计算时长，取值：   - true：是 - false：否 |
| holidayOptions | Array of Object | 兼容出勤套件类型。 |
| useCalendar | Boolean | 是否使用考勤日历，取值：   - true：是 - false：否 |
| hiddenInApprovalDetail | Boolean | textnote在详情页是否隐藏，取值：   - true：是 - false：否 |
| disabled | Boolean | 是否可编辑，取值：   - true：是 - false：否 |
| asyncCondition | Boolean | 套件是否开启异步获取分条件规则，取值：   - true：是 - false：否 |
| behaviorLinkage | Array | 表单关联控件列表。 |
| value | String | 控件值。 |
| targets | Array | 关联控件列表。 |
| fieldId | String | 字段 id。 |
| behavior | String | 行为。 |
| showAttendOptions | Boolean | 兼容出勤套件类型。 |
| notUpper | String | 是否需要大写，默认是需要，取值：   - 1：不需要 - 0 或空：需要 |
| fieldsInfo | String | 关联表单中的fields存储 |
| eSign | Boolean | e签宝专用标识。 |
| mainTitle | String | 加班套件4.0新增 加班明细描述。 |
| formula | String | 公式。 |
| choice | Integer | 内部联系人choice，取值：   - 1：多选 - 0：单选 |
| children | Array | 子控件列表。 |
| componentName | String | 子控件类型，取值：   - TextField：单行输入框 - TextareaField：多行输入框 - NumberField：数字输入框 - DDSelectField：单选框 - DDMultiSelectField：多选框 - DDDateField：日期控件 - DDDateRangeField：时间区间控件 - TextNote：文字说明控件 - PhoneField：电话控件 - DDPhotoField：图片控件 - MoneyField：金额控件 - DDAttachment：附件 - InnerContactField：联系人控件 - DepartmentField：部门控件 - RelateField：关联审批单 - AddressField：省市区控件 - StarRatingField：评分控件 - FormRelateField：关联控件 |
| props | Object | 子控件属性 |
| id | String | 控件id |
| label | String | 控件名称 |
| bizAlias | String | 控件业务别名 |
| required | Boolean | 是否必填 |
| options | Array of String | 单选框选项值。 |
| icon | String | 图标。 |
| appType | Integer | 表单类型。 |
| bizType | String | 代表表单业务含义的类型。 |
| engineType | Integer | 引擎类型，取值：   - 1：页面 - 0：表单 |
| status | String | 状态，取值：   - PUBLISHED：启用 - INVALID：停用 - SAVED：草稿 |
| listOrder | Integer | 排序 id。 |
| customSetting | String | 业务自定义设置数据。 |
| procType | String | 目标类型，取值：   - inner：内部 - outer：外部 - customer：自定义 |
| visibleRange | String | 可见范围类型。 |
| gmtCreate | String | 创建时间的时间戳。 |
| gmtModified | String | 修改时间的时间戳。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "result" : {
    "creatorUserId" : "26652461xxxx5992",
    "appUuid" : "xxxx",
    "formCode" : "PROC-17428B8C-6C60-470E-xxxx-64F1037AE067",
    "formUuid" : "FORM-28215C3E-00E3-4118-xxxx-4091F828AF2F",
    "name" : "示例模板",
    "memo" : "xxxx",
    "ownerIdType" : "orgId",
    "schemaContent" : {
      "title" : "示例模板",
      "icon" : "common",
      "items" : [ {
        "componentName" : "TextField",
        "props" : {
          "id" : "TextField-K2AD4O5B",
          "label" : "单行输入框",
          "bizAlias" : "我的单行输入框",
          "required" : true,
          "placeholder" : "请输入文字",
          "options" : [ "选项1" ],
          "appId" : 1234567,
          "durationLabel" : "xxxx",
          "pushToCalendar" : 1,
          "align" : "top",
          "statField" : [ {
            "id" : "TextField-K2AD4O5B",
            "label" : "单行输入框",
            "upper" : true,
            "unit" : "xxxx"
          } ],
          "hideLabel" : true,
          "objOptions" : [ {
            "value" : "xxxx"
          } ],
          "format" : "yyyy-MM-dd",
          "pushToAttendance" : true,
          "labelEditableFreeze" : true,
          "push" : {
            "pushSwitch" : 1,
            "pushTag" : "xxxx",
            "attendanceRule" : 1
          },
          "commonBizType" : "xxxx",
          "requiredEditableFreeze" : true,
          "unit" : "天",
          "extract" : true,
          "link" : "xxxx",
          "payEnable" : true,
          "hidden" : true,
          "bizType" : "hrm.xxxx",
          "staffStatusEnabled" : true,
          "actionName" : "添加",
          "attendTypeLabel" : "请假",
          "childFieldVisible" : {
            "key" : true
          },
          "notPrint" : "1",
          "verticalPrint" : true,
          "duration" : true,
          "holidayOptions" : [ {
            "key" : "xxxx"
          } ],
          "useCalendar" : true,
          "hiddenInApprovalDetail" : true,
          "disabled" : true,
          "asyncCondition" : true,
          "behaviorLinkage" : [ {
            "value" : "xxxx",
            "targets" : [ {
              "fieldId" : "TextField-K2AD4O5B",
              "behavior" : "xxxx"
            } ]
          } ],
          "showAttendOptions" : true,
          "notUpper" : "1",
          "fieldsInfo" : "xxxx",
          "eSign" : true,
          "mainTitle" : "xxxx",
          "formula" : "xxxx",
          "choice" : 1
        },
        "children" : [ {
          "componentName" : "TextField",
          "props" : {
            "id" : "TextField-abcd",
            "label" : "姓名",
            "bizAlias" : "userName",
            "required" : true
          }
        } ]
      } ]
    },
    "icon" : "null",
    "appType" : 0,
    "bizType" : "hrm.xxxx",
    "engineType" : 0,
    "status" : "PUBLISHED",
    "listOrder" : 1,
    "customSetting" : "null",
    "procType" : "inner",
    "visibleRange" : "PRIVATE",
    "gmtCreate" : "1638326995000",
    "gmtModified" : "1640344585000"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | formNotExist | 审批表单模板不存在 | 审批表单模板不存在 |
| 400 | invalidParameter | 参数错误，具体可能为：企业ID、审批模板code等参数错误 | 参数错误，具体可能为：企业ID、审批模板code等参数错误 |
| 400 | noPermission | 没有权限访问当前表单 | 权限校验失败 |
| 400 | aflowProcessCodeIsError | 获取审批模板失败或审批模板已被删除 | 获取审批模板失败或审批模板已被删除 |
| 400 | internalError | %s | 系统内部异常 |
| 500 | systemError | 系统异常 | 系统异常 |
