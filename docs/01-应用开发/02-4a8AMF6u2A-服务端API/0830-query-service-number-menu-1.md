---
title: "查询服务号菜单"
source_url: "https://open.dingtalk.com/document/development/query-service-number-menu-1"
namespace: "development"
slug: "query-service-number-menu-1"
group: "应用开发"
tab: "服务端API"
breadcrumb: "专属钉钉 > 互动服务窗 > 菜单管理 > 查询服务号菜单"
doc_id: "JY0QMkxr0P"
updated_at: "2026-06-01 09:15:50"
---

> Source: https://open.dingtalk.com/document/development/query-service-number-menu-1
> Path: 应用开发 / 服务端API / 专属钉钉 > 互动服务窗 > 菜单管理 > 查询服务号菜单
> Updated: 2026-06-01 09:15:50

# 查询服务号菜单

调用本接口查询指定服务号的会话菜单。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/serviceaccount/menu/get |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_service\_account\_menu-服务号菜单管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 30c9a84136943eaxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| unionid | String | 是 | jYdrJoCmTo0iE | 服务号的unionid，可通过[查询服务号列表](0812-query-service-number-list.md)接口获取。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/serviceaccount/menu/get" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=3167eafxxxxa60bc59' \
-d 'unionid=jYdrJoCmTo0iE'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/menu/get");
OapiServiceaccountMenuGetRequest req = new OapiServiceaccountMenuGetRequest();
req.setUnionid("jYdrJoCmTo0iE");
OapiServiceaccountMenuGetResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiServiceaccountMenuGetRequest("https://oapi.dingtalk.com/topapi/serviceaccount/menu/get")

req.unionid="jYdrJoCmTo0iE"
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
$req = new OapiServiceaccountMenuGetRequest;
$req->setUnionid("jYdrJoCmTo0iE");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/serviceaccount/menu/get");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/serviceaccount/menu/get");
OapiServiceaccountMenuGetRequest req = new OapiServiceaccountMenuGetRequest();
req.Unionid = "jYdrJoCmTo0iE";
OapiServiceaccountMenuGetResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | 10c0npg1bgup3 | 请求ID。 |
| menu | MenuConfigDTO |  | 菜单。 |
| button | MenuButtonDTO[] |  | 菜单按钮列表。 |
| name | String | 天气 | 菜单名称。 |
| type | String | click | 菜单类型。  **[!NOTE]**  如果为父菜单，则该字段为空。 |
| key | String | KEY\_WEATHER | 菜单绑定的key值。 |
| url | String | https://www.taobao.com | 菜单绑定的URL。 |
| media\_id | String | mvFiiRhuwt5IiE | 菜单素材id。 |
| sub\_button | MenuSubButtonDTO[] |  | 子菜单按钮列表。 |
| type | String | click | 子菜单类型。 |
| name | String | 杭州天气 | 子菜单名称。 |
| key | String | WEATHER\_HANGZHOU | 子菜单绑定的key值。 |
| url | String | https://www.taobao.com | 子菜单绑定的URL。 |
| media\_id | String | mvFiiRhuwt5IiE | 子菜单素材id。 |
| enable\_input | Boolean | false | 是否允许用户输入：   - **true**：允许 - **false**：不允许 |
| status | Number | 0 | 状态：   - **0**：正常 - **1**：停用 |

### **响应体示例**

```
{
  "errcode":0,
  "request_id":"10c0npg1bgup3",
  "menu": {
    "button": [
      {
        "key": "KEY_WEATHER",
        "media_id": "mvFiiRhuwt5IiE",
        "name": "今日天气",
        "sub_button": [
          {
            "key": "WEATHER_HANGZHOU",
            "media_id": "mvFiiRhuwt5IiE",
            "name": "杭州天气",
            "type": "click",
            "url": "https:\/\/www.taobao.com"
          }
        ],
        "type": "view",
        "url": "https:\/\/www.taobao.com"
      }
    ],
    "enable_input": false,
    "status": 0
  }
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
