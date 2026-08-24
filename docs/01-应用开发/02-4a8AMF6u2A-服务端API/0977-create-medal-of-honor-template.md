---
title: "创建荣誉勋章模板"
source_url: "https://open.dingtalk.com/document/development/create-medal-of-honor-template"
namespace: "development"
slug: "create-medal-of-honor-template"
group: "应用开发"
tab: "服务端API"
breadcrumb: "企业文化 > 荣誉 > 创建荣誉勋章模板"
doc_id: "vTuBAXoHAi"
updated_at: "2026-06-04 19:10:41"
---

> Source: https://open.dingtalk.com/document/development/create-medal-of-honor-template
> Path: 应用开发 / 服务端API / 企业文化 > 荣誉 > 创建荣誉勋章模板
> Updated: 2026-06-04 19:10:41

# 创建荣誉勋章模板

调用本接口，根据创建荣誉勋章模板人Id、荣誉勋章名称等信息，创建企业荣誉勋章模板。

## **接口调用说明**

> **[!NOTE]**
>
> - 创建企业荣誉勋章模板，会流入钉钉后台进行审核，一般5个工作日内审核完毕。
> - 企业每周的审核次数有限制（标准版每周10次/专业版每周20次），超过后接口会报错。如有特殊原因希望提高审核次数上限，请联系我们申请并讲明原因。
> - 针对同一家组织，不允许并发调用本接口创建。如需批量创建，请串行逐个执行。

### 设计规范

为了保障勋章能够顺利上架，避免安全、法务、涉敏、涉政等问题，荣誉名称和图形设计需要注意内容规范，详情参见[荣誉设计规范](https://alidocs.dingtalk.com/i/p/nb9XJor4WgY8myAp/docs/lo1YvX0prG98k244KR79JPw7xzbmLdEZ)。

### 规范条款

1. 您承诺遵守《钉钉荣誉规范条款》，保证所上传的内容不违反国家法律法规，不侵犯任何第三方的合法权益，不存在违背社会公序良俗的情况。
2. 您同意，钉钉有权对您上传的内容进行审核、作出判断，对违反本规则的内容进行处理（包括停止发布、删除等），按钉钉相关规则对您的使用钉钉进行限制。
3. 您同意，钉钉有权基于正常运营的需要对本服务进行变更（包括升级、停止运营等），或以钉钉提供的其他服务进行替代。
4. 钉钉有权根据正常运营的需要对本规则进行修订，如您不接受修订后的内容，请停止使用本服务，您使用的行为将视为您同意遵守本规则。
5. 上传素材中不得包含涉黄、涉政等违规的内容（包含但不仅限于图片、文字）。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/orgCulture/honors/templates |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用　appType-第三方企业应用 |
| 权限要求 | permission-OrgCulture.Honor.Write-组织文化荣誉信息写权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过以下获取：   - 企业内部应用，调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 - 第三方企业应用，调用[获取第三方应用授权企业的accessToken](0034-obtain-the-access-token-of-the-authorized-enterprise-1.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| userId | String | 是 | 创建荣誉勋章模板的管理员所在组织的userId信息。    需要主管理员角色或者子管理员角色。 |
| medalName | String | 是 | 荣誉勋章名称。     - 最大长度10字符 。 - 不支持表情图标等。 |
| medalDesc | String | 是 | 荣誉勋章描述。     - 最大长度30字符 。 - 不支持表情图标等。 |
| medalMediaId | String | 是 | 荣誉勋章图片，可调用[上传媒体文件](0646-upload-media-files.md)接口获取出参`media_id`参数字段。     - 图片尺寸 900\*900，不超过1M，支持PNG 。 - 图片请使用钉钉媒体资源标识符media\_id。 |
| avatarFrameMediaId | String | 是 | 头像挂件，可调用[上传媒体文件](0646-upload-media-files.md)接口获取出参`media_id`参数字段。     - 图片尺寸 240\*240，不超过1M，支持PNG。 - 图片请使用钉钉媒体资源标识符media\_id。 |
| defaultBgColor | String | 是 | 背景颜色:   - #FFFBB4 - #FFE7BC - #FFDAF4 - #DAF6A8 - #E4D7FF - #BFDFFF - #B9F2D6       仅以上颜色可选。 |

### 请求示例

HTTP

```
POST /v1.0/orgCulture/honors/templates HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:6df1****23d618ab1d72f29e39b37
Content-Type:application/json

{
  "userId" : "manager7675",
  "medalName" : "客户第一",
  "medalDesc" : "客户服务用心，奖励荣誉",
  "medalMediaId" : "@xxxxxxx",
  "avatarFrameMediaId" : "$xxxxxxx",
  "defaultBgColor" : "#FFFBB4"
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
    public static com.aliyun.dingtalkorg_culture_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkorg_culture_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkorg_culture_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkorg_culture_1_0.models.CreateOrgHonorHeaders createOrgHonorHeaders = new com.aliyun.dingtalkorg_culture_1_0.models.CreateOrgHonorHeaders();
        createOrgHonorHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkorg_culture_1_0.models.CreateOrgHonorRequest createOrgHonorRequest = new com.aliyun.dingtalkorg_culture_1_0.models.CreateOrgHonorRequest()
                .setUserId("manager7675")
                .setMedalName("客户第一")
                .setMedalDesc("客户服务用心，奖励荣誉")
                .setMedalMediaId("@xxxxxxx")
                .setAvatarFrameMediaId("$xxxxxxx")
                .setDefaultBgColor("#FFFBB4");
        try {
            client.createOrgHonorWithOptions(createOrgHonorRequest, createOrgHonorHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.orgCulture_1_0.client import Client as dingtalkorgCulture_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.orgCulture_1_0 import models as dingtalkorg_culture__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkorgCulture_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkorgCulture_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_org_honor_headers = dingtalkorg_culture__1__0_models.CreateOrgHonorHeaders()
        create_org_honor_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_org_honor_request = dingtalkorg_culture__1__0_models.CreateOrgHonorRequest(
            user_id='manager7675',
            medal_name='客户第一',
            medal_desc='客户服务用心，奖励荣誉',
            medal_media_id='@xxxxxxx',
            avatar_frame_media_id='$xxxxxxx',
            default_bg_color='#FFFBB4'
        )
        try:
            client.create_org_honor_with_options(create_org_honor_request, create_org_honor_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        create_org_honor_headers = dingtalkorg_culture__1__0_models.CreateOrgHonorHeaders()
        create_org_honor_headers.x_acs_dingtalk_access_token = '<your access token>'
        create_org_honor_request = dingtalkorg_culture__1__0_models.CreateOrgHonorRequest(
            user_id='manager7675',
            medal_name='客户第一',
            medal_desc='客户服务用心，奖励荣誉',
            medal_media_id='@xxxxxxx',
            avatar_frame_media_id='$xxxxxxx',
            default_bg_color='#FFFBB4'
        )
        try:
            await client.create_org_honor_with_options_async(create_org_honor_request, create_org_honor_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\CreateOrgHonorHeaders;
use AlibabaCloud\SDK\Dingtalk\Vorg_culture_1_0\Models\CreateOrgHonorRequest;
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
        $createOrgHonorHeaders = new CreateOrgHonorHeaders([]);
        $createOrgHonorHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $createOrgHonorRequest = new CreateOrgHonorRequest([
            "userId" => "manager7675",
            "medalName" => "客户第一",
            "medalDesc" => "客户服务用心，奖励荣誉",
            "medalMediaId" => "@xxxxxxx",
            "avatarFrameMediaId" => "\$xxxxxxx",
            "defaultBgColor" => "#FFFBB4"
        ]);
        try {
            $client->createOrgHonorWithOptions($createOrgHonorRequest, $createOrgHonorHeaders, new RuntimeOptions([]));
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
  dingtalkorgculture_1_0  "github.com/alibabacloud-go/dingtalk/orgCulture_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkorgculture_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkorgculture_1_0.Client{}
  _result, _err = dingtalkorgculture_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  createOrgHonorHeaders := &dingtalkorgculture_1_0.CreateOrgHonorHeaders{}
  createOrgHonorHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  createOrgHonorRequest := &dingtalkorgculture_1_0.CreateOrgHonorRequest{
    UserId: tea.String("manager7675"),
    MedalName: tea.String("客户第一"),
    MedalDesc: tea.String("客户服务用心，奖励荣誉"),
    MedalMediaId: tea.String("@xxxxxxx"),
    AvatarFrameMediaId: tea.String("$xxxxxxx"),
    DefaultBgColor: tea.String("#FFFBB4"),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.CreateOrgHonorWithOptions(createOrgHonorRequest, createOrgHonorHeaders, &util.RuntimeOptions{})
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
import dingtalkorgCulture_1_0, * as $dingtalkorgCulture_1_0 from '@alicloud/dingtalk/orgCulture_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkorgCulture_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkorgCulture_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let createOrgHonorHeaders = new $dingtalkorgCulture_1_0.CreateOrgHonorHeaders({ });
    createOrgHonorHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let createOrgHonorRequest = new $dingtalkorgCulture_1_0.CreateOrgHonorRequest({
      userId: "manager7675",
      medalName: "客户第一",
      medalDesc: "客户服务用心，奖励荣誉",
      medalMediaId: "@xxxxxxx",
      avatarFrameMediaId: "$xxxxxxx",
      defaultBgColor: "#FFFBB4",
    });
    try {
      await client.createOrgHonorWithOptions(createOrgHonorRequest, createOrgHonorHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.CreateOrgHonorHeaders createOrgHonorHeaders = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.CreateOrgHonorHeaders();
            createOrgHonorHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.CreateOrgHonorRequest createOrgHonorRequest = new AlibabaCloud.SDK.Dingtalkorg_culture_1_0.Models.CreateOrgHonorRequest
            {
                UserId = "manager7675",
                MedalName = "客户第一",
                MedalDesc = "客户服务用心，奖励荣誉",
                MedalMediaId = "@xxxxxxx",
                AvatarFrameMediaId = "$xxxxxxx",
                DefaultBgColor = "#FFFBB4",
            };
            try
            {
                client.CreateOrgHonorWithOptions(createOrgHonorRequest, createOrgHonorHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| result | Object | 荣誉勋章创建结果。 |
| honorId | String | 荣誉勋章模板Id。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "success" : true,
  "result" : {
    "honorId" : "10000283"
  }
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 500 | system.error | 系统繁忙，请稍后再试 | 系统繁忙，请稍后再试 |
| 500 | parameter.wrong | 参数为空或不符合文档要求 | 参数为空或不符合文档要求 |
| 500 | system.check.limit | 剩余审核次数不足 | 剩余审核次数不足 |
| 500 | system.image.large | 图片文件大小超过限制 | 图片文件大小超过限制 |
| 500 | system.corp.noauth | 组织已认证且激活人数大于6人才可提交审核 | 组织已认证且激活人数大于6人才可提交审核 |
| 500 | system.userNotExist | 用户不在组织内 | 用户不在组织内 |
| 500 | system.userNotAdmin | 用户无权限新建荣誉勋章 | 用户无权限新建荣誉勋章 |
| 500 | parameter.text.unsafe | 文案含有敏感词 | 文案含有敏感词 |
| 500 | parameter.media.wrong | 图片等多媒体素材非钉钉media\_id格式 | 图片等多媒体素材非钉钉media\_id格式，请检查图片尺寸是否满足文档要求 |
| 500 | parameter.text.large | 荣誉勋章名称或描述长度不符合要求 | 荣誉勋章名称或描述长度不符合要求 |
| 500 | parametar.color.wrong | 荣誉勋章背景色不符合要求 | 荣誉勋章背景色不符合要求 |
| 500 | system.freq.limit | 请求频繁，创建荣誉勋章不支持并发调用 | 请求频繁，创建荣誉勋章不支持并发调用 |
