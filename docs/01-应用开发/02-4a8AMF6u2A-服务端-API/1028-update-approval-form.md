---
title: "更新申请单状态"
source_url: "https://open.dingtalk.com/document/development/update-approval-form"
namespace: "development"
slug: "update-approval-form"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 更新申请单状态"
doc_id: "lS87CqY2iH"
updated_at: "2026-06-03 09:58:25"
---

> Source: https://open.dingtalk.com/document/development/update-approval-form
> Path: 应用开发 / 服务端 API / 行业与生态 > 生态开放 > 阿里商旅 > 出差申请 > 更新申请单状态
> Updated: 2026-06-03 09:58:25

# 更新申请单状态

通过此接口更新审批单的处理状态，适用于企业差旅、报销等场景中对申请单进行审批操作（如同意、拒绝、转交或取消）。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip\_write-阿里商旅专用写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | OpenApiUpdateApplyRq | 是 |  | 请求对象，封装所有更新参数。 |
| thirdpart\_apply\_id | String | 是 | 12345 | 外部申请单ID，调用[获取申请单列表](1025-search-enterprise-approval-form-data.md)接口获取。 |
| operate\_time | Date | 是 | 2017-01-01 00:00:00 | 操作时间。 |
| status | Number | 是 | 1 | 申请单状态：   - 1：已同意 - 2：已拒绝 - 3：已转交 - 4：已取消 |
| userid | String | 是 | user1 | 审批人的userid，需为钉钉系统内有效的用户标识。 |
| user\_name | String | 否 | 张三 | 审批人姓名。 |
| note | String | 否 | 同意 | 审批备注信息，可为空。 |
| corpid | String | 是 | corp1 | 企业的corpid，标识目标企业租户。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=cae2bbxxxx8fa112' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update");
OapiAlitripBtripApprovalUpdateRequest req = new OapiAlitripBtripApprovalUpdateRequest();
OpenApiUpdateApplyRq obj1 = new OpenApiUpdateApplyRq();
obj1.setThirdpartApplyId("12345");
obj1.setOperateTime(StringUtils.parseDateTime("2017-01-01 00:00:00"));
obj1.setStatus(1L);
obj1.setUserid("user1");
obj1.setUserName("张三");
obj1.setNote("同意");
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripApprovalUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripApprovalUpdateRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update")

req.rq=""
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
$req = new OapiAlitripBtripApprovalUpdateRequest;
$rq = new OpenApiUpdateApplyRq;
$rq->thirdpart_apply_id="12345";
$rq->operate_time="2017-01-01 00:00:00";
$rq->status="1";
$rq->userid="user1";
$rq->user_name="张三";
$rq->note="同意";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/approval/update");
OapiAlitripBtripApprovalUpdateRequest req = new OapiAlitripBtripApprovalUpdateRequest();
OapiAlitripBtripApprovalUpdateRequest.OpenApiUpdateApplyRqDomain obj1 = new OapiAlitripBtripApprovalUpdateRequest.OpenApiUpdateApplyRqDomain();
obj1.ThirdpartApplyId = "12345";
obj1.OperateTime = DateTime.Parse(2017-01-01 00:00:00");
obj1.Status = 1L;
obj1.Userid = "user1";
obj1.UserName = "张三";
obj1.Note = "同意";
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripApprovalUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | 成功 | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 操作是否成功。 |

### **响应体示例**

```
{
  "errcode":"0",
  "success":"true",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
