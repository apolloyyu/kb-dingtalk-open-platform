---
title: "获取外部联系人详情"
source_url: "https://open.dingtalk.com/document/development/obtains-the-external-contact-details-of-an-enterprise"
namespace: "development"
slug: "obtains-the-external-contact-details-of-an-enterprise"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 外部联系人 > 获取外部联系人详情"
doc_id: "eySHOTpJ71"
updated_at: "2026-05-27 13:09:35"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-external-contact-details-of-an-enterprise
> Path: 应用开发 / 服务端API / 通讯录管理 > 外部联系人 > 获取外部联系人详情
> Updated: 2026-05-27 13:09:35

# 获取外部联系人详情

调用本接口，获取企业外部联系人的详细信息。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/extcontact/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ext\_read-企业外部联系人读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| user\_id | String | 是 | 112500xxxx4889 | 外部联系人userId，可调用[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口获取userid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/extcontact/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=53584xxxx2c50b' \
-d 'user_id=112500xxxx4889'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/get");
OapiExtcontactGetRequest req = new OapiExtcontactGetRequest();
req.setUserId("112500xxxx4889");
OapiExtcontactGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiExtcontactGetRequest("https://oapi.dingtalk.com/topapi/extcontact/get")

req.user_id="112500xxxx4889"
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
$req = new OapiExtcontactGetRequest;
$req->setUserId("112500xxxx4889");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/extcontact/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/get");
OapiExtcontactGetRequest req = new OapiExtcontactGetRequest();
req.UserId = "112500xxxx4889";
OapiExtcontactGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenExtContact |  | 查询结果。 |
| title | String | 开发工程师 | 职位。 |
| share\_dept\_ids | Number[] | [1,2,3] | 共享部门ID列表。 |
| label\_ids | Number[] | [1,2,3] | 标签。 |
| remark | String | 备注内容 | 备注。 |
| address | String | 地址内容 | 地址。 |
| name | String | 张三 | 姓名。 |
| follower\_user\_id | String | 6767531692 | 负责人的userId。 |
| state\_code | String | 86 | 国家码。 |
| company\_name | String | 钉钉 | 公司名。 |
| share\_user\_ids | String[] | ["042059613752"] | 共享员工userId列表。 |
| mobile | String | 13088888888 | 手机号。  **[!NOTE]**  第三方企业应用不返回此参数。 |
| userid | String | 0123456789 | 外部联系人userId。 |
| email | String | xxx@1.com | 邮箱。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | xrudojam4g8f | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "result":{
    "share_user_ids":[
      "66220007745510"
    ],
    "follower_user_id":"manager4220",
    "address":"北京",
    "share_dept_ids":[],
    "label_ids":[
      1561077317
    ],
    "share_dept_ids": [
      42xxxx36
    ],
    "mobile":"136***47616",
    "remark":"技术负责人",
    "title":"CFO",
    "userid":"011250026469774889",
    "company_name":"钉钉",
    "name":"王经理",
    "state_code":"86",
    "email":"zhang@example.com"
  },
  "request_id":"xrudojam4g8f"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33009 | 无效的tokenGrantType | 请检查access\_token是否正确 |
| 33012 | 无效的userId | 请检查userId是否正确 |
| 43007 | 需要操作权限 | 请检查access\_token是否具有操作权限 |
| 400001 | 系统错误 | 请稍后再试 |
