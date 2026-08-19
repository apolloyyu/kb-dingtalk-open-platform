---
title: "火车票城市搜索"
source_url: "https://open.dingtalk.com/document/development/train-ticket-city-search"
namespace: "development"
slug: "train-ticket-city-search"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > 阿里商旅 > 城市基本数据 > 火车票城市搜索"
doc_id: "CGaQhr0EYP"
updated_at: "2026-06-08 09:47:03"
---

> Source: https://open.dingtalk.com/document/development/train-ticket-city-search
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > 阿里商旅 > 城市基本数据 > 火车票城市搜索
> Updated: 2026-06-08 09:47:03

# 火车票城市搜索

调用本接口可实现火车票城市的搜索功能，支持根据用户输入的关键词进行城市名称和城市码的模糊匹配，适用于企业差旅场景中的火车票预订流程。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_ali\_business\_trip-阿里商旅专用权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | bE74xxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1444-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1446-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| rq | SuggestRq | 是 |  | 请求对象。 |
| keyword | String | 是 | 杭州 | 搜索关键字，用于匹配城市名称或城市码。 |
| userid | String | 是 | user1 | 当前操作用户的ID，用于上下文识别与权限校验。 |
| corpid | String | 是 | corp1 | 企业标识ID，用于确定所属企业数据范围。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=7bbfdc5exxxxc8430d784' \
-d 'rq=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest");
OapiAlitripBtripTrainCitySuggestRequest req = new OapiAlitripBtripTrainCitySuggestRequest();
SuggestRq obj1 = new SuggestRq();
obj1.setKeyword("杭州");
obj1.setUserid("user1");
obj1.setCorpid("corp1");
req.setRq(obj1);
OapiAlitripBtripTrainCitySuggestResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAlitripBtripTrainCitySuggestRequest("https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest")

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
$req = new OapiAlitripBtripTrainCitySuggestRequest;
$rq = new SuggestRq;
$rq->keyword="杭州";
$rq->userid="user1";
$rq->corpid="corp1";
$req->setRq($rq);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/alitrip/btrip/train/city/suggest");
OapiAlitripBtripTrainCitySuggestRequest req = new OapiAlitripBtripTrainCitySuggestRequest();
OapiAlitripBtripTrainCitySuggestRequest.SuggestRqDomain obj1 = new OapiAlitripBtripTrainCitySuggestRequest.SuggestRqDomain();
obj1.Keyword = "杭州";
obj1.Userid = "user1";
obj1.Corpid = "corp1";
req.Rq_ = obj1;
OapiAlitripBtripTrainCitySuggestResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | SuggestRs |  | 结果对象。 |
| cities | CityVo[] |  | 城市列表。 |
| name | String | 杭州 | 城市名称。 |
| code | String | HGH | 城市码。 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |
| success | Boolean | true | 成功标识。 |

### **响应体示例**

```
{
  "result":{
    "cities":{
      "code":"hk",
      "name":"汉口"
    }
  },
  "errcode":"0",
  "success":"true",
  "errmsg":"成功"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
