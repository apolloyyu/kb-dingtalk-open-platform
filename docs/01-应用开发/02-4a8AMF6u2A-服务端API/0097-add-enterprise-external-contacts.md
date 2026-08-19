---
title: "添加外部联系人"
source_url: "https://open.dingtalk.com/document/development/add-enterprise-external-contacts"
namespace: "development"
slug: "add-enterprise-external-contacts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 外部联系人 > 添加外部联系人"
doc_id: "Ao6R46x8pq"
updated_at: "2026-05-27 13:09:30"
---

> Source: https://open.dingtalk.com/document/development/add-enterprise-external-contacts
> Path: 应用开发 / 服务端API / 通讯录管理 > 外部联系人 > 添加外部联系人
> Updated: 2026-05-27 13:09:30

# 添加外部联系人

调用本接口，添加企业外部联系人。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/extcontact/create |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_ext\_write-企业外部联系人写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| contact | OpenExtContact | 是 |  | 外部联系人信息。 |
| title | String | 否 | 开发工程师 | 职位。 |
| label\_ids | Number[] | 是 | [1561077317,1561077310] | 标签列表，可调用[获取外部联系人标签列表](0101-obtains-a-list-of-external-contact-tags.md)接口查询标签信息。  参考[企业如何自定义标签组](https://tms.dingtalk.com/markets/dingtalk/biaoqianzu)添加自定义标签。每次调用最多传20个labelId。 |
| share\_dept\_ids | Number[] | 否 | [1,2,3] | 共享给的部门ID，可调用[获取子部门ID列表](0083-obtain-the-list-of-sub-department-ids.md)接口获取，每次调用最多传20个部门ID。 |
| address | String | 否 | 北京市 | 地址。 |
| remark | String | 否 | 王经理 | 备注。 |
| follower\_user\_id | String | 是 | manager4220 | 负责人的userId，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId，  每次调用最多传20个userId。 |
| name | String | 是 | 张xx | 外部联系人的姓名。 |
| state\_code | String | 是 | 86 | 手机号国家码。 |
| company\_name | String | 否 | 钉钉 | 外部联系人的企业名称。 |
| share\_user\_ids | String[] | 否 | ["023420013644"] | 共享给的员工userid列表，可通过[根据手机号查询用户](0063-query-users-by-phone-number.md)接口获取userId，每次调用最多传20个userId。 |
| mobile | String | 是 | 130xxxx8888 | 外部联系人的手机号。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/extcontact/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=d5f0efxxxx9fa9e1' \
-d 'contact=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/create");
OapiExtcontactCreateRequest req = new OapiExtcontactCreateRequest();
OapiExtcontactCreateRequest.OpenExtContact contact = new OapiExtcontactCreateRequest.OpenExtContact();
contact.setTitle("开发工程师");
contact.setLabelIds(Arrays.asList(1561077317L,1561077310L));
contact.setShareDeptIds(Arrays.asList(1L,2L,3L));
contact.setFollowerUserId("manager4220");
contact.setName("张xx");
contact.setStateCode("86");
contact.setCompanyName("钉钉");
contact.setShareUserIds(Arrays.asList("023420013644"));
contact.setMobile("130xxxx8888");
req.setContact(contact);
OapiExtcontactCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiExtcontactCreateRequest("https://oapi.dingtalk.com/topapi/extcontact/create")

req.contact=""
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
$req = new OapiExtcontactCreateRequest;
$contact = new OpenExtContact;
$contact->title="开发工程师";
$contact->label_ids="[1,2,3]";
$contact->share_dept_ids="[1,2,3]";
$contact->address="地址内容";
$contact->remark="备注内容";
$contact->follower_user_id="023420013645";
$contact->name="张三";
$contact->state_code="86";
$contact->company_name="钉钉";
$contact->share_user_ids="[\"023420013644\"]";
$contact->mobile="13088888888";
$req->setContact($contact);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/extcontact/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/create");
OapiExtcontactCreateRequest req = new OapiExtcontactCreateRequest();
OapiExtcontactCreateRequest.OpenExtContactDomain obj1 = new OapiExtcontactCreateRequest.OpenExtContactDomain();
obj1.Title = "开发工程师";
obj1.LabelIds = new long[] { 1,2,3 };
obj1.ShareDeptIds = new long[] { 1,2,3 };
obj1.Address = "地址内容";
obj1.Remark = "备注内容";
obj1.FollowerUserId = "023420013645";
obj1.Name = "张三";
obj1.StateCode = "86";
obj1.CompanyName = "钉钉";
obj1.ShareUserIds = ""023420013644"";
obj1.Mobile = "13088888888";
req.Contact_ = obj1;
OapiExtcontactCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| userid | String | 123420013632 | 外部联系人的userId。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6idz5ss49kkj | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "userid":"011250026469774889",
  "request_id":"6idz5ss49kkj"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33009 | 无效的tokenGrantType | 请检查access\_token是否合法 |
| 40036 | 参数为空 | 请检查上述必填参数是否都已经填写 |
| 60103 | 无效的电话号码 | 请检查电话号码是否正确 |
| 60204 | 需要外部联系人标签 | 请填上 label\_ids |
| 60205 | 未开通外部联系人功能 | 需要用户提供授权函后，进行开通外部联系人功能 |
| 43007 | 需要授权 | 请确认access\_token是否有操作权限 |
| 60112 | 无效的用户名称 | 请确认用户名称是否正确 |
| 22005 | 该外部联系人已经存在 | 请确认外部联系人手机号是否正确 |
| -1 | 系统繁忙 | 请稍后再试 |
