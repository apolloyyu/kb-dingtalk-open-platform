---
title: "创建公告"
source_url: "https://open.dingtalk.com/document/development/create-an-enterprise-announcement"
namespace: "development"
slug: "create-an-enterprise-announcement"
group: "应用开发"
tab: "服务端API"
breadcrumb: "公告 > 创建公告"
doc_id: "YMjdIGq85L"
updated_at: "2026-07-14 09:21:48"
---

> Source: https://open.dingtalk.com/document/development/create-an-enterprise-announcement
> Path: 应用开发 / 服务端API / 公告 > 创建公告
> Updated: 2026-07-14 09:21:48

# 创建公告

调用本接口，创建企业公告。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/blackboard/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_blackboard\_manage-钉钉公告管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| create\_request | OapiCreateBlackboardVo | 是 |  | 请求对象。 |
| operation\_userid | String | 是 | manager01 | 操作人的userId，必须是公告管理员。 |
| author | String | 否 | 杨xx | 公告作者。 |
| private\_level | Number | 否 | 0 | 保密等级：   - **0**：普通公告 - **20**：保密公告 |
| ding | Boolean | 否 | false | 是否发送应用内钉提醒：   - **true**：发送 - **false**：不发送 |
| blackboard\_receiver | BlackboardReceiverOpenVo | 是 |  | 公告接收人。 |
| deptid\_list | Number[] | 否 | [1] | 接收部门ID列表，最大的列表长度为20。  **[!NOTE]**  如果传-1，代表根部门，会给组织全员发送公告。 |
| userid\_list | String[] | 否 | ["manager02"] | 接收人userId列表，最大的列表长度为1000。 |
| title | String | 是 | 入职须知 | 公告标题。 |
| push\_top | Boolean | 否 | true | 公告是否置顶。   - **true**：置顶 - **false**：不置顶 |
| content | String | 是 | 欢迎加入我们的大家庭 | 公告内容。 |
| category\_id | String | 否 | 987uy66t5rt54er | 公告分类ID。 |
| coverpic\_mediaid | String | 否 | @lAxxxxeRzMqM0BLA | 封面图，格式为`@mediaId`。  可以通过[上传媒体文件](0646-upload-media-files.md)接口上传图片，获取media\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/blackboard/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=473axxxx5ad18' \
-d 'create_request=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/create");
OapiBlackboardCreateRequest req = new OapiBlackboardCreateRequest();
OapiCreateBlackboardVo boardVoObj = new OapiCreateBlackboardVo();
boardVoObj.setOperationUserid("manager4220");
boardVoObj.setAuthor("杨xx");
boardVoObj.setPrivateLevel(0L);
boardVoObj.setDing(false);
BlackboardReceiverOpenVo receiverOpenVoObj = new BlackboardReceiverOpenVo();
receiverOpenVoObj.setDeptidList(Arrays.asList(1L));
receiverOpenVoObj.setUseridList(Arrays.asList("mamanger123"));
boardVoObj.setBlackboardReceiver(receiverOpenVoObj);
boardVoObj.setTitle("入职须知");
boardVoObj.setPushTop(true);
boardVoObj.setContent("欢迎加入我们的大家庭");
boardVoObj.setCategoryId("987uy66t5rt54er");
boardVoObj.setCoverpicMediaid("@lADPDeC2ufXOeRzMqM0BLA");
req.setCreateRequest(boardVoObj);
OapiBlackboardCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiBlackboardCreateRequest("https://oapi.dingtalk.com/topapi/blackboard/create")

req.create_request=""
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
$req = new OapiBlackboardCreateRequest;
$create_request = new OapiCreateBlackboardVo;
$create_request->operation_userid="manager01";
$create_request->author="张三";
$create_request->private_level="0";
$create_request->ding="false";
$blackboard_receiver = new BlackboardReceiverOpenVo;
$blackboard_receiver->deptid_list="[123456]";
$blackboard_receiver->userid_list="[\"manager02\"]";
$create_request->title="入职须知";
$create_request->push_top="true";
$create_request->content="欢迎加入我们的大家庭";
$create_request->category_id="987uy66t5rt54er";
$create_request->coverpic_mediaid="@lAxxxxeRzMqM0BLA";
$req->setCreateRequest($create_request);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/blackboard/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/blackboard/create");
OapiBlackboardCreateRequest req = new OapiBlackboardCreateRequest();
OapiBlackboardCreateRequest.OapiCreateBlackboardVoDomain obj1 = new OapiBlackboardCreateRequest.OapiCreateBlackboardVoDomain();
obj1.OperationUserid = "manager01";
obj1.Author = "张三";
obj1.PrivateLevel = 0L;
obj1.Ding = false;
OapiBlackboardCreateRequest.BlackboardReceiverOpenVoDomain obj2 = new OapiBlackboardCreateRequest.BlackboardReceiverOpenVoDomain();
obj2.DeptidList = new long[] { 123456 };
obj2.UseridList = ""manager02"";
obj1.BlackboardReceiver= obj2;
obj1.Title = "入职须知";
obj1.PushTop = true;
obj1.Content = "欢迎加入我们的大家庭";
obj1.CategoryId = "987uy66t5rt54er";
obj1.CoverpicMediaid = "@lADPDeC2ufXOeRzMqM0BLA";
OapiBlackboardCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Boolean | true | 是否创建成功。   - **true**：成功 - **false**：失败 |
| success | Boolean | true | 本次调用是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | roz884n3k7rf | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "result": true,
  "success": true,
  "request_id": "roz884n3k7rf"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
