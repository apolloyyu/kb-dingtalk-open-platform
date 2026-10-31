---
title: "添加家长"
source_url: "https://open.dingtalk.com/document/development/add-parent"
namespace: "development"
slug: "add-parent"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 添加家长"
doc_id: "epjTcC7ZM7"
updated_at: "2026-06-08 09:48:16"
---

> Source: https://open.dingtalk.com/document/development/add-parent
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 添加家长
> Updated: 2026-06-08 09:48:16

# 添加家长

调用本接口，在指定的班级下添加家长信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/guardian/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_safe-钉钉教育家校通讯录写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| class\_id | Number | 是 | 4240018 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| stu\_id | String | 是 | 2334455 | 学生ID，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取userid参数值。 |
| mobile | String | 是 | 150xxxx2322 | 手机号码。 |
| biz\_id | String | 否 | biz\_id | 业务ID，自定义值，每次调用该参数保持唯一。 |
| operator | String | 是 | user01 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |
| relation | String | 是 | F | 家长与学生的关系。   - **F**：爸爸 - **M**：妈妈 - **GF**：爷爷 - **GM**：奶奶 - **GFA**：外公 - **GMA**：外婆 - **U**：叔叔 - **A**：阿姨 - **B**：哥哥 - **S**：姐姐 - **O**：其他 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/guardian/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=99bffbbf-0079-4ab5-8060-8cc70932c1fb' \
-d 'biz_id=123' \
-d 'class_id=1234' \
-d 'mobile=13675893456' \
-d 'operator=12345' \
-d 'relation=F' \
-d 'stu_id=1234'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/guardian/create");
OapiEduGuardianCreateRequest req = new OapiEduGuardianCreateRequest();
req.setClassId(4240018L);
req.setBizId(biz_id);
req.setMobile("150xxxx2322");
req.setOperator("user01");
req.setRelation("F");
req.setStuId("2334455");
OapiEduGuardianCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduGuardianCreateRequest("https://oapi.dingtalk.com/topapi/edu/guardian/create")

req.class_id=1234
req.stu_id="1234"
req.mobile="13675893456"
req.biz_id="123"
req.operator="12345"
req.relation="F"
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
$req = new OapiEduGuardianCreateRequest;
$req->setClassId("1234");
$req->setStuId("1234");
$req->setMobile("13675893456");
$req->setBizId("123");
$req->setOperator("12345");
$req->setRelation("F");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/guardian/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/guardian/create");
OapiEduGuardianCreateRequest req = new OapiEduGuardianCreateRequest();
req.ClassId = 1234L;
req.StuId = "1234";
req.Mobile = "13675893456";
req.BizId = "123";
req.Operator = "12345";
req.Relation = "F";
OapiEduGuardianCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenEduUserCreateResponse |  | 调用结果。 |
| biz\_id | String | biz\_id | 业务ID。 |
| userid | String | manager01 | 家长的userId。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 5bsof0hsgtds | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "biz_id": "biz_id",
    "userid": "manager01"
  },
  "success": true,
  "request_id": "5bsof0hsgtds"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
