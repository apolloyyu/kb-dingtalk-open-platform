---
title: "获取数字化证书"
source_url: "https://open.dingtalk.com/document/development/obtain-digital-certificate"
namespace: "development"
slug: "obtain-digital-certificate"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 数字化证书 > 获取数字化证书"
doc_id: "v1kWWoqBMK"
updated_at: "2026-06-08 09:48:24"
---

> Source: https://open.dingtalk.com/document/development/obtain-digital-certificate
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 数字化证书 > 获取数字化证书
> Updated: 2026-06-08 09:48:24

# 获取数字化证书

调用本接口，获取数字化证书。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/cert/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_digital\_cert\_read-钉钉教育行业数字化认证信息读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| userid | String | 是 | user01 | 学校老师的userId，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取userid参数值。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/cert/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=bb3d98a7-592d-4f92-a0b8-7d705b4fc2cd' \
-d 'userid=123456778'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/cert/get");
OapiEduCertGetRequest req = new OapiEduCertGetRequest();
req.setUserid("user01");
OapiEduCertGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCertGetRequest("https://oapi.dingtalk.com/topapi/edu/cert/get")

req.userid="123456778"
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
$req = new OapiEduCertGetRequest;
$req->setUserid("123456778");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/cert/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/cert/get");
OapiEduCertGetRequest req = new OapiEduCertGetRequest();
req.Userid = "123456778";
OapiEduCertGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenQueryCertResponse |  | 返回结果。 |
| current\_cert\_level | Number | 1 | 当前用户最高认证等级。   - **0**：没有认证 - **1**：初级 - **2**：中级 - **3**：高级 |
| cert\_datas | Certdata[] |  | 认证明细。 |
| cert\_status | Number | 2 | 当前等级认证状态。   - **0**：未获取 - **1**：认证中 - **2**：证书制作中 - **3**：已获取 |
| can\_cert | Boolean | true | 是否可以参加当前认证考试。   - **true**：可以 - **false**：敬请期待 |
| cert\_level | Number | 2 | 认证等级。   - **0**：没有认证 - **1**：初级 - **2**：中级 - **3**：高级 |
| practical\_task\_data | OpenPracticalTaskData[] |  | 实操任务完成信息。 |
| finish | Boolean | true | 是否完成实操任务。   - **true**：完成 - **false**：未完成 |
| task\_code | String | sendImMsg | 实操任务code。   - **sendCard**：发布打卡 - **sendImMsg**：发布消息 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg":"ok",
  "result": {
    "current_cert_level": 1,
    "cert_datas": {
      "cert_status": 2,
      "can_cert": true,
      "cert_level": 2
    },
    "practical_task_data": {
      "finish": true,
      "task_code": "sendImMsg"
    }
  },
  "success": true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
