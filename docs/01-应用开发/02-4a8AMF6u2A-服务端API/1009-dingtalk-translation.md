---
title: "钉钉文本翻译"
source_url: "https://open.dingtalk.com/document/development/dingtalk-translation"
namespace: "development"
slug: "dingtalk-translation"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 生态开放 > AI > 钉钉文本翻译"
doc_id: "Fb5tOepwNo"
updated_at: "2026-06-03 09:50:59"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-translation
> Path: 应用开发 / 服务端API / 行业与生态 > 生态开放 > AI > 钉钉文本翻译
> Updated: 2026-06-03 09:50:59

# 钉钉文本翻译

通过此接口，可将一段文本内容翻译为目标语言。支持多种语言互译，适用于多语言场景下的内容处理。输入源文本及源语言、目标语言参数，即可获得对应的翻译结果。

## **接口调用说明**

该翻译接口适用于以下典型业务场景：

- **多语言消息自动翻译**：在跨国团队沟通中，自动将员工发送的中文消息翻译为英文或其他语言，提升协作效率。
- **国际化应用内容处理**：企业开发面向海外用户的应用时，可使用本接口动态翻译界面文案、通知内容等。
- **日志与报表本地化展示**：将系统生成的日志或报表内容实时翻译成用户所在地区的语言，增强可读性。
- **跨语言知识库同步**：实现中英文文档之间的批量翻译，便于维护多语言知识库。

支持的语言对详见下方“支持的语言转换”表格，方向可逆，满足双向翻译需求。建议在用户触发查看异语种内容时调用本接口进行实时翻译

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/ai/mt/translate |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用appType-第三方企业应用 |
| 权限要求 | permission-`qyapi_ai_base`-钉钉AI平台基础权限包 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该API的应用凭证。   - 企业内部应用，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 - 第三方企业应用，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| query | String | 是 | 这是一个测试 | 翻译源文字符串。 |
| source\_language | String | 是 | zh | 翻译源语言类型。 |
| target\_language | String | 是 | en | 翻译目标语言类型。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/ai/mt/translate" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=76bd22xxxx8728a' \
-d 'query=%E8%BF%99%E6%98%AF%E4%B8%80%E4%B8%AA%E6%B5%8B%E8%AF%95' \
-d 'source_language=zh' \
-d 'target_language=en'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/ai/mt/translate");
OapiAiMtTranslateRequest req = new OapiAiMtTranslateRequest();
req.setQuery("这是一个测试");
req.setSourceLanguage("zh");
req.setTargetLanguage("en");
OapiAiMtTranslateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiAiMtTranslateRequest("https://oapi.dingtalk.com/topapi/ai/mt/translate")

req.query="这是一个测试"
req.source_language="zh"
req.target_language="en"
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
$req = new OapiAiMtTranslateRequest;
$req->setQuery("这是一个测试");
$req->setSourceLanguage("zh");
$req->setTargetLanguage("en");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/ai/mt/translate");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/ai/mt/translate");
OapiAiMtTranslateRequest req = new OapiAiMtTranslateRequest();
req.Query = "这是一个测试";
req.SourceLanguage = "zh";
req.TargetLanguage = "en";
OapiAiMtTranslateResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | String | This is a test | 翻译结果字符串。 |
| errcode | Number | 0 | 返回码。 |
| request\_id | String | e95jy33txuww | 请求ID。 |

### **响应体示例**

```
{
    "errcode": 0,
    "result": "This is a test",
    "request_id": "e95jy33txuww"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。

## **支持的语言转换 (方向可逆)**

语言类型缩写可参考标准ISO-639-1。

| source\_language/target\_language | target\_language/source\_language |
| --- | --- |
| zh | id |
| en | ru |
| zh | en |
| en | es |
| en | fr |
| en | th |
| en | vi |
| id | en |
| ar | en |
| tr | en |
| ja | zh |
| zh | vi |
| zh | th |
| zh | ko |
| it | zh |
| en | ja |
| zh | ru |
| zh | fr |
| zh | de |
| zh | es |
