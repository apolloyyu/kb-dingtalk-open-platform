---
title: "获取部门详情"
source_url: "https://open.dingtalk.com/document/development/obtains-queries-department-details"
namespace: "development"
slug: "obtains-queries-department-details"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取部门详情"
doc_id: "GBr2enMEVB"
updated_at: "2026-07-20 09:21:48"
---

> Source: https://open.dingtalk.com/document/development/obtains-queries-department-details
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 获取部门详情
> Updated: 2026-07-20 09:21:48

# 获取部门详情

调用本接口，查看某个部门详情。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/dept/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_addresslist\_edu\_read-【敏感】钉钉教育家校通讯录读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| dept\_id | Number | 是 | 132691544 | 家校部门ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_id参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/dept/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=8b67a5xxxxd95cd' \
-d 'dept_id=1234'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/dept/get");
OapiEduDeptGetRequest req = new OapiEduDeptGetRequest();
req.setDeptId(132691544L);
OapiEduDeptGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduDeptGetRequest("https://oapi.dingtalk.com/topapi/edu/dept/get")

req.dept_id=1234
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
$req = new OapiEduDeptGetRequest;
$req->setDeptId("1234");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/dept/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/dept/get");
OapiEduDeptGetRequest req = new OapiEduDeptGetRequest();
req.DeptId = 1234L;
OapiEduDeptGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | Result |  | 返回结果。 |
| detail | OpenEduDeptDetail |  | 部门详情。 |
| nick | String | 实验学校 | 部门别名。 |
| chain | String | [4240016] | 节点链。从顶层节点到当前节点的中间节点，其内容不包含当前节点。 |
| feature | String | {} | 部门节点特有属性。 |
| name | String | 一年级1班 | 部门名称。 |
| contact\_type | String | custom | 通讯录类型。   - **classic**：传统经典4层结构。校区/学段/年级/班级 - **custom**：自定义结构 |
| dept\_type | String | dept | 节点类型。   - **campus**：校区 - **period**：学段 - **grade**：年级 - **class**：班级 - **dept**：普通节点，没有业务含义，主用存在于自定义通讯录中 |
| dept\_id | Number | 4240017 | 部门ID。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | ojwww99lh3t0 | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "detail": {
      "chain": "[]",
      "contact_type": "classic",
      "dept_id": 132691544,
      "dept_type": "campus",
      "feature": "{}",
      "name": "未来PARK小学",
      "nick": ""
    }
  },
  "success": true,
  "request_id": "ojwww99lh3t0"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
