---
title: "智能人事员工调岗"
source_url: "https://open.dingtalk.com/document/development/intelligent-personnel-staff-transfer"
namespace: "development"
slug: "intelligent-personnel-staff-transfer"
group: "应用开发"
tab: "服务端API"
breadcrumb: "智能人事 > 员工关系 > 智能人事员工调岗"
doc_id: "EOtxyB2KRO"
updated_at: "2026-07-14 09:22:32"
---

> Source: https://open.dingtalk.com/document/development/intelligent-personnel-staff-transfer
> Path: 应用开发 / 服务端API / 智能人事 > 员工关系 > 智能人事员工调岗
> Updated: 2026-07-14 09:22:32

# 智能人事员工调岗

调用本接口，给智能人事员工调岗，支持以下内容调整，如员工部门列表、主部门、职务、职位和职级。

## **接口调用说明**

调用本接口前，需要对智能人事产品进行升级。智能人事升级职位管理功能后，需注意：

- 调用通讯录[更新用户信息v1](1457-update-user-details.md)接口和[更新用户信息v2](0057-user-information-update.md)接口更新员工部门或者员工职位时，接口会出现报错，报错信息如下图所示：

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0512993871/p1087123.png)
- 如果需要更新员工部门或者员工职位，请参考使用[智能人事员工调岗](#)接口。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/hrm/processes/transfer |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Hrm.Process.ReadWrite-智能人事流程读写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 被调岗员工userId。 |
| deptIdsAfterTransfer | Array of Long | 否 | 部门ID。 |
| mainDeptIdAfterTransfer | Long | 否 | 员工调岗后的人事主部门ID。    主部门ID需要在当前员工所在的部门ID列表中或参数deptIdsAfterTransfer列表中。 |
| positionIdAfterTransfer | String | 否 | 员工调岗后的职位ID。  **[!NOTE]**  该参数的填写方式与是否升级职位有关，可参考下方[升级说明-职位](#2b77c5d261v0z)说明。   - 如果是未升级，该参数不传。 - 如果是已升级，该参数必填，可通过[获取企业职位列表](0934-obtain-enterprise-position-information.md)接口获取`positionId`。  如果智能人事升级职位管理功能，调用本接口调岗员工的职位，需要检查职位与部门的所属关系。参数deptIdsAfterTransfer内的部门ID必须是该职级设置的下属部门的子集。 |
| positionNameAfterTransfer | String | 否 | 员工调岗后的职位名称，长度最大124字符。是否升级职位，该参数填写方式不同，可参考下方[升级说明-职位](#2b77c5d261v0z)。  **[!NOTE]**  该参数的填写方式与是否升级职位有关，可参考下方[升级说明-职位](#2b77c5d261v0z)说明。   - 如果是未升级，该参数必填，请填写职位名称。 - 如果是已升级，该参数不传，会自动更新参数职位ID参数`positionIdAfterTransfer`对应的职位名称。 |
| rankIdAfterTransfer | String | 否 | 员工调岗后的职级ID。  **[!NOTE]**  该参数的填写方式与是否升级岗位职级有关，可参考下方[升级说明-岗位职级](#2b77c5d261v0z)说明。   - 如果是未升级，该参数不传。 - 如果是已升级，该参数必填，调用[获取企业职级列表](0935-obtain-enterprise-rank-information.md)接口获取rankId参数值。 |
| positionLevelAfterTransfer | String | 否 | 员工调岗后的职级名称，长度不超过64字符。  **[!NOTE]**  该参数的填写方式与是否升级岗位职级有关，可参考下方[升级说明-岗位职级](#2b77c5d261v0z)说明。   - 如果是未升级，该参数必填，请填写岗位职级名称。 - 如果是已升级，该参数不传，会自动更新参数职级ID参数`rankIdAfterTransfer`对应的职级名称。 |
| jobIdAfterTransfer | String | 否 | 员工调岗后的职务ID，调用[获取企业职务列表](0936-obtain-enterprise-title-information.md)接口获取jobId参数值。  **[!NOTE]**  使用该字段，需要升级职位管理，升级方式请参考下方[升级说明-职位](#2b77c5d261v0z)说明 |
| operateUserId | String | 否 | 操作人userId。 |

### 请求示例

HTTP

```
POST /v1.0/hrm/processes/transfer HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:xxxxx
Content-Type:application/json

{
  "userId" : "2332",
  "deptIdsAfterTransfer" : [ 123 ],
  "mainDeptIdAfterTransfer" : 123,
  "positionNameAfterTransfer" : "经理",
  "positionLevelAfterTransfer" : "L1",
  "jobIdAfterTransfer" : "aefadfadaewedad",
  "positionIdAfterTransfer" : "fasdfaddsadfa",
  "rankIdAfterTransfer" : "fasdfaddsadfa",
  "operateUserId" : "232312312"
}
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkhrm_1_0.*;
import com.aliyun.dingtalkhrm_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkhrm_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkhrm_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkhrm_1_0.Client client = Sample.createClient();
        HrmProcessTransferHeaders hrmProcessTransferHeaders = new HrmProcessTransferHeaders();
        hrmProcessTransferHeaders.xAcsDingtalkAccessToken = "<your access token>";
        HrmProcessTransferRequest hrmProcessTransferRequest = new HrmProcessTransferRequest()
                .setUserId("2332")
                .setDeptIdsAfterTransfer(java.util.Arrays.asList(
                    123L
                ))
                .setMainDeptIdAfterTransfer(123L)
                .setPositionNameAfterTransfer("经理")
                .setPositionLevelAfterTransfer("L1")
                .setJobIdAfterTransfer("aefadfadaewedad")
                .setPositionIdAfterTransfer("fasdfaddsadfa")
                .setRankIdAfterTransfer("fasdfaddsadfa")
                .setOperateUserId("232312312");
        try {
            client.hrmProcessTransferWithOptions(hrmProcessTransferRequest, hrmProcessTransferHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.hrm_1_0.client import Client as dingtalkhrm_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.hrm_1_0 import models as dingtalkhrm__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkhrm_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkhrm_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrm_process_transfer_headers = dingtalkhrm__1__0_models.HrmProcessTransferHeaders()
        hrm_process_transfer_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_transfer_request = dingtalkhrm__1__0_models.HrmProcessTransferRequest(
            user_id='2332',
            dept_ids_after_transfer=[
                123
            ],
            main_dept_id_after_transfer=123,
            position_name_after_transfer='经理',
            position_level_after_transfer='L1',
            job_id_after_transfer='aefadfadaewedad',
            position_id_after_transfer='fasdfaddsadfa',
            rank_id_after_transfer='fasdfaddsadfa',
            operate_user_id='232312312'
        )
        try:
            client.hrm_process_transfer_with_options(hrm_process_transfer_request, hrm_process_transfer_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        hrm_process_transfer_headers = dingtalkhrm__1__0_models.HrmProcessTransferHeaders()
        hrm_process_transfer_headers.x_acs_dingtalk_access_token = '<your access token>'
        hrm_process_transfer_request = dingtalkhrm__1__0_models.HrmProcessTransferRequest(
            user_id='2332',
            dept_ids_after_transfer=[
                123
            ],
            main_dept_id_after_transfer=123,
            position_name_after_transfer='经理',
            position_level_after_transfer='L1',
            job_id_after_transfer='aefadfadaewedad',
            position_id_after_transfer='fasdfaddsadfa',
            rank_id_after_transfer='fasdfaddsadfa',
            operate_user_id='232312312'
        )
        try:
            await client.hrm_process_transfer_with_options_async(hrm_process_transfer_request, hrm_process_transfer_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessTransferHeaders;
use AlibabaCloud\SDK\Dingtalk\Vhrm_1_0\Models\HrmProcessTransferRequest;
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
        $hrmProcessTransferHeaders = new HrmProcessTransferHeaders([]);
        $hrmProcessTransferHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $hrmProcessTransferRequest = new HrmProcessTransferRequest([
            "userId" => "2332",
            "deptIdsAfterTransfer" => [
                123
            ],
            "mainDeptIdAfterTransfer" => 123,
            "positionNameAfterTransfer" => "经理",
            "positionLevelAfterTransfer" => "L1",
            "jobIdAfterTransfer" => "aefadfadaewedad",
            "positionIdAfterTransfer" => "fasdfaddsadfa",
            "rankIdAfterTransfer" => "fasdfaddsadfa",
            "operateUserId" => "232312312"
        ]);
        try {
            $client->hrmProcessTransferWithOptions($hrmProcessTransferRequest, $hrmProcessTransferHeaders, new RuntimeOptions([]));
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
  dingtalkhrm_1_0  "github.com/alibabacloud-go/dingtalk/hrm_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkhrm_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkhrm_1_0.Client{}
  _result, _err = dingtalkhrm_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  hrmProcessTransferHeaders := &dingtalkhrm_1_0.HrmProcessTransferHeaders{}
  hrmProcessTransferHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  hrmProcessTransferRequest := &dingtalkhrm_1_0.HrmProcessTransferRequest{
    UserId: tea.String("2332"),
    DeptIdsAfterTransfer: []*int64{tea.Int(123)},
    MainDeptIdAfterTransfer: tea.Int64(123),
    PositionNameAfterTransfer: tea.String("经理"),
    PositionLevelAfterTransfer: tea.String("L1"),
    JobIdAfterTransfer: tea.String("aefadfadaewedad"),
    PositionIdAfterTransfer: tea.String("fasdfaddsadfa"),
    RankIdAfterTransfer: tea.String("fasdfaddsadfa"),
    OperateUserId: tea.String("232312312"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.HrmProcessTransferWithOptions(hrmProcessTransferRequest, hrmProcessTransferHeaders, &util.RuntimeOptions{})
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
import dingtalkhrm_1_0, * as $dingtalkhrm_1_0 from '@alicloud/dingtalk/hrm_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkhrm_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkhrm_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let hrmProcessTransferHeaders = new $dingtalkhrm_1_0.HrmProcessTransferHeaders({ });
    hrmProcessTransferHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let hrmProcessTransferRequest = new $dingtalkhrm_1_0.HrmProcessTransferRequest({
      userId: "2332",
      deptIdsAfterTransfer: [
        123
      ],
      mainDeptIdAfterTransfer: 123,
      positionNameAfterTransfer: "经理",
      positionLevelAfterTransfer: "L1",
      jobIdAfterTransfer: "aefadfadaewedad",
      positionIdAfterTransfer: "fasdfaddsadfa",
      rankIdAfterTransfer: "fasdfaddsadfa",
      operateUserId: "232312312",
    });
    try {
      await client.hrmProcessTransferWithOptions(hrmProcessTransferRequest, hrmProcessTransferHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkhrm_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkhrm_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTransferHeaders hrmProcessTransferHeaders = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTransferHeaders();
            hrmProcessTransferHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTransferRequest hrmProcessTransferRequest = new AlibabaCloud.SDK.Dingtalkhrm_1_0.Models.HrmProcessTransferRequest
            {
                UserId = "2332",
                DeptIdsAfterTransfer = new List<long?>
                {
                    123
                },
                MainDeptIdAfterTransfer = 123,
                PositionNameAfterTransfer = "经理",
                PositionLevelAfterTransfer = "L1",
                JobIdAfterTransfer = "aefadfadaewedad",
                PositionIdAfterTransfer = "fasdfaddsadfa",
                RankIdAfterTransfer = "fasdfaddsadfa",
                OperateUserId = "232312312",
            };
            try
            {
                client.HrmProcessTransferWithOptions(hrmProcessTransferRequest, hrmProcessTransferHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 是否调岗成功：   - **true**：成功 - **false**：失败 |

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
| 400 | ranIdInvalid | 职级id不合法 | 职级id不合法 |
| 400 | mainDeptIdInvalid | 传入主部门id有误 | 传入主部门id有误 |
| 400 | rankIdAgainstConstraint | 职位和职级违法绑定约束 | 职位和职级违法绑定约束 |
| 400 | positionIdInvalid | 职位id不合法 | 职位id不合法 |
| 400 | positioinAgainstConstraint | 职位和主部门违反绑定约束 | 职位和主部门违反绑定约束 |
| 400 | suiteCallInvalid | 企业没有开通微应用 | 企业没有开通微应用 |
| 400 | invokeFrequentyly | 调用频繁 | 调用频繁 |
| 400 | invalidParameter | 参数错误 | 参数错误 |
| 400 | noPermission | 无权限访问 | 无权限访问 |
| 500 | systemError | 系统异常 | 系统异常 |

## **升级说明**

### **职位**

升级方式有两种，如下：

> **[!NOTE]**
>
> 如果职位是**文本类型**，表示**未升级**。

- 方式一：升级职位字段。如下图所示。

  ![](https://img.alicdn.com/imgextra/i1/O1CN01abV6gy29xQM9waVaT_!!6000000008134-2-tps-2298-1316.png)
- 方式二：升级职位管理。如下图所示。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2512993871/p1087128.png)

### **岗位职级**

升级方式有两种，如下：

> **[!NOTE]**
>
> 如果**岗位职级**是文本类型，表示未升级。

- 方式一：升级**岗位职级**字段。如下图所示。

  ![](https://img.alicdn.com/imgextra/i1/O1CN01c5Wmd121dFzJkzcFe_!!6000000007007-2-tps-2394-1470.png)
- 方式二：升级职位管理。如下图所示。

  ![image](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/2512993871/p1087146.png)
