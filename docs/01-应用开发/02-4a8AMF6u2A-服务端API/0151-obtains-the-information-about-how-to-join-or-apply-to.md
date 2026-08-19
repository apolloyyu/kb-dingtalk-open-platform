---
title: "获取已加入或正在申请加入上下游组织的组织和个人信息"
source_url: "https://open.dingtalk.com/document/development/obtains-the-information-about-how-to-join-or-apply-to"
namespace: "development"
slug: "obtains-the-information-about-how-to-join-or-apply-to"
group: "应用开发"
tab: "服务端API"
breadcrumb: "通讯录管理 > 上下游组织（原合作空间） > 获取已加入或正在申请加入上下游组织的组织和个人信息"
doc_id: "vvMfLSZPYb"
updated_at: "2026-05-26 09:00:59"
---

> Source: https://open.dingtalk.com/document/development/obtains-the-information-about-how-to-join-or-apply-to
> Path: 应用开发 / 服务端API / 通讯录管理 > 上下游组织（原合作空间） > 获取已加入或正在申请加入上下游组织的组织和个人信息
> Updated: 2026-05-26 09:00:59

# 获取已加入或正在申请加入上下游组织的组织和个人信息

调用本接口通过上下游组织组织ID获取加入或申请加入上下游组织的组织和个人信息。上下游组织是基于普通组织底层构建的业务类型，通讯录相关API都可以使用。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/union/cooperate/info/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_related\_org\_read-钉钉通讯录关联组织读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be31xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| status | Number | 是 | 0 | 加入空间的状态：   - **0**：申请中的 - **1**：已成功加入 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/union/cooperate/info/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=9fc0cxxxx03041' \
-d 'status=0'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/union/cooperate/info/list");
OapiUnionCooperateInfoListRequest req = new OapiUnionCooperateInfoListRequest();
req.setStatus(0L);
OapiUnionCooperateInfoListResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiUnionCooperateInfoListRequest("https://oapi.dingtalk.com/topapi/union/cooperate/info/list")

req.status=0
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
$req = new OapiUnionCooperateInfoListRequest;
$req->setStatus("0");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/union/cooperate/info/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/union/cooperate/info/list");
OapiUnionCooperateInfoListRequest req = new OapiUnionCooperateInfoListRequest();
req.Status = 0L;
OapiUnionCooperateInfoListResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenCooperateUnionVo[] |  | 加入或申请加入的空间信息。 |
| auth\_level | Number | 1 | 加入企业认证等级：   - 0：未认证 - 1：高级认证 - 2：中级认证 - 3：初级认证 |
| userids | String[] | ["036063186819979769","030651132420130642"] | 单独加入的员工。  所在部门不需要加入的情况，直接选择的几个员工。 |
| dept\_ids | Number[] | [83945234,85253077,84942289] | 加入的部门列表。部门下的员工会全部加入。 |
| union\_type | Number | 2 | 加入的方式：   - 1：全部加入(不需要选择部门和员工) - 2：部分加入 |
| dept\_name | String | 测试企业 | 挂载部门名称(在上下游组织中的架构属性)，不设置默认是加入企业的名称。 |
| dept\_id | Number | 13333 | 挂载部门ID(在上下游组织中的架构属性)。 |
| union\_org\_name | String | 测试企业 | 加入企业的企业名称。 |
| union\_corp\_id | String | "test" | 加入企业的企业corpId。 |
| success | Boolean | true | 调用是否成功。 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "result":{
    "union_corp_id":"\"test\"",
    "auth_level":"1",
    "userids":"[\"036063186819979769\",\"030651132420130642\",\"043608532837402927\",\"194525202135286347\"]",
    "dept_ids":"[83945234,85253077,84942289]",
    "union_type":"2",
    "union_org_name":"测试企业",
    "dept_name":"测试企业",
    "dept_id":"13333"
  },
  "errcode":0,
  "success":"true",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
