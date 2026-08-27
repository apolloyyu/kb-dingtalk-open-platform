---
title: "更新外部联系人"
source_url: "https://open.dingtalk.com/document/development/update-enterprise-external-contacts"
namespace: "development"
slug: "update-enterprise-external-contacts"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 外部联系人 > 更新外部联系人"
doc_id: "6JTXSvddq8"
updated_at: "2026-05-27 13:09:32"
---

> Source: https://open.dingtalk.com/document/development/update-enterprise-external-contacts
> Path: 应用开发 / 服务端API / 通讯录管理 > 外部联系人 > 更新外部联系人
> Updated: 2026-05-27 13:09:32

# 更新外部联系人

调用本接口，更新企业外部联系人。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/extcontact/update |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_ext\_write-企业外部联系人写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| contact | OpenExtContact | 是 |  | 外部联系人信息。 |
| title | String | 否 | 开发工程师 | 职位。 |
| label\_ids | Number[] | 是 | [1,2,3] | 标签列表，可调用[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口查询标签信息。  参考[企业如何自定义标签组](https://tms.dingtalk.com/markets/dingtalk/biaoqianzu)添加自定义标签。  每次调用最多传20个labelId。 |
| share\_dept\_ids | Number[] | 否 | [420606536] | 共享给的部门ID，可调用[获取子部门ID列表](0083-obtain-the-list-of-sub-department-ids.md)接口获取。  每次调用最多传20个部门ID。 |
| address | String | 否 | 北京 | 地址。 |
| remark | String | 否 | 技术负责人 | 备注。 |
| follower\_user\_id | String | 是 | 023420013645 | 负责人的userId。 |
| name | String | 是 | 张xx | 外部联系人的姓名。 |
| user\_id | String | 是 | 123420013632 | 该外部联系人的userId，可调用[获取外部联系人列表](0100-obtain-the-external-contact-list.md)接口获取。 |
| company\_name | String | 否 | 钉钉 | 外部联系人的企业名称。 |
| share\_user\_ids | String[] | 否 | ["023420013644"] | 共享给的员工userid列表。  每次调用最多传20个labelId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/extcontact/update" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=34ddexxxx6c95' \
-d 'contact=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/update");
OapiExtcontactUpdateRequest req = new OapiExtcontactUpdateRequest();
OapiExtcontactUpdateRequest.OpenExtContact contact = new OapiExtcontactUpdateRequest.OpenExtContact();
contact.setTitle("开发工程师");
contact.setLabelIds(Arrays.asList(1L,2L,3L));
contact.setShareDeptIds(Arrays.asList(420606536
L));
contact.setAddress("北京");
contact.setRemark("技术负责人");
contact.setFollowerUserId("023420013645");
contact.setName("张xx");
contact.setUserId("123420013632");
contact.setCompanyName("钉钉");
contact.setShareUserIds(Arrays.asList("user123"));
req.setContact(contact);
OapiExtcontactUpdateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiExtcontactUpdateRequest("https://oapi.dingtalk.com/topapi/extcontact/update")

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
$req = new OapiExtcontactUpdateRequest;
$contact = new OpenExtContact;
$contact->title="开发工程师";
$contact->label_ids="[1,2,3]";
$contact->share_dept_ids="[1,2,3]";
$contact->address="地址内容";
$contact->remark="备注内容";
$contact->follower_user_id="023420013645";
$contact->name="张三";
$contact->user_id="123420013632";
$contact->company_name="钉钉";
$contact->share_user_ids="[\"023420013644\"]";
$req->setContact($contact);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/extcontact/update");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/extcontact/update");
OapiExtcontactUpdateRequest req = new OapiExtcontactUpdateRequest();
OapiExtcontactUpdateRequest.OpenExtContactDomain obj1 = new OapiExtcontactUpdateRequest.OpenExtContactDomain();
obj1.Title = "开发工程师";
obj1.LabelIds = new long[] { 1,2,3 };
obj1.ShareDeptIds = new long[] { 1,2,3 };
obj1.Address = "地址内容";
obj1.Remark = "备注内容";
obj1.FollowerUserId = "023420013645";
obj1.Name = "张三";
obj1.UserId = "123420013632";
obj1.CompanyName = "钉钉";
obj1.ShareUserIds = ""023420013644"";
req.Contact_ = obj1;
OapiExtcontactUpdateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 8n3mksu5hqzy | 请求ID。 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id": "8n3mksu5hqzy""
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

| 错误码（errcode） | 错误码描述（errmsg） | 解决方案 |
| --- | --- | --- |
| 33009 | 无效的tokenGrantType | 请检查access\_token是否正确 |
| 40036 | 参数为空 | 请检查是否填写了必填参数 |
| 40003 | 无效的userId | 请检查userId是否正确 |
| 60112 | 无效的用户名称 | 请检查用户名称是否正确 |
| 60121 | 未找到对应的用户 | 请检查用户信息是否正确 |
| 60204 | 需要外部联系人的label | 请填写外部联系人的label\_ids |
| 43007 | 需要权限 | 请检查access\_token是否有权限进行此操作 |
| 60103 | 无效的手机号码 | 请检查手机号是否正确 |
| 60200 | 外部联系人已存在 | 请检查外部联系人信息是否正确 |
| 60203 | 超出外部联系人数量 | 请移除部分外部联系人 |
| -1 | 系统繁忙 | 请稍后再试 |
