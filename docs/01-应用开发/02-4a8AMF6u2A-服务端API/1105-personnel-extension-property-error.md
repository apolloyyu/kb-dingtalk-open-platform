---
title: "保存人员扩展属性"
source_url: "https://open.dingtalk.com/document/development/personnel-extension-property-error"
namespace: "development"
slug: "personnel-extension-property-error"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 医疗 > 保存人员扩展属性"
doc_id: "KedOSpXqUy"
updated_at: "2025-09-23 19:22:18"
---

> Source: https://open.dingtalk.com/document/development/personnel-extension-property-error
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 医疗 > 保存人员扩展属性
> Updated: 2025-09-23 19:22:18

# 保存人员扩展属性

支持保存人员扩展属性。已有的属性包括职称、状态、备注等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/industry/medicals/users/{userId}/extends |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Medical.ContactExt.Write-医疗通讯录拓展信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 发起请求的用户的userid。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userExtendKey | String | 是 | 用户拓展字段key，最大长度32字符。   - **Job**：职称。 - **UserProb**：属性。 |
| userExtendValue | String | 是 | 用户扩展字段value，最大长度128字符。   - 当**userExtendKey**取值为**Job**时，**userExtendValue**取值为：    - **1**：主任医师。   - **2**：副主任医师。   - **3**：主治医师。   - **4**：住院医师。   - **5**：尚未考医师职称。   - **6**：主任药师。   - **7**：副主任药师。   - **8**：主管药师。   - **9**：药师。   - **10**：药士。   - **11**：主任护师。   - **12**：副主任护师。   - **13**：主管护师。   - **14**：护师。   - **15**：护士。   - **16**：主任技师。   - **17**：副主任技师。   - **18**：主管技师。   - **19**：技师。   - **20**：技士。 - 当**userExtendKey**取值为**UserProb**时，**userExtendValue**取值为：    - **0**：其他。   - **1**：本院。   - **2**：外院。   - **5**：外院（博士后）。   - **6**：外院（进修）。   - **7**：外院（外校生）。   - **8**：外院（研究生）。   - **9**：外院（住培）。   - **10**：外院（专培）。 |
| userDisplayName | String | 否 | 字段展示名称最大长度256字符。 |

### 请求示例

HTTP

```
POST /v1.0/industry/medicals/users/323xxx/extends?userExtendKey=Job&userExtendValue=1&userDisplayName=Job HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:76exxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkindustry_1_0.*;
import com.aliyun.dingtalkindustry_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkindustry_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkindustry_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkindustry_1_0.Client client = Sample.createClient();
        SaveUserExtendValuesHeaders saveUserExtendValuesHeaders = new SaveUserExtendValuesHeaders();
        saveUserExtendValuesHeaders.xAcsDingtalkAccessToken = "<your access token>";
        SaveUserExtendValuesRequest saveUserExtendValuesRequest = new SaveUserExtendValuesRequest()
                .setUserExtendKey("Job")
                .setUserExtendValue("1")
                .setUserDisplayName("Job");
        try {
            client.saveUserExtendValuesWithOptions("323xxx", saveUserExtendValuesRequest, saveUserExtendValuesHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.industry_1_0.client import Client as dingtalkindustry_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.industry_1_0 import models as dingtalkindustry__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkindustry_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkindustry_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        save_user_extend_values_headers = dingtalkindustry__1__0_models.SaveUserExtendValuesHeaders()
        save_user_extend_values_headers.x_acs_dingtalk_access_token = '<your access token>'
        save_user_extend_values_request = dingtalkindustry__1__0_models.SaveUserExtendValuesRequest(
            user_extend_key='Job',
            user_extend_value='1',
            user_display_name='Job'
        )
        try:
            client.save_user_extend_values_with_options('323xxx', save_user_extend_values_request, save_user_extend_values_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        save_user_extend_values_headers = dingtalkindustry__1__0_models.SaveUserExtendValuesHeaders()
        save_user_extend_values_headers.x_acs_dingtalk_access_token = '<your access token>'
        save_user_extend_values_request = dingtalkindustry__1__0_models.SaveUserExtendValuesRequest(
            user_extend_key='Job',
            user_extend_value='1',
            user_display_name='Job'
        )
        try:
            await client.save_user_extend_values_with_options_async('323xxx', save_user_extend_values_request, save_user_extend_values_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Models\SaveUserExtendValuesHeaders;
use AlibabaCloud\SDK\Dingtalk\Vindustry_1_0\Models\SaveUserExtendValuesRequest;
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
        $saveUserExtendValuesHeaders = new SaveUserExtendValuesHeaders([]);
        $saveUserExtendValuesHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $saveUserExtendValuesRequest = new SaveUserExtendValuesRequest([
            "userExtendKey" => "Job",
            "userExtendValue" => "1",
            "userDisplayName" => "Job"
        ]);
        try {
            $client->saveUserExtendValuesWithOptions("323xxx", $saveUserExtendValuesRequest, $saveUserExtendValuesHeaders, new RuntimeOptions([]));
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
  dingtalkindustry_1_0  "github.com/alibabacloud-go/dingtalk/industry_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkindustry_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkindustry_1_0.Client{}
  _result, _err = dingtalkindustry_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  saveUserExtendValuesHeaders := &dingtalkindustry_1_0.SaveUserExtendValuesHeaders{}
  saveUserExtendValuesHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  saveUserExtendValuesRequest := &dingtalkindustry_1_0.SaveUserExtendValuesRequest{
    UserExtendKey: tea.String("Job"),
    UserExtendValue: tea.String("1"),
    UserDisplayName: tea.String("Job"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.SaveUserExtendValuesWithOptions(tea.String("323xxx"), saveUserExtendValuesRequest, saveUserExtendValuesHeaders, &util.RuntimeOptions{})
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
import dingtalkindustry_1_0, * as $dingtalkindustry_1_0 from '@alicloud/dingtalk/industry_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkindustry_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkindustry_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let saveUserExtendValuesHeaders = new $dingtalkindustry_1_0.SaveUserExtendValuesHeaders({ });
    saveUserExtendValuesHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let saveUserExtendValuesRequest = new $dingtalkindustry_1_0.SaveUserExtendValuesRequest({
      userExtendKey: "Job",
      userExtendValue: "1",
      userDisplayName: "Job",
    });
    try {
      await client.saveUserExtendValuesWithOptions("323xxx", saveUserExtendValuesRequest, saveUserExtendValuesHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkindustry_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkindustry_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.SaveUserExtendValuesHeaders saveUserExtendValuesHeaders = new AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.SaveUserExtendValuesHeaders();
            saveUserExtendValuesHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.SaveUserExtendValuesRequest saveUserExtendValuesRequest = new AlibabaCloud.SDK.Dingtalkindustry_1_0.Models.SaveUserExtendValuesRequest
            {
                UserExtendKey = "Job",
                UserExtendValue = "1",
                UserDisplayName = "Job",
            };
            try
            {
                client.SaveUserExtendValuesWithOptions("323xxx", saveUserExtendValuesRequest, saveUserExtendValuesHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkindustry__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkindustry_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkindustry_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkindustry_1_0::Client> client = make_shared<Alibabacloud_Dingtalkindustry_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkindustry_1_0::SaveUserExtendValuesHeaders> saveUserExtendValuesHeaders = make_shared<Alibabacloud_Dingtalkindustry_1_0::SaveUserExtendValuesHeaders>();
  saveUserExtendValuesHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkindustry_1_0::SaveUserExtendValuesRequest> saveUserExtendValuesRequest = make_shared<Alibabacloud_Dingtalkindustry_1_0::SaveUserExtendValuesRequest>(map<string, boost::any>({
    {"userExtendKey", boost::any(string("Job"))},
    {"userExtendValue", boost::any(string("1"))},
    {"userDisplayName", boost::any(string("Job"))}
  }));
  try {
    client->saveUserExtendValuesWithOptions(make_shared<string>("323xxx"), saveUserExtendValuesRequest, saveUserExtendValuesHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
  }
  catch (std::exception &err) {
    if (!Darabonba_Util::Client::empty(err.code) && !Darabonba_Util::Client::empty(err.message)) {
      // err 中含有 code 和 message 属性，可帮助开发定位问题
    }
  }
}
```

## 响应

### 响应体

| 名称 | 类型 | 描述 |
| --- | --- | --- |
| success | Boolean | 调用是否成功。 |

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
| 200 | staff.not.found | 钉钉员工不存在 | 钉钉员工不存在 |
| 400 | invalid.parameter | invalidParameter | 参数非法 |
| 500 | system.error | system error %s | 系统错误 |
