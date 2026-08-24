---
title: "获取文件操作记录"
source_url: "https://open.dingtalk.com/document/development/obtain-file-operation-records"
namespace: "development"
slug: "obtain-file-operation-records"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 文件 > 获取文件操作记录"
doc_id: "nsckkWsAxA"
updated_at: "2026-06-04 19:09:58"
---

> Source: https://open.dingtalk.com/document/development/obtain-file-operation-records
> Path: 应用开发 / 服务端API / 专属钉钉 > 文件 > 获取文件操作记录
> Updated: 2026-06-04 19:09:58

# 获取文件操作记录

获取专属钉钉内成员所有所在组织的操作文件或文档的记录。

## **接口调用说明**

获取文件操作记录接口，需同时满足以下条件才可调用：

- 调用的组织类型是专属钉钉组织；
- 创建的应用类型是企业内部应用。

## 请求

### 基本信息

| 字段 | 值 |
| --- | --- |
| HTTP URL | https://api.dingtalk.com/v1.0/exclusive/fileAuditLogs |
| HTTP Method | GET |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-Custom.OpFileAudit.Read-专属钉钉文件审计日志读权限 |

### 请求头

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| x-acs-dingtalk-access-token | String | 是 | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 查询参数

| 名称 | 类型 | 是否必填 | 描述 |
| --- | --- | --- | --- |
| startDate | Long | 是 | 操作日志起始时间，UNIX时间戳，单位毫秒。 |
| endDate | Long | 是 | 操作日志截止时间，UNIX时间戳，单位毫秒。 |
| pageSize | Integer | 是 | 每页最大条目数，最大值500。 |
| nextGmtCreate | Long | 否 | 操作记录生成时间，UNIX时间戳，单位毫秒，作为分页偏移量。   - 如果是首次调用，该参数不传入。 - 如果是非首次调用，该参数传上次调用时返回的最后一条记录的gmtCreate。 |
| nextBizId | Long | 否 | 操作记录文件id，作为分页偏移量。   - 如果是首次调用，该参数不传入。 - 如果是非首次调用，该参数传上次调用时返回的最后一条记录的bizId。 |

### 请求示例

HTTP

```
GET /v1.0/exclusive/fileAuditLogs?startDate=1577340931837&endDate=1577945731837&pageSize=500&nextGmtCreate=1577340931837&nextBizId=100000 HTTP/1.1
Host:api.dingtalk.com
x-acs-dingtalk-access-token:token123
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
    public static com.aliyun.dingtalkexclusive_1_0.Client createClient() throws Exception {
        com.aliyun.teaopenapi.models.Config config = new com.aliyun.teaopenapi.models.Config();
        config.protocol = "https";
        config.regionId = "central";
        return new com.aliyun.dingtalkexclusive_1_0.Client(config);
    }

    public static void main(String[] args_) throws Exception {
        java.util.List<String> args = java.util.Arrays.asList(args_);
        com.aliyun.dingtalkexclusive_1_0.Client client = Sample.createClient();
        com.aliyun.dingtalkexclusive_1_0.models.ListAuditLogHeaders listAuditLogHeaders = new com.aliyun.dingtalkexclusive_1_0.models.ListAuditLogHeaders();
        listAuditLogHeaders.xAcsDingtalkAccessToken = "<your access token>";
        com.aliyun.dingtalkexclusive_1_0.models.ListAuditLogRequest listAuditLogRequest = new com.aliyun.dingtalkexclusive_1_0.models.ListAuditLogRequest()
                .setStartDate(1577340931837L)
                .setEndDate(1577945731837L)
                .setPageSize(500)
                .setNextGmtCreate(1577340931837L)
                .setNextBizId(100000L);
        try {
            client.listAuditLogWithOptions(listAuditLogRequest, listAuditLogHeaders, new com.aliyun.teautil.models.RuntimeOptions());
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

from alibabacloud_dingtalk.exclusive_1_0.client import Client as dingtalkexclusive_1_0Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dingtalk.exclusive_1_0 import models as dingtalkexclusive__1__0_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> dingtalkexclusive_1_0Client:
        """
        使用 Token 初始化账号Client
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        config.protocol = 'https'
        config.region_id = 'central'
        return dingtalkexclusive_1_0Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_audit_log_headers = dingtalkexclusive__1__0_models.ListAuditLogHeaders()
        list_audit_log_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_audit_log_request = dingtalkexclusive__1__0_models.ListAuditLogRequest(
            start_date=1577340931837,
            end_date=1577945731837,
            page_size=500,
            next_gmt_create=1577340931837,
            next_biz_id=100000
        )
        try:
            client.list_audit_log_with_options(list_audit_log_request, list_audit_log_headers, util_models.RuntimeOptions())
        except Exception as err:
            if not UtilClient.empty(err.code) and not UtilClient.empty(err.message):
                # err 中含有 code 和 message 属性，可帮助开发定位问题
                pass

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        list_audit_log_headers = dingtalkexclusive__1__0_models.ListAuditLogHeaders()
        list_audit_log_headers.x_acs_dingtalk_access_token = '<your access token>'
        list_audit_log_request = dingtalkexclusive__1__0_models.ListAuditLogRequest(
            start_date=1577340931837,
            end_date=1577945731837,
            page_size=500,
            next_gmt_create=1577340931837,
            next_biz_id=100000
        )
        try:
            await client.list_audit_log_with_options_async(list_audit_log_request, list_audit_log_headers, util_models.RuntimeOptions())
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

use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Dingtalk;
use \Exception;
use AlibabaCloud\Tea\Exception\TeaError;
use AlibabaCloud\Tea\Utils\Utils;

use Darabonba\OpenApi\Models\Config;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\ListAuditLogHeaders;
use AlibabaCloud\SDK\Dingtalk\Vexclusive_1_0\Models\ListAuditLogRequest;
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
        $listAuditLogHeaders = new ListAuditLogHeaders([]);
        $listAuditLogHeaders->xAcsDingtalkAccessToken = "<your access token>";
        $listAuditLogRequest = new ListAuditLogRequest([
            "startDate" => 1577340931837,
            "endDate" => 1577945731837,
            "pageSize" => 500,
            "nextGmtCreate" => 1577340931837,
            "nextBizId" => 100000
        ]);
        try {
            $client->listAuditLogWithOptions($listAuditLogRequest, $listAuditLogHeaders, new RuntimeOptions([]));
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
  dingtalkexclusive_1_0  "github.com/alibabacloud-go/dingtalk/exclusive_1_0"
  openapi  "github.com/alibabacloud-go/darabonba-openapi/v2/client"
  "github.com/alibabacloud-go/tea/tea"
)

/**
 * 使用 Token 初始化账号Client
 * @return Client
 * @throws Exception
 */
func CreateClient () (_result *dingtalkexclusive_1_0.Client, _err error) {
  config := &openapi.Config{}
  config.Protocol = tea.String("https")
  config.RegionId = tea.String("central")
  _result = &dingtalkexclusive_1_0.Client{}
  _result, _err = dingtalkexclusive_1_0.NewClient(config)
  return _result, _err
}

func _main (args []*string) (_err error) {
  client, _err := CreateClient()
  if _err != nil {
    return _err
  }

  listAuditLogHeaders := &dingtalkexclusive_1_0.ListAuditLogHeaders{}
  listAuditLogHeaders.XAcsDingtalkAccessToken = tea.String("<your access token>")
  listAuditLogRequest := &dingtalkexclusive_1_0.ListAuditLogRequest{
    StartDate: tea.Int64(1577340931837),
    EndDate: tea.Int64(1577945731837),
    PageSize: tea.Int32(500),
    NextGmtCreate: tea.Int64(1577340931837),
    NextBizId: tea.Int64(100000),
  }
  tryErr := func()(_e error) {
    defer func() {
      if r := tea.Recover(recover()); r != nil {
        _e = r
      }
    }()
    _, _err = client.ListAuditLogWithOptions(listAuditLogRequest, listAuditLogHeaders, &util.RuntimeOptions{})
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
import dingtalkexclusive_1_0, * as $dingtalkexclusive_1_0 from '@alicloud/dingtalk/exclusive_1_0';
import OpenApi, * as $OpenApi from '@alicloud/openapi-client';
import * as $tea from '@alicloud/tea-typescript';

export default class Client {

  /**
   * 使用 Token 初始化账号Client
   * @return Client
   * @throws Exception
   */
  static createClient(): dingtalkexclusive_1_0 {
    let config = new $OpenApi.Config({ });
    config.protocol = "https";
    config.regionId = "central";
    return new dingtalkexclusive_1_0(config);
  }

  static async main(args: string[]): Promise<void> {
    let client = Client.createClient();
    let listAuditLogHeaders = new $dingtalkexclusive_1_0.ListAuditLogHeaders({ });
    listAuditLogHeaders.xAcsDingtalkAccessToken = "<your access token>";
    let listAuditLogRequest = new $dingtalkexclusive_1_0.ListAuditLogRequest({
      startDate: 1577340931837,
      endDate: 1577945731837,
      pageSize: 500,
      nextGmtCreate: 1577340931837,
      nextBizId: 100000,
    });
    try {
      await client.listAuditLogWithOptions(listAuditLogRequest, listAuditLogHeaders, new $Util.RuntimeOptions({ }));
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
        public static AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client CreateClient()
        {
            AlibabaCloud.OpenApiClient.Models.Config config = new AlibabaCloud.OpenApiClient.Models.Config();
            config.Protocol = "https";
            config.RegionId = "central";
            return new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client(config);
        }

        public static void Main(string[] args)
        {
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Client client = CreateClient();
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.ListAuditLogHeaders listAuditLogHeaders = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.ListAuditLogHeaders();
            listAuditLogHeaders.XAcsDingtalkAccessToken = "<your access token>";
            AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.ListAuditLogRequest listAuditLogRequest = new AlibabaCloud.SDK.Dingtalkexclusive_1_0.Models.ListAuditLogRequest
            {
                StartDate = 1577340931837,
                EndDate = 1577945731837,
                PageSize = 500,
                NextGmtCreate = 1577340931837,
                NextBizId = 100000,
            };
            try
            {
                client.ListAuditLogWithOptions(listAuditLogRequest, listAuditLogHeaders, new AlibabaCloud.TeaUtil.Models.RuntimeOptions());
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
| list | Array | 获取的文件操作记录列表。 |
| operatorName | String | 操作用户的昵称。 |
| platform | Integer | 操作端。   - 0：IOS端 - 1：ANDROID端 - 2：WEB端，即网页版钉钉 - 11：WIN端 - 12：MAC端 |
| platformView | String | 操作端含义值。   - 0：IOS端 - 1：ANDROID端 - 2：WEB端，即网页版钉钉 - 11：WIN端 - 12：MAC端 |
| status | Integer | 记录状态。   - 0：正常 - 1：删除 |
| action | Integer | 操作类型。   - 0：上传文件 - 1：删除文件 - 2：下载文件 - 3：预览文件 - 4：覆盖文件 - 5：创建外链分享 - 6：重命名文件 - 7：移动文件 - 8：复制或转发文件 - 9：离职转交 - 10：创建文档 - 11：删除文档 - 12：导出文档 - 13：预览文档 - 14：回滚文档 - 15：应用内分享文档 - 16：文档移动 - 17：创建副本 - 18：文档评论 - 19：文档导入 - 20：更改协作者 - 21：重命名 - 22：撤回文件 - 23：知识库上传文件 - 24：文档组织内公开 - 25：文档仅成员可见 - 26：知识库组织内公开 - 27：知识库仅成员可见 - 28：知识库添加成员 - 29：知识库移除成员 - 30：知识库修改成员 - 31：知识库预览文件 - 32：知识库下载文件 - 33：知识库移动文件 |
| actionView | String | 操作类型含义值。   - 0：上传文件 - 1：删除文件 - 2：下载文件 - 3：预览文件 - 4：覆盖文件 - 5：创建外链分享 - 6：重命名文件 - 7：移动文件 - 8：复制或转发文件 - 9：离职转交 - 10：创建文档 - 11：删除文档 - 12：导出文档 - 13：预览文档 - 14：回滚文档 - 15：应用内分享文档 - 16：文档移动 - 17：创建副本 - 18：文档评论 - 19：文档导入 - 20：更改协作者 - 21：重命名 - 22：撤回文件 - 23：知识库上传文件 - 24：文档组织内公开 - 25：文档仅成员可见 - 26：知识库组织内公开 - 27：知识库仅成员可见 - 28：知识库添加成员 - 29：知识库移除成员 - 30：知识库修改成员 - 31：知识库预览文件 - 32：知识库下载文件 - 33：知识库移动文件 |
| resource | String | 文件名。 |
| gmtCreate | Long | 记录生成时间，UNIX时间戳，单位毫秒。 |
| userId | String | 操作员工的userId。 |
| ipAddress | String | 本次操作所在的机器IP。 |
| orgName | String | 文件所属组织名称。 |
| receiverName | String | 文件接收方名称。 |
| receiverTypeView | String | 文件接收方类型含义值。   - 0：单聊 - 1：群聊 - 2：钉盘 - 3：文档 |
| receiverType | Integer | 文件接收方类型。   - 0：单聊 - 1：群聊 - 2：钉盘 - 3：文档 |
| resourceExtension | String | 文件类型。 |
| resourceSize | Long | 文件大小。 |
| targetSpaceId | Long | 文件所属的空间ID。 |
| realName | String | 操作人的姓名。 |
| bizId | String | 文件ID。 |
| operateModuleView | String | 操作来源含义值。   - 0：我的文件 - 1：单聊或者普通群 - 2：企业群 - 3：公共区 - 4：微应用钉盘存储空间 - 5：共享文件夹 - 6：单聊 - 7：普通群 - 8：员工个人工作文件夹 - 9：临时空间 - 10：隐藏会话 - 11：会话 - 12：收集文件 - 13：自定义个人空间 - 14：自定义业务空间 - 15：内部自定义企业空间 - 16：项目钉盘 - 17：群任务 - 18：收藏空间 - 19：行业运营 - 20：ding空间 - 21：日程ding空间 - 22：数据导出空间 - 23：团队空间 |
| operateModule | Long | 操作来源。   - 0：我的文件 - 1：单聊或者普通群 - 2：企业群 - 3：公共区 - 4：微应用钉盘存储空间 - 5：共享文件夹 - 6：单聊 - 7：普通群 - 8：员工个人工作文件夹 - 9：临时空间 - 10：隐藏会话 - 11：会话 - 12：收集文件 - 13：自定义个人空间 - 14：自定义业务空间 - 15：内部自定义企业空间 - 16：项目钉盘 - 17：群任务 - 18：收藏空间 - 19：行业运营 - 20：ding空间 - 21：日程ding空间 - 22：数据导出空间 - 23：团队空间 |
| gmtModified | Long | 记录修改时间，UNIX时间戳，单位毫秒。 |
| docMemberList | Array | 成员授权列表。      需满足以下条件，此字段才生效：文档或知识库已进行授权操作。 |
| memberName | String | 接收人名称。 |
| memberType | Integer | 接收人类型。   - 0：部门 - 1：群 - 2：用户 - 3：组织 |
| memberTypeView | String | 成员类型含义值。   - 0：部门 - 1：群 - 2：用户 - 3：组织 |
| permissionRole | Long | 权限类型。   - 0：无权限 - 1：可查看和下载 - 2：可编辑 - 3：管理者 - 4：仅可查看，不能下载 |
| permissionRoleView | String | 权限类型含义值。   - 0：无权限 - 1：可查看和下载 - 2：可编辑 - 3：管理者 - 4：仅可查看，不能下载 |
| docReceiverList | Array | 文件接收人列表。      只有进行了文档分享操作时，返回该字段。 |
| receiverName | String | 授权成员名称。 |
| receiverType | Integer | 授权成员类型。   - 0：单聊 - 1：群聊 - 2：钉盘 - 3：文档 |
| receiverTypeView | String | 授权成员类型含义值。   - 0：单聊 - 1：群聊 - 2：钉盘 - 3：文档 |
| workSpaceName | String | 知识库名称。 |
| workSpacePcUrl | String | 知识库PC端地址。 |
| workSpaceMobileUrl | String | 知识库移动端地址。 |
| docPcUrl | String | 文档PC端地址。 |
| docMobileUrl | String | 文档移动端地址。 |
| workSpaceId | Long | 知识库id。 |
| prevWorkSpaceId | Long | 原知识库id。 |
| prevWorkSpaceName | String | 原知识库名称。 |
| prevWorkSpacePcUrl | String | 原知识库PC端地址。 |
| prevWorkSpaceMobileUrl | String | 原知识库移动端地址。 |

### 响应体示例

```
HTTP/1.1 200 OK
Content-Type:application/json

{
  "list" : [ {
    "operatorName" : "测试",
    "platform" : 11,
    "platformView" : "WIN",
    "status" : 0,
    "action" : 0,
    "actionView" : "企业群",
    "resource" : "文件名",
    "gmtCreate" : 1577601221260,
    "userId" : "123",
    "ipAddress" : "1.1.1.1",
    "orgName" : "水果公司",
    "receiverName" : "总经理办公室",
    "receiverTypeView" : "单聊",
    "receiverType" : 0,
    "resourceExtension" : "doc",
    "resourceSize" : 1024,
    "targetSpaceId" : 11258620,
    "realName" : "张三",
    "bizId" : "11258620701",
    "operateModuleView" : "企业群",
    "operateModule" : 2,
    "gmtModified" : 1577601221260,
    "docMemberList" : [ {
      "memberName" : "张三",
      "memberType" : 0,
      "memberTypeView" : "部门",
      "permissionRole" : 1,
      "permissionRoleView" : "阅读者（可查看\\下载）"
    } ],
    "docReceiverList" : [ {
      "receiverName" : "张三",
      "receiverType" : 1,
      "receiverTypeView" : "单聊"
    } ],
    "workSpaceName" : "测试知识库",
    "workSpacePcUrl" : "https://xxxx",
    "workSpaceMobileUrl" : "https://xxxx",
    "docPcUrl" : "https://xxxx",
    "docMobileUrl" : "https://xxxx",
    "workSpaceId" : 123
  } ]
}
```

### 错误码

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| HttpCode | 错误码 | 错误信息 | 说明 |
| --- | --- | --- | --- |
| 400 | param.error | 参数错误 | 参数错误，请确认必填参数是否遗漏，nextGmtCreate与nextBizId必须配合使用 |
| 400 | param.invalid | %s | 参数不合法，操作列表长度不能大于500 |
| 400 | system.error | %s | 系统错误 |
