---
title: "查询项目中文件操作日志"
source_url: "https://open.dingtalk.com/document/development/query-file-operation-logs-of-a-project"
namespace: "development"
slug: "query-file-operation-logs-of-a-project"
group: "应用开发"
tab: "服务端API"
breadcrumb: "Teambition 项目管理 > 项目 > 查询项目中文件操作日志"
doc_id: "WgrPGNW9L9"
updated_at: "2025-10-09 18:06:36"
---

> Source: https://open.dingtalk.com/document/development/query-file-operation-logs-of-a-project
> Path: 应用开发 / 服务端API / Teambition 项目管理 > 项目 > 查询项目中文件操作日志
> Updated: 2025-10-09 18:06:36

# 查询项目中文件操作日志

调用本接口获取钉钉项目空间任务中文件的操作日志列表，操作记录包括上传文件、删除文件等操作。

## 接口调用说明

项目管理中**旧版项目**操作文件可以调用该接口获取文件日志信息，项目管理中**新版项目**操作文件无法调用该接口获取文件日志信息。

## 请求

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/workspace/auditlog/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_project-钉钉任务管理权限 |

### 查询参数

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的访问凭证，通过调用[获取企业内部应用的accessToken](0033-obtain-the-access-token-of-an-internal-app.md)接口获取。 |

### 请求体

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| start\_date | Number | 是 | 1604160000000 | 操作日志起始时间，Unix时间戳，单位毫秒。 |
| end\_date | Number | 是 | 1606665600000 | 操作日志截止时间，Unix时间戳，单位毫秒。 |
| page\_size | Number | 是 | 500 | 操作列表长度，最大500。 |
| load\_more\_gmt\_create | Number | 否 | 1605369600000 | 操作记录生成时间，作为分页偏移量，分页查询时必传，Unix时间戳，单位毫秒。 |
| load\_more\_bizId | Number | 否 | 22 | 操作记录文件id，作为分页偏移量，与load\_more\_gmt\_create一起使用。  返回记录的biz\_id为load\_more\_biz\_id且gmt\_create为load\_more\_gmt\_create之后的操作列表，分页查询获取下一页时，传最后一条记录的biz\_id和gmt\_create。 |

### 请求示例

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/workspace/auditlog/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b771xxxx6e1b809c' \
-d 'end_date=1606665600000' \
-d 'load_more_bizId=22' \
-d 'load_more_gmt_create=1605369600000' \
-d 'page_size=500' \
-d 'start_date=1604160000000'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/workspace/auditlog/list");
OapiWorkspaceAuditlogListRequest req = new OapiWorkspaceAuditlogListRequest();
req.setStartDate(1604220878000L);
req.setEndDate(1605257678000L);
req.setPageSize(30L);
req.setLoadMoreGmtCreate(1604371894000L);
req.setLoadMoreBizId(22L);
OapiWorkspaceAuditlogListResponse rsp = client.execute(req,access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiWorkspaceAuditlogListRequest("https://oapi.dingtalk.com/topapi/workspace/auditlog/list")

req.start_date=1604160000000
req.end_date=1606665600000
req.page_size=500
req.load_more_gmt_create=1605369600000
req.load_more_bizId=22
try:
  resp= req.getResponse()
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiWorkspaceAuditlogListRequest;
$req->setStartDate("1604160000000");
$req->setEndDate("1606665600000");
$req->setPageSize("500");
$req->setLoadMoreGmtCreate("1605369600000");
$req->setLoadMoreBizId("22");
$resp = $c->execute($req, "https://oapi.dingtalk.com/topapi/workspace/auditlog/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/workspace/auditlog/list");
OapiWorkspaceAuditlogListRequest req = new OapiWorkspaceAuditlogListRequest();
req.StartDate = 1604160000000L;
req.EndDate = 1606665600000L;
req.PageSize = 500L;
req.LoadMoreGmtCreate = 1605369600000L;
req.LoadMoreBizId = 22L;
OapiWorkspaceAuditlogListResponse rsp = client.Execute(req);
Console.WriteLine(rsp.Body);
```

## 响应

### 响应体

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| result | OpenAuditLogDto |  | 返回结果。 |
| log\_list | EventAuditLogDto[] |  | 操作记录列表。 |
| receiver\_name | String | 总经理办公室 | 文件接收方名称。 |
| gmt\_create | String | 1577601221260 | 记录修改时间，Unix时间戳，单位毫秒。 |
| org\_name | String | 测试企业 | 企业名称。 |
| project\_name | String | 测试项目 | 项目名称。 |
| task\_name | String | 测试任务 | 任务名称。 |
| resource\_extension | String | docx | 文件类型。 |
| resource\_size | String | 1024 | 文件大小。 |
| resource | String | test.docx | 文件名。 |
| action | String | 上传文件 | 操作类型。 |
| browser | String | Chrome | 操作机器浏览器。 |
| ip\_address | String | 1.1.1.1 | 操作机器IP。 |
| platform | String | MacOs | 操作端。 |
| operator\_name | String | 测试 | 操作者名字。 |
| ding\_talk\_id | String | 12345676 | 用户的钉钉ID。 |
| emp\_id | String | 12344 | 用户所在企业中的员工ID。 |
| biz\_id | String | 111 | 文件ID。 |
| request\_id | String | 5imidzv0jgdr | 请求ID。 |

### 响应体示例

```
{
  "errcode":0,
  "result":{
    "log_list":[
      {
        "action":"查看文件",
        "bizId":21,
        "dingTalkId":138393823,
        "empId":"180420",
        "gmtCreate":1604371898000,
        "operatorName":"xx",
        "orgName":"xxxx",
        "platform":"Unknown",
        "projectName":"权限测试1",
        "resource":"xxx.png",
        "resourceExtension":"png",
        "resourceSize":46313,
        "taskName":"Task"
      },
      {
        "action":"分享",
        "bizId":33,
        "dingTalkId":138393823,
        "empId":"180420",
        "gmtCreate":1604386447000,
        "ipAddress":"xx.xx.xx.xx",
        "operatorName":"xxxx",
        "orgName":"xxxx",
        "platform":"Android",
        "projectName":"权限测试1",
        "receiverName":"钉钉项空间",
        "taskName":"Task"
      }
    ]
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
