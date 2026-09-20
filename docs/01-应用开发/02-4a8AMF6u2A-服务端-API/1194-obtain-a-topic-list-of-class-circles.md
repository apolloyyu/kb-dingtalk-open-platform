---
title: "获取班级圈话题列表"
source_url: "https://open.dingtalk.com/document/development/obtain-a-topic-list-of-class-circles"
namespace: "development"
slug: "obtain-a-topic-list-of-class-circles"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 班级圈 > 获取班级圈话题列表"
doc_id: "y6TGxgm1bA"
updated_at: "2026-06-08 09:48:21"
---

> Source: https://open.dingtalk.com/document/development/obtain-a-topic-list-of-class-circles
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 班级圈 > 获取班级圈话题列表
> Updated: 2026-06-08 09:48:21

# 获取班级圈话题列表

调用本接口，获取班级圈话题列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/circle/topiclist |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_edu\_task-钉钉教育班级圈数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| class\_id | Number | 是 | 12348756 | 班级ID，调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_id参数值。 |
| biz\_type | Number | 是 | 4 | 业务类型，固定值为**4**，表示班级圈。 |
| userid | String | 是 | user456 | 用户userId，建议传当前班级内老师的userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/circle/topiclist" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=f1e62a83-9b17-415c-95ca-4e0b8077068d' \
-d 'biz_type=1' \
-d 'class_id=1' \
-d 'userid=1'
```

Java

```
DingTalkClient client= new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/circle/topiclist");
OapiEduCircleTopiclistRequest req= new OapiEduCircleTopiclistRequest();
req.setClassId(238756L);
req.setBizType(4L);
req.setUserid("user456");
OapiEduCircleTopiclistResponse rsp= client.execute(req,access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCircleTopiclistRequest("https://oapi.dingtalk.com/topapi/edu/circle/topiclist")

req.class_id=1
req.biz_type=1
req.userid="1"
try:
  resp= req.getResponse(access_token)
  print(resp)
except Exception,e:
  print(e)
```

PHP

```
include "TopSdk.php";
date_default_timezone_set('Asia/Shanghai');

$c = new DingTalkClient(DingTalkConstant::$CALL_TYPE_OAPI, DingTalkConstant::$METHOD_POST , DingTalkConstant::$FORMAT_JSON);
$req = new OapiEduCircleTopiclistRequest;
$req->setClassId("1");
$req->setBizType("1");
$req->setUserid("1");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/circle/topiclist");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/circle/topiclist");
OapiEduCircleTopiclistRequest req = new OapiEduCircleTopiclistRequest();
req.ClassId = 1L;
req.BizType = 1L;
req.Userid = "1";
OapiEduCircleTopiclistResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenCircleTopicResponse[] |  | 返回结果。 |
| topic\_id | Number | 273485 | 话题ID。 |
| init\_topic | Boolean | false | 是否是初始化话题。   - **true**：是 - **false**：不是 |
| name | String | 0510作业讨论 | 话题名称。 |
| post\_count | Number | 12 | 动态数量。 |
| album\_media\_id | String | DetfSIAe9CLM8Mz | 话题背景图片。 |
| desc | String | 5月10日作业讨论 | 话题描述。 |
| success | Boolean | true | 是否成功。   - **true**：是 - **false**：不是 |
| errmsg | String | ok | 返回码描述 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": [
    {
      "topic_id": "273485",
      "init_topic": "false",
      "name": "0510作业讨论",
      "post_count": "12",
      "album_media_id": "DetfasdSIAe9CLM8Mz",
      "desc": "5月10日作业讨论"
    }
  ],
  "success": true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
