---
title: "更新企业内部应用"
source_url: "https://open.dingtalk.com/document/development/update-internal-h5-applications"
namespace: "development"
slug: "update-internal-h5-applications"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "钉钉应用 > 应用管理 > 更新企业内部应用"
doc_id: "tG02MsNilC"
updated_at: "2026-07-14 09:22:20"
---

> Source: https://open.dingtalk.com/document/development/update-internal-h5-applications
> Path: 应用开发 / 服务端 API / 钉钉应用 > 应用管理 > 更新企业内部应用
> Updated: 2026-07-14 09:22:20

# 更新企业内部应用

通过此接口更新企业内部应用的基本信息与配置参数，支持动态调整应用的名称、描述、图标、首页地址、管理后台地址及IP白名单等。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/microApp/apps/{agentId} |
| HTTP Method | PUT |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_microapp\_manage-管理微应用的权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 路径参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| agentId | Long | 是 | 应用的agentId，请参考[基础概念-AgentId](https://open.dingtalk.com/document/orgapp/basic-concepts-beta#813cbd7067yn0)。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| opUnionId | String | 是 | 操作更新的员工unionId，可调用[查询用户详情](0056-query-user-details.md)接口获取unionid参数值。      操作更新的员工必须有该应用的管理权限，否则会出现**没有操作应用的权限**的错误。 应用管理权限查看路径：管理员登录[钉钉管理后台](https://oa.dingtalk.com) **> 安全与权限 > 权限管理 > 管理组查看**。 |
| name | String | 否 | 应用名称，名称可以由中文、数字以及字母组成，长度范围要求2-20个字符。 |
| desc | String | 否 | 应用描述，最大长度200个字符。 |
| icon | String | 否 | 应用图标，可调用[上传媒体文件](https://open.dingtalk.com/document/orgapp/upload-media-files)接口获取media\_id参数值。 |
| homepageLink | String | 否 | 应用首页地址，请输入http或https开头的网址链接。  例如：`https://www.dingtalk.com`。 |
| pcHomepageLink | String | 否 | 应用PC端地址，请输入http或https开头的链接。  例如：`https://www.dingtalk.com`。 |
| ompLink | String | 否 | 应用管理后台地址，输入http或https开头的链接。  例如：`https://www.dingtalk.com`。 |
| ipWhiteList | Array of String | 否 | 服务器出口ip白名单，支持带一个\*号通配符的IP格式。 |

### 请求示例

HTTP

```
PUT /v1.0/microApp/apps/111 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:08F778xxx
Content-Type:application/json

{
  "opUnionId" : "unionIdxxxx",
  "name" : "namexx",
  "desc" : "应用名称",
  "icon" : "mediaxxx",
  "homepageLink" : "https://www.dingtalk.com",
  "pcHomepageLink" : "https://www.dingtalk.com",
  "ompLink" : "https://www.dingtalk.com",
  "ipWhiteList" : [ "1.2.3.4" ]
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
    public static com.aliyun.dingtalkmicro_app_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkmicro_app_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        
        com.aliyun.dingtalkmicro_app_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkmicro_app_1_0.models.UpdateInnerAppHeaders updateInnerAppHeaders = new com.aliyun.dingtalkmicro_app_1_0.models.UpdateInnerAppHeaders();
        updateInnerAppHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkmicro_app_1_0.models.UpdateInnerAppRequest updateInnerAppRequest = new com.aliyun.dingtalkmicro_app_1_0.models.UpdateInnerAppRequest()
                .setOpUnionId("unionIdxxxx")
                .setName("namexx")
                .setDesc("应用名称")
                .setIcon("mediaxxx")
                .setHomepageLink("https://www.dingtalk.com")
                .setPcHomepageLink("https://www.dingtalk.com")
                .setOmpLink("https://www.dingtalk.com")
                .setIpWhiteList(java.util.Arrays.asList(
                    "1.2.3.4"
                ));
        try {
            client.updateInnerAppWithOptions("111", updateInnerAppRequest, updateInnerAppHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.micro_app_1_0.client import Client as dingtalkmicroApp_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.micro_app_1_0 import models as dingtalkmicro_app__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkmicroApp_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkmicroApp_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_inner_app_headers = dingtalkmicro_app__1__0_models.UpdateInnerAppHeaders()
        update_inner_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_inner_app_request = dingtalkmicro_app__1__0_models.UpdateInnerAppRequest(
            op_union_id='unionIdxxxx',
            name='namexx',
            desc='应用名称',
            icon='mediaxxx',
            homepage_link='https://www.dingtalk.com',
            pc_homepage_link='https://www.dingtalk.com',
            omp_link='https://www.dingtalk.com',
            ip_white_list=[
                '1.2.3.4'
            ]
        )
        try:
            client.update_inner_app_with_options('111', update_inner_app_request, update_inner_app_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        update_inner_app_headers = dingtalkmicro_app__1__0_models.UpdateInnerAppHeaders()
        update_inner_app_headers.x_acs_dingtalk_access_token = '<your access token>'
        update_inner_app_request = dingtalkmicro_app__1__0_models.UpdateInnerAppRequest(
            op_union_id='unionIdxxxx',
            name='namexx',
            desc='应用名称',
            icon='mediaxxx',
            homepage_link='https://www.dingtalk.com',
            pc_homepage_link='https://www.dingtalk.com',
            omp_link='https://www.dingtalk.com',
            ip_white_list=[
                '1.2.3.4'
            ]
        )
        try:
            await client.update_inner_app_with_options_async('111', update_inner_app_request, update_inner_app_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\UpdateInnerAppHeaders;
use AlibabaCloud\SDK\Dingtalk\Vmicro_app_1_0\Models\UpdateInnerAppRequest;
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
        $updateInnerAppHeaders = new UpdateInnerAppHeaders([]);
        $updateInnerAppHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $updateInnerAppRequest = new UpdateInnerAppRequest([
            "opUnionId" => "unionIdxxxx",
            "name" => "namexx",
            "desc" => "应用名称",
            "icon" => "mediaxxx",
            "homepageLink" => "https://www.dingtalk.com",
            "pcHomepageLink" => "https://www.dingtalk.com",
            "ompLink" => "https://www.dingtalk.com",
            "ipWhiteList" => [
                "1.2.3.4"
            ]
        ]);
        try {
            $client->updateInnerAppWithOptions("111", $updateInnerAppRequest, $updateInnerAppHeaders, new RuntimeOptions([]));
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
  dingtalkmicroapp_1_0  "github.com/alibabacloud-go/dingtalk/microApp_1_0"
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
func CreateClient () (_result *dingtalkmicroapp_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkmicroapp_1_0.Client{}
  _result, _err = dingtalkmicroapp_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  updateInnerAppHeaders := &dingtalkmicroapp_1_0.UpdateInnerAppHeaders{}
  updateInnerAppHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  updateInnerAppRequest := &dingtalkmicroapp_1_0.UpdateInnerAppRequest{
    OpUnionId: tea.String("unionIdxxxx"),
    Name: tea.String("namexx"),
    Desc: tea.String("应用名称"),
    Icon: tea.String("mediaxxx"),
    HomepageLink: tea.String("https://www.dingtalk.com"),
    PcHomepageLink: tea.String("https://www.dingtalk.com"),
    OmpLink: tea.String("https://www.dingtalk.com"),
    IpWhiteList: []*string{tea.String("1.2.3.4")},
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.UpdateInnerAppWithOptions(tea.String("111"), updateInnerAppRequest, updateInnerAppHeaders, &util.RuntimeOptions{})
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
const dingtalkmicroApp_1_0 = require('@alicloud/dingtalk/microApp_1_0');
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
    return new dingtalkmicroApp_1_0.default(config);
  }

  static async main(args) {
    let client = Client.createClient();
    let updateInnerAppHeaders = new dingtalkmicroApp_1_0.UpdateInnerAppHeaders({ });
    updateInnerAppHeaders.xAcsDingtalkAccessToken = '<your access token>';
    let updateInnerAppRequest = new dingtalkmicroApp_1_0.UpdateInnerAppRequest({
      opUnionId: 'unionIdxxxx',
      name: 'namexx',
      desc: '应用名称',
      icon: 'mediaxxx',
      homepageLink: 'https://www.dingtalk.com',
      pcHomepageLink: 'https://www.dingtalk.com',
      ompLink: 'https://www.dingtalk.com',
      ipWhiteList: [
        '1.2.3.4'
      ],
    });
    try {
      await client.updateInnerAppWithOptions('111', updateInnerAppRequest, updateInnerAppHeaders, new Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.UpdateInnerAppHeaders updateInnerAppHeaders = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.UpdateInnerAppHeaders();
            updateInnerAppHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.UpdateInnerAppRequest updateInnerAppRequest = new AlibabaCloud.SDK.Dingtalkmicro_app_1_0.Models.UpdateInnerAppRequest
            {
                OpUnionId = "unionIdxxxx",
                Name = "namexx",
                Desc = "应用名称",
                Icon = "mediaxxx",
                HomepageLink = "https://www.dingtalk.com",
                PcHomepageLink = "https://www.dingtalk.com",
                OmpLink = "https://www.dingtalk.com",
                IpWhiteList = new List<string>
                {
                    "1.2.3.4"
                },
            };
            try
            {
                client.UpdateInnerAppWithOptions("111", updateInnerAppRequest, updateInnerAppHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Boolean | 更新结果。   - 如果更新成功，该值为true。 - 如果更新失败，不返回result，接口会响应对应报错信息。 |

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
| 400 | invalidParam | 参数错误: %s | 参数错误 |
| 400 | invalidUser | 用户id不合法，不在对应企业中 | 用户id不合法，不在对应企业中 |
| 400 | invalidEcologicalCorpId | 不合法的合作空间corpId | 不合法的合作空间corpId |
| 400 | noAppManagePermission | 没有操作应用的权限 | 没有操作应用的权限 |
| 400 | illegalIp | ip不合法 | ip不合法，可能是单个ip不合法，也可能是ip总长度超过了50 |
| 400 | invalidAgentId | 不合法的agentId | 不合法的agentId |
| 400 | illegalAppName | 应用名称含有不规范词语 | 应用名称含有不规范词语 |
| 400 | illegalAppDesc | 应用描述含有不规范词语 | 应用描述含有不规范词语 |
| 400 | illegalAppIcon | 应用图标含有不规范词语 | 应用图标含有不规范词语 |
| 500 | systemError | 系统繁忙 | 系统繁忙 |
