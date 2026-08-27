---
title: "学习推荐数据回流"
source_url: "https://open.dingtalk.com/document/development/learn-to-recommend-data-backflow"
namespace: "development"
slug: "learn-to-recommend-data-backflow"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家庭 > 学习推荐数据回流"
doc_id: "Bcs2VKxort"
updated_at: "2026-06-08 09:47:58"
---

> Source: https://open.dingtalk.com/document/development/learn-to-recommend-data-backflow
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家庭 > 学习推荐数据回流
> Updated: 2026-06-08 09:47:58

# 学习推荐数据回流

调用本接口，家长首页学习推荐数据回流。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/recommend/return |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-edu\_study\_log\_write-钉钉教育学习数据写权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| summary | String | 否 | 考试学习 | 摘要。 |
| result\_value | String | 是 | 98 | 结果分值。 |
| thumbnail | String | 是 | http://www.aaa.jpg | 媒体缩略图链接。 |
| type | String | 是 | 4 | 类型。   - **1**：词汇 - **2**：课文 - **3**：题目 - **4**：考试 - **5**：知识点 - **6**：课程 - **7**：其他 |
| title | String | 是 | 考试 | 内容标题。 |
| userid | String | 是 | user01 | 学习孩子的userId。 |
| class\_id | Number | 否 | 677995086 | 班级ID，调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| return\_url | String | 是 | http://ao.cxxxx.com | 回跳地址。 |
| subject\_code | String | 否 | cn\_p\_shuxue | 学段编码，可通过[获取学段元数据列表](1128-dingtalk-the-main-data-of-the-education-ecosystem-to-query.md)接口获取period\_code参数值。 |
| result\_type | Number | 是 | 4 | 结果分值类型。   - **1**：对错 - **2**：百分打分 - **3**：百分比打分 - **4**：数值 |
| textbook\_code | String | 否 | FBnCv218004 | 教材版本。 |
| out\_content\_id | String | 是 | uk\_1 | ISV侧内容唯一ID。  **[!NOTE]**  由ISV回传得到。 |
| out\_tx\_id | String | 是 | uk\_2 | 外部提交唯一ID。  **[!NOTE]**  由ISV回传得到。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/recommend/return" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=e3a30605-7c49-405b-8751-ecb8a33ca84a' \
-d 'class_id=1234' \
-d 'out_content_id=1234' \
-d 'out_tx_id=123' \
-d 'result_type=1' \
-d 'result_value=1' \
-d 'return_url=%2Fpages%2Findex%2Findex' \
-d 'subject_code=xxx' \
-d 'summary=%E6%91%98%E8%A6%81' \
-d 'textbook_code=xxx' \
-d 'thumbnail=%E7%BC%A9%E7%95%A5%E5%9B%BE' \
-d 'title=%E6%A0%87%E9%A2%98' \
-d 'type=1' \
-d 'userid=1234'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/recommend/return");
OapiEduRecommendReturnRequest req = new OapiEduRecommendReturnRequest();
req.setSummary("考试学习");
req.setResultValue("98");
req.setThumbnail("http://www.aaa.jpg");
req.setType("4");
req.setTitle("考试");
req.setUserid("user01");
req.setClassId(677995086L);
req.setReturnUrl("http://ao.cxxxx.com");
req.setSubjectCode("cn_p_shuxue");
req.setResultType(4L);
req.setTextbookCode("FBnCv218004");
req.setOutContentId("uk_1");
req.setOutTxId("uk_2");
OapiEduRecommendReturnResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduRecommendReturnRequest("https://oapi.dingtalk.com/topapi/edu/recommend/return")

req.summary="摘要"
req.result_value="1"
req.thumbnail="缩略图"
req.type="1"
req.title="标题"
req.userid="1234"
req.class_id=1234
req.return_url="/pages/index/index"
req.subject_code="xxx"
req.result_type=1
req.textbook_code="xxx"
req.out_content_id="1234"
req.out_tx_id="123"
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
$req = new OapiEduRecommendReturnRequest;
$req->setSummary("摘要");
$req->setResultValue("1");
$req->setThumbnail("缩略图");
$req->setType("1");
$req->setTitle("标题");
$req->setUserid("1234");
$req->setClassId("1234");
$req->setReturnUrl("/pages/index/index");
$req->setSubjectCode("xxx");
$req->setResultType("1");
$req->setTextbookCode("xxx");
$req->setOutContentId("1234");
$req->setOutTxId("123");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/recommend/return");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/recommend/return");
OapiEduRecommendReturnRequest req = new OapiEduRecommendReturnRequest();
req.Summary = "摘要";
req.ResultValue = "1";
req.Thumbnail = "缩略图";
req.Type = "1";
req.Title = "标题";
req.Userid = "1234";
req.ClassId = 1234L;
req.ReturnUrl = "/pages/index/index";
req.SubjectCode = "xxx";
req.ResultType = 1L;
req.TextbookCode = "xxx";
req.OutContentId = "1234";
req.OutTxId = "123";
OapiEduRecommendReturnResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |
| request\_id | String | 6bzhf2vn89pv | 请求ID。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "success":"true",
  "request_id": "6bzhf2vn89pv"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
