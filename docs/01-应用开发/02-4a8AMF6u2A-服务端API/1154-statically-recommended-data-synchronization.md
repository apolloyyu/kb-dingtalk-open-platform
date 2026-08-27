---
title: "静态推荐数据同步"
source_url: "https://open.dingtalk.com/document/development/statically-recommended-data-synchronization"
namespace: "development"
slug: "statically-recommended-data-synchronization"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家庭 > 静态推荐数据同步"
doc_id: "ciNsLY8Ipt"
updated_at: "2026-06-08 09:48:00"
---

> Source: https://open.dingtalk.com/document/development/statically-recommended-data-synchronization
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家庭 > 静态推荐数据同步
> Updated: 2026-06-08 09:48:00

# 静态推荐数据同步

调用本接口，同步静态推荐数据。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/recommend/create |
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
| thumbnail | String | 是 | http://www.aaa.jpg | 缩略图url地址。 |
| type | String | 是 | 4 | 类型。   - **1**：词汇 - **2**：课文 - **3**：题目 - **4**：考试 - **5**：知识点 - **6**：课程 - **7**：其他 |
| title | String | 是 | 考试 | 内容标题。 |
| userid | String | 是 | user01 | 当前用户的userId。 |
| period\_code | String | 是 | primary\_school | 学段编码，可通过[获取学段元数据列表](1128-dingtalk-the-main-data-of-the-education-ecosystem-to-query.md)接口获取period\_code参数值。 |
| class\_id | Number | 否 | 677995086 | 班级ID，调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_type为class时的dept\_id参数值。 |
| return\_url | String | 是 | http://ao.cxxxx.com | 回跳地址。 |
| subject\_code | String | 否 | cn\_p\_shuxue | 学科编码，可通过[获取学科元数据列表](1134-dingtalk-the-main-data-of-the-education-ecosystem-query-the-subject.md)获取subject\_code参数值。 |
| textbook\_code | String | 否 | FBnCv218004 | 教材版本。 |
| out\_content\_id | String | 是 | uk\_1 | ISV侧内容唯一ID。  **[!NOTE]**  由ISV回传得到。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/recommend/create" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=69fc5582-0c0d-428d-b0eb-a51dd177a858' \
-d 'class_id=123' \
-d 'out_content_id=123' \
-d 'period_code=xxxx' \
-d 'return_url=%2Fpages%2Findex%2Findex' \
-d 'subject_code=xxx' \
-d 'summary=%E6%96%87%E7%AB%A0%E6%91%98%E8%A6%81' \
-d 'textbook_code=xxx' \
-d 'thumbnail=http%3A%2F%2Fxxxx' \
-d 'title=%E8%AF%BE%E6%96%87%E5%AD%A6%E4%B9%A0%E9%B2%81%E8%BF%85%E6%96%87%E7%AB%A0%E9%97%B0%E5%9C%9F' \
-d 'type=1' \
-d 'userid=12344'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/recommend/create");
OapiEduRecommendCreateRequest req = new OapiEduRecommendCreateRequest();
req.setSummary("考试学习");
req.setThumbnail("RSDFS");
req.setType("4");
req.setTitle("考试");
req.setUserid("user01");
req.setPeriodCode("primary_school");
req.setClassId(677995086L);
req.setReturnUrl("http://ao.cxxxx.com");
req.setSubjectCode("cn_p_shuxue");
req.setTextbookCode("FBnCv218004");
req.setOutContentId("uk_1");
OapiEduRecommendCreateResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduRecommendCreateRequest("https://oapi.dingtalk.com/topapi/edu/recommend/create")

req.summary="文章摘要"
req.thumbnail="http://xxxx"
req.type="1"
req.title="课文学习鲁迅文章闰土"
req.userid="12344"
req.period_code="xxxx"
req.class_id=123
req.return_url="/pages/index/index"
req.subject_code="xxx"
req.textbook_code="xxx"
req.out_content_id="123"
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
$req = new OapiEduRecommendCreateRequest;
$req->setSummary("文章摘要");
$req->setThumbnail("http://xxxx");
$req->setType("1");
$req->setTitle("课文学习鲁迅文章闰土");
$req->setUserid("12344");
$req->setPeriodCode("xxxx");
$req->setClassId("123");
$req->setReturnUrl("/pages/index/index");
$req->setSubjectCode("xxx");
$req->setTextbookCode("xxx");
$req->setOutContentId("123");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/recommend/create");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/recommend/create");
OapiEduRecommendCreateRequest req = new OapiEduRecommendCreateRequest();
req.Summary = "文章摘要";
req.Thumbnail = "http://xxxx";
req.Type = "1";
req.Title = "课文学习鲁迅文章闰土";
req.Userid = "12344";
req.PeriodCode = "xxxx";
req.ClassId = 123L;
req.ReturnUrl = "/pages/index/index";
req.SubjectCode = "xxx";
req.TextbookCode = "xxx";
req.OutContentId = "123";
OapiEduRecommendCreateResponse rsp = client.Execute(req, access_token);
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
