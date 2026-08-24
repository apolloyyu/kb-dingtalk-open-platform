---
title: "删除学生"
source_url: "https://open.dingtalk.com/document/development/delete-student"
namespace: "development"
slug: "delete-student"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 删除学生"
doc_id: "6rmxsIhhhr"
updated_at: "2026-06-04 19:11:26"
---

> Source: https://open.dingtalk.com/document/development/delete-student
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 删除学生
> Updated: 2026-06-04 19:11:26

# 删除学生

调用本接口，删除学生。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/edu/classes/{classId}/students/{userId} |
| HTTP Method | DELETE |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-教育行业扩展通讯录写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| classId | Long | 是 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| userId | String | 是 | 学生的userId，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取userid参数值。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| operator | String | 是 | 操作人userId，可调用[通过免登码获取用户信息](0024-obtain-the-userid-of-a-user-by-using-the-log-free.md)接口获取userid参数值。 |

### 请求示例

HTTP

```
DELETE /v1.0/edu/classes/12345/students/stu123?operator=manager123456 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:638bab94c8xxxx
Content-Type:application/json
```

Java

```
// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.sample;

import com.aliyun.tea.*;
import com.aliyun.teautil.*;
import com.aliyun.teautil.models.*;
import com.aliyun.dingtalkedu_1_0.*;
import com.aliyun.dingtalkedu_1_0.models.*;
import com.aliyun.teaopenapi.*;
import com.aliyun.teaopenapi.models.*;

public class Sample {

    /**
     * 使用 Token 初始化账号Client
     * @return Client
     * @throws Exception
     */
    public static com.aliyun.dingtalkedu_1_0.Client createClient() throws Exception {
        Config config = new Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkedu_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkedu_1_0.Client client = Sample.createClient();
        DeleteStudentHeaders deleteStudentHeaders = new DeleteStudentHeaders();
        deleteStudentHeaders.xAcsDingtalkAccessToken = "<your access token>";
        DeleteStudentRequest deleteStudentRequest = new DeleteStudentRequest()
                .setOperator("manager123456");
        try {
            client.deleteStudentWithOptions("12345", "stu123", deleteStudentRequest, deleteStudentHeaders, new RuntimeOptions());
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

from alibabacloud_dingtalk.edu_1_0.client import Client as dingtalkedu_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.edu_1_0 import models as dingtalkedu__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkedu_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkedu_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_student_headers = dingtalkedu__1__0_models.DeleteStudentHeaders()
        delete_student_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_student_request = dingtalkedu__1__0_models.DeleteStudentRequest(
            operator='manager123456'
        )
        try:
            client.delete_student_with_options('12345', 'stu123', delete_student_request, delete_student_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        delete_student_headers = dingtalkedu__1__0_models.DeleteStudentHeaders()
        delete_student_headers.x_acs_dingtalk_access_token = '<your access token>'
        delete_student_request = dingtalkedu__1__0_models.DeleteStudentRequest(
            operator='manager123456'
        )
        try:
            await client.delete_student_with_options_async('12345', 'stu123', delete_student_request, delete_student_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\DeleteStudentHeaders;
use AlibabaCloud\SDK\Dingtalk\Vedu_1_0\Models\DeleteStudentRequest;
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
        $deleteStudentHeaders = new DeleteStudentHeaders([]);
        $deleteStudentHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $deleteStudentRequest = new DeleteStudentRequest([
            "operator" => "manager123456"
        ]);
        try {
            $client->deleteStudentWithOptions("12345", "stu123", $deleteStudentRequest, $deleteStudentHeaders, new RuntimeOptions([]));
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
  dingtalkedu_1_0  "github.com/alibabacloud-go/dingtalk/edu_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkedu_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkedu_1_0.Client{}
  _result, _err = dingtalkedu_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  deleteStudentHeaders := &dingtalkedu_1_0.DeleteStudentHeaders{}
  deleteStudentHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  deleteStudentRequest := &dingtalkedu_1_0.DeleteStudentRequest{
    Operator: tea.String("manager123456"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.DeleteStudentWithOptions(tea.String("12345"), tea.String("stu123"), deleteStudentRequest, deleteStudentHeaders, &util.RuntimeOptions{})
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
import dingtalkedu_1_0, * as $dingtalkedu_1_0 from '@alicloud/dingtalk/edu_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkedu_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkedu_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let deleteStudentHeaders = new $dingtalkedu_1_0.DeleteStudentHeaders({ });
    deleteStudentHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let deleteStudentRequest = new $dingtalkedu_1_0.DeleteStudentRequest({
      operator: "manager123456",
    });
    try {
      await client.deleteStudentWithOptions("12345", "stu123", deleteStudentRequest, deleteStudentHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkedu_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkedu_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkedu_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.DeleteStudentHeaders deleteStudentHeaders = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.DeleteStudentHeaders();
            deleteStudentHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkedu_1_0.Models.DeleteStudentRequest deleteStudentRequest = new AlibabaCloud.SDK.Dingtalkedu_1_0.Models.DeleteStudentRequest
            {
                Operator = "manager123456",
            };
            try
            {
                client.DeleteStudentWithOptions("12345", "stu123", deleteStudentRequest, deleteStudentHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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

#include <alibabacloud/dingtalkedu__1__0.hpp>
#include <alibabacloud/open_api.hpp>
#include <boost/any.hpp>
#include <darabonba/core.hpp>
#include <darabonba/util.hpp>
#include <iostream>
#include <map>

using namespace std;

Alibabacloud_Dingtalkedu_1_0::Client createClient() {
  shared_ptr<Alibabacloud_OpenApi::Config> config = make_shared<Alibabacloud_OpenApi::Config>();
  config->protocol = make_shared<string>("https");
  config->regionId = make_shared<string>("central");
  return Alibabacloud_Dingtalkedu_1_0::Client(config);
}

int main(int argc, char *args[]) {
  args++;
  shared_ptr<Alibabacloud_Dingtalkedu_1_0::Client> client = make_shared<Alibabacloud_Dingtalkedu_1_0::Client>(createClient());
  shared_ptr<Alibabacloud_Dingtalkedu_1_0::DeleteStudentHeaders> deleteStudentHeaders = make_shared<Alibabacloud_Dingtalkedu_1_0::DeleteStudentHeaders>();
  deleteStudentHeaders->xAcsDingtalkAccessToken = make_shared<string>("<your access token>");
  shared_ptr<Alibabacloud_Dingtalkedu_1_0::DeleteStudentRequest> deleteStudentRequest = make_shared<Alibabacloud_Dingtalkedu_1_0::DeleteStudentRequest>(map<string, boost::any>({
    {"operator", boost::any(string("manager123456"))}
  }));
  try {
    client->deleteStudentWithOptions(make_shared<string>("12345"), make_shared<string>("stu123"), deleteStudentRequest, deleteStudentHeaders, make_shared<Darabonba_Util::RuntimeOptions>(Darabonba_Util::RuntimeOptions()));
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
| success | Boolean | 是否删除成功，true表示删除成功。 |

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
| 400 | invalidParameter | PARAMETER INVALID | 参数非法 |
| 400 | illegalOrg | ILLEGAL ORG | 未被组织授权 |
| 400 | noRight | NO RIGHT | 当前用户没有操作权限 |
| 500 | systemBusy | SYSTEM BUSY | 系统繁忙 |
| 500 | deleteStudentFail | DELETE\_STUDENT\_FAIL | 删除学生失败 |
