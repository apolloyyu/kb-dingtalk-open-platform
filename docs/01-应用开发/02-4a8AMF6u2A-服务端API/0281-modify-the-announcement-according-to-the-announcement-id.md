---
title: "更新公告"
source_url: "https://open.dingtalk.com/document/development/modify-the-announcement-according-to-the-announcement-id"
namespace: "development"
slug: "modify-the-announcement-according-to-the-announcement-id"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 更新公告"
doc_id: "sqDrz1sErR"
updated_at: "2026-05-27 17:06:33"
---

> Source: https://open.dingtalk.com/document/development/modify-the-announcement-according-to-the-announcement-id
> Path: 应用开发 / 服务端API / 公告 > 更新公告
> Updated: 2026-05-27 17:06:33

# 更新公告

调用本接口，更新公告。

## **接口调用说明**

本接口只有以下权限的人员可更新公告：

- 主管理员。
- 公告子管理员并且是待修改公告的创建者。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/blackboard/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_manage-钉钉公告管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| update\_request | OapiUpdateBlackboardVo | 是 |  | 请求对象。 |
| author | String | 否 | 杨xx | 公告作者。 |
| ding | Boolean | 否 | true | 是否发送应用内钉提醒：   - **true**：发送 - **false**：不发送 |
| blackboard\_id | String | 是 | 908uhyg76tfr543e | 公告ID。 |
| title | String | 是 | 入职须知 | 公告标题。 |
| content | String | 是 | 欢迎加入我们的大家庭 | 公告内容。 |
| category\_id | String | 否 | 89uuy7ytg6bnnjh7 | 公告分类ID，可以通过[获取公告分类列表](0284-obtains-the-list-of-categories-not-deleted-for-enterprise-announcements.md)接口获取id参数值。 |
| notify | Boolean | 否 | true | 修改后是否再次通知接收人。   - **true**：通知 - **false**：不通知 |
| operation\_userid | String | 是 | manager01 | 操作人userid，必须是公告管理员。 |
| coverpic\_mediaid | String | 否 | @lADPDeC2ufXOeRzMqM0BLA | 封面图，格式为`@mediaId`。  可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片，获取media\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/blackboard/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=871c8xxxx49c903' \
-d 'update_request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/update");
OapiBlackboardUpdateRequest req = new OapiBlackboardUpdateRequest();
OapiUpdateBlackboardVo boardVoObj = new OapiUpdateBlackboardVo();
boardVoObj.setAuthor("杨xx");
boardVoObj.setDing(true);
boardVoObj.setBlackboardId("09fa8384ac52cd0a826f1bf5b983e184");
boardVoObj.setTitle("入职须知");
boardVoObj.setContent("欢迎加入我们的大家庭");
boardVoObj.setCategoryId("89uuy7ytg6bnnjh7");
boardVoObj.setNotify(true);
boardVoObj.setOperationUserid("manager4220");
boardVoObj.setCoverpicMediaid("@lADPDeC2ufXOeRzMqM0BLA");
req.setUpdateRequest(boardVoObj);
OapiBlackboardUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiBlackboardUpdateRequest("https://oapi.dingtalk.com/topapi/blackboard/update")

req.update_request=""
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
$req = new OapiBlackboardUpdateRequest;
$update_request = new OapiUpdateBlackboardVo;
$update_request->author="张三";
$update_request->ding="true";
$update_request->blackboard_id="908uhyg76tfr543e";
$update_request->title="入职须知";
$update_request->content="欢迎加入我们的大家庭";
$update_request->category_id="89uuy7ytg6bnnjh7";
$update_request->notify="true";
$update_request->operation_userid="manager01";
$update_request->coverpic_mediaid="@lADPDxxxx0BLA";
$req->setUpdateRequest($update_request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/blackboard/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/update");
OapiBlackboardUpdateRequest req = new OapiBlackboardUpdateRequest();
OapiBlackboardUpdateRequest.OapiUpdateBlackboardVoDomain obj1 = new OapiBlackboardUpdateRequest.OapiUpdateBlackboardVoDomain();
obj1.Author = "张三";
obj1.Ding = true;
obj1.BlackboardId = "908uhyg76tfr543e";
obj1.Title = "入职须知";
obj1.Content = "欢迎加入我们的大家庭";
obj1.CategoryId = "89uuy7ytg6bnnjh7";
obj1.Notify = true;
obj1.OperationUserid = "manager01";
obj1.CoverpicMediaid = "@lADPDxxxxM0BLA";
req.UpdateRequest_ = obj1;
OapiBlackboardUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 本次调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | roz884n3k7rf | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": true,
  "success": true,
  "request_id": "ro28a9oke82d"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
