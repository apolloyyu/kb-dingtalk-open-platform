---
title: "获取班级圈动态列表"
source_url: "https://open.dingtalk.com/document/development/dynamic-list-opening-of-class-circle"
namespace: "development"
slug: "dynamic-list-opening-of-class-circle"
group: "应用开发"
tab: "服务端 API"
breadcrumb: "行业与生态 > 行业开放 > 新教育 > 班级圈 > 获取班级圈动态列表"
doc_id: "aTJpH5KUe3"
updated_at: "2026-06-08 09:48:23"
---

> Source: https://open.dingtalk.com/document/development/dynamic-list-opening-of-class-circle
> Path: 应用开发 / 服务端 API / 行业与生态 > 行业开放 > 新教育 > 班级圈 > 获取班级圈动态列表
> Updated: 2026-06-08 09:48:23

# 获取班级圈动态列表

调用本接口，获取班级圈动态列表。

## **请求**

| **基本信息** | |
| --- | --- |
| HTTP URL | https://oapi.dingtalk.com/topapi/edu/circle/post/list |
| HTTP Method | POST |
| 支持的应用类型 | appType-企业内部应用 |
| 权限要求 | permission-qyapi\_edu\_task-钉钉教育班级圈数据读权限 |

### **查询参数**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| access\_token | String | 是 | 6d1bxxxx | 调用该接口的应用凭证，通过[获取企业内部应用的access\_token](1446-obtain-orgapp-token.md)接口获取。 |

### **请求体**

| 名称 | 类型 | 是否必填 | 示例值 | 描述 |
| --- | --- | --- | --- | --- |
| open\_feed\_query\_param | OpenFeedQueryParam | 否 |  | 请求结构。 |
| cursor | Number | 否 | 1620704981000 | 分页游标，第一页传入系统时间，毫秒。  **[!NOTE]**  返回的数据的时间戳不超过该数值 |
| student\_id | String | 否 | stu123 | 学生的userId，可调用[获取人员列表](1157-obtains-a-list-of-home-school-user-identities.md)接口获取userid参数值。 |
| class\_id | Number | 否 | 26347 | 班级ID，可调用[获取部门列表](1156-obtains-the-department-node-list.md)接口获取dept\_id参数值。 |
| topic\_id | Number | 否 | 19827347 | 话题ID，可调用[获取班级圈话题列表](1194-obtain-a-topic-list-of-class-circles.md)接口获取topic\_id参数值。 |
| biz\_type | Number | 否 | 4 | 业务类型，固定值为**4**，表示班级圈。 |
| feed\_type | Number | 否 | 0 | 动态类型，固定值**0**。 |
| count | Number | 否 | 10 | 分页大小，最大值20。 |
| user\_role | String | 否 | 老师 | 角色，可不传。 |
| userid | String | 否 | t\_63312 | 当前人登录人userId，如果没有人登录。可以传入班级的老师userId。 |

### **请求示例**

curl

```
curl -X POST "https://oapi.dingtalk.com/topapi/edu/circle/post/list" \
-H 'Content-Type:application/x-www-form-urlencoded;charset=utf-8' \
-d 'access_token=76c22564-cc79-4152-b5e8-4952231d249b' \
-d 'open_feed_query_param=null'
```

Java

```
DingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/circle/post/list");
OapiEduCirclePostListRequest req = new OapiEduCirclePostListRequest();
OpenFeedQueryParam openFeedQueryParam = new OpenFeedQueryParam();
openFeedQueryParam.setCursor(1620704981000L);
openFeedQueryParam.setCount(10L);
openFeedQueryParam.setStudentId("stu123");
openFeedQueryParam.setClassId(26347L);
openFeedQueryParam.setTopicId(19827347L);
openFeedQueryParam.setBizType(4L);
openFeedQueryParam.setFeedType(0L);
openFeedQueryParam.setUserid("tch123");
openFeedQueryParam.setUserRole("老师");
req.setOpenFeedQueryParam(openFeedQueryParam);
OapiEduCirclePostListResponse rsp = client.execute(req, access_token);
```

Python

```
import dingtalk.api

req=dingtalk.api.OapiEduCirclePostListRequest("https://oapi.dingtalk.com/topapi/edu/circle/post/list")

req.open_feed_query_param="数据结构示例JSON格式"
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
$req = new OapiEduCirclePostListRequest;
$open_feed_query_param = new OpenFeedQueryParam;
$open_feed_query_param->cursor="1";
$open_feed_query_param->student_id="1";
$open_feed_query_param->class_id="11";
$open_feed_query_param->topic_id="1";
$open_feed_query_param->biz_type="1";
$open_feed_query_param->feed_type="1";
$open_feed_query_param->count="1";
$open_feed_query_param->user_role="1";
$open_feed_query_param->userid="1";
$req->setOpenFeedQueryParam($open_feed_query_param);
$resp = $c->execute($req, $access_token, "https://oapi.dingtalk.com/topapi/edu/circle/post/list");
```

C#

```
IDingTalkClient client = new DefaultDingTalkClient("https://oapi.dingtalk.com/topapi/edu/circle/post/list");
OapiEduCirclePostListRequest req = new OapiEduCirclePostListRequest();
OpenFeedQueryParam openFeedQueryParam = new OpenFeedQueryParam();
openFeedQueryParam.Cursor = 1620704981000L;
openFeedQueryParam.Count = 10L;
openFeedQueryParam.StudentId = "stu123";
openFeedQueryParam.ClassId = 26347L;
openFeedQueryParam.TopicId = 19827347L;
openFeedQueryParam.BizType = 4L;
openFeedQueryParam.FeedType = 0L;
openFeedQueryParam.Userid = "tch123";
openFeedQueryParam.UserRole = "老师";
req.OpenFeedQueryParam = openFeedQueryParam;
OapiEduCirclePostListResponse rsp = client.Execute(req, accessToken);
Console.WriteLine(rsp.Body);
```

## **响应**

### **响应体**

| 名称 | 类型 | 示例值 | 描述 |
| --- | --- | --- | --- |
| result | OpenCircleTopicResponse |  | 返回结果。 |
| has\_more | Boolean | false | 是否还有更多数据。   - **true**：有 - **false**：没有 |
| posts | Posts[] |  | 动态列表。 |
| comments | Comments[] |  | 动态对应的评论。 |
| comment\_id | Number | 865785 | 评论ID。 |
| content | String | 钉钉是一种工作方式 | 评论内容。 |
| origin\_user | OrgUserDto |  | 评论发送者。 |
| show\_name | String | 小钉 | 评论人名称。 |
| staff\_id | String | user456 | 员工userId。 |
| author | Author |  | 动态作者。 |
| owner | Boolean | true | 是否是当前人。   - **true**：是 - **false**：不是 |
| show\_name | String | 钉三多 | 页面展示的作者昵称。 |
| icon\_media\_id | String | #bjhk5432y4sfdoiuxxxx | 作者头像。 |
| title | String | 经理 | 员工在公司的职位信息。 |
| type | String | 1 | 用户类型。 |
| avatar\_media\_id | String | #bjh423nvkbGHxxxx | 作者头像. |
| nick | String | 钉三多 | 作者昵称。 |
| is\_owner | Boolean | true | 是否是当前人。   - **true**：是 - **false**：不是 |
| tag | Number | 661 | 员工标签。 |
| user\_role | String | 子管理员 | 用户角色。 |
| staff\_id | String | user345 | 作者userId。 |
| feed\_type | Number | 0 | 动态类型，0表示动态。 |
| biz\_id | String | 4 | 业务ID。 |
| post\_id | Number | 52340896 | 动态ID。 |
| create\_at | Number | 1620704981000 | 创建时间。 |
| content | Content |  | 动态内容。  **[!NOTE]**  需要自行解析里面的内容。 |
| geo\_content | String | 绿城未来park | 地址位置信息。 |
| text | String | 测试 | 动态文字内容。 |
| content\_type | Number | 1 | 内容类型。取值如下。   - 1：文本 - **2**：图片 - **3**：视频 - **4**：链接 - **5**：地理位置 - **6**：附件 - **7**：转发 - **8**：富文本 - **9**：钉盘文件 |
| tags | String | 班级测试 | 动态标签。 |
| status | Number | 0 | 状态，0表示正常。 |
| success | Boolean | true | 是否成功。   - **true**：成功 - **false**：失败 |
| errmsg | String | ok | 返回码描述。 |
| errcode | Number | 0 | 返回码。 |

### **响应体示例**

```
{
  "errcode": 0,
  "errmsg": "ok",
  "result": {
    "has_more": false,
    "posts": [
      {
        "author": {
          "avatar_media_id": "#bjh423nvkbGHxxxx",
          "icon_media_id": "#bjhk5432y4sfdoiuxxxx",
          "is_owner": true,
          "nick": "钉三多",
          "owner": true,
          "show_name": "钉三多",
          "staff_id": "user456",
          "tag": "661",
          "title": "经理",
          "type": "1",
          "user_role": "子管理员"
        },
        "biz_id": "4",
        "create_at": 1620704981000,
        "feed_type": 0,
        "post_id": 52340896,
        "status": 0,
        "tags": "",
        "comments": [
          {
            "comment_id": 865785,
            "content": "钉钉是一种工作方式",
            "origin_user": {
              "show_name": "小钉",
              "staff_id": "user456"
            }
          }
        ],
        "content": {
          "content_type": 1,
          "geo_content": "绿城未来park",
          "text": "测试"
        }
      }
    ]
  },
  "success": true
}
```

### **错误码**

若调用该接口报错，可根据错误信息在[全局错误码](0013-server-api-error-codes-1.md)文档中查找解决方案。
