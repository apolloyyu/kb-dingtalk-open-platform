---
title: "创建班级"
source_url: "https://open.dingtalk.com/document/development/create-a-class"
namespace: "development"
slug: "create-a-class"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建班级"
doc_id: "kXltTIm5PK"
updated_at: "2026-06-08 09:48:13"
---

> Source: https://open.dingtalk.com/document/development/create-a-class
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家校通讯录2.0 > 创建班级
> Updated: 2026-06-08 09:48:13

# 创建班级

调用本接口，在指定的年级下创建班级。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/class/create |
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
| open\_class | OpenClass | 是 |  | 班级信息。 |
| nick | String | 否 | 实验班 | 班级别名。 |
| only\_use\_nick | String | 是 | true | 是否只展现nick。 |
| name | String | 是 | 一班 | 班级名。 |
| class\_level | Number | 是 | 1 | 每个年级下班级级数，1班为1，2班为2。 |
| super\_id | Number | 是 | 4240018 | 年级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为grade时的dept\_id参数值。 |
| operator | String | 是 | user01 | 钉钉企业管理员userId，即有家校通讯录管理范围的管理员userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/class/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=a05094e8-401e-43c3-a4b7-38005e870244' \
-d 'open_class=null' \
-d 'operator=1234' \
-d 'super_id=12345'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/class/create");
OapiEduClassCreateRequest req = new OapiEduClassCreateRequest();
OpenClass openClass = new OpenClass();
openClass.setNick("实验班");
openClass.setName("一班");
openClass.setClassLevel(1L);
openClass.setOnlyUseNick("true");
req.setOpenClass(openClass);
req.setOperator("user01");
req.setSuperId(4240018L);
OapiEduClassCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduClassCreateRequest("https://oapi.dingtalk.com/topapi/edu/class/create")

req.open_class=""
req.super_id=12345
req.operator="1234"
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
$req = new OapiEduClassCreateRequest;
$open_class = new OpenClass;
$open_class->nick="香蕉班";
$open_class->only_use_nick="true";
$open_class->name="二年级1班";
$open_class->class_level="1";
$req->setOpenClass($open_class);
$req->setSuperId("12345");
$req->setOperator("1234");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/class/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/class/create");
OapiEduClassCreateRequest req = new OapiEduClassCreateRequest();
OapiEduClassCreateRequest.OpenClassDomain obj1 = new OapiEduClassCreateRequest.OpenClassDomain();
obj1.Nick = "香蕉班";
obj1.OnlyUseNick = "true";
obj1.Name = "二年级1班";
obj1.ClassLevel = 1L;
req.OpenClass_ = obj1;
req.SuperId = 12345L;
req.Operator = "1234";
OapiEduClassCreateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenClassCreateResponse |  | 调用结果。 |
| dept\_id | Number | 4240018 | 班级ID。 |
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
    "dept_id": 4240018
  },
  "success": true,
  "request_id": "5bsof0hsgtds"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
