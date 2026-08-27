---
title: "家庭Feed同步"
source_url: "https://open.dingtalk.com/document/development/dingtalk-education-family-feed-synchronization"
namespace: "development"
slug: "dingtalk-education-family-feed-synchronization"
group: "应用开发"
tab: "服务端API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 家庭 > 家庭Feed同步"
doc_id: "MM9x4uqPpX"
updated_at: "2026-06-08 09:47:56"
---

> Source: https://open.dingtalk.com/document/development/dingtalk-education-family-feed-synchronization
> Path: 应用开发 / 服务端API / 行业与生态 > 行业开放 > 新教育 > 家庭 > 家庭Feed同步
> Updated: 2026-06-08 09:47:56

# 家庭Feed同步

调用本接口，同步钉钉教育家庭Feed，包括媒体类型、媒体链接、设置同步类型等。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/feed/sync |
| HTTP Method | POST |
| 支持的应用类型 | appType-第三方企业应用 |
| 权限要求 | permission-qyapi\_edu\_feed-钉钉教育Feed数据管理权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | Be3xxxx | 调用该接口的应用凭证，通过[获取第三方企业的access\_token](1448-obtain-isvapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| feed\_medias | IndustrySyncFeedMediaReq[] | 是 |  | 媒体list，最多可传入999。 |
| media\_type | Number | 否 | 1 | 媒体类型。   - **1**：图片 - **2**：视频 - **3**：文本 - **4**：直播 |
| media\_url | String | 是 | http://www.aaa.jpg | 媒体链接。 |
| thumbnail\_url | String | 否 | http://www.aaa.jpg | 媒体缩略图链接。 |
| media\_uid | String | 否 | 390898402 | 媒体用户的userId。 |
| fee\_type | Number | 是 | 1 | 同步类型。   - **1**：全量同步 - **2**：单个同步 |
| dept\_id | Number | 否 | 12398 | 部门或班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_id参数值。 |
| album\_id | String | 否 | al1342 | 媒体相册ID。 |
| send\_uid | String | 否 | 23428409328 | 媒体发送用户的userId。 |
| op\_userId | String | 否 | 2384082340 | 操作人的userId。 |
| send\_time | Number | 否 | 1605858971991 | 发送时间戳，单位毫秒。 |
| future | String | 否 | kindergarten | 拓展字段。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/feed/sync" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=ff67856e-515f-4e14-9e8e-9a95ae20cb5c' \
-d 'album_id=al1342' \
-d 'dept_id=12398' \
-d 'fee_type=1' \
-d 'feed_medias=null' \
-d 'future=%E6%8B%93%E5%B1%95%E5%AD%97%E6%AE%B5' \
-d 'media_uid=390898402' \
-d 'op_userId=2384082340' \
-d 'send_time=1605858971991' \
-d 'send_uid=23428409328'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/feed/sync");
OapiEduFeedSyncRequest req = new OapiEduFeedSyncRequest();
List<IndustrySyncFeedMediaReq> list2 = new ArrayList<IndustrySyncFeedMediaReq>();
IndustrySyncFeedMediaReq obj3 = new IndustrySyncFeedMediaReq();
list2.add(obj3);
obj3.setMediaType(1L);
obj3.setMediaUrl("http://www.aaa.jpg");
obj3.setThumbnailUrl("http://www.aaa.jpg");
req.setFeedMedias(list2);
req.setMediaUid("390898402");
req.setFeeType(1L);
req.setDeptId(12398L);
req.setAlbumId("al1342");
req.setSendUid("23428409328");
req.setOpUserId("2384082340");
req.setSendTime(1605858971991L);
OapiEduFeedSyncResponse rsp = client.execute(req, access_token);
System.out.println(rsp.getBody());
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduFeedSyncRequest("https://oapi.dingtalk.com/topapi/edu/feed/sync")

req.feed_medias=""
req.media_uid="390898402"
req.fee_type=1
req.dept_id=12398
req.album_id="al1342"
req.send_uid="23428409328"
req.op_userId="2384082340"
req.send_time=1605858971991
req.future="拓展字段"
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
$req = new OapiEduFeedSyncRequest;
$feed_medias = new IndustrySyncFeedMediaReq;
$feed_medias->media_type="1";
$feed_medias->media_url="http://www.aaa.jpg";
$feed_medias->thumbnail_url="http://www.aaa.jpg";
$req->setFeedMedias(array($feed_medias));
$req->setMediaUid("390898402");
$req->setFeeType("1");
$req->setDeptId("12398");
$req->setAlbumId("al1342");
$req->setSendUid("23428409328");
$req->setOpUserId("2384082340");
$req->setSendTime("1605858971991");
$req->setFuture("拓展字段");
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/feed/sync");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/feed/sync");
OapiEduFeedSyncRequest req = new OapiEduFeedSyncRequest();
List<OapiEduFeedSyncRequest.IndustrySyncFeedMediaReqDomain> list2 = new List<OapiEduFeedSyncRequest.IndustrySyncFeedMediaReqDomain>();
OapiEduFeedSyncRequest.IndustrySyncFeedMediaReqDomain obj3 = new OapiEduFeedSyncRequest.IndustrySyncFeedMediaReqDomain();
list2.Add(obj3);
obj3.MediaType = 1L;
obj3.MediaUrl = "http://www.aaa.jpg";
obj3.ThumbnailUrl = "http://www.aaa.jpg";
req.FeedMedias_ = list2;
req.MediaUid = "390898402";
req.FeeType = 1L;
req.DeptId = 12398L;
req.AlbumId = "al1342";
req.SendUid = "23428409328";
req.OpUserId = "2384082340";
req.SendTime = 1605858971991L;
req.Future = "拓展字段";
OapiEduFeedSyncResponse rsp = client.Execute(req, access_token);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| success | Boolean | true | 请求是否成功。   - **true**：成功 - **false**：失败 |
| errcode | Number | 0 | 返回码。 |
| errmsg | String | ok | 返回码描述。 |

### **响应体示例**

```
{
  "errcode":0,
  "success":"true",
  "errmsg":"ok"
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
