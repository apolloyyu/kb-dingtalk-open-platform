---
title: "机票城市搜索"
source_url: "https://open.dingtalk.com/document/development/air-ticket-city-search"
namespace: "development"
slug: "air-ticket-city-search"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 城市基本数据 > 机票城市搜索"
doc_id: "TplvsnvuyK"
updated_at: "2026-06-08 09:47:02"
---

> Source: https://open.dingtalk.com/document/development/air-ticket-city-search
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 城市基本数据 > 机票城市搜索
> Updated: 2026-06-08 09:47:02

# 机票城市搜索

调用本接口可实现机票城市的模糊匹配与智能推荐，适用于用户在预订机票时输入城市名称进行搜索的场景。支持根据搜索关键词返回国内或国际航班相关城市，并可根据配置返回邻近机场信息，提升用户选城效率。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | SuggestRq | 是 |  | 请求对象，封装城市搜索所需的参数。 |
| keyword | String | 是 | 北京 | 搜索关键字，表示用户输入的城市名称或拼音，用于模糊匹配。 |
| userid | String | 是 | user1 | 用户的userid，标识发起请求的用户身份。 |
| type | Number | 否 | 0 | 机场城市类型，控制返回结果范围：   - **0**：国内机场 - **2**：国内机场+临近机场 - **3**：国际机场 |
| corpid | String | 是 | corp1 | 企业ID，用于标识所属企业，确保权限与数据隔离。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=0770d3xxxx100cda50' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest");
OapiAlitripBtripFlightCitySuggestRequest req = new OapiAlitripBtripFlightCitySuggestRequest();
SuggestRq obj1 = new SuggestRq();
obj1.setKeyword("北京");
obj1.setUserid("user1");
obj1.setType(0L);
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripFlightCitySuggestResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripFlightCitySuggestRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest")

req.rq=""
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
$req = new OapiAlitripBtripFlightCitySuggestRequest;
$rq = new SuggestRq;
$rq->keyword="北京";
$rq->userid="user1";
$rq->type="0";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/flight/city/suggest");
OapiAlitripBtripFlightCitySuggestRequest req = new OapiAlitripBtripFlightCitySuggestRequest();
OapiAlitripBtripFlightCitySuggestRequest.SuggestRqDomain obj1 = new OapiAlitripBtripFlightCitySuggestRequest.SuggestRqDomain();
obj1.Keyword = "北京";
obj1.Userid = "user1";
obj1.Type = 0L;
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripFlightCitySuggestResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | SuggestRs | module | 接口返回的结果对象，包含城市列表及推荐信息。 |
| cities | CityVo[] | cities | 城市列表。 |
| code | String | HGH | 三字码。 |
| name | String | 杭州 | 城市名称。 |
| distance | Number | 100 | 与搜索城市距离，单位千米，只在邻近机场推荐有值。 |
| travel\_name | String | 上海 | 邻近机场城市，只在邻近机场推荐有值。 |
| nearby | Boolean | false | 是否为邻近城市。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 成功标识。 |

### **响应体示例**

```
{
  "result":{
    "cities":{
      "code":"HGH",
      "distance":"100",
      "name":"杭州",
      "travel_name":"上海"
    },
    "nearby":"false"
  },
  "errcode":"0",
  "success":"true",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
