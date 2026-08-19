---
title: "获取外部联系人列表"
source_url: "https://open.dingtalk.com/document/development/obtain-the-external-contact-list"
namespace: "development"
slug: "obtain-the-external-contact-list"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 外部联系人 > 获取外部联系人列表"
doc_id: "1Hn6Q6zhlE"
updated_at: "2026-05-27 13:09:33"
---

> Source: https://open.dingtalk.com/document/development/obtain-the-external-contact-list
> Path: 应用开发 / 服务端API / 通讯录管理 > 外部联系人 > 获取外部联系人列表
> Updated: 2026-05-27 13:09:33

# 获取外部联系人列表

调用本接口，获取企业外部联系人列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/extcontact/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ext\_read-企业外部联系人读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| size | Number | 否 | 20 | 支持分页查询，与offset参数同时设置时才生效，此参数代表分页大小，最大100。 |
| offset | Number | 否 | 0 | 支持分页查询，与size参数同时设置时才生效，此参数代表偏移量，偏移量从0开始。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/extcontact/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=b5039xxxx8bcc' \
-d 'offset=0' \
-d 'size=20'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/list");
OapiExtcontactListRequest req = new OapiExtcontactListRequest();
req.setSize(20L);
req.setOffset(0L);
OapiExtcontactListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiExtcontactListRequest("https://oapi.dingtalk.com/topapi/extcontact/list")

req.offset=0
req.size=20
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
$req = new OapiExtcontactListRequest;
$req->setOffset("0");
$req->setSize("20");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/extcontact/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/list");
OapiExtcontactListRequest req = new OapiExtcontactListRequest();
req.Offset = 0L;
req.Size = 20L;
OapiExtcontactListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| results | OpenExtContact[] |  | 查询结果。 |
| title | String | 开发工程师 | 职位。 |
| share\_dept\_ids | Number[] | 1,2,3 | 共享部门ID列表。 |
| label\_ids | Number[] | 1,2,3 | 外部联系人标签列表。 |
| remark | String | 备注内容 | 备注。 |
| address | String | 地址内容 | 地址。 |
| name | String | 张三 | 姓名。 |
| follower\_user\_id | String | 6767531692 | 负责人的userid。 |
| state\_code | String | 86 | 国家码。 |
| company\_name | String | 钉钉 | 公司名。 |
| share\_user\_ids | String[] | 042059613752 | 共享员工userid列表。 |
| mobile | String | 13088888888 | 手机号。  **[!NOTE]**  第三方企业应用不返回此参数。 |
| userid | String | 0123456789 | 外部联系人的userid。 |
| email | String | 1@1.com | 邮箱。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 439eqp31da45 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "results": [
    {
      "address": "北京",
      "company_name": "钉钉",
      "email": "zhang@example.com",
      "follower_user_id": "manager4220",
      "label_ids": [
        1517
      ],
      "mobile": "1360054xxxx",
      "name": "王经理",
      "remark": "技术负责人",
      "share_dept_ids": [
        42536
      ],
      "share_user_ids": [
        "0423752"
      ],
      "state_code": "86",
      "title": "CFO",
      "userid": "01129774889"
    }
  ],
  "request_id": "439eqp31da45"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33009 | 无效的tokenGrantType | 请检查access\_token是否正确 |
| 40069 | 无效的size | 请调整分页大小 |
| 40068 | 无效的偏移量 | 请调整偏移量 |
| 400001 | 系统错误 | 请稍后再试 |
